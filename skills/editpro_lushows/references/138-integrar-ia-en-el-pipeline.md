# 138 — Integrar IA en el pipeline

## Qué resuelve

Meter modelos de IA dentro de una tubería automatizada **sin perder el determinismo, sin quemar el
presupuesto y sin que un error 429 a las once de la noche tumbe el proyecto**.

La IA en un pipeline de edición no es un adorno: en el caso maestro cuatro de los doce pasos la usan
(`transcribir`, `cortes`, `generar-ilustracion`, `generar-musica`). Pero se comporta distinto a ffmpeg:
cuesta dinero, falla por razones ajenas a ti, tarda lo que quiere y **no da lo mismo dos veces**.

De ahí sale la regla que ordena todo el módulo:

> **La IA produce insumos, no resultados. Su salida se congela como archivo, y el pipeline consume el
> archivo, no el modelo.**

---

## Dónde va la IA y dónde no

| Paso | ¿IA? | Qué hace exactamente |
|---|---|---|
| `analizar` | no | ffprobe. Es medición, no interpretación |
| `transcribir` | **sí** | audio a texto con timecodes, marcando tomas falsas y risas |
| `cortes` | **sí, asistida** | propone entrada/salida; el humano aprueba (módulo `137`) |
| `validar-cortes` | no | reglas duras. Una compuerta con criterio variable no es compuerta |
| `subtitulos` | no | pura mecánica sobre los timecodes que ya existen |
| `limpiar-voz` | no | cadena de filtros determinista |
| `generar-ilustracion` | **sí** | arte de marca, con los archivos de marca como referencia |
| `forzar-marca` | no | duotono matemático (módulo `64`) |
| `generar-musica` | **sí** | música original del largo exacto |
| `montar` | **jamás** | si el render llama a un modelo, deja de ser reproducible |
| `musicalizar` | no | mezcla y ducking, medibles |
| `verificar` | **sí, opcional** | retranscribir el resultado y comparar (módulo `133`) |

La fila que más importa es `montar`. **Ninguna llamada a IA dentro del render.** El día que la metas, el
mismo CSV deja de producir el mismo video y todo el módulo `132` se cae.

---

## Congelar la salida: el patrón fundamental

Toda salida de IA se escribe a disco con tres archivos hermanos:

```
assets/generado-ia/
  frasco-duotono.png              el resultado
  frasco-duotono.prompt.txt       el prompt exacto que lo produjo
  frasco-duotono.meta.json        modelo, fecha, costo, parametros, referencias
```

```json
{
  "modelo": "imagen-generativa-v4",
  "fecha": "2026-08-04T22:14:03Z",
  "costo_usd": 0.04,
  "parametros": { "aspecto": "9:16", "calidad": "alta" },
  "referencias": ["assets/marca/paleta.png", "assets/marca/logo.png"],
  "intentos": 3,
  "nota": "el intento 1 y 2 salieron con verde que no es de la paleta; se forzo duotono despues"
}
```

Por qué los tres, y no solo la imagen:

- El **prompt** es lo único que te acerca a reproducirla si pierdes el archivo.
- El **meta** te dice cuánto costó (para el presupuesto) y con qué modelo (para el día que lo apaguen).
- La **nota** guarda lo que ya falló, que es el comentario más valioso (módulo `136`).

---

## Reintentos: el mínimo que no te deja tirado

Las APIs fallan por cosas que no controlas. Un pipeline sin reintentos se cae en el elemento 30 de 50 por
un error temporal de red.

**Espera exponencial con jitter**: cada reintento espera el doble que el anterior, más un ruido aleatorio.
El ruido evita que cinco procesos paralelos reintenten todos en el mismo instante y vuelvan a chocar.

```js
// llamar-ia.mjs -- envoltura unica para toda llamada a un modelo.
// Todas las llamadas del pipeline pasan por aqui. Si cada paso implementa sus
// propios reintentos, terminas con cuatro politicas distintas y ninguna probada.

const ESPERA_BASE_MS = 1500;
const MAX_INTENTOS = 5;

// Errores que SI vale la pena reintentar: son temporales.
// 400 y 401 no se reintentan nunca: reintentar un prompt invalido cinco veces
// solo gasta cinco veces mas tiempo y, en algunas APIs, cinco veces mas dinero.
const REINTENTABLES = new Set([408, 429, 500, 502, 503, 504]);

const dormir = (ms) => new Promise((r) => setTimeout(r, ms));

export async function llamarIA(fn, { etiqueta = "llamada", maxIntentos = MAX_INTENTOS } = {}) {
  let ultimo;
  for (let intento = 1; intento <= maxIntentos; intento++) {
    try {
      const t0 = Date.now();
      const r = await fn();
      console.log(`  ${etiqueta}: OK en el intento ${intento} (${((Date.now() - t0) / 1000).toFixed(1)} s)`);
      return r;
    } catch (e) {
      ultimo = e;
      const codigo = e.status ?? e.code ?? 0;

      if (!REINTENTABLES.has(codigo)) {
        // Fallar rapido y con el mensaje del servidor, que suele decir exactamente
        // que esta mal en el prompt o en las credenciales.
        throw new Error(`${etiqueta}: error ${codigo} no reintentable.\n  ${e.message}`);
      }
      if (intento === maxIntentos) break;

      // Si el servidor dice cuanto esperar, se le hace caso: es mas fiable que la formula.
      const sugerido = Number(e.headers?.["retry-after"]) * 1000;
      const espera = sugerido || ESPERA_BASE_MS * 2 ** (intento - 1) + Math.random() * 800;

      console.log(`  ${etiqueta}: error ${codigo}, reintento ${intento + 1}/${maxIntentos} en ${(espera / 1000).toFixed(1)} s`);
      await dormir(espera);
    }
  }
  throw new Error(
    `${etiqueta}: fallo tras ${maxIntentos} intentos.\n  Ultimo error: ${ultimo?.message}\n` +
    `  ARREGLO: revisa la cuota de la cuenta y el estado del servicio antes de volver a correr.`
  );
}
```

Esperas resultantes: 1,5 s → 3 s → 6 s → 12 s. Cinco intentos cubren casi cualquier bache temporal sin
dejar el proceso colgado media hora.

---

## Timeouts: nunca esperar para siempre

Una llamada que se cuelga sin timeout congela el lote entero. Toda llamada lleva su reloj:

```js
export async function conTimeout(promesa, ms, etiqueta) {
  let temporizador;
  const limite = new Promise((_, rechazar) => {
    temporizador = setTimeout(
      () => rechazar(new Error(`${etiqueta}: paso de ${ms / 1000} s sin responder. Se aborta.`)),
      ms
    );
  });
  try {
    return await Promise.race([promesa, limite]);
  } finally {
    clearTimeout(temporizador);
  }
}
```

Valores razonables a agosto de 2026:

| Tarea | Timeout | Por qué |
|---|---|---|
| Transcribir 2 min de audio | 120 s | suele tardar 10–30 s |
| Generar una imagen | 180 s | 15–60 s normalmente |
| Generar música de 60 s | 300 s | es lo más lento |
| Proponer cortes sobre una transcripción | 90 s | es texto, va rápido |

---

## Caché de llamadas: no pagar dos veces lo mismo

Igual que la caché de segmentos del módulo `132`, pero por prompt. Es lo que hace que volver a correr el
pipeline no cueste dinero.

```js
// cache-ia.mjs -- si ya pediste esto exactamente, no lo vuelvas a pedir.
// Correr el pipeline entero 5 veces mientras ajustas el montaje costaria 5 veces
// la transcripcion. Con esto cuesta una.

import { createHash } from "node:crypto";
import { existsSync, readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const DIR = join(process.env.PROYECTO || process.cwd(), "analisis", "cache-ia");

export async function conCache(clave, fn) {
  mkdirSync(DIR, { recursive: true });
  const h = createHash("sha1").update(JSON.stringify(clave)).digest("hex").slice(0, 16);
  const archivo = join(DIR, `${h}.json`);

  if (existsSync(archivo) && !process.env.FORZAR_IA) {
    console.log(`  cache: ${h}`);
    return JSON.parse(readFileSync(archivo, "utf8"));
  }
  const r = await fn();
  writeFileSync(archivo, JSON.stringify(r, null, 2), "utf8");
  console.log(`  guardado: ${h}`);
  return r;
}
```

La clave debe incluir **todo lo que cambia la respuesta**: el modelo, el prompt, los parámetros, y la
huella del archivo de entrada. Si te olvidas del modelo en la clave, cambias de modelo y la caché te
devuelve la respuesta del anterior.

---

## Validar lo que devuelve el modelo

Un modelo puede devolverte JSON con timecodes en minutos cuando pediste segundos, o un segmento que
termina antes de empezar. **Nunca metas la salida cruda de un modelo en la tabla.**

```js
// validar-segmentos.mjs -- la salida del modelo entra al pipeline solo si pasa esto.
// Sin esta funcion, un timecode absurdo del modelo se convierte en un corte
// imposible que ffmpeg rechaza tres pasos despues, con un error que no menciona
// al modelo por ningun lado.

export function validarSegmentos(datos, duracionClip, clip) {
  if (!Array.isArray(datos?.segmentos)) {
    throw new Error(
      `El modelo no devolvio un arreglo 'segmentos' para ${clip}.\n` +
      `  Devolvio: ${JSON.stringify(datos).slice(0, 200)}\n` +
      `  ARREGLO: revisa el prompt; exige el formato JSON explicitamente.`
    );
  }

  const limpios = [];
  for (const [i, s] of datos.segmentos.entries()) {
    const ini = Number(s.inicio), fin = Number(s.fin);

    if (!Number.isFinite(ini) || !Number.isFinite(fin)) {
      console.log(`  DESCARTADO seg ${i}: tiempos no numericos (${s.inicio}, ${s.fin})`);
      continue;
    }
    if (fin <= ini) {
      console.log(`  DESCARTADO seg ${i}: fin ${fin} no es mayor que inicio ${ini}`);
      continue;
    }
    if (fin > duracionClip + 0.5) {
      // Sintoma clasico: el modelo devolvio minutos donde se pidieron segundos.
      console.log(`  SOSPECHA seg ${i}: fin ${fin} s pero ${clip} dura ${duracionClip.toFixed(1)} s`);
      console.log(`  Revisa si el modelo esta devolviendo mm:ss en vez de segundos.`);
      continue;
    }
    if (typeof s.texto !== "string" || s.texto.trim() === "") {
      console.log(`  DESCARTADO seg ${i}: sin texto`);
      continue;
    }
    limpios.push({ inicio: Number(ini.toFixed(1)), fin: Number(fin.toFixed(1)), texto: s.texto.trim() });
  }

  if (limpios.length === 0) {
    throw new Error(`Ningun segmento valido para ${clip}. No se sigue con datos vacios.`);
  }
  const descartados = datos.segmentos.length - limpios.length;
  if (descartados > 0) console.log(`  ${descartados} segmentos descartados de ${datos.segmentos.length}`);
  return limpios;
}
```

---

## El presupuesto: contar antes de gastar

Cada llamada suma. Un lote de 50 clips a transcribir puede costar más de lo que crees si nadie lleva la
cuenta.

```js
// presupuesto.mjs -- tope duro de gasto por corrida.
// Existe porque un bucle con un error puede pedir 400 imagenes en dos minutos.
// El tope no optimiza el costo: evita el accidente.

const TOPE_USD = Number(process.env.TOPE_IA_USD || 3);
let gastado = 0;

export function cobrar(usd, etiqueta) {
  gastado += usd;
  console.log(`  costo ${etiqueta}: $${usd.toFixed(3)}  (acumulado $${gastado.toFixed(2)} de $${TOPE_USD})`);
  if (gastado > TOPE_USD) {
    throw new Error(
      `TOPE DE GASTO SUPERADO: $${gastado.toFixed(2)} de $${TOPE_USD}.\n` +
      `  Se detiene el pipeline. Revisa si hay un bucle pidiendo de mas.\n` +
      `  Si es correcto, sube TOPE_IA_USD a proposito.`
    );
  }
}

export const totalGastado = () => gastado;
```

Y al final de la corrida, el resumen honesto:

```
=== COSTO DE ESTA CORRIDA ===
transcribir      14 clips    $0.42
cortes            1 llamada  $0.08
ilustraciones     4 imagenes $0.16
musica            1 pista    $0.30
                             -----
                             $0.96
```

Guarda ese resumen en `analisis/costos.csv` acumulando por fecha. En tres meses tienes el costo real por
video, que es un número que casi nadie tiene y que hace falta para cotizar (ver `economist_lushows`).

---

## Concurrencia y cuotas

Las cuotas se cuentan de dos formas y hay que respetar las dos: **peticiones por minuto** y **unidades de
trabajo por minuto** (tokens, segundos de audio, imágenes).

| Regla | Valor práctico |
|---|---|
| Concurrencia contra un API | 3–4, no más |
| Al recibir un 429 | bajar la concurrencia a la mitad durante esa corrida |
| Lotes grandes | trocear: 10 elementos, pausa de 5 s, 10 más |
| Si el proveedor manda `Retry-After` | obedecerlo, siempre |

Y una decisión de diseño que ahorra dolores: **procesa en serie los pasos caros y en paralelo los baratos.**
Transcribir 14 clips en paralelo con concurrencia 3 está bien; generar 20 imágenes en paralelo es la forma
más rápida de comerte la cuota del día.

---

## Cuando la IA falla del todo: el plan B

Un paso de IA puede quedar fuera de servicio. El pipeline debe seguir siendo utilizable:

| Paso | Plan B |
|---|---|
| `transcribir` | modelo local (más lento, sin costo) o transcripción manual del bloque que falta |
| `cortes` | medir a mano con la onda de audio del paso `analizar` (módulo `15`) |
| `generar-ilustracion` | usar un fotograma real del bruto y pasarle `forzar-marca` |
| `generar-musica` | pista de biblioteca con licencia (módulo `74`) |
| `verificar` texto | la verificación técnica del módulo `133` sigue funcionando sin IA |

Escribe el plan B en `TRAMPAS.md`, no lo dejes en la cabeza. El día que lo necesites vas a estar con prisa.

---

## Errores comunes

- **Llamar a un modelo dentro de `montar`.** Mata la reproducibilidad del video ese mismo día.
- **No congelar la salida de IA como archivo.** La próxima corrida da otra imagen y el video cambia solo.
- **Guardar la imagen sin el prompt.** Costó dinero y no se puede volver a producir igual.
- **Reintentar errores 400 o 401.** El prompt sigue inválido en el quinto intento; solo gastas tiempo.
- **Reintentos sin jitter.** Cinco procesos paralelos reintentan a la vez y vuelven a chocar.
- **Llamadas sin timeout.** Una petición colgada congela el lote entero sin decir nada.
- **Meter la salida cruda del modelo en la tabla.** Un timecode en minutos se convierte en un corte
  imposible que falla tres pasos después.
- **Caché cuya clave no incluye el modelo.** Cambias de modelo y te devuelve respuestas del anterior.
- **No tener tope de gasto.** Un bucle con un error pide 400 imágenes en dos minutos.
- **Concurrencia alta contra un API.** Cuota quemada y 429 en cadena.
- **Automatizar la elección entre las variantes generadas.** Es gusto (módulo `137`): la IA genera cuatro,
  tú eliges una.
- **No registrar el costo por corrida.** Nunca sabes cuánto cuesta de verdad un video, y cotizas a ciegas.
- **Confiar en que el modelo seguirá existiendo.** Se apagan versiones. Anota cuál usaste y ten plan B
  (módulo `139`).

---

## Checklist

- [ ] Ningún paso de render llama a un modelo de IA
- [ ] Toda salida de IA está congelada como archivo en `assets/generado-ia/` o `analisis/`
- [ ] Cada archivo generado tiene su `.prompt.txt` y su `.meta.json` al lado
- [ ] Todas las llamadas pasan por una sola envoltura con reintentos
- [ ] Los reintentos usan espera exponencial con jitter y respetan `Retry-After`
- [ ] Solo se reintentan errores temporales (408, 429, 5xx)
- [ ] Toda llamada tiene timeout, con valor pensado por tipo de tarea
- [ ] Existe caché por prompt y la clave incluye modelo, parámetros y huella del insumo
- [ ] La salida del modelo se valida antes de entrar a cualquier tabla
- [ ] Los timecodes devueltos se comprueban contra la duración real del clip
- [ ] Hay tope de gasto por corrida y el pipeline se detiene al superarlo
- [ ] Cada corrida imprime el costo desglosado y lo acumula en `analisis/costos.csv`
- [ ] La concurrencia contra APIs está limitada a 3–4
- [ ] Cada paso de IA tiene un plan B escrito en `TRAMPAS.md`
- [ ] La elección entre variantes generadas la hace un humano

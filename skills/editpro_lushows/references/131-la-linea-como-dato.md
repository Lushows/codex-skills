# 131 — La línea de tiempo como dato

## Qué resuelve

Que el montaje deje de ser un archivo binario que solo tú puedes abrir, y pase a ser **una tabla de texto
que cualquiera puede leer, comparar, versionar y corregir**.

La idea central del bloque, y probablemente la más importante de toda la skill después de la verificación:

> **El montaje debe vivir como DATO, no como archivo.**

Una tabla de filas donde cada fila es un bloque: tipo, fuente, entrada, salida, inserto, nota. Cambiar
`57.7` por `58.4` reconstruye el video completo, idéntico salvo en eso.

Eso es lo contrario de arrastrar clips en una línea de tiempo y rezar por no haber movido algo más.

---

## El problema real que resuelve

En una línea de tiempo visual (CapCut, Premiere, DaVinci) el montaje vive dentro del programa. De ahí
salen cuatro problemas que no se pueden arreglar con disciplina:

| Problema | Qué pasa en la práctica |
|---|---|
| **No se puede comparar** | ¿Qué cambió entre `v04` y `v05`? Nadie sabe. Hay que ver los dos videos enteros. |
| **No se puede deshacer parcialmente** | Moviste el corte del bloque 3 y sin querer arrastraste el 4. Lo descubres tres versiones después. |
| **No se puede explicar** | ¿Por qué ese corte quedó en 58.4? "Porque sonaba mejor". Dentro de dos semanas nadie sabe. |
| **No se puede regenerar** | Si el archivo del proyecto se corrompe o cambias de programa, el montaje se perdió. |

Con la línea como dato, los cuatro desaparecen: comparar es un `git diff`, deshacer es cambiar un número,
explicar es la columna `nota`, y regenerar es correr `montar` otra vez.

---

## La tabla: `montaje.csv`

Una fila = un bloque de video. Estas son las columnas del caso maestro:

```csv
bloque,tipo,fuente,entrada,salida,inserto,texto_pantalla,nota
```

| Columna | Qué lleva | Ejemplo |
|---|---|---|
| `bloque` | identificador estable, ordena el video | `b03` |
| `tipo` | qué clase de bloque es | `video`, `imagen`, `negro`, `titulo` |
| `fuente` | archivo del que sale | `clip-07.mp4`, `assets/generado-ia/frasco.png` |
| `entrada` | segundo exacto donde empieza, un decimal | `44.1` |
| `salida` | segundo exacto donde termina | `58.4` |
| `inserto` | qué se ve encima mientras se oye la voz | `broll:clip-11@12.0-15.4`, `punch:1.25`, vacío |
| `texto_pantalla` | la palabra o frase del subtítulo de golpe | `VIDRIO RECICLADO` |
| `nota` | **por qué** ese número es ese número | `58.4 exacto: en 57.7 cortaba "caracteristicas"` |

Dos columnas hacen todo el trabajo conceptual:

- **`inserto`** separa lo que se OYE de lo que se VE. Es la técnica del módulo `23` (voz continua, imagen
  picada) convertida en columna. Sin ella la tabla es un guion; con ella es un montaje.
- **`nota`** es la memoria del proyecto. Es donde vive el *por qué*. Sin ella, dentro de un mes vas a
  "arreglar" un número que estaba bien.

### Ejemplo completo (VIDEO-BOTELLA, 48 s, vertical 9:16)

```csv
bloque,tipo,fuente,entrada,salida,inserto,texto_pantalla,nota
b01,video,clip-03.mp4,12.4,20.6,punch:1.30,MIRA ESTO,"gancho: entra en seco sin saludo. punch para que no se lea videollamada"
b02,video,clip-03.mp4,44.1,50.9,,VIDRIO RECICLADO,"50.9 y no 49.9: en 49.9 se comia la -o final de reciclado"
b03,imagen,assets/generado-ia/frasco-duotono.png,0.0,2.4,,,"respiro visual antes del dato. 2.4 s: menos se lee como error de render"
b04,video,clip-07.mp4,8.0,15.2,broll:clip-11@12.0-15.4,3 SEMANAS,"broll entra en el segundo 4.0 del bloque, cuando dice 'tres semanas'"
b05,video,clip-07.mp4,51.3,58.4,,,"58.4 exacto: en 57.7 cortaba 'caracteristicas'; en 58.5 entra 'Listo, cortemos esa'"
b06,video,clip-09.mp4,22.8,29.1,punch:1.15,SIN PLASTICO,"punch suave, es el bloque de la objecion, no quiero que grite"
b07,titulo,,0.0,1.8,,GASTROLATAM,"cierre de marca. 1.8 s es el minimo legible en vertical"
b08,video,clip-12.mp4,3.2,7.4,,,"blooper. corte en seco a proposito, ver modulo 34"
```

Ocho filas. Eso es el video entero. Se lee en veinte segundos y se entiende sin abrir nada.

**La suma de `salida - entrada` da la duración final antes de renderizar.** En este ejemplo: 48.1 s. Si
necesitas 60, ya sabes que faltan 12 y de qué tipo — no lo descubres después de ocho minutos de render.

---

## Cómo se lee esa tabla: el paso `montar`

`pipeline/montar.mjs`. Lee el CSV, corta cada bloque a un segmento intermedio, y los une.

```js
// montar.mjs -- convierte montaje.csv en un video.
// La tabla manda. Si el video quedo mal, se corrige la tabla y se vuelve a correr;
// NUNCA se ajusta un numero directamente en un comando de ffmpeg suelto: eso
// desincroniza la tabla del resultado y se pierde la trazabilidad.

import { readFileSync, writeFileSync, mkdirSync, existsSync } from "node:fs";
import { spawnSync } from "node:child_process";
import { join } from "node:path";

const RAIZ = process.env.PROYECTO || process.cwd();
const TABLA = join(RAIZ, "montaje.csv");
const SEG = join(RAIZ, "trabajo", "segmentos");
const SALIDA = join(RAIZ, "salida");

// Formato fijo del master. Vive aqui y en ningun otro lado, para que todos los
// segmentos salgan identicos y el concat por copia funcione (ver modulo 101).
const W = 1080, H = 1920, FPS = 30, SR = 48000;

function leerCsv(ruta) {
  const lineas = readFileSync(ruta, "utf8").trim().split(/\r?\n/);
  const cab = lineas.shift().split(",");
  return lineas.map((l, i) => {
    // partir respetando comillas: la columna nota casi siempre trae comas
    const celdas = l.match(/("([^"]|"")*"|[^,]*)(,|$)/g)
      .map((c) => c.replace(/,$/, "").replace(/^"|"$/g, "").replace(/""/g, '"'))
      .slice(0, cab.length);
    const fila = Object.fromEntries(cab.map((c, j) => [c, (celdas[j] ?? "").trim()]));
    fila.__linea = i + 2; // numero de linea real en el archivo, para los errores
    return fila;
  });
}

function correrFfmpeg(args, contexto) {
  const r = spawnSync("ffmpeg", ["-hide_banner", "-loglevel", "error", "-y", ...args], {
    encoding: "utf8",
  });
  if (r.status !== 0) {
    throw new Error(`ffmpeg fallo en ${contexto}\n${r.stderr.trim()}`);
  }
}

const filas = leerCsv(TABLA);
mkdirSync(SEG, { recursive: true });
mkdirSync(SALIDA, { recursive: true });

const lista = [];
let total = 0;

for (const f of filas) {
  const dur = Number(f.salida) - Number(f.entrada);
  if (!(dur > 0)) {
    console.log(`FILA ${f.__linea} (${f.bloque}): salida ${f.salida} no es mayor que entrada ${f.entrada}.`);
    process.exit(1);
  }
  total += dur;

  const destino = join(SEG, `${f.bloque}.mp4`);
  const escala = `scale=${W}:${H}:force_original_aspect_ratio=increase,crop=${W}:${H},fps=${FPS}`;

  if (f.tipo === "video") {
    // -ss ANTES de -i busca rapido pero por fotograma clave; -ss DESPUES es exacto.
    // Aqui va despues porque un corte de voz mal ubicado por 0.3 s parte una palabra.
    correrFfmpeg([
      "-i", join(RAIZ, "entrada", f.fuente),
      "-ss", f.entrada, "-to", f.salida,
      "-vf", escala, "-af", `aresample=${SR}`,
      "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
      "-c:a", "aac", "-b:a", "192k", "-ar", String(SR), "-ac", "2",
      destino,
    ], `${f.bloque} (linea ${f.__linea})`);
  } else if (f.tipo === "imagen") {
    // Imagen fija: hay que fabricarle audio en silencio, si no el concat descuadra.
    correrFfmpeg([
      "-loop", "1", "-t", String(dur), "-i", join(RAIZ, f.fuente),
      "-f", "lavfi", "-t", String(dur), "-i", `anullsrc=r=${SR}:cl=stereo`,
      "-vf", escala, "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p",
      "-c:a", "aac", "-b:a", "192k", "-shortest", destino,
    ], `${f.bloque} imagen`);
  } else if (f.tipo === "negro" || f.tipo === "titulo") {
    correrFfmpeg([
      "-f", "lavfi", "-t", String(dur), "-i", `color=c=black:s=${W}x${H}:r=${FPS}`,
      "-f", "lavfi", "-t", String(dur), "-i", `anullsrc=r=${SR}:cl=stereo`,
      "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p",
      "-c:a", "aac", "-b:a", "192k", destino,
    ], `${f.bloque} ${f.tipo}`);
  } else {
    console.log(`FILA ${f.__linea}: tipo '${f.tipo}' desconocido. Validos: video, imagen, negro, titulo.`);
    process.exit(1);
  }

  lista.push(`file '${destino.replace(/\\/g, "/")}'`);
  console.log(`${f.bloque}  ${dur.toFixed(1)} s  ${f.tipo.padEnd(7)} ${f.fuente || "-"}`);
}

const listaTxt = join(SEG, "lista.txt");
writeFileSync(listaTxt, lista.join("\n") + "\n", "utf8");

const version = process.argv[2] || "01";
const destinoFinal = join(SALIDA, `v${version}-corte.mp4`);
correrFfmpeg(["-f", "concat", "-safe", "0", "-i", listaTxt, "-c", "copy", destinoFinal], "concat final");

console.log(`\n${filas.length} bloques  ${total.toFixed(1)} s  ->  ${destinoFinal}`);
```

Fíjate en lo que **no** hace: no decide nada. Todas las decisiones están en el CSV. El script solo obedece.

---

## La prueba del número: cambiar `57.7` por `58.4`

Este es el caso real que dio nombre a la idea. El bloque `b05` cortaba a mitad de la palabra
"características". El arreglo completo, de principio a fin:

```diff
-b05,video,clip-07.mp4,51.3,57.7,,,"cierre del argumento"
+b05,video,clip-07.mp4,51.3,58.4,,,"58.4 exacto: en 57.7 cortaba 'caracteristicas'; en 58.5 entra 'Listo, cortemos esa'"
```

```powershell
.\edit.ps1 montar 06
```

Y el video vuelve a existir, **idéntico en todo salvo en ese bloque**. No hay riesgo de haber movido el
b04 sin darte cuenta. No hay que volver a alinear los subtítulos. No hay que rehacer la mezcla.

Compara eso con la versión artesanal: abrir el proyecto, encontrar el corte, arrastrarlo, verificar que
no se movió lo de al lado, reexportar, y confiar.

---

## Las cuatro ventajas, concretas

### 1. Reproducible

Mismo CSV + mismo material = mismo video. Siempre. Eso es lo que permite el módulo `132`.

### 2. Versionable

El CSV va en git junto al pipeline. Entonces esto es posible:

```powershell
git log --oneline -- montaje.csv
git diff HEAD~1 -- montaje.csv
```

y la respuesta a "¿qué cambió entre v04 y v05?" son tres líneas de texto, no dos videos.

Mensaje de commit que sí sirve:

```
montaje: b05 hasta 58.4 para no partir "caracteristicas"
```

### 3. Auditable

La columna `nota` responde el "¿por qué?" antes de que lo preguntes. Cuando el cliente diga "el corte del
final me suena raro", abres la tabla y ves que 58.4 fue deliberado y por qué. Si además fue una decisión
del cliente, la nota lo dice y no se discute dos veces.

### 4. Programable

Como es una tabla, se puede transformar con código:

- **Versión de 30 s**: filtra las filas con `rol` secundario y vuelve a montar.
- **Versión horizontal**: cambia `W`/`H` y vuelve a montar. La tabla no cambia.
- **Versión sin blooper**: borra la última fila.
- **Diez ganchos distintos**: diez CSV que solo difieren en `b01`. Eso es el módulo `134`.

---

## Reglas de la tabla (las que evitan el 90% de los problemas)

1. **La tabla es la única fuente de verdad.** Si ajustas algo en un comando suelto y no en la tabla, la
   tabla mintió y todo lo demás se cae.
2. **Un decimal, siempre.** `58.4`, no `58.4231`. El oído no distingue la centésima y los números largos
   esconden errores de dedo.
3. **Toda fila rara lleva `nota`.** Si un número parece equivocado y no lo es, escríbelo. Es el módulo `136`
   aplicado a datos: el comentario dice *por qué*, no *qué*.
4. **`bloque` no se reordena renombrando.** Si necesitas meter algo entre `b03` y `b04`, se llama `b03b`.
   Renumerar todo rompe las notas, los nombres de segmento y el historial.
5. **Las rutas son relativas a la raíz del proyecto.** Nunca `C:\Users\...` dentro del CSV.
6. **Nada de fórmulas de Excel.** Si abres el CSV en Excel, cuidado: convierte `58.4` a fecha, cambia
   comas por puntos según el idioma del sistema y rompe el archivo. Ábrelo en un editor de texto o en
   VS Code.

---

## Qué NO poner en la tabla

La tabla describe la **estructura**, no todos los detalles. Si le metes todo, se vuelve ilegible y pierdes
la ventaja principal, que es leerla de un vistazo.

| Va en la tabla | Va en otro lado |
|---|---|
| qué bloque, de dónde, desde cuándo hasta cuándo | los parámetros del códec (van en el script) |
| el inserto y el texto en pantalla | el estilo del subtítulo (va en el `.ass`) |
| el porqué de cada número | la cadena de limpieza de voz (va en `limpiar-voz`) |
| el orden | el volumen de la música y el ducking (va en `musicalizar`) |

Regla: **si el valor es igual en todos los bloques, no es columna, es configuración.**

---

## Errores comunes

- **Ajustar un corte en el comando de ffmpeg y no en la tabla.** Es el pecado original. A partir de ahí la
  tabla ya no describe el video y todo el sistema pierde sentido.
- **Escribir números con más de un decimal.** `58.4231` da falsa precisión y esconde errores de dedo.
- **Dejar `nota` vacía en los cortes finos.** El número raro de hoy es el "error" que alguien arregla en
  tres semanas, rompiendo lo que estaba bien.
- **Abrir el CSV en Excel y guardarlo.** Cambia separadores, convierte `58.4` en fecha y te rompe el
  archivo sin avisar.
- **Renumerar los bloques al insertar uno nuevo.** Se pierde la correspondencia con notas, segmentos y
  commits anteriores. Usa `b03b`.
- **Meter rutas absolutas en la columna `fuente`.** El proyecto deja de ser portable.
- **Convertir la tabla en un guion.** Si no tiene `entrada`/`salida` medidos, no es un montaje: es una
  intención.
- **Una tabla con 40 columnas.** Se vuelve ilegible. Lo que es igual en todas las filas es configuración,
  no columna.
- **No versionar el CSV.** Sin git, pierdes la ventaja de comparar y volver atrás, que es la mitad del valor.
- **Confundir `inserto` con `fuente`.** `fuente` es lo que se OYE; `inserto` es lo que se VE encima. Si los
  mezclas, pierdes la técnica de voz continua e imagen picada.

---

## Checklist

- [ ] Existe `montaje.csv` en la raíz del proyecto y es la única fuente de verdad del corte
- [ ] Cada fila tiene `bloque`, `tipo`, `fuente`, `entrada`, `salida`
- [ ] Existe la columna `inserto`, separando lo que se oye de lo que se ve
- [ ] Existe la columna `nota` y los cortes finos la tienen escrita, con el *por qué*
- [ ] Todos los tiempos tienen exactamente un decimal
- [ ] Las rutas de `fuente` son relativas a la raíz del proyecto
- [ ] La suma de `salida - entrada` se imprime antes de renderizar y cuadra con la duración objetivo
- [ ] `montar` no toma ninguna decisión: solo obedece a la tabla
- [ ] Cambiar un número y volver a montar produce un video idéntico salvo en ese bloque
- [ ] `montaje.csv` está en git y cada cambio tiene un mensaje de commit que explica el porqué
- [ ] Nunca se ajustó un tiempo en un comando suelto sin actualizar la tabla
- [ ] El CSV nunca se guardó desde Excel
- [ ] Los identificadores de bloque no se renumeran: se insertan como `b03b`
- [ ] Lo que es igual en todas las filas está en el script, no repetido como columna

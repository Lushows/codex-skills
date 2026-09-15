# 127 — Costos y cuotas: qué cuesta cada cosa, cómo abaratarla y qué hacer con un 429

## La regla que evita el susto

> **Calcula el costo ANTES de generar, no después de recibir la factura.**

Suena obvio. Nadie lo hace. Y el patrón de gasto en generación de video es traicionero porque cada
clip individual parece barato —dos dólares, tres dólares— y la factura del mes llega en trescientos.

La razón es simple: **pagas por lo que generas, no por lo que usas.** Y la relación entre esas dos
cosas en un montaje real es de 5 a 1 o peor.

---

## Los precios (agosto 2026)

Todos aproximados y **verificables en la página oficial del proveedor**. Los precios de este mercado
se mueven cada pocos meses.

### Video

| Modelo | USD/segundo aprox. |
|---|---|
| Veo 3.1 Lite, 720p, sin audio | ~$0.03 |
| Veo 3.1 Lite, 720p | ~$0.05 |
| Veo 3.1 Fast, 720p | ~$0.10 |
| **Veo 3.1 estándar, 720p/1080p, con audio** | **~$0.40** |
| Veo 3.1 4K | ~$0.30–$0.60 |
| Seedance 2.0 (tier rápido) | ~$0.022 |
| Seedance 2.0 (normal, según revendedor) | ~$0.056–$0.08 |
| Kling 3.0 estándar (fal) | ~$0.084 |
| Kling 3.0 pro (fal) | ~$0.112 |
| Kling 3.0 multi-plano con audio | ~$0.20 |
| ~~Sora 2 Pro~~ (deprecado) | ~$0.75 |

**El número que tienes que memorizar: un clip de 8 segundos con audio en Veo estándar cuesta unos
$6 USD.** Si generas 20 variantes de eso buscando la buena, gastaste $120 en un plano.

### Imagen

| Modelo | USD/imagen aprox. |
|---|---|
| Imagen 4 Fast | ~$0.02 |
| Grok Imagine | ~$0.02 |
| Gemini 2.5 Flash Image | bajo |
| Gemini 3 Pro Image (1K/2K) | ~$0.134 |
| Gemini 3 Pro Image (4K) | ~$0.24 |

Detalle que muerde: **Gemini 3 Pro Image cobra ~560 tokens por cada imagen que le mandas de
entrada.** Seis referencias en cada llamada, repetidas cien veces, se notan.

### Transcripción

| Servicio | USD/minuto aprox. |
|---|---|
| Deepgram | ~$0.0043 |
| OpenAI Whisper (archivo) | ~$0.003–$0.006 |
| AssemblyAI | ~$0.0061 (~$0.37/hora) |
| Google Cloud STT | ~$0.016 |
| OpenAI tiempo real | ~$0.017 |

La transcripción es **barata**. Una hora de entrevista cuesta menos de medio dólar. No optimices
aquí; optimiza en video.

### Música

Lyria en Vertex: verifica el precio vigente en la página de precios de Vertex AI. A la fecha está en
`preview` y el esquema de cobro puede cambiar. En términos relativos es mucho más barato que video.

---

## De dónde sale el gasto real

Descomposición de un proyecto típico de reel de 30 segundos con 6 planos generados:

```
Planos que quedaron en el corte final ..........  6 clips × 5 s
Variantes descartadas ..........................  ~18 clips × 5 s   (3 por plano)
Pruebas de prompt del principio .................  ~8 clips × 5 s
Regeneraciones por derivación de marca ..........  ~6 clips × 5 s
Clips generados de más "por si acaso" ...........  ~4 clips × 5 s
──────────────────────────────────────────────────
TOTAL GENERADO: 42 clips × 5 s = 210 segundos
TOTAL USADO:    30 segundos
```

**Ratio real: 7 a 1.** A $0.40/s eso son $84 para un reel de 30 segundos. A $0.05/s son $10.50.

Esa diferencia —$84 contra $10.50, por el mismo trabajo— es enteramente decisiones tuyas de
configuración. Ahí está el margen.

---

## Las siete formas de abaratar (en orden de impacto)

### 1. Apaga el audio en el b-roll

**La palanca más grande que existe.** El audio puede multiplicar el precio por 4 u 8 según la
variante.

Y aquí está lo absurdo: **el b-roll va debajo de tu voz en off y tu música; ese audio lo vas a
silenciar de todos modos.** Estás pagando 4× por una pista que borras.

Regla: `generateAudio: false` por defecto. Actívalo solo cuando el plano tiene un personaje hablando
en cámara y necesitas la sincronía labial.

### 2. Usa el tier barato para lo que nadie mira fijo

De tus 6 planos, típicamente 1 es el plano protagonista (el producto, la cara, el momento) y 5 son
apoyo de 2 segundos.

- **Plano protagonista** → Veo estándar. Vale la pena.
- **Los 5 de apoyo** → Lite o Fast. Nadie los va a pausar para juzgarlos.

Solo eso baja la factura del proyecto entre 60% y 80%.

### 3. Genera la duración exacta

Cada segundo generado se paga aunque no lo uses. Si el plano dura 3 segundos en el guion, genera 4
(3 + colchón de medio segundo por punta), no 8.

Corolario: **haz el guion antes de generar.** "Genero unos clips y después veo qué monto" es la
forma más cara de trabajar que existe.

### 4. Prueba en imagen antes de gastar en video

Una imagen de Imagen 4 Fast cuesta $0.02. Un clip de Veo estándar cuesta $2.

Antes de generar video, **resuelve la composición, la paleta y el estilo en imágenes fijas.** Cuando
tengas el fotograma cero aprobado, entonces sí lo mandas a animar. Estás pagando $0.06 por tres
iteraciones de imagen en vez de $6 por tres iteraciones de video.

Esta es la razón real por la que el módulo `122` existe.

### 5. Usa la Batch API

Google corta el precio **exactamente a la mitad** en la Batch API, a cambio de una ventana de
procesamiento de hasta 24 horas.

Si estás generando 200 imágenes para una campaña que se publica la semana entrante, no hay ninguna
razón para pagar el doble. Planifica con un día de anticipación y ahorra el 50%.

### 6. Prepara el audio antes de transcribir

Antes de subir nada a un servicio de transcripción:

```bash
ffmpeg -i bruto.mp4 -vn -ac 1 -ar 16000 -c:a pcm_s16le audio.wav
```

Mono, 16 kHz, sin video. No es solo más barato en algunos esquemas de cobro: es **radicalmente más
rápido de subir** y la calidad de transcripción es igual o mejor, porque 16 kHz es la frecuencia con
la que están entrenados los modelos de voz.

Un video de una hora pasa de varios gigas a ~55 MB. Y nunca uses streaming para un archivo ya
grabado: cuesta entre 20% y 80% más.

### 7. Cachea todo y no regeneres nunca lo mismo

Guarda junto a cada resultado: prompt, semilla, parámetros, modelo, fecha y costo. Con eso:

- no vuelves a generar algo que ya tenías,
- puedes reusar planos entre proyectos de la misma marca,
- y cuando el cliente pide "el de la vez pasada", lo tienes.

Una estructura mínima que funciona:

```
proyecto/
  generado/
    plano-01/
      clip.mp4
      referencia.png
      meta.json     ← {"modelo":"veo-3.1-generate-001","seed":48211,
                        "prompt":"...","params":{...},"segundos":5,"usd":0.25}
```

---

## Cuotas y el 429

### Qué es un 429

`429 Too Many Requests` = te pasaste del límite de peticiones permitidas. Hay varios límites
simultáneos y el mensaje no siempre te dice cuál tocaste:

- **peticiones por minuto** (el más común)
- **generaciones concurrentes** (cuántas operaciones tienes abiertas al tiempo)
- **cuota diaria del proyecto**
- **límites del modelo específico** (los modelos `preview` suelen tener cuotas mucho más estrechas)

### ❌ Lo que NO se hace

```js
// esto empeora todo
while (true) {
  const r = await generar();
  if (r.ok) break;
  // reintenta inmediatamente
}
```

Reintentar sin esperar te hunde más: sigues consumiendo el presupuesto de peticiones, el servicio te
sigue rechazando, y algunos proveedores endurecen el límite cuando detectan este patrón.

### ✅ Retroceso exponencial con jitter

```js
async function conReintentos(fn, maxIntentos = 6) {
  for (let i = 0; i < maxIntentos; i++) {
    try {
      return await fn();
    } catch (e) {
      const codigo = e.status ?? e.code;
      // 429 = cuota; 500/503 = el servicio está mal. Los dos se reintentan.
      if (codigo !== 429 && codigo !== 500 && codigo !== 503) throw e;
      if (i === maxIntentos - 1) throw e;

      // respeta Retry-After si el servidor lo manda
      const retryAfter = Number(e.headers?.['retry-after']) * 1000;
      const espera = retryAfter || (2 ** i) * 1000 + Math.random() * 1000;

      console.warn(`  ${codigo} — esperando ${Math.round(espera/1000)}s (intento ${i+1}/${maxIntentos})`);
      await new Promise(r => setTimeout(r, espera));
    }
  }
}
```

Las esperas quedan en ~1 s, 2 s, 4 s, 8 s, 16 s, 32 s. El **jitter** (el `Math.random()`) evita que
si tienes varios trabajos en paralelo, todos reintenten en el mismo instante y se vuelvan a chocar.

### Y sobre todo: genera en serie, no en paralelo

```js
// ❌ 40 peticiones simultáneas = 429 garantizado
await Promise.all(planos.map(p => generar(p)));

// ✅ una a la vez, con pausa
for (const p of planos) {
  await conReintentos(() => generar(p));
  await new Promise(r => setTimeout(r, 3000));
}
```

Generar video es lento de todos modos (uno a varios minutos por clip). El paralelismo agresivo no te
ahorra tiempo real y sí te garantiza rechazos. Si quieres paralelismo, ponle un tope de 2 o 3
concurrentes.

### Si el 429 es persistente

1. **Mira la cuota real** en Google Cloud → IAM y administración → Cuotas. Filtra por el servicio.
2. **Pide aumento de cuota.** Es un formulario. Para proyectos con facturación activa, suelen
   aprobarlo.
3. **Cambia de región.** `us-central1` está saturada casi siempre. Prueba otra región donde el
   modelo esté disponible.
4. **Verifica que no sea un `preview`.** Los modelos preview (como `lyria-3-pro-preview`) tienen
   cuotas mucho más estrechas y no las van a subir.

---

## Presupuestar para un cliente

Lo que la gente cotiza mal: cotizan el costo del clip final. Cotiza esto:

```
Segundos que van en la pieza final ......................  S
Ratio de exploración (5× a 8× en la práctica) ...........  ×6
Segundos a generar ......................................  S × 6
Tarifa según tier y audio ...............................  T
──────────────────────────────────────────────────────────
COSTO DE GENERACIÓN = S × 6 × T
+ imágenes de prueba (≈ $0.02 × 30)
+ transcripción (≈ $0.40/hora de bruto)
+ música (2 o 3 generaciones)
+ MARGEN DE SEGURIDAD 30%
```

Ejemplo, reel de 30 segundos con la mitad generada:

```
15 s finales × 6 = 90 s generados
90 s × $0.05 (Lite sin audio) = $4.50
+ imágenes de prueba: $0.60
+ música: ~$1
+ 30% de margen
≈ $8 USD de costo directo
```

Y ese mismo reel, si generas todo en Veo estándar con audio: `90 × $0.40 = $36`.

**La misma pieza cuesta $8 o $36 según cómo configures.** Eso es tu margen, y es la razón por la que
este módulo existe.

Nota para vender: **el costo de la API no es lo que le cobras al cliente.** Le cobras tu criterio,
tu montaje y tu tiempo. La API es un insumo, como la gasolina para un transportador. Pero si no
sabes cuánto gasta el carro, no sabes cuánto ganas.

---

## Errores comunes

- **Generar con audio por defecto.** Es la palanca de costo más grande y casi siempre estás pagando
  por una pista que vas a silenciar.
- **Usar el tier caro para todo.** El 80% de tus planos son apoyo de 2 segundos. Van en Lite.
- **Generar 8 segundos para usar 2.** Pagaste 8. Haz el guion antes.
- **Explorar directamente en video.** Explora en imagen a $0.02, no en video a $2.
- **No usar la Batch API cuando podías esperar unas horas.** Estás pagando el doble por nada.
- **Subir el video completo a transcribir.** Extrae audio mono 16k: mismo resultado, fracción del
  tamaño.
- **Usar transcripción en tiempo real para un archivo grabado.** Entre 20% y 80% más caro.
- **Reintentar un 429 inmediatamente y en bucle.** Empeoras el bloqueo.
- **Lanzar 40 generaciones en paralelo.** 429 garantizado y no ganas tiempo real.
- **No poner jitter en el retroceso.** Los trabajos paralelos vuelven a chocar sincronizados.
- **No guardar prompt, semilla y parámetros.** Regeneras lo mismo dos veces y lo pagas dos veces.
- **Cotizar el costo del clip final.** El ratio real de exploración es de 5 a 8 a 1.
- **Confiar en precios de blogs.** La mitad de los "precios agosto 2026" son copias de enero.
- **No poner una alerta de presupuesto en la nube.** El día que un bucle se descontrole, lo vas a
  saber por la factura.

---

## Checklist

- [ ] Verifiqué los precios en la **página oficial** del proveedor, no en un blog
- [ ] Calculé el costo del plano **antes** de generarlo (segundos × tarifa × variantes)
- [ ] `generateAudio` está **apagado** en todo lo que no lleve voz sincronizada
- [ ] Los planos de apoyo van en el **tier barato**; el tier caro solo para el plano protagonista
- [ ] Hice el **guion antes** de generar y sé cuántos segundos necesita cada plano
- [ ] Exploré composición y estilo en **imágenes fijas** antes de gastar en video
- [ ] Si podía esperar horas, usé la **Batch API** (mitad de precio)
- [ ] Extraje el audio a **mono 16 kHz** antes de transcribir, y no usé streaming
- [ ] Mi código genera **en serie** (o con tope bajo de concurrencia), con pausa entre llamadas
- [ ] Mi código maneja 429/500/503 con **retroceso exponencial + jitter**, y respeta `Retry-After`
- [ ] Guardo `meta.json` con modelo, prompt, semilla, parámetros, segundos y costo por cada
      generación
- [ ] La cotización al cliente usa un ratio de exploración de **5× a 8×** más 30% de margen
- [ ] Tengo una **alerta de presupuesto** configurada en la cuenta de nube

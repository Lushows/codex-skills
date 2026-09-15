# 115 — Audio y efectos: qué se puede escribir y qué no

El audio en CapCut se guarda con la misma lógica que todo lo demás: material + segmento + compañeros.
Pero acá hay una frontera importante que hay que entender antes de perder tiempo:

> **Hay cosas que son *datos* (se escriben desde afuera) y cosas que son *procesos* (los tiene que
> calcular CapCut o su nube).**

Un desvanecido es un dato: dos números. La separación de voz y música es un proceso: hay un modelo que
tiene que analizar el audio y generar archivos nuevos. Podés escribir la bandera que lo pide, pero el
trabajo lo hace la app.

Este módulo separa las dos cosas.

---

## Materiales de audio

```json
{
  "id": "AAAA-...",
  "type": "extract_music",
  "name": "musica_fondo",
  "path": "C:/media/reel001/musica.mp3",
  "duration": 143000000,
  "music_id": "",
  "local_material_id": "",
  "source_platform": 0,
  "intensifies_path": "",
  "wave_points": []
}
```

| Campo | Qué es |
|---|---|
| `path` | Ruta absoluta al archivo. Igual que en video: sin acentos, corta, estable. |
| `duration` | Duración real del archivo **en microsegundos** |
| `type` | `"extract_music"` (archivo importado), `"music"` (de la biblioteca), `"sound"` (efecto), `"record"` (grabado en la app) |
| `wave_points` | La forma de onda dibujada en la línea de tiempo. Se puede dejar vacío: CapCut la recalcula. |

**El `type` importa.** Si le ponés `"music"` a un archivo tuyo, CapCut puede buscarlo en su biblioteca
y no encontrarlo. Para archivos que vos importás, `"extract_music"` es el valor seguro. Como siempre:
mirá qué escribe CapCut en el molde cuando importás un MP3 a mano.

Sacá la duración con `ffprobe`:

```bash
ffprobe -v error -show_entries format=duration -of csv=p=0 musica.mp3
```

Y convertila: `round(segundos * 1000000)`.

---

## Segmentos de audio

```json
{
  "id": "BBBB-...",
  "material_id": "AAAA-...",
  "target_timerange": { "start": 0, "duration": 51400000 },
  "source_timerange": { "start": 8000000, "duration": 51400000 },
  "volume": 0.25,
  "speed": 1.0,
  "extra_material_refs": ["CCCC-...", "DDDD-...", "EEEE-..."],
  "visible": true,
  "render_index": 0
}
```

Las mismas dos ventanas de tiempo del módulo 113:

- `source_timerange` → desde qué segundo del MP3 arranco (útil para saltarte la intro de la canción)
- `target_timerange` → dónde cae en el video

Y la misma regla: **`target.duration = source.duration / speed`**.

### `volume`

Es un multiplicador lineal, no decibeles:

| `volume` | Equivale a |
|---|---|
| 1.0 | 100%, sin cambio (0 dB) |
| 0.5 | −6 dB |
| 0.25 | −12 dB |
| 0.1 | −20 dB |
| 0.0 | silencio |

Conversión desde decibeles: `volume = 10 ** (dB / 20)`.

**Valores prácticos que funcionan** (ver módulo 103 para el porqué):

| Situación | `volume` de la música |
|---|---|
| Música sola, sin voz | 0.5 – 0.7 |
| Música bajo una voz clara | **0.12 – 0.20** |
| Música bajo voz en ambiente ruidoso | 0.08 – 0.12 |
| Efecto de sonido puntual | 0.4 – 0.8 |

La música casi siempre está más fuerte de lo que debería. Si dudás, bajala.

**Ojo:** `volume` en el segmento es un valor único para todo el clip. Para automatizar el volumen a lo
largo del tiempo (agachar la música justo cuando habla y subirla después) necesitás **fotogramas
clave**, que es el terreno más frágil del formato. Alternativa mucho más segura: **cortá la música en
varios segmentos** con volúmenes distintos, o hacé el ducking con ffmpeg (`sidechaincompress`, módulo
103) antes de meter el archivo.

---

## Desvanecidos: `audio_fades`

Esto sí es un dato puro y se escribe sin drama.

```json
// en materials.audio_fades[]
{
  "id": "CCCC-...",
  "type": "audio_fade",
  "fade_in_duration": 500000,
  "fade_out_duration": 1200000
}
```

Y el segmento lo referencia desde `extra_material_refs`.

Duraciones que funcionan:

| Caso | Entrada | Salida |
|---|---|---|
| Música de fondo en un reel | 300–500 ms | 800–1500 ms |
| Corte entre dos músicas | 200 ms | 200 ms |
| Voz (para quitar el clic del corte) | 20–40 ms | 20–40 ms |
| Cierre de video | — | 1500–2500 ms |

**El detalle que hace que un video suene amateur o profesional:** un video que termina con la música
cortada de golpe suena a error. Una salida de 1,5 segundos y suena intencional. Es literalmente un
número en un archivo.

Ese fade de 20-40 ms en la voz también importa: cuando cortás un clip en medio de una onda de audio,
el salto de amplitud produce un clic audible. Un fade cortísimo lo elimina.

---

## Los compañeros que CapCut pone solo

Todo segmento de audio (y de video con sonido) suele traer varios materiales compañeros que existen
aunque no los uses:

| Grupo en `materials` | Qué guarda | ¿Lo escribo yo? |
|---|---|---|
| `speeds` | Velocidad de reproducción | Sí (1.0 si no hago nada) |
| `sound_channel_mappings` | Cómo se mapean los canales (izq/der/ambos) | Copiar del molde |
| `vocal_separations` | Estado de la separación voz/música | Copiar del molde |
| `audio_fades` | Los desvanecidos | Sí |
| `beats` | Marcas de tiempo del ritmo detectado | Solo lectura, útil |
| `realtime_denoises` | Reducción de ruido | Bandera, el trabajo lo hace CapCut |
| `vocal_beautifys` | "Embellecer voz" | Bandera |

**La regla es siempre la misma:** copiá estos objetos del molde con IDs nuevos. Si falta alguno que
CapCut esperaba, el proyecto no abre. Si sobra uno huérfano, tampoco.

---

## La frontera: datos vs. procesos

Acá está lo que hay que entender para no perder una tarde.

### Cosas que SÍ podés escribir desde afuera (datos)

- Qué archivo suena y desde qué segundo
- Cuándo empieza y cuándo termina en el video
- El volumen
- Los desvanecidos de entrada y salida
- La velocidad de reproducción
- Cuántas pistas de audio hay y qué va en cada una

### Cosas que NO se resuelven escribiendo un campo (procesos)

| Función | Por qué |
|---|---|
| **Separar voz y música** | Un modelo de IA tiene que analizar el audio y generar dos archivos nuevos. La bandera solo *pide* el proceso. |
| **Reducción de ruido** | Idem: se calcula al reproducir o al exportar. |
| **Embellecer voz** | Procesamiento en tiempo real. |
| **Detección de beats** | CapCut analiza la canción y llena `beats`. Vos podés **leerlo**, pero no lo generás. |
| **Subtítulos automáticos** | Va a la nube de ByteDance, consume créditos. |
| **Texto a voz** | Idem. |

**Qué hacer con esto:** si necesitás separación de voz o quitar ruido de verdad, **hacelo antes con
ffmpeg o con una herramienta dedicada** (módulo 103: `afftdn`, `arnndn`, `highpass`, `loudnorm`), y
metele a CapCut el archivo ya limpio. Es más rápido, más controlable, y no depende de créditos.

El puente es para el **montaje**, no para el procesamiento de señal. Ese trabajo lo hace mejor ffmpeg.

### `beats`: lo que sí vale la pena leer

Si en el molde le pediste a CapCut que detecte el ritmo de una canción, `materials.beats` te queda con
una lista de marcas de tiempo en microsegundos.

**Eso es oro para un montaje automático.** Podés leer esas marcas y alinear tus cortes exactamente en
el pulso de la música (módulo 24). No necesitás generar los beats: solo leerlos de un molde que ya los
tiene, o calcularlos aparte con una librería de análisis de audio y escribir tus cortes en esas
posiciones.

```bash
jq '.materials.beats[] | .user_beats, .ai_beats' draft_content.json
```

---

## Efectos de video: `materials.effects`

Los efectos visuales (glitch, destello, zoom pulsante, granulado) viven en `materials.effects[]` o
`materials.video_effects[]` según la versión, y van en pistas `type: "effect"` o referenciados desde
un segmento.

```json
{
  "id": "FFFF-...",
  "name": "Glitch",
  "effect_id": "6790...",
  "resource_id": "6790...",
  "type": "video_effect",
  "adjust_params": [
    { "name": "effects_adjust_speed",     "value": 0.5 },
    { "name": "effects_adjust_intensity", "value": 0.8 }
  ]
}
```

**Misma historia que las plantillas de texto:** `effect_id` y `resource_id` son del catálogo de
ByteDance. **No se inventan.** Se copian de un molde donde aplicaste el efecto a mano.

Los `adjust_params` sí son tuyos: son los deslizadores que ves en la interfaz, normalizados de 0.0 a
1.0. Esos podés variarlos libremente.

**Consejo de oficio, no técnico:** los efectos de CapCut envejecen mal y muy rápido. Un glitch estaba
de moda hace dos años y hoy grita "editado con plantilla". El módulo 21 y el 63 tienen la opinión
larga. Para el puente: usá dos o tres efectos como máximo, siempre los mismos, y que sean sutiles.

---

## Una arquitectura de audio que funciona

Para un reel típico, esta distribución de pistas es la que menos problemas da:

```
tracks[n]   audio  →  efectos puntuales (whoosh, ding)    volume 0.4–0.8
tracks[n-1] audio  →  música de fondo                     volume 0.12–0.20, fades
tracks[n-2] audio  →  voz en off separada (si la hay)      volume 1.0
tracks[0..] video  →  los clips (su audio propio va acá)   volume 1.0
```

Reglas:

- **Una pista, un propósito.** No mezcles música y efectos en la misma pista: cuando quieras bajarle
  el volumen a la música vas a tener que tocarlos todos.
- **La voz siempre a 1.0** y todo lo demás relativo a ella. Si la voz quedó baja, arreglá el archivo
  con `loudnorm` (módulo 103), no subiendo el volumen del segmento.
- **Normalizá el audio antes de importar.** Un archivo a −16 LUFS entra parejo y no tenés que andar
  ajustando volúmenes clip por clip.

```bash
# normalizar a estándar de redes antes de meterlo a CapCut
ffmpeg -i voz_cruda.wav -af "highpass=f=80,afftdn=nf=-25,loudnorm=I=-16:TP=-1.5:LRA=11" voz.wav
```

Ese comando de una línea hace más por tu audio que cualquier función de la app.

---

## Errores comunes

**Poner la música muy fuerte.** El error universal. Si hay voz, la música va en 0.12–0.20, no en 0.5.

**Cortar la música de golpe al final.** Suena a error técnico. Una salida de 1,5 s cuesta un número.

**No poner un fade cortito en los cortes de voz.** El clic del corte es audible y le da un aire barato
al video. 20–40 ms lo resuelven.

**Intentar automatizar el volumen con fotogramas clave.** Es el terreno más frágil del formato. Cortá
la música en segmentos con volúmenes distintos, o hacé el ducking con ffmpeg antes.

**Confundir `volume` con decibeles.** 0.5 no es "la mitad de fuerte", es −6 dB. La conversión es
`10^(dB/20)`.

**Esperar que escribir `vocal_separations` separe la voz.** Es una bandera que pide un proceso, no el
proceso. Si necesitás voz limpia, limpiala con ffmpeg antes.

**Confiar en la reducción de ruido de CapCut para audio malo.** Está bien para un poquito de zumbido.
Para un audio realmente sucio, el resultado suena metálico. Arreglalo en origen.

**Inventar `effect_id` o `resource_id`.** Son del catálogo de ByteDance. Se copian del molde.

**Usar el `type` equivocado en el material de audio.** Un archivo tuyo es `"extract_music"`. Si le
ponés `"music"`, CapCut puede intentar resolverlo contra su biblioteca.

**Mezclar música y efectos en la misma pista.** Te ata las manos para ajustar niveles después.

**Olvidar que la duración del audio también va en microsegundos.** Una canción de 2:23 son
`143000000`, no `143000`.

**Meter efectos visuales de moda.** Envejecen en meses y delatan la plantilla. Dos o tres, sutiles, y
siempre los mismos.

---

## Checklist

- [ ] Cada archivo de audio tiene su material con `path` absoluto y `duration` en microsegundos
- [ ] El `type` del material corresponde (archivos importados: `"extract_music"`)
- [ ] Cada segmento de audio tiene `source_timerange` y `target_timerange` coherentes
- [ ] `target.duration == source.duration / speed`
- [ ] La voz está en `volume: 1.0` y todo lo demás es relativo a ella
- [ ] La música bajo voz está entre 0.12 y 0.20, no más
- [ ] Todos los segmentos de música tienen `audio_fades` de entrada y de salida
- [ ] El final del video tiene una salida de al menos 1,5 s
- [ ] Los cortes de voz tienen un fade de 20–40 ms para matar el clic
- [ ] Normalicé el audio con `loudnorm` **antes** de importarlo, no lo arreglo con volúmenes
- [ ] Limpié ruido con ffmpeg antes de importar, no confío en la función de la app
- [ ] Una pista por propósito: voz, música, efectos, separadas
- [ ] Los compañeros (`speeds`, `sound_channel_mappings`, `vocal_separations`) los copié del molde con IDs nuevos
- [ ] Ningún compañero quedó huérfano ni le falta a un segmento
- [ ] Los `effect_id` / `resource_id` salen de un molde real
- [ ] Abrí el proyecto y **escuché** el resultado con audífonos, no solo miré que abre

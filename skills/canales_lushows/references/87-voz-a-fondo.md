# 87 · Voz a fondo

**Qué resuelve:** la voz es el 70% de la percepción de calidad del episodio. Se genera
con **edge-tts** (voces neuronales de Microsoft, gratis y sin API key) y se procesa con
una cadena fija. Coste: $0. Reclamos de Content ID: imposibles.

> 📌 **Este módulo es el resumen.** El bloque `280–289` es la versión operativa y las
> medidas de allí son las vigentes: ritmo (§ `281`), tabla de pausas por signo (§ `282`),
> cifras (§ `283`), una sola pasada (§ `284`), relieve (§ `285`), cadena (§ `286`) y el
> riesgo de licencia de `edge-tts` (§ `287`). Donde este módulo y el bloque discrepen,
> mandan el bloque y el código de `piloto/`.

---

## La voz del canal

```
es-MX-JorgeNeural   ·   rate -6%   ·   pitch -2Hz      ← lo que hay HOY en voz.py
```

⚠️ Este módulo se escribió con `+8% / -3Hz`, que daba **168 ppm**: demasiado rápido. El
canal bajó a `-6% / -2Hz` = **147 ppm medidas** (§ `281`). Las tablas de pausas de más
abajo se midieron a `+8%`; las vigentes, medidas a `-6%`, están en § `282`.

Grave, seca, sin sonrisa. El acento mexicano neutro es el que menos localiza en
Latinoamérica y no suena a locutor de radio comercial.

```bash
pip install edge-tts
```

## Catálogo útil (todas verificadas en el listado de edge-tts)

| Registro | Voz | Notas |
|---|---|---|
| **Canal (documental)** | `es-MX-JorgeNeural` | La del canal. Grave y neutra |
| Alternativa colombiana | `es-CO-GonzaloNeural` | Un poco más clara y cercana |
| Alternativa neutra US | `es-US-AlonsoNeural` | Sirve si Jorge se repite mucho |
| Rioplatense | `es-AR-TomasNeural` | Localiza mucho: a propósito |
| Femenina neutra | `es-MX-DaliaNeural` | Para citas de una mujer del expediente |

## 🔴 La regla de UNA pasada

**El texto se genera de una sola vez. Nunca frase por frase.**

Misma voz, mismo párrafo, medido:

| Método | Duración | Qué pasa |
|---|---|---|
| Troceado en frases y pegado con silencios | **13,99 s** | Cada trozo arranca su entonación desde cero |
| **Una sola pasada, puntuación haciendo las pausas** | **9,81 s** | Prosodia continua |

**Un 43% más largo y suena cortado.** El modelo neuronal construye la curva de
entonación sobre el texto completo: al partirlo, cada fragmento vuelve a empezar en el
tono de arranque y la cifra final suena despegada de la frase que la trae.

Si hay que trocear (por bloques del guion visual), se trocea por **párrafo completo**,
nunca por frase, y jamás dentro de una oración.

## La puntuación es la partitura

Las pausas no se editan: se escriben. Medido con `es-MX-JorgeNeural` a `+8%`:

| Signo | Pausa añadida | Uso |
|---|---|---|
| `,` coma · `;` | **+0,24 s** | Respiración corta dentro de la frase |
| `:` dos puntos · ` — ` raya | **+0,26 s** | Anuncia lo que viene |
| `.` punto | **+1,03 s** | Cierra idea |
| `...` suspensivos | **+1,01 s** | Suspenso. Es el recurso del gancho |
| `?` interrogación | **+1,01 s** | Pregunta que queda en el aire |
| Salto de línea o párrafo | **+1,03 s** | **No añade más que un punto** |

Dos consecuencias prácticas: **el párrafo no pausa más que un punto** (para más hay que
meter silencio con `anullsrc`), y **los suspensivos compran un segundo entero sin cerrar
la idea** — por eso son el signo del gancho.

## `rate` y `pitch`

| Parámetro | Rango útil | Efecto |
|---|---|---|
| `rate` | `-10%` a `+20%` | **+8%** es el del canal. Sobre +20% se atropella |
| `pitch` | `-6Hz` a `+2Hz` | **−3Hz** da gravedad sin sonar a truco |

Cambiar `rate` cambia la duración del episodio: tocarlo después de la fase de tiempos
descoloca el guion visual entero.

## Generar

```python
import asyncio, io, edge_tts

async def di(texto, destino, voz="es-MX-JorgeNeural", rate="+8%", pitch="-3Hz"):
    com = edge_tts.Communicate(texto, voz, rate=rate, pitch=pitch)
    audio = b""
    async for ch in com.stream():
        if ch["type"] == "audio":
            audio += ch["data"]
    if not audio:
        raise RuntimeError(f"sin audio [{voz}]: {texto[:40]}")
    io.open(destino, "wb").write(audio)
```

El `raise` no sobra: cuando el servicio rechaza una voz devuelve el flujo **sin datos y
sin excepción**. Sin él, el pipeline sigue con un MP3 de 0 bytes y el fallo aparece tres
fases después.

## La cadena de proceso

```
highpass=f=80,
equalizer=f=240:width_type=q:w=1.0:g=2.5,
equalizer=f=3200:width_type=q:w=1.2:g=3.0,
equalizer=f=7000:width_type=q:w=1.5:g=-2.0,
acompressor=threshold=0.10:ratio=3.5:attack=6:release=160:makeup=1.6,
aexciter=level_in=1:level_out=1:amount=1.2:drive=6:blend=0.3:freq=7500,
aecho=0.85:0.55:22:0.16,
alimiter=limit=0.95
```

| Filtro | Qué hace | Por qué |
|---|---|---|
| `highpass=f=80` | Quita el retumbe | El TTS trae basura bajo 80 Hz que ensucia el grave del colchón |
| `equalizer 240 +2,5` | Cuerpo | La voz sintética es delgada de pecho |
| `equalizer 3200 +3,0` | Presencia | La banda de la inteligibilidad: la saca de la mezcla |
| `equalizer 7000 −2,0` | Doma la sibilancia | Sin esto, cada «s» pica |
| `acompressor` | Nivel estable | El sidechain (`85`) necesita una señal predecible |
| `aexciter` | Armónicos altos | Le da "aire": es lo que hace que no suene a robot |
| `aecho 0,85:0,55:22 ms` | Micro-ambiente | 22 ms es una sala pequeña; sin él la voz flota sobre la mezcla |
| `alimiter=0.95` | Techo | Antes de entrar al maestro |

Después, en la mezcla, la voz lleva `highpass=f=85`, su propio `acompressor` y
`volume=1.85`. Medida así, el stem de voz de `episodio01` da **−24,8 LUFS**: es la
referencia contra la que se calibra todo lo demás (`80`, `89`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Generar frase por frase | 43% más largo y con prosodia rota. Es *el* defecto de este canal |
| Pegar silencios entre trozos | Empeora lo anterior: se oye el corte de entonación |
| Confiar en `\n\n` para pausar más | No añade nada sobre el punto: hace falta silencio explícito |
| No comprobar que el flujo trae audio | MP3 de 0 bytes y el fallo aparece tres fases después |
| Cambiar `rate` después de la fase de tiempos | Se descoloca el guion visual entero |
| Saltarse el realce de 3,2 kHz | Hay que agachar el fondo el doble para entender |
| Aprobar la imagen antes que la voz | Si la voz cambia, se rehacen las fases 4 a 7 |

## Relacionado

`85` ducking · `86` medir · `88` idiomas · `95` escribir para el oído

---

## 🔴 El eco que enredaba la voz

12-sep-2026. Luis, oyendo el audio suelto sin imagen: *«la escucho como muy enredada …
se escucha feo»*. La cadena de voz llevaba esto desde el principio:

```
aecho=0.85:0.55:22:0.16
```

Un *slapback* de **22 ms al 16%**, puesto para «dar presencia». Es una receta conocida
en música, y es mala idea sobre narración: un retardo tan corto sumado al original
produce **filtrado en peine** — cancelaciones repartidas cada ~45 Hz a lo largo de todo
el espectro de la palabra. El resultado se oye hueco y doblado, y sobre una voz sintética,
que ya arrastra artificio, se lee directamente como enredo.

**La presencia no se da con un eco: se da con el ecualizador**, y la cadena ya lo tenía
(+3 dB en 3,2 kHz). El eco no añadía nada que no estuviera ya, y ensuciaba.

Quitarlo no cambia ni la duración ni los tiempos: la locución se rehace desde el crudo
(§ `400`), el reloj no se mueve y el montaje no se toca.

## Cómo se detectó, que es lo interesante

**No por medida.** El máster daba −14,1 LUFS, pico −1,2 dBTP, sin recorte, con la voz
14-15 dB por encima de la cama. Todo correcto. Lo cazó una persona **oyendo el audio sin
la imagen delante** — y esa es la prueba que faltaba en el protocolo: el sonido de este
canal se diseña para ir debajo de unas imágenes, y eso tapa sus defectos. Escucharlo
solo es un control de calidad distinto, y hay que hacerlo.

## Copias de revisión: el códec importa

Los MP4 con audio **AAC** no sonaban en la máquina de Luis; el mismo audio en **MP3** sí.
El fichero era correcto de manual (AAC-LC, 44,1 kHz, estéreo, sin lista de edición rara,
−13 dB RMS medidos). Da igual: una copia de revisión que no suena no sirve de nada.

> Para revisar se entrega **MP4 con audio MP3**, o el audio suelto en MP3. El máster se
> queda en AAC, que es lo que YouTube quiere.

Y el nivel de la copia de revisión se sube con **`volume`, no con un segundo `loudnorm`**:
normalizar por encima de un máster ya normalizado (LRA 2,2) es bombeo garantizado.

## Relacionado

§ `86` (medir el audio · la frecuencia de muestreo) · § `400` (el silencio) · § `286`
(la cadena de proceso) · § `140` (control de calidad)

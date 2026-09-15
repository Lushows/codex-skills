# 85 · Ducking y espacio

**Qué resuelve:** que la voz mande siempre sin tener que aplastar el resto. El ducking
mal hecho se oye peor que no tenerlo: bombea, se come las primeras sílabas o deja el
fondo muerto. Con tres parámetros bien puestos, nadie nota que existe.

---

## Qué es

`sidechaincompress` toma **dos entradas**: la que se comprime y la que manda. Cuando la
segunda pasa un umbral, la primera baja. Aquí manda la voz y baja todo lo demás.

```
[bed][vozsc]sidechaincompress=threshold=0.055:ratio=2.8:attack=60:release=750[bedd]
```

**El orden importa:** primera entrada = lo que se agacha, segunda = la que empuja.
Invertirlas produce el efecto contrario y no da error.

## 🔴 Una salida de filtro se consume UNA sola vez

La voz hace dos cosas: se oye, y controla el ducking. Pero una etiqueta de ffmpeg se
gasta al usarla — reutilizar `[voz]` en el `sidechaincompress` y en el `amix` final
rompe el grafo. La solución es `asplit`:

```
[1:a]aformat=channel_layouts=stereo,highpass=f=85,
     acompressor=threshold=0.06:ratio=3.2:attack=8:release=180,
     volume=1.85,asplit=2[voz][vozsc]
```

`[vozsc]` es la copia de control; **no se escucha nunca**, solo entra al sidechain. Sale
después del compresor de voz a propósito: así el umbral ve una señal ya estable y el
ducking no depende de lo fuerte que hable el locutor en cada frase.

## Los parámetros, uno a uno

| Parámetro | Valor del canal | Qué pasa si se mueve |
|---|---|---|
| `threshold` | **0,055** (≈ −25 dBFS) | Más alto: solo agacha en los gritos. Más bajo: agacha con la respiración |
| `ratio` | **2,8** | Por encima de 5 el fondo desaparece y vuelve: eso es bombeo |
| `attack` | **60 ms** | Por debajo de 20 ms se come el ataque de la primera sílaba |
| `release` | **750 ms** | Por debajo de 400 ms el fondo sube entre palabra y palabra: bombeo |
| `makeup` | 1 (sin usar) | El nivel se recupera después, en el maestro |

`threshold` va en **lineal**, no en dB. La conversión:

| Lineal | dBFS | Lineal | dBFS |
|---|---|---|---|
| 0,020 | −34,0 | 0,100 | −20,0 |
| **0,055** | **−25,2** | 0,178 | −15,0 |
| 0,079 | −22,0 | 0,316 | −10,0 |

`dB = 20·log10(lineal)` · `lineal = 10^(dB/20)`

## Cuánto tiene que bajar

El objetivo es **4 a 6 LU** de descenso mientras habla la voz. No más.

| Descenso | Resultado |
|---|---|
| 0-2 LU | No se nota: la voz sigue peleando con el fondo |
| **4-6 LU** | La voz manda y el fondo sigue vivo. Es el punto |
| 8-12 LU | El fondo desaparece en cada frase: se oye el vaivén |
| >12 LU | Ya no es ducking, es un interruptor |

Se comprueba midiendo (`86`): el LUFS momentáneo del `bed` con y sin voz encima no
debe diferir más de 6 LU.

## El espacio de frecuencia: la otra mitad del trabajo

El ducking baja el nivel; **el filtrado le hace sitio a la voz**. La inteligibilidad de
la palabra vive entre 2 y 4 kHz, así que el colchón se corta antes:

```
[g1][g2][aire][lat][sala]amix=inputs=5:normalize=0,
lowpass=f=1100,tremolo=f=0.14:d=0.28,
afade=t=in:st=0:d=2.5,afade=t=out:st=87.3:d=3.2[cama]
```

`lowpass=f=1100` sobre la cama es lo que permite tenerla a solo 12-15 LU bajo la voz sin
que estorbe: ocupa el registro grave, que la voz no usa. Un colchón de banda ancha al
mismo nivel taparía cada consonante.

| Capa | Banda que ocupa | Cómo se le hace sitio |
|---|---|---|
| Voz | 85 Hz - 12 kHz, con el peso en 2-4 kHz | `highpass=f=85` y un realce en 3,2 kHz (`87`) |
| Colchón | 40-1100 Hz | `lowpass=f=1100` |
| Objetos | La que les toque | Ducking + nivel (`83`) |
| Picos | 40-90 Hz (impacto), 700 Hz+ (riser) | El silencio posterior (`84`) |

## Espacio estéreo

La voz va **al centro y en mono**; el colchón, ancho. Es lo que da la sensación de que
la voz está delante y el mundo detrás, sin tocar ni un nivel.

```
# ensanchar solo el colchón, nunca la voz
[cama]stereotools=mlev=0.9:slev=1.4[camaw]
```

Nunca aplicar ensanchado a la mezcla completa: en un móvil, que suma a mono, lo que se
ensanchó se cancela y la voz pierde cuerpo.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Reutilizar `[voz]` sin `asplit` | ffmpeg falla: la etiqueta ya se consumió |
| Entradas del sidechain al revés | Se agacha la voz bajo la música, sin aviso de error |
| `threshold` en dB | ffmpeg lo espera lineal: 0,055, no −25 |
| `attack` por debajo de 20 ms | Se pierde el ataque de la primera sílaba de cada frase |
| `release` por debajo de 400 ms | El fondo sube entre palabras: bombeo audible |
| `ratio` alto para "que se oiga la voz" | El fondo desaparece y reaparece; se oye el truco |
| Ducking sin `lowpass` en la cama | Hay que agachar el doble para entender la palabra |
| Ensanchar la mezcla completa | En móvil se cancela y la voz pierde cuerpo |
| Poner el ducking después del `loudnorm` | El sidechain ve señal ya nivelada y deja de reaccionar |

## Relacionado

`80` arquitectura · `84` picos · `86` medir · `87` voz

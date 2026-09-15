# 100 · Anatomía de un sonido

**Qué resuelve:** por qué durante semanas el fondo del canal fue `anoisesrc=c=pink`
más un tono de 55 Hz y el espectador lo llamó «un ruido». No faltaba música: faltaban
las cuatro cosas que convierten una frecuencia en un **instrumento**.

---

## Las cuatro cosas

| # | Ingrediente | Qué aporta | Sin él suena a |
|---|---|---|---|
| 1 | **Fundamental** | La altura. Es la nota que el oído nombra | — |
| 2 | **Armónicos** | El timbre. *Qué* instrumento es | Examen de oído |
| 3 | **Envolvente** | El gesto. *Cómo* se produjo el sonido | Zumbido de nevera |
| 4 | **Ruido de ataque** | La materia. Arco, aire, fieltro, madera | Sintetizador de 1982 |

Un `sine` solo tiene el punto 1. Por eso no es un instrumento: **es una medida**.

## Medido, no opinado

Tres versiones de un Do4 (261,63 Hz), dos segundos cada una:

```bash
# 1) seno puro
ffmpeg -filter_complex "sine=f=261.63:d=2:sample_rate=44100,volume=0.5[out]" \
  -map "[out]" -ar 44100 -ac 1 -y seno.wav

# 2) cinco armónicos, todos con la MISMA caída
ffmpeg -filter_complex "\
sine=f=261.63:d=2:sample_rate=44100,volume='0.5*exp(-t/0.8)':eval=frame[a0];\
sine=f=523.26:d=2:sample_rate=44100,volume='0.19*exp(-t/0.8)':eval=frame[a1];\
sine=f=784.89:d=2:sample_rate=44100,volume='0.09*exp(-t/0.8)':eval=frame[a2];\
sine=f=1046.5:d=2:sample_rate=44100,volume='0.042*exp(-t/0.8)':eval=frame[a3];\
[a0][a1][a2][a3]amix=inputs=4:normalize=0[out]" -map "[out]" -ar 44100 -ac 1 -y igual.wav

# 3) cada armónico con SU caída + ataque de 8 ms  ← esto ya es un piano
ffmpeg -filter_complex "\
sine=f=261.63:d=2:sample_rate=44100,volume='0.5*exp(-t/0.800)':eval=frame[a0];\
sine=f=523.26:d=2:sample_rate=44100,volume='0.19*exp(-t/0.470)':eval=frame[a1];\
sine=f=784.89:d=2:sample_rate=44100,volume='0.09*exp(-t/0.333)':eval=frame[a2];\
sine=f=1046.5:d=2:sample_rate=44100,volume='0.042*exp(-t/0.250)':eval=frame[a3];\
[a0][a1][a2][a3]amix=inputs=4:normalize=0,afade=t=in:st=0:d=0.008[out]" \
  -map "[out]" -ar 44100 -ac 1 -y piano.wav
```

Medido con `ebur128`:

| Versión | I | Pico real | Qué se oye |
|---|---|---|---|
| Seno puro | −27,9 LUFS | −24,1 dBFS | Un pitido de examen |
| Caídas iguales | −34,3 LUFS | −22,4 dBFS | Un órgano de juguete |
| Caídas distintas | −34,8 LUFS | −22,4 dBFS | Una nota de piano |

**Las tres miden casi lo mismo y suenan a tres mundos distintos.** El volumen no es
el problema del fondo que teníamos: la forma lo es.

## 🔴 El generador `sine` no sale a escala completa

Comprobado en esta instalación (ffmpeg 8.1.2):

```
sine=f=440:d=1                   → pico  -18,06 dBFS   (amplitud 0,125)
aevalsrc='sin(2*PI*440*t)':d=1   → pico    0,00 dBFS   (amplitud 1,0)
```

**`sine` sale 8 veces (18 dB) por debajo de `aevalsrc`.** Mezclar los dos en el mismo
grafo sin compensar es la razón número uno de que un instrumento quede inaudible al
lado de otro. Regla del canal: o todo sale de `sine`, o se compensa con `volume=8`.

## Los armónicos: dónde vive el timbre

La serie es `f0 · 1, 2, 3, 4…`. Lo que cambia entre instrumentos es **qué pesa cada
uno** y **cuáles faltan**:

| Instrumento | Perfil | Se escribe como |
|---|---|---|
| Piano | Todos, cayendo rápido | `1/n^1,4` con caída propia por armónico (`101`) |
| Cuerda frotada | Todos, sostenidos | `1/n^1,15`, sin caída (`102`) |
| Flauta | Casi solo la fundamental | `1 · 0,16 · 0,05` (`103`) |
| **Clarinete** | **Solo impares** | `1, 3, 5, 7, 9` (`103`) |
| Percusión | Ninguno: no hay altura | Ruido + filtro resonante (`104`) |

Un armónico por encima de 16 kHz no se oye y sí consume margen: se descarta al
construir la voz.

## La envolvente es el gesto

La envolvente cuenta **cómo se produjo** el sonido, y el oído lo lee sin pensarlo:

| Ataque medido | Se interpreta como | Ejemplo del canal |
|---|---|---|
| 8–15 ms | Un golpe | Piano, timbal, golpe de mesa |
| 40–60 ms | Una nota pulsada | Bajo |
| 130–250 ms | Algo que **empuja** | Violín, violonchelo |
| 400 ms o más | Algo que **aparece** | Colchón, pad |

Es el parámetro que más identidad da y el que más se olvida.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Usar un `sine` pelado como música | Pitido de examen de oído; es lo que pasó |
| Mezclar `sine` y `aevalsrc` sin compensar 18 dB | Un instrumento tapa al otro sin razón aparente |
| Todos los armónicos con la misma caída | Órgano de juguete: la nota no se «redondea» |
| Armónicos por encima de 16 kHz | Margen gastado en algo inaudible |
| Envolvente plana | Zumbido; el oído no encuentra el gesto |
| Ruido filtrado como sustituto de música | «Se siente como un ruido» — literal |

## Relacionado

`101` piano · `104` percusión · `108` por qué suena a pitido · `82` música por código

# 117 · Dejarle sitio a la voz

**Qué resuelve:** el error que tuvimos. Una cama densa obliga a bajarla hasta que deja de
sentirse, y entonces el episodio se queda sin fondo en cada pausa. La solución no es el
volumen: es **componer pocas notas y lejos de la banda de la voz**.

---

## La banda

**300 - 3.400 Hz** es la banda telefónica (norma ITU-T G.712). Conviene saber qué es y
qué no: no es "donde está la voz", es el recorte mínimo que conserva la inteligibilidad.
La voz de `es-MX-JorgeNeural` (`87`) tiene su fundamental alrededor de **100-130 Hz**,
pero lo que hace entender las palabras —formantes y consonantes— vive por encima de 300,
con lo más crítico entre **2 y 4 kHz**. Por eso se mide ahí.

| Banda | Qué vive | Quién manda |
|---|---|---|
| 40 - 110 Hz | Bajo del ostinato, impactos | **La música.** La voz apenas está |
| 110 - 300 Hz | Fundamental de la voz + acordes medios | Zona compartida. Cuidado |
| **300 - 3.400 Hz** | Inteligibilidad de la locución | **La voz, sola** |
| > 5.200 Hz | Nada: `piano.py:110` corta ahí | — |

## 🔴 El `loudnorm` iguala todas las piezas: lo único que cambia es la banda

`tocar()` termina en `loudnorm=I=-30:TP=-6:LRA=6` (`piano.py:111`). Medido sobre nueve
piezas distintas, el nivel total sale entre **−27,85 y −29,10 dB RMS**: 1,25 dB de
diferencia entre la pieza más escasa y la más densa.

**Componer más notas no sube la pieza. Mueve la energía a la banda de la voz.**

| Pieza | Notas | Máx. simultáneas | Notas ≥300 Hz | Total | Banda voz | **Margen** |
|---|---|---|---|---|---|---|
| `112_desnudo` (ostinato sin cima) | 24 | 4 | **0** / 24 | −28,43 | −48,47 | **20,04 dB** |
| `115_cifra` (octavas, sin 3ª) | 8 | 4 | 2 / 8 | −28,91 | −45,20 | 16,30 dB |
| `112_con_cima` | 29 | 5 | 4 / 29 | −28,50 | −43,17 | 14,68 dB |
| `mus_sospecha` (piloto) | — | — | — | −27,85 | −41,93 | 14,08 dB |
| `mus_cierre` (piloto) | — | — | — | −28,68 | −42,59 | 13,91 dB |
| `117_escaso` | 19 | 5 | 3 / 19 | −28,57 | −42,24 | 13,67 dB |
| `119_1890` | 22 | 6 | 4 / 22 | −29,10 | −40,09 | 10,98 dB |
| `mus_expediente` (piloto) | — | — | — | −28,17 | −38,43 | **10,26 dB** |
| `117_denso` | 52 | **11** | **32** / 52 | −29,08 | −35,69 | **6,61 dB** 🔴 |

**Umbral del canal: ≥ 12 dB de margen.** Por debajo, la pieza pelea con la locución y la
única salida es bajarla hasta que no se siente — que es exactamente el error de `80`.

Dos lecturas más de la tabla:

- `mus_expediente` es **la pieza del piloto más justa** (10,26 dB), y no por casualidad:
  es la única cuya melodía toca en **todos** los compases. `mus_sospecha` toca uno de
  cada dos y gana casi 4 dB de margen con la misma armonía.
- Medido aparte: la energía por encima de 300 Hz y la energía entre 300 y 3.400 Hz
  difieren **menos de 0,02 dB** en las tres piezas del piloto. Es decir: **todo lo que
  el piano pone por encima de 300 Hz ya está dentro de la banda de la voz.** No hay nada
  que ganar filtrando por arriba; lo que hay que hacer es poner menos notas ahí.

## Medirlo

```python
def solapes(notas):
    """Máximo de notas sonando a la vez, y cuántas caen en la banda de la voz."""
    ev = []
    for t, n, d, _ in notas:
        ev.append((t, 1)); ev.append((t + d, -1))
    ev.sort()
    viva = maxv = 0
    for _, s in ev:
        viva += s; maxv = max(maxv, viva)
    return maxv, sum(1 for _, n, _, _ in notas if hz(n) >= 300), len(notas)
```

```bash
# Margen real del archivo ya renderizado, en dB
ffmpeg -i pieza.wav -af "astats=measure_perchannel=none:measure_overall=RMS_level" -f null -
ffmpeg -i pieza.wav -af "highpass=f=300:poles=2,highpass=f=300:poles=2,\
lowpass=f=3400:poles=2,astats=measure_perchannel=none:measure_overall=RMS_level" -f null -
```

⚠️ `astats` imprime en nivel **info**: con `-loglevel error` no sale nada y parece que la
medición falló. El `highpass` va **dos veces** porque con `poles=2` la pendiente es de
12 dB/octava y una sola pasada deja pasar demasiado grave.

## Las cuatro reglas de la textura escasa

| Regla | Valor | Por qué |
|---|---|---|
| **Notas simultáneas** | máx. **5** | A partir de 6 el margen cae por debajo de 12 dB |
| **Notas ≥ 300 Hz** | menos del **20%** del total | `117_denso` tiene el 62% y por eso falla |
| **Melodía** | uno de cada dos compases | `mus_sospecha` gana 4 dB sobre `mus_expediente` solo por esto |
| **Registro de la melodía** | octava 4, nunca 5 | `D5` = 587,33 Hz y sus armónicos caen en pleno 2-4 kHz |

Y una que no es de textura: el nivel base de la mezcla es **0,34**, medido para quedar
**14 LU bajo la voz** (`acabar.py:100`). Ese número se multiplica por la intensidad del
bloque (`115`). **No se toca el `loudnorm` de la pieza para subirla o bajarla**: se toca
la intensidad.

## El error que tuvimos

En `80` está documentado: el colchón medía **24 LU por debajo de la voz** en lugar de
12-15. Durante la locución no se notaba nada; en cada respiración el nivel se caía al
suelo y el episodio daba **18 saltos de nivel**. Al subirlo al rango correcto bajaron a 6.

La causa no fue el fader. Fue que la cama era demasiado densa para el sitio que tenía, y
la única forma de que no molestara era enterrarla. **Una pieza escasa se puede tener alta;
una densa hay que esconderla, y una cama escondida no cumple su función.**

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Añadir voces "para que suene más rico" | El `loudnorm` iguala el total: lo único que sube es la banda de la voz |
| Melodía en la octava 5 | Los armónicos caen en 2-4 kHz, justo donde viven las consonantes |
| Bajar el fader en vez de quitar notas | La cama deja de sentirse y las pausas suenan a corte (`80`) |
| Filtrar la pieza por arriba para "hacerle sitio" | Ya está cortada a 5.200 Hz: todo lo de arriba de 300 está en la banda |
| Melodía en todos los compases | 4 dB de margen perdidos por nada |
| Medir con `-loglevel error` | `astats` no imprime y parece que falló la medición |
| Tocar `loudnorm` para ajustar el nivel | Descuadra la mezcla entera. El mando es la intensidad del bloque |

## Relacionado

`112` el ostinato · `115` progresiones por tramo · `116` tempo y pulso · `118` cuándo no
debe haber música · `80` arquitectura de la mezcla · `85` ducking · `86` medir el audio · `87` voz a fondo

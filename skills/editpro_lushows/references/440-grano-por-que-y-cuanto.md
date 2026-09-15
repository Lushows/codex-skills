# 440 — Grano: por qué y cuánto

El grano tiene **una** función técnica y una estética. La técnica se puede medir y tiene un óptimo
numérico. La estética no. Este módulo mide la técnica para que la estética no se gaste el presupuesto
de la otra.

Lo que este módulo **no** repite: las dosis de acabado (`editpro/66`), el grano como efecto de época
(`editpro/57`), el grano por canal de la emulación de película (`editpro/257`) ni las cuatro recetas
por procedencia de pieza (`canales/66`). Aquí solo: **cuánto ruido es, de verdad, cada número**, y
**a partir de qué punto deja de comprar nada**.

---

## 1. `alls=N` no es la desviación. Medido

Casi todo el mundo trata `alls` como si fuera la sigma del ruido. No lo es. Medido sobre un gris
plano de 128 (1920×1080, un fotograma, sin compresión de por medio):

| filtro | σ real (niveles) | media | pico |
|---|---|---|---|
| `noise=alls=2:allf=t+u` | 0,500 | 127,48 | ±1 |
| `noise=alls=3:allf=t+u` | 0,610 | 127,99 | ±1 |
| `noise=alls=5:allf=t+u` | **0,992** | 127,97 | ±2 |
| `noise=alls=6:allf=t+u` | 1,177 | 127,46 | ±3 |
| `noise=alls=8:allf=t+u` | 1,555 | 127,45 | ±4 |
| `noise=alls=12:allf=t+u` | 2,321 | 127,41 | ±6 |
| `noise=alls=20:allf=t+u` | 3,861 | 127,37 | ±10 |
| `noise=alls=30:allf=t+u` | 5,782 | 127,32 | ±15 |

Dos hechos que salen de la tabla y no están en ningún sitio:

**(a) `allf=u` reduce a la mitad la amplitud real.** El mismo `alls` sin la `u` (gaussiano) da casi el
doble: `alls=5:allf=t` → σ **1,709** y pico ±8, frente a 0,992 y ±2 con `u`. No son dos sabores de lo
mismo: son dos dosis distintas con la misma etiqueta. Si alguien te pasa una receta con `alls=8` y no
te dice si lleva `u`, no te ha dicho la dosis.

**(b) `u` oscurece.** La media baja de 128,0 a 127,3 según sube `alls`. Es ruido uniforme recortado
contra el fondo: quita un poco más de lo que pone. A `alls=30` son −0,7 niveles en toda la imagen. No
es grave; es motivo para no encadenar tres pasadas de grano "por si acaso".

```bash
# medir la sigma real de TU compilación, en 10 segundos
ffmpeg -v error -f lavfi -i color=c=gray:s=1920x1080 -vf "noise=alls=5:allf=t+u" \
  -frames:v 1 -pix_fmt gray -f rawvideo - | python -c \
  "import sys,numpy as np;a=np.frombuffer(sys.stdin.buffer.read(),'u1');print(a.std())"
```

---

## 2. Para qué sirve de verdad: el antibandeo, medido

El grano rompe los escalones de un degradado. Eso no es opinión, es *dithering*: el ruido convierte
un error de cuantización sistemático en uno aleatorio, y el ojo (que promedia una vecindad) recupera
el valor continuo.

Caso real del canal: un fondo de tinta cuyo degradado recorre **35 niveles a lo ancho de 1920 px**.

```python
import numpy as np
x = np.linspace(0, 1, 1920); real = 60 + 35*x       # el degradado continuo
def analiza(sig, semilla=1):
    rng = np.random.default_rng(semilla)
    q = np.round(real if sig == 0 else np.clip(real + rng.uniform(-sig*1.732, sig*1.732, real.shape), 0, 255))
    cortes = np.flatnonzero(np.diff(q) != 0)                      # dónde salta el valor
    anchos = np.diff(np.r_[0, cortes, len(q)-1])                  # anchura de cada escalón
    prom = np.convolve(q, np.ones(16)/16, mode="valid")           # lo que promedia el ojo
    return anchos.mean(), len(cortes), np.abs(prom - real[8:8+len(prom)]).mean()
```

| σ | `alls` con `u` | anchura del escalón | saltos | error del promedio de 16 px |
|---|---|---|---|---|
| 0,00 | — | **53,3 px** | 35 | 0,178 |
| 0,50 | 2 – 3 | 1,9 px | 1 014 | **0,112** |
| 0,99 | 5 | 1,4 px | 1 414 | 0,208 |
| 1,55 | 8 | 1,2 px | 1 578 | 0,311 |
| 2,32 | 12 | 1,1 px | 1 688 | 0,466 |
| 3,09 | 16 | 1,1 px | 1 749 | 0,610 |

Léelo despacio, porque decide la dosis de todo el canal:

1. **Sin grano, la banda mide 53 px de ancho.** Por eso se ve: es una franja plana del ancho de un
   dedo con un borde duro.
2. **Con σ = 0,5 ya está disuelta** (1,9 px) y el error de reconstrucción **baja** de 0,178 a 0,112.
   El grano no solo tapa la banda: hace la imagen *más fiel* al degradado real.
3. **A partir de ahí no se gana nada.** De 1,9 px a 1,1 px no hay diferencia visible, y el error de
   reconstrucción **empeora** monótonamente: 0,112 → 0,610.

> **El trabajo técnico del grano está hecho en σ ≈ 0,5, o sea `alls=2` o `3` con `u`.** Todo lo que
> pongas por encima es decisión estética, y se paga en bits (`editpro/446`) y en fidelidad.

El piloto del canal usa `alls=5` (σ 0,99). Es el doble del mínimo funcional: está pagando textura,
no antibandeo. Es una decisión legítima — pero es una decisión, no una necesidad.

---

## 3. Dónde hace falta y dónde no

| Zona del cuadro | ¿banda? | grano necesario |
|---|---|---|
| Degradado de fondo, viñeta, foco suave | sí, casi siempre | `alls=2-3:t+u` mínimo |
| Cielo, pared lisa, humo | sí | idem |
| Collage de recortes con detalle | no | ninguno — ya hay alta frecuencia |
| Texto y rótulos | no | el grano sobre el texto solo lo ensucia |
| Piel en primer plano | no | el grano encima de piel afilada canta |

Esto es lo que justifica no aplicarlo al vídeo entero: la mitad del cuadro no lo necesita y toda ella
paga. Ver `editpro/448`.

---

## 4. Grano solo en luma

| filtro | σ |
|---|---|
| `noise=c0s=5:c0f=t+u` | 0,893 |
| `noise=c0s=8:c0f=t+u` | 1,381 |
| `noise=c0s=12:c0f=t+u` | 2,081 |

Prácticamente la misma σ que `alls` del mismo número, pero sin tocar el croma. Como el croma va
submuestreado en 4:2:0, el ruido de color se agrupa en bloques de 2×2 y se ve como confeti. **Si
dudas, `c0s`.** `alls` solo tiene sentido cuando quieres el confeti (VHS, `editpro/57`).

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Copiar un `alls` de una receta sin saber si llevaba `u` | La mitad o el doble de la dosis pretendida |
| Subir `alls` "para que se note" cuando el problema era una banda | La banda ya estaba resuelta en σ 0,5; solo pagas bits |
| Grano sobre todo el cuadro para tapar una banda de una esquina | Ver `editpro/448` |
| Grano en `alls` cuando bastaba `c0s` | Confeti de color en el 4:2:0 |
| Encadenar dos pasadas de grano | La media se va oscureciendo y el ruido se suma en cuadratura, no linealmente |
| Aplicar grano y no volver a mirar la banda | El grano puede desaparecer en la compresión y la banda vuelve (`editpro/446`) |
| Dar el grano por bueno mirando un PNG | El PNG no dice si es temporal (`editpro/441`) ni si sobrevive |

---

## Relacionado

`editpro/441` grano temporal o congelado · `editpro/446` ruido que sobrevive a la compresión ·
`editpro/448` textura por capa, no global · `editpro/449` medir si la textura suma ·
`editpro/66` viñeta, nitidez y textura (dosis de acabado) · `editpro/57` grano como efecto ·
`editpro/257` grano por canal en emulación de película · `canales/66` las cuatro texturas por
procedencia · `canales/52` texturas de fondo

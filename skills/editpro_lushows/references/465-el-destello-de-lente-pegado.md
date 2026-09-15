# 465 — El destello de lente pegado: afirmar un sol que no existe

**Qué resuelve:** el `56` (punto 3) lo dice con claridad: un destello real ocurre porque **hay una
fuente de luz en el encuadre**; si tu plano es una oficina con luz plana y le pones un flare, estás
afirmando que hay un sol ahí, y el ojo lo detecta como incoherente aunque el espectador no sepa
explicarlo. **→ ver `56` para el porqué.** Aquí se miden las dos cosas que lo convierten en dato: si
hay fuente, y cuánto lava la imagen la capa que pegaste.

---

## 1. Primera medida: ¿hay fuente en el encuadre?

Una fuente de luz o un reflejo especular **satura**. En un fotograma de 8 bits, eso son píxeles pegados
al techo. Si no hay ninguno, no hay nada en ese plano capaz de producir un destello.

```python
# fuente.py — ¿hay algo lo bastante brillante como para producir un flare?
import sys, numpy as np
from PIL import Image
for p in sys.argv[1:]:
    im = np.asarray(Image.open(p).convert("RGB")).astype(np.float32)
    Y = 0.299*im[...,0] + 0.587*im[...,1] + 0.114*im[...,2]
    print(f"{p:22} %píxeles ≥240: {(Y>=240).mean()*100:6.3f}%   "
          f"p99,9={np.percentile(Y,99.9):6.1f}   Ymáx={Y.max():5.1f}")
```

Tres fotogramas de archivo reales, medidos:

| Plano | % de píxeles ≥240 | Percentil 99,9 | Lectura |
|---|---|---|---|
| Fajos de billetes, luz de estudio | **0,000%** | 219,6 | **No hay fuente. Ninguna.** |
| Pasillo institucional | 0,033% | 215,1 | Un reflejo mínimo; no sostiene un flare |
| Avión contra el cielo | 0,290% | 246,0 | Sí hay fuente: el cielo satura |

> **Umbral: por debajo del 0,02% de píxeles ≥240 no hay fuente de luz en el encuadre.** Un destello ahí
> no es un efecto: es una afirmación falsa sobre la escena. Y en el plano de los billetes el número es
> **0,000%** — ni un píxel.

Esta medida cuesta tres segundos y resuelve la discusión antes de abrir el banco de destellos.

---

## 2. Segunda medida: cuánto lava

Los destellos de banco vienen sobre negro y se mezclan en modo Pantalla o Suma. A opacidad alta **suman
luz por todo el cuadro**, no solo donde está el dibujo del destello, y eso aplana la imagen. Se mide
restando contra la placa limpia y mirando **en qué decil de luminancia cae la luz añadida**.

```bash
# el compuesto, a dos dosis
ffmpeg -y -loglevel error -i placa.png -i destello.png \
  -filter_complex "[0:v][1:v]blend=all_mode=screen:all_opacity=0.35" -frames:v 1 flare_35.png
```

```bash
# y la lectura rápida, sin escribir código: recuerda -loglevel info (ver 460)
ffmpeg -hide_banner -loglevel info -i flare_35.png -vf signalstats,metadata=print -f null - 2>&1 \
  | grep -E "YMIN|YLOW|YAVG"
```

Mismo destello (halo + barra + tres iris), mismo plano, dos dosis:

| | YMIN | YLOW (p10) | **YAVG** | Luz añadida al decil más oscuro | % de píxeles tocados |
|---|---|---|---|---|---|
| Placa limpia | 21 | 51 | **106,1** | — | — |
| + destello al 35% | 24 | 55 | **110,8** | **+6,1** | 43,6% |
| + destello al 100% | 24 | 56 | **120,2** | **+18,1** | 53,1% |

A opacidad plena el destello sube la luminancia media **14,1 puntos** (106,1 → 120,2) y mete **18
niveles de luz en la parte más oscura de la imagen**, tocando más de la mitad del cuadro. Eso es precisamente lo que el `56`
llama "lavan la imagen": los negros dejan de ser negros, y el negro que es negro de verdad es el primer
punto de la lista de lo que hace que un video se vea caro.

> **Umbral: si el decil más oscuro gana más de 8 niveles, aplanaste el plano.** Comprueba después el
> contraste con `63-look-cinematografico.md` y los scopes con `69-monitoreo-y-scopes.md`.

---

## 3. Tercera medida: ¿está anclado a algo?

Un destello real nace de una fuente física: si la cámara se mueve, el destello **se mueve con esa
fuente** (y además pivota respecto al eje óptico). Una capa pegada con `overlay=x=0:y=0` tiene, por
construcción, **desplazamiento cero**: la placa se mueve y el destello no.

```bash
# placa con paneo de 2 px por fotograma, por construcción
ffmpeg -y -loglevel error -loop 1 -i foto.png -t 1.0 -r 30 \
  -vf "crop=540:960:x='2*n':y=400" -c:v libx264 -crf 14 -pix_fmt yuv420p pan.mp4
```

Con esa placa, la capa pegada se desplaza 0 px/fotograma mientras la escena se desplaza 2. No hace falta
medirlo: lo dice el comando. Lo que sí hay que hacer es **anclar el destello a la fuente** siguiendo su
posición, y eso es un problema de seguimiento: `264-tracking-y-seguimiento.md`.

Y la regla del `56` que no se mide y manda sobre todo lo anterior: **si el flare estaba en el material
porque filmaste contra una luz, no lo estás poniendo, lo estás conservando.** Eso sí es cine.

---

## Errores frecuentes

1. **Poner el destello y luego buscarle sitio.** Primero se mide si hay fuente; si no la hay, no hay
   conversación.
2. **Bajar la opacidad para "integrarlo".** Al 35% sigue metiendo +6 niveles en las sombras y tocando el
   43% del cuadro. Menos opacidad no es más integración.
3. **Usar modo Normal en vez de Pantalla.** El elemento viene sobre negro: tapas el plano con un
   rectángulo (`267`, §3).
4. **Dejarlo clavado en un plano que se mueve.** Desplazamiento cero contra una escena que se desplaza:
   es el delator más barato de cazar.
5. **Medir el YMIN del fotograma completo y concluir que no lavó.** El mínimo global apenas se mueve
   (21→24) porque los píxeles más oscuros pueden estar lejos del destello. El número útil es la luz
   añadida **por decil**, no el mínimo.
6. **Corregir el contraste después para "recuperar el negro".** Estás peleando contra tu propia capa:
   quítala o redúcela en origen.
7. **Compensar la falta de fuente añadiendo un resplandor.** El `glow` de `267` §5.1 no inventa luz:
   toma la que ya hay en el plano y la derrama. Ese sí vale siempre.

---

## Relacionado

- `56-efectos-que-se-ven-baratos.md` (punto 3) — el porqué, y la excepción del flare filmado.
- `267-particulas-y-elementos-de-luz.md` — modo Pantalla, dosis, y el `glow` que sustituye al flare.
- `432-medir-un-destello.md` — **los cuatro números de un destello (base, pico, anchura, fotogramas).**
  Este módulo mide si el destello *debe existir*; el `432` mide si *ocurrió* y con qué forma.
- `430-el-destello-como-puntuacion.md` · `434-bloom-y-halacion.md` · `435-fugas-de-luz.md`
- `264-tracking-y-seguimiento.md` — anclar una capa a algo que se mueve.
- `63-look-cinematografico.md` · `69-monitoreo-y-scopes.md` — el negro que se te llevó por delante.
- `222-exposicion-y-rango-dinamico.md` — qué significa un píxel saturado.
- `460-el-catalogo-medido.md` — el banco y la trampa del `-loglevel`.

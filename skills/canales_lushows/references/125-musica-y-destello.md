# 125 · Música y destello: el golpe completo

**Qué resuelve:** que el gancho visual del canal pegue. Un fogonazo de luz sin sonido no se
lee como un recurso: se lee como un error de codificación. El golpe completo son **tres
cosas en el mismo fotograma** — luz, impacto sonoro y acento musical.

---

## Las tres capas, y la que casi siempre falta

| Capa | Qué es | Dónde se declara |
|---|---|---|
| **Luz** | Campana de brillo+contraste sobre todo el cuadro | `DESTELLOS` en `guion_visual.py`, la pinta `motor.py` |
| **Impacto** | `tr_flash` — 0,55 s, con su pico en 0,009 s | `PISTAS` en `acabar.py` |
| **Acento musical** | Un acorde del piano en la misma altura del bloque | `PISTAS`, generado con `piano.py` (`123`) |

La tercera es la que se olvida y la que convierte el efecto en un golpe de verdad: sin
acento, luz e impacto suenan a "efecto de plantilla"; con acento, suenan a la banda sonora
del episodio reaccionando.

## La luz: una campana de Gauss, nunca un interruptor

```python
bri = "+".join(f"{f:.3f}*exp(-pow((t-{td:.2f})/{s:.3f}\\,2))" for td, f, s in picos)
con = "+".join(f"{f*1.4:.3f}*exp(-pow((t-{td:.2f})/{s:.3f}\\,2))" for td, f, s in picos)
filtros.append(f"[{ultimo}]eq=brightness='{bri}':contrast='1+{con}':eval=frame[fx]")
```

Rendido, para el destello más fuerte del episodio (`"aprendiz"`, fuerza 0,22, ancho 0,09):

```
eq=brightness='0.220*exp(-pow((t-4.45)/0.090\,2))':contrast='1+0.308*exp(-pow((t-4.45)/0.090\,2))':eval=frame
```

| Parámetro | Valor | Nota |
|---|---|---|
| `fuerza` (brillo) | **0,14 a 0,22** | 0,22 solo en el golpe del gancho |
| contraste | `fuerza × 1,4` | El contraste va SIEMPRE por encima del brillo: si no, el flash lava |
| `ancho` (media anchura) | **0,075 s**, 0,09 en el golpe | La campana cae al 10 % en ±1,517·ancho |
| Duración visible | **±0,114 s ≈ ±3 fotogramas** a 25 fps | Por eso el sonido tiene 6 fotogramas de margen |

🔴 `eq` solo evalúa expresiones con `eval=frame`. Sin eso lee el valor una vez al arrancar
y **el destello no ocurre**, sin error ni aviso.

## El sonido: dónde está su energía, no dónde empieza el archivo

Medido sobre los archivos reales del banco:

| Sonido | Duración | Pico | Regla de anclaje |
|---|---|---|---|
| `tr_flash` | 0,55 s | **0,009 s** | `t − 0,06` → pico a **−51 ms** del fotograma |
| `dr_golpe` | 1,20 s | 0,019 s | `t − 0,10` → pico a −81 ms |
| `dr_impacto` | 2,80 s | 0,010 s | `t − 0,12` → pico a −110 ms |
| `dr_riser` | 2,40 s | **2,373 s** | debería ser `t − 2,37` |

```python
("tr_flash", cuando("broma", 33.06) - 0.06, 0.45, 0.28, False),
("tr_flash", esc("metodo")[0] - 0.25, 0.55, 0.36, False),
```

La tolerancia de sincronía (ITU-R BT.1359): el oído empieza a detectar el audio
**adelantado a partir de +45 ms** y **retrasado a partir de −125 ms**. El margen no es
simétrico: adelantar molesta antes que retrasar. Regla del canal: **entre −40 ms y +80 ms
respecto al fotograma del destello**. Los −51 ms de `tr_flash` están justo en el borde y
funcionan porque el pico de luz también tiene anchura.

## 🔴 Hallazgo: el riser del episodio 01 está decapitado

```python
("dr_riser", cuando("aprendiz", 20.60) - 2.2, 2.3, 0.42, False),
```

El archivo dura 2,40 s y **su cresta está en 2,373 s**. El `atrim=0:2.30` la corta antes de
que llegue, y encima el `afade=t=out:st=1.90:d=0.4` ya venía bajándola. El riser sube y
**nunca llega arriba**: el espectador oye la preparación y no oye el golpe. Arreglo:

```python
("dr_riser", cuando("aprendiz") - 2.37, 2.40, 0.42, False),   # dur = archivo entero
# y para esta pista, r_out corto (0,15) o la cresta se vuelve a comer
```

Mismo problema, más leve, en `tr_whoosh`: su pico está en 0,457 s y se ancla en
`esc_ini − 0.35`, así que el barrido culmina **0,107 s después del corte** en vez de en él.

## El acento musical del golpe

Un acorde de `piano.py` en la altura del bloque, con el mismo desfase que el flash:

```python
import piano
# la tríada del bloque, en el registro alto para que se oiga por encima del colchón
piano.tocar([(0.000, "D3", 2.2, 0.80), (0.014, "A3", 2.0, 0.55),
             (0.028, "F4", 1.8, 0.62)], os.path.join(SON, "ac_golpe.wav"), cola=1.5)

g = cuando("aprendiz")
PISTAS += [
    ("tr_flash",  g - 0.06, 0.55, 0.32, False),   # el impacto
    ("ac_golpe",  g - 0.03, 2.8, 0.26, False),    # el acento: ataque de 8 ms
]
```

Y el acento **debe estar en el modo del bloque**. Un acorde de re menor sobre el colchón de
`sospecha` (que lleva la cuarta aumentada) suena a error de afinación, no a golpe. Si el
bloque es de sospecha, el acento lleva su `Ab`.

## El presupuesto

Uno por bloque como máximo, y **el más fuerte en el golpe del gancho**. En el episodio 01:
cinco destellos en 63 s, fuerzas 0,15 · **0,22** · 0,14 · 0,18 · 0,20. El de `"aprendiz"`
es el único que se lleva el acorde además del impacto.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Fogonazo mudo | Se lee como un error de codificación del vídeo |
| `eq` sin `eval=frame` | El destello no ocurre, y no avisa nadie |
| Contraste igual o menor que el brillo | El flash lava la imagen en vez de golpearla |
| Anclar el sonido por el inicio del archivo | Un riser con la cresta al final llega tarde o se corta |
| `atrim` más corto que la cresta del efecto | El golpe nunca llega arriba (bug real: `dr_riser`) |
| Audio más de 40 ms adelantado | Se percibe la desincronía (ITU-R BT.1359) |
| Acento en un modo que no es el del bloque | Suena a nota equivocada, no a acento |
| Un destello por escena | El recurso se gasta y el golpe del gancho no destaca |

## Relacionado

`74` flash y golpe · `123` anclar a palabra · `84` picos dramáticos · `67` luz y destellos ·
`124` el silencio

# 464 — La partícula flotante: todas del mismo tamaño

**Qué resuelve:** el `267-particulas-y-elementos-de-luz.md` es el módulo de partículas y ahí está casi
todo: para qué sirven de verdad, el modo Pantalla, las dosis de opacidad (polvo 8–20%, humo 15–35%), las
dos capas —delante y detrás— y la prueba del interruptor. **→ léelo. Este módulo no lo repite.**

Lo que `267` enuncia como regla ("las partículas tienen tamaños distintos; todas iguales = falso") es lo
que aquí se mide. Porque es la razón por la que un preset de partículas se reconoce al instante aunque
la opacidad esté bien puesta: **un campo de partículas de preset es monodisperso**, todas del mismo
tamaño, y el mundo real no tiene eso.

---

## 1. Por qué el tamaño delata más que la opacidad

El polvo en el aire está repartido en profundidad. Lo que está a 20 cm del objetivo aparece grande y
desenfocado; lo que está a cinco metros, minúsculo y nítido. **Un campo real es una distribución**, con
muchas partículas pequeñas y unas pocas grandes. Un generador de preset dibuja el mismo sprite N veces.

El ojo no cuenta partículas, pero lee la ausencia de profundidad de inmediato: si todas son iguales, no
hay un delante ni un detrás, y la capa se lee como lo que es, una calcomanía sobre el cristal.

---

## 2. La medición: componentes conexas y energía multiescala

Dos cifras sobre la capa de partículas **aislada** (sobre negro, antes de mezclarla):

```python
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter, label
img = np.asarray(Image.open("particulas.png").convert("L")).astype(np.float32)/255
lab, k = label(img > 0.10)                       # cada mancha, una etiqueta
areas = np.bincount(lab.ravel())[1:]             # su área en píxeles
p10, p90 = np.percentile(areas,10), np.percentile(areas,90)
print(f"{k} manchas  mediana={np.median(areas):.0f}px  razón p90/p10={p90/max(p10,1):.1f}")
e0 = (img**2).sum()                              # energía que sobrevive a cada escala
print("  ".join(f"σ={s}: {(gaussian_filter(img,s)**2).sum()/e0*100:.1f}%" for s in (1,2,4,8)))
```

La **razón p90/p10** dice cuánto se parecen entre sí la partícula grande y la pequeña. La **energía
multiescala** dice en cuántas escalas vive el campo: se difumina progresivamente y se mira cuánta señal
queda. Un campo de un solo tamaño desaparece de golpe al pasar de su escala.

---

## 3. Los números

Dos campos de 900 partículas cada uno sobre 540×960. El primero es el preset: todas de radio 3 y la
misma opacidad. El segundo reparte radios de 1 a 14 px por ley de potencia, con la opacidad ligada al
tamaño (lo grande está cerca y por tanto es más tenue y más borroso):

| Campo | Manchas detectadas | Área mediana | p10 | p90 | **Razón p90/p10** | Energía tras σ=8 |
|---|---|---|---|---|---|---|
| Preset (todas iguales) | 556 | 121 px | 121 | 282 | **2,3×** | **26,6%** |
| Con profundidad | 224 | 61 px | 9 | 2.663 | **295,9×** | **77,0%** |

Dos lecturas:

- **Razón 2,3× frente a 295,9×.** En el preset, la partícula del percentil 90 es apenas el doble que la
  del percentil 10 —y ese doble sale solo de los solapes entre partículas vecinas, no de una decisión—.
  En el campo con profundidad hay dos órdenes de magnitud entre la más chica y la más grande.
- **El campo monodisperso vive en una sola escala.** Al difuminar con σ=8 pierde tres cuartas partes de
  su energía (queda el 26,6%), mientras el campo con profundidad conserva el 77,0% porque parte de sus
  partículas son más grandes que el difuminado. Eso es exactamente lo que hace la compresión de una red
  social con las partículas finas: se las come. Un campo de una sola escala **desaparece entero**; uno
  con profundidad sobrevive a medias, que es lo que quieres (`267`, la prueba de la compresión).

> **Umbral: razón p90/p10 por debajo de 10 y el campo es de preset.** Un campo grabado o construido con
> profundidad está en decenas o centenas.

Honestidad sobre el banco: los dos campos son sintéticos, generados para aislar la variable. Si vas a
usar este umbral con material propio, **mide primero tu polvo grabado** (`267`, §4.1: cuarto oscuro,
linterna de lado y una toalla sacudida) y calibra con ese número.

---

## 4. Qué se hace en su lugar

El sustituto no es "buscar un preset mejor": es **construir tres estratos**, que además es la única
forma de cumplir la regla de `267` de tener capa delante y detrás.

| Estrato | Tamaño | Opacidad | Tratamiento |
|---|---|---|---|
| Lejano (detrás del sujeto) | 1–3 px | 6–10% | nítido, muchas partículas |
| Medio (detrás) | 3–6 px | 10–15% | nítido, deriva lenta |
| Cercano (delante del sujeto) | 8–16 px | 5–8% | **`gblur=sigma=6`**, pocas partículas |

```bash
# el estrato cercano: pocas, grandes, desenfocadas y muy tenues
ffmpeg -y -loglevel error -i con_sujeto.mp4 -i polvo_grande.mp4 -filter_complex "\
[1:v]scale=1080:1920,gblur=sigma=6,colortemperature=temperature=3800:mix=0.7[p];\
[0:v][p]blend=all_mode=screen:all_opacity=0.07:shortest=1" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

Tres capas al 7–12% miden mejor y se ven mejor que una sola al 30%. El resto —modo Pantalla, teñir con
la temperatura de la escena, que se muevan con la cámara— está en `267` y no cambia.

---

## Errores frecuentes

1. **Ajustar la opacidad y dar el problema por resuelto.** La opacidad correcta con tamaño único sigue
   leyéndose como calcomanía. Son dos variables distintas.
2. **Medir la capa ya mezclada con el plano.** Las componentes conexas se miden sobre la capa aislada,
   sobre negro. Mezclada, el detector cuenta manchas del fondo.
3. **Escalar un preset para "variar el tamaño".** Escalar el campo entero mantiene la razón p90/p10
   intacta: sigue siendo monodisperso, solo que más grande.
4. **Duplicar la misma capa tres veces a distintos tamaños.** Mejora la razón, pero el patrón de
   posiciones se repite y el ojo lo caza. Desplaza, refleja y recorta cada copia.
5. **Poner las grandes nítidas.** Lo que está cerca del objetivo está fuera de foco. Sin `gblur` en el
   estrato cercano, la profundidad no aparece.
6. **Olvidar que la red va a recomprimir.** El estrato fino es el primero que muere; súbelo a una cuenta
   de prueba (`267`, §7).
7. **Usar partículas sin motivo en la escena.** Antes que cualquier medición, la pregunta de `267`:
   ¿por qué hay algo flotando en ese aire?

---

## Relacionado

- `267-particulas-y-elementos-de-luz.md` — **el módulo de partículas. Dosis, capas, glow, integración.**
- `56-efectos-que-se-ven-baratos.md` — el marco de por qué un efecto decorativo delata.
- `262-la-tecnica-del-sandwich.md` · `263-integrar-un-elemento.md` — poner una capa detrás del sujeto.
- `428-el-efecto-que-se-rompe-en-la-compresion.md` · `446-ruido-que-sobrevive-a-la-compresion.md` —
  **cuánto del estrato fino llega de verdad al espectador.**
- `93-compresion-sin-perder-calidad.md` — por qué el estrato fino desaparece al subirlo.
- `460-el-catalogo-medido.md` — el banco y las seis magnitudes.

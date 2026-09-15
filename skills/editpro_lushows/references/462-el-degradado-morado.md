# 462 — El degradado morado: cómo se detecta en un fotograma ya montado

**Dónde está la frontera, antes de nada:** el degradado violeta-magenta-azul de toda *startup* de
2018–2021 es territorio de dirección creativa. Quién decide que ese morado está quemado, que no es de
la marca y con qué se sustituye es `directorcreativo_lushows`:
**→ `directorcreativo_lushows/157-gradientes-y-color-generativo.md`** (su sección "Anti-cliché" nombra
exactamente este degradado), y en la misma skill `37-gradientes-y-color-avanzado`,
`33-construir-una-paleta` y `97-tendencias-de-diseno-2026` (la "estética IA genérica" como sello de lo
desechable).

Lo tuyo es otra cosa: **te llega un fotograma ya montado —o un plano generado, o una plantilla que
heredaste— y hay que demostrar que está teñido, cuánto, y arreglarlo en la línea de tiempo.** Eso es
este módulo. Por qué la IA deriva hacia paletas que nadie pidió está en `125-la-ia-no-respeta-la-marca.md`.

---

## 1. La magnitud que no falla: el verde como canal mínimo

Un morado es, por definición, rojo y azul por encima del verde. Si una imagen está teñida de violeta,
**en cada píxel el canal verde es el más bajo de los tres**. En material fotográfico real eso no pasa
casi nunca: la luz del mundo reparte los tres canales según lo que haya delante.

```python
# morado.py — detector sobre UN fotograma ya montado
import sys, numpy as np
from PIL import Image
for p in sys.argv[1:]:
    im = np.asarray(Image.open(p).convert("RGB").resize((270,480))).astype(np.float32)/255
    r,g,b = im[...,0], im[...,1], im[...,2]
    mx, mn = im.max(2), im.min(2)
    v = mx; s = np.where(mx>0,(mx-mn)/np.maximum(mx,1e-6),0)
    d = np.maximum(mx-mn,1e-6)
    h = np.select([mx==r, mx==g], [((g-b)/d)%6, (b-r)/d+2], (r-g)/d+4)*60   # matiz en grados
    util  = (s>0.18)&(v>0.12)                       # píxeles con color de verdad
    banda = util & (h>=255)&(h<=320)                # violeta-magenta
    print(f"{p:22} morado={banda.sum()/max(util.sum(),1)*100:5.1f}%  "
          f"G=mínimo en {(g<=np.minimum(r,b)).mean()*100:5.1f}% de los píxeles")
```

---

## 2. Los números

Cinco imágenes, mismo detector. Tres son fotogramas de archivo reales; una es el degradado de
plantilla (tres manchas radiales violeta / magenta / azul); otra es ese degradado **puesto encima de la
foto real al 35% de opacidad**, que es lo que de verdad hace la gente:

| Imagen | % en banda violeta-magenta | Verde = canal mínimo |
|---|---|---|
| Plano de archivo (pasillo) | 0,1% | **2,4%** |
| Plano de archivo (dinero) | 0,1% | 8,7% |
| Plano de archivo (avión) | 0,7% | 20,4% |
| Degradado de plantilla puro | 59,4% | **100,0%** |
| Foto real + degradado al **35%** | 68,6% | **100,0%** |
| Duotono de marca (azul→crema) | 0,0% | **0,0%** |

Dos cosas que enseña la tabla:

- **A un 35% de opacidad el tinte ya es total.** El porcentaje de banda morada sube por encima del
  degradado puro (68,6% frente a 59,4%, porque la foto aporta saturación) y el verde queda por debajo
  en el **100%** de los píxeles. No hay "un toque de morado": o hay morado o no lo hay.
- **La concentración de matiz no sirve para detectarlo.** Medida aparte, el pasillo real tiene el 93,5%
  de sus píxeles dentro de una sola banda de 60°, más concentrado que el degradado (87,4%). Una foto
  puede ser monocroma sin ser de plantilla. El discriminante es *cuál* es la banda y qué canal manda.

---

## 3. El umbral

> **Verde como canal mínimo en más del 80% de los píxeles, con más del 30% en la banda 255°–320°: la
> imagen está teñida de violeta por decisión de alguien que no eras tú.** Por debajo del 25% de "G
> mínimo", el matiz es del material.

Ojo con el falso positivo legítimo: **una marca cuyo color de verdad es violeta** da exactamente los
mismos números, y ahí el detector no dice "barato", dice "es coherente". Quién decide cuál de las dos
cosas es, ya está dicho arriba: `directorcreativo`.

---

## 4. Qué se hace en la edición

No se "quita el morado" bajando saturación: eso deja una imagen gris y sucia. Se **sustituye el mapa de
color** por uno que sí sale de la marca.

```bash
# Duotono de marca a partir de la luminancia: cada extremo a un color del sistema.
ffmpeg -y -loglevel error -i plano.mp4 -vf "format=gray,\
curves=r='0/0.04 0.5/0.30 1/0.96':g='0/0.09 0.5/0.35 1/0.94':b='0/0.22 0.5/0.52 1/0.90'" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p duotono.mp4
```

Medido con el mismo detector, ese duotono da **0,0% de banda morada y 0,0% de verde mínimo**: el tinte
desapareció y la imagen sigue siendo de un solo color, el de la marca. Los tres juegos de `curves` son
los tres colores del sistema: el punto `0/` es la sombra, el `1/` es la luz.

Las otras dos vías, según el caso:

- **Matar solo el intruso** cuando el resto del plano está bien — la receta está en `125`, sección
  "Solo matar el color intruso".
- **LUT de marca** aplicada al corte terminado, que es lo que garantiza consistencia entre planos:
  `64-forzar-la-paleta-de-marca.md` y `65-luts.md`.

Y una regla de orden: **el duotono va sobre el corte terminado, no sobre cada clip.** Si cada clip lleva
el suyo, la referencia cambia en cada corte (`62-emparejar-planos.md`).

---

## Errores frecuentes

1. **Tratar esto como una discusión de gusto.** La pregunta "¿este morado es de la marca?" no es tuya.
   Mide, enseña el número y rutéalo a `directorcreativo`.
2. **Bajar la saturación para quitar el tinte.** Quita el color, no el mapa: queda una imagen apagada
   con el mismo sesgo.
3. **Medir el matiz medio del fotograma.** Una imagen mitad naranja y mitad azul promedia gris y el
   número no dice nada. Se mide la *distribución*, no la media.
4. **Usar la concentración de matiz como prueba.** Una foto real puede estar más concentrada que el
   degradado: la tabla lo demuestra.
5. **Creer que al 30–35% de opacidad "apenas se nota".** Medido: al 35% el verde ya es el canal mínimo
   en el 100% de los píxeles.
6. **Aplicar el duotono clip a clip.** Va sobre el corte, después del emparejado.
7. **Pedirle a la IA que respete la paleta y dar por bueno el resultado sin medirlo.** `125` es
   explícito: la corrección en post es la única garantía. Este módulo te da la verificación.

---

## Relacionado

- `directorcreativo_lushows/157-gradientes-y-color-generativo.md` — **el criterio. Empieza ahí.**
- `directorcreativo_lushows/37-gradientes-y-color-avanzado.md` y su `33-construir-una-paleta.md`
- `directorcreativo_lushows/97-tendencias-de-diseno-2026.md` — la "estética IA genérica".
- `125-la-ia-no-respeta-la-marca.md` — por qué deriva y las tres formas de imponer la paleta.
- `64-forzar-la-paleta-de-marca.md` · `65-luts.md` · `62-emparejar-planos.md`
- `447-la-textura-que-delata-a-la-ia.md` (§4) — el **otro** delator de color, la dispersión de tono:
  métrica distinta y complementaria a esta; no la repitas, úsala junto con ella.
- `468-el-filtro-global.md` — por qué un tinte único encima de todo no empareja nada.

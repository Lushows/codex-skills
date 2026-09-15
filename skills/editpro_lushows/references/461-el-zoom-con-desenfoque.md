# 461 — El zoom con desenfoque: cuántos fotogramas de papilla cuesta

**Qué resuelve:** el `56` abre su lista negra con el zoom borroso y da la razón —es el preset de todas
las apps, dura demasiado, no comunica nada y va mudo—. **→ ver `56`, punto 1, para el porqué.** Aquí se
mide: cuántos fotogramas del video dejan de ser imagen y pasan a ser puré, y cuál es el número por
encima del cual el espectador lo ve.

---

## 1. La magnitud: nitidez por fotograma

Un desenfoque es, literalmente, **quitarle alta frecuencia a la imagen**. Eso se mide con el
laplaciano: un operador que responde a los cambios bruscos entre píxeles vecinos. Su desviación típica
es una cifra por fotograma que sube con el detalle y se desploma con el desenfoque.

```python
# nitidez.py — nitidez por fotograma (desviación típica del laplaciano)
import subprocess, numpy as np, sys
def leer(path, w=270, h=480):                      # 1/4 de resolución: corre en un PC viejo
    p = subprocess.run(["ffmpeg","-v","error","-i",path,"-vf",f"scale={w}:{h}",
                        "-f","rawvideo","-pix_fmt","gray","-"], capture_output=True)
    a = np.frombuffer(p.stdout, dtype=np.uint8); n = len(a)//(w*h)
    return a[:n*w*h].reshape(n,h,w).astype(np.float32)
def lap(f):
    return (4*f[1:-1,1:-1]-f[:-2,1:-1]-f[2:,1:-1]-f[1:-1,:-2]-f[1:-1,2:]).std()
for path in sys.argv[1:]:
    s = np.array([lap(f) for f in leer(path)]); base = np.median(s)
    malos = int((s < 0.85*base).sum())
    print(f"{path}: base={base:.2f}  bajo el 85%: {malos} fotogramas "
          f"({malos/30:.2f} s)  mínimo={s.min()/base*100:.0f}%")
```

No hace falta abrir el video. Devuelve una serie de números y la serie cuenta la historia entera.

---

## 2. Las tres versiones, medidas

Mismo par de planos, mismo corte en el segundo 1,0, 30 fps, banco a 540×960 (ver `460`):

```bash
# a) corte duro
ffmpeg -y -loglevel error -i A.mp4 -i B.mp4 \
  -filter_complex "[0:v][1:v]xfade=transition=fade:duration=0.034:offset=1.0" \
  -r 30 -c:v libx264 -crf 14 -pix_fmt yuv420p corte.mp4

# b) el preset: zoom con desenfoque de medio segundo
ffmpeg -y -loglevel error -i A.mp4 -i B.mp4 \
  -filter_complex "[0:v][1:v]xfade=transition=zoomin:duration=0.5:offset=1.0" \
  -r 30 -c:v libx264 -crf 14 -pix_fmt yuv420p preset.mp4

# c) el golpe de escala de 3 fotogramas sobre el corte duro
ffmpeg -y -loglevel error -i corte.mp4 \
  -vf "scale=w='540*if(between(t,1.0,1.1),1.18-(t-1.0)*1.8,1)':h=-2:eval=frame,crop=540:960" \
  -r 30 -c:v libx264 -crf 14 -pix_fmt yuv420p golpe.mp4
```

| Versión | Fotogramas bajo el 85% de la base | Mínimo alcanzado | Duración del "hueco" |
|---|---|---|---|
| Corte duro | **0** | 99% | 0 fotogramas |
| Golpe de escala, 3 f | **0** | **91%** | 1 fotograma al 91% |
| `xfade=zoomin`, 0,5 s | **10** | **3%** | 0,33 s |

La serie del preset, fotograma a fotograma, es la prueba:

```
34: 16,7   35: 10,8   36: 3,0   37: 1,1   38: 0,6   39: 2,4   40: 5,7   41: 9,8   42: 14,0   43: 17,8
```

Frente a una base de 21,7. Durante **cuatro fotogramas seguidos la imagen conserva menos del 15% de su
detalle** (13,8% · 5,1% · 2,8% · 11,1%), y en el peor —el 38— queda en el **2,8%**. Medio segundo a 30
fps son 15 fotogramas: el preset se come 14 y 10 de ellos son inservibles.

---

## 3. El umbral

> **Más de 2 fotogramas por debajo del 70% de la nitidez base y el espectador lo ve como un borrón, no
> como una transición.** Entre 1 y 2 fotogramas se lee como impacto. Cero, como corte.

Ese es el número que separa el golpe de `53` del preset. No es el filtro: es **cuántos fotogramas
dejaste sin imagen**. El mismo `zoomin` con `duration=0.1` da 3 fotogramas y deja de delatar.

Y el segundo número, el de coste: **la transición del preset ocupa 14 de los 75 fotogramas del clip de
prueba** —0,47 s, el 18,7% del tiempo en pantalla— y 10 de esos 14 no muestran nada legible. En un reel
de 20 segundos con ocho cortes así son **2,6 segundos de papilla**. Ver `28-duracion-optima.md` y
`321-cadencia-mediana-y-varianza.md`.

---

## 4. Qué se hace en su lugar

1. **El golpe de escala de `53`**: 12–25% de aumento, 3 fotogramas, con impacto de audio. Medido arriba:
   mínimo 91%, cero fotogramas rotos. Es el mismo gesto sin el coste.
2. **Cortar sobre movimiento** (`54-transiciones-por-movimiento.md`): si el plano A termina con un
   barrido y el B empieza con otro, el propio material tapa el corte y no hay nada que desenfocar.
3. **Si de verdad quieres el borrón, que sea un `whip`** de 2–3 fotogramas con sonido (`53`, `76`).
4. **Y si el efecto tiene que estar, aplícalo al rótulo y no al cuadro.** Esa es la palanca de
   rehabilitación del `469`, con números.

Una nota honesta: **el desenfoque no es el problema, la duración lo es.** El desenfoque de movimiento
real de una cámara que hace un barrido rápido deja fotogramas igual de rotos, y nadie lo lee como
barato, porque dura 2 fotogramas y viene de la física del plano.

---

## Errores frecuentes

1. **Cambiar `zoomin` por otro preset de la lista de `xfade`** y dejar `duration=0.5`. La medida sale
   igual de mal: el problema es el medio segundo, no el nombre del efecto.
2. **Medir sobre el archivo ya exportado para Instagram.** La compresión ya destruyó alta frecuencia y
   la base de nitidez baja: mides el codificador (`460`, §3).
3. **Usar la nitidez media del clip como base cuando hay un rótulo que entra.** El texto añade alta
   frecuencia y sube la mediana. Compara contra el fotograma inmediatamente anterior, no contra la
   mediana. Esto se ve claro en `469`.
4. **Poner el golpe en cada corte.** Tres fotogramas rotos ocho veces también suman. Uno o dos por
   video.
5. **Dejarlo mudo.** Un hueco de nitidez sin evento de audio es la definición de efecto pegado (`76`).
6. **Animar la escala sin `eval=frame`.** El filtro se evalúa una sola vez y no pasa nada; `84` lo
   advierte y sigue siendo el fallo más común de este comando.
7. **Aplicar el golpe con `scale` sobre 1080×1920 en un ordenador viejo.** Es lentísimo: prueba con
   `-t 0.4` antes de lanzar el render completo.

---

## Relacionado

- `56-efectos-que-se-ven-baratos.md` (punto 1) — **el porqué. Léelo primero.**
- `53-whip-flash-y-golpe.md` — el sustituto, con sus dosis.
- `54-transiciones-por-movimiento.md` — tapar el corte con el propio material.
- `107-ffmpeg-transiciones-xfade.md` — el catálogo completo de `xfade` y sus parámetros.
- `420-un-efecto-es-una-hipotesis.md` · `422-coste-en-render-y-en-atencion.md` — el arnés y su factura.
- `460-el-catalogo-medido.md` — el banco de pruebas y la trampa del `-loglevel`.
- `469-rehabilitar-un-efecto-quemado.md` — este mismo efecto, rescatado con números.

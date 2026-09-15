# 155 · Cachés que sirven el archivo equivocado

**Qué resuelve:** una caché con **clave incompleta** devuelve el archivo de otro. En
pantalla sale la imagen que no es, y no hay un solo error.

---

## Cómo se manifiesta

La caché de PNG escalados se nombraba con el **nombre del fichero**:
`destino = os.path.join(carp, f"{objetivo}_{os.path.basename(ruta)}")`.

`ficha_policial.png` existe en dos carpetas del banco: `fx/` (la ficha dibujada) y
`recortes/` (la ficha real del expediente). Las dos producían la misma clave
`600_ficha_policial.png`; la primera que se escalara ganaba y **la segunda reutilizaba
el PNG de la primera**. En el plano donde debía verse el documento real se veía el
dibujo. Render correcto, ffmpeg contento, auditoría limpia, **imagen equivocada en
pantalla**.

Es el fallo más difícil de ver del bloque, porque el resultado *parece* bien: hay una
ficha policial en el plano de la ficha policial.

## Por qué ocurre

La caché existe por una razón medida: ffmpeg **reescala cada elemento en cada
fotograma**. Con recortes de archivo de 3.000-8.000 px mostrados a 600, eso son
cuatrocientas reducciones idénticas por elemento; una escena de 16 s con 14 elementos
tardaba **7 minutos** en un i7 de 2009. Prerreducir cada PNG una sola vez a 1,4× su
tamaño en pantalla vuelve trivial el trabajo por fotograma.

El error no está en cachear: está en la **clave**. Una clave tiene que contener *todo*
lo que determina el contenido. Aquí estaban el ancho objetivo y el nombre del fichero,
y faltaban los dos que importaban: **la carpeta de origen** y **la versión del fichero
(`mtime`)**.

Y la resolución de nombres del canal **invita** a la colisión: `motor.buscar()` recorre
`PROPIAS + texto/ fx/ recortes/ recursos/ render/ archivo/` y devuelve el primero que
exista. Los basenames repetidos entre carpetas no son un accidente, son el diseño: el
episodio puede tener su propio `f_muerte` que gana al del banco común.

## Cómo se caza

Buscar los basenames que se repiten entre carpetas. Son los candidatos exactos:

```python
import collections, os
vistos = collections.defaultdict(list)
for c in ("texto", "fx", "recortes", "recursos", "render", "archivo"):
    d = os.path.join(BASE, c)
    if os.path.isdir(d):
        for f in os.listdir(d):
            vistos[os.path.splitext(f)[0]].append(c)
for alias, carps in sorted(vistos.items()):
    if len(carps) > 1:
        print(f"  COLISIÓN  {alias:<26} en {', '.join(carps)}")
```

```
  COLISIÓN  ficha_policial             en fx, recortes
```

Y la confirmación que zanja la discusión: borrar la caché y volver a renderizar. **Si
la imagen cambia, la caché estaba mintiendo.**

```bash
rm -rf salida/_escalados && python motor.py ep01-lustig
```

## La guardia automática

La clave se construye con un **hash de la ruta absoluta**, no con el nombre. Es lo que
hoy hace `motor.escalado()`:

```python
def escalado(ruta, ancho):
    clave = (ruta, ancho)                     # la clave en memoria: ruta COMPLETA
    if clave in _ESCALADOS:
        return _ESCALADOS[clave]
    destino = ruta
    try:
        from PIL import Image
        im = Image.open(ruta)
        objetivo = int(ancho * 1.4)           # margen para rotación y deriva
        if im.width > objetivo * 1.15:
            carp = os.path.join(DIRS["salida"], "_escalados")
            os.makedirs(carp, exist_ok=True)
            # OJO: la caché se nombra con un HASH DE LA RUTA COMPLETA, no con el
            # nombre del fichero. Hay basenames repetidos entre carpetas
            # ('ficha_policial.png' vive en fx/ y en recortes/) y cachear por
            # basename hacía que el segundo reutilizara el PNG del primero:
            # imagen equivocada en pantalla y ni un solo error.
            base = re.sub(r"[^\w]+", "_", os.path.basename(ruta))
            sello = hashlib.md5(os.path.abspath(ruta).encode()).hexdigest()[:8]
            destino = os.path.join(carp, f"{objetivo}_{sello}_{base}.png")
            if not os.path.exists(destino):
                alto = max(1, int(im.height * objetivo / im.width))
                im.convert("RGBA").resize((objetivo, alto), Image.LANCZOS).save(destino)
    except Exception:
        destino = ruta                        # ante la duda, el original
    _ESCALADOS[clave] = destino
    return destino
```

Tres decisiones que merecen nombre: **el nombre legible se conserva**
(`600_a3f81c02_ficha_policial.png`), porque el hash evita la colisión y el basename
permite auditar la carpeta a ojo; **la caché vive en `salida/`**, que es por episodio,
así que uno no contamina a otro; y **ante cualquier excepción se devuelve el
original**, porque la caché es una optimización — si falla, el render tarda más, no
sale mal.

⚠️ **Falta un factor:** el `mtime` del origen. Si se reedita `ficha_policial.png` sin
cambiarle el nombre, la caché sirve la versión vieja. La forma completa es
`md5(ruta_absoluta + str(os.path.getmtime(ruta)))`; mientras no esté, la regla es
**borrar `_escalados` después de tocar cualquier PNG del banco**.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Cachear por nombre de fichero | Dos carpetas, un PNG: imagen equivocada, cero errores |
| Clave sin el ancho objetivo o sin `mtime` | Se sirve el tamaño de otro plano, o la versión vieja |
| Caché compartida entre episodios | El episodio 02 hereda los escalados del 01 |
| No devolver el original ante excepción | Un PNG raro tumba el render entero |
| Renombrar recursos para «evitar colisiones» | Se pierde la prioridad episodio-sobre-banco, que es el diseño |

## Relacionado

`150` el catálogo del fallo silencioso · `192` alias estables y colisiones ·
`199` el manifiesto del material · `156` recursos que no existen · `59` biblioteca de
fondos · `98` episodios largos

# 248 · Pre-escalado y caché

**Qué resuelve:** ffmpeg **reescala cada elemento en cada fotograma**. Prerreducir cada
PNG una sola vez convierte ese trabajo en trivial — y abre la puerta al fallo más difícil
de ver del motor: una caché que sirve el archivo de otro.

---

## La función

```python
def escalado(ruta, ancho):
    clave = (ruta, ancho)
    if clave in _ESCALADOS:
        return _ESCALADOS[clave]
    destino = ruta
    try:
        from PIL import Image
        im = Image.open(ruta)
        objetivo = int(ancho * 1.4)
        if im.width > objetivo * 1.15:            # solo si de verdad sobra tamano
            carp = os.path.join(DIRS["salida"], "_escalados")
            os.makedirs(carp, exist_ok=True)
            base = re.sub(r"[^\w]+", "_", os.path.basename(ruta))
            sello = hashlib.md5(os.path.abspath(ruta).encode()).hexdigest()[:8]
            destino = os.path.join(carp, f"{objetivo}_{sello}_{base}.png")
            if not os.path.exists(destino):
                alto = max(1, int(im.height * objetivo / im.width))
                im.convert("RGBA").resize((objetivo, alto), Image.LANCZOS).save(destino)
    except Exception:
        destino = ruta                            # ante la duda, el original
    _ESCALADOS[clave] = destino
    return destino
```

El **1,4×** es margen para la rotación y la deriva: un recorte girado 2,4° ocupa más
ancho del que declara, y si se prerreduce justo al tamaño de pantalla el escalado final
lo amplía y se ve blando. El **1,15** de la condición evita trabajo inútil: si el origen
apenas es mayor que el objetivo no se toca.

El nombre conserva el basename legible junto al hash, para poder auditar la carpeta a
ojo; y la caché vive en `salida/`, que es **por episodio**, así que el 02 no hereda los
escalados del 01.

## El hash es de la RUTA, no del nombre

`ficha_policial.png` puede vivir en `fx/` (la ficha dibujada) y en `recortes/` (la ficha
real del expediente). Cacheando por basename las dos producían la misma clave y la
segunda reutilizaba el PNG de la primera: en el plano del documento real se veía el
dibujo, con ffmpeg contento y auditoría limpia (`155`).

No es un caso de laboratorio: contando basenames repetidos entre carpetas, el banco
actual tiene **30 colisiones de 382 alias**. Treinta alias que existen en dos sitios,
casi todos entre `recortes/` y `archivo/`, que
es el par natural: el recorte con alfa y el original del que salió. Y la resolución de
nombres **invita** a la colisión: `buscar()` recorre las carpetas del episodio primero y
el banco después, precisamente para que el episodio pueda tener su propio `f_muerte` que
gane al del banco común. Los basenames repetidos no son un accidente: son el diseño.

## Falta el `mtime`

La clave contiene la ruta y el ancho. No contiene la **versión del fichero**. Si se
reedita un PNG sin cambiarle el nombre, la caché sirve la versión vieja. Reproducido con
una imagen de prueba:

```
1) origen ROJO
   cache -> 700_f07818c8__prueba_mtime_png.png · color (255, 0, 0)
2) el mismo fichero, reeditado a AZUL
   cache -> 700_f07818c8__prueba_mtime_png.png · color (255, 0, 0)
```

Se reeditó el origen y el render sigue usando el rojo. La forma completa, verificada:

```python
sello = hashlib.md5(("%s|%s" % (os.path.abspath(ruta),
                                os.path.getmtime(ruta))).encode()).hexdigest()[:8]
```

```
CON mtime en la clave:
   cache -> 700_897ae8d6__prueba_mtime_png.png · color (255, 0, 0)
   cache -> 700_b4887b49__prueba_mtime_png.png · color (0, 0, 255)
```

Mientras no esté puesto, la regla es **borrar `_escalados` después de tocar cualquier
PNG del banco**: `rm -rf ep01-lustig/salida/_escalados`. Y es también la prueba que
zanja la discusión sobre si la caché miente: si al borrarla la imagen cambia, mentía.

## Cuánto ahorra de verdad

Aquí hay una sorpresa que conviene tener escrita. Medido sobre el bloque `oficio`
(6,73 s, 7 elementos), en un i7 de 2009:

| | Tiempo |
|---|---|
| con pre-escalado | 89,6 s |
| sin pre-escalado (rutas originales) | 86,2 s |
| solo el fondo, sin ningún elemento | **39,7 s** |

**La caché no ahorra nada en este episodio**, y las dos razones están medidas. La
primera: el material ya viene cortado a medida. El ratio origen/pantalla de los 61
elementos tiene **mediana 2,07 y máximo 3,7** — nada que ver con los recortes de archivo
de 3.000-8.000 px mostrados a 600 para los que se escribió la función, donde la relación
era de 10× o 20× y una escena de 16 s con 14 elementos tardaba siete minutos.

La segunda: casi la mitad del coste de la escena es **el fondo**, que se escala a 4320 px
y pasa por `zoompan` en cada fotograma. Optimizar los elementos cuando el cuello de
botella es el fondo no mueve la aguja.

La caché sigue puesta y sigue siendo correcta —cuesta 56 MB y 52 ficheros en este
episodio— pero **el presupuesto de render de este canal ya no se gana ahí** (`232`). El
siguiente sitio donde mirar es el `scale=4320` del fondo.

Y el `except Exception: destino = ruta` del final no es descuido: la caché es una
optimización, así que si falla —un PNG con perfil raro, un fichero a medio escribir,
Pillow ausente— el render tarda más, no sale mal.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Cachear por nombre de fichero | Dos carpetas, un PNG: imagen equivocada y cero errores |
| Clave sin el ancho objetivo | Se sirve el tamaño pensado para otro plano |
| Clave sin `mtime` | Se reedita el origen y el render usa la versión vieja |
| Caché compartida entre episodios | El episodio 02 hereda los escalados del 01 |
| Prerreducir justo al tamaño de pantalla | La rotación amplía y el recorte se ve blando |
| No devolver el original ante excepción | Un PNG raro tumba el render entero |
| Optimizar los elementos sin medir el fondo | Se afina lo barato e intacto queda el 44 % caro |

## Relacionado

`155` cachés que sirven el archivo equivocado · `192` alias estables ·
`232` presupuesto de render · `241` resolución de anclas · `199` el manifiesto del
material · `238` render por lotes y reanudar

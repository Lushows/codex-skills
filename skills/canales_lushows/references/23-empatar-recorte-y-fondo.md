# 23 · Empatar recorte y fondo

**Qué resuelve:** el recorte está bien y el fondo está bien, pero juntos se ven mal. La
causa siempre es una de cuatro: luz del lado contrario, cámara a otra altura, grano que
no coincide o temperatura que no coincide. Tres se arreglan; una no.

---

## Las cuatro comprobaciones, con su umbral

| Eje | Cómo se mide | Empata si | Arreglo |
|---|---|---|---|
| **Dirección de la luz** | Δ luminancia mitad izq − mitad der | mismo signo que el fondo, `|Δ| ≤ 6` | Espejo o re-iluminación |
| **Temperatura** | cociente R/B de la zona opaca | `abs(temp_e/temp_f − 1) ≤ 0,12` | `colorbalance` al 65% |
| **Grano** | energía de alta frecuencia | `grano_e ≥ 0,55 × grano_f` | Añadir ruido al más limpio |
| **Ángulo de cámara** | altura del horizonte | a ojo, no hay número fiable | **No tiene arreglo** |

## Medirlo

```python
from PIL import Image, ImageChops, ImageFilter, ImageStat

def _lum(t):  return (0.2126*t[0] + 0.7152*t[1] + 0.0722*t[2]) / 255 * 100

def perfil(png):
    """Perfil fotografico de la zona OPACA de un PNG (o de un fondo entero)."""
    im, rgb = Image.open(png).convert("RGBA"), Image.open(png).convert("RGB")
    m = im.split()[3].point(lambda v: 255 if v > 128 else 0)
    if m.getextrema()[1] == 0: raise ValueError(f"{png}: alfa vacio")
    w, h = im.size
    def med(box):                       # None si esa mitad no tiene recorte
        mk = m.crop(box)
        return ImageStat.Stat(rgb.crop(box), mk).mean if mk.getextrema()[1] else None
    R, G, B = ImageStat.Stat(rgb, m).mean
    izq, der = med((0, 0, w//2, h)), med((w//2, 0, w, h))
    hf = ImageChops.difference(rgb, rgb.filter(ImageFilter.GaussianBlur(1.4)))
    return {"L": _lum((R, G, B)), "temp": R / max(1.0, B),
            "lat": (_lum(izq) - _lum(der)) if izq and der else 0.0,  # >0 luz por la izq
            "grano": sum(ImageStat.Stat(hf, m).mean) / 3}
```

Del fondo se mide **la zona donde va a caer el recorte** — `Image.open(fondo).crop(caja)`
— no la lámina entera: llevan viñeta y el borde puede estar 25 L bajo el centro.

## Arreglo 1 · Luz del lado contrario

**Opción A — espejo.** Barata y perfecta, pero solo si en la foto no hay texto, ni
insignia, ni ninguna asimetría identificable. Cambiar el lado de la raya del pelo es
aceptable; poner un letrero al revés es un error factual.
`ImageOps.mirror(img)` en PIL · `hflip` en ffmpeg.

**Opción B — re-iluminar con degradado.** Levanta un lado y baja el otro sin tocar la
opacidad:

```python
from PIL import Image, ImageEnhance, ImageOps

def reiluminar(png, salida, desde="izq", fuerza=0.22):
    im = Image.open(png).convert("RGBA")
    w, h = im.size
    # linear_gradient es vertical (0 arriba); ROTATE_90 lo pone horizontal: 0 a la izq
    g = Image.linear_gradient("L").transpose(Image.ROTATE_90).resize((w, h))
    if desde == "izq":
        g = ImageOps.mirror(g)            # 255 a la izquierda: ese lado se aclara
    rgb = im.convert("RGB")
    claro  = ImageEnhance.Brightness(rgb).enhance(1 + fuerza)
    oscuro = ImageEnhance.Brightness(rgb).enhance(1 - fuerza)
    Image.merge("RGBA", (*Image.composite(claro, oscuro, g).split(),
                         im.split()[3])).save(salida)
```

`fuerza` entre **0,16 y 0,28**. Por encima de 0,35 aplana la foto y se ve el degradado.

## Arreglo 2 · Temperatura

Se acerca al fondo **al 65%, nunca del todo**: al 100% muere el material y el episodio
entero queda del mismo marrón. El factor sale del cociente de temperaturas:

```python
k = (perfil(fondo)["temp"] / perfil(recorte)["temp"]) ** 0.65   # >1 = calentar
r = r.point(lambda v: min(255, int(v * k ** 0.5)))              # canal R
b = b.point(lambda v: min(255, int(v / k ** 0.5)))              # canal B
```

En ffmpeg: `colorbalance=rm=0.06:bm=-0.05` (rango −0,3 a 0,3; por encima de 0,10 se ve).

## Arreglo 3 · Grano

`revista.py` ya siembra grano (118-138, alfa 26) en todo lo que pasa por él. Si un
recorte sigue demasiado limpio contra un fondo texturado: `noise=alls=11:allf=t+u` en
ffmpeg, o esa misma capa de ruido en PIL con `alfa=34`. Nunca al revés: **no se
desenfoca el fondo para igualar un recorte limpio**.

## El caso sin arreglo · el ángulo de cámara

Un soldado fotografiado a la altura del pecho no encaja en un pasillo con el horizonte
alto. La perspectiva no se inventa con un filtro. **Dos salidas, y solo dos:**

1. **Descartar.** Es lo normal: si no empata, no se usa.
2. **Ascenderlo a DOCUMENTO.** Deja de fingir que está dentro de la escena y pasa a ser
   un papel pegado encima: tijera con margen grueso (`tijera.py`, `borde=18-20`), sombra
   larga, 3° de inclinación y rótulo con la fuente. Un documento pinchado en un tablero
   no empata la perspectiva con nada. Rescata casi todo el material que fallaría por ángulo.

## Auditar antes de montar

Sobre **gris medio**, nunca sobre negro: los halos se disimulan en oscuro y saltan en gris.

```bash
ffmpeg -f lavfi -i color=c=0x808080:s=1400x900 -i recortes/chapo_us.png \
  -filter_complex "[0][1]overlay=(W-w)/2:(H-h)/2" -frames:v 1 -y _audit.png
```

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Medir el fondo entero en vez de la zona | La viñeta falsea el contraste 20-25 L |
| Cuadrar la temperatura al 100% | El episodio entero queda del mismo marrón |
| Espejar una foto con texto o insignia | Error factual visible |
| Desenfocar el fondo para igualar un recorte limpio | Se pierde el fondo por salvar un elemento |
| Forzar un recorte con el ángulo equivocado | Se lee como error de montaje |
| Auditar sobre negro | Los halos aparecen en el render final |
| `ImageStat` sobre máscara vacía | `ZeroDivisionError`: guardar con `getextrema()` |

## Relacionado

`22` profundidad por capas · `25` el borde de papel · `66` grano y textura ·
`51` paleta por escena · `53` luz y viñeta

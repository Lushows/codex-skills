# 161 · Auditar sobre gris, nunca sobre negro

**Qué resuelve:** los halos y las figuras semitransparentes **se disimulan sobre negro**.
Los visores de imágenes, el fondo del explorador y los fondos del canal son oscuros, así
que un recorte sucio pasa la revisión y aparece en el vídeo rodeado de un contorno
fantasma. Sobre gris medio (128) salta a la primera.

---

## Por qué el negro miente

Un recorte con el alfa mal limpiado no tiene un borde: tiene un **degradado** de píxeles
semitransparentes heredados del fondo original de la foto, que casi siempre es claro.

| Fondo de revisión | Qué le pasa al degradado |
|---|---|
| Negro | El píxel semitransparente se mezcla con negro → se oscurece → **desaparece** |
| Blanco | Se aclara y también desaparece, si el fondo original era claro |
| **Gris 128** | Ni sube ni baja: queda a media altura y **se ve entero** |

Gris 128 es el único valor que no favorece a ninguna procedencia — el mismo motivo por el
que los laboratorios de color usan gris neutro y no negro.

## La medida: cuánto borde blando tiene cada recorte

El ojo confirma, pero primero se mide. Un halo es **superficie semitransparente
desproporcionada respecto a la superficie opaca**:

```python
#!/usr/bin/env python3
"""halos.py <carpeta_de_recortes> - ordena los recortes por riesgo de halo."""
import os, sys, numpy as np
from PIL import Image

LIMITE = 0.12      # borde blando / superficie opaca

def medir(ruta):
    a = np.asarray(Image.open(ruta).convert("RGBA"))[:, :, 3]
    blando, opaco = float(((a > 12) & (a < 243)).sum()), float((a >= 243).sum())
    if opaco / a.size < 0.005: return None   # PNG casi vacio: ese es otro problema
    return blando / opaco, blando / a.size * 100

def main(carp):
    filas = []
    for fn in sorted(os.listdir(carp)):
        if not fn.lower().endswith(".png"): continue
        m = medir(os.path.join(carp, fn))
        if m: filas.append((m[0], m[1], fn))
    filas.sort(reverse=True)
    print(f"{'ratio':>7}{'%blando':>9}  archivo")
    for r, p, fn in filas:
        print(f"{r:7.2f}{p:9.2f}  {fn}{'   <-- HALO' if r > LIMITE else ''}")
    v = [f[0] for f in filas]
    print(f"\nn={len(filas)}  mediana={np.median(v):.2f}  "
          f"sobre el limite: {sum(1 for x in v if x > LIMITE)}")

main(sys.argv[1])
```

**Medido de verdad, sobre las dos carpetas del piloto:**

| Carpeta | n | ratio mediana | máximo | por encima de 0,12 |
|---|---|---|---|---|
| `ep01-lustig/recortes` (tijera + silueta limpia) | 69 | **0,01** | 0,10 `torre_postal` | **0** |
| `piloto/recortes` (banco antiguo, rembg sin limpiar) | 62 | 0,01 | **0,82** `_descartado_avion` | **5** |

Los cinco del banco antiguo: `_descartado_avion` 0,82 · `helicoptero` 0,72 ·
`_r_chapo_us` 0,55 · `uniforme` 0,26 · `cara_ovalo` 0,25 — y `chapo_perfil` justo en el
límite, 0,12. **El helicóptero tiene más borde blando que cuerpo opaco**: en el vídeo es
una nube gris con forma de rotor. Los de tijera se quedan en 0,02: el polígono es duro.
Los tres que rozan 0,06-0,10 (`torre_postal`, `torre_hoy`, `torre_construccion`) son
siluetas de rembg **ya limpiadas** (umbral 150/205 + erosión 5 px): ése es el suelo real
de una silueta.

## La hoja de contactos sobre gris

Paso obligatorio **después de recortar y antes de escribir el guion visual**: si un
recorte está sucio, se descarta o se rehace ahora, no cuando ya está renderizado.

```python
#!/usr/bin/env python3
"""contactos.py <carpeta> [salida.png] - todos los recortes sobre gris 128."""
import math, os, sys
from PIL import Image

GRIS, CELDA, COL, MARGEN = (128, 128, 128), 300, 8, 6

def main(carp, dest="_contactos.png"):
    fich = [f for f in sorted(os.listdir(carp)) if f.lower().endswith(".png")]
    hoja = Image.new("RGB", (COL*CELDA, math.ceil(len(fich)/COL)*CELDA), GRIS)
    for i, fn in enumerate(fich):
        im = Image.open(os.path.join(carp, fn)).convert("RGBA")
        k = (CELDA - 2*MARGEN) / max(im.size)
        im = im.resize((max(1,int(im.width*k)), max(1,int(im.height*k))), Image.LANCZOS)
        hoja.paste(im, ((i % COL)*CELDA + (CELDA-im.width)//2,
                        (i // COL)*CELDA + (CELDA-im.height)//2), im)   # mascara = alfa
    hoja.save(dest)
    print(f"{len(fich)} recortes -> {dest}  {hoja.size[0]}x{hoja.size[1]}")

main(*sys.argv[1:])
```

Pasada sobre las 62 piezas del banco común, la hoja delata a la primera lo que el
medidor había ordenado: el retrato recortado en óvalo sale con una aureola gruesa y la
foto de grupo **se ve traslúcida** —el gris se lee a través de la ropa—. Y aparecen dos
cosas que ningún número mira: piezas con **barras negras de letterbox** incrustadas del
JPG original, y un PNG que es la captura de otra hoja de contactos, colado en el banco
como si fuera material.

**Qué se busca, en este orden:**

1. **Aureola** alrededor de la figura: alfa sin limpiar. Se rehace con umbral 150/205 y
   erosión de 5 px, o se pasa a recorte de tijera.
2. **Figura fantasma**: un cuerpo entero traslúcido. rembg devolvió una máscara de
   confianza baja. **No se arregla: se descarta.**
3. **Trozos amputados**: un brazo o media cabeza. Sobre negro el hueco parece sombra.
4. **Restos del fondo original**: una esquina de cielo pegada al hombro.
5. **Celdas casi todas grises**: el PNG existe y pesa, pero no hay figura (`151`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Revisar recortes en el explorador de Windows (fondo claro/oscuro) | El halo se disimula y llega al render |
| Aceptar un recorte por su miniatura | A 120 px no hay halo visible en ningún caso |
| Subir el umbral de alfa para "limpiar" el halo | Se come el pelo y el contorno real; la figura queda recortada a hachazos |
| Medir el halo en % del PNG en vez de contra la superficie opaca | Un recorte pequeño en un lienzo grande sale siempre bien |
| Corregir un recorte fantasma en vez de descartarlo | rembg falló porque la escena no era segmentable: va a fallar igual |
| Hacer la hoja de contactos después de renderizar | Cada recorte rehecho cuesta un render entero |

## Relacionado

`160` la grilla de fotogramas · `163` contraste elemento-fondo · `23` empatar recorte y
fondo · `25` el borde de papel · `151` capturas en blanco que pesan lo normal

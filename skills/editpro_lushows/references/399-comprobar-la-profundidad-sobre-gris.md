# 399 — Comprobar la profundidad sobre gris

**Qué resuelve:** el cuadro tiene profundidad **en este fondo concreto**. Mueves el elemento 60 px, o
cambias de escena, y desaparece. Porque lo que estabas midiendo no era la distancia entre planos: era
la diferencia entre el elemento y esa mancha del fondo. Sobre gris 128 esa confusión se cae sola.

`canales 161` ya explica por qué el gris es el fondo de revisión —el negro esconde los halos, el blanco
también— y da el medidor de borde blando. Eso no se repite. **Aquí va la otra lectura del mismo gris:
la de la separación entre planos.**

---

## 1. La demostración

Tres elementos del piloto, a 620 px, compuestos primero sobre `f_torre` y después sobre gris 128. Se
mide el elemento contra un anillo de 18 px a su alrededor.

| Elemento | Fondo | ΔY | ΔC | ΔS |
|---|---|---|---|---|
| `retrato_lustig` | `f_torre` | **54,4** | 2,7 | 31,6 |
| `retrato_lustig` | gris 128 | **8,1** | 29,9 | 27,3 |
| `ficha_policial` | `f_torre` | **46,8** | 9,6 | 34,1 |
| `ficha_policial` | gris 128 | **14,3** | 32,3 | 26,8 |
| `billetes_falsos` | `f_torre` | **34,7** | 35,7 | 42,3 |
| `billetes_falsos` | gris 128 | **1,3** | 57,4 | 19,2 |

La columna ΔY se derrumba: 54,4 → 8,1 · 46,8 → 14,3 · 34,7 → **1,3**.

> Esos 54 puntos de luminancia **no eran del elemento**. Eran de la zona oscura del fondo que le tocó
> detrás. El elemento no estaba separado: estaba **apoyado**.

Y a la vez aparece lo que el fondo tapaba: sobre `f_torre`, `retrato_lustig` da **ΔC = 2,7** — su
contraste y el del fondo son prácticamente iguales. En el eje de contraste ese elemento y ese fondo
están a la misma distancia. Nadie lo habría visto porque la diferencia de luz lo disimulaba entero.

---

## 2. Qué se lee sobre gris y qué no

Ésta es la parte que se hace mal.

| Lectura | Sobre el fondo real | Sobre gris 128 |
|---|---|---|
| ΔY elemento–fondo | **útil**: dice si se recorta contra ESE fondo | inútil: el gris está donde está |
| ΔC, ΔS contra el anillo | contaminadas por el fondo | **no son separaciones**: el gris tiene C ≈ 4–11 y S = 0 |
| C, S, ACUT **absolutos** del elemento | contaminados por lo que hay detrás | **limpios, y comparables** |

> **Sobre gris no se miden separaciones: se miden coordenadas.** La separación entre dos planos es la
> diferencia entre sus coordenadas, no la diferencia contra el gris.

El procedimiento correcto, entonces, tiene dos pasos y la gente hace solo el segundo:

1. **Sobre gris:** apuntar las cuatro coordenadas de cada plano (`390`). Son estables, no dependen de
   la escena y valen para todo el episodio.
2. **Sobre el fondo real:** comprobar ΔY, que es lo único que sí es propio de esa colocación, y que
   decide si el elemento se recorta contra el fondo o se hunde en él.

---

## 3. La hoja de planos

`canales 161` monta una hoja de contactos de **recortes** sobre gris para cazar halos. Ésta es la
hermana: una hoja de **planos**, con cada elemento ya escalado y tratado como va a salir, ordenado en
columnas por cota.

```python
#!/usr/bin/env python3
"""planos.py - una columna por cota de profundidad, sobre gris 128."""
from PIL import Image

GRIS, CELDA, MARGEN = (128, 128, 128), 460, 10

def hoja(cotas, dest="_planos.png"):
    """cotas: dict {'frente': [PIL RGBA ya tratadas], 'medio': [...], ...}"""
    filas = max(len(v) for v in cotas.values())
    h = Image.new("RGB", (len(cotas)*CELDA, filas*CELDA), GRIS)
    for c, (nombre, ims) in enumerate(cotas.items()):
        for f, im in enumerate(ims):
            k = (CELDA - 2*MARGEN) / max(im.size)
            r = im.resize((max(1, int(im.width*k)), max(1, int(im.height*k))), Image.LANCZOS)
            h.paste(r, (c*CELDA + (CELDA-r.width)//2,
                        f*CELDA + (CELDA-r.height)//2), r)     # máscara = alfa
    h.save(dest); print(f"{dest}  {h.size[0]}x{h.size[1]}")
```

**Importante y contraintuitivo:** la hoja escala todas las celdas al mismo tamaño, o sea, **anula el eje
de tamaño a propósito**. Eso es lo que la hace útil: si quitando el tamaño las columnas siguen
distinguiéndose, los otros tres ejes están haciendo su trabajo. Si sin el tamaño todas las columnas se
ven iguales, tu profundidad era solo escala (`396` §3.2).

**Qué se busca, en este orden:**

1. **Las columnas se distinguen sin leer el rótulo.** Si no, no hay escalón en desenfoque/contraste/color.
2. **Dentro de una columna, todo se parece.** Un elemento que en la columna "medio" se ve más nítido que
   sus vecinos está mal cocinado.
3. **Ninguna columna es una fila de manchas.** Eso es pasarse de escalón (más de −75 % de ACUT).
4. **La sombra concuerda con la columna.** La columna "medio" con sombras de plano frente es `394` §4.
5. **Halos.** Siguen apareciendo aquí, y siguen siendo `canales 161`.

---

## 4. El gris tiene que ser gris de verdad

Tres formas de invalidar la prueba sin darse cuenta:

- **Guardar la hoja con un perfil de color raro.** Si el visor le aplica una conversión, el 128 deja de
  ser 128 y las coordenadas se corren. Guarda en sRGB a secas, sin conversiones intermedias.
- **Revisarla en un visor con fondo propio.** El explorador de Windows y muchos visores pintan un fondo
  detrás de las zonas transparentes de un PNG. La hoja se guarda en **RGB**, no en RGBA: así no hay
  transparencia que rellenar y lo que ves es lo que hay.
- **Mirarla en un monitor con "modo lectura" o filtro de luz azul.** Cambia la temperatura de todo y el
  eje de saturación deja de ser legible.

Y una cuarta que es la más común: **mirarla en miniatura.** A 120 px no se distingue un escalón de
desenfoque de −30 % de uno de −60 %. La hoja se abre al 100 %.

---

## 5. Cuándo esta prueba no sirve

Si el escalón de profundidad de tu escena se apoya deliberadamente en el fondo —un elemento claro que
existe para recortarse contra una zona oscura— la caída de ΔY sobre gris **no es un fallo**: es el
resultado esperado. Lo que tienes que comprobar entonces es otra cosa: que esa zona oscura del fondo
**esté ahí toda la vida del elemento**. Si el fondo tiene zoom o deriva (`canales 22`), la mancha se
mueve, el elemento no, y la separación se evapora a mitad de plano.

La comprobación es de `canales 160`: la grilla de fotogramas. Medir ΔY en el primer fotograma del
elemento y en el último. Si cae más de 15 puntos, la separación era prestada.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Leer ΔC o ΔS contra el gris como separación | El gris no es un plano: tiene C ≈ 4–11 y S = 0 |
| Dar por buena la profundidad solo sobre el fondo real | ΔY 54,4 se cae a 8,1: la separación era del fondo |
| No hacer la lectura sobre el fondo real | ΔY es lo único que dice si se recorta contra ESE fondo |
| Hacer la hoja de planos con los tamaños reales | El eje de tamaño tapa a los otros tres |
| Guardar la hoja en RGBA | El visor pinta su propio fondo detrás y la prueba se anula |
| Perfil de color no sRGB | El 128 deja de ser 128 y las coordenadas se corren |
| Revisar la hoja en miniatura | A 120 px no se distingue −30 % de −60 % de ACUT |
| Olvidar que el fondo se mueve | La mancha que separaba se va y el elemento se queda |
| Confundir esta prueba con la de halos | Ésa es `canales 161`: mide el borde blando, no la separación |

## Relacionado

`390` la profundidad es separación medida · `393` el escalón de contraste y color ·
`394` la sombra que asienta · `396` el plano que no separa · `398` profundidad en vertical ·
`331` medir la separabilidad · `332` mirar y medir · `333` la hoja de contactos como decisión ·
`canales 161` auditar sobre gris (halos y borde blando) · `canales 160` la grilla de fotogramas ·
`canales 22` profundidad por capas

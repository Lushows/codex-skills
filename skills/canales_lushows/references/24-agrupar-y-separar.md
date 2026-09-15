# 24 · Agrupar y separar

**Qué resuelve:** hay cinco recortes en pantalla y el espectador no sabe si son cinco
cosas o dos ideas. La percepción agrupa sola, según reglas conocidas; el trabajo es
usarlas a propósito en vez de sufrirlas.

---

## Las seis leyes que sirven en un collage

| Ley | Qué agrupa | Cómo se aplica aquí |
|---|---|---|
| **Proximidad** | Lo que está cerca | Separación menor de 40 px = un bloque |
| **Semejanza** | Lo que se ve del mismo material | Mismo grosor de margen y mismo rango de `rot` |
| **Región común** | Lo que comparte un contenedor | Una lámina de papel crema detrás del grupo |
| **Continuidad** | Lo que está alineado | Un borde compartido con tolerancia ±6 px |
| **Destino común** | Lo que se mueve igual | Misma `deriva` en la tabla de eventos |
| **Cierre** | Lo que forma una figura completa | El rótulo cierra el objeto y lo vuelve una unidad |

## Los números de la separación

| Distancia entre bordes | Cómo se lee |
|---|---|
| 0 - 18 px | Colisión. Parece un error de posición |
| **18 - 40 px** | **Un bloque. Dos recortes que son una sola idea** |
| 40 - 110 px | **Tierra de nadie.** Ni juntos ni separados: es el defecto más común |
| **120 px o más** | **Elementos independientes** |

La tierra de nadie es donde caen los montajes hechos a ojo. Si dos elementos están a
70 px, o se acercan a 30 o se alejan a 140. No hay término medio útil.

## La herramienta más barata: destino común

Dos recortes con la **misma `deriva`** se leen como un grupo aunque estén a 200 px, y
lo hacen sin gastar un solo píxel de composición:

```python
"elementos": [
    {"r": "planta_pescado",  "x": "W*0.194-w/2", "y": "H*0.5-h/2", "w": 460,
     "deriva": (7, -3), "rot": -2.1},
    {"r": "planta_pescado2", "x": "W*0.347-w/2", "y": "H*0.5-h/2", "w": 440,
     "deriva": (7, -3), "rot":  1.8},          # misma deriva: es el mismo grupo
    {"r": "reloj_real",      "x": "W*0.806-w/2", "y": "H*0.219-h/2", "w": 520,
     "deriva": (0, 5),  "rot": -1.4},          # otra deriva: es otra idea
]
```

Al revés funciona igual de bien: para **romper** un grupo que se está leyendo junto sin
querer, basta con darle a uno una deriva distinta.

## Región común: la lámina de fondo

Cuando tres o cuatro recortes son una unidad (los tres pasos de un método, las tres
fotos de la misma planta), se pega debajo una lámina de papel crema `#E6DCC4` un poco
más grande que la caja del grupo. Es el recurso más claro y el más caro en píxeles:

```python
from PIL import Image, ImageFilter

def lamina_grupo(w, h, borde=34, salida="recursos/_lamina_grupo.png"):
    """Papel crema con sombra, para poner DEBAJO de un grupo de recortes."""
    m = borde + 26
    lienzo = Image.new("RGBA", (w + 2*m, h + 2*m), (0, 0, 0, 0))
    sil = Image.new("L", (w + 2*borde, h + 2*borde), 255)
    neg = Image.new("RGBA", sil.size, (0, 0, 0, 150))
    neg.putalpha(sil.filter(ImageFilter.GaussianBlur(14)))
    lienzo.alpha_composite(neg, (m - borde + 9, m - borde + 14))
    papel = Image.new("RGBA", sil.size, (230, 220, 196, 255))
    lienzo.alpha_composite(papel, (m - borde, m - borde))
    lienzo.save(salida)
    return lienzo.size
```

Va **primera** en la lista de `elementos` (queda debajo de todo, `22`) y su `dura`
cubre la vida entera del grupo: entra 0,2 s antes que el primer recorte y muere 0,2 s
después que el último. Una lámina que aparece y desaparece a destiempo delata el truco.

## Continuidad: alinear un borde

Alinear **uno solo** de los cuatro bordes basta para que dos recortes se lean como
pareja. El de arriba es el que mejor funciona en este canal, porque los recortes tienen
alturas distintas y el borde inferior desigual se ve casual.

- Tolerancia: **±6 px**. Alineado.
- **7 a 24 px**: se lee como que uno está mal puesto. La banda prohibida.
- Más de 24 px: desalineado a propósito, y se acepta.

Ojo con la rotación: `rot` cambia la caja del elemento (`20`), así que dos recortes con
la misma `y` pero ángulos distintos **no** tienen el borde superior alineado. Se alinea
sobre la caja girada, o se les pone el mismo ángulo.

## Semejanza: lo que hace que un grupo sea familia

Tres cosas, todas ya en `revista.py` y `tijera.py`:

1. **Mismo `borde`** (14 px para recortes de revista, 15-20 para tijera). Un margen de
   14 al lado de uno de 20 rompe la familia.
2. **Mismo rango de ángulo**, alternando signo: −2,4° / +1,8° / −2,1°.
3. **Misma semilla de grano por escena**, no por alias, cuando el grupo debe verse de
   la misma hoja.

Y al contrario: para que un elemento **no** pertenezca al grupo, se le cambia el
tratamiento — margen más grueso, ángulo más marcado, plano medio (`22`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Separaciones de 40-110 px | Ni bloque ni elementos sueltos: el cuadro se ve desordenado |
| Misma deriva a elementos de ideas distintas | Se leen como un grupo y el espectador busca la relación |
| Lámina de grupo con `dura` corta | Aparece y desaparece dentro de la vida del grupo: delata el truco |
| Alinear la `y` de dos elementos con `rot` distinto | Quedan desalineados 7-20 px: la banda prohibida |
| Cinco elementos sueltos sin ninguna agrupación | El ojo los cuenta uno a uno y pierde la frase |
| Grupo con márgenes de papel de grosores distintos | Se rompe la semejanza y deja de leerse como familia |

## Relacionado

`20` retícula del collage · `21` peso visual y jerarquía · `25` el borde de papel ·
`26` superposición y oclusión · `29` plantillas de escena

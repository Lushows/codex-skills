# 159 — Microtipografía y pulido

Esto es lo que separa al diseñador profesional del aficionado, y casi nadie lo nota… conscientemente. La **microtipografía** son los detalles diminutos del texto: las comillas correctas, el guion adecuado, el espaciado fino, los números bien elegidos. El lector no los "ve", pero SIENTE que algo está bien hecho o que algo está descuidado. Es el pulido invisible que hace que un texto se vea caro. Cierra el bloque tipográfico y refina todo lo del 40 al 48 y el 152 editorial.

## Comillas tipográficas (el error #1)
El teclado tiene comillas "rectas" (`"` y `'`) que son de MÁQUINA DE ESCRIBIR. En tipografía profesional NUNCA se usan en texto. Usa las **curvas** ("comillas inglesas") o las **angulares** (español formal):

| Mal (recto) | Bien (curvo/inglés) | Bien (angular, español) |
|---|---|---|
| `"hola"` | "hola" | «hola» |
| `'casa'` | 'casa' | — |
| `it's` | it's (apóstrofo curvo) | — |

En español formal y editorial se prefieren las **« »** (latinas); en uso general las **" "** (inglesas) son aceptadas. Lo prohibido es la recta. El apóstrofo correcto es ' (curvo), no '.
```css
/* deja que el navegador ponga las comillas correctas por idioma */
q { quotes: "«" "»" "“" "”"; }
:lang(en) q { quotes: "“" "”" "‘" "’"; }
```

## Guiones: tres largos, tres usos
| Signo | Nombre | Uso | Ejemplo |
|---|---|---|---|
| `-` | Guion corto (hyphen) | Palabras compuestas, partición | teórico-práctico |
| `–` | Raya media (en dash) | Rangos | 2020–2026, páginas 10–14 |
| `—` | Raya larga (em dash) | Incisos, diálogo | —dijo ella— |

Usar el guion corto para rangos o incisos es un error clásico. La raya media va en rangos sin espacios; la raya larga en incisos (en español, pegada a la palabra que abre).

## Números: oldstyle vs. tabular vs. proporcional
Muchas fuentes traen VARIOS juegos de números:
| Tipo | Aspecto | Para qué |
|---|---|---|
| **Lining** (de caja alta) | Todos a la altura de mayúsculas | Titulares, todo-mayúsculas |
| **Oldstyle** (de estilo antiguo) | Suben y bajan como minúsculas | Texto corrido (se integran mejor) |
| **Tabular** | Cada cifra mismo ancho | TABLAS, precios, datos que alinean en columna |
| **Proporcional** | Anchos según la cifra | Texto normal, más natural |

```css
.tabla-precios { font-variant-numeric: tabular-nums lining-nums; }
.texto-articulo { font-variant-numeric: oldstyle-nums proportional-nums; }
```
Regla: en TABLAS y montos que deben alinearse, SIEMPRE tabular (si no, las columnas de números quedan dentadas). En texto largo, oldstyle se ve más elegante.

## Ligaduras
Dos letras que chocan (f+i, f+l) se fusionan en un solo glifo más limpio: **fi → ﬁ**. Las fuentes buenas lo hacen solas.
- **Ligaduras estándar** (fi, fl, ffi): déjalas activas siempre.
- **Ligaduras discrecionales** (st, ct decorativas): solo en titulares/lujo, nunca en texto largo.
```css
body { font-feature-settings: "liga" 1; }       /* estándar on */
.lujo { font-feature-settings: "liga" 1, "dlig" 1; }  /* discrecionales */
```

## Versalitas (small caps) REALES
Las **versalitas** son mayúsculas con la altura de las minúsculas. Sirven para siglas (NASA, ONU), arranques de capítulo, créditos. ¡OJO! No las simules encogiendo mayúsculas (se ven flacas y mal espaciadas). Usa las versalitas REALES de la fuente:
```css
.sigla { font-variant-caps: small-caps; }  /* usa el glifo real si existe */
```

## Espaciado fino: kerning y tracking
- **Kerning:** el ajuste de espacio entre PARES concretos de letras (la A junto a la V se acercan; la T junto a la o). Las fuentes buenas lo traen; actívalo:
```css
body { font-kerning: normal; }
```
- **Tracking (letter-spacing):** el espacio GENERAL entre todas las letras.
  - Texto en MAYÚSCULAS: ábrelo un poco (`letter-spacing: .05em`) — las mayúsculas piden aire.
  - Texto en minúsculas/cuerpo: déjalo en 0 o casi.
  - Titulares MUY grandes: ciérralo levemente (`letter-spacing: -.02em`) — en grande sobra espacio.

## Otros detalles del pulido invisible
- [ ] **Espacio fino antes de signos** en francés; en español NO se separa el signo.
- [ ] **No dejes una palabra sola** colgando (viudas, ver 152): `text-wrap: pretty/balance`.
- [ ] **Cifras y unidades juntas:** "5 km", "50 %" con espacio fino, sin que se partan en dos líneas (`5&nbsp;km`).
- [ ] **Versalitas para siglas largas** en mayúsculas dentro de texto (evita que GRITEN).
- [ ] **Elipsis real** … (un glifo) en vez de tres puntos `...`.
- [ ] **Multiplicación con × real** (no la equis), **× vs x**; menos con − real en cifras.
- [ ] **Sangrías y comillas consistentes** en todo el documento.

## Ejemplo trabajado
Página de precios de una marca premium. Antes: comillas rectas, "$1,500-2,000", números proporcionales en la tabla (columnas dentadas), siglas "API" gritando en mayúsculas dentro del texto. Después:
- Comillas «curvas» correctas, montos con números **tabulares** alineados, rango con **raya media** ($1.500–2.000).
- "API", "SSL" en **versalitas**, integradas sin gritar.
- Títulos con `letter-spacing: -.01em`, mayúsculas de etiquetas con `+.06em`.
- Ligaduras activas, kerning normal, elipsis y × reales.
Nadie sabrá explicar por qué, pero la página entera se ve más cara y más confiable. Ese es el pulido invisible.

## Siguiente paso
Haz una "pasada de microtipografía" sobre tu pieza más importante (web, menú, presentación, manual): reemplaza comillas rectas por curvas, guiones por la raya correcta, números de tabla por tabulares, activa kerning y ligaduras, y caza palabras solas. Es la última capa del oficio — con esto cierras el dominio tipográfico (40–49, 150–159) y puedes volver al sistema completo de marca (44 tipografía de marca, 11 plataforma).

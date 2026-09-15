# 152 — Tipografía editorial avanzada

La diferencia entre una revista que se ve "de papel premium" y un PDF que parece hecho en Word no está en la fuente: está en los DETALLES de maquetación. Este módulo es para cuando diseñas algo que se lee de verdad — una revista, un libro, un reporte anual, un dossier de marca, un menú largo, un brandbook (ver 90 si existe). El oficio editorial es el gimnasio donde se forja el buen tipógrafo.

## La grilla tipográfica (la columna vertebral)
Una **grilla** (grid) es la estructura invisible de columnas y líneas que ordena la página. Define dónde empieza el texto, los márgenes, las imágenes.

- **Márgenes generosos.** En editorial premium el blanco no es desperdicio, es lujo. Regla clásica de libro: margen exterior > superior > interior, y el inferior el mayor (el texto "flota" hacia arriba).
- **Grilla de columnas** para revistas: 6 o 12 columnas dan flexibilidad (texto a 1, 2 o 3 columnas, fotos a ancho variable).
- **Grilla de línea base** (baseline grid): todas las líneas de texto caen en un renglón invisible común, incluso entre columnas. Es lo que hace que una doble página se vea "afinada como reloj". Ver 48 escalas y ritmo.

## Medida de línea (lo que más afecta la lectura)
La **medida** (measure) es el ancho de la columna de texto. Es el ajuste más importante para que algo se lea cómodo.

| Medida | Caracteres por línea | Resultado |
|---|---|---|
| Muy corta | < 45 | Ojo salta mucho, cansa |
| **Óptima** | **55–75** (ideal ~66) | Lectura fluida |
| Muy larga | > 85 | El ojo se pierde al volver |

```css
p { max-width: 66ch; }  /* ch = ancho de un carácter; truco editorial en web */
```

## Interlineado (leading)
El espacio entre líneas. Regla base: **130–150%** del tamaño del texto. Texto más largo o columna más ancha → más interlineado. Titulares grandes → interlineado más apretado (110–120%).
```css
body { font-size: 17px; line-height: 1.55; }  /* ~26px de interlineado */
h1   { font-size: 64px; line-height: 1.05; }
```

## Viudas y huérfanas (el detalle que delata)
- **Huérfana** (orphan): la primera línea de un párrafo queda SOLA al final de una columna/página.
- **Viuda** (widow): la última línea de un párrafo (a veces una sola palabra) queda SOLA arriba de la siguiente columna.

Ambas se ven mal y gritan "amateur". Se corrigen:
- [ ] Ajustando el texto (acortar/alargar una frase con el editor).
- [ ] Variando levemente el interlineado o el tracking de un párrafo (ver 159).
- [ ] En web, evitar que la ÚLTIMA palabra de un título quede sola:
```css
h2 { text-wrap: balance; }   /* equilibra las líneas de un titular */
p  { text-wrap: pretty; }    /* evita viudas feas en párrafos (2026) */
```
Nunca dejes una palabra suelta colgando en un título. Usa `&nbsp;` entre las dos últimas si hace falta.

## Detalle fino editorial
- **Sangría O espacio entre párrafos, no ambos.** En libro: sangría (primer renglón indentado), sin espacio extra. En web/revista: espacio entre párrafos, sin sangría. El primer párrafo tras un título NUNCA lleva sangría.
- **Versalitas** (small caps) para siglas y arranques de capítulo (ver 159).
- **Números oldstyle** en texto corrido (los que "suben y bajan" como minúsculas) — se integran mejor (ver 159).
- **Comillas tipográficas** « » " " y guiones correctos — — no el guion del teclado (ver 159).
- **Capitular** (drop cap): la letra grande inicial de un capítulo. Alinea su tope y su base con líneas del texto.
- **Ríos de blanco:** si justificas el texto, vigila los huecos blancos que se alinean verticalmente entre palabras. Se cortan con tracking, partición de palabras (hyphenation) o cambiando la medida.

## Justificado vs. alineado a la izquierda
- **Izquierda (ragged right):** más fácil, espaciado de palabra uniforme, borde derecho irregular. Lo seguro para web y la mayoría de casos.
- **Justificado:** ambos bordes rectos, look de libro/periódico. SOLO con buena partición de palabras activada, si no, abre ríos y huecos feos. En web usa con cuidado: `text-align: justify; hyphens: auto;`.

## Ejemplo trabajado
Reporte anual de 40 páginas, A4. Grilla de 12 columnas, margen inferior amплio. Cuerpo a 2 columnas, medida ~64 caracteres, fuente serif a 10.5pt / interlineado 14.5pt sobre grilla base de 14.5pt. Cifras en tablas con números **tabulares** (alinean en columna, ver 159); cifras en texto con **oldstyle**. Titulares de sección en sans variable peso 620, `text-wrap: balance`. Cero viudas (revisión página por página). Resultado: se lee como documento de banca de inversión, no como informe casero.

## Siguiente paso
La próxima vez que maquetes algo largo, haz una pasada FINAL solo de detalle: viudas, huérfanas, ríos, comillas y guiones correctos, sangrías consistentes. Es la pasada que separa al pro (profundiza en 159 microtipografía). Para jerarquía y escala, ver 43 y 48.

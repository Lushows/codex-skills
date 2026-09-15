# 150 — Fuentes variables

Hasta hace poco, una familia tipográfica eran muchos archivos sueltos: uno para Light, otro para Regular, otro para Bold, otro para Italic… Una **fuente variable** es UN solo archivo que contiene infinitos pesos y variaciones de esa familia, controlables con números. Es uno de los avances más prácticos de la tipografía web moderna, y a junio 2026 es la norma para marcas serias. Este módulo te enseña a entenderlas y usarlas sin tecnicismos.

## Qué es exactamente
Imagina una perilla deslizante: en un extremo la letra es finísima, en el otro extremo es gordísima, y puedes parar en CUALQUIER punto intermedio. Esa perilla se llama **eje** (axis). Una fuente variable trae uno o varios ejes en un mismo archivo.

| Eje | Etiqueta | Qué controla | En simple |
|---|---|---|---|
| **Weight** | `wght` | Grosor del trazo (1–1000) | De finito a negrísimo |
| **Width** | `wdth` | Ancho de la letra | Condensada ↔ expandida |
| **Optical size** | `opsz` | Ajuste según tamaño | Afina remates para titular vs. texto |
| **Slant** | `slnt` | Inclinación mecánica | Italic falsa pero limpia |
| **Italic** | `ital` | Cursiva real (0 o 1) | Letra rediseñada, no solo inclinada |
| **Grade** | `GRAD` | Engorda sin mover el ancho | Útil para dark mode (ver 155) |

Los cuatro primeros son **ejes registrados** (estándar). Cualquier fundición puede inventar ejes propios (custom), por ejemplo "redondez" o "energía".

## Por qué importan (la ventaja real)
1. **Velocidad web.** Antes cargabas 4–6 archivos de fuente. Ahora cargas 1. Menos peso = página más rápida = mejor experiencia y mejor SEO. Es ahorro real de kilobytes.
2. **Diseño sin límites de peso.** ¿Quieres un peso 537, exactamente entre Medium y Semibold? Puedes. Eso da jerarquías finísimas (ver 43 jerarquía).
3. **`opsz` automático.** Tu titular de 80px usa remates afilados y elegantes; tu texto de 16px usa una versión más robusta y legible — del MISMO archivo. Esto es lo que hace que el texto fino se vea "caro".
4. **Animación.** Puedes animar el peso de un texto al pasar el mouse, de Regular a Bold suavemente (ver 158 tipografía cinética).

## Cómo se usa en la web (CSS)
Dos formas. La moderna y simple:

```css
/* Lo normal: usa las propiedades estándar */
h1 { font-weight: 720; }          /* cualquier número, no solo 400/700 */
.condensada { font-stretch: 75%; } /* ancho */

/* Control total de TODOS los ejes a la vez */
.titular {
  font-variation-settings:
    "wght" 680,
    "wdth" 88,
    "opsz" 72;
}
```

Regla de oro: usa `font-weight` y `font-stretch` cuando puedas (son las propiedades "oficiales"); usa `font-variation-settings` solo para ejes raros o varios a la vez. No mezcles las dos para el mismo eje.

Al cargar la fuente, declara el rango disponible:
```css
@font-face {
  font-family: "Inter var";
  src: url("Inter.woff2") format("woff2");
  font-weight: 100 900;   /* rango, no un solo valor */
  font-stretch: 75% 125%;
  font-display: swap;
}
```

## Fuentes variables recomendadas (reales, junio 2026)

| Fuente | Ejes | Buena para | Licencia |
|---|---|---|---|
| **Inter** | wght, opsz, ital, + custom | UI, dashboards, tech | Gratis (OFL) |
| **Roboto Flex** | 12+ ejes (wght, wdth, opsz, GRAD…) | Casi todo, muy flexible | Gratis (OFL) |
| **Source Serif / Sans** | wght, opsz | Editorial, corporativo serio | Gratis (OFL) |
| **Recursive** | wght, slnt, MONO, CASL, CRSV | Marcas con personalidad tech | Gratis (OFL) |
| **Fraunces** | wght, opsz, SOFT, WONK | Editorial cálida, lujo suave | Gratis (OFL) |
| **GT Flexa / ABC families** | wght, wdth | Marcas premium | De pago (Grilli/Dinamo) |

Para licencias y dónde conseguirlas, ver 49 fuentes recomendadas y licencias.

## Cuándo NO usarla
- Si la marca usa una sola fuente en un solo peso, una variable no aporta (carga el peso estático).
- En print clásico, muchas imprentas y plantillas viejas aún esperan archivos estáticos.
- Algunos software de diseño antiguos no las soportan bien; verifica antes de comprometerte.

## Ejemplo trabajado
Marca de café de especialidad, web. Eliges **Fraunces** (variable) para títulos y **Inter** (variable) para texto.
- Título grande: `font-variation-settings: "wght" 540, "opsz" 144, "SOFT" 40;` → serif cálida, redondeada, "artesanal".
- Subtítulo: `"wght" 380, "opsz" 40;` → más sobrio.
- Cuerpo (Inter): `font-weight: 420;` → un pelín más que Regular, mejor color de texto en pantalla.
Resultado: dos archivos cargados, jerarquía de 6 niveles, y un `opsz` que hace que el título de 96px se vea editorial y el texto de 17px se lea cómodo.

## Siguiente paso
Define para tu marca: una fuente variable de titulares y una de texto, con los pesos exactos de cada nivel de jerarquía (ver 43, 48 escalas y ritmo). Anota los valores `font-variation-settings` en el manual para que cualquier desarrollador los replique idénticos. Si quieres una fuente 100% única, sigue al 151 type design custom.

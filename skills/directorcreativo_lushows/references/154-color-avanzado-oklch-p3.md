# 154 — Color avanzado: OKLCH y Display-P3

Durante 30 años pintamos la web con HEX (`#FF5733`) y HSL. Funcionan, pero tienen defectos que arruinan paletas y gradientes. A junio 2026, los navegadores modernos soportan formas MUCHO mejores de definir color: **OKLCH** (color predecible para el ojo) y **Display-P3** (más colores vivos en pantallas modernas). Este módulo te explica por qué importan y cómo usarlos. Es la actualización natural del 32 sistemas de color y el 33 construir una paleta.

## El problema de HSL y HEX
En **HSL** (Hue, Saturation, Lightness) la "L" (luminosidad) MIENTE. Un amarillo con L=50% se ve clarísimo; un azul con L=50% se ve oscurísimo — aunque el número diga lo mismo. Resultado: si construyes una paleta variando solo la L, los colores no tienen brillo parejo. Tu "verde y azul al mismo nivel" se ven a niveles distintos.

HEX es aún peor para pensar: `#2E7D32` no te dice nada a la vista. No puedes "aclararlo un 10%" mentalmente.

## La solución: OKLCH
**OKLCH** es un espacio de color **perceptualmente uniforme**: los números coinciden con lo que el ojo ve. Sus tres valores:

| Letra | Nombre | Rango | En simple |
|---|---|---|---|
| **L** | Lightness (luminosidad) | 0% – 100% | Qué tan claro, REAL para el ojo |
| **C** | Chroma (saturación) | 0 – ~0.37 | Qué tan vívido/intenso |
| **H** | Hue (matiz) | 0 – 360 | El color (el "tono") |

```css
color: oklch(62% 0.17 145);   /* verde */
```

La magia: si subes la L de DOS colores distintos al mismo valor, se ven igual de claros. Eso hace paletas coherentes y accesibles (ver 35 contraste).

### Por qué supera a HSL/HEX
- **Brillo real:** L=70% es L=70% para el ojo en CUALQUIER matiz.
- **Paletas por sistema:** fija L y C, gira solo H → familia de colores hermana y equilibrada.
- **Escalas de tinte perfectas:** baja L de a pasos iguales → 50, 100, 200… 900 (como Tailwind) sin saltos raros.
- **Gradientes sin zona muerta:** interpolar en OKLCH evita el "gris sucio" del medio (ver 157 gradientes).

```css
:root {
  /* familia de marca: misma L y C, solo cambia el matiz */
  --verde:  oklch(62% 0.15 150);
  --azul:   oklch(62% 0.15 250);
  --coral:  oklch(62% 0.15  30);
  /* escala de un mismo color, solo cambia L */
  --verde-100: oklch(95% 0.04 150);
  --verde-500: oklch(62% 0.15 150);
  --verde-900: oklch(30% 0.10 150);
}
```

## Display-P3 y wide gamut (colores más vivos)
**Gamut** = el rango de colores que una pantalla puede mostrar. El viejo estándar es **sRGB**. Las pantallas modernas (iPhone, MacBook, OLED) muestran **Display-P3**: ~25% más colores, especialmente verdes y rojos MÁS intensos que sRGB no alcanza.

Con HEX estás encerrado en sRGB. Con la función `color()` accedes a P3:
```css
.cta {
  /* fallback sRGB para pantallas viejas */
  background: #ff2d55;
  /* rojo vivísimo solo visible en P3, con respaldo */
  background: color(display-p3 1 0.17 0.33);
}
/* OKLCH puede salir de sRGB solo (chroma alto) y el navegador usa P3 si puede */
.cta-2 { background: oklch(65% 0.28 25); }
```
Úsalo para acentos que deben GRITAR (un CTA, un highlight de marca). El texto y los fondos grandes mejor mantenlos seguros en sRGB.

## Compatibilidad (junio 2026)
OKLCH y `color()` están soportados en todos los navegadores modernos (Chrome, Safari, Firefox, Edge actuales). Aun así, da un **fallback** para navegadores viejos: declara primero el HEX, luego la versión moderna (la cascada CSS usa la última que entienda).

```css
.btn {
  background: #2E7D32;              /* todos lo entienden */
  background: oklch(55% 0.13 150); /* los modernos usan este */
}
```

## Tabla de equivalencia mental
| Quiero… | En OKLCH cambio… |
|---|---|
| Aclarar un color | Subir **L** |
| Hacerlo más pastel/apagado | Bajar **C** |
| Hacerlo más vivo | Subir **C** |
| Cambiar de color | Mover **H** |
| Color hermano equilibrado | Mismo L y C, otro **H** |

## Ejemplo trabajado
Marca fintech, color base verde `#16A34A`. En OKLCH ≈ `oklch(65% 0.17 150)`.
- Escala UI: 50 `oklch(97% 0.02 150)` … 500 `oklch(65% 0.17 150)` … 900 `oklch(34% 0.10 150)`. Pasos de L uniformes = se ve profesional.
- Acento "éxito/dinero" para celebraciones: `oklch(70% 0.27 150)` (verde P3 vivísimo, imposible en sRGB) con fallback `#16A34A`.
- Secundario azul hermano: `oklch(65% 0.17 250)` — mismo brillo y saturación que el verde, equilibrio perfecto.
Resultado: paleta matemáticamente coherente, accesible y con un verde de marca que "brilla" en pantallas buenas.

## Siguiente paso
Reconstruye tu paleta (33) en OKLCH: fija L y C de marca, genera la familia girando H, y crea cada escala de tinte bajando solo L. Verifica contrastes (35) — con OKLCH es más fácil acertar. Para gradientes en estos espacios, sigue al 157.

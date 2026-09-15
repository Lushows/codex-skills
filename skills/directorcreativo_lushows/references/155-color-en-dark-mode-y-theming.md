# 155 — Color en dark mode y theming

El error número uno del dark mode (modo oscuro) es creer que es "invertir los colores". No lo es. Un dark mode mal hecho cansa la vista, pierde jerarquía y se ve barato. Uno bien hecho se siente premium, descansado y caro. Este módulo te enseña a diseñarlo de verdad, y a montar un sistema de **temas** (theming) que cambie de claro a oscuro sin rediseñar todo. Apóyate en el 32 modos de color, 34 color en el sistema y 154 OKLCH.

## Por qué NO se invierte y ya
- Negro puro `#000` sobre blanco puro `#FFF` invertido vibra y cansa: demasiado contraste.
- Los colores de marca saturados (un azul vivo) sobre negro "brillan" y marean.
- Las sombras (que dan profundidad en claro) desaparecen en oscuro: necesitas OTRO recurso para mostrar jerarquía.

## Regla 1 — Nada de negro puro ni blanco puro
| Rol | Claro | Oscuro (bien hecho) |
|---|---|---|
| Fondo base | `#FFFFFF` | `#121212` – `#1A1A1A` (gris muy oscuro, no negro) |
| Texto principal | `#1A1A1A` (no negro puro) | `#E8E8E8` (gris claro, no blanco puro) |
| Texto secundario | gris medio | gris más apagado, NUNCA gris clarísimo |

El texto en dark mode debe rondar **87% de opacidad** de blanco para el principal, no 100%. Material Design lo formalizó: blanco puro sobre oscuro "deslumbra".

## Regla 2 — Elevación por LUZ, no por sombra
En claro, lo que está "más arriba" (tarjetas, menús) lleva sombra. En oscuro, **la sombra no se ve**. El truco: cuanto más cerca/elevado está un elemento, **más CLARO** es su fondo (como si la luz lo tocara más).

```css
/* Niveles de elevación en dark mode: gris que sube */
--surface-0: #121212;   /* fondo de la app */
--surface-1: #1E1E1E;   /* tarjeta */
--surface-2: #242424;   /* menú flotante */
--surface-3: #2C2C2C;   /* modal/diálogo */
```
Cada nivel un poco más claro = sensación de profundidad sin sombras.

## Regla 3 — Desatura los colores de marca
Un color que vibra en claro debe **bajar saturación y subir un poco la luminosidad** en oscuro para no chillar. En OKLCH es directo (ver 154): baja la C, ajusta la L.
```css
/* Marca azul */
--brand-light: oklch(55% 0.18 250);  /* en tema claro */
--brand-dark:  oklch(72% 0.12 250);  /* más claro, menos saturado, descansa la vista */
```

## Regla 4 — Mantén el contraste (y vigílalo de nuevo)
Texto y fondo en oscuro también deben cumplir WCAG AA (4.5:1) — ver 35. Un gris secundario que pasaba en claro puede fallar en oscuro. Revisa CADA par otra vez. APCA (ver 156) es especialmente útil aquí porque modela mejor el texto claro sobre fondo oscuro.

## Tokens semánticos (la clave del theming)
No uses el color directo en tus componentes. Usa **tokens semánticos**: nombres por FUNCIÓN, no por color. Así, cambiar de tema solo cambia el valor del token, no mil sitios.

```css
/* MAL: el componente conoce el color */
.card { background: #1E1E1E; color: #E8E8E8; }

/* BIEN: tokens semánticos que cambian por tema */
:root {
  --bg-surface: #FFFFFF;
  --text-primary: #1A1A1A;
  --brand: oklch(55% 0.18 250);
}
:root[data-theme="dark"] {
  --bg-surface: #1E1E1E;
  --text-primary: #E8E8E8;
  --brand: oklch(72% 0.12 250);
}
.card { background: var(--bg-surface); color: var(--text-primary); }
```

| Token semántico | Qué representa |
|---|---|
| `--bg-base` / `--bg-surface` | Fondos de app y de tarjetas |
| `--text-primary` / `--text-muted` | Textos principal y secundario |
| `--brand` / `--brand-hover` | Color de marca y su estado hover |
| `--border` / `--divider` | Líneas y separadores |
| `--success` / `--warning` / `--danger` | Estados |

Detectar el modo del sistema automáticamente:
```css
@media (prefers-color-scheme: dark) { :root { /* valores dark por defecto */ } }
```

## Errores frecuentes
- [ ] Negro/blanco puros (vibran, cansan).
- [ ] Sombras como única jerarquía en oscuro (no se ven).
- [ ] Colores de marca saturados sin desaturar (chillan).
- [ ] Olvidar revisar contraste en el nuevo tema.
- [ ] Hardcodear colores en componentes en vez de tokens.
- [ ] Imágenes/logos con fondo blanco "recortado" que aparece como caja blanca en oscuro (usa PNG transparente o versión para fondo oscuro, ver 27 versiones).

## Ejemplo trabajado
Dashboard de la marca (azul `oklch(55% 0.18 250)`). Tema oscuro:
- Fondo `#141414`, tarjetas `#1F1F1F`, modales `#2A2A2A` (elevación por luz).
- Texto principal `#E6E6E6` (87%), secundario `#9A9A9A`.
- Marca desaturada a `oklch(72% 0.12 250)` para botones; hover sube L a 78%.
- Verde éxito y rojo error reajustados y reverificados a AA.
- Todo vía tokens semánticos → el switch claro/oscuro cambia 12 variables, no el código de los 40 componentes.
Resultado: un dark mode que se siente diseñado, no invertido.

## Siguiente paso
Define tu set de **tokens semánticos** una sola vez (claro y oscuro) y conéctalos a tus componentes. Revisa contraste de AMBOS temas (35, 156). Si tu marca tiene varios sub-temas o marcas (ver 15 arquitectura), los tokens son también la vía para multi-brand theming.

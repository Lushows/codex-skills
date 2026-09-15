# 20 — Layout, grid & composición (lo que separa "diseñado" de "templated")

La diferencia entre Awwwards y Bootstrap casi nunca está en color o tipografía — está en la **composición**: cómo se distribuye el espacio, dónde cae el peso visual, qué tan intencional se siente la rejilla. **Léelo cuando estructures cualquier página/sección.** Código en CSS Grid moderno.

## 1. Grid systems & CSS Grid mastery

12 columnas siguen siendo la base (divisible por 2/3/4/6 → splits 6/6, 4/8, 3/9, 7/5 asimétrico premium), pero con líneas nombradas y `subgrid`, no `col-md-4`.

**Content-grid (full-bleed + centered) — el patrón más importante de 2026.** Contenido legible (~65ch) con imágenes/bandas que rompen a ancho completo, sin wrappers anidados:
```css
.content-grid{
  --gap:clamp(1rem,6vw,3rem); --full:minmax(var(--gap),1fr);
  --content:min(70ch, 100% - var(--gap)*2); --popout:minmax(0,2rem); --feature:minmax(0,5rem);
  display:grid;
  grid-template-columns:
    [full-start] var(--full) [feature-start] var(--feature) [popout-start] var(--popout)
    [content-start] var(--content) [content-end]
    var(--popout) [popout-end] var(--feature) [feature-end] var(--full) [full-end];
}
.content-grid > *{ grid-column:content }
.content-grid > .popout{ grid-column:popout }
.content-grid > .feature{ grid-column:feature }
.content-grid > .full-bleed{ grid-column:full }
```
**`grid-template-areas`** para layout de página completa (legible/mantenible): `"header header" "sidebar main" "footer footer"`.
**`subgrid`** para que tarjetas alineen sus partes internas (título/cuerpo/CTA) aunque tengan distinto largo: `.card{ display:grid; grid-row:span 3; grid-template-rows:subgrid }`.
**Auto-grid intrínseco sin media queries:** `repeat(auto-fit, minmax(min(100%,18rem), 1fr))`.

## 2. Composición & jerarquía (teoría aplicada)

- **Contraste de escala:** el h1 debe ser **4-8× el body**, no 1.5×. La timidez tipográfica es la marca #1 de lo templated. `clamp(2.5rem,6vw,6rem)` para hero.
- **Whitespace como herramienta:** el espacio es el material de lujo. Secciones premium respiran (`padding-block:clamp(4rem,12vw,10rem)`). Más aire = más importancia percibida.
- **Peso visual & balance:** simétrico = formal/corporativo/estable; **asimétrico = dinámico/editorial/premium** (contrabalancea un elemento grande y claro con uno pequeño y oscuro/saturado).
- **Punto focal único** por pantalla. Si todo grita, nada se oye.
- **Alineación óptica > matemática:** círculos, iconos, comillas, flechas, play-buttons necesitan ajuste manual (`transform:translateX(-2px)`) — el centro matemático se ve descentrado.
- **Patrones de lectura:** Z-pattern (layouts ligeros: logo→nav→CTA→visual→CTA final); F-pattern (contenido denso: alinea headings y CTAs a la izquierda).
- **Gestalt:** proximidad (agrupa con espacio, no líneas; junta label a input, separa grupos), similitud (mismo estilo = misma función), continuación (alinea para ríos limpios).
- **Tensión:** romper la rejilla a propósito (sangrado, overlap) crea energía — **solo funciona si hay una rejilla disciplinada de fondo que romper.**
- **Rule of thirds / golden ratio:** útiles como *punto de partida* (1.618 → split 62/38), pero es BS tratarlo como ley — el balance óptico y el ritmo mandan.

## 3. Spacing & rhythm

**8pt grid** (estándar Apple/Google/Figma): todo espaciado múltiplo de 8 (4 = medio paso).
```css
:root{ --space-2xs:8px; --space-xs:12px; --space-sm:16px; --space-md:24px; --space-lg:32px;
  --space-xl:48px; --space-2xl:64px; --space-3xl:96px; --space-4xl:128px }
```
**Escala modular** (ratio ~1.5) cuando quieres expresividad: `4,8,12,18,27,40,60,90`. El gap *dentro* de un grupo siempre menor que el gap *entre* grupos → así se lee la jerarquía sin bordes.
**Ritmo vertical:** alinea `margin-block` a múltiplos del line-height base (24px).
**Regla de oro:** el espaciado externo de un componente lo controla el **padre (`gap`)**, nunca `margin` del hijo → componentes reutilizables, sin colapso de márgenes.

## 4. Editorial/magazine (muy 2026)

El look ganador en Awwwards 2026: **editorial/zine con caos controlado** sobre rejilla estricta.
- **Big type as graphic:** titulares `clamp(4rem,14vw,12rem)`, sangrando fuera del viewport (`overflow:clip` en el padre) o detrás de imágenes vía `z-index`.
- **Overlapping** (imagen y texto en la misma celda, desplaza uno):
```css
.overlap{ display:grid; grid-template-columns:1fr 1fr }
.overlap img{ grid-column:1/3; grid-row:1 }
.overlap .txt{ grid-column:2/3; grid-row:1; align-self:end; transform:translateX(-2rem); z-index:2 }
```
- **Drop caps / pull quotes:** `p::first-letter{ float:left; font-size:4.5em; line-height:.8 }`; pull quote en `grid-column:popout`.
- **Mixing column counts:** intro 1 col, cuerpo 2 (`columns:2`), citas full. Alterna deliberadamente.
- **Bento evolucionado:** tiles asimétricos (`span N`), una tile "héroe" 2×2 dominante, mezcla de ratios. Para features/showcases, NO para texto largo.

## 5. Catálogo de section & hero archetypes

| Archetype | Cuándo | Receta |
|---|---|---|
| **Split-screen hero** | SaaS, producto con visual | Grid `1fr 1fr`, texto izq, visual full-height der. Stack en mobile |
| **Centered hero** | Landing simple/statement | Stack centrado `max-width:50ch`, mucho aire. El más fácil de hacer genérico → sálvalo con escala tipográfica brutal |
| **Asymmetric hero** | Editorial/agencia/portfolio | Titular off-center (col 1-8), imagen sangrando (col 7-13), overlap. Premium por defecto |
| **Sticky-scroll feature** | Explicar producto paso a paso | Texto `position:sticky` izq mientras visuales scrollean der |
| **Bento feature grid** | 4-7 features de un vistazo | Asimétrico, una tile 2×2 dominante |
| **Zigzag/alternating** | Features con imagen | Filas alternando img-izq/txt-der; en mobile **siempre** imagen arriba (no alternes) |
| **Marquee** | Logos/"trusted by"/tags | Track horizontal en loop + `prefers-reduced-motion` off |
| **Stats band** | Prueba social cuantitativa | 3-4 col, número enorme + label, fondo contrastante full-bleed |
| **Logo wall** | Clientes/partners | Auto-grid, grayscale `opacity:.6`, color en hover |
| **Testimonial** | Confianza | Card grande con pull-quote + avatar, o grid masonry |
| **Footer** | Cierre | Multi-col `auto-fit minmax`, o "big footer" con titular-CTA gigante |

## 6. Composición responsive

- **Reflow, no shrink:** no escales el desktop; recompón. El grid de 12 col colapsa a `1fr` bajo ~768px.
- **Asimetría en mobile:** la horizontal no cabe → conviértela en asimetría de **espaciado/escala vertical** (offsets, tamaños de tipo dispares). No fuerces overlaps que rompen legibilidad.
- **Mantén jerarquía al apilar:** el orden de stack respeta la prioridad visual. `order` con cuidado (rompe a11y si abusas).
- **Fluid sin breakpoints:** `clamp()` (tipo/spacing) + `auto-fit minmax` (grids) elimina la mayoría de media queries; resérvalas para *cambios de composición* (split→stack).

## ⛔ Layout anti-patterns
1. **Centered everything** (sello #1 de templated) — centra solo statements cortos, alinea izq la lectura.
2. **Equal-weight grids** sin jerarquía — da una tile dominante.
3. **Cramped/no whitespace** — el aire es lujo.
4. **Tipografía tímida** — h1 apenas mayor que el body.
5. **Gutters inconsistentes** — un `--gap` por contexto.
6. **Full-width text** (120ch) — limita a 60-75ch.
7. **Wrappers anidados** para full-bleed — usa content-grid.
8. **Simetría perezosa** (50/50 siempre) — prueba 62/38, 7/5.
9. **Romper la rejilla sin rejilla** — overlaps sin sistema = desastre.
10. **Mobile = desktop encogido**; alternar zigzag en mobile (imagen siempre arriba).
11. **Márgenes en hijos** para espaciar — usa `gap` del padre.
12. **Centrado matemático** de iconos/comillas ignorando alineación óptica.

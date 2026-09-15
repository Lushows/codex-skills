# 45 — Editorial, contenido & long-form reading

Para blogs, publicaciones, revistas digitales, brand storytelling, docs y content-marketing donde **leer es la experiencia central**. Cuando el contenido es el producto, **la tipografía es la UI**. **Léelo para artículos/blogs/publicaciones/long-form.** Pareja de 03 (tipografía), 20 (layout), 26 (scrollytelling).

## 1. La experiencia de lectura (los valores reales)

Tres números: **measure, leading, size.**
- **Measure:** **50-75 caracteres/línea**, **66ch sweet spot** (`max-width:66ch` o `min(66ch,100%)`). <45ch el ojo salta; >80ch se pierde el retorno.
- **Font size de cuerpo:** mínimo 16px, **estándar editorial 2026 = 18-21px** (The Verge/Medium/Stripe Press viven en 19-21). **20px** = default excelente para lectura pura.
- **Line-height:** **1.5-1.7** (más ancha la measure, más leading: 66ch→1.6, 75ch→1.7, columnas estrechas→1.45). Headings 1.05-1.2.
- **Ritmo de párrafo:** **una** señal, no dos — o `margin-block:0 1.4em` (web) o `text-indent:1.5em` sin margen (libro). Mezclar = error de aficionado. Ritmo vertical en múltiplos de una unidad base (`--rhythm:1.6rem`).
- **Contraste cómodo (NO negro puro sobre blanco puro):** `#1a1a1a`-`#222` sobre `#fafaf8`-`#fcfcfa` (blanco cálido casi marfil), ~13:1-16:1 (no 21:1). Tinta y papel cálidos.
- **Serif vs sans (2026):** con Retina el viejo "sans en pantalla" cayó — **el serif vuelve con fuerza en editorial** (ritmo, peso, herencia). Patrón premium: **serif para cuerpo + sans para meta/UI** (o serif display en titulares + sans en cuerpo). Lo clave: una fuente *diseñada para texto*, no un display estirado.
- **Mejores fuentes de lectura (web):** *serif de texto* **Source Serif 4** (gratis, gran en pantalla), **Spectral**, **Newsreader** (optical sizes), **Lora**, Charter/Tiempos Text/Editorial New (pago). *Sans cuerpo/UI* Inter/Source Sans 3. Combo gratis robusto: **Newsreader o Source Serif 4 (cuerpo) + Inter (meta)**.
- **Craft 2026:**
```css
.article-body{ text-wrap:pretty; hanging-punctuation:first last; font-feature-settings:"kern","liga","onum" } /* old-style numerals */
h1,h2,h3,blockquote{ text-wrap:balance }  /* balance en titulares ≤6 líneas, pretty en cuerpo */
```

## 2. Article layout + content-grid breakout

**Anatomía:** (1) hero/header (kicker/categoría, título serif display `clamp(2.5rem,6vw,4.5rem)`, dek, byline+avatar, meta fecha/tiempo de lectura, portada full-bleed); (2) cuerpo columna única 60-66ch centrada; (3) rupturas (imágenes full-bleed, pull quotes, code anchos); (4) apoyos (sidenotes, ToC sticky); (5) cierre (bio, newsletter CTA, related).
**El patrón clave — content-grid con breakouts por named grid lines** (el cuerpo en measure estrecha mientras imágenes/quotes rompen hacia fuera sin wrappers anidados):
```css
.content{ --gap:clamp(1rem,6vw,3rem); --full:minmax(var(--gap),1fr); --content:min(66ch,100% - var(--gap)*2); --popout:minmax(0,2rem); --feature:minmax(0,5rem);
  display:grid; grid-template-columns:[full-start] var(--full) [feature-start] var(--feature) [popout-start] var(--popout)
    [content-start] var(--content) [content-end] var(--popout) [popout-end] var(--feature) [feature-end] var(--full) [full-end]; }
.content > *{grid-column:content} .content > .popout{grid-column:popout} .content > .feature{grid-column:feature} .content > .full{grid-column:full}
```
Versión mínima: `grid-template-columns:1fr min(66ch,100%) 1fr; .content>*{grid-column:2} .content>.full-bleed{grid-column:1/-1}`.
**Reading features:** progress bar sticky top (se llena con el scroll del `<article>`) · tiempo de lectura `Math.ceil(palabras/220)` min · ToC flotante sticky con scroll-spy (`IntersectionObserver`, resalta la sección activa), colapsa a "On this page" en mobile.

## 3. Estética editorial / magazine

**Blog default** = plantilla, una columna gris, todo igual. **Publicación diseñada** = sistema con tensión:
- **Asimetría y tensión de grid** (no todo centrado; titulares desplazados, imágenes que sangran, white space desigual deliberado).
- **Type grande con jerarquía dramática** (serif display de alto contraste, kickers en sans uppercase con tracking, contraste fuerte titular gigante↔cuerpo modesto).
- **Composiciones zine** (overlapping controlado, tipografía como imagen).
- **Art-directed articles** (modelo NYT/The Verge: cada historia importante con su propio tratamiento — color/fuente/ruptura de plantilla). La plantilla es el piso, no el techo.
- **El índice/homepage de la publicación** = *portada* curada (featured grande + jerarquía), no un feed cronológico plano. Las tag/category pages merecen header propio.

## 4. Contenido rico & componentes

- **Imágenes:** `<figure>`+`<figcaption>` (sans pequeño 0.8em atenuado, alineada al borde de la imagen). Tres anchos vía content-grid (content/feature/full). Lazy + `aspect-ratio`.
- **Pull quote** (texto *extraído* del cuerpo, grande 1.6-2.2em serif, en `.feature`/`.popout`) ≠ **blockquote** (cita externa real con indent + atribución). No confundir.
- **Drop cap moderno:** `p:first-of-type::first-letter{ initial-letter:3 3; -webkit-initial-letter:3 3 }` (no float hacky).
- **Sidenotes/marginalia** (Tufte/Gwern): notas al margen lateral (el ojo no salta); en mobile colapsan a inline/footnotes con ancla. `counter()` para numeración.
- **Tablas:** scroll horizontal en `.full` en mobile, zebra sutil, `tabular-nums`.
- **Code blocks:** **Shiki** (estándar 2026, colores reales del theme), mono (JetBrains Mono), botón copiar, en `.full`/`.feature`. Inline con fondo sutil.
- **Callouts/asides** (note/warning/tip, fondo tenue del acento), **embeds** (video con `aspect-ratio`, tweets como cita estilizada), **lightbox** (respeta reduced-motion).

## 5. Sistemas de contenido & features de lectura

- **Dark mode de lectura:** texto **off-white `#e8e8e6`** (NUNCA `#fff`) sobre `#15151a`-`#1a1a1f` (NUNCA `#000` puro — halation). Atenúa imágenes (`filter:brightness(.9)`).
- **Preferencias:** toggle tema (light/sepia/dark), tamaño de fuente (±, hasta ~150-250%), persistido en `localStorage`. Sepia esperado para lectura larga.
- **"Reader mode" como vara:** una columna sin distracciones. Si tu reader mode se ve mejor que tu artículo, fallaste.
- **Save/bookmark, share** (`navigator.share` en mobile), copy-link. **Related** al pie (3-6, thumbnail+kicker+título). **Newsletter CTA** integrado en el flujo (no popup agresivo), tono editorial. **Paywall con gusto** (fade-out, valor antes de pedir).
- **CMS/MDX content modeling:** componentes (Callout/PullQuote/Figure/CodeBlock) como MDX components/bloques del CMS — la "typographic component library" para contenido (un set `.prose`/`.article-body` que cubra todo el HTML del CMS).

## 6. Tendencias 2026 + craft

**Vigente:** editorial print-inspired, **serifs grandes de alto contraste**, revival del slow-content/long-read, art direction por historia, zine con asimetría controlada, optical sizes.
**Craft que distingue:** optical margin alignment (`hanging-punctuation`) · old-style numerals (`"onum"`) en cuerpo, tabular en tablas · baseline grid (todo el ritmo en múltiplos) · caption refinada (créditos diferenciados) · pull quote considerada (no duplicar texto visible) · **smart quotes** (" " ' ') y em-dashes reales (—), nunca rectos.
**A11y de lectura:** opción de fuente dyslexia-friendly o sans alta legibilidad + line-height ≥1.5; nunca bloquees zoom; respeta `prefers-reduced-motion`/`prefers-contrast`; WCAG AA mín (AAA ~7:1 ideal para cuerpo).

## Editorial/reading anti-patterns — blacklist
measure demasiado ancha (>80ch, cuerpo full-width — el error #1) · texto diminuto (14-16px en página de lectura) · negro puro sobre blanco puro (vibra/cansa) · sin ritmo vertical · walls of text (párrafos de 12 líneas, sin subtítulos/imágenes/quotes) · doble señal de párrafo (indent + margen) · line-height aplastado (1.2-1.3) o excesivo (>1.8) · display font como cuerpo (Playfair/Bodoni a 18px) · justificado sin `hyphens:auto` · comillas/guiones rectos + números lining en cuerpo serio · ToC/progress que tapan el texto en mobile · dark mode = invertir colores (texto `#fff` sobre `#000`, imágenes quemadas) · newsletter popup antes de leer una línea · captions centradas sin relación con su imagen · el "blog default" (plantilla única, gris sobre gris, cero jerarquía/art direction).

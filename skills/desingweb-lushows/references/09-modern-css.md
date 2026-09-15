# 09 — CSS moderno (2025-2026): features que elevan el diseño

Guía accionable de CSS de vanguardia con buen soporte real. Cada feature: **qué es**, **para qué sirve en diseño**, **snippet copy-paste** y **soporte/fallback**. Datos de soporte verificados contra MDN, web.dev, Chrome for Developers y State of CSS 2025.

> Regla de oro: usa lo moderno como *mejora progresiva*. Si la feature falla, la página debe seguir siendo usable. Envuelve lo arriesgado en `@supports`.

---

## 1. `:has()` — el selector padre (y mucho más)

**Qué es:** selecciona un elemento según lo que contiene o según el estado de sus hijos/hermanos. Es el primer selector "hacia arriba" de CSS.

**Para qué sirve en diseño:** estados de UI sin JavaScript. Cambiar el layout de una card si tiene imagen, resaltar un formulario con error, atenuar el resto de cards cuando una está en hover, theming según contenido.

```css
/* Card con imagen: layout de 2 columnas. Sin imagen: 1 columna */
.card:has(img) { grid-template-columns: 120px 1fr; }

/* Form con un input inválido: borde rojo en el contenedor */
form:has(:invalid) { border-color: oklch(62% 0.22 25); }

/* Hover en una card => atenúa las hermanas (efecto "spotlight") */
.grid:has(.card:hover) .card:not(:hover) { opacity: .5; filter: saturate(.6); }

/* Layout reactivo a un checkbox => menú/drawer sin JS */
body:has(#nav-toggle:checked) .drawer { translate: 0 0; }
```

**Soporte:** Baseline (todas las modernas) desde dic-2023. Sólido en Chrome/Edge/Safari/Firefox.
**Fallback:** el estilo base ya debe verse bien; `:has()` sólo añade el "extra". Para cosas críticas, replica con JS toggleando una clase.

---

## 2. Container Queries — `@container`

**Qué es:** media queries pero respecto al **tamaño del contenedor padre**, no del viewport. Un componente decide su layout según el espacio que tiene, no según la pantalla.

**Para qué sirve en diseño:** componentes verdaderamente reutilizables. La misma card se ve compacta en un sidebar y amplia en el main, sin saber dónde está.

```css
.card-zone { container-type: inline-size; container-name: card; }

.card { display: grid; gap: .5rem; }

@container card (min-width: 30rem) {
  .card { grid-template-columns: 160px 1fr; align-items: center; }
  .card h3 { font-size: 1.5rem; }
}

/* Unidades de contenedor: tipografía relativa al contenedor */
.card h3 { font-size: clamp(1rem, 5cqi, 2rem); } /* cqi = 1% del inline del contenedor */
```

**Soporte:** Baseline **Widely available** (ago-2025). Producción sin miedo.
**Fallback:** si no hay soporte, el contenedor usa el layout base (mobile-first). Envuelve en `@supports (container-type: inline-size){}` si quieres ser explícito.

---

## 3. Subgrid

**Qué es:** permite que un grid hijo herede las pistas (filas/columnas) del grid padre, alineando elementos a través de componentes anidados.

**Para qué sirve en diseño:** alinear cabeceras, cuerpos y footers de varias cards en una fila aunque tengan distinta cantidad de texto. Adiós a alturas fijas y hacks.

```css
.cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }

.card {
  display: grid;
  grid-row: span 3;            /* ocupa 3 filas del padre */
  grid-template-rows: subgrid; /* hereda esas filas: title / body / footer alineados */
}
```

**Soporte:** ~97% global (2025). Chrome 117+, Safari 16+, Firefox 71+, Edge 118+. Seguro en producción.
**Fallback:** sin subgrid, cada card usa su propio grid (se ve bien, sólo pierde la alineación perfecta entre cards).

---

## 4. Tipografía fluida con `clamp()`

**Qué es:** `clamp(MIN, PREFERIDO, MAX)` escala un valor entre dos límites usando una unidad de viewport en el medio. Tipografía y spacing responsive **sin media queries**.

**Para qué sirve en diseño:** ritmo tipográfico continuo. El H1 crece suave de móvil a desktop sin saltos bruscos.

```css
:root {
  /* min 2rem, escala con viewport, max 4.5rem */
  --step-h1: clamp(2rem, 1.2rem + 4vw, 4.5rem);
  --step-body: clamp(1rem, 0.95rem + 0.4vw, 1.125rem);
  --space-section: clamp(3rem, 8vw, 8rem);
}
h1 { font-size: var(--step-h1); line-height: 1.05; }
body { font-size: var(--step-body); }
section { padding-block: var(--space-section); }
```

Tip: la parte `rem + vw` (no sólo `vw`) garantiza que el zoom y el redimensionado respeten accesibilidad. Usa una calculadora tipo Utopia para generar la escala completa.

**Soporte:** universal desde 2020. Sin reservas.

---

## 5. Color moderno: OKLCH + `color-mix()`

**Qué es:** OKLCH es un espacio de color perceptual (`oklch(L C H)` = luminosidad / croma / matiz). Mantiene la luminosidad consistente entre colores y produce gradientes sin "zonas muertas grises". `color-mix()` mezcla dos colores en el espacio que elijas.

**Para qué sirve en diseño:** paletas coherentes (mismo L = mismo "peso visual"), estados hover/active derivados con una sola línea, gradientes vívidos.

```css
:root {
  --brand: oklch(62% 0.19 250);          /* azul */
  --brand-hover: oklch(from var(--brand) calc(l - 0.08) c h); /* relative color: -8% luz */
  --surface: oklch(98% 0.01 250);
}

.btn { background: var(--brand); }
.btn:hover { background: var(--brand-hover); }

/* Tinte: 85% superficie + 15% marca, mezclado en oklch */
.tag { background: color-mix(in oklch, var(--brand) 15%, white); }

/* Gradiente vívido sin midpoint sucio */
.hero { background: linear-gradient(in oklch 135deg, oklch(70% 0.2 30), oklch(70% 0.2 280)); }
```

**Soporte:** OKLCH y `color-mix()` en Chrome/Edge 111+, Safari 16.2+, Firefox 113+ (~95% del tráfico, 2025). *Relative color syntax* (`oklch(from ...)`) es más nuevo: úsalo con fallback.
**Fallback:** declara primero un color hex/`rgb()` y luego el oklch; el navegador antiguo ignora la línea que no entiende.

```css
.btn { background: #3b6fe0; background: var(--brand); }
```

---

## 6. `@property` — animar lo que antes no se podía

**Qué es:** registra una custom property con tipo (`<angle>`, `<color>`, `<number>`...). Al tener tipo, el navegador **puede interpolarla**, así que ahora puedes *animar* ángulos de gradiente, posiciones cónicas, etc.

**Para qué sirve en diseño:** bordes brillantes giratorios, gradientes que rotan, efectos "premium" sin JS ni SVG.

```css
@property --angle {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

/* Borde cónico giratorio brillante */
.glow {
  position: relative;
  border-radius: 1rem;
  background: #0b0b10;
}
.glow::before {
  content: "";
  position: absolute; inset: -2px;
  border-radius: inherit;
  padding: 2px;
  background: conic-gradient(from var(--angle),
    oklch(70% 0.2 280), oklch(70% 0.2 30), oklch(70% 0.2 280));
  /* recorta el relleno y deja sólo el "marco" */
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor; mask-composite: exclude;
  animation: spin 4s linear infinite;
}
@keyframes spin { to { --angle: 360deg; } }
```

**Soporte:** Chrome/Edge 85+, Safari 16.4+, **Firefox 128+** (ya disponible en todas las modernas, 2025).
**Fallback:** sin `@property` el `--angle` no anima; el borde se queda estático pero igual con el gradiente bonito. Acepta el degradado.

---

## 7. View Transitions API (same-document y cross-document)

**Qué es:** anima la transición entre dos estados del DOM (o entre dos páginas) con un crossfade/morph automático del navegador. Captura el "antes" y "después" y los interpola.

**Para qué sirve en diseño:** transiciones tipo app nativa: una miniatura que se expande a detalle, navegación entre páginas con elementos que persisten (hero shared element).

```js
/* Same-document (SPA / cambios de estado) */
document.startViewTransition(() => {
  updateTheDOM(); // tu cambio de estado / re-render
});
```

```css
/* Nombra elementos que deben "viajar" entre estados */
.card-hero { view-transition-name: hero; }

/* Personaliza la animación */
::view-transition-old(hero),
::view-transition-new(hero) { animation-duration: .4s; }
```

```css
/* Cross-document (MPA / navegación entre páginas) — sólo Chromium hoy */
@view-transition { navigation: auto; }
```

**Soporte same-document:** Chrome/Edge 111+, Safari 18+, **Firefox 144+** (oct-2025) → Baseline newly available.
**Soporte cross-document (`@view-transition`):** sólo Chromium (Chrome 126+). Firefox/Safari ignoran el at-rule.
**Fallback:** es 100% mejora progresiva. Sin soporte, el DOM cambia al instante (sin animación). No rompe nada. Usa el patrón:

```js
if (!document.startViewTransition) { updateTheDOM(); return; }
document.startViewTransition(() => updateTheDOM());
```

---

## 8. Scroll Snap

**Qué es:** hace que un contenedor "encaje" en puntos concretos al hacer scroll. Carruseles y secciones full-screen con un par de líneas.

**Para qué sirve en diseño:** galerías horizontales, slideshows, secciones de pantalla completa que se alinean perfecto.

```css
.gallery {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  gap: 1rem;
  scroll-padding: 1rem;
}
.gallery > * {
  flex: 0 0 80%;
  scroll-snap-align: center;
  scroll-snap-stop: always; /* no saltarse items con un flick fuerte */
}

/* Secciones full-screen verticales */
.story { scroll-snap-type: y mandatory; overflow-y: auto; height: 100dvh; }
.story > section { scroll-snap-align: start; min-height: 100dvh; }
```

**Soporte:** Baseline desde abr-2022. Universal. Combínalo con `scroll-behavior: smooth`.

---

## 9. Scroll-driven animations — `animation-timeline`

**Qué es:** vincula una animación al **progreso del scroll** (no al reloj). `scroll()` = progreso del scroller; `view()` = visibilidad del elemento dentro del viewport. Corre en el compositor (suave, sin JS por frame).

**Para qué sirve en diseño:** barras de progreso de lectura, parallax, reveals al entrar en pantalla, encogimiento de header.

```css
@keyframes reveal { from { opacity: 0; translate: 0 2rem; } to { opacity: 1; translate: 0; } }

.section {
  animation: reveal linear both;
  animation-timeline: view();         /* progresa según entra en viewport */
  animation-range: entry 0% cover 35%;
}

/* Barra de progreso de lectura */
.progress {
  transform-origin: left;
  animation: grow linear both;
  animation-timeline: scroll(root block);
}
@keyframes grow { from { scale: 0 1; } to { scale: 1 1; } }
```

**Soporte:** Chrome/Edge 115+. Firefox tras flag / llegando; Safari aún no completo (2025).
**Fallback:** envuelve en `@supports (animation-timeline: scroll())`. Sin soporte, el contenido simplemente aparece visible (estado final). Para reveals críticos, usa IntersectionObserver como respaldo. Respeta `@media (prefers-reduced-motion: reduce)`.

---

## 10. `text-wrap: balance` y `pretty`

**Qué es:** `balance` reparte el texto en líneas de longitud pareja (ideal para titulares). `pretty` evita "huérfanas" (una sola palabra en la última línea) en párrafos.

**Para qué sirve en diseño:** titulares que no dejan una palabra colgando; tipografía pulida sin `<br>` manuales.

```css
h1, h2, h3, .lead { text-wrap: balance; }   /* titulares equilibrados */
p { text-wrap: pretty; }                     /* párrafos sin huérfanas */
```

**Soporte:** `balance` en todas las modernas (Baseline). `pretty` en Chromium y Safari 17.5+; Firefox lo está adoptando.
**Fallback:** sin soporte, el texto envuelve como siempre (degradación invisible). Cero riesgo. `balance` se limita a ~6 líneas por rendimiento.

---

## 11. `backdrop-filter` — glassmorphism

**Qué es:** aplica filtros (blur, saturate) a lo que está **detrás** de un elemento.

**Para qué sirve en diseño:** navbars y cards "de vidrio", modales con fondo difuminado, overlays elegantes.

```css
.glass {
  background: color-mix(in oklch, white 12%, transparent);
  backdrop-filter: blur(14px) saturate(160%);
  -webkit-backdrop-filter: blur(14px) saturate(160%); /* Safari */
  border: 1px solid color-mix(in oklch, white 25%, transparent);
}
```

**Soporte:** Baseline newly available. Chrome 76+, Firefox 103+, Safari 9+ (necesita `-webkit-`), Edge 17+.
**Fallback:** si falla, deja un fondo semi-opaco sólido para mantener contraste/legibilidad.

---

## 12. `mask`, `clip-path` y `mix-blend-mode`

**Qué es:** `clip-path` recorta formas geométricas; `mask` recorta con imágenes/gradientes (bordes suaves, fades); `mix-blend-mode` mezcla un elemento con el fondo como en Photoshop.

**Para qué sirve en diseño:** secciones diagonales, fades de imagen en los bordes, texto que invierte color sobre cualquier fondo, efectos "duotone".

```css
/* Sección con corte diagonal */
.hero { clip-path: polygon(0 0, 100% 0, 100% 88%, 0 100%); }

/* Fade suave en el borde inferior de una imagen */
.fade-img { -webkit-mask: linear-gradient(#000 70%, transparent); mask: linear-gradient(#000 70%, transparent); }

/* Texto que se adapta al fondo (logos sobre imágenes) */
.overlay-text { mix-blend-mode: difference; color: white; }
```

**Soporte:** `clip-path` y `mix-blend-mode` universales. `mask` requiere `-webkit-mask` en Safari/algunos. Mejoras puramente estéticas → fallback = sin recorte.

---

## 13. Anchor Positioning (úsalo con cuidado)

**Qué es:** posiciona un elemento (tooltip, popover, menú) anclado a otro sin JavaScript ni offsets frágiles, con manejo automático de overflow (`position-try`).

**Para qué sirve en diseño:** tooltips, dropdowns y popovers que se reubican solos si no caben.

```css
.btn { anchor-name: --trigger; }
.tooltip {
  position: absolute;
  position-anchor: --trigger;
  top: anchor(bottom); left: anchor(center);
  position-try-fallbacks: flip-block, flip-inline; /* se voltea si no cabe */
}
```

**Soporte:** Chrome/Edge 125+. Safari 26 y Firefox aún detrás de flag (no Baseline en 2025).
**Fallback:** imprescindible respaldo con Floating UI / posicionamiento JS, o envolver en `@supports (anchor-name: --x)`. No lo uses como única vía en producción crítica todavía.

---

## Combos que se ven caros (pero son baratos)

1. **Borde brillante giratorio:** `@property` (`<angle>`) + `conic-gradient(from var(--angle))` + `mask-composite: exclude` para vaciar el centro. Marco neón animado, cero JS. (ver §6)

2. **Spotlight de cards:** `:has()` + `:not(:hover)` → al pasar sobre una card, las demás bajan opacidad y saturación. Sensación premium, sin una línea de JavaScript.
   ```css
   .grid:has(.card:hover) .card:not(:hover) { opacity: .45; scale: .98; }
   ```

3. **Hero con shared element:** `view-transition-name: hero` en la miniatura y en la página de detalle + `@view-transition { navigation: auto; }`. La imagen "vuela" entre páginas como app nativa. (ver §7)

4. **Reveal de secciones sin librería:** `animation-timeline: view()` + `@keyframes` de fade/translate. Reemplaza AOS.js entero. Respeta `prefers-reduced-motion`. (ver §9)

5. **Glass navbar coherente:** `backdrop-filter: blur() saturate()` + `color-mix(in oklch, white 12%, transparent)` para el tinte + borde con `color-mix`. Vidrio real con paleta consistente. (ver §11 y §5)

6. **Tema hover derivado:** un solo color base en OKLCH y deriva hover/active/disabled con `calc(l ± 0.08)` o `color-mix`. Paleta entera desde una variable. (ver §5)

7. **Titular perfecto:** `text-wrap: balance` en el H1 + tipografía fluida `clamp()` + `line-height: 1.05`. Titular que respira igual en cualquier ancho. (ver §4 y §10)

---

### Plantilla `@supports` para mejoras arriesgadas

```css
/* Base sólida primero */
.reveal { opacity: 1; }

@supports (animation-timeline: view()) {
  .reveal { opacity: 0; animation: fade-in linear both; animation-timeline: view(); }
}
@media (prefers-reduced-motion: reduce) {
  .reveal, .glow::before { animation: none; opacity: 1; }
}
```

**Mantra:** diseño base que funciona en todo → capa de lujo moderna encima → respeta `prefers-reduced-motion`. Así nunca rompes y siempre impresionas donde el navegador lo permite.

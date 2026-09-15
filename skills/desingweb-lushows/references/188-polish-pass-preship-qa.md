# 188 — The polish pass & pre-ship QA checklist

**CRAFT.** El último-milla que separa "done" de "shipped-with-pride" (distinto de handoff/48). Pareja de 48 (testing/handoff), 06 (anti-slop), 16 (a11y), 40 (performance). Regla de oro: **el last 10% (polish) es lo único que el usuario percibe como calidad — la diferencia entre functional y crafted son cien fixes pequeños; pasa la lista con *fresh eyes*, no de memoria.**

## 1. The mindset

Nadie nota un border-radius consistente; todos notan el de 1px desalineado. **Fresh-eyes pass** (revisa desfamiliarizado — al día siguiente, en otro dispositivo, en incógnito, o a 50% zoom para romper el patrón perceptivo). **Polish como respeto** (lo amateur no es feo, es *descuidado*). **Squint test** (entrecierra los ojos — la jerarquía debe sobrevivir el desenfoque). Es una **disciplina separada** del diseño: QA de craft con checklist.

## 2. Visual polish pass
☐ **Optical alignment, no solo mathematical** (iconos/flechas/glifos ajustados ópticamente; texto en botón a veces -1px vertical) · ☐ **spacing en escala 8pt/4pt** (cero valores mágicos `13px`) · ☐ **border-radius consistente** (nested: externo = interno + padding) · ☐ **shadow consistente** (una escala, misma dirección de luz) · ☐ **alignment a grid** · ☐ **state parity en CADA interactivo** (default/hover/focus/active/disabled — el disabled el más olvidado) · ☐ **orphans & widows** (`text-wrap:balance` headings, `pretty` párrafos, `&nbsp;` en CTAs) · ☐ **image quality/aspect** (`object-fit:cover`, retina 2x, `aspect-ratio`) · ☐ **dark-mode parity** (borders en vez de shadows, imágenes que no queman) · ☐ **consistencia de case**.

## 3. Interaction & state QA
☐ **todos los estados** (default/hover/focus/active/loading/empty/error — empty y error los más abandonados) · ☐ **loading feedback** (skeleton/spinner, nunca pantalla en blanco; >400ms necesita feedback) · ☐ **transiciones con tokens** (misma duration/easing) · ☐ **`:focus-visible` en todo** (nunca `outline:none` sin reemplazo) · ☐ **touch targets ≥44×44px** + separación · ☐ **el back button** (no pierde datos/estado) · ☐ **form validation se siente bien** (inline, accionable, no agresiva antes de terminar) · ☐ **no dead-ends** · ☐ **un CTA primario por pantalla** en flujos críticos.

## 4. Responsive & cross-device
☐ **cada breakpoint 320px → ultrawide ≥2560px** (probar mínimo real iPhone SE y máximo) · ☐ **los awkward in-between** (redimensiona continuamente; los bugs viven en 600-800 y 900-1100px) · ☐ **dispositivos reales** (iOS `env(safe-area-inset-*)`, notch/Dynamic Island, barra Safari) · ☐ **landscape** móvil · ☐ **text-zoom 200%** (WCAG 1.4.4) · ☐ **content-not-cut** (sin scroll horizontal accidental) · ☐ **long-content & no-content** (nombre de 60 chars, carrito vacío, lista de 1000, avatar sin imagen).

## 5. Performance & technical QA
☐ **CWV en verde (campo)** — **LCP <2.5s, INP <200ms, CLS <0.1** (INP el más fallado 2026, solo ~48% de páginas móviles pasa las tres) · ☐ **cero layout shift** (`width/height`/`aspect-ratio`, `size-adjust` en fonts, reservar espacio) · ☐ **imágenes optimizadas** (AVIF/WebP, `srcset`/`sizes`, lazy bajo el fold, `fetchpriority="high"` en el LCP) · ☐ **fonts sin FOUT/FOIT** (`font-display:swap`/`optional`, preload, `size-adjust`, subset) · ☐ **console limpia** (cero errors/404/mixed-content) · ☐ **lazy-load + code-splitting + diferir terceros** · ☐ **the slow-3G test** (throttle Slow 3G + 4× CPU — ¿sigue usable? ¿aparecen los skeletons?) · ☐ **bundle check**.

## 6. A11y, content & cross-browser (pre-launch final)
**A11y:** ☐ keyboard-only pass (Tab/Shift-Tab/Enter/Esc, orden lógico, foco nunca atrapado, skip-link) · ☐ screen-reader spot-check (landmarks, un solo `h1`, labels, `aria-live`) · ☐ contraste WCAG AA + APCA en límites · ☐ alt text real / `alt=""` decorativas · ☐ `prefers-reduced-motion`. **Content:** ☐ proofread (cero lorem/"Test"/"asdf"/placeholders/fechas hardcodeadas) · ☐ microcopy con tono ("Crear cuenta" no "Submit") · ☐ números/monedas/fechas localizados. **Cross-browser:** ☐ Safari/Firefox/Chrome/Edge (Safari rompe `gap`/`:has`/fechas/`backdrop-filter`). **Pre-launch técnico:** ☐ 404 y 500 diseñados · ☐ favicon completo + meta title/description + **OG/Twitter cards** (probar en el debugger) + `theme-color` · ☐ `robots.txt`/`sitemap.xml`/canonical/`lang`/structured data + **`noindex` removido de staging** (el clásico que mata lanzamientos) · ☐ HTTPS/redirects/analytics/legales.

**Regla de cierre:** imprime el checklist y pásalo en una sesión con fresh eyes. Lo crafted no es talento — es **no saltarse la lista**.

## Skipped-polish anti-patterns — blacklist
**`outline:none` sin focus alternativo** · **disabled-state inexistente o = default** · **empty/error sin diseñar** · **valores mágicos de spacing** (`23px`) · **imágenes sin `width/height`** (CLS) · **sombras/radios inconsistentes** · **lorem/"Test" en producción** · **`noindex` heredado de staging** · **OG tags ausentes** (link feo al compartir) · **touch targets <44px pegados** · **hover-only affordances** (rotos en touch) · **auto-play/parallax ignorando `prefers-reduced-motion`** · **scroll horizontal accidental en móvil** · **probar solo en Chrome desktop a 1440px** · **validación que grita antes de terminar de escribir** · **viudas/huérfanas en titulares**.

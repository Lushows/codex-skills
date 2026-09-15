# 16 — Accesibilidad & diseño inclusivo (sin matar la estética)

Playbook práctico WCAG 2.2 / 2026. Premisa: accesibilidad y diseño premium NO chocan. El 99% se resuelve con HTML semántico, `:focus-visible` (no `:focus`) y respetar `prefers-*`. Lo que mata la a11y casi nunca es la estética: son `<div onclick>`, `outline:none` sin reemplazo y `placeholder` como `label`. **Repásalo antes de entregar cualquier proyecto** (es parte de la calidad, junto con `06-anti-slop`).

## 1. WCAG 2.2 (oct-2023) — los criterios que importan a UI premium

- **2.4.11 Focus Not Obscured (AA):** el elemento enfocado no puede quedar tapado por sticky headers/cookie bars. Usa `scroll-padding-top` igual a la altura del header.
- **2.4.13 Focus Appearance (AA):** indicador de foco ≥ borde de **2px CSS** alrededor, **contraste ≥3:1** entre enfocado/no enfocado.
- **2.5.7 Dragging (AA):** todo drag (sliders, reordenar) necesita **alternativa de un puntero** (botones +/−, click). No drag-only.
- **2.5.8 Target Size (AA):** targets **24×24px CSS** mín (44×44 ideal, guía Apple). Iconos: agranda el hit area con padding/pseudo-elemento, no el glifo.
- **3.2.6 Consistent Help (A):** ayuda (chat/tel/FAQ) en el mismo orden relativo en todas las páginas.
- **3.3.7 Redundant Entry (A):** no re-pedir info ya ingresada (autofill, "igual que envío").
- **3.3.8 Accessible Authentication (AA):** no exigir puzzles/recordar/transcribir CAPTCHA sin alternativa. Permite paste en password/OTP, respeta `autocomplete="one-time-code"`.

**APCA / WCAG 3.0 (estado 2026):** WCAG 3.0 sigue en Working Draft, sin fecha; APCA fue retirado del borrador (exploratorio). **WCAG 2.1/2.2 AA es el estándar legal** (ADA, EAA europeo). Práctica: **cumple 4.5:1 como piso legal, usa APCA para tuning perceptual.** APCA da un valor **Lc** (~−108 a +108) que modela percepción real. Targets: body 16px → **Lc 75**; microcopy 12-14px → Lc 75-90; headings 24px+ bold → Lc 45-60. Captura un problema que 4.5:1 ignora (grises sobre fondo oscuro). Tools: `contrast.tools` (tab APCA), `apcacontrast.com`.

## 2. HTML semántico + ARIA bien hecho

**Primera regla de ARIA:** no uses ARIA si un elemento HTML nativo ya da la semántica + comportamiento. `<button>` ya es focusable, activable con Enter/Space y se anuncia como botón; `<div role="button" tabindex="0">` te obliga a reimplementar todo (y casi siempre mal).
- **Landmarks:** una sola `<main>`, `<header>`/`<footer>`, `<nav>` (etiqueta varios con `aria-label`), `<aside>`. No envuelvas todo en `<div>`.
- **Headings:** un `<h1>` por página, sin saltar niveles. Los SR navegan por headings = la tabla de contenidos del usuario ciego.
- **Accessible name** (precedencia): `aria-labelledby` > `aria-label` > contenido > `title`. Iconos sin texto: `<button aria-label="Cerrar"><svg aria-hidden="true" focusable="false">…</svg></button>`. SVG decorativo SIEMPRE `aria-hidden="true"`.
- **ARIA más mal usado:** `aria-label` en spans/divs que no aceptan nombre, `role="button"` sin teclado, `aria-hidden="true"` sobre algo focusable (atrapa foco fantasma), roles redundantes.

## 3. Teclado y foco — focus rings premium

Nunca `outline:none` a secas. Usa `:focus-visible` (teclado, no click). Truco premium: **doble anillo** (destaca sobre cualquier fondo):
```css
:where(a,button,input,select,textarea,[tabindex]):focus-visible{
  outline:3px solid var(--focus,#111); outline-offset:2px;
  box-shadow:0 0 0 6px #fff; border-radius:inherit;        /* halo -> visible en oscuro */
}
:focus:not(:focus-visible){ outline:none; }                 /* sin ring en mouse */
```
- **Skip link** (primer focusable): `.skip-link{position:absolute;left:-9999px} .skip-link:focus{position:fixed;left:1rem;top:1rem;z-index:999}`.
- **Focus order = orden del DOM.** No reordenes con `order`/`position` rompiendo el Tab. **Nunca `tabindex` positivo (>0).**
- **Roving tabindex** para widgets compuestos (tabs/menus/grids): solo el activo `tabindex="0"`, resto `-1`; flechas mueven foco. Alt: `aria-activedescendant`.
- **Restaurar foco:** al cerrar modal/drawer → `triggerEl.focus()`.

## 4. Componentes premium accesibles (patrones APG)

- **Modal/Dialog:** usa `<dialog>` nativo. `showModal()` **ya** atrapa foco, bloquea fondo, habilita Esc, da `::backdrop`. La "trampa de foco" manual es consejo obsoleto con `<dialog>`. `aria-labelledby` al título; `close` → restaura foco al trigger.
- **Toasts** (live region): región pre-renderizada vacía, inserta texto en un paso.
  ```html
  <div aria-live="polite" aria-atomic="true" class="sr-status"></div> <!-- éxito/info -->
  <div role="alert" class="sr-status"></div>                          <!-- error crítico -->
  ```
  `polite` para éxito/info/loading; `assertive`/`role="alert"` SOLO errores que interrumpen. Máx 2 live regions.
- **Form validation:** `<label for>` + `aria-invalid="true"` + `aria-describedby="err-id"` + error en texto (no solo borde rojo) + `autocomplete`.
- **Custom select/combobox:** APG Select-Only Combobox (foco en el combobox, `aria-activedescendant`, `aria-expanded`, `role=listbox/option`). Si no necesitas estética custom → `<select>` nativo.
- **Tabs:** `role=tablist/tab/tabpanel`, `aria-selected`, roving tabindex, flechas + Home/End.
- **Accordion:** `<details><summary>` nativo (teclado/foco/semántica gratis).
- **Tooltip:** nunca info esencial solo en hover; accesible por teclado (`:focus-within`) y descartable con Esc (1.4.13). Sin interactivos dentro.
- **Carousel:** botón de pausa para auto-play (2.2.2).

## 5. Visual y motion a11y

```css
@media (prefers-reduced-motion: reduce){ *,*::before,*::after{ animation-duration:.01ms!important; animation-iteration-count:1!important; transition-duration:.01ms!important; scroll-behavior:auto!important } }
@media (prefers-contrast: more){ :root{ --fg:#000; --bg:#fff } }
@media (prefers-reduced-transparency: reduce){ .glass{ backdrop-filter:none; background:#fff } }
@media (forced-colors: active){ .btn{ border:1px solid ButtonText } }  /* usa system colors */
```
- **Color no solo:** estado nunca solo por color (error → + icono + texto). 1.4.1.
- **Zoom/resize:** funciona a 200% (1.4.4) y reflow a 400% sin scroll horizontal (1.4.10). Usa `rem`/`clamp()`, evita alturas fijas en px que recortan texto.
- **Forms:** cada input con `<label for>` (o `aria-labelledby`); `autocomplete` correcto (1.3.5). El placeholder NO es label.

## 6. Screen readers + testing

Testea con **≥2**: NVDA + Firefox/Chrome (gratis, amplio) y VoiceOver + Safari (Apple). JAWS/NVDA interpretan ARIA distinto; VO es más permisivo → lo que funciona en VO puede fallar en NVDA.
**sr-only correcto:**
```css
.sr-only{ position:absolute; width:1px; height:1px; padding:0; margin:-1px; overflow:hidden; clip:rect(0 0 0 0); clip-path:inset(50%); white-space:nowrap; border:0 }
```
No metas focusables dentro de `.sr-only` (atrapa foco invisible). No abuses de texto oculto verboso.
**Alt text:** decorativo → `alt=""` (vacío, no omitir); informativo → describe función/contenido (no "imagen de…"); complejo (gráficos) → resumen en `alt` + descripción larga adyacente; imagen en link → describe el destino.
**Checklist:** (1) automático axe DevTools (capta ~30-40%) > Lighthouse > WAVE/Pa11y CI; (2) teclado manual (Tab/Shift+Tab/Enter/Space/flechas/Esc — foco visible, orden lógico, sin trampas, modales devuelven foco); (3) SR pass NVDA+VO; (4) zoom 200/400%, reduced-motion ON, forced-colors.

## A11y anti-patterns — blacklist
`outline:none` sin reemplazo · `<div>/<span>` con onclick en vez de `<button>/<a>` · placeholder como única etiqueta · `tabindex` positivo · `aria-hidden` sobre focusable · color como único indicador · `<a href="#">`/`javascript:void(0)` para acciones · info esencial solo en hover · `role="button"` sin Enter/Space · auto-play con sonido sin pausa · skip link ausente · `alt` ausente (≠ `alt=""`) o `alt="imagen"` · live region poblada en el mismo tick en que se crea · confiar 100% en el scanner automático.

# 357 · Web performance y Core Web Vitals (el campo manda, no el lab)

> Google rankea con datos de usuarios REALES (CrUX p75), no con tu Lighthouse de laptop.
> El cuello de botella de 2026 es INP: ~43% de sitios lo fallan y casi nadie lo mide bien.

## Umbrales "good" 2026 (p75 de campo)
| Métrica | Mide | Good | Needs-improvement | Poor |
|---|---|---|---|---|
| LCP | carga del bloque mayor | ≤2.5s | 2.5–4.0s | >4.0s |
| INP | peor interacción→paint de la sesión | ≤200ms | 200–500ms | >500ms |
| CLS | estabilidad visual (sin unidad) | ≤0.1 | 0.1–0.25 | >0.25 |

Google evalúa al **p75**: 75% de las visitas deben estar en "good" para pasar. INP reemplazó a FID
en marzo 2024 (FID solo medía el *primer* delay, no el coste total de procesar). [no verificado] circula
que el March-2026 core update bajó LCP a 2.0s — la doc oficial de Google sigue en 2.5s; trátalo como rumor.

## INP: el problema #1 (parte las long tasks)
INP = peor latencia interacción-a-paint. Causa raíz: **long tasks (>50ms)** que bloquean el main thread.
El mayor lever es estructural: **shippea MENOS JavaScript**. Tácticas inmediatas:
```js
async function handleClick(){
  updateUIImmediately();          // pinta el feedback YA
  await scheduler.yield();        // cede el hilo a mitad de interacción (Chrome 129+)
  doExpensiveWork();              // el trabajo caro va después del paint
}
```
**RSC/streaming SSR** es el fix de fondo: los Server Components shippean **cero JS cliente** en las partes
no interactivas (casos reportados: −62% bundle, ~3× render). Ojo: SSR plano mejora LCP/FCP del *initial
load* pero NO arregla INP — hidratar un árbol interactivo gigante reintroduce las long tasks.

## LCP: descubre el recurso crítico antes
- `<link rel=preload>` + `fetchpriority="high"` en la imagen/fuente del hero; **nunca** `loading="lazy"` en la imagen LCP.
- Critical CSS inline en `<head>`; difiere el resto con `media="print"`→onload o `rel=preload`.
- Fuentes: `preconnect` al origen, `font-display: swap` **con fallback `size-adjust`** (evita reflow→CLS).
- TTFB <200ms (CDN edge + cache, ver [[358-caching-strategy-multilayer]]); WebP/AVIF (~30% < JPEG).

## CLS: reserva el espacio
`width`/`height` o `aspect-ratio` en **todo** media/iframe/ad. Reserva caja para contenido async
(banners, embeds, "skeleton" del mismo tamaño). Inyecta nada por encima de contenido ya pintado.

## Bundle, code-split, terceros
Code-split por ruta + `import()` lazy; tree-shaking real exige ESM y `sideEffects:false` en package.json.
**Terceros (analytics/chat/ads) son los top regresores de INP/CLS** → `defer`, facade (carga el chat solo
al click), o sandbox en iframe. Auditá el coste con `performance.measure` por tarea, no por intuición.

## Lab vs campo (el error caro)
**Lighthouse** = una carga sintética en hardware rápido. **CrUX** = agregado 28-días de usuarios reales —
y **CrUX manda en el ranking**, no Lighthouse. Un Lighthouse 100 con CrUX fallando es habitual (red lenta,
fuentes/ads tardíos, dispositivos de gama baja). Tras un fix, esperá ~28-30 días para que Search Console
refleje el campo. Medí en producción con `web-vitals` JS + RUM, no solo en CI.

## Gotchas
1. Preload de *todo* → contención de ancho de banda; preload **solo** el recurso LCP.
2. CLS aparece solo bajo throttle (red 3G, fuentes/ads tardíos) — testealo con CPU/red ralentizada.
3. `scheduler.yield()` no existe en Safari/Firefox 2026 — feature-detect y cae a `setTimeout(0)`.
4. Mejorar el p50 no mueve el ranking si el **p75** (móvil gama baja) sigue en poor.

Cruza con [[89-web-performance-profunda]], [[358-caching-strategy-multilayer]] y [[360-load-testing-web]].

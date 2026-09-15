# 279 · Animación web: Motion, GSAP, View Transitions

> El 90% de la animación de producto es transform+opacity. Lo demás es saber qué NO animar
> (layout) y cuándo soltar React por la GPU. Motion fluido = 60fps en el compositor, no en el main thread.

## La física del frame: solo anima transform y opacity
El navegador pinta en capas. Animar `width/top/margin` dispara **layout + paint** en cada frame (jank).
Animar `transform`/`opacity` solo toca el **compositor** (GPU), salta layout y paint.

```css
/* ❌ layout thrash */ .x{ transition: width .3s, top .3s }
/* ✅ compositor    */ .x{ transition: transform .3s, opacity .3s }
```
`will-change: transform` promueve a capa propia (úsalo puntual; abusar consume VRAM). Ver [[89-web-performance-profunda]].

## Motion (ex Framer-Motion): el default React
Paquete ahora independiente (`motion`, antes `framer-motion`). Declarativo, maneja layout animations
(FLIP automático), gestos y orquestación.

```jsx
import { motion, AnimatePresence } from 'motion/react'
<AnimatePresence>
  {open && <motion.div
    initial={{ opacity:0, y:8 }} animate={{ opacity:1, y:0 }} exit={{ opacity:0, y:8 }}
    transition={{ type:'spring', stiffness:300, damping:30 }} />}
</AnimatePresence>
<motion.div layout />   // FLIP: anima cambios de layout sin calcular deltas a mano
```
- `AnimatePresence` anima desmontaje (exit) — React solo no puede.
- `layoutId` compartido = transición magic-move entre dos componentes distintos.
- Spring > duration para gestos: responde a velocidad, se siente físico.

## GSAP: timelines, scroll, lo que Motion no
Para secuencias complejas, scroll-driven y SVG/canvas pesado. `ScrollTrigger` es el estándar.
GSAP es agnóstico de framework — vive fuera del ciclo de React, limpia en cleanup.

```js
useGSAP(() => {
  gsap.to('.hero', { x:200, scrollTrigger:{ trigger:'.hero', scrub:1, pin:true } })
}, { scope: ref })   // useGSAP auto-revierte al desmontar
```

## View Transitions API (nativo, sin lib)
Cross-fade/morph entre estados o rutas con cero JS de animación. Soporte amplio en 2026; degrada limpio.
```js
document.startViewTransition(() => updateDOM())        // SPA
// CSS: ::view-transition-old(root)/new(root) + view-transition-name para elementos compartidos
```
React 19 expone `<ViewTransition>` experimental; Next App Router lo integra para transiciones de ruta.

| Necesidad | Herramienta |
|---|---|
| Enter/exit, gestos, layout en React | Motion |
| Scroll-driven, timelines, SVG morph | GSAP + ScrollTrigger |
| Transición de ruta/estado simple | View Transitions nativo |
| 3D / shaders / partículas | Three.js (ver [[75-webgl-threejs-shaders-creative-coding]]) |

## Performance de motion
- Mide capas y FPS en DevTools → Rendering → "Layer borders" + "Paint flashing".
- `prefers-reduced-motion`: respétalo SIEMPRE, recorta a opacidad o desactiva (a11y + legal).
- No animes 50 elementos a la vez en main thread; usa `stagger` y CSS donde puedas.
- JS animando `style.left` en rAF = el anti-patrón clásico; pásalo a transform.

## Gotchas
1. `will-change` permanente fragmenta memoria de GPU — ponlo on-hover, quítalo al terminar.
2. Animar height "auto" no es interpolable; usa `grid-template-rows: 0fr→1fr` o `max-height`.
3. `layout` de Motion + contenido de texto cambiante = distorsión; aísla con `layout="position"`.
4. `prefers-reduced-motion` ignorado es un fallo de accesibilidad reportable.

Cruza con [[89-web-performance-profunda]] y [[75-webgl-threejs-shaders-creative-coding]].

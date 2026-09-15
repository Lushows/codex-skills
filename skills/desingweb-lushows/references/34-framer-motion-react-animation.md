# 34 — Motion (Framer Motion) & animación en React

Llena el hueco React/componentes (07/12 cubren GSAP/Lenis vanilla). **Léelo cuando animes en React: modales, listas, shared-element, gestos, page transitions.** Framer Motion se renombró a **Motion** (`motion.dev`); el import pasó de `"framer-motion"` a `"motion/react"` (API idéntica). Versión actual **Motion v12**.

## 1. Estado 2026

```bash
npm i motion
```
```jsx
import { motion, AnimatePresence, useScroll, useSpring, useMotionValue, useTransform, useReducedMotion } from "motion/react"
```
v12: animación directa de colores `oklch`/`color-mix`, scroll acelerado por HW, **motor híbrido** (usa WAAPI en el compositor cuando puede, cae a JS para springs sobre layout). Dos sabores: **Motion for React** (`motion.div`) y **Motion vanilla** (`animate()`/`scroll()`).
Componente base declarativo: `initial` (entrada) · `animate` (actual) · `exit` (salida) · `whileHover/whileTap/whileInView` (gestos) · `transition`.
```jsx
<motion.div initial={{opacity:0,y:24}} animate={{opacity:1,y:0}} exit={{opacity:0,y:-24}}
  transition={{type:"spring", stiffness:300, damping:30}} />
```

## 2. Variants, AnimatePresence, layout/layoutId

**Variants + orquestación** (se propagan a los hijos `motion.*`):
```jsx
const list={ hidden:{}, show:{transition:{staggerChildren:0.08, delayChildren:0.2}} }
const item={ hidden:{opacity:0,y:20}, show:{opacity:1,y:0,transition:{type:"spring",stiffness:400,damping:32}} }
<motion.ul variants={list} initial="hidden" animate="show">
  {data.map(d=><motion.li key={d.id} variants={item}>{d.text}</motion.li>)}
</motion.ul>
```
v12: `delayChildren: stagger(0.1, {from:"center"})`; `when:"beforeChildren"`.
**AnimatePresence** — anima el *unmount* (imposible con CSS). Requiere `key` única + prop `exit`. `mode="wait"` (espera salida antes de montar; ideal page transitions) · `mode="popLayout"` (saca del flujo para que el resto se reacomode).
```jsx
<AnimatePresence mode="wait">{open && <motion.div key="modal" initial={{opacity:0,scale:.9}} animate={{opacity:1,scale:1}} exit={{opacity:0,scale:.9}}/>}</AnimatePresence>
```
**`layout` y `layoutId` — killer feature (magic move / shared element):** `layout` anima cambios de posición/tamaño por re-render; `layoutId` comparte identidad entre dos elementos distintos (Motion interpola entre ambos: tabs underline, card→detalle):
```jsx
{active===t && <motion.div layoutId="underline" className="absolute -bottom-1 h-0.5 w-full bg-black" transition={{type:"spring",stiffness:500,damping:35}}/>}
```
Para layout fiable, anima `transform`/`opacity`, no `width`/`height`.
**Scroll-linked:** `const {scrollYProgress}=useScroll(); const x=useSpring(scrollYProgress,{stiffness:100,damping:30})` → `<motion.div style={{scaleX:x, transformOrigin:"0%"}}/>`.

## 3. Física de springs

Config: `{type:"spring", stiffness, damping, mass, bounce, visualDuration}`. **stiffness** = fuerza al destino (alto=rápido/seco) · **damping** = fricción (bajo=más rebote) · **mass** = inercia.
**Por qué los springs se sienten mejor:** una duración fija salta si cambias el destino a mitad; un spring arranca desde la velocidad actual → gestos/interrupciones continuos. **UI interactiva → spring; reveals decorativos → tween/duration.**
Configs que se sienten bien:
- UI snappy (botones/toggles): `stiffness:400, damping:30`
- Cards/modales (suave premium): `stiffness:300, damping:30`
- Drawers/sheets grandes: `stiffness:260, damping:30`
- Rebote juguetón: `stiffness:500, damping:18` (o `{bounce:0.4, visualDuration:0.4}`)
- Sin rebote crítico: `stiffness:200, damping:40`
API moderna recomendada: `{type:"spring", bounce:0.25, visualDuration:0.5}` (`visualDuration`=segundos percibidos hasta llegar, más intuitivo).
**MotionValues** (no disparan re-render de React → perf): `const x=useMotionValue(0); const opacity=useTransform(x,[-150,0,150],[0,1,0]); const smoothX=useSpring(x,{stiffness:300,damping:30})` → `<motion.div style={{x,opacity}} drag="x"/>`.

## 4. Gestos

```jsx
<motion.div drag dragConstraints={{left:0,right:300}} dragElastic={0.2} dragMomentum
  whileHover={{scale:1.05}} whileTap={{scale:0.95}} whileDrag={{cursor:"grabbing"}} whileFocus={{outline:"2px solid #10b981"}}/>
```
`dragConstraints` acepta una `ref`. Swipe-to-dismiss: `onDragEnd={(e,info)=>{ if(info.offset.x>120||info.velocity.x>500) dismiss() }}`. Reorder sin librería: `import {Reorder} from "motion/react"` → `<Reorder.Group values onReorder={setItems}>` + `<Reorder.Item value={item}>`.

## 5. Performance & best practices

- **Anima solo `transform` (x/y/scale/rotate) y `opacity`** (GPU). Evita `width/height/top/left/margin`; usa `scale` o layout animations.
- **MotionValues no re-renderizan** — para valores a 60fps (scroll/drag/mouse) úsalos vía `style={{x}}`, nunca `useState`.
- **`LazyMotion` + `m`** para bundle: `motion` completo ~34kb; con `m` + diferido ~4.6-6kb inicial. `domAnimation` (+15kb: animaciones/variants/exit/hover) · `domMax` (+25kb: + drag/pan + **layout animations**).
```jsx
import {LazyMotion, domAnimation, m} from "motion/react"
<LazyMotion features={domAnimation} strict><m.div animate={{opacity:1}}/></LazyMotion>  // usa m.* no motion.*; strict avisa errores
```
- **A11y `useReducedMotion`:** `const reduce=useReducedMotion(); <motion.div animate={{x:reduce?0:100}} transition={reduce?{duration:0}:{type:"spring"}}/>`.
- **SSR/Next App Router:** componentes con hooks de Motion son client → `"use client"`. Page transitions: `AnimatePresence mode="wait"` con `usePathname()` como `key`. `initial={false}` evita animar en el 1er render (hidratación sin flash).
- **Cuándo qué:** CSS (hovers triviales) · **Motion** (state-driven, layout/shared-element, gestos, orquestación React) · **GSAP/Lenis** (timelines cinematográficas, scroll-scrubbing pesado).

## 6. Recetas copy-paste

**Drawer:** overlay `initial={{opacity:0}}` + aside `initial={{x:"100%"}} animate={{x:0}} exit={{x:"100%"}} transition={{type:"spring",stiffness:300,damping:30}}` dentro de `<AnimatePresence>`.
**Acordeón (height sin saltos):** `<AnimatePresence initial={false}>{open && <motion.section initial={{height:0,opacity:0}} animate={{height:"auto",opacity:1}} exit={{height:0,opacity:0}} style={{overflow:"hidden"}}/>}` .
**Counter:** `const count=useMotionValue(0); const rounded=useTransform(count,v=>Math.round(v)); useEffect(()=>{const c=animate(count,1234,{duration:1.5,ease:"easeOut"});return c.stop},[])` → `<motion.span>{rounded}</motion.span>`.
**Reveal on scroll (una vez):** `<motion.div initial={{opacity:0,y:40}} whileInView={{opacity:1,y:0}} viewport={{once:true,margin:"-100px"}} transition={{type:"spring",stiffness:300,damping:30}}/>`.
**Toast stack:** `<AnimatePresence mode="popLayout">` + `layout` en cada toast + `exit={{opacity:0,x:50}}`.

## Anti-patterns — blacklist
animar `width/height/top/left/margin` en vez de `transform`/`scale` · manejar scroll/drag/mouse con `useState` (re-render por frame) · olvidar `key` única o `exit` en `AnimatePresence` · condicionar el propio `<AnimatePresence>` en vez de su hijo · hardcodear `duration` para UI interactiva (salta al interrumpirse → usa spring) · importar `motion` completo en bundle crítico (usa `LazyMotion`+`m`) · ignorar `useReducedMotion` · `layoutId` duplicado en pares no relacionados (teletransportes raros) · olvidar `"use client"` en Next App Router · springs con `damping` <10 en UI seria (rebote infantil).

# 52 — Teoría del motion & principios de animación

La capa de **teoría/craft** (el *por qué* del buen motion), que potencia los cookbooks 04/07/34/39. **Léelo para entender el movimiento a fondo, no solo copiar snippets.** La diferencia entre una interfaz *viva* y una *barata* casi nunca está en *qué* se anima, sino en *cómo*. El motion no es decoración: es la capa de comunicación del espacio, el tiempo y la causalidad.

## 1. Los 12 principios de Disney en UI

**Críticos (80% del valor):**
1. **Slow in & slow out (easing)** — el #1 de UI. Nada arranca/frena de golpe; `linear` se siente robótico y barato.
2. **Timing** — la velocidad comunica peso/urgencia (toast rápido 200ms = ligero; modal lento 400ms = importante).
3. **Follow-through & overlapping** — los elementos sobrepasan y asientan (overshoot/settle) — la base del feeling "spring"; cards escalonadas, no en bloque.
4. **Staging** — dirige el ojo a lo importante (un error que se sacude mientras el resto queda quieto).
5. **Anticipation** — prepara para lo que viene (botón que se hunde antes de ejecutar) → menos sensación de "salto".
**Útiles:** 6. **Arcs** (el movimiento natural curva, no recto) · 7. **Secondary action** (todas las microinteracciones lo son) · 8. **Squash & stretch** (tactilidad, con moderación) · 9. **Exaggeration** (amplificar para que el feedback *se lea*, sutil en UI) · 10. **Appeal** (el carisma total).
**Secundarios:** 11. **Straight-ahead vs pose-to-pose** (en UI casi siempre pose-to-pose: defines estados from/to, el motor interpola) · 12. **Solid drawing** (coherencia de profundidad/elevación).

## 2. Easing & timing — teoría

**Por qué:** el movimiento natural nunca es lineal (gravedad/inercia/fricción producen aceleración).
**Familias (curvas reales):**
| Curva | cubic-bezier | Cuándo |
|---|---|---|
| Standard | `(.4,0,.2,1)` | mueve dentro de pantalla (default) |
| **Decelerate/ease-out** | `(0,0,.2,1)` | **elementos que ENTRAN** (llegan rápido, asientan) |
| **Accelerate/ease-in** | `(.4,0,1,1)` | **elementos que SALEN** (arrancan suave, se van rápido) |
| Sharp | `(.4,0,.6,1)` | entran y vuelven (menús temporales) |
**Regla de oro — easing asimétrico:** lo que entra usa `ease-out` (debes *ver* dónde llega); lo que sale usa `ease-in` (quítate del medio rápido). Mismo easing para ambos = error que se siente "off".
**Duration por distancia/tamaño:** mientras más grande/lejos viaja, más tarda. Mobile: estándar 300ms, entrada 225ms, salida 195ms (sale más rápido que entra), grandes 375-400ms (techo). Desktop: 150-200ms (más snappy). Tablet ~+30%, wearables ~−30%.
**Rango "que se siente bien":** **~100-500ms**. <100ms = instantáneo (bueno para hover/press, malo para transición espacial); >500ms = el usuario *espera*. Hover/feedback 150-250ms; página/modal 300-500ms.
**Spring vs duration:** spring define *física* (stiffness/damping/mass), no tiempo → más orgánico e **interrumpible** (si re-disparas a mitad, redirige desde la velocidad actual; un cubic-bezier "salta"). Por eso **Material 3 Expressive e iOS migraron a spring** (Expressive con rebote para momentos hero, Standard con rebote mínimo utilitario).
**Personalidad de la curva = tono de voz:** elegante (ease-out suave, sin overshoot) · juguetón (overshoot + bounce + squash) · técnico (rápido, sharp, sin rebote). Un banco no rebota; una app infantil sí.

## 3. El propósito del motion (funcional)

"Motion provides meaning" (Material). Debe ganarse su lugar con una función: (1) **orientación/relaciones espaciales** · (2) **feedback/respuesta** · (3) **estado/progreso** · (4) **guiar la atención** · (5) **continuidad/conectar estados** · (6) **personalidad de marca** · (7) **delight** (el menos importante, el primero en sacrificarse).
**Ayuda vs hiere:** ayuda cuando *reduce* carga cognitiva (explica de dónde vino, dónde mirar); hiere cuando *añade* carga (anima por animar, bloquea esperando, satura). **Jerarquía:** funcional > continuidad > feedback > delight. Si una animación no cabe en una de las 7 funciones, candidata a eliminar.

## 4. Coreografía & orquestación

- **Staggering:** items de lista con delay incremental (~20-50ms) → ritmo que guía el ojo (entrar todos a la vez = plano/abrumador).
- **Leader/follower (focal point):** un elemento inicia (la imagen/héroe), título y descripción lo siguen a ritmos distintos → jerarquía por tiempo.
- **Parent-child:** el contenedor se mueve, el contenido hereda → coherencia física.
- **Spatial continuity (shared element):** la pregunta clave es **"¿de dónde vino / a dónde fue?"** — una thumbnail que se expande a vista completa mantiene continuidad. La herramienta de orquestación más potente.
- **Sequencing vs simultaneity:** secuencia para *narrar*, simultaneidad para *velocidad*.
- **"One big moment" vs death-by-microinteractions:** UN momento protagonista por pantalla; el motion de una página debe tener picos y silencios, como la música.

## 5. Microinteracciones & transiciones de estado

**Anatomía (Dan Saffer):** (1) **Trigger** (manual o sistema); (2) **Rules** (la lógica); (3) **Feedback** (aquí vive el motion); (4) **Loops & modes** (comportamiento en el tiempo).
**Principios:** los elementos **nunca solo aparecen/desaparecen — transicionan** (un dropdown crece desde su trigger; un item eliminado colapsa su altura y arrastra a los vecinos) · hover/press/focus **<150ms** para sentirse responsive · skeleton (shimmer) se percibe más rápido que spinner · **haptic-visual pairing** en mobile multiplica la solidez · el mejor motion es **invisible** (hace todo sólido y responsivo sin que sepas por qué).

## 6. Sistemas, marca & 2026

**Motion tokens (consistencia):**
```css
--duration-fast:150ms; --duration-base:250ms; --duration-slow:400ms;
--ease-standard:cubic-bezier(.4,0,.2,1); --ease-decelerate:cubic-bezier(0,0,.2,1); --ease-accelerate:cubic-bezier(.4,0,1,1);
--distance-sm:8px; --distance-md:24px; --distance-lg:64px;
```
+ **named motions** semánticos (`motion.enter/exit/emphasized`). Garantiza que todo "se mueva igual".
**Signature motion:** cada marca de élite tiene un movimiento firma (una curva/overshoot/timing) que la vuelve reconocible *sin logo*.
**Accesibilidad (daño físico real):** usuarios con **trastornos vestibulares** sufren mareo/náusea con parallax agresivo, zoom, scroll-jacking. Respeta **`prefers-reduced-motion`** SIEMPRE (`animation/transition-duration:.01ms!important`). Enfoque **no-motion-first** (Tatiana Mac): diseña sin motion, añádelo como mejora. *Reduce ≠ eliminar*: a menudo = reemplazar movimiento espacial por un simple **fade de opacidad** (seguro vestibularmente, aún comunica).
**Performance (60fps):** anima **solo `transform` y `opacity`** (GPU/compositor); evita `width/height/top/left/margin` (reflow→jank); `will-change` con moderación. 30fps con stutter se siente *peor* que ninguna animación.
**Tendencias 2026:** springs interrumpibles por defecto, Material 3 expresivo (shape morphing), scroll-driven CSS nativo (`animation-timeline`), View Transitions API, péndulo de regreso al *calm/intentional motion*.

## Motion anti-patterns — blacklist
`linear` easing · over-animation (animar lo que no cumple ninguna de las 7 funciones) · death by microinteractions · demasiado lento (>500ms que hace esperar; bloquear la UI durante la animación) · mismo easing enter/exit · janky/<60fps (animar layout properties, reflows) · inconsistente (sin motion tokens) · accessibility-ignored (sin `prefers-reduced-motion`; parallax que marea) · decorativo no funcional · aparecer/desaparecer de golpe (teletransporte, rompe continuidad) · overshoot/bounce en contexto serio (banco/error) · bloquear la entrada del usuario (animaciones largas no interrumpibles).
**Principio rector:** la mejor animación de UI es la que el usuario *no nota* — hizo el producto obvio, sólido y vivo sin pedir aplausos.

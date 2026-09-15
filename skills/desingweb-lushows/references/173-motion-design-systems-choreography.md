# 173 — Motion design systems & choreography

**CRAFT + diseño.** Motion como sistema, no animaciones sueltas. Pareja de 52 (motion theory), 04 (motion library), 15 (tokens), 149/160 (loaders/reveals). Regla de oro: **la consistencia es craft — eases/duraciones ad-hoc por componente = slop; codifica timing y easing en tokens, igual que color y spacing; el movimiento es un activo de marca con lenguaje propio.**

## 1. Por qué un SISTEMA de movimiento

Que se "sienta diseñado" casi nunca está en *qué* se mueve, sino en *cómo* se mueve **consistente**. Cada componente inventando su duración (`0.3s` aquí, `450ms` allá) y curva (`ease`, `ease-in-out`, una random) = slop (el ojo percibe incoherencia sin saber nombrarla). El movimiento es un **activo de marca con lenguaje propio** — la personalidad vive en curvas + timing: **luxurious** (largo 400-600ms, eases muy suaves, sin rebote), **playful** (springs con bounce, overshoot, staggers marcados), **precise** (rápido 120-200ms, lineal-ish, "se quita del medio"). Material 3 formaliza dos schemes: *expressive* (hero moments) y *standard* (funcional).

## 2. Motion tokens — el sistema en CSS vars

```css
:root{
  --dur-instant:80ms; --dur-fast:140ms; --dur-base:240ms; --dur-slow:360ms; --dur-slower:520ms;
  --ease-out: cubic-bezier(0,0,0.2,1);          /* enter: llega y frena */
  --ease-in: cubic-bezier(0.4,0,1,1);           /* exit: arranca y se va */
  --ease-in-out: cubic-bezier(0.4,0,0.2,1);     /* move on-screen */
  --ease-emphasized: cubic-bezier(0.2,0,0,1);   /* M3 emphasized, hero */
  --ease-signature: cubic-bezier(0.16,1,0.3,1); /* la curva DE LA MARCA */
  --move-sm:8px; --move-md:16px; --move-lg:32px;
  /* CAPA SEMÁNTICA — lo que de verdad usas */
  --motion-enter: var(--dur-base) var(--ease-out);
  --motion-exit:  var(--dur-fast) var(--ease-in);
  --motion-move:  var(--dur-base) var(--ease-in-out);
}
```
La clave es la **capa semántica**: los componentes nunca consumen `--dur-base` crudo, consumen `--motion-enter` → el significado (entrar/salir/mover) queda desacoplado del valor, y rediseñar la "voz" del movimiento es un cambio en un solo lugar.

## 3. La ciencia del easing

**`ease-out` para ENTER** (rápido→lento, el elemento "llega" y se asienta — el más usado), **`ease-in` para EXIT** (lento→rápido, acelera al salir), **`ease-in-out` para MOVE** (A→B dentro de pantalla). **Asimetría enter/exit (regla de oro):** entradas más largas, salidas más cortas (entrar pide atención, salir debe liberarla rápido; ej. enter 240ms ease-out, exit 140ms ease-in). **Custom bezier vs spring:** bezier determinista (duración fija, ideal tokens y a11y), spring orgánico (duración emerge de stiffness/damping — para gestos e interacción directa). Por qué `linear`/`ease` default **se ven baratos:** `linear` no existe en la naturaleza (robótico); el `ease` default es genérico y reconocible como "sin diseñar" → la firma de marca vive en una curva custom.

## 4. Guías de duración

Relación **distancia/tamaño ↔ duración** (más desplazamiento/escala = más larga): **micro** 80-200ms (hover/focus/toggle/feedback), **transición** 200-400ms (enter/exit de componente, dropdowns, tabs), **page/hero** 400-600ms. Heurísticas: rutinas UI 160-240ms, enter/exit 240-360ms. **Tope "don't make me wait":** rara vez >500-600ms (pasado eso es lentitud, no elegancia; excepción: hero moments). En móvil recorta ~30%.

## 5. Coreografía y orquestación

El sistema anima **relaciones**, no un elemento: **stagger** (60-100ms entre elementos; Carbon/GSAP convergen en ~70ms — demasiado bajo se ve simultáneo, demasiado alto lento), **orden de entrada** (most-important-first: el ancla entra primero y los secundarios siguen, guiando la mirada; en listas stagger top→down o desde el origen del gesto), **follow-through/overlap** (principios Disney: los elementos no arrancan/paran todos a la vez, se solapan — el segundo empieza antes de que el primero termine), **"one thing moves, related things respond"** (parent-child timing: el contenedor se expande y, con delay, su contenido aparece). **El timeline GSAP como partitura** (orquestación seria con posición relativa, no `transition-delay` disperso):
```js
const tl = gsap.timeline({ defaults:{ ease:"power3.out", duration:0.4 }});
tl.from(".hero-title", { y:32, opacity:0 })
  .from(".hero-sub", { y:16, opacity:0 }, "-=0.25")              // overlap
  .from(".card", { y:24, opacity:0, stagger:0.07 }, "-=0.2");    // 70ms stagger
```

## 6. Funcional vs decorativo + a11y

**Funcional** (siempre justificado): feedback, continuidad espacial (de dónde viene/a dónde va), dirigir atención (un solo foco). **Decorativo** (con presupuesto: si todo se mueve, nada destaca — el movimiento es recurso escaso). **`prefers-reduced-motion` como modo de primera clase** (no parche final): no es "apagar todo", es sustituir movimiento *vestibular* (desplazamientos grandes, parallax, zoom, rotación) por *fades*/cambios instantáneos, preservando feedback esencial. **Documentar el movimiento** al nivel de color/tipografía (tabla de tokens, curvas con preview, do/don't, motion spec por componente) — la **firma** (misma curva, mismo ritmo en toda la experiencia) es lo que hace que se "sienta diseñado".

## Motion-system anti-patterns — blacklist
**duraciones/eases hardcodeadas** por componente en vez de tokens · **`transition: all`** (anima props no intencionadas, mata rendimiento; especifica `transform, opacity`) · **animar `width/height/top/left/margin`** en vez de `transform`/`opacity` · **`ease` default o `linear` para UI** (lee barato/robótico) · **enter y exit con misma duración/curva** (rompe la asimetría natural) · **duraciones >600ms** en interacciones cotidianas · **stagger fuera de 60-100ms** · **todo se mueve a la vez** (sin jerarquía, sin foco) · **`prefers-reduced-motion` como afterthought** (o ausente, o un "apagar todo" que rompe feedback) · **parallax pesado, blurs y box-shadow animados** (jank) · **spring sin tope de duración** en transiciones programadas (impredecible para a11y/tests) · **movimiento decorativo sin presupuesto** que compite con el funcional · **animación que bloquea** la interacción (no se puede interrumpir/reversar).

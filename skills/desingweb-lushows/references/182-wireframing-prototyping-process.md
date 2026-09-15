# 182 — Wireframing, prototyping & the design process

**PROCESS/craft.** El embudo de incertidumbre del diseño. Pareja de 00 (design director), 183 (IA), 48/37 (handoff/manual), 50 (UX strategy). Regla de oro: **fidelity matches the question — la fidelidad de un artefacto debe igualar la pregunta que respondes; subir fidelidad antes de tiempo es la forma más cara de equivocarse.**

## 1. La fidelity ladder y cuándo

Tres ejes independientes (visual/content/interactivity). Subes solo cuando baja la incertidumbre: **sketch** (minutos, pensar con las manos, desechable) → **lo-fi wireframe grayscale** (estructura y flujo, no estética — su falta de detalle es feature: la gente critica sin miedo, se discute función no color) → **mid-fi** (jerarquía/espaciado, el caballo de batalla) → **hi-fi mockup** (validación visual, aprobación stakeholders, percepción/confianza) → **interactive prototype** (testear flujos con personas) → **coded prototype** (real feel, perf, responsive verdadero, handoff — a menudo el destino final 2026). **"Don't polish too early":** pulir un diseño no validado convierte una hipótesis barata en compromiso emocional caro + sesga el feedback (comentan sombras en vez de arquitectura).

## 2. Craft del wireframing

**Estructura primero** (dibuja el **user flow/task flow** antes de cualquier pantalla — si el flujo está roto, ninguna pantalla bonita lo salva). **Jerarquía y flujo, no píxeles**. **Grayscale obligatorio** (quitar color fuerza a resolver jerarquía con tamaño/peso/espaciado). **Placeholder realista, no lorem-as-final** (el lorem miente sobre el espacio del contenido real). **Annotations** (un wireframe sin anotaciones es ambiguo — documenta reglas de negocio, empty states, validaciones).

## 3. Prototyping para validación

**Testea flujos, no estética** (define la tarea, observa sin guiar). **Match fidelity to question** (¿dudas del flujo? lo-fi clickable; ¿dudas de confianza/marca? hi-fi). **Throwaway vs evolving** (decide antes: ¿se tira o evoluciona a producción?). **Micro-interaction prototyping:** Figma Smart Animate (80% sin código), **Rive** con state machines para producción real, Spline solo cuando el 3D aporta valor. Workflow 2026: Figma (hub) → Rive (2D interactivo) → código (lo definitivo).

## 4. El proceso AI-acelerado (2026)

El tiempo de prototipo cayó de **días a horas**. Tres paradigmas: **prompt-to-prototype / "vibe coding"** (describes en lenguaje natural, genera diseño Y código — Lovable, v0, Bolt, Replit), **design-to-code** (Figma Make), **visual AI builders** (Galileo, Figma AI). Hito feb-2026: integración bidireccional Figma↔Claude Code vía **MCP** (lee tokens, variantes, auto-layout, Code Connect). **Dónde la IA acelera:** wireframes/variaciones masivas, primeros borradores, boilerplate, exploración divergente. **Dónde el juicio humano es irremplazable:** decidir *qué* problema resolver, jerarquizar trade-offs, juzgar si un flujo *siente* bien, marca, ética/a11y. La IA produce 10 opciones; el humano sabe cuál merece existir.

## 5. Iteración y crítica

**Divergent → convergent (Double Diamond):** primero abre (genera muchas opciones sin juzgar, "10 ideas luego elige"), luego cierra (analiza y aísla). No mezcles los modos (criticar mientras ideas mata la divergencia). **Kill your darlings** (tu favorita no es sagrada; si los datos la contradicen, muere). **Crítica: describe, don't prescribe** (el feedback útil describe el problema observado "dudé dónde dar clic para pagar", no dicta la solución "pon un botón rojo"). **Versioning** (documenta *por qué* cambió, no solo qué).

## 6. De diseño a build

**Design tokens como contrato** (cuando el color se llama `color/primary` no `#6366F1`, el handoff deja de ser "¿qué azul?" y se vuelve intercambio de datos estructurado; spec DTCG estable 2026). **"El handoff murió"** (designers y devs comparten tokens/componentes/código; MCP+Code Connect acercan diseño y código). **Prototyping IN code** (comportamiento responsive/perf real desde el inicio). **Responsive desde el primer wireframe** (diseñar solo a 1440px y "adaptar después" genera deuda). **Documenta decisiones** (tokens + componentes + Code Connect + registro del *por qué*).

## Process anti-patterns — blacklist
**polish prematuro** (pixel-perfect sobre una hipótesis no validada) · **saltar el user flow** (pantallas sin mapear la tarea) · **lorem ipsum como contenido final** · **color en el wireframe** (tapa jerarquía rota) · **fidelidad que no iguala la pregunta** (hi-fi para validar arquitectura) · **testear estética en vez de flujos** ("¿te gusta?" en vez de observar atascos) · **crítica prescriptiva** (dictar soluciones, criticar contra el gusto propio) · **una sola idea** (converger sin divergir) · **apego** (defender un diseño contra la evidencia) · **handoff por encima del muro** (specs sin tokens compartidos) · **hex en vez de tokens** · **responsive como pensamiento tardío** · **aceptar output de IA sin juicio** (usar la primera variante sin curaduría) · **prototipo eterno** (pulir un throwaway que debió morir).

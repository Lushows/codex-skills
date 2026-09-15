# 142 — Anatomía del diseño web premiado (Awwwards/FWA)

**CRAFT, no vertical.** Léelo para entender QUÉ hace que un sitio gane Site of the Day y cómo emularlo a cualquier presupuesto. Pareja de 05 (referencias/estudios), 00 (dirección), 07 (motion), 39 (interacción), 10 (art-direction pro). Regla de oro: **un sitio = UNA idea memorable; la usabilidad (30%) pesa más que la creatividad (20%) → los tech demos pierden.**

## 1. Qué gana realmente en 2026

El jurado de Awwwards puntúa con peso fijo: **Design 40%, Usability 30%, Creativity 20%, Content 10%** (media ≥8.0 = SOTD, ≥6.5 = Honorable Mention; mínimo 18 jurados, se descartan los 3 votos más alejados). Lectura estratégica: **la usabilidad pesa MÁS que la creatividad** → el WebGL no gana solo, gana al servicio de una dirección de arte y narrativa. **Ingredientes recurrentes de un SOTD:** dirección de arte audaz y propietaria (no un theme), **un** momento WebGL/canvas memorable (UNO, no diez), custom motion con timing de cine, una interacción inesperada que el jurado recuerde al día siguiente, sound design opcional con toggle, **performance real (CWV: LCP/INP/CLS ya es requisito**, un sitio bonito que tarda 6s muere en Usability). **"Looks expensive" vs "tech demo":** lo caro se siente con restraint, jerarquía tipográfica impecable y motion que guía la atención; el tech demo grita "mira lo que sé hacer" (partículas sin propósito, scroll-jacking, 60MB de assets) — la diferencia es **intención**.

## 2. La anatomía / fórmula canónica

En orden: (1) **cinematic loader** (cubre la carga de assets WebGL; funcional + branding, no decorativo), (2) **hero reveal** (`clip-path` wipe, máscara de texto con SplitText line-by-line stagger, o cámara WebGL que se asienta), (3) **el momento WebGL/canvas** (galería con shader, distorsión de imagen en hover, objeto 3D scroll-driven — **el único momento "wow"**), (4) **pinned/horizontal sections** (`ScrollTrigger.pin`), (5) **kinetic typography** (tipografía grande como elemento de diseño, velocity-skew en scroll), (6) **custom cursor** (contextual: crece sobre links, muestra "view"/"drag", magnetic), (7) **smooth scroll** (Lenis, base de todo), (8) **bold footer** (gran tipografía, a veces el segundo momento WebGL). **Regla de oro: un sitio = una idea memorable** (cada ganador tiene UNA cosa; si tu sitio tiene cinco "momentos", no tiene ninguno).

## 3. Estudios y sus firmas (recetas para emular)

**Active Theory** — el referente WebGL/Three.js inmersivo (mundos 3D navegables, audio reactivo; receta: R3F + shaders custom). **Resn** — WebGL juguetón surrealista, física con propósito narrativo. **Cuberto** — **cursores custom + ilustración propietaria + micro-interacciones** (su firma es el cursor magnético fluido con `lerp`; la receta más copiable y barata de "award feel"). **Obys** — editorial + motion (tipografía como estructura, grids deliberados; menos WebGL, más craft tipográfico). **Locomotive** — creadores de la cultura del smooth-scroll (Lenis es heredero); scroll como narrativa. **Unseen/Studio Lhoumeau** — minimalismo con UN detalle de motion exquisito; restraint llevado a virtuosismo.

## 4. El stack técnico de los ganadores

| Capa | Herramientas |
|---|---|
| Smooth scroll | **Lenis** (estándar absoluto) |
| Animación | **GSAP + ScrollTrigger** (motor del 90%), SplitText, GSAP 100% gratis |
| 3D/WebGL | Three.js, **R3F + drei**, **OGL** (ligero), GLSL custom |
| Alt | Anime.js v4, Motion (React) |
| Vector/3D no-code | Spline, **Rive** (ligerísimo, ideal mobile) |
| Frameworks | **Astro** (perf-first), Next.js, a veces Barba.js |

El combo nuclear repetido: **Lenis + GSAP ScrollTrigger + Three/R3F/OGL + GLSL + Astro/Next.**

## 5. La capa de gusto (taste layer) — por qué casi todo lo "effect-heavy" pierde

El gusto es lo que el código no compra: **restraint** ("cada motion sirve un propósito — deleitar o mejorar usabilidad"; el efecto sin función penaliza Usability), **timing** (el 80% de la sensación premium está en `ease` y `duration`; custom cubic-bezier/`power3.out`, nunca `linear` ni defaults; stagger 0.05-0.1s), **disciplina de color** (2-3 colores + neutros), **tipografía** (jerarquía clara, una display con carácter + una neutral legible; la tendencia editorial/archival 2026 gana mucho), **sound** (siempre con toggle, nunca autoplay). **Tensión maximalismo vs minimalismo:** la respuesta honesta de 2026 es un **blend** — base minimalista limpia y rápida + UN momento expresivo (ni brutalismo gratuito ni minimalismo aburrido).

## 6. Aplicar a distintos presupuestos

**Award feel barato (sin WebGL, ~días):** (1) Lenis smooth scroll, (2) tipografía display potente + jerarquía obsesiva, (3) **UN** momento (máscara de texto en reveal con SplitText, o `clip-path` wipe entre secciones), (4) **cursor custom magnético** (estilo Cuberto, ~40 líneas con `lerp`), (5) micro-interacciones con timing cuidado. Esto solo, bien ejecutado, ya compite por Honorable Mention. **Medio:** + Rive/Spline para un objeto animado (sin coste GPU de Three), `ScrollTrigger.pin` para una sección horizontal, displacement en imágenes. **Full WebGL (semanas):** R3F + drei, shaders GLSL custom, escena scroll-driven con cámara animada por GSAP, audio reactivo. **Performance como criterio:** en cualquier nivel LCP <2.5s, INP <200ms, CLS <0.1; lazy-load del WebGL, comprime texturas, `prefers-reduced-motion`.

## Crafted ✅ vs Tech-demo ❌ — blacklist
UN momento WebGL con propósito / **partículas+3D en cada sección** · smooth scroll que respeta el input / **scroll-jacking que secuestra el control** · custom cursor contextual / **cursor que esconde el real sin razón** · `prefers-reduced-motion` respetado / **motion forzado, mareante** · loader que precarga (funcional) / **loader falso de 4s "porque se ve cool"** · type-driven con jerarquía / **texto ilegible sobre shader animado** · 2-3 colores con restraint / **paleta arcoíris + glow everywhere** · LCP <2.5s, assets comprimidos / **60MB de texturas, 6s de carga** · sound con toggle / **autoplay de audio invasivo** · una idea memorable / **cinco efectos, cero memoria**.

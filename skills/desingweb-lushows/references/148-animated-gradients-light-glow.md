# 148 — Animated gradients, light, glow & aurora

**CRAFT, code-heavy.** Léelo para el look Stripe/Linear/Vercel: mesh gradients, glow, aurora, god-rays, gradientes animados. Pareja de 02 (color systems), 09 (modern CSS), 147 (grano anti-banding), 13 (dashboards/SaaS). Regla de oro: **un solo foco de luz por viewport; el gradiente premium es restraint, no fiesta de color; todo gradiente suave necesita su capa de grano.**

## 1. Por qué luz y gradiente son la firma "premium-tech"

La luz es la única textura que sugiere que algo está vivo y es caro de producir: un fondo plano es barato; un mesh gradient que respira o un glow que reacciona al cursor comunica "ingeniería seria detrás" (el ojo lee gradación suave + emisión como volumen/profundidad sin skeuomorfismo). **Encaja:** heroes, dashboards SaaS, dark-mode landing, pricing, auth. **NO:** contenido denso de lectura, e-commerce con muchas fotos (el glow compite).

## 2. Animated CSS gradients (sin JS)

Un `linear-gradient()` crudo **no es animable**. La solución 2026: registrar color-stops y ángulo como `@property` tipadas (Baseline desde julio 2024) → el navegador interpola `<color>`/`<angle>` reales:
```css
@property --c1{ syntax:"<color>"; initial-value:#5b8cff; inherits:false; }
@property --angle{ syntax:"<angle>"; initial-value:0deg; inherits:false; }
.hero{ background:linear-gradient(var(--angle), var(--c1), #b14bff);
  animation:shift 12s ease-in-out infinite alternate, spin 20s linear infinite; }
@keyframes shift{ to{ --c1:#00d4ff; } } @keyframes spin{ to{ --angle:360deg; } }
```
**Conic spin** (el "aura" girando) gratis con `@property --angle`. **OKLCH + color-mix() para gradientes sin barro:** interpolar `in oklch` evita las zonas grises/muertas que produce sRGB al cruzar tonos opuestos: `background:linear-gradient(in oklch, oklch(70% .2 250), oklch(75% .18 330))`; `--accent-soft: color-mix(in oklch, var(--accent) 30%, transparent)`.

## 3. Mesh gradients

**CSS puro** — stack de `radial-gradient` translúcidos sobre un color base, posiciones animadas:
```css
.mesh{ background-color:#0a0a12;
  background-image:
    radial-gradient(at 20% 30%, oklch(65% .2 260 / .55) 0px, transparent 50%),
    radial-gradient(at 80% 20%, oklch(70% .2 330 / .50) 0px, transparent 50%),
    radial-gradient(at 60% 80%, oklch(68% .18 200 / .45) 0px, transparent 50%);
  animation:drift 18s ease-in-out infinite alternate; }
@keyframes drift{ to{ background-position:10% -8%, -6% 12%, 8% 6%; } }
```
Para movimiento más fluido, separa cada blob en su elemento y anima `transform:translate()` + `filter:blur(60px)` (transform es GPU-cheap). **WebGL (look Stripe fluido):** el estándar 2026 es **Paper Shaders** (`@paper-design/shaders-react`, zero-dependency, 30+ efectos): `<MeshGradient colors={[...]} distortion={0.8} swirl={0.6} grainOverlay={0.12} />` (el `grainOverlay` mata el banding integrado). **Grano encima (anti-banding):** todo gradiente suave en 8-bit produce banding → capa de ruido al 4-10% con `mix-blend-mode:overlay` (ver ref 147).

## 4. Glow & bloom

**Neon text glow** (capas de `text-shadow` de radios crecientes): `text-shadow:0 0 4px #6ee7ff, 0 0 12px #6ee7ff, 0 0 32px #00aaff, 0 0 64px #0066ff`. **Element bloom barato** (hermano borroso detrás, más eficiente que box-shadow gigante):
```css
.card::before{ content:""; position:absolute; inset:-2px; z-index:-1;
  background:linear-gradient(120deg,#6ee7ff,#a855f7); filter:blur(24px); opacity:.55; border-radius:inherit; }
```
**"Lamp"/spotlight gradient** (el haz de Linear desde arriba): `.lamp::before{ background:radial-gradient(60% 40% at 50% 0%, oklch(75% .2 250 / .5), transparent 70%); }`. **Glow que sigue al cursor** (radial anclado a `--x/--y`, solo escribe variables sin layout):
```css
.spotlight{ background:radial-gradient(220px circle at var(--x) var(--y), oklch(80% .18 250 / .25), transparent 60%); }
```
```js
el.addEventListener('pointermove', e=>{ const r=el.getBoundingClientRect();
  el.style.setProperty('--x',`${e.clientX-r.left}px`); el.style.setProperty('--y',`${e.clientY-r.top}px`); });
```

## 5. Aurora / light-leak / god-rays

**Aurora borealis** (gradientes saturados muy borrosos animados en translate/rotate sobre fondo oscuro):
```css
.aurora::before, .aurora::after{ content:""; position:absolute; inset:-30%;
  background:conic-gradient(from 0deg, #00ffa3, #00b3ff, #b14bff, #00ffa3);
  filter:blur(80px); opacity:.4; mix-blend-mode:screen; animation:aurora 16s ease-in-out infinite alternate; }
.aurora::after{ animation-duration:22s; animation-direction:alternate-reverse; }
@keyframes aurora{ to{ transform:translate3d(8%,-6%,0) rotate(40deg) scale(1.2); } }
```
**Light leak** (gradiente cálido con `mix-blend-mode:screen`/`color-dodge`, opacidad baja, deslizando — sobre dark bg "quema" luz sin tapar contenido). **God-rays cónicos** (`repeating-conic-gradient` de cuñas claras + `filter:blur(6px)` + mask vertical).

## 6. Performance & taste

**`filter:blur()` es caro** (repinta cada frame si lo animas) → **nunca animes `blur` ni `box-shadow`**, deja el blur estático y anima `transform`/`opacity` (la aurora de arriba sigue esa regla: blur fijo + translate animado). Marca capas pesadas con `will-change:transform` (con moderación). **`prefers-reduced-motion` obligatorio** (congela en un frame estático bonito, no apagues el gradiente). Pausa shaders WebGL fuera de viewport. **Dark bg amplifica el glow** (el mismo color emite el doble sobre `#08080c` que sobre blanco — diseña el glow en oscuro). **Restraint:** un foco de luz, saturación alta + blur generoso + opacidad baja (.3-.5) lee premium; opacidad alta + bordes duros lee "tema de Windows 98".

## Gradient/glow anti-patterns — blacklist
**rainbow de 6+ colores girando** (screensaver, no producto; máx 2-3 tonos vecinos en OKLCH) · **gradientes en sRGB cruzando tonos opuestos** (azul→naranja = zona gris muerta al centro; usa `in oklch`) · **banding sin grano** (todo gradiente suave necesita su capa de ruido) · **animar `filter:blur` o `box-shadow`** (jank; anima `transform`) · **glow en cada elemento** (si todo brilla, nada brilla; un focal point) · **`mix-blend-mode` sobre fondo claro** esperando que "queme" (`screen`/`color-dodge` solo sobre oscuro) · **box-shadow blur >100px en superficies grandes** (usa pseudo-hermano con `filter:blur`) · **olvidar `prefers-reduced-motion`** · **WebGL shader fullscreen sin pausar** (drena batería) · **`@property` sin `initial-value` válido** (la animación no arranca silenciosamente) · **glow del color de marca exacto** (debe ser una versión más clara/saturada en `oklch` con +lightness, no el mismo hex plano).

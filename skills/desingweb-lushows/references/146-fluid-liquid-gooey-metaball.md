# 146 — Fluid, liquid, gooey & metaball effects

**CRAFT, code-heavy.** Léelo para gooey menus, blobs, metaballs, liquid hover/distortion, morphing de formas. Pareja de 41 (generative art), 08/38 (WebGL), 81 (CSS art), 39 (interacción). Regla de oro: **el gooey es un acento, no un sistema — zonas pequeñas (menú, cursor, loader), nunca fullscreen con filtro SVG; el efecto premium se nota en el *casi*.**

## 1. La familia y su vibe

Gooey/blob/liquid es la estética **orgánica, viscosa, premium-juguetona** (superficies que se fusionan y deforman en vez de rectángulos rígidos; lo opuesto al brutalismo). **Encaja:** marcas creativas/estudio, beauty/skincare/wellness (la viscosidad lee como "sérum/líquido vivo"), productos para niños, bebidas, fintech cálida — el gooey-merge de blobs lee como células/hongos/agua (perfecto para nichos biológicos como BIO-SETA). **Wrong:** dashboards densos, banca/legal serio, e-commerce de volumen (distrae del Add-to-Cart), UI de visita diaria (la novedad cansa).

## 2. El filtro SVG gooey (el clásico barato)

La receta de Lucas Bebber: **desenfocar** + **umbralizar el alpha** con `feColorMatrix` de alto contraste → los bordes suaves que se solapan se "pegan" en una masa de goo:
```html
<svg style="position:absolute;width:0;height:0"><defs>
  <filter id="goo">
    <feGaussianBlur in="SourceGraphic" stdDeviation="10" result="blur"/>
    <feColorMatrix in="blur" mode="matrix"
      values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 19 -9" result="goo"/>
    <feBlend in="SourceGraphic" in2="goo"/>
  </filter>
</defs></svg>
```
**Anatomía de `0 0 0 19 -9`:** el `19` multiplica el alpha (más alto = bordes más nítidos); el `-9` desplaza el umbral (más negativo = los blobs deben acercarse más para fusionarse). `stdDeviation` = viscosidad (más blur = goo más blando; **sube el blur → sube el multiplicador alpha** para mantener bordes definidos). **Aplicación:** `.gooey-menu{filter:url(#goo)}` + hijos círculos del **mismo color sólido** que al expandirse (`transform:translateY`) pasan por estados de fusión. Casos: menú radial pegajoso, dots de loader que se tragan, sticky cursor (círculo cursor + círculo target bajo el mismo filtro se conectan al acercarse). **Requisito:** mismo color sólido + mismo contenedor con el filtro.

## 3. Metaballs

Campo escalar: cada blob aporta `influencia = r²/dist²`, se dibuja la **isolínea** donde la suma cruza un threshold. **Barato (SVG/CSS):** N círculos bajo el filtro `#goo` animados con posiciones random = fondo de blobs fusionándose sin matemática. **Real (Canvas 2D):**
```js
for(let y=0;y<H;y+=2) for(let x=0;x<W;x+=2){
  let sum=0;
  for(const b of balls){ const dx=x-b.x, dy=y-b.y; sum += (b.r*b.r)/(dx*dx+dy*dy); }
  if(sum>1){ /* dentro de la isolínea → pinta el pixel */ }
}
```
Para fondos full-screen 60fps, mueve el campo a un **fragment shader WebGL** (mismo `sum>threshold` por pixel en GPU, con `smoothstep` para anti-alias del borde) — la versión de demos premium.

## 4. Liquid distortion (WebGL)

El "liquid hover": desplazas las UV de la textura con ruido (simplex/curl) modulado por mouse/velocidad. Stack: **OGL** (ligero) o Three:
```glsl
uniform sampler2D uTex; uniform vec2 uMouse; uniform float uTime, uHover; varying vec2 vUv;
float snoise(vec3 v); // pega implementación Ashima/Gustavson
void main(){
  float strength = uHover * smoothstep(0.4, 0.0, distance(vUv, uMouse));
  float ripple = snoise(vec3(vUv*6.0, uTime*0.4));
  gl_FragColor = texture2D(uTex, vUv + ripple*0.04*strength);
}
```
Actualizas `uMouse` en `pointermove` **con lerp** (inercia líquida), `uTime` cada frame, `uHover` un ease al enter/leave. Para transición de página líquida (slider), usa displacement map + `mix(texA, texB, smoothstep(...))`. Lib lista: curtains.js o `gl-transitions`.

## 5. Blob shapes & morphing

**a) Border-radius blob (sin librería, el más barato):** 8 valores de radio asimétricos animados:
```css
.blob{ border-radius:42% 58% 70% 30% / 45% 45% 55% 55%; animation:morph 8s ease-in-out infinite; }
@keyframes morph{ 33%{ border-radius:70% 30% 46% 54% / 30% 60% 40% 70%; } 66%{ border-radius:30% 70% 60% 40% / 60% 30% 70% 40%; } }
```
Con `filter:blur(40px)` + varios apilados = manchas de color de fondo (los "gradient blobs" de Stripe/Linear). **b) SVG path morph con GSAP MorphSVG (ahora 100% GRATIS):**
```js
gsap.to("#shapeA",{ duration:1.4, ease:"power2.inOut",
  morphSVG:{ shape:"#shapeB", shapeIndex:"auto" }, repeat:-1, yoyo:true });
```
`shapeIndex:"auto"` evita que el path se enrolle feo. Alternativa data-driven: **flubber**.

## 6. Performance & taste

**Los filtros SVG son caros en GPU** (`feGaussianBlur` repinta cada frame; animar muchos bajo `filter:url(#goo)` a full-screen tira el framerate, sobre todo Safari/iOS) → **gooey en zonas pequeñas**, para fondos grandes usa Canvas/WebGL no filtro SVG. `will-change:transform` en los items animados (no en el contenedor con filtro); anima `transform`/`opacity`, jamás `width/top/left`. **WebGL degrada** (detecta `gl` nulo/GPU débil → imagen estática; pausa el RAF fuera de viewport). **`prefers-reduced-motion` obligatorio** (el goo y la distorsión son disparadores vestibulares). **Sutileza:** `stdDeviation` y amplitud de displacement bajos (el premium se nota en el *casi* — un puente de goo apenas visible, una onda de 4% de UV).

## Fluid/gooey anti-patterns — blacklist
**`filter:url(#goo)` sobre el `<body>` o secciones full-screen** (muere el framerate en móvil) · **todo jiggling a la vez** (botones, cards, fondo y cursor blobeando = caos epiléptico) · **blobs de distinto color bajo el mismo filtro goo** (no se fusionan limpio, salen halos sucios — mismo color sólido) · **olvidar `prefers-reduced-motion`** · **`stdDeviation` enorme sin subir el multiplicador alpha** (blobs lavados, fantasmales) · **liquid distortion sin lerp/inercia** (robótico, nervioso, mata la metáfora líquida) · **WebGL sin fallback** (pantalla en blanco) · **animar `width/height/top` del blob** en vez de `transform`/`border-radius` · **gooey en UI transaccional** (checkout, dashboards, forms — distrae y envejece) · **no pausar el rAF fuera de viewport** · **morph SVG entre paths de topología muy distinta sin `shapeIndex`/flubber** (interpolación retorcida) · **texto de lectura larga bajo goo** (ilegible).

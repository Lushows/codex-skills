# 08 — WebGL / 3D inmersivo (nivel Active Theory / Resn)

Referencia accionable para usar gráficos 3D y shaders en la web sin matar el rendimiento.
El 3D bien usado eleva un sitio a Awwwards; mal usado lo vuelve lento y pretencioso.

---

## 1. Cuándo usar WebGL/3D (y cuándo NO)

**Regla de oro:** el 3D debe SERVIR AL MENSAJE, no ser decoración pesada. Si quitas el efecto
y la página comunica igual de bien, probablemente no lo necesitas.

**SÍ usar WebGL/3D cuando:**
- El producto ES visual/espacial: un objeto físico, un mapa, un configurador, un dato 3D.
- Eres un estudio creativo/portafolio y el "wow" técnico ES parte del posicionamiento.
- Necesitas un efecto imposible con CSS: distorsión de imagen real, fluidos, partículas masivas,
  displacement por shader, transiciones entre texturas.
- Un hero que cuenta una historia con scroll (scrollytelling 3D).

**NO usar (la mayoría de los sitios NO lo necesitan):**
- Sitios de contenido, blogs, SaaS B2B, landings de conversión donde la velocidad manda.
- Cuando un MP4/WebM, un Lottie o un gradiente CSS animado logran el 90% del efecto al 5% del costo.
- Si el equipo no puede mantenerlo: un canvas WebGL roto es peor que no tenerlo.
- Móvil de gama baja como público principal.

> Coste real: un canvas Three.js + postprocessing puede pesar 600KB–1.5MB de JS y consumir GPU
> constante (batería). Un shader simple en OGL puede costar solo ~30KB. Mide siempre.

---

## 2. Escala de herramientas (de menos a más esfuerzo)

### a) CSS 3D transforms — esfuerzo MÍNIMO, peso 0KB
Qué: `transform: rotateY()`, `perspective`, `translateZ` con `transform-style: preserve-3d`.
Cuándo: tarjetas que giran, parallax por capas, tilt en hover, cubos. No es WebGL pero da profundidad.
```css
.card { transform-style: preserve-3d; transition: transform .4s; }
.card:hover { transform: perspective(800px) rotateX(8deg) rotateY(-12deg); }
```
Peso: 0 (nativo). Siempre primera opción si basta.

### b) Spline / Rive / Unicorn Studio — NO-CODE, embebible
Tres herramientas distintas, no compiten 1:1:

- **Spline** (spline.design): escenas **3D completas** no-code (modelas, animas, triggers de
  scroll/click/hover). Integración nativa con Webflow. Exporta a `<iframe>` o componente React/viewer.
  Cuándo: hero con objeto 3D interactivo sin escribir Three.js. Peso: medio-alto (runtime ~1MB+).
  ```html
  <!-- Viewer oficial de Spline -->
  <script type="module" src="https://unpkg.com/@splinetool/viewer/build/spline-viewer.js"></script>
  <spline-viewer url="https://prod.spline.design/XXXX/scene.splinecode"></spline-viewer>
  ```
- **Rive** (rive.app): **animación 2D interactiva** con *state machines* (lógica de estados),
  hasta ~120 FPS, archivos diminutos. Ideal para micro-interacciones de UI, botones, mascotas,
  loaders que reaccionan al usuario. NO es 3D. Peso: runtime ~100KB + archivo `.riv` (KB).
  ```html
  <canvas id="rive" width="500" height="500"></canvas>
  <script src="https://unpkg.com/@rive-app/canvas"></script>
  <script>
    new rive.Rive({ src: 'hero.riv', canvas: document.getElementById('rive'),
      autoplay: true, stateMachines: 'State Machine 1' });
  </script>
  ```
- **Unicorn Studio** (unicorn.studio): **WebGL 2D no-code** por capas (como Figma/Photoshop) con
  +60 efectos: shaders de gradiente, glow, distorsión, pixelado, ruido. Genera embed listo.
  Cuándo: fondos generativos animados y efectos shader sin escribir GLSL. Peso: medio.
  ```html
  <div data-us-project="TU_PROJECT_ID" data-us-scale="1" data-us-dpi="1.5"
       data-us-lazyload="true" data-us-production="true"></div>
  <script type="text/javascript">
  !function(){var u=window.UnicornStudio;if(u&&u.init){u.init()}else{
    window.UnicornStudio={isInitialized:!1};var i=document.createElement("script");
    i.src="https://cdn.jsdelivr.net/gh/hiunicornstudio/unicornstudio.js/dist/unicornStudio.umd.js";
    i.onload=function(){UnicornStudio.init()};(document.head||document.body).appendChild(i)}}();
  </script>
  ```

### c) OGL / curtains.js — LIGERO, escribes shaders
- **OGL** (github.com/oframe/ogl): WebGL mínimo, ES6, sin dependencias. Core ~8KB, +math 6KB,
  +extras 15KB (~29KB total, menos con tree-shaking). Para quien quiere controlar sus shaders sin
  el peso de Three.js. Ideal: distorsión de imagen, fondos de shader, partículas medianas.
- **curtains.js**: especializado en "atar" planos WebGL a imágenes/videos HTML existentes y
  distorsionarlos con shaders, manteniendo el DOM accesible. Perfecto para galerías con hover.

### d) Three.js — el estándar
Qué: abstracción madura sobre WebGL (escenas, cámaras, luces, materiales, geometría, render loop).
Casi todo sitio 3D custom lo usa por debajo. WebGL2/WebGPU disponibles.
Cuándo: escenas 3D reales, modelos `.glb`, postprocessing (DOF, grano de film), scrollytelling.
Peso: ~150KB+ core, más addons. Combínalo con GSAP ScrollTrigger para scroll-driven.

### e) React Three Fiber (R3F) + drei — máximo esfuerzo/poder en React
Qué: Three.js como componentes JSX declarativos. **drei** añade helpers (Environment, Html,
OrbitControls, useTexture, instancing). Cuándo: app React con estado complejo y escenas grandes.
Coste: todo lo de Three.js + React + reconciler. Solo si ya vives en React.

---

## 3. Efecto estrella: distorsión de imagen en hover con shader

**Concepto:** renderizas la imagen como textura sobre un plano WebGL. Un *displacement map*
(textura de gradiente/ruido) y un *uniform* (`uHover` 0→1 animado, o `uMouse`) desplazan los UV de
muestreo. Resultado: la imagen se "derrite", ondula o hace RGB shift al pasar el mouse. Es el efecto
firma de Active Theory / Resn / Codrops.

**Esqueleto con OGL** (plano fullscreen con textura + hover uniform):
```js
import { Renderer, Camera, Geometry, Program, Mesh, Texture } from 'ogl';

const renderer = new Renderer({ alpha: true, dpr: Math.min(2, devicePixelRatio) });
const gl = renderer.gl;
canvasWrap.appendChild(gl.canvas);

const texture = new Texture(gl);
const img = new Image(); img.src = 'foto.jpg';
img.onload = () => (texture.image = img);

const program = new Program(gl, {
  vertex: /* glsl */`
    attribute vec2 uv; attribute vec2 position; varying vec2 vUv;
    void main(){ vUv = uv; gl_Position = vec4(position, 0.0, 1.0); }`,
  fragment: /* glsl */`
    precision highp float;
    uniform sampler2D tMap; uniform float uHover; uniform vec2 uMouse;
    varying vec2 vUv;
    void main(){
      vec2 uv = vUv;
      // distorsión radial hacia el mouse, escalada por hover
      float d = distance(uv, uMouse);
      uv += (uv - uMouse) * uHover * 0.15 * (1.0 - d);
      // RGB shift: muestreo desfasado por canal
      float s = uHover * 0.012;
      float r = texture2D(tMap, uv + vec2(s, 0.0)).r;
      float g = texture2D(tMap, uv).g;
      float b = texture2D(tMap, uv - vec2(s, 0.0)).b;
      gl_FragColor = vec4(r, g, b, 1.0);
    }`,
  uniforms: { tMap:{value:texture}, uHover:{value:0}, uMouse:{value:[0.5,0.5]} }
});

const mesh = new Mesh(gl, { geometry: new Geometry(gl, {
  position:{size:2,data:new Float32Array([-1,-1, 3,-1, -1,3])},
  uv:{size:2,data:new Float32Array([0,0, 2,0, 0,2])} }), program });

// animar uHover 0→1 en mouseenter/leave (con tu lib de easing, p.ej. GSAP)
el.addEventListener('mouseenter', ()=> tweenTo(program.uniforms.uHover, 1));
el.addEventListener('mouseleave', ()=> tweenTo(program.uniforms.uHover, 0));
el.addEventListener('mousemove', e=>{ const r=el.getBoundingClientRect();
  program.uniforms.uMouse.value=[(e.clientX-r.left)/r.width,(e.clientY-r.top)/r.height]; });

requestAnimationFrame(function loop(){ renderer.render({ scene: mesh });
  requestAnimationFrame(loop); });
```

**Patrón curtains.js:** en vez de crear el canvas a mano, declaras la imagen en HTML con clase de
plano, curtains la "envuelve" y solo escribes el fragment shader con un uniform de hover. Mantiene la
`<img>` real (mejor para SEO/accesibilidad y fallback). Usa una **displacement texture** como input.

---

## 4. Fondos generativos (gradient mesh / partículas)

**Opción NO-CODE:** un *gradient mesh* WebGL animado o campo de partículas con **Unicorn Studio**
(embed del punto 2c) — cero GLSL, controlas colores y velocidad en su editor. Para gradientes
animados puros también sirve la lib `@stripe/...`-style o un shader propio.

**Opción CÓDIGO (gradient mesh con shader, OGL/Three):** un quad fullscreen + fragment con ruido
(simplex/FBM) mezclando 2–4 colores y un `uTime`:
```glsl
uniform float uTime; varying vec2 vUv;
void main(){
  vec3 a = vec3(0.05,0.20,0.15), b = vec3(0.00,0.45,0.35);
  float n = sin(vUv.x*3.0 + uTime*0.3) * cos(vUv.y*3.0 - uTime*0.2);
  gl_FragColor = vec4(mix(a, b, n*0.5+0.5), 1.0);
}
```
**Partículas:** usa instancing/`Points` con un `BufferGeometry` de posiciones. Mantén el conteo
razonable (5k–30k en desktop, mucho menos en móvil) y anima en el vertex shader, no en JS.

---

## 5. Integración y performance (crítico)

- **Lazy-load del canvas:** no cargues Three/OGL ni inicialices el render hasta que el contenedor
  esté cerca del viewport. Carga el JS con `import()` dinámico tras intersección.
- **Pausar render fuera de viewport** con `IntersectionObserver`: si no se ve, no llames a
  `requestAnimationFrame`. Esto ahorra GPU/batería enormemente.
```js
let running = false, rafId;
function loop(){ renderer.render({ scene: mesh }); rafId = requestAnimationFrame(loop); }
new IntersectionObserver(([e]) => {
  if (e.isIntersecting && !running){ running = true; loop(); }
  else if (!e.isIntersecting && running){ running = false; cancelAnimationFrame(rafId); }
}, { threshold: 0.05 }).observe(canvasWrap);
```
- **Respeta `prefers-reduced-motion`:** si el usuario lo pidió, NO animes — muestra imagen estática
  o un frame congelado.
```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
if (reduce) { showStaticImage(); } else { initWebGL(); }
```
- **Fallback a imagen estática:** si no hay contexto WebGL (`canvas.getContext('webgl2')` null) o
  falla la carga, deja la `<img>`/poster visible. Renderiza el HTML primero, mejora después.
- **Máximo 1 experiencia WebGL pesada por página.** Varios canvas activos compiten por la GPU.
- **Móvil:** baja `dpr` (`Math.min(1.5, devicePixelRatio)`), reduce partículas, considera desactivar
  el efecto y servir un MP4/poster. Prueba en gama media real, no solo en tu equipo.
- **Otros:** prefiere funciones GLSL nativas (`mix`, `dot`, `normalize`), texturas RGBA8, genera
  mipmaps, y usa GSAP ScrollTrigger para acoplar scroll a la animación 3D.

---

## 6. Recursos (URLs reales)

- Three.js — https://threejs.org/ · docs https://threejs.org/docs/
- React Three Fiber — https://r3f.docs.pmnd.rs/ · drei — https://github.com/pmndrs/drei
- OGL (ligero) — https://github.com/oframe/ogl
- curtains.js — https://www.curtainsjs.com/
- Spline (3D no-code) — https://spline.design/
- Rive (animación interactiva) — https://rive.app/
- Unicorn Studio (WebGL no-code) — https://www.unicorn.studio/ · embed https://www.unicorn.studio/docs/embed/
- Theatre.js (animación con timeline) — https://www.theatrejs.com/
- Codrops (tutoriales WebGL) — https://tympanus.net/codrops/ · distorsión hover https://tympanus.net/codrops/tag/distortion/
- Three.js Journey (curso) — https://threejs-journey.com/
- MDN WebGL best practices — https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/WebGL_best_practices

> Inspiración nivel referencia: Active Theory, Resn, Basement Studio, y los demos de Codrops/Awwwards.
> Empieza simple (CSS 3D / no-code), sube de herramienta solo cuando el mensaje lo exija.

# 174 — 3D typography & text en WebGL

**CRAFT, code-heavy.** El "WebGL headline" (uno de los gestos más premiados). Pareja de 161 (escena 3D), 145 (kinetic type), 154/155 (shaders/partículas), 38 (R3F). Regla de oro: **MSDF para nitidez y volumen de texto; TextGeometry solo cuando necesitas grosor físico que reacciona a la luz; HTML real cuando el contenido es la prioridad semántica — texto en canvas es INVISIBLE a SEO/screen-readers, SIEMPRE espejo HTML.**

## 1. Por qué 3D type & las opciones

| Approach | Qué es | Cuándo |
|---|---|---|
| **TextGeometry** (extruded mesh) | Glifos tesselados + profundidad/bevel | Headlines cortas, estáticas, material físico (metal/glass). Geometría pesada. |
| **MSDF text** (troika/drei `<Text>`) | Quad texturizado con signed distance field | **Default para casi todo**: crisp a cualquier zoom, barato. |
| **HTML-overlay** | Texto DOM real posicionado sobre el canvas | Cuando el texto debe ser seleccionable/SEO y el WebGL es solo fondo. |

El truco de élite: combinar HTML real (SEO/a11y) + capa WebGL de enhancement sincronizada.

## 2. MSDF text — la forma correcta de texto nítido

Un **MSDF (multi-channel signed distance field)** codifica la distancia al borde del glifo en RGB; el shader reconstruye con `median(r,g,b)` + `smoothstep` → bordes afilados **a cualquier escala con una sola textura** (bitmap text falla: al escalar interpola píxeles = blur). Con drei `<Text>` (envuelve troika-three-text):
```jsx
<Text font="/fonts/ClashDisplay-Bold.woff" fontSize={1.4} letterSpacing={-0.03} maxWidth={8}
      anchorX="center" anchorY="middle" sdfGlyphSize={64} outlineWidth={0.02} outlineColor="#000">
  DESIGN IN MOTION
  <meshStandardMaterial metalness={0.6} roughness={0.2} />
</Text>
```
Troika hace **parsing de fuente, generación de SDF y layout (kerning, ligaduras, RTL, fallback) en un web worker** sin frame drops (no pre-generas atlas). El shader core: `float d=median(...); float alpha=smoothstep(0.5-fwidth(d), 0.5+fwidth(d), d);`. **Limitación 2026:** todo método de textura degrada en magnificación extrema; la novedad es el **Slug algorithm (Lengyel, patentes liberadas mar-2026)** → rendering vectorial GPU atlas-free sin techo de resolución (emergente).

## 3. Extruded 3D text (TextGeometry)

Para volumen físico real que reacciona a la luz:
```js
new FontLoader().load('/fonts/helvetiker_bold.typeface.json', font=>{
  const geo = new TextGeometry('STUDIO', { font, size:1.2, depth:0.35, curveSegments:12,
    bevelEnabled:true, bevelThickness:0.04, bevelSize:0.03, bevelSegments:5 });
  geo.center();   // TextGeometry NO está centrada por defecto
  const mat = new THREE.MeshPhysicalMaterial({ metalness:1, roughness:0.15 }); // o transmission:1 (vidrio)
  scene.add(new THREE.Mesh(geo, mat));
});
```
**Iluminarla bien es el 80%** (metal/transmission necesita un **environment map** o el cromo se ve plano negro; en R3F `<Environment preset="studio" />` + luces de acento). **Performance:** TextGeometry tessela cada glifo a miles de triángulos (`curveSegments`/`bevelSegments` altos multiplican vértices) — caro y **estático** (no actualices el string cada frame). **Hornea** (bake a `.glb`) si la headline es fija; para texto que cambia → MSDF.

## 4. Shader effects sobre texto

El "liquid/chrome 3D type". Modifica el vertex (displacement reactivo a scroll/mouse) y el fragment (gradiente/iridiscencia):
```glsl
// VERTEX — onda reactiva
uniform float uTime; uniform vec2 uMouse; varying vec2 vUv;
void main(){ vUv=uv; vec3 p=position; p.z += sin(p.x*3.0+uTime)*0.12 + length(uMouse-uv)*-0.3; // se hunde hacia el cursor
  gl_Position = projectionMatrix * modelViewMatrix * vec4(p,1.0); }
```
En R3F: `<Text><myDistortMaterial /></Text>` (shaderMaterial de drei) o `MeshTransmissionMaterial` para vidrio líquido. Para **dissolve/disintegración**, el referente 2026 es el **WebGPU Gommage Effect (Codrops, ene 2026)**: disuelve texto MSDF en polvo/pétalos usando **TSL** + compute particles (samplea el SDF para emitir partículas en el contorno; ligado a particle morph ref 155).

## 5. Kinetic 3D type & layout

**Per-letter en 3D:** divide en glifos individuales y animálos con stagger (`'EXPLODE'.split('').map((ch,i)=> <Float key={i}><Text position={[i*0.7-2,0,0]}>{ch}</Text></Float>)`); con GSAP anima `position.z`/`rotation`/opacity con `stagger` para explode/assemble. **Texto en curva/cilindro:** `mesh.position.set(Math.cos(a)*R, 0, Math.sin(a)*R); mesh.lookAt(0,0,0)` (marquee 3D en cilindro). **Scroll-driven:** drei `ScrollControls` + `useScroll`, mapea `scroll.offset` a rotación/posición.

## 6. Performance & a11y (CRÍTICO para texto)

**La trampa #1:** texto dentro de un `<canvas>` WebGL es **invisible para SEO y screen-readers** (para Google y un lector de pantalla tu headline cromada **no existe**) — descalificante en cualquier auditoría seria. **La regla de oro: el texto real vive en HTML; el WebGL es enhancement:**
```html
<h1 class="hero-title">Design in Motion</h1>                  <!-- texto real, indexable -->
<!-- o, si el WebGL DEBE pintar la headline, espejo: -->
<canvas id="gl" aria-hidden="true"></canvas>
<h1 class="sr-only">Design in Motion</h1>
```
**DPR cap** (`gl={{ dpr: Math.min(devicePixelRatio, 2) }}` — MSDF en retina sin cap funde la GPU). **MSDF sobre geometría** (~10× más rápido que canvas-texture, mucho más ligero que TextGeometry para texto animado). **`prefers-reduced-motion`** (desactiva ondas/scroll-distortion, render estático). **Fallback CSS chrome/gradient** (si WebGL no carga, el `<h1>` HTML debe verse premium: `background:linear-gradient(...); -webkit-background-clip:text; color:transparent`).

## 3D-type anti-patterns — blacklist
**texto solo en canvas sin espejo HTML** (invisible a SEO/screen-readers — el pecado capital; siempre `<h1>` real o `.sr-only`) · **TextGeometry para texto que cambia cada frame** (recrea geometría = jank; usa MSDF) · **`curveSegments`/`bevelSegments` altos "por si acaso"** (explosión de vértices invisible al ojo) · **MSDF physical/glass material sin environment map** (cromo negro plano; el reflejo *es* el material) · **sin DPR cap** (retina + MSDF + partículas = 15fps en móvil) · **olvidar `geo.center()`** en TextGeometry (pivote roto en animaciones) · **ignorar `prefers-reduced-motion`** en kinetic type · **bitmap font atlas para headlines escalables** (blur al zoom; MSDF lo resuelve) · **magnificación extrema con MSDF** (bordes degradados; evalúa Slug si necesitas zoom infinito) · **no proveer fallback CSS** (usuarios sin WebGL ven hero vacío).

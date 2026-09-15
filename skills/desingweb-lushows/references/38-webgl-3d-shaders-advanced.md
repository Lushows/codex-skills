# 38 — WebGL, Three.js, R3F & shaders avanzado (web premium)

Cookbook avanzado, más profundo que 08. **Léelo cuando construyas producto 3D, configuradores, shaders o efectos WebGL premium.** Código actual a 2026 (Three r184, R3F v9/React 19). Pareja de 08, 12, 26.

## 1. Decisión de stack & setup 2026

| Caso | Stack | Por qué |
|---|---|---|
| Sitio React/Next con 3D | **R3F v9 + drei** | Declarativo, ecosistema pmndrs, React 19 |
| Efectos 2D de imagen (hover/distorsión/galerías) | **OGL** (~50kb) | Sin escena 3D real, gana a Three (~150kb) |
| Three vanilla, control total | **Three.js r184** | Máximo control |
| Hero decorativo sin lógica | **Unicorn Studio / Spline / Paper Shaders** | No-code, 36kb embed |

**R3F mínimo (producto-vidrio flotante):**
```jsx
<Canvas dpr={[1,2]} gl={{antialias:true,alpha:true,powerPreference:'high-performance'}} camera={{position:[0,0,5],fov:35}}>
  <Float speed={1.5} rotationIntensity={0.4} floatIntensity={0.8}>
    <mesh geometry={nodes.Bottle.geometry}>
      <MeshTransmissionMaterial thickness={0.6} roughness={0.05} ior={1.45} chromaticAberration={0.06} distortion={0.2} samples={6} resolution={512}/>
    </mesh>
  </Float>
  <Environment resolution={256}>
    <Lightformer form="rect" intensity={2} position={[0,3,2]} scale={[4,1,1]}/>
    <Lightformer form="circle" intensity={1.5} position={[-3,1,1]} scale={2} color="#ffd9b3"/>
  </Environment>
  <OrbitControls enableDamping dampingFactor={0.05} enableZoom={false}/>
</Canvas>
useGLTF.preload('/bottle-draco.glb')
```
**Lenis + R3F:** `<ReactLenis root options={{lerp:0.1}}>`; scroll-driven 3D con drei `<ScrollControls pages={3} damping={0.2}>` → `useScroll().offset` dentro de `useFrame`.

## 2. Showcase / configurador de producto 3D

**Pipeline de optimización GLB** (optimize primero, luego inspecciona):
```bash
gltf-transform optimize in.glb out.glb --compress draco --texture-compress ktx2 --texture-size 1024 --simplify true
npx gltfjsx final.glb --transform --types -o Model.jsx   # componente React tipado (corre Draco/KTX2)
```
**Presupuestos:** geometría <100k tris/hero · texturas 1024px (2048 solo para zoom AR) · GLB final <2-3MB · draw calls <100/frame.
**Floating-product-hero:** `<Float>` + `<Environment>` con Lightformers (softbox de estudio). Vidrio/líquido = `MeshTransmissionMaterial` (IOR ~1.45 vidrio, ~1.33 agua). PBR = `meshStandardMaterial` + Environment para reflejos.
**Configurador** (swap material/color sin recargar GLB): `<meshStandardMaterial color={colors[variant]}/>` desde estado React. **Turntable:** `rotation.y = lerp(rotation.y, targetY, 0.08)` en `useFrame`.
**AR:** `<model-viewer src="m.glb" ios-src="m.usdz" ar ar-modes="webxr scene-viewer quick-look" camera-controls>`; AR custom → `@react-three/xr` v6.

## 3. Shaders GLSL para efectos premium

Fundamentos: vertex posiciona (`gl_Position`), fragment colorea (`gl_FragColor`); `uniforms` JS→shader, `varying` vertex→fragment, `uv` coords 0-1. Wiring R3F: `useFrame(({clock,pointer})=>{ u.uTime.value=clock.elapsedTime; u.uMouse.value.lerp(pointer,0.1) })`.
**Gradiente animado:**
```glsl
uniform float uTime; varying vec2 vUv;
void main(){ float w=.5+.5*sin(vUv.x*3.+uTime+vUv.y*2.); gl_FragColor=vec4(mix(vec3(.05,.4,.3),vec3(.9,.5,.7),w),1.); }
```
**Fresnel/rim glow** (la base de todo look atmosférico):
```glsl
varying vec3 vNormal; varying vec3 vViewDir; uniform vec3 uColor;
void main(){ float f=pow(1.-dot(normalize(vViewDir),normalize(vNormal)),3.); gl_FragColor=vec4(uColor*f,f); }
// vertex: vViewDir=normalize(cameraPosition-worldPos.xyz); vNormal=normalize(normalMatrix*normal);
```
**Simplex noise** (motion orgánica) — pega `snoise` (Ashima) → `float n=snoise(vec3(vUv*3.,uTime*.2));`.
**Displacement en vertex:** `vec3 p=position+normal*snoise(vec3(position.xy*2.,uTime*.3))*.25;`.
**Dissolve/reveal:** `if(snoise(vec3(vUv*8.,0.))>uProgress) discard;` + borde incandescente con `smoothstep`.
Partículas/GPGPU: `THREE.GPUComputationRenderer` o `useFBO` (ping-pong) para avanzar posiciones en textura flotante; curl noise (derivado de simplex) para campos de flujo.

## 4. Efectos de imagen & transiciones WebGL

**Hover distortion (RGB-shift por velocidad)** — el patrón Codrops:
```glsl
uniform sampler2D uTex; uniform vec2 uVelocity; uniform float uHover; varying vec2 vUv;
void main(){ vec2 off=uVelocity*.02*uHover;
  float r=texture2D(uTex,vUv+off).r, g=texture2D(uTex,vUv).g, b=texture2D(uTex,vUv-off).b; gl_FragColor=vec4(r,g,b,1.); }
```
`uVelocity` desde JS (`pointer-lastPointer`) o velocidad de Lenis (`lenis.on('scroll',({velocity})=>u.uVelocity.value=velocity)`).
**Transición por displacement entre 2 imágenes:** mezcla `uTex1`/`uTex2` con `mix(...,uProgress)` desplazando UVs por una textura de ruido. **Ripple/fluid:** FBO ping-pong acumulando impulsos del mouse (ecuación de onda).
**Post-processing tasteful** (`@react-three/postprocessing`):
```jsx
<EffectComposer disableNormalPass>
  <Bloom luminanceThreshold={1} intensity={0.6} mipmapBlur/>      {/* selectivo: solo emissive>1 */}
  <ChromaticAberration offset={[0.0008,0.0008]}/>
  <DepthOfField focusDistance={0.02} focalLength={0.05} bokehScale={3}/>
</EffectComposer>
```

## 5. Performance & integración (crítico)

- **DPR cap:** `dpr={[1,2]}` siempre. Nunca `devicePixelRatio` crudo (móvil 3-4× = 9-16× el trabajo).
- **On-demand:** `frameloop="demand"` para estático/configuradores; `invalidate()` tras cambios.
- **Draw calls <100/frame.** `InstancedMesh(geo,mat,N)` → N objetos en 1 draw call.
- **Móvil:** `precision mediump float` (~2× más rápido); shadow maps 512-1024; máx 3 luces con sombra; detecta low-end (`navigator.hardwareConcurrency<=4` → poster estático).
- **Lazy-mount del Canvas (no bloquear LCP):** IntersectionObserver con `rootMargin:'200px'` → monta `<Canvas>` o muestra `<img poster>`.
- **DOM↔WebGL sync:** lee `getBoundingClientRect()` de elementos HTML → coords de mundo → posiciona el plano WebGL. drei `<Html transform occlude>` para HTML sobre la escena.
- **LCP / reduced-motion:** WebGL **NUNCA** es el LCP (poster real primero, monta WebGL después). `prefers-reduced-motion` → desactiva Float/autorotación/shaders animados, 1 frame estático. Al desmontar: `geometry/material/texture.dispose()`.

## 6. No-code & híbridos

- **Paper Design Shaders** (`@paper-design/shaders-react`, zero-dependency): `<MeshGradient colors={['#0a3','#fc7','#e57']} speed={0.3}/>` — fondos/gradientes premium sin GLSL.
- **Unicorn Studio** (no-code WebGL 2D, layers tipo Figma, 36kb): `<div data-us-project="ID">` + `UnicornStudio.init()`.
- **Spline** (3D no-code): `@splinetool/react-spline` `<Spline scene="...splinecode"/>` (más pesado, das control de perf al runtime).
- **Cuándo:** Paper = fondos/gradientes · Unicorn = arte 2D interactivo embebido · Spline = 3D decorativo rápido · **hand-code (R3F/OGL)** en cuanto necesites lógica de negocio, configurador real o presupuesto de perf estricto.

## WebGL anti-patterns
DPR sin cap (quema GPU móvil) · WebGL como LCP · sin fallback móvil/low-end · `frameloop="always"` en escenas estáticas · barrel import de Three (`import * as THREE`) sin tree-shake (~600kb) · no disponer geo/tex/mat al desmontar (memory leak) · escenas sobrecargadas (>100k tris, >100 draw calls, >3 luces con sombra, postprocessing apilado sin medir) · `highp` en móvil cuando `mediump` basta · texturas sin comprimir en vez de KTX2 · ignorar `prefers-reduced-motion` · HDRI 4k+ cuando `resolution={256}` procedural con Lightformers basta.

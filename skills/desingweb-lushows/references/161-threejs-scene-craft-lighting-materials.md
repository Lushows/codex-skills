# 161 — Three.js scene craft (lighting, materials, postprocessing)

**CRAFT, code-heavy.** El fix a "¿por qué mi 3D se ve barato?". Pareja de 08/38 (WebGL/R3F/shaders), 154 (shaders), 164 (WebGPU), 14 (AI imagery). Regla de oro: **environment map (IBL) + ACES tone mapping + color spaces correctos te llevan del 0 al 70% del realismo en ~5 líneas; el problema casi nunca es el modelo, es luz/entorno/color.**

## 1. Por qué la mayoría del 3D web se ve barato

4 razones, ninguna es "el modelo": **sin environment map (IBL)** (un `MeshStandardMaterial` sin `scene.environment` es plástico mate — los PBR *necesitan* algo que reflejar), **tone mapping `NoToneMapping`** (los colores se queman a blancos planos), **color space mal** (texturas albedo como lineal → lavado/sobresaturado), **luz directa dura sin relleno** (sombras negras de PS2). **Checklist "looks rendered":** `toneMapping = ACESFilmicToneMapping` · `outputColorSpace = SRGBColorSpace` · texturas albedo `colorSpace = SRGBColorSpace` · `scene.environment = HDRI` (el cambio #1 en impacto) · sombras suaves (PCFSoft o ContactShadows/AccumulativeShadows) · postpro mínimo (AO + sutil bloom + grain/vignette).

## 2. Lighting — el entorno es el secreto, no las luces

Jerarquía de impacto: **IBL (HDRI) > sombras de contacto > relleno de área > 3-point.**
```jsx
<Environment preset="city" background={false} environmentIntensity={1} /> {/* IBL: ilumina PBR + reflejos */}
<ContactShadows position={[0,-0.5,0]} opacity={0.6} scale={10} blur={2.5} far={4} /> {/* ancla al suelo */}
<directionalLight position={[5,8,5]} intensity={2} castShadow shadow-mapSize={[2048,2048]} shadow-bias={-0.0001}/>
```
**Studio look custom** con `Lightformer` (softboxes virtuales: key + fill frío + rim). **`AccumulativeShadows`** (sombras horneadas en runtime, ideal producto estático). **3-point** sigue valiendo para escenas dinámicas (Key direccional ~45° + Fill ~1/3 opuesto frío + Rim que separa del fondo), pero con IBL presente baja todas las intensidades.

## 3. Materials (PBR) — Standard vs Physical

`MeshStandardMaterial` = metalness/roughness base barato; `MeshPhysicalMaterial` añade clearcoat/transmission/iridescence/sheen (más caro):
```js
new THREE.MeshStandardMaterial({ color:0x8899aa, metalness:1, roughness:0.15 }); // metal (SIN env se ve gris muerto)
new THREE.MeshPhysicalMaterial({ metalness:0.9, roughness:0.5, clearcoat:1, clearcoatRoughness:0.03 }); // car paint
new THREE.MeshPhysicalMaterial({ roughness:0.1, iridescence:1, iridescenceIOR:1.3 }); // iridiscencia (de moda)
```
**Regla de oro PBR:** metalness es casi binario (0 o 1, no 0.5); el realismo vive en el mapa de **roughness** (variación = huellas/microrayas/desgaste; material uniforme = CGI falso). **El vidrio/transmisión (el darling 2026)** con `MeshTransmissionMaterial` (drei): `transmission={1} thickness={1.5} roughness={0.05} ior={1.5} chromaticAberration={0.06} samples={10} resolution={1024}` (renderiza la escena a un buffer — caro; limita samples/resolution; **el vidrio necesita environment map para verse a vidrio**).

## 4. Tone mapping & color — el ajuste que lo cambia todo

```js
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.0;             // tu "dial" 0.8-1.2
renderer.outputColorSpace = THREE.SRGBColorSpace; // default r152+
```
ACES comprime el rango HDR con rolloff suave en highlights (los blancos no se queman a plano, transicionan como cine). **Caveat:** ACES baja contraste/saturación → compénsalo subiendo saturación del HDRI o con `HueSaturation` en postpro. Alternativas: **AgX** (`AgXToneMapping`, r163+, mejor saturación en highlights, Blender-style), **`NeutralToneMapping`** (preserva color de producto, ideal e-commerce). **La trampa #1 de texturas:** mapas de color (albedo/emissive) en `SRGBColorSpace`; mapas de datos (normal/roughness/metalness/AO) en `LinearSRGBColorSpace` (default) — confundirlo da el look "lavado".

## 5. Postprocessing — el stack cinematográfico

`postprocessing` de pmndrs (combina efectos en *un* fragment shader, más barato que `EffectComposer` nativo):
```jsx
<EffectComposer disableNormalPass multisampling={4}>
  <N8AO aoRadius={0.5} intensity={2} />                        {/* AO de contacto: el #1 en realismo */}
  <Bloom mipmapBlur luminanceThreshold={1} intensity={0.6} />  {/* selective: solo emisivos >1 */}
  <DepthOfField focusDistance={0.01} focalLength={0.04} bokehScale={4} /> {/* CARO; foco cinematográfico */}
  <Vignette offset={0.15} darkness={0.6} />
  <Noise opacity={0.04} blendFunction={BlendFunction.OVERLAY} /> {/* film grain: mata el look "CGI limpio" */}
</EffectComposer>
```
**Selective bloom:** es por material, no por pass — para que un objeto brille, saca su color del rango 0-1: `<meshStandardMaterial emissive="hotpink" emissiveIntensity={2} toneMapped={false} />` con `luminanceThreshold={1}`. **Costo (descendente):** DoF > N8AO > Bloom > ChromaticAberration/Vignette/Noise. **Stack mínimo de alto ROI: N8AO + Vignette + Noise** (Bloom solo con emisivos; DoF solo en hero estático).

## 6. Performance

```jsx
<Canvas dpr={[1,2]} frameloop="demand" gl={{antialias:true, powerPreference:'high-performance'}} performance={{min:0.5}}>
```
**`frameloop="demand"`** (mayor ahorro para escenas semi-estáticas; `invalidate()` fuerza frame). **Assets comprimidos** (`.glb` con **Draco** + **KTX2/Basis**; `gltf-transform` recorta 70-90%). **Instancing** (≥100 copias → `InstancedMesh`/drei `<Instances>`). **Bake vs realtime** (escena estática → hornea lightmaps en Blender + `MeshBasicMaterial`). **Mobile fallback** (`detect-gpu`; baja resolution de transmisión, samples de AO, desactiva DoF/sombras realtime; o poster). **WebGL ≠ LCP** (lazy-mount con IntersectionObserver/`next/dynamic ssr:false`; poster estático hasta viewport). **`prefers-reduced-motion`** (pausa autorotación, congela frame). **TL;DR:** env map + ACES + color spaces = 0→70%; sombras de contacto + roughness con variación + postpro sutil = 70→95%; el último 5% es DoF/transmisión/grading (caro, solo el hero shot).

## 3D-scene anti-patterns — blacklist
**`MeshStandardMaterial` sin `scene.environment`** (plástico muerto) · **`metalness: 0.5`** (es 0 o 1; el gris intermedio no existe en la naturaleza) · **`NoToneMapping`** u olvidar ACES/AgX (highlights quemados) · **albedo en `LinearSRGBColorSpace`** (o normal map en sRGB → look lavado) · **`dpr` sin cap** (×3 en retina, GPU en llamas) · **`frameloop="always"` en escena estática** (batería al 100%) · **una sola `DirectionalLight` sin fill ni IBL** (sombras de PS2) · **texturas 4K sin comprimir** (50MB de VRAM) · **roughness uniforme** (CGI falso; mete imperfección) · **DoF + transmisión + bloom a la vez en móvil** (slideshow) · **canvas que bloquea el LCP / monta en SSR** · **`castShadow` sin `shadow-bias`** (shadow acne) · **`emissiveIntensity` alto sin `toneMapped={false}`** (ACES lo aplasta antes de florecer).

# 75 — WebGL / Three.js / shaders / creative coding

3D interactivo y visuales generativos en web (corazón de una agencia de diseño).

## Three.js (npm `three@0.184.0` / r184)
Pilares: **scene** (grafo), **camera** (`PerspectiveCamera(fov, aspect, near, far)`), **renderer**, **mesh**
(geometry + material), **light**. Carga 3D generado por IA con **GLTFLoader** (`.glb`/`.gltf`); navegación
`OrbitControls`; post-procesado `EffectComposer` (bloom, DOF, outline).
```js
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(50, innerWidth/innerHeight, 0.1, 100);
const renderer = new THREE.WebGPURenderer({ antialias:true });        // o WebGLRenderer
new GLTFLoader().load('model.glb', g => scene.add(g.scene));
renderer.setAnimationLoop(() => renderer.render(scene, camera));
```

## React Three Fiber (R3F) + drei
3D declarativo en React: el JSX describe la escena, R3F reconcilia con Three.js. `drei` aporta helpers.
```jsx
<Canvas><ambientLight/><mesh><boxGeometry/><meshStandardMaterial color="coral"/></mesh><OrbitControls/></Canvas>
```

## Shaders (GLSL)
Vertex shader (posición) + fragment shader (color por píxel). **Uniforms** pasan datos JS→GPU (`uTime`, `uMouse`,
`uResolution`). El enfoque "fragment-shader-as-art" (ShaderToy): renderizar un quad full-screen y pintar todo con
matemáticas — incluido **raymarching** (marchar un rayo por SDFs para 3D procedural sin geometría). Para fondos generativos premium.
```glsl
uniform float uTime;
void main(){ gl_FragColor = vec4(0.5+0.5*sin(uTime+gl_FragCoord.xyx), 1.0); }
```

## WebGPU + TSL
WebGPU = el sucesor de WebGL 2026, **soporte universal** (Safari lo añadió sep-2025). Habilita **compute shaders**
(GPGPU: partículas, física, simulación). Three.js trae **TSL (Three.js Shading Language)** desde r171: escribes
shaders como funciones JS componibles que **compilan a WGSL (WebGPU) y GLSL (WebGL)** automáticamente — un código para ambos backends.
```js
import { positionLocal, sin, time } from 'three/tsl';
material.colorNode = sin(time.add(positionLocal.y));
```

## Libs / performance / splats
`p5.js` (generativo/enseñanza), `Pixi.js` (2D acelerado, WebGPU en v8), `GSAP` (animación, estándar Awwwards), `OGL`
(WebGL ultraligero). **Rendimiento:** reduce **draw calls** con instancing (`InstancedMesh` para miles de copias),
merge de geometrías, atlas de texturas, **LOD**. Móvil: limita `pixelRatio` a 2, evita post pesado. **Gaussian splats
en web** (ref 59): `@mkkellogg/gaussian-splat-3d`, `spark` (R3F) renderizan `.ply`/`.splat`/`.ksplat` ordenando millones de gaussianas por profundidad cada frame — pesado, ideal con WebGPU.

## Gotchas
1. **Disposal manual:** Three.js no libera GPU memory por GC; llama `.dispose()` en geometrías/materiales/texturas al desmontar o tendrás leaks.
2. **Demasiados draw calls:** 1000 meshes separados = 1000 draw calls = jank. Usa instancing.
3. **Texturas gigantes:** un PBR 4K ×4 mapas tumba móviles; comprime con KTX2/Basis.
4. **TSL aún madurando:** no todos los nodos/efectos tienen paridad WGSL↔GLSL; verifica en tu target.
5. **Color management:** Three.js usa sRGB/linear por default desde r152+; mezclar espacios da colores lavados.
6. **Splats devoran VRAM:** millones de gaussianas saturan móviles; limita el conteo y usa WebGPU sorting.

**Fuentes:** github.com/mrdoob/three.js/releases/tag/r184 · threejs.org/docs/pages/TSL.html · utsubo.com/blog (WebGPU+Three.js migration 2026).

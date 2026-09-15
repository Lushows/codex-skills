# 155 — Particle systems & point clouds

**CRAFT, code-heavy.** Léelo para partículas atmosféricas, morphing (nube→logo/texto), repulsión de cursor, point clouds. Pareja de 41 (generative), 08/38 (WebGL/R3F), 154 (shaders), 164 (WebGPU compute). Regla de oro: **una partícula debe *significar* algo (polvo, datos, disolución de una palabra) o no debe existir; la densidad coincide con el peso emocional — morphing 500k donde bastaba drift 800 es el error #1.**

## 1. Las familias y qué comunican

| Familia | Conteo | Comunica | Técnica |
|---|---|---|---|
| **Ambient drift** (polvo, esporas, nieve) | 500-3k | atmósfera, profundidad, calma | CPU `Points` |
| **Morphing** (cloud→logo→texto→model) | 30k-500k | transformación, marca, "magia" | GPGPU + target textures |
| **Interactive repel** (huye del cursor) | 5k-200k | presencia del usuario | mouse uniform en sim shader |
| **Point cloud** (look de escaneo 3D/LiDAR) | 100k-2M | tecnología, realidad capturada | `Points` desde `.ply`/`.splat` |
| **Confetti/burst** | 100-2k | logro, recompensa | CPU físico, vida corta |

## 2. CPU particles (simple, hasta ~2-5k)

Cuando la cantidad es baja y la lógica simple (drift, twinkle), no necesitas GPGPU. Un `BufferGeometry` con atributos + update por frame en CPU:
```js
const geo = new THREE.BufferGeometry();
geo.setAttribute('position', new THREE.BufferAttribute(positions, 3)); // Float32Array COUNT*3
const mat = new THREE.PointsMaterial({ size:0.05, sizeAttenuation:true, map:softSprite,
  transparent:true, depthWrite:false, blending:THREE.AdditiveBlending, color:0x9fe8c0 });
// update: p[i*3+1]+=speed*dt; if(p[i*3+1]>10)p[i*3+1]=-10; geo.attributes.position.needsUpdate=true;
```
El cuello de botella es el re-upload del buffer + loop JS: por encima de ~5k notas coste en móvil → GPGPU.

## 3. GPGPU / FBO particles (la técnica pro, 100k-1M+)

Idea: **la CPU no toca las posiciones**. Guardas posición (y velocidad) en un **píxel de una textura** (RGB=XYZ). Un sim shader lee esa textura y escribe la siguiente, en **ping-pong** entre dos render targets (nunca lees y escribes la misma). Un material de render lee la textura de posición y coloca los puntos (1024² = 1M partículas).
```js
import { GPUComputationRenderer } from 'three/addons/misc/GPUComputationRenderer.js';
const gpu = new GPUComputationRenderer(512, 512, renderer); // 512² = 262144
const posVar = gpu.addVariable('texturePosition', simFragment, pos0);
gpu.setVariableDependencies(posVar, [posVar]); gpu.init();
// loop: gpu.compute(); renderMat.uniforms.uPos.value = gpu.getCurrentRenderTarget(posVar).texture;
```
```glsl
// simFragment (corre 1 vez por partícula por frame)
vec3 pos = texture2D(texturePosition, uv).xyz;       // estado anterior (ping-pong auto)
vec3 flow = curlNoise(pos*0.3 + uTime*0.1)*0.02;     // turbulencia
vec3 toTarget = (texture2D(uTarget,uv).xyz - pos)*0.04; // resorte a la forma
vec3 d = pos - uMouse; vec3 repel = normalize(d)*smoothstep(1.5,0.0,length(d))*0.15; // repulsión cursor
gl_FragColor = vec4(pos + flow + toTarget + repel, 1.0);
```
En **TSL/WebGPU** (r160+) esto se escribe con compute nodes y `storage()` buffers, sin el truco de textura (ref 164).

## 4. Morphing particles (la palabra que se forma)

Necesitas **posiciones objetivo** en una `DataTexture` con el mismo layout. **Desde imagen/texto:** render el texto a un `<canvas>`, lee los píxeles, cada píxel oscuro = una posición objetivo (`if(img[i]>128) pts.push(x,y,0)`). **Desde modelo 3D:** `MeshSurfaceSampler` muestrea N puntos sobre la superficie. La transición es un `mix` con `uProgress` (GSAP/scroll), con **delay por partícula** + curl noise durante el vuelo:
```glsl
float t = smoothstep(0.0,1.0, clamp(uProgress*1.5 - aDelay, 0.0, 1.0));
vec3 pos = mix(shapeA, shapeB, t) + curlNoise(shapeA+uTime)*(1.0-t)*0.5;
```
La secuencia cloud→texto→logo→model es solo intercambiar `uTarget`/`shapeB` y relanzar `uProgress`.

## 5. Interacción

**Repulsión/atracción de cursor** (raycast un plano invisible → `uMouse` vec3 → fuerza en el sim shader; atracción = invierte el signo; suaviza el mouse con lerp). **Curl noise flow** (campo libre de divergencia → fluyen sin colapsar; el "default bonito" para idle). **Scroll-driven assembly** (mapea `scrollProgress` → `uProgress`: la nube se ensambla al bajar, se desintegra al subir; con Lenis para que no haya saltos).

## 6. Performance & gusto

**Point size + DPR** (`renderer.setPixelRatio(Math.min(devicePixelRatio,2))`; puntos de 1px en retina desaparecen → mínimo 1.5-2px). **Additive blending + soft sprite** (`AdditiveBlending` + `depthWrite:false` + textura radial = glow que se acumula; sin sprite suave los puntos son cuadrados feos; el additive sobre fondo oscuro da el look "energía"). **Draw calls** (un `Points` = un draw call sin importar el conteo; para meshes usa `InstancedMesh`; nunca un mesh por partícula). **`frameloop="demand"`** si la escena es estática hasta interacción; pausa con `IntersectionObserver` fuera de viewport. **Presupuesto móvil** (divide el conteo por 4-8; 1M desktop → ~64-128k móvil; baja la textura GPGPU a 256²/512²). **`prefers-reduced-motion`** (congela la sim en un estado estático bonito, no la ocultes). **Atmósfera vs ruido:** partículas lentas, pocas, de bajo contraste que refuerzan profundidad/marca = atmósfera; rápidas, brillantes, muchas que compiten con el texto legible = ruido.

## Particle anti-patterns — blacklist
**partículas blancas a `size:1` sobre fondo blanco** (invisibles/sucias) · **quad duro sin textura radial** (puntos cuadrados pixelados; usa soft sprite o `discard` por distancia al centro) · **re-upload de buffers de 100k+ en CPU cada frame** (eso es trabajo de GPGPU) · **un Mesh/Sprite por partícula** (miles de draw calls; usa Points/InstancedMesh) · **`depthWrite:true` con additive** (artefactos de orden, bordes negros) · **no tocar DPR** (1M puntos × DPR 3 en móvil = horno) · **morphing a 500k cuando el momento pedía 800 de drift** · **`frameloop="always"` fuera de viewport** (quema batería invisible) · **ignorar `prefers-reduced-motion`** · **curl noise a velocidad alta como fondo de texto** (atmósfera → ruido ilegible) · **point cloud crudo sin tono/recorte** (se ve como datos, no diseño) · **GPGPU sin sembrar el estado inicial** (textura a cero = "explosión" no intencionada en frame 1).

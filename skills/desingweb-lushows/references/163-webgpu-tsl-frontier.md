# 163 — Frontera del rendering: WebGPU & TSL

**CRAFT, avanzado.** Léelo para WebGPU, Three Shading Language, compute shaders — el techo creativo de 2026. Pareja de 12 (frontier 2026), 08/38 (WebGL/Three), 154 (GLSL), 155 (partículas GPGPU). Regla de oro: **WebGPU gana cuando hay *cómputo* o *cantidad masiva de objetos*; si tu escena es un glTF estático con OrbitControls, WebGL2 te sirve y WebGPU no mueve la aguja. TSL escribe una vez y compila a GLSL Y WGSL.**

## 1. Estado de WebGPU en 2026: ya es baseline

**Baseline en los cuatro motores:** Chrome/Edge (estable desde Chrome 113), Firefox (Windows 141+, macOS ARM 145+), **Safari (shipped en Safari 26, sept 2025** — macOS Tahoe/iOS/iPadOS/visionOS 26). Cobertura real **~95%** con el ~5% restante cayendo a WebGL2 automáticamente. **Qué te da sobre WebGL:** **compute shaders** (GPGPU nativo — *lo* que WebGL nunca tuvo; fin del hack de ping-pong de FBOs), API moderna explícita (pipelines/bind groups), mejor perf en draw calls altos (2-10× con 50k+ instancias; 10-100× en compute), **storage buffers** (arrays de memoria GPU que persisten entre frames). **Adoptar vs WebGL:** si tu cuello de botella es upload de texturas o compilación de shaders, **WebGPU no ayuda**; gana con *cómputo* o *cantidad masiva*. **El fallback es el regalo:** en Three, `WebGPURenderer` detecta `navigator.gpu` y cae a WebGL2 solo — escribes una vez (en TSL), corre en ambos.

## 2. Three.js WebGPURenderer: la migración

```js
import * as THREE from 'three/webgpu';   // OJO al subpath
const renderer = new THREE.WebGPURenderer({ antialias:true });
await renderer.init();                    // ← CRÍTICO
```
**El gotcha #1:** la init de WebGPU es **asíncrona** — si olvidas `await renderer.init()`, tu escena renderiza **nada, sin error, en silencio** (canvas negro, hora perdida). **R3F** funciona vía factory async en `gl`. La mayoría de drei va sin cambios. **Qué NO porta auto:** shaders GLSL crudos (`ShaderMaterial`; reescribe en TSL o mantén dos rutas con `renderer.isWebGPURenderer`), post-processing de pmndrs (varios passes no corren; usa `THREE.PostProcessing` + passes TSL). **Esfuerzo honesto:** sin shaders custom 1-2h; con GLSL a convertir 1-2 días; app grande con post-pro 1-2 semanas.

## 3. TSL (Three Shading Language): el futuro de los shaders

Sistema de shaders **basado en nodos, escrito en JavaScript**, que compila a **GLSL *y* WGSL** (escribes una vez, el compilador emite el dialecto según el renderer). **Por qué es el futuro:** portable (un código, dos backends), composable (los nodos son funciones JS reutilizables), debuggable (es JS — logueas, inspeccionas el grafo, refactorizas con tu IDE), abstrae el boilerplate de bind groups/uniforms. Nodos: `uv()`, `texture(map,uv())`, `float()`, `vec3()`, `mix(a,b,t)`, `uniform()`, `Fn()`, operadores method-chain (`.add()`, `.mul()`, `.pow()`, `.normalize()`):
```js
import { Fn, uv, vec3, vec4, mix, uniform, sin, time } from 'three/tsl';
const material = new THREE.MeshBasicNodeMaterial();
material.colorNode = Fn(()=>{ const t = sin(uv().x.add(time)).mul(0.5).add(0.5);
  return vec4(mix(colorA, colorB, t), 1.0); })();
```
Lo asignas a slots semánticos (`colorNode`, `positionNode`, `normalNode`, `emissiveNode`, `roughnessNode`). Usa `MeshStandardNodeMaterial` y conservas el pipeline PBR completo mientras inyectas lógica. **Regla:** salvo que necesites una feature aún no cubierta, TSL es la forma recomendada de escribir shaders en Three hoy.

## 4. Compute shaders (la superpotencia de WebGPU)

Corre código arbitrario en la GPU **fuera del pipeline de rasterización**. En WebGL simulabas partículas codificando posiciones en texturas + ping-pong de FBOs (frágil, indirecto); con WebGPU escribes directo a **storage buffers** que persisten entre frames:
```js
import { Fn, instancedArray, instanceIndex, vec3, deltaTime } from 'three/tsl';
const positions = instancedArray(1_000_000, 'vec3'), velocities = instancedArray(1_000_000, 'vec3');
const updateCompute = Fn(()=>{ const pos=positions.element(instanceIndex), vel=velocities.element(instanceIndex);
  vel.addAssign(vec3(0,-9.8,0).mul(deltaTime)); pos.addAssign(vel.mul(deltaTime)); })().compute(1_000_000);
// loop: renderer.compute(updateCompute);  // el positionNode del material lee el mismo buffer: cero transfer CPU↔GPU
```
**Cuándo cambia lo posible:** 1M+ partículas a 60fps, fluidos (SPH), N-body, boids, cloth, atractores caóticos — todo en GPU (lo que en WebGL costaba 50k con hacks).

## 5. Qué se vuelve posible

Sistemas de partículas masivos (millones con física real), fluidos reales (SPH, no fakes 2D), post-processing más rápido (passes TSL nativos), ML inference en GPU (style transfer/segmentación vía compute), WebXR + WebGPU (Vision Pro renderiza con WebGPU). **El techo creativo sube.**

## 6. Adopción pragmática & perf

Progressive enhancement: `if(navigator.gpu){ /* WebGPU + TSL */ } else { /* WebGL2 o 2D degradado */ }` (con WebGPURenderer el fallback a WebGL2 es automático igual). **Las reglas viejas siguen:** cap DPR (`Math.min(devicePixelRatio,2)`), **lazy-load** el módulo `three/webgpu` (dynamic import, es pesado), `prefers-reduced-motion` (baja `COUNT`/pausa el compute), **dispose explícito** (`buffer.destroy()` o memory leak), throttle en `visibilitychange`. **Es prematuro cuando:** escena estática/simple, equipo que no domina shaders, audiencia legacy/low-end donde WebGL2 ya entrega.

## WebGPU/TSL anti-patterns — blacklist
**olvidar `await renderer.init()`** (canvas negro silencioso, sin error — el bug #1) · **mezclar imports `three` + `three/webgpu`** (inconsistencias; un solo subpath) · **checks de capability WebGL** (`gl.capabilities.isWebGL2` → `undefined`; usa `gl.isWebGPURenderer`) · **esperar que tu GLSL de `ShaderMaterial` "simplemente funcione"** (no porta; reescribe en TSL) · **no hacer `buffer.destroy()`** en storage/compute buffers (memory leak GPU) · **adoptar WebGPU "porque es nuevo"** en escenas estáticas sin compute · **DPR sin cap** asumiendo que "WebGPU es rápido" · **`computeAsync` de init en cada frame** (init una vez, update por frame) · **bundlear `three/webgpu` síncrono en la ruta crítica** (TTI destrozado; dynamic import) · **asumir pmndrs/postprocessing funciona** sobre WebGPURenderer (usa `THREE.PostProcessing` + passes TSL).

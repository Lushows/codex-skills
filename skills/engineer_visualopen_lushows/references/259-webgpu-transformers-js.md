# 259 · Inferencia en el navegador (WebGPU + transformers.js + ONNX-web)

> Cero servidor, cero egress, cero clave API expuesta: el modelo se descarga al cliente y corre en SU GPU.
> WebGPU convirtió "IA en el browser" de demo de juguete a algo de producción — con asteriscos grandes.

## El stack
- **transformers.js v3** (Hugging Face): corre 🤗 Transformers en el browser. v3 shippeó oct-2024 con **WebGPU**, 120+ arquitecturas y 1200+ modelos pre-convertidos en el Hub. Activar WebGPU = `device: 'webgpu'` al cargar el pipeline.
- **onnxruntime-web**: el motor por debajo. transformers.js **solo come modelos ONNX**. Backends: WASM (universal), WebGPU (rápido), WebGL (legacy).
- **WebLLM / WebGPU directo**: para LLMs grandes (Llama 3.2) compilados a WebGPU sin transformers.js.

```js
import { pipeline } from '@huggingface/transformers';
const pipe = await pipeline('feature-extraction', 'Xenova/all-MiniLM-L6-v2',
  { device: 'webgpu', dtype: 'q4' });          // cuantizado a 4-bit, GPU del cliente
```

## WebGPU vs WASM: el salto que importa
| | WASM | WebGPU |
|---|---|---|
| Velocidad relativa | base | **hasta ~100×** en cargas paralelas |
| Soporte global | universal | ~**70%** (2024), subiendo |
| Cae a | — | fallback automático a WASM |
| Bueno para | embeddings ligeros, móvil sin GPU | generación, modelos medianos |

Patrón correcto: **siempre escribir el fallback a WASM**. El mismo código corre en todos lados; solo va más rápido donde hay WebGPU. No asumas WebGPU presente (Safari/iOS llegó tarde, navegadores corporativos lo bloquean).

## Qué sí y qué no en el browser
**Sí (producción hoy):** embeddings para búsqueda semántica local, clasificación de imagen/texto, ASR (whisper-web), TTS (Kokoro/HeadTTS), VLMs pequeños (SmolVLM), LLMs cuantizados chicos. Privacidad total: la data nunca sale del tab.
**No / con dolor:** difusión SDXL/FLUX completa (pesos de GB + tiempo de paso prohibitivo), video, cualquier cosa que necesite VRAM real sostenida. La generación de imagen pesada sigue siendo servidor.

## Costo y descarga: el cuello real
- El modelo se **baja al cliente** la primera vez: un modelo de 200MB-1GB mata el cold start y el ancho de banda móvil.
- Cachea con **Cache API / OPFS** para no re-bajar en cada visita.
- Cuantiza agresivo (`dtype: 'q4'`/`'q8'`) — menos bytes que bajar y menos VRAM en el cliente.
- WebGPU tiene su propio cold start: compilar shaders no es gratis; precalienta con un run dummy.

## Gotchas
- **Solo ONNX**: si tu modelo no está en el Hub como ONNX, hay que exportarlo (`optimum`); ops no soportadas rompen el export.
- **Sin DOM desde el worker**: corre la inferencia en un **Web Worker** para no congelar la UI; el cruce de tensores tiene costo, evita llamadas chatty.
- **Memoria del tab**: el browser mata pestañas glotonas; vigila VRAM/heap, libera pipelines no usados.
- **Heterogeneidad de GPU**: el mismo modelo vuela en una RTX y se arrastra en una iGPU; mide en hardware de gama baja.
- **70% de soporte ≠ 100%**: detecta `navigator.gpu` y degrada con dignidad, no asumas.

## Cuándo elegir browser sobre servidor
Elige browser cuando: la privacidad es el producto (la foto/voz no debe salir), quieres latencia sin red, o cero costo de GPU por usuario. Elige servidor cuando: el modelo pesa GBs, necesitas calidad SOTA o usuarios en móviles débiles.

Cruza con [[73-edge-computing-wasm]], [[261-browser-avatar-gen]] y [[72-busqueda-semantica-embeddings]].

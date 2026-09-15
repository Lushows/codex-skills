# 108 — IA local / on-device (2026)

> Snapshot fechado. 2026 consolidó la IA local como alternativa real a la nube para muchos casos.

## Runtimes
- **Ollama** — iteración rapidísima. **Desde 0.19 (30 mar 2026) reemplazó su motor por MLX en Apple Silicon**: en M5 Max con Qwen3.5-35B-A3B, prefill +57%, decode +93%.
- **LM Studio 0.4.14** — MTP speculative decoding estable, mejor GUI.
- **llama.cpp / GGUF** — estándar de cuantización portátil. **MLX** (Apple) — 20-30% más rápido que llama.cpp en Apple Silicon.
- **WebLLM / transformers.js** — LLMs en el navegador vía WebGPU.

## Mejores modelos pequeños 2026
- **Qwen3.6-35B-A3B** (abr 2026) — MoE, solo **3.5B params activos** de 35B → rápido. "El modelo que hace que valga la pena la IA local en Mac." ⚠️ Pero el archivo de 20GB debe caber en RAM.
- **Gemma 4** (Google) — 12B corre en 16GB RAM con audio nativo; 26B MoE a 85 tok/s en consumer.
- **gpt-oss** (OpenAI, Apache 2.0, 20B y 120B). **Phi/SmolLM** para ultra-ligero.

## Phone/NPU & Apple
**Gemini Nano** en Pixel/Samsung; **Nano V3** soportado por MediaTek **Dimensity 8550** ("LLM Booster") → gama media.
**Google LiteRT** (LLMs en Android sin nube), **Snapdragon 8 Elite** (APIs NPU abiertas). **Apple Foundation Models**
framework: apps de terceros usan el modelo on-device (~3B) gratis. **M5** corre LLMs locales hasta **4× más rápido** que M4 Pro en prompts.

**Local vs cloud:** local gana en privacidad, costo marginal cero, offline, latencia. Cloud gana en modelos frontera (razonamiento PhD, contextos enormes, agentes complejos).

## Gotchas
1. MoE: el archivo completo (20GB) debe caber en RAM/VRAM aunque solo 3B estén activos → "3B ≠ ligero".
2. Cuantización agresiva (Q4 y menos) degrada razonamiento/código más que chat.
3. Ollama+MLX solo Apple Silicon; en Windows/NVIDIA usa llama.cpp/CUDA.
4. Las NPUs de teléfono optimizadas para modelos del fabricante; GGUF arbitrario cae a CPU/GPU, no NPU.
5. "Corre en mi laptop" ≠ velocidad usable; sin GPU/Apple Silicon decente, decode lento.
6. **Para BIO-SETA/Addrian:** un modelo local NO reemplaza a Claude en la nube para conversación de ventas matizada; sirve para clasificación/extracción barata offline.

**Fuentes:** codersera.com (local AI runtimes may 2026) · ollama.com/blog/mlx · gsmarena.com (Dimensity 8550) · apple.com/newsroom (M5) · machinelearning.apple.com.

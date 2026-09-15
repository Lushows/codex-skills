# 81 — Modelos de generación de IMAGEN: estado del arte (junio 2026)

> Snapshot fechado — el churn es brutal, re-verifica. Mercado multipolar: ningún modelo gana en todo.

## Líderes closed (API)
- **GPT Image 2** (OpenAI) — reemplazó a 1.5 en **abril 2026**. #1 en blind-arena (~509) por photoreal, prompt adherence compleja y texto multilingüe. Precio por imagen no transparente `[no verificado]`.
- **Nano Banana Pro / Gemini 3 Pro Image** (Google) — **GA junio 2026**. ~$0.134/img a 2K, **$0.24 a 4K**, batch 50% off. 2-5s, **best-in-class en text rendering** (carteles, tipografía legible), watermark SynthID. El rey de realismo + claridad comercial.
- **Imagen 4 Ultra** (DeepMind) — el output más fotorrealista de 2026 (piel/telas/reflejos casi indistinguibles).
- **Seedream 5.0 Lite** (ByteDance, ~ene/feb 2026, **$0.035/img**) — "knowledge-driven" con búsqueda web en tiempo real. El 5.0 full NO liberado. Seedream 4.5 = rey de lo estilizado.
- **Midjourney V7** — líder de **calidad estética/cinematográfica**. ~$0.30-0.60/img, más lento.
- **Ideogram 3** — líder en tipografía. **Recraft V3** — único con **SVG vectorial nativo** ($0.08/img vector).

## Open weights (la gran historia 2026)
- **FLUX.2** (BFL): familia **[max]/[pro]/[dev]/[klein]**. [max] = máxima consistencia de edición; **Pro** = el default (velocidad+calidad+precio); fuerte en retratos face-forward. **[klein]** (15 ene 2026): flow 9B + Qwen3-8B text, distilado a 4 pasos, top open-weights en editing arena. **Licencia mixta: 4B = Apache 2.0; 9B = NON-commercial.**
- **Z-Image** — **100% Apache 2.0** en todas las variantes (Turbo/foundation/Omni/Edit): comercial+fine-tune+self-host sin pagar. **La opción open más limpia legalmente.**
- **Qwen-Image 2.x** — licencia propietaria, fuerte en edición.

## Gotchas
1. "Nano Banana Pro" = oficialmente **Gemini 3 Pro Image** — verifica el SKU que llamas.
2. Todo output de Google lleva **SynthID** invisible — relevante si necesitas imágenes "limpias".
3. **FLUX.2 9B es NON-commercial** — fácil violar la licencia self-hosteándolo para un producto; usa 4B Apache o Z-Image.
4. Seedream 5.0 "full" NO liberado; lo disponible es **5.0 Lite** — no asumas paridad.
5. El 4K en Nano Banana Pro casi duplica el costo vs 2K — controla la resolución.
6. GPT Image 2 lidera en votos pero sin precio transparente — presupuestar es difícil.

**Fuentes:** llm-stats.com/leaderboards (image) · bfl.ai/blog/flux2-klein · zimage.design · deepmind.google/models/gemini-image · seed.bytedance.com (Seedream).

# 83 — LLMs frontier: estado del arte (junio 2026)

> Snapshot fechado. SOTA dividido por eje: Claude=coding/escritura, GPT-5.5=agentic/terminal/long-context, Gemini 3.1=multimodal/razonamiento/precio.

## Claude (Anthropic)
- **Opus 4.8 — 28 mayo 2026.** **88.6% SWE-bench Verified**; **69.2% SWE-Bench Pro** (vs 58.6% GPT-5.5, 54.2% Gemini 3.1). **SOTA de coding** y escritura matizada.
- **Sonnet 4.6** — caballo de batalla costo/calidad para coding.

## OpenAI
- **GPT-5.5 ("Spud") — 23 abr 2026.** **$5/$30 por 1M tokens** (Batch/Flex 50% off). SWE-Bench Pro 58.6%, pero **gana en Terminal-Bench 2.0 (82.7% vs 69.4% Opus)** y long-context retrieval. Cerró la fine-tuning API. **gpt-oss** = open weights competitivo.

## Google
- **Gemini 3.1 Pro — Preview 19 feb 2026.** **$2/$12 por 1M** (>200K tokens: $4/$18). **Context 2.0M tokens.** 80.6% SWE-bench; domina multimodal (Video-MME 78.2%). **El más barato del trío frontier** a tier estándar.

## Open weights / otros
- **DeepSeek V4 Pro: $0.435/$0.87 por 1M; Flash: $0.14/$0.28.** Context 1M, output 384K. R2/V5 pendiente.
- **Qwen 3.7 Max: $2.50/$7.50, context 1M**; open **Qwen 3.6-35B** (262K). **Llama 4 Maverick** (400B, 1M, $0.27/$0.85). **Grok 4.3: $1.25/$2.50, 1M**; Grok 4 Fast expone **2.0M tokens**. **GLM-5 y MiniMax M2.5** (open) ya rivalizan en SWE-bench.

## Gotchas
1. **SWE-bench Verified ≠ SWE-Bench Pro ≠ Pro Public** — los rankings se invierten según cuál cites; nombra el subset exacto.
2. Gemini 3.1 **sube de tier a >200K tokens** ($4/$18) — el "barato" se encarece en prompts largos.
3. GPT-5.5 **subió de precio** y **cerró fine-tuning API** — re-evalúa si dependías.
4. Context "1M-2M" es nominal; el **recall efectivo** cae mucho antes (GPT-5.5 destaca aquí).
5. **Costo+calidad frontier:** Gemini 3.1 o DeepSeek V4. **Coding crudo:** Opus 4.8.
6. **Muchas versiones casi-homónimas** (Opus 4.6/4.7/4.8, GPT-5.4/5.5, Gemini 3/3.1) — **fija el ID exacto en producción.**

**Fuentes:** vellum.ai/blog (Opus 4.8) · llm-stats.com · llm-stats.com/benchmarks/swe-bench-verified · morphllm.com (DeepSeek V4).

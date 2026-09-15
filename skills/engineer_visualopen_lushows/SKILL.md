---
name: engineer_visualopen_lushows
description: >-
  Manual de ingeniería de élite para CONSTRUIR, DESPLEGAR y VENDER software y apps de IA
  end-to-end (366 referencias bajo demanda). NÚCLEO — auto-hospedar IA VISUAL open-source
  (avatares parlantes, video, imagen, lip-sync, TTS, 3D) en GPU serverless BARATO y CORRECTO:
  RunPod/Modal/Replicate, CUDA/torch/flash_attn/xformers (ABI), OOM de RAM/VRAM, modelos que
  cargan sub-modelos, sizing de disco y Network-Volume, video segmentado/largo, elegir GPU
  (Ampere/Ada/Hopper/Blackwell), HANDLER de producción, integrar app (submit/poll/webhook,
  timeouts, cold-start, execution-timeout), build Docker (GHCR+Actions, smoke-test), afinar
  VRAM/fragmentación/OOM-mid-run, torch.compile/TensorRT, cuantización (fp8/SVDQuant/GGUF/AWQ/
  torchao), multi-GPU (context/sequence parallel), serving (ComfyUI/Triton/vLLM/SGLang), billing
  de RunPod, storage R2/S3, evals (FID/FVD/LSE), ffmpeg, resiliencia/fallback a API premium.
  AHORA TAMBIÉN FULL-STACK DE PRODUCTO: web frontend (React/Next/Tailwind/forms/animación/testing)
  y seguridad web (CSP/XSS/CSRF/CORS, auth OAuth2.1/passkeys, secrets, supply-chain), backend y
  APIs (REST/OpenAPI/GraphQL/webhooks/background-jobs/uploads), bases de datos (Postgres/Redis/
  vector-DBs/ORMs/migraciones/sharding), auth y PAGOS LatAm (Stripe/Wompi/MercadoPago/PSE/Nequi,
  facturación electrónica DIAN/SAT), DevOps (CI-CD/Docker/deploy Vercel-Render-Fly/observabilidad/
  IaC), cloud y serverless (Cloudflare Workers/D1/R2/edge/colas/cron), patrones de apps de IA
  (RAG/agentes/MCP/memoria/evals/guardrails/streaming-UI/function-calling/cost-control), MESSAGING
  para negocios (WhatsApp-Cloud/Baileys/chatbots/Telegram/Discord/inbox omnicanal), growth (SEO/
  analytics-PostHog-GA4/A-B-testing/CRO/funnels/referral), producto y UX (onboarding/pricing-page/
  dashboards/design-systems/accesibilidad), mobile (React-Native/Expo/push/offline-sync), SaaS
  (multi-tenancy/billing/créditos/métricas-MRR-churn-LTV/legal-LatAm-Habeas-Data/soporte), data-eng
  (ETL-ELT/warehouse/dbt/event-schema/BI), automatización (n8n/Make/scraping/browser-automation/RPA),
  realtime y colaboración (WebSockets/SSE/WebRTC/CRDT-Yjs/presence/LiveKit), performance y escala
  (Core-Web-Vitals/caching-multicapa/load-testing/rate-limiting), fiabilidad y ops (resilience-
  patterns/monitoring-on-call/incident-postmortems/backups-DR/feature-flags) y copywriting/contenido
  (AIDA-PAS/SEO-writing/email/social). Usar para CUALQUIER decisión de ingeniería, infra, costo,
  seguridad, datos o producto al construir software (con o sin IA), no solo GPU.
  Marca: Lushows / AGENTE STUDIO.
---

# engineer_visualopen_lushows

Manual de ingeniería para desplegar IA visual open-source en GPU serverless. Nace de
una sesión real (LongCat-Video-Avatar 1.5 en RunPod) donde se perdieron horas por
errores evitables. **La meta: cero adivinanzas, estructura actual, iteración fluida.**

## 📚 Biblioteca de referencias (carga bajo demanda, `references/`)

El cuerpo de este SKILL.md es el núcleo (reglas, matriz, debug, costo, handler, build).
Para profundidad por tema, lee el archivo de `references/` correspondiente:

- **`references/01-audio-avatar-pipeline.md`** — audio que mueve la boca: separación de voz
  (audio-separator/UVR), encoders (Whisper vs wav2vec2), prep (16kHz, pyloudnorm, alineación
  frames↔audio), evaluar sync (LSE-C/LSE-D), TTS open (F5/Kokoro/XTTS). **Léelo para avatares/lip-sync.**
- **`references/02-open-models-catalog-2026.md`** — catálogo de modelos visuales open con params, VRAM
  (fp16→quant), **licencia** y fit por tarjeta (24/48/80GB). Avatares, T2V/I2V, imagen, lip-sync.
  **Léelo al ELEGIR modelo** (ojo licencias: FLUX-dev/FLUX.2 non-commercial; LongCat-Avatar=MIT).
- **`references/03-model-customization-lora-controlnet.md`** — **LoRA** (cargar/apilar/fusionar/entrenar),
  **ControlNet**, **IP-Adapter/InstantID**, img2img/inpaint/condición de video, y **prompt engineering**
  (weighting, negatives, CFG distilled). **Léelo para personalizar/condicionar un modelo o afinar prompts.**
- **`references/04-systems-layer-gateway-queue.md`** — la app que fronta la GPU: **async Python** (GIL,
  asyncio/threads/procesos), **FastAPI gateway** (BackgroundTasks NO es cola), **Postgres como cola**
  (FOR UPDATE SKIP LOCKED, LISTEN/NOTIFY), brokers (Celery gotchas), caché/dedup, rate limiting, API design.
  **Léelo al construir el backend que orquesta los jobs.**
- **`references/05-tts-voice-cloning-2026.md`** — **TTS open + clonación de voz**: catálogo con licencia
  (Kokoro/Chatterbox/CosyVoice2/Fish/Higgs Apache-MIT; F5/XTTS non-commercial), zero-shot (segundos de ref,
  es-CO), streaming/latencia, emoción, self-host vs API, flujo "voz de WhatsApp" (Whisper→LLM→TTS). **Léelo para voz.**
- **`references/06-comfyui-backend-produccion.md`** — **ComfyUI headless como API**: `/prompt`+WS+`/history`,
  API format, custom nodes/Manager/snapshots, comfy-deploy/serverless, `extra_model_paths.yaml`, ComfyUI vs
  handler vs diffusers. **Léelo si tu pipeline es un node-graph.**
- **`references/07-training-finetuning-a-fondo.md`** — **LoRA/DreamBooth/full/TextInv** (cuándo cada uno),
  dataset prep (imgs/captions/buckets/reg), tools (kohya/ai-toolkit/SimpleTuner/OneTrainer), hiperparámetros
  REALES SDXL vs FLUX, overfitting, LoRA de VIDEO (Wan/LTX/motion). **Léelo para entrenar.**
- **`references/08-upscaling-restauracion.md`** — **Real-ESRGAN/SUPIR/SwinIR/HAT** + cara **GFPGAN vs
  CodeFormer** (`fidelity_weight`), tiled upscaling sin OOM, pipeline 480p→1080p, restauración de video
  (temporal). **Léelo para upscale/restaurar.**
- **`references/09-interpolacion-edicion-video-ffmpeg.md`** — **RIFE/FILM/IFRNet** (interpolar fps), pipeline
  render-chico→interpolar→upscalar, **ffmpeg avanzado** (concat/trim `-c copy`/crop/overlay/fade/subs/audio/
  GIF), codecs H.264/VP9/AV1 + faststart/yuv420p. **Léelo para editar/exportar video.**

### Roadmap de referencias (✅ 366/366)
**Dominio (IA visual/avatar):** 01 audio-avatar · 02 catálogo modelos · 03 LoRA/ControlNet · 05 TTS/clonación
voz · 06 ComfyUI backend producción · 07 training/fine-tuning a fondo · 08 upscaling/restauración (Real-ESRGAN/
GFPGAN/CodeFormer/SUPIR) · 09 interpolación + edición de video.
**GPU/infra:** 10 profiling/optimización (torch profiler/nsight) · 11 TensorRT/ONNX/compilación AOT · 12
cuantización con código · 13 multi-GPU/distribuido (FSDP/DeepSpeed/NCCL/context-parallel) · 14 batching/KV-cache/PagedAttention.
**Serving/MLOps:** 15 observabilidad prod (Prometheus/Grafana/DCGM/Sentry/OTel) · 16 CI/CD para modelos · 17
evals generativos (FID/FVD/CLIP/LSE) · 18 model registry/versionado · 19 load-testing/capacity (Ley de Little).
**Arquitectura de código/sistemas:** 04 gateway/cola · 20 diseño de APIs (REST/gRPC/GraphQL) · 21 Postgres a fondo
+ pgvector · 22 caching/CDN · 23 event-driven (Kafka/Streams/outbox/saga) · 24 microservicios vs monolito ·
25 código limpio (SOLID/pydantic/types) · 26 testing a fondo (pytest/mocking/e2e).
**Seguridad/ops:** 27 seguridad de apps (OWASP 2025/authn/JWT/OAuth) · 28 seguridad de IA/agentes (prompt injection/
guardrails/OWASP LLM Top 10) · 29 IaC & deploy (Docker/Terraform/k8s/Render) · 30 FinOps de GPU.
**LLM & RAG (ola 2):** 31 RAG a fondo (chunking/embeddings/rerank/hybrid/RAGAS) · 32 agentes y tool-use (ReAct/
MCP/LangGraph/cuándo agente vs workflow) · 33 servir tu propio LLM (vLLM/SGLang/structured output) · 34 prompt
engineering LLM (system prompt/structured/prompt-caching/reasoning) · 35 vision encoders y VLMs (CLIP/SigLIP/DINOv3, auto-caption/moderación).
**Dominio extendido (ola 2):** 36 datasets/scraping/captioning (auto-caption training) · 37 moderación/safety de
imagen (NSFW/**CSAM obligación legal**) · 38 watermarking/procedencia (C2PA/SynthID/EU AI Act Art.50) · 39 legal de
IA generativa (copyright/likeness/deepfakes/NO FAKES/Colombia) · 40 voz en tiempo real (STT/TTS streaming/voice agents).
**Integraciones & sistemas (ola 2):** 41 WhatsApp Cloud API a fondo (templates/media/24h/Flows/pricing) · 42 pagos
LatAm (Stripe/Wompi/MercadoPago/PSE/Nequi/Pix/COD) · 43 search (Postgres FTS vs Meili/Typesense/ES + hybrid) · 44
realtime (SSE/WebSocket/WebRTC + backplane Redis) · 45 Kubernetes a fondo (GPU Operator/KEDA/cuándo NO usarlo).
**🎨 DIRECCIÓN CREATIVA — crear imágenes/videos/animaciones (ola 3):** 46 dirección de arte de imágenes IA
(composición/luz/óptica/film-stock, anti-AI-slop) · 47 dirección cinematográfica de video (shot types/camera moves/
Veo/Kling/Runway/Higgsfield) · 48 animación con IA (motion brush/avatares/loops/cinemagraphs) · 49 consistencia de
personaje y marca (sref/cref/LoRA/IP-Adapter/Kontext) · 50 storyboard & planificación de shots · 51 transiciones y
montaje (J/L cuts/match cut/xfade/Rule of Six) · 52 color grading & look cinematográfico (Resolve/scopes/grano/
halación) · 53 motion graphics & tipografía cinética (captions/Remotion/drawtext) · 54 música/SFX/sonido (ducking/
LUFS/Suno) · 55 pipeline de producción de video IA end-to-end (idea→export, ejemplo reel 30s).
**IA avanzada & producto (ola 4):** 56 RAG agéntico/GraphRAG (Self/CRAG, contextual retrieval, LazyGraphRAG) · 57
fine-tune de modelo propio (avatar/video-LoRA/distillation/GRPO) · 58 observabilidad de LLM/LLMOps (Langfuse/OTel/
evals/cost) · 59 3D generativo (Gaussian splatting/TRELLIS/Hunyuan3D/image-to-3D) · 60 edición de imagen avanzada
(FLUX Kontext/inpaint/BiRefNet/IC-Light relight/compositing) · 61 voice agents & telephony (Vapi/Pipecat/Twilio/
μ-law/latencia) · 62 analytics & tracking (PostHog/funnels/A-B/feature-flags/Habeas-Data) · 63 multi-tenancy &
billing SaaS (RLS/Stripe meters/créditos/quotas) · 64 data pipelines/MLOps datos (Dagster/dbt/medallion/ELT) · 65
automation/n8n (webhooks/firma-HMAC/AI-workflows/cuándo-graduar-a-código).
**Frontend & plataforma (ola 5):** 66 agentes avanzados/computer-use (MCP a fondo, browser/computer automation) ·
67 email transaccional/deliverability (SPF/DKIM/DMARC/Resend/Postmark) · 68 SEO técnico/GEO (CWV/schema/llms.txt
realidad) · 69 i18n/l10n (next-intl/ICU/Intl/es-LatAm/RTL) · 70 accesibilidad a11y/WCAG 2.2 (POUR/ARIA/EAA-2025) ·
71 mobile RN/Expo (SDK54/New-Arch/EAS/push) · 72 búsqueda semántica/embeddings (Qwen3/MRL/HNSW/hybrid/pgvector) ·
73 edge computing/WASM (CF Workers/DO/wasmtime/transformers.js) · 74 seguridad ofensiva/pentesting autorizado
(OWASP WSTG/Burp/nuclei/LLM red-team) · 75 WebGL/Three.js/shaders/creative-coding (R3F/TSL/WebGPU/splats web).
**🎬 Cine, comerciales & producto (ola 6):** 76 VFX/efectos visuales (comp pipeline, keying/roto, Runway-Aleph,
Autodesk-Flow, sims) · 77 comerciales/spots (brief, Big-Idea, AIDA/PAS/StoryBrand, estructuras 6/15/30/60s, DR-vs-
brand, performance-creative) · 78 cine/lenguaje cinematográfico (mise-en-scène, lentes/anamórfico, aspect-ratios,
iluminación de género, DPs) · 79 consistencia de campaña/brand-world (look-bible, style-frames, --sref/style-LoRA,
multi-formato, governance) · 80 visualización/fotografía de producto (packshot/hero, specular control, pipeline
BiRefNet→Kontext→IC-Light, specs Amazon, contact-shadow).
**🔥 ESTADO DEL ARTE jun-2026 (ola 7, snapshot fechado, re-verificar):** 81 modelos imagen SOTA (GPT-Image-2/Nano-
Banana-Pro/FLUX.2/Z-Image) · 82 modelos video SOTA (Veo-3.1/Kling-3/Sora-2/Wan-2.7/LTX-2.3) · 83 LLMs frontier
(Opus-4.8/GPT-5.5/Gemini-3.1/DeepSeek-V4) · 84 avatares SOTA (OmniHuman-1.5/Hedra-C3/HeyGen) · 85 audio SOTA (Suno-V5/
ElevenLabs-Music/Chatterbox).
**Web/frontend moderno 2026 (ola 7):** 86 realtime/CRDT (Yjs/Liveblocks) · 87 state-mgmt (Zustand+TanStack-Query) ·
88 design-systems/tokens (DTCG/shadcn-registry) · 89 web-perf (INP/RSC/CrUX) · 90 PWA/offline (Workbox/Dexie).
**Stack 2026 (ola 7):** 91 Next.js-16/React-19 (Cache-Components/PPR) · 92 frameworks (Astro/Svelte5/RR7/Qwik) · 93
TypeScript-7/tsgo · 94 Tailwind-v4/CSS-OKLCH · 95 tooling (Vite8-Rolldown/Bun/Biome).
**Backend/AI-stack 2026 (ola 7):** 96 DBs serverless (Neon/Supabase/Drizzle-vs-Prisma-7) · 97 backend (Hono/Elysia/
tRPC) · 98 AI-frameworks (AI-SDK-v6/Mastra/LangGraph) · 99 generative-UI/streaming · 100 durable-execution (Inngest/Temporal).
**Negocio/growth 2026 (ola 7):** 101 growth/marketing (loops/CRO/LTV-CAC) · 102 pricing (usage-based/AI-margin/
LatAm-COP) · 103 launch-playbook (waitlist/PH/distribution) · 104 comunidad/retención (aha-moment/Skool) · 105
marketing-con-IA (n8n+LLM/governance).
**IA emergente jun-2026 (ola 7):** 106 robótica/embodied (VLA/π0/Figure/Optimus) · 107 world-models (Genie-3/Marble/
Cosmos-3) · 108 IA-local (Ollama-MLX/Qwen3.6/Apple-FM) · 109 hardware (Blackwell/RTX-5090/Groq) · 110 estado-del-arte-IA (agentes/costo-collapse/EU-AI-Act).
**🏭 PRODUCCIÓN REAL — avatar segmentado en RunPod (ola 8, la sesión que originó este skill, núcleo on-scope):**
111 LongCat-Avatar en RunPod, playbook end-to-end (arquitectura/input verificado/5-errores-caros/costo real) ·
112 execution-timeout & economía del cold start (el fallo a **20m8s**, sizing del timeout, los renders fallidos
SÍ cobran) · 113 **Network Volume** para modelos grandes (matar la re-descarga de 44GB → ~35% menos costo +
más rápido) · 114 video segmentado/largo (`num_segments`: 93-frames/3.72s+3.2s/solape-13/cap, normalizar audio
16kHz) · 115 render largo asíncrono + **poller durable de servidor** (el video no se pierde aunque cierres el
navegador) · 116 voz-clon en producción (retención 7-días de MiniMax/re-clonado resiliente/noise_reduction sin
ffmpeg) · 117 control de cámara/movimiento del avatar **por prompt** (estático/no-zoom, sin negative-prompt,
límite 125-chars) · 118 checklist pre-lanzamiento de render GPU (para no quemar dinero en fallos evitables).
**🛠️ PROFUNDIDAD TÉCNICA — self-hosting de IA visual (ola 9, verificado jun-2026):**
*Avatares & talking-head:* 119 comparativa avatares self-hosted (LongCat/OmniHuman/Hallo3/EMO2/Sonic/MultiTalk/
MuseTalk/SadTalker, VRAM/licencia/fit) · 120 LivePortrait/expression-transfer (Act-One/X-Portrait, retargeting) ·
121 pose/landmarks/audio-encoders para avatar (DWPose/wav2vec2-vs-Whisper/InsightFace, sync).
*Modelos de video:* 122 Wan self-hosting a fondo (T2V/I2V/VACE, 1.3B-vs-14B, fp8) · 123 Hunyuan-Video + FramePack
(video largo en VRAM baja ~6GB) · 124 LTX-Video (DiT rápido casi-realtime).
*Inferencia/optimización:* 125 Diffusers offloading/memoria (model/sequential/group offload, VAE-tiling) · 126
attention backends (FA2/FA3/xformers/SDPA/Sage, ABI — el debug real de LongCat) · 127 torch.compile + TensorRT
para difusión (fp8 Hopper/Ada, warmup).
*Cuantización/memoria/arranque:* 128 cuantización de difusión (fp8/SVDQuant-Nunchaku/GGUF-video/torchao) · 129
VRAM mid-run/OOM hands-on (expandable_segments, picos de VAE) · 130 cold-start optimización profundo (mmap/lazy/snapshot).
*Plataformas GPU:* 131 RunPod a fondo (serverless/pods/flex-active/regiones/volúmenes/billing real) · 132 comparativa
plataformas (RunPod/Modal/Replicate/Fal/Beam/Baseten) · 133 Cog/Replicate packaging.
*Audio self-hosting:* 134 Whisper/faster-whisper/WhisperX (alineación/diarización/word-timestamps) · 135 RVC/voice-
conversion (so-vits/Seed-VC, VC-vs-TTS-clone) · 136 music/SFX gen (MusicGen/Stable-Audio/ACE-Step, licencias).
*Visión utilitaria:* 137 matting/bg-removal a escala (BiRefNet/RMBG-2/SAM/RVM) · 138 upscaling/restauración video a
escala (Real-ESRGAN/SUPIR/SeedVR2, tiling) · 139 ControlNet/IP-Adapter/InstantID serving (consistencia).
*Sistemas/ops de jobs GPU:* 140 streaming de progreso de difusión al cliente (RunPod-stream/SSE/callback_on_step_end) ·
141 webhooks HMAC + idempotencia + DLQ · 142 ffmpeg para avatar/video a fondo (concat segmentos/mux/faststart/NVENC).
**🧱 PROFUNDIDAD II — serving, training, infra y ops (ola 10, verificado jun-2026):**
*Serving frameworks:* 143 ComfyUI custom-nodes + API en producción · 144 Triton Inference Server para difusión
(ensembles/dynamic-batching) · 145 batch/dynamic-batching de difusión (CFG-2×, latencia vs throughput).
*Lip-sync & avatar a fondo:* 146 lip-sync puro (Wav2Lip/MuseTalk-realtime/LatentSync, +restaurador) · 147 avatar
realtime/streaming (STT→LLM→TTS→lip-sync, presupuesto de latencia, WebRTC) · 148 face-restoration del output (GFPGAN
vs CodeFormer — ojo licencia no-comercial).
*Generación imagen/video:* 149 FLUX serving a fondo (dev-non-commercial/schnell/Kontext/fp8/LoRA-stack) · 150 SDXL/
SD3.5 serving optimizado (turbo/LCM/compile) · 151 AnimateDiff + SVD image-to-video.
*Training propio:* 152 LoRA-training de avatar/personaje (dataset→serving) · 153 dataset curation/captioning (JoyCaption/
Florence-2/Qwen-VL) · 154 distillation/aceleración (LCM/Turbo/DMD/Hyper-SD — el `--use_distill` de LongCat).
*Build & entorno:* 155 Docker para ML a fondo (CUDA base/multi-stage/cache) · 156 GHCR + GitHub Actions para workers
GPU (cache/sha-vs-latest/smoke-test) · 157 uv + entornos CUDA reproducibles (lockfiles/índices cu12x).
*Scaling & SRE:* 158 autoscaling de inferencia GPU (scale-to-zero/KEDA/queue-depth) · 159 monitoreo/SLO de servicio
GPU (DCGM/cost-per-job/error-budget) · 160 disaster-recovery + cascada de fallback (self-hosted→API premium).
*Sistemas & datos:* 161 colas de jobs GPU a fondo (BullMQ/Celery/prioridad/DLQ) · 162 storage/CDN para media generada
(R2/S3/signed-URLs/lifecycle) · 163 gestión de pesos de modelos (HF Hub/gated/auth/resiliencia de descarga).
*Calidad, safety & test:* 164 evals de calidad avatar/video (LSE-C/D/SyncNet/ArcFace/VBench) · 165 moderación/safety
del output (NSFW/deepfake/likeness/EU-AI-Act Art.50) · 166 testing del worker GPU local + CI sin GPU.
**🌐 COBERTURA TOTAL — 100 refs de profundidad (ola 11, verificado jun-2026):**
*3D generativo:* 167 image-to-3D (TRELLIS/Hunyuan3D) · 168 Gaussian-splatting serving · 169 NeRF · 170 texturas/PBR ·
171 mesh processing. *Cara/identidad (ojo likeness):* 172 face-swap (InsightFace no-comercial) · 173 PuLID/InstantID ·
174 IP-Adapter face · 175 face-enhance · 176 expression/gaze edit. *Relight/compositing:* 177 IC-Light (V2 non-commercial) ·
178 harmonization · 179 shadow-gen · 180 bg-replacement pipeline · 181 HDR/tone-mapping. *Edición imagen:* 182 inpaint/
outpaint · 183 FLUX-Kontext deep · 184 OmniGen unified · 185 instruct-edit · 186 object removal. *Profundidad/geometría:*
187 depth (DepthAnything/Marigold) · 188 normal/segmentation · 189 optical-flow (RAFT) · 190 tracking (CoTracker/SAM2) ·
191 pose full-body. *Try-on/producto:* 192 virtual try-on (IDM-VTON) · 193 product-photography pipeline · 194 packshot/
ghost-mannequin · 195 texto-en-imagen · 196 QR-art. *Video control:* 197 camera-control · 198 VACE deep · 199 keyframe/
FLF2V · 200 video-extension/loop · 201 video-inpaint. *Video avanzado:* 202 full-body talking avatar (OmniAvatar) · 203
motion/dance-gen · 204 video restyle/relight · 205 audio-reactive video · 206 video super-res temporal. *Motores TTS:* 207
F5-TTS · 208 Kokoro/MeloTTS · 209 XTTS/Coqui · 210 CosyVoice/Fish-Speech · 211 Chatterbox. *Voz avanzada:* 212 emotion/
style TTS · 213 streaming TTS · 214 singing-voice · 215 dubbing/translation · 216 voice-design. *Audio proc:* 217 source-
separation (Demucs/UVR) · 218 denoise/enhance (DeepFilterNet) · 219 audio super-res · 220 forced-alignment/VAD · 221 audio-
watermarking (AudioSeal). *LLM/VLM serving:* 222 vLLM multimodal · 223 SGLang/LMDeploy · 224 TensorRT-LLM VLM · 225 VLM
caption/moderación · 226 structured-output sobre imagen. *Sistemas GPU:* 227 CUDA-graphs · 228 MIG · 229 MPS/time-slicing ·
230 spot/preemptible · 231 checkpoint/resume. *Distribuido:* 232 NCCL tuning · 233 FSDP/DeepSpeed difusión · 234 context/
sequence-parallel video · 235 Ray · 236 gang/topology scheduling. *Training avanzado:* 237 DreamBooth/full-FT · 238
Diffusion-DPO/reward · 239 ControlNet-training · 240 IP-Adapter-training · 241 webdataset/data-loading. *MLOps:* 242
orquestación (Dagster/Flyte) · 243 KServe/BentoML/Ray-Serve · 244 experiment-tracking · 245 data/model-versioning (DVC→
lakeFS) · 246 canary/shadow/blue-green. *Seguridad:* 247 supply-chain (pickle/safetensors) · 248 container/GPU isolation +
SSRF · 249 adversarial/jailbreak · 250 privacidad/biometría · 251 audit-logging. *Costo/bench:* 252 GPU-benchmarking · 253
spot/reserved/arbitraje · 254 cost-allocation/chargeback · 255 TCO self-host-vs-API · 256 throughput checklist. *Edge/on-
device:* 257 CoreML/MLX · 258 ONNX/TFLite móvil · 259 WebGPU/transformers.js · 260 quant/distill edge · 261 browser-avatar.
*Producto/integración:* 262 créditos/cuotas/billing · 263 asset/gallery mgmt · 264 Discord/Telegram bots · 265 prompt-
enhancement con LLM · 266 C2PA/watermark (EU-AI-Act).
**🚀 FULL-STACK DE PRODUCTO — construir y vender apps de IA (ola 12, verificado jun-2026):**
*Copy & contenido:* 267 copywriting persuasivo (AIDA/PAS) · 268 content/SEO-writing · 269 storytelling de marca · 270
email/newsletter copy · 271 social copy/hooks. *Seguridad web:* 272 frontend (CSP/XSS/CSRF/CORS) · 273 auth (OAuth2.1/
passkeys) · 274 API-security (rate-limit/keys/WAF) · 275 secrets-management · 276 supply-chain web (npm/SCA). *Frontend
eng:* 277 component-architecture · 278 forms/validación (RHF/Zod) · 279 animaciones (Motion/GSAP) · 280 data-fetching
(TanStack) · 281 testing frontend (Playwright/Vitest). *Backend/API:* 282 REST/OpenAPI · 283 GraphQL · 284 webhooks/
event-APIs · 285 background-jobs web (BullMQ/Inngest) · 286 file-uploads/media. *Bases de datos:* 287 Postgres avanzado
(EXPLAIN/índices) · 288 Redis patterns · 289 vector-DBs (Qdrant/Pinecone) · 290 modelado/migraciones · 291 ORMs (Prisma/
Drizzle). *Auth & pagos LatAm:* 292 auth-providers (Clerk/Auth0) · 293 RBAC/multi-tenant · 294 Stripe a fondo · 295 pagos
LatAm (Wompi/MercadoPago/PSE) · 296 facturación-electrónica (DIAN/SAT). *DevOps:* 297 CI/CD (GH-Actions) · 298 Docker/
Compose web · 299 deploy (Vercel/Render/Fly) · 300 observabilidad web (Sentry/OTel) · 301 IaC (Terraform/Pulumi).
*Cloud/serverless:* 302 functions edge/lambda · 303 Cloudflare (Workers/D1/R2) · 304 CDN/caching · 305 colas cloud · 306
cron/scheduling. *AI app patterns:* 307 RAG en producción · 308 agentes en producción · 309 memoria de agentes · 310
evals de LLM-apps · 311 guardrails. *AI integración:* 312 streaming-UI · 313 function-calling · 314 MCP a fondo · 315 apps
multimodales · 316 cost-control LLM. *Messaging (negocios LatAm):* 317 WhatsApp-Cloud deep · 318 chatbot-UX · 319 Baileys ·
320 Telegram/Discord/IG · 321 inbox omnicanal. *Growth:* 322 SEO-técnico · 323 analytics (PostHog/GA4) · 324 A/B-testing ·
325 CRO/funnels · 326 referral/viral. *Producto/UX:* 327 onboarding/activación · 328 pricing-page · 329 dashboards/data-viz ·
330 design-systems deep · 331 accesibilidad deep. *Mobile:* 332 RN/Expo a fondo · 333 push-notifications · 334 deploy-stores ·
335 offline-sync · 336 native-modules. *SaaS:* 337 métricas (MRR/churn/LTV) · 338 multi-tenancy patterns · 339 billing/cuotas/
créditos · 340 legal/ToS/privacy-LatAm · 341 soporte/helpdesk. *Data eng:* 342 ETL/ELT · 343 warehouse (BigQuery/DuckDB) ·
344 dbt · 345 event-schema · 346 BI/dashboards. *Automatización:* 347 n8n/Make/Zapier · 348 workflow-patterns · 349 scraping ·
350 browser-automation · 351 RPA. *Realtime/colab:* 352 WS/SSE/WebRTC deep · 353 CRDT/Yjs · 354 presence/cursors · 355 live-
updates · 356 calls/LiveKit. *Performance/escala:* 357 Core-Web-Vitals · 358 caching multi-capa · 359 DB-scaling/sharding ·
360 load-testing · 361 rate-limiting. *Fiabilidad/ops:* 362 resilience-patterns · 363 monitoring/on-call · 364 incident/
postmortems · 365 backups/DR · 366 feature-flags/rollout.

> **Cómo crecer:** cada nueva ola añade `references/NN-tema.md` (verificado con research) + una línea aquí.
> Fronteras siguientes: real-time/CRDT (Yjs/Liveblocks), state mgmt avanzado, design systems/tokens, web perf
> profunda, PWA/offline-first, blockchain/web3 (si aplica), game dev, robotics/embodied AI, quantum (futuro), etc.

---

## ⛔ Las 12 reglas de oro (memorízalas — cada una se pagó con horas perdidas)

1. **VERIFICA contra la fuente real ANTES de construir.** Lee el `requirements.txt`, el
   script de inferencia y un JSON de ejemplo del repo oficial. No asumas args, formato
   de input, ni versiones. (Ej: LongCat pinea `torch==2.6.0` exacto → eso decide la GPU.)
2. **NUNCA hornees modelos grandes (>2-3GB) en la imagen Docker.** Reventaba el build de
   RunPod (límite 30 min + `input/output error` al escribir capa gigante). El modelo se
   descarga en **runtime a un Network Volume** (1 vez, lo reusan todos los workers).
3. **La GPU está casada con la versión CUDA/torch de tu imagen.** No es libre. Ver matriz ↓.
4. **OBSERVABILIDAD PRIMERO.** Loguea cada paso (`flush=True`), transmite la salida de
   subprocess EN VIVO a los logs, envuelve el handler en `try/except` con traceback.
   Sin esto, "vuelas a ciegas" y cada iteración cuesta una hora.
5. **No confíes en el auto-build de GitHub de RunPod — está roto/es frágil.** Usa
   **GitHub Actions → GHCR → RunPod descarga la imagen** (patrón ↓). Habilita iteración real.
6. **Investiga lo MÁS NUEVO del mercado, no modelos de hace 2 años.** En IA visual
   open, lo bueno cambia cada mes. Cita papers/repos con fecha.
7. **Verifica compatibilidad ANTES de mandar al usuario a crear cuentas/pagar/buckets.**
   (Storage S3 vs R2, formatos, ACLs, nombres en minúscula, etc.)
8. **En tiempos muertos (builds, deploys), estudia y anticipa.** No esperes ocioso:
   valida el siguiente paso contra el repo real y ten el fix listo.
9. **NO vayas error-por-error: audita el grafo de imports COMPLETO.** Cuando falta un
   módulo, clona el repo y traza todos los imports del script de inferencia. Detecta deps
   que el `requirements.txt` no declara (`triton`, `regex`, `tqdm`) y líneas TÓXICAS que
   rompen pip entero (paquetes que no existen en PyPI, libs de sistema listadas como pip).
   Luego un **smoke-test de imports en el BUILD** (ver §3) atrapa lo que quede.
10. **NUNCA `pip install ... || true`.** Oculta fallos: la imagen compila "verde" y revienta
    en runtime con `ModuleNotFoundError`. Con el resolver moderno de pip, UNA línea inválida
    en el requirements tumba TODO el archivo → no instala NADA. Quita las líneas malas con
    `sed` y deja que pip falle el build si algo falla de verdad.
11. **La RAM del sistema importa TANTO como la VRAM.** Cargar un modelo grande lo INSTANCIA en
    RAM antes de moverlo a la GPU. Un DiT de 13.6B en fp32 = **54GB de RAM** solo para nacer →
    OOM (`SIGKILL -9`, "triggered memory limits") en una GPU con poca RAM. En RunPod la RAM va
    atada a la GPU (A40=50GB, A100=251GB). Calcula RAM ≈ params×4 (fp32) o ×2 (bf16). Ver §6.6.
12. **Lee el CÓDIGO DE CARGA para encontrar TODOS los modelos/archivos que necesita** — no solo
    el repo "principal". Muchos modelos cargan componentes de OTROS repos por rutas relativas
    (`checkpoint_dir/../OtroModelo`, `subfolder="text_encoder"`). Si solo bajas el principal:
    `OSError: Incorrect path_or_model_id`. Grepea los `from_pretrained(...)` y mapea cada ruta. Ver §10.

---

## 1. Matriz GPU ↔ CUDA ↔ torch (junio 2026)

| Arquitectura | GPUs típicas | Compute | CUDA mín | torch wheel | Notas |
|---|---|---|---|---|---|
| **Ampere** | A40, A6000 (48GB), A100 (40/80GB) | sm_80/86 | 11.x–12.x | cu118/cu124/cu126 | El "48 GB" barato de RunPod. Se está volviendo escaso. |
| **Ada** | L4, L40, RTX 4090 | sm_89 | 12.x | cu124+ | |
| **Hopper** | H100, H200 (141GB) | sm_90 | 12.x | cu124+ | Caro pero potente. |
| **Blackwell** | RTX 5090 (32GB), RTX PRO 6000 (96GB), B200 | **sm_120** | **12.8** | **cu128 (torch≥2.7)** | Lo que RunPod empuja en 2026. Las "PRO". |

### Pinning exacto torch ↔ torchvision ↔ torchaudio ↔ índice cu
**Las tres librerías DEBEN ser del mismo par, y el índice cu NO es un superset entre versiones:**

| torch | torchvision | torchaudio | índices cu disponibles |
|---|---|---|---|
| **2.6.0** | 0.21.0 | 2.6.0 | cu118, **cu124**, cu126 — **NO cu128** |
| **2.7.0** | 0.22.0 | 2.7.0 | cu118, cu126, **cu128** — **NO cu124** |
| **2.8.0** | 0.23.0 | 2.8.0 | cu126, cu128, cu129 — **NO cu118/cu124** |

Regla: `torchvision = 0.{torch_minor+15}.0`; `torchaudio = misma versión que torch`. Instala las 3
del MISMO índice: `pip install torch==2.7.0 torchvision==0.22.0 torchaudio==2.7.0 --index-url .../cu128`.
**⚠️ Gotcha:** torch 2.6 NO tiene cu128 (no corre Blackwell); torch 2.7 NO tiene cu124. No asumas que
una URL existe — el set de CUDA cambia cada release.

**Claves:**
- **`torch 2.7.0` fue el PRIMER release estable con soporte nativo Blackwell (sm_120)**,
  con wheels **cu128**. torch 2.6 NO tiene cu128. (PyTorch issue #159207.)
- Una imagen **cu128 corre en TODO** (Ampere+Ada+Hopper+Blackwell) → es la más universal.
  Una imagen cu124 NO corre en Blackwell ("no kernel image is available").
- Error **`no kernel image is available for execution`** = tu torch es demasiado viejo
  para la GPU (ej. cu124 en Blackwell). Sube CUDA/torch.
- Si el modelo pinea `torch==2.6.0` y quieres Blackwell: hay que **forzar torch 2.7+cu128**
  (quitar el pin con `sed` del requirements) — funciona "con ajustes" pero es riesgo.
- **⚠️ torch 2.7.0 ROMPE TODO el ecosistema de atención en cp310** (flash_attn 2.7.4.post1 Y
  xformers 0.0.30 dan el mismo `undefined symbol _ZN3c105Error...__cxx11`; no hay wheel funcional
  de ninguno). **REGLA: NO subas a la última torch porque sí — usa la que el repo pinea y probó,
  salvo que NECESITES una GPU que la obligue.** Y revalúa esa necesidad si cambian las condiciones:
  ej. nos fuimos a Blackwell por "Ampere escaso en la región del Network Volume" → al QUITAR el
  volumen, Ampere volvió a estar disponible → ya no hacía falta Blackwell → volvimos a torch 2.6
  cu124 (combo nativo del repo) y se acabó la guerra de ABI. Una imagen **cu124 corre en
  Ampere/Ada/Hopper** (todo menos Blackwell sm_120) = pool enorme de GPUs sin tocar torch 2.7.

### flash_attn (la trampa #1 de runtime)
- Usa **wheel pre-compilado** que coincida con: python (cp310), torch (torch2.7), CUDA (cu12), ABI.
  Ej: `flash_attn-2.7.4.post1+cu12torch2.7cxx11abiFALSE-cp310-cp310-linux_x86_64.whl`.
  Así NO necesita compilar (sin nvcc, builds rápidos).
- **`undefined symbol: _ZN3c10...` al importar = mismatch de C++ ABI.** Cambia
  `cxx11abiFALSE` ↔ `cxx11abiTRUE` para que coincida con tu wheel de torch.
- **Detecta el ABI de TU torch antes de elegir el wheel** (en vez de adivinar):
  ```python
  import torch
  print(torch.compiled_with_cxx11_abi())   # True -> usa cxx11abiTRUE ; False -> cxx11abiFALSE
  print(torch.__version__, torch.version.cuda)   # para los campos torchX.Y y cu12
  ```
  Decodifica el wheel: `flash_attn-<ver>+cu12torch2.6cxx11abiFALSE-cp310-cp310-linux_x86_64.whl` =
  cuda 12.x · torch 2.6.x · ABI vieja · CPython 3.10. Los 4 (cuda major, torch minor, abi, cp) deben
  coincidir. **2026: torch ≥2.7 suele venir con ABI NUEVA (TRUE)** → el reflejo viejo de usar abiFALSE
  rompe. Verifica con `compiled_with_cxx11_abi()`.
- flash_attn **2.8.x da undefined symbol con torch 2.6**; el **2.7.4.post1 es el combo estable**
  (Dao-AILab/flash-attention #1783). Verifica el ABI del torch oficial que instalas.
- **torch 2.7.0 ROMPIÓ flash_attn 2.7.4.post1**: el wheel da `undefined symbol _ZN3c105Error...`
  porque PyTorch cambió el ABI en 2.7 y ese wheel se compiló contra el viejo. **Cambiar
  FALSE↔TRUE NO basta — no hay wheel funcional** (issues Dao-AILab #1644, #1696, abiertos).
- **⚠️ xformers NO te salva en torch 2.7 cp310:** `xformers==0.0.30` (la única con wheel cp310 para
  cu128) trae su PROPIO `_C_flashattention3.so` que da **el MISMO `undefined symbol _ZN3c105Error...
  __cxx11`** al `import xformers.ops`. O sea: torch 2.7 rompe flash_attn Y xformers en cp310. No
  hay escapatoria fácil por el lado de las librerías de atención.
- **SOLUCIÓN REAL y definitiva: vuelve al torch que el repo pinea.** Si el repo dice `torch==2.6.0`,
  úsalo con cu124 y el flash_attn `cu12torch2.6` (ese SÍ funciona). Pierdes Blackwell, pero cu124
  corre en Ampere/Ada/Hopper (pool enorme). **Pelear con wheels de atención para torch 2.7 = horas
  perdidas; cambiar a torch 2.6 = 1 commit.** (Lección LongCat: gastamos ~2h en flash_attn↔xformers
  ABI antes de simplemente volver a 2.6 cu124, que funcionó al primer intento.)
- Si DE VERDAD necesitas Blackwell (torch 2.7): tus opciones son (a) compilar flash_attn desde
  fuente con nvcc en la imagen (lento, ~30-60min build), o (b) parchear el modelo a SDPA si su
  código lo soporta (`F.scaled_dot_product_attention`, trae FA2 nativa en torch 2.7, sin ABl).
  Ninguna es trivial. Por eso: **NO subas a torch 2.7 salvo necesidad real de Blackwell.**
- El backend de atención suele venir en el `config.json` del modelo (`enable_flashattn2`/
  `enable_xformers`/`enable_bsa`), NO por CLI → si necesitas cambiarlo, **parchéalo en el handler
  tras descargar el modelo** (con `json.load`/`json.dump`).

---

## 2. Modelos grandes → Network Volume (no en la imagen)

**Patrón correcto:**
- **Imagen Docker = solo código + librerías** (~6-8GB) → build rápido, sin reventar.
- **Modelo (~30GB) → se baja en runtime a `/runpod-volume`** (Network Volume persistente),
  UNA vez, con marcador `.download_complete`. Los workers siguientes lo montan al instante.

```python
VOL = '/runpod-volume' if os.path.isdir('/runpod-volume') else '/app/weights'
CKPT = os.path.join(VOL, 'NombreDelModelo')
_DONE = os.path.join(CKPT, '.download_complete')
def ensure_model():
    if os.path.exists(_DONE): return CKPT, None
    try:
        from huggingface_hub import snapshot_download
        os.makedirs(CKPT, exist_ok=True)
        snapshot_download(repo_id='org/model', local_dir=CKPT, max_workers=8)
        open(_DONE, 'w').close()
        return CKPT, None
    except Exception as e:
        return None, str(e)
```

- Activa `HF_HUB_ENABLE_HF_TRANSFER=1` (descarga rápida). Instala `huggingface_hub[hf_transfer]`.
- **El Network Volume FIJA la región del endpoint.** La GPU compatible DEBE existir y estar
  disponible en esa región. (En RunPod, filtra por la GPU al crear el volumen.)
- Costo volumen ≈ **$0.07/GB/mes**. 100GB = ~$7/mes. Optimiza el tamaño cuando funcione
  (descarga solo los pesos que el modelo realmente carga, ej. saltar fp32 si usas int8).
- **NO** dejar el modelo en disco efímero del contenedor (5GB **default**): se llena → falla.
  Pero el **Container disk se puede subir** (ej. 70GB) → entonces SÍ cabe el modelo en efímero.

### TRADEOFF crítico: Network Volume (region-lock) vs disco efímero (re-descarga)
Aprendido a sangre con LongCat: **un solo Network Volume FIJA la región y si la GPU compatible
escasea ahí, el worker NUNCA arranca** (se queda "Initializing", 0 workers, sin logs — horas
perdidas). Dos salidas:
- **Modelo mediano (~20GB) → SIN volumen, Container disk grande (70GB), descarga en cada cold
  start.** Pierdes ~3-6 min de re-descarga por cold start, pero el worker corre en CUALQUIER
  región con GPU libre. **Esto fue lo que destrabó LongCat.** Ideal con `active=0` y uso esporádico.
- **Modelo grande / alto volumen → Network Volume + `active=1` caliente** para no re-streamear.
  Si usas volumen, **adjunta varias regiones** o elige una con stock real de tu GPU.
- Recuerda: un cambio de Container disk (o de dep) **solo aplica a workers NUEVOS** → borra los
  "Outdated" o cambia el SHA de la imagen para forzar recreación.

---

## 3. Despliegue: CI → registry → serverless (NO auto-build de RunPod)

> El auto-build de GitHub en RunPod es frágil: pushes que no disparan build, "Redeploy"
> que rehace el commit viejo, sin opción de reconectar. **No dependas de él.**

**Patrón GHCR + GitHub Actions (iteración fluida):**

`.github/workflows/build.yml` (crear por la **web de GitHub** — un PAT normal no tiene
`workflow` scope para subir archivos en `.github/workflows/`):

```yaml
name: build-and-push-image
on:
  push: { branches: [ main ] }
  workflow_dispatch: {}
jobs:
  build:
    runs-on: ubuntu-latest
    permissions: { contents: read, packages: write }
    steps:
      - name: Liberar disco del runner   # imágenes CUDA son grandes
        run: |
          sudo rm -rf /usr/share/dotnet /opt/ghc /usr/local/lib/android "$AGENT_TOOLSDIRECTORY" /opt/hostedtoolcache /usr/local/.ghcup
          sudo docker system prune -af || true
      - uses: actions/checkout@v4
      - uses: docker/login-action@v3
        with: { registry: ghcr.io, username: ${{ github.actor }}, password: ${{ secrets.GITHUB_TOKEN }} }
      - uses: docker/build-push-action@v6
        with:
          context: .
          push: true
          tags: |
            ghcr.io/<owner-lowercase>/<repo>:latest
            ghcr.io/<owner-lowercase>/<repo>:${{ github.sha }}
```

Pasos:
1. Commit del workflow → Actions construye y publica la imagen (~10-20 min; tiene HORAS
   de límite, a diferencia de los 30 min de RunPod).
2. **Hacer el paquete GHCR PÚBLICO** (repo → Packages → Package settings → Danger Zone →
   Change visibility → Public) para que RunPod lo baje sin credenciales.
3. RunPod: crear endpoint **"Deploy from Docker registry"** (NO GitHub) con imagen
   `ghcr.io/<owner>/<repo>:latest`. Sin registry auth (es público). Sin Start command
   (la imagen ya trae el CMD).
4. **Iterar después:** push → Actions reconstruye → en RunPod **"Redeploy"** re-descarga
   `:latest`. **Cero recreaciones, cero webhook roto.**

> GHCR/imagen Docker requiere todo en minúscula. owner `Lushows` → `lushows`.

### Smoke-test de deps en el BUILD (atrapa fallos sin gastar GPU)
Agrega al final del Dockerfile un paso que importe TODO el grafo de deps. Si falta o falla
una, **revienta el build en Actions (gratis, 5 min)** en vez de fallar en RunPod tras un
cold start de 8 min en GPU pagada:
```dockerfile
RUN python -c "import torch, flash_attn, triton, regex, tqdm, audio_separator, onnxruntime, \
    transformers, diffusers, librosa, scipy, onnx, PIL, torchvision; \
    print('=== SMOKE IMPORT OK ===')"
```
Este test ya pagó: atrapó `flash_attn` ABI y `onnxruntime` executable-stack ANTES de runtime.
**Build verde con smoke-test = todas las deps importan.** Lo único que NO valida es runtime GPU
(VRAM/OOM/kernels JIT) — eso solo se ve corriendo.

### Pins rotos del upstream → arréglalos en el build
- **Paquete que no existe en PyPI** (vendored/typo, ej. `tritonserverclient==0.0.6` → 404):
  quítalo con `sed`. NO confundir con `triton` (compilador de kernels, sí necesario).
- **Lib de sistema listada como pip** (ej. `libsndfile1==0.0.1`): instálala por `apt`, quítala del requirements.
- **Pin viejo con bug de plataforma**: `onnxruntime==1.16.3` trae el `.so` con bandera
  "executable stack" → `ImportError: cannot enable executable stack` en glibc moderno. **Sube
  a `onnxruntime>=1.17`** (release notes 1.17: binarios sin executable stack). NO uses
  `execstack` (removido de Debian moderno).

---

## 4. Observabilidad primero (handler de serverless)

```python
def log(*a): print('[app]', *a, flush=True)   # CMD con python -u

def handler(job):
    try:
        log('volume_mounted=', os.path.isdir('/runpod-volume'))
        log('disco:', shutil.disk_usage(VOL))
        # ... ensure_model(), download inputs ...
        log('lanzando:', ' '.join(cmd))
        p = subprocess.run(cmd, cwd=REPO)   # SIN capture_output -> streamea a logs en vivo
        log('returncode=', p.returncode)
        if p.returncode != 0:
            return {'error': f'fallo (rc {p.returncode}). Ver logs.'}
        # ... upload, return {'output_video_url': url} ...
    except Exception as ex:
        log('EXCEPCION:\n', traceback.format_exc())
        return {'error': 'excepcion: ' + str(ex)}
```

- **`subprocess.run(cmd)` sin `capture_output`** → la salida del proceso hijo (torchrun,
  etc.) se transmite EN VIVO a los logs del serverless. Ahí ves el crash real.
- **`try/except` de tope con `traceback.format_exc()`** → captura cualquier error y lo
  devuelve/loguea en vez de morir en silencio.
- **NUNCA `sys.exit()` en un handler async** → enmascara el error real con cosas como
  "Event loop is closed".
- Diagnóstico de estado: status **FAILED** del job = el worker **crasheó** (proceso muerto:
  OOM de RAM, segfault, import fallido). Si el handler **devuelve** `{'error':...}` el job
  queda **COMPLETED** con ese output. Distinguirlos te dice si es crash vs error controlado.

---

## 5. RunPod serverless — cheatsheet

- **Endpoint tipo Queue** + handler `runpod.serverless.start({'handler': handler})`.
- **GPU**: marca varias compatibles por prioridad (cheapest-first). RunPod usa la 1ª libre.
  "Unavailable" suele ser TEMPORAL (pico de demanda) → se recupera. Las "PRO" = Blackwell.
- **Execution timeout**: súbelo (ej. 1200s) para modelos lentos / cold start + descarga.
  Es un TECHO de seguridad, solo pagas el tiempo real.
- **Idle timeout** 5s + **Active workers 0** = escala a cero → no pagas en reposo.
- **FlashBoot ON** = cold starts más rápidos tras el primero.
- **Network Volume** (Advanced) montado en `/runpod-volume`; fija la región.
- **Logs vacíos pero "job in progress"** = worker arrancando (pull de imagen) o descarga
  silenciosa → no es error, espera. Logs aparecen cuando el contenedor corre.
- **Workers tab**: estado real (initializing/running/throttled). Workers "Outdated" en
  regiones ajenas = sobras, RunPod las limpia.
- **Costo** ≈ $/s × segundos reales. Ej: RTX 5090 ~$0.00044/s → ~$0.10-0.18/video.

---

## 6. Modelos visual open 2026 (punto de partida — RE-INVESTIGAR siempre)

> Verifica el estado del arte con búsqueda fresca; esto cambia mensualmente.

- **Avatares parlantes (foto+audio→video con gestos):** LongCat-Video-Avatar 1.5
  (Meituan, 13.6B, ~48GB / 32GB con int8, gestos+lip-sync, #1 calidad EvalTalker),
  EchoMimicV2/V3 (medio cuerpo, más liviano), Wan2.2-S2V, HunyuanVideo-Avatar, InfiniteTalk.
- **Lip-sync sobre video base:** MuseTalk. **Cabeza simple (peor):** SadTalker (2024, evitar).
- **TTS / clonación de voz:** F5-TTS (en/zh), MiniMax (multilingüe, clone+TTS con voice_id
  cacheado), ElevenLabs (mejor narrador, de pago).
- **APIs premium (cero deploy, $/video alto):** Kling AI Avatar, OmniHuman (vía fal).
  Útil como **red de seguridad** si el self-host se atasca y hay urgencia.

---

## 6.5 Rendimiento y costo — palancas de inferencia (diffusion video/avatar)

> Verificado contra el código real de LongCat-Avatar 1.5 + research 2026. Aplica a DiTs de video en general.

### Las palancas que mueven costo (de mayor a menor impacto)
1. **`num_inference_steps`** — lineal en pasos del DiT. **La palanca #1.** 50→8 ≈ 6× más barato.
2. **`use_distill`** — activa el camino destilado. En LongCat-Avatar-1.5 fuerza:
   `num_inference_steps=8`, `text_guidance_scale=1.0`, `audio_guidance_scale=1.0` (vs 50 y 4.0).
   La destilación es el mayor ahorro: ~6× menos forward passes a calidad casi igual. **Úsalo siempre que el modelo lo ofrezca.**
3. **Resolución** — costo ∝ píxeles. LongCat: **480p = 480×832**, **720p = 768×1280** (~2.25× más cómputo y VRAM).
4. **`num_segments` / largo del clip** — lineal en frames. LongCat v1.5: **93 frames/segmento @ 25fps ≈ 3.7s**; segmentos extra reusan los últimos 13 frames como condición. Un clip de 1 min = varios segmentos = varios × el costo.
5. **`use_int8` / FP8** — hace caber el modelo en una GPU más barata (menor $/s) y acelera atención; costo de calidad modesto.
6. **CFG (guidance scales)** — cada paso con CFG = 2 forward passes. Los destilados suelen bajarlo a 1.0 (sin CFG). Bájalo donde el modelo lo permita.

### Cuantización (cuando no cabe en VRAM)
- **FP8 > INT8** a igual bits (el float degrada menos que el entero). **FP8 requiere Ada sm_89+**; en Ampere solo INT8.
- Libs: **torchao** (mejor para diffusion, compone con `torch.compile`, FP8/INT8) · **bitsandbytes** (fácil, corre en Ampere) · **optimum-quanto** (portable). Nativo en Diffusers existe pero básico.
- LongCat trae su `load_quantized_dit` (torch+safetensors puro, sin libs externas).

### Atención por arquitectura (rankeado por velocidad)
| Arch | Mejor backend | Notas |
|---|---|---|
| **Ampere** (A40/A6000, sm_80/86) | FlashAttention-2 / xformers; **SageAttention (INT8) ~2× FA2** | FA-3 NO corre aquí |
| **Hopper** (H100/H200, sm_90) | **FlashAttention-3** (1.5–2× FA2) | FA-3 es Hopper-only |
| **Blackwell** (5090/PRO 6000, sm_120) | **SageAttention 2/3**; SA3 (FP4) ~5× FA | FA-3 NO corre aquí |
| Fallback universal | **SDPA** (`F.scaled_dot_product_attention`) | Sin dolor de ABI, más lento |

### VRAM aprox (DiT video ~14B, pesos INT8)
- Pesos int8 ~14-16GB. **480p clip corto ≈ 22-28GB total** → cabe cómodo en **48GB (A40/A6000)**.
- **720p / más frames ≈ 35-45GB+** → 48GB al límite, mejor 80GB o offload. **Frames y resolución mueven la VRAM más que los pesos.**

### Modelo de costo ($/video)
`$/gen = $/s × (cold_start_s + inference_s)`. La GPU rápida solo gana en $/job cuando su
**ratio de velocidad supera su ratio de precio**. Ej: clip 720p ~90s en A40 ($0.00034/s) ≈
**$0.031**; mismo job 35s en H100 ($0.00116/s) ≈ **$0.041** → la A40 (más lenta) gana. Para
jobs diarios/batch, el tier **48GB Ampere/Ada es el piso de costo**. La rápida gana con
destilación/FP8/FA3 que le den ventaja super-lineal, o cuando la latencia vale.

### Estrategia de carga del modelo por tamaño (impacto en cold-start)
| Tamaño | Estrategia |
|---|---|
| **<5GB** | Hornear en la imagen (build rápido, sin red en runtime) |
| **5-20GB** | Hornear si CI/disco lo permite, o cache de modelo de RunPod |
| **20-50GB** (LongCat ~30GB on-disk) | **Network Volume + `snapshot_download` 1 vez** con marcador `.download_complete`. NO hornear (revienta build) |
| **>50GB** | Network Volume + **1 active worker caliente** para no re-streamear pesos en cada cold start |

**FlashBoot** cachea el estado del worker en el host físico → cold starts ~250-500ms al volver,
PERO es estadístico: si el tráfico te mueve de host, pagas cold start completo. `active=0` para
tráfico esporádico/dev; `active=1` solo si la latencia o re-streamear un modelo >50GB es inaceptable.

### Presets recomendados
| Knob | "Clip diario barato (presentador)" | "Premium" |
|---|---|---|
| Resolución | **480p** | 720p |
| `use_distill` | **on (8 pasos)** | on, o 12-25 pasos |
| Cuant | **int8** en A40 48GB | bf16/FP8 en H100/H200 |
| Atención | Sage/FA2 (Ampere) | FA3 (Hopper) / SA3 (Blackwell) |
| Worker | flex, active=0 | active=1 (sin cold start) |
| GPU | **A40 48GB ($0.00034/s)** → ~$0.10-0.18/video | H100/H200 |

---

## 6.6 RAM del sistema: el OOM que nadie ve venir

> Todos miran la VRAM y se olvidan de la RAM. Un modelo grande **te mata por RAM antes de tocar la GPU.**

- **El modelo se INSTANCIA en RAM antes de ir a la GPU.** `Model(**config)` aloca todos los params
  en CPU (fp32 por default) → un DiT de **13.6B en fp32 = 54GB de RAM**. Luego se castea a bf16 o
  se mueve a GPU, pero el PICO ya pasó. Súmale text_encoder (UMT5-XXL ~11GB bf16), whisper (~3GB),
  overhead de torch/python (~5GB). Pico fácil de **45-55GB**.
- **Síntoma:** `unhealthy container: triggered memory limits (OOM)` + `Signal 9 (SIGKILL)` +
  `exitcode -9`. El job queda FAILED. NO es VRAM (la GPU ni se usó), es RAM del sistema.
- **En RunPod la RAM va ATADA a la GPU**, no se elige aparte:
  | GPU | VRAM | RAM aprox |
  |---|---|---|
  | A40 / A6000 | 48GB | **~50GB** ← se queda corto con DiTs 13B+ |
  | L40 / L40S | 48GB | ~62-94GB |
  | A100 80GB | 80GB | **~250GB** |
  | H100 80GB | 80GB | ~250GB |
- **Regla rápida:** RAM necesaria ≈ (params × 4 bytes si instancia en fp32) + encoders + ~10GB.
  Para 13.6B → ~64GB+ → necesitas **≥80GB de RAM = tier A100/H100** (o L40S si justo).
- **Fixes (de más rápido a más barato):**
  1. **GPU con más RAM** (A100/H100 = ~250GB). Config-only, sin rebuild. Funciona seguro pero +caro.
  2. **Cargar en la precisión correcta + sin doble copia** (patch, mantiene la GPU barata):
     - `from_pretrained(..., dtype="auto")` (antes `torch_dtype`) → carga en la precisión del
       checkpoint (bf16) en vez de fp32 → **la mitad de RAM**. (transformers viejo forzaba fp32 = 2×.)
     - `from_pretrained(..., device_map="auto")` → activa Big Model Inference de Accelerate: arma el
       esqueleto en **meta device** (sin alocar) y materializa los pesos DIRECTO a la GPU →
       **pico de CPU-RAM ≈ tamaño del modelo, sin la doble copia** (random-init + pesos).
     - `low_cpu_mem_usage=True` (default cuando hay `device_map`) → carga shard por shard.
     - Para un modelo construido a mano (DiT con `Model(**config)`): `torch.set_default_dtype(torch.bfloat16)`
       antes de instanciar, o construir bajo `with torch.device('meta'):` y cargar el state_dict con
       `assign=True`. Reduce el pico ~½ → cabe en A40 (50GB).
- **Verifica la RAM del worker en los logs** (`9 vCPUs · 50 GB RAM`) para saber tu techo.

---

## 6.7 Modelos multi-repo + sizing de disco PRECISO

### Dependencias ocultas entre repos
Muchos modelos NO son autocontenidos: cargan sub-componentes de OTRO repo de HuggingFace por
ruta relativa. **LongCat-Avatar-1.5** carga el tokenizer + text_encoder (UMT5) + vae del repo
BASE `LongCat-Video` vía `os.path.join(checkpoint_dir, '..', 'LongCat-Video')`:
```python
UMT5EncoderModel.from_pretrained(checkpoint_dir/'../LongCat-Video', subfolder="text_encoder", torch_dtype=torch.bfloat16)
AutoencoderKLWan.from_pretrained(checkpoint_dir/'../LongCat-Video', subfolder="vae", torch_dtype=torch.bfloat16)
```
- **Síntoma si falta:** `OSError: Incorrect path_or_model_id: '.../LongCat-Video'` o `HFValidationError`.
- **Cómo encontrarlo:** grepea TODOS los `from_pretrained(` del script de inferencia ANTES de
  desplegar. Cada uno apunta a una ruta → mapea qué repos/carpetas necesitas en disco.
- **Descarga solo lo necesario** del repo base con `allow_patterns` (ej. `tokenizer/*`,
  `text_encoder/*`, `vae/*`) → salta el DiT base que no usas (puede pesar 60GB+).
- **Ubícalos donde el código los busca:** si carga `checkpoint_dir/../X`, baja X como **carpeta
  hermana** del checkpoint (`VOL/X`), no dentro.

### Sizing de disco — cuéntalo, no lo adivines
Lee los tamaños reales en HuggingFace (pestaña Files, o el árbol) y suma TODO:
```
disco_necesario = imagen_docker + Σ(cada modelo que cargas) + staging_descarga + margen
```
Ejemplo LongCat verificado: imagen ~18GB + avatar int8 21GB (quantized 15.9 + whisper 3 + lora 2.35)
+ base 23GB (text_encoder UMT5 **22.7GB** + vae 0.5) + staging ~15GB = **~82GB** → Container disk 100GB.
- **El `text_encoder` UMT5-XXL pesa 22.7GB** — la sorpresa que nadie estima. SIEMPRE verifica el
  tamaño de los encoders, no solo del DiT.
- `snapshot_download(local_dir=...)` baja a `.cache/huggingface/download/` y luego mueve → suma
  ~el tamaño del archivo más grande como staging transitorio.
- Si `No space left on device`: NO es bug, es que sumaste mal. Recuenta y sube el Container disk.

---

## 6.8 Video segmentado: el clip sale corto

> Los modelos de video generan en CHUNKS de N frames. El default suele ser 1 chunk = clip corto.

- **LongCat v1.5:** 93 frames/segmento @ 25fps. 1er segmento = 3.72s; cada extra suma
  `(93-13)/25 = 3.2s` (reusa 13 frames de solape como condición). `--num_segments=1` por default
  → **el video sale ~3.7s aunque tu audio dure 13s.**
- **Duración total** = `93/fps + (num_segments-1)*(93-13)/fps`. Para cubrir D segundos:
  `num_segments = ceil((D - 3.72)/3.2) + 1`. Calcúlalo en el handler desde la duración del audio
  (`librosa.load`) y pásalo por CLI. Pon un **tope** (ej. 16) para no pasar el execution timeout.
- **Output multi-segmento:** verifica cómo guarda. LongCat NO concatena: guarda `ai2v_demo_1.mp4`
  (1er seg) y re-guarda `video_continue_{N}.mp4` en cada iteración con el acumulado. **El último
  `video_continue_{num_segments}.mp4` YA es el video completo** (acumula sin duplicar solape y
  recorta el audio a la longitud) → un glob "el .mp4 más nuevo" lo agarra. NO concatenes a mano
  (los archivos por-segmento ya traen audio muxeado y son acumulativos → concatenar = audio repetido).
- **Costo:** cada segmento es una generación SEPARADA → 1 min de video = ~16-19 segmentos = 16-19×
  el costo/tiempo de un segmento. Esto es inherente; bájalo con clips más cortos, no con params.

---

## 6.9 La cascada de capas (metodología de debug)

Auto-hospedar un modelo grande falla en CAPAS, y se resuelven EN ORDEN — cada fix destapa la
siguiente. La cascada real de LongCat (cada una costó tiempo; tenerla evita perderlo):

```
1. Worker no arranca        → region-lock del Network Volume (GPU escasa en esa región)
2. No space left on device  → modelo a disco efímero pequeño → subir Container disk / volumen
3. ModuleNotFoundError       → deps faltantes/tóxicas en requirements → auditar imports + smoke-test
4. ImportError onnxruntime   → pin viejo con executable-stack → subir versión
5. undefined symbol (flash)  → ABI torch↔flash_attn/xformers → volver al torch del repo
6. no kernel image           → torch/CUDA no soporta la arch de la GPU → alinear cu/arch
7. Incorrect path_or_model_id→ modelo carga sub-modelos de OTRO repo → bajar el repo hermano
8. SIGKILL / OOM (RAM)        → instanciación del modelo excede RAM → GPU con más RAM o bf16
9. video corto / params      → num_segments/resolución/steps → ajustar al output deseado
10. runtime GPU (VRAM/kernels)→ lo único no verificable sin correr
```
**Disciplina:** ANTES de cada capa, lee el repo real (requirements, script de inferencia, código
de carga, tamaños en HF). El smoke-test en build (§3) colapsa las capas 3-5 en un build gratis de
5 min. La observabilidad (§4) hace que cada capa se diagnostique en 1 minuto, no en 1 hora.

---

## 6.10 Formatos de modelo, dtypes y tamaños (la base del sizing)

> Saber cuánto pesa y en qué precisión carga un modelo es lo que predice RAM, VRAM y disco.

- **Formatos de peso:** `.safetensors` (preferido, seguro, mmap rápido) · `.bin`/`.pth` (pickle, evitar
  si hay safetensors) · sharded = `model-00001-of-0000N.safetensors` + un `*.index.json` que mapea
  tensores→shard. `from_pretrained` lee el index y junta los shards.
- **Tamaño por precisión** (params P): fp32 = **4·P bytes** · fp16/bf16 = **2·P** · int8 = **1·P** ·
  fp4/int4 = **0.5·P**. Ej: 13.6B → fp32 54GB, bf16 27GB, int8 14GB. **Esto decide RAM (al instanciar)
  y VRAM (al correr).** El disco es el del archivo en el repo (suele ser bf16 o int8 ya).
- **Qué dtype carga `from_pretrained`:** lee `dtype` del `config.json`; si no está, usa el dtype del
  primer peso del checkpoint. transformers VIEJO forzaba fp32 (doblaba memoria de un checkpoint bf16).
  **Pasa `dtype="auto"` (o explícito) para no duplicar.** (El param se llama `dtype`; `torch_dtype` es
  legacy pero sigue aceptado.)
- **Cuantización:** int8/fp8 se guarda con un `quantization_config.json` + pesos `quantized_model-*`.
  Cargarlo NO requiere instanciar fp32 si el loader usa meta device (ver §6.6). FP8 solo Ada sm_89+.
- **Componentes típicos de un DiT de video** (y de dónde salen): `vae` (encode/decode latentes, ~0.5GB),
  `text_encoder` (UMT5/T5, **el sorpresa: 5-23GB**), `tokenizer` (KB), `scheduler` (config), `dit`/
  `transformer` (el grande), `audio_encoder` (whisper/wav2vec, ~3GB para avatares). Mapea cada uno a
  su repo/carpeta (§6.7) y a su tamaño (§6.10) ANTES de fijar disco/RAM/GPU.

---

## 6.11 Descarga de HuggingFace (snapshot_download a fondo)

```python
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id='org/model',
    local_dir=CKPT,
    revision='v1.5',                 # tag/branch/commit -> descarga REPRODUCIBLE e inmutable
    allow_patterns=['vae/*', 'text_encoder/*', 'tokenizer/*'],   # solo lo que cargas
    ignore_patterns=['*.bin', '*fp32*', '*.mp4'],                # salta lo que no
    max_workers=8,
    token=os.getenv('HF_TOKEN'),     # requerido para repos GATED/privados (o token=True)
)
```
- **Patterns = `fnmatch`, donde `*` SÍ cruza `/`** → `text_encoder/*` agarra anidados, NO necesitas `**`.
- **`revision=`** fija commit/tag → builds reproducibles (no te cambia el modelo bajo los pies).
- **Gated/privado:** `token="hf_..."` o env **`HF_TOKEN`** (o `HUGGING_FACE_HUB_TOKEN`).
- **`HF_HUB_ENABLE_HF_TRANSFER=1`** requiere `pip install hf_transfer`; paraleliza archivos grandes
  (~2× en links rápidos) PERO sin barra de progreso, sin resume, sin proxy. **2026:** el Hub migró a
  backend **Xet**; el análogo nuevo es `HF_XET_HIGH_PERFORMANCE=1`.
- **Resume:** `snapshot_download` reanuda descargas parciales por archivo (vía cache). (hf_transfer NO.)
- Marca `.download_complete` al terminar TODO (avatar + repos hermanos) para que workers calientes salten.

---

## 6.12 Storage de salida: Cloudflare R2 / S3 (subir el video y dar URL)

```python
import boto3
from botocore.config import Config
s3 = boto3.client(
    's3',
    endpoint_url=f'https://{ACCOUNT_ID}.r2.cloudflarestorage.com',
    aws_access_key_id=R2_KEY_ID, aws_secret_access_key=R2_SECRET,
    region_name='auto',                       # R2 lo exige pero lo ignora
    config=Config(signature_version='s3v4'),
)
s3.upload_file(local_mp4, BUCKET, key, ExtraArgs={'ContentType': 'video/mp4'})  # NO pases ACL
public_url = f'{PUBLIC_URL_BASE}/{key}'       # PUBLIC_URL_BASE = https://pub-<hash>.r2.dev (o dominio propio)
```
- **R2 NO soporta ACLs.** `ACL=public-read` se ignora (no error, no efecto) y NO hace público el objeto.
  Se hace público a nivel BUCKET: activar **r2.dev** (`https://pub-<hash>.r2.dev/<key>`, rate-limited,
  para dev) o un **Custom Domain** vía CDN de Cloudflare (producción).
- `region_name` debe ser literalmente `"auto"`. Bucket en **minúsculas**. `ContentType` correcto para
  que el navegador lo reproduzca inline.
- Presigned URLs funcionan en el endpoint S3, NO en custom domains.
- Mismo patrón sirve para S3 real (cambia endpoint/region; S3 sí tiene ACL pero usa bucket policy).

---

## 6.13 Billing de RunPod serverless a fondo (lo que infla el costo sin que lo veas)

- **El COLD START se cobra.** Pagas el "Start time" = inicializar contenedor + **cargar el modelo a
  VRAM** (pull de imagen + download + load). Por eso un modelo grande con descarga en runtime
  **infla el costo en silencio** (~$0.35-0.45/video solo en bajar 44GB). → Network Volume o `active=1`.
- **Por segundo**, redondeado hacia arriba, desde que el worker arranca hasta que para del todo.
- **`executionTimeout`** = máximo que un job corre DESPUÉS de que un worker lo toma (solo durante
  ejecución). **`ttl` (Job TTL)** = vida total desde que se envía, **incluye cola + ejecución**; al
  expirar BORRA el job aunque estuviera corriendo (status → 404). Ambos tope 7 días. No los confundas.
- **`idle timeout`** (default 5s) = cuánto sigue caliente el worker tras un request.
- **Active vs Flex:** Active (siempre prendido) ≈ **30% más barato/seg** que Flex, pero pagas 24/7.
  Flex escala a cero (no pagas en reposo) pero paga cold start cada vez. Elige por patrón de tráfico.
- **Palancas de costo reales:** (1) Network Volume → mata el re-download del cold start; (2) destilación
  + 480p + int8 → menos segundos de cómputo; (3) GPU correcta (más barata que alcance RAM/VRAM);
  (4) `active=1` solo si el cold start o re-streamear pesos pesa más que el costo de tenerlo prendido.

---

## 6.14 Toolkit de debug: señales y exit codes (qué te está matando)

| Código | Señal | Significado | Acción |
|---|---|---|---|
| **-9 / 137** | SIGKILL | **OOM-killer del kernel** (RAM del sistema, NO VRAM). No atrapable. | Más RAM o cargar en bf16/meta (§6.6) |
| **-11 / 139** | SIGSEGV | Segfault: acceso a memoria malo, CUDA/driver mismatch, ABI de extensión nativa | Revisar versiones torch/cuda/flash_attn |
| **-6 / 134** | SIGABRT | `abort()`: assert C++, NCCL fatal, "device-side assert" CUDA, excepción C++ | Leer el traceback C++/CUDA arriba |
| **1** | — | Excepción de Python sin atrapar (hay traceback) | El error de app normal — leer el traceback |

- **torchrun / `torch.distributed.elastic`** envuelve el fallo en `ChildFailedError` y lo imprime como
  un cuadro **"Root Cause / Failures"** con el **local rank**, host, y el **exit code o señal** (ej.
  "Signal 9 (SIGKILL) received by PID …"). El agente mata todo el grupo si UN rank muere. Lee la señal:
  `Signal 9` = OOM de RAM; `exitcode 1` = excepción Python (busca el traceback REAL más arriba).
- **Reproducir/inspeccionar:** en RunPod, un **Pod interactivo** (no serverless) con la MISMA imagen te
  da shell SSH para correr el comando a mano y ver el error en vivo (serverless no da shell).
- **`No space`/OOM en build vs runtime:** el smoke-test (§3) atrapa imports en build; los OOM y los
  modelos faltantes solo se ven corriendo (runtime). Por eso la observabilidad (§4) es no-negociable.

---

## 6.15 Secretos y seguridad

- **Secretos SOLO por variables de entorno del endpoint** (RunPod env / Render env). NUNCA en la imagen
  Docker, en el repo, ni en los logs. No los imprimas en `log()` ni los pidas en chat/capturas.
- **GHCR:** el paquete debe ser **público** para que RunPod lo baje sin auth. Si es privado, configura
  "registry authentication" en el endpoint con un PAT de solo-lectura de packages.
- **HuggingFace gated:** `HF_TOKEN` como env (no hardcode). Token de solo-lectura.
- **R2/S3:** keys con permiso mínimo (solo ese bucket). El `BUCKET_SECRET_ACCESS_KEY` lo pega el usuario
  directo en el panel, no se comparte.
- **PAT de GitHub para push:** un PAT normal NO tiene `workflow` scope → no puede subir
  `.github/workflows/*` por git; crea ese archivo por la web de GitHub.

---

## 6.16 Proveedores serverless GPU 2026 (cuándo cada uno)

| Proveedor | Modo | Posición |
|---|---|---|
| **RunPod Serverless** | Imagen **Docker** + handler | GPU/seg más barato, scale-to-zero, FlashBoot. Más control, más DIY. **Default para un contenedor propio.** |
| **Modal** | **SDK decorador** Python (`@app.function(gpu=...)`) | DX elegante, cold starts rápidos, $/seg algo mayor. Si vives en Python. |
| **Replicate** | **Cog** (Dockerfile-ish) | Publicar/compartir modelos con API instantánea; **cold starts de modelos custom duros**, $/run mayor. |
| **fal** | SDK/decorador | Optimizado para **media generativa** (imagen/video), warm muy rápido, GPUs premium; menos libertad de contenedor. |
| **Beam** | SDK decorador (+ imágenes custom) | Entre Modal y RunPod en simplicidad/costo. |

Container/Dockerfile: **RunPod, Replicate (Cog)**. SDK-decorador: **Modal, fal, Beam**. Para un avatar/
video custom con control total y costo mínimo → **RunPod**. Si urge y el self-host se atasca → API
premium (Kling/OmniHuman vía **fal**) como red de seguridad.

---

## 6.17 Handler de PRODUCCIÓN: warm-state, concurrencia, progreso

> Más allá de la observabilidad (§4): cómo estructurar el worker para que sea rápido y barato.

- **Carga el modelo UNA vez por worker, NO por job.** Un global a nivel de MÓDULO (top del script,
  fuera de `handler()`) **persiste entre invocaciones del MISMO worker caliente.** El cold start corre
  el módulo entero (baja+carga el modelo a VRAM); cada job siguiente solo llama `handler(event)` y
  reusa el global → **sin overhead de arranque.** Esto es clave para el costo: con `active=1` (o
  mientras el worker siga caliente) el modelo NO se re-descarga ni re-carga.
  ```python
  # --- nivel módulo: corre 1 vez por worker (cold start) ---
  MODEL = None
  def _load():
      global MODEL
      if MODEL is None:
          ensure_model(); MODEL = load_into_vram()   # caro, 1 sola vez
      return MODEL
  def handler(job):
      model = _load()                                 # reusa el global caliente
      ...
  runpod.serverless.start({'handler': handler})
  ```
- **Concurrencia por worker = 1 por default.** Para correr varios jobs en un worker necesitas
  `async def handler` + `concurrency_modifier` en `start({...})`. Sirve para trabajo I/O-bound
  (descargas), NO multiplica el cómputo de GPU (comparten VRAM). Para generación pesada, 1 es lo correcto.
- **Progreso en vivo:** `runpod.serverless.progress_update(job, "bajando modelo 40%")` → se ve en
  `/status` mientras el job está `IN_PROGRESS`. Útil para UIs que muestran avance.
- **Streaming:** un handler `yield` (generador) emite chunks consumibles por `/stream/{id}`. Pon
  `"return_aggregate_stream": True` en el start para que el agregado salga también por `/run`.
- **Idempotencia:** valida el input arriba y devuelve errores estructurados; un mismo job no debe
  cobrar doble si el cliente reintenta (ver §6.22).

---

## 6.18 Integración app ↔ serverless (submit / poll / webhook) — el patrón correcto

> Aquí estuvo el bug "STUDIO dice 'falló'" — el cliente se rendía antes de que el job terminara.

API RunPod (`https://api.runpod.ai/v2/{endpoint_id}/`, header `Authorization: Bearer <API_KEY>`):

| Op | Qué hace | Cuándo |
|---|---|---|
| `POST /run` | **Async**, devuelve `{id, status:IN_QUEUE}` al instante. Resultado guardado **30 min**. | Jobs largos (video). **USA ESTE.** |
| `POST /runsync` | **Bloquea** hasta terminar; resultado **1 min** (máx 5). Si el job excede la ventana HTTP, se cae la conexión y igual debes hacer poll. | Jobs cortos/interactivos. |
| `GET /status/{id}` | Estado + resultado. | Polling. |
| `GET /stream/{id}` | Chunks de un generador. | Streaming. |
| `POST /cancel/{id}` · `/retry/{id}` · `/purge-queue` · `/health` | gestión | — |

**Estados:** `IN_QUEUE` → `IN_PROGRESS` → `COMPLETED` / `FAILED` / `CANCELLED` / `TIMED_OUT`
(TIMED_OUT ≠ FAILED: expiró en cola o el worker no reportó a tiempo).

**El bug clásico (lo que nos pasó):** usar `/runsync` o hacer poll con pocos reintentos en un job que
tarda 10 min (cold start + descarga + generación) → el cliente "se rinde" y muestra "falló", aunque
el worker SIGUE trabajando y termina bien. **FIX, dos opciones:**
1. **Webhook (mejor):** en `/run` manda `"webhook"` como clave de **nivel superior** (hermana de
   `"input"`, NO adentro). RunPod hace `POST` del resultado a esa URL al terminar. Tu endpoint debe
   responder **HTTP 200**; si falla, RunPod reintenta **solo 2 veces más, cada 10s**, y se rinde.
   ```json
   { "input": {"input_image_url":"...","input_audio_url":"..."}, "webhook": "https://studio/api/runpod-callback" }
   ```
2. **Poll con backoff:** `/run` → guarda el `id` → consulta `/status/{id}` con backoff exponencial
   (ej. 3s,5s,8s,13s… hasta el `executionTimeout` del endpoint). NO te rindas a los 30s. Muestra
   "Generando… (puede tardar minutos, no se pierde)" mientras tanto.
- **El límite real del job es el `executionTimeout` del endpoint** (no la ventana HTTP). Sube ese
  timeout para jobs largos; el HTTP es solo transporte.
- **Guarda el resultado tú** (R2/DB) apenas llegue el webhook/poll COMPLETED, para no depender de la
  retención de 30 min de RunPod.

---

## 6.19 Dockerfile profesional + build RÁPIDO (cache de capas)

> Por qué un cambio de 1 línea en el handler dispara un rebuild de ~8 min — y cómo arreglarlo.

- **ORDEN de capas = lo más importante.** Docker invalida una capa y TODAS las hijas cuando cambia.
  Pon lo que cambia POCO arriba (apt, torch, deps) y el código ABAJO. **Copia `requirements.txt`
  primero, instala, y SOLO DESPUÉS `COPY app/`:**
  ```dockerfile
  COPY requirements.txt .
  RUN pip install -r requirements.txt      # capa cacheada si requirements no cambia
  # ... torch, flash_attn, smoke-test ...
  COPY app/ /app/longcat/app/              # un cambio de código solo invalida ESTO (rápido)
  ```
  Si el `COPY app/` está ARRIBA del pip install, cualquier edición de código invalida la instalación
  de torch/flash_attn → re-instala todo → 8 min. Bájalo y ese rebuild desaparece.
- **Cache de capas en GitHub Actions** (rebuilds de segundos en vez de minutos):
  ```yaml
  - uses: docker/setup-buildx-action@v3        # BuildKit requerido
  - uses: docker/build-push-action@v6
    with:
      push: true
      cache-from: type=gha
      cache-to: type=gha,mode=max              # mode=max cachea capas intermedias (default min NO)
  ```
  **Gotcha:** el cache de GHA tope **~10GB/repo** → una imagen CUDA+torch lo revienta y causa misses
  silenciosos. Para imágenes grandes usa **`type=registry`**: `cache-to: type=registry,ref=ghcr.io/
  owner/repo:buildcache,mode=max` (+ matching `cache-from`), sin tope de 10GB.
- **Multi-stage:** compila/instala en una etapa `builder` (con compiladores/`-dev`), y `COPY --from=builder`
  solo los artefactos a una etapa runtime slim → imagen más chica → cold start más rápido (menos pull).
- **`.dockerignore`:** excluye `.git`, pesos locales `*.pt/*.safetensors`, caches, test output → contexto
  de build más chico, menos invalidaciones espurias, menos upload a BuildKit.

---

## 6.20 Testing LOCAL del worker (sin desplegar, sin gastar GPU)

El SDK `runpod` corre tu handler localmente:
- **`test_input.json`** en el cwd con `{"input": {...}}` → `python handler.py` lo detecta, llama el
  handler 1 vez con ese input, imprime el resultado y sale. **Cero red, cero GPU cloud.**
- **`--test_input '{"input":{...}}'`** inline (tiene prioridad sobre el archivo).
- **`--rp_serve_api`** levanta una API FastAPI local en `http://localhost:8000` que imita el endpoint:
  `curl -X POST http://localhost:8000/runsync -d '{"input":{...}}'`.
- **`--rp_log_level DEBUG`** sube verbosidad; **`--rp_debugger`** diagnósticos extra.
- Útil para validar el parsing del input, el armado del comando y la subida a R2 con un mock, ANTES
  de gastar un cold start de 10 min en la nube.

---

## 6.21 Reproducibilidad y determinismo

- **Imagen base por digest:** `FROM nvidia/cuda@sha256:...` (no un tag móvil — los re-pushean).
- **Endpoint apunta al SHA completo** de la imagen GHCR (no `:latest`, que es mutable).
- **Deps pip pineadas** `==`; para integridad total `pip install --require-hashes -r requirements.txt`.
- **Pesos del modelo:** `revision="<commit-sha>"` en `from_pretrained`/`snapshot_download` → HF no te
  mueve a un snapshot nuevo bajo los pies.
- **Determinismo de inferencia:** sembrar todo (`torch.manual_seed`, `numpy.random.seed`, CUDA). Para
  bitwise estricto `torch.use_deterministic_algorithms(True)` + env de cuBLAS (cuesta throughput; la
  mayoría se queda en "sembrado pero no bitwise").

---

## 6.22 Resiliencia y fallback (que el sistema no se caiga)

- **Retry con backoff + jitter:** reintenta fallos transitorios (cold-start starvation, 5xx) con
  backoff exponencial + jitter aleatorio (evita thundering herd cuando el endpoint escala).
- **Idempotency key** por job lógico → reintentos (o webhook + poll disparando ambos) NO cobran doble GPU.
- **Circuit breaker:** tras N fallos seguidos, abre el breaker y deja de martillar; sonda half-open antes
  de reanudar.
- **Timeouts en 2 capas:** HTTP del cliente Y `executionTimeout` del endpoint → un worker colgado no te
  cuelga indefinidamente.
- **Fallback a API premium:** si el self-host falla / está frío / el breaker está abierto → enruta el
  MISMO job a fal.ai / Replicate (Kling/OmniHuman). Mantén una **interfaz de job agnóstica del proveedor**
  (`engines/` + `providers/` como en AGENTE STUDIO) para que el fallback sea un swap, no un rewrite.
- **Observa el gasto:** loguea `$/job` (segundos × $/s de la GPU) por corrida → detecta cold-starts caros
  o crash-loops antes de que se coman el saldo.

---

## 6.23 Gestión de VRAM y OOM-mid-run (≠ OOM al cargar)

> Dos OOMs distintos: **al cargar** (pesos no caben → offload/cuant) vs **a mitad de corrida**
> (pico de ACTIVACIONES o **fragmentación** del allocator). Este es el segundo.

- **Fragmentación = OOM con VRAM libre.** El caching allocator de PyTorch agarra segmentos grandes y
  sub-aloca. Tras muchos ciclos alloc/free de tamaños variables (típico en diffusion: resoluciones/
  frames cambiantes) los segmentos quedan agujereados → una petición de 2GB contiguos falla aunque
  haya 6GB libres en total. Error: `reserved memory >> allocated memory ... try max_split_size_mb`.
- **`PYTORCH_CUDA_ALLOC_CONF`** (env, ANTES de iniciar CUDA):
  - **`expandable_segments:True`** ← **el fix de mayor leverage.** Permite crecer/encoger segmentos
    in-place (vía remapeo de direcciones) → corta drásticamente la fragmentación en cargas de forma
    variable. `export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`.
  - `max_split_size_mb:256` — no parte bloques grandes para requests chicos (reserva los grandes).
  - `garbage_collection_threshold:0.8` — recupera cache proactivamente al cruzar la fracción.
- **Entre jobs:** soltar refs Python → `gc.collect()` → `torch.cuda.empty_cache()` (en ESE orden;
  empty_cache NO libera tensores vivos ni baja el pico, solo devuelve cache no usado para el SIGUIENTE
  alloc). `torch.cuda.reset_peak_memory_stats()` para re-medir.
- **Leer `torch.cuda.memory_summary()`:** `Allocated` = tensores vivos. `Reserved` = lo que PyTorch
  tiene del driver. **`Reserved − Allocated` grande = fragmentación.** `num_alloc_retries > 0` = ya
  estás al borde.
- **APIs de diffusers para bajar VRAM** (en video, las activaciones = frames×H×W dominan → el VAE
  decode y la atención revientan):
  - **`enable_vae_tiling()`** — decodifica el latente en tiles espaciales (y temporales en VAEs de
    video) con overlap → decodifica 4K/clips largos en ~8GB. **El fix del OOM en el paso VAE decode.**
  - **`enable_vae_slicing()`** — decodifica el batch de a 1 (casi gratis, usar siempre con batch>1).
  - **`enable_model_cpu_offload()`** — submódulos enteros en CPU, sube de a 1 a la GPU → pico ≈ el
    componente más grande, **mínima penalización** (1 transferencia PCIe por componente). **Empieza aquí.**
  - **`enable_sequential_cpu_offload()`** — offload por capa, streaming cada step → mínima VRAM pero
    **~3-5× más lento.** Último recurso. (Más nuevo y mejor: `enable_group_offload(use_stream=True)`.)
  - **NUNCA `.to("cuda")` después de activar offload** → pelea con los hooks de accelerate.

---

## 6.24 torch.compile, precisión y cuantización (decodificadas)

- **`torch.compile(model)`** (Dynamo→Inductor→kernels fusionados). Modos: `default` (balance) ·
  `reduce-overhead` (CUDA graphs, mata el overhead de launch en el denoise loop, requiere **shapes
  estáticos**) · `max-autotune` (benchmarka todo, compile de minutos, máxima velocidad — vale para un
  server que compila 1 vez y sirve muchas). Speedup típico ~1.3-2.5× en el forward del DiT/UNet.
- **El impuesto del cold start:** la 1ª llamada compila (segundos-minutos) y se paga en CADA proceso
  fresco salvo que persistas el cache. **FIX:** `TORCHINDUCTOR_CACHE_DIR=/runpod-volume/inductor`
  (en el volumen) y/o la **Mega-Cache** (`torch.compiler.save_cache_artifacts()` → blob portable →
  `load_cache_artifacts()` al arrancar). Requiere MISMA arch GPU + mismas versiones torch/triton/CUDA.
  **Compilación regional:** compila SOLO el bloque caliente (`pipe.transformer = torch.compile(...)`),
  no todo el pipe → compile más rápido, sin recompiles por el VAE/scheduler.
- **Precisión (wins gratis):** `torch.set_float32_matmul_precision("high")` (TF32 en Ampere+, mucho
  más rápido, calidad casi igual) · **bf16 > fp16 para diffusion** (mismo exponente que fp32 → sin
  NaN/imágenes negras; fp16 solo en pre-Ampere; deja el VAE en fp32 si sale negro) · `model.to(memory_format=torch.channels_last)` (acelera UNet/VAE conv-heavy).
- **Formatos de cuantización (cuál es para qué):**
  | Formato | Qué es | LLM/Diffusion |
  |---|---|---|
  | **torchao int8/fp8** (weight-only + dynamic) | nativo PyTorch, **compone con torch.compile** | **el mejor para DiTs de diffusion** (fp8 dynamic +compile ≈ 1.54× en FLUX H100) |
  | **bitsandbytes NF4** (4-bit) | rescate de VRAM en consumer | ambos; corre DiTs grandes en tarjeta chica, hit de calidad menor |
  | **GPTQ / AWQ** | 4-bit con calibración / activation-aware | **LLM-first** (no los uses en DiT salvo loader específico) |
  | **GGUF** | formato llama.cpp (CPU/edge) | LLM-first (creciente en diffusion vía ComfyUI) |
  - **FP8 solo ACELERA en sm_89+ (Ada/Hopper/Blackwell);** en A100 (sm_80) solo ahorra memoria, no
    da el matmul rápido. Siempre combina FP8 con `torch.compile` o dejas la mitad del win en la mesa.

---

## 6.25 Schedulers/samplers + trucos de largo/calidad de video

- **Schedulers (mismo modelo, distinto sampler):** **DPM++ 2M Karras** converge en ~15-25 pasos lo
  que DDIM necesita 40+ (mejor general SD/SDXL) · **flow-matching Euler** (`FlowMatchEulerDiscreteScheduler`)
  es el CORRECTO para rectified-flow (FLUX/SD3, y LongCat) · Euler/DDIM = workhorses lentos.
- **Modelos destilados (cambian el modelo, no el sampler):** LCM (~4-8 pasos) · Turbo (1-4) · DMD/DMD2
  (1-4, SOTA one-step). Si el repo trae `use_distill` → úsalo (es el ahorro #1, ver §6.5).
- **Trucos de video (más largo/suave barato):**
  - **VAE temporal tiling** — decodifica en chunks que se solapan en el EJE TIEMPO → el pico de
    memoria escala con el tile, no con el total de frames.
  - **Sliding window / chunked** — genera en ventanas de N frames condicionando cada una en la cola de
    la anterior (lo que hace LongCat con sus segmentos, §6.8) → video arbitrariamente largo con VRAM
    acotada. Cuida drift/seams → overlap + blend.
  - **Interpolación post-gen — RIFE/FILM** — genera MENOS frames y sube de 8→24/30fps después (mucho
    más barato que generarlos en el difusor, que es lineal en frames).
  - **Upscaling — Real-ESRGAN** — genera en 480p (barato) y sube a 1080p después, en vez de pagar
    ~2.25× por 720p nativo. **Pipeline canónico de costo: render chico → interpolar → upscalar.**

---

## 6.26 Serving: frameworks y batching (cuál y por qué)

| Framework | Tipo | Cuándo |
|---|---|---|
| **Handler RunPod custom** | función `handler(job)` | **Default para un pipeline de video/imagen idiosincrático** (script propio lanzado por torchrun). Máximo control. |
| **ComfyUI como API** | node-graph headless (`--listen`, `POST /prompt`) | Si tu pipeline ES un grafo de loaders/sampler/VAE/LoRA/ControlNet. comfy-deploy lo versiona. |
| **Triton (Dynamo-Triton)** | C++ multi-modelo, dynamic batching, ensembles | Enterprise NVIDIA, multi-framework, tuning fino. Pesado de operar. |
| **Ray Serve / LitServe** | Python; composición / FastAPI+batching | Pipelines de varios modelos (Ray) o un API custom con menos boilerplate (LitServe, ~2× FastAPI). |
| **vLLM / SGLang** | motores de TOKENS (PagedAttention/RadixAttention) | **SOLO LLMs. NO sirven diffusion** (un DiT no tiene KV cache). |
- **`TorchServe` está ARCHIVADO (ago-2025), no lo uses para nuevo.**
- **Batching:** sube la utilización (amortiza la lectura de pesos), pero en **video diffusion el batch
  suele ser 1** porque las activaciones (resolución×frames) llenan la VRAM → un 2º sample = OOM. Escala
  con más **workers/GPUs**, no con batch más grande. Batching paga cuando el costo/sample es chico vs
  VRAM (LLM decode, imagen low-res).

---

## 6.27 Multi-GPU: cuál te deja CORRER un modelo que no cabe

| Paralelismo | Reparte | ¿Hace caber un modelo grande? |
|---|---|---|
| **Data (DDP)** | el batch (replica el modelo) | NO — solo throughput; el modelo debe caber en 1 GPU |
| **Tensor (TP)** | matmuls/heads DENTRO de una capa | SÍ (pesos); comm-pesado → **NVLink, 1 nodo** |
| **Pipeline (PP)** | el modelo por capas/etapas | SÍ (pesos); tolera red lenta → multi-nodo |
| **FSDP / ZeRO** | params/grad/optim shard | SÍ (pesos); sobre todo training |
| **Sequence/Context parallel** | la SECUENCIA/latente entre GPUs | **SÍ (ACTIVACIONES) ← el lever de VIDEO** |
- **Context parallel = lo que usan los DiTs de video grandes** (LongCat/Wan/Hunyuan) vía
  `context_parallel_size` + `torchrun --nproc_per_node=N`. **N debe ser igual a `ulysses_degree ×
  ring_degree`** o NCCL se cuelga. **Ulysses** (all-to-all, shard de secuencia) + **Ring attention**
  (streamea K/V en anillo) = USP/2D hybrid (xDiT). Esto hace caber UNA generación enorme cuando las
  activaciones (no los pesos) revientan la VRAM.
- **NCCL** implementa los collectives (all-reduce/all-gather/all-to-all) sobre NVLink (intra-nodo) o
  IB/RoCE (inter-nodo). TP/Ulysses = bandwidth-hungry → 1 nodo NVLink. `NCCL_DEBUG=INFO` para diagnosticar.

---

## 6.28 Monitoreo GPU + driver/toolkit/runtime

- **Herramientas:** `nvidia-smi` (cols: **GPU-Util %** = *solo un busy-flag*, no qué tan llenos los SMs;
  Mem; **Pwr Usage/Cap** = mejor proxy de saturación real; Temp) · `nvtop`/`nvitop`/`gpustat` (TUIs) ·
  **DCGM / `dcgm-exporter`** (Prometheus: SM occupancy, **tensor-core active %**, DRAM bandwidth %,
  NVLink — la utilización REAL) · `pynvml` desde Python · `torch.cuda.utilization()`.
- **"GPU-Util 100% pero LENTO"** = estás **memory-bound**: un kernel siempre corre pero los tensor
  cores esperan memoria (DRAM-bw alto, tensor-active bajo, power < TDP). **"Util baja"** = GPU
  hambrienta (CPU/preprocesado/data-loading/requests chicos). Solo DCGM (no el util de nvidia-smi)
  distingue compute-bound vs memory-bound.
- **Driver vs toolkit vs runtime** (constantemente confundidos):
  - **Driver del host** (`libcuda.so`) → fija la **versión CUDA máxima** (el "CUDA Version" de
    `nvidia-smi` = el MÁX del driver, NO lo instalado).
  - **CUDA toolkit** (`nvcc`) → solo COMPILE-time (compilar extensiones). **NO lo necesitas en la
    imagen si usas wheels precompilados** → base `runtime` slim, no `devel`.
  - **Runtime CUDA** (lo trae el wheel de torch) → habla con el `libcuda` del driver.
  - **Compat:** un driver NUEVO corre runtimes VIEJOS (cu124/126/118). Al revés no. `no kernel image`
    = tu torch es muy VIEJO para la GPU (cu124 en Blackwell), no al revés.

---

## 6.29 Arquitectura del sistema de jobs (cola async)

> Request síncrono se rompe con jobs de minutos (timeout HTTP). Patrón estándar: **cliente → API
> (encola, devuelve id) → cola → pool de workers GPU → store de resultado → notifica (webhook/poll).**

- **Máquina de estados:** `queued → running → done | failed | cancelled` (+ `dead-letter`). RunPod:
  `IN_QUEUE → IN_PROGRESS → COMPLETED | FAILED | CANCELLED | TIMED_OUT`.
- **Tabla `jobs` (Postgres):**
  ```sql
  id UUID PK · idempotency_key TEXT UNIQUE · status · input JSONB · input_hash TEXT  -- cache key
  output_url · error · error_code · attempts · max_attempts · worker_id · provider   -- runpod|fal|replicate
  cost_usd · created_at · started_at · finished_at · lease_expires_at                -- visibility timeout
  ```
  Sin broker propio: **Postgres `SELECT ... FOR UPDATE SKIP LOCKED`** como dispatch (sin infra extra).
- **Semántica de entrega:** las colas son **at-least-once** (un worker puede terminar y morir antes
  del ack → re-corre). **Exactly-once de ENTREGA es imposible** (Two Generals). Lo que SÍ logras:
  **effectively-once de PROCESAMIENTO = at-least-once + consumidor idempotente:**
  - **Idempotency key** del cliente → `INSERT ... ON CONFLICT (idempotency_key) DO NOTHING RETURNING id`.
  - **Visibility timeout / lease** → si el worker muere, expira el lease y se re-entrega.
  - **Dead-letter queue** tras `max_attempts` → un job veneno no bloquea la cola ni quema GPU en loop.

---

## 6.30 Seguridad profunda (input/SSRF, contenedor, webhooks)

- **🔴 SSRF — el riesgo #1 de un worker que baja URLs del usuario** (`input_image_url`): el atacante
  apunta a recursos internos que el worker alcanza pero él no — el clásico **metadata `169.254.169.254`**
  (así fue Capital One 2019: SSRF→metadata→creds IAM→100M registros). Mitigación (defensa en capas):
  - **Allowlist de destino** (dominios + solo `https`), no denylist.
  - **Resuelve DNS → valida la IP RESUELTA → conecta a ESA IP** (cierra el hueco DNS-rebinding). Bloquea
    `127/8`, RFC1918 (`10/8`,`172.16/12`,`192.168/16`), **`169.254/16` link-local**, `::1`, `fc00::/7`.
  - **Sin redirects** (o re-valida cada hop) · timeout · tope de tamaño/streaming · `Content-Type` allowlist.
  - **Exige IMDSv2** en la infra (hop-limit 1) para que ni un SSRF funcional lea metadata. Lib: `advocate`.
- **Validación de input:** **Pydantic v2** (`extra='forbid'`, bounds), magic-bytes (no la extensión),
  **descompresión-bomba** (Pillow `MAX_IMAGE_PIXELS`, tope de entradas/size en zips).
- **Contenedor/supply-chain:** **`USER nonroot`** (UID≥10000) · base mínima + multi-stage (sin nvcc/-dev)
  · **escanear Trivy/Grype** (fallar en HIGH/CRITICAL) · **SBOM con Syft** · pin base por digest · `pip
  install --require-hashes` + `pip-audit` · **NUNCA `|| true`** · smoke-test de imports en el build (§3).
- **Webhooks:** cuando RECIBES uno, no confíes en el body por llegar a tu URL. Verifica **firma HMAC-
  SHA256 sobre los bytes crudos** + **`hmac.compare_digest`** (tiempo constante) + **timestamp/replay
  window** (~5min). **RunPod NO firma sus webhooks** → asegúralo tú (secreto de alta entropía en la URL
  de callback, y busca el job por id en TU DB en vez de confiar en el body). Y hazlo **idempotente**
  (RunPod reintenta el webhook 2 veces más / 10s → puede llegar 2-3 veces).

---

## 6.31 Dependencias (uv) + MLOps + evaluar calidad generativa

- **`uv`** (Astral, Rust) = estándar 2026: 10-100× más rápido que pip, reemplaza pip/pip-tools/poetry/
  virtualenv, **lockfile universal `uv.lock`** (hash-pinned, reproducible, PEP 751). Para Docker:
  `uv pip compile requirements.in -o requirements.txt --generate-hashes` → instala con `--require-hashes`.
- **MLOps / ciclo del modelo:** pin `revision=<commit-sha>` en HF (no branch/tag, se mueven) · un
  **model registry** (MLflow/W&B) mapea "nombre+versión+stage" a artefacto + el eval que lo promovió.
  - **Rollout de versión nueva:** **shadow** (copia tráfico, NO devuelve output, compara offline) →
    **canary** (1→5→25→100%, auto-rollback en regresión) → **blue-green** (flip atómico, rollback = flip).
    El rollback debe ser un FLIP de config (puntero de stage / SHA de imagen), no un rebuild.
- **Evaluar OUTPUT generativo** (no hay label único → usa una CANASTA, no confíes en una sola):
  - Imagen **FID** (distancia de distribuciones Inception, set-level, sin sentido en 1 imagen) · Video
    **FVD** (FID temporal, I3D) · adherencia al prompt **CLIP-score** · **aesthetic score** (LAION) ·
    preferencia humana **HPSv2/ImageReward/PickScore**.
  - **La evaluación HUMANA (side-by-side / Elo) sigue siendo el rey** — toda métrica automática es un
    proxy con fallos (FID mejora mientras se ve peor; CLIP premia keyword-stuffing). Usa las automáticas
    como **tripwire de regresión** (golden set de prompts+seeds, alerta en deltas), con paneles humanos periódicos.

---

## 6.32 Costo avanzado + media (ffmpeg)

- **Spot / community + checkpointing:** spot/interruptible (RunPod Community) = mucho más barato pero
  **se interrumpe** → **checkpointea progreso** (segmentos/latentes/step a R2) para REANUDAR, no reiniciar.
  En video multi-segmento es natural: checkpointea cada segmento, al resumir salta los hechos (§6.8).
- **Cache/dedup de resultados:** hashea los inputs normalizados → si `input_hash` ya tiene un COMPLETED,
  **devuelve el `output_url` cacheado y salta la regeneración** (la "inferencia" más barata = 0 GPU-seg).
- **Right-sizing:** la GPU más barata que QUEPA (RAM+VRAM) suele ganar en $/job aunque sea más lenta (la
  rápida gana solo si su ratio de velocidad supera el de precio — §6.5). **Modela el cold start**
  (`$/job = $/s × (cold_start + inference)`; ~$0.35-0.45/video solo de bajar 44GB) → Network Volume o
  warm worker + cargar el modelo 1 vez por worker (§6.17). **Loguea `cost_usd` por job** (§6.22).
- **ffmpeg para web (los 2 flags más olvidados):**
  ```bash
  ffmpeg -i in.mp4 -c:v libx264 -profile:v high -pix_fmt yuv420p -crf 20 -preset medium \
         -c:a aac -b:a 128k -movflags +faststart -shortest out.mp4
  ```
  - **`-movflags +faststart`** → mueve el `moov` atom al frente → el navegador reproduce mientras
    descarga (sin esto, espera el archivo completo).
  - **`-pix_fmt yuv420p`** → sin esto, Safari/QuickTime muestran NEGRO (no soportan yuv444/422).
  - `-crf 20` (calidad constante, ~18 visualmente lossless) · `-shortest` (corta al stream más corto,
    clave al muxear audio aparte). **AV1/VP9** = ~30-50% más chicos pero encode lento + soporte
    angosto → manda H.264 por compat, AV1 opcional para clientes modernos.

---

## 7. Checklist de despliegue (orden)

1. [ ] Leer repo real: `requirements.txt` (pins de torch — **úsalos, no subas a la última**),
       script de inferencia (args + JSON de input exacto), **TODOS los `from_pretrained` (¿carga
       de otros repos?)**, dónde escribe el output (¿segmentos?), VRAM **y RAM** necesarias.
2. [ ] **Sizing de disco:** sumar imagen + cada modelo (verificar tamaños en HF, ojo encoders) +
       staging → fijar Container disk con margen. **Sizing de RAM:** params×(4 fp32 / 2 bf16) +
       encoders + 10GB → elegir GPU con suficiente RAM (no solo VRAM).
3. [ ] Elegir GPU según matriz (cu compatible con el pin de torch) + RAM suficiente + disponibilidad.
4. [ ] Dockerfile: deps only (modelo NO horneado), torch+flash_attn del COMBO del repo, sin `|| true`,
       **smoke-test de imports al final** (revienta el build, no la GPU).
5. [ ] Handler con observabilidad (logs + stream subprocess + try/except), descarga de TODOS los
       repos necesarios (principal + hermanos con `allow_patterns`), `num_segments` desde el input.
6. [ ] CI (Actions) → GHCR público. Apuntar el endpoint al **SHA completo**, no `:latest`.
7. [ ] RunPod: endpoint "Docker registry" + GPUs (con RAM) + Container disk + timeout + env (storage).
       Network Volume solo si conviene (ojo region-lock); si no, disco grande + descarga en runtime.
8. [ ] Storage (R2/S3): bucket en minúscula, sin ACL si es R2, `PUBLIC_URL_BASE` para URL pública.
9. [ ] 1ª corrida = lenta (descarga modelos). Leer logs `[app]`. Si falla, ubícalo en la cascada (§6.9).

---

## 8. Errores comunes → fix inmediato

| Síntoma | Causa | Fix |
|---|---|---|
| Build RunPod "exceeded 30 min" / `input/output error` | modelo horneado (imagen enorme) | Sacar modelo de la imagen → Network Volume |
| `no kernel image is available` | torch/CUDA viejo para la GPU | Subir a cu128/torch2.7 (Blackwell) |
| `undefined symbol _ZN3c10...` al importar flash_attn | mismatch C++ ABI | Cambiar wheel cxx11abi FALSE↔TRUE |
| job status FAILED, logs no muestran error | worker crasheó (no error controlado) | Observabilidad: stream subprocess + try/except |
| `No space left on device` en descarga | modelo a disco efímero (5GB) | Montar Network Volume, descargar ahí |
| Push no dispara build en RunPod | auto-build GitHub roto | GHCR + Actions; RunPod solo descarga |
| GPU "Unavailable" | pico temporal de demanda | Esperar / marcar varias GPUs compatibles |
| Storage 403 / bucket inválido | R2 no soporta ACL; nombres minúscula | Quitar ACL, bucket lowercase, PUBLIC_URL_BASE |
| `ModuleNotFoundError` saliendo de a uno en runtime | `pip install -r req.txt \|\| true` ocultó un fallo; línea tóxica tumbó todo el archivo | Quitar `\|\| true`; `sed` las líneas inválidas; auditar grafo de imports + smoke-test en build |
| `ImportError: cannot enable executable stack` | `onnxruntime==1.16.3` (.so con bandera execstack) en glibc moderno | Subir a `onnxruntime>=1.17` (sin execstack); NO usar `execstack` (no está en Debian nuevo) |
| Worker viejo sigue fallando tras cambiar config | el cambio (disco/dep) solo aplica a workers NUEVOS | Borrar workers "Outdated" o cambiar la imagen (SHA) → fuerza recreación |
| `IMAGE_NOT_FOUND: manifest unknown` en RunPod | tag corto (SHA 7) no existe en GHCR | Usar el **SHA completo (40)** o `:latest`; Actions solo publica SHA largo + latest |
| Build RunPod auto-build no toma el push | auto-build GitHub frágil | Smoke-test en build de Actions; RunPod solo descarga imagen por SHA |
| `undefined symbol _ZN3c105Error...__cxx11` (flash_attn O xformers) | torch 2.7.0 cambió el ABI; no hay wheel cp310 funcional de flash_attn 2.7.4 ni xformers 0.0.30 | Volver al torch del repo (2.6 cu124) — NO pelear con wheels de atención en 2.7 |
| `unhealthy container: triggered memory limits (OOM)` / `SIGKILL -9` | RAM del sistema insuficiente para instanciar el modelo (fp32) | GPU con más RAM (A100/H100) o patch a bf16/meta device. Ver §6.6 |
| `OSError: Incorrect path_or_model_id` / `HFValidationError` | el modelo carga sub-modelos de OTRO repo (ruta relativa) y no lo bajaste | Grepea los `from_pretrained`; baja el repo hermano a la ruta esperada. Ver §6.7 |
| Video sale corto (ej. 3s de un audio de 13s) | `num_segments=1` por default; el modelo genera en chunks | Calcular `num_segments` desde la duración del audio y pasarlo por CLI. Ver §6.8 |
| `No space left on device` con Container disk grande | sumaste mal el disco (encoders enormes, ej. UMT5 22.7GB) | Recontar imagen + TODOS los modelos + staging; subir disco. Ver §6.7 |

---

## Relacionado
- Proyecto vivo: AGENTE STUDIO (lip-sync RunPod). Ver memoria `project-studio-runpod-lipsync`.
- Disciplina: memorias `feedback_prepare_deeply`, `feedback_verify_before_setup`.
- **Mantener esta skill viva:** cada vez que un error nuevo cueste >30 min, agregar su
  fila a "Errores comunes" y la lección a "Reglas de oro".

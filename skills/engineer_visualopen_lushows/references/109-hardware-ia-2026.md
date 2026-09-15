# 109 — Hardware de IA (2026)

> Snapshot fechado. Precios muy volátiles — re-verifica.

## NVIDIA Blackwell (data center)
**B200** ~$30K-50K lista (costo fab ~$5.5-7K); **DGX B300** ~$300-350K; **GB200 NVL72** en asignación apretada. Renta cloud B200 Q2 2026 ~$4.50-7.00/hr.

## Consumer GPU — RTX 50-series
**RTX 5090 con 32GB GDDR7** = líder precio/rendimiento (~$0.99/hr cloud); 32GB caben SDXL + ControlNet + varios LoRAs.
**El VRAM sigue siendo el limitante real** para correr modelos grandes localmente.

## AMD / Google / inferencia especializada
**AMD MI400/MI450 "Helios"** (2026) con **HBM4 a 19.6 TB/s** (>2× MI350) → entrenar grandes sin pipeline parallelism;
ROCm cierra brecha pero **CUDA aún domina el ecosistema**. **Google Ironwood (TPU v7)** — 4,614 TFLOPS/chip.
**Groq LPU** (276-300 tok/s en Llama 70B, hasta 1,665 con spec decoding; $0.79/M output). **Cerebras CS-3** (wafer-scale, 900K cores, sin comunicación chip-a-chip). **SambaNova, AWS Trainium/Inferentia.**

## Apple Silicon & cloud
**M5** (Neural Engine 16-core + acelerador por core GPU, 4× compute GPU vs M4); M5 Pro/Max con memoria unificada alta
→ corre modelos grandes 100% on-device (la memoria unificada es la ventaja: un M5 Max con mucha RAM corre lo que una
5090 32GB no). **Cloud:** H100 cayó de ~$8/hr (2023) a **$1.80-3.50/hr** (Q2 2026), spot hasta $1.20/hr.

**Comprar vs rentar:** **Rentar** (RunPod/spot) si uso esporádico o necesitas Blackwell/H100. **Comprar** Mac M5 con RAM alta o una 5090 si haces inferencia local constante (privacidad + costo marginal cero).

## Gotchas
1. **VRAM es el muro, no FLOPS:** 32GB de la 5090 no corre 70B en fp16; necesitas cuantización o multi-GPU.
2. Precios B200/GB200 muy variables + escasez → "list price" ≠ lo que pagas.
3. Apple M5: memoria unificada compartida CPU/GPU/NPU; un modelo grande deja poca RAM para el SO.
4. Groq/Cerebras brillan en throughput de inferencia pero no entrenas en ellos; lock-in de API.
5. AMD MI400: hardware competitivo, pero **verifica soporte ROCm de tu framework** antes de comprometerte.
6. **Para LatAm: importar GPUs es caro/lento; rentar cloud por hora suele ganar a comprar.**

**Fuentes:** siliconanalysts.com · intuitionlabs.ai (NVIDIA GPU pricing) · spheron.network (best GPU inference 2026) · gpunex.com (NVIDIA vs AMD 2026).

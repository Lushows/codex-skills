# 82 — Modelos de generación de VIDEO: estado del arte (junio 2026)

> Snapshot fechado. La frontera se movió a **audio nativo sincronizado + 4K + control multi-shot**; la resolución ya no diferencia.

## Closed / API frontier
- **Google Veo 3.1** — líder general. **Único con diálogo sincronizado a 48kHz** (no solo SFX), 4K, 16:9+9:16, reference controls avanzados.
- **OpenAI Sora 2 / 2 Pro** — coherencia narrativa fuerte. **Pro: $0.30/s a 720p, $0.50/s a 1080p.** ⚠️ Reportes: **Sora 2 web/apps se apagaron el 26 abr 2026**, API discontinúa 24 sep 2026 — OpenAI pivota a enterprise. **Ten fallback.**
- **Kling 3.0** (Kuaishou) — **único con 4K nativo** y **el premium más barato (~$0.10/s)**, excelente multi-shot/subject consistency. **Kling 3.0 Omni** unifica video+audio+imagen+edición con lip-sync nativo 5 idiomas.
- **Seedance 2.0** (ByteDance) — top en text-to-video arena.
- **Runway Gen-4.5 + Aleph** — Aleph = edición video in-context; Gen-4.5 **cayó del top-10** (el churn es real). **Hailuo 2.3** (~$0.28/video 6s). **Luma Ray 3, Pika 2.5, Higgsfield.**

## Open weights (lo desplegable)
- **Wan 2.7** (Alibaba, abr 2026) — first/last frame, 9-grid input, **Apache 2.0**. ⚠️ **Wan 2.5 y 2.6 son SOLO API de Alibaba Cloud, SIN pesos** — solo 2.2 y 2.7 self-hosteables.
- **LTX-2.3** (Lightricks, 5 mar 2026) — 22B, **4K nativo a 50fps con audio estéreo 24kHz**, Apache 2.0. El open más capaz en 4K+audio.
- **HunyuanVideo 1.5** (Tencent) — 8.3B, **75s en una sola RTX 4090**, Apache 2.0. Ideal "GPU poor".

## Gotchas
1. **Wan 2.5/2.6 NO tienen pesos abiertos** pese a que muchos los citan como open — solo API de Alibaba.
2. **Solo Veo 3.1 hace diálogo 48kHz real**; el "audio nativo" de otros es mayormente SFX/ambiente.
3. **Sora 2 con apagado (26 abr 2026)** — riesgo de dependencia.
4. Precio por segundo varía 5×: Kling ~$0.10/s vs Sora 2 Pro 1080p $0.50/s — escoge según volumen.
5. HunyuanVideo 1.5 cabe en 4090 pero **75s de render por clip** — no es tiempo real.
6. Runway Gen-4.5, líder hace meses, ya salió del top-10 — **no te cases con un modelo.**

**Fuentes:** atlascloud.ai/blog (best video 2026) · artificialanalysis.ai/video/leaderboard · aimagicx.com (open-source video) · findaivideo.com.

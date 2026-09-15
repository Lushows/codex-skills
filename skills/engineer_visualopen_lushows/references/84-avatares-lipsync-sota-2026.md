# 84 — Avatares parlantes y lip-sync: estado del arte (junio 2026)

> Snapshot fechado. La frontera pasó de "sincronizar labios" a **interpretar intención semántica/tono emocional** + gestos full-body desde una imagen + audio.

## Modelos / motores SOTA
- **OmniHuman 1.5** (ByteDance) — film-grade desde **una sola imagen + audio**. Entrenado con **18,700 horas** de movimiento. Salto clave: **no solo sincroniza labios, interpreta intención semántica y tono emocional** (no patrones de audio). Soporta text prompts para control de cámara. Vía API (fal, evolink). El líder de realismo cinematográfico.
- **Hedra Character-3** — **primer modelo omnimodal en producción** (imagen+texto+audio simultáneos). Micro-expresiones + **movimiento full-body**, fuerte en expresividad dramática. Tiene **Live Avatars** (tiempo real). "Nuevo rey de talking heads" 2026.
- **HeyGen** (Avatar IV/V) — comercial. Creator $29/mes, **Avatar IV/V = 20 créditos/min**, API desde $5, 30+ idiomas.
- **Synthesia** — enterprise, **140+ idiomas** (lidera cobertura), desde $29/mes.
- **Kling Act-Two / Runway Act** — "performance transfer" (actuación → avatar) en sus suites.
- **Open source:** **Hunyuan-Avatar** (Tencent, self-hostable), **Sonic**, **EchoMimic**, **LongCat-Video-Avatar 1.5** (gestos+lip-sync, auto-hospedable en RunPod — nuestro caso).

## Gotchas
1. "OmniHuman 1.5" se promociona en sitios de terceros (omnihuman-15.com no es oficial) — usa endpoints serios (fal/evolink) para producción.
2. **HeyGen cobra por crédito/minuto** (20 créditos/min): un video largo consume rápido — modela el costo por minuto.
3. **Real-time** limitado: Hedra Live Avatars sí; la mayoría de OmniHuman/Hunyuan es **offline batch render**.
4. Synthesia gana en idiomas (140+) vs HeyGen (30+) — elige según mercado.
5. Los **open** (Hunyuan-Avatar/Sonic/EchoMimic/LongCat) dan control y costo bajo pero exigen VRAM seria y tuning — no plug-and-play.
6. Calidad full-body+gestos varía mucho con la imagen de referencia: encuadre/iluminación/resolución dominan.

**Fuentes:** fal.ai/models/bytedance/omnihuman · evolink.ai/blog (OmniHuman 1.5) · weshop.ai/blog (Hedra review 2026) · eesel.ai/blog (HeyGen pricing).

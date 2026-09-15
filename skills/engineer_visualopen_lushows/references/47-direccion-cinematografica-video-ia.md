# 47 — Dirección cinematográfica de video con IA (t2v/i2v): dirigir como un DP

Un modelo de video no es un generador de clips, es un equipo de rodaje que obedece órdenes vagas con resultados
vagos. Dirige con la jerarquía de un set: **plano → sujeto + acción → movimiento de cámara → luz → estilo/
atmósfera → duración.** El error más caro: pedir demasiado en un clip. **Un plano = una idea = un movimiento.**

## Estructura de prompt (2026)
> `[shot type] of [subject] [doing action], [camera movement], [lighting], [mood/style], [film look]`

Ej (Runway Gen-4 / Veo 3): *Medium close-up of an elderly fisherman mending a net, slow dolly-in, golden hour backlight with haze, shallow depth of field, cinematic, shot on anamorphic lens.*

## Tipos de plano
`extreme wide / establishing`, `wide`, `full`, `medium`, `medium close-up`, `close-up`, `extreme close-up`,
`over-the-shoulder`, `POV`, `aerial / top-down`.

## Movimiento de cámara (léxico universal)
`dolly in/out`, `push-in`, `pull-back`, `pan left/right`, `tilt up/down`, `truck/track`, `pedestal up/down`,
`crane/jib`, `orbit/arc around subject`, `handheld`, `static/locked-off`, `whip pan`, `FPV drone`, `Steadicam
follow`. **Higgsfield** es la herramienta especializada 2026 con presets nombrados (bullet time, crash zoom, robo
arm, dolly zoom/Vertigo) que clavan el movimiento mejor que el prompt suelto.

## Intensidad de movimiento
Casi todos exponen control (motion brush/camera control Runway/Kling, "motion strength"). **Para look premium:
menos es más.** Movimiento sutil + un solo eje = caro; movimiento caótico = videojuego barato.

## Panorama de modelos 2026
- **Google Veo 3/3.1** — líder en física + único fuerte en **audio nativo sincronizado** (diálogo/SFX/ambiente). Para anuncios con voz, 1ª opción.
- **Runway Gen-4/Turbo** — consistencia de personaje/escena, motion brush, controles de director maduros.
- **Kling 2.1/2.5** — calidad altísima y económico, excelente i2v, `start+end frame`.
- **OpenAI Sora 2** — coherencia larga, audio, físicas, remixing.
- **Hailuo/MiniMax 02** — movimiento expresivo, buen precio. **Luma Ray 2/3** — naturalista, keyframes. **Pika 2.x** — efectos, rápido.
- **Open source:** **Wan 2.2** y **Hunyuan Video** — para auto-hospedar en GPU (RunPod), control total.

## Image-to-video
**La calidad del primer frame dicta TODO.** Genera el start frame con tu mejor modelo de imagen (MJ/FLUX/Nano
Banana), corrígelo, *luego* anímalo. Start frame mediocre = video mediocre garantizado. En el prompt describe solo
el *movimiento*, no re-describas la escena ya presente. **First-last-frame/keyframes** (Kling/Luma/Runway): fija
frame inicial y final → transiciones controladas (producto cerrado→abierto, día→noche). La forma más confiable de domar el caos.

## Gotchas
- **Morphing/warping:** miembros/objetos que mutan → baja motion strength, acorta a 4-5s, simplifica la acción.
- **Temporal flicker:** texturas que hierven → evita fondos muy detallados; usa Veo/Kling 2.5.
- **Roturas de física** (líquidos/telas/multitudes): Veo 3 y Sora 2 son los menos malos; lo demás, evita.
- **Duración limitada** (5-10s nativos): no pidas una "escena" larga; encadena clips cortos con continuidad de start/end frame.
- **Texto que baila:** ningún modelo mantiene texto legible en movimiento → ponlo en post.
- **Deriva de cámara no pedida:** si quieres plano fijo, escribe `static locked-off shot, no camera movement` explícito.

**Fuentes:** runwayml.com · deepmind.google/models/veo · klingai.com · openai.com/sora · higgsfield.ai · github.com/Wan-Video.

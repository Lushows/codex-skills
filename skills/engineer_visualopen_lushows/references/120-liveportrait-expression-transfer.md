# 120 · LivePortrait y expression-transfer (driver de video, no de audio)

> Cuando ya tienes la ACTUACIÓN en un video y solo quieres pasarla a una foto/personaje: transfieres expresión y pose 1:1, sin depender del audio.

## El caso de uso
Avatar **audio-driven** (LongCat, MuseTalk → [[119-avatares-talking-head-self-hosted-2026]]) infiere el movimiento DESDE el audio: bueno cuando no tienes referencia, pero la actuación es "promedio". **Expression-transfer** copia la actuación de un **video driver** real (un actor grabándose) a una imagen estática (retrato, personaje, ilustración). Control total del gesto, parpadeo, mirada y pose de cabeza, frame a frame.

Úsalo cuando: quieres dirección de actuación precisa, doblar a un personaje que no existe (dibujo, foto de stock), reenactment, o pulir la microexpresión de un avatar audio-driven (pipeline en dos etapas: audio mueve boca → LivePortrait añade vida a ojos/cejas).

## Modelos
| Modelo | VRAM | Licencia | Driver | Fuerte en | Notas |
|---|---|---|---|---|---|
| **LivePortrait** (Kwai/KlingAI) | ~6-8GB (256px) | **MIT** ✅ | video o webcam | retargeting fino, stitching, tiempo casi real | **12.8ms/frame en RTX 4090**; el estándar open |
| **Act-One** (Runway) | — (API) | Cerrada ❌ | video | actuación cinematográfica | No self-hosted, referencia de calidad [no verificado: sin pesos] |
| **X-Portrait** (ByteDance) | ~16-24GB | Research ⚠️ | video | movimiento de cabeza amplio, expresión fuerte | basado en ControlNet+diffusion; pesos research |
| **AniPortrait** (Tencent) | ~16GB | Apache-2.0 ✅ | audio **o** video | audio2pose + video2video | híbrido: puede correr audio-driven o por video |

## Por qué LivePortrait gana en self-hosted
- **MIT** (código y pesos), comercial sin fricción.
- Basado en **warping implícito de keypoints** (no diffusion) → ligero, ~6-8GB, casi tiempo real. X-Portrait/Hallo3 son diffusion → más pesados y lentos.
- Módulos de control con MLP de costo despreciable:
  - **Stitching**: pega la cara animada de vuelta al frame original sin costura visible (clave para half/full body).
  - **Eyes retargeting** y **lip retargeting**: controlas apertura de ojos y boca de forma independiente al driver (corriges sobre-actuación o cierras boca en silencios).
  - **Animal mode**: fine-tune sobre ~230K frames (gatos/perros). Ojo: **stitching y retargeting NO están entrenados para animales** → en animal mode pierdes esos módulos.

## Comando típico (LivePortrait)
```bash
git clone https://github.com/KwaiVGI/LivePortrait && cd LivePortrait
pip install -r requirements.txt
# descargar pesos (insightface + liveportrait) a ./pretrained_weights
python inference.py \
  -s assets/examples/source/foto.jpg \   # imagen fuente (a animar)
  -d assets/examples/driving/actor.mp4 \  # video driver (la actuación)
  --flag_stitching --flag_eye_retargeting --flag_lip_retargeting
# salida en animations/  (concat source|driver|result)
```
Flags útiles: `--flag_relative_motion` (transfiere movimiento relativo, no pose absoluta → preserva identidad de la fuente), `--flag_pasteback` (pega al frame original).

## Gotchas
- **Foto fuente frontal y neutral** rinde mejor; perfiles extremos rompen el warping.
- Sin diffusion → **no inventa** lo que no ve: si el driver gira 90° pero la foto es frontal, aparecen artefactos (no hay textura de oreja/perfil). Para giros grandes usa X-Portrait/AniPortrait (diffusion).
- Es **silent**: LivePortrait NO genera sync de audio. El video driver aporta el movimiento de boca; si quieres que hable un audio, primero genera el driver con un audio-driven o usa AniPortrait en modo audio.
- El driver y la fuente comparten **face landmarks** internamente; si la detección de cara falla (insightface), no anima → ver encoders y detección en [[121-pose-landmarks-audio-encoders-avatar]].
- VRAM sube con resolución; el modelo opera la cara a ~256/512px y hace pasteback, así que 6-8GB basta incluso en GPUs modestas.

Cruza con [[119-avatares-talking-head-self-hosted-2026]], [[121-pose-landmarks-audio-encoders-avatar]].

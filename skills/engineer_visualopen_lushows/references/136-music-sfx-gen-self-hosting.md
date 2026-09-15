# 136 · Música y SFX generativos self-hosting (banda sonora para reels/comerciales)

> Generar música y efectos de sonido open-source para acompañar vídeo. La trampa NO es la VRAM
> (cabe en cualquier GPU) — es la **licencia comercial**. MusicGen es NC: no lo uses en un comercial.

## El cuadro de decisión (lo que de verdad importa: licencia)
| Modelo | Tarea | VRAM | Duración | Licencia | Uso comercial |
|---|---|---|---|---|---|
| **ACE-Step 1.5** | música (canción completa, multilingüe, letras) | <4 GB | canción full, síntesis <10 s | **MIT** | **Sí, libre** |
| **Stable Audio Open 1.5** | música + SFX (texto→audio) | ~12 GB fp16 | hasta ~47 s | Stability AI Community | Sí **bajo umbral de ingresos** |
| **MusicGen** (Meta/AudioCraft) | música, condicionable por melodía | ~12 GB (stereo fp16) | ~30 s, extensible | **CC-BY-NC 4.0** | **NO** (no comercial) |
| **AudioGen** (Meta/AudioCraft) | **SFX** / sonido ambiental desde texto | media-baja | corto | pesos CC-BY-NC | **NO** (no comercial) |

Regla: para un comercial/reel monetizado → **ACE-Step (MIT)** primero; Stable Audio Open si estás bajo el umbral de ingresos de la Community License. MusicGen/AudioGen solo para prototipo interno o draft, nunca en el entregable final.

## ACE-Step 1.5 — el ganador práctico 2026
- MIT, multilingüe, soporta letras y **edición**, personalización ligera vía **LoRA**. Síntesis de canción completa en <10 s con **<4 GB VRAM** → corre hasta en GPU pequeña / parte del flujo sin reservar A100.
- Rival open de Suno; calidad muy por encima de MusicGen para canciones estructuradas.
```bash
pip install acestep   # o clonar ace-step/ACE-Step-1.5
# prompt de estilo + (opcional) letras → wav; LoRA para sonido de marca consistente
```

## Stable Audio Open 1.5 — texto→audio versátil (música + SFX)
- ~12 GB fp16, clips hasta ~47 s. Bueno para **loops, texturas, SFX y stems** además de música corta.
- Licencia **Stability AI Community**: comercial permitido **mientras los ingresos de la empresa estén por debajo del umbral** (verifica el monto vigente en la licencia [no verificado el umbral exacto a fecha]). Por encima → licencia de pago.

## MusicGen / AudioGen (AudioCraft) — solo prototipo
- MusicGen: `small/medium/large`, condicionable por melodía de referencia (tarareas → arregla). `stereo` ~12 GB fp16. **CC-BY-NC**: úsalo para iterar ideas, no en el master final.
- AudioGen: especializado en **efectos de sonido** desde texto ("pasos en grava", "lluvia") — útil para SFX puntuales, misma restricción NC.

## Patrón de producción (banda sonora de reel)
1. Genera la cama musical con **ACE-Step** (prompt de género/mood + BPM acorde al corte) → wav 30-60 s.
2. SFX puntuales con **Stable Audio Open** (o librería con licencia) y mézclalos.
3. **Ajusta a la duración del vídeo y duck bajo la voz** con ffmpeg:
```bash
ffmpeg -i video.mp4 -i music.wav -filter_complex \
 "[1:a]aloop=-1:size=2e9,atrim=0:duration=DUR[m];[0:a][m]sidechaincompress=threshold=0.05:ratio=8[a]" \
 -map 0:v -map "[a]" -shortest out.mp4
```
4. Loudness a -14 LUFS (web/redes) con `loudnorm`.

## Sizing y caché
- Todo cabe en 4-12 GB → una L4/A10/T4 sirve; no necesitas H100 para audio gen. El cuello es **iteración** (varios takes hasta que pega con el corte), no la VRAM.
- Cachea pesos en Network Volume [[113-network-volume-modelos-grandes]] para no re-bajar en cold start.
- Conserva el **prompt + seed** de cada take para reproducir/variar la cama de marca.

Cruza con [[54-musica-sfx-sonido-video]] (diseño de sonido y mezcla dentro del pipeline de vídeo) y [[02-open-models-catalog-2026]] (estado/licencias de los modelos open vigentes).

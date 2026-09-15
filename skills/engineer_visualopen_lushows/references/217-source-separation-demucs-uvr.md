# 217 · Source separation (Demucs / MDX / UVR): aislar la voz del avatar

> La muestra que clonas casi nunca viene limpia: tiene música, ruido de fondo o el "other" del mix.
> Separar fuentes ANTES de clonar/transcribir es el primer eslabón: basura entra, basura clona.

## Para qué, en el pipeline de avatar
La grabación de referencia (un reel, un podcast, un video viejo) trae voz + música + ambiente.
El clonador de voz ([[116-voice-clone-produccion-retencion]]) y el TTS necesitan **voz seca**, sin
acompañamiento ni reverb fuerte. Source separation extrae el stem de **vocals** y descarta el resto.
Esto va antes de denoise ([[218-audio-denoise-enhance-deepfilternet]]) y antes de transcribir.

## El campo (open, self-host) en 2026
| Familia | Qué hace | Cuándo usarla |
|---|---|---|
| **Demucs v4** (`htdemucs`, `htdemucs_ft`) | 4 stems (vocals/drums/bass/other), realismo multi-stem | default robusto; `_ft` (fine-tuned) preserva mejor voz+acompañamiento |
| **MDX-Net** (UVR-MDX-NET variants) | separación de precisión, instrumentales/acapellas más limpias | cuando quieres vocal acapella lo más seco posible |
| **BS/Mel-RoFormer** | SOTA actual, artefactos bajos, sonido natural | mejor calidad percibida de voz; más lento/pesado |
| **MDX23 (ensemble)** | combina htdemucs_ft + MDXv3 + UVR-MDX FT | máxima calidad, pero **muy lento** (~17 min/5 min en T4) |

Para una muestra de avatar lo pragmático: **RoFormer vocals** o **htdemucs_ft** → suficiente para clonar.
Reserva el ensemble MDX23 para material muy sucio donde la voz vale el costo de cómputo.

## Hands-on (Demucs)
```bash
pip install demucs
# solo el stem de voz, modelo fine-tuned:
demucs --two-stems=vocals -n htdemucs_ft entrada.wav -o out/
# salida: out/htdemucs_ft/entrada/{vocals.wav, no_vocals.wav}
```
`--two-stems=vocals` evita calcular drums/bass/other → más rápido. Salida a 44.1k; remuestrea al
sample rate que pida tu clonador (a menudo 16k/24k) en el siguiente paso con ffmpeg.

UVR (Ultimate Vocal Remover) es la **GUI** que orquesta estos pesos (MDX/Demucs/RoFormer) con
ensembles — útil para curar a mano; en producción serverless invoca los pesos por CLI/Python.

## Detalles que muerden
- **VRAM/tiempo**: RoFormer y ensembles son pesados; htdemucs corre cómodo en GPU mediana. En CPU es
  viable pero lento — batchea offline, no en el request caliente.
- **Reverb/eco**: separation quita música, NO quita reverb de sala. Para eso, un modelo de-reverb o
  enhance ([[218-audio-denoise-enhance-deepfilternet]]) después.
- **Bleed**: en voces solapadas con instrumentos fuertes queda "fantasma" instrumental → sube a un
  ensemble o aplica un segundo pase MDX inst.
- **Mono vs estéreo**: clona en mono; colapsa antes de separar si el estéreo confunde al modelo.
- **Licencias**: Demucs es MIT; pesos de UVR community varían — revisa antes de uso comercial.

## Orden recomendado del front audio
separar (217) → denoise/de-reverb (218) → super-res si la fuente es pobre (219) → clonar/TTS (116).
No inviertas: denoise sobre música mete artefactos; separa primero.

Cruza con [[01-audio-avatar-pipeline]] y [[116-voice-clone-produccion-retencion]].

# 218 · Denoise y enhance de audio (DeepFilterNet / Resemble-Enhance)

> Tras separar la voz, todavía quedan ruido de fondo, hiss y reverb. El clon suena a lo que le das:
> una muestra seca y nítida produce un avatar creíble; una sucia arrastra el ruido al output para siempre.

## Dónde encaja
Va **después** de source separation ([[217-source-separation-demucs-uvr]]) y **antes** de clonar voz
([[116-voice-clone-produccion-retencion]]) o de transcribir. Dos trabajos distintos que a veces se
confunden:
- **Denoise**: quitar ruido/hiss/eco preservando la voz tal cual (no la "mejora").
- **Enhance/restore**: reconstruir voz degradada — denoise + de-reverb + a veces re-síntesis y upsampling.

## Las dos herramientas open clave (2026)
| Herramienta | Tipo | Fuerte en | Notas |
|---|---|---|---|
| **DeepFilterNet3** | denoise real-time, no generativo | clips cortos, baja latencia, alto PESQ/STOI; incluye upsampling a 48k | ganador para la mayoría; corre en CPU/consumer, no inventa audio |
| **Resemble-Enhance** | denoise + enhancer **generativo** | grabaciones muy degradadas, de-reverb, claridad | GPU recomendable; al ser generativo puede "alucinar" timbre — verifica que no cambie la voz |

Regla práctica: empieza con **DeepFilterNet3** (seguro, no altera identidad). Solo si la voz sigue
turbia o con reverb pasa por **Resemble-Enhance**, escuchando que el timbre del avatar no se desvíe.

## Hands-on
```bash
# DeepFilterNet3 — denoise + upsample a 48k en un paso
pip install deepfilternet
deepFilter voz.wav -o limpio/        # salida 48 kHz

# Resemble-Enhance — denoise + enhance (GPU)
pip install resemble-enhance
resemble-enhance entrada/ salida/ --denoise_only   # solo denoise, sin re-síntesis
resemble-enhance entrada/ salida/                  # denoise + enhancer generativo
```
Para clonar, baja luego al sample rate del clonador con ffmpeg ([[142-ffmpeg-avatar-video-a-fondo]]):
```bash
ffmpeg -i limpio.wav -ar 24000 -ac 1 ref_24k.wav
```

## Detalles que muerden
- **No sobre-procesar**: dos pases de enhance generativo dejan la voz "plástica" / metálica. Un pase.
- **De-reverb ≠ denoise**: DeepFilterNet quita ruido, no reverb de sala. Para eco usa Resemble-Enhance
  o un de-reverb dedicado. Si la sala es muy viva, mejor regraba: ningún modelo lo arregla del todo.
- **Identidad de voz**: el enhancer generativo puede correr el timbre. Compara A/B la muestra original
  vs enhanced; si cambió, quédate con denoise puro.
- **Orden con super-res**: si la fuente es de baja calidad de banda (teléfono, 8k), antes de enhance
  conviene bandwidth extension ([[219-audio-superres-bandwidth]]).
- **Real-time vs batch**: DeepFilterNet es streaming-capable; para preparar muestras hazlo offline,
  no en el request caliente del worker GPU.

## Checklist de muestra lista para clonar
voz seca, mono, sin música, sin reverp audible, sin clipping, ≥ 16 kHz (mejor 24/48), 10-60 s útiles.

Cruza con [[116-voice-clone-produccion-retencion]] y [[142-ffmpeg-avatar-video-a-fondo]].

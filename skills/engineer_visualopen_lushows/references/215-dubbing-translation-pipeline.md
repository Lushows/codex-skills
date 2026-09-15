# 215 · Doblaje y traducción de voz end-to-end (STT→MT→TTS-clone→lip-sync)

> Doblar un video con la voz original en otro idioma es una **cadena de 5 eslabones**. El que falle marca
> el techo de calidad. Y el problema duro no es traducir: es que la traducción **dure lo mismo** que el labio.

## La cadena (5 eslabones, [verificado])
```
1. Separación   Demucs → vocal + fondo (preserva música/SFX del original)
2. STT          WhisperX → texto + timestamps por palabra + diarización (50+ idiomas)
3. MT           NLLB / M2M-100 → traducción
4. TTS-clone    XTTS / CosyVoice / GPT-SoVITS / Chatterbox → voz clonada del locutor (3-10s de ref)
5. Lip-sync     Wav2Lip / LatentSync / MuseTalk → boca alineada al nuevo audio
6. Mux          remezcla voz nueva + fondo original → MP4
```

## Proyectos open de referencia (2026, [verificado])
| Proyecto | STT | MT | TTS | Lip-sync | Nota |
|---|---|---|---|---|---|
| **Linly-Dubbing** | WhisperX, FunASR | — | CosyVoice, GPT-SoVITS, XTTS, Edge | Linly-Talker | One-shot clone 3-10s; fuerte en chino |
| **OmniVoice Studio** | WhisperX | sí | difusión zero-shot (clon 3s) | — | "alternativa local a ElevenLabs" |
| **VoxDub** | Whisper | NLLB | TTS | Wav2Lip | Pipeline compacto |
| **Union.ai demo** | Whisper | M2M | Coqui XTTS | SadTalker | Referencia didáctica |

WhisperX es el STT de facto: timestamps a nivel palabra + diarización, indispensable para alinear.

## El problema central: isocronía (que el doblaje quepa en el tiempo)
La traducción casi nunca dura lo mismo que el original. Si no la ajustas, el labio y la voz se desincronizan
y el lip-sync amplifica el error. Soluciones, en orden de calidad:
1. **MT consciente de longitud**: pide al traductor una versión que quepa en N segundos (prompt o length penalty).
2. **Time-stretch sin cambiar pitch**: **pyrubberband** estira/comprime el audio TTS a la duración del segmento
   (VAD-based duration alignment). Es la palanca práctica que usa Bluez-Dubbing.
3. **Ajuste de pausas**: reparte el desfase en silencios entre frases, no dentro de las palabras.
4. **Re-sintetizar con velocidad objetivo** si el TTS acepta control de duración.

## Detalles que muerden
- **Diarización antes de clonar**: si hay 2 hablantes y no los separas, clonas un timbre promedio = ninguno.
  WhisperX diariza → un modelo de voz por speaker.
- **Demucs no es opcional**: sin separar, el TTS pisa la música original o esta se cuela en la referencia de
  clonado. Aísla vocal para el clon, **conserva el fondo** para la mezcla final.
- **Lip-sync depende del audio final**: corre el lip-sync **después** del time-stretch, sobre el wav definitivo.
  Si estiras después, rompes el sync que ya calculaste.
- **Acumulación de error**: STT 95% × MT 90% × clon 90% × sync 90% ≈ 70% global. Valida en cada eslabón, no
  solo al final.
- **Referencia de clonado limpia**: 3-10s de un segmento sin música ni solapamiento; una mala ref domina todo
  el doblaje (ver [[05-tts-voice-cloning-2026]]).

## Orquestación y costo
Es una cadena serial → encadena como jobs, no un monolito (un eslabón que cae no debe reprocesar todo).
GPU media (12-24GB) alcanza; el lip-sync suele ser el cuello (frame a frame). Para video largo, segmenta por
escena y paraleliza. Mantén workers calientes por eslabón si haces volumen.

Cruza con [[134-whisper-faster-whisperx-self-hosting]] y [[146-lipsync-a-fondo-wav2lip-musetalk-latentsync]].

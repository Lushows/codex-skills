# 221 · Watermarking de audio generado (AudioSeal) y procedencia

> Generas voz clonada para avatares. Eso obliga a marcarla: para detectar tu propio output, defenderte
> de mal uso ("yo no dije eso") y cumplir reglas de IA generativa. La marca va en el audio, no en metadatos.

## Por qué marcar el audio, no solo el contenedor
Metadatos (ID3, tags de archivo) se borran al recortar, recomprimir o re-subir. Un **watermark de señal**
vive en la forma de onda: sobrevive a edición y permite responder "¿esto lo generó mi sistema?". Es la
capa de audio del problema de procedencia que ya cubre el lado de imagen/video ([[38-watermarking-procedencia]]).

## AudioSeal — el estándar open (Meta, 2026)
Marca de agua **localizada** para voz generada por IA. Arquitectura generador/detector entrenada en
conjunto:
- **Detección a nivel de muestra** (1/16000 s): no solo dice "marcado sí/no", sino **qué tramos** lo
  están — detecta si un clip real fue parcheado con un trozo de voz clonada.
- **Robustez SOTA** a manipulaciones reales: filtrado, ruido, compresión (MP3/Opus), resampling.
- **Detector de un solo paso**, hasta dos órdenes de magnitud más rápido que WavMark → viable en
  producción y streaming (v0.2+ soporta streaming).
- Imperceptible por evaluación humana y automática (pérdida perceptual con masking auditivo).

```python
from audioseal import AudioSeal
gen = AudioSeal.load_generator("audioseal_wm_16bits")
det = AudioSeal.load_detector("audioseal_detector_16bits")
wm = gen(audio, sample_rate=16000, alpha=1.0)        # audio + marca (16 bits de mensaje)
audio_marcado = audio + wm
result, message = det.detect_watermark(audio_marcado, sample_rate=16000)
# result: prob por muestra de estar marcado; message: los 16 bits embebidos (tu ID/clave)
```
Los **16 bits** sirven como payload: codifica un id de versión/cliente para rastrear el origen.

## Dónde insertarlo en el pipeline
**Último paso**, justo antes de entregar/mux con el video: TTS/clon ([[116-voice-clone-produccion-retencion]])
→ AudioSeal → muxear con ffmpeg ([[142-ffmpeg-avatar-video-a-fondo]]). Después solo recompresión normal,
que el watermark aguanta.

## Combinar con procedencia firmada (C2PA)
Watermark de señal y manifiesto firmado son **complementarios**:
- **AudioSeal** = robusto, sobrevive edición, detectable sin metadatos, pero payload chico (16 bits).
- **C2PA** ([[266-c2pa-watermark-implementacion]]) = manifiesto criptográfico con autor, herramienta,
  cadena de edición; rico pero **se pierde** si quitan metadatos.
Producción seria usa ambos: C2PA para la procedencia declarada y firmada, AudioSeal como respaldo que
persiste cuando el manifiesto se cae.

## Detalles que muerden
- **No es DRM ni cifrado**: un adversario con esfuerzo puede degradar la marca; es disuasión y trazabilidad,
  no candado. Sirve para detección a escala, no para impedir copia.
- **alpha (fuerza)**: subirlo mejora robustez pero arriesga audibilidad en voz limpia; el default es
  buen punto. Verifica A/B que no introduzca artefactos en tu timbre.
- **Sample rate**: modelos a 16 kHz; si entregas a 48k, marca en el dominio correcto del pipeline.
- **Cadena de detección**: guarda el mapping bits→cliente en tu lado; el watermark solo lleva el id,
  no la identidad.
- **Cumplimiento**: marcar IA generativa es cada vez requisito (UE AI Act y similares) — trátalo como
  parte del entregable, no opcional.

Cruza con [[38-watermarking-procedencia]] y [[266-c2pa-watermark-implementacion]].

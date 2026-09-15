# 214 · Síntesis de canto (SVS): pitch, melodía y la voz que canta

> El TTS habla; el canto exige **pitch controlado por una partitura**. Son dos problemas distintos:
> *sintetizar* canto desde una melodía (SVS) vs *convertir* una voz cantada en otra (SVC). No los mezcles.

## SVS ≠ SVC (la distinción que define todo)
| | **SVS** (Singing Voice Synthesis) | **SVC** (Singing Voice Conversion) |
|---|---|---|
| Entrada | Letra + partitura (MIDI/F0) | Audio cantado existente |
| Genera | Canto desde cero | Re-timbra un canto ya grabado |
| Modelo típico | **DiffSinger**, DiTSinger, VISinger | **RVC** |
| Necesitas | Score + alineación fonema-nota | Voz fuente + modelo del timbre destino |

Si tienes la melodía pero no a quién la cante → SVS. Si tienes un cantante guía y quieres otro timbre → SVC.

## DiffSinger (el caballo de batalla SVS, [verificado])
Modelo acústico por **diffusion** (*shallow diffusion mechanism*): convierte ruido en mel-espectrograma
condicionado por la partitura, iterativamente. Open-source PyTorch (fork **openvpi** = el production-ready).
- **Entradas**: letra + pitch (F0) **o** letra + MIDI. Necesita **alineación fonema↔nota** precisa.
- **Salida**: mel a 44.1kHz → vocoder (HiFi-GAN/NSF) → wav. Fidelidad alta, features production.
- **Frontends**: OpenUTAU genera el score/alineación y llama a DiffSinger como motor.

Alternativas SVS 2026: **DiTSinger** (Diffusion Transformer + alineación implícita, escala mejor),
**RDSinger** (reference-based), **Prompt-Singer** (control por lenguaje natural). DiffSinger sigue siendo
el default por madurez de tooling.

## RVC para canto (SVC, [verificado])
RVC (Retrieval-based Voice Conversion) convierte canto **preservando el pitch** de la voz fuente. No
sintetiza melodía: necesita un canto guía. Flujo típico de cover: cantas tú (o usas un acapella) → RVC
re-timbra al modelo objetivo. **Demucs** separa voz/instrumental antes y remezcla después.

## Pipeline de un cover end-to-end
```
1. Separación: Demucs → acapella + instrumental
2a. SVC: acapella → RVC (modelo timbre destino)        ← si ya hay un cantante guía
2b. SVS: MIDI+letra → DiffSinger                        ← si solo hay partitura, sin cantante
3. Vocoder (si SVS) → wav 44.1kHz
4. Mezcla: voz + instrumental, alinear y masterizar
```

## Detalles que muerden
- **Alineación fonema-nota es el 80% del trabajo SVS**: un MIDI mal alineado produce canto que "patina"
  sobre las sílabas. OpenUTAU/labels manuales para piezas serias.
- **F0/pitch tracking sucio = artefactos**: en SVC, un extractor de pitch (RMVPE/CREPE) malo mete gallos.
  Usa RMVPE; es el estándar actual en RVC.
- **Vibrato y notas sostenidas** exponen al vocoder: HiFi-GAN base a veces zumba en sostenidos largos →
  NSF-HiFiGAN (pitch-aware) lo arregla.
- **Dataset de voz para entrenar RVC**: 10-30 min de canto limpio del timbre destino. Hablado no basta para
  cantar bien (rango y técnica distintos).
- **Sample rate**: trabaja a 44.1kHz de punta a punta; mezclar 22kHz (TTS hablado) con 44.1 suena turbio.

## Sizing
DiffSinger/RVC corren en GPU 8-12GB para inferencia. Entrenar un modelo RVC: una GPU consumer (12-24GB) y
horas, no días. SVS no necesita reentrenar si usas un modelo de voz ya publicado.

Cruza con [[135-rvc-voice-conversion-self-hosting]].

# 165 · Moderar el OUTPUT generado (NSFW, deepfake, likeness, legal)

> El modelo que generó el avatar NO te protege: tú sirves el MP4, tú respondes por él. Una pasada de
> moderación sobre la SALIDA (no solo la entrada) es barata, rápida y obligatoria desde ago-2026 (EU AI Act).

## Qué hay que clasificar en la salida
1. **NSFW** — desnudez/sexual no pedido (modelo derivó, o el usuario subió input adversarial).
2. **Deepfake de persona real sin consentimiento** — la cara de entrada es de alguien que no autorizó.
3. **Likeness / figura pública** — generar a un famoso/político (riesgo legal + reputacional alto).
4. **Marca de procedencia faltante** — salida sin C2PA = incumplimiento legal en la UE.

## NSFW de imagen/video: clasificadores open
- **Falconsai/nsfw_image_detection** (ViT, HF, 55M+ descargas): binario normal/nsfw, 224×224, ~98% en su set, ~milisegundos en GPU. *Gate rápido* sí/no. Verificado jun-2026.
- **NudeNet v3** (ONNX runtime, sin TensorFlow → cold start ligero): detección por **regiones del cuerpo** (cubierto vs expuesto) con bounding boxes. Úsalo si necesitas granularidad ("torso expuesto") en vez de un sí/no.
- **Video** = no clasifiques cada frame. Muestrea **1 frame cada 0.5-1s** (FFmpeg `-vf fps=2`), clasifica los keyframes, agrega: si **cualquier** frame supera el umbral → marca el video. 60s a 2fps = 120 imágenes ≈ <1s en T4.
```python
from transformers import pipeline
clf = pipeline("image-classification", model="Falconsai/nsfw_image_detection")
frames = sample_frames(mp4, fps=2)
nsfw = max(clf(f)[0]["score"] for f in frames if clf(f)[0]["label"]=="nsfw")
if nsfw > 0.85: block(reason="nsfw")
```

## Deepfake / cara de persona real
Dos preguntas distintas:
- **¿La SALIDA parece real (riesgo de pasar por video auténtico)?** Detectores open: **FaceForensics++** (benchmark+modelos), ensembles tipo **DeepSafe**, backbones **EfficientNet** entrenados en FF++/Celeb-DF/DFDC. Verificado jun-2026. Útil para auditar, no infalible (carrera armamentista).
- **¿La cara de ENTRADA es una persona real sin consentimiento?** Eso NO lo resuelve un clasificador: necesitas **gate de consentimiento** en el producto (el usuario declara/firma que tiene derecho sobre la imagen) + opcional match contra una lista de figuras públicas. La detección es defensa en profundidad, no la política.

## Consentimiento / likeness (proceso, no modelo)
- Checkbox + registro auditable: "declaro que tengo derecho a usar esta imagen/voz". Guarda timestamp + hash de la imagen.
- Lista de bloqueo de figuras públicas (face-match contra un set curado) → revisión manual antes de servir.
- Voz: igual de sensible que la cara (clonación). Cruza con [[116-voice-clone-produccion-retencion]] para retención/consentimiento de la muestra de voz.

## Bloquear vs marcar (severidad)
| Veredicto | Acción |
|---|---|
| NSFW alto / deepfake de figura pública | **Bloquear**, no entregar, log + alerta |
| NSFW borderline / score medio | **Marcar** para revisión humana, cuarentena |
| Limpio | Entregar **con credencial de procedencia** (C2PA) |

## Procedencia obligatoria: C2PA + EU AI Act
El **EU AI Act Art. 50** es plenamente exigible **2 ago 2026**: la salida de IA generativa debe marcarse en formato **legible por máquina** como artificial. El mecanismo nombrado por la Comisión es **C2PA Content Credentials** (manifiesto firmado: qué sistema generó, cuándo, quién firma); para video cubre MP4/MOV. Multas hasta **15M EUR o 3% facturación global**. Embebe el manifiesto C2PA al exportar el MP4 + watermark opcional. Detalle en [[38-watermarking-procedencia]] y obligaciones en [[39-legal-ia-generativa]].

## Costo de la pasada de moderación
- NSFW (ViT, 120 frames/video en GPU): **<1s**, fracción de centavo. Despreciable vs los ~$1.25-2 del render.
- Deepfake-detect (EfficientNet por frame muestreado): segundos, también barato.
- **Dónde correrla:** en el mismo worker GPU justo tras el render (modelo ya caliente, sin cold-start extra) o en un micro-paso CPU/T4 barato del pipeline async. NO en la ruta síncrona del usuario.
- **Fail-closed:** si el clasificador crashea/timeout → trata como "no verificado" y cuarentena, no como "limpio".

## Gotchas
1. Moderar **solo la entrada** no basta: el modelo puede derivar NSFW desde input limpio.
2. Umbrales por **percentil de tu propio tráfico**, no el default del paper — calibra con casos reales y revisa falsos positivos (arte/médico).
3. Clasificar **cada frame** es derroche; muestrea keyframes.
4. Los detectores de deepfake **envejecen** (modelos nuevos los evaden) — versiónalos y reentrena.
5. C2PA **se puede strippear** (re-encode borra el manifiesto) → no es DRM; complementa con watermark robusto. Cruza con [[37-moderacion-safety-imagen]].

**Fuentes:** huggingface.co/Falconsai/nsfw_image_detection · github.com/notAI-tech/NudeNet · github.com/siddharthksah/DeepSafe (FF++) · c2paviewer.com/articles/eu-ai-act-content-credentials.

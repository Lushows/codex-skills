# 205 · Vídeo reactivo al audio (visualizers, Deforum, beat-sync)

> El movimiento del vídeo lo dirige una señal de audio: bajo→pulso, agudo→detalle, beat→cambio de escena.
> No es lip-sync (eso es [[202-fullbody-talking-avatar]]); aquí el audio modula **parámetros de generación**.

## La idea de fondo
Extraes features del audio (amplitud, bandas de frecuencia, beats) y las **mapeas a parámetros** de un
generador frame-a-frame: fuerza de denoise, peso de IPAdapter/ControlNet, zoom/pan de Deforum, seed-travel.
El audio es la **curva de control**; el modelo de difusión es el render. Toda la magia está en el mapeo.

## El stack en ComfyUI (2026)

| Pieza | Para qué |
|---|---|
| **ComfyUI_Yvann-Nodes** | nodos de reactividad de audio; conecta con IPAdapter/AnimateDiff/ControlNet |
| **Deforum: BeatDetection / BeatDetection v2** | detecta timing de beats → dispara cambios en el beat |
| **Deforum: FrequencyRangeAmplitude** | amplitud por banda (bass/treble) → anima por frecuencia |
| **ComfyUI-AudioReactor** (`tocubed`) | reacción a audio para visualizers/instalaciones |
| **AnimateDiff** (workflows Civitai) | difusión temporal + máscaras de dilatación + ruido beat-synced |

Patrón típico: **bass → escala/pulso**, **treble → detalle/textura**, **beat → cambio de prompt o seed**.

## Dos enfoques
- **Generativo puro** (AnimateDiff/Deforum guiado por audio): nace del ruido, todo el frame reacciona.
  Más psicodélico, menos control de contenido.
- **Vídeo existente + reactividad** (Audioreactive Dancers): tomas un sujeto en vídeo y lo animas/distorsionas
  al beat con ControlNet + máscaras + ruido beat-synced. Conserva contenido, añade pulso.

## Lo que muerde
- **Mapeo audio→param es arte, no fórmula**: normaliza la envolvente (smooth + clamp) o el vídeo
  convulsiona en cada pico. Suaviza con media móvil; deja headroom.
- **Beat-detection falla** en música sin percusión clara → mejor banda de frecuencia + umbral que beat puro.
- **Coherencia temporal**: AnimateDiff da continuidad; Deforum puro (seed-travel) puede saltar. Si quieres
  continuidad de sujeto, ancla con IPAdapter/ControlNet, no sólo seed.
- **Sample-rate y hop**: el análisis de audio debe alinear su hop al **fps del vídeo** (un valor por frame),
  o la reactividad se desfasa del sonido.
- **Coste**: es generación frame-a-frame larga → presupuesta muchos frames. GPU media basta (no necesita 80GB),
  pero el tiempo total escala con la duración de la canción.
- **Render barato primero**: prototipa a baja resolución/fps, valida el mapeo, luego sube y haz super-res
  ([[206-video-superres-temporal]]).

## El mapeo audio→parámetro (donde se gana o se pierde)
```
envolvente cruda → suavizar (media móvil ~3-5 frames) → normalizar [0,1] → clamp con headroom
                → escalar al rango útil del parámetro (p. ej. denoise 0.35–0.6, no 0–1)
```
- **Bass (20-200Hz)** → escala/zoom/pulso del sujeto.
- **Mid/treble** → detalle, fuerza de IPAdapter, textura.
- **Beat (BeatDetection)** → disparo discreto: cambio de prompt, salto de seed, transición de escena.
- Hop del análisis = **1/fps** → exactamente un valor de control por frame; si no, la reactividad se desfasa.

## Sizing y serving
- Es generación **frame-a-frame larga**: el coste escala con la **duración de la canción**, no con la
  resolución de un frame. Una GPU media (no 80GB) basta; lo caro es el número de frames.
- Prototipa a 12-15fps baja resolución, valida el mapeo (que el pulso pegue al sonido), luego sube fps/res
  y haz super-res ([[206-video-superres-temporal]]). Cruza con [[30-finops-gpu]].
- ComfyUI como motor; workflow versionado. Pesos (AnimateDiff/ControlNet/IPAdapter) cabe hornearlos o
  en volumen según tamaño ([[113-network-volume-modelos-grandes]]).

## Pipeline
```
audio → análisis (beats + bandas, hop = 1/fps) → suavizar+normalizar → curva por frame
     → ComfyUI (AnimateDiff/Deforum) modulando denoise/IPAdapter/zoom → frames → super-res → mux audio (ffmpeg)
```

Cruza con [[54-musica-sfx-sonido-video]].

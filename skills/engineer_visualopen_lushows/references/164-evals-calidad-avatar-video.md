# 164 · Evals de calidad de avatar/video (¿el cambio mejoró o empeoró?)

> Tras tocar el handler, el prompt, los pasos o la versión del modelo, NO se decide por "se ve bien".
> Se mide contra un golden-set fijo y se compara con el champion. Sin gate, cada commit es una ruleta.

## Las 4 dimensiones que importan en un avatar parlante
1. **Lip-sync** — ¿el labio sigue al audio? (la que más rompe y la que el ojo humano detecta a 1 frame).
2. **Identidad** — ¿la cara generada sigue siendo la persona de la imagen de entrada?
3. **Calidad de video** — nitidez, coherencia temporal, ausencia de flicker/artefactos.
4. **Naturalidad** — gestos, parpadeo, micro-movimiento; el "valle inquietante" no lo atrapa ninguna métrica sola → A/B humano.

## Lip-sync: SyncNet (LSE-C / LSE-D)
El estándar de facto sigue siendo **SyncNet** (2026): **LSE-D** = distancia audio↔labio, *menor* mejor (referencia buena ≈ 6-8); **LSE-C** = confidence, *mayor* mejor. También se reportan como **Sync-C / Sync-D**.
```python
# python run_syncnet.py --videofile out.mp4  →  emite LSE-C, LSE-D
assert lse_d <= BASELINE_LSE_D + 0.5, f"lip-sync regresó: {lse_d}"
assert lse_c >= BASELINE_LSE_C - 0.5
```
*Falla:* SyncNet **no es shift-invariant** → si cambia el crop/alineación de la cara entre runs, el score se mueve sin que el sync cambie. Fija el detector y el crop. Cruza con [[17-evals-modelos-generativos]].

## Identidad: ArcFace cosine
Embeddings de cara con **ArcFace** (`insightface`); coseno entre la cara de entrada y un muestreo de N frames de salida. *Mayor* mejor; >0.6 suele leerse como "misma persona", <0.4 es deriva.
```python
from insightface.app import FaceAnalysis            # buffalo_l
sims = [cos(emb_ref, emb(frame)) for frame in sample_frames(out, every=15)]
id_score = mean(sims); assert id_score >= 0.55, f"perdió identidad: {id_score}"
```
*Falla:* perfil extremo/oclusión baja el coseno sin que haya deriva real → muestrea frames frontales y reporta también el **mínimo** (un dip identifica el segmento malo).

## Calidad de video: FVD + VBench
- **FVD** (Fréchet Video Distance, backbone I3D): coherencia temporal vs un set real, *menor* mejor. Números absolutos NO comparables entre repos (backbone/preproceso) → úsalo solo intra-pipeline.
- **VBench / VBench-2.0** (2026): suite multi-dimensión —Subject/Background Consistency, Aesthetic Quality, Motion Smoothness— con scores por VLM. Útil para coherencia e identidad temporal; ojo: VBench-2.0 **excluye lip-sync de Motion Rationality** (no es evaluable solo visualmente) → el sync se mide aparte con SyncNet. [no verificado: pesos VBench específicos para talking-head; usar dimensiones genéricas].

## A/B humano: el ground truth del release
Las automáticas atrapan **regresiones** barato; los **humanos deciden releases**. Panel A/B ciego: mismo input (imagen+audio+seed), dos outputs (champion vs candidate), el evaluador elige. Computa **Elo / Bradley-Terry** con ≥30-50 pares. Pregunta concreta: "¿cuál tiene mejor sincronía de labios?" separada de "¿cuál se ve más natural?" — promediar dimensiones oculta regresiones puntuales.

## Golden eval set (congelado, versionado)
Un set fijo de **(imagen, audio, prompt, seed)** representativo de tus casos (presentador frontal, perfil, audio corto/largo, distintas marcas). Vive en Git; **nunca se edita en silencio** (invalida la historia). Cada candidato lo corre entero → comparas LSE-D, LSE-C, ArcFace, FVD, VBench frente al champion. Incluye audio largo para verificar segmentación (cruza con [[114-video-segmentado-largo-clip]]).

## Gate automático en CI
```
render golden-set → mide [LSE-D, LSE-C, ArcFace-mean/min, FVD, VBench]
                  → compara vs champion.json
                  → BLOQUEA merge si regresión > umbral en cualquier eje
                  → publica grid HTML/MP4 lado a lado para el reviewer humano
```
Útil para no degradar al "optimizar costo" (`--use_int8`, menos pasos de distill, 480p): el gate dice cuánta calidad costó cada palanca de [[111-longcat-avatar-runpod-produccion]]. El render del golden-set es caro (GPU) → córrelo en `main`/release, no en cada push.

## Gotchas
1. **No optimices contra UNA métrica** (Goodhart): subir LSE-C overfitteando degrada naturalidad. Mira el vector completo.
2. **LSE rompe con cambios de crop/FPS** entre runs — estandariza preproceso (FPS, resolución de cara).
3. **Pocos samples → FVD ruidoso**; fija N y seeds, trackea varianza (un +0.01 puede ser ruido).
4. **ArcFace promedio miente** si un solo segmento se rompió — reporta el mínimo por segmento.
5. **Audio desalineado** (mp3→wav mal normalizado) arruina LSE sin que el modelo tenga culpa — normaliza a WAV 16kHz mono ANTES de medir. Cruza con [[01-audio-avatar-pipeline]].

**Fuentes:** github.com/joonson/syncnet_python (LSE-C/LSE-D) · arxiv.org/html/2503.21755v1 (VBench-2.0) · github.com/deepinsight/insightface (ArcFace) · arxiv.org/pdf/2008.10010.

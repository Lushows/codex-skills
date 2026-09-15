# 76 — VFX y efectos visuales con IA (pipeline híbrido real + generativo)

El VFX moderno no es "generar un clip" — es **integrar** elementos (reales, CG y IA) en un plano que el ojo lea
como UNA fotografía. El núcleo es el **comp pipeline**: capas FG/midground/BG + matte paintings, fusionadas con
blending (`over`, `screen`, `add`), corrección por capa y un *grade* final unificador. **El comp se gana o se pierde
en los bordes y en la luz compartida.** Tools pro: **Nuke** (nodal, estándar de cine), **After Effects**, **DaVinci Fusion**.

## Integración FG/BG y matching
(1) **Edge matching** — el borde hereda el softness y ruido del destino, nunca un borde quirúrgico. (2) **Light wrap**
— la luz del fondo "envuelve" el contorno del FG (anti-cutout). (3) **Grain match** — re-granular el elemento limpio
al ISO del fondo (el grano IA suele ser inexistente/plástico → delata el plano). (4) Black/white point y curva
iguales. (5) **Interactive light** — derrames de color del entorno sobre el sujeto. Sin esto = "*floating element*".

## Keying / chroma & rotoscopia
Green/blue screen → *keyer* (Keylight, Primatte, IBK) + **despill** (quita rebote verde en piel/pelo). Sin croma →
**roto** (matte a mano o asistido IA). 2026: **Runway** (seg/roto IA), **Roto Brush 3** de AE (matte propagado),
matting **BiRefNet**/SAM por frame. Pelo, humo y motion blur = el infierno del roto.

## Set extension / sky / screen replacement
Requieren **matchmove/tracking**: 3D camera solve para extensiones, y **planar tracking** con **Mocha** para
superficies planas (cielos, pantallas de teléfono/monitor) manteniendo *parallax* y roll-off del lente. El cielo nuevo respeta dirección/dureza de la luz original.

## Partículas y simulaciones
Tradicional: **Houdini** (Pyro fuego/humo, FLIP agua, RBD debris), **Trapcode Particular** (AE), **EmberGen**
(tiempo real). IA generativa: **Runway/Kling/Pika Pikaffects** (explode/melt/inflate) — FX virales con poco control físico; sirven de *plates* de referencia, no *hero sims*.

## Tools AI VFX 2026
**Runway Gen-4 Aleph** (video-to-video en contexto: añade VFX, cambia clima/estación, relight, genera ángulos nuevos,
add/remove objects — jul-2025) + **Multi-Motion Brush** (hasta 5 regiones con vectores independientes). **Higgsfield**
(presets FX/cámara). **Autodesk Flow Studio** (ex-Wonder Studio): convierte footage en escena CG controlable y exporta
mocap/camera-tracking/alpha/clean-plates/character-passes a Maya/Blender/Unreal vía USD — **el puente real entre IA y
pipeline de cine.** **Viggle/Domo** (motion transfer). **IC-Light** (relight imagen). De-aging/digital makeup con face-pipelines.

## Gotchas
1. **Inconsistencia temporal/flicker** — la IA cambia textura/identidad frame a frame; bloquea con reference frames, EbSynth o re-grain, y comp por encima en vez de regenerar todo.
2. **Oclusión rota** — el elemento generado pasa "por encima" de algo que debería taparlo; necesitas *holdout mattes* (recortes del FG real).
3. **Bordes "cutout"** — falta light wrap + grain match; el #1 delator de comp amateur.
4. **Uncanny en de-aging** — ojos muertos/piel de cera; re-añade grano de piel y micro-movimiento.
5. **Banding/plástico en relight** — el relight IA aplana especulares; preserva los highlights originales como capa `add`.
6. **Drift de identidad en motion transfer** — la cara "muta"; ancla con ID-lock o reemplaza la cara en post.

**Fuentes:** replicate.com/runwayml/gen4-aleph · runwayml.com/changelog · help.wonderdynamics.com/release-notes · github.com/ZhengPeng7/BiRefNet.

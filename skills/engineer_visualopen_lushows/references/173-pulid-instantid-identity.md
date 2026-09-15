# 173 · Identidad preservada en generación (PuLID / InstantID)

> Face-swap pega una cara sobre una imagen existente. Esto es distinto: **generas** una imagen nueva desde texto que *es* esa persona.
> PuLID e InstantID inyectan un embedding de identidad en el difusor → la persona aparece en escenas, estilos y poses que nunca existieron.

## El problema que resuelven
Quieres "mi marca/personaje en una foto de estudio cyberpunk" con **una sola foto de
referencia**, sin entrenar un LoRA por persona (lento, caro, no escala). Estos métodos
son **tuning-free**: un embedding de cara en inferencia y listo.

Diferencia con face-swap (`[[172-face-swap-insightface-reactor]]`):
- **Swap**: parte de una imagen destino que ya existe y reemplaza la cara. No inventa escena.
- **ID-preservation**: el texto inventa toda la escena; la identidad es una *condición* más
  del difusor. Más flexible, más caro (corres el difusor completo cada vez).

## Los dos jugadores

| Método | Base fuerte | Cómo inyecta ID | Trade-off |
|---|---|---|---|
| **InstantID** | SDXL (adapters oficiales) | IdentityNet (ControlNet-like) + IP-Adapter sobre embedding ArcFace | Mejor en SDXL, muy fiel pero puede "pegar" pose/encuadre de la referencia |
| **PuLID** | SDXL y **FLUX** (PuLID-FLUX) | Contrastive alignment + branch Lightning T2I | Más fiel de identidad y menos intrusivo en el prompt; PuLID-FLUX a veces flojea en alineación texto-imagen |

Regla práctica 2026: **SDXL → InstantID** (estabilidad y compatibilidad probada); **FLUX → PuLID-FLUX** (es la vía viva de ID en FLUX). [no verificado: el ranking cambia rápido — métodos como EcomID, InfiniteYou y Omni-ID ya compiten o superan en fidelidad].

## InstantID: detalles que muerden
- Usa **dos** condicionamientos: el embedding facial (IP-Adapter) **y** un keypoints-map de la cara (IdentityNet, vía ControlNet). Si pasas los keypoints de la foto fuente, **clonas su pose** → para variar pose, regenera/omite el keypoints map o usa uno de otra cara.
- Escalas: `ip_adapter_scale` (cuánta identidad) y `controlnet_conditioning_scale` (cuánta estructura). Subir ambos a tope → cara fiel pero rígida y "fotocopiada".

## PuLID: detalles
- Pensado para **alta fidelidad con baja interferencia** en el prompt: la persona aparece
  pero el modelo sigue obedeciendo el texto. Por eso suele ganar cuando quieres escenas
  creativas, no retratos calcados.
- En FLUX-dev, `id_weight` (~0.8-1.0) controla la fuerza; bajarlo recupera libertad creativa
  a costa de parecido.
- El truco del **contrastive alignment**: entrena para que el embedding de ID empuje la cara
  sin contaminar el resto de la imagen → menos "fuga" de la foto de referencia hacia fondo/luz.

## Receta de arranque

| Escenario | Stack | Ajustes iniciales |
|---|---|---|
| Retrato fiel, SDXL | InstantID | `ip_adapter_scale 0.8`, `controlnet 0.8`, keypoints de la fuente |
| Escena creativa, SDXL | InstantID | `ip_adapter_scale 0.6`, `controlnet 0.4`, sin keypoints fuente |
| Escena creativa, FLUX | PuLID-FLUX | `id_weight 0.8`, steps 20-25 |

Ajusta **un** parámetro a la vez. Si la cara sale calcada y rígida, baja escalas; si no se
parece, súbelas o mejora la foto de referencia (frontal, nítida, bien iluminada).

## Fit en el pipeline de serving
- Ambos dependen de **InsightFace** (`antelopev2`/`buffalo_l`) para el embedding → arrastras la misma licencia no-comercial de `[[172-face-swap-insightface-reactor]]`. Cuidado al comercializar.
- VRAM: SDXL+InstantID cabe en 12-16GB; FLUX+PuLID quiere 24GB+ (FLUX es pesado). Cachea checkpoints en el volumen (`[[113-network-volume-modelos-grandes]]`).
- Combina con ControlNet/IP-Adapter de pose/composición para fijar encuadre sin sacrificar identidad: ver `[[139-controlnet-ipadapter-serving-consistencia]]`.

## Identidad consistente de marca
Si el objetivo es un **personaje/embajador recurrente** (no una persona real), estos métodos te dan el ancla de cara estable entre generaciones. Estrategia completa de consistencia en `[[49-consistencia-personaje-marca-ia]]`.

## Riesgo legal — likeness sintético
Generar la cara de una **persona real** sin consentimiento es suplantación, igual que el swap. Aplica etiquetado de contenido sintético y moderación. Un personaje **ficticio** original baja el riesgo, pero verifica que no se parezca a alguien real (celebridad). Ver `[[39-legal-ia-generativa]]` y `[[165-moderacion-safety-output-generado]]`.

Cruza con [[139-controlnet-ipadapter-serving-consistencia]], [[49-consistencia-personaje-marca-ia]], [[172-face-swap-insightface-reactor]] y [[174-ip-adapter-face-deep]].

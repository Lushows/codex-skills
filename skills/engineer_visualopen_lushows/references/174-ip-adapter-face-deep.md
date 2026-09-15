# 174 · IP-Adapter (face / plus / FaceID) a fondo

> IP-Adapter es el "adaptador de prompt por imagen": metes una imagen de referencia y el difusor la usa como condicionamiento, sin reentrenar.
> Las variantes de **cara** son la base sobre la que se montan PuLID/InstantID. Conocer pesos y escalas es la diferencia entre parecido y caricatura.

## La familia (qué usa cada una)

| Variante | Condicionamiento | Para qué | Necesita |
|---|---|---|---|
| IP-Adapter (base) | CLIP image embedding | estilo/objeto general | solo CLIP |
| IP-Adapter Plus | CLIP (patch-level, más detalle) | referencia fiel de textura/forma | CLIP |
| **FaceID** | embedding **ArcFace** (InsightFace) en vez de CLIP | identidad de cara | InsightFace + LoRA |
| **FaceID Plus / Plus v2** | ArcFace **+** CLIP (estructura facial controlable) | identidad + control de forma de cara | InsightFace + LoRA + CLIP |

Clave: FaceID **reemplaza** el embedding CLIP por el de reconocimiento facial → captura *quién es*, no solo *cómo se ve* la foto. Plus v2 reintroduce CLIP de forma **controlable** para gobernar la estructura facial (más/menos parecido estructural).

## Pesos y escalas (lo que de verdad mueve la aguja)
- `set_ip_adapter_scale` (peso del adapter): rango útil **0.5-1.0**. ~0.6 es un buen punto de partida. Demasiado alto = cara fiel pero el prompt deja de mandar (rigidez, artefactos).
- FaceID viene con un **LoRA acompañante**: cárgalo a **0.6-0.8**. Olvidar el LoRA es el error #1 → identidad débil o rara.
- **Plus v2** añade `s_scale` (peso de la estructura CLIP): súbelo si quieres que el parecido incluya forma de cara; bájalo si quieres solo identidad y dejar que el modelo reinterprete.
- SDXL: la versión `faceid-plusv2_sdxl` usa el **mismo** InsightFace que la de SD1.5; cambia el backbone del difusor, no el extractor.

## Receta de arranque (SDXL, parecido fuerte sin matar el prompt)
```
ip_adapter_scale     = 0.6
faceid_lora_weight   = 0.7
plusv2_structure (s) = 0.5   # subir → cara más calcada
steps                = 30, CFG 5-7
```
Ajusta en este orden: 1) LoRA, 2) ip_adapter_scale, 3) s_scale. Cambia uno a la vez.

## Combinar con ControlNet (el combo que usa todo el mundo)
IP-Adapter FaceID fija **quién**; ControlNet (openpose/depth/canny) fija **pose/composición**.
Juntos = misma persona en la postura que tú dictas. Esa es la columna de la consistencia de
personaje. Detalles de serving (orden de carga, conflicto de escalas, VRAM) en
`[[139-controlnet-ipadapter-serving-consistencia]]`.

## Errores comunes (debug rápido)

| Síntoma | Causa probable | Fix |
|---|---|---|
| Identidad débil / no se parece | falta el LoRA de FaceID o peso bajo | cargar LoRA a 0.6-0.8 |
| Cara calcada, prompt ignorado | `ip_adapter_scale` muy alto | bajar a ~0.6 |
| Cara deforme/artefactos | s_scale alto + steps bajos | bajar s_scale, subir steps |
| Embedding falla | InsightFace no detecta la cara fuente | foto frontal, nítida, una sola cara |
| Mezcla dos identidades | varias caras en la referencia | recortar a una cara |

## Versión correcta por backbone
Cada difusor necesita su par de pesos: no mezcles `faceid_sd15` con un checkpoint SDXL.
Para SDXL usa `ip-adapter-faceid-plusv2_sdxl.bin` + su LoRA SDXL. El extractor InsightFace
es el mismo en ambos; lo que cambia es el adapter y el LoRA. Equivocar el par = error de
dimensiones o resultado basura.

## Dónde encaja vs PuLID/InstantID
InstantID **es**, por dentro, un IP-Adapter facial + IdentityNet; PuLID usa su propio alineamiento. FaceID es la opción más ligera y portable (solo adapter + LoRA), buena cuando no quieres el ControlNet extra de InstantID. Comparativa en `[[173-pulid-instantid-identity]]`.

## Costos y licencia
- VRAM: el adapter es barato (cientos de MB); el costo es el difusor base. Cachea adapter+LoRA+InsightFace en el volumen (`[[113-network-volume-modelos-grandes]]`).
- **Licencia**: depende de InsightFace (ArcFace) → no-comercial salvo licencia. Misma trampa que `[[172-face-swap-insightface-reactor]]`.
- **Likeness**: generar caras de personas reales arrastra el riesgo legal de deepfake/suplantación → `[[39-legal-ia-generativa]]`, `[[165-moderacion-safety-output-generado]]`.

Cruza con [[139-controlnet-ipadapter-serving-consistencia]], [[173-pulid-instantid-identity]] y [[172-face-swap-insightface-reactor]].

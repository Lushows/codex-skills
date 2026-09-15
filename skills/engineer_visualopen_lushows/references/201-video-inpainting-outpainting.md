# 201 · Inpaint / outpaint de video (quitar objeto, expandir frame, coherente en el tiempo)

> Borrar un logo de 200 frames o ensanchar un vertical a 16:9 sin parpadeo: el reto no es pintar un
> frame, es que los 200 sean **temporalmente coherentes**. Dos familias resuelven esto distinto.

## El problema central: flicker temporal
Inpaintar frame a frame con un modelo de imagen produce **parpadeo**: cada frame rellena distinto y
el ojo lo ve como hervor. La región editada debe propagarse en el tiempo siguiendo el movimiento
real (flujo óptico) o estar generada por un modelo que entienda temporalidad.

## Dos familias
| Familia | Motor | Fuerte en | Débil en |
|---|---|---|---|
| **Propagación (ProPainter)** | Flujo óptico + transformer disperso, **determinista** | Quitar objeto/logo, completar, outpaint suave; cero flicker | Si lo oculto nunca se ve en NINGÚN frame, no puede inventarlo bien |
| **Generativa (VACE MV2V)** | Difusión Wan enmascarada | Inventar contenido nuevo plausible, edición creativa, expandir mucho | Puede derivar/alucinar; más coste y VRAM |

- **ProPainter**: propaga píxeles reales de otros frames hacia la región borrada vía flujo. Como usa
  info que SÍ existe en el clip, es nítido y sin hervor. Ideal **object/logo removal** y video
  completion. Limitación: si el fondo tras el objeto **nunca** aparece (objeto siempre tapándolo), no
  hay de dónde copiar → ahí necesitas generativo.
- **VACE MV2V** ([[198-vace-control-video-deep]]): máscara + difusión → **genera** lo que falta.
  Cuando hay que inventar (outpaint grande, cambiar un elemento por otro), gana. Riesgo: deriva y
  coste.

## Object removal (receta)
1. **Máscara que sigue el objeto** en todos los frames → SAM2/CoTracker
   ([[190-tracking-cotracker-sam2]]) para propagar la máscara con el movimiento.
2. Dilatar la máscara un poco (sombras/bordes del objeto).
3. ProPainter con la secuencia máscara → relleno propagado.
4. Si quedan zonas sin fuente (fondo nunca visible) → parche generativo VACE en esas regiones.

## Outpainting / cambio de aspect ratio (receta)
1. Crear lienzo mayor (vertical→16:9): el video original centrado, bordes = máscara a rellenar.
2. **ProPainter outpaint** si el movimiento de cámara ya revela algo de esos bordes (paneo).
3. **VACE outpaint** si los bordes son contenido totalmente nuevo (cámara estática) → el modelo lo
   genera coherente con la escena y el prompt.
4. Feather en la unión original↔generado para que no se note la costura.

## Detalles que muerden
- **La máscara es el 80% del trabajo**: máscara que no sigue bien al objeto = halo/fantasma. Invierte
  en buen tracking ([[190-tracking-cotracker-sam2]]) antes de inpaintar.
- **Dilatación y feather**: borde de máscara muy ajustado deja contorno del objeto; muy ancho borra
  fondo bueno. Ajusta + feather temporal.
- **Resolución de ProPainter**: trabaja a resolución reducida por VRAM; sube con upscale temporal
  después, no fuerces full-res de un tirón.
- **Coste**: ProPainter es barato (no difusión). VACE generativo cuesta como una generación normal —
  úsalo solo en las regiones que lo necesiten, no en todo el frame.
- **Clips largos**: ambos heredan límites de ventana → trocear y coser ([[200-video-extension-looping]]).

## Decisión rápida
- ¿El fondo tapado **aparece** en algún frame? → **ProPainter** (nítido, barato, sin flicker).
- ¿Hay que **inventar** contenido nuevo? → **VACE MV2V** (generativo).
- ¿Ambos? → ProPainter primero, VACE solo en huecos imposibles.

Cruza con [[190-tracking-cotracker-sam2]] y [[182-inpaint-outpaint-serving]].

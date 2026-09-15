# 179 · Generación de sombra (contacto/proyectada realista para packshots)

> Un producto recortado sobre fondo limpio sin sombra se ve **flotando** — el tell #1 del compositing.
> La sombra ancla el objeto al plano; generarla bien (suave, con dirección y penumbra) es lo que separa packshot pro de recorte amateur.

## Dos sombras, no una
- **Sombra de contacto** (ambient occlusion): el oscurecimiento JUSTO bajo el objeto donde toca la superficie. Corta, dura, oscura. Da el "está apoyado".
- **Sombra proyectada** (cast shadow): la que el objeto arroja según la luz direccional. Larga, suave, con **penumbra** (borde difuso). Da la dirección y altura de la luz.
Un packshot creíble suele necesitar **ambas**. Falta la de contacto → flota; falta la proyectada → se ve sin luz definida.

## Métodos (2026)
| Enfoque | Cómo | Cuándo |
|---|---|---|
| **Diffusion shadow-gen single-step** | red entrenada en datos sintéticos, predice sombra controlable (dirección/suavidad/intensidad) en 1 step [verificado, arXiv 2412.11972] | producción rápida, control paramétrico |
| **GPSDiffusion** (CVPR 2025) | difusión con **geometry prior** del objeto → sombra físicamente coherente con la forma [verificado] | formas complejas, calidad alta |
| **MultiShadow** | varios objetos insertados, sombras múltiples consistentes vía T2I pre-entrenado [verificado] | escenas con N productos |
| **3D/render** | reconstruir/relight en 3D y rasterizar la sombra | máxima fidelidad, lento y caro |
| **Fake manual** | elipse difuminada bajo el objeto, gaussian blur, baja opacidad | baseline barato, sirve para contacto simple |

El truco clave: los métodos de difusión **bypassean el 3D** — predicen la sombra directo desde la imagen del objeto, sin construir/renderizar geometría [verificado].

## Pipeline
1. **Cutout con alpha** del objeto (matting, [[137-matting-bg-removal-escala]]).
2. **Define la luz**: dirección (acimut), altura/elevación, suavidad (tamaño de fuente → penumbra), intensidad. Debe **coincidir** con la luz del relight ([[177-ic-light-relight-serving]]) o canta.
3. **Genera sombra** en capa separada (no quemada en el objeto) → controlas opacidad/blur post.
4. **Contacto + proyectada**: si el modelo solo da una, añade la de contacto como capa AO oscura corta bajo la base.
5. **Componer** bajo el objeto, sobre el plano. Recorta la sombra al plano (no debe trepar paredes salvo que toque).

## Coherencia luz↔sombra (lo que rompe el realismo)
- La **dirección de la sombra** debe ser opuesta a la fuente de luz del relight. Si IC-Light puso luz desde la izquierda, la sombra cae a la derecha. Mismatch = cerebro detecta fake al instante.
- **Penumbra ∝ tamaño de la fuente**: luz dura (sol, flash) → sombra de borde nítido; softbox/nublado → borde muy difuso. Una sombra dura bajo luz suave es incoherente.
- **Densidad ∝ ambient**: escena muy iluminada → sombra clara/translúcida; estudio negro → sombra densa.
- **Decae con la distancia**: la sombra se ablanda y aclara conforme se aleja del punto de contacto.

## Gotchas
1. **Sombra de contacto ausente** = objeto flotando aunque la proyectada exista; nunca la omitas.
2. **Dirección desalineada con el relight** = el fake más común; sincroniza ambos pasos con el MISMO vector de luz.
3. **Borde uniforme** (mismo blur de la base a la punta) es físicamente imposible — gradúa el blur con la distancia.
4. **Sombra opaca 100%** se ve como mancha; en escena real casi siempre es semitransparente.
5. **Objetos transparentes** (frascos, vidrio) proyectan sombra con cáustica/transmisión, no una silueta sólida — caso difícil, revisa a ojo.
6. **Quemar la sombra en el objeto** te quita control; siempre capa aparte.

Cruza con [[193-product-photography-pipeline]] y [[177-ic-light-relight-serving]].

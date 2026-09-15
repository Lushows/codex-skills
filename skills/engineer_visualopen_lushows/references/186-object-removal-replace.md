# 186 · Quitar y reemplazar objetos (click → SAM → mask → inpaint)

> Quitar un objeto bien es **segmentar exacto + inpaintar el hueco con contexto real**, no borrar.
> El pipeline "Inpaint Anything" (SAM + LaMa/FLUX-Fill) es el estándar; el dilatado del mask es el truco.

## El pipeline canónico (Inpaint Anything, verificado arXiv 2304.06790)
Tres pasos — **click → segment → remove**:
1. **Click / box** sobre el objeto (1-2 puntos o bbox).
2. **SAM** (Segment Anything) genera el mask del objeto desde el click. SAM 2/3 para video y prompting más robusto.
3. **Inpaint** del hueco con **LaMa** (rápido, barato, SOTA en remove "limpio") o **FLUX-Fill/SDXL-inpaint** (mejor en huecos grandes/texturados).

Tres módulos de la familia:
- **Remove Anything** — borra y rellena con contexto (LaMa).
- **Fill Anything** — rellena con contenido nuevo prompteado (AIGC inpaint).
- **Replace Anything** — cambia el fondo manteniendo el objeto (mask invertido).

## LaMa vs modelos de difusión (la decisión clave)
| Caso | Usa | Por qué |
|---|---|---|
| Quitar objeto, fondo simple/repetitivo (cielo, pared, césped) | **LaMa** | rapidísimo, sin VRAM grande, sin alucinar; resuelve por estructura, no genera |
| Hueco grande o textura compleja que requiere "inventar" plausible | **FLUX-Fill / SDXL-inpaint** | genera contenido coherente; LaMa emborrona en huecos grandes |
| Reemplazar por objeto nuevo (no quitar) | **inpaint difusión + prompt** | LaMa no genera contenido dirigido |

Regla: **remove → LaMa primero** (barato, sin alucinar); si emborrona, escala a difusión. Replace/Fill → siempre difusión.

## El truco que decide la calidad: dilatar el mask
- SAM da el mask **ajustado al pixel del objeto**. Si inpaintas ese mask exacto, queda un **halo/fantasma** del objeto (sombra de contacto, borde antialiased, reflejo).
- **Dilata el mask** 8-20px antes de inpaintar para tragarte el borde, la sombra de contacto y el reflejo. Sin dilatación, el objeto "sigue ahí" en silueta.
- Para sombras proyectadas largas, extiende el mask hacia la dirección de la sombra manualmente o con un segundo click.

## Serving (handler de producción)
- Input: `image_url` + (`points` | `bbox` | `mask_url`). Si vienen puntos/bbox → corre SAM server-side; si viene mask → salta SAM.
- **SAM warm en VRAM** (carga es el cuello), inpaint model warm aparte. Dos modelos = sizing de VRAM ([[113-network-volume-modelos-grandes]]).
- Pipeline interno: SAM → dilatar → crop+padding → inpaint → composite-back → color-match (ver [[182-inpaint-outpaint-serving]] para crop/blend).
- Idempotencia por hash(image+mask+model). Devuelve mask usado (debug) + resultado.

## Video: removal temporalmente consistente
- Frame-a-frame con SAM independiente **parpadea** (mask salta entre frames).
- Usa **SAM 2** (segmentación con memoria/tracking) o **CoTracker** para propagar el mask consistente, luego inpaint por frame o un inpainter de video. Ver [[190-tracking-cotracker-sam2]] [no verificado: aún por crear].

## Gotchas
1. **Halo del objeto** — el #1; dilata el mask SIEMPRE. Mask ajustado deja silueta fantasma.
2. **Sombra/reflejo huérfanos** — quitas el objeto pero su sombra queda → se ve sobrenatural. Incluye sombra en el mask.
3. **LaMa en hueco grande emborrona** — escala a difusión; LaMa es para huecos chicos/medios con fondo estructurado.
4. **SAM sobre/sub-segmenta** en objetos con bordes ambiguos (vidrio, pelo) → añade puntos negativos o refina con matting.
5. **Replace que no matchea luz/perspectiva** — el objeto nuevo necesita relight (IC-Light) y match de grano/DoF como cualquier composite ([[60-edicion-imagen-avanzada-ia]] §compositing).
6. **Licencias** — SAM (Apache/research según versión) y los pesos del inpainter: revisa antes de uso comercial ([[39-legal-ia-generativa]]).

Cruza con [[182-inpaint-outpaint-serving]], [[190-tracking-cotracker-sam2]] y [[60-edicion-imagen-avanzada-ia]].

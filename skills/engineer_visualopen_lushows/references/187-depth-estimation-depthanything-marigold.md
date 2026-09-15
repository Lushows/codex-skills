# 187 · Depth estimation: Depth-Anything-v2, Marigold, Depth Pro

> Profundidad monocular: de una sola imagen sacas un mapa de distancia por píxel.
> Es la materia prima de ControlNet-depth, relight, parallax y reconstrucción 3D.

## Qué es y para qué
Un modelo de depth toma RGB → devuelve mapa de profundidad (cada píxel = distancia relativa o métrica).
Usos en producción visual:
- **Control de generación**: depth → ControlNet/T2I-Adapter para fijar geometría de la escena.
- **Relight / compositing**: separar fondo/sujeto, niebla por distancia, sombras coherentes.
- **2.5D / parallax**: animar una foto fija (cámara que orbita) sin modelar 3D.
- **Pre-paso de image-to-3D**: depth + normales alimentan mallas (ver cierre).

## Familias (2026)
| Modelo | Tipo | Fuerte en | Flojo en | Notas |
|---|---|---|---|---|
| **Depth-Anything-v2** | discriminativo (ViT) | robustez, velocidad, escenas complejas | transparentes/reflejos | `S/B/L`; ViT-S 25M params, >10× más rápido que Marigold |
| **Marigold** | generativo (difusión, SD) | detalle fino, bordes, transparentes | lento, pesado (~4B) | difusión → varios pasos; mejor textura de profundidad |
| **Depth Pro** (Apple) | métrico, 1 forward | **métrico absoluto** nítido y rápido | menos ecosistema ControlNet | da metros sin calibrar, alta resolución |

`Depth-Anything-v2-L` marca **97.1% en DA-2K** (matching de pares de profundidad), por encima de
Marigold, GeoWizard, DepthFM, MiDaS. [verificado]

## Relativo vs métrico (la trampa más común)
- **Relativo** (afín-invariante): solo ordena "más cerca/más lejos". Suficiente para ControlNet, parallax.
- **Métrico**: da distancia real en metros. Necesario para 3D real, medición, AR. Depth-Anything tiene
  checkpoints métricos por fine-tuning (indoor/outdoor); Depth Pro lo da nativo.
- Si pides "depth" y obtienes valores 0-1 sin escala → es relativo. No lo trates como metros.

## Decidir cuál usar
- **ControlNet-depth para imagen/video** → Depth-Anything-v2 (rápido, ya integrado en ComfyUI). El detalle
  extra de Marigold rara vez se nota tras pasar por el generador.
- **Bordes finísimos, pelo, transparencias** → Marigold (asume el costo de difusión).
- **Necesitas metros / AR / medir** → Depth Pro o Depth-Anything métrico.

## Ingeniería de serving
- **VRAM**: Depth-Anything-v2-L cabe sobrado en 8-12GB; Marigold pide más por ser SD (≥12-16GB cómodo).
- **Throughput**: Depth-Anything procesa lotes a decenas de fps en Ada; Marigold es por-imagen lento
  (varios pasos de denoise). Para video, Depth-Anything gana por goleada.
- **Coherencia temporal en video**: depth por-frame **parpadea**. Suaviza con flujo óptico (warp del frame
  previo) o usa variantes video-depth. No proceses cada frame aislado y esperes estabilidad.
- **Resolución**: corre a la nativa del modelo y reescala el mapa; subir input no siempre mejora y cuesta VRAM.
- **Formato de salida**: guarda 16-bit (PNG/EXR) si vas a 3D; 8-bit basta para ControlNet visual.

## Receta ComfyUI (ControlNet-depth en imagen)
1. Carga imagen → nodo Depth-Anything-v2 (preprocessor) → mapa de profundidad.
2. Mapa → ControlNet-depth (peso 0.5-0.8) junto al prompt.
3. Si la geometría sale "aplanada", sube peso; si "congela" la creatividad, bájalo.
4. Para batch de video, sustituye el preprocessor por uno con suavizado temporal o aplica warp por flujo.

## Errores que muerden
- Mezclar mapas relativos de frames distintos como si compartieran escala → saltos en video/3D.
- Pasar depth invertido (cerca=oscuro vs cerca=claro) al ControlNet equivocado → geometría espejada.
- Esperar bordes perfectos en transparentes con un modelo discriminativo: ahí Marigold o nada.
- Subir input a 4K esperando más detalle: el modelo procesa a su resolución nativa; solo gastas VRAM.
- Tratar salida 0-1 de Depth-Anything como metros para AR: es relativa, usa el checkpoint métrico o Depth Pro.

Cruza con [[139-controlnet-ipadapter-serving-consistencia]] y [[167-image-to-3d-trellis-hunyuan3d]].

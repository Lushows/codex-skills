# 168 · 3DGS: entrenar splats, render tiempo real, serving web

> 3D Gaussian Splatting captura una escena real (fotos/video) → render free-viewpoint >100 FPS en browser.
> Aquí: entrenar, comprimir (PLY→SPZ/SOG, 10-20×), y servir en WebGL/WebGPU. No es mesh — ver gotcha.

## Qué es (vs lo de [[59-3d-generativo-gaussian-splatting]])
Millones de **gaussianas 3D anisotrópicas** (posición, covarianza/escala, opacidad, color SH) rasterizadas,
no MLP queryado por rayo como NeRF ([[169-nerf-instant-ngp-nerfstudio]]). Explícito → entrena en minutos,
renderiza interactivo. El default 2026 para escenas captadas fotorrealistas.

## Entrenar splats
Necesitas **poses de cámara** (COLMAP/glomap SfM) de 50-200 fotos overlapping con parallax.
```bash
pip install nerfstudio
ns-process-data images --data ./photos --output-dir ./proc   # corre COLMAP
ns-train splatfacto --data ./proc                            # ~7-45 min según escena
ns-export gaussian-splat --load-config <cfg.yml> --output-dir ./export   # → .ply
```
Alternativas: repo original `graphdeco-inria/gaussian-splatting`, **Postshot** (GUI Win), **Brush** (Rust/WGPU, multiplataforma).
Tiempos: 7-45 min típico; investigación CVPR 2026 baja a ~100s con 15× accel `[no verificado en repos estables]`.

## Comprimir antes de servir (obligatorio)
El `.ply` crudo de params es enorme (cientos de MB). Para web/móvil:

| Formato | Reducción | Notas |
|---|---|---|
| **SPZ** (Niantic) | ~10× (250MB→~25MB) | quantización fixed-point + columnas; streaming-friendly |
| **SOG** | ~20× | orden self-organizing + quantize; el más pequeño |
| **KSPLAT** | ~5× | formato del viewer mkkellogg, carga rápida |
| `.splat` | ~3-4× | quantize simple, soporte amplio |

Khronos publicó `KHR_gaussian_splatting` para glTF 2.0 (RC feb-2026, ratificación Q2-2026) → splats dentro de GLB estándar.

## Servir / viewers web
- **@mkkellogg/gaussian-splats-3d** — three.js, maduro, KSPLAT/PLY/SPLAT.
- **Spark** (three.js) y **gsplat.js** — integración con escenas three existentes.
- **Babylon.js** — `GaussianSplattingMesh` nativo.
- **PlayCanvas SuperSplit / SuperSplat** — editor + viewer web, exporta SOG/SPZ.
- **WebGPU** > WebGL para escenas densas (mejor sort + compute); fallback WebGL para soporte universal.
El sort por profundidad de las gaussianas es el cuello de botella en cliente → WebGPU compute o sort en worker.

## Serving en producción (patrón)
1. **Entrenamiento offline** en GPU (job en cola, ver [[04-systems-layer-gateway-queue]] y [[115-async-render-largo-poller-durable]]); produce `.ply`.
2. **Comprimir** a SPZ/SOG en el mismo job → subir a R2/CDN.
3. **Cliente** carga el viewer estático + fetch del SPZ. **Cero GPU server en runtime** — el render es 100% en el navegador del usuario.
4. Edge/CDN para los blobs; el viewer es JS/WASM estático ([[73-edge-computing-wasm]]).
Esto hace 3DGS baratísimo de operar: pagas GPU solo al entrenar, no al ver.

## Gotchas
1. **Los splats NO son meshes** — no hay UV-unwrap, retopo, ni collision-mesh de una nube de gaussianas. Si necesitas asset de juego/CAD, usa image-to-3D mesh ([[167-image-to-3d-trellis-hunyuan3d]]), no splatting crudo.
2. **COLMAP falla** en superficies sin textura/reflectivas/repetitivas → poses basura → reconstrucción basura. Captura mate, bien iluminada, alto overlap, orbitando (parallax), no rotando en el sitio.
3. **Tamaño en cliente** — sin comprimir, un splat tumba el móvil (RAM + sort). Siempre SPZ/SOG antes de browser.
4. **Floaters/artefactos** en zonas poco vistas; recorta el bbox y poda gaussianas de baja opacidad en post.
5. **Escenas dinámicas** (gente, hojas movidas entre fotos) → fantasmas; usa 4D-GS o captura estática.
6. **Licencia** del 3DGS original (INRIA) es non-commercial para investigación; usa implementaciones MIT (gsplat, Brush) para producto comercial.

## Fuentes
docs.nerf.studio · github.com/nerfstudio-project/gsplat · github.com/mkkellogg/GaussianSplats3D ·
github.com/nianticlabs/spz · playcanvas.com/supersplat · khronos.org (KHR_gaussian_splatting).

Cruza con [[59-3d-generativo-gaussian-splatting]], [[73-edge-computing-wasm]] y [[169-nerf-instant-ngp-nerfstudio]].

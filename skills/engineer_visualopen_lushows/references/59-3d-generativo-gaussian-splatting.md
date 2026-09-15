# 59 — 3D generativo (Gaussian Splatting / NeRF / image-to-3D)

## 3D Gaussian Splatting (3DGS) — el default 2026 para escenas captadas fotorrealistas
A diferencia de **NeRF** (MLP implícito queryado por rayo — lento de entrenar/renderizar), 3DGS es **explícito**:
millones de gaussianas 3D anisotrópicas (posición, covarianza/escala, opacidad, color SH) rasterizadas en tiempo
real (>100 FPS). Entrena en minutos vs horas de NeRF, renderiza interactivo en browser. Formato: `.ply` de params, comprimido a **`.splat`**/`.spz` para web.

## Image-to-3D (una imagen → mesh) — la pista más caliente
- **TRELLIS / TRELLIS.2** (Microsoft) — TRELLIS.2-4B usa "O-Voxel" sparse → meshes de producción con **materiales PBR completos** (base color, normal, roughness, metallic, AO). Mejor cuando necesitas topología limpia + PBR.
- **Hunyuan3D 2.1/3.0** (Tencent) — dos etapas (DiT shape + Paint texture); texturas fuertes + PBR.
- **Stable Fast 3D** (Stability) — sub-segundo, menor fidelidad; previews/bulk.
- **TripoSR/Tripo, Rodin (Hyper3D)** — feed-forward rápido + API comercial pulida.

**Text-to-3D:** encadena texto→imagen (Flux) → image-to-3D (le gana a la optimización SDS estilo DreamFusion vieja).

## 3D desde video / muchas fotos
**Fotogrametría** (RealityCapture, Meshroom) = meshes watertight para medición/CAD; **splatting** (Nerfstudio
`splatfacto`, Postshot) = renders fotorrealistas free-viewpoint pero no meshes limpios. Ambos necesitan poses de
cámara de **COLMAP** (SfM) o glomap. Pipeline: 50-200 fotos overlapping → COLMAP → train splat/NeRF.
```bash
pip install nerfstudio
ns-process-data images --data ./photos --output-dir ./proc      # corre COLMAP
ns-train splatfacto --data ./proc
ns-export gaussian-splat --load-config <config.yml> --output-dir ./export
```

## Casos de uso & formatos
Producto 3D para ecommerce (spin/AR try-in-room), avatares 3D, assets AR/VR, sets de producción virtual. **Formatos:**
**GLB** (web/engines), **USDZ** (Apple AR Quick Look), `.ply`/`.splat`/`.spz` (splat viewers).

## Servir en web
Meshes vía **`<model-viewer>`** (web component de Google, GLB+USDZ, botón AR gratis) o **three.js** (`GLTFLoader`).
Splats vía **gsplat.js**, **@mkkellogg/gaussian-splats-3d**, **Spark** (three.js), o **Babylon.js** (GaussianSplattingMesh nativo).

## Gotchas
1. **Los splats NO son meshes** — no puedes UV-unwrap/retopo/collision-mesh una nube de gaussianas; si necesitas asset de juego/CAD, usa image-to-3D mesh, no splatting crudo.
2. **COLMAP falla en superficies sin textura/reflectivas/repetitivas** — poses malas = reconstrucción basura; captura mate, bien iluminado, alto overlap, con parallax (orbita, no rotes en el sitio).
3. **Los `.ply`/`.splat` son enormes** (cientos de MB) — comprime (`.spz`, SOG, sort+quantize) antes de mandar a browser/móvil.
4. **Hallucination del lado trasero** en image-to-3D de una sola vista — el lado no visto es inventado; da multi-view para precisión.
5. **Licencia PBR & VRAM** — TRELLIS.2-4B/Hunyuan3D quieren ~16-24GB; revisa licencias (algunos non-commercial) antes de shippear assets de producto.
6. **Drift USDZ vs GLB** — convierte y *prueba on-device*; la conversión de materiales (emissive, alpha) rompe seguido en AR Quick Look.

**Fuentes:** github.com/microsoft/TRELLIS.2 · github.com/Tencent-Hunyuan/Hunyuan3D-2 · docs.nerf.studio · modelviewer.dev.

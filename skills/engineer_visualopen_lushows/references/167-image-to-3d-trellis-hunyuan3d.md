# 167 · Image/Text-to-3D: TRELLIS, Hunyuan3D-2, TripoSR

> Una imagen (o un prompt) → mesh con topología + textura PBR, en segundos-minutos, self-hosted.
> Profundiza el overview de [[59-3d-generativo-gaussian-splatting]]: aquí van repos exactos, VRAM medida,
> dos-etapas shape→paint, formatos y los gotchas que rompen un asset de producción.

## Por qué image-to-3D y no splatting
Splatting capta una *escena* fotorrealista pero NO da mesh limpio (ver [[168-gaussian-splatting-serving]]).
Para un **objeto** que vas a poner en web/AR/juego con UVs, colisión y materiales editables, necesitas un
generador feed-forward que emita **mesh + PBR**. Eso es esta página.

## Los modelos (junio 2026)

| Modelo | Repo | VRAM (inferencia) | Salida | Licencia |
|---|---|---|---|---|
| **TRELLIS** / TRELLIS.2-4B | `microsoft/TRELLIS` | ~16GB (base) · 24GB+ (4B) | mesh + PBR (O-Voxel sparse) | MIT (código) [no verificado para 4B] |
| **Hunyuan3D-2.1** | `Tencent-Hunyuan/Hunyuan3D-2.1` | **10GB shape · 21GB paint · 29GB ambos** | mesh + PBR (albedo/normal/rough/metallic) | Tencent Community (comercial OK, no redistribuir pesos) |
| **Hunyuan3D-2.5** | idem 2.x | 24GB+ [no verificado] | PBR ultra-detalle (guía normal+ref) | Tencent Community |
| **TripoSR** | `VAST-AI-Research/TripoSR` | ~6GB | mesh sin PBR, sub-segundo | MIT |
| **Stable Fast 3D** | `stabilityai/stable-fast-3d` | ~7GB | mesh + material ligero, <1s | SAI Community (gated) |

**Best fidelidad PBR 2026:** Hunyuan3D-2.1 (texturas/materiales) · **mejor topología+PBR producción:** TRELLIS.2-4B `[~]`.
**Bulk/preview barato:** TripoSR / Stable Fast 3D (feed-forward sub-segundo, calidad menor).

## Pipeline de dos etapas (Hunyuan3D)
1. **Shape** (DiT de difusión sobre latente de forma) → mesh crudo. ~10GB VRAM.
2. **Paint** (Hunyuan3D-Paint): proyección multi-vista simultánea → UV seamless de **albedo, normal,
   roughness, metallic**. ~21GB. Captura micro-detalle (grano de cuero, aluminio cepillado).
```bash
git clone https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1
pip install -r requirements.txt          # + texture/ subpaquete para paint
python examples/image_to_3d.py --image in.png --output out.glb --texture
```
TRELLIS expone `pipeline.run(image)` y luego `outputs['mesh']` / `outputs['gaussian']` (emite ambas reps).

## Text-to-3D
No optimices SDS estilo DreamFusion (lento, artefactos). **Encadena** texto→imagen (Flux, ver
[[02-open-models-catalog-2026]]) → image-to-3D. Más rápido y mejor geometría. Para multi-vista coherente,
genera 4 vistas con un modelo MV y aliméntalas al generador 3D.

## Formatos de salida
- **GLB** — web/engines (three.js, `<model-viewer>`, Unity/Unreal con PBR embebido). Default.
- **OBJ/FBX** — DCC/Unreal; FBX preserva jerarquía de materiales.
- **USDZ** — Apple AR Quick Look (convertir + probar on-device).
- **PLY** — solo geometría/color vértice; no para asset PBR final.
GLB embebe las texturas PBR; OBJ saca mapas como PNG sueltos + `.mtl`.

## VRAM y batch
- Single-objeto cabe en 24GB (RTX 4090 / L4 / A10). 29GB (shape+paint juntos) pide **A100-40GB** o
  partir en dos pasos con offload (ver [[125-diffusers-offloading-memoria]]).
- Para servir en RunPod serverless: hornear pesos en imagen o Network Volume ([[113-network-volume-modelos-grandes]]);
  cold start re-bajando 20-30GB mata la economía ([[112-execution-timeout-cold-start-economics]]).

## Gotchas
1. **Lado trasero alucinado** — de una sola imagen, lo no visto es inventado. Da multi-view o vista trasera para precisión dimensional.
2. **Escala/orientación arbitrarias** — el GLB sale sin unidades reales ni up-axis consistente; normaliza bbox y rota a Y-up en post ([[171-mesh-processing-optimizacion]]).
3. **Topología sucia** — mesh denso, non-manifold, sin UV-seams limpias → casi siempre necesita retopo/decimate antes de juego ([[171-mesh-processing-optimizacion]]).
4. **Licencia ≠ MIT en los buenos** — Hunyuan permite vender assets pero NO redistribuir pesos; revisa antes de shippear el modelo en tu producto.
5. **PBR drift al convertir a USDZ** — emissive/alpha/metallic rompen en AR Quick Look; convierte y prueba en iPhone real.
6. **Transparencia/vidrio/pelo** fallan: estos modelos asumen superficie opaca difusa-especular; objetos translúcidos salen sólidos.

## Fuentes
github.com/microsoft/TRELLIS · github.com/Tencent-Hunyuan/Hunyuan3D-2.1 · arxiv.org/abs/2506.15442 (HY3D-2.1) ·
arxiv.org/abs/2506.16504 (HY3D-2.5) · github.com/VAST-AI-Research/TripoSR.

Cruza con [[59-3d-generativo-gaussian-splatting]], [[02-open-models-catalog-2026]], [[170-texturas-materiales-pbr-gen]] y [[171-mesh-processing-optimizacion]].

# 171 · Post-proceso de mesh: decimate, UV, retopo, export web/game

> El mesh que sale de TRELLIS/Hunyuan/NeRF ([[167-image-to-3d-trellis-hunyuan3d]]) es denso, sucio y a veces
> non-manifold. Antes de web/juego: limpiar → decimar → UV → (retopo) → exportar GLB/USDZ. Aquí el pipeline,
> con comandos Blender/CLI y los gotchas que rompen el asset en el navegador o el engine.

## El problema
Generadores 3D emiten mallas de cientos de miles–millones de tris, con: triángulos degenerados, vértices
duplicados, agujeros, geometría non-manifold, normales invertidas y UVs ausentes o caóticas. Web/móvil
quieren **<100k tris** y UV limpias; un juego quiere topología quad para deformar.

## El pipeline (orden importa)

| Paso | Qué | Herramienta |
|---|---|---|
| 1. Limpiar | merge by distance, borrar loose/degenerados, recalcular normales, tapar agujeros | Blender (`mesh.remove_doubles`, `fill_holes`), MeshLab, **pymeshlab** |
| 2. Decimar | bajar conteo de tris preservando silueta | Blender Decimate, **`meshoptimizer`** (`gltfpack`), Simplygon |
| 3. UV unwrap | generar/limpiar UVs (auto-seams) | Blender Smart UV / **xatlas** (lib) |
| 4. Retopo (opcional) | topología quad limpia para deformación/animación | InstantMeshes / QuadRemesher / Blender Quadriflow |
| 5. Bake | hornear detalle del high-poly al low-poly (normal+AO) | Blender bake, Marmoset, xNormal |
| 6. Export | GLB/USDZ comprimido | **`gltfpack`**, `gltf-transform`, USD tools |

## Comandos concretos
```bash
# Decimar + comprimir GLB en un paso (Draco/meshopt) — ideal web:
gltfpack -i in.glb -o out.glb -cc          # -cc = meshopt compress, reduce tris pesados
# Pipeline programable de geometría:
gltf-transform optimize in.glb out.glb --compress draco --texture-compress webp
# UV atlas sin GUI:
python -c "import xatlas, trimesh; m=trimesh.load('in.obj'); \
  vm,idx,uv=xatlas.parametrize(m.vertices,m.faces); ..."
# Limpieza batch headless (pymeshlab):
python -c "import pymeshlab as ml; ms=ml.MeshSet(); ms.load_new_mesh('in.obj'); \
  ms.meshing_remove_duplicate_vertices(); ms.meshing_remove_unreferenced_vertices(); \
  ms.meshing_repair_non_manifold_edges(); \
  ms.meshing_decimation_quadric_edge_collapse(targetfacenum=50000); ms.save_current_mesh('out.glb')"
```
Blender headless para retopo/bake: `blender -b -P script.py` (sin GUI, scriptable en el job GPU/CPU).

## Decimate vs Retopo (no es lo mismo)
- **Decimate** = colapsa tris manteniendo forma; sale triangulado, topología fea pero barata. **Suficiente
  para props estáticos web/AR.**
- **Retopo** = malla quad nueva siguiendo la superficie; cara, pero **necesaria para animar/deformar**
  (personajes, rigging) y para subdivisión limpia. Quadriflow/InstantMeshes automatizan; QuadRemesher (paga) mejor.

## Targets por destino

| Destino | Tris | UV | Formato | Notas |
|---|---|---|---|---|
| Web `<model-viewer>` / three.js | 20-100k | sí | **GLB + meshopt/Draco** | comprime texturas a WebP/KTX2 |
| AR Quick Look (iOS) | <50k | sí | **USDZ** | probar on-device; materiales rompen seguido |
| Juego (estático) | 5-50k | sí | GLB/FBX | normal-bake del high-poly |
| Juego (animado) | retopo quad | sí | FBX/glTF skinned | rigging necesita topología limpia |

## Gotchas
1. **UV antes de bake, decimate antes de UV** — decimar después del UV invalida las coords; respeta el orden.
2. **Non-manifold rompe bake/booleans** — repara aristas non-manifold antes de hornear normales o salen artefactos negros.
3. **Normales invertidas** — generadores 3D a veces dan caras volteadas → se ven huecas/negras; `recalculate outside`.
4. **Texturas dominan el peso, no la geometría** — un GLB de 100k tris pesa menos que sus texturas 4K; comprime a **KTX2/Basis** o WebP, no solo Draco la malla.
5. **Draco vs meshopt** — Draco comprime más la geometría pero descomprime más lento en cliente; **meshopt (`-cc`)** suele ser mejor balance para web. KTX2 para texturas en ambos.
6. **USDZ material drift** — emissive/alpha/metallic se desvían al convertir GLB→USDZ; convierte y prueba en iPhone real.
7. **Escala/up-axis** — normaliza bbox y rota a Y-up (glTF) o Y-up/Z-up según engine antes de exportar; los generadores dan escala arbitraria ([[167-image-to-3d-trellis-hunyuan3d]]).
8. **gltfpack tira animaciones/extensiones raras** — verifica que no borró skinning/morph targets si el asset los tenía.

## Automatizar en el job
Todo esto es headless (pymeshlab, gltf-transform, blender -b) → mételo al final del job de generación 3D
en la cola GPU ([[115-async-render-largo-poller-durable]], [[04-systems-layer-gateway-queue]]) y sube el GLB
optimizado a R2/CDN listo para el viewer.

## Fuentes
github.com/zeux/meshoptimizer (gltfpack) · github.com/donmccurdy/glTF-Transform ·
github.com/jpcy/xatlas · github.com/cnr-isti-vclab/PyMeshLab · docs.blender.org (bake/decimate) · github.com/wjakob/instant-meshes.

Cruza con [[167-image-to-3d-trellis-hunyuan3d]] y [[170-texturas-materiales-pbr-gen]].

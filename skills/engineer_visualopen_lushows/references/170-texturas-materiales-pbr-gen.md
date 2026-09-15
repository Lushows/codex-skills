# 170 · Generar texturas y materiales PBR para 3D

> Un mesh sin material es plástico gris. PBR = stack de mapas (albedo/base-color, normal, roughness,
> metallic, AO, height) que el render usa para luz física. Aquí: generarlos con IA open, sintetizarlos
> desde una foto, y los gotchas de espacios de color que arruinan el look.

## Qué es un material PBR (metallic-roughness)
El workflow estándar (glTF, Unreal, Unity HDRP) usa estos canales:

| Mapa | Qué codifica | Espacio color |
|---|---|---|
| **Base Color / Albedo** | color difuso SIN luz/sombra horneada | **sRGB** |
| **Normal** | perturbación de normales (detalle fino) | **Linear** (tangent-space, OpenGL/DirectX difieren en Y) |
| **Roughness** | rugosidad micro-superficie (0 espejo → 1 mate) | Linear |
| **Metallic** | metal vs dieléctrico (casi binario) | Linear |
| **AO** | oclusión ambiental | Linear |
| **Height/Displacement** | desplazamiento real de geometría | Linear |
Algunos engines empacan ORM (AO+Rough+Metal) en R/G/B de un PNG → menos texturas.

## Caminos para generarlas

### 1. Texturar un mesh existente (texto/imagen → UV)
- **Hunyuan3D-Paint** (`Tencent-Hunyuan/Hunyuan3D-2.1`, subpaquete texture): proyección **multi-vista
  simultánea** → UV seamless de albedo/normal/roughness/metallic. ~21GB VRAM. Mejor PBR open 2026.
- **Hunyuan3D-2.5 material gen**: toma normal map + imagen de referencia como guía → PBR de ultra-detalle.
- **TRELLIS.2-4B**: emite PBR completo (base/normal/rough/metal/AO) junto con el mesh ([[167-image-to-3d-trellis-hunyuan3d]]).
- **TEXTure / Text2Tex** (más viejos, SD-based): proyectan SD sobre el mesh vista a vista; baratos pero con seams.

### 2. Material tileable desde un prompt o una foto (sin mesh)
- **MatGen / generadores de SVBRDF**: una foto frontal de superficie → albedo+normal+rough+metal tileables.
- **CGAN albedo→PBR**: dada solo el albedo, inferir normal/rough/metallic (líneas de investigación, calidad variable).
- Difusión SDXL + ControlNet tiling para base-color tileable, luego derivar normal con métodos clásicos (Sobel→normal) o un modelo SVBRDF.

### 3. Clásico/determinista (sin IA)
Desde una foto de albedo: **height→normal** (`normalmap` de Substance, o `gimp normalmap`, o numpy gradient),
AO por bake en Blender. Barato, predecible, sin alucinación.

## Pipeline típico (mesh generado → material en engine)
```
mesh (GLB de TRELLIS/HY3D)  →  UV unwrap si falta ([[171-mesh-processing-optimizacion]])
   →  Hunyuan3D-Paint  →  {albedo.png(sRGB), normal.png, rough.png, metal.png}
   →  empacar en GLB (texturas embebidas) o ORM packed
   →  probar en <model-viewer> / Babylon / Unreal
```

## Gotchas (los que de verdad rompen el look)
1. **Espacio de color** — albedo es **sRGB**, el resto **linear**. Cargar normal/roughness como sRGB → material lavado o demasiado brillante. Es el bug #1.
2. **Convención Y del normal** — OpenGL (Y+) vs DirectX (Y-). Engine equivocado → relieve invertido (concavidades salen convexas). Voltea el canal G si se ve mal.
3. **Luz horneada en el albedo** — IA que mete sombras/specular en base-color → doble sombra al renderizar. El albedo debe ser plano, delit. Hunyuan separa esto; modelos baratos no.
4. **Seams en UV** — si el unwrap es malo, la proyección multi-vista deja costuras visibles. Buen UV antes de pintar ([[171-mesh-processing-optimizacion]]).
5. **Resolución y tiling** — 2K/4K para hero, 512-1K para props; texturas tileables deben ser seamless (probar en plano repetido).
6. **Metallic casi-binario** — valores intermedios (0.3-0.7) casi nunca son físicos; la IA a veces los emite → corrige a 0 o 1.
7. **VRAM del paint** — 21GB (HY3D) no cabe en 16GB; offload o L4/4090/A100 ([[125-diffusers-offloading-memoria]]).
8. **Licencia** — Hunyuan permite vender el asset, no redistribuir pesos; revisa antes de shippear modelo embebido.

## Servir
GLB embebe las texturas → `<model-viewer>` / three.js `GLTFLoader` aplican PBR automático. Para Unreal/Unity,
exporta OBJ/FBX + mapas sueltos y reconstruye el material graph (ORM packing recomendado).

## Fuentes
arxiv.org/abs/2506.15442 (Hunyuan3D-2.1 PBR) · arxiv.org/abs/2506.16504 (2.5 material) ·
github.com/Tencent-Hunyuan/Hunyuan3D-2.1 · github.com/microsoft/TRELLIS · docs glTF metallic-roughness.

Cruza con [[167-image-to-3d-trellis-hunyuan3d]] y [[171-mesh-processing-optimizacion]].

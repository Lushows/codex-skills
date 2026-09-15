# 169 · NeRF práctico: Instant-NGP, nerfstudio, cuándo NeRF vs 3DGS

> NeRF = campo de radiancia **implícito** (MLP queryado por rayo). En 2026 cedió el default a 3DGS, pero
> sigue ganando en superficies sin textura, reflejos y donde quieres geometría/densidad continua. Cuándo cada uno.

## NeRF en una línea
Una red (MLP) mapea `(x,y,z,θ,φ) → (RGB, densidad)`. Renderizas por **volume rendering** integrando a lo
largo del rayo. Implícito y continuo → suave, pero query por píxel = lento. **Instant-NGP** rompe ese costo.

## Instant-NGP (NVIDIA)
Tres pilares optimizados: **hash grid multirresolución** (encoding posicional aprendido en O(1)), MLP
minúsculo, y rayos/ocupancia con CUDA fusionado. Speedups ~1000× → entrena una escena en **segundos**.
```bash
# Repo NVIDIA (tiny-cuda-nn): build C++/CUDA, GUI propia
git clone --recursive https://github.com/NVlabs/instant-ngp
# o vía nerfstudio (recomendado para pipeline reproducible):
ns-train instant-ngp --data ./proc
```
Necesita GPU NVIDIA con `tiny-cuda-nn` compilado (CUDA toolkit correcto, ver matriz en [[02-open-models-catalog-2026]]).

## nerfstudio (el framework que debes usar)
De UC Berkeley; API modular, soporta NeRF **y** 3DGS bajo el mismo CLI/poses.
- **`nerfacto`** — el método recomendado para escenas reales: mete las mejores ideas de Instant-NGP +
  módulos de calidad (appearance embedding, proposal sampling, distortion). Default si dudas.
- `instant-ngp` — más rápido, menor calidad en escenas grandes/reflejos.
- `tensorf`, `mipnerf` — específicos (mip-NeRF para anti-alias multi-escala).
- `splatfacto` — 3DGS dentro de nerfstudio (ver [[168-gaussian-splatting-serving]]).
Mismo `ns-process-data` (COLMAP) alimenta NeRF o splat → puedes probar ambos sin re-procesar.
```bash
ns-process-data images --data ./photos --output-dir ./proc
ns-train nerfacto --data ./proc
ns-viewer --load-config <cfg.yml>     # viewer web en localhost
ns-export poisson --load-config <cfg.yml>   # NeRF → mesh (marching cubes/poisson)
```

## NeRF vs 3DGS — la tabla de decisión

| Criterio | NeRF (nerfacto) | 3DGS (splatfacto) |
|---|---|---|
| Velocidad entrenamiento | seg-min (Instant-NGP) | min |
| Render runtime | más lento, server-side normalmente | **>100 FPS, corre en browser** |
| Superficies sin textura/reflejos | **mejor** (densidad continua) | floaters, peor |
| Mesh limpio extraíble | sí (marching cubes, calidad media) | **no** (nube de gaussianas) |
| Servir en web barato | difícil (necesita GPU o baking) | **fácil** (viewer estático, ver [[168]]) |
| Edición/relighting | campos de densidad editables, NeRF-Editing | inmaduro |
| Tamaño del asset | pesos MLP pequeños | PLY grande (comprimir SPZ/SOG) |

**Regla:** si vas a **servir interactivo en web/móvil** → 3DGS. Si necesitas **geometría continua, reflejos,
o derivar mesh/densidad** (medición, VFX, relighting) → NeRF. nerfstudio incluso ofrece `nerf2gs2nerf`
(convertir entre ambos) para empezar en uno y exportar al otro.

## Gotchas
1. **Mismo talón de Aquiles que 3DGS: COLMAP.** Poses malas = basura. Captura mate, overlap alto, parallax real.
2. **Instant-NGP atado a CUDA/`tiny-cuda-nn`** — build frágil; fija versión de CUDA toolkit vs driver/torch ([[129-vram-mid-run-oom-hands-on]] para temas de memoria).
3. **NeRF no renderiza en tiempo real out-of-the-box** para servir; baking (MobileNeRF, BakedSDF) o pasa a 3DGS si necesitas FPS en cliente.
4. **Mesh de NeRF es ruidoso** — superficie con burbujas; necesita post (decimate, smooth, retopo, ver [[171-mesh-processing-optimizacion]]).
5. **Escenas grandes/exteriores** → usa `nerfacto` con scene-contraction (unbounded), no NeRF vanilla que asume escena acotada.

## Fuentes
docs.nerf.studio · github.com/nerfstudio-project/nerfstudio · github.com/NVlabs/instant-ngp ·
docs.nerf.studio/nerfology/methods/nerfacto · .../nerf2gs2nerf.

Cruza con [[168-gaussian-splatting-serving]] y [[59-3d-generativo-gaussian-splatting]].

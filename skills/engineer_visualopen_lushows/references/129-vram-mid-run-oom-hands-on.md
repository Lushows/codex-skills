# 129 · VRAM mid-run / OOM hands-on (el OOM que pega a mitad del video)

> El modelo cargó, los primeros pasos corrieron, y reventó en el frame 40 o en el VAE decode.
> Eso NO es "el modelo no cabe" — es un **pico transitorio** o **fragmentación**. Se diagnostica.

## Por qué OOM a mitad del run (no al cargar)
Los pesos son constantes; lo que crece son las **activaciones**, y su pico no está donde crees:
- **VAE decode**: el latente pasa a pixel space al final → pico enorme y breve. Decodificar un batch
  de N a la vez multiplica el pico ~Nx. Causa #1 de OOM "al terminar".
- **Attention**: en video, la secuencia es `frames × H × W` tokens. El mapa de attention escala
  **cuadrático** con la longitud. Más frames o más resolución = pico que aparece recién en los pasos
  de denoise, no al cargar.
- **Más frames / más resolución mid-pipeline**: pasar de 480P a 720P, o de 49 a 81 frames, dispara
  activaciones de forma no lineal. El run "casi cabía" y un frame extra lo tumba.
- **Fragmentación**: tras muchos allocs/frees de tamaños distintos, hay VRAM libre **total** pero no
  un bloque contiguo. `cudaMalloc` falla aunque `nvidia-smi` muestre memoria libre.

## Palanca #1: matar la fragmentación
```bash
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
```
Usa CUDA VMM para crecer/encoger segmentos virtuales en vez de bloques `cudaMalloc` que **nunca se
fusionan**. Caso real reportado: **16.39 GiB → 10.83 GiB** de uso. Es lo primero que pruebas ante un
OOM con "memoria libre disponible". Ponlo **antes** de importar torch (o en el env del worker).

## Palanca #2: tiling/slicing del VAE (mata el pico de decode)
```python
pipe.enable_vae_tiling()    # divide la imagen en tiles solapados → procesa un tile a la vez
pipe.enable_vae_slicing()   # decodifica el batch imagen-por-imagen en vez de todas juntas
```
- **Tiling** reduce el pico por **resolución** (clave en 720P/video). **Slicing** por **batch**.
- Casi siempre elimina el OOM del paso final con coste de tiempo despreciable. Para video, tiling es
  obligatorio en alta resolución.

## Palanca #3: bajar frames / resolución
El recurso más directo: menos `num_frames`, menor `height/width`. Genera a 480P y sube con un
up-scaler aparte; o genera el clip por segmentos (ver framepack). Costo lineal en calidad, salto
grande en VRAM porque ataca el término cuadrático de attention.

## Diagnóstico paso a paso
1. **Mide el pico real**, no el estable:
   ```python
   torch.cuda.reset_peak_memory_stats()
   # ... un run completo, incluido VAE decode ...
   print(torch.cuda.max_memory_allocated() / 1e9, "GB pico")
   print(torch.cuda.memory_summary())   # reservado vs allocated → si hay gap grande = fragmentación
   ```
2. **¿Reservado >> allocated?** → fragmentación → `expandable_segments:True`.
3. **¿El pico salta justo al final?** → VAE → `enable_vae_tiling()` + `enable_vae_slicing()`.
4. **¿El pico crece con frames/res?** → attention → baja frames/res o segmenta el clip.
5. **`empty_cache` NO crea memoria**, solo devuelve bloques cacheados al allocator para que otra
   parte los reuse; no arregla un pico genuino. Útil **entre** etapas (tras descargar el DiT, antes
   del VAE), inútil dentro de un forward.
   ```python
   gc.collect(); torch.cuda.empty_cache()   # entre stages, no dentro del denoise loop
   ```
6. **Aísla el culpable**: corre solo el denoise (sin decode) y solo el decode. Sabrás cuál pico manda.

## Gotchas
- `nvidia-smi` muestra lo **reservado** por PyTorch, no lo realmente usado → no confíes en él para
  medir headroom; usa `max_memory_allocated`.
- `expandable_segments` puede chocar con allocators VMM externos (ej. NCCL `ncclMemAlloc`) en multi-GPU. [no verificado: estado por versión de torch]
- Offload (model/sequential CPU offload) mueve **pesos**, no recorta el **pico de activaciones** del
  VAE — por eso offload + OOM-mid-run conviven; necesitas tiling además del offload.
- Mide siempre tras un run **completo incluido decode**: el OOM vive en el último 5% del pipeline.

Cruza con [[125-diffusers-offloading-memoria]], [[10-profiling-optimizacion-kernels]] y [[123-hunyuan-framepack-video-largo-low-vram]].

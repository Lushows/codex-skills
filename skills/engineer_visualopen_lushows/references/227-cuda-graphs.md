# 227 · CUDA Graphs (matar el overhead de lanzamiento en el loop de difusión)

> Cada paso de denoise lanza cientos de kernels diminutos desde la CPU. A batch chico, la GPU
> espera a la CPU más de lo que computa. CUDA Graphs captura el grafo una vez y lo **reproduce** sin
> volver a pagar el lanzamiento.

## El problema: CPU-bound en el loop de difusión
Un step de UNet/DiT son cientos de kernels (conv, attention, norm, elementwise). La CPU encola cada
uno con ~5-15µs de overhead. Si cada kernel computa pocos µs (batch 1, resolución modesta), la GPU
pasa **ratos ociosa** esperando el siguiente lanzamiento. 30-50 steps × cientos de kernels = ese
overhead se vuelve el cuello de botella. Síntoma: `nvidia-smi` muestra utilización <100% y subir batch
no escala lineal.

## La solución: capturar y reproducir
CUDA Graphs graba toda la secuencia de kernels de **una** iteración en un grafo, y luego la lanza con
**un solo** call. Se elimina el ida-y-vuelta CPU→GPU por kernel.

### Tres APIs en PyTorch
| API | Cuándo |
|---|---|
| `torch.cuda.graph(g)` (context manager) | capturar un bloque a mano; control total |
| `torch.cuda.make_graphed_callables(fn, sample)` | envolver un módulo/callable → drop-in |
| `torch.cuda.CUDAGraph()` crudo | casos raros, ya tienes warmup propio |

### Patrón (warmup obligatorio)
```python
# 1. warmup en un stream lateral (3-5 iters) para que cuDNN/cuBLAS elijan algoritmos
s = torch.cuda.Stream(); s.wait_stream(torch.cuda.current_stream())
with torch.cuda.stream(s):
    for _ in range(3): out = model(static_in)
torch.cuda.current_stream().wait_stream(s)
# 2. capturar
g = torch.cuda.CUDAGraph()
with torch.cuda.graph(g):
    static_out = model(static_in)
# 3. en el loop: copiar entrada al buffer estático y reproducir
for t in steps:
    static_in.copy_(real_in); g.replay(); real_out = static_out.clone()
```

## Reglas que muerden (rompen la captura)
- **Punteros estáticos**: el grafo reproduce las MISMAS direcciones de memoria. Entradas/salidas deben
  vivir en buffers fijos; `copy_()` dentro, nunca reasignar tensores nuevos.
- **Shapes fijos**: un grafo = una forma. Resolución/batch dinámicos ⇒ un grafo por shape (cachéalos).
- **Nada de sincronización ni control-flow dependiente de CPU** dentro de la captura (`.item()`,
  `if tensor>0`, prints). Eso aborta o corrompe.
- **RNG**: usa el generador de CUDA capturable; un `torch.randn` ingenuo se congela al valor capturado.
- **Memoria**: el caching allocator necesita pool estable; primer warmup mal hecho ⇒ "operation would
  make the legacy stream depend on a capturing stream".

## Atajo: deja que `torch.compile` lo haga
`torch.compile(model, mode="reduce-overhead")` activa **CUDAGraph Trees** automáticamente: captura,
maneja el árbol de grafos y los buffers estáticos por ti, tolerando mejor shapes múltiples. Es la ruta
recomendada en 2026 salvo que necesites control manual. [no verificado: % exacto depende del modelo]

## Ganancia esperada
- Mayor beneficio a **batch chico / kernels pequeños** (overhead alto vs compute). NVIDIA reporta hasta
  ~1.58× en Stable Diffusion; en server con muchos requests cortos el alivio de jitter de latencia es
  tan valioso como el throughput.
- Si ya eres compute-bound (batch grande, 4K), la ganancia tiende a cero: no es bala de plata.

Cruza con [[127-torch-compile-tensorrt-difusion]] y [[10-profiling-optimizacion-kernels]].

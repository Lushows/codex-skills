# 11 — TensorRT, ONNX y compilación AOT

El path AOT cambia flexibilidad por latencia: congelas el grafo y (normalmente) las shapes, y construyes un
engine específico del hardware. Pipeline: **PyTorch → ONNX → engine TensorRT**, o sáltate ONNX con **Torch-TensorRT**.

## Export a ONNX
Dos exporters: legacy TorchScript `torch.onnx.export(..., dynamo=False)` y el nuevo **dynamo**
`torch.onnx.export(model, args, "m.onnx", dynamo=True, opset_version=20)` (maneja shapes dinámicas y más ops
limpio — preferido en PyTorch reciente). Usa `dynamic_axes`/`dynamic_shapes` para dejar batch/seq libres.
Valida con `onnx.checker` + `onnxruntime`.

## ONNX Runtime (ORT) — el win más rápido (sin build de engine)
```python
import onnxruntime as ort
sess = ort.InferenceSession("m.onnx",
    providers=["TensorrtExecutionProvider","CUDAExecutionProvider","CPUExecutionProvider"])
```
`CUDAExecutionProvider` = baseline fácil; `TensorrtExecutionProvider` JIT-construye engines TRT para subgrafos
soportados al primer run → activa `trt_engine_cache_enable` para no reconstruir en cada cold start.

## TensorRT propiamente
```bash
trtexec --onnx=m.onnx --saveEngine=m.fp16.plan --fp16 \
        --minShapes=x:1x4x64x64 --optShapes=x:1x4x128x128 --maxShapes=x:2x4x128x128
```
FP16 = default seguro. INT8 necesita cache de calibración; **FP8 conv requiere Hopper/Ada y TRT ≥10.2.**
**Un engine está atado a la arch GPU exacta + versión TRT** — constrúyelo en el SKU target, nunca mandes un
engine Ada a una caja Hopper.

## Cuantización para TRT
Usa **NVIDIA Model Optimizer** (renombrado de "TensorRT Model Optimizer", dic-2025) para PTQ/QAT → INT8/FP8/
NVFP4; su `examples/diffusers` cubre sdxl/sd3/flux-dev/schnell. Adobe reportó ~60% menos latencia de diffusion
con ModelOpt + TRT.

## Torch-TensorRT (quédate en PyTorch)
`trt_model = torch_tensorrt.compile(model, inputs=[...], enabled_precisions={torch.float16})`. Hace fallback a
Torch en ops no soportadas → más tolerante que ONNX→TRT crudo.

## Diffusion-específico
Además de TRT: **Stable-Fast** y **OneDiff** dan speedups con menos fricción para SD/SDXL. En **Blackwell**, el
path torchao (MXFP8/NVFP4) ya es competitivo sin salir de PyTorch.

**Cuándo TRT paga:** latencia-crítica, shapes fijas, alto QPS donde un build de minutos se amortiza.
**Cuándo basta `torch.compile`:** shapes dinámicas, iteración rápida, research, o si un 1.5-2× ya cumple SLA.

## Gotchas
1. Engine = arch GPU + versión TRT específico → reconstruye al cambiar HW/driver o falla en silencio al cargar.
2. Cold start: el 1er build puede tardar minutos → pre-construye y cachea el `.plan`; en TRT-EP fija el cache dir.
3. Shapes dinámicas necesitan profiles min/opt/max explícitos; fuera del rango TRT da error en runtime.
4. INT8 sin datos de calibración representativos → colapso de calidad; valida FID/CLIP, no solo que corra.
5. FP8 conv puede saltarse en group/depthwise convs (usa INT8 ahí); FP8 necesita sm_89+ y TRT ≥10.2.

**Fuentes:** docs.pytorch.org/docs/stable/onnx.html · TensorRT 10.12 release notes · github.com/NVIDIA/Model-Optimizer · developer.nvidia.com/blog (8-bit Stable Diffusion).

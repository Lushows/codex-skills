# 12 — Cuantización con código (hands-on)

Meta: meter pesos grandes en menos VRAM y a menudo ir más rápido, con pérdida de calidad MEDIDA. Elige el
método por hardware y por componente (DiT backbone vs text encoders).

## bitsandbytes (4-bit / 8-bit) vía diffusers/transformers
```python
from diffusers import FluxTransformer2DModel, BitsAndBytesConfig as DiffBnB
nf4 = DiffBnB(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=torch.bfloat16)
transformer = FluxTransformer2DModel.from_pretrained(
    "black-forest-labs/FLUX.1-dev", subfolder="transformer", quantization_config=nf4, torch_dtype=torch.bfloat16)
```
`nf4` = default 4-bit de alta calidad; corre en cualquier CUDA moderna (sin gate FP8). Buen ahorro de VRAM,
speedup modesto. Usa `transformers.BitsAndBytesConfig` igual para los **text encoders T5/CLIP**.

## torchao (nativo PyTorch, compone con torch.compile)
```python
from torchao.quantization import quantize_, int8_weight_only, Float8DynamicActivationFloat8WeightConfig
quantize_(pipe.transformer, int8_weight_only())                           # cualquier GPU, weight-only
quantize_(pipe.transformer, Float8DynamicActivationFloat8WeightConfig())  # sm_89+
pipe.transformer = torch.compile(pipe.transformer, mode="max-autotune")
```
`int8_weight_only` = INT8 storage, computa en bf16 (universal, memoria). `float8dq` (dynamic-act FP8) = el más
rápido **pero requiere compute capability ≥8.9** (4090/Ada, Hopper). En **Blackwell** torchao añade MXFP8/NVFP4.
**Gate FP8:** bajo sm_89 hace fallback o error — checa `torch.cuda.get_device_capability()`.

## GGUF (k-quant, para DiTs de baja VRAM)
En **ComfyUI** usa **city96/ComfyUI-GGUF** (`Unet Loader (GGUF)`); diffusers carga GGUF vía
`GGUFQuantizationConfig`. Combo típico: NF4 UNet + T5XXL GGUF para meter FLUX en 8-12GB.

## AWQ / GPTQ para text encoders
Son LLM-oriented; aplícalos a los encoders T5/LLM vía `transformers` (`AwqConfig`, `GPTQConfig`) — ambos son
calibration-based (activation-aware / 2º orden) → da prompts representativos. El DiT mismo va mejor con bnb/torchao/GGUF.

## Calibración & calidad
Weight-only (`int8_weight_only`, nf4) es data-free. Activation/INT8-static y AWQ/GPTQ necesitan calibración
parecida a producción. **Mide siempre el delta:** CLIP-score/FID vs baseline fp16 en seeds fijos + grid lado a
lado. Quant + `torch.compile` se apilan — cuantiza primero, compila después.

## Gotchas
1. FP8 (`float8*`) requiere sm_89+ en silencio — verifica capability; en Ampere usa INT8/NF4.
2. bnb 4-bit ahorra VRAM pero no siempre acelera (overhead de dequant) — benchmarkea, no asumas.
3. Acoplamiento de versiones diffusers↔torchao rompe (ej. torchao ≥0.16 incompat. reportado) — pinea versiones.
4. Cuantizar el VAE o capas sensibles a atención arruina el output; cuantiza backbone/encoders, deja el VAE en fp16/bf16.
5. Las k-quants GGUF varían muchísimo (Q4_K_S vs Q8_0) — toma la más grande que quepa, no la más chica por default.

**Fuentes:** huggingface.co/docs/diffusers/quantization (torchao, bitsandbytes) · github.com/pytorch/ao · pytorch.org/blog (Blackwell MXFP8/NVFP4) · github.com/city96/ComfyUI-GGUF.

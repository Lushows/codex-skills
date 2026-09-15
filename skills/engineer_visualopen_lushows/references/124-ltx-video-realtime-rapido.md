# 124 · LTX-Video (DiT casi-realtime — el video open MÁS rápido)

> LTX-Video (Lightricks) es el primer DiT de video que genera **más rápido de lo que se ve**: 30fps a
> 1216×704 en tiempo real sobre H100. La jugada cuando priorizas velocidad/costo sobre el detalle de Wan.

## Por qué es rápido
DiT compacto + **VAE de compresión espacio-temporal muy agresiva** → opera sobre un espacio latente
diminuto, así que cada step procesa mucho menos. Las variantes **distilled** colapsan el sampling a
**8 steps recomendados** (o menos) en vez de 40+. Menos latentes × menos steps = casi-realtime.

## Variantes (v0.9.8, lo último — soporta hasta 60s)
| Modelo | VRAM | Resolución | FPS | Steps | Realtime |
|---|---|---|---|---|---|
| ltxv-13b-0.9.8-dev | alta | hasta 4K | 50 | 40+ | no |
| ltxv-13b-0.9.8-distilled | media | hasta 4K | 50 | **8** | sí (H100) |
| **ltxv-2b-0.9.8-distilled** | **baja** | estándar | 30 | **8** | sí (H100) |
| ltxv-13b-0.9.8-dev-fp8 | < full | hasta 4K | 50 | 40+ | sí (H100) |
| ltxv-13b-0.9.8-distilled-fp8 | mínima | hasta 4K | 50 | **8** | sí (H100) |

Default: **1216×704 @30fps**. T2V e I2V, más extensión de video y keyframes. La **2B-distilled** y las
**fp8** son las que caben en GPU modesta (rango consumer 8-16GB [no verificado: cifra exacta de VRAM por
variante no publicada como número único]; la 2B es claramente la de menor footprint).

## Instalación
```bash
git clone https://github.com/Lightricks/LTX-Video.git && cd LTX-Video
python -m venv env && source env/bin/activate
python -m pip install -e .[inference]
```
Pesos en HF: `Lightricks/LTX-Video-0.9.8-13B-distilled`, `...-2b-0.9.8-distilled`, fp8.

## Inferencia
Image-to-video (config elige la variante/steps):
```bash
python inference.py --prompt "PROMPT" --conditioning_media_paths IMAGE.png \
  --conditioning_start_frames 0 --height 704 --width 1216 \
  --num_frames 121 --seed 42 \
  --pipeline_config configs/ltxv-13b-0.9.8-distilled.yaml
```
Extensión de video (clips largos por encadenado): mismo comando con `--conditioning_media_paths VIDEO.mp4`
y `--conditioning_start_frames START`. El `.yaml` define modelo, steps y caché → cambiar de 13B a 2B o a
fp8 es solo cambiar el config. **ComfyUI** soportado oficialmente (ComfyUI-LTXVideo) con workflows de cada variante.

## Trade-off vs Wan / Hunyuan
| Eje | LTX-Video | Wan 2.2 | HunyuanVideo 1.5 |
|---|---|---|---|
| Velocidad | **realtime / 8 steps** | lenta (14B) | media (50 steps; 8-12 distilled) |
| Calidad/detalle/física | buena, menos que Wan | **referencia** | alta |
| VRAM mínima útil | **2B/fp8 → modesta** | 24GB (5B) | 14GB |
| Control fino | keyframes/extensión | **VACE (pose/depth/ref)** | limitado |
| Caso | previews, iteración, volumen, tiempo real | hero shots, control | clips cortos premium |

Regla: **prototipas y escalas volumen con LTX** (barato, rápido, iteración instantánea); subes a Wan/VACE
para el render final con control o calidad cinematográfica. Para video largo low-VRAM → FramePack (123).

## Optimización de velocidad
- Quédate con **distilled (8 steps)**; subir steps casi no mejora y mata el realtime.
- **fp8** recorta VRAM y acelera el GEMM en Ada/Hopper con pérdida marginal.
- Compila el DiT (torch.compile / TensorRT) para exprimir la latencia ya baja → ver compilación AOT.
- VAE de salida y decode pueden dominar a resoluciones altas; baja resolución si necesitas realtime estricto.

Cruza con [[122-wan-video-self-hosting-2026]] y [[11-tensorrt-onnx-compilacion-aot]].

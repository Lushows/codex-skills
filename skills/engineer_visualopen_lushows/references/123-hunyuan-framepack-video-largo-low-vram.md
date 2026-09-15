# 123 · HunyuanVideo + FramePack (video largo con VRAM baja por anclaje de contexto)

> HunyuanVideo da calidad alta con 8.3B params; FramePack rompe el muro de la VRAM para video LARGO:
> 1 minuto a 30fps con **6GB**, porque el costo de memoria deja de crecer con la duración del clip.

## HunyuanVideo 1.5 (lo último, 2026)
Modelo ligero de Tencent: **8.3B params**, T2V + I2V, 480p/720p, hasta **121 frames @24fps** (~5s).
| Item | Valor |
|---|---|
| VRAM mínima | **14GB** con model offloading activo (def.) |
| Sin offload | más rápido si la VRAM sobra (≥~40GB cómodo) |
| Steps | 50 def.; modelo **step-distilled** 8-12 steps (480p I2V, ~75% más rápido); mínimo 4 |
| Optimizaciones | CPU/group offload, **fp8 GEMM**, **sparse attention** |

Instalación + inferencia (repo `Tencent-Hunyuan/HunyuanVideo-1.5`):
```bash
git clone https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5.git && cd HunyuanVideo-1.5
pip install -r requirements.txt
huggingface-cli download tencent/HunyuanVideo-1.5 --local-dir ./ckpts
torchrun --nproc_per_node=1 generate.py --prompt "..." --resolution 480p \
  --num_inference_steps 50 --model_path ./ckpts
```
HunyuanVideo "vanilla" hace clips cortos de altísima calidad. Para **video largo** no escales frames
(VRAM y tiempo crecen) → usa FramePack.

## FramePack — el truco del contexto de tamaño fijo
FramePack (lllyasviel) es predicción de **siguiente frame**: comprime el contexto de frames pasados a una
**longitud constante** según importancia (los frames recientes pesan más, los lejanos se comprimen duro).
Resultado: **mismo costo de VRAM para 1s que para 1 min**. Corre un modelo Hunyuan-13B por debajo.

| Item | Valor |
|---|---|
| VRAM mínima | **6GB** para 60s @30fps (1800 frames), modelo 13B |
| GPUs | RTX **30/40/50** series (fp16/bf16). GTX 10/20 NO soportadas. |
| Descarga | ~30GB de pesos (auto desde HF en el primer run) |
| Velocidad (4090) | 2.5 s/frame sin optimizar; **1.5 s/frame con TeaCache** |
| Longitud | arbitraria (genera progresivamente, frame a frame) |

### Anti-drift (por qué no se degrada)
Generar 1800 frames autoregresivos suele **derivar** (color, identidad, estructura se van). FramePack
ancla cada predicción al contexto comprimido + a los frames clave (anti-drift sampling, generación
bidireccional/desde el final), así el clip largo mantiene coherencia en vez de colapsar.

### Correrlo
```bash
# Linux
git clone https://github.com/lllyasviel/FramePack.git && cd FramePack
pip install -r requirements.txt
python demo_gradio.py        # GUI Gradio; primer arranque baja ~30GB
# Windows: paquete one-click → update.bat → run.bat
```
La GUI toma una **imagen inicial + prompt** y extiende. Empieza mostrando los primeros segundos rápido
porque genera por secciones (feedback temprano, no esperas el clip entero).

## Cuándo usar qué
- **Clip corto (≤5s), máxima calidad, ≥14GB** → HunyuanVideo 1.5 directo (distilled si quieres velocidad).
- **Video LARGO (20s-1min+) con GPU pequeña (6-12GB)** → **FramePack**. Es la única ruta sana low-VRAM
  para minutos de video sin segmentar a mano.
- **Necesitas control/pose/audio-driven** → no es esto; ve a Wan/VACE.

## Gotchas
- FramePack descarga ~30GB la 1ª vez → en serverless **monta Network Volume** o el cold-start sangra.
- 6GB es el **piso**; más VRAM = batches/optimizaciones y mejor velocidad. TeaCache casi duplica el throughput.
- La 13B bajo FramePack es lenta por frame: 1min @30fps = 1800 frames × ~1.5-2.5s → planifica timeout largo.
- HunyuanVideo con offload activo evita OOM pero rebota pesos CPU↔GPU; si tienes VRAM, desactívalo.

Cruza con [[114-video-segmentado-largo-clip]], [[129-vram-mid-run-oom-hands-on]] y [[02-open-models-catalog-2026]].

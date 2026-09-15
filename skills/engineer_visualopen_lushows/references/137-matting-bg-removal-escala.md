# 137 · Matting y bg-removal a escala (packshots y avatar sobre fondo)

> Quitar fondo bien es un problema de **borde** (pelo, transparencias, anti-alias), no de máscara binaria.
> A escala lo que importa: calidad de alpha, batch throughput y que el modelo quepa en VRAM modesta.

## El eje del problema
- **Segmentación** = máscara binaria (objeto/fondo). Barata, bordes duros, aliasing.
- **Matting** = alpha continuo `[0..1]` por píxel → resuelve pelo, humo, vidrio, motion blur.
- Para **packshot** (producto e-commerce) basta una máscara muy fina. Para **avatar/persona** sobre fondo nuevo necesitas matting real o se ve recortado con tijera.

## Modelos imagen (2026)

| Modelo | Tipo | VRAM | Licencia | Cuándo |
|---|---|---|---|---|
| **BiRefNet** | matting alta-res (dicotomous seg) | ~6-8GB @1024 | MIT (pesos) | default calidad de borde, pelo |
| **RMBG-2.0** (BRIA) | matting (arquitectura BiRefNet + dataset propio) | ~6GB | source-available, **comercial requiere licencia BRIA** | mejor en e-commerce/stock; cuidado licencia |
| **InSPyReNet** | salient object @ alta-res | ~4-6GB | MIT | retrato/producto, muy nítido, ligero |
| **SAM3** (Meta, nov-2025) | segmentación promptable (texto/punto/caja) | ~8-12GB | revisar licencia repo `facebookresearch/sam3` [no verificado: términos comerciales] | recorte por prompt, multi-objeto, no da alpha fino → combinar |
| **BEN2 / SDMatte** | matting | ~6GB | revisar por repo | alternativas en ComfyUI-RMBG |

Regla: **BiRefNet** o **InSPyReNet** para producción libre de fricción legal. **RMBG-2.0** solo con licencia BRIA en uso comercial. **SAM3** para *seleccionar qué* recortar; refina el alpha con BiRefNet sobre el bbox.

## Video matting

| Modelo | Mecanismo | Throughput | Notas |
|---|---|---|---|
| **RVM** (Robust Video Matting) | RNN recurrente con memoria temporal | 4K ~76 FPS / HD ~104 FPS en 1080 Ti | sin trimap, persona en tiempo real, estándar de facto |
| BiRefNet **frame-by-frame** | imagen por frame | lento + **flicker** | solo si no hay alternativa; añadir suavizado temporal |

Para avatar/persona en video: **RVM**. Su memoria recurrente evita el parpadeo de bordes que sufre cualquier modelo de imagen aplicado frame a frame. Cruza con [[09-interpolacion-edicion-video-ffmpeg]] para el remux del alpha.

## Comandos

BiRefNet (transformers/diffusers-style):
```python
from transformers import AutoModelForImageSegmentation
m = AutoModelForImageSegmentation.from_pretrained(
    "ZhengPeng7/BiRefNet", trust_remote_code=True).to("cuda").half()
# input 1024x1024, salida = alpha 1 canal -> componer con RGBA
```

RMBG-2.0 (idéntica firma, repo `briaai/RMBG-2.0`). RVM video:
```bash
python inference.py --variant mobilenetv3 \
  --checkpoint rvm_mobilenetv3.pth --device cuda \
  --input-source in.mp4 --output-type video \
  --output-composition out.mp4 --output-alpha alpha.mp4
# variant resnet50 = más calidad, más VRAM
```

Salida con alpha a PNG/WebP RGBA o premultiplicado para componer:
```bash
ffmpeg -i fg.mp4 -i alpha.mp4 -filter_complex "[0][1]alphamerge" -c:v qtrle out.mov
```

## Batch y throughput
- **Resolución manda**: BiRefNet @1024 es el sweet spot; @2048 cuadruplica VRAM/tiempo con poca ganancia salvo bordes de pelo extremos.
- **Half precision** (`.half()`) ≈ −40% VRAM, sin pérdida visible de alpha.
- **Batch por carpeta** de packshots: agrupa por tamaño para no re-padear; un worker A10/L4 procesa cientos/h.
- Pre-redimensiona a la res del modelo, **infiere el alpha en baja, súbelo** (guided filter) y aplícalo sobre la imagen original a tamaño completo → conserva detalle sin pagar VRAM de alta-res.
- Cuello de botella suele ser **I/O y decode**, no la GPU → pipeline con prefetch.

## Calidad de borde (lo que muerde)
- **Halo / fringe de color**: el fondo viejo "sangra" en el borde. Aplica **decontaminación de color** (color decontamination) tras el alpha, o erosiona 1-2px el alpha.
- **Premultiplicado vs straight alpha**: web/compositing esperan straight; algunos motores premultiplican. Mezclar = bordes oscuros o brillantes.
- **Sombra de contacto**: el matting borra la sombra → para packshot sobre blanco, genera sombra sintética aparte o el producto "flota".
- **Vidrio/transparencias**: ningún modelo binario lo resuelve; necesitas matting (BiRefNet) y aún así revisar.

## Pipeline recomendado (avatar/packshot a escala)
1. Imagen → **SAM3** (opcional) selecciona el sujeto por prompt si hay varios objetos.
2. **BiRefNet/InSPyReNet** produce alpha fino sobre el bbox.
3. Decontaminación de color + sombra sintética.
4. Componer RGBA sobre fondo de marca / generado.
5. Video → **RVM** directo (no la cadena de imagen).

Para avatares parlantes recortados sobre fondo, encadena con [[01-audio-avatar-pipeline]] (el matting va *después* del lip-sync). Edición/relleno de fondo avanzado en [[60-edicion-imagen-avanzada-ia]]; catálogo y licencias en [[02-open-models-catalog-2026]].

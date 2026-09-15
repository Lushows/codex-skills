# 260 · Preparar modelos para edge (cuantización + distillation + pruning agresivos)

> Un SDXL crudo NO corre en un móvil. Lo que corre es un modelo destilado a 2 pasos, podado y en INT8/4-bit.
> Edge no es "el mismo modelo más pequeño": es un modelo distinto, optimizado en tres ejes a la vez.

## Las tres palancas (se combinan, no se eligen)
| Palanca | Qué reduce | Técnicas edge | Riesgo |
|---|---|---|---|
| **Step distillation** | nº de pasos (el costo dominante) | LCM, LCM-LoRA, SDXL-Turbo, ADD, BK-SDM, EdgeFusion | calidad/diversidad |
| **Quantization** | bytes por peso / latencia | INT8 estático, INT4/W4A16, VQ 4-bit, FP8 | precisión, ops faltantes |
| **Pruning** | nº de parámetros/capas | structured pruning, layer drop + distill | colapso si agresivo |

## Distillation: la palanca que más rinde en difusión
Difusión paga por **paso**. Pasar de 50 pasos a 1-4 es el mayor ahorro, más que cualquier cuantización.
- **LCM / LCM-LoRA**: LoRA plug-and-play de destilación de pasos, compatible con todo SD/SDXL. ~32 h-A100 de entreno [no verificado]. Te baja a 4-8 pasos sin reentrenar el modelo base.
- **SDXL-Turbo (ADD)**: generación en **1 paso** en tiempo real.
- **BK-SDM → EdgeFusion**: arquitectura podada + LCM como maestro → fotorrealista en **2 pasos, <1s** en edge limitado. El blueprint de referencia para móvil.

## Cuantización: el punto dulce y el muro
- **INT8 estático** (con dataset de calibración) es la base que el NPU acelera; la dinámica suele caer a CPU.
- **VQ (vector quantization) a 4-bit**: modelos **ya destilados** se comprimen a 4 bits **sin pérdida notable** — destilar primero, cuantizar después funciona mucho mejor que al revés.
- **INT4 directo muerde**: conflicto fundamental pruning↔cuantización — el pruning concentra la distribución de parámetros y **estrecha el margen de tolerancia** de la cuantización. Combinar ambos al máximo colapsa.
- Herramientas unificadas: **Intel Neural Compressor**, **NVIDIA ModelOpt** (distill + prune + quant en un pipeline).

## El orden importa (receta)
1. **Destilar** primero (LCM/Turbo) → menos pasos, modelo más estable.
2. **Podar** con re-distillation (layer distillation contigua) para recuperar calidad tras quitar capas.
3. **Cuantizar** al final, INT8 estático o VQ-4bit, con calibración del dominio real.
4. **Medir on-device**: latencia, RAM pico, térmica, y calidad (FID/CLIP) vs el maestro — no solo tamaño.

## Resultados orientativos
- Pruning puede recortar **~60%** de tamaño (500→200 MB) manteniendo ~89.5% de precisión, latencia ~125 ms [no verificado, caso genérico].
- Cuantización ~50% menos memoria a ~91% precisión [íd.].
- EdgeFusion: 2 pasos, <1s en edge. SDXL-Turbo: 1 paso. Ese es el rango objetivo para móvil/browser.

## Gotchas
- **Destilar mata diversidad**: 1-paso da imágenes más "promedio"/menos variadas; valida que el caso de uso lo tolere.
- **Calibración pobre = artefactos**: el dataset de calibración INT8 debe parecerse a la entrada real, no a ImageNet random.
- **Ops INT8 faltantes** en chips viejos → fallback a CPU. Verifica el target ANTES (ver [[258-onnx-tflite-mobile-diffusion]]).
- **No apiles ciegamente**: prune+int4 a la vez suele colapsar; sube agresividad de a un eje y mide.
- **Edge-cloud híbrido** (Hybrid SD): pasos iniciales en cloud, refinamiento en device — opción si la calidad pura on-device no llega.

Cruza con [[128-cuantizacion-difusion-fp8-svdquant-gguf]], [[154-distillation-aceleracion-modelos-propios]] y [[257-coreml-mlx-diffusion-on-device]].

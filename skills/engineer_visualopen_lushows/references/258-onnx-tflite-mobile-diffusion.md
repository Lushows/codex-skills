# 258 · Difusión en Android (ONNX Runtime / TFLite / NNAPI / NPU)

> Android es fragmentación pura: 50 SoCs, 5 NPUs incompatibles, drivers que mienten sobre qué ops aceleran.
> Hacer correr un difusor aquí es 20% modelo y 80% pelear con el execution provider correcto del chip de turno.

## El stack y quién acelera qué
| Capa | Qué es | Acelera en |
|---|---|---|
| **TFLite** | runtime de Google, `.tflite` | NNAPI, GPU delegate, Hexagon, EdgeTPU |
| **ONNX Runtime Mobile** | `.ort`/`.onnx` recortado | NNAPI EP, XNNPACK, QNN EP (Qualcomm) |
| **NNAPI** | API unificada Android → CPU/GPU/NPU | requiere **Android 8.1+**, recomendado 9+ |
| **QNN / Qualcomm AI Engine** | SDK directo al Hexagon/HTP | salta NNAPI, mucho más rápido en Snapdragon |
| **LiteRT** | nuevo nombre de TFLite (2024+) | mismo motor, branding actualizado |

Verdad incómoda: **NNAPI está en declive**. Google empuja delegates directos y los vendors empujan sus SDKs (QNN de Qualcomm, etc.). Para SD real en Snapdragon, el camino rápido es **QNN EP / Qualcomm AI Engine**, no NNAPI genérico.

## ONNX vs TFLite: cuál elegir
- **TFLite** gana en tamaño de binario, soporte de delegates y herramienta de cuantización madura → mejor para empotrar en una app Android pura.
- **ONNX Runtime** gana si ya tienes el modelo en ONNX (Diffusers exporta ahí) y quieres un solo runtime cross-plataforma con desktop. El **QNN EP** desbloquea el HTP de Snapdragon.
- Conversión típica: `PyTorch → ONNX → (onnx2tf / tf → tflite)`. Cada salto puede romper ops no soportadas.

## Cuantización: el muro real
INT8 es obligatorio para caber y para que el NPU lo toque, pero:
- Degrada calidad por aproximación numérica; en UNet de difusión el daño se nota en texturas/coherencia.
- **Operadores faltantes**: chips como Kirin 990/980 o ciertos Snapdragon no implementan varios ops INT8 → el modelo cae a CPU (lentísimo) o falla al cargar.
- **QDQ vs ops por capa**: usa cuantización estática (necesita dataset de calibración) para que el NPU acelere; la dinámica suele quedarse en CPU.

## Números que ponen los pies en la tierra
- SD 1.5/2.1 como **fp16 ONNX** en Snapdragon 8 Gen 1 ≈ **~20 s por paso** [no verificado, foro onnxruntime]. A 20-30 pasos → minutos. Inusable sin destilación.
- `onnxruntime-android` reportadamente **no soporta NNAPI para el grafo SD** → de nuevo, el camino es QNN o GPU delegate.
- Conclusión: en móvil **no corras 30 pasos**. Necesitas modelo destilado a 1-4 pasos (ver [[260-quant-distill-para-edge]]); si no, manda el job a la nube (ver [[113-network-volume-modelos-grandes]]).

## Patrón de despliegue sensato
1. Modelo **destilado** (LCM / SDXL-Turbo / BK-SDM / EdgeFusion) → 1-2 pasos.
2. Cuantizado **INT8 estático** con calibración real.
3. Probar matriz de chips: Snapdragon (QNN), MediaTek (NeuroPilot/NNAPI), Exynos. Fallback a CPU/XNNPACK SIEMPRE presente.
4. Medir latencia, RAM pico y **térmica sostenida**, no solo el primer run (el SoC baja clocks).

## Gotchas
- **Drivers mienten**: NNAPI reporta que soporta un op y luego lo ejecuta en CPU silenciosamente. Perfilar con trazas, no confiar en la API.
- **RAM pico**: el difusor + decoder VAE puede picar GBs; el OS mata la app sin aviso. Descarga submódulos secuencialmente.
- **Fragmentación = matriz de QA**: lo que vuela en un Pixel/Tensor puede no cargar en un MediaTek barato.
- **EdgeFusion** logra fotorrealista text-aligned en **2 pasos, <1s** en edge limitado vía cuant+profiling+deploy on-device — es el tipo de objetivo a perseguir, no SDXL crudo.

Cruza con [[257-coreml-mlx-diffusion-on-device]], [[260-quant-distill-para-edge]] y [[71-mobile-react-native-expo]].

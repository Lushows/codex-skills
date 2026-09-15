# 112 · Execution timeout y economía del cold start (GPU serverless)

> La lección más cara: un timeout mal puesto mata el render a medias **y te lo cobra**.

## El cold start NO es gratis y CUENTA dentro del execution time
En serverless que escala a 0, cada worker frío hace, dentro del mismo run que cobras:
1. **Pull de la imagen Docker** (si no está cacheada en el nodo).
2. **Descarga de pesos** del modelo. LongCat-Avatar baja **~44GB** (int8 + base: tokenizer/text_encoder/vae).
3. **Carga a VRAM** + warmup.
4. Recién ahí empieza la **generación**.

Sin almacenamiento persistente, los pasos 2-3 se repiten **en cada arranque frío** (~8-12 min).
Mátalos con [[113-network-volume-modelos-grandes]].

## Sizing del Execution Timeout (regla)
```
timeout ≥ cold_start + N_segmentos · t_segmento + margen
```
Caso real (LongCat, 480p, 8 pasos distill, A100/H100):
- cold_start ≈ 8-12 min (con re-descarga de 44GB)
- t_segmento ≈ 1.5 min (8 pasos denoising ~11s/paso + VAE + encode)
- 1 min de video = 16-19 segmentos → 24-29 min de generación
- **Total ≈ 35-40 min → pon timeout 2400-3000s.** Con 1200s murió a los **20m 8s** en el segmento 7/16.

> Para ~2 min (35 segmentos) puedes irte a ~60 min → ahí el Network Volume deja de ser opcional.

## Los renders fallidos SÍ se cobran
RunPod factura el tiempo de GPU consumido **hasta el kill**. Un fallo por timeout en el minuto 20 te
cuesta ~$1-2 y no produces nada. Por eso: **mejor sobre-dimensionar el timeout** que arriesgar un kill.

## Cómo confirmar que fue el timeout (no el modelo)
1. Pestaña **Requests** → estado `Failed` + `Execution time` ≈ tu timeout configurado → fue el timeout.
2. **Logs** congelados en un segmento intermedio (ej. "Generating segment 7/16") sin logs de upload.
3. Si `Execution time` << timeout y hay un traceback → es otra cosa (OOM, modelo, input).

## Idle timeout (warm pool) vs cold cada vez
- **Idle Timeout** alto mantiene el worker vivo entre jobs → el 2º+ video del lote salta el cold start.
- Útil si generas **en tanda**. Para videos sueltos y esporádicos, escala a 0 → frío siempre → el
  Network Volume es lo que abarata el frío (no re-baja pesos), no el idle.

## Palancas de costo (ordenadas por impacto, caso LongCat)
| Palanca | Efecto |
|---|---|
| Network Volume (no re-bajar 44GB) | ~35% + render más rápido | 
| Warm pool (idle timeout) para tandas | salta cold start del 2º+ |
| GPU correcto (A100 vs H100) | $/s vs velocidad — medir, no asumir |
| distill + int8 + 480p | ya es el piso de costo de inferencia |
| num_segments (duración) | lineal: menos video = menos $ |

Cruza con [[30-finops-gpu]] y [[19-load-testing-capacity-planning]].

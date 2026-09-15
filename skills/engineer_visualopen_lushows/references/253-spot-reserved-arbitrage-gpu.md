# 253 · Spot vs on-demand vs reserved + arbitraje multi-cloud de GPU

> El mismo H100 cuesta $1.03 o $4.29/h según provider y modalidad de compra. Elegir mal cuadruplica la factura.
> Estrategia = mapear cada job a su modalidad y rutear por precio en vivo, con fallback por capacidad.

## Las tres modalidades (qué pagas, qué arriesgas)
| Modalidad | Descuento vs on-demand | Riesgo | Para qué job |
|---|---|---|---|
| **On-demand** | base (0%) | ninguno | latencia-crítica, baja escala, dev |
| **Spot / community / preemptible** | 60-90% más barato | preempción sin aviso (segundos) | batch, training, renders largos resumibles |
| **Reserved / committed (1-3 años)** | ~45-50% extra sobre on-demand | pagas idle si no usas | baseline predecible 24/7 |

Combinación óptima: **reserved para el baseline, on-demand para el burst, spot para el batch**. Nunca reserves capacidad de pico — pagas idle el 90% del tiempo.

## Precios de referencia (junio 2026, verificar antes de citar)
| GPU | Spot más barato | On-demand típico | Provider caro (on-dem) |
|---|---|---|---|
| H100 SXM | ~$1.03-1.19/h (Spheron/RunPod) | $2.69/h (RunPod) | $4.29/h (Lambda) |
| H100 PCIe | ~$1.49/h | $1.99/h (RunPod) | $3.29/h (Lambda) |
| A100 80GB | ~$0.60/h (Spheron spot) | $1.07-1.39/h | — |
| B200 | — | desde ~$2.12/h | — |

[no verificado caso a caso — los marketplaces fluctúan por hora/región]. Vast.ai usa subasta: precio baja pero la fiabilidad varía host-a-host (ver varianza en [[252-gpu-benchmarking-metodologia]]).

## Arbitraje multi-cloud (el patrón)
1. **Normaliza el precio a $/seg por GPU-clase** (no por nombre): A100-80GB en RunPod vs Vast vs Spheron es el mismo silicio a precio distinto.
2. **Tabla de routing por job**: dev/bajo volumen → API managed por-call (Replicate/fal); steady alto volumen → tu worker por-segundo en el provider más barato con tu GPU en stock.
3. **Fallback en cascada por capacidad/outage**: si el provider A no tiene stock o sube de precio, salta a B. Misma imagen Docker portable (GHCR) → cambias solo el endpoint ([[160-disaster-recovery-cascada-fallback]]).
4. **Cuidado con egress y storage regional**: mover 44GB de pesos entre providers cuesta. Un Network Volume ata el endpoint a una región ([[113-network-volume-modelos-grandes]]) — el arbitraje real es entre regiones donde ya tienes pesos cacheados.

## Spot sin perder el job
- **Checkpoint resumible** a R2/S3 cada N pasos → una preempción cuesta minutos, no el render entero.
- **Drain handler**: RunPod/cloud avisan con segundos de antelación; captura la señal, flush del checkpoint, sal limpio. Detalle de manejo en [[230-spot-preemptible-gpu-handling]].
- **No corras inferencia interactiva en spot**: la preempción mata la SLA. Spot es para lo asíncrono.

## Cuándo conviene committed/reserved
Solo con **carga baseline medida**. Regla: si tu utilización sostenida > ~50-60% de un worker 24/7, el reserved gana sobre on-demand. Por debajo, on-demand + spot. Mide la utilización real antes de comprometerte — no la proyectada.

## Gotchas
1. Reservar capacidad de burst = pagar idle. El error de FinOps más caro.
2. Spot barato en una región sin tu GPU en stock = nunca arranca; elige región por disponibilidad, no por precio nominal.
3. Comparar por nombre de GPU sin ver VRAM/variante (PCIe vs SXM, 40 vs 80GB) infla o desinfla el cálculo.
4. Marketplace (Vast) barato pero host poco fiable → reintentos y varianza de throughput comen el ahorro.

**Fuentes:** spheron.network/blog/gpu-cloud-pricing-comparison-2026 · intuitionlabs.ai/articles/h100-rental-prices-cloud-comparison · buildmvpfast.com/api-costs/gpu · synpixcloud.com/blog/cloud-gpu-pricing-comparison-2026.

Cruza con [[230-spot-preemptible-gpu-handling]], [[132-plataformas-gpu-serverless-comparativa]] y [[30-finops-gpu]].

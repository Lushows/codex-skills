# 30 — FinOps de GPU

## Modelo de costo
`$/job = $/seg × (cold_start_seg + queue_seg + inference_seg)`. En RunPod Serverless se cobra por-segundo de worker
activo *incluyendo cold start y carga del modelo*. Una inferencia de 4 seg con cold start de 40 seg cuesta 44 seg
→ **el cold start domina en jobs cortos.** Trackea `cost = price_per_sec × billed_sec` por request y atribúyelo.

## Trampa del cold start + mitigación
El cold start (pull del contenedor + carga de pesos a VRAM) puede exceder la inferencia. Mitiga con **workers warm/
active** (min replicas calientes — pagas idle pero matas cold starts), **flashboot/snapshot**, **imágenes chicas**
(multi-stage, hornear pesos en imagen o volumen rápido), y **mantener el modelo residente** (cargar 1 vez al
arranque del proceso, no por request). Balancea costo idle del warm-pool vs frecuencia de cold start según tu tráfico.

## Spot / community + checkpointing
RunPod Community / spot = mucho más barato pero **interrumpible**. Haz los jobs largos **resumibles** — checkpoint
de progreso a R2/S3 → una preempción cuesta minutos, no el job entero. No corras inferencia latencia-crítica en
spot; sí batch/training/renders largos.

## Cache & dedup de resultados
Hashea el input (prompt + params + modelo + seed) → cachea el output en R2/Redis. Requests idénticos (común en
estudios multi-marca reusando assets) cuestan **$0** en hit. Dedupea jobs idénticos in-flight (single-flight).

## Right-sizing
Matchea la GPU a la VRAM del modelo, no a la más grande — un modelo que cabe en 24GB (L4/A10) no debe correr en
H100 80GB. Cuantiza (fp8/int8/AWQ/GGUF) para caber en una GPU más chica y barata. Mide headroom de VRAM.

## Arbitraje multi-provider
Precios difieren entre **RunPod / fal / Replicate / Modal / Lambda / Vast.ai**. Replicate/fal cobran por-predicción
(simple, más margen); RunPod/Vast por-segundo (más barato, más ops). Rutea por job: dev/bajo-volumen → API managed
por-call; steady alto-volumen → tu worker por-segundo. Mantén un fallback por capacidad/outage.

## Reserved / active discounts
Workers committed/active (siempre prendidos) tienen menor $/seg que on-demand puro. Vale una vez que tienes carga
baseline predecible; deja el burst en on-demand.

## Atribución por-job + budgets/alertas
Tagea cada job con `brand_id`/`job_type`, graba `billed_sec`, `gpu_type`, `$`, agrega. **Budget alerts** + un
**kill-switch duro** (cap $/día o jobs/hora por marca) — un loop de agente o batch runaway puede gastar miles de la
noche a la mañana (Unbounded Consumption LLM10). Alerta en anomalías de costo-por-job (cold-start storms, retries).

## Showback / chargeback (estudio multi-marca)
**Showback** = reporta el gasto GPU de cada marca para visibilidad; **chargeback** = lo facturas. Con tags por-job
produces un reporte por-marca (compute + storage + egress) y precias el servicio con margen. Trackea unit
economics: $/render, $/minuto-avatar.

## Gotchas
1. Ignorar el cold start en el modelo de costo sub-estima 5-10× en jobs cortos.
2. Spot sin checkpointing → la preempción desperdicia el job entero.
3. Sin tag de costo por-job → no sabes qué marca/feature es no-rentable.
4. Sin kill-switch de gasto → un loop de retry o atacante drena el budget.
5. Workers warm idle facturan 24/7 — dimensiona el warm-pool al tráfico.

**Fuentes:** docs.runpod.io/serverless/pricing · fal.ai/pricing · replicate.com/pricing · finops.org/framework/capabilities (showback vs chargeback).

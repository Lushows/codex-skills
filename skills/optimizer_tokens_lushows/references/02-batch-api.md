# 02 — Batch API (50% descuento, combinable con cache = 95%)

**Impacto:** 50% descuento sobre costo estándar, COMBINABLE con prompt caching.
**Esfuerzo:** Medio (re-arquitectar pipeline para async).
**Cuándo aplicar:** Tareas que NO requieren respuesta inmediata (jobs nocturnos, enrichment masivo, análisis offline).
**Cuándo NO aplicar:** Chat con usuario esperando, respuestas en vivo, cualquier UX síncrona.

## Por qué importa

Stack económico con caching = **hasta 95% ahorro vs llamada estándar.**

| Modo | Costo (Sonnet 4.6) |
|---|---|
| Standard (no cache) | $3.00 / 1M input |
| Standard + cache hit | $0.30 / 1M (90% off) |
| Batch + cache miss | $1.50 / 1M (50% off) |
| **Batch + cache hit** | **$0.15 / 1M (95% off)** |

## Anthropic — Message Batches API

### Crear un batch

```python
from anthropic import Anthropic

client = Anthropic()

batch = client.messages.batches.create(
    requests=[
        {
            "custom_id": "factura_001",
            "params": {
                "model": "claude-sonnet-4-6",
                "max_tokens": 1024,
                "system": [{"type": "text", "text": OCR_SYSTEM, "cache_control": {"type": "ephemeral"}}],
                "messages": [
                    {"role": "user", "content": [
                        {"type": "image", "source": {...}},
                        {"type": "text", "text": "Extrae datos."}
                    ]}
                ]
            }
        },
        {
            "custom_id": "factura_002",
            "params": {...}
        },
        # ... hasta 100,000 requests por batch
    ]
)

print(f"Batch ID: {batch.id}")
print(f"Status: {batch.processing_status}")  # "in_progress"
```

### Poll hasta completar

```python
import time

while True:
    batch = client.messages.batches.retrieve(batch.id)
    if batch.processing_status == "ended":
        break
    print(f"Procesando: {batch.request_counts.processing}, completadas: {batch.request_counts.succeeded}")
    time.sleep(60)

print(f"✅ Batch complete!")
print(f"Succeeded: {batch.request_counts.succeeded}")
print(f"Errored: {batch.request_counts.errored}")
```

### Obtener resultados

```python
for result in client.messages.batches.results(batch.id):
    if result.result.type == "succeeded":
        text = result.result.message.content[0].text
        save_to_db(result.custom_id, text)
    elif result.result.type == "errored":
        log_error(result.custom_id, result.result.error)
    elif result.result.type == "expired":
        retry_queue.add(result.custom_id)
```

### Límites del Batch API Anthropic

- **Max 100,000 requests** por batch
- **Max 256 MB** de payload total
- **SLA: 24 horas** (típicamente < 1 hora)
- **Resultados disponibles 29 días** post-creación
- Soporta TODAS las features de Messages API: vision, tools, caching, structured outputs

## OpenAI — Batch API

Similar shape:

```python
from openai import OpenAI

client = OpenAI()

# 1. Subir archivo JSONL con requests
batch_file = client.files.create(
    file=open("requests.jsonl", "rb"),
    purpose="batch"
)

# 2. Crear batch
batch = client.batches.create(
    input_file_id=batch_file.id,
    endpoint="/v1/chat/completions",
    completion_window="24h"
)

# 3. Poll
while batch.status not in ["completed", "failed", "expired"]:
    batch = client.batches.retrieve(batch.id)
    time.sleep(60)

# 4. Descargar output
output_file = client.files.content(batch.output_file_id)
```

**Mismo descuento: 50% off.**

## Gemini — Batch API

Disponible en Vertex AI con BigQuery como input/output:

```python
from google.cloud import aiplatform

batch_job = aiplatform.BatchPredictionJob.create(
    job_display_name="my_batch",
    model_name="gemini-2.5-pro",
    gcs_source="gs://bucket/input.jsonl",
    gcs_destination_prefix="gs://bucket/output/",
)
```

**Descuento: 50% off** en Gemini API direct, similar en Vertex.

## Cuándo SÍ y cuándo NO usar batch

### ✅ Casos ideales para batch

| Caso | Ejemplo |
|---|---|
| Procesamiento nocturno | "A las 2 AM procesa todas las facturas del día" |
| Enrichment de datos | "Para cada cliente nuevo, generá insight con LLM" |
| Análisis de feedback | "Resume todos los reviews del mes" |
| Generación masiva de contenido | "Para 1000 productos, generá description SEO" |
| Re-evaluación / migration | "Re-procesa todos los docs viejos con el nuevo modelo" |
| Embeddings | "Para 50K artículos, generá embeddings" |

### ❌ Casos NO usar batch

| Caso | Por qué |
|---|---|
| Chatbot WhatsApp en vivo | Usuario espera respuesta inmediata |
| Dashboard interactivo | UX requiere < 5 segundos |
| Asistente de programación | Pair programming requiere realtime |
| Búsqueda con resultados LLM | Usuario en frente esperando |

## Pipeline híbrido: realtime + batch

Patrón común en SaaS:

```
┌─────────────────────────────────────────────┐
│  HOT PATH (Realtime, Standard API + Cache)  │
│  Cliente sube factura → OCR inmediato       │
│  Latencia: 2-5 segundos                     │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  COLD PATH (Batch nocturno)                 │
│  Cada noche a las 2AM:                      │
│  - Recategorización avanzada                │
│  - Detección de anomalías                   │
│  - Generación de reportes semanales         │
│  - Análisis tendencias                      │
│  Costo: 50% off                             │
└─────────────────────────────────────────────┘
```

**El usuario percibe respuesta instantánea + features ricas al día siguiente.**

## Implementación práctica con queue

```python
# Cliente sube factura
def process_invoice_realtime(file):
    # Crítico: OCR inmediato
    ocr_result = call_anthropic_realtime(file)

    # Encolar análisis profundo para batch
    queue.add({
        "type": "deep_analysis",
        "ocr_result": ocr_result,
        "file_id": file.id,
        "tenant_id": tenant_id
    })

    return ocr_result

# Job nocturno
def run_nightly_batch():
    pending = queue.get_all_pending()

    batch = client.messages.batches.create(
        requests=[
            {
                "custom_id": item["file_id"],
                "params": build_analysis_params(item)
            }
            for item in pending
        ]
    )

    # 50% descuento aplica a TODAS las 1000+ requests
```

## Casos del usuario

### BIO-SETA / AGENTE GASTROWHATS
- **Hot path:** respuesta WhatsApp (realtime, NO batch)
- **Cold path:** análisis nocturno de conversaciones del día para detectar:
  - Productos más preguntados (insight para inventario)
  - Objeciones comunes (mejora del bot)
  - Clientes interesados sin compra (re-engagement)
- **Ahorro estimado del cold path:** $50-100/mes en Anthropic

### AGENTE STUDIO
- **Hot path:** generación cuando user en sesión activa
- **Cold path:** batch overnight para:
  - Pre-generar variations de creativos para mañana
  - Re-procesar assets viejos con nuevo modelo
  - Análisis competidor scrapeado
- **Ahorro estimado:** 40-50% del costo creativo

### AGENTE TRADING
- **Hot path:** alertas de mercado en tiempo real
- **Cold path:** análisis post-mercado (4 PM en adelante):
  - Resúmenes del día por instrumento
  - Análisis de patrones del día completo
  - Reporte semanal compilado batch
- **Ahorro estimado:** 60% (la mayoría del análisis NO necesita realtime)

### SaaS XPRIZE (gastrobares)
- **Hot path:** OCR factura cuando llega (cliente WhatsApp espera confirmación)
- **Cold path nocturno:**
  - Categorización avanzada con más context
  - Detección anomalías ("este mes el proveedor X subió 20%")
  - Reportes semanales por cliente
  - Sync a Siigo en bulk si la API permite
- **Ahorro estimado:** 70% del costo LLM total

## Checklist al migrar a batch

- [ ] Identificar qué workloads NO requieren realtime
- [ ] Calcular volumen actual (requests/día candidatos)
- [ ] Diseñar queue de jobs pendientes
- [ ] Implementar batch creation + polling
- [ ] Handling de errors: separar `succeeded` / `errored` / `expired`
- [ ] Retry strategy para `errored` (revisar si es retryable)
- [ ] Re-encolar `expired` (caso raro pero pasa)
- [ ] Cron job para disparar batch (típico: 2 AM)
- [ ] Combinar con prompt caching (95% ahorro stack)
- [ ] Medir ahorro vs baseline pre-batch

## Limitaciones a tener en cuenta

- **SLA es 24h máximo.** Si necesitas resultados en 1h garantizadas, no es batch.
- **No es realtime ni near-realtime.** Esperá horas, no minutos.
- **Si una request del batch falla**, las otras siguen. Maneja errores per-request.
- **Batch result es JSONL stream**, no JSON response — iterá con `for result in ...`.

Relacionado: [[01-prompt-caching]], [[10-monitoring-budget]], [[03-model-routing]]

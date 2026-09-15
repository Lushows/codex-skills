# 09 — Streaming + Early Termination

**Impacto:** 20-50% reducción en output tokens + UX dramáticamente mejor.
**Esfuerzo:** Bajo a medio.
**Cuándo aplicar:** Cualquier respuesta visible al usuario (chat, dashboards, generación de texto largo).
**Cuándo NO aplicar:** Pipelines batch puros, agentes autónomos sin user-facing UI.

## Por qué streaming importa para costos

### Reason 1: UX progresiva permite parar temprano

Sin streaming: el usuario espera 8 segundos por respuesta de 800 tokens, lee, decide que ya tiene la info que necesitaba.
Con streaming: el usuario empieza a leer al token 50 (1 segundo), encuentra lo que buscaba al token 150, cancela.

**Si tu UI permite cancelar, cancelar = no pagás tokens no generados.**

### Reason 2: max_tokens dinámico es más fácil de ajustar

Sin streaming: setás `max_tokens=2000` "por si acaso". Generás 2000 cada vez.
Con streaming + stop sequences inteligentes: parás cuando encontrás `[FIN]` o llegaste al schema completo. Ahorrás 50%+.

### Reason 3: Errores de loop infinito detectados temprano

Sin streaming: el modelo se atora generando lo mismo 10 veces, esperás 30 segundos, pagás 4000 tokens.
Con streaming: detectás repetición al token 200, abortás.

## Implementación básica (Anthropic)

```python
from anthropic import Anthropic

client = Anthropic()

# Sin streaming (espera respuesta completa)
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1000,
    messages=[{"role": "user", "content": "Explica RAG en detalle"}]
)
print(response.content[0].text)

# Con streaming (chunks llegan a medida que se generan)
with client.messages.stream(
    model="claude-sonnet-4-6",
    max_tokens=1000,
    messages=[{"role": "user", "content": "Explica RAG en detalle"}]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)

    # Acceder al message completo al final
    final_message = stream.get_final_message()
    print(f"\nTokens used: {final_message.usage.output_tokens}")
```

## TypeScript / Vercel AI SDK

```typescript
import { streamText } from 'ai';
import { anthropic } from '@ai-sdk/anthropic';

const result = await streamText({
  model: anthropic('claude-sonnet-4-6'),
  prompt: 'Explica RAG en detalle',
  maxTokens: 1000,
});

for await (const chunk of result.textStream) {
  process.stdout.write(chunk);
}
```

## Early termination patterns

### Patrón 1: Stop sequences

Le decís al modelo "cuando veas X, parate":

```python
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1000,
    stop_sequences=["[END]", "###", "</response>"],
    messages=[{
        "role": "user",
        "content": "Genera 5 ideas. Termina con [END] cuando completes."
    }]
)
# El modelo para SOLO al generar "[END]", aunque max_tokens permita más
```

**Ahorro:** evita generación excesiva. El modelo aprende que `[END]` = stop.

### Patrón 2: Early termination en cliente (streaming)

```python
def stream_with_early_stop(prompt, max_words=50):
    word_count = 0
    accumulated = ""

    with client.messages.stream(
        model="claude-haiku-4-5",
        max_tokens=200,
        messages=[{"role": "user", "content": prompt}]
    ) as stream:
        for text in stream.text_stream:
            accumulated += text
            word_count = len(accumulated.split())

            print(text, end="", flush=True)

            # Parar cuando llegamos al límite
            if word_count >= max_words:
                stream.close()  # Cancela el resto (no se paga)
                break

    return accumulated
```

**Use case:** "Dame respuesta corta" pero el modelo se entusiasma y genera ensayo. Cortás manualmente.

### Patrón 3: Schema-based stop (structured outputs)

Cuando generás JSON, parar al completar el schema:

```python
def stream_until_valid_json(prompt):
    accumulated = ""

    with client.messages.stream(
        model="claude-sonnet-4-6",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt + "\nResponde con JSON válido."}]
    ) as stream:
        for text in stream.text_stream:
            accumulated += text

            # Intentar parsear: si JSON ya completo, parar
            try:
                json.loads(accumulated)
                stream.close()
                return accumulated
            except json.JSONDecodeError:
                continue  # Aún incompleto

    return accumulated
```

### Patrón 4: max_tokens dinámico por tipo de query

```python
def get_max_tokens(task_type, query):
    """Adaptive max_tokens based on task complexity."""
    if task_type == "classify":
        return 50  # "category_X" — corto
    elif task_type == "extract":
        return 300  # JSON con datos extraídos
    elif task_type == "summarize":
        # Heurística: output ~25% del input
        input_tokens = count_tokens(query)
        return min(int(input_tokens * 0.25), 800)
    elif task_type == "generate_long":
        return 4000
    else:
        return 1000  # default conservador

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=get_max_tokens(task_type, query),
    ...
)
```

**Ahorro:** evita generar 2000 tokens cuando solo necesitabas 100.

### Patrón 5: Detectar loops y abortar

```python
def stream_with_loop_detection(prompt):
    chunks = []
    repetition_threshold = 3  # 3 chunks idénticos consecutivos = loop

    with client.messages.stream(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}]
    ) as stream:
        for text in stream.text_stream:
            chunks.append(text)

            # Check si los últimos N son idénticos
            if len(chunks) >= repetition_threshold:
                last_n = chunks[-repetition_threshold:]
                if len(set(last_n)) == 1:  # Todos iguales
                    print("\n⚠️ Loop detectado, abortando.")
                    stream.close()
                    break

    return "".join(chunks)
```

## Streaming en UI (importante para UX)

### React con Vercel AI SDK

```typescript
'use client';
import { useChat } from 'ai/react';

export default function Chat() {
  const { messages, input, handleSubmit, handleInputChange, isLoading, stop } = useChat();

  return (
    <div>
      {messages.map(m => (
        <div key={m.id}>
          <strong>{m.role}:</strong> {m.content}
        </div>
      ))}

      <form onSubmit={handleSubmit}>
        <input value={input} onChange={handleInputChange} />
        {!isLoading ? (
          <button type="submit">Send</button>
        ) : (
          <button type="button" onClick={stop}>
            Stop  {/* User puede cortar, ahorra tokens */}
          </button>
        )}
      </form>
    </div>
  );
}
```

**Key UX patterns:**
- Mostrar "Generando..." mientras stream
- Botón "Parar" prominente (user puede cancelar y NO paga el resto)
- Mostrar tokens generados live (transparencia de costo)

## Streaming + caching combinados

```python
def stream_with_caching(prompt, system):
    with client.messages.stream(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        system=[{
            "type": "text",
            "text": system,
            "cache_control": {"type": "ephemeral"}  # ← caching activo
        }],
        messages=[{"role": "user", "content": prompt}]
    ) as stream:
        for text in stream.text_stream:
            yield text

        final = stream.get_final_message()
        print(f"Cache reads: {final.usage.cache_read_input_tokens}")
```

Funciona perfecto: caching reduce input cost, streaming reduce output cost + mejora UX.

## Cuándo NO usar streaming

❌ **Pipelines batch puros** — nadie está mirando, no hay user esperando
❌ **Tool calling pipelines no-conversational** — esperás respuesta completa para procesar
❌ **APIs que retornan JSON estructurado a otro sistema** — el cliente espera el JSON completo
❌ **Background jobs** — async by design

## Métricas que importan

```python
class StreamingMetrics:
    def __init__(self):
        self.total_requests = 0
        self.requests_cancelled = 0  # User canceló mid-stream
        self.tokens_saved_by_cancel = 0
        self.avg_first_token_latency_ms = 0  # Time to first token (TTFT)
        self.avg_full_response_latency_ms = 0

    @property
    def cancel_rate(self) -> float:
        return self.requests_cancelled / self.total_requests if self.total_requests > 0 else 0

    @property
    def cost_saved_by_cancellation(self) -> float:
        return self.tokens_saved_by_cancel * 0.000015  # Sonnet output $15/1M
```

**Targets:**
- TTFT < 1 segundo (UX percibida como instantánea)
- Cancel rate 5-15% (señal saludable de que users tienen opción)
- Si cancel rate > 30% → algo está mal (respuestas demasiado largas o lentas)

## Casos del usuario

### BIO-SETA / AGENTE GASTROWHATS
- WhatsApp NO soporta streaming en mensajes (mensaje llega completo)
- **Alternativa:** typing indicator → respuesta completa
- Pero EN DASHBOARD interno (admin chat con AI), streaming ayuda
- **Stop sequences:** "[FIN]" cuando bot completa respuesta

### AGENTE STUDIO
- Generación de copy creativo en dashboard → streaming UI ESENCIAL
- User ve copy generándose live, puede cortar si va mal
- **Ahorro:** 20-30% en costos de generación

### AGENTE TRADING
- Análisis técnico live en dashboard → streaming
- User ve insight construyéndose, decide en tiempo real
- **Ahorro:** ~25% por cancelaciones tempranas

### SaaS XPRIZE
- Reportes mensuales generados en dashboard → streaming
- Chat con asistente del SaaS → streaming
- OCR de facturas → NO streaming (proceso interno, output JSON)
- **Ahorro estimado:** 15-25% en interfaces user-facing

## Checklist

- [ ] Identificar endpoints con UI user-facing
- [ ] Implementar streaming en esos endpoints
- [ ] UI muestra "stop" / "cancel" button prominentemente
- [ ] Stop sequences inteligentes (e.g., "[END]", "</response>")
- [ ] max_tokens adaptive por tipo de query
- [ ] Loop detection en streaming
- [ ] Métricas: TTFT, cancel rate, tokens saved
- [ ] Combinar con caching para max ahorro

Relacionado: [[01-prompt-caching]], [[03-model-routing]], [[04-context-engineering]]

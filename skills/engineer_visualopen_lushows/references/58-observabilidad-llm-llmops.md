# 58 — Observabilidad de LLM (LLMOps)

No puedes debuggear, controlar costo, ni mejorar una app LLM que no ves. La unidad es el **trace**: un request →
árbol de **spans** (render de prompt, retrieval, embedding, cada LLM call, cada tool call, sub-agente). Captura por
span: input/output, modelo+params, tokens (in/out), latencia, **costo**, metadata (user id, session, versión).

## Langfuse (la opción OSS dominante 2026)
MIT-core, self-hosteable, **OpenTelemetry-native** (SDK v4 implementa el OTel `SpanExporter`). Da traces, sessions,
**scores/evals**, **prompt management con versionado**, datasets, playground. Self-host = Docker; **producción v3+
necesita Postgres + Redis + blob S3-compatible.** Alternativas: **LangSmith** (mejor con LangChain/LangGraph,
hosted), **Helicone** (proxy drop-in, una base-URL, el más rápido de montar, gran cost), **Arize Phoenix** (OSS, fuerte eval offline/drift).

```python
from fastapi import FastAPI
from langfuse import observe, get_client
from langfuse.openai import openai          # auto-traces cada call
app = FastAPI(); langfuse = get_client()

@app.post("/chat")
@observe()                                  # crea el span raíz
async def chat(msg: str, user_id: str):
    langfuse.update_current_trace(user_id=user_id, session_id="sess-1")
    prompt = langfuse.get_prompt("support-bot", label="production")   # versionado
    r = openai.chat.completions.create(model="gpt-4o-mini", messages=prompt.compile(question=msg))
    langfuse.score_current_trace(name="user_thumb", value=1)          # feedback online
    return r.choices[0].message.content
```

## Cost tracking & prompt management
**Costo** por request/user/session: Langfuse/Helicone computan $ desde tokens × tabla de precios — slicea por
`user_id`/`session_id` para hallar tus whales y agentes runaway. **Prompt management** desacopla prompts del código:
edita + label `production` en la UI, fetch por label en runtime (cacheado client+server), rollback instantáneo sin deploy.

## Evals — online + offline
**Offline:** dataset de regresión de golden inputs en cada cambio, scoreado por **LLM-as-judge** (modelo fuerte
gradúa correctitud/faithfulness/tono) + exact-match/regex donde sea determinista. **Online (prod):** samplea traces
live → judge async para hallucination/calidad, y captura **feedback de usuario** (thumbs, edits, abandonment) como
scores. Trackea hallucination juzgando answer-vs-retrieved-context faithfulness en muestra rolling.

## OTel GenAI semantic conventions
Estandarizan atributos (`gen_ai.system`, `gen_ai.request.model`, `gen_ai.usage.input_tokens/output_tokens`) → emites
a Langfuse + OTel collector + tu APM con una sola instrumentación. Prefiere auto-instrumentación (OpenLLMetry, OpenInference) sobre spans a mano.

## Gotchas
1. **PII se filtra a los traces** — prompts/outputs traen emails/nombres/pagos. Enmascara en el boundary del SDK; self-host si no puedes mandar data del usuario a un vendor.
2. **El sampling rompe tu mate de costo** — escala stats por la tasa de sampleo o sub-reportas el gasto.
3. **Spans async/streaming no cierran** — olvidar cerrar un span en un call streamed deja spans huérfanos; usa context managers/decorators.
4. **LLM-as-judge es sesgado y ruidoso** — favorece verbosidad y su propia familia; calibra contra labels humanos y pinea el judge model+prompt.
5. **Prompt-cache stale en self-host** — el cache agresivo puede servir un prompt viejo tras un nuevo label; verifica TTL/invalidación.
6. **Langfuse self-host v3+ necesita Redis+S3** — correrlo solo en Postgres pierde eventos bajo carga.

**Fuentes:** github.com/langfuse/langfuse · langfuse.com/integrations/native/opentelemetry · opentelemetry.io/docs/specs/semconv/gen-ai.

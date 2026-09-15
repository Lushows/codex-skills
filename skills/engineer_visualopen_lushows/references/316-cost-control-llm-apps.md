# 316 · Control de costo en apps LLM — pagar 10x menos por lo mismo

> El costo de una app LLM no lo decide el precio del modelo, sino cuántos tokens repites sin necesidad.
> Caching + routing + batch combinados bajan la factura hasta ~95% sin tocar la calidad.

## Las cuatro palancas (de mayor a menor impacto)
| Palanca | Ahorro típico | Cuándo |
|---|---|---|
| **Prompt caching** | hasta 90% del input cacheado | system prompt / contexto largo y estable |
| **Model routing** | 3-5x | la mayoría de queries son fáciles |
| **Batch API** | 50% fijo | trabajo no urgente (≤24h) |
| **Semantic cache** | evita la llamada entera | preguntas repetidas/similares |

## 1. Prompt caching — el más rentable
Anthropic (2026): el cache-write cuesta **1.25x** el input normal (TTL 5min) o **2.0x** (TTL 1h); los
hits posteriores pagan solo **0.10x** → 90% de descuento sobre lo cacheado.

```ts
// Marca el prefijo estable (system + docs) como cacheable
messages: [{ role:'system', content:[
  { type:'text', text: SYSTEM_PROMPT,
    cache_control:{ type:'ephemeral' } } // <- el cache-breakpoint
]}]
```
- **Ordena de estable→volátil**: system y RAG fijos primero, mensaje del usuario al final. El caché vive
  en el **prefijo común**; cualquier cambio temprano lo invalida.
- **Mata el caché sin querer**: un timestamp o un tool no-determinista al inicio rompe el prefijo (ver
  [[313-tool-use-function-calling-patterns]]). Mantén lo variable al final.

## 2. Model routing — barato por defecto, caro a demanda
No uses Opus para clasificar un "sí/no". Enruta por dificultad (precios 2026, in/out por 1M tok):

| Modelo | Precio | Úsalo para |
|---|---|---|
| Haiku 4.5 | $1 / $5 | clasificar, extraer, routing, respuestas cortas |
| Sonnet 4.6 | $3 / $15 | el 90% del trabajo: chat, tool-use, RAG |
| Opus 4.8 | $5 / $25 | razonamiento duro, código complejo, agentes largos |

Patrón: un **Haiku decide** si la query necesita Opus; la mayoría no.

## 3. Batch API — mitad de precio por esperar
Trabajo asíncrono (resúmenes nocturnos, enriquecer un CSV, evals) → Batch API = **50% off** automático
en input y output, ventana de ≤24h. Combinable con caching → ahorro acumulado hasta ~95%.

## 4. Semantic cache — la llamada que no haces
Antes de pegarle al LLM, busca la pregunta en un vector-store de Q&A previas; si la similitud > umbral,
devuelve la respuesta cacheada. Mata FAQs repetidas a costo casi cero. Cuidado: invalida cuando los
datos subyacentes cambian (no cachees "¿cuál es mi saldo?").

## Higiene de tokens
- **Comprime el contexto**: no metas el historial completo; resume turnos viejos.
- **`max_tokens` real**: limita el output al tamaño que de verdad necesitas.
- **RAG enfocado**: 3 chunks relevantes baten 20 mediocres y cuestan menos.
- **Observa el gasto**: loguea tokens in/out por request y por feature; sin medición no optimizas (ver [[255-tco-selfhost-vs-api]]).

Cruza con [[34-prompt-engineering-llm]] y [[255-tco-selfhost-vs-api]].

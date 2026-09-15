# 309 · Memoria y contexto en agentes (short/long-term, vector memory, compaction)

> El context window es RAM volátil: se llena, se degrada y se borra al cerrar la sesión. La memoria
> es el disco: lo que el agente **recuerda entre turnos y entre sesiones**. Confundirlos cuesta caro.

[[308-agentes-produccion-orquestacion]] gobierna el loop; este archivo gobierna qué entra y
permanece en la cabeza del agente. La memoria bien hecha es RAG aplicado al propio agente.

## Las tres memorias
| Tipo | Vive en | Recupera por | Ejemplo |
|---|---|---|---|
| **Short-term (working)** | context window del turno | está siempre presente | historial de la conversación actual |
| **Long-term semántica** | vector DB | similitud (RAG) | "el cliente prefiere envío exprés" |
| **Episodic** | store por sesión/usuario | sesión/tiempo | "la última vez pediste melena de león" |
| **Procedural** | system prompt / skills | siempre/by-rule | reglas, tono, herramientas disponibles |

Short-term es rápido pero finito y se pierde; long-term persiste pero hay que **ir a buscarlo**. El
arte está en decidir qué se promueve de short a long y qué se trae de long a short en cada turno.

## El context window se degrada antes de llenarse
- **Lost in the middle**: lo del centro de un contexto largo se ignora. Pon lo crítico al inicio y al
  final, no en medio de 40 mensajes.
- **Context rot**: meter todo el historial degrada la calidad y dispara coste/latencia. Más tokens ≠
  mejor respuesta. Cura el contexto, no lo acumules.
- **Presupuesto de tokens**: reserva cupo fijo para system, memoria recuperada, historial y respuesta.
  Si te pasas, comprime — no truncos a ciegas el final (pierdes la pregunta).

## Compaction (cómo no reventar la ventana en sesiones largas)
- **Summarization rolling**: cada N turnos, un LLM barato resume el bloque viejo a un párrafo y lo
  reemplaza. El detalle exacto va a long-term por si hace falta recuperarlo.
- **Sliding window + pinned**: mantén los últimos K turnos verbatim + un resumen acumulado + mensajes
  "fijados" (datos del pedido, identidad). Anthropic/Claude Agent SDK lo hacen como *context editing*.
- **Estructura > prosa**: guarda hechos como JSON (`{cliente, ciudad, producto_interes}`) no como
  párrafos. Es más denso, parseable y no se contradice solo.

## Vector memory (long-term que escala)
- Embebe cada hecho/preferencia/interacción y guárdalo con metadata (`user_id`, `ts`, `type`). En cada
  turno, recupera top-k por similitud con el mensaje actual e inyéctalo (es RAG, ver [[307-rag-en-produccion-a-fondo]]).
- **Write-policy**: no guardes cada mensaje. Extrae hechos salientes con un LLM ("¿hay algo digno de
  recordar?") y deduplica contra lo ya almacenado (mismo content-hash → no insertar).
- **Conflict resolution**: cuando un hecho nuevo contradice uno viejo ("ahora vivo en Medellín"),
  versiona y marca el viejo como `superseded`, no lo borres — el historial importa para auditoría.
- **Decay/relevancia**: combina similitud + recencia + frecuencia de acceso (estilo memoria humana,
  patrón de Generative Agents). Lo viejo y nunca usado se purga.

## Frameworks de memoria 2026
- **Mem0**: capa de memoria con extracción+dedup automática, backend vectorial; popular para chatbots.
- **LangGraph store / checkpointer**: memoria por thread (short) y cross-thread (long) integrada al grafo.
- **Letta (ex-MemGPT)**: gestiona jerarquía memoria-de-contexto vs externa, paginando como un OS.
- **Zep**: memoria temporal con knowledge graph (qué era cierto y cuándo). Para asistentes con historia larga.
- Caso real del repo: `src/customerMemory.js` (perfil persistente por número) es exactamente esto a mano.

## Multi-tenant y privacidad
- **Aísla por `user_id`/`tenant`** en el filtro de recuperación, igual que en RAG. Una fuga de memoria
  entre usuarios es fuga de datos personales.
- **PII en memoria**: no persistas datos sensibles sin necesidad; redacta antes de guardar ([[311-guardrails-safety-llm-apps]]).
  Cumple borrado a petición (GDPR): la memoria debe ser borrable por usuario.

## Gotchas
1. **Guardar todo = recuperar ruido**: una memoria llena de trivia hunde la precision del retrieval.
2. **Resumir sin guardar el detalle** pierde datos irrecuperables; resume a short, archiva a long.
3. **No deduplicar** infla la memoria con el mismo hecho 50 veces y sesga el top-k.
4. **Memoria sin eval**: mide si recuperar memoria mejora la respuesta; a veces solo añade coste ([[310-evals-llm-apps]]).

Cruza con [[308-agentes-produccion-orquestacion]], [[307-rag-en-produccion-a-fondo]] y [[32-agentes-y-tool-use]].

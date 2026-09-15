# 308 · Agentes en producción (orquestación, planificación, loops, HITL, costo/latencia)

> Un agente de demo cierra el loop una vez. Un agente de producción **se orquesta, no se desboca,
> pide ayuda humana cuando toca y no quema $50 por consulta**. El loop es fácil; gobernarlo no.

[[32-agentes-y-tool-use]] cubre el loop ReAct, frameworks y MCP. Aquí va lo operativo: cómo
estructurar el sistema, controlar la trayectoria y sobrevivir al fallo no-determinista.

## ¿Workflow o agente? (decide antes de codear)
Anthropic lo repite: **no uses agente si un workflow basta**. Pasos conocidos → workflow determinista
(chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer). Trayectoria
impredecible y abierta → agente. El agente añade latencia, coste y no-determinismo: páguenlo solo
cuando el problema lo exige. La mayoría de "agentes" en producción son en realidad workflows con 1-2
puntos de decisión LLM, y está bien que así sea.

## Orquestación
| Patrón | Cuándo | Riesgo |
|---|---|---|
| Single-agent + buenas tools | 80% de casos | tool mal descrita → elección errónea |
| Orchestrator-worker | subtareas paralelizables/especializadas | coordinación, doble coste de tokens |
| Routing (clasificador → skill) | dominios disjuntos (soporte/ventas/billing) | router con baja precision degrada todo |
| Handoff | transferencia de contexto entre roles | pérdida de estado en el traspaso |

- **Grafo de estados explícito** (LangGraph): nodos = pasos, aristas = transiciones, estado serializable.
  Da checkpointing, replay y human-in-the-loop nativos. Madurez de producción (Klarna, Uber, LinkedIn).
- **Estado durable**: persiste el estado del agente (DB/checkpointer) tras cada paso. Si el worker muere
  a mitad, retomas desde el último checkpoint en vez de reiniciar el plan completo.

## Planificación
- **Plan-and-execute** para tareas largas: genera el plan completo una vez, ejecuta paso a paso →
  menos re-planificaciones, menos tokens. Re-planifica solo si un paso falla o el mundo cambió.
- **Reflection/evaluator-optimizer**: un segundo paso evalúa la salida y reintenta. Sube calidad,
  duplica coste — actívalo solo en outputs críticos, no en cada turno.
- Evita Tree-of-Thought en producción salvo problemas de búsqueda pura: explosión de coste.

## Control del loop (donde se queman las cuentas)
- **`max_steps` + timeout duro**: sin límite, un bucle quema dinero hasta que alguien lo nota.
- **Detector de bucles**: si la misma tool se llama con los mismos args N veces → aborta o escala a humano.
- **Tool con efectos = idempotente o confirmada**: `refund`, `send_email`, `delete` deben llevar
  idempotency-key o pasar por human-in-the-loop. Nunca dejes una tool destructiva sin guardia.
- **Presupuesto por request**: corta el job si supera X tokens/$/segundos y devuelve resultado parcial.

## Human-in-the-loop (HITL)
- **Interrupt + resume**: el grafo se pausa en un nodo de aprobación, persiste estado, espera la
  decisión humana (cola/UI) y reanuda. No bloquees un worker esperando a una persona — desacopla.
- Define **umbrales de escalado**: baja confianza del modelo, monto alto, acción irreversible, o
  cliente VIP → siempre humano. El agente propone, el humano dispara.

## Costo y latencia
- **Modelo por rol**: Haiku/gpt-oss para routing y clasificación; modelo caro solo para el razonamiento
  duro. Un router barato delante recorta el 70% del gasto.
- **Prompt caching** del system + schemas de tools (90% off en lectura): el prompt de tools es enorme y
  constante → cachearlo es dinero gratis.
- **Paraleliza tools independientes** (parallel tool-calls) para bajar latencia de pared; pero si B
  depende de A, no las hagas paralelas.
- **Streaming + progreso**: emite estados ("buscando pedido…") para que el usuario no perciba el timeout.

## Observabilidad y evals (no negociable)
- Traza cada paso con OpenTelemetry (Langfuse, LangSmith, Arize Phoenix). Sin trazas, debuggear un
  agente no-determinista es imposible.
- **Trajectory eval** y **tool-correctness**: ¿la secuencia fue eficiente?, ¿llamó la tool correcta con
  args correctos? Mide precision/recall de tool-selection, no solo la respuesta final ([[310-evals-llm-apps]]).

## Gotchas
1. **Sobre-ingeniería multi-agente**: cada agente extra añade modos de fallo de coordinación. Empieza con uno.
2. **Descripciones de tools vagas** son el bug #1 de selección — escríbelas con precondiciones y ejemplos.
3. **MCP remoto = superficie de ataque**: valida orígenes, no expongas tools destructivas sin confirmación.
4. **El no-determinismo no se "arregla"**, se acota: límites, guardrails y HITL, no más prompt-tuning.

Cruza con [[32-agentes-y-tool-use]], [[66-agentes-avanzados-computer-use]], [[309-memoria-contexto-agentes]] y [[311-guardrails-safety-llm-apps]].

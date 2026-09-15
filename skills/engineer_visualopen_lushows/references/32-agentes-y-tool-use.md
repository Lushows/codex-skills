# Agentes y Tool-Use con LLMs: El Loop, Frameworks 2026 y MCP

Un **agente** es un LLM que en un bucle decide qué herramienta llamar, observa el resultado y repite hasta resolver la tarea. La diferencia clave con un *workflow* es el control de flujo: en un workflow el código orquesta pasos fijos; en un agente, el LLM decide la trayectoria en runtime.

## El loop ReAct

```
reason → act → observe → (repeat) → answer
```

El modelo razona ("necesito el clima"), actúa (llama `get_weather`), observa el resultado y vuelve a razonar. En 2026 el "reason" suele ser el *reasoning* nativo del modelo (extended thinking de Claude, o-series), no CoT manual en el prompt.

## Function / tool calling

Se declara cada tool con un **JSON Schema**; el LLM devuelve `tool_calls` con argumentos validados contra el schema.

```python
tools = [{
  "name": "get_order",
  "description": "Busca un pedido por ID",
  "input_schema": {
    "type": "object",
    "properties": {"order_id": {"type": "string"}},
    "required": ["order_id"]
  }
}]
```

- **Parallel tool calls**: el modelo puede pedir varias herramientas en un turno (p. ej. clima de 3 ciudades). Mantén las tools independientes para aprovecharlo.
- **Structured output**: fuerza la respuesta final a un schema (Pydantic / `response_format`) para parsear sin regex.

## ¿Agente o workflow? (guía de Anthropic)

Anthropic ("Building effective agents"): **no construyas un agente si un workflow basta.** Los agentes añaden latencia, coste y no-determinismo. Usa workflows (cadenas, routing, parallelization) cuando los pasos son conocidos; reserva agentes para tareas abiertas donde no puedes predecir cuántos pasos hacen falta. Patrones de workflow: prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer.

## Patrones de planning

- **Plan-and-execute**: el agente genera un plan completo primero, luego ejecuta paso a paso (menos llamadas de re-planificación, mejor para tareas largas).
- **Reflection / self-critique**: el agente evalúa su propia salida y reintenta (evaluator-optimizer).
- **Tree-of-Thought**: explora múltiples ramas de razonamiento y poda; caro, úsalo solo en problemas de búsqueda.

## Memoria

- **Short-term**: la ventana de contexto del turno actual (historial de mensajes).
- **Long-term vectorial**: hechos/preferencias embebidos en una vector DB, recuperados por similitud (igual que RAG). Ej.: perfil de cliente persistente.
- **Episodic**: registro de interacciones pasadas ("la última vez pediste X") indexado por sesión/usuario.

## Multi-agente

- **Orchestrator-worker**: un agente coordinador delega subtareas a workers especializados. Patrón más usado en producción.
- **Debate**: varios agentes argumentan y un juez decide; mejora factualidad, multiplica coste.
- **Handoff**: un agente transfiere la conversación a otro (soporte → ventas). Nativo en OpenAI Agents SDK.

## Frameworks 2026

- **LangGraph** (LangChain): grafo de estados explícito, máxima madurez en producción (Klarna, Uber, LinkedIn). Control fino, checkpointing, human-in-the-loop. Curva de aprendizaje alta.
- **OpenAI Agents SDK**: evolución de Swarm; handoffs, guardrails, sandbox de ejecución. Ligero, OpenAI-céntrico.
- **Claude Agent SDK** (antes Claude Code SDK, renombrado finales 2025): runtime de agente de propósito general. Paquetes `claude-agent-sdk` (Python) y npm (TS). Integra MCP nativamente y extended thinking. Bloqueado a modelos Claude.
- **CrewAI** (v1.14+): equipos de agentes con roles, soporte A2A. Rápido de prototipar.
- **AG2**: sucesor comunitario de AutoGen (Microsoft, ahora en modo mantenimiento). Conversaciones multi-agente.
- **smolagents** (Hugging Face): minimalista, agentes que escriben/ejecutan código Python como "acción".
- **Pydantic AI**: capa type-safe; validación Pydantic de inputs/outputs, ideal si ya usas FastAPI.

## MCP (Model Context Protocol)

Estándar abierto (Anthropic, 2024) para conectar LLMs a herramientas/datos vía servidores MCP reutilizables. En 2026 es el estándar de facto, junto con **A2A** (agent-to-agent, Google) y **AGENTS.md** (OpenAI), bajo la Agentic AI Foundation (Linux Foundation; Anthropic, OpenAI, Google, Microsoft, AWS). Un servidor MCP expone `tools`, `resources` y `prompts`; cualquier cliente compatible (Claude Desktop, Cursor, tu agente) los consume sin código a medida. Transporte: stdio (local) o HTTP/SSE (remoto).

## Evals para agentes

- **Trajectory eval**: ¿la secuencia de pasos fue correcta/eficiente?, no solo la respuesta final.
- **Tool-correctness**: ¿llamó la tool correcta con los args correctos? Mide precision/recall de tool-selection.
- Herramientas: LangSmith, Braintrust, OpenAI Evals, Arize Phoenix (tracing OpenTelemetry).

## Control de coste/latencia

- Cachea el prompt de sistema + schemas de tools (prompt caching → 90% off en lectura).
- Limita `max_iterations` del loop para evitar bucles infinitos.
- Usa un modelo barato (Haiku, gpt-oss-20B) para routing y uno caro solo para razonamiento.

## Gotchas

1. **El loop sin límite quema dinero**: pon `max_steps`/timeout y un guardrail que detecte bucles (misma tool con mismos args repetida).
2. **Descripciones de tools = prompt**: una `description` vaga hace que el modelo elija mal. Escríbelas con ejemplos y precondiciones.
3. **Parallel tool calls rompen orden**: no asumas secuencia; si la tool B depende de A, no las hagas paralelas.
4. **Sobre-ingeniería con multi-agente**: la mayoría de problemas se resuelven con un agente + buenas tools; multi-agente añade fallos de coordinación.
5. **MCP remoto = superficie de ataque**: un servidor MCP malicioso puede inyectar instrucciones; valida orígenes y no expongas tools destructivas sin confirmación.

## Fuentes
- [Anthropic — Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [AI agent framework comparison 2026 (QubitTool)](https://qubittool.com/blog/ai-agent-framework-comparison-2026)
- [LangGraph docs](https://langchain-ai.github.io/langgraph/)
- [Claude Agent SDK](https://platform.claude.com/docs/en/agents-and-tools/claude-agent-sdk)
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)

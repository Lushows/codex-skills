# 98 — AI application frameworks (2026)

Split por lenguaje (TS vs Python) y por tarea (streaming chat / agentes stateful / extracción estructurada / prompt
optimization). **MCP es el estándar universal de tool-calling** debajo de casi todos.

## Las opciones
- **Vercel AI SDK (v6 en 2026)** — *el* estándar para **streaming AI a UIs web**. v6 añade **`ToolLoopAgent`** (maneja
  el loop call-LLM→tools→feed→repeat, 20 steps default), human-in-the-loop tool approval, structured outputs estables, DevTools. Provider-agnóstico. **Para cualquier feature chat/streaming web.**
  ```ts
  import { streamText } from "ai"; import { anthropic } from "@ai-sdk/anthropic"
  const r = streamText({ model: anthropic("claude-sonnet-4-6"), prompt: "..." })
  return r.toUIMessageStreamResponse()
  ```
- **Mastra** — el framework de agentes **TS end-to-end** (agentes, workflows, memoria, RAG, evals, MCP). Sin "Python tax". Complementa al AI SDK (a menudo lo usa por debajo).
- **LangGraph** — el default 2026 para **agentes stateful de producción en industrias reguladas** (state machines de grafo, durable execution, checkpointing). Para grafos complejos/auditables/long-running.
- **LlamaIndex** — líder **RAG/data-framework** (ingestion/indexing/retrieval). MCP es su default de tool-calling.
- **Pydantic AI** — agentes **Python tipados** (Pydantic outputs, model-agnostic, DI). **CrewAI** — prototipo rápido de **multi-agente role-based**. **DSPy** — **prompts como compilación** (optimiza prompts contra métricas; production-immature). **Instructor** — **structured output** (coerce a Pydantic/Zod con retries).

**Elegir:** streaming web → AI SDK · agentes TS → Mastra · grafos enterprise → LangGraph · RAG sobre docs → LlamaIndex · agentes Python tipados → Pydantic AI · multi-agente rápido → CrewAI · JSON confiable → Instructor · prompt opt → DSPy. **MCP:** 12,000+ servers, soporte nativo en casi todos.

## Gotchas
1. El `Agent` del AI SDK es una *interface* en v6, `ToolLoopAgent` es el impl default — lee la migración v5→v6.
2. El poder de LangGraph viene con overhead conceptual (nodes/edges/state) — overkill para un chatbot simple.
3. CrewAI demea rápido pero los loops multi-agente **queman tokens y se atascan** sin caps de steps.
4. DSPy necesita **buenas métricas de eval** — métrica basura, prompt optimizado basura.
5. Los MCP servers corren código con acceso a tools — **vetea servers no confiables** (SSRF/permisos amplios).
6. Mezclar frameworks (LangChain + AI SDK + custom) = dolor de version-churn; pinea y minimiza el stack.

**Fuentes:** speakeasy.com/blog (agent framework comparison) · vercel.com/blog/ai-sdk-6 · getknit.dev/blog (MCP ecosystem 2026) · developers.llamaindex.ai.

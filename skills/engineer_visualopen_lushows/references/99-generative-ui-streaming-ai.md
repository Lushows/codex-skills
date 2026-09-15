# 99 — Generative UI & streaming AI interfaces (2026)

La nueva UX va más allá del text box: **token streaming → structured/partial-object streaming → streaming de
componentes UI → canvases/artifacts editables**, con updates optimistas e interrupt/resume. El **Vercel AI SDK** define los patrones.

## Token streaming (baseline)
`streamText` (server) + `useChat` (`@ai-sdk/react`, client) = el stack canónico. `useChat` maneja todo el state del chat y streamea token-por-token. Ya es la UX esperada (mejora la latencia percibida).
```tsx
"use client"; import { useChat } from "@ai-sdk/react"
export default function Chat(){ const { messages, sendMessage } = useChat(); /* render parts */ }
```

## Generative UI (streaming de componentes React)
El salto: en vez de streamear *texto*, streameas **componentes React**. Capas del AI SDK: Core/UI/**RSC**. Con
**`streamUI`** los tools devuelven UI (async generator que `yield`ea un spinner, luego `return`ea el componente final) — "¿qué clima?" puede devolver `<WeatherCard/>`, no un párrafo. (Requiere framework RSC como Next; muchos prefieren ahora el approach **UI-message + typed data-parts** por portabilidad.) **`streamObject`** streamea **JSON parcial** contra un schema Zod → un form/list/card se llena progresivamente.

## Tool-call UIs / interrupt-resume / canvas
Los tool calls renderizan como **estados UI ricos** (pending→running→result). Con `ToolLoopAgent` (v6) + **human-in-
the-loop approval** puedes mostrar "el agente quiere enviar este WhatsApp — ¿apruebas?" a mitad del loop (**interrupt/
resume**). **App-gen (v0/bolt/lovable):** v0 (componentes React), **Lovable** (full-stack, ~$400M ARR feb 2026), Bolt
(prototipos rápidos). Workflow de agencia: v0 componentes → Lovable app → Claude Code production cleanup. **Chat vs canvas/artifacts:** superficie persistente *directamente editable* junto al chat (ChatGPT Canvas, Claude Artifacts, v0 preview). **Optimistic AI UIs:** renderiza el resultado esperado al instante, reconcilia al responder.

## Gotchas
1. **AI SDK RSC (`streamUI`) está en modo maintenance-lean** — el equipo lleva a UI-message streaming con typed data-parts; no sobre-inviertas en RSC-only.
2. El streaming **rompe el error handling naive** — un fallo a mitad de stream necesita estados UI explícitos (no un try/catch sobre una respuesta terminada).
3. Los parciales de `streamObject` son **incompletos por definición** — tus componentes deben renderizar con campos faltantes.
4. Generative UI **expande tu attack surface** — nunca dejes que el modelo elija componentes/props arbitrarios sin allowlist.
5. Interrupt/resume + tool approval necesita **estado durable** (ver ref 100) o un refresh pierde el progreso del agente.
6. v0/Bolt/Lovable producen **código prototipo** — gran velocidad pero audita seguridad/perf antes de prod ("the prototype trap").

**Fuentes:** ai-sdk.dev/docs · vercel.com/academy/ai-sdk (multi-step+generative-ui) · nxcode.io (vibe design tools 2026) · lovable.dev/guides.

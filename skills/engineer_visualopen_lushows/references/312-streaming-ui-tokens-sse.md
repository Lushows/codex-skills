# 312 · Streaming UI de tokens (SSE) — chat que escribe en vivo

> El LLM tarda 5-30s en la respuesta completa, pero el primer token sale en ~300ms.
> Si esperas el final, la UI parece colgada; si haces stream, parece instantánea.

## El transporte: SSE, no WebSocket
Streaming LLM es **unidireccional** (server→cliente) → `Server-Sent Events` gana a WebSocket:
una sola respuesta HTTP, reconexión automática, atraviesa proxies. El AI-SDK de Vercel (2026)
migró su data-stream protocol a SSE justo por esto: keep-alive con ping, reconnect, mejor caché.

```js
// Server (Next.js route handler) — AI SDK
import { streamText } from 'ai';
import { anthropic } from '@ai-sdk/anthropic';
export async function POST(req) {
  const { messages } = await req.json();
  const result = streamText({ model: anthropic('claude-sonnet-4-6'), messages });
  return result.toUIMessageStreamResponse(); // SSE: text-deltas + tool-calls + finish
}
```

```tsx
// Cliente — useChat maneja estado, history y re-render por delta
const { messages, sendMessage, status, stop } = useChat();
// status: 'submitted' | 'streaming' | 'ready' | 'error'
```

## Text-stream vs data-stream
| Necesitas | Protocolo | Cómo |
|---|---|---|
| Solo texto | text stream | `streamProtocol: 'text'`, lees `text-delta` |
| Tool-calls, metadata, fuentes | **data stream** (default) | parts tipados: `text`, `tool-*`, `data-*` |

Para tool-use (ver [[313-tool-use-function-calling-patterns]]) **necesitas data-stream**: el text plano
no transporta los eventos de herramienta.

## Partial rendering sin parpadeo
- **Acumula, no reemplaces**: cada delta se **concatena** al mensaje en curso. Renderiza Markdown
  incremental con un parser tolerante a Markdown incompleto (un ```` ``` ```` aún sin cerrar).
- **Auto-scroll inteligente**: pega al fondo solo si el usuario ya estaba al fondo; si scrolleó arriba,
  no lo arrastres. Detecta con `scrollHeight - scrollTop - clientHeight < 50`.
- **Cursor de typing**: un `▍` parpadeante mientras `status === 'streaming'`.

## Cancelación (lo que casi nadie hace bien)
El usuario debe poder cortar una respuesta cara a medias:
```tsx
{status === 'streaming' && <button onClick={stop}>Detener</button>}
```
Server: el `AbortSignal` del request debe propagarse al SDK del LLM → deja de facturar output tokens
en cuanto el cliente aborta. Sin esto, cancelar en UI sigue quemando dinero en el backend.

## Detalles que muerden
- **Buffering del proxy**: Nginx/Cloudflare a veces bufferean SSE → envía `X-Accel-Buffering: no` y
  `Content-Type: text/event-stream`. Sin esto el stream llega en bloques, no token a token.
- **Render cost**: re-parsear Markdown en cada delta es caro con respuestas largas → memoiza los
  bloques ya cerrados, re-renderiza solo el último.
- **Errores a mitad de stream**: un fallo tras el primer token NO es un HTTP 500 limpio → emite un
  evento `error` en el propio stream y muestra retry preservando lo ya recibido.
- **Resumability**: si la pestaña se cierra, el stream se pierde. Para chats serios, persiste deltas
  en Redis y reanuda con el `Last-Event-ID` de SSE.

Cruza con [[140-streaming-progreso-difusion-cliente]] y [[99-generative-ui-streaming-ai]].

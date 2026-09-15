# 44 — Realtime: WebSockets / SSE / WebRTC

## Elige el transporte por dirección y payload
- **SSE** (Server-Sent Events) — **server→client una vía** sobre HTTP long-lived (`text/event-stream`). **Auto-
  reconnect** + `Last-Event-ID` para resumir. Lo más simple: pasa proxies, sin handshake especial. Ideal para
  **streaming de tokens LLM**, progreso de jobs, feeds de notificación, log tailing.
- **WebSocket** — **full-duplex** TCP persistente. Para **chat, colaboración, multiplayer, live cursors** — algo que
  necesita baja latencia client→server. Para streaming LLM, WS deja al cliente mandar un **frame de cancel** → el
  server **aborta la llamada LLM en ms**; SSE sigue generando (quemando tokens) hasta que nota el TCP disconnect — costo material a escala.
- **WebRTC** — **media peer-to-peer** (audio/video/data) con NAT traversal (STUN/TURN). Para **llamadas voz/video**; necesita signaling (a menudo WS) y relays TURN.

## FastAPI / Starlette
```python
@app.get("/stream")
async def stream():
    async def gen():
        async for tok in llm.astream(prompt):
            yield f"data: {tok}\n\n"
    return StreamingResponse(gen(), media_type="text/event-stream")
```
WebSocket = `@app.websocket("/ws")` con `await ws.accept()` y loop `receive_text()`/`send_text()`.

## Escalar WebSockets
Cada proceso solo conoce SUS conexiones. Con N instancias tras un LB, los broadcasts necesitan un **backplane:** cada
instancia **se suscribe a Redis Pub/Sub** (o NATS/Kafka); para broadcast, publicas a un canal y todas hacen fan-out a
sus sockets locales. **Sticky sessions** (LB fija cliente a un pod) **o** **stateless + Redis** (preferido a escala).
Una instancia Uvicorn maneja ~**1,000-5,000 WS** concurrentes según throughput — planea el nº de instancias.

## Heartbeats / presencia
WS **ping/pong** (o heartbeat app ~20-30s) para detectar conexiones muertas y evitar que proxies/LBs maten sockets
idle. SSE auto-reconnecta; resume con `Last-Event-ID`. Backoff en reconnect. **Presencia:** trackea online en **Redis**
(SET/hash con TTL refrescado por heartbeat); publica join/leave en Pub/Sub. NO en memoria de proceso (se pierde en restart, invisible a otros pods).

## Para un producto IA/WhatsApp
SSE al dashboard para **token streaming + progreso de jobs** = default pragmático; pasa a WS solo si necesitas cancel client→server o chat bidireccional.

## Gotchas
1. **SSE no tiene señal de cancelación** del cliente → tokens LLM desperdiciados en streams abandonados; detecta disconnect (`await request.is_disconnected()`) y aborta.
2. Proxies con buffering (nginx, algunos CDNs) **bufferean SSE/streaming** — desactiva (`X-Accel-Buffering: no`, `proxy_buffering off`).
3. WebSockets **sin backplane Redis** funcionan en dev (1 instancia) y rompen en prod (N instancias) — "works on my machine".
4. **Idle timeouts:** los LBs (ALB, Cloudflare) tiran WS/SSE idle — heartbeat bajo el timeout.
5. WebRTC **necesita TURN** para ~10-20% de usuarios tras NAT simétrico; STUN solo falla — presupuesta un TURN (coturn).

**Fuentes:** jetbi.com/blog (streaming architecture 2026) · ably.com/blog (scaling pub-sub WebSockets+Redis) · engineering.surveysparrow.com (SSE).

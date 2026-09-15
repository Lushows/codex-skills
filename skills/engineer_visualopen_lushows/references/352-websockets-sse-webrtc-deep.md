# 352 · Transportes realtime a fondo: WS vs SSE vs WebRTC (escalado y reconexión)

> [[44-realtime-websockets-sse-webrtc]] elige el transporte; aquí lo industrializas:
> backplane que no se cae, reconexión sin perder mensajes, y dónde QUIC ya gana.

## Decisión por eje (no por moda)
| Eje | SSE | WebSocket | WebRTC (datachannel) | WebTransport (HTTP/3) |
|---|---|---|---|---|
| Dirección | server→client | full-duplex | full-duplex P2P | full-duplex |
| Transporte | HTTP/1.1-2 | TCP upgrade | UDP+DTLS | QUIC/UDP |
| Reconnect | nativo (`Last-Event-ID`) | manual | ICE restart | manual |
| Head-of-line block | sí (TCP) | sí (TCP) | no | no (streams indep.) |
| Datagramas no fiables | no | no | sí | sí |
| Soporte browser 2026 | 99% | 99% | 97% | ~75% (Safari 26.4+) [no verificado] |

Regla: server→client puro → **SSE**. Bidireccional con cancel client→server → **WS**. Media/voz → **WebRTC** ([[356-video-audio-calls-livekit.md]]). WebTransport solo como *enhancement* con fallback WS — aún no es default 2026.

## Reconexión que no pierde mensajes
El reconnect "que funciona" no basta: hay que **resumir sin huecos ni duplicados**.
- **SSE**: el server manda `id:` por evento; al reconectar el browser envía `Last-Event-ID` → reemites desde ahí. Necesitas un **buffer por canal** (lista en Redis con TTL) para servir el gap.
- **WS**: implementa tú el protocolo. Cliente guarda `lastSeq`; al reconectar manda `{resume: lastSeq}` → server reenvía el delta desde un ring-buffer. Sin esto, un blip de red = mensajes perdidos en silencio.
- **Idempotencia**: cada mensaje con `id` único; el cliente descarta duplicados (un resume puede solapar). At-least-once + dedup > exactly-once.
- **Backoff**: exponencial con jitter (250ms→8s, ±20%) para no martillar al server tras un deploy que tira 50k sockets a la vez (*thundering herd*).

## Escalado: el backplane es el sistema
Cada proceso solo conoce SUS sockets. Con N pods, broadcast necesita fan-out cruzado:
- **Redis Pub/Sub**: simple, fire-and-forget, sin persistencia → si un pod estaba reconectando, **pierde** el mensaje. OK para presencia/efímero.
- **Redis Streams / NATS JetStream / Kafka**: con offset → el consumidor resume tras caída sin huecos. Úsalo cuando el mensaje importa (chat, eventos de pedido).
- **Sticky vs stateless**: sticky sessions (LB fija cliente↔pod) simplifica estado local pero desbalancea y complica deploys; **stateless + Redis** escala mejor y sobrevive a rolling restarts. Preferido a escala.
- **Sharding por sala**: hashea `room_id`→pod (consistent hashing) para que un broadcast de sala no toque todos los pods. Esencial >100k conexiones.

## Capacidad y límites reales
- Uvicorn/Node: ~**1k–5k WS** concurrentes por proceso según throughput de mensajes; CPU del serializer (JSON) suele ser el techo antes que la RAM. Usa **msgpack/protobuf** si los frames son densos.
- Fan-out es O(suscriptores): 10k clientes en una sala × 10 msg/s = 100k sends/s desde un pod → mide y shardea.
- Límite de FDs del kernel (`ulimit -n`), `somaxconn`, y memoria por socket (~30–60KB con buffers) son los muros físicos.

## Auth y seguridad del canal
- **Handshake, no query string**: no metas el token en la URL del WS (queda en logs/proxies). Manda el JWT como primer frame tras `accept()`, o en `Sec-WebSocket-Protocol`; cierra con código 1008 si no valida.
- **Expiración a mitad de sesión**: un WS vive horas; el JWT caduca antes. Implementa **re-auth in-band** (frame de refresh) o cierra y reconecta con token nuevo. Sin esto, sesiones zombi con permisos vencidos.
- **Origin check + rate-limit del upgrade**: valida `Origin` (anti CSWSH) y limita conexiones por IP/usuario; un atacante que abre 100k sockets te agota FDs.
- **SSE hereda cookies**: cuidado con CSRF en endpoints SSE autenticados por cookie; exige header custom o token.

## WebRTC para datos (no solo video)
Datachannel = UDP fiable-opcional, sin head-of-line block: ideal para **cursores/estado de juego** de muy baja latencia. Costo: signaling (vía WS), **STUN** (descubrir IP pública) y **TURN** (relay para ~10–20% tras NAT simétrico) — presupuesta un coturn. P2P no escala a salas grandes → para >~10 peers usa **SFU** ([[356-video-audio-calls-livekit.md]]).

## Serverless y edge: dónde viven los sockets
- **Lambda/Vercel Functions** no mantienen conexiones largas → usa **API Gateway WebSocket** (gestiona el socket, tú respondes a `$connect`/`$disconnect`/`$default`) o un servicio managed (Ably, Pusher, PartyKit).
- **Cloudflare Durable Objects**: un objeto con estado por sala = backplane natural sin Redis; el DO es la autoridad y guarda las conexiones de su sala. Encaja perfecto con [[353-crdt-collab-yjs]] y [[354-presence-cursors]].
- **Render/Fly/contenedor**: proceso largo clásico → tú montas el backplane Redis. Más control, más ops.

## Gotchas que muerden en prod
1. **Proxy buffering**: nginx/CDN bufferean SSE → `proxy_buffering off` + `X-Accel-Buffering: no`. Sin esto, los eventos llegan en ráfagas.
2. **Idle timeout del LB** (ALB 60s, Cloudflare 100s) mata sockets quietos → heartbeat por debajo del umbral.
3. **Pub/Sub sin persistencia** = mensajes perdidos durante reconnect; no lo descubres en dev (1 pod).
4. **Deploy = tormenta de reconexión**: drena conexiones gradualmente (cierre con código 1001 + backoff con jitter), no las tires todas de golpe.
5. **SSE sin señal de cancel**: stream LLM abandonado quema tokens; detecta `request.is_disconnected()` y aborta — ver [[355-live-updates-patterns]].

Cruza con [[44-realtime-websockets-sse-webrtc]], [[355-live-updates-patterns]] y [[356-video-audio-calls-livekit.md]].

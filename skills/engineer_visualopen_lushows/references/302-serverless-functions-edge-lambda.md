# 302 · Funciones serverless: Edge vs Node, cold start y límites

> El runtime no es un detalle: define cold start, qué APIs tienes y cuánto puede correr la función.
> Elegir mal te deja sin `fs`, sin streaming largo, o pagando arranques de 2s en cada poll.

## Los dos runtimes
| | Edge (V8 isolate) | Node / Lambda |
|---|---|---|
| Arranque en frío | 0-10ms (sin OS, solo isolate) | 800ms-2.5s (peor con conexión a DB) |
| APIs | Solo Web standard (`fetch`, `Request`, `crypto`) | Node completo (`fs`, módulos nativos, todo npm) |
| Bundle | 1MB free / 4MB pro (V8) | Decenas de MB |
| Memoria | baja (~128MB) | hasta 10GB |
| Duración | ~25s para iniciar respuesta, stream hasta 300s | hasta 15 min (Vercel Node / Lambda) |
| Uso | redirects, auth-check, personalización, geo | trabajo pesado, SDKs Node, DB, ffmpeg, llamar GPU |

## Aviso fuerte (2026) [verificado]
**Vercel deprecó los "Edge Functions" como producto el 2-jun-2026.** El runtime Edge sigue existiendo dentro
de Vercel Functions, pero el camino recomendado es **Node runtime + Fluid Compute** (concurrencia dentro de la
misma instancia → menos cold start, pricing por *Active CPU*). En Cloudflare el modelo isolate (Workers) sigue
siendo de primera clase → ver [[303-cloudflare-workers-d1-r2]].

## Cold start: por qué importa para GPU
Tu función serverless casi nunca hace el trabajo pesado: **orquesta**. Recibe el webhook, mete un job en cola
([[305-message-queues-cloud]]), arranca el worker GPU y responde rápido. El cold start del isolate (0-10ms) gana
para el endpoint de *submit/poll*; el Node runtime gana cuando necesitas el SDK pesado o `fs`. No corras la
inferencia dentro de la función serverless: 15 min de wall-clock no alcanzan para un render largo y pagas CPU ocioso.

## Streaming
- **Edge runtime**: debe empezar a emitir la respuesta dentro de ~25s; luego puede streamear hasta 300s.
- **Node runtime**: streaming con `ReadableStream`; ambos soportan `waitUntil()` para tarea async tras responder.
- Patrón LLM/avatar: streamea tokens/progreso por SSE desde el runtime, pero el render real corre fuera (cola+worker).
  Para render largo no streamees el binario: devuelve URL firmada de [[162-storage-cdn-media-generada]].

## Límites que muerden
- **Edge sin `fs` ni módulos nativos**: si tu lib (sharp, ffmpeg-static, un SDK) toca el FS o binario nativo →
  falla en runtime, no en build. Usa Node runtime para eso.
- **Bundle Edge 1-4MB**: un SDK gordo no entra. Mueve a Node o llama un Worker dedicado.
- **Timeout vs render largo**: 15 min < render de video. **No esperes el resultado dentro de la función**:
  patrón submit→poll/webhook (ver [[115-async-render-largo-poller-durable]]).
- **Cold start sobre DB**: conexión nueva por arranque mata latencia → usa pooler/HTTP-DB o mantén Fluid caliente.

## Regla de decisión
1. ¿Solo Web APIs, respuesta <300s, latencia global crítica? → **Edge/isolate** (o Worker CF).
2. ¿`fs`, SDK Node, ffmpeg, hasta 15 min? → **Node / Lambda** con Fluid Compute.
3. ¿Trabajo > 15 min o GPU? → **ni una ni otra**: cola + worker durable, función solo orquesta.

Cruza con [[73-edge-computing-wasm]] y [[299-deploy-vercel-render-fly-railway]].

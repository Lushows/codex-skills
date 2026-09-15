# 355 · Patrones de live-update: polling vs push, optimistic, invalidación

> El transporte ([[352-websockets-sse-webrtc-deep]]) mueve bytes; este es el patrón de
> *aplicación*: cuándo refrescas, cómo mantienes el cache fresco y cómo mientes bien (optimistic).

## Polling vs push: elige por frescura y costo
| Patrón | Latencia | Costo | Cuándo |
|---|---|---|---|
| **Polling fijo** | = intervalo | alto (requests vacías) | datos que cambian raro; simplicidad |
| **Polling adaptativo** | variable | medio | acelera al haber actividad, frena en idle |
| **Long-poll** | ~push | medio | sin infra WS, frescura casi-instantánea |
| **SSE push** | instantánea | bajo (1 conexión) | server→client: feeds, progreso, tokens LLM |
| **WS push** | instantánea | bajo | bidireccional, cancel client→server |

Default 2026: **push (SSE)** para server→client; polling solo para datos perezosos o cuando no puedes mantener conexiones. Polling con `stale-while-revalidate` da UX decente sin sockets.

## Optimistic UI: mentir y reconciliar
Actualiza la UI **antes** de que el server confirme; revierte si falla.
1. Snapshot del estado actual (para rollback).
2. Aplica el cambio optimista al cache → la UI responde en 0ms.
3. Dispara la mutación.
4. **onError**: restaura el snapshot + toast. **onSuccess**: reemplaza con la verdad del server (puede traer campos que no adivinaste: id, timestamps).
5. **Siempre invalida/refetch** al final para reconciliar con el estado real.

TanStack Query: `onMutate`/`onError`/`onSettled`. SWR: `mutate(key, fn, { optimisticData, rollbackOnError })`. Imprescindible: que el server devuelva **el recurso final**, no solo 200 — así no adivinas el id real.

## Invalidación de cache: el problema difícil
- **TanStack Query**: `queryKey` jerárquico = namespace. `invalidateQueries(['orders'])` limpia todo lo que empiece por `orders` (lista, detalle, filtros). Invalidación amplia o quirúrgica con una llamada. Por eso domina 2026 (~12M dl/sem vs 7.7M de SWR) [no verificado cifras].
- **SWR**: `mutate` con key-matching; wildcard necesita `unstable_serialize` o enumerar keys a mano → más bookkeeping.
- **Push-driven invalidation**: el evento del server (vía SSE/WS) trae el `entityId` cambiado → invalidas **solo esa key** en vez de refetchear todo. El patrón ganador: WS no manda *el dato*, manda "**la entidad X cambió**" → el cliente decide refetchear o aplicar el delta. Evita confiar en payloads de WS como fuente de verdad (pueden llegar desordenados).

## Suscripciones: entrega del delta
- **Server manda solo el id/evento** ("order 42 → shipped"), cliente refetch del recurso → simple, consistente, robusto a reordenamientos. Default.
- **Server manda el delta completo** → menos requests pero exige orden garantizado y dedup por `seq` ([[352-websockets-sse-webrtc-deep]]); úsalo solo en flujos de alto volumen donde el refetch sea caro.
- **Reconciliar al reconectar**: tras un blip, **refetchea las queries activas** (TanStack lo hace en `refetchOnReconnect`) — los eventos perdidos durante la caída se recuperan por refetch, no por replay. Cinturón y tirantes.

## Streaming LLM (caso del agente)
- Tokens por **SSE** al dashboard (server→client, simple, reconecta solo).
- **Cancelación**: SSE no tiene canal de vuelta → si el usuario abandona, detecta `request.is_disconnected()` en el server y **aborta la llamada LLM** (no quemes tokens en streams huérfanos). Si necesitas cancel explícito desde el cliente, sube a **WS** y manda un frame `{cancel}`.
- **Progreso de jobs** (render de video, etc.): mismo SSE con eventos `{stage, pct}`; el cliente actualiza la barra sin polling.

## Coalescing y backpressure
Cuando los eventos llegan más rápido que lo que el cliente puede renderizar, no apliques uno a uno:
- **Debounce de invalidación**: varios eventos de la misma key en <100ms → una sola invalidación/refetch al final, no N.
- **Coalesce de deltas**: acumula deltas en un buffer y aplica en el siguiente frame (`requestAnimationFrame`) → un repaint, no veinte. Crítico en feeds de alta frecuencia (tickers, logs).
- **Backpressure**: si el cliente se ahoga, el server debe poder **dropear** updates intermedios y mandar solo el último estado (last-value-wins por key) — útil en dashboards donde solo importa el valor actual, no cada paso.
- **Pausa en background**: con `visibilitychange` oculto, frena polling y descarta updates no críticos; reanuda + refetch al volver al foreground.

## Gotchas
1. **Optimistic sin rollback** = UI miente permanentemente al fallar. Siempre snapshot + revert.
2. **No invalidar tras la mutación** deja cache divergente del server (el bug clásico "no se actualiza hasta refrescar").
3. **Confiar en el payload de WS como verdad**: llegan desordenados/duplicados → trata el push como *señal de invalidación*, refetchea la verdad.
4. **Polling agresivo** quema batería/cuota; hazlo adaptativo (frena al pasar a background con `visibilitychange`).
5. **Doble fuente** (push + polling simultáneos) genera flicker y carreras → elige uno por query.

Cruza con [[280-data-fetching-caching-frontend]], [[352-websockets-sse-webrtc-deep]] y [[353-crdt-collab-yjs]].

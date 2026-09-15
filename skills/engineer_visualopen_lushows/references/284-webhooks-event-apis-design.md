# 284 · Diseñar webhooks salientes (firma, reintentos, idempotencia, versiones)

> [[141-webhooks-hmac-idempotencia-dlq-jobs-gpu]] cubre *recibir/verificar* webhooks en el worker GPU;
> esto es el lado **emisor**: cómo *tú* publicas eventos a terceros sin que pierdan, dupliquen o falsifiquen nada.

## El evento como recurso versionado
Un webhook entrega un **evento inmutable**, no un comando. Estructura mínima:
```json
{ "id":"evt_01H...", "type":"video.render.completed", "api_version":"2026-01-15",
  "created":"2026-06-07T12:00:00Z", "data":{ "job_id":"...", "url":"..." } }
```
- `id` único (ULID/UUIDv7) → el receptor deduplica por él (idempotencia del lado de ellos).
- `type` con namespace jerárquico (`recurso.acción`) → permite suscripción granular y filtrado.
- **`api_version` pineada por endpoint**: nuevos campos no rompen suscriptores viejos; bumps mayores conviven
  (entregas la versión que el suscriptor configuró). Versiona el **payload**, igual que el contrato REST en [[282-rest-openapi-a-fondo]].
- **Thin vs fat payload**: thin manda solo `id`+`type` y el receptor hace `GET` (evita datos stale/grandes y fugas);
  fat manda el objeto entero (menos round-trips, más riesgo de orden/stale). Para media generada, thin + URL firmada.

## Firma: Standard Webhooks (HMAC-SHA256)
Estándar de facto en jun-2026: **Standard Webhooks** (equipo Svix; adoptado por OpenAI, **Anthropic**, Gemini,
Supabase, Twilio, PagerDuty). Tres headers:
- `webhook-id` (= `id` del evento), `webhook-timestamp` (epoch), `webhook-signature`.
- Firma = `HMAC-SHA256(secret, "{id}.{timestamp}.{body}")`, base64, **prefijada por versión**: `v1,<sig>`
  (simétrica) / `v1a,<sig>` (asimétrica). El header lista múltiples firmas separadas por espacio.
- **Rotación de secret**: durante la ventana firmas con el viejo *y* el nuevo (`v1,sigA v1,sigB`) → el receptor
  acepta si cualquiera valida; luego retiras el viejo. Cero downtime.
- **Anti-replay**: el receptor rechaza si `|now - timestamp| > 5 min`. Compara firmas en tiempo constante.

## Entrega: reintentos, orden, idempotencia
- **At-least-once**: asume que el receptor verá duplicados → tu deber es dar `id` estable; el suyo, deduplicar.
- **Backoff exponencial con jitter**: ej. 0s, 30s, 2m, 10m, 1h, 6h... hasta ~24h. `2xx` = éxito; resto = retry.
  Respeta `Retry-After` si lo devuelven. (Implementación: una cola de jobs, ver [[285-background-jobs-queues-web.md]] vía [[23-event-driven-colas]].)
- **Orden NO garantizado**: la red y los retries reordenan. Incluye `created` y/o un `sequence` por recurso para
  que el receptor descarte eventos viejos. No asumas "completed" llega después de "started".
- **Idempotencia del emisor**: persiste `(endpoint, event_id)` ya entregado → no re-disparas el mismo evento si tu
  productor re-corre (cf. [[141-webhooks-hmac-idempotencia-dlq-jobs-gpu]]).

## Resiliencia operativa
- **Auto-disable + alerta**: tras N fallos consecutivos (ej. 5 días de 4xx/5xx) deshabilita el endpoint y notifica
  al dueño → no quemas cómputo reinteleando un endpoint muerto para siempre.
- **DLQ + replay manual**: eventos agotados van a una cola muerta; expón un botón "reenviar" y un log de entregas
  (status, latencia, intento) por evento — soporte y debugging lo exigen.
- **SSRF**: el receptor URL lo pone el cliente → valida que no apunte a `169.254.169.254`/IPs privadas/localhost,
  resuelve DNS y revalida la IP, bloquea redirects a rangos internos. (Mismo vector que en [[141-webhooks-hmac-idempotencia-dlq-jobs-gpu]].)

## ¿Webhook, polling o SSE/WebSocket?
| Mecanismo | Cuándo |
|---|---|
| **Webhook** | notificación push servidor→servidor, baja frecuencia, receptor con endpoint público |
| **Polling** (`GET /events?after=cursor`) | receptor detrás de firewall, o quiere control de ritmo; siempre ofrécelo como fallback |
| **SSE / WebSocket** | push a un **browser/cliente** en vivo (progreso de render), no integración B2B |

Ofrece **siempre** un endpoint de polling de eventos: webhooks se pierden, el polling es la red de seguridad.

## Gotchas
1. Firmar el body **parseado** (re-serializado) rompe la firma → firma los **bytes crudos** recibidos/enviados.
2. Timeout corto del receptor + payload fat → entrega falla; usa thin payload o sube el timeout pactado.
3. Sin `event_id` estable, el receptor no puede deduplicar → garantízalo aunque reintentes.
4. Reintentar sobre `2xx` lento (no `4xx/5xx`) duplica innecesariamente — define éxito = cualquier `2xx`.

Cruza con [[141-webhooks-hmac-idempotencia-dlq-jobs-gpu]] y [[23-event-driven-colas]].

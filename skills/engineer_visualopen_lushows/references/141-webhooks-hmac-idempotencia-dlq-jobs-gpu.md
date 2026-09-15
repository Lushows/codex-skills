# 141 · Webhooks de "job terminó": HMAC, idempotencia, DLQ

> El webhook ahorra el poll constante, pero un endpoint que confía en cualquier POST es un agujero:
> spoofing, replays, doble-cobro, y jobs que mueren en silencio. Recibir el "job terminó" bien =
> firma + anti-replay + idempotencia + DLQ. El webhook acelera; el poller de [[115]] es la red.

## Por qué el webhook NO basta solo
- Se **pierde** (red, deploy a mitad de entrega, 5xx tuyo) → job huérfano.
- Se **duplica** (el proveedor reintenta) → procesas dos veces → doble guardado / doble cobro.
- Se **falsifica** (cualquiera conoce tu URL pública) → guardas un MP4 atacante.
Regla: webhook + poller durable juntos = *exactly-once efectivo*. El webhook dispara rápido; si falla,
el `setInterval` del poller cierra el trabajo igual (idempotente).

## 1. Verificar firma HMAC
El proveedor firma el **cuerpo crudo** (raw bytes, antes de parsear JSON) con un secreto compartido.
Compara en tiempo constante.
```js
import crypto from 'crypto';
function verify(rawBody, header, secret) {
  const expected = crypto.createHmac('sha256', secret).update(rawBody).digest('hex');
  const got = Buffer.from(header || '', 'utf8');
  const exp = Buffer.from(expected, 'utf8');
  return got.length === exp.length && crypto.timingSafeEqual(got, exp); // anti timing-attack
}
```
Gotchas que muerden:
- **Body crudo**: firma sobre los bytes exactos. Si Express ya hizo `JSON.parse`, el re-`stringify`
  reordena claves → firma no coincide. Usa `express.raw({type:'application/json'})` en esa ruta.
- `timingSafeEqual` **tira** si los buffers tienen distinta longitud → chequea longitud antes.
- No uses `==` sobre strings de firma (filtra por timing). Detalle OWASP en [[27-seguridad-apps-owasp]].

## 2. Anti-replay (timestamp)
Aunque la firma sea válida, un atacante puede **reenviar** un webhook capturado. El proveedor manda un
timestamp; inclúyelo en la base firmada y rechaza lo viejo:
```js
const ts = Number(req.header('X-Timestamp'));
if (Math.abs(Date.now()/1000 - ts) > 300) return res.sendStatus(403); // ventana 5 min
// y firma sobre `${ts}.${rawBody}` para que el ts no se pueda alterar sin romper el HMAC
```

## 3. Idempotencia (no procesar dos veces)
Clave de idempotencia = `jobId` (o `eventId` del proveedor). Persistir el "ya visto" **antes** de
ejecutar el efecto. Dos niveles:

| Nivel | Mecanismo | Cuándo |
|---|---|---|
| Rápido | `INSERT ... ON CONFLICT DO NOTHING` en tabla `processed_events(jobId PK)` | si hay Postgres |
| De archivo | la pieza ya tiene `videoFile` + se borró su `.json` (ver [[115]]) | stack en disco |

```js
const fresh = await db.query(
  'INSERT INTO processed_events(job_id) VALUES($1) ON CONFLICT DO NOTHING RETURNING job_id', [jobId]);
if (fresh.rowCount === 0) return res.sendStatus(200); // ya procesado → ACK y salir
await finalizeJob(jobId);  // descarga MP4, guarda, cobra
```
La marca de idempotencia es la **misma** que usa el poller, así webhook y poll no se pisan: el que
llegue segundo ve "ya guardado" y no hace nada. Eso es el exactly-once efectivo.

## 4. ACK rápido, trabajo en background
Responde `200` en <1-2s y haz el trabajo pesado (descargar el MP4 de 200MB) **fuera** del request: si
tardas, el proveedor cree que falló y reintenta → más duplicados. Encola (ver [[23-event-driven-colas]]) y devuelve.

## 5. Reintentos con backoff + DLQ
Tu finalización puede fallar transitoriamente (R2 caído, OOM al transcodificar). No la pierdas:
```
attempt → falla → reencola con delay = min(base·2^n, cap) + jitter   (n=intento)
n=1:2s  n=2:4s  n=3:8s ... cap 5min ; jitter ±20% para evitar thundering herd
```
Tras `MAX_RETRIES` (p.ej. 6) → mueve a **dead-letter queue**: una tabla/cola `jobs_dlq` con el
payload, el último error y el contador. La DLQ es para inspección humana, no se reintenta sola.
```js
if (attempt >= MAX_RETRIES) { await dlq.put({jobId, payload, lastError, attempts: attempt}); alert(jobId); }
else schedule(jobId, backoff(attempt));
```
Gotchas:
- **Idempotencia ⇒ reintentos seguros**: solo puedes reintentar sin miedo porque `finalizeJob` es
  idempotente. Sin idempotencia, cada reintento es un riesgo de duplicado.
- **DLQ con runbook**: cada item debe poder re-drenarse a mano tras arreglar la causa (un botón
  "reprocesar" que vuelve a llamar `finalizeJob` — idempotente, así que es seguro).
- **Alerta**: un item en DLQ = un video que el cliente NO recibió. Notifica (Slack/operador), no lo
  dejes morir en una tabla que nadie mira.

## Checklist de endpoint seguro
- [ ] `express.raw` (body crudo) · HMAC con `timingSafeEqual` + chequeo de longitud.
- [ ] Timestamp en la base firmada + ventana ±5 min · idempotencia persistida **antes** del efecto.
- [ ] ACK <2s, finalización en background · backoff con jitter + DLQ con alerta y reproceso manual.
- [ ] Poller de [[115]] activo como red de seguridad si el webhook se pierde.

Cruza con [[115-async-render-largo-poller-durable]], [[23-event-driven-colas]] y
[[27-seguridad-apps-owasp]].

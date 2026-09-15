# 36 — Tiempo real, notificaciones & colaborativo (apps que se sienten vivas)

Linear/Figma/Notion/Slack combinan 3 ingredientes ortogonales: **optimistic UI** (latencia cero local), **real-time** (cambios de otros llegan solos) y **presence** (ves a quién hay). **Léelo cuando construyas dashboards en vivo, chat, colaboración, o sistemas de notificaciones.** Pareja de 13 (app UI), 18 (AI UI).

## 1. Transporte & arquitectura

**Decisión rápida:**
- **SSE (Server-Sent Events)** → **unidireccional** servidor→cliente (feeds de notificaciones, progreso de job, streaming de LLM). HTTP plano, atraviesa proxies/CDN, **reconecta solo** (`Last-Event-ID`), sin librería. **Default del 80% de dashboards.**
- **WebSocket** → **bidireccional** baja latencia (chat, colaboración, cursores). Tú gestionas reconexión + heartbeat.
- **Long-polling** → fallback legacy.
- **WebTransport (HTTP/3)** → multiplexa streams + datagramas (cursores donde perder un frame da igual). Chrome/Edge sí, **Safari no** → enhancement con fallback a WS.
**Stack manejado (no construyas WS a mano):** **Liveblocks** (presencia+Yjs+comentarios, el más producto-listo) · **PartyKit** (Cloudflare Durable Objects, rooms) · **Convex** (backend reactivo, queries que se re-ejecutan solas) · **Pusher/Ably** (pub/sub clásico) · **Supabase Realtime** (Postgres broadcast/presence).
**Cliente SSE mínimo (con UX de "¿conectado?"):**
```js
function connect(){
  const es=new EventSource('/api/stream');
  es.onopen=()=>setStatus('connected');       // punto verde
  es.onerror=()=>setStatus('reconnecting');    // reintenta solo
  es.addEventListener('notification', e=>inbox.add(JSON.parse(e.data))); // dedupe por id
}
```
**Cliente WS robusto** = reconexión con **backoff exponencial + jitter** + heartbeat (ping/pong ~25s) + **cola mientras `readyState!==OPEN`** que se vacía al reconectar. Nunca asumas la conexión viva: hazla **visible** (verde/ámbar/rojo, "Reconectando…"). Una app que congela en silencio se siente rota.

## 2. Optimistic UI & sync engines

**El patrón** (el corazón del "instant" de Linear): aplica el cambio en local **ya**, encólalo, **rollback** si falla:
```js
async function toggleDone(id, value){
  const prev=store.get(id);
  store.patch(id,{done:value,_pending:true});            // 1. instantáneo
  try{ const fresh=await api.update(id,{done:value}); store.patch(id,{...fresh,_pending:false}); } // 2-3. envía+reconcilia
  catch(e){ store.set(id,prev); toast.error('No se pudo guardar'); }  // 4. rollback
}
```
Claves: **rollback con snapshot** · **mutation queue** ordenada (no dispares la 2ª mutación de una entidad hasta cerrar la 1ª) · **reconciliación por server truth** (tu optimista era una *predicción*). Optimistic = *tu* cambio se ve ya; real-time = el cambio de *otro* llega solo. Linear se siente mágico porque hace **ambos sobre un sync engine local**.
**Local-first / sync engines (la ola 2026):** gestionan cola offline + reconciliación + reactividad por ti. **Zero** (Rocicorp, mejor DX web reactiva, React-only) · **ElectricSQL** (Postgres→SQLite local, offline real) · **Convex** (backend reactivo completo) · **InstantDB** · **TinyBase** (store local pequeño) · **PowerSync** (battle-tested móvil) · **Yjs** (texto/colaborativo). Decisión: ElectricSQL=camino simple a local-first con Postgres · PowerSync=producción/móvil · Zero=mejor DX web · Convex=backend entero reactivo.

## 3. Presence & awareness

Presence = estado **efímero** por usuario (cursor, selección, "escribiendo"), no persistido, expira al desconectar (TTL/heartbeat). Canal separado del documento.
```js
room.updatePresence({cursor:{x,y}, selection:ids});
room.subscribe('others', others=>renderCursors(others));   // Liveblocks
// Yjs: provider.awareness.setLocalStateField('cursor',{x,y})
```
- **Live cursors (efecto Figma):** **throttle** a ~30-60ms (no por cada `mousemove`), interpola con CSS transform/rAF para fluidez. Color + nombre por usuario, fade-out al inactivar.
- **Typing indicator:** envía `typing:true` + `setTimeout` que lo apaga a ~3s (debounce). Nunca persistas.
- **Avatar stack:** 3-5 + "+N", dedupe por usuario (no por pestaña).
- **Heartbeat:** sin ping en X seg → offline (`beforeunload` no es fiable; confía en el TTL del servidor).
- **"X está editando":** lock **suave** (aviso, no bloqueo duro) — los CRDTs evitan el bloqueo real.

## 4. Edición colaborativa (con aviso de complejidad)

**CRDT vs OT:** en 2026 **los CRDTs ganaron** para la mayoría y **Yjs es el estándar** (texto/canvas/listas/mapas). OT (Google Docs clásico) requiere servidor central que transforma operaciones (más control, mucho más difícil). CRDT converge sin servidor autoritario, offline-first.
```js
import * as Y from 'yjs'; import {WebsocketProvider} from 'y-websocket'
const doc=new Y.Doc(); new WebsocketProvider('wss://srv','room-id',doc)
const text=doc.getText('content')   // bindings: TipTap, ProseMirror, Monaco, Lexical
```
**Aviso honesto:** colaboración real es **cara** (merge UX, version history = snapshots + GC, comentarios anclados a rangos con *relative positions*, garbage collection de memoria). **No la construyas desde cero** — usa Yjs + binding maduro o Liveblocks. Si solo necesitas "varios ven la misma lista", un broadcast simple basta (no metas CRDT).

## 5. Sistemas de notificaciones (anatomía)

**Tipos (no los mezcles en un canal):** transaccional ("tu pedido se envió"), social ("te mencionaron"), sistema ("nuevo login"), marketing (separado, opt-in).
**Inbox vs Feed:** para SaaS casi siempre **Inbox** (read/unread + acciones, tipo email), no Feed.
**Anatomía del notification center:**
```
[🔔 badge: 3] ← NO-LEÍDAS (no total), tope "9+"
 └─ Panel: tabs por categoría · item (avatar+texto+timestamp relativo+dot no-leído+acción inline)
    · agrupación ("10 comentarios nuevos", no 10 filas) · "Marcar todo leído" · auto-archivo 30d · empty state
```
**Batching/grouping (anti-spam, lo más importante):** agrupa por hilo/entidad en ventana de inactividad o conteo máx. "10 comentarios nuevos" = mismo valor informativo con 1/10 de la interrupción. Es **primitiva de infraestructura**, no un `if` — por eso existen **Courier, Knock, SuprSend, Novu**.
**Canales — estrategia:** in-app (siempre, barato) · push (urgente, interrumpe) · email (asíncrono, durable). Regla: *email para lo que espera, push para lo que no, in-app para todo*. Respeta preferencias por categoría×canal. **iOS:** Web Push solo si la PWA está instalada en pantalla de inicio → no cuentes con push web en iOS para usuarios normales (usa in-app + email).
**Entrega real-time:** SSE empuja al inbox; actualiza el badge optimistamente al marcar leído (rollback si falla); dedupe por `id`.

## 6. Patrones 2026 & anti-patrones

**Qué se siente vivo y rápido:** optimistic (0ms) + real-time (cambios ajenos solos) + presence, todo sobre store local reactivo. **Actividad de IA/agentes en vivo** es el nuevo frente: muestra el agente como "participante" con cursor/estado ("Claude está editando…", streaming de tokens) reutilizando presence/streaming. El movimiento **local-first** (Zero/Electric/Convex) es la tendencia dominante.

### Anti-patterns — blacklist
una notificación por evento (10 comentarios = 10 pings → **agrupa SIEMPRE**) · badge con el total en vez de no-leídas · push para todo · **"todo se mueve"** (listas que reordenan bajo el dedo mientras lee → acumula y muestra tras botón **"3 nuevos ↑"**) · conexión muerta silenciosa (hazla visible) · optimistic sin rollback (la UI miente) · mutaciones concurrentes sin cola · enviar cada `mousemove` sin throttle · CRDT por defecto donde un broadcast basta (sobre-ingeniería + fuga de memoria) · auto-dismiss de errores accionables · re-render de toda la lista por cada evento (usa updates granulares, keys estables, memo, virtualización) · marketing en el mismo canal que transaccional.

**Regla de oro:** lo que el usuario hizo debe sentirse **instantáneo** (optimistic); lo que hicieron otros debe **avisar sin interrumpir** (batch + "nuevos ↑"); y el sistema debe **decir siempre la verdad** sobre su estado (conectado/sincronizando/error).

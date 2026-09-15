# 354 · Presence y cursores en vivo: awareness, avatares, typing y escala

> Presence es el canal **efímero** que da vida a una app colaborativa: quién está,
> dónde apunta su cursor, qué escribe. Reglas distintas al doc persistente de [[353-crdt-collab-yjs]].

## Por qué presence es su propio canal
El estado del documento debe **persistir y converger**; la presencia debe **expirar sola**. Mezclarlos es el error nº1: si guardas cursores en el `Y.Doc`, infla el CRDT con tombstones para siempre y replicas posiciones obsoletas. Presence vive en un canal paralelo, **last-write-wins**, sin historial, con **TTL**.

## El protocolo awareness (Yjs)
Cada cliente publica un **state local** (objeto JSON arbitrario) asociado a su `clientID`; el resto lo recibe vía broadcast. No hay merge: es reemplazo total por cliente.
```js
provider.awareness.setLocalStateField('user', { name:'Ana', color:'#e11', cursor:{ anchor, head } })
provider.awareness.on('change', ({ added, updated, removed }) => render(provider.awareness.getStates()))
```
- **Heartbeat implícito**: si un cliente deja de refrescar (cierre de pestaña, crash), los demás expiran su estado tras ~30s → desaparece de la lista sin necesidad de un "leave" explícito.
- **Tamaño**: el state se rebroadcasta entero en cada cambio → mantenlo **pequeño** (nombre, color, posición). No metas el objeto user completo.

## Cursores y selección
- **Posición estable**: no guardes offsets numéricos crudos (se desincronizan al editar otros). Usa **relative positions** de Yjs (`Y.createRelativePosition`) que se reanclan tras inserciones/borrados concurrentes. Sin esto, el cursor remoto "salta" al teclear.
- **Throttle**: mousemove dispara ~60–120 ev/s; throttlea a **~20–30/s** (cada 30–50ms) antes de broadcastear. A 50 usuarios sin throttle son miles de mensajes/s inútiles.
- **Interpolación**: en el receptor, anima el cursor entre updates (lerp) para que se vea fluido pese a recibir a 20Hz.

## Typing indicators y selección de rango
- **Typing**: estado booleano con **auto-expiry** (debounce: set `typing:true` al teclear, `false` tras 2–3s sin teclas). Nunca lo persistas.
- **Selección remota**: pinta el rango con el color del usuario + label flotante con su nombre; usa el mismo color en cursor, avatar y selección para identificación instantánea.

## Avatares / lista de presentes
- **Facepile**: deriva la lista de `awareness.getStates()`; dedup por user-id (un user con 2 pestañas = 2 clientIDs → colapsa a un avatar con badge "2").
- **Color determinista**: hashea el user-id a un color de paleta accesible → mismo usuario, mismo color en todas las sesiones.

## Escala: presence es más caótico que el doc
El doc cambia cuando alguien edita; la presence cambia **constantemente** (cada movimiento de ratón). Es el canal de mayor volumen.
- **Backplane separado**: presence por **Redis Pub/Sub** (efímero, fire-and-forget — perderlo no importa, se reemite al siguiente movimiento), no por el stream persistente del doc ([[352-websockets-sse-webrtc-deep]]).
- **Estado en Redis con TTL**: hash por sala `presence:{room}` con TTL refrescado por heartbeat; al expirar, broadcast de `leave`. Nunca en memoria de proceso (se pierde en restart, invisible a otros pods).
- **Sharding por sala**: presence de una sala solo toca el pod dueño de esa sala (consistent hashing) → un mar de cursores no inunda toda la flota.
- **WebRTC datachannel** para cursores cuando la latencia <50ms es crítica (whiteboard, juego): UDP sin head-of-line block, peer-to-peer; cae a SFU >~10 peers ([[356-video-audio-calls-livekit.md]]).

## Viewport y "follow"
- **Follow mode**: un user puede "seguir" a otro → su viewport se ancla al de él. Implementa publicando el rect de scroll/zoom en el awareness state; el seguidor reposiciona su cámara con cada update (con interpolación para no marear).
- **Spotlight / "jump to"**: avatar clicable que hace scroll a la posición del otro → lee su `cursor`/viewport del awareness y anima. UX clave en docs largos.
- **Densidad**: con >20 cursores en pantalla, agrupa los lejanos en un contador en el borde ("+12") y muestra solo los del viewport visible; pintar 50 labels satura.

## Sin Yjs: presence en cualquier app
No necesitas CRDT para tener presence. El patrón es transporte-agnóstico:
- Cliente emite `{userId, cursor, lastSeen}` por WS/SSE cada ~30–50ms (throttled).
- Server mantiene `presence:{room}` en Redis (hash con TTL ~10s, refrescado por cada update) y rebroadcasta a la sala.
- Un barrido (o TTL) expira los ausentes → `leave`. Idéntico a awareness de Yjs pero a mano; úsalo en dashboards/whiteboards sin doc colaborativo.

## Gotchas
1. **Cursor en el Y.Doc** = CRDT hinchado permanente. Siempre awareness.
2. **Offsets absolutos** se desincronizan con ediciones concurrentes → relative positions.
3. **Sin throttle** mousemove satura el backplane; sin interpolación se ve a tirones.
4. **Multi-pestaña** = múltiples clientIDs del mismo user → dedup en la facepile.
5. **Sin TTL/expiry**, los fantasmas (pestañas crasheadas) se quedan "online" para siempre.
6. **Managed** (Liveblocks Presence, PartyKit) resuelve todo esto sin infra — pésalo si no quieres mantener Redis+sharding.

Cruza con [[353-crdt-collab-yjs]] y [[352-websockets-sse-webrtc-deep]].

# 86 — Real-time collaboration & CRDTs

## CRDT vs OT
**CRDT** (Conflict-free Replicated Data Type) = estructura con merge automático garantizado matemáticamente, sin
servidor central. **OT** (Operational Transformation, el viejo Google Docs) transforma ops entre sí y **requiere
servidor central**. Regla 2026: P2P/local-first → CRDT; server-authoritative → OT, pero la mayoría de builds nuevos usan CRDT (tolera offline+P2P). Tradeoff CRDT: overhead de metadata (tombstones), mitigado con encoding columnar.

## Yjs (el estándar)
~900k+ downloads/semana. Tipos compartidos `Y.Map/Y.Array/Y.Text/Y.XmlFragment` que auto-mergean. Bindings:
ProseMirror/TipTap, Lexical, CodeMirror, Monaco, Slate. **Dos canales ortogonales:** document sync (CRDT) y **awareness** (presencia efímera — cursores, no persistida).
```js
import * as Y from 'yjs'; import { WebsocketProvider } from 'y-websocket'
const doc = new Y.Doc(); const provider = new WebsocketProvider('wss://host','room-1',doc)
provider.awareness.setLocalStateField('user', { name:'Ana', color:'#e11' })
const text = doc.getText('content')
```
Providers: **y-websocket** (relay central, fácil), **y-webrtc** (P2P, necesita signaling), **y-indexeddb** (offline), **Hocuspocus** (backend Yjs production con auth).

## Managed / otros
**Liveblocks** (WebSocket + storage + Presence + Comments + Yjs, cero infra). **PartyKit** (Cloudflare, Durable
Objects con API amigable). **Automerge** (JSON CRDT, version history, Peritext rich-text). **Loro** (Rust, rising).
**Local-first sync engines:** ElectricSQL ("Durable Sync" sobre Postgres), Zero (Rocicorp, mejor DX web), PowerSync — NO son CRDTs puros (sync engines, last-write-wins/server-resolved); úsalos para apps DB-backed, Yjs/Automerge para rich-text.

## Gotchas
1. Awareness es **efímera** — nunca guardes cursores/presencia en el Y.Doc; infla el CRDT persistente para siempre.
2. La metadata CRDT crece con el nº de ediciones; snapshot/compacta periódicamente.
3. y-webrtc necesita signaling y colapsa a escala — usa y-websocket/Hocuspocus para >~10 peers.
4. Formateo rich-text concurrente (bold/italic solapados) es el caso duro — solo Peritext/Yjs-XML lo manejan bien.
5. No mezcles modelos OT y CRDT — CRDT no tiene "rebase" ni autoridad que rechace una edición.
6. y-indexeddb es por-origin; iOS Safari puede evictar tras ~7 días de inactividad.

**Fuentes:** github.com/yjs/yjs · docs.yjs.dev · liveblocks.io/blog · electric-sql.com.

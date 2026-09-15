# 353 · Colaboración a fondo: CRDT, Yjs, sync, offline y conflictos

> [[86-realtime-collaboration-crdt]] da el mapa; aquí entras al motor: cómo Yjs
> codifica el doc, cómo sincronizas con menos bytes, y qué hacer con offline y growth.

## El modelo mental de Yjs
Un `Y.Doc` es una secuencia de **structs** (Item) inmutables identificados por `(clientID, clock)` — un reloj de Lamport por cliente. Insertar nunca borra: marca **tombstones** (deleteSet). El merge es determinista porque el orden total se deriva de IDs, no de wall-clock. Por eso dos peers que aplican las mismas ops en distinto orden **convergen** al mismo estado.

- **State vector**: mapa `clientID → clock` = "qué he visto de cada cliente". Es la clave del sync diferencial.
- **Update**: blob binario de structs nuevos. Codificación **columnar (v2)** comprime brutalmente ediciones secuenciales.

## Sync protocol (2 mensajes, no "mandar todo")
1. Peer A manda su **state vector** (`Y.encodeStateVector(doc)`).
2. Peer B responde con `Y.encodeStateAsUpdate(doc, svA)` = **solo el delta** que A no tiene.
3. Simétrico al revés. Tras eso, updates incrementales en vivo.

Esto es lo que hace `y-websocket`/Hocuspocus por debajo. Nunca serialices el doc completo en cada cambio: manda el update binario del evento `doc.on('update')`.

## Rendimiento 2026 (medido, [no verificado] cifras exactas)
| Lib | Velocidad | Bundle | Fuerte en |
|---|---|---|---|
| **Yjs** | el más rápido, ~26k–156k ops/s | pequeño | text, ecosistema enorme (920k dl/sem) |
| **Loro** (Rust/WASM) | comparable/mejor en docs gigantes | medio | muchos editores concurrentes, perf-critical |
| **Automerge 2.x** | mejoró ~3x (260k keystrokes ~600ms) | grande | **historial/branching como feature** |
| **Liveblocks** | managed (no compites en perf) | — | cero infra, presence+comments |

Default sin razón en contra: **Yjs**. Necesitas version history/attribution como producto → Automerge. Docs enormes + muchos editores → evalúa Loro.

## Offline-first
- **y-indexeddb**: persiste el doc local; al volver online, el sync protocol reconcilia el delta automáticamente. El usuario edita sin red y converge sin conflictos visibles — la ventaja real del CRDT.
- **Eviction**: IndexedDB es por-origin; **iOS Safari** puede evictar tras ~7 días de inactividad → no asumas durabilidad; ten el servidor como fuente persistente.
- **Snapshot inicial**: carga local primero (instantáneo), luego sincroniza con server (background) — patrón local-first puro.

## Growth de metadata: el impuesto del CRDT
Tombstones + clocks crecen con el **nº de ediciones**, no con el tamaño del texto. Un doc muy editado se hincha aunque tenga 2 párrafos.
- **GC de tombstones**: Yjs hace GC de contenido borrado por defecto (deja un marcador delgado).
- **Snapshot + compactación**: persiste `encodeStateAsUpdate` periódicamente y descarta el log de updates viejos. En Hocuspocus, debounce de persistencia.
- **No metas presencia en el doc**: cursores van por **awareness** (efímero), nunca en el `Y.Doc` persistente — los inflarías para siempre (ver [[354-presence-cursors]]).

## Backend: no inventes el servidor
- **Hocuspocus**: server Yjs production-ready (auth hooks, persistencia Postgres/SQLite, webhooks, debounce). Default self-hosted.
- **Liveblocks / PartyKit (Cloudflare Durable Objects)**: managed; un DO por sala = autoridad de sync natural y barata.
- **Persistencia**: guarda el update binario en una columna `bytea`/`BLOB`, no JSON. Y guarda **snapshots**, no el log entero.

## Auth y permisos (lo que el CRDT no resuelve)
El CRDT garantiza convergencia, **no autorización**. Cualquiera con el update binario puede aplicarlo.
- **Gate en el provider**: Hocuspocus `onAuthenticate` valida el JWT antes de unir a la sala; rechaza → no recibe ni emite updates.
- **Permisos por sub-documento**: read-only se hace **no aceptando** updates de ese cliente en el server (el cliente puede editar local, pero el server descarta y no propaga). No hay "campo read-only" nativo en el CRDT.
- **No confíes en el cliente**: valida en el server qué docs puede ver/editar cada user; el merge no filtra.

## Gotchas
1. **Rich-text concurrente** (bold/italic solapados) es el caso duro: usa binding XML de Yjs (ProseMirror/TipTap/Lexical) o Peritext (Automerge); no lo resuelvas a mano.
2. **y-webrtc** colapsa a escala (signaling + full-mesh): >~10 peers → y-websocket/Hocuspocus.
3. **No mezcles OT y CRDT**: CRDT no tiene "rebase" ni autoridad que rechace una edición; si necesitas validación server-authoritative, CRDT no es la herramienta.
4. **Sync engines DB-backed** (ElectricSQL, Zero, PowerSync) **no son CRDTs puros** (resuelven last-write-wins/server) — úsalos para apps DB-backed, Yjs/Automerge para rich-text colaborativo.
5. **clientID colisión**: aleatorio de 32 bits; en flotas enormes considera el riesgo de colisión (raro pero corrompe el merge).

Cruza con [[86-realtime-collaboration-crdt]], [[354-presence-cursors]] y [[335-offline-sync-mobile]].

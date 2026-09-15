# 335 · Offline-first / sync móvil (DB local, outbox, resolución de conflictos)

> Una app de avatares/IA debe usarse en el metro sin señal: el usuario edita, encola y la verdad se reconcilia al volver online.
> Offline-first no es "cachear GETs"; es tratar la DB local como fuente primaria y sincronizar como efecto secundario.

## Tres niveles de "offline"
1. **Cache de lectura** (React Query con persistencia): GETs sobreviven sin red. Suficiente para apps casi-read-only.
2. **Outbox de escritura**: mutaciones se guardan en SQLite con estado `pending` y se reintentan al reconectar. Cubre la mayoría.
3. **Sync bidireccional reactivo** (WatermelonDB): DB local reactiva + motor pull/push. Para apps con muchos datos y edición intensa offline.

## Opciones de DB local
| Opción | Cuándo |
|---|---|
| **MMKV** | KV caliente (flags, sesión, prefs); no es base relacional. |
| **expo-sqlite** | relacional crudo; control total, tú escribes el sync. |
| **WatermelonDB** | ORM reactivo sobre SQLite, queries observables que re-renderizan solo, **sync engine incluido**. |
| **op-sqlite / Drizzle** | SQLite rápido + ORM tipado en TS; sync manual. |

WatermelonDB en Expo SDK 54 funciona vía **development build** (tiene módulo nativo; Expo Go no lo carga — ver [[332-react-native-expo-a-fondo]]). Combina muy bien con **Supabase** como backend de sync.

## Patrón outbox (expo-sqlite, manual y robusto)
- Cada tabla con `updated_at`, `deleted_at` (soft delete) y `synced` (0/1).
- Mutación = escribir local (UI optimista, instantánea) + fila en `outbox`.
- Worker al reconectar (`expo-network` / `NetInfo`): drena el outbox en orden, marca `synced=1`, maneja errores con reintento+backoff. Idempotencia con **client-generated UUID** para no duplicar si el ACK se pierde.

## Resolución de conflictos
- **Last-write-wins (LWW)**: el `updated_at` más nuevo gana. Simple, suficiente para datos "propiedad de un usuario". WatermelonDB de fábrica: si un record cambió en server y local desde `last_pulled_at`, **gana el local** (configurable).
- **Per-field merge**: mezclas campo a campo (nombre del server, avatar del local). Más trabajo, menos pérdida.
- **CRDT**: convergencia automática sin coordinación, ideal para **edición colaborativa/concurrente** (texto, listas). Ver [[353-crdt-collab-yjs]] — úsalo cuando dos personas editan el mismo doc a la vez, no para CRUD de usuario único (ahí LWW basta y CRDT es sobreingeniería).

## Protocolo de sync (modelo WatermelonDB / Supabase)
- **Pull**: server devuelve `{ created, updated, deleted }` desde `last_pulled_at`; cliente aplica.
- **Push**: cliente manda cambios locales; server resuelve y responde nuevo timestamp.
- Hazlo **incremental** (delta por timestamp/cursor), **transaccional** (todo o nada por batch) y **reanudable** (si corta a mitad, el próximo pull retoma sin duplicar).
- Realtime opcional encima (Supabase Realtime / WebSocket) para empujar cambios sin polling.

## Detección de red y UX offline
- `@react-native-community/netinfo` o `expo-network`: distingue **sin conexión** de **conectado pero sin internet** (captive portal). Reacciona al evento, no al estado inicial.
- UX honesta: muestra estado de cada item (`pending`/`synced`/`error`), no un spinner global. El usuario debe poder seguir trabajando mientras la cola drena en background.
- **Backoff** al reintentar: exponencial con jitter; no martilles el server al recuperar señal con 50 mutaciones encoladas a la vez.

## Gotchas
1. **Reloj del cliente miente**: usa timestamps del **server** como verdad, o LWW se corrompe con relojes desincronizados.
2. **Soft delete siempre**: borrar duro local rompe el sync (el server nunca se entera de la baja).
3. **UUID en cliente**: sin id idempotente, un ACK perdido duplica el registro al reintentar.
4. **Migraciones de schema** de la DB local: versiona y migra o la app crashea tras update OTA/binario.
5. **Archivos grandes** (avatares/video generado) NO van en la DB: guarda blob en FS (`expo-file-system`) y solo la URI/metadata en SQLite.
6. Conflictos de listas/orden: LWW pierde inserciones concurrentes → ahí sí escala a CRDT.

**Fuentes:** supabase.com/blog/react-native-offline-first-watermelon-db · docs WatermelonDB sync · dev.to offline-first SQLite.

Cruza con [[90-pwa-offline-first]] y [[353-crdt-collab-yjs]].

# 73 — Edge computing & WebAssembly

## Cloudflare Workers (V8 isolates, no contenedores)
Un proceso V8 corre miles de isolates con ~5ms de cold start (vs cientos de ms en Lambda). Aislamiento a nivel de
heap V8. **Límites 2026:** CPU 30s default, subible a **5 min (300.000 ms)** en Paid; memoria 128 MB. Wall-clock no se cobra mientras esperas I/O — solo CPU.

## Estado y datos
- **Durable Objects (DO):** objeto con identidad única + storage transaccional (chat rooms, contadores, locks). SQLite-backed en GA, billing de storage SQLite desde 7-ene-2026. `sql.exec()` embebido.
- **Workers KV** (key-value eventualmente consistente, lecturas globales) · **R2** (objetos S3-compat, sin egress) · **D1** (SQLite serverless) · **Queues** (async) · **Workers AI** (inferencia en edge sobre modelos open curados).
```js
export default { async fetch(req, env) {
  const id = env.ROOM.idFromName("sala-1"); const obj = env.ROOM.get(id);   // Durable Object
  return obj.fetch(req);
}}
```

## Edge vs origin
**En el edge:** baja latencia (auth, redirects, A/B, personalización), geo-routing, transformación ligera, caché
dinámica. **NO en edge:** cómputo pesado/largo (>CPU limit), deps nativas grandes, modelos ML grandes, DB monolítica regional (cada hop cruza el continente).

## WebAssembly
Ejecuta Rust/Go/C/Zig compilados a binario portable, en navegador y servidor. Runtimes: **wasmtime** (referencia),
**wasmer**. **WASI** (Preview 2 / component model 2026) da acceso a archivos/red/reloj capability-based. **WASM gana a
JS** en cómputo numérico intensivo (parsing, compresión, cripto, físicas, codecs), portar libs C, ejecución
determinista sandboxed. **IA en WASM:** `onnxruntime-web` (WASM/WebGPU) y `transformers.js` (v3, WebGPU) corren modelos en el navegador sin servidor.
```rust
#[no_mangle] pub extern "C" fn suma(a: i32, b: i32) -> i32 { a + b }   // cargo build --target wasm32-wasip1
```

## Otras plataformas / edge DBs
Vercel Edge Functions (V8), Deno Deploy (V8, TS nativo, KV), Fastly Compute (¡corre WASM nativo vía wasmtime, no V8!). **Edge DBs:** Turso/libSQL (fork SQLite, embedded replicas cerca del edge con sync).

## Gotchas
1. **No Node APIs completas:** isolates no tienen `fs`, sockets crudos ni muchos módulos nativos. `nodejs_compat` flag con cuidado.
2. **CPU vs wall-clock:** el límite es **CPU time**; un `await fetch` largo no cuenta, pero un loop sí te mata.
3. **DO single-threaded por objeto:** un DO "caliente" es cuello de botella; reparte por sharding de IDs.
4. **WASM no toca el DOM:** debe llamar a JS para UI; el cruce JS↔WASM tiene costo de serialización (evita llamadas chatty).
5. **Tamaño del bundle WASM:** un modelo ONNX de cientos de MB mata cold start y ancho de banda móvil.
6. **Cold start de módulos WASM grandes:** compilar no es gratis; usa caché de módulos compilados.

**Fuentes:** developers.cloudflare.com/workers/platform/limits · developers.cloudflare.com/durable-objects · turso.tech.

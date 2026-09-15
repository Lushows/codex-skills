# 115 · Render largo asíncrono: el poller durable de servidor

> Un render de 20-40 min NO cabe en una request HTTP ni en la paciencia del navegador. Sin un poller
> de servidor, el video termina en la nube pero **nunca llega a tu biblioteca**. Lección vivida.

## El anti-patrón (lo que pasó)
1. App hace submit → guarda estado → responde "generando", devuelve `id`.
2. El **navegador** poolea cada 5s, pero corta a los **15 min** (180 intentos) → muestra "revisa luego".
3. El render dura ~24-40 min → cuando termina, el `id` ya se perdió en el cliente.
4. **No hay nada del lado del servidor** que cierre el trabajo → el MP4 queda huérfano en R2.

## El patrón correcto: estado durable + poller de servidor
**(a) Estado durable en disco** (sobrevive reinicios y cierre del navegador):
```
data/brands/<brand>/lipsync/<pieceId>.json  ->  { estado:'generando', provider, engine, jobId, costo }
```
**(b) Poller de servidor en el tick** (cada 60s, además del poll del cliente):
```js
async function pollPending({ deps } = {}) {
  for (const brand of fs.readdirSync(brandsRoot())) {
    const dir = path.join(brandsRoot(), brand, 'lipsync');
    if (!fs.existsSync(dir)) continue;
    for (const f of fs.readdirSync(dir)) {
      if (!f.endsWith('.json')) continue;
      const pieceId = f.replace(/\.json$/, '');
      try { await status({ brandId: brand, pieceId, deps }); } catch (_) {} // transitorio -> próximo tick
    }
  }
}
// index.js: setInterval(() => { runTick(); pollPending().catch(...); }, 60_000)
```
**(c) `status()` idempotente**: si la pieza ya tiene `videoFile` → limpia el `.json` residual y
retorna listo. Si el proveedor reporta `done` → descarga el MP4, guarda en biblioteca con su costo,
borra el `.json`. Si `failed` → escribe estado error. Si sigue → deja el `.json` para el próximo tick.

## Por qué esto lo arregla todo
- Cierras el navegador → el servidor termina el trabajo igual.
- El servidor se reinicia (deploy) → el `.json` en disco persistente sobrevive → el poller reanuda.
- El render dura más que cualquier timeout de cliente → no importa, el tick lo recoge.

## Detalles
- **Idempotencia**: el poll debe poder correr N veces sin duplicar piezas ni doble-cobro. Marca de
  "ya guardado" = la pieza con `videoFile` + borrar el `.json`.
- **Backoff**: 60s está bien para renders de minutos. No poolees cada segundo (gastas requests).
- **Cliente**: súbele el tope de paciencia (p.ej. 40 min) y cambia el copy a "aparecerá solo en la
  biblioteca cuando termine — puedes cerrar esto".
- **Webhook como alternativa**: si el proveedor soporta webhook al terminar, úsalo en vez de poolear
  (menos requests). Pero mantén el poller como red de seguridad si el webhook se pierde.

Cruza con [[100-durable-execution-background-jobs-2026]], [[04-systems-layer-gateway-queue]] y
[[23-event-driven-colas]].

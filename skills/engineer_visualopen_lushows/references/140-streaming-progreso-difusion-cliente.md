# 140 · Streaming de progreso de difusión al cliente

> Un render de 20-40 min con una barra muerta en 0% genera desconfianza y soporte. Reportar
> `% de pasos/segmentos` cuesta poco y convierte la espera en algo tolerable. NO reemplaza al
> poller durable — lo complementa: el progreso es UX, el poller es la fuente de verdad.

## Capas del problema
Hay tres saltos donde el progreso puede morir:
1. **Worker GPU → gateway**: el handler tiene que *emitir* el % mientras corre la difusión.
2. **Gateway → navegador**: transportar ese % en vivo (SSE/WS) o por poll.
3. **Mapeo a número**: convertir `step k/N` (y `segmento j/M` en video largo) a un % monótono.

## Capa 1 — emitir progreso desde el worker

### diffusers: `callback_on_step_end`
Es la fuente real de progreso por paso. Firma (diffusers ≥0.25, verificada):
`callback(pipe, step:int, timestep:int, callback_kwargs:dict) -> dict`. Debe **retornar** un dict
(vacío vale) con los tensores que declaraste en `callback_on_step_end_tensor_inputs`.
```python
total = num_inference_steps
def on_step(pipe, step, timestep, kw):
    emit_progress((step + 1) / total)   # 0..1, monótono
    return kw                            # no toques latents si no hace falta
pipe(prompt, num_inference_steps=total,
     callback_on_step_end=on_step,
     callback_on_step_end_tensor_inputs=["latents"])
```
Gotcha: el viejo `callback=`/`callback_steps=` está **deprecado**; usa `callback_on_step_end`. No
decodifiques el VAE por step para una preview salvo que lo pidan: puede **duplicar** el tiempo de inferencia.

### RunPod: handler generador + `/stream`
Un handler que es **función generadora** (`yield`) expone resultados parciales en el endpoint
`/stream`. El `emit_progress` de arriba alimenta una cola que el generador drena:
```python
import runpod, queue
def handler(job):
    q = queue.Queue()
    def emit_progress(p): q.put({"progress": round(p, 3)})
    t = threading.Thread(target=run_diffusion, args=(job["input"], emit_progress)); t.start()
    while t.is_alive() or not q.empty():
        try: yield q.get(timeout=1)
        except queue.Empty: pass
    yield {"progress": 1.0, "output": result_ref}   # último yield = resultado
runpod.serverless.start({"handler": handler, "return_aggregate_stream": True})
```
- `return_aggregate_stream: True` → los `yield` también quedan accesibles vía `/run` y `/runsync`,
  no solo `/stream` [verificado en docs RunPod]. El cliente drena `POST /v2/<id>/stream/<jobId>`.
- Gotcha: el progreso vive **mientras el worker corre**. Si el navegador se cae se pierde — la
  verdad final la cierra el poller de [[115-async-render-largo-poller-durable]].

## Capa 2 — gateway → navegador (SSE)
SSE es lo más simple para una barra unidireccional (no necesitas WS). Tu gateway abre un stream
hacia RunPod `/stream` y reemite como `text/event-stream`:
```js
res.writeHead(200, {'Content-Type':'text/event-stream','Cache-Control':'no-cache','Connection':'keep-alive'});
for await (const chunk of pollRunpodStream(jobId))   // chunk = {progress} | {output}
  res.write(`data: ${JSON.stringify(chunk)}\n\n`);
res.write('event: done\ndata: {}\n\n'); res.end();
```
Cliente: `new EventSource('/api/lipsync/'+id+'/progress')` → `bar.style.width = ev.progress*100+'%'`.
Detalles de SSE (reconexión, `Last-Event-ID`, WS vs SSE vs WebRTC) en [[44-realtime-websockets-sse-webrtc]].
Si no quieres mantener conexión abierta 40 min, **degrada a poll**: el `.json` durable guarda
`progress` y el cliente lo lee cada 5-10s (mismo poll del estado).

## Capa 3 — mapear segmentos → % en video largo
En video segmentado (ver [[114-video-segmentado-largo-clip]]) el render son `M` segmentos, cada uno
con `N` pasos de difusión. El % global combina ambos para que la barra no se reinicie por segmento:

| Magnitud | Fórmula |
|---|---|
| Progreso de un segmento | `seg_p = (step+1)/N` |
| Progreso global | `(segmento + seg_p) / M` |
| Con pesos por duración | `(Σ dur_j hechos + dur_actual·seg_p) / Σ dur` |

```python
def global_pct(seg_idx, step, N, M):   # 0..1, monótono creciente
    return (seg_idx + (step + 1) / N) / M
```
Gotchas:
- **Monotonicidad**: nunca dejes que el % retroceda al cambiar de segmento. Clampea: `p = max(p, last)`.
- **No llegues a 100% antes del mux**: reserva el último 3-5% para encode/concat/upload ffmpeg
  (ver [[142-ffmpeg-avatar-video-a-fondo]]). Mapea difusión a `0..0.95` y el post a `0.95..1.0`.
- **ETA**: estima con media móvil de segundos/paso reales, no constante; varía con resolución/VRAM.

## Dónde encaja en la arquitectura
El gateway/cola ([[04-systems-layer-gateway-queue]]) tiene el estado del job y reexpone el progreso;
el worker solo emite. Regla: **progreso = mejor-esfuerzo (UX); completitud = poller durable**. Nunca
marques "listo" por un `progress:1.0` del stream — márcalo cuando el MP4 está en biblioteca.

Cruza con [[115-async-render-largo-poller-durable]], [[44-realtime-websockets-sse-webrtc]],
[[04-systems-layer-gateway-queue]] y [[114-video-segmentado-largo-clip]].

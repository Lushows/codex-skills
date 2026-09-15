# 06 — ComfyUI como backend de producción (2026)

> Cuándo tu pipeline ES un grafo de loaders/sampler/VAE/LoRA/ControlNet, ComfyUI headless es un
> backend de inferencia legítimo (no solo una UI). Esta ref es para servirlo como API.

## Qué es

ComfyUI es un **node-graph**: cada nodo es una operación (load checkpoint, encode prompt, KSampler,
VAE decode, save image). El grafo se ejecuta en orden topológico con caché por nodo (re-ejecuta solo
lo que cambió). **La UI es solo UN cliente del servidor** — el server Python expone HTTP+WebSocket y
corre headless por default.

## Correrlo headless (API)

```bash
python main.py --listen 0.0.0.0 --port 8188 --disable-auto-launch
# flags útiles: --highvram / --lowvram / --novram (gestión VRAM),
#   --output-directory /data/out, --extra-model-paths-config extra_model_paths.yaml,
#   --cpu (debug sin GPU)
```

### Endpoints clave

| Método | Ruta | Qué hace |
|---|---|---|
| `POST` | `/prompt` | Encola un workflow (JSON **API format**) + `client_id`. Devuelve `{prompt_id, number}`. |
| `GET` | `/history/{prompt_id}` | Resultado del job: nodos de salida → archivos + metadata. |
| `GET` | `/view?filename=...&subfolder=...&type=output` | Descarga el archivo generado (imagen/video). |
| `WS` | `/ws?clientId=...` | Progreso en vivo: `status`, `executing` (nodo actual), `progress` (step), `executed` (outputs), preview images. |
| `POST` | `/upload/image` | Sube input (img2img/ControlNet). |
| `GET` | `/object_info` | Esquema de TODOS los nodos disponibles (para validar). |
| `POST` | `/interrupt` · `/queue` · `/history` (DELETE para limpiar) | gestión de cola. |

### Patrón cliente correcto (poll + WS)

```python
import json, urllib.request, uuid, websocket
CID = str(uuid.uuid4())
def queue(wf):
    data = json.dumps({"prompt": wf, "client_id": CID}).encode()
    r = urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:8188/prompt", data=data))
    return json.loads(r.read())["prompt_id"]
ws = websocket.WebSocket(); ws.connect(f"ws://127.0.0.1:8188/ws?clientId={CID}")
pid = queue(workflow_api_json)
while True:                                   # esperar "executing" con node=None y mismo prompt_id
    m = json.loads(ws.recv())
    if m["type"]=="executing" and m["data"]["node"] is None and m["data"]["prompt_id"]==pid:
        break
hist = json.loads(urllib.request.urlopen(f"http://127.0.0.1:8188/history/{pid}").read())[pid]
# hist["outputs"][node_id]["images"] -> [{filename, subfolder, type}] -> GET /view
```
(Ver el oficial `script_examples/websockets_api_example.py` en el repo Comfy-Org/ComfyUI.)

## Exportar workflow en "API format"

- En la UI: **Settings → Enable Dev Mode Options** → aparece **"Save (API Format)"**. El JSON normal de
  la UI (con posiciones de nodos) **NO sirve para `/prompt`**; necesitas el API format (mapa `node_id →
  {class_type, inputs}`).
- Para parametrizar: cargas el JSON, ubicas el nodo por su `id` o `class_type`, y sobreescribes
  `inputs` (ej. `wf["6"]["inputs"]["text"] = prompt_usuario`, `wf["3"]["inputs"]["seed"] = seed`). Los
  IDs son frágiles entre versiones del workflow → usa **título de nodo** o `class_type` para localizar.

## Custom nodes

- **ComfyUI-Manager** (Comfy-Org): instala/actualiza nodes y descarga sus dependencias. En headless,
  usa su **CLI `comfy-cli`**: `comfy node install <nombre>`, `comfy node restore-snapshot snapshot.json`.
- **Reproducibilidad:** exporta un **snapshot** (`comfy node save-snapshot`) que pinea cada custom node
  a un commit → reconstruible en Docker. NO instales nodes a mano en producción; hornéalos en la imagen.
- **Dependencias:** cada custom node trae su `requirements.txt`. En Docker, instálalos en el build
  (mismo smoke-test de imports del SKILL §3). Custom nodes que compilan (ej. con CUDA) = el mismo
  dolor de ABI torch/flash_attn del SKILL §1.

## ComfyDeploy / versionar workflows como API

- **comfy-deploy (comfydeploy.com)**: versiona un workflow como **endpoint API** con sus inputs
  tipados; corre serverless, maneja modelos/nodes. Útil para exponer un grafo a tu app sin operar el
  server tú mismo.
- **RunningHub / Replicate (cog-comfyui) / ViewComfy / Modal**: alternativas que envuelven ComfyUI en
  un endpoint serverless. ViewComfy y la guía de Modal documentan el patrón "ComfyUI as API" completo.
- **Self-host serverless (RunPod):** misma receta del SKILL — imagen Docker con ComfyUI + custom nodes
  horneados, modelos en Network Volume, handler que arranca `main.py --listen` y hace el ciclo
  `/prompt` → WS → `/history` → sube a R2. (SKILL §6.26: "ComfyUI como API" es una fila de la tabla de serving.)

## Gestión de modelos

- Checkpoints en `models/checkpoints/`, LoRAs en `models/loras/`, VAE en `models/vae/`, ControlNet en
  `models/controlnet/`, upscalers en `models/upscale_models/`, etc.
- **`extra_model_paths.yaml`** (raíz de ComfyUI) mapea carpetas externas → **úsalo para apuntar al
  Network Volume** sin copiar modelos a la imagen:
  ```yaml
  comfyui:
    base_path: /runpod-volume/models/
    checkpoints: checkpoints/
    loras: loras/
    vae: vae/
    controlnet: controlnet/
  ```
- Mismo principio del SKILL §2: **modelos NO en la imagen Docker** → Network Volume + `extra_model_paths.yaml`.

## ComfyUI vs handler custom vs diffusers directo

| Opción | Cuándo |
|---|---|
| **ComfyUI** | Tu pipeline es un grafo visual de loaders/sampler/LoRA/ControlNet/upscale; quieres iterar el workflow sin tocar código; reuso de nodes de la comunidad. |
| **Handler custom (script propio)** | Pipeline idiosincrático lanzado por `torchrun` (avatares/video grandes tipo LongCat), control total, sin overhead de grafo. **Default del SKILL para video/avatar.** |
| **diffusers directo** | Pipeline estándar y simple (txt2img SDXL/FLUX), máximo control de código, sin la capa de grafo; mejor para integrar en una app Python existente y aplicar `torch.compile`/offload finos (SKILL §6.23-24). |

Regla: **prototipas en la UI de ComfyUI → exportas API format → lo sirves headless**. Si el grafo es
trivial o necesitas optimizaciones de bajo nivel, baja a diffusers.

## Gotchas

1. **El JSON de la UI ≠ API format.** Postear el workflow normal a `/prompt` falla. Activa Dev Mode y
   usa "Save (API Format)".
2. **Bindea a localhost detrás de un reverse proxy con auth.** `--listen 0.0.0.0` expone el server SIN
   autenticación — cualquiera puede encolar jobs y leer tu disco vía `/view`. Pon Nginx/Caddy con API
   key delante y bindea ComfyUI a `127.0.0.1`.
3. **Custom nodes rompen entre versiones de ComfyUI.** Pinea ComfyUI a un commit Y los custom nodes con
   un snapshot. Un `git pull` de ComfyUI puede romper nodes que dependen de internals.
4. **Los `node_id` del workflow cambian al re-exportar.** Si parametrizas por ID, un re-export rompe tu
   código. Localiza nodos por `class_type` o por título único.
5. **VRAM:** ComfyUI gestiona offload solo (`--lowvram`/`--novram`), pero un workflow con varios modelos
   grandes (checkpoint + ControlNet + upscaler) puede OOM. Mismo arsenal del SKILL §6.23 (tiling, offload).
6. **`/history` se limpia.** El historial es en memoria/limitado → descarga el output (`/view`) y súbelo a
   R2 apenas el job termina; no dependas de que `/history` lo retenga.

## Fuentes
- https://github.com/comfyanonymous/ComfyUI/blob/master/script_examples/websockets_api_example.py
- https://www.runflow.io/blog/comfyui-api-developer-guide
- https://www.viewcomfy.com/blog/building-a-production-ready-comfyui-api
- https://9elements.com/blog/hosting-a-comfyui-workflow-via-api/
- https://cohorte.co/blog/the-comfyui-production-playbook
- https://docs.comfy.org/development/cloud/overview

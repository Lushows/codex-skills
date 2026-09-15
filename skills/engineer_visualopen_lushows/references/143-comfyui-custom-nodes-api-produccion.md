# 143 · ComfyUI en producción: API, custom nodes y serverless headless

> ComfyUI no es solo una UI: es un motor de grafos con API HTTP+WebSocket que puedes manejar sin abrir el navegador.
> El truco de producción es tratar el workflow como JSON (API format), encolar por `/prompt` y leer el resultado por WS+`/history`.

## Los dos formatos de workflow (no confundir)
ComfyUI guarda DOS JSON distintos. El de la UI ("Save") trae layout de nodos (posiciones, links visuales) y **la API lo rechaza**. El que necesitas es **"Save (API Format)"** (activa `Settings → Enable Dev mode options`). Ese JSON es un dict `{ "<node_id>": { "class_type": "...", "inputs": {...} } }` — es lo que ComfyUI llama internamente "prompt". Plantilla mínima:

```json
{ "3": { "class_type": "KSampler",
         "inputs": { "seed": 42, "steps": 20, "cfg": 7.0, "sampler_name": "euler",
                     "model": ["4",0], "positive": ["6",0], "negative": ["7",0], "latent_image": ["5",0] } } }
```
Los inputs que son `["<node_id>", <slot>]` son **conexiones** entre nodos; los escalares son parámetros. Para parametrizar (prompt del usuario, seed, resolución) parcheas esos escalares antes de encolar.

## API HTTP (puerto 8188 por defecto)
| Endpoint | Uso |
|---|---|
| `POST /prompt` | Encola. Body `{"prompt": <api_json>, "client_id": "<uuid>"}`. Devuelve `{"prompt_id","number","node_errors"}` |
| `GET /history/{prompt_id}` | Outputs del job (rutas de imágenes, subfolder, type) |
| `GET /view?filename=&subfolder=&type=output` | Descarga el binario del resultado |
| `POST /upload/image` | Sube imagen de entrada (multipart) → para img2img/controlnet |
| `GET /object_info` | Introspección: TODOS los nodos cargados + sus INPUT_TYPES (valida deps antes de encolar) |
| `GET /system_stats` · `POST /free` | VRAM/RAM · libera modelos de VRAM |
| `POST /interrupt` · `GET /queue` | Cancela el job en curso · estado de la cola |

## WebSocket: progreso en tiempo real
Conecta a `ws://host:8188/ws?clientId=<uuid>` (el MISMO `client_id` del POST). Tipos de mensaje:
- `status` → tamaño de cola.
- `executing` → `{"node": "<id>", "prompt_id": ...}`. Cuando `data["node"] is None` y el `prompt_id` coincide → **job terminado**.
- `progress` → `{"value","max"}` por paso del sampler (barra de progreso).
- `executed` → outputs de un nodo (incluye imágenes).
- Mensajes **binarios** = previews (frames intermedios) — descártalos o muéstralos como preview en vivo.

Patrón cliente: abrir WS → `POST /prompt` → loop sobre WS hasta `executing` con `node=None` → `GET /history/{id}` → por cada output, `GET /view`. No hagas polling ciego de `/history`; el WS te dice cuándo.

## Custom nodes: estructura y registro
Un custom node es una carpeta en `ComfyUI/custom_nodes/<paquete>/` con:
```
__init__.py            # exporta NODE_CLASS_MAPPINGS y NODE_DISPLAY_NAME_MAPPINGS
nodes.py               # las clases
requirements.txt       # deps extra (se instalan al arrancar / por el manager)
pyproject.toml         # opcional; metadata para ComfyUI Registry
```
Cada nodo es una clase Python con:
- `@classmethod INPUT_TYPES(cls)` → dict con `required` / `optional` / `hidden`; cada input es `(tipo, opts)` ej. `("INT", {"default": 20, "min": 1, "max": 150})`.
- `RETURN_TYPES = ("IMAGE",)`, `FUNCTION = "run"`, `CATEGORY = "mi/grupo"`, y el método que ejecuta.
- `__init__.py` debe exponer `NODE_CLASS_MAPPINGS = {"MiNodo": MiNodo}`. Sin eso, ComfyUI **no lo ve**. Reiniciar ComfyUI tras cambios (no hay hot-reload fiable).

Gotcha: dos paquetes con la misma **clave** en `NODE_CLASS_MAPPINGS` colisionan silenciosamente; usa prefijos únicos. Las deps de `requirements.txt` de varios custom nodes pueden **chocar versiones** (numpy/torch) — fija versiones y prueba el set completo, no nodo a nodo.

## Headless en serverless
- Arranca con `python main.py --listen 0.0.0.0 --port 8188 --disable-auto-launch` (sin abrir browser). En GPU serverless: `--highvram` si cabe (evita re-cargar a VRAM), o deja que ComfyUI gestione (offload automático).
- **Modelos**: NO los hornees en la imagen si son enormes; móntalos desde Network Volume y symlinkea `models/checkpoints`, `models/vae`, etc. al volumen (ver [[113-network-volume-modelos-grandes]]).
- **Warm worker**: arranca ComfyUI una vez como subproceso persistente dentro del handler; reusa el server HTTP entre jobs en vez de re-arrancar el proceso por request (cold start de carga de modelos a VRAM se paga una vez).
- **Determinismo**: clava `seed` (no `randomize`) si el caller pide reproducibilidad; el `client_id` debe ser único por worker para no cruzar streams de WS.
- **Custom nodes en la imagen**: instálalos en build (clónalos + `pip install -r`), NO en runtime — instalar deps en cold start mata el tiempo de arranque.

## Gotchas de producción
- `node_errors` no vacío en la respuesta de `/prompt` = workflow inválido (falta un modelo, input mal mapeado). Valida contra `/object_info` antes de encolar.
- La cola es **global por proceso**: un worker procesa de a uno. Para concurrencia real → N workers/réplicas, no N prompts en un ComfyUI.
- `/free` o `--lowvram` para modelos que no caben; OOM mid-run no da error limpio en la API, se ve como WS que muere.
- Limpia `output/` y `temp/` periódicamente o el disco efímero del worker se llena.

Cruza con [[06-comfyui-backend-produccion]] y [[139-controlnet-ipadapter-serving-consistencia]].

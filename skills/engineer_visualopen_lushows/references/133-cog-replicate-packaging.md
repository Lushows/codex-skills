# 133 · Cog (Replicate): empaquetado, predict.py y cuándo usarlo vs Dockerfile propio

> Cog es el empaquetador de Replicate: convierte tu modelo en un contenedor con API HTTP estándar
> sin que escribas un Dockerfile. Cómodo cuando encaja; jaula cuando tu pipeline es raro. Aquí el
> qué, el cómo y la decisión Cog-vs-GHCR para IA visual self-hosted.

## Qué es Cog
Herramienta open-source (`replicate/cog`) que, a partir de **dos archivos**, buildea una imagen Docker
con server de inferencia, schema de inputs/outputs y manejo de GPU. Genera `cog.yaml` + `predict.py`.

## cog.yaml (cómo se buildea)
Define el entorno. Tres claves: `build`, `image`, `predict`.
```yaml
build:
  gpu: true
  cuda: "12.1"            # Cog elige base CUDA/torch compatible — cruza matriz con la skill
  python_version: "3.11"
  python_packages:
    - "torch==2.4.0"
    - "diffusers==0.30.0"
  system_packages:
    - "ffmpeg"
predict: "predict.py:Predictor"   # archivo:Clase
```
Cog resuelve CUDA↔torch por ti, pero si necesitas flash_attn/xformers con ABI fino, fíjalo a mano
(Cog no adivina la ABI). Ver la matriz GPU↔CUDA↔torch de la skill.

## predict.py (cómo corre)
```python
from cog import BasePredictor, Input, Path

class Predictor(BasePredictor):
    def setup(self):
        # SE EJECUTA UNA VEZ al arrancar el contenedor → warm-state.
        # Carga pesos a VRAM aquí, NO en predict(). Esto es lo que evita re-cargar por request.
        self.model = load_model("./weights")

    def predict(self,
        image: Path = Input(description="cara"),
        audio: Path = Input(description="voz"),
        prompt: str = Input(default="static camera"),
    ) -> Path:
        # Corre por cada request. Mantén limpio IN/OUT por job (igual que el handler RunPod).
        return Path(generate(self.model, image, audio, prompt))
```
`setup()` = el equivalente Cog al warm-state del handler de RunPod: pesos en VRAM una vez, no por job.

## Build y push
```bash
cog build -t mi-modelo            # buildea local
cog predict -i image=@cara.png    # prueba local antes de pushear
cog login                         # token de Replicate
cog push r8.im/<usuario>/<modelo> # sube al registry; crea la página/API en Replicate
```
Tras el push, el modelo tiene página web, API HTTP y versión inmutable (hash). Llamas vía API REST
o SDK con submit + poll (async), igual patrón que [[111-longcat-avatar-runpod-produccion]].

## Cuándo Cog vs Dockerfile propio + GHCR
| Situación | Elige |
|---|---|
| Modelo "normal" (un repo, un pipeline, deps limpias) y quieres API pública ya | **Cog → Replicate** |
| Necesitas la inmutabilidad/versionado y página de Replicate | **Cog** |
| Pipeline carga sub-modelos de otros repos, paths raros, system deps finas, build multi-stage | **Dockerfile propio + GHCR** |
| Quieres correr en RunPod/Modal/Beam con control total del contenedor | **Dockerfile propio + GHCR** |
| Cold start crítico y quieres hornear/cachear pesos a tu manera | **Dockerfile propio + GHCR** |

Cog te quita el Dockerfile pero te mete en SU forma de buildear; si tu modelo pelea con esa forma
(sub-modelos, descargas a paths fijos, ABI exótica), terminas peleando con Cog. Para los casos de
IA visual pesada de esta skill, el patrón ganador suele ser **GHCR + Actions** sobre RunPod, no Cog.
Pipeline de build/push y pin de SHA en [[16-cicd-modelos-workers]].

## Gotchas
- **Pesos en la imagen vs descarga en setup()**: hornearlos engorda la imagen (pull lento) pero evita
  re-descarga; descargarlos en `setup()` los baja en cada cold. Mismo dilema que [[113-network-volume-modelos-grandes]]
  (en Replicate no hay Network Volume equivalente abierto → tiendes a hornear o usar su cache).
- **`cuda`/torch mal casados** → build verde pero runtime con `CUDA error`. Fija versiones explícitas.
- **`setup()` que carga en `predict()`** por error → pagas la carga del modelo en CADA request.
- **Inputs `Path`** se materializan a disco temporal; limpia OUT por job para no fugar entre requests.

Cruza con [[132-plataformas-gpu-serverless-comparativa]] y [[16-cicd-modelos-workers]].

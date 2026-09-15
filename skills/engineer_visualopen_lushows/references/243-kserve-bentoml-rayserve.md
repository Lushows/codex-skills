# 243 · Frameworks de serving (KServe / Seldon / BentoML / Ray Serve) vs worker propio

> Antes de escribir tu propio handler de inferencia, conviene saber qué resuelven los frameworks de
> serving. La pregunta real no es "cuál es mejor", sino "¿necesito uno, o mi worker en RunPod ya basta?".

## La decisión de fondo: framework vs worker artesanal
Para auto-hospedaje **barato y serverless** (RunPod, un modelo de video/avatar, volumen bajo-medio), el
**worker propio gana casi siempre**: handler Python + cola de jobs del proveedor + warm-state. Sin K8s,
sin control-plane, sin pagar nodos idle. Los frameworks de serving brillan cuando tienes **K8s propio**,
muchos modelos, tráfico sostenido y necesitas autoscaling/batching/observabilidad estandarizados.

## Los cuatro, por filosofía
| Framework | Filosofía | K8s obligatorio | Punto fuerte |
|---|---|---|---|
| **BentoML** | Python-first: servir un modelo se siente como una API FastAPI | **No** | DX rápida, adaptive batching, equipos chicos |
| **KServe** | Estandariza: capa de serving unificada, ecosistema Kubeflow | **Sí** | "Batteries included" serverless en K8s |
| **Seldon Core v2** | Cloud-native, extensible, features de gobierno | **Sí** | Industrias reguladas: logging de payload, drift, explainability built-in |
| **Ray Serve** | Apps distribuidas, agnóstico de framework | No (usa Ray) | Workflows Python dinámicos, multi-modelo, escala con Ray |

## Cuándo cada uno
- **BentoML** → startups y equipos chicos que escriben Python y quieren iterar rápido sin operar K8s.
  Corre en un contenedor cualquiera; se integra bien con serverless. Es el más cercano al "worker propio
  pero con batching y empaquetado resueltos".
- **KServe** → ya tienes Kubernetes y quieres serving serverless **estandarizado** (scale-to-zero,
  canary nativo) sobre muchos modelos. Es el default si vives en Kubeflow.
- **Seldon Core v2** → cuando **gobierno** es requisito: payload logging, drift detection, explainability
  son parte del producto, no un plugin. KServe lo soporta vía plugins; Seldon lo trae de fábrica.
- **Ray Serve** → pipelines de inferencia **dinámicos y Pythonic** (varios modelos encadenados, lógica
  de routing en código), o si ya usas Ray para training/batch.

## Para difusión / GPU NVIDIA pesada
Ninguno de estos reemplaza a **Triton** cuando el cuello es la GPU pura (kernels optimizados, dynamic
batching a nivel CUDA, múltiples modelos en una GPU). Patrón común: **Triton como motor** + uno de estos
(o tu worker) como capa de orquestación/API encima (ver [[144-triton-inference-server-difusion]]).

## Rendimiento (referencia)
BentoML reporta 1000+ req/s con p95 < 50ms en ResNet50 sobre hardware modesto vía adaptive batching.
Para modelos generativos pesados (video/avatar) el cuello NO es el framework sino la VRAM y el tiempo de
generación por clip: el serving framework no te salva de un cold-start de 25 min ni de un OOM.

## Recomendación para este stack
1. **MVP / volumen bajo** → worker propio en RunPod serverless. Cero frameworks. Máximo control de coste.
2. **Quieres batching + empaquetado sin K8s** → **BentoML** sobre el mismo contenedor.
3. **Ya tienes K8s + muchos modelos + tráfico sostenido** → **KServe** (o Seldon si necesitas gobierno).
4. **GPU NVIDIA como cuello** → **Triton** debajo, da igual la capa de arriba.

## Detalles que muerden
- Un framework de serving **no elimina** el problema de cargar 44GB a VRAM ni el cold-start: eso lo
  resuelve el almacenamiento de pesos, no el serving. No esperes magia de latencia en modelos enormes.
- K8s + KServe/Seldon = nodos GPU potencialmente idle = coste fijo. Mata el ahorro del serverless si el
  tráfico es esporádico. Mide antes de adoptarlo.
- Scale-to-zero en KServe sigue pagando el cold-start del primer request: mismo problema que el worker.

Cruza con [[144-triton-inference-server-difusion]] y [[132-plataformas-gpu-serverless-comparativa]].

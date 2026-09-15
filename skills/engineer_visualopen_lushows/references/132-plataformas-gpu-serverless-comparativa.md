# 132 · Comparativa de plataformas GPU serverless para IA visual self-hosted

> No todas las "serverless GPU" sirven para auto-hospedar tu modelo open. Unas te dan el contenedor
> completo (RunPod, Modal, Beam), otras te obligan a empaquetar a su manera (Replicate/Cog) o solo
> sirven modelos suyos (Fal). Esta es la elección por caso (jun-2026, precios verificados).

## El eje que decide: ¿cuánto control del contenedor te dan?
- **Control total (tu Dockerfile + GHCR)**: RunPod, Beam, Baseten (Truss). Pones lo que quieras.
- **Control "pythónico" (defines en código, ellos buildean)**: Modal (decoradores `@app.function`).
- **Empaquetado opinado (Cog)**: Replicate. Cómodo si encaja, jaula si no. Ver [[133-cog-replicate-packaging]].
- **Catálogo + API, poco self-host**: Fal. Brutal para modelos suyos (Flux), no para tu repo raro.

## Tabla comparativa
| Plataforma | Cobro | Cold start | Volúmenes/storage | Deploy | Control contenedor | Para IA visual self-host |
|---|---|---|---|---|---|---|
| **RunPod** | $/s por GPU (flex/active); H100 ~$4.18/hr flex | medio (mata con Network Volume/FlashBoot) | Network Volume regional ($0.07/GB-mes) | tu imagen GHCR → endpoint | total | **mejor default**: modelos enormes, control, barato |
| **Modal** | $/s; H100 ~$3.95/hr; $30/mes free credit | bajo (segundos), snapshots | Volumes + mounts nativos | `modal deploy` desde Python | alto (defines en código) | excelente si tu pipeline es Python puro y quieres DX |
| **Replicate** | $/s por modelo; A100-80GB ~$5.04/hr | medio-alto | poco control (lo gestiona Cog) | `cog push r8.im/...` | bajo (vía Cog) | bueno si Cog encaja y quieres API+página pública |
| **Fal** | por output (≈$0.006-0.008/img Flux) o $/s | ~0 (warm, no lo pagas) | n/a (gestionado) | limitado a sus runtimes | bajo | top para Flux/imagen; flojo para repos custom raros |
| **Beam** | $/s competitivo; free 10h GPU | **muy bajo (2-3s)** | volúmenes propios | `beam deploy` (Python) | medio-alto | gran opción si el cold start te duele y es Python |
| **Baseten** | $/GPU-hr + mínimo dedicado | bajo (5-10s, container cache) | gestionado | Truss (empaquetado) | medio | producción seria con SLA; mínimos awake encarecen lo esporádico |

## Lectura rápida por necesidad
- **Modelo open enorme (44GB+), control de CUDA/torch, lo más barato esporádico** → **RunPod** +
  Network Volume. Es el caso de [[111-longcat-avatar-runpod-produccion]]. Detalle en [[131-runpod-a-fondo-serverless-pods-volumes]].
- **Pipeline Python, quiero DX y desplegar desde el editor** → **Modal** (o **Beam** si el cold start manda).
- **Quiero una API pública/página y mi modelo encaja en Cog** → **Replicate**. Ver [[133-cog-replicate-packaging]].
- **Solo necesito Flux/imagen a escala, sin operar infra** → **Fal** (output-based, warm).
- **Producción con SLA y tráfico constante** → **Baseten** (active/dedicado) o RunPod **active workers**.

## Trampas al comparar precios
- El **$/hr de tabla NO es el costo real**: súmale cold start facturado (initializing cuenta) e idle
  timeout. Un H100 "barato" con cold de 10 min puede salir más caro que un A100 con volumen.
- **Por-output (Fal)** parece caro por imagen pero esconde que no pagas frío ni infra ociosa.
- **Mínimos awake (Baseten)** matan el caso esporádico: pagas aunque no llegue tráfico.
- Mide $/video real, no $/hr de catálogo. Metodología en [[112-execution-timeout-cold-start-economics]] y [[30-finops-gpu]].

## Vendor lock-in (qué tan fácil te vas)
- **Bajo**: RunPod/Beam (tu Dockerfile corre casi igual en otro lado).
- **Medio**: Modal/Baseten (atado a su SDK/runner, pero el modelo es portable).
- **Alto**: Replicate (Cog) y Fal (su catálogo). Reescribir el empaquetado para migrar.

Regla Lushows: prototipa donde haya free credit (Modal $30, Beam 10h), pero **produce IA visual pesada
en RunPod** por control + Network Volume + $/s honesto. Cruza con [[131-runpod-a-fondo-serverless-pods-volumes]] y [[133-cog-replicate-packaging]].

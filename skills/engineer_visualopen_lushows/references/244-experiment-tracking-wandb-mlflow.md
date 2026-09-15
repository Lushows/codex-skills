# 244 · Tracking de experimentos (W&B / MLflow) para training visual

> Entrenar un LoRA o afinar un avatar sin tracking es entrenar a ciegas: ¿qué LR + qué dataset + qué
> seed produjo el checkpoint bueno? Sin registro, no lo reproduces. Un tracker captura métricas,
> hiperparámetros, artifacts y código de cada run en un dashboard comparable.

## Qué registra un tracker
- **Métricas** por step/epoch (loss, FID/FVD, CLIP-score, LR) → curvas comparables entre runs.
- **Hiperparámetros**: LR, batch, rank del LoRA, steps, scheduler, seed.
- **Artifacts**: checkpoints, samples generados, el dataset usado (versionado).
- **Entorno**: versión de código, métricas de sistema (GPU util, VRAM), para reproducir.

## W&B vs MLflow, lo que importa
| Eje | Weights & Biases | MLflow |
|---|---|---|
| Naturaleza | SaaS gestionado (free: 5 seats, 5GB/mes; Pro ~$60/user/mes) | Open-source 100% gratis, **self-hosted** |
| Dashboard / UX | Best-in-class, tiempo real, colaborativo | Funcional, sin pulido de W&B |
| **Sweeps** (HPO) | **Integrado y best-in-class** | **No tiene**; usa Optuna o Ray Tune al lado |
| Artifacts / registry | A la par; lineage + stages | A la par; Tracking+Projects+Models+Registry |
| Lock-in | Formato propietario; export parcial | Mínimo; portable, self-host |
| Integraciones | Más profundas (frameworks) | Buenas, menos que W&B |

## Cuándo cada uno
- **W&B** → investigación/iteración rápida de LoRA y afinado de avatar, equipo que quiere **sweeps
  integrados** y dashboards en vivo para comparar samples visuales. El sweep automático de hiperparámetros
  ahorra días cuando buscas el rank/LR óptimo. Coste: SaaS + lock-in del formato propietario.
- **MLflow** → quieres **gratis, self-hosted y sin lock-in**, controlas tu infra, y no te importa montar
  Optuna/Ray Tune aparte para HPO. Ideal si ya self-hospedas todo (coherente con la filosofía de barato).

## Patrón para training visual (LoRA / avatar)
1. Cada job de training (en GPU serverless) **loguea al tracker** vía API: métricas + samples cada N steps.
2. Sube samples generados como artifacts → revisión visual en el dashboard (clave: la loss no te dice si
   la cara se ve bien; los samples sí — cruza con [[164-evals-calidad-avatar-video]]).
3. Al terminar, registra el checkpoint en el registry con alias (`staging`/`production`).
4. El run guarda el **hash del dataset** usado → reproducibilidad real (ver [[245-data-model-versioning-dvc-lakefs]]).

## Detalles que muerden
- En GPU serverless efímera, el tracker debe loguear a un **backend remoto** (W&B cloud o un MLflow server
  con backing store persistente): si el worker muere, el dashboard ya tiene los datos. No guardes runs solo
  en disco efímero del contenedor.
- W&B **Sweeps** vale su precio cuando barres hiperparámetros del LoRA; con MLflow ese trabajo lo haces a
  mano con Optuna. Cuenta ese esfuerzo en la decisión.
- Logging síncrono pesado en cada step ralentiza el training: usa modo async / cada N steps.
- No subas los 44GB de pesos base como artifact en cada run: versiona el **delta** (el LoRA), no el modelo.

## Recomendación para este stack
Empieza con **W&B** si iteras LoRA/avatar y valoras sweeps + revisión visual de samples (free tier alcanza
para arrancar). Migra/usa **MLflow self-hosted** si el lock-in o el coste recurrente molestan y ya tienes
infra propia. Para 1-2 personas iterando modelos visuales, los sweeps integrados suelen justificar W&B.

Cruza con [[152-lora-training-avatar-personaje-propio]] y [[164-evals-calidad-avatar-video]].

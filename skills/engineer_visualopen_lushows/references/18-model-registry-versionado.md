# 18 — Model registry y versionado

Trata cada versión de modelo como un **artefacto inmutable y direccionable**: mismos inputs → mismos bytes →
mismos outputs. Si no puedes decir EXACTAMENTE qué pesos sirvieron un request, no puedes debuggear ni rollback.

## HF Hub revisions
**Pin un commit SHA, nunca branch/tag** (las branches se mueven):
```python
model = AutoModel.from_pretrained("org/model", revision="a1b2c3d4")   # inmutable
```

## MLflow Model Registry — aliases, no stages
Las **stages se deprecaron en MLflow 2.9** (se removerán). Usa **aliases** (desde 2.8): `@champion`/`@challenger`
= punteros mutables nombrados a números de versión inmutables; a diferencia de stages, puedes poner **varios
aliases** a una versión (ideal canary/A-B):
```python
from mlflow import MlflowClient
c = MlflowClient()
v = c.create_model_version("avatar-lipsync", source=run_uri, run_id=run_id)   # lineage
c.set_registered_model_alias("avatar-lipsync", "challenger", v.version)
# en prod:  models:/avatar-lipsync@champion
```

## W&B Artifacts / DVC
**W&B Artifacts:** artefactos versionados+dedupeados (`model:v7` + aliases como `production`) con DAG de lineage.
**DVC:** Git-trackea un `.dvc` chico mientras los pesos multi-GB viven en S3/R2; `dvc.lock` graba hashes →
checkout byte-reproducible. Versiona la **data de training y los pesos** que el registry referencia.

## Versionado semántico de modelos
**MAJOR** = cambio breaking (output/formato de prompt incompatible) · **MINOR** = re-train con ganancia, misma
interfaz · **PATCH** = config/threshold. Codifícalo en el tag y el model card.

## Model cards
Cada versión trae card: uso intended, data de training + cutoff, resultados de eval (golden-set de ref 17),
limitaciones/sesgos, HW/VRAM, y **el digest exacto de imagen que la sirve**. Es tu audit trail.

## Promote → canary → rollback (atado al registry)
Train → log versión (inmutable) → evals → si pasa, `@challenger` → deploy a slice canary → compara vs
`@champion` → al éxito mueve `@champion` a la nueva versión; **rollback = reapunta `@champion` a la versión
previa** (instantáneo, sin rebuild). El serving (ref 16) resuelve el alias en el rollout.

## Reproducibilidad — pinea TODO
SHA del modelo, **digest** de imagen Docker, versiones CUDA/torch, lockfile (`uv.lock`/requirements con hashes),
versión del prompt template, params de inferencia (sampler/steps/seed). Una versión solo es reproducible si TODO esto se graba junto.

## Gotchas
1. Cargar modelos HF por branch/tag = no reproducible — pin el commit SHA.
2. Las **stages de MLflow están deprecadas** — código nuevo usa aliases; mezclar confunde el tooling.
3. Los aliases son *punteros mutables* — nunca asumas que `@champion` es la misma versión en el tiempo; loguea el número resuelto por request.
4. DVC sin remote configurado deja archivos grandes sin trackear en silencio.
5. Un model card sin el digest de imagen no reproduce una inferencia pasada — los pesos no bastan.

**Fuentes:** mlflow.org/docs (Model Registry workflow) · github.com/mlflow/mlflow/issues/10336 (deprecating stages) · huggingface.co/docs/huggingface_hub · dvc.org/doc.

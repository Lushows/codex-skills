# 301 · IaC: Terraform / OpenTofu / Pulumi (cuándo, y cuándo NO)

> [[29-iac-deploy]] toca Terraform de pasada; aquí la decisión completa: state, módulos, drift, y la
> pregunta honesta — ¿IaC o el dashboard del PaaS basta? Para una marca/STUDIO, casi siempre el dashboard.

## ¿IaC o no? (la decisión que ahorra meses)
| Situación | Veredicto |
|---|---|
| 1 app en Render/Vercel/RunPod, 1–2 personas | **Dashboard + `render.yaml`** (ver [[299-...]]). IaC es overhead. |
| Recursos cloud crudos (VPC, IAM, buckets, DNS, colas) repetibles | **IaC sí.** |
| Multi-entorno (dev/stg/prod) idénticos que deben no driftear | **IaC sí.** |
| Necesitas reproducir TODO desde cero / disaster recovery auditado | **IaC sí.** |
La trampa: montar Terraform para 3 recursos que tocas una vez al mes. El `tfstate` se vuelve una carga
mayor que el problema. Empieza con clicks; **gradúa a IaC cuando el click ya no escala**.

## Las tres herramientas (2026)
| | Lenguaje | Licencia | Notas |
|---|---|---|---|
| **Terraform** | HCL (DSL) | **BSL 1.1** (revierte a MPL en 2027 para 1.6+) | ecosistema más grande, registry oficial |
| **OpenTofu** | HCL (drop-in) | **MPL 2.0** (libre, Linux Foundation) | fork GA ene-2024; features que upstream no tiene; reemplazo creíble |
| **Pulumi** | TS/Python/Go/C# | **Apache 2.0** | lenguajes reales (loops/tests), no DSL; ideal si el equipo ya es dev |

Para Lushows (TS/JS): **Pulumi** evita aprender HCL. Para máxima compatibilidad de módulos/registry y
licencia libre: **OpenTofu**. Terraform "puro" solo si una herramienta lo exige.

## State: el corazón (y el pie de bala)
`*.tfstate` es **el source of truth** de lo desplegado. Reglas no negociables:
- **Remoto + locking**: S3+DynamoDB, GCS, o el backend nativo de Terraform/Tofu Cloud / Pulumi Cloud.
  Sin lock, dos `apply` concurrentes **corrompen** el state.
- **Nunca lo commitees**: contiene secrets en claro y dos personas pisándolo lo rompe.
- **Nunca lo edites a mano**; si diverge, `import` / `state rm`, no notepad.

## Módulos: DRY de verdad
```hcl
module "worker_endpoint" {
  source       = "./modules/runpod-endpoint"
  gpu_type     = "H100"
  image_digest = var.worker_digest   # el SHA del worker (ver [[16-cicd-modelos-workers]])
  volume_id    = module.storage.volume_id
}
```
Un módulo = set reusable con `variables` (input) y `outputs`. Un dir/workspace por entorno
(`envs/prod`, `envs/stg`) con los mismos módulos y distintos `.tfvars` → entornos idénticos sin copiar-pegar.

## Drift detection: el silencio que te muerde
Drift = alguien tocó la consola y el mundo real ya no matcha el state. El siguiente `apply` quiere
**destruir** algo que está en uso. Defensa: **`plan` programado** (cron/CI) que alerta si hay diff.
```yaml
# .github/workflows/drift.yml
on: { schedule: [{ cron: "0 */6 * * *" }] }   # cada 6h
jobs:
  drift:
    steps:
      - run: tofu plan -detailed-exitcode || echo "::warning::drift detectado" # exit 2 = hay cambios
```
Equipos con drift-check cada 6h cazan cambios manuales en horas, no semanas después en un apply sorpresa.

## Flujo y disciplina
`init → plan → apply`. **El `plan` se revisa en el PR** (igual que código). CD: `apply` solo tras merge a
`main`, con OIDC para asumir el rol cloud (sin keys largas — ver [[297-cicd-pipelines-github-actions]]).
**Pinea versiones de providers** (`required_providers`) o un update silencioso cambia tu infra.

## Gotchas
1. `tfstate` commiteado o local sin lock → secrets filtrados / corrupción en runs concurrentes.
2. IaC para 3 recursos = overhead > beneficio; usa el dashboard hasta que escale.
3. Cambio manual en consola sin drift-check → `apply` futuro destruye lo que alguien usa.
4. Providers sin pinear → update silencioso re-crea recursos.
5. Secrets en `.tfvars` commiteados; van a un secret manager o vars de CI, no al repo.

**Fuentes:** opentofu.org · developer.hashicorp.com/terraform (BSL/remote state) · pulumi.com/docs/iac/comparisons · encore.dev/resources/opentofu-vs-terraform-2026.
Cruza con [[29-iac-deploy]].

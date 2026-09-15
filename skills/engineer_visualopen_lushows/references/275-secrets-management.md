# 275 · Gestión de secretos: vaults, rotación, env vars

> Un `ANTHROPIC_API_KEY` commiteado se descubre en minutos por bots que escanean GitHub.
> Los secretos no se "guardan bien": se **centralizan, se rotan y se inyectan en runtime**.
> El `.env` en disco es un punto de partida, no un destino.

## La jerarquía (de peor a mejor)
1. **Hardcoded en código** ☠️ — en el repo para siempre, en cada fork, en cada clon.
2. **`.env` en `.gitignore`** — mínimo viable; secreto en texto plano en disco, sin rotación ni audit.
3. **Env vars del PaaS** (Render/Railway/Vercel/Fly secrets) — inyectadas en runtime, no en disco
   del repo. Suficiente para proyectos pequeños (caso BIO-SETA, AGENTE STUDIO).
4. **Secret manager dedicado** (Vault, AWS/GCP Secrets Manager, Doppler, Infisical) — versionado,
   rotación, ACL por servicio, audit log, leasing dinámico. Para producción seria/multi-servicio.

## Herramientas y cuándo
| Herramienta | Modelo | Brilla en |
|---|---|---|
| **HashiCorp Vault** | servidor central, secretos **dinámicos** (credenciales DB efímeras con TTL), transit-encrypt | infra grande, zero-standing-privilege |
| **Doppler / Infisical** | SaaS/self-host, sincroniza a PaaS/CI, UI | equipos que quieren un panel y sync fácil |
| **SOPS + age/KMS** | cifra el archivo, lo commiteas **cifrado** en git | GitOps/IaC, secretos versionados con el código |
| **AWS/GCP Secrets Manager** | nativo cloud, rotación automática + IAM | ya vives en ese cloud |
| **PaaS env secrets** | inyección runtime simple | apps mono-servicio en Render/Vercel |

**SOPS** resuelve la tensión "quiero secretos en git pero no en plano": cifra valores con una clave
(age o KMS), el archivo cifrado es seguro en el repo, se descifra en deploy. Encaja con IaC ([[29-…]]).

## Rotación — el secreto que no rota es deuda
- **Rota tras cualquier exposición** (commit, log, ex-empleado) y **periódicamente** (90 días típico).
- **Rotación sin downtime**: soporta **dos secretos válidos a la vez** (overlap). Despliega el nuevo,
  migra consumidores, revoca el viejo. Sin overlap, rotar = caída.
- **Secretos dinámicos** (Vault): credenciales con TTL que expiran solas → la rotación es el default,
  no un evento. La credencial de DB vive horas, no años.
- Versiona secretos (Secrets Manager guarda versiones) → rollback si el nuevo rompe algo.

## Inyección en runtime — no en la imagen
- **Inyecta por env var en el arranque** (el orquestador/PaaS lo hace), no hornees secretos en la
  imagen Docker (quedan en las capas, `docker history` los muestra) ni en el `.env` del build.
- En K8s: **External Secrets Operator** o CSI driver montan desde el vault como env/volumen.
  Evita `Secret` de K8s a secas (base64 ≠ cifrado; va en etcd en claro si no hay encryption-at-rest).
- **Nunca pases secretos como build-args de Docker** ni como flags de CLI (quedan en `ps`/history).

## No filtrarlos
- **Pre-commit**: `gitleaks` / `git-secrets` como hook + en CI → bloquea el push con un secreto.
- **GitHub/GitLab secret scanning + push protection** activado a nivel repo/org.
- **No loguees** bodies, headers `Authorization`, ni objetos config completos. Redacta en el logger
  (allow-list de campos logueables). Cuidado con APM/error-trackers que capturan el contexto.
- Si se filtró: **rota primero, investiga después**. Reescribir la historia de git (BFG/filter-repo)
  **no** invalida el secreto — ya está en clones, forks, caché. Asume comprometido.

## Secretos de modelos / pesos
Las API keys de HuggingFace/registries y los tokens R2/S3 son secretos: mismas reglas. Un `HF_TOKEN`
en una imagen pública filtra acceso a modelos privados. Inyecta por env del worker, no en el Dockerfile.

## Gotchas
1. `.env` commiteado "solo una vez" → vive en la historia; rota ese secreto ya.
2. Secreto en build-arg de Docker → persiste en capas aunque borres el ENV después.
3. K8s `Secret` sin encryption-at-rest → base64 plano en etcd, leíble por cualquiera con acceso.
4. Rotar sin ventana de solapamiento → los consumidores con el viejo caen en el corte.
5. Error-tracker que captura variables locales → tu secreto acaba en el dashboard del SaaS.

**Fuentes:** cheatsheetseries.owasp.org (Secrets Management) · developer.hashicorp.com/vault/docs ·
github.com/getsops/sops · github.com/gitleaks/gitleaks · docs CIS Benchmark.

Cruza con [[29-iac-deploy]] y [[247-model-supply-chain-pickle-safetensors]].

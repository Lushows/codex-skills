# 334 · Deploy en stores (App Store / Play, revisión, OTA con EAS Update, versionado)

> Publicar no es `eas submit` y listo: es pasar revisión humana + diseñar qué se actualiza por binario y qué por OTA.
> Y en 2026 Apple endureció qué puede cambiar una app sin pasar por review.

## Pipeline EAS Build → Submit
```
eas build --profile production --platform all     # binarios firmados en la nube
eas submit --profile production --platform all     # sube a ASC / Play Console
```
- **iOS**: necesitas Apple Developer ($99/año), App Store Connect API key (EAS la usa para subir sin Xcode), bundle id, capacidades (push, etc.) declaradas.
- **Android**: Play Console ($25 único), AAB firmado (Play App Signing), service account JSON para `eas submit`.
- **Internal/TestFlight + Internal Testing track**: prueba con reviewers reales antes de producción. TestFlight no pasa full review; producción sí.

## Revisión — qué tumba apps
- **Apple**: privacy manifest + nutrition labels obligatorios; login social → si pides datos, ofrece **Sign in with Apple**; nada de placeholders/crashes; permisos con justificación en `Info.plist` (cámara/micro/fotos — clave para apps de avatar/IA). Apps de IA generativa: declara moderación de contenido o rebote.
- **Google Play**: Data safety form, target SDK al día (API 35/36), declaración de permisos sensibles, política de contenido para IA. Política dura: **una app NO puede actualizarse por un mecanismo distinto al de Play** ni descargar código ejecutable (dex/JAR/.so) fuera de Play.

## OTA con EAS Update — la línea que NO cruzas
```
eas update --branch production --message "fix copy"
```
- OTA mueve **solo JS + assets**. Código nativo = build+submit nuevos.
- **Apple aplica test funcional** (no "¿hubo push?" sino "¿cambió lo que la app fundamentalmente hace?"). En 2026 Apple bloqueó/retiró apps (Replit, Vibecode, "Anything") por **generar y ejecutar código que se auto-modifica en runtime**. Un **bundle JS fijo que solo llama APIs nativas ya auditadas** está del lado correcto desde siempre.
- Google: bundle JS interpretado OK; **descargar y ejecutar código nativo nuevo = violación**.
- Regla práctica: OTA para **bugfixes, copy, tweaks de UI, feature flags**. NO para reescribir el propósito de la app ni meter funciones nativas nuevas a escondidas.

## Versionado — binario vs OTA
- **`runtimeVersion`** ata un update OTA a builds con código nativo compatible. Si cambia lo nativo, **sube runtimeVersion** → los updates viejos no aplican a binarios nuevos y viceversa (evita crashes por mismatch).
- Políticas: `appVersion` (ata a la versión semántica), `sdkVersion`, o fingerprint (hash del proyecto nativo, lo más preciso).
- Esquemas tipo **PaceVer** [no verificado como estándar] separan "release que requiere binario" de "release que va directo a devices".
- `version` (visible en store) + `buildNumber`/`versionCode` (entero creciente, lo exige cada submit). EAS puede **auto-incrementar** (`autoIncrement` en `eas.json`).

## Phased / staged rollout
- **Play**: staged rollout por % (5%→20%→100%) desde Play Console; pausa/reanuda si suben crashes. `eas submit` sube; el rollout se controla en consola o vía `--rollout`.
- **iOS**: Phased Release for automatic updates (7 días, % creciente) en ASC; review manual lo expone primero a TestFlight.
- **OTA staged**: EAS Update soporta **rollouts graduales** por branch/canal y **rollback** instantáneo (re-publica el update anterior) — un OTA malo se revierte en minutos sin pasar por tienda. Por eso bugfix crítico va por OTA, no por binario.

## Canales y entornos
- `eas.json` define perfiles: `development` (dev-client), `preview` (interno/QA, distribución ad-hoc/internal), `production` (store).
- **EAS Update channels** mapean a branches: build de `production` escucha canal `production`; QA usa `preview`. Así un mismo binario recibe el update correcto sin recompilar.

## CI/CD
Conecta esto a [[297-cicd-pipelines-github-actions]]: en push a `main` → `eas build` + `eas submit` (binario) o `eas update` (OTA) según qué cambió. Distingue ramas: `production` vs `preview` (PR builds con `eas build` + QR para QA).

## Gotchas
1. OTA a runtime incompatible → crash en cold-start; respeta `runtimeVersion`.
2. `versionCode`/`buildNumber` repetido → submit rechazado; auto-incrementa.
3. Apple rebota por permisos sin descripción, IA sin moderación, o falta Sign in with Apple.
4. Play rebota por Data safety incompleta o target SDK viejo.
5. Primer review tarda días: no prometas fecha; deja buffer. OTA luego es minutos.

**Fuentes:** docs.expo.dev/eas-update/introduction · capgo.app/blog/first-time-app-review-guide · bitrise.io OTA policy.

Cruza con [[297-cicd-pipelines-github-actions]] y [[333-push-notifications]].

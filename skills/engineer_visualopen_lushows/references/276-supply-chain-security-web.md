# 276 · Supply-chain web: dependencias, lockfiles, SRI, sandboxing

> En 2025 el npm pasó de "nuisance" a arma: el gusano **Shai-Hulud** se auto-replicó publicando
> paquetes maliciosos, y el incidente de **chalk/debug** (18 paquetes, miles de millones de
> descargas/semana) inyectó robo de cripto vía phishing a un maintainer. Tu `node_modules` es
> código de terceros que corre con tus permisos. Trátalo como hostil.

## El modelo de amenaza
- **Cuenta de maintainer comprometida** (phishing/token robado) → publica versión troyana.
- **Typosquatting / dependency confusion**: `reqeusts`, o un paquete interno con el mismo nombre en
  el registry público con versión mayor → el resolver baja el malicioso.
- **Postinstall scripts**: `npm install` ejecuta `postinstall` con tus permisos → exfiltra `.env`,
  `~/.aws`, tokens de CI. El vector favorito.
- **Transitivas**: no instalaste el paquete malo; lo trajo una dependencia de tu dependencia.

## Lockfiles — el ancla de integridad
El `package-lock.json` / `pnpm-lock.yaml` / `yarn.lock` fija **versión exacta + hash SRI (SHA-512)**
de cada paquete (campo `integrity`). En CI usa **`npm ci`** (no `npm install`): instala exactamente
el lock y **falla si el hash no coincide** → detecta tampering del tarball.

```
npm ci            # determinista, respeta el lock, falla ante mismatch
npm install       # puede actualizar el lock silenciosamente — NO en CI
```

- Commitea el lockfile **siempre**. Sin él, cada build resuelve versiones nuevas → no reproducible.
- Revisa los **diffs del lockfile** en PRs: un cambio de `resolved`/`integrity` inesperado es señal.

## Bloquear postinstall y demorar adopción
- **`--ignore-scripts`** por defecto (`npm config set ignore-scripts true`); habilita scripts solo
  para los pocos paquetes que de verdad los necesitan (`allow-scripts`/`can-i-ignore-scripts`).
- **`minimumReleaseAge` / cooldown**: NO instales versiones recién publicadas. pnpm soporta
  `minimumReleaseAge` (instala solo versiones con N días de antigüedad). CIS recomienda ≥60 días
  para paquetes nuevos → da tiempo a que la comunidad detecte la versión maliciosa antes que tú.
- **pnpm trust levels**: clasifica versiones por *Trusted Publisher* / *Provenance* / *sin evidencia*
  y avisa de downgrades de confianza.

## SCA y auditoría continua
- **`npm audit` / `pnpm audit` / `osv-scanner`** en CI contra la advisory DB. Falla el build en
  *high/critical*. Complementa con **Dependabot/Renovate** para PRs de upgrade (con cooldown).
- **SCA real** (Socket.dev, Snyk, Endor): no solo CVEs — detectan *comportamiento* (un paquete que de
  repente abre red, lee `process.env`, ofusca código). Los CVEs llegan tarde; el ataque es nuevo.
- Minimiza la superficie: menos deps = menos riesgo. Audita transitivas (`npm ls`), elimina las muertas.

## Provenance y SLSA — útil pero no bala de plata
**npm provenance** (Sigstore/SLSA L3, GA desde 2023) firma un vínculo verificable entre versión
publicada ↔ commit fuente ↔ pipeline de build. Publica con `npm publish --provenance` desde CI.
**Límite descubierto en 2025**: Shai-Hulud publicó paquetes con provenance **válida** — la firma
prueba *qué pipeline* construyó el paquete, no que el estado interno del pipeline estuviera limpio.
Provenance sube el listón, no lo cierra. Combínala con cooldown + SCA de comportamiento.

## SRI en el frontend (CDN)
Si cargas JS/CSS de un CDN, el **Subresource Integrity** garantiza que el byte servido es el que
esperas — si el CDN es comprometido, el navegador rechaza el recurso alterado:

```html
<script src="https://cdn.x/lib.js"
        integrity="sha384-BASE64HASH" crossorigin="anonymous"></script>
```

Genéralo (`openssl dgst -sha384 -binary file | openssl base64 -A`). Combínalo con CSP
`require-sri-for script style` donde aplique. **Self-host** los assets críticos cuando puedas:
elimina el CDN del modelo de amenaza.

## Sandboxing del build y runtime
- **CI con permisos mínimos**: tokens de publish de corta vida, OIDC en vez de secretos estáticos,
  el job de `install` sin acceso a secretos de producción (separa install de deploy).
- **`postinstall` en contenedor sin red ni montaje de `~`** cuando sea posible.
- Runtime: corre la app como usuario no-root, read-only FS, sin capabilities extra (alinea con
  [[247-model-supply-chain-pickle-safetensors]] para pesos: nunca `pickle` no confiable, prefiere safetensors).

## Gotchas
1. `npm install` en CI (en vez de `npm ci`) → el lock se actualiza solo y el hash-check se pierde.
2. Lockfile no commiteado → builds no reproducibles, ataque indetectable por diff.
3. Confiar en provenance como prueba de "limpio" → un pipeline comprometido firma malware válido.
4. Auto-merge de Dependabot sin cooldown → adoptas la versión troyana en horas.
5. SRI omitido en un solo `<script>` de CDN → ese es el que te compromete.

**Fuentes:** unit42.paloaltonetworks.com (npm threat landscape) · socket.dev/blog (Shai-Hulud) ·
docs.npmjs.com (provenance) · pnpm.io/settings (minimumReleaseAge) · developer.mozilla.org (SRI) ·
CIS Software Supply Chain Benchmark.

Cruza con [[247-model-supply-chain-pickle-safetensors]].

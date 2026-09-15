# 95 — Tooling moderno (2026)

La toolchain se fue casi entera a **Rust/Go/Zig**. Versiones (jun 2026):

- **Vite 8** — major sobre **Rolldown** (bundler Rust de VoidZero, reemplaza Rollup/esbuild internamente). Rolldown **1.0 RC ene 2026**. Builds **1.6×-7.7× más rápidos** que Vite 7.
- **Vite+ (`vite-plus`)** — toolchain unificada de VoidZero (**alpha 2026**): un tool con Vite+Vitest+Oxlint+Oxfmt+Rolldown+tsdown, cero config. El "una binary para todo".
- **Bun 1.3.x** (1.3.13) — **runtime + package manager + bundler + test runner** en Zig, ~3× Node. REPL nativo, `--compile`, decorators ES, Windows ARM64. Aceptado como package manager (Turborepo lo soporta stable).
- **Biome 2.x** (2.4.15) — **linter + formatter** en Rust, drop-in de ESLint+Prettier con un config. v2 añadió scanner multi-archivo + primeros plugins.
- **Oxc / oxlint / oxfmt** — la toolchain Rust bajo Vite+. **oxlint 50-100× más rápido que ESLint**; oxfmt ~30× Prettier. Tradeoff: ecosistema de reglas/plugins más chico que ESLint.
- **pnpm** — el package manager default para monorepos (content-addressable, strict node_modules). **Turbopack** — bundler Rust de Next, stable y default en Next 16. **esbuild/SWC** — siguen como transpilers internos.

## Monorepo
- **Turborepo 2.9.x** (Rust) — task runner + remote caching, soporte Bun stable, worktrees. Filosofía "solo cachea mis tasks". Lean.
- **Nx 22.x** (22.7.5) — "build platform" pesado: CI que auto-fixea PRs, graph UI, soporte .NET/Maven. Para orgs grandes políglotas.

```bash
bun create vite@latest my-app        # stack lean 2026
bunx biome check --write .           # lint+format en una pasada Rust
npx tsgo --noEmit                    # type-check 10×
```

## Gotchas
1. Vite 8 + Rolldown es nuevo — algunos plugins Rollup no portaron; verifica tu ecosistema antes de upgrade desde Vite 7.
2. Vite+ es **alpha** — no lo apuestes en un producto que shippea.
3. Bun-as-runtime aún tiene gaps Node-API; algunos native addons fallan — Bun-as-package-manager es más universal/seguro.
4. Migrar ESLint→Biome/oxlint: reglas custom/community pueden no tener equivalente; audita tu ruleset.
5. Mezclar package managers en un monorepo (un app Bun, otra pnpm) rompe lockfiles — estandariza por repo.
6. Turborepo vs Nx es filosofía, no solo perf — Nx pesa en repos chicos; Turborepo se siente delgado en políglotas grandes.

**Fuentes:** alexcloudstar.com (Vite 8/Rolldown/Oxc 2026) · voidzero.dev/posts · github.com/oven-sh/bun/releases · biomejs.dev/blog · nx.dev/blog (Nx 22).

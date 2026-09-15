# 92 — El stack de frameworks 2026 (alternativas a Next)

El landscape se consolidó duro en 2025-26. Versiones actuales:

- **Astro 6.4.x** (sobre **Vite 7**). ⚠️ **Cloudflare adquirió Astro en enero 2026** → edge-first. **Cero JS por
  default** vía islands; solo hidrata lo que marcas. **Content Layer** + **Server Islands** (cache de shell estático
  + stream de islands dinámicas personalizadas). Framework-agnóstico (mezcla React/Vue/Svelte/Solid). **Úsalo para:** sitios content-heavy, blogs, marketing, docs, catálogos e-commerce donde el payload JS importa.
- **SvelteKit 2.57.x + Svelte 5.55.x** — los **runes** (`$state`, `$derived`, `$effect`, `$props`) reemplazaron el
  `$:` implícito con un modelo explícito basado en signals (funciona fuera de `.svelte`). + **remote functions** (calls cliente→server tipados). Runtime más chico, sin VDOM. **Úsalo para:** apps donde bundle size y perf runtime son prioridad.
  ```svelte
  <script> let count = $state(0); let double = $derived(count*2) </script>
  ```
- **React Router 7** (ex-Remix) — el merge Remix/RR está hecho; RR7 = el path canónico "framework mode" (SSR,
  loaders, actions, nested routing sin la complejidad RSC de App Router). **Remix 3** se reimagina como framework **bundler-free** (track aparte). **Úsalo para:** equipos React con SSR+loaders sin comprometerse a RSC/Next.
- **TanStack Start** — full-stack React/Solid sobre TanStack Router + Nitro. Type-safe end-to-end. **Aún RC** (pre-1.0) a mid-2026.
- **Nuxt 4** (Vue 3) — file routing, auto-imports, Nitro, hybrid rendering. Maduro. Para Vue shops.
- **Qwik / Qwik City** — **resumability** (serializa estado de ejecución y *resume* donde el server paró → ~O(1) JS en load sin importar el tamaño). Para apps muy grandes donde TTI debe quedar plano.
- **SolidStart** — full-stack Solid con signals fine-grained (sin VDOM ni re-render).

**Rendering recap:** SSG (build), SSR (per-request), ISR (revalidate), streaming SSR (chunks + Suspense), islands/resumability (ship menos JS).

## Gotchas
1. La adquisición CF de Astro puede sesgar features a CF edge — vigila adapter/lock-in.
2. Los runes de Svelte 5 son cambio de modelo mental breaking; hábitos de Svelte 4 confunden.
3. TanStack Start aún RC — pinea versiones, espera churn antes de 1.0.
4. "Remix" es ambiguo ahora: aclara si es **React Router 7** (el merge) o el **Remix 3** bundler-free.
5. Islands complican estado cliente compartido entre islands — necesitas nano-stores/signals, no props.
6. La resumability de Qwik requiere estado serializable en todos lados; closures sobre valores no-serializables rompen.

**Fuentes:** github.com/withastro/astro/releases · astro.build/blog · svelte.dev/blog · github.com/sveltejs/kit/releases · qwik.dev.

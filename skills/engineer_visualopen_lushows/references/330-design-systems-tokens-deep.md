# 330 · Design systems y tokens a fondo (DTCG, theming, shadcn/registry)

> Un token no es "una variable de color". Es la fuente única de verdad que viaja de Figma al CSS sin
> que nadie copie un hex a mano. Sin tokens, el dark-mode y el rebranding son refactors infernales.

## DTCG: el formato estándar (estado 2026)
- El **Design Tokens Format Module** del W3C Community Group alcanzó su **primera versión estable (v1)**
  en oct 2025: multi-archivo, theming y color avanzado resueltos. NO es estándar W3C formal, pero es el
  de facto (editado por Adobe, Google, Microsoft, Figma, Salesforce, Shopify…). [verificado 2026]
- Forma del token (JSON): `$value`, `$type`, `$description`. Aliases con `{group.token}` que se resuelven
  automáticamente. Agrupación por objeto anidado.
  ```json
  { "color": { "brand": { "500": { "$type": "color", "$value": "#10b981" } },
    "bg":    { "accent": { "$value": "{color.brand.500}" } } } }
  ```
- Tooling: **Style Dictionary** (transforma DTCG → CSS vars / Tailwind / iOS / Android), Tokens Studio
  (Figma ↔ tokens), Terrazzo. El JSON es el origen; lo demás se genera.

## Las tres capas de tokens (no saltárselas)
| Capa | Qué es | Ejemplo |
|---|---|---|
| **Primitivos** (global) | Paleta cruda, sin semántica | `green-500: #10b981`, `space-4: 16px` |
| **Semánticos** (alias) | Intención, apuntan a primitivos | `color-bg-accent → green-500` |
| **Componente** | Específicos de un componente | `button-bg-primary → color-bg-accent` |

El dark-mode y el theming SOLO tocan la capa semántica: el botón apunta a `color-bg-accent` y ese alias
cambia de valor según el tema. Nunca hardcodees primitivos en componentes.

## Theming y dark-mode
- En CSS: variables en `:root` y override en `[data-theme="dark"]` o `.dark`. El componente lee la var,
  no el hex. Cambiar tema = cambiar el mapa semántico, cero cambios en componentes.
- **No inviertas colores** para dark: el dark bien hecho desatura, sube luminancia de texto, evita negro
  puro (#000) → usa #0a0a0a/#111 para reducir el halo. Sombras → menos opacas o bordes sutiles.
- Multi-brand: cada marca = un set de valores semánticos sobre los mismos nombres. Un solo build, N temas.
- `color-scheme: light dark` + `prefers-color-scheme` para respetar el SO; permite override manual persistido.

## shadcn/ui y el modelo registry
- **shadcn no es una librería npm**: copia el código del componente a tu repo (lo posees, lo editas).
  Se apoya en Radix (a11y) + Tailwind + CSS vars semánticas (`--background`, `--foreground`, `--primary`…).
- **Registry**: distribuís tus propios componentes/tokens vía `components.json` + un registry JSON; el CLI
  (`npx shadcn add <url>`) los instala. Tu design system propio servido como registry = consistencia real
  entre apps sin publicar paquetes. (Ver skill [[vercel:shadcn]] para CLI/registry a fondo.)
- Sus tokens ya están en capa semántica → se mapean 1:1 con tu pipeline DTCG.

## Gobernanza (lo que mantiene vivo el sistema)
- Naming consistente y documentado; un token mal nombrado se propaga para siempre.
- Versionado del paquete de tokens (semver); breaking change de un semántico = major.
- Source of truth única: Figma variables ↔ DTCG JSON sincronizados; prohibido el hex suelto en código.
- Linter/CI que falle si un componente usa un valor literal en vez de un token.
- Documentación viva (Storybook + tabla de tokens autogenerada desde el JSON).

## Errores
- Saltarse la capa semántica → dark-mode imposible sin tocar cada componente.
- Demasiados primitivos sin semántica → nadie sabe cuál usar.
- Tokens que no viajan a código (se quedan en Figma) → drift diseño/dev.
- Hardcodear en dark con `!important` → deuda eterna.

Cruza con [[88-design-systems-tokens]] y [[277-component-architecture-patterns]].

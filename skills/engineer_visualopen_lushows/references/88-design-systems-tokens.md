# 88 — Design systems & tokens

## Design tokens
Pares clave-valor nombrados y platform-agnostic (`color.brand.primary = #4F46E5`). Hito 2026: el formato **W3C
DTCG** llegó a su **primera versión estable (oct 2025)** — JSON vendor-neutral, tokens tipados (`$type`) que se referencian (`{color.base.blue}`).

## Arquitectura de 3 capas (el consenso)
- **Primitive/global** (reference): paleta cruda — `blue.500`, `space.4`. Sin semántica.
- **Semantic/alias**: por intención, referencia primitives — `color.action.bg → {blue.500}`. **Esta capa es la que swapean los themes.**
- **Component**: scoped — `button.primary.bg → {color.action.bg}`.
Esta indirección hace baratos dark mode y multi-brand: solo re-mapeas la capa semántica por theme.
```json
{ "color": { "blue": {"500":{"$type":"color","$value":"#3b82f6"}},
  "action": {"bg":{"$type":"color","$value":"{color.blue.500}"}} } }
```

## El pipeline
**Style Dictionary v4** (soporte DTCG) ingiere `.tokens.json` y compila a CSS vars/Tailwind/iOS/Android/JS
(`npx style-dictionary build`). **Figma→code:** diseñadores en **Figma Variables** (modes=themes) → exportan vía **Tokens Studio** (emite DTCG JSON) → Git → Style Dictionary compila.

## shadcn/ui — el paradigma copy-paste
En vez de dep npm, un CLI **copia el código fuente** (sobre **Radix UI** + Tailwind) a TU repo. Tú lo dueñas/editas,
sin version-lock. Theming por CSS vars de tu capa de tokens. `npx shadcn@latest add button dialog`. **El registry**
(killer feature 2026): un `registry.json` distribuye no solo componentes sino hooks/utils/**tokens**/feature-kits/
convenciones/CI/instrucciones de agente IA — la base de design systems internos. **Radix** = primitivos accesibles unstyled (focus/ARIA/keyboard). **Storybook** = workshop/docs + visual regression.

## Gotchas
1. No te saltes la capa semántica — componentes referenciando primitives = theming imposible.
2. La sintaxis `$value`/`$type` DTCG difiere del token JSON legacy — configs viejos de Style Dictionary necesitan migración a v4.
3. Los Figma Variable modes no mapean 1:1 a grupos DTCG anidados — el config de export de Tokens Studio importa.
4. Los componentes shadcn son un *snapshot*, no una dependencia — no recibes fixes upstream automáticos; trackea changelogs.
5. Colisiones de nombres de tokens entre registries/brands compuestos — namespacéalos.
6. Radix es solo comportamiento; sin tus estilos visibles de foco falla accesibilidad pese a la a11y de Radix.

**Fuentes:** w3.org/community/design-tokens · styledictionary.com/info/dtcg · ui.shadcn.com/docs/changelog · radix-ui.com.

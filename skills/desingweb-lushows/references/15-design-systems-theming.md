# 15 — Design systems, tokens & theming multi-marca

Frontera 2026 de design tokens, theming y sistemas multi-marca. Patrones a nivel código (vanilla CSS y React+Tailwind) para **levantar muchas webs on-brand rápido** y construir product UIs reales. **Léelo cuando construyas algo con tema/marca conmutable, un sistema reutilizable, o varias marcas sobre un codebase** (AGENTE STUDIO multi-marca, FACTUM, dashboards). Pareja de 02 (color) y 13 (app UI).

---

## 1. Arquitectura de tokens de 3 capas (la que escala)

Modelo canónico (Radix, shadcn, Geist, Material 3). **Regla de oro:** los componentes **nunca** consumen primitives directamente; solo semantic tokens. Re-theme = cambiar una capa, no un find-and-replace global.

**Tier 1 — Primitive/Global** (raw values, sin significado — *cómo se ve*):
```css
:root{
  --blue-500:oklch(.62 .19 256); --gray-50:oklch(.985 0 0); --gray-900:oklch(.21 0 0);
  --space-1:.25rem; --space-2:.5rem; --space-4:1rem; --space-6:1.5rem; --space-8:2rem;
  --radius-sm:.25rem; --radius-md:.5rem; --radius-lg:.75rem; --radius-full:9999px;
  --text-xs:.75rem; --text-sm:.875rem; --text-base:1rem; --text-lg:1.125rem; --text-xl:1.25rem; --text-2xl:1.5rem;
  --font-weight-normal:400; --font-weight-medium:500; --font-weight-semibold:600;
  --shadow-sm:0 1px 2px oklch(0 0 0/.05); --shadow-md:0 4px 8px -2px oklch(0 0 0/.10); --shadow-lg:0 12px 24px -6px oklch(0 0 0/.15);
  --z-dropdown:1000; --z-sticky:1100; --z-overlay:1300; --z-modal:1400; --z-popover:1500; --z-toast:1700;
  --duration-fast:100ms; --duration-normal:200ms; --duration-slow:320ms;
  --ease-out:cubic-bezier(0,0,.2,1); --ease-in-out:cubic-bezier(.4,0,.2,1);
}
```
**Tier 2 — Semantic/Alias** (dan contexto; **esto es lo que se themea**). El par **bg/fg** y los niveles **surface/elevation** son la columna vertebral:
```css
:root{
  --color-bg:var(--gray-50); --color-surface:oklch(1 0 0); --color-surface-raised:oklch(1 0 0); --color-surface-sunken:var(--gray-50);
  --color-fg:var(--gray-900); --color-fg-muted:oklch(.55 0 0); --color-fg-subtle:oklch(.65 0 0);
  --color-border:oklch(.92 0 0); --color-border-strong:oklch(.85 0 0); --color-ring:var(--brand-8);
  --color-accent:var(--brand-9); --color-accent-hover:var(--brand-10); --color-accent-fg:oklch(.99 0 0);
  --color-success:oklch(.62 .17 150); --color-success-bg:oklch(.96 .04 150);
  --color-danger:oklch(.58 .24 27); --color-danger-bg:oklch(.96 .05 27);
  --color-warning:oklch(.70 .17 75); --color-info:oklch(.62 .16 240);
}
```
**Tier 3 — Component** (opcional; solo si un componente debe desviarse): `--{component}-{prop}-{variant}`. La mayoría de componentes deben vivir con Tier 2; inflar Tier 3 es deuda.

## 2. Multi-brand en la práctica (un codebase, N marcas)

Primitives + component fijos; **solo se sobrescribe Tier 2** vía `data-brand` (marca) ortogonal a `data-theme`/`.dark` (modo). Se combinan.
```css
[data-brand="biofungi"]{ --brand-seed:oklch(.55 .15 150) } /* esmeralda */
[data-brand="acme"]    { --brand-seed:oklch(.60 .20 256) } /* azul */
[data-brand="lush"]    { --brand-seed:oklch(.62 .24 350) } /* magenta */
```
**Derivar escala 1→12 desde UN seed con relative color syntax (OKLCH)** — varía L (suaviza C en extremos), H constante → pasos perceptualmente uniformes:
```css
[data-brand]{
  --brand-1:oklch(from var(--brand-seed) .99 calc(c*.10) h);
  --brand-3:oklch(from var(--brand-seed) .95 calc(c*.40) h);
  --brand-6:oklch(from var(--brand-seed) .83 calc(c*.80) h);
  --brand-8:oklch(from var(--brand-seed) .68 c h);
  --brand-9:var(--brand-seed);                                /* accent solid */
  --brand-10:oklch(from var(--brand-seed) calc(l - .05) c h); /* hover */
  --brand-11:oklch(from var(--brand-seed) .52 calc(c*.9) h);  /* texto low-contrast */
  --brand-12:oklch(from var(--brand-seed) .25 calc(c*.6) h);  /* texto high-contrast */
}
```
Alternativa con mejor soporte legacy (`color-mix`): `--brand-3:color-mix(in oklch,var(--brand-seed) 12%,white); --brand-10:color-mix(in oklch,var(--brand-seed) 88%,black);`
**Dark por marca** (combina atributos, invierte rampa):
```css
[data-theme="dark"]{ --color-bg:var(--gray-950); --color-surface:var(--gray-900); --color-fg:var(--gray-50);
  --color-accent:var(--brand-8); --color-border:oklch(1 0 0/.10) }
```
**Switch runtime (cero flash):** setea el atributo en `<html>` antes de pintar. Inyecta un script bloqueante en `<head>` que lea `localStorage` y aplique el atributo **antes** del primer paint (evita FOUC). Cambiar marca/tema = un atributo; todo re-resuelve `var()` sin recompilar.
```js
document.documentElement.dataset.brand='acme';
document.documentElement.dataset.theme=matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light';
```

## 3. Tailwind v4 (CSS-first, 2026)

v4 elimina `tailwind.config.js`: config en CSS vía `@theme` (engine Rust, builds 3.5×, incremental 8-100×). **Todo token en `@theme` genera utilities** y queda como CSS var.
```css
@import "tailwindcss";
@theme{
  --color-brand-500:oklch(.62 .19 256);  /* → bg-brand-500, text-brand-500, border-brand-500 */
  --spacing:.25rem; --radius-md:.5rem; --font-display:"Geist",sans-serif; --ease-out:cubic-bezier(0,0,.2,1);
}
```
**Truco clave para semantic tokens dinámicos (patrón shadcn):** usa `@theme inline` para mapear vars semánticas a utilities, pero deja los **valores** en `:root`/`.dark` para que el theming runtime funcione. Si pones el valor directo en `@theme`, Tailwind lo "hornea" y dark mode no cambia.
```css
:root{ --background:oklch(1 0 0); --foreground:oklch(.145 0 0) }
.dark{ --background:oklch(.145 0 0); --foreground:oklch(.985 0 0) }
@theme inline{ --color-background:var(--background); --color-foreground:var(--foreground); } /* "inline" = referencia, no copia */
```
**Dark toggle manual:** `@custom-variant dark (&:where([data-theme=dark], [data-theme=dark] *));`
**Cuándo Tailwind vs vanilla vars:** Tailwind para layout/spacing/estados rápidos; vanilla CSS vars para tokens consumidos solo en componentes. Híbrido ideal: tokens semánticos en CSS vars + utilities mapeadas con `@theme inline`.

## 4. shadcn/ui + Radix (estándar de facto)

shadcn define semantic tokens OKLCH en `:root`/`.dark`, convención **bg implícito + sufijo `-foreground` para el texto encima**:
```
--background/--foreground · --card/--card-foreground · --popover/--popover-foreground
--primary/--primary-foreground · --secondary · --muted/--muted-foreground · --accent/--accent-foreground
--destructive · --border · --input · --ring · --chart-1..5 · --sidebar(+ variantes) · --radius
```
Portar una marca: deja la **estructura**, cambia valores. `--primary=brand-9`, `--primary-foreground=brand-1/blanco`, `--ring=brand-8`, `--accent/--muted=brand-3`, `--border=brand-6`. Genera ambos modos con un theme generator OKLCH.

**Radix Colors — por qué 12 steps** (cada step un uso fijo → contraste/jerarquía sin adivinar):
| Step | Uso | Step | Uso |
|---|---|---|---|
| 1 | App background | 7 | Border interactivo |
| 2 | Subtle background | 8 | Border fuerte + focus ring |
| 3 | Component bg normal | 9 | Solid bg (accent) |
| 4 | Component bg hover | 10 | Solid bg hover |
| 5 | Component bg active/selected | 11 | Texto low-contrast |
| 6 | Border sutil (no interactivo) | 12 | Texto high-contrast |

Mapea: surface=1/2, hover items=4, border=6/7, ring=8, accent=9, accent-hover=10, fg-muted=11, fg=12. Variantes solid y **alpha** (translúcidas, ideales para overlays sobre cualquier fondo). Las 12 marcas Radix comparten índices → cambiar color = cambiar prefijo.

## 5. Estados de componente y completitud UX (pro vs amateur)

**Matriz obligatoria por componente interactivo:** `default · hover · focus-visible · active/pressed · disabled · loading · error/invalid · selected/checked` (+ `empty` para listas/tablas). Faltar `focus-visible` o `disabled` es la señal #1 de UI amateur.
```css
.btn{ background:var(--color-accent); color:var(--color-accent-fg); transition:background var(--duration-fast) var(--ease-out) }
.btn:hover{ background:var(--color-accent-hover) }
.btn:focus-visible{ outline:2px solid var(--color-ring); outline-offset:2px }   /* nunca outline:none sin reemplazo */
.btn:active{ transform:translateY(1px) }
.btn:disabled{ opacity:.5; cursor:not-allowed }
.btn[data-loading]{ color:transparent }  /* + spinner absoluto centrado */
```
**Forms UX:** validación inline **on-blur** (no on-keystroke); error ligado con `aria-describedby` + `aria-invalid="true"`; error usa `--color-danger` en borde+texto + **ícono** (no solo color → daltonismo). **Empty states:** ilustración/ícono + título + 1 línea + CTA. **Loading:** skeletons con `--color-surface-sunken` + shimmer para listas/cards; spinner solo acciones puntuales. **Focus management:** en modales, trap del focus, `Esc` cierra, devuelve foco al trigger. **Contraste:** texto normal ≥4.5:1, large/UI ≥3:1; OKLCH ayuda (≥0.2 de diferencia de L texto↔bg suele garantizar el ratio).

## 6. Pipeline de tooling (Figma → código)

Flujo 2026: **Tokens Studio / Figma Variables → DTCG JSON (en Git) → Style Dictionary → CSS vars / Tailwind `@theme` / JS / iOS / Android**, en CI. El **DTCG spec llegó a su 1ª versión estable (2025.10)** → JSON portable entre herramientas.
```json
{ "color": { "blue": { "500": { "$value":"oklch(0.62 0.19 256)", "$type":"color" } },
  "accent": { "$value":"{color.blue.500}", "$type":"color" } } }
```
```js
// build.js — Style Dictionary v4 + sd-transforms
import StyleDictionary from 'style-dictionary';
import { register } from '@tokens-studio/sd-transforms';
register(StyleDictionary);
export default {
  source:['tokens/**/*.json'], preprocessors:['tokens-studio'],
  platforms:{ css:{ transformGroup:'tokens-studio', buildPath:'src/styles/',
    files:[{ destination:'tokens.css', format:'css/variables', options:{ outputReferences:true } }] } }
};
```
`outputReferences:true` preserva los alias como `var()` (no aplana) → conserva la cascada semántica. **¿Cuándo vale la pena?** Solo con ≥2 plataformas o ≥2 marcas y diseñadores tocando tokens en Figma. Para un solo sitio Tailwind, escribir CSS vars a mano es más rápido.

## Anti-patterns (blacklist)

- **Componentes consumiendo primitives** (`bg-blue-500` en un botón) en vez de semantic tokens → re-theme imposible.
- **Valores semánticos dentro de `@theme` (no `@theme inline`)** → dark/brand no cambia en runtime.
- **`outline:none` en focus** sin reemplazo visible → fallo a11y crítico.
- **Solo color para error/estado** (sin ícono/texto) → invisible para daltónicos.
- **z-index mágicos** (`99999`) en vez de escala de tokens.
- **Escalas en HSL/sRGB** → pasos perceptualmente desiguales; usa OKLCH.
- **Theming con clases swapeadas en cada componente** (`dark:bg-x dark:text-y` por todos lados) en vez de semantic vars en `:root`/`.dark`.
- **Inflar Tier 3** (component tokens para todo) → deuda.
- **Olvidar estados** `disabled`/`loading`/`empty` → delator de UI amateur.
- **`#hex` sueltos** fuera del Tier 1 → tokens fantasma.
- **Style Dictionary para un sitio de una sola marca** → over-engineering; escribe las vars a mano.

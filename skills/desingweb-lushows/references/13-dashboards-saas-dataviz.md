# 13 — Dashboards, SaaS & data-viz (app UI, no marketing)

Frontera 2026 del diseño del **producto** (la app en sí), no la landing. Estética "Linear/Vercel" y más allá. **Léelo cuando construyas un dashboard, panel, SaaS, herramienta interna o cualquier UI con datos/tablas/charts** (FACTUM, dashboards de BIO-SETA/AGENTE STUDIO, etc.). Para marketing usa 10/11; esto es para la app.

---

## 1. El lenguaje visual moderno (el "Linear look" y su evolución)

La estética 2026 abandona las sombras pesadas de Material/Bootstrap y se construye sobre **hairline borders (1px) + elevación por luminosidad**, no por drop-shadows. En dark mode no se proyectan sombras: **se sube la capa aclarando la superficie**. Un único **accent color** marca selección/foco/CTA; el 95% de la UI es neutro. Densidad alta pero respirada.

- **Hairline borders** en vez de sombras. Borde = `1px solid` a ~6-10% de contraste. En dark, blanco translúcido `rgba(255,255,255,0.06)`–`0.10`.
- **Elevación = luminosidad**, no shadow. Cada capa que sube es ~3-5% más clara. Sombras solo en overlays flotantes (popover, command palette, dropdown), muy suaves.
- **Un solo accent**, generado en **OKLCH/LCH** (no HSL) — perceptualmente uniforme.
- **Radius system** coherente: `4px` (inputs/badges), `6-8px` (botones/cards), `10-12px` (paneles/modales), `9999px` (pills). Linear/Vercel viven en 6-8px. Radios >16px en chrome de app huelen a landing.
- **Glow sutil**, no gradient cards. Tarjetas con gradiente de marca everywhere = dated.

### Dark app tokens (copy-paste, estilo Radix Slate / Vercel Geist)
```css
/* SURFACES (elevación por luminosidad) */
--bg-app:#08090A; --bg-subtle:#0E0F11; --bg-surface:#131416; --bg-elevated:#18191B; --bg-hover:#1C1D1F; --bg-active:#232427;
/* BORDERS (hairline) */
--border-subtle:rgba(255,255,255,.06); --border:rgba(255,255,255,.09); --border-strong:rgba(255,255,255,.14);
/* TEXT */
--text-primary:#EDEDEF; --text-secondary:#A1A1AA; --text-tertiary:#71717A; --text-disabled:#52525B;
/* ACCENT (uno solo) */
--accent:#5E6AD2; --accent-hover:#6B77E0; --accent-fg:#FFFFFF; --accent-subtle:rgba(94,106,210,.14); --focus-ring:#5E6AD2;
/* SEMÁNTICOS */
--success:#30A46C; --warning:#F5A623; --danger:#E5484D; --info:#0091FF;
```
### Light app tokens (no es invertir — light app ≠ landing blanca)
```css
--bg-app:#FCFCFD; --bg-subtle:#F7F8F9; --bg-surface:#FFFFFF; --bg-hover:#F1F2F4; --bg-active:#E8EAED;
--border-subtle:#ECEDEF; --border:#E1E3E6; --border-strong:#CDD0D4;
--text-primary:#18191B; --text-secondary:#51555E; --text-tertiary:#80858E;
--accent:#5E6AD2; --accent-subtle:rgba(94,106,210,.10);
--success:#218358; --warning:#9A6700; --danger:#CE2C31; --info:#0072F5;
```
**Tipografía:** Inter o Geist Sans (UI). CLAVE 2026: **mono para TODO número/dato tabular** — Geist Mono / JetBrains Mono / IBM Plex Mono, o Inter con `font-variant-numeric: tabular-nums` (+ `font-feature-settings:"tnum" 1`). Base UI **13-14px** (apps densas, no 16px de marketing).

## 2. Layout systems (app shell)

- **App shell "inverted-L"** (Linear): sidebar colapsable **240-280px** + topbar fina (48-56px) + content. Sidebar: workspace switcher arriba, nav primaria, secciones colapsables, perfil/settings abajo.
- **Responsive collapse**: sidebar → icon-rail (56-64px) en tablet → off-canvas drawer en móvil. Breakpoints app: 768/1024/1280.
- **Multi-pane / split view**: patrón **"inbox" de 3 columnas** (lista | preview/detalle | panel contextual). Notion, Linear, Height, Superhuman. Cada pane scrollea independiente; navegable por teclado (`j`/`k`).
- **Keyboard-first**: atajos visibles (`G` luego `I` = Inbox; `C` crear; `/` buscar). Muestra keys como `<kbd>`.
- **Command palette (Cmd+K)**: Trigger `⌘K` → Input con fuzzy filter en vivo → Results agrupados (Recientes/Acciones/Navegación) con highlight de fila activa + flechas → Footer (`↑↓ navigate · ↵ select · esc close`). Soporta modos anidados. Librería: **`cmdk`** (lógica/a11y/filtrado, styling tuyo). Panel `max-width:640px`, top ~20vh (no centrado vertical exacto), backdrop blur sutil.
- **Empty states**: nunca vacío gris. Icono/ilustración mono + frase + **un CTA** + shortcut opcional.
- **Loading skeletons** (no spinners para layouts): bloques `--bg-hover` con **shimmer** suave (gradiente que barre, 1.2-1.5s). Spinner solo para acciones <1s. Skeleton con la forma real de las filas.

## 3. Data viz bien hecha

**Cuándo cada chart:** **line** = tendencia temporal · **area/stacked** = volumen acumulado · **bar/column** = categorías discretas · **horizontal bar** = rankings con labels largos · **sparkline** = micro-tendencia en KPI card (sin ejes) · **donut** SOLO 2-4 partes (nunca >5, nunca serie temporal) · **heatmap** = densidad/cohortes · **funnel** = conversión. Nunca pie de 8 tajadas ni 3D.

**Paletas (hex):**
```
/* CATEGORICAL (máx 8, colorblind-aware) */
#5E6AD2 #26B5CE #30A46C #F5A623 #E5484D #8E4EC6 #EC4899 #94A3B8
/* SEQUENTIAL (1 hue, claro→oscuro) */
#EAF2FF #C6DBFF #93BBFF #5E9CFF #2F7DF6 #1B5FD9 #0E45A8 #082E73
/* DIVERGING (punto medio neutro) */
#E5484D #F08F8F #F6C9C9 #E8EAED #BFE3CF #6CC79A #30A46C
```
Reglas: **consistencia cross-chart** (Producto A = mismo azul en todo el dashboard). No rojo+verde sin forma/patrón. Máx ~6-8 series antes de agrupar en "Other".

**KPI / stat card:** label (tertiary 12px) · **valor grande en mono/tabular-nums** (24-32px) · **delta** con flecha + color semántico (`+12.4%`/`−3.1%`) · sparkline opcional · período de comparación tertiary ("vs last 30d"). NO gradientes de marca en estas cards.

**Tablas que no apestan:** sticky header · **density toggle** (compact 32 / comfortable 40 / spacious 48px) · zebra OFF (mejor hairline divider) · **números a la derecha con tabular-nums** · columnas ordenables/redimensionables · **inline edit** (click→input, Enter confirma, Esc cancela) · checkbox + bulk action bar flotante · row hover sutil. >1000 filas: **virtualización** (`@tanstack/react-virtual` + `@tanstack/react-table`). Formato: `Intl.NumberFormat` con `notation:"compact"` (1.2K, 3.4M).

**Librerías + tradeoffs:** **Recharts v3** (default pragmático, SVG, ~150kB, hasta ~1-2k puntos) · **Tremor** (dashboards llave-en-mano estética shadcn, sobre Recharts, techo bajo) · **visx** (primitivas D3, control pixel-perfect, tú construyes) · **Nivo** (30+ tipos, pesado 500kB+) · **Observable Plot/D3** (bespoke total) · **Canvas** cuando >10k puntos (SVG colapsa por nodos DOM).

## 4. Micro-interacciones & polish premium

- **Timing**: micro-feedback **100-150ms** · tooltip/popover/dropdown **150-200ms** · modal/sheet **200-300ms**. Nunca >350ms en chrome de app. `prefers-reduced-motion` obligatorio.
- **Easing**: nada de `linear`. `ease-out` (`cubic-bezier(.16,1,.3,1)`) en aparición; `ease-in-out` entre estados.
- **Button press**: `:active{transform:scale(.97)}` con `transition:transform 120ms`.
- **Optimistic UI**: refleja la acción YA, reconcilia con server después; si falla, rollback + toast.
- **Toasts**: esquina (bottom-right/top-center), entrada 200-300ms, auto-dismiss 4-5s, stackeables, con "Undo". Librería: **`sonner`** o `react-hot-toast`.
- **Focus ring**: `box-shadow:0 0 0 2px var(--bg-app),0 0 0 4px var(--focus-ring)` (offset, no `outline` feo). Solo con teclado (`:focus-visible`).
- **View transitions**: cross-fade/slide sutil al cambiar pane/ruta (View Transitions API o Framer Motion `layout`).

## 5. Dark mode como default (para tools)

- **Dark-first de verdad**: diseña sobre la superficie oscura primero; light se deriva.
- **Nunca `#000` puro**: rompe la elevación y produce eye-strain. Canvas en `#08`–`#0E`.
- **Tokens semánticos**, no hex hardcodeados en componentes. Cambiar de modo = reasignar primitivos.
- **Elevación con overlays blancos** `rgba(255,255,255,.03→.08)` apilados. Sombra de overlay flotante: `0 8px 24px rgba(0,0,0,.4)`.
- **Contraste/a11y**: texto normal ≥4.5:1, grande/UI ≥3:1. Baja saturación de accents en dark. Jerarquía por opacidad 87/60/38%.
- **Warm vs cool**: cool/neutral-frío (`#08090A`) = developer-tool serio (Linear/Vercel/Supabase). Warm-gray = más humano (Notion). Define la voz. Tinta los grises hacia tu accent un par de grados para cohesión.

## 6. Freshness 2026 vs Dated — anti-slop dashboards

**Se ve 2026:** hairline borders + elevación por luz · un solo accent · neutros casi-negros · **mono/tabular-nums para números** · `⌘K` · multi-pane inbox · skeletons con shimmer · OKLCH theming · glass panel **sutil** (solo overlays) · empty states con personalidad · motion 150-250ms · iconografía stroke fino consistente (Lucide).

**Blacklist:**
- ❌ Plantillas admin **Bootstrap/AdminLTE**, sidebar azul fuerte, cards con `0 4px 6px`.
- ❌ **Material elevation pesada** (shadows 8-24px por card).
- ❌ **Gradient cards everywhere** / KPI con gradiente purple-pink.
- ❌ **Rainbow charts**: 12 colores saturados, pie 3D, leyenda de 10 tajadas.
- ❌ `#000` puro de fondo y `#FFF` puro para todo el texto en dark.
- ❌ Números en fuente proporcional que "bailan" (sin `tabular-nums`).
- ❌ Border-radius enorme (16-24px) en chrome de app; radios inconsistentes mezclados.
- ❌ Spinners para layouts completos.
- ❌ **Glassmorphism saturado** en cada card.
- ❌ Emojis como iconografía de producto; iconos de packs distintos mezclados.
- ❌ Demasiados accents compitiendo (color para decorar, no para significar).
- ❌ Animaciones >350ms, bounces, parallax en una app de trabajo.
- ❌ Densidad de marketing (16px base, mucho aire) en una tool que debe mostrar datos.

**Stack ref 2026:** Inter/Geist + Geist Mono · Radix Colors/Themes (OKLCH) o tokens propios · shadcn/ui + Tailwind · `cmdk` · `sonner` · Recharts/Tremor (visx para custom) · `@tanstack/table`+`react-virtual` · Lucide icons · Framer Motion/View Transitions.

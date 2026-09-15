# 48 — Design QA, testing, handoff & design ops

La capa de calidad/workflow que separa "amateur" de "studio-grade": verificar que lo construido coincide con la intención, es consistente, accesible, testeado y enviado sin deuda visual. **Léelo antes de publicar cualquier proyecto, o al montar un sistema/pipeline.** Pareja de 15 (tokens), 35 (estados), 16/40 (a11y/perf).

## 1. Design QA — la revisión pre-envío

Revisión sistemática del **sitio construido contra la intención de diseño** (no "se ve bien", una auditoría contra criterios). Se hace tras cerrar la feature y **antes** de marcarla "done"; idealmente por quien diseñó (o peer con ojo de diseño).
**Checklist (úsalo como gate literal):**
- **Spacing/layout:** paddings/margins según escala (4/8px o tokens); alineación óptica vs matemática; grid en todos los breakpoints; sin "magic numbers".
- **Typography:** tamaños/leading/tracking/weight según tokens; jerarquía; sin widows/orphans; truncation/wrapping con texto largo real.
- **Color/contraste:** tokens (no hex sueltos), estados hover/focus/active/disabled, dark mode, **contraste AA** (4.5:1 texto, 3:1 UI).
- **Estados de componente** (lo que más se omite): `default/hover/focus-visible/active/disabled/loading/error/selected` — todos.
- **Estados de página** (segundo olvido): `empty` (con CTA, no blanco), `loading` (skeletons), `error` (accionable, no stack trace), `no-results`, `offline`.
- **Contenido real, no lorem:** nombres largos, emails de 40 chars, otra moneda, 0 ítems, 10.000 ítems, otro idioma. El lorem oculta el 80% de los bugs de layout.
- **Responsive:** breakpoints reales (360/768/1024/1440) y **entre** ellos (resize continuo); safe areas iOS, teclado virtual, landscape.
- **Pixel vs intent:** no es pixel-perfect ciego — "¿captura la *intención*?". Si el dev mejoró el spacing, acéptalo; si rompió el ritmo, corrígelo.
- **Motion:** duración/easing del sistema, `prefers-reduced-motion`, sin jank.
- **Cross-browser/device:** Chrome, **Safari (el que más rompe)**, Firefox; iOS Safari + Android Chrome reales.
**Gate "is this actually done":** no se mergea si falta un estado, hay lorem en prod o falla un breakpoint. "Done" = pasa el checklist + screenshots de evidencia en el PR.

## 2. Visual regression testing

Detectar que un cambio de CSS rompió *otra* pantalla. Flujo: **baseline → diff → review → approve**.
**Self-hosted — Playwright `toHaveScreenshot()`** (gratis, en repo):
```ts
await expect(page).toHaveScreenshot('hero.png', { maxDiffPixelRatio: 0.01 });
```
Anti-flake: **correr en Docker** (mismo OS/fuentes que el baseline — el #1 causante de falsos positivos), viewport fijo, `waitForLoadState`, esperar fuentes, `animations:'disabled'`. Baselines en el repo (`--update-snapshots`). Multi-browser/viewport nativo. Coste $0, gestionas los PNG.
**Cloud — Chromatic** (con Storybook): captura cada story, snapshots en la nube (no contaminan el repo), cross-browser paralelo, y su mayor valor: **dashboard de review compartido** (diseñadores + devs aprueban). Alternativas: Percy, Lost Pixel (barato cloud-lite).
**Cuándo vale:** design systems / productos con muchas pantallas reutilizando componentes. Para una landing de una página, Playwright screenshots bastan. **Automatiza VRT sobre el component library, no sobre cada página de marketing.**

## 3. Storybook & documentación de componentes

Storybook 9 (con Vitest) = catálogo como **fuente de verdad viva** + suite de tests. **Una story por estado** (default/loading/error/empty/disabled/edge content) documenta y testea a la vez.
```ts
export const Loading: Story = { args: { state: 'loading' } };
export const WithLongName: Story = { args: { name: 'Maximiliano de la Concepción' } };
```
Addons que lo elevan: **`addon-vitest`** (corre las **play functions**/interaction tests), **`addon-a11y`** (axe-core por story, panel A11y con highlighting), **`@chromatic-com/storybook`** (VRT por story).
```ts
play: async ({ canvasElement }) => { const c = within(canvasElement);
  await userEvent.click(c.getByRole('button',{name:/enviar/i})); await expect(c.getByText(/gracias/i)).toBeInTheDocument(); }
```
**Cuándo vale:** reuso (design system, multi-marca, equipo). Para one-off es overhead. **Para una agencia multi-marca SÍ vale** (un Storybook por marca o uno con theming por tokens).

## 4. Figma → code handoff (Dev Mode 2026)

Gira sobre **Figma Dev Mode + MCP server** (beta GA 2026, seat Dev/Full): expone node tree, variants, constraints, **design tokens/variables** y assets al coding agent (Claude Code/Cursor/Copilot) — lee **datos estructurados y nombres de tokens reales**, no adivina de una imagen.
**Code Connect** (el eslabón que evita código basura): vincula un componente Figma a su implementación real, así Dev Mode/MCP muestran *tu* snippet (`<Button variant="primary">`) en vez de una aproximación. Sin él, la IA reinventa componentes existentes (el peor anti-patrón AI-to-code).
**Token pipeline (evita drift):** `Figma Variables → export (Tokens Studio/API) → tokens.json (W3C DTCG) → Style Dictionary → CSS vars/Tailwind/iOS/Android`. Una marca cambia su primario → un commit propaga a todo. Define **code syntax** en las variables Figma (`var(--color-bg-primary)`) → el MCP entrega ese nombre al LLM → cero hex sueltos.
**Qué necesita el dev:** tokens (no valores), estados, responsive/constraints, specs de motion, edge cases de contenido, link a la story de Storybook.

## 5. Testing automatizado de UI — la pirámide

```
  E2E (Playwright) — flujos críticos, pocos, lentos
  Component/Interaction (Storybook play + Vitest) — muchos, rápidos
  Unit (lógica/hooks/utils) — base ancha
```
Transversales: **a11y** y **performance** como gates en cada PR.
**Gate a11y (CI):** `@axe-core/playwright` (chequeo dirigido, falla ante violaciones WCAG) + **Lighthouse CI** (`lhci autorun`, auditoría ancha perf/a11y/SEO con assertions). axe = regresión fina; LHCI = gate ancho.
```ts
const r = await new AxeBuilder({ page }).analyze(); expect(r.violations).toEqual([]);
```
**Budget de perf en CI** (`lighthouserc.js`): `'largest-contentful-paint':['error',{maxNumericValue:2500}]`, `'cumulative-layout-shift':['error',{maxNumericValue:0.1}]`, `'categories:performance':['error',{minScore:0.9}]`. Build → preview → `lhci autorun` → falla el PR si excede.
**Qué automatizar vs manual:** automatiza regresión (visual, axe, perf budget, E2E críticos, interaction tests); mantén manual el **juicio de intención** (¿el spacing *siente* bien?, ¿el motion deleita?) — eso es Design QA humano.

## 6. Design ops & consistencia a escala (multi-marca)

- **Tokens como contrato:** una sola fuente (Figma Variables → Style Dictionary); cada marca = un set de tokens sobre la *misma* estructura de componentes. Cambiar marca = swap de token file, no reescribir CSS.
- **Versionado:** design system con semver + changelog (breaking change de token = major); componentes como paquete npm versionado.
- **Contribución:** RFC para nuevos componentes, ownership claro, un "design system team" que aprueba PRs; las marcas *consumen*, no parchean local.
- **IA en design ops 2026:** MCP + Code Connect generan código respetando el sistema; agentes corren el QA checklist + a11y como pre-commit; VRT con AI-diffing reduce falsos positivos por anti-aliasing.

### Launch checklist (gate final antes de prod)
Design QA pasado + screenshots en PR · todos los estados (empty/loading/error) probados · contenido real, cero lorem · responsive en devices reales + entre breakpoints · VRT verde / cambios visuales aprobados · axe sin violaciones + Lighthouse a11y ≥90 · Lighthouse perf en budget (LCP/CLS/TBT) · cross-browser (incl. Safari iOS) · meta/OG, favicon, 404, títulos por página · tokens sincronizados (sin drift Figma↔code) · `prefers-reduced-motion` + focus-visible OK.

## QA/handoff anti-patterns — blacklist
shipping sin QA (mergear porque "compila") · sin estados (solo happy path) · lorem en prod/contenido falso (oculta overflow/truncation) · drift Figma↔code (hex sueltos en vez de tokens) · IA-to-code sin Code Connect (reinventa componentes) · sin a11y test ("lo revisamos después" = nunca) · pixel-pushing ciego vs ignorar la intención (ambos extremos) · VRT flaky por OS mismatch (baseline en Mac, CI en Linux → ruido) · snapshots sin review compartido · probar solo los 3 breakpoints del Figma (romper entre ellos) · Safari/iOS de último o nunca.

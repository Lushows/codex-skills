# 281 · Testing frontend: Vitest, Testing-Library, Playwright

> El stack 2026 se decantó: **Vitest** (unit/componente), **Testing-Library** (queries semánticas),
> **Playwright** (e2e + visual). La pirámide invertida — muchos e2e, pocos unit — es la trampa: lenta,
> frágil, cara. Apunta a ~20-30 e2e en los flujos donde un fallo cuesta dinero, el resto abajo.

## Vitest desplazó a Jest (y por qué)
Comparte la config de Vite/SWC (sin Babel aparte), ESM nativo, arranque y ejecución mucho más rápidos.
API casi idéntica a Jest (`describe/it/expect/vi`). **Vitest 4** (dic 2025) marcó **Browser Mode estable**
y trajo visual regression integrado. [verificado: release Vitest 4]

```js
import { describe, it, expect, vi } from 'vitest'
describe('cartTotal', () => {
  it('aplica descuento', () => expect(cartTotal(items, 0.1)).toBe(90))
})
vi.mock('./api', () => ({ getOrder: vi.fn().mockResolvedValue({ id:1 }) }))
```

## Testing-Library: testea como el usuario, no la implementación
Query por **rol/label/texto**, nunca por clase o `data-testid` salvo último recurso. Si el test se rompe
al refactorizar sin cambiar comportamiento, está acoplado a la implementación.

```jsx
render(<LoginForm />)
await userEvent.type(screen.getByLabelText(/email/i), 'a@b.com')
await userEvent.click(screen.getByRole('button', { name: /entrar/i }))
expect(await screen.findByRole('alert')).toHaveTextContent(/inválido/) // findBy = espera async
```
Prioridad de queries: `getByRole` > `getByLabelText` > `getByText` > `getByTestId`. Esto fuerza accesibilidad de paso.

## jsdom vs Browser Mode
jsdom (default) es rápido pero **simula** el DOM: no hay layout real, CSS, ni eventos nativos fieles.
Browser Mode corre el componente en **Chromium/Firefox/WebKit reales** vía Playwright — para
componentes con foco, scroll, medición o CSS que importa.

```js
// vitest.config — browser mode estable en v4
test: { browser: { enabled:true, provider:'playwright', instances:[{ browser:'chromium' }] } }
```
Con `vitest-browser-react` el `render` trae locators con retry-ability (no más `waitFor` manual).

## Playwright: e2e en los flujos que cuestan plata
Auth, checkout/Stripe, async Server Components que Vitest no renderiza. Usa locators auto-waiting y
web-first assertions (`toBeVisible` reintenta hasta timeout) — adiós a sleeps frágiles.

```js
test('checkout', async ({ page }) => {
  await page.goto('/cart')
  await page.getByRole('button', { name:'Pagar' }).click()
  await expect(page.getByText('Pago confirmado')).toBeVisible()  // reintenta, no flakea
})
```
- `page.route()` para mockear red y aislar de backends.
- `storageState` reusa sesión autenticada entre tests (no re-loguear cada vez).
- Trace viewer (`--trace on`) = grabación paso a paso para debug de fallos en CI.

## Visual regression
Snapshots de pixel comparados contra baseline. `await expect(page).toHaveScreenshot()` en Playwright; o
el visual regression nativo de Vitest 4. Genera baselines en el **mismo OS que CI** (fuentes/antialias
difieren) → corre la baseline en Docker para evitar diffs fantasma.

| Capa | Herramienta | Qué prueba |
|---|---|---|
| Lógica pura/hooks | Vitest | reducers, utils, schemas Zod |
| Componente | Vitest + Testing-Library (jsdom o browser) | render, interacción, a11y |
| Flujo completo | Playwright | auth, checkout, navegación real |
| Visual | Playwright / Vitest 4 | regresiones de pixel |

## Gotchas
1. `getByTestId` por todos lados = tests que no detectan regresiones de UX reales; usa rol/label.
2. Olvidar `await` en `userEvent`/`findBy` → falsos verdes (assert antes de que pinte).
3. Snapshots visuales generados en local + CI con OS distinto = diffs eternos; baseline en Docker.
4. Mockear todo en e2e lo convierte en un test de integración disfrazado; mockea solo lo externo (pagos reales no).
5. Demasiados e2e = suite lenta y flaky; sube lógica a unit, deja e2e para los caminos de dinero.

Cruza con [[26-testing-a-fondo-python]] y [[350-browser-automation-playwright]].

# 33 — i18n, localización & RTL (multilingüe)

**i18n** = preparar el código para cualquier idioma/región (una vez); **l10n** = adaptar a un mercado concreto (por locale). **Léelo cuando el sitio deba soportar varios idiomas/países o escalar fuera de un solo locale.** Regla de oro: **el código nunca contiene texto, formatos ni supuestos culturales hardcodeados.** Un `locale` es BCP 47: `es-CO`, `es-MX`, `pt-BR`, `ar-SA`. Pareja de 15 (tokens) y 22 (SEO).

## 1. Arquitectura i18n

Todo string visible vive en catálogos, nunca en JSX/HTML. **Namespaces** (un archivo por dominio: `common`, `checkout`, `auth`) para **lazy-loading**.
```
/locales/es-CO/common.json  /locales/es-MX/common.json  /locales/en/common.json
```
Valores en **ICU MessageFormat** (plurales/género/interpolación sin concatenar):
```json
{ "cart_items": "{count, plural, =0 {Tu carrito está vacío} one {# producto} other {# productos}}",
  "greeting": "Hola, {name}" }
```
**Pluralización ICU (lo que más se rompe):** categorías CLDR `zero/one/two/few/many/other`. Español usa solo `one`/`other`; **árabe usa las seis**. **Nunca** `count===1 ? 'producto' : 'productos'` en código (revienta en árabe/ruso/polaco) — deja que ICU resuelva por locale.
**next-intl (recomendado 2026 Next.js App Router):** ~2KB, RSC nativo (traduce en servidor, cero JS al cliente), ICU de fábrica:
```ts
// i18n/request.ts
export default getRequestConfig(async ({locale}) => ({ messages:(await import(`../locales/${locale}/common.json`)).default }));
```
```tsx
const t = await getTranslations('checkout');  // server
const t = useTranslations('checkout');         // client ('use client')
<h1>{t('cart_items', {count: 3})}</h1>
```
SPAs no-Next → **i18next**/**react-intl**; Vue → **vue-i18n**.

## 2. La Intl API nativa (sin librería)

`Intl` resuelve formato locale-aware sin dependencias. Columna vertebral de toda l10n.
```js
// COP: coma decimal, punto de miles, $ antes, SIN decimales
new Intl.NumberFormat('es-CO',{style:'currency',currency:'COP',maximumFractionDigits:0}).format(1234567); // "$ 1.234.567"
new Intl.NumberFormat('es-MX',{style:'currency',currency:'MXN'}).format(1234.5);  // "$1,234.50" (MX invierte separadores)
new Intl.DateTimeFormat('es-CO',{dateStyle:'long'}).format(new Date());            // "3 de junio de 2026"
new Intl.RelativeTimeFormat('es',{numeric:'auto'}).format(-1,'day');               // "ayer"
new Intl.PluralRules('ar').select(3);                                              // "few"
['ñoño','nube','año'].sort(new Intl.Collator('es').compare);                       // orden con ñ/acentos
new Intl.ListFormat('es',{type:'conjunction'}).format(['rojo','verde','azul']);    // "rojo, verde y azul"
```
**Colombia:** decimal = coma, miles = punto, símbolo `$` antes, COP sin decimales (`maximumFractionDigits:0`). **Nunca asumas formato gringo.**

## 3. CSS para i18n y RTL: propiedades lógicas

Reemplaza **siempre** físicas por lógicas (se adaptan a LTR↔RTL sin reescribir CSS):

| Físico (evitar) | Lógico (usar) |
|---|---|
| `margin-left/right` | `margin-inline-start/end` |
| `padding-top/bottom` | `padding-block-start/end` |
| `left/right: 0` | `inset-inline-start/end` |
| `text-align: left` | `text-align: start` |
| `border-left` | `border-inline-start` |
| `width/height` | `inline-size/block-size` |

```css
.card{ margin-inline-start:1rem; padding-block:1rem; text-align:start; border-inline-start:3px solid }
:dir(rtl) .icon-arrow{ transform:scaleX(-1) }  /* flechas SÍ se voltean */
```
Activa RTL con `<html dir="rtl" lang="ar">`. **Se voltea:** layout, flechas, sliders/progress, breadcrumbs, comillas. **NO se voltea:** logos, números, relojes, iconos de marca, código, gráficos con eje temporal.

## 4. Layout & diseño para localización

**Expansión de texto — diséñala:** desde inglés, español **+20-30%**, alemán +35%, ruso +10%. "Save"(4)→"Guardar"(7)→"Speichern"(9). Reglas: nunca anchos fijos en botones/labels (usa `min-width`+padding flexible) · evita truncar con `...` (deja crecer: `flex-wrap`, altura auto) · `line-height` ≥1.5 (los acentos á/ñ y diacríticos necesitan aire) · **nunca texto dentro de imágenes** (no se traduce/indexa/es accesible — usa overlay HTML/CSS) · fuentes multi-script **Noto** (sin "tofu" □).
Varía también: dirección (calle→ciudad→país en LatAm), nombres (no asumas nombre+apellido), teléfono, posición de la moneda.

## 5. URL & SEO multilingüe

**Estrategia de URL** (mayor a menor señal SEO): ccTLD (`tienda.com.co`) > **subdirectorio** (`tienda.com/es-co/`, lo más práctico, hereda autoridad) > subdominio.
**hreflang recíproco** + **`x-default`**:
```html
<link rel="alternate" hreflang="es-co" href="https://tienda.com/es-co/">
<link rel="alternate" hreflang="es-mx" href="https://tienda.com/es-mx/">
<link rel="alternate" hreflang="x-default" href="https://tienda.com/">
<link rel="canonical" href="https://tienda.com/es-co/">
```
**Detección de locale:** `Accept-Language`/geo-IP solo como **sugerencia** (banner "¿Ir a la versión de México?"). **NUNCA auto-redirijas por IP** (rompe SEO — Googlebot rastrea desde EE.UU. — atrapa viajeros/VPN, frustra). La elección explícita manda y se persiste. **Switcher** lista cada idioma **en su propio idioma** ("Español", "العربية", "English"), **no banderas** (país ≠ idioma).

## 6. Español LatAm: variantes & workflow

| Concepto | es-CO | es-MX | es-AR | es-ES |
|---|---|---|---|---|
| Tratamiento | usted (formal default) | tú | **vos** ("tenés") | tú/vosotros |
| Moneda | $ COP (sin centavos) | $ MXN | $ ARS | € EUR |
| auto | carro | carro/coche | auto | coche |
| celular | celular | celular | celular | móvil |
| computador | computador | computadora | computadora | ordenador |
| Decimal/miles | 1.234,56 | 1,234.56 | 1.234,56 | 1.234,56 |

**Español neutro** (sin regionalismos, sin "vos", evita modismos) como base eficiente; luego **localiza overlays** por mercado clave. En Colombia el **"usted"** es la formalidad esperada en comercio.
**Workflow (TMS):** Crowdin/Lokalise/Phrase como repositorio central. Flujo: dev push de claves → **MT borrador** → **revisión humana** (post-edición) → sync. **Da contexto** (capturas, descripción, límite de caracteres); **nunca strings concatenados** (el orden de palabras cambia por idioma).
**Localiza más allá del texto:** medios de pago (PSE/Nequi/Bancolombia CO, OXXO/SPEI MX, Mercado Pago AR), formatos, imágenes culturales, festivos, impuestos (IVA 19% CO vs 16% MX).

## i18n anti-patterns — blacklist
strings hardcodeados · concatenar strings (`"Tienes "+n+" items"` — usa ICU) · pluralización con if/ternario (usa CLDR) · CSS físico (`margin-left`, `text-align:left`) · texto en imágenes · auto-redirect por IP/Accept-Language · anchos fijos en botones (texto +20-35%) · asumir formato número/fecha/moneda gringo (usa `Intl`) · hreflang no recíproco o sin `x-default` · banderas como selector de idioma · una sola variante de español para toda LatAm · asumir orden nombre+apellido.

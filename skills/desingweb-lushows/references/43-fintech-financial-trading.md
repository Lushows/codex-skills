# 43 — Fintech, financiero & trading UI/UX

Para UIs que manejan dinero: números densos, confianza crítica. **Léelo para facturación (FACTUM), trading (AGENTE TRADING), pagos o cualquier UI financiera.** Pareja de 13 (dashboards), 21 (forms), 29 (pricing), 31 (confianza).

## 1. Lenguaje visual fintech & confianza

La estética "dinero confiable" 2026 se construye con **restricción, precisión y aire**, no con sellos de candado. Regla Mercury: *"si quitas el logo, ¿se sabe quién lo construyó?"*. El slop genérico = clon de Stripe (fondo oscuro + gradiente índigo + Inter + mono cerca de números).
**Paletas reales:** Mercury (púrpura + dark, evita azul/verde a propósito) · Ramp (amarillo + azul profundo *domados con whitespace*) · Brex (naranja + negro) · Stripe (gradiente, funciona porque su público es dev — en consumo la estética "code-like" da ansiedad).
```css
/* "calm money" para trading (denso) */
--bg:#0B0D10; --surface:#14171C; --surface-2:#1C2128; --border:#262C36; --text:#E6E9EF; --text-dim:#9AA4B2;
--pos:#1FB877; --neg:#E5484D; --warn:#F5A623; --brand:#6E56CF;  /* acento, no gradiente */
```
Para FACTUM (light, documento de dinero): fondo `#FFFFFF`/`#FAFAFB`, texto `#0F1115`, un acento, mucho blanco. La seriedad la da **tipografía + alineación**, no adornos. Sans neutral (Inter/Geist) + `font-feature-settings:"tnum" 1` en TODO lo numérico.
**Señales de confianza que funcionan (no que asustan):** **transparencia > badges** (Wise muestra la comisión exacta antes de comprometer; Mercury explica límites FDIC en vez de ocultarlos) · regulación como lockup tipográfico sobrio ("Vigilado por la SFC", "PCI DSS"), no sticker brillante · **una sola cosa primero** (Ramp=ahorro, Wise=comisión — la ambigüedad mata la conversión).

## 2. UX de números & dinero (núcleo)

**Formato:** siempre `Intl.NumberFormat` con locale explícito (cachea el formatter, no lo crees por fila):
```js
new Intl.NumberFormat('es-CO',{style:'currency',currency:'COP',maximumFractionDigits:0}).format(1250000); // $ 1.250.000
new Intl.NumberFormat('en-US',{style:'currency',currency:'USD'}).format(1250.5);                          // $1,250.50
```
**Display:** **tabular-nums siempre** en tablas (sin esto las columnas "bailan") · montos **alineados a la derecha** · **negativos** con signo `−` delante del símbolo (`−$1.250.000`), o paréntesis en contabilidad; **color + signo + flecha, NUNCA solo color** (daltonismo) · **deltas** `▲ +2,4%` / `▼ −1,1%` (triple redundancia) con roll por dígito + pulso (estilo Coinbase RollingNumber) · **números grandes** abreviar solo en resúmenes (`$1,2 M`), **el total a pagar siempre completo** · precisión por moneda (COP=0, USD=2), no mezclar en una columna.
**Tabla financiera densa-pero-legible:** fila ~40-44px · monto a la derecha tnum · hover sutil · separadores 1px tenues (no grid pesado tipo Excel) · estado por chip con texto (`● Pagada`/`● Vencida`) · sticky header · agrupar por día con subtotal.
**Input de dinero:** entrada cruda al tipear, **formatea en `blur`** (formatear mientras escribe mueve el cursor) · símbolo como prefijo fijo · `inputmode="decimal"`.
**UI de factura (FACTUM):** (1) Header (emisor: nombre/NIT/dirección/logo + nº + fechas + estado); (2) Bill-to; (3) **tabla de líneas** (Descripción·Cantidad·Precio unit·Descuento·**IVA por línea**·Importe); (4) **Totales a la derecha** (Subtotal→Descuento→IVA 19%→**Total a pagar destacado**, la cifra más grande y de mayor contraste); (5) pie (método de pago, notas, numeración DIAN).

## 3. UI de trading / mercados

- **Charts:** **TradingView Lightweight Charts** (canvas, ligero, rápido; candlestick/OHLC/line/area/histogram; `series.update()` para mutar la última vela en tiempo real vía WebSocket). Para charts no-financieros del dashboard → Recharts/visx; D3 solo para custom extremo.
- **Ticker/precio en vivo:** verde/rojo + flecha + **pulso breve 150-250ms** en el dígito que cambia (Coinbase RollingNumber con `accessibilityLabel`). No parpadear toda la fila. Respeta `prefers-reduced-motion`.
- **Order book:** bids/asks a cada lado, mejor bid arriba/mejor ask abajo, spread al centro, barra de *depth* acumulada de fondo, tabular-nums.
- **Buy/Sell:** botones claramente diferenciados (verde compra/rojo venta, nunca ambiguos); muestra costo total + comisión **antes** de confirmar.
- **Portfolio/P&L:** posición, valor de mercado, costo base, **P&L absoluto y %** con triple redundancia; watchlist compacta con sparkline + último + delta.
- **"Markets dashboard":** chart dominante + order book + panel de orden + posiciones/P&L + watchlist; paneles redimensionables; densidad alta es esperada en trading (≠ §1 consumo).

## 4. Forms & flujos de dinero

- **Checkout:** Stripe Elements/Payment Element (validación en vivo, PCI delegado). **Conexión bancaria:** patrón **Plaid Link**; Plaid Transfer exige **authorization antes de crear** la transferencia. **KYC:** auto-poblar desde el banco (Identity) reduce fricción (cada campo extra cuesta drop-off).
- **"Review before you send":** pantalla obligatoria con **monto · destinatario · comisión · tasa · cuándo llega · total** antes de confirmar (modelo Wise).
- **Acción de alto riesgo:** *fricción intencional* (pausa visible ~1s + paso de confirmación señalan "se está verificando") · confirmación explícita (escribir el monto) · ventana de **undo** · **dual approval** para montos altos B2B · errores con causa + acción, nunca un código técnico crudo.

## 5. Dashboards financieros

Difieren del SaaS genérico por **precisión, densidad, tiempo real.** Una métrica protagonista primero (balance/ahorro). Balance/spend cards (cifra grande tnum + delta + sparkline). Cash-flow (barras in/out), breakdown por categoría (con valores, no solo color). Alerts de dinero (cobro fallido, factura vencida) con acción directa.
**FACTUM:** lista de facturas con estado por chip (`Borrador·Enviada·Pagada·Vencida·Anulada`) + total adeudado arriba · payment tracking (días vencidos, parcial/total) · dunning UI (secuencia visible/editable, tono escalable sin oscuridad) · reportes (IVA recaudado, ingresos por periodo, top clientes) exportables.

## 6. Confianza, seguridad, compliance + 2026

- **2FA/MFA:** TOTP/passkeys > SMS; flujo claro + códigos de respaldo, sin asustar. Settings de seguridad legibles (dispositivos/sesiones).
- **Compliance display** honesto ("Vigilado por X", cobertura, con límites). La regulación 2026 moldea el diseño desde el inicio.
- **Accesibilidad de números (crítico):** versión visual `aria-hidden="true"` + texto solo-lector con la cifra hablada ("un millón doscientos cincuenta mil pesos") — los lectores leen mal símbolos/separadores. Accessible colors para daltonismo; contraste WCAG AA en cifras.
- **Tendencias:** *calm money*/financial wellness · **AI co-pilot** (pronostica cash-flow, marca hábitos) con consentimiento y claridad · **embedded finance** (pagar dentro del SaaS donde ocurre la intención).

### Fintech anti-patterns (regulados — CFPB/FTC/UDAAP)
ocultar comisiones / drip pricing (revelar al final) · falsa urgencia sobre dinero · opciones preseleccionadas que cobran de más / cancelación enterrada · color solo para +/− · cifras que bailan sin tabular-nums · estética "code-like" (hashes/IDs) en UI de consumo · abreviar el **total a pagar** · mezclar precisiones de moneda en una columna · animaciones de precio agresivas que enmascaran el dato · ignorar `prefers-reduced-motion`.
**Checklist confianza:** comisión/total visible antes de confirmar · review en cada movimiento · tabular-nums + alineación derecha · +/− con signo+flecha+color · `Intl.NumberFormat` con locale + formatter cacheado · total destacado + IVA por línea · regulación honesta · números accesibles · confirmación/undo/dual-approval en alto riesgo · una métrica protagonista por pantalla.

# 29 — Pricing pages & monetización (que convierte éticamente)

Para SaaS (FACTUM/facturación) y e-commerce. **Léelo cuando diseñes una pricing page, paywall o flujo de upgrade.** Pareja de 17 (copy), 21 (checkout) y 13 (app UI).

## 1. Anatomía & layout

Estructura canónica (orden no negociable): (1) **headline orientado a valor** (no "Pricing": *"Factura sin fricción. Empieza gratis."*); (2) **subheadline que mata la objeción #1** ("Sin contratos. Cancela cuando quieras. Sin cargos sorpresa."); (3) **toggle Monthly/Annual** (anual por defecto + badge "Ahorra 2 meses"); (4) **cards de tiers** (3 col desktop, stack mobile); (5) **tabla comparativa** debajo; (6) **social proof** (logos, nº usuarios, testimonios); (7) **guarantee + FAQ**; (8) **CTA de cierre** repetido.
**3 tiers es el óptimo** (convierten ~1.4× vs 2; 4+ peor por choice overload). Más granularidad → add-ons, no más columnas.
**Card (good-better-best):** nombre + "para quién es" · precio grande + cadencia · **CTA por tier** (recomendado sólido, otros outline) · **5-7 features máx**, cada tier arranca con "Todo lo de [anterior], más:" · el central con badge **"Recomendado"** + elevación (borde de marca, escala 1.05, sombra) = **center-stage effect**.
**Mobile (58% del tráfico):** nunca scroll horizontal; stack vertical, recomendado primero/marcado, tabla colapsable por accordion.
**FAQ/guarantee al final** = último cierre. Responde objeciones reales ("¿cambio de plan?", "¿qué pasa si supero el límite?", "¿permanencia?", "¿factura electrónica DIAN?").

## 2. Psicología & estrategia (basada en evidencia)

- **Anchoring:** el primer número fija la referencia. Tier caro a la izquierda o Enterprise primero → Pro parece barato (+25-60% ticket).
- **Decoy/center-stage:** un tier intermedio "peor en relación precio/valor" empuja al premium (+35-50% del tier objetivo).
- **Charm pricing ($X9):** $29/$99 baja la percepción en self-serve/e-commerce; en Enterprise/B2B alto → números redondos (señal premium).
- **Annual framing:** muestra el **mensual equivalente del plan anual** como número grande ("$24/mes"), mensual real secundario. Descuento 10-20% comunicado como "2 meses gratis" > "-17%".
- **Value metric (la decisión más importante):** la métrica que escala con el valor percibido. Para FACTUM: **nº de facturas/documentos al mes** o empresas/NITs, NO per-seat (un contador maneja varias empresas).
- **Choice overload:** 3 planes, 5-7 features, un recomendado.
- **Enterprise "Contact sales":** ancla alta + captura deals grandes ("Hablar con ventas" en vez de precio).

## 3. Diseño de planes/tiers

- **Nombra por cliente, no por tamaño:** FACTUM → **"Independiente / Negocio / Empresa"** ("ese soy yo"), no "Basic/Pro" genérico.
- **Qué gatear vs incluir:** incluye SIEMPRE el **core job** en el plan más bajo (emitir factura electrónica válida — gatearlo mata confianza). Gatea por **volumen** (facturas/mes), **funciones de poder** (multi-empresa, API, reportes, roles, integraciones) y **soporte**.
- **Upgrade path obvio:** "Todo lo de X, más:" + límites visibles ("Hasta 50 facturas/mes").
- **Add-ons** para no inflar tiers (paquetes de facturas extra, usuarios, soporte premium).
- **Tendencia 2026:** per-seat puro cayó 21%→15%; **híbrido (base + usage/overage) subió 27%→41%**. Para FACTUM: **base mensual + bolsa de documentos con overage** = lo más alineado al valor.

## 4. Paywall & upgrade UX in-product

- **Soft paywall > hard** (deja ver/probar con restricción ligera; hard solo para acciones que cuestan dinero real).
- **Prompts contextuales en el momento de necesidad** (no timer genérico): "Llegaste a 45/50 facturas. Sube a Negocio para facturar sin límite."
- **Quota/usage UX:** consumo siempre visible (barra "38/50 facturas"), avisa al 80% y 100%, upgrade inline ahí.
- **Upgrade modal:** una pantalla, beneficio concreto del destino, precio claro, CTA único, "cerrar" visible.
- **Trial expiration:** avisa día -3/-1, resume el valor obtenido, pago de 1 clic. **Reverse trial** (premium gratis N días → eligen) convierte mejor que freemium puro (2-5%; trial-to-paid 18-40%).
- **Downgrade/cancel ético:** cancelar **tan fácil como suscribirse** (online si se suscribió online). OK: pausa, downgrade a free, descuento de retención **una vez** honesto. Prohibido: obligar a llamar, esconder el botón, multi-pasos para frustrar.

## 5. Checkout/suscripción SaaS

- **Flujo signup→paid de mínima fricción:** plan preseleccionado en el upgrade, sin re-pedir datos.
- **Stripe Checkout** (hosted, PCI-safe) + **Customer Portal** (cliente gestiona plan/pago/cancelación). No construyas formularios de tarjeta propios.
- **Proration automática** (Stripe la calcula); webhooks con **verificación de firma** + idempotencia + async.
- **Tax/VAT:** Stripe Tax; en Colombia, IVA + factura electrónica DIAN del propio cobro.
- **LatAm payment methods (crítico CO):** además de tarjeta → **PSE** (32% de pagos online), **Nequi**, **Daviplata**, considera **Mercado Pago**. Ofrecer PSE + Nequi sube conversión vs solo tarjeta internacional. Gateways: PayU Latam, Mercado Pago, agregadores (Dodo/Rebill) para suscripción.

## 6. Confianza & conversión

- **Reductores de ansiedad cerca del CTA:** "Sin tarjeta requerida", "Cancela cuando quieras", "Garantía 30 días", "Sin permanencia".
- **Transparencia > "Contáctanos" para todo:** precios reales en self-serve; "Contact sales" solo Enterprise.
- **Social proof:** logos, nº de empresas, testimonios con cara ("+X.000 empresas facturan con FACTUM").
- **ROI/value calculator** cuando el ahorro es cuantificable ("¿cuántas facturas al mes?" → horas/dinero ahorrado).
- **Dunning (recuperar pagos fallidos):** Stripe Smart Retries (~57% recuperado) + secuencia de 4 emails (Día 0/3/7/12 → +35-45%). Retención legítima, no dark pattern.
**Tendencias 2026:** usage/outcome-based en alza (Gartner: ≥40% del gasto SaaS migra a usage/agent/outcome para 2030); AI pricing (créditos/por tarea/outcome); pricing pages mobile-first.

## Pricing anti-patterns / dark patterns — blacklist
| Anti-pattern | Por qué |
|---|---|
| Hard-to-cancel (obligar a llamar) | FTC multó a Amazon $2.5B (2025). Cancelar = tan fácil como suscribirse |
| Forced annual (esconder mensual) | Manipula, genera churn de marca |
| Hidden fees / cargos sorpresa | Mata confianza, viola normativa |
| Drip pricing (precio real solo al final) | Sancionado FTC; muestra total desde el inicio |
| Opt-out preseleccionado (add-on marcado) | Consentimiento no genuino, ilegal CPRA/FTC |
| Confirmshaming ("No, no quiero ahorrar") | Manipulación emocional |
| "Cerrar" oculto en modales de upgrade | Coerción visual |
| Roach motel (fácil entrar, imposible salir) | Núcleo de dark patterns regulados |
| Fake urgency/countdowns falsos | Engaño, erosiona credibilidad |

**Regla ética:** retén con **valor y honestidad** (pausa, downgrade, descuento ofrecido una vez, dunning), nunca con **fricción diseñada** para atrapar.

## Quick-apply FACTUM
3 tiers **Independiente/Negocio/Empresa** (Negocio recomendado, center-stage) · value metric **base + facturas/mes con overage** (híbrido) · toggle anual por defecto + charm pricing · quota visible + soft paywall + prompt al 80/100% · Stripe Checkout + Portal + Tax + **PSE/Nequi** · cierre con sin-tarjeta/cancela-cuando-quieras/garantía/FAQ DIAN/logos · dunning Smart Retries + 4 emails · cancelación 1-clic en el portal.

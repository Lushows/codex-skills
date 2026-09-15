# 64 — ROAS real vs ROAS de plataforma: la verdad financiera

El número más peligroso del Ads Manager es el ROAS, porque parece plata y no lo es. Este módulo te da el sistema para saber cuánto ganas DE VERDAD con la pauta, decidir tu ROAS objetivo desde el margen (no desde un gurú), y triangular plataforma vs backend vs banco cada semana. Léelo antes de celebrar o despedir una campaña por su ROAS. Actualizado jun-2026. El modelado fino de unit economics (margen, LTV, breakeven, viabilidad) es de **economist_lushows** — aquí te doy lo operativo para decidir pauta; rutea ahí el cálculo de negocio.

## Los cuatro números, definidos

- **ROAS de plataforma** = ventas que Meta SE ATRIBUYE ÷ gasto. Históricamente inflado por view-through, atribución 7d-click y **modeled conversions** (ventas que Meta estima estadísticamente cuando no pudo rastrear, p.ej. usuarios sin tracking). **Novedad 2026:** Meta quitó las ventanas view-through del API (12-ene-2026) → esa fuente de inflación bajó mucho; y si activas **atribución incremental**, el ROAS reporta SOLO lo causado (menos, más honesto). Aun así no es tu caja: sigue siendo la estimación de Meta de SU contribución, no la plata que entró al banco.
- **MER** (Marketing Efficiency Ratio) = ventas TOTALES del negocio ÷ gasto publicitario TOTAL. Todas las ventas (web, WhatsApp, recompras, orgánicas) sobre todo el gasto pago (Meta + Google + TikTok). No depende de atribución: es el número que no miente. El MER por canal se reparte en cada skill hermana; el MER total los suma.
- **nCAC** = gasto ÷ clientes NUEVOS adquiridos (excluye recompras). Te dice cuánto pagas por crecer de verdad.
- **Profit por pedido** = AOV − costo de producto − envío/empaque − comisión pasarela − CPA. Si da negativo y no hay recompra fuerte, estás comprando ventas con plata de tu bolsillo.

## ROAS objetivo: se calcula desde el margen, paso a paso

**Breakeven ROAS = 1 ÷ margen bruto %**. Ejemplo completo:
1. Vendes un combo a COP $150.000.
2. Costo de producto: $45.000. Envío + empaque: $15.000. Comisión pasarela ~3%: $4.500.
3. Margen bruto = 150.000 − 64.500 = $85.500 → 57% del precio.
4. Breakeven ROAS = 1 ÷ 0.57 = **1.75**. Debajo de 1.75 pierdes plata en el primer pedido; arriba, ganas.
5. ROAS objetivo operativo = breakeven × colchón (1.3–1.5 para cubrir fijos y la inflación de atribución que queda) ≈ **2.3–2.6**.
6. CPA máximo equivalente = margen bruto por pedido = $85.500 (breakeven) → objetivo operativo ~$55.000–65.000.

Si no conoces tu margen bruto: PARA. No pautes más hasta calcularlo (economist_lushows, unit economics). "ROAS 3 porque lo dijo un video" puede ser quiebra para un margen de 25% y dejar plata en la mesa para uno de 75%. Ojo en Colombia: si vendes contraentrega (COD), descuenta el **% de rechazo** (5–15%) del cálculo — una "venta" que el cliente rechaza en la puerta es costo de envío puro, no margen.

## Cuándo sirve cada número

| Pregunta | Número correcto |
|---|---|
| ¿Qué campaña/ad funciona mejor DENTRO del mismo setup? | ROAS de plataforma (sesgo parejo entre ellas → comparable) |
| ¿La pauta es rentable para el negocio? | MER + profit por pedido |
| ¿Puedo pagar por crecer? | nCAC vs margen del primer pedido (o LTV si hay recompra) |
| ¿Cuánto subo/bajo presupuesto este mes? | MER tendencial (¿se sostiene al subir gasto? ver 65) |
| ¿Meta o Google traen mejor cliente? | nCAC y MER por canal (rutea a google_ads_lushows / tiktok_ads_lushows) |

Regla: **ROAS de plataforma para decisiones DENTRO de Meta; MER para decisiones SOBRE Meta.**

## Triangulación semanal (15 minutos, mismo día cada semana)

Tres fuentes, una fila por semana:
1. **Backend**: pedidos y ventas reales — tu tienda (Shopify/Woo) o, si vendes por WhatsApp, tu CRM/etiquetas de chat: el backend ES tus etiquetas de pedidos cerrados (ver 53). Cuenta también clientes nuevos vs recompra.
2. **Ads Manager**: gasto y ventas atribuidas (export, ver 63).
3. **Banco/pasarela**: la plata que efectivamente entró (detecta contraentrega fallida, devoluciones, chargebacks).

### Plantilla de hoja semanal

| Semana | Gasto Meta (COP) | Ventas plataforma | Ventas reales (backend) | MER | Clientes nuevos | nCAC | Factor inflación | Decisión / nota |
|---|---|---|---|---|---|---|---|---|
| 1–7 jun | 1.400.000 | 5.600.000 (ROAS 4.0) | 3.900.000 | 2.79 | 26 | 53.846 | 1.44× | Mantener; plataforma infla ~44% |
| 8–14 jun | 2.000.000 | 7.400.000 (ROAS 3.7) | 5.200.000 | 2.60 | 33 | 60.606 | 1.42× | Subí gasto 43%, MER cayó solo 7% → escalable (ver 65, 72) |

**Factor de inflación = ventas plataforma ÷ ventas reales** (típicamente 1.2–1.8×; varía por mezcla de retargeting y canal). Con 4–6 semanas ya conoces TU factor y puedes traducir mentalmente el Ads Manager: "ROAS 4 en pantalla ≈ MER 2.8 real". Esa traducción es tu superpoder de reporting (ver 67).

### Cómo calcular el MER en 3 cuentas
1. Suma TODAS las ventas reales del periodo (backend + banco), de todos los canales y recompras incluidas.
2. Suma TODO el gasto pago del periodo (Meta + Google + TikTok + lo que sea).
3. MER = (1) ÷ (2). Si MER < breakeven ROAS del negocio, estás perdiendo plata aunque el Ads Manager muestre ROAS 4. Si MER ≥ objetivo y se sostiene al escalar, tienes luz verde para subir presupuesto (ver 65).

## Discrepancias: qué es normal y qué es alarma

- **Plataforma 20–60% más que el backend**: normal (modeled, recompras atribuidas, view-through residual).
- **Plataforma MENOS que las ventas reales del canal**: normal si vendes por WhatsApp sin CAPI de cierre — Meta no ve la venta del chat (fix: evento `business_messaging`/Purchase por CAPI con `ctwa_clid` al cerrar, o vivir con el CRM como verdad, ver 53, 62).
- **Plataforma 2–3× el backend sostenido**: ALARMA — deduplicación rota (ver 62) o retargeting auto-atribuyéndose todo (ver 65).
- **GA4 reporta 20–50% MENOS que Meta**: normal y estructural (last-click vs 7d-click), no es error de nadie (ver 66).

## Ejemplo resuelto: del ROAS lindo a la decisión real

Marca de café, semana: gasto $1.000.000, Ads Manager dice ROAS 4.5 ($4.5M). Backend real: $2.9M de ventas, de las cuales $400.000 fueron recompras (no atribuibles a la pauta nueva) y $150.000 fueron COD rechazado. Cálculo honesto:
- Ventas reales netas = 2.9M − 0.15M (COD fallido) = $2.75M → MER = 2.75.
- Ventas de clientes NUEVOS = 2.75M − 0.4M = $2.35M, 22 clientes nuevos → nCAC = $45.454.
- Margen bruto 55% → breakeven ROAS 1.82, objetivo 2.5. MER 2.75 > 2.5 → **rentable, escalable**.
Reportas MER 2.75 y nCAC $45k, no "ROAS 4.5". El dueño confía porque el número cuadra con su banco (ver 67).

## Errores comunes — blacklist
- Reportar(te) el ROAS de plataforma como ganancia ("ROAS 4 = gano 4 pesos por peso") sin restar costo de producto ni inflación.
- Fijar ROAS objetivo sin conocer el margen bruto (economist_lushows).
- Comparar el ROAS de una campaña de retargeting contra una de prospección y "concluir" que retargeting es mejor (se auto-atribuye, ver 65).
- No registrar la hoja semanal: sin serie histórica no hay factor de inflación ni tendencia, solo ansiedad diaria.
- Olvidar devoluciones y contraentregas rechazadas (en Colombia el COD fallido puede comerse 5–15% de "ventas").
- Mezclar recompras en el CAC: para saber si creces, el costo se mide contra clientes NUEVOS (nCAC).
- Asustarse porque la atribución incremental bajó el ROAS: dejó de contar lo que no causaste, no perdiste ventas (ver 65).

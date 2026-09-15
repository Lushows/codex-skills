# 101 — Playbook: e-commerce / tienda online

Sirve para entender la economía REAL de vender por internet (no el sueño del "tráfico gratis"): qué deja cada venta después de envío, devoluciones y publicidad, y por qué la mayoría de las tiendas mueren no por falta de ventas sino por vender por debajo de su costo de adquisición. Si vas a montar una tienda online, este módulo es tu chequeo de viabilidad antes de invertir.

> Aviso de país: comisiones de pasarela de pago, costo de envío, IVA/impuestos a la venta y reglas de protección al consumidor (derecho de retracto / devoluciones) cambian por país y ciudad. Aquí explico el MÉTODO y doy ejemplos ilustrativos. Pregúntame tu país/ciudad y conseguimos las cifras reales (ver 21).

---

## La verdad incómoda del e-commerce

El e-commerce NO es "pongo una tienda y vendo". Es un negocio de **márgenes finos + adquisición pagada**. La plata no se gana en la venta: se gana en la **segunda, tercera y cuarta compra** del mismo cliente (recompra). Si tu producto no se recompra y dependes 100% de anuncios, estás en una carrera donde Meta/Google se quedan con tu margen.

Regla mental: **una tienda online es rentable cuando el margen de contribución por venta cubre el costo de traer a ese cliente Y deja sobra para el negocio.** Todo lo demás es decoración.

---

## Los 4 modelos (elige con los ojos abiertos)

| Modelo | Capital de arranque (orientativo) | Margen bruto típico | Riesgo principal |
|---|---|---|---|
| **Marca propia** (tú fabricas/maquilas y vendes) | Medio-alto (inventario + branding) | 50–75% | Inventario muerto, validar antes de producir |
| **Retail online** (compras a mayorista y revendes) | Medio (inventario) | 20–40% | Margen finito, guerra de precio |
| **Dropshipping** (el proveedor despacha, tú no tocas stock) | Bajo (solo ads + tienda) | 15–30% real tras ads | Sin control de calidad/tiempos; márgenes que no cubren el CAC |
| **Marketplace** (vendes dentro de Amazon/MercadoLibre/Falabella) | Bajo-medio | -comisión 10–20% | Dependes de la plataforma; te clonan; te suben comisión |

- **Marca propia** es el único que construye un activo (la marca y la base de clientes son tuyas). Es el más difícil y el más defendible.
- **Dropshipping** suena fácil pero el 90% fracasa: márgenes flacos que no aguantan el CAC + cero diferenciación. Sirve para *testear demanda* barato, no como negocio final.
- **Marketplace** da tráfico gratis pero alquilas la relación con el cliente. Úsalo como canal, no como casa.

---

## El stack mínimo (qué necesitas para arrancar)

1. **Tienda**: plataforma lista (Shopify, Tiendanube, WooCommerce, o incluso vender por WhatsApp/Instagram al inicio).
2. **Pagos**: pasarela local (cobra **comisión por transacción**, típicamente ~2–4% + fijo — verifica tu país). En LatAm suma pago contra entrega, PSE/Nequi/transferencia.
3. **Envíos**: transportadora/courier. Decide quién paga el envío (tú, el cliente, o "gratis" disfrazado en el precio).
4. **Medición**: píxel de Meta/Google + analítica básica para saber tu conversión y tu ROAS real.

Arranque mínimo viable: **NO montes la tienda perfecta**. Vende primero por Instagram/WhatsApp con 1–3 productos y link de pago. Si vendes ahí, ya validaste demanda; entonces inviertes en tienda (ver 52, 57).

---

## Métricas que de verdad importan (KPIs)

| KPI | Qué es | Rango orientativo |
|---|---|---|
| **Conversión** | % de visitas que compran | **1–3%** es lo normal en e-commerce. <1% = problema; >4% = muy bueno |
| **AOV** (ticket promedio) | Valor promedio de cada pedido | Súbelo con combos, envío gratis desde X, upsell |
| **CAC** | Cuánto cuesta traer 1 cliente que compra | Debe ser **menor** que tu margen de contribución |
| **ROAS** | Ingresos / gasto en ads. ROAS 3 = $3 vendidos por $1 de ads | Necesitas ROAS > tu punto de equilibrio (ver cálculo abajo) |
| **Tasa de recompra** | % de clientes que vuelven a comprar | El verdadero motor de la rentabilidad (ver 52, LTV) |

**Define para no técnicos:**
- **AOV** = Average Order Value = cuánto gasta en promedio quien compra.
- **CAC** = Customer Acquisition Cost = gasto en ads ÷ clientes nuevos conseguidos con ese gasto.
- **ROAS** = Return On Ad Spend = ventas generadas ÷ plata gastada en anuncios.
- **Margen de contribución** = lo que queda de una venta después de TODOS los costos variables (producto, envío, comisión, empaque), antes de gastos fijos.

---

## Estructura de costos de UNA venta (orden mental)

```
Precio de venta
 − Costo del producto (COGS)
 − Comisión de pasarela de pago
 − Costo de envío (la parte que pagas tú)
 − Empaque
 − Provisión por devoluciones/cambios
 = MARGEN DE CONTRIBUCIÓN  ← de aquí sale el CAC y la utilidad
 − CAC (publicidad por cliente)
 = Utilidad por venta (antes de fijos)
```

Si ese número de abajo es negativo, **cada venta te hace perder plata**. Más ventas = más pérdida. Esto mata tiendas todos los días.

---

## Ejemplo numérico — unit economics de una venta (cifras ILUSTRATIVAS)

Producto: una crema. Precio de venta **$80.000** (moneda local ilustrativa).

| Concepto | Valor | Nota |
|---|---|---|
| Precio de venta | $80.000 | |
| − Costo del producto (COGS) | −$28.000 | 35% del precio |
| − Comisión pasarela (3,5%) | −$2.800 | verifica tu país |
| − Envío que asumo yo | −$8.000 | ofrezco "envío gratis" |
| − Empaque | −$2.000 | |
| − Provisión devoluciones (5% × costo) | −$2.000 | 1 de cada 20 vuelve |
| **= Margen de contribución** | **$37.200** | 46,5% del precio |

Ahora el CAC. Supón conversión **2%** y que un clic de anuncio cuesta **$700**:
- Para 1 venta necesito 50 visitas (1 ÷ 2%). 50 clics × $700 = **$35.000 de CAC**.

**Utilidad por venta = $37.200 − $35.000 = $2.200.** Apenas sobrevives, y aún NO pagaste plataforma, tu tiempo ni impuestos.

**Aquí está la lección:** con esos números el negocio NO funciona con una sola compra. Funciona si el cliente **recompra**. Si la mitad recompra una vez (sin volver a pagar CAC), el segundo pedido deja ~$37.200 limpios → tu LTV sube y recién ahí hay negocio (ver 52 para LTV/CAC).

**Palancas para arreglar este ejemplo** (cualquiera de estas lo salva):
- Subir AOV a $120.000 con combo → margen de contribución sube y absorbe el CAC.
- Subir conversión de 2% → 3% (mejor página, fotos, reseñas) → CAC baja de $35.000 a ~$23.000.
- Bajar costo del clic con mejor segmentación/creatividades (ver 57).
- Cobrar el envío o subir el umbral de "envío gratis".

---

## ROAS de equilibrio (cómo saber tu mínimo)

Tu **ROAS de equilibrio** = Precio ÷ Margen de contribución.
En el ejemplo: 80.000 ÷ 37.200 = **2,15**. Significa que por debajo de ROAS 2,15 pierdes plata en cada venta pagada. Apunta a ROAS cómodamente por encima de eso (3+) para que sobre para fijos y utilidad. Calcula ESTE número antes de prender un solo anuncio.

---

## Cómo arrancar mínimo viable (orden real)

1. Elige 1–3 productos con margen ≥ 40–50% y potencial de recompra.
2. Vende por Instagram/WhatsApp + link de pago. Cero inversión en web (ver 52).
3. Mide conversión real y tu CAC con un presupuesto chico de ads (ver 57).
4. Calcula tus unit economics con datos REALES (no estimados).
5. Solo si los números cierran → monta tienda, automatiza, escala el gasto.
6. Desde el día 1 captura datos del cliente (correo/WhatsApp) para recompra (ver 52 y 89).

---

## Trampas que matan a este negocio

- **Vender por debajo del CAC.** El error #1. Escalas ads y escalas la pérdida. Calcula el unit economics ANTES.
- **Depender 100% de ads.** Si todo tu tráfico es pagado y subes a Meta/Google de proveedor único, no tienes negocio: tienes una manguera que ellos pueden encarecer cuando quieran. Construye correo, WhatsApp, recompra, orgánico.
- **"Envío gratis" sin meterlo en el precio.** El envío no es gratis; alguien lo paga. Si no lo cubres, te comes el margen.
- **Ignorar devoluciones.** En ropa/calzado pueden ser 20–40%. Sin provisión, tu margen real es ficción.
- **Inventario muerto.** Producir mucho antes de validar. Compra/produce poco, vende, repón.
- **Confundir ROAS con utilidad.** ROAS alto con margen bajo sigue dando pérdida. Mira margen de contribución, no solo ROAS.
- **No medir conversión.** Si no sabes tu %, no puedes calcular CAC y vuelas a ciegas.

---

## Errores comunes

- Creer que "tráfico = ventas". Tráfico sin conversión es gasto.
- Bajar el precio para vender más → matas el margen que paga el CAC.
- Gastar en la web bonita antes de validar que alguien compra.
- Olvidar impuestos a la venta y comisiones en el cálculo de margen (verifica tu país).
- Medir éxito por ventas brutas en vez de utilidad por venta.

---

## Siguiente paso típico

Arma la tabla de unit economics de TU producto con cifras reales (precio, COGS, comisión, envío, devoluciones) y calcula tu margen de contribución y tu ROAS de equilibrio. Si la utilidad por venta es negativa o apenas positiva, antes de invertir en ads sube AOV o conversión, y diseña la recompra (ver 52 y 89). Dime tu país y producto y lo calculamos juntos.

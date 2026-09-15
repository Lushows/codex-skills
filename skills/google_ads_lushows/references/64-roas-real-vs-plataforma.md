# 64 — ROAS real vs plataforma

Lee este módulo cuando Google Ads te muestra un ROAS de 6 pero la cuenta del banco no lo siente, cuando tu cliente dice "el panel dice que ganamos pero no veo la plata", o cuando vas a tomar una decisión de escalar/cortar basándote en el ROAS que reporta la plataforma. **El ROAS de Google Ads casi siempre está inflado.** No porque Google mienta, sino porque mide lo que puede ver y atribuye generosamente. Aquí aprendes a triangular y a saber cuánto ganaste **de verdad**.

Aviso de ruteo: este módulo te enseña a **leer** las cifras. Si el problema es de fondo —"¿este negocio aguanta pagar pauta?", "¿cuál es mi CAC objetivo?", "¿cuál es mi margen real?", "¿cuál es mi MER meta?"— eso es modelo de negocio y va a **`economist_lushows`**. Aquí asumimos que ya sabes tu margen y tu CAC máximo, y te enseñamos a contrastarlos con lo que el panel afirma.

## Por qué el ROAS de plataforma infla

Google Ads cuenta una venta como suya cuando puede atribuírsela. Eso lo lleva a sobrecontar por varias razones acumuladas:

| Razón | Qué pasa |
|---|---|
| **Atribución generosa** | Si alguien hizo clic y compró 30 días después por otra vía, Ads se lleva el crédito (ver 16) |
| **Conversiones que ya iban a pasar** | El cliente de marca te iba a comprar igual; el anuncio no creó la venta (ver 65, incrementalidad) |
| **Doble conteo** | Conversiones mal deduplicadas (ver 62) inflan el numerador |
| **Modelado** | Parte de las conversiones son **estimadas** (Consent Mode, conversiones modeladas), no reales 1:1 |
| **Solo ve su parte** | No descuenta devoluciones, fraude, ni costos del producto |
| **Atribución data-driven (default 2026)** | Reparte crédito fraccional entre touchpoints de forma opaca; útil para optimizar, peligrosa si la lees como caja |

Resultado típico: el ROAS de plataforma puede estar **20–50% por encima** del ROAS incremental real, sobre todo en campañas de **marca** y **remarketing** (ver 65). En 2026, con más modelado y data-driven por defecto, esa brecha tiende a ser mayor, no menor.

## ROAS vs margen: por qué un ROAS "bueno" puede perder plata

El error conceptual que arruina negocios: confundir ROAS con ganancia. El ROAS no descuenta el costo del producto. Fórmula del **break-even ROAS** (el mínimo para no perder):

```
Break-even ROAS = 1 ÷ margen de contribución

Margen 25%  → break-even ROAS = 1 / 0.25 = 4.0
Margen 50%  → break-even ROAS = 1 / 0.50 = 2.0
Margen 70%  → break-even ROAS = 1 / 0.70 = 1.43
```

Si vendes con 25% de margen y tu ROAS es 3, **estás perdiendo plata** aunque el panel se vea verde: necesitabas 4 solo para empatar. Para un producto digital tipo Calculadora de Costos Gastronómicos ($10.000 COP, margen casi 100%, sin costo marginal por copia), tu break-even ROAS es ~1.0 — casi cualquier ROAS positivo es ganancia. Pero ese cálculo de margen y meta es trabajo de modelo de negocio (ver `economist_lushows`); aquí solo te dejamos la fórmula para que no celebres un ROAS que pierde.

## MER y nCAC: las métricas que sí ven el negocio completo

Dos conceptos que el panel de Ads NO te da y que necesitas:

- **MER (Marketing Efficiency Ratio):** ingresos **totales** del negocio ÷ gasto **total** en publicidad (Google + Meta + TikTok + todo). Mide si TODA tu inversión genera ingresos, sin pelearte por quién se lleva el crédito de cada venta. Es la métrica **a prueba de atribución**.

```
MER = ingresos totales del negocio ÷ gasto total en publicidad
Ej: vendiste $50M, gastaste $10M en toda la pauta → MER = 5.0
```

- **nCAC (new customer CAC):** cuánto te cuesta traer un **cliente nuevo** (no recompras). El ROAS de plataforma cuenta recompras de clientes que ya tenías como si la pauta los hubiera "adquirido". El nCAC corta ese autoengaño.

```
nCAC = gasto en adquisición ÷ clientes NUEVOS (excluye recompras)
```

La definición formal de MER, CAC, LTV y cuánto deben valer para TU negocio → **`economist_lushows`**. Aquí solo úsalos como contrapeso al ROAS del panel.

## Triangular: la verdad está en el cruce de cuatro fuentes

Nunca creas a una sola fuente. Cruza cuatro:

| Fuente | Qué te dice | Sesgo |
|---|---|---|
| **Google Ads** | ROAS de plataforma, por campaña | Infla (atribución generosa) |
| **GA4** | Atribución multicanal, comparación entre fuentes | Modelo distinto a Ads (ver 62) |
| **Backend / e-commerce** | Ventas reales registradas (Shopify, tu sistema, planilla) | La verdad operativa, pero no sabe qué las causó |
| **Banco / pasarela** | Plata que de verdad entró (Wompi, Mercado Pago, Nequi, banco) | La verdad financiera final |

El método práctico, semanal:
1. Suma el **gasto total** en Ads de la semana (panel).
2. Suma los **ingresos reales** del backend/banco de esa semana.
3. Calcula **MER** = ingresos ÷ gasto total. Compáralo con tu MER objetivo (ver `economist_lushows`).
4. Mira el **ROAS de plataforma** al lado. Calcula el **factor de inflado**: `ROAS panel ÷ (MER atribuible a Google)`. Si el panel dice ROAS 6 pero tu MER real es 2.5, aprendes que ese canal infla ~2.4x y descuentas mentalmente desde ahí.
5. Decide con el **MER y el backend**, no con el ROAS del panel.

### Plantilla de triangulación (cópiala a tu hoja)

```
SEMANA: ____________
Gasto Google Ads:        $__________   ROAS panel Google:   ____
Gasto Meta:              $__________   Gasto TikTok: $______
GASTO PUBLICITARIO TOTAL: $__________

Ingresos backend (real): $__________
Ingresos banco/pasarela: $__________   (deben cuadrar ±)

MER = ingresos ÷ gasto total =        ____   (objetivo: ____)
Factor inflado Google = ROAS panel ÷ MER = ____x
Clientes nuevos: ____   →  nCAC = $______

DECISIÓN: [escalar / sostener / cortar] porque _______________
```

Si tu MER da rentable y **crece** cuando subes pauta, vas bien aunque el ROAS de plataforma "baje" — el ROAS de plataforma baja al escalar porque agarras tráfico más frío. Eso es normal y no es señal de cortar.

## Caso real

Panel de Ads: ROAS 5.2, "vamos increíble". Banco: los ingresos no subieron cuando se duplicó el gasto. Triangulando:
- Las campañas de **marca** mostraban ROAS 12 (gente que buscaba el nombre del negocio: iban a comprar igual, ver 65).
- El **remarketing** mostraba ROAS 8 (gente que ya estaba decidida).
- Las campañas de **genérico** (demanda nueva real) tenían ROAS 1.8.
- El MER real del negocio era 2.3, no 5.2. Factor de inflado: 2.26x.

Decisión correcta: no celebrar el 5.2; medir incrementalidad en marca/remarketing (ver 65) y juzgar la expansión por el genérico y el MER. Reportar "MER 2.3 real y creciendo", no "ROAS 5.2" (ver 67).

## Errores comunes — blacklist

1. **Tomar el ROAS de plataforma como verdad financiera.** Está inflado 20–50%. Decide con backend y MER (ver 65 para saber cuánto descontar).
2. **No triangular nunca.** Una sola fuente miente. Cruza Ads + GA4 + backend + banco antes de escalar o cortar.
3. **Confundir ROAS con margen.** ROAS 3 con margen 25% pierde plata (break-even era 4). El ROAS no descuenta costo de producto (ver `economist_lushows`).
4. **Contar recompras como adquisición.** El panel infla mezclando clientes nuevos y viejos. Mira nCAC.
5. **Asustarse porque el ROAS de plataforma baja al escalar.** Es normal: agarras tráfico más frío. Lo que importa es que el MER siga rentable.
6. **Pedir que Ads y el banco cuadren al peso.** Nunca van a cuadrar (atribución, ventanas, devoluciones, modelado). Busca consistencia de tendencia, no igualdad exacta.
7. **Decidir el modelo de negocio dentro de Google Ads.** Viabilidad, margen, CAC/LTV objetivo y MER meta se definen en `economist_lushows`, no en el panel de pauta.
8. **Triangular sin restar devoluciones ni fraude.** El backend debe ser ingreso neto cobrado, no ventas brutas; si no, sigues inflando un nivel más abajo.

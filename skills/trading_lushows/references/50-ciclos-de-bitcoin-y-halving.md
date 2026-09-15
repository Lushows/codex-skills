# 50 — Ciclos de Bitcoin y halving

El "ciclo de 4 años" es la narrativa más famosa de cripto. Hay que entenderla — y también
entender por qué apostar el sistema a ella sería mala ciencia.

## Qué es el halving

Bitcoin emite monedas nuevas como recompensa a los mineros (los computadores que validan
transacciones). Cada ~4 años (cada 210.000 bloques), esa recompensa **se corta a la mitad**:
50 → 25 → 12.5 → 6.25 → 3.125 BTC por bloque. Es un recorte de oferta nueva programado en el
código — nadie lo decide, sucede solo.

| Halving | Año aproximado | Recompensa resultante |
|---|---|---|
| 1º | 2012 | 25 BTC |
| 2º | 2016 | 12.5 BTC |
| 3º | 2020 | 6.25 BTC |
| 4º | 2024 | 3.125 BTC |

## La narrativa del ciclo de 4 años

La historia que se cuenta: tras cada halving hay menos BTC nuevo a la venta; si la demanda
se mantiene, el precio sube. El patrón histórico observado ha sido, a grandes rasgos:
**halving → mercado alcista (12-18 meses) → máximo histórico → caída fuerte (bear market,
−70/80% en ciclos pasados) → acumulación → siguiente halving**.

## La crítica honesta (léela dos veces)

- **N=4.** Solo han ocurrido cuatro halvings. Cuatro observaciones no son evidencia
  estadística; son una anécdota repetida. Con N=4, casi cualquier patrón "cuadra".
- **El efecto marginal se encoge.** Cada halving recorta una emisión cada vez más pequeña
  respecto al BTC ya circulante. El choque de oferta del 4º halving es mucho menor que el del 1º.
- **El mercado aprende.** Si "todo el mundo sabe" que después del halving sube, el movimiento
  tiende a adelantarse o a no ocurrir — los patrones públicos se arbitran.
- **La estructura del mercado cambió.** ETFs, institucionales y derivados hacen que los ciclos
  viejos hayan ocurrido en un mercado que ya no existe.
- Los expertos honestos dicen "el ciclo puede romperse o estirarse"; los vendedores de humo
  dicen "el ciclo garantiza X precio en Y fecha". Desconfía de fechas y precios objetivo.

Dónde está el ciclo actual respecto al último halving: **verificar al día** — no asumir de memoria.

## Cómo aplica al AGENTE TRADING

- El bot **no opera el ciclo**: opera régimen actual en velas 1h (`trending-up`, etc.).
  El ciclo es contexto de fondo, no señal de entrada.
- Utilidad real: calibrar expectativas. En fase alcista del ciclo habrá más semanas
  `trending-up` (más trades); en bear, el bot solo-LONG pasará meses casi sin operar — eso
  es correcto, no un bug.
- Peligro a evitar en Fase 8: subir el riesgo "porque viene el halving". El riesgo por trade
  (1.5%) no se toca por narrativas de ciclo.

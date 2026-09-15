# LTV y recompra en dropshipping

## La verdad incómoda primero

En dropshipping de producto único y ganador de temporada, **el LTV es casi igual al primer pedido**.
La gran mayoría de las tiendas que citan LTV lo usan para justificar un CAC que no pueden pagar.

```
Si tu economía solo cierra contando la segunda compra, no tienes negocio:
tienes una apuesta sobre un comportamiento que todavía no observaste.
```

Regla dura: **el primer pedido tiene que ser rentable por sí solo.** El LTV es una mejora, no un
rescate.

## Definiciones que no hay que confundir

| Métrica | Fórmula | Nota |
|---|---|---|
| Valor del primer pedido | ticket − costos − CAC | esto ya lo tienes (`223`) |
| Tasa de recompra a 90 días | clientes con ≥2 pedidos ÷ clientes | el número real |
| Pedidos por cliente | pedidos ÷ clientes únicos | |
| **LTV bruto** | ticket promedio × pedidos por cliente | infla, no lo uses solo |
| **LTV de contribución** | margen de contribución × pedidos por cliente | **el que sirve** |
| Ratio LTV/CAC | LTV de contribución ÷ CAC | ≥ 3 es sano en negocios con recompra |

## Tasas de recompra: qué esperar de verdad

| Tipo de producto | Recompra a 90 días (verificar) |
|---|---|
| Producto único, novedad, sin consumible | 2-8% |
| Con consumible o repuesto | 15-30% |
| Marca de nicho con catálogo | 20-40% |
| Regalo de temporada | 1-5% |

El proyecto México (bundle de temporada, diciembre) cae en la franja baja. Planea con **recompra
cercana a cero** y trata cualquier segunda venta como bono.

## Cuándo el LTV sí cambia la decisión

| Condición | ¿Puedes usar LTV para pagar más CAC? |
|---|---|
| Tienes consumible/repuesto con demanda real | sí, con cautela |
| Tienes ≥3 meses de datos propios de recompra | sí |
| Tienes catálogo de nicho coherente | sí |
| Producto único de novedad | **no** |
| Primera temporada, sin datos | **no** |
| Estás copiando la tasa de recompra de un caso ajeno | **no** |

Y aun cuando puedas: la caja llega **después**. Pagar un CAC de hoy con un ingreso de dentro de 90
días requiere capital que con menos de USD 500 no tienes. Ver `234`.

## Cómo calcular el LTV de contribución bien

```
LTV_contribución = MC_promedio_por_pedido × pedidos_por_cliente
```

Ejemplo México bundle, MC antes de publicidad USD 30,72:

| Pedidos por cliente | LTV de contribución | Ratio sobre CAC 10,54 |
|---|---|---|
| 1,00 | 30,72 | 2,91 |
| 1,10 | 33,79 | 3,21 |
| 1,25 | 38,40 | 3,64 |
| 1,50 | 46,08 | 4,37 |

Subir de 1,00 a 1,10 pedidos por cliente (10% de recompra) mejora el ratio 10%. Útil, no
transformador. Compáralo con el bundle, que duplicó el techo de CAC en un solo movimiento (`218`).

## Las palancas de recompra, ordenadas por rentabilidad

| # | Palanca | Costo | Efecto |
|---|---|---|---|
| 1 | Upsell post-compra (mismo día) | ~0 CAC | el más rentable (`219`) |
| 2 | Correo de repuesto/consumible al día correcto | ~0 | 2-8% de apertura a compra |
| 3 | WhatsApp con lista propia | bajo | alto en LatAm |
| 4 | Retargeting a compradores | bajo CPM | útil solo con catálogo |
| 5 | Programa de referidos | costo del incentivo | funciona en nichos afines |

El "día correcto" del correo de repuesto se calcula así: **duración real del consumible × 0,8**. Si
el filtro dura 60 días, escribe al día 48.

## Lo que el LTV no arregla

| Problema | ¿Lo arregla el LTV? |
|---|---|
| Holgura < 1,3x en el primer pedido | no |
| Tasa de cobro del 52% en COD | no |
| Producto de temporada que muere en enero | no |
| Ticket demasiado bajo | no — sube el ticket (`220`) |
| CAC que sube en Buen Fin | no, llega tarde |

## Un activo que sí vale: la lista

Aun con recompra baja, cada comprador te deja **datos**: teléfono, correo, ciudad, qué ángulo lo
convirtió. Eso vale para:

- el siguiente producto de la misma audiencia,
- públicos similares (lookalike) de compradores reales, que bajan el CAC del siguiente lanzamiento,
- una campaña de temporada el año que viene.

Tratar la lista como activo es la diferencia entre "vendí un producto" y "construí algo". Pero
consérvala con permiso y con las reglas de datos del país (ver `07`; para el marco formal invoca
`contador_lushows` en lo tributario y revisa la normativa de datos personales local).

## Regla final

```
Diseña la economía para que el primer pedido pague todo.
Trata el LTV como utilidad extra, nunca como parte del plan.
```

## Relacionados
`07` · `218` · `219` · `220` · `223` · `224` · `227` · `228` · `231` · `234` · `235` · `239`

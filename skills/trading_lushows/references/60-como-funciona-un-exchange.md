# 60 — Cómo funciona un exchange

## Las piezas, en simple

Un **exchange** (como Binance) es un mercado digital donde compradores y vendedores se
encuentran. Sus piezas:

| Pieza | Qué hace |
|---|---|
| Libro de órdenes | La lista pública de todas las ofertas de compra (bids) y venta (asks) pendientes |
| Matching engine | El motor que cruza órdenes: cuando un bid y un ask coinciden en precio, hay trade |
| Custodia | El exchange guarda tus monedas y tu dinero mientras están en la plataforma |
| API | La puerta por donde los programas (como el bot) consultan precios y mandan órdenes |

El **matching engine** es lo importante de entender: no le compras "al exchange", le compras
a otro participante. El exchange solo empareja y cobra comisión por cada cruce. El
emparejamiento sigue prioridad **precio-tiempo**: mejor precio primero; a igual precio, el
que llegó antes.

## Spot vs derivados

- **Spot**: compras el activo real. Pagas $X, recibes BTC de verdad en tu cuenta. Lo máximo
  que puedes perder es lo que pusiste.
- **Derivados (futuros, perpetuos)**: apuestas sobre el precio sin tener el activo, con
  **apalancamiento** (operar con plata prestada: 10x = mover $1.000 con $100). Permite SHORT,
  pero introduce la **liquidación**: si el precio va en contra lo suficiente, el exchange
  cierra tu posición a la fuerza y pierdes el depósito. La mayoría del retail apalancado
  termina liquidado.

## Custodia: la letra pequeña que quebró a miles

"Not your keys, not your coins": mientras las monedas están en el exchange, legalmente
dependes de que el exchange sea solvente y honesto. **FTX (2022)** era el 2º exchange del
mundo y usaba los fondos de clientes a escondidas; quebró y la gente perdió todo lo depositado.
Reglas derivadas: usar exchanges grandes y regulados, no dejar en la plataforma más capital
del que se está operando, y activar 2FA + whitelist de retiros.

## Binance en concreto

- El exchange con mayor volumen spot del mundo (verificar ranking al día).
- Ofrece spot, futuros, margin; el bot usa/usará **solo spot**.
- **Testnet**: un Binance de mentira con la misma API para probar sin plata real — el paso
  obligado de la Fase 8.
- **Geo-bloqueo**: Binance.com no acepta tráfico desde EE.UU. (allá opera Binance.US, otra
  empresa). Por eso el servidor del bot no puede estar en un datacenter de EE.UU.

## Cómo aplica al AGENTE TRADING

- Elección deliberada de **spot sin apalancamiento**: sin liquidaciones posibles, el peor
  escenario de un trade es el stop, nunca la cuenta.
- El paper actual simula el matching con precios reales + modelo de costos (0.1% + 0.05%
  por lado); la Fase 8 lo reemplaza por el matching engine real vía API — primero testnet.
- El plan de Render **Frankfurt** existe exactamente por el geo-bloqueo: un servidor en
  región de EE.UU. recibiría errores 451 de la API de Binance.

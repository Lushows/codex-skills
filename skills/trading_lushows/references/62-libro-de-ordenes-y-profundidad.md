# 62 — Libro de órdenes y profundidad

## Anatomía del libro

El **libro de órdenes** (order book) es la fila de espera del mercado: todas las órdenes
limit pendientes, ordenadas por precio.

```
        ASKS (venden)          ← el lado de la oferta
 precio 100.10 | 2.1 BTC
 precio 100.05 | 0.8 BTC
 precio 100.02 | 1.5 BTC   ← mejor ask
 ------ SPREAD ------
 precio 100.00 | 1.2 BTC   ← mejor bid
 precio  99.95 | 3.0 BTC
 precio  99.90 | 5.4 BTC
        BIDS (compran)         ← el lado de la demanda
```

- **Bid**: el mejor precio al que alguien quiere comprar. **Ask**: el mejor al que alguien
  quiere vender.
- **Spread**: la distancia entre ambos. Es un costo invisible: comprar a market paga el ask,
  vender a market recibe el bid — cruzar el spread siempre cuesta.
- **Profundidad**: cuánto volumen hay acumulado a cada nivel de precio. Un libro "profundo"
  aguanta órdenes grandes sin moverse; uno "delgado" se desplaza con cualquier empujón.

## Slippage según tamaño: la física del libro

Una orden market "come" el libro nivel por nivel. Si el mejor ask solo tiene 0.5 BTC y
quieres 2, los otros 1.5 se llenan a precios peores. Ese deterioro es el **slippage**, y
crece con el tamaño de la orden en relación con la profundidad:

| Tu orden vs profundidad del par | Slippage esperado |
|---|---|
| $1.000 en BTC/USDT (libro de millones) | Prácticamente cero — ni se nota |
| $100.000 en BTC/USDT | Bajo, ya medible |
| $1.000 en un token ilíquido | Puede ser 1-5%: te comes el libro entero |

Por eso "$1.000 no mueve BTC pero sí mueve un token pequeño": no es magia, es que el libro
del token tiene centavos donde BTC tiene millones. La profundidad exacta de cada par:
**verificar al día** (se ve en la vista de profundidad de Binance).

## Lo que el libro NO dice (anti-humo)

- Las órdenes limit visibles se pueden **cancelar en milisegundos** — los "muros" de compra
  gigantes suelen ser teatro (spoofing, ver `68`), no demanda real.
- Existen órdenes ocultas (iceberg) que no se ven. El libro es una foto parcial y maquillable.
- "Leer el libro" en tiempo real (tape reading) es un oficio de scalpers profesionales;
  para swing en velas 1h aporta casi nada.

## Cómo aplica al AGENTE TRADING

- Con capital de laboratorio ($200-1.000) operando BTC/ETH, el bot es **plancton en un
  océano**: su tamaño jamás moverá el libro, y el modelo de slippage de 5 bps es razonable
  e incluso conservador en horas líquidas (ver `63`).
- La profundidad es EL argumento técnico para no salir de BTC/ETH: la misma lógica de bot
  en un par delgado tendría costos reales varias veces mayores que los modelados.
- En Fase 8 vale la pena registrar el spread al momento de cada ejecución (dato gratis en
  la respuesta de la API) para auditar el modelo de costos con datos propios.

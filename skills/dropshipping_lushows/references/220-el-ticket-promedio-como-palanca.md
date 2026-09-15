# El ticket promedio como palanca

## La palanca más poderosa y la menos trabajada

De las cuatro variables de la ecuación (`06`), el ticket es la única que:

- puedes cambiar **hoy**, sin permiso de nadie,
- no depende de la subasta publicitaria,
- no depende del proveedor,
- y cuyo efecto sobre la utilidad es **no lineal**.

```
UTILIDAD = (TICKET − COSTOS POR PEDIDO − CAC) × PEDIDOS COBRADOS
              ↑
           sube esto y el paréntesis entero se expande,
           porque una parte grande de los costos NO se mueve
```

## La demostración numérica (México verificado)

| | Suelto 699 MXN | Bundle 1.099 MXN |
|---|---|---|
| Ticket | USD 38,20 | USD 60,05 (+57%) |
| Costo total por pedido | USD 22,92 | USD 29,33 (+28%) |
| Techo de CAC | USD 15,28 | USD 30,73 (**+101%**) |
| CAC | USD 12,65 | USD 10,54 |
| **Utilidad por pedido** | **USD 2,63** | **USD 20,18** |
| Holgura | 1,21x | 2,92x |
| ROAS de equilibrio | 2,50 | 1,95 |

En esta corrida (prepago): **+57% de ticket → +667% de utilidad**. En la corrida equivalente de
contraentrega el salto es de **+396%**, porque parte de una base menos apretada (USD 4,11 en vez de
2,63). Las dos cifras son correctas y miden comparaciones distintas: ver la tabla de `218`.
Verifica con tus propios números en `228`.

## Por qué la utilidad se mueve más que proporcionalmente

Porque el ticket sube contra una base de costos **parcialmente fija**:

```
Ticket        ↑ 57%
Costos        ↑ 28%   ← solo suben los que escalan con el contenido
Diferencia    ↑ 101%  ← ese es el techo de CAC
Y la utilidad = techo − CAC, y el CAC no subió (bajó).
```

El flete al cliente (USD 8,74) y el CAC (USD ~10,54) son **costos fijos por pedido**: cuestan lo
mismo con una caja de USD 10 adentro que con una de USD 30. Suman USD 19,28 por pedido que pagas
igual. Contra un ticket de 38,20 son el 50%; contra 60,05 son el 32%.

**Esa dilución es todo el juego.**

## Las 6 palancas del ticket, ordenadas por impacto

| # | Palanca | Impacto típico en ticket | Esfuerzo | Módulo |
|---|---|---|---|---|
| 1 | Bundle / oferta multiproducto | +40-70% | medio | `218` |
| 2 | Estructura de 3 opciones | +10-25% | bajo | `217` |
| 3 | Order bump en checkout | +5-15% | bajo | `219` |
| 4 | Upsell post-compra | +5-12% | medio | `219` |
| 5 | Subir el precio base un escalón | +5-10% | nulo | `216`, `217` |
| 6 | Cobrar el envío (o umbral de gratis) | +5-15% | bajo | `222` |

Las seis se suman. No son alternativas.

## Cuánto vale un dólar más de ticket

Con la estructura México (bundle, comisión ~3,5%, sin costo de producto adicional):

| +USD al ticket | Sube el techo de CAC en | Efecto en holgura (CAC 10,54) |
|---|---|---|
| +1,00 | ~0,96 | 2,92x → 3,01x |
| +5,00 | ~4,82 | 2,92x → 3,38x |
| +10,00 | ~9,65 | 2,92x → 3,83x |

Compáralo con bajar el costo del producto: negociar un 10% de descuento con el proveedor (~USD 1,7
sobre un costo de 17) mueve el techo 1,7. Subir el ticket USD 10 mueve 9,65. **Y lo segundo se hace
en una tarde.**

## El ticket también arregla el CPM de temporada

En Q4 el CPM sube 20-50% y en Black Friday 50-80%. Eso empuja el CAC hacia arriba. Con ticket flaco,
la holgura se cae debajo de 1,3x y quedas fuera del mercado justo en la semana que más se vende.

| Escenario | Holgura base | Holgura con CAC +40% |
|---|---|---|
| Suelto (1,21x) | 1,21x | 0,86x → **pierdes dinero** |
| Bundle (2,92x) | 2,92x | 2,09x → **sigues sano** |

Subir el ticket **antes** de la temporada es lo que te permite competir en la temporada. Ver `238`.

## El ticket y la velocidad de caja

Un ticket más alto también significa más dinero por vuelta del capital. Con prepago (retorno ~3 días,
~25 vueltas en 75 días de temporada), cada vuelta reinvierte más. Ver `233` y `234`.

## Errores de ticket

| Error | Consecuencia |
|---|---|
| Copiar el precio del competidor | heredar su economía sin conocer su costo |
| Bajar precio para "entrar al mercado" | entras sin holgura y sales sin capital |
| Subir ticket agregando peso | el flete se come el aumento (`145`) |
| Medir ticket sin restar reembolsos | el ticket real es el **cobrado y retenido** |
| Optimizar CVR antes que ticket | la CVR la pelea la competencia; el ticket lo decides tú |

## El orden correcto de trabajo

```
1. Ticket      ← lo decides tú, hoy               (218, 219, 217, 222)
2. Costos      ← lo negocias, semanas             (28, 110, 145)
3. Tasa de cobro ← lo operas                       (30, 229)
4. CVR         ← lo peleas con página y oferta     (210-215)
5. CAC         ← lo decide la subasta, último      (80-81)
```

Casi todo el mundo empieza por el 5. Por eso casi todo el mundo quiebra.

## Aplicación México dic-2026

Objetivo de ticket: **≥ USD 60** (≈1.099 MXN) antes de encender presupuesto serio. Con bump del
15-30% del ticket en checkout, apuntar a un ticket promedio efectivo de USD 62-64. Con eso, la
holgura aguanta el CPM de Buen Fin y de diciembre.

## Relacionados
`06` · `11` · `28` · `145` · `216` · `217` · `218` · `219` · `222` · `223` · `228` · `233` · `234` · `238`

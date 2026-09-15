# La ecuación del negocio

## La fórmula completa, en una línea

```
UTILIDAD = (TICKET − COSTOS POR PEDIDO − CAC) × PEDIDOS COBRADOS
```

Todo lo que hagas en este negocio mueve una de esas cuatro variables. Si una acción no mueve
ninguna, es entretenimiento.

## Desglose de cada término

### TICKET (lo que paga el cliente)
Palancas: precio base, **bundle** (`218`), **upsell y order bump** (`219`), envío cobrado.
Es la palanca **más poderosa y la menos usada**, porque sube el ingreso sin tocar el CAC ni el flete.

### COSTOS POR PEDIDO
```
costo del producto
+ flete internacional (si aplica)
+ arancel e impuestos de importación
+ flete al cliente final
+ comisión de pasarela o de plataforma
+ costo de los pedidos fallidos repartido entre los buenos   ← el que todos olvidan
```
El último renglón es el que hunde operaciones aparentemente sanas. Ver `163`, `229`.

### CAC (costo de adquirir un cliente que efectivamente paga)
```
CAC = inversión publicitaria ÷ pedidos COBRADOS
```
Ojo con el denominador: **pedidos cobrados**, no pedidos generados. En contraentrega, la diferencia
entre uno y otro es del 22% al 48%. Ver `224`.

### PEDIDOS COBRADOS
```
pedidos cobrados = impresiones × CTR × CVR × tasa de cobro
```
Cuatro multiplicadores. Mejorar un 20% cada uno no da 20%: da **107%** ((1,2)⁴ = 2,07). Por eso
mejoras pequeñas y simultáneas superan a una sola mejora grande.

## La ecuación en forma de diagnóstico

Cuando algo no funciona, el problema está en uno de estos cuatro lugares. Identifícalo antes de
tocar nada:

| Síntoma | Variable rota | Dónde mirar |
|---|---|---|
| Nadie hace clic | CTR → el creativo | `248`, `249`, `250` |
| Hacen clic, nadie compra | CVR → la página o la oferta | `204`, `210`, `203` |
| Compran pero no llega la plata | Tasa de cobro | `159`, `163`, `282` |
| Vende pero no queda nada | Ticket o costos | `220`, `227`, `229` |
| Vende y deja, pero no escala | CAC sube al subir presupuesto | `269`, `264` |

**Nunca toques dos variables a la vez.** Si cambias el creativo y el precio el mismo día, no vas a
saber cuál movió la aguja.

## El techo de CAC: el número que gobierna todo

```
TECHO DE CAC = TICKET − COSTOS POR PEDIDO
```

Es lo máximo que puedes pagar por una venta antes de perder plata. Todo el negocio es la competencia
entre tu **techo de CAC** y el **CAC real** que te cobra la subasta publicitaria.

- Si techo > CAC real → tienes negocio.
- Si techo ≈ CAC real → estás trabajando gratis.
- Si techo < CAC real → estás pagando por vender.

**Lo importante:** el techo de CAC lo controlas tú (precio, bundle, costos, proveedor). El CAC real
lo controla el mercado. Por eso la mayor parte del trabajo rentable está en **subir el techo**, no en
pelear con la subasta. Ver `11`.

## El ROAS de equilibrio

```
ROAS de equilibrio = TICKET ÷ TECHO DE CAC
```

Es el ROAS por debajo del cual pierdes plata. Lo necesitas **antes** de mirar el panel de anuncios,
porque el ROAS solo no significa nada: un ROAS de 2,0 puede ser excelente o ruinoso según tu margen.

Ver `226` para el cálculo completo y `228` para el modelo ejecutable.

## Ejemplo trabajado (México, prepago, bundle)

```
Ticket                          MXN 1.099  =  USD 60,05
− Costo del producto (bundle)               USD 16,50
− Flete al cliente                          USD  8,74
− Comisión de pasarela con MSI (5,5%)       USD  3,30
− Reembolsos (3% repartido)                 USD  0,78
                                          ─────────────
TECHO DE CAC                                USD 30,73
CAC real (CPM 6,75 · CTR 2,2% · CVR 3,0%)   USD 10,54
                                          ─────────────
UTILIDAD POR VENTA                          USD 20,18
ROAS de equilibrio                              1,95
```

Léelo así: **puedes pagar hasta $30,73 por venta**. Estás pagando $10,54. Tienes casi 3x de holgura,
que es lo que te permite escalar cuando el CPM de Black Friday suba.

## La regla que se deriva de la ecuación

> Cuando el CAC sube por temporada, no bajes el precio para "ser más competitivo".
> Sube el ticket. El CAC no baja con el precio; el techo sí sube.

Ver `238`.

## Relacionados
`11` el techo de CAC · `223` economía unitaria · `224` calcular el CAC real · `226` ROAS de equilibrio · `228` modelo financiero · `220` el ticket como palanca

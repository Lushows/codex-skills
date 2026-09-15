# La cadena logística completa

> El cliente ve una caja en su puerta. Tú tienes que ver **once eslabones**, cada uno con su reloj,
> su costo y su forma de romperse. El dropshipper que fracasa no falla en el anuncio: falla en el
> eslabón 7 y se entera por una reseña de una estrella.

## Los once eslabones

| # | Eslabón | Quién manda | Reloj típico | Cómo se rompe |
|---|---|---|---|---|
| 1 | Producción / picking en fábrica | Proveedor | 1-5 días (7-20 si es fabricación) | Lote agotado, "se acabó el color" |
| 2 | Control de calidad previo | **Tú o tu agente** | 0-2 días | No existe → te enteras con el cliente |
| 3 | Consolidación en bodega China | Agente / forwarder | 1-3 días | Espera a llenar el contenedor |
| 4 | Despacho de exportación China | Forwarder | 1-2 días | Documentos mal armados |
| 5 | Tránsito internacional | Aerolínea / naviera | Ver `146` | Overbooking aéreo, rolling marítimo |
| 6 | Llegada y desconsolidación | Agente en destino | 1-3 días | Vuelo llega sin la carga ("short-shipped") |
| 7 | **Despacho de aduana destino** | Aduana | 3-10 días | Inspección física, valor cuestionado. Ver `151` |
| 8 | Bodega local / recepción | Tú o 3PL | 1-2 días | Conteo no cuadra, faltantes |
| 9 | Picking y empaque del pedido | Tú o 3PL | mismo día - 1 día | Error de SKU, dirección mal impresa |
| 10 | Última milla | Paquetería | 1-5 días | Ver `153`, `154`, `155` |
| 11 | Entrega efectiva y cobro | Repartidor + cliente | El momento de la verdad | Ver `159`, `163` |

## Las dos cadenas que compiten

| | **China directo al cliente** | **Stock local** |
|---|---|---|
| Eslabones por pedido | 1→11 completos, cada vez | 9→11 solamente |
| Tiempo al cliente | 12-30 días | 1-5 días |
| Aduana | Por cada paquete, en nombre del cliente | Una vez, por ti, en lote |
| Arancel | Imprevisible, a veces lo paga el cliente. Ver `149` | Conocido y pagado antes de vender |
| Capital inmovilizado | Casi cero | Todo el lote |
| Devoluciones | Imposibles de gestionar de verdad | Normales |
| Abandono de checkout por demora | ~18% se van (Baymard) | No aplica |
| Compatible con COD | **No.** Ver `31` | Sí |

> La verdad incómoda: casi todo lo que se llama "dropshipping" hoy en LatAm que funciona
> **no es dropshipping puro**. Es importar un lote pequeño, guardarlo y despachar local. El
> dropshipping puro desde China sobrevive solo en nichos de ticket alto donde el cliente acepta
> esperar, y aun ahí `03` explica por qué se está muriendo.

## El reloj que le importa al cliente

El cliente no cuenta días de tránsito. Cuenta desde que le cobran hasta que toca la caja. Eso
incluye tus fines de semana, tu día de picking y la aduana.

| Promesa en la web | Realidad de la cadena China directo | ¿Se cumple? |
|---|---|---|
| "5-7 días" | 12-30 | Nunca |
| "10-15 días" | 12-30 | La mitad de las veces |
| "15-25 días hábiles" | 12-30 | Casi siempre, pero casi nadie compra |
| "2-4 días" con stock local | 2-5 | Sí |

Ver `157` para cómo se comunica esto sin mentir y sin matar la conversión.

## Dónde se pierde el dinero, por eslabón

| Eslabón | Fuga típica | Magnitud |
|---|---|---|
| 2 (calidad) | Producto defectuoso que descubres vendiendo | 3-12% del lote |
| 5 (tránsito) | Elegir aéreo por pánico cuando cabía marítimo | 4-8× el flete. Ver `147` |
| 7 (aduana) | Almacenaje por documentos mal hechos | USD 15-60/día, verificar con tu agente |
| 10 (última milla) | Zona no cubierta, reexpedición | Ver `173` |
| 11 (entrega) | Rechazo en COD: pagas ida **y** vuelta | Ver `163` |

## Quién hace qué: los tres modelos de operación

| Modelo | Tú haces | Costo | Cuándo |
|---|---|---|---|
| **Todo tú** | Compras, importas, guardas en tu casa, empacas | Solo flete + arancel | Primer lote, capital < USD 500 |
| **Fulfillment / 3PL local** | Compras e importas; ellos guardan y despachan | Almacenaje + fee por pedido, verificar | Desde ~300 pedidos/mes |
| **Plataforma de proveedores locales** (Dropi y similares) | Solo vendes; ellos tienen el producto | Comisión ~5% + flete. Ver `132` | Validar demanda sin capital |

Para el proyecto de diciembre 2026 en México con menos de USD 500: **modelo "todo tú"**, stock
local, un solo SKU en bundle. No hay presupuesto para 3PL y no lo necesitas por debajo de 300
pedidos al mes.

## Checklist antes de lanzar un anuncio

1. ¿Tengo el producto **físicamente** o tengo fecha firme de llegada con holgura de 5 días?
2. ¿Sé cuánto me cuesta puesto en la puerta del cliente? (`152`)
3. ¿Sé quién paga el arancel y cuándo? (`149`)
4. ¿Tengo número de guía automático para el cliente? (`156`)
5. ¿La paquetería cubre las zonas que va a alcanzar mi anuncio? (`173`)
6. ¿Qué hago si el envío se atrasa? (`171`) — tener el guion escrito antes, no después.
7. ¿Mi promesa de entrega aguanta la peor semana del mes, no la mejor? (`169`)

Si una respuesta es "lo veo cuando pase", no lances. El eslabón que no planeaste es el que te va a
costar el margen entero.

## Relacionados
`146` tiempos de tránsito · `147` modos de envío · `151` despacho de aduana · `152` costo puesto en
destino · `157` comunicar la entrega · `169` temporada alta · `174` tablero logístico

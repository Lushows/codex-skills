# El contraentrega: cómo funciona

> Contraentrega (COD, *cash on delivery*) es vender a crédito sin saberlo. Tú pagas el producto, el
> empaque y el flete, y **el cliente decide si te paga cuando abre la puerta**. Es la razón por la
> que funciona en LatAm y la razón por la que quiebra a quien no lo modela bien.

## El circuito, paso a paso

| # | Paso | Quién | Tu dinero |
|---|---|---|---|
| 1 | Cliente hace pedido en la web o por WhatsApp | Cliente | 0 |
| 2 | **Confirmación previa** (llamada/WhatsApp) | Tú | costo de confirmar |
| 3 | Picking y empaque | Tú | producto + empaque salen de tu bodega |
| 4 | Generas guía COD con monto a recaudar | Tú | — |
| 5 | Paquetería recoge | Paquetería | **flete de ida comprometido** |
| 6 | Reparto | Paquetería | — |
| 7 | **Entrega y cobro** | Repartidor | entra el dinero… si entrega |
| 7b | No entrega | — | **flete de ida + flete de vuelta + producto de regreso** |
| 8 | Liquidación a tu cuenta | Paquetería / plataforma | 2-7 días hábiles (Dropi) hasta 10-15 según operador |

## Los cuatro costos del COD

| Costo | Cuándo se paga | Magnitud |
|---|---|---|
| Flete de ida | Siempre, entregue o no | MX 120-200 MXN · CO USD 2,50-3,20 |
| Comisión de recaudo | Solo si cobra | % del monto, verificar |
| **Flete de retorno** | Cuando no entrega | Igual o parcial al de ida |
| Comisión de plataforma | Si usas una | Dropi **5%** |

## Las tasas, que son todo el negocio

| Escenario | Tasa de entrega |
|---|---|
| Sin confirmación | **45-60%** |
| Con confirmación previa | **65-78%** |
| Urbano con confirmación por WhatsApp o voz IA | **70-85%** |
| CDMX/GDL/MTY con 99minutos, confirmado | **78%** |
| México sin confirmar / confirmado | 45-55% / 60-72% |
| Colombia sin confirmar / confirmado | 50-60% / 65-78% |

Traducción al bolsillo (fórmula del desperdicio, `163`):

```
desperdicio = (1 − tasa) ÷ tasa
```

| Tasa | Desperdicio | Significa |
|---|---|---|
| 78% | **0,282** | Por cada 100 entregados, pagaste 28 fallidos |
| 65% | 0,538 | 54 fallidos por cada 100 buenos |
| 52% | **0,923** | Casi un fallido por cada bueno |

## El capital: por qué el COD no es para quien arranca

El COD te obliga a financiar **todos** los pedidos, incluidos los que nunca te van a pagar, y a
esperar de 10 a 15 días para ver el dinero.

| | COD | Prepago |
|---|---|---|
| Capital necesario | **Alto** | **Bajo** |
| Días hasta tener la plata | 10-15 | ~3 |
| Vueltas de caja en 75 días | ~6 | ~25 |
| Riesgo del fallido | Tuyo | Casi nulo |

Con **menos de USD 500** no hay COD viable: el primer lote de fallidos te consume el capital antes
de la primera liquidación. Ver `30` y `32`.

## Dónde el COD sí gana

| Condición | Por qué |
|---|---|
| Mercado con baja bancarización | El COD es el único medio de pago disponible |
| Producto de impulso, ticket bajo-medio | El cliente no compraría prepago a un desconocido |
| Operación urbana concentrada | La tasa sube a 78-85% |
| Confirmación previa sistemática | Sin ella, no hay negocio |
| Capital de trabajo suficiente para 3 ciclos | Aguantas la liquidación |

## Las palancas para que funcione, en orden de impacto

1. **Confirmación previa de cada pedido.** +15 a +25 puntos de entrega. Ver `159`, `160`, `161`.
2. **Concentrar en zonas urbanas** con buena paquetería. Ver `173`.
3. Enrutar por destino, no despachar todo con la misma. Ver `154`.
4. Dos teléfonos y referencia de dirección obligatorios en el checkout.
5. Avisar el día de entrega para que el cliente esté.
6. Filtrar pedidos sospechosos antes de despachar. Ver `172`.
7. Reintento gestionado, no automático. Ver `171`.

## El COD y China: incompatibles

Ya está desarrollado en `31`, pero el resumen: financiar 15-30 días de tránsito **más** 10-15 días
de liquidación **más** el 30-50% de fallidos es matemáticamente imposible con capital pequeño. El
COD exige stock local. Sin excepción.

## Contracargos y fraude

El COD no tiene contracargos (no hay tarjeta), pero tiene su propia plaga: pedidos falsos,
direcciones inventadas, competidores saboteando. Ver `172`.

## Prepago disfrazado: la opción intermedia

| Variante | Cómo funciona | Efecto |
|---|---|---|
| Anticipo parcial | Cliente paga el flete por adelantado, el resto contra entrega | Sube mucho la tasa, baja algo la conversión |
| Descuento por prepago | 10-15% menos si paga en línea | Migra a los que sí tienen tarjeta |
| COD solo fuera de zona urbana | Prepago en ciudad, COD en el resto | Mezcla sana |

Son la forma de empezar a migrar sin perder el volumen de golpe.

## Cuándo abandonar el COD

- Tu tasa de entrega lleva 3 semanas por debajo del 60% pese a confirmar.
- El capital de trabajo no alcanza para dos ciclos simultáneos.
- El producto pasó de impulso a considerado y el ticket subió.
- Tu mercado tiene penetración de tarjeta suficiente (México urbano, Chile, España).

## Relacionados
`30` COD vs prepago · `31` COD y China · `32` rotación de caja · `159` subir la tasa de entrega ·
`160` confirmación WhatsApp · `163` costo de los rechazos · `172` fraude en COD · `132` Dropi

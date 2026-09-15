# Upsell, cross-sell y order bump

## Los tres, definidos sin confusión

| Nombre | Qué es | Dónde aparece | Ejemplo |
|---|---|---|---|
| **Order bump** | casilla que agrega algo pequeño al carrito | en el checkout, antes de pagar | "+199 MXN: agrega el estuche de viaje" |
| **Upsell** | versión mayor o cantidad mayor del mismo producto | antes de pagar, o justo después | "llévate 2 y ahorra 300" |
| **Cross-sell** | producto distinto que complementa | después de pagar (upsell post-compra) o en el carrito | "el repuesto para 6 meses" |

Los tres atacan la misma variable: el **ticket**. Y el ticket es la palanca donde el flete y el CAC
ya están pagados (`220`).

## Por qué el post-compra es dinero casi gratis

Cuando el cliente ya pagó, el CAC de esa venta ya está cubierto. Todo lo que agregue después entra
con una estructura de costos distinta:

| | Venta principal | Upsell post-compra |
|---|---|---|
| CAC | USD 10,54 | **USD 0** |
| Flete adicional | — | ~0 si va en la misma caja |
| Pasarela | % | % |
| Margen que queda | utilidad normal | **casi todo el precio menos el costo** |

Esa es la razón por la que un upsell post-compra con 10-20% de aceptación puede valer más que una
mejora del 10% en CVR: llega sin CAC.

## Tasas de aceptación de referencia

| Mecanismo | Rango típico | Notas |
|---|---|---|
| Order bump en checkout | 10-30% | el más fácil de implementar |
| Upsell de cantidad ("lleva 2") | 15-35% | funciona con consumibles y regalables |
| Upsell post-compra 1 clic | 8-20% | requiere pasarela que lo soporte |
| Cross-sell por correo (día 7-30) | 2-8% | ver `230` |

**Verificar con tus propios datos.** Estos rangos varían mucho por nicho, país y precio del
complemento. Los publicados por plataformas suelen ser optimistas.

## La regla del precio del complemento

```
Precio del order bump ≈ 15% a 35% del ticket principal
```

| Ticket principal | Rango sano del bump |
|---|---|
| 699 MXN | 100-250 MXN |
| 1.099 MXN | 165-385 MXN |
| 1.799 MXN | 270-630 MXN |

Por encima del 35%, el cliente vuelve a "modo decisión" y se enfría; a veces abandona el carrito
entero. Por debajo del 15%, no mueve la aguja.

## Impacto en la economía: ejemplo

Base México bundle: ticket USD 60,05 · techo de CAC USD 30,73 · CAC USD 10,54 · utilidad USD 20,18.

Agrega un order bump de USD 10,00 con costo marginal de USD 3,00 y 20% de aceptación:

```
Ingreso extra promedio por pedido  = 0,20 × 10,00 =  USD 2,00
Costo extra promedio por pedido    = 0,20 ×  3,00 =  USD 0,60
Comisión pasarela sobre el extra   ≈ 0,20 × 10,00 × 0,035 = USD 0,07
Utilidad extra por pedido                          ≈  USD 1,33

Nuevo techo de CAC ≈ 30,73 + 1,33 = USD 32,06
Nueva holgura      ≈ 32,06 ÷ 10,54 = 3,04x
```

Un solo order bump bien puesto movió la holgura de 2,92x a ~3,04x. Verificar con `228`.

## Dónde poner cada uno

```
Página de producto
  └─ 3 opciones de compra (A suelto / B bundle / C doble)        ← 217
Carrito
  └─ cross-sell discreto: "quienes llevaron esto también..."
Checkout
  └─ ORDER BUMP: una sola casilla, un solo producto, una línea   ← el más rentable
Pago aceptado
  └─ UPSELL 1 CLIC: sin volver a pedir tarjeta                   ← sin CAC
Correo día 3 / 7 / 21
  └─ CROSS-SELL de repuesto o complemento                        ← 230
```

## Reglas que no se rompen

| Regla | Por qué |
|---|---|
| **Una** oferta por punto | dos opciones en el checkout bajan la conversión principal |
| Nunca pongas el bump antes del formulario de pago | interrumpe la intención |
| El upsell post-compra no debe retrasar la confirmación | el cliente necesita ver "pedido confirmado" |
| Si el bump baja la CVR principal, quítalo | mide la CVR total, no solo la aceptación del bump |
| Todo debe caber en la misma caja | si dispara un segundo envío, revisa la aritmética (`145`) |

El error más caro: un bump que sube el ticket 8% y baja la conversión del checkout 12%. Neto
negativo. Mide **pedidos cobrados × ticket**, no el porcentaje de aceptación.

## Qué ofrecer, por nicho

| Nicho | Order bump que funciona |
|---|---|
| Mascotas | correa a juego, bolsas biodegradables, placa grabada |
| Belleza | estuche de viaje, aplicador extra, repuesto |
| Cocina | set de recetas impreso, accesorio de corte extra |
| Hogar | recargas, unidades adicionales para otro cuarto |
| Bebés | segunda unidad para la pañalera |
| Auto | segunda base para el otro carro |
| Fitness | banda de resistencia adicional, guía de rutinas |

## Frontera

Cómo se **escribe** la oferta del bump y cómo se maneja la objeción del cliente en conversación:
invoca `ventas_lushows`. Cómo se **ve** el checkout: invoca `desingweb-lushows`.

## Relacionados
`145` · `210` · `216` · `217` · `218` · `220` · `223` · `228` · `230`

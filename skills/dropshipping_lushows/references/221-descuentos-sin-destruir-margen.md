# Descuentos sin destruir margen

## Lo que cuesta un descuento

Un descuento no sale del precio: sale **entero** del techo de CAC. Y el techo de CAC es lo que te
permite comprar tráfico.

México, bundle: ticket USD 60,05 · costos USD 29,33 · techo USD 30,72 · CAC USD 10,54.

| Descuento | Ticket | Techo de CAC | Holgura | Utilidad |
|---|---|---|---|---|
| 0% | 60,05 | 30,72 | 2,91x | 20,18 |
| 5% | 57,05 | 27,86 | 2,64x | 17,32 |
| 10% | 54,05 | 25,01 | 2,37x | 14,47 |
| 15% | 51,04 | 22,16 | 2,10x | 11,62 |
| 20% | 48,04 | 19,31 | 1,83x | 8,77 |
| 30% | 42,04 | 13,60 | 1,29x | 3,06 |

(La comisión de pasarela baja con el ticket, así que el techo cae un poco menos que el descuento
nominal. Verificado con el modelo de `228`.)

**Un 20% de descuento se come el 57% de tu utilidad por pedido.** Un 30% se come el 85%.

## Cuántas ventas extra tienes que hacer para empatar

```
ventas extra necesarias = utilidad_original ÷ utilidad_con_descuento − 1
```

| Descuento | Utilidad/pedido | Ventas extra para igualar la utilidad total |
|---|---|---|
| 10% | 14,47 | +39% |
| 20% | 8,77 | +130% |
| 30% | 3,06 | +560% |

Si tu descuento del 20% no duplica las ventas, perdiste. Casi ningún descuento duplica ventas.

## Cuándo un descuento sí tiene sentido

| Situación | ¿Descontar? | Alternativa mejor |
|---|---|---|
| Liquidar stock muerto antes de que caduque o se devalúe | **sí** | ninguna |
| Recuperar carrito abandonado (cupón dirigido) | sí, acotado | recordatorio sin cupón primero |
| Buen Fin / Black Friday, donde el mercado lo exige | sí, planeado | MSI y bundle en vez de % |
| Segunda compra de un cliente existente | sí | ya no pagas CAC (`230`) |
| CPM alto y caen las ventas | **no** | ver abajo |
| "Para arrancar / para entrar al mercado" | **no** | mejor oferta (`210`) |
| Competidor bajó precio | **no** | cambia la comparación, no el precio |

## El error del CPM alto

Cuando el CPM sube y las ventas caen, el instinto es descontar. Es exactamente al revés: con CPM
alto necesitas **más** techo de CAC, no menos. Descontar en temporada alta es pagar publicidad cara
con margen barato. Ver `238`.

## Formas de descontar que no destruyen margen

| Mecanismo | Por qué es mejor | Costo real |
|---|---|---|
| **Más producto por el mismo precio** | sube costo marginal, no baja ticket | costo del extra, no % del ticket |
| **Envío gratis sobre un umbral** | sube el ticket promedio | el flete, ya calculado (`222`) |
| **Digital de regalo** | valor percibido alto | ~0 |
| **MSI en vez de %** | +36% CVR por ~1,5 pp | 1,5 pp del ticket |
| **Ancla verificable** ("ahorras 298 vs por separado") | el bundle ya es el descuento | 0 adicional |
| Descuento en la 2ª unidad | mantiene el ticket base | costo de la unidad extra |

Regla mental: **regalar producto cuesta el costo; descontar cuesta el precio.** El costo es una
fracción del precio. Por eso regalar siempre es más barato que descontar el mismo valor nominal.

### Ejemplo comparado

Quieres dar al cliente una sensación de USD 15 de beneficio:

| Forma | Valor percibido | Costo real para ti |
|---|---|---|
| Descuento de USD 15 | 15 | **15,00** |
| Accesorio que vale 15 al público | 15 | ~4,50 (costo) |
| Guía digital que vale 15 | 15 | ~0,00 |

## Cupones: reglas de operación

| Regla | Razón |
|---|---|
| Nunca campo de cupón visible sin cupón activo | el cliente sale a buscarlo y no vuelve |
| Cupón solo por correo o SMS de recuperación | dirigido, medible |
| Fecha de expiración real | si no expira, no urge |
| Un solo cupón por cliente | evita apilamiento |
| Nunca cupón permanente | el precio lista deja de existir |

## Descuento y percepción de calidad

En categorías donde el cliente compra confianza (bebés, salud, estética), el descuento profundo
**baja** la conversión: activa la sospecha. En esas categorías el descuento debe ser envío gratis,
regalo o MSI, nunca un −40% en rojo.

## Antes de aprobar cualquier descuento

```
1. Recalcula el techo de CAC con el precio descontado        (11, 228)
2. Verifica que la holgura siga ≥ 2,0x en escenario conservador
3. Calcula cuántas ventas extra necesitas para empatar
4. Si no crees que las vas a hacer, no descuentes
```

Para auditar la aritmética de un descuento concreto, invoca `Matematicas_lushows`.

## Relacionados
`11` · `210` · `216` · `217` · `218` · `220` · `222` · `228` · `230` · `238`

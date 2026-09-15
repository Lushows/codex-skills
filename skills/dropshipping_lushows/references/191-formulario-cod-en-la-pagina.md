# Formulario COD en la página

> Vigencia: 14-sep-2026. Decisión COD vs prepago: `30`. Por qué COD y China no se llevan: `31`.

En Colombia, ~70% del ecommerce de producto físico se paga contraentrega. En ese contexto, el
checkout tradicional de tres pasos es un lastre: la gente no va a pagar nada ahora, así que pedirle
que navegue un checkout es fricción sin propósito. La respuesta es el **formulario COD en la misma
página de producto**.

## Qué es

Un bloque de 3-4 campos, dentro de la página de producto, que crea el pedido de un clic. Sin ir a
carrito ni a checkout. La herramienta estándar en Shopify es **Releasit**; hay equivalentes.

## Lo que gana

| Métrica | Checkout normal | Formulario COD |
|---|---|---|
| Conversión conservadora | 2,0% | **4,5%** |
| Conversión con buena página y creativo | 3,0% | **6,5%** |
| Conversión de ganador real | 4,0% | **8,5%** |

El salto es enorme. Pero **conversión no es facturación**: en COD, el número que manda es la tasa de
entrega efectiva. `30`.

## La aritmética que nadie enseña

Un pedido COD no es una venta hasta que el cliente recibe y paga.

| Concepto | Ejemplo Colombia |
|---|---|
| Pedidos creados | 100 |
| Contactados / confirmados | 78 |
| Despachados | 78 |
| **Entregados y pagados** | **55-65** |
| Devueltos | 13-23 |
| Costo del flete de ida y vuelta de los devueltos | **Lo pagas tú** |

> Rangos orientativos; **verificar con tu transportadora y tu producto**. Con una tasa de entrega de
> 60%, una conversión de 6,5% se comporta como un 3,9% de prepago — y además con el costo de los
> fletes fallidos encima.

Antes de elegir COD, corre el número completo: invoca `Matematicas_lushows` y usa el techo de CAC de
`11`.

## Estructura del formulario

| Campo | ¿Va? | Nota |
|---|---|---|
| Nombre completo | Sí | |
| **Teléfono / WhatsApp** | Sí | El campo más importante: sin él no hay confirmación |
| Dirección | Sí | Con espacio para referencias |
| Ciudad / departamento | Sí | Lista desplegable, no texto libre |
| Correo | Opcional | Súbelo si puedes: sirve para remarketing |
| Cantidad / bundle | Sí | Botones de opción, no menú |

Cuatro campos obligatorios. Ni uno más.

## El texto del formulario (listo para copiar — Colombia)

> ### Pide ahora y paga cuando lo recibas
>
> No pagas nada hoy. Llena tus datos, te llamamos para confirmar y pagas en efectivo al mensajero
> cuando te llegue.
>
> [ Nombre completo ]
> [ Teléfono / WhatsApp ]
> [ Dirección con referencias ]
> [ Ciudad ▾ ]
>
> **[ PEDIR AHORA — PAGO CONTRA ENTREGA ]**
>
> Envío gratis a toda Colombia · Llega en 2 a 5 días hábiles · Si no te gusta, no lo recibes.

La última línea (`si no te gusta, no lo recibes`) es la reversión de riesgo natural del COD y hay
que decirla: es la mayor ventaja del modelo. `188`.

## Dónde va en la página

| Ubicación | Prioridad |
|---|---|
| En el encabezado, junto al precio | **Obligatoria** |
| Después del video | Sí |
| Después de la prueba social | Sí |
| Al final, antes del pie | Sí |

Botón fijo en móvil que baja al formulario, con el texto `Pedir contra entrega`.

## La confirmación: donde se gana o se pierde el negocio

El pedido COD sin confirmar es un flete perdido. Reglas:

1. **Contacta en menos de 30 minutos.** La tasa de confirmación cae rápido con el tiempo.
2. **WhatsApp primero, llamada después.** En LatAm nadie contesta números desconocidos.
3. **Mensaje corto y claro** (listo para copiar):

> Hola [nombre], soy [tu nombre] de [tienda]. Recibimos tu pedido de [producto] por $[monto], pago
> contra entrega. ¿Te lo despacho a [dirección]? Llega en 2 a 5 días hábiles.

4. **Dos intentos, luego uno al día siguiente.** Después, cancela y no despaches.
5. **Nunca despaches sin confirmar** salvo que tu tasa de entrega sin confirmar sea comprobadamente
   alta. Cada devolución te cuesta dos fletes.

Si automatizas esta confirmación con un bot de WhatsApp, invoca `ventas_lushows` para el guion y
mira `133` para las plataformas COD.

## Cuándo NO usar formulario COD

| Situación | Por qué |
|---|---|
| **México, prepago, cierre en la web** | El caso del proyecto de diciembre 2026: no aplica |
| El producto viene de China con 3-5 semanas de tránsito | `31`: la tasa de rechazo se dispara |
| Ticket alto | El mensajero carga mucho efectivo, la transportadora lo limita |
| Tu transportadora no maneja recaudo en tu zona | Sin recaudo no hay COD |
| Margen que no aguanta 35% de devoluciones | Haz la cuenta antes, no después |

## Coexistencia: COD y prepago en la misma página

Se puede, y suele ayudar:

- Formulario COD como opción principal.
- Botón secundario `Pagar ahora y ahorra $X` con un descuento pequeño (5-10%).

El descuento por prepago vale la pena: te ahorra el flete fallido y la comisión de recaudo, y mejora
el flujo de caja. Comunícalo como beneficio: `Paga ahora y te sale $50.000 en vez de $55.000`.

## Relacionados
`30` COD vs prepago · `31` COD y China · `190` checkout prepago · `193` pasarelas LatAm · `203` conversión esperada

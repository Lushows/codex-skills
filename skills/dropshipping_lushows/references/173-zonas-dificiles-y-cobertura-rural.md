# Zonas difíciles y cobertura rural

> Tu tasa de entrega nacional es un promedio que miente. Adentro hay ciudades que entregan al 82% y
> municipios que entregan al 38%. Mientras los mires juntos, los buenos están financiando a los
> malos y tú crees que el problema es el producto.

## Por qué una zona es difícil

| Causa | Efecto |
|---|---|
| Cobertura real menor que la declarada | La paquetería reexpide o devuelve |
| Un solo intento de entrega | Si no está, vuelve |
| Reparto semanal, no diario | 5-8 días de entrega |
| Direcciones sin nomenclatura | El repartidor no encuentra |
| Menor bancarización → COD obligatorio | Tasa de cobro más baja |
| Inseguridad en la ruta | Entregas suspendidas |
| Geografía (montaña, río, isla) | Recargo y tiempo |

## El diagnóstico: segmentar el promedio

Toma tus últimos 200-300 pedidos y arma esta tabla. Es media hora de trabajo y suele ser el
hallazgo más rentable del mes.

| Zona | Pedidos | Entregados | Tasa | Desperdicio | Margen por despachado |
|---|---|---|---|---|---|
| Metro A | | | | (1−t)/t | |
| Metro B | | | | | |
| Ciudades intermedias | | | | | |
| Municipios pequeños | | | | | |
| Rural / difícil acceso | | | | | |

Usa el script de `163` por zona. Vas a encontrar zonas con margen negativo que llevabas meses
subsidiando.

## Los cuatro tratamientos

| Tasa de la zona | Tratamiento |
|---|---|
| **> 70%** | Normal. Escala pauta ahí |
| **55-70%** | Confirmación reforzada + enrutamiento a la transportadora fuerte de la zona |
| **40-55%** | **Anticipo del flete** o prepago obligatorio |
| **< 40%** | **Excluir**, o solo prepago con envío cobrado |

Excluir no es abandonar el mercado: es dejar de pagar por vender ahí en condiciones que pierden
dinero. Puedes volver cuando tengas otra transportadora o un modelo prepago.

## Las palancas, de menor a mayor fricción

1. **Enrutar a la transportadora correcta.** En Colombia, Interrapidísimo y Envía cubren donde
   Coordinadora no llega (`154`). En México, 99minutos es urbano y Estafeta o Paquetexpress
   alcanzan más lejos (`153`). Gratis, y vale varios puntos.
2. **Confirmación obligatoria, más estricta**: además del monto y la dirección, pide una referencia
   ("frente a la iglesia", "tienda de la esquina") y un segundo teléfono.
3. **Aviso el día de la entrega** con ventana horaria.
4. **Anticipo del flete** en línea: el cliente paga el envío por adelantado y el resto contra
   entrega. Sube muchísimo la tasa; baja algo la conversión.
5. **Prepago obligatorio** con descuento como compensación.
6. **Exclusión** por código postal o municipio en el checkout.

## Cómo se excluye bien

| Mal | Bien |
|---|---|
| Que el cliente pague y después le digas que no llegas | Bloquear el código postal en el checkout |
| Mensaje seco de "no enviamos ahí" | "En tu zona enviamos con pago anticipado. ¿Te muestro cómo?" |
| Excluir un departamento entero | Excluir por municipio o CP específico |
| Excluir sin revisar | Revisar cada 3 meses: la cobertura cambia |

Convertir la exclusión en una oferta de prepago recupera parte de esos clientes en vez de perderlos.

## Segmentar la pauta, no solo la logística

Si la zona difícil te llega igual porque el anuncio alcanza todo el país, el filtro logístico llega
tarde. Se arregla arriba:

- Excluir ubicaciones en la campaña, o
- Concentrar presupuesto en las ciudades que entregan bien.

En México, **CDMX / GDL / MTY con confirmación entregan al 78%** — por eso el dinero se concentra
ahí y no se reparte por todo el país. Para la mecánica de segmentación geográfica, invoca
`facebook_ads_lushows`.

## La trampa del volumen

Existe la tentación de aceptar la zona mala "porque suma pedidos". Los pedidos no son el negocio; el
margen sí. Una zona al 45% con desperdicio de 1,22 puede dejar margen negativo por pedido: **entre
más vendes ahí, más pierdes**. Es el error que más rápido quiebra a una tienda que "está creciendo".

## Cuándo la zona difícil sí vale la pena

| Condición | Por qué |
|---|---|
| Ticket alto que aguanta el flete doble | El margen absorbe el desperdicio |
| Competencia nula ahí | Puedes cobrar más |
| Producto que allá no se consigue | Menos rechazo, más necesidad |
| Prepago aceptado por el cliente | Desaparece el problema |
| Clientes que recompran | El segundo pedido no paga CAC |

## Revisión periódica

| Cada | Qué revisas |
|---|---|
| Semanal | Tasa por ciudad, top 5 y bottom 5 |
| Mensual | Reclasificar zonas entre los cuatro tratamientos |
| Trimestral | Reabrir zonas excluidas y probar con 30 pedidos |
| Al cambiar de transportadora | Todo el mapa otra vez |

## Relacionados
`153` paqueterías México · `154` paqueterías Colombia · `159` tasa de entrega · `163` costo de los
rechazos · `172` fraude · `174` tablero · invoca `facebook_ads_lushows`

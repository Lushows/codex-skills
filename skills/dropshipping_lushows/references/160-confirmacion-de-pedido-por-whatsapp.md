# Confirmación de pedido por WhatsApp

> Confirmar sube la tasa de entrega **de 45-60% a 65-78%**, y en urbano hasta **70-85%**. No es
> servicio al cliente: es la operación más rentable del negocio. Este módulo trae el guion completo,
> listo para copiar, con el manejo de las cinco objeciones que aparecen siempre.

## Las reglas antes del guion

| Regla | Por qué |
|---|---|
| Confirma **antes de despachar**, nunca después | Después ya pagaste el flete |
| Primer contacto en **menos de 30 minutos** | La intención de compra se enfría rápido |
| Pregunta cerrada, no abierta | "¿Confirmas?" no; "¿Te lo enviamos hoy o mañana?" sí |
| Di el **monto exacto** que va a pagar | Evita el "no tenía efectivo" |
| Máximo 3 intentos en 24 h, luego cierras | Más es acoso y te reportan |
| Todo por escrito queda como prueba | Sirve contra reclamos |
| Un humano o un bot bien hecho, no un formulario | El formulario no confirma nada |

## El guion — mensaje 1 (a los 5-30 minutos)

> Hola {Nombre} 👋 Soy {tu nombre} de {Tienda}.
> Me llegó tu pedido de **{Producto}** por **${monto}**.
>
> Solo confirmo dos datos antes de despacharlo:
> 📍 {Dirección tal como la escribió}
> 📞 {Teléfono}
>
> ¿Está correcto? Si sí, respóndeme **SÍ** y sale hoy mismo.

Por qué funciona: dice quién eres, qué pidió y cuánto vale (elimina el "no recuerdo"), muestra los
datos (corrige direcciones malas) y pide una acción de una palabra.

## Mensaje 2 — si no responde (a las 3-4 horas)

> {Nombre}, te escribo por el pedido de **{Producto}**.
> Tengo la última unidad apartada a tu nombre hasta hoy a las {hora}.
> ¿Te la despacho? Responde **SÍ** o **NO** y listo, no te molesto más.

## Mensaje 3 — último (al día siguiente, en la mañana)

> Buenos días {Nombre}. Última vez que te escribo por el pedido de **{Producto}**.
> Si sigues interesado, respóndeme hoy y te lo despacho.
> Si ya no, dime **NO** y lo libero sin ningún problema. 🙌

Sin respuesta después del mensaje 3: **no despachas**. Un pedido no confirmado que se despacha es
un fallido con el 55-70% de probabilidad, y pagas ida y vuelta.

## Confirmado — mensaje de cierre

> ¡Listo {Nombre}! Tu pedido sale hoy 📦
> Llega entre el **{fecha}** y el **{fecha+n}**.
> Monto a pagar al recibir: **${monto} exactos**.
> Te mando el número de guía apenas salga de bodega.
>
> Ten el teléfono a la mano el día de la entrega, el repartidor te llama antes de llegar.

Esa última línea sube la tasa varios puntos por sí sola.

## Las cinco objeciones

### 1. "Déjame pensarlo" / "Después te confirmo"

> Claro {Nombre}, sin problema.
> Solo para que sepas: tengo la unidad apartada hasta {hora de hoy}. Después la libero para
> otro pedido.
> Y recuerda que **no pagas nada ahora**: pagas cuando el repartidor te lo entregue en la mano. Si
> cuando llega no te convence, no lo recibes y ya.
>
> ¿Te lo aparto entonces?

### 2. "Está muy caro"

> Te entiendo. El precio es **${monto}** e incluye el envío hasta tu puerta — no pagas flete aparte.
> Y {beneficio concreto del producto, una línea}.
> Si lo comparas con {alternativa}, sale {comparación honesta}.
>
> ¿Lo dejamos en el paquete de {N} unidades a ${monto} o prefieres solo uno?

*(Bajar el precio no es opción. Cambiar el tamaño del paquete sí. Para trabajo fino de objeciones,
invoca `ventas_lushows`.)*

### 3. "¿Y si no me sirve / no es como en la foto?"

> Por eso es **pago contra entrega**: el repartidor te lo lleva, lo revisas ahí mismo y si no es lo
> que esperabas, **no lo recibes y no pagas nada**. Cero riesgo para ti.
> {Si aplica: y tienes {N} días de garantía, cualquier falla te lo cambiamos.}
>
> ¿Te lo despacho hoy?

### 4. "No estoy seguro de estar en casa" / "No sé si voy a tener el efectivo"

> Fácil de resolver. Dime **qué día te queda mejor** y lo programo para ese día: ¿{día 1} o
> {día 2}?
> Y si prefieres, lo puede recibir otra persona: solo dime el nombre.
> El monto exacto es **${monto}**, para que lo tengas listo.

*(Nunca dejes "cualquier día". Una ventana concreta sube mucho la entrega.)*

### 5. "¿Ustedes son confiables?" / "¿Cómo sé que no es estafa?"

> Pregunta justa, {Nombre}. Mira:
> • **No pagas nada por adelantado.** Pagas solo cuando tienes el producto en la mano.
> • Te mando el número de guía de {transportadora} para que lo sigas tú mismo.
> • Estamos en {redes / web} y llevamos {tiempo} enviando a todo {país}.
>
> Si quieres, te mando fotos del producto real antes de despachar.

## Qué NO hacer

| Error | Consecuencia |
|---|---|
| "¿Confirmas tu pedido?" a secas | Tasa de respuesta baja, no resuelve dudas |
| Escribir a los 3 días | Ya se enfrió: casi nadie confirma |
| Despachar el que no contestó "por si acaso" | Es el fallido más caro que existe |
| Rebajar el precio en la confirmación | Enseñas que tu precio es negociable |
| Mandar 8 mensajes | Bloqueo y reporte del número |
| Usar un número nuevo para 300 mensajes al día | Bloqueo de WhatsApp. Calienta el número gradualmente |
| No registrar el resultado de cada confirmación | No puedes medir nada (`174`) |

## Qué registrar de cada pedido

`confirmado_si` · `confirmado_no` · `sin_respuesta` · `dato_corregido` · `hora_primer_contacto` ·
`intentos` · `motivo_de_no`. Los motivos de "no" son oro puro: te dicen si el problema es el precio,
el anuncio o el producto.

## Números a vigilar

| Métrica | Bueno | Malo |
|---|---|---|
| Tasa de confirmación | 60-80% | < 45% |
| Tiempo al primer contacto | < 30 min | > 3 h |
| Entrega de los **confirmados** | 75-88% | < 65% |
| Entrega de los **no confirmados** | 30-45% | — (por eso no se despachan) |

## Relacionados
`159` tasa de entrega · `161` confirmación por voz con IA · `162` reusar un bot propio ·
`158` contraentrega · `163` costo de los rechazos · `172` fraude · invoca `ventas_lushows`

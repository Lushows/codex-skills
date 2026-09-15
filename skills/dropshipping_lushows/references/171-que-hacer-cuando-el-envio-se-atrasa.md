# Qué hacer cuando el envío se atrasa

> El retraso no se puede evitar siempre. Lo que sí se puede elegir es **quién avisa primero**. Si
> avisas tú, eres una tienda que se hace cargo. Si avisa el cliente, eres una tienda que lo dejó
> tirado. El mismo retraso, dos negocios distintos.

## La regla

> **Avisa antes de que pregunte.** Siempre. Sin excepción. Aunque no tengas solución todavía.

Un cliente informado espera. Un cliente ignorado pide reembolso, hace contracargo y deja reseña. El
costo de un mensaje proactivo es cero; el de callarse es el CAC completo más el producto.

## Los cuatro niveles de retraso

| Nivel | Situación | Qué haces |
|---|---|---|
| **1. Leve** | 1-2 días sobre lo prometido | Mensaje proactivo, nueva fecha, nada más |
| **2. Moderado** | 3-5 días, o sin movimiento 72 h | Mensaje + compensación pequeña + fecha firme |
| **3. Grave** | Más de 7 días o riesgo de extravío | Llamada + opciones: reenvío o reembolso |
| **4. Fecha perdida** | El producto era para una fecha que ya pasó | **Reembolso inmediato**, sin pelear |

El nivel 4 es el de Navidad. Un regalo que llega el 27 de diciembre no sirve. Pelearlo es perder
dos veces.

## Guiones, listos para copiar

### Nivel 1 — retraso leve

> Hola {Nombre}, te escribo para avisarte yo antes de que te preguntes 🙂
> Tu pedido de **{Producto}** va con un día de retraso por {motivo real y breve}.
> **Nueva fecha de entrega: {fecha}.**
> Guía: {número} — puedes seguirlo aquí: {enlace}.
> Cualquier cosa, me escribes directo a este número.

### Nivel 2 — retraso moderado

> {Nombre}, tu pedido de **{Producto}** se está demorando más de lo que te prometí y quiero ser
> claro contigo: {motivo real}.
> **Nueva fecha: {fecha}** y ya está confirmada con la transportadora.
> Por la molestia te dejo **{compensación concreta}** para tu próxima compra.
> Si prefieres cancelar y te devuelvo el dinero, dímelo y lo hago hoy mismo. Tú decides.

### Nivel 3 — grave / posible extravío

> {Nombre}, tu pedido lleva {n} días sin movimiento y ya abrí una investigación con
> {transportadora} (caso {número}).
> No te voy a poner a esperar mi reclamo. Tienes dos opciones y cualquiera es hoy:
> **1)** Te despacho otra unidad hoy mismo, sin costo.
> **2)** Te devuelvo el dinero completo ahora.
> ¿Cuál prefieres?

### Nivel 4 — la fecha ya no sirve

> {Nombre}, tu pedido no va a llegar antes de {fecha}, y sé que lo comprabas para eso.
> **Te devuelvo el dinero completo, hoy.** Ya lo estoy procesando, no tienes que hacer nada.
> Lamento haberte fallado. Si el producto te sigue interesando para después, te dejo
> {compensación} para cuando quieras.

## Por qué funcionan

1. **Dicen el motivo real.** "Problemas logísticos" no significa nada; "la transportadora tuvo
   saturación en el centro de distribución de {ciudad}" sí.
2. **Dan una fecha nueva y concreta**, no "a la brevedad".
3. **Ofrecen salida.** El cliente que puede cancelar y elige quedarse ya no es un riesgo.
4. **Compensan antes de que lo pidan.** Compensar después de la queja vale la mitad.
5. **Asumen.** "Te fallé" desactiva el conflicto. "Fue la transportadora" lo enciende.

## La compensación: cuánto y cómo

| Nivel | Compensación razonable |
|---|---|
| 1 | Ninguna. Solo información |
| 2 | Cupón para próxima compra (20-30% del margen del pedido) |
| 3 | Reenvío gratis o reembolso completo, a elección del cliente |
| 4 | Reembolso completo + cupón |

Regla: **la compensación sale del margen de ese pedido, no de un presupuesto aparte.** Si el
producto no aguanta compensar un retraso, tu margen es demasiado fino (`42`).

## Lo que nunca se hace

| Práctica | Consecuencia |
|---|---|
| Silencio hasta que reclama | Contracargo y reseña |
| "Está en camino" sin fecha | El cliente pierde la paciencia igual, pero desconfiando |
| Culpar a la transportadora | Al cliente no le importa quién falló: te compró a ti |
| Prometer una segunda fecha que tampoco cumples | La segunda promesa rota es irreversible |
| Negar el reembolso cuando la fecha ya pasó | Contracargo garantizado, y lo pierdes |
| Responder con plantilla genérica | Se nota, y enfurece |

## Cuándo reembolsar sin discutir

1. La fecha del uso ya pasó (regalo, evento, temporada).
2. Han pasado más de 7-10 días sin movimiento de tracking.
3. El cliente lo pide y el pedido aún no ha sido despachado.
4. Es cliente nuevo y el ticket es bajo: discutir cuesta más que reembolsar.
5. Hubo dos promesas rotas.

El reembolso rápido es más barato que el contracargo: el contracargo te cuesta el dinero **más** la
penalización de la pasarela y el daño a tu ratio. Ver `192`.

## El sistema que detecta antes del cliente

| Alerta | Acción automática |
|---|---|
| Sin recolección > 24 h | Reclamo a la paquetería |
| Sin movimiento > 48-72 h | Mensaje nivel 1 al cliente |
| Intento fallido | Mensaje con opción de reprogramar |
| Fecha prometida vencida | Mensaje nivel 2 |
| Sin movimiento > 7 días | Escalado a humano, nivel 3 |

Esto se automatiza con el bot que ya tienes (`162`), respetando la ventana de 24 h de WhatsApp.

## Relacionados
`156` tracking · `157` comunicar la entrega · `162` bot propio · `164` devoluciones ·
`165` paquetes perdidos · `169` temporada alta · `174` tablero

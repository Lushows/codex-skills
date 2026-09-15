# Tracking y visibilidad del envío

> El tracking no es un servicio al cliente: es un **instrumento financiero**. Cada mensaje de "¿dónde
> está mi pedido?" cuesta tiempo de atención, y cada cliente que no sabe dónde está su paquete es un
> candidato a contracargo, a rechazo en la puerta y a reseña de una estrella.

## Los dos trackings

| | **Externo** (para el cliente) | **Interno** (para ti) |
|---|---|---|
| Qué muestra | Estado simple, fecha estimada | Estado crudo, tiempos por etapa, excepciones |
| Quién lo lee | El comprador | Tú y el tablero (`174`) |
| Objetivo | Tranquilizar y confirmar | Detectar el problema antes que el cliente |
| Frecuencia | Eventos clave | Barrido diario |

Los dos son obligatorios. El que solo tiene el externo se entera de los problemas por WhatsApp del
cliente, que es tarde y caro.

## Los eventos que sí importan

| Evento | Mensaje al cliente | Por qué |
|---|---|---|
| Pedido confirmado | Sí, inmediato | Reduce ansiedad post-pago |
| Pedido empacado / en preparación | Sí | Prueba de movimiento |
| **Despachado + número de guía** | **Sí, el más importante** | Es el que corta el 60% de las consultas |
| En ruta de entrega hoy | Sí | Sube la tasa de entrega: el cliente se queda |
| Intento fallido | **Sí, con acción concreta** | Ver `171` |
| Entregado | Sí, + pedir reseña | Cierra el ciclo |
| Sin movimiento > X días | **Alerta interna, no al cliente todavía** | Tú actúas antes |

## La cadencia mínima

```
Día 0   Compra   →  "Recibimos tu pedido. Lo preparamos hoy."
Día 0-1 Despacho →  "Va en camino. Guía XXXX. Llega entre el D y el D+n."
Día n-1 En ruta  →  "Tu pedido sale hoy a entrega. Ten el teléfono a la mano."
Día n   Entrega  →  "Entregado. Cuéntanos cómo te fue." + reseña
```

Cuatro mensajes. Ni uno más en operación normal. El quinto es ruido y te reportan.

## Las alertas internas: el barrido diario

| Condición | Umbral típico | Acción |
|---|---|---|
| Sin evento de recolección | > 24 h desde que generaste la guía | La paquetería no lo recogió. Reclama hoy |
| Sin movimiento en tránsito | > 48-72 h | Abre caso con guía y fecha |
| Intento fallido | 1 intento | Contacta al cliente **ese día** (`171`) |
| Dos intentos fallidos | 2 | Llamada, no mensaje. Si no contesta, reprograma |
| En destino sin entregar | > 4 días | Riesgo de devolución automática |
| Sin actualización total | > 7-10 días | Probable extravío. Ver `165` |

Esto se puede hacer con una hoja de cálculo y 15 minutos al día hasta los ~200 pedidos/mes. No
necesitas software para empezar; necesitas **hacerlo todos los días**.

## Página de seguimiento propia vs link de la paquetería

| | Link de la paquetería | Página propia |
|---|---|---|
| Costo | Cero | Bajo, requiere integración |
| El cliente sale de tu marca | Sí | No |
| Oportunidad de vender más | Ninguna | Sí (cross-sell suave) |
| Estados confusos | Muestra códigos internos | Traduces a lenguaje humano |
| Cuándo | Al arrancar | Cuando pases de ~300 pedidos/mes |

Al arrancar: link de la paquetería, pero **acompañado de un mensaje tuyo que explique qué significa
el estado**. "En centro de distribución" no le dice nada a nadie.

## Traducir los estados

| Lo que dice la paquetería | Lo que el cliente necesita leer |
|---|---|
| En tránsito / En centro de distribución | "Ya salió de nuestra bodega y va en camino" |
| En proceso de entrega | "Hoy sale a tu dirección. Ten el teléfono disponible" |
| Visita fallida / Cliente ausente | "El repartidor no te encontró. Responde este mensaje y lo reprogramamos para mañana" |
| Devuelto a origen | "Regresó a bodega. ¿Lo reenviamos o prefieres reembolso?" |
| Entregado | "Llegó. Cualquier cosa, respóndenos aquí" |

## El tracking y el fraude

En prepago, la guía con entrega confirmada es tu **prueba contra un contracargo**. Guarda:

1. Número de guía y captura del estado "entregado" con fecha y hora.
2. Nombre de quien recibió, si la paquetería lo captura.
3. Dirección de entrega igual a la de facturación.
4. IP y correo del pedido.
5. Conversación con el cliente.

Sin eso, el contracargo se pierde casi siempre. Ver `172` y `192`.

## Errores que salen caros

| Error | Costo |
|---|---|
| Generar la guía y no despachar el mismo día | El tracking dice "creada" y el cliente cree que le mentiste |
| Mandar el número de guía días después | 60% de las consultas evitables se vuelven mensajes |
| No avisar del intento fallido | El paquete se devuelve solo y pagas ida y vuelta |
| Prometer fecha exacta en vez de rango | Un día de retraso = cliente furioso |
| Callarse cuando hay un problema | El cliente se entera igual, pero ahora desconfía |
| No mirar el tracking hasta que reclaman | Pierdes la ventana de reclamación de la paquetería (`165`) |

## Qué automatizar primero

1. Mensaje de despacho con guía — **automático, el mismo día**. Ver `162`.
2. Alerta interna de "sin movimiento > 48 h".
3. Mensaje de intento fallido con opción de reprogramar.
4. Solicitud de reseña 2 días después de entregado.

Todo lo demás puede esperar.

## Relacionados
`157` comunicar la entrega · `159` tasa de entrega · `162` bot propio para confirmar · `165`
paquetes perdidos · `171` cuando el envío se atrasa · `172` fraude · `174` tablero logístico

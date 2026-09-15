# Reusar un bot propio para confirmar

> Si ya tienes construido un bot de WhatsApp con IA —y en este proyecto **lo tienes**: el agente
> que atiende clientes por WhatsApp Cloud API con Claude, con su panel, su memoria de cliente y su
> aviso al operador— no contrates una plataforma de confirmación. El 80% del trabajo ya está hecho.
> Lo que falta es conectarlo al pedido.

## Qué ya está resuelto y qué falta

| Pieza | ¿Existe en tu bot? | Qué falta |
|---|---|---|
| Conexión a WhatsApp (Cloud API) | ✅ | Nada |
| Motor de conversación con IA | ✅ | Prompt específico de confirmación |
| Memoria por cliente | ✅ | Guardar estado del pedido |
| Panel para ver conversaciones | ✅ | Columna de estado de confirmación |
| Aviso al operador | ✅ | Disparo cuando hay que escalar |
| Pausar la IA y tomar el control | ✅ | Nada |
| **Disparo automático al crear un pedido** | ❌ | **Construirlo** |
| **Máquina de estados del pedido** | ❌ | **Construirlo** |
| Reintentos programados | ❌ | Un cron |
| Registro del motivo del "no" | ❌ | Un campo |

Trabajo real: días, no meses. Y a costo marginal, porque la infraestructura ya está pagada.

## La máquina de estados mínima

```
PEDIDO_NUEVO
   → CONFIRMANDO      (se envió mensaje 1)
       → CONFIRMADO   → LISTO_PARA_DESPACHO
       → RECHAZADO    → CERRADO (con motivo)
       → DATO_CORREGIDO → vuelve a CONFIRMANDO
       → SIN_RESPUESTA_1 → (3-4 h) mensaje 2
            → SIN_RESPUESTA_2 → (día siguiente) mensaje 3
                 → NO_DESPACHAR  ← el estado que te ahorra el flete doble
```

Cada transición se guarda con fecha y hora. Sin eso no puedes medir nada de `174`.

## La trampa que te va a morder: la ventana de 24 horas

WhatsApp Cloud API solo deja enviar mensajes libres dentro de **24 horas desde el último mensaje
del cliente**. Fuera de esa ventana **Meta responde 200 OK pero no entrega nada** (error de
entrega 131047). Es la trampa más cruel de la plataforma: tu sistema registra "enviado", tu tablero
dice que confirmaste, y el cliente nunca recibió nada.

| Situación | ¿Entrega? | Qué hacer |
|---|---|---|
| El cliente te escribió primero (vino de un anuncio Click-to-WhatsApp) | ✅ 24 h de ventana | Mensaje libre |
| El cliente compró en la web y nunca te escribió | ❌ | **Plantilla aprobada por Meta** |
| Mensaje 2, a las 4 h, sin respuesta del cliente | Depende de cuándo escribió él | Verificar ventana antes de enviar |
| Mensaje 3, al día siguiente | ❌ casi seguro | **Plantilla** |

**Implementación obligatoria:** una función guardia que, antes de cada envío, pregunte si la
ventana está abierta; si está cerrada, que use plantilla o registre el intento como no entregable.
Y un endpoint que liste los errores de entrega, para que no te enteres por casualidad.

## Plantillas que necesitas aprobadas en Meta

| Plantilla | Uso | Notas |
|---|---|---|
| Confirmación de pedido | Abrir conversación con quien compró en la web | Con variables: nombre, producto, monto |
| Recordatorio de confirmación | Mensaje 2 y 3 | Que ofrezca responder SÍ/NO |
| Despacho con guía | Avisar el envío | Ver `156` |
| Aviso de intento fallido | Reprogramar | Ver `171` |

Pide la aprobación **con dos semanas de anticipación**. En temporada alta los tiempos de revisión
se alargan y quedarte sin plantilla en diciembre es quedarte sin operación.

## El prompt del bot en modo confirmación

El prompt de venta y el prompt de confirmación son distintos y no deben mezclarse. Un bot en "modo
soporte" que tiene prohibido cerrar puede sabotear una confirmación en curso — es un error que ya
costó caro en otro proyecto.

El prompt de confirmación debe:

1. Tener el guion de `160` como estructura, no como texto rígido.
2. Conocer el pedido: producto, monto exacto, dirección, fecha estimada.
3. Tener permiso explícito de **cerrar**: confirmar y dar por despachado.
4. Manejar las cinco objeciones de `160` sin bajar el precio.
5. Escalar al operador si: el cliente se enoja, pide algo fuera de catálogo, o insiste en negociar.
6. Devolver un **resultado estructurado**: `confirmado | rechazado | corregido | sin_respuesta` +
   motivo. Si el bot no devuelve un dato estructurado, no sirve para operar.

## Costo

Cada conversación de confirmación son pocos turnos. Lo que dispara el costo es el prompt de sistema
grande repetido. Dos reglas:

1. **Caché del prompt de sistema** (TTL 5 min o 1 h). Baja el costo mucho cuando confirmas en lote.
2. **No achiques el prompt** a costa de que el bot confirme mal: un fallido cuesta más que mil
   tokens.

Para afinar esto, invoca `optimizer_tokens_lushows`.

## Separación de canales: la línea que no se cruza

| Canal | Para qué |
|---|---|
| **WhatsApp** | Negocio: cliente, confirmación, despacho, aprobaciones del operador |
| **Telegram u otro** | Alarmas de infraestructura: "el bot se cayó", "hay 12 pedidos sin confirmar" — **sin datos de cliente** |

Mezclar los dos termina en datos de clientes en un canal de alertas. No lo hagas.

## Checklist de implementación

1. Webhook o job que detecte pedido nuevo y dispare el estado `CONFIRMANDO`.
2. Guardia de ventana de 24 h antes de **cada** envío.
3. Plantillas aprobadas para los envíos fuera de ventana.
4. Cron a las 3-4 h y al día siguiente para los mensajes 2 y 3.
5. Estado del pedido visible en el panel, filtrable.
6. Botón de "tomar el control" que pause la IA en esa conversación.
7. Barrido diario de pedidos atascados en `CONFIRMANDO` más de 24 h.
8. Endpoint de errores de entrega, revisado a diario.
9. Registro de motivo de rechazo para alimentar el anuncio y el producto.

## Cuándo NO conviene reusar tu bot

- Si el volumen es de 5 pedidos al día: confirma tú a mano. Automatizar cuesta más que el problema.
- Si tu bot está inestable en producción: una confirmación que falla en silencio es peor que no
  confirmar.
- Si la operación es prepago puro sin necesidad de confirmar (el caso de diciembre 2026): entonces
  el bot sirve para **posventa y tracking**, no para confirmar.

## Relacionados
`160` guion de confirmación · `161` voz con IA · `156` tracking · `159` tasa de entrega ·
`171` cuando se atrasa · `174` tablero · invoca `optimizer_tokens_lushows`

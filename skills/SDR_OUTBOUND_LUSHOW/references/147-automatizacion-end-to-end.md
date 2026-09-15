# 147 — Automatización end-to-end

`34` te enseñó a automatizar costuras sueltas (los cinco flujos de mayor retorno) y `146` te dio el diseño de quién es dueño de cada dato. Este módulo une todo: **la tubería completa que lleva un lead de la lista → la secuencia → el CRM → el handoff al vendedor sin que una mano humana lo mueva.** La meta no es automatizar tareas aisladas, es que **el dato viaje solo de punta a punta** y el humano solo aparezca donde aporta juicio (escribir el mensaje de venta, decidir en la reunión). Cuando la tubería está bien armada, tú prospectas y conversas; el sistema hace la logística.

## El principio: automatiza el movimiento del dato, no el juicio

La línea que nunca cruzas: **automatiza mover, registrar y avisar; deja que el humano decida y convenza.** Un webhook puede crear un Deal y mandar un aviso en 2 segundos; no debe redactar la respuesta de venta ni calificar a fondo (eso es criterio humano, `ventas_lushows`). Automatizar de más —respuestas de venta robotizadas, calificación por reglas ciegas— produce la sensación de spam que mata el outbound. La tubería mueve datos a la velocidad de la máquina; la conversación la lleva la persona a velocidad humana.

## La tubería completa (los seis tramos)

```
① SOURCING            Apollo/Maps → export → Clay
   (25, 21)                                    │
                                               ▼
② ENRIQUECER+VERIFICAR  Clay enriquece, NeverBounce verifica, se calcula score
   (31, 28, 38)          → solo pasa lo verificado y tier A/B                │
                                                                            ▼
③ A LA SECUENCIA       Clay (nativo) empuja al sequencer solo los limpios
   (33, 146)             → Instantly/Smartlead arranca la cadencia (60)     │
                                                                            ▼
④ EVENTO: RESPUESTA    Sequencer detecta reply → webhook clasifica          │
   (34, 64)             positivo / objeción / baja / no interesado          │
                        ├─ positivo → sigue a ⑤                              │
                        ├─ baja/no  → CRM lead_status = nurture/descartado (76, 77)
                        └─ objeción → avisa al humano (68)                   │
                                                                            ▼
⑤ AL CRM + SCORING     crea/actualiza Contact+Account, crea Deal (SQL),     │
   (141, 143)          sella sql_source, sincroniza estado (148)            │
                                                                            ▼
⑥ ROUTING + HANDOFF    round-robin asigna owner (142) → notifica en <60s    │
   (142, 73)           → contexto del lead al AE → reunión en Calendly →    │
                        Deal actualizado → el humano entra a conversar
```

Cada flecha es un flujo automatizado (nativo o vía Make/n8n). El **único punto donde entra la mano humana** es después de ⑥: el SDR/AE conversa. Todo lo anterior corre solo.

## Orquestación: el orden y las condiciones importan

Automatizar no es disparar acciones al azar; es una secuencia con condiciones. Reglas de orquestación:

- **Verifica antes de enviar (tramo ②→③).** Nunca empujes al sequencer un email sin verificar —un bounce daña la reputación del dominio (ver `40`). El verificador es un portón, no un adorno.
- **Clasifica antes de actuar (tramo ④).** Una respuesta no es un evento único: "quítame" ≠ "cuéntame más". Clasifica (con reglas o IA, ver `35`) y ramifica; nunca trates todas las respuestas igual.
- **Deduplica antes de crear (tramo ⑤).** Busca por dominio/email normalizado antes de crear Contact/Account, o llenas el CRM de duplicados (ver `146`, `148`).
- **Asigna y avisa junto (tramo ⑥).** Asignar sin notificar = lead dormido. El aviso instantáneo es parte del mismo paso.

## Resiliencia: qué pasa cuando un flujo falla

La automatización sin manejo de errores es peor que el trabajo manual, porque **falla en silencio** y no te enteras. Blíndala:

- **Reintentos.** Si un webhook falla (la herramienta destino estaba caída), que reintente con espera, no que se pierda.
- **Confirma antes de dar OK.** En serverless/webhooks, espera a que la acción **termine** antes de responder éxito. (Lección real: en entornos async mal manejados, responder OK antes de completar = eventos perdidos silenciosos. Aplica igual a AVISPA'O y a cualquier webhook.)
- **Log de lo que pasó.** Una tabla/hoja simple con qué se disparó y cuándo. Cuando "un lead desapareció", el log te dice en qué tramo se cayó.
- **Alerta de fallo.** Si un flujo crítico (respuesta→CRM) falla, que te avise a Slack/WhatsApp. Un flujo roto en silencio pierde leads durante días.
- **Idempotencia.** Que reprocesar el mismo evento no cree dos Deals ni mande dos avisos. (Otra lección real: sin idempotencia, un reintento duplica registros.)

## Ejemplo: pseudocódigo del tramo ④→⑤→⑥

```
ON webhook "reply" desde Smartlead:
   dedup_key = normalizar(email)                      # minúsculas, sin espacios
   IF ya_procesado(dedup_key + message_id): RETURN     # idempotencia

   categoria = clasificar(texto_respuesta)             # positivo/objeción/baja/no (35)

   MATCH categoria:
     "baja" | "no_interesado":
        CRM.set(lead_status = nurture|descartado, motivo)   # 76, 77
        RETURN
     "objeción":
        Slack.avisar(owner, "objeción de {nombre}: {texto}")  # humano decide (68)
     "positivo":
        contacto = CRM.buscar_o_crear(dedup_key)             # dedup (146)
        deal = CRM.crear_deal(sql_source="outbound-SDR", ...) # 141, 143
        owner = routing.round_robin(vertical, capacidad)      # 142
        deal.owner = owner
        Slack.avisar(owner, "🔥 {nombre} de {empresa} — contáctalo ya")

   log(dedup_key, categoria, resultado)                # rastro para depurar
   RETURN OK   # solo después de que todo lo anterior terminó
```

Los umbrales, pesos y la lógica de negocio (qué es "positivo", el cap de routing) son decisiones tuyas; que los números cuadren → `Matematicas_lushows`. Bajar el costo de la IA que clasifica respuestas → `optimizer_tokens_lushows`.

## Errores comunes

- **Automatizar el juicio de venta.** Respuestas robotizadas o calificación por reglas ciegas → se siente spam y quema leads.
- **Enviar sin verificar** → bounces que dañan el dominio (tramo ② saltado).
- **Sin idempotencia ni dedup** → Deals y avisos duplicados en cada reintento.
- **Fallos silenciosos.** Sin log ni alerta, un flujo roto pierde leads días sin que nadie lo note.
- **Automatizar 15 flujos de golpe.** Empieza por la columna vertebral (④→⑤→⑥) y estabilízala antes de añadir adornos (heredado de `34`).

## La frontera

La tubería **mueve y registra**; en el instante en que aparece el humano (post-⑥), empieza el oficio de venta: respuestas y objeciones tempranas → `64`, `68`; discovery → `71`; handoff con contexto → `73`; cierre → `ventas_lushows`. El diseño de quién es dueño de cada dato → `146`; la sincronía bidireccional que sostiene el tramo ⑤ → `148`; las herramientas de pegamento a fondo → `107`, y la IA dentro de los flujos → `35`.

## Siguiente paso

Dibuja tu tubería sobre los seis tramos con tus herramientas reales y monta primero la columna vertebral ④→⑤→⑥ (respuesta → CRM → routing/aviso), con dedup, idempotencia y log desde el día 1. Estabilízala una semana, luego añade ①②③ hacia atrás. Sincronía de estados → `148`; que la mano humana entre limpia → `73` y `ventas_lushows`.

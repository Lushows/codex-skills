# 54 — Del clic al cierre en chat: el handoff tráfico → conversación

Entre el clic en el ad y la venta hay un terreno que el media buyer SÍ controla: los primeros segundos de la conversación. Lee este módulo si pautas CTWA (ver 50) o lead forms con botón a WhatsApp (ver 52). Importante: el OFICIO completo de la conversación de venta (descubrir, recomendar, manejar objeciones, cerrar) es **ventas_lushows 82** — no lo improvisa el ads manager. Aquí está el handoff: que el lead llegue caliente, con contexto, medido y atendido. Jerga: "handoff" = entrega del lead del ad a la conversación; "message match" = que el saludo refleje la promesa del ad.

## Congruencia ad → primera respuesta

El usuario clicó por UNA promesa específica. Si el saludo la ignora, se rompe el hilo y se enfría:

- Ad: "Combo Melena de León + Reishi 20% off" → Saludo correcto: "¡Hola! Vi que te interesa el combo Melena + Reishi con 20% off 🙌 ¿Te cuento las presentaciones?" → Saludo que mata: "Hola, bienvenido a nuestra tienda, ¿en qué podemos ayudarte?"
- Cómo se configura: **mensaje pre-llenado distinto por campaña** ("Hola, vi el anuncio del combo X") + el bot lee ese texto o el `referral` del ad (ver 53) y abre con el contexto correcto. En la app Business: respuestas rápidas por campaña y leer el banner de origen del ad.
- Regla: cada campaña con oferta distinta = saludo distinto. Es la versión chat del "message match" de las landings.

### Plantillas de saludo congruente por tipo de ad

| Tipo de ad | Saludo congruente |
|---|---|
| Oferta con descuento | "¡Hola! Vi que te interesa [producto] con [X]% off 🙌 ¿Te cuento las presentaciones?" |
| Producto específico | "¡Hola! Te muestro [producto] — ¿lo quieres para [uso A] o [uso B]?" |
| Prueba/valoración | "¡Hola! Agendemos tu [valoración/visita] gratis. ¿En qué zona estás?" |
| Catálogo / "ver más" | "¡Hola! Te paso el catálogo 👇 dime cuál te late y te cotizo con envío" |

## Tiempos de respuesta

- **<5 minutos** o el lead se enfría (misma regla 21× de los lead forms, ver 52). En WhatsApp la expectativa es aún más agresiva: minutos, no horas.
- Un **bot 24/7 responde el 100% al instante** — esa es tu ventaja estructural sobre el competidor que contesta "mañana le digo". Además explota la ventana gratis de 72h del CTWA (ver 50).
- Si es humano: notificaciones activas, turnos definidos, y NO pautar en horarios sin cobertura (programación de pauta: ver 18/57).

> 2026: el **Meta Business Agent** (bot de IA de Meta, 3-jun-2026, ver `actualizacion-2026-06` §4) responde al instante de fábrica. Si compites contra negocios que lo activan, tu ventaja ya no es "tengo bot" sino la **congruencia del saludo, el guion de cierre y la medición CAPI** — cosas que el bot genérico de Meta no afina por ti.

## Etiquetado desde el primer mensaje

Cada conversación entra etiquetada y avanza de etiqueta:

```
Nuevo → Interesado → Pedido (dio datos) → Cliente | No calificado
```

- Alimenta dos cosas: la **medición** del embudo (ver 53) y el **remarketing** — la lista de "Interesado que no compró" es tu mejor audiencia personalizada para la próxima campaña (ver 21/23).
- Si hay bot: que etiquete automático por estado de la conversación. Si es manual: disciplina diaria, sin excepciones.

## Calificación temprana sin interrogatorio

2 preguntas máximo antes de aportar valor, integradas natural:

1. **Ciudad** ("¿A qué ciudad te lo enviaríamos?") — define envío/contraentrega y descalifica fuera de cobertura.
2. **Qué busca / para qué** ("¿Lo quieres para memoria/concentración o para energía?") — permite recomendar y revela intención.

Todo lo demás (presupuesto, urgencia) sale en el flujo de la venta, no en un formulario disfrazado de chat. Cinco preguntas seguidas sin dar nada = abandono. Para high-ticket la pre-calificación sí es más dura y deliberada (ver 58).

## Cuándo escala el bot a humano

Triggers claros de handoff:

- Intención de compra explícita ("quiero pedir", "cómo pago") → humano o flujo de cierre + notificación al operador.
- Objeción compleja, queja, caso médico/legal, negociación de precio fuera de guion.
- El cliente lo pide ("¿me puede atender una persona?") — el bot nunca lo niega.
- 2 vueltas sin entender al cliente → escala, no insiste.

El humano entra LEYENDO el historial — nunca "¿en qué puedo ayudarte?" después de 10 mensajes.

## Specs del media buyer para quien construye el bot

Lo que TÚ le pides por escrito al que arma el bot (tuyo, agencia o dev — stack: ver 96). Esta es tu checklist de entrega:

1. **Contexto del ad en el saludo**: leer mensaje pre-llenado y/o `referral` y abrir según campaña.
2. **Guardar la fuente**: `ctwa_clid`, `source_id` y nombre de campaña en el perfil del contacto desde el mensaje 1 (ver 53). Sin esto la atribución muere para siempre.
3. **Etiquetas automáticas** por etapa, consultables/exportables.
4. **Eventos hacia fuera**: webhook o CAPI cuando alguien pasa a "Pedido" y a "Cliente", con valor de venta y `messaging_channel: "whatsapp"` (ver 53).
5. **Handoff a humano** con notificación (al WhatsApp del operador) y pausa del bot en ese chat.
6. Horario y tono: el bot responde 24/7; define qué promete fuera de horario humano ("te confirmo el envío a primera hora").

### Mini-flujo de chat de referencia (ticket bajo)

```
Bot: ¡Hola! Vi que te interesa el Combo X con 20% off 🙌 ¿A qué ciudad lo enviaríamos?
Cliente: Medellín
Bot: ¡Genial, allá llega en 1-2 días! ¿Lo quieres para [uso A] o [uso B]?
Cliente: Para energía
Bot: Perfecto, el Combo X es ideal. Queda en $X con envío. Pagas contraentrega o
     por Nequi 👍 ¿Te lo despacho?  → [etiqueta: Interesado]
Cliente: Sí, pásame los datos  → [etiqueta: Pedido] → dispara evento OrderCreated (ver 53)
```

> El número de WhatsApp queda guardado: tras la venta, alimenta recompra y remarketing (lista "Cliente" / "Interesado que no compró", ver 21/23). Cada conversación es un activo, no un gasto de un solo uso.

## Errores comunes — blacklist

- Saludo genérico corporativo tras un ad de oferta específica: rompes el message match y la tasa de respuesta cae a la mitad.
- Bot que interroga (5 preguntas antes de dar precio): el cliente vino a comprar, no a llenar un censo.
- No guardar la fuente del ad en el mensaje 1: la atribución muere ahí (ver 53).
- Humanos que entran sin leer el historial: cliente repite todo, confianza rota.
- El ads manager "mejorando" el guion de cierre por intuición: ese oficio tiene método — ventas_lushows 82.
- Pautar 24/7 con bot a medio construir "para ir probando": cada conversación mal atendida es plata gastada Y un cliente quemado para remarketing.
- Bot que niega el humano cuando el cliente lo pide: mata la confianza justo en el momento de comprar.

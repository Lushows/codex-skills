# 34 — Integraciones y automatización

Tu stack de outbound son varias herramientas (datos, Clay, sequencer, CRM, señales). Cada una es una isla. Las **integraciones** son los puentes que hacen que un dato viaje solo de una a otra: cuando alguien responde en Smartlead, que se marque en HubSpot; cuando entra un lead nuevo, que Clay lo enriquezca y lo empuje al sequencer. Sin puentes, un humano copia y pega entre herramientas todo el día —y ese humano se equivoca y se cansa. Este módulo es cómo pegar el stack con Zapier/Make/n8n y webhooks. La automatización end-to-end profunda vive en `147`; n8n/Make a fondo en `107`.

## El principio: el dato debe fluir sin manos

El outbound se rompe en las **costuras** entre herramientas. Cada copy-paste manual es un punto donde se pierde un lead, se duplica un contacto o se contacta a alguien que ya respondió. La meta es que los eventos disparen acciones automáticamente: **evento → regla → acción**, sin que nadie mire. Eso se llama automatización basada en eventos, y sus dos piezas son el **trigger** (el evento que dispara) y el **webhook/acción** (lo que pasa después).

Un **webhook** es simplemente un aviso automático que una herramienta envía a otra cuando pasa algo ("oye, este lead respondió") vía una URL. Es el mecanismo más directo y confiable para conectar herramientas.

## Las tres herramientas de pegamento

| Herramienta | Qué es | Fuerte en | Débil en | Precio aprox |
|---|---|---|---|---|
| **Zapier** | Conector no-code, el más popular | Miles de apps, facilísimo, plantillas | Caro al escalar (cobra por tarea) | Free → ~$20–70+/mes |
| **Make** (ex-Integromat) | Conector visual con flujos complejos | Más barato por operación, lógica visual potente | Curva un poco mayor | Free → ~$9–34+/mes |
| **n8n** | Open-source, self-host o cloud | Barato/gratis self-host, control total, código cuando hace falta | Requiere algo más técnico | self-host gratis / cloud ~$20+ |

Regla práctica: **Zapier** para empezar y flujos simples; **Make** cuando el volumen encarece Zapier o necesitas lógica ramificada; **n8n** cuando quieres control total y bajar costos self-hosteando (ideal si tienes algo de perfil técnico). Detalle en `107`.

Ojo: muchas integraciones **ya son nativas** —Clay escribe directo a Instantly/HubSpot, HubSpot habla con Smartlead— y no necesitan Zapier. Usa el pegamento solo donde no haya conector nativo.

## Los flujos que sí valen la pena automatizar

No automatices por deporte; automatiza las costuras que sangran. Los cinco flujos de mayor retorno:

1. **Lead nuevo → enriquecer → CRM.** Entra un contacto (de un formulario, una señal, una lista) → webhook a Clay → Clay enriquece y verifica → escribe en el CRM ya limpio y puntuado (ver `31`, `38`).
2. **Respuesta positiva → crear Deal + avisar.** El sequencer detecta respuesta → webhook → crea Deal en CRM + notifica al SDR/AE en Slack/WhatsApp. El humano actúa rápido (velocidad de respuesta = más reuniones).
3. **Sincronía de estados sequencer ↔ CRM.** Respondió / se dio de baja / rebotó en Instantly → se refleja en el `lead_status` del CRM (ver `32`). Evita el desastre de re-contactar a quien ya respondió.
4. **Señal detectada → a la cola de outbound.** Cambió de cargo / la empresa levantó ronda → webhook → mete al contacto en una campaña específica de señal (ver `37`, `128`).
5. **Reunión agendada → handoff.** Se agenda en Calendly → crea/actualiza Deal + asigna owner AE + manda contexto (ver `73`).

## Ejemplo: el flujo #2 paso a paso

"Cuando alguien responde positivo en Smartlead, crear Deal en HubSpot y avisar por Slack."

```
TRIGGER  (Smartlead → webhook)
   Evento: "positive reply" en campaña X
   Envía: {email, nombre, empresa, texto_respuesta}
      │
      ▼
FILTRO (en Make/Zapier)
   ¿la categoría de respuesta = "interesado"?  → sigue
   (si es "no interesado" → otra rama: marca nurture, ver 76)
      │
      ▼
ACCIÓN 1 (HubSpot)
   Buscar contacto por email → si existe, update; si no, create
   Crear Deal: etapa "Reunión por agendar", owner = SDR, sql_source = outbound
      │
      ▼
ACCIÓN 2 (Slack / WhatsApp)
   Mensaje: "🔥 Respuesta positiva de {nombre} ({empresa}).
            Respondió: '{texto_respuesta}'. Contáctalo ya."
```
El SDR ve el aviso en segundos y entra a **conversar** —y esa conversación (calificar, manejar objeción, agendar) escala hacia el oficio de venta: `ventas_lushows` para el cierre, `64`/`68` para las respuestas tempranas.

## Buenas prácticas al pegar el stack

- **Empieza con 2–3 flujos, no 15.** Automatiza primero las costuras que más duelen (respuestas y estados).
- **Deduplica en el puente, no después.** Antes de crear un contacto, busca por email/dominio. Duplicar es el pecado clásico (ver `32`, `139`).
- **Maneja los errores.** Si un webhook falla, que reintente o avise; no que se pierda en silencio. En serverless/webhooks, siempre confirma que la acción terminó antes de responder OK (lección real: async mal manejado = eventos perdidos).
- **Registra qué pasó.** Un log simple (una hoja o una tabla) de qué se disparó ayuda a depurar cuando "un lead desapareció".
- **No sobre-automatices el juicio humano.** Automatiza el movimiento de datos; deja que la persona decida el mensaje de venta.

## Errores comunes

- **Automatizar sin deduplicar** → CRM lleno de contactos repetidos.
- **Zapier para todo** cuando Make/n8n haría lo mismo por 1/5 del costo a volumen.
- **Reconstruir con Zapier lo que ya es nativo** (Clay→Instantly no necesita puente).
- **Flujos que re-contactan a quien respondió** por no sincronizar estados (flujo #3 ausente).

## Siguiente paso

Lista tus herramientas y dibuja las costuras entre ellas (¿dónde copias y pegas hoy?). Automatiza primero el flujo #3 (sincronía de estados) y el #2 (respuesta → aviso). Para el sistema entero de punta a punta → `147` y el mapa completo → `39`. Para IA dentro de estos flujos (enriquecer/redactar) → `35`, y bajar su costo → `optimizer_tokens_lushows`.

# 52 — Lead form extensions

Lee este módulo cuando quieres capturar datos del cliente **sin obligarlo a salir del anuncio ni esperar a que tu landing cargue** — útil cuando no tienes una buena página de cierre todavía, cuando el cliente está en móvil con mala conexión, o cuando vendes servicios/B2B donde el primer paso es "déjame tus datos y te contacto". Aquí Google captura el lead dentro del propio anuncio; tu trabajo es **filtrar** quién entra y **contactarlo en minutos**, porque un lead frío en una hora no vale casi nada (ver 54).

## Qué es y cómo funciona

**Lead form extension** (extensión/asset de formulario de clientes potenciales) es un formulario que se abre **dentro de Google**, sin ir a tu web. La persona toca el anuncio, ve un formulario con sus datos ya prellenados por Google (nombre, email, teléfono — los que tiene de su cuenta), confirma y listo. Menos fricción = más leads. Disponible en **Search, YouTube, Demand Gen y Display**.

Setup en la cuenta: Ads → **Activos → Formulario para clientes potenciales** → eliges titular, descripción del negocio, las **preguntas**, el mensaje de la pantalla final con un botón ("Escríbenos por WhatsApp" o "Ver más") y enlazas tu **política de privacidad**. Lo asocias a la campaña de Search o de video.

El problema que esa misma facilidad crea: **es TAN fácil que entra cualquiera**, incluso quien tocó por curiosidad o por error. Por eso un lead form sin diseño de filtros se llena de basura — números falsos, gente sin presupuesto, fuera de zona. La clave no es recoger más leads, es recoger los **correctos** (ver 58 high-ticket para el caso extremo de fricción intencional).

## Campos que filtran, no que solo llenan

Google deja agregar **preguntas calificadoras** al formulario. Úsalas como filtro, no como decoración:

| Tipo de pregunta | Para qué sirve | Ejemplo (gastronomía/servicios) |
|---|---|---|
| Presupuesto / rango | Saca a quien no puede pagar | "¿Cuánto inviertes hoy en control de costos?" |
| Tipo de negocio | Confirma que es tu cliente | "¿Restaurante, cafetería o dark kitchen?" |
| Urgencia / cuándo | Prioriza al que compra ya | "¿Cuándo necesitas resolverlo?" |
| Ubicación | Filtra fuera de zona | "¿En qué ciudad estás?" |
| Rol / decisor | Saca al que no decide | "¿Eres tú quien decide la compra?" |

Dos perillas más que mueven calidad:
- **Tipo de formulario "más calificado" vs "más volumen":** Google deja elegir. "Más calificado" pide una confirmación extra (un toque más) y entran menos pero mejores; "más volumen" entra todo el mundo. Para servicios/high-ticket, elige **calificado**.
- **Mensaje de la pantalla final:** dile al lead el siguiente paso real ("te escribimos por WhatsApp en menos de 10 minutos") y pon un botón que lo lleve directo a tu WhatsApp. Esto fija la expectativa, reduce el "¿quién me escribe?" y a veces el propio lead te escribe primero.

Regla honesta: cada campo extra **baja el volumen** de leads pero **sube la calidad**. Con presupuesto chico, prefieres 10 leads buenos que 50 basura que te queman el día persiguiendo gente que nunca iba a comprar (ver ventas_lushows 82). Empieza con 1-3 preguntas que de verdad filtren; no pidas 8 campos "para completar el perfil".

Plantilla concreta para este proyecto (calculadora gastronómica, $10.000):

```
Titular:      Controla tus costos y deja de perder plata cada mes
Descripción:  Calculadora en Excel para restaurantes, cafés y dark kitchens
Pregunta 1:   ¿Qué tipo de negocio tienes?  [Restaurante / Café / Dark kitchen / Otro]
Pregunta 2:   ¿En qué ciudad estás?         [texto corto]
Pantalla final: "Te escribimos por WhatsApp en menos de 10 minutos con el acceso"
Botón final:  [Escríbenos por WhatsApp →]  (link a wa.me/57...)
Tipo:         Más calificado
```

Para un servicio B2B/high-ticket la plantilla cambia: agrega "¿Cuál es tu presupuesto?" con rangos y "¿Eres tú quien decide la compra?" — preguntas que espantan al curioso (ver 58). Para producto barato de volumen, menos preguntas y tipo "más volumen". Ajusta el número de campos a tu ticket: a mayor precio, más filtro.

## Integración: que el lead llegue a tu mano en segundos

Un lead capturado que nadie ve durante horas está muerto. **La velocidad de contacto es la variable #1 del cierre**: contactar en los primeros 5 minutos multiplica la tasa de conversión frente a contactar una hora después (ver 54). Por eso el formulario tiene que **salir de Google y llegar a ti automáticamente**:

1. **Webhook (lo mejor):** Google envía cada lead en tiempo real a una URL (tu CRM, una hoja, un bot de WhatsApp). Apenas envían, te llega y disparas el mensaje. Esto lo conecta tu dev → engineer_visualopen_lushows (webhook + WhatsApp). En este proyecto, el bot ya recibe y responde por WhatsApp: un webhook que cree el contacto en `customerMemory` y arranque la conversación es la jugada exacta — el lead recibe respuesta en segundos.
2. **Conectores (Zapier/Make):** intermedio, sin código, pero suman segundos/minutos de retraso. Sirven para empezar mientras montas el webhook.
3. **Descarga manual (lo malo):** bajar un CSV desde la cuenta cada cierto rato. Suficiente para volumen muy bajo, fatal para velocidad. El lead se enfría y te lo gana la competencia.

Lo crítico: **dispara el contacto al instante** (WhatsApp/llamada) y guarda el **gclid** del lead en tu sistema para luego subir la conversión real con OCI (ver 53, 96 stack-OCI). El webhook de Google ya entrega el gclid junto al lead — no lo botes. El cierre de esa conversación es oficio de ventas, no de Google → ventas_lushows 82.

## Verificación obligatoria (jun-2026)

Antes de prender el formulario, Google exige aceptar sus **términos de leads** y vincular un **enlace a tu política de privacidad** (este proyecto ya tiene `/privacy`). Sin política de privacidad publicada, Google **no deja activar** el lead form. Tenla lista y enlazada antes de empezar. Además, los leads en el panel de Ads **caducan a los ~30 días** si no los descargas/webhookeas — otra razón para automatizar la salida.

## Errores comunes — blacklist

1. **Formulario sin preguntas calificadoras.** Se llena de curiosos. Agrega 1–3 filtros (presupuesto, tipo, ciudad) o gastarás el día persiguiendo basura.
2. **No conectar webhook y bajar leads "cuando me acuerde".** Contactar en 5 minutos vs 1 hora cambia el cierre por completo. Automatiza la salida a WhatsApp/CRM (engineer_visualopen_lushows).
3. **No fijar la expectativa en la pantalla final.** Si el lead no sabe quién ni cuándo lo contactan, desconfía y no contesta. Dile el siguiente paso exacto y pon botón a WhatsApp.
4. **Elegir "más volumen" cuando vendes high-ticket.** Más leads malos no es ganar. Usa "más calificado" y preguntas duras (ver 58).
5. **No medir el cierre, solo los leads.** Un lead form que trae 100 leads y cierra 0 es un fracaso caro. Sube las conversiones reales con OCI (ver 53, 60 métricas).
6. **Olvidar la política de privacidad.** Sin el enlace, Google no activa el formulario. Tenla publicada (`/privacy`).
7. **Pedir demasiados campos por "completar el perfil".** Cada campo extra cuesta volumen; pide solo lo que filtra o lo que necesitas para el primer contacto. Lo demás se pregunta en el chat (ventas_lushows 82).

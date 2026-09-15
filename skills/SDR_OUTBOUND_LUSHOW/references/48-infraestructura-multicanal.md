# 48 — Infraestructura multicanal sin quemar cuentas

El outbound moderno es multicanal —email + LinkedIn + teléfono + WhatsApp entrelazados convierten mucho más que cualquier canal solo (ver `61`)— pero cada canal tiene su propia infraestructura, su propio límite y su propia forma de banearte. Este módulo es el mapa de esos límites: **cuánto puedes hacer por canal sin quemar la cuenta**, y cómo orquestar los cuatro sin que ninguno explote. La diferencia con `61` (el diseño de la cadencia: qué mensaje va en qué día) es que aquí hablamos de la **fontanería y los topes técnicos** de cada canal. Pasar estos límites no te da más resultados: te da cuentas suspendidas y números baneados, que es perder el activo entero.

## Por qué cada canal tiene su propio techo

Cada plataforma protege su ecosistema a su manera. Email castiga las quejas de spam y los bounces (ver `40`). LinkedIn castiga la automatización agresiva y el exceso de invitaciones. WhatsApp castiga que te bloqueen/reporten. El teléfono no te "banea" pero tiene límites humanos y regulatorios. **La regla común: cada canal quiere que te comportes como humano, no como máquina.** Si respetas eso, corres por años; si no, quemas cuentas más rápido de lo que las creas.

## Los límites por canal (2026)

| Canal | Límite seguro | Qué te quema | Cuenta/infra |
|---|---|---|---|
| **Email** | 30–50 correos/buzón/día (ver `44`) | Bounce >4%, spam >0.3% | Dominios+buzones secundarios (`41`), autenticados (`42`), calentados (`43`) |
| **LinkedIn** | ~15–25 invitaciones/día, ~50–80 mensajes/día | Automatización detectada, muchas invites ignoradas, reportes | 1 cuenta/persona; personal warm, Sales Navigator |
| **Teléfono (cold call)** | 40–80 llamadas/día por persona | Nada te "banea", pero regulación (no-call lists) y quemar leads | Números locales, software de marcación |
| **WhatsApp** | Decenas–cientos/día según quality tier (ver `47`) | Bloqueos/reportes, quality rating rojo | Número dedicado, API oficial + plantillas |

### Email
Ya cubierto en profundidad en el Bloque 4 (`40`–`46`). Resumen: nunca el dominio principal, ~40/buzón/día, rota entre buzones para escalar. El volumen se construye con más buzones, no con buzones más grandes (ver `44`).

### LinkedIn — el más frágil de automatizar
LinkedIn detecta bots y suspende cuentas con facilidad. Reglas de oro:
- **Invitaciones (connection requests):** máximo ~15–25/día (LinkedIn limitó las invites semanales a ~100–200). Personaliza; muchas invites ignoradas/rechazadas bajan tu "acceptance rate" y te marcan.
- **Mensajes:** ~50–80/día a conexiones existentes. Los **InMails** (mensajes pagados a no-conexiones) son limitados por tu plan de Sales Navigator.
- **Automatización:** herramientas como Expandi, Waalaxy, HeyReach imitan comportamiento humano (delays, horarios, límites). Aun así, LinkedIn prefiere que uses **una cuenta por persona real**, "calentada" (perfil completo, actividad orgánica). Nunca automatices una cuenta nueva y vacía.
- **Sales Navigator** es la infraestructura de búsqueda/datos de LinkedIn (ver `22`); no confundir la búsqueda (permitida, potente) con la automatización de envío (riesgosa).

### Teléfono
No hay baneo, pero sí regulación (registros "no llamar" en algunos países) y el costo de quemar el lead si llamas mal. Software: marcadores como Aircall, JustCall, Kixie (a veces integran WhatsApp y CRM). El *guion* de la llamada y el manejo de la conversación → `ventas_lushows`; aquí solo el volumen sano (~40–80 marcaciones/día/persona) y números locales para mejor contactabilidad.

### WhatsApp
Cubierto en `47`. Resumen: número dedicado, API oficial con plantillas para el primer toque, warmup del número, vigila el quality rating, mejor como 2º/3er toque que como frío puro.

## Cómo orquestar los cuatro sin quemar nada

La clave no es maximizar un canal, sino **repartir el peso**. Una cadencia multicanal bien montada usa poco de cada canal por prospecto, entrelazado, en vez de martillar uno solo:

```
Ejemplo de reparto por prospecto (14 días) — diseño detallado en 61:
  Día 1   Email 1        (buzón secundario)
  Día 2   LinkedIn: ver perfil + invitación personalizada
  Día 4   Email 2 (seguimiento)
  Día 6   LinkedIn: mensaje (si aceptó) o InMail
  Día 8   Llamada 1
  Día 10  WhatsApp (si mostró señal / hay base legal; ver 47, 49)
  Día 13  Email 3 (break-up)
```

Cada prospecto recibe ~3 correos, 2 toques de LinkedIn, 1 llamada, quizá 1 WhatsApp — **ninguna cuenta se sobrecarga**. Multiplica por tu lista y verifica que la suma diaria por canal quede bajo los límites de la tabla. Si tu meta de volumen empuja un canal sobre su tope, **agregas capacidad** (más buzones de email, otra cuenta de LinkedIn de otra persona del equipo, otro número de WhatsApp), no subes el límite del que tienes.

## La orquestación técnica

- **CRM / plataforma de secuencias como cerebro:** herramientas como Smartlead, Instantly (email-first), o Outreach/Salesloft/HubSpot/lemlist/Reply.io (multicanal) orquestan la cadencia y respetan límites por canal automáticamente. La plataforma decide qué toque toca hoy y por qué canal, sin que te pases de la raya.
- **Un dato, muchos canales:** el mismo prospecto de tu lista (ver `20`) se enriquece con correo, LinkedIn URL, teléfono y WhatsApp (datos; ver `23`), y la plataforma lo mueve por la secuencia.
- **Registro central:** todas las respuestas de todos los canales caen en un solo lugar para no contactar dos veces ni pisar una conversación abierta.

## Errores comunes (qué NO hacer)

- Tratar todos los canales con la lógica del email (volumen alto). LinkedIn y WhatsApp te banean con una fracción de ese volumen.
- Automatizar una cuenta de LinkedIn nueva/vacía o pasar de ~20 invites/día. Suspensión.
- Meter todo el volumen en un solo canal "porque funciona". Concentras riesgo; diversifica.
- Descoordinar canales: mandar email y WhatsApp el mismo minuto, o seguir una secuencia cuando el prospecto ya respondió en otro canal. Centraliza.
- Escalar subiendo límites en vez de sumar capacidad (más buzones/cuentas/números).

## Siguiente paso

Ya tienes los límites técnicos de cada canal; el **diseño de la cadencia** —qué mensaje, qué día, qué canal, por qué— está en `61` (Bloque 6). Antes de mandar por cualquier canal, asegúrate de la base legal y el opt-out en cada uno (ver `49`: CAN-SPAM, GDPR, Habeas Data). Para la infraestructura específica de WhatsApp, `47`; de email, `40`–`46`. Para la conversación y el cierre en cualquier canal → `ventas_lushows`.

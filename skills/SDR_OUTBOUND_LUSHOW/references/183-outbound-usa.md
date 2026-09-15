# 183 — Outbound en Estados Unidos

Estados Unidos es el mercado donde nació el outbound moderno y donde vive la mayoría de las herramientas, plantillas y benchmarks que usa esta skill. Si vendes desde LatAm hacia USA (ver `187`, el arbitraje de costos que hace esto tan atractivo) o le vendes a empresas gringas, este es tu manual. Todo cambia respecto a LatAm: **el correo es el rey, no WhatsApp**; el prospecto espera directness (ir al grano) no rapport lento; los datos son abundantes y baratos; el volumen es mayor; y la ley (CAN-SPAM) es la más permisiva de las tres jurisdicciones. Aquí sí aplica el playbook clásico —bien ejecutado.

## El principio: email-first, directo, a escala

En USA el decisor B2B vive en su bandeja de correo y en LinkedIn, no en WhatsApp (mandarle WhatsApp a un ejecutivo gringo sin relación es raro y contraproducente). La cultura de negocio premia la **claridad y la brevedad**: el prospecto te da 3 segundos, quiere saber quién eres, qué quieres y qué gano yo — sin rodeos ni rapport artificial. El halago largo y la construcción de relación lenta que funciona en LatAm, en USA se lee como pérdida de tiempo. Y como los datos son abundantes, el juego es de **relevancia a escala**: listas grandes bien segmentadas, deliverability impecable, personalización eficiente (ver `52`, `66`).

## Los canales, ordenados para USA

| Canal | Rol en USA |
|---|---|
| **Email** | Canal #1 del B2B. Todo el stack (Instantly, Smartlead, Apollo) está optimizado para esto (ver `33`, `50`) |
| **LinkedIn** | Segundo canal fuerte; conexión + mensaje, muy usado por decisores (ver `26`, `57`) |
| **Cold call** | Vivo y efectivo en muchos sectores; el opener y hook aquí, la venta → `ventas_lushows` (ver `58`) |
| **SMS/texto** | Usado en algunos verticales B2C y SMB, con reglas propias (TCPA) |
| **WhatsApp** | Marginal en B2B USA; no es el canal |

La secuencia clásica: email + LinkedIn + llamada entrelazados en una cadencia multicanal (ver `61`).

## Los datos: abundantes y baratos

Aquí USA es el paraíso opuesto a LatAm:

- **ZoomInfo, Apollo, Clearbit, Lusha, Cognism** tienen cobertura profunda de empresas y contactos gringos con emails y teléfonos directos verificados (ver `25`).
- **LinkedIn Sales Navigator** tiene su mayor densidad de datos aquí (ver `26`).
- **Intent data** (Bombora, 6sense, señales de compra) es un mercado maduro: sabes qué cuentas están investigando tu categoría (ver `36`, `37`).
- El costo por lead es bajo y la verificación (NeverBounce, ZeroBounce) es estándar y barata (ver `28`).

Esto invierte la estrategia: en LatAm el cuello de botella son los datos; en USA los datos sobran y el cuello de botella es **la deliverability y la relevancia** — sobresalir en una bandeja saturada.

## La ley: CAN-SPAM (la más permisiva)

La ley federal de correo comercial. Detalle en `49`; lo esencial:

- **No exige consentimiento previo** para el primer email B2B en frío. Esto es lo que hace a USA tan accesible al outbound.
- Sí exige: remitente y "From" verdaderos, asunto no engañoso, identificar que es comercial, una **dirección postal física** real en el correo, y un **opt-out funcional procesado en ≤10 días hábiles**.
- Sanción: hasta ~$53.000 USD por correo infractor.
- Ojo con reglas de canal: **SMS** cae bajo TCPA (más estricto, requiere consentimiento) y **llamadas** bajo listas Do-Not-Call. El email frío B2B es la vía limpia y establecida.

Además de la ley, en 2024+ Google y Yahoo endurecieron requisitos técnicos para remitentes masivos (SPF, DKIM, DMARC obligatorios, tasa de queja <0,3%): cumplir es hoy condición de entregar, no opcional (ver `42`, `45`).

## El estilo del mensaje: directo y con "what's in it for me"

- **Asunto corto y honesto** (2–4 palabras), que parezca de un humano no de marketing (ver `51`).
- **Primera línea sobre ellos, no sobre ti.** Nada de "Somos una empresa líder en…". Un observación relevante o un resultado.
- **Cuerpo de 50–90 palabras.** Un problema, una prueba, una pregunta. El gringo no lee párrafos.
- **CTA de bajo compromiso:** "¿Vale la pena una charla de 15 min?" o interest-based ("¿te mando más info?"), no "agenda aquí" agresivo (ver `55`).

## Ejemplo: cold email B2B (USA, SaaS)

```
Asunto: quick question, {Company}

Hi {Name},

Noticed {Company} just opened a second location in Austin —
congrats. Usually when restaurant groups hit multi-location,
food-cost tracking in spreadsheets starts breaking down.

We help groups your size see real per-plate margin without the
Excel headache — {similar client} cut waste 8% in a quarter.

Worth a quick 15-min look next week?

{Firma con dirección postal + línea de opt-out}
```

Directo, sobre ellos, prueba concreta, CTA suave, cumple CAN-SPAM (dirección + opt-out). La conversación de venta que siga → `ventas_lushows`.

## Errores comunes (qué NO hacer)

- Traer el rapport lento y el halago largo de LatAm: el gringo lo lee como relleno, cierra el correo.
- Mandar WhatsApp en frío a un ejecutivo USA: fuera de norma, contraproducente.
- Volumen sin deliverability: con datos abundantes es fácil sobre-enviar y quemar dominios (ver `43`, `44`, `119`).
- Ignorar los requisitos 2024+ de Google/Yahoo: sin SPF/DKIM/DMARC no entregas (ver `42`).
- Olvidar la dirección física y el opt-out: viola CAN-SPAM directo (ver `49`).

## Siguiente paso

Monta infraestructura de email a escala: dominios secundarios calentados (ver `41`, `43`), SPF/DKIM/DMARC (`42`), un sequencer como Instantly o Smartlead (`33`). Construye listas grandes y segmentadas con Apollo/ZoomInfo (`25`) verificadas (`28`), y escribe cold email directo estilo USA (`50`, `56`). Si vendes desde LatAm hacia USA, el arbitraje y la logística están en `187`; los husos horarios en `186`. La venta → `ventas_lushows`.

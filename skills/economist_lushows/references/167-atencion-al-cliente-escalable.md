# 167 — Atención al cliente escalable

Cómo dar soporte que crece sin que tus costos exploten ni la calidad se caiga: pasar de "yo respondo todo" a un sistema con autoservicio, prioridades claras y métricas. El soporte bien hecho no es un gasto: es retención y ventas repetidas (ver 89).

## La verdad incómoda primero
A más clientes, más preguntas. Si tu único plan es "contratar más gente cada vez que llegan tickets", tu costo de soporte crece igual de rápido que tus ventas y te como el margen (ver 53). Escalar significa: que cada cliente nuevo te cueste *menos* atender que el anterior. Eso se logra moviendo volumen hacia abajo en una pirámide.

## La pirámide del soporte (de barato a caro)
Mueve el máximo de volumen hacia las capas de abajo. Cada capa que sube cuesta más por interacción.

| Capa | Qué es | Costo por consulta | Meta de volumen |
|---|---|---|---|
| 1. Autoservicio | FAQ, tutoriales, página de ayuda | Casi $0 | 40-60% |
| 2. Bot / respuestas automáticas | Chatbot, plantillas, IA | Muy bajo | 20-30% |
| 3. Asíncrono humano | Tickets, email, WhatsApp en cola | Medio | 15-25% |
| 4. Sincrónico humano | Llamada, chat en vivo, visita | Alto | <10% |

**Regla práctica:** antes de contratar a la persona #2 de soporte, exprime la capa 1 y 2. Una FAQ bien hecha puede quitarte el 50% de las preguntas repetidas gratis.

## Capa 1 — Autoservicio (lo más rentable)
1. **Lista las 20 preguntas que más te repiten** (mira tu chat de un mes; ver 89 para el dato real de conversaciones).
2. Escribe una respuesta clara de cada una. Eso es tu FAQ.
3. Ponla donde el cliente la vea: web, link en el perfil de WhatsApp, mensaje de bienvenida del bot.
4. Actualízala cada mes con las nuevas preguntas repetidas.

> Para un negocio de productos (p. ej. hongos funcionales), las FAQ típicas: dosis, tiempos de envío, formas de pago, devoluciones, "¿esto sirve para X?". Cada una respondida = una conversación humana ahorrada.

## Capa 2 — Bots y plantillas
- **Plantillas / respuestas rápidas:** textos pre-escritos para lo más común. No es robotizar; es no escribir lo mismo 40 veces.
- **Bot / IA:** responde lo simple, recoge datos (nombre, ciudad, qué busca) y **escala a humano cuando detecta intención de compra o frustración**. La regla de oro: el bot nunca debe dejar al cliente atrapado. Siempre una salida a "hablar con una persona".
- Mide qué % resuelve el bot solo vs. cuántos terminan pidiendo humano. Ese % es tu palanca de escala.

## SLA — la promesa de tiempo
Un **SLA** (Service Level Agreement) es el compromiso de cuánto tardas en responder/resolver. Aunque no lo publiques, defínelo internamente para no improvisar.

Ejemplo de SLA simple para un negocio pequeño:
| Canal | Primera respuesta | Resolución |
|---|---|---|
| WhatsApp / chat | < 30 min (horario laboral) | < 4 h |
| Email | < 4 h | < 24 h |
| Reclamo / queja | < 1 h | < 24 h |

> Recordatorio de país/horario: ajusta los tiempos a tu horario de atención real y a las expectativas locales. En algunos mercados responder en 5 min es lo esperado; en otros, 1 h está bien.

## Tickets — para no perder a nadie
Un **ticket** = una solicitud abierta hasta que se resuelve. Aunque uses solo WhatsApp, lleva una lista mínima: quién, qué pide, estado (nuevo / en curso / resuelto), prioridad. Sin esto, los casos se caen entre las grietas y pierdes clientes en silencio.

**Prioriza así (triaje):**
1. Cliente molesto / a punto de cancelar → primero.
2. Cliente con intención de compra → segundo (es plata esperando).
3. Pregunta general → tercero (muchas las cubre la FAQ).

## KPIs de soporte (los 5 que importan)
Define términos:
- **Tiempo de primera respuesta:** cuánto tardas en contestar la primera vez. El que más pesa en la percepción.
- **Tiempo de resolución:** cuánto hasta cerrar el caso.
- **Tasa de resolución en el primer contacto (FCR):** % de casos resueltos sin ida y vuelta. Más alto = más eficiente.
- **CSAT (satisfacción):** preguntas "¿Qué tan satisfecho quedaste? 1-5". % de 4-5 = tu CSAT.
- **% de autoservicio / deflexión:** cuántas consultas resolvió la FAQ/bot sin humano. Tu indicador de escala.

| KPI | Rango orientativo saludable |
|---|---|
| 1ª respuesta (chat) | < 30 min |
| Resolución | < 24 h |
| FCR | > 70% |
| CSAT | > 85% (4-5 de 5) |
| Autoservicio | > 40% del volumen |

(Rangos ilustrativos, no datos duros — mide los tuyos y mejóralos mes a mes; ver 21 sobre cómo conseguir benchmarks reales.)

## Ejemplo numérico (cifras ilustrativas)
Negocio con **600 consultas/mes**. Un agente cuesta $1.500.000/mes y atiende ~300 consultas bien.

**Sin sistema:** 600 consultas ÷ 300 = **2 agentes = $3.000.000/mes**. Costo por consulta = $5.000.

**Con pirámide:** FAQ + bot resuelven el 50% (300 consultas).
- Quedan 300 para humanos → **1 agente = $1.500.000/mes**.
- Costo del bot/herramientas: ~$200.000/mes.
- Total = **$1.700.000/mes**. Costo por consulta = ~$2.833.

**Ahorro: $1.300.000/mes (-43%)** y, si la FAQ es buena, el cliente se atiende más rápido. Ese ahorro es margen puro (ver 53) o presupuesto para crecer.

> Cifras ilustrativas: usa los costos reales de tu ciudad y los sueldos vigentes (pregunta país/ciudad primero).

## Soporte como retención (no como gasto)
Retener es 5-7x más barato que conseguir un cliente nuevo (regla orientativa, ver 89). Un cliente con un problema bien resuelto suele quedar **más leal** que uno que nunca tuvo problemas. Tres movimientos:
- Resuelve rápido y con buena cara → recompra y recomendación.
- Después de resolver, pregunta CSAT y, si está feliz, pide reseña/referido.
- Detecta patrones: si 30 personas preguntan lo mismo, no es soporte, es un problema de producto, web o comunicación que debes arreglar en la raíz.

## Cómo arrancar mínimo viable (esta semana)
1. Junta las 20 preguntas más repetidas → escribe FAQ.
2. Crea 8-10 respuestas rápidas/plantillas.
3. Define tu SLA interno (aunque sea en un papel).
4. Lleva una lista de tickets simple (una hoja de cálculo basta al inicio).
5. Empieza a medir 1ª respuesta y CSAT. Solo eso ya te da control.

## Errores comunes
- **Querer automatizar todo de golpe** y dejar al cliente atrapado con un bot sin salida a humano. Furia garantizada.
- **No medir nada** y "sentir" que vas bien. Sin KPIs no sabes si mejoras.
- **Contratar gente antes de exprimir el autoservicio.** Escalas el costo, no la eficiencia.
- **Tratar las quejas como molestia** en vez de oro: cada queja repetida es un arreglo de producto pendiente.
- **SLA fantasma:** prometer rapidez y no cumplirla genera más enojo que no prometer nada.
- **No cerrar el ticket:** dejar casos "en el aire" = clientes perdidos sin que te enteres.

## Siguiente paso típico
Saca hoy tus 20 preguntas más repetidas de tu historial de chat (ver 89) y conviértelas en FAQ + plantillas; mide tiempo de 1ª respuesta y CSAT desde mañana. Cuando tengas el dato de cuánto resuelve solo el autoservicio, decide si necesitas más manos o mejor proceso (ver 168).

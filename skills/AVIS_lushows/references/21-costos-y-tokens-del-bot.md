# 21 · Costos y tokens del bot

> Destilado de la skill **optimizer_tokens_lushows** (caching, batching, routing, semantic cache, compresión, RAG, presupuesto/guardrails). AVIS rutea a esa skill cuando haya que optimizar costos en serio; aquí queda lo aplicado a AVIS. AVIS corre con **Gemini `gemini-2.5-flash`** (barato y rápido) y su regla #1 de plata: **lo que se puede leer con código NO usa IA** — el XML DIAN es gratis (ver ref 04).

## Dónde gasta tokens AVIS

Cada llamada a Gemini cuesta `tokens_entrada + tokens_salida`. El system prompt + el contexto del comercio entran en CADA turno, así que son el gasto silencioso más grande, no la respuesta.

| Dónde gasta | Qué consume | Palanca para abaratar |
|---|---|---|
| **Cada turno de chat** | system prompt + persona + historial + mensaje | Cachear el prefijo del sistema (context caching); recortar historial a los últimos N turnos; `max_output_tokens` corto |
| **Visión de factura PDF** | el PDF como `inlineData` + prompt de extracción | Solo cuando NO hay XML; 1 sola pasada, nunca reprocesar |
| **Visión de factura foto** | imagen + prompt | Igual que PDF; comprimir imagen antes de mandar |
| **Categorización de gasto** | texto corto de la factura | Tarea de texto = barata; saltarla si la fuente ya trae categoría |
| **Lectura XML/ZIP DIAN** | **cero IA** (es `fast-xml-parser`) | Ya es gratis — preferir siempre esta vía |
| **El CRUCE (no contar doble)** | **cero IA** (comparación numérica/NIT en código) | Ya es gratis |
| **Organize / reportes de blog** | resumen o redacción larga | Batch nocturno (no realtime); plantilla fija + datos, no narrar todo |

## Las palancas, en orden de impacto

1. **XML exacto sin IA (#1).** Si llega ZIP/XML de la DIAN, AVIS lo parsea con código: exacto y $0. La visión es el plan B caro, no el principal. Esto es la diferencia entre centavos y fracciones de centavo por factura.
2. **Caché del prompt del sistema.** La persona de AVIS + reglas de cumplimiento + formato no cambian entre mensajes → se cachean como prefijo. Solo el mensaje del cliente y el contexto del comercio varían. Cachear lo que se reusa 3+ veces; nunca cachear lo de un solo uso.
3. **Modelo barato por defecto (`gemini-2.5-flash`).** Flash sobra para chat, categorizar y leer facturas. No subir a un modelo grande salvo caso que de verdad lo pida (routing).
4. **No reprocesar.** Una factura ya leída (tiene `fuente` y `datos`) NO se vuelve a mandar a visión. Un duplicado detectado en el cruce NO gasta IA. Idempotencia = ahorro.
5. **Comprimir el contexto.** Mandar a Gemini solo lo necesario: últimos turnos relevantes, no toda la conversación; resumen del comercio, no el volcado entero. Recortar el historial evita que el costo por turno crezca sin parar.
6. **Batch donde aplique.** Lo que no espera el cliente (reportes semanales, organize del blog, enriquecimiento nocturno) va en lote, no en tiempo real.

## Orden de magnitud del costo

Con `gemini-2.5-flash` (precios de centavos por millón de tokens), cada acción típica de AVIS cuesta **una fracción de centavo de dólar**:

- **Turno de chat** (con caché de sistema): centésimas de centavo.
- **Leer factura por XML:** **$0** de IA (solo código).
- **Leer factura por PDF/foto (visión):** unas pocas décimas de centavo, la acción más cara.
- **Categorizar un gasto:** texto corto, casi nada.

Lectura para Lushows: una pyme con decenas de facturas y cientos de mensajes al mes gasta **centavos, no dólares**. El riesgo no es el costo unitario; es un bucle o un abuso que dispare el volumen.

## Guardrails de presupuesto

El gasto unitario es bajo, pero un loop o un abuso lo multiplica. Mínimos no negociables:

- **Tope de tokens de salida** por respuesta (`max_output_tokens`) para que AVIS no escriba ensayos.
- **Rate limit por número/comercio:** un teléfono no puede disparar miles de llamadas/hora.
- **Anti-reproceso:** no mandar a visión un documento ya procesado; respetar idempotencia del cruce.
- **Tracking de gasto** por comercio (tokens y $) y **alerta** si un comercio se sale de su norma.
- **Kill switch:** si el gasto diario supera un umbral, AVIS degrada (solo XML/código, sin visión) o pausa y avisa al operador, antes de que llegue una factura sorpresa.

> **Roadmap:** dashboard de costo por comercio (tokens/visión/$ al mes), semantic cache para las FAQ de cumplimiento más repetidas, y un router que solo escale de Flash a un modelo mayor en la fracción de casos que de verdad lo necesiten.

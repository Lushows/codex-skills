# 196 — Anti-patrones compilado (todos los errores del outbound en un lugar)

Este módulo es el **índice maestro de lo que NO hacer** en toda la disciplina. El módulo `97` cubrió los errores fatales que matan campañas enteras; este los recoge todos —de cada bloque de la skill, incluyendo los de operación y agencia— en un solo mapa navegable. Importa porque el outbound es una cadena larga (targeting → datos → deliverability → copy → cadencia → calificación → handoff → ops; ver `98`) y cada eslabón tiene su forma de romperse. Tener el catálogo completo en un lugar te sirve como **checklist de auditoría**: antes de lanzar, o cuando algo se cae, recorres el bloque sospechoso y encuentras el anti-patrón. Cada error apunta al módulo que enseña cómo hacerlo bien.

## Cómo usar este compilado

No lo leas de corrido buscando memorizar. Úsalo así: cuando un número esté mal (ver diagnóstico en `83`), ve a la sección del bloque correspondiente y revisa si estás cometiendo alguno de sus anti-patrones. Es un mapa de "dónde suele romperse cada cosa".

## Bloque 0 — Fundamentos y mentalidad

- **Tratar outbound como suerte, no como sistema.** Sin ecuación de pipeline no puedes predecir ni mejorar (ver `05`, `98`).
- **Rendirse antes de que el sistema madure.** Warmup + señal estadística toman semanas; apagar al día 3 es abandonar antes de arrancar (ver `04`, `97` err 12).
- **Confundir actividad con resultado.** Mandar muchos correos no es progreso si no puedes repetir el resultado (ver `80`).
- **Ignorar la ética/reputación por volumen.** Spam a escala quema tu nombre; el juego es relevancia a escala (ver `07`).

## Bloque 1 — Targeting / ICP

- **ICP difuso o "todos".** Sin cliente ideal claro, el mensaje no le habla a nadie (ver `10`, `12`).
- **Perseguir cuentas que no existen en volumen suficiente** (TAM/SAM/SOM mal dimensionado): prometes lo que el mercado no tiene (ver `13`, `17`).
- **Ignorar el comité de compra:** escribirle a una sola persona cuando deciden varias (ver `11`, `22`).
- **No usar triggers/señales:** escribir en frío puro cuando un evento real dispararía el reply (ver `14`, `37`).

## Bloque 2 — Datos y sourcing

- **Comprar listas y mandarles en frío:** bounces + quejas destruyen la reputación en un día (ver `28`, `49`, `97` err 3).
- **No verificar los correos antes de enviar:** bounces altos = reputación al piso (ver `28`).
- **Scraping ilegal o que viola términos:** riesgo legal y de baneo (ver `27`).
- **Datos sin enriquecer:** listas sin la señal que hace relevante el mensaje (ver `29`, `36`).

## Bloque 3 — Stack y automatización

- **Automatizar en Fase 1 (antes de que funcione):** escalas el fracaso y quemas dominios (ver `35`, `66`, `98`).
- **Creer que "comprar la herramienta" es el sistema:** la herramienta ejecuta el sistema, no lo reemplaza (ver `30`).
- **Sobre-automatizar la personalización hasta volverla genérica falsa** (ver `52`, `97` err 5).

## Bloque 4 — Deliverability (el más caro)

- **Enviar frío desde el dominio principal.** El error #1: lo quemas, irreversible (ver `41`, `97` err 1).
- **Saltarse SPF/DKIM/DMARC:** directo a spam desde el correo uno (ver `42`).
- **Saltarse el warmup:** buzón nuevo enviando en volumen = spam (ver `43`).
- **Exceder límites de envío por buzón (~30–50/día):** dispara filtros de spam (ver `44`).
- **No monitorear reputación:** descubres el dominio quemado cuando ya arrastró resultados (ver `46`).

## Bloque 5 — Copy / mensaje

- **"Personalización" falsa** ("Hola {nombre}" en plantilla genérica): se nota y no mueve la aguja (ver `52`, `53`).
- **Pedir la venta en el primer toque:** el outbound agenda, no cierra (ver `55`, `97` err 6).
- **Subject lines de clickbait o spam-words:** caes en spam o pierdes credibilidad (ver `51`).
- **Correo largo sobre ti y no sobre el prospecto:** nadie lo lee (ver `50`, `54`).
- **Meterte a "cerrar" en el copy:** el cierre es conversación humana → `ventas_lushows`.

## Bloque 6 — Cadencias

- **Un solo toque y rendirse:** tiras el 60–70% de las respuestas posibles (ver `60`, `63`, `97` err 7).
- **Monocanal:** solo email o solo WhatsApp deja conversiones sobre la mesa (ver `61`, `97` err 8).
- **Cadencia demasiado agresiva o demasiado espaciada:** timing mal calibrado mata el ritmo (ver `62`).
- **No adaptar la respuesta según lo que contestan** (ver `64`, `68`).

## Bloque 7 — Calificación y handoff

- **Pasarle leads basura al vendedor:** destruye su confianza y el forecast (ver `70`, `78`, `97` err 9).
- **Perseguir el "tal vez" eterno en vez de un "no" rápido** (ver `78`).
- **Handoff sin contexto:** el vendedor recibe la reunión sin saber nada del prospecto (ver `73`).
- **No nutrir el "no ahora":** tiras leads que comprarían en 3 meses (ver `76`).

## Bloque 8 — Métricas

- **Medir vanity metrics** ("correos enviados") en vez de reply positivo y reuniones (ver `80`, `97` err 10).
- **No segmentar los números por canal/segmento:** el promedio miente (ver `81`, `96`).
- **"Optimizar" sin diagnóstico:** tocar cosas al azar sin saber dónde se rompe (ver `83`).
- **Números inventados en reportes:** todo cálculo debe ser exacto → `Matematicas_lushows`.

## Bloque 9 y agencia (operación / negocio)

- **Vender la agencia sin máquina propia probada:** vendes humo (ver `190`, `192`).
- **Compartir infra de envío entre clientes:** uno hunde a todos (ver `194`, el pecado capital de la agencia).
- **Prometer ventas/ROI (no reuniones):** prometes lo que no controlas y quedas como estafa (ver `193`).
- **Cobrar por reunión sin conocer tus ratios:** trabajas gratis o a pérdida (ver `191`).
- **No definir "reunión calificada":** pelea en cada factura (ver `193`).
- **Sumar clientes más rápido de lo que puedes operarlos bien:** la calidad se cae, incumples SLAs (ver `194`).
- **Competir solo por precio:** te empuja a volumen-sin-relevancia y a quemar tu reputación (ver `191`, `195`).

## Legal / cumplimiento (transversal)

- **Ignorar Habeas Data (Colombia), GDPR, CAN-SPAM:** multas reales + reputación destruida (ver `49`, `181`).
- **Sin opt-out real:** ilegal y dispara quejas de spam (ver `45`, `49`).

## El anti-patrón raíz (del que salen casi todos)

Casi todos los errores de arriba son formas de una misma enfermedad: **priorizar volumen sobre relevancia**. Spray-and-pray, listas compradas, personalización falsa, cero calificación, infra compartida — todos nacen de "más rápido, más masivo, más barato" en lugar de "más relevante, más medido, más contenido". El outbound de 2026 castiga el volumen sin relevancia con spam, baneos y reputación quemada. La cura es siempre la misma: **relevancia a escala, sistema medible, disciplina de deliverability** (ver `98`, `197`).

## Siguiente paso

Usa este compilado como auditoría: antes de tu próximo lanzamiento, recorre el bloque de cada etapa de tu campaña y marca que no estás cometiendo sus anti-patrones. Si ya tienes un problema, cruza el síntoma con `83` (diagnóstico por métrica) para ubicar el eslabón roto. Para construir el sistema que evita todo esto por diseño, `198`. Para hacia dónde va el outbound y qué errores nuevos evitar, `197`.

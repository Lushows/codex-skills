# 94 — Auction Insights e inteligencia

Lee este módulo cuando quieras saber contra quién compites de verdad, cuando tu impression share caiga y no sepas por qué, o cuando un cliente diga "espía a la competencia". Tienes dos herramientas gratis y legales: **Auction Insights** (informe de subastas, dentro de tu cuenta — te dice contra quién pujas) y el **Ads Transparency Center** (centro de transparencia de anuncios de Google — te deja ver los anuncios activos de CUALQUIER anunciante). Con esas dos lees el mercado sin pagar nada ni espiar de forma turbia. Lo demás es interpretarlo bien. Marco: Google **captura intención**; saber quién más pelea por esa misma intención es lo que te dice si pujas, mejoras calidad o cedes.

## Auction Insights: las 5 columnas que importan

Ruta: selecciona campaña/grupo/keyword → arriba **"Estadísticas de subasta"** (Auction Insights). Muestra con quién compartes subastas. Disponible para Search y Shopping; en PMax hay una versión limitada. Las columnas:

| Columna | Qué significa | Cómo leerla |
|---|---|---|
| **Impression share** (cuota de impresiones) | % de las veces que apareciste de las que podías | Bajo (<50%) = te están dejando atrás (presupuesto o Ad Rank, ver 01) |
| **Overlap rate** (tasa de superposición) | % de veces que un competidor apareció cuando tú también | Alto = compiten cabeza a cabeza por lo mismo |
| **Position above rate** (tasa de posición superior) | % de veces que ESE rival quedó ARRIBA de ti cuando ambos salieron | Alto = te están ganando posición; revisa puja/QS |
| **Top of page rate** (tasa parte superior) | % de tus impresiones que salieron arriba de los orgánicos | Bajo = apareces pero abajo, menos clics |
| **Outranking share** (cuota de superación) | % de veces que TÚ quedaste arriba de ese rival (o saliste y él no) | Alto = los dominas; bajo = ellos a ti |

Lectura en 30 segundos: si un competidor tiene **overlap alto + position above alto + tu impression share bajo**, ese rival te está comiendo esas subastas. La causa es Ad Rank (puja × Quality Score × contexto × formato, ver 01): o pujas poco, o tu anuncio/landing es peor. No es magia, es matemática de subasta. Mira la tendencia (segmenta por tiempo): un rival cuyo overlap sube semana a semana entró agresivo y va por tu terreno.

## Qué hacer con lo que ves

| Lo que ves | Diagnóstico | Acción |
|---|---|---|
| Impression share bajo por "presupuesto" (columna IS perdido por presupuesto) | Te quedas sin plata antes de fin de día | Sube presupuesto, o concentra horario/geo donde sí convierte (ver 70, 26) |
| Impression share bajo por "ranking" (IS perdido por ranking) | Tu Ad Rank pierde | Mejora QS: relevancia keyword-anuncio-landing (ver 31, 36, 01) |
| Un rival nuevo con overlap subiendo | Entró competencia agresiva | Revisa tus negativos, tu oferta, tu CPA tope; no entres a guerra de pujas ciega (ver 22, 64) |
| Tú dominas (outranking alto) en términos caros | Estás pagando de más para ganar | ¿Vale ese término? Mira CPA real, no ego (ver 60) |
| Position above alto de UN rival en marca | Te pujan tu propia marca | Defiende con campaña de marca y, si toca, reporta uso de tu nombre (ver 39) |

Regla: Auction Insights te dice **dónde estás perdiendo posición**; la decisión de pelear o ceder la toma el CPA/ROAS real (ver 64), no las ganas de "salir primero". A veces el primer lugar no es rentable y el competidor que lo tiene se está desangrando — déjalo.

## Ads Transparency Center: ver los anuncios del rival

El **Ads Transparency Center** (adstransparency.google.com) es público: pones el nombre/dominio de un anunciante y ves los anuncios que tiene **corriendo ahora** — texto, imágenes, video, formatos, rango de fechas, y región donde se muestran. Es el equivalente de Google a la Biblioteca de Anuncios de Meta (ver `facebook_ads_lushows`). Solo muestra de anunciantes verificados, que en 2026 son casi todos.

Cómo usarlo bien:
1. **Busca a tus 3–5 competidores reales** (los que viste en Auction Insights, no los que tú crees).
2. **Mira qué ángulos repiten**: si llevan meses con el mismo mensaje, probablemente les funciona. La constancia es la pista más honesta de qué vende.
3. **Mira formatos**: ¿están en Search puro, o también Demand Gen/YouTube/PMax? Te dice dónde invierten y dónde no estás peleando.
4. **Filtra por región** (Colombia/LatAm) para ver lo que muestran a TU mercado, no a otro.
5. **Anota promesas y precios** que muestran (sin copiarlos textual).

## Qué copiar y qué NO

| COPIA (inspírate) | NO COPIES (te quema) |
|---|---|
| El ángulo/intención que repiten (qué dolor atacan) | El texto literal — anuncio genérico clonado, mal QS |
| La estructura de oferta que sostienen meses | Su precio sin saber sus márgenes (ver `economist_lushows`) |
| Los formatos donde invierten (Search/PMax/YouTube) | Pujar sobre su MARCA sin estrategia (caro, riesgoso, ver 39) |
| Las objeciones que responden en el anuncio | Su nombre/logo en tu copy (riesgo legal/política, ver 08) |

El error mental clásico: ver al competidor y querer **ser igual pero más barato**. Eso es una carrera al fondo. Lo inteligente es ver qué hace y **diferenciarte** donde él es débil (tu propuesta única, rutea a `directorcreativo_lushows` para el ángulo de marca). Espiar es para entender el campo de batalla, no para volverte una copia. Si quieres el ángulo de venta que ataca esas objeciones mejor que el rival, rutea a `ventas_lushows`.

## Decisión: ¿peleo, mejoro o cedo esta subasta?

Cuando ves que un rival te gana, el árbol de decisión honesto:

| Situación | Pregunta clave | Decisión |
|---|---|---|
| Pierdes posición pero el término convierte bien para ti | ¿El CPA sigue ≤ mi CAC máximo si subo puja? | Si sí, sube puja moderado; si no, no entres |
| Pierdes por ranking, no por puja | ¿Mi QS es bajo (anuncio/landing flojos)? | Mejora relevancia y landing antes que puja (ver 36, 31, 33) |
| Rival domina un término que NO te convierte | ¿De verdad lo necesito? | Cédelo; déjalo que pague de más |
| Te pujan tu propia marca | ¿Es competidor o revendedor/afiliado? | Defiende con marca; si usa tu nombre/logo, evalúa reporte (ver 39, 08) |
| Rival nuevo, agresivo, en todo | ¿Está sostenido o es un sprint? | Observa 2–3 semanas; muchos se desangran y se van |

La inteligencia no es ganar todas las subastas; es **ganar las rentables y dejar las trampas a la competencia**. El rival que está primero en todo a cualquier costo suele estar quemando plata que tú no tienes que quemar (valida tu economía con `economist_lushows`).

## Rutina de inteligencia (qué revisar y cada cuánto)

| Tarea | Frecuencia | Herramienta |
|---|---|---|
| Impression share y su causa (presupuesto/ranking) | Semanal | Auction Insights |
| Rivales que suben overlap | Semanal | Auction Insights (segmentado por tiempo) |
| Ángulos/formatos nuevos del competidor | Mensual | Ads Transparency Center |
| Tu marca pujada por terceros | Semanal | Auction Insights (campaña de marca) |

## Errores comunes — blacklist

- **Confundir "salir primero" con "ser rentable".** Outranking alto en términos que no convierten es quemar plata por ego; decide por CPA/ROAS (ver 64).
- **Leer impression share sin ver la CAUSA** (presupuesto vs ranking). Cada causa tiene acción distinta; no subas puja si el problema es QS (ver 01, 36).
- **Copiar el texto del anuncio del competidor literal.** Anuncio genérico clonado = peor Quality Score y cero diferenciación (ver 31).
- **Pujar sobre la marca del competidor sin pensar.** Caro, baja conversión y a veces problema de política; hazlo solo con estrategia clara (ver 39).
- **Asumir competidores en vez de mirarlos.** Tus rivales reales son los de Auction Insights, no los que imaginas.
- **Copiar el precio del rival sin conocer sus márgenes.** Puede estar perdiendo plata; valida tu economía con `economist_lushows`.
- **Entrar a guerra de pujas porque un rival subió.** Si tu CPA se rompe, ese término dejó de valer; cede y gana donde sí eres rentable.
- **Espiar una vez y olvidarlo.** El mercado se mueve; revisa Auction Insights cada semana y el Transparency Center cada mes.

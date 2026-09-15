# 53 — Conversiones offline (OCI)

Lee este módulo cuando tu venta **no se cierra en la web** sino en una conversación — WhatsApp, llamada, visita, propuesta — y por eso Google "no ve" cuándo de verdad ganaste plata. Si tu cuenta optimiza por "formularios enviados" o "clic en WhatsApp" pero esos leads casi nunca compran, este es **el upgrade #1 para Search → WhatsApp/llamada en LatAm**. Es el equivalente Google del `ctwa_clid` de Meta (ver facebook_ads_lushows): le devuelves a la máquina la verdad de quién compró, y la máquina deja de traerte curiosos. Si lees un solo módulo de medición, que sea este.

## El problema que OCI resuelve

Google optimiza por lo que tú le dices que es una conversión. Si le dices "una conversión es un clic a WhatsApp", Smart Bidding (ver 15) te traerá **gente que da clic a WhatsApp** — aunque ninguno compre. La máquina es obediente, no adivina. El hueco entre "dio clic" y "pagó" es donde se quema el presupuesto en LatAm: el cierre pasa offline (en el chat, en la llamada) y Google se queda ciego, así que sigue trayendo perfiles parecidos a los clickeadores, no a los compradores.

**OCI** (*Offline Conversion Import* — importación de conversiones offline) cierra ese hueco. La idea en una frase: **capturas el gclid cuando entra el lead, y cuando ese lead califica o compra, le subes a Google esa conversión con su valor**. Así Google aprende a traer **compradores**, no clics.

El **gclid** (*Google Click ID*) es el identificador único que Google le pega a cada clic en tu anuncio (viaja en la URL como `?gclid=XXXX`). Es el hilo que conecta "este clic" con "esta venta" semanas después. (Variantes que verás en jun-2026: **GBRAID/WBRAID** son los identificadores equivalentes en iOS/app cuando no hay gclid; el sistema los maneja igual — captúralos si aparecen.)

## Cómo funciona el flujo (de punta a punta)

```
1. Persona busca → da clic en tu anuncio → llega con un ?gclid=XXXX en la URL
2. Capturas el gclid en el formulario / landing / chat (campo oculto)
3. El lead pasa a WhatsApp/llamada/CRM CON su gclid pegado
4. Días después: ese lead compra (o califica) → lo marcas en tu CRM/hoja
5. Subes a Google: gclid + qué pasó ("Compra") + valor (ej. $10.000 COP) + fecha y hora del clic
6. Smart Bidding aprende: "los clics como ESE traen plata" → trae más iguales
```

Tres maneras de subir la conversión a Google:

| Método | Cómo | Para quién |
|---|---|---|
| **Subida manual (CSV)** | Subes un archivo en Herramientas → Conversiones → Subidas, con la plantilla de Google | Volumen bajo, empezar hoy |
| **Google Sheets vinculada** | Una hoja con el formato exacto de Google que la cuenta jala sola (programada cada día) | Pyme sin dev, semi-automático |
| **API (Google Ads API)** | Tu sistema sube en tiempo real apenas se marca la venta | Volumen alto, con dev → engineer_visualopen_lushows |

Para una pyme en Colombia, la ruta realista es **Google Sheets programada**: el equipo marca "vendió" en la hoja con su gclid y valor, Google la lee a diario. Sin código, y ya optimizas por compradores. Cuando crezca el volumen, migras a API.

## Capturar el gclid — el paso que casi todos saltan

Si no capturas el gclid, OCI no existe. Tres formas:

1. **En la landing/formulario:** un campo oculto (`<input type="hidden">`) que lee el `?gclid=` de la URL con un pedazo de JavaScript y lo guarda con los datos del lead. Lo arma tu dev → desingweb-lushows para la landing, engineer_visualopen_lushows si hay backend que persista. Es el cimiento; sin esto no hay nada.
2. **En el lead form de Google (ver 52):** el webhook ya te entrega el gclid junto al lead. Solo guárdalo en tu CRM/`customerMemory`.
3. **En el chat de WhatsApp:** si el anuncio lleva directo a WhatsApp, el truco es pasar por una **landing puente** que capture el gclid y lo meta en el primer mensaje (o lo asocie al número). En Meta esto lo da el `ctwa_clid` nativo; en Google search→WhatsApp **casi siempre necesitas la landing puente** (anuncio → landing con botón "WhatsApp" que arrastra el gclid). Anótalo: es la diferencia entre medir o no.

Guarda **gclid + número/email + fecha-hora del clic** juntos. Sin esa tripleta no puedes subir nada — Google rechaza la conversión si falta la marca de tiempo o si el gclid no calza con un clic real de los últimos ~90 días.

## Valor por etapa: enséñale a Google qué lead vale más

OCI brilla cuando subes **valor**, no solo "sí/no". En ventas con ciclo largo (ver 58 high-ticket) puedes subir conversiones en cada etapa con un valor que refleje la probabilidad de cierre:

| Etapa del lead | Valor que subes (ejemplo COP) |
|---|---|
| Lead calificado (es tu cliente, tiene presupuesto) | $20.000 |
| Propuesta enviada / reunión asistida | $50.000 |
| Venta cerrada | $200.000 (valor real del cliente) |

Así Smart Bidding no persigue "muchos leads" sino "leads que avanzan y cierran". Es la diferencia entre una cuenta que **parece** funcionar (CTR bonito, muchos leads) y una que **factura** (ver 64 ROAS-real). El stack completo para montar esto —hoja, columnas, automatización, cruce con `customerMemory`— está en 96 stack-OCI, y el cierre que genera esas ventas es ventas_lushows 82.

## Setup mínimo para una pyme (sin dev, hoy)

Lo más realista para empezar en Colombia, paso a paso:

1. **Crea la acción de conversión OCI:** Herramientas → Conversiones → Nueva → "Importar" → "Conversiones desde clics" → nómbrala "Venta WhatsApp". Marca el conteo, la ventana (ej. 90 días) e inclúyela en "Conversiones" (la columna que optimiza Smart Bidding).
2. **Captura el gclid:** campo oculto en la landing puente (ver arriba). Si usas lead form de Google, el webhook ya lo trae.
3. **Arma la hoja:** Google Sheets con las columnas exactas que pide Google — `Google Click ID`, `Conversion Name`, `Conversion Time`, `Conversion Value`, `Conversion Currency` (COP). Una fila por venta.
4. **Vincula la hoja:** en Subidas → programa la importación diaria desde esa Sheet. El equipo solo llena filas; Google jala solo.
5. **Disciplina:** cada vez que se cierra una venta, el operador pega el gclid del cliente (guardado en `customerMemory`) y el valor en la hoja. Eso es todo.

En una semana ya tienes a Google optimizando por compradores en vez de clickeadores. Cuando el volumen crezca, migras a la API (engineer_visualopen_lushows).

## Errores comunes — blacklist

1. **Optimizar por "clic a WhatsApp" y nunca subir la venta.** Google te trae clickeadores, no compradores. OCI es lo que cierra ese hueco; sin él, vuelas a ciegas y pagas curiosos.
2. **No capturar el gclid.** Sin gclid no hay OCI. El campo oculto en la landing es el cimiento — móntalo antes que nada (ver desingweb-lushows).
3. **Subir solo "sí compró" sin valor.** Pierdes la mejor parte: con valor por etapa, Google prioriza los leads que de verdad facturan (ver 58, 64).
4. **Subir las conversiones tarde.** Smart Bidding aprende con datos frescos. Sube al menos cada semana, idealmente a diario con la hoja automática; conversiones de hace un mes pesan poco.
5. **Marcar mal en el CRM.** Si el equipo no registra quién compró con su gclid, no hay qué subir. El registro disciplinado del cierre es parte del trabajo (ver ventas_lushows, `customerMemory` del proyecto).
6. **Creer que OCI arregla un mal producto o una mala oferta.** Optimiza tráfico hacia compradores; no convierte por ti. La oferta y el cierre siguen siendo tuyos (viabilidad → economist_lushows).
7. **No alinear la "conversión que importa" con el negocio.** Si subes "lead" como conversión final, optimizas a leads. La conversión que le declaras a Google como principal debe ser la que paga la luz: la **venta**.

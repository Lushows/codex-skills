# 09 — Glosario Meta Ads en lenguaje simple

Diccionario de consulta rápida: cada término en 1-2 líneas, sin jerga circular. Úsalo cuando cualquier otro módulo (o Ads Manager) suelte una sigla que no reconoces. Organizado por tema. Donde algo cambió en 2026, está marcado.

## Subasta y entrega

- **CPM**: costo por mil impresiones; lo que pagas por mostrar tu anuncio 1.000 veces. Es termómetro de costo de inventario, no un KPI de negocio (ver 01).
- **eCPM**: el CPM "efectivo" que Meta calcula internamente para comparar tu anuncio contra todos los demás en la subasta (ver 01).
- **Total Value**: el puntaje con que tu ad compite = Bid × EAR + Ad Quality. Gana el mayor, no el que más puja.
- **EAR (Estimated Action Rate)**: probabilidad estimada de que la persona haga la acción que pediste; la calcula el ML.
- **Andromeda**: motor de retrieval de Meta que preselecciona qué ads compiten por cada usuario leyendo el creativo; por eso el creativo es el targeting (ver 92).
- **GEM**: modelo generativo de Meta (nov-2025) sobre Andromeda que mejora la predicción de qué ad le sirve a quién.
- **Entity ID**: identidad que Meta asigna a un creativo; varios creativos casi-idénticos colapsan en uno solo, por eso necesitas variedad conceptual (ver 02, 92).
- **Alcance (reach)**: cuántas personas DISTINTAS vieron tu anuncio al menos una vez.
- **Impresiones**: cuántas veces se mostró el anuncio en total (una persona puede sumar varias).
- **Frecuencia**: impresiones ÷ alcance; veces promedio que cada persona vio tu ad. Arriba de 3-4 en frío suele ser fatiga (ver 39).
- **Pacing**: cómo Meta reparte tu presupuesto a lo largo del día buscando las subastas más baratas; por eso no juzgas resultados a media mañana.
- **Learning phase**: fase inicial donde el sistema explora a quién mostrarle tu ad; necesita ~50 conversiones/semana por ad set para estabilizar (ver 13).
- **Learning limited**: estado cuando el ad set no llega a esas ~50/semana; entrega errática y más cara. En cuentas chicas es normal (ver 07).

## Métricas

- **CTR**: porcentaje de impresiones que generaron clic. Mide si el creativo llama la atención.
- **Outbound CTR**: CTR contando solo clics que SALEN de Meta (hacia tu web/WhatsApp); más honesto que el CTR total, que incluye clics en "ver más".
- **CPC**: costo por clic.
- **CPA**: costo por adquisición/resultado (una compra, un lead, una conversación). La métrica reina del día a día.
- **ROAS**: retorno sobre gasto publicitario = ingresos atribuidos ÷ gasto. ROAS 3 = cada peso invertido devolvió 3 en ventas (atribuidas, ojo).
- **AOV**: valor promedio del pedido (average order value).
- **MER**: ingresos TOTALES del negocio ÷ gasto TOTAL en ads; el "ROAS del negocio completo", inmune a mentiras de atribución (ver 64).
- **Incrementalidad**: las ventas que NO habrían ocurrido sin el ad; la verdad detrás del ROAS. Meta ya ofrece atribución incremental que reporta menos pero real (ver 16, 65).
- **nCAC**: costo de adquirir un cliente NUEVO (excluye recompras); el número que le importa a economist_lushows.
- **Thumbstop (hook rate)**: % de gente que pasó de los primeros ~3 segundos del video; mide la fuerza del gancho (ver 37).
- **Hold rate**: % que sigue viendo a los 15s (o % de retención); mide si el video sostiene la atención tras el gancho.
- **CVR**: tasa de conversión; % de visitantes/clics que terminan en el resultado (compra, lead).

## Estructura

- **Campaña**: nivel superior; define el objetivo (qué resultado quieres).
- **Ad set (conjunto de anuncios)**: nivel medio; define presupuesto, audiencia, ubicaciones y evento de optimización.
- **Ad (anuncio)**: nivel inferior; el creativo (video/imagen + texto + botón) que la gente ve.
- **CBO / Advantage+ budget**: presupuesto definido a nivel CAMPAÑA; Meta lo reparte entre ad sets según rendimiento.
- **ABO**: presupuesto definido a nivel AD SET; tú controlas cuánto recibe cada uno (útil para testing controlado, ver 17).
- **ODAX**: la estructura de 6 objetivos de campaña de Meta: Awareness, Traffic, Engagement, Leads, App promotion, Sales (ver 11).
- **Value Rules**: reglas para decirle a Meta que ciertos clientes valen más (ej. nuevos vs recurrentes); claves con el cap de clientes existentes (ver 15, 24).

## Audiencias

- **Custom audience (audiencia personalizada)**: gente que YA interactuó contigo: visitó tu web (vía dataset), te escribió, está en tu lista de clientes (ver 21).
- **Lookalike (audiencia similar)**: Meta busca gente parecida a una custom audience tuya (ej. parecida a tus compradores). Menos relevante en la era broad (ver 22).
- **Broad (abierta)**: sin segmentación (solo país/edad mínima); dejas que Andromeda encuentre al comprador leyendo tu creativo. El default moderno (ver 20).
- **Advantage+ audience**: tu segmentación es solo una "sugerencia"; el sistema explora más allá de ella.
- **Overlap (solapamiento)**: cuando dos ad sets le compiten a la misma gente; te subes el precio a ti mismo.
- **Retargeting/remarketing**: mostrar anuncios a quien ya te conoce (visitó, carriteó, escribió) para cerrarlo (ver 03, 23).
- **Cap de clientes existentes**: límite (25-30%, mar-2026) del gasto en Advantage+ Sales hacia gente que ya te compró, para forzar adquisición.

## Medición

- **Dataset (antes "Píxel")**: el contenedor de eventos; el código en tu web que reporta lo que hacen los visitantes (ver 05). El Pixel ID = Dataset ID.
- **CAPI**: Conversions API; los mismos eventos enviados desde tu servidor para recuperar lo que el navegador pierde (ver 06).
- **EMQ**: Event Match Quality; nota 1-10 de qué tan bien Meta empareja tus eventos de servidor con personas reales. **Piso 2026: ≥ 8** (ver 06).
- **AEM (Aggregated Event Measurement)**: el sistema de 8 eventos web priorizados por dominio tras iOS 14.5 (ver 05).
- **Atribución**: a qué anuncio se le "cuelga" cada conversión.
- **7d-click / 1d-view**: ventana de atribución. **Cambio 2026**: Meta quitó las ventanas view-through (7d/28d) del API en ene-2026; hoy la atribución del API es **solo-clic** (1d/7d-click). Reporta menos, es más honesto (ver 16).
- **`ctwa_clid`**: id de clic de un anuncio Click-to-WhatsApp; lo capturas en el primer mensaje del cliente para atribuir la conversación y la venta vía CAPI de mensajería (ver 53).
- **Deduplicación**: mecanismo (mismo `event_id`) para que un evento enviado por dataset Y CAPI cuente una sola vez.
- **UTM**: etiquetas en la URL (`utm_source=facebook...`) para que TU analítica (GA4, etc.) sepa de dónde vino cada visita, independiente de Meta (ver 66).

## Formatos y campañas

- **CTWA**: Click-to-WhatsApp; anuncio cuyo botón abre un chat de WhatsApp con tu negocio. El formato rey de la pyme LatAm. Ventana de 72h de mensajes gratis por conversación iniciada (ver 50, 53).
- **WhatsApp por-mensaje**: desde jul-2025 WhatsApp cobra por mensaje (no por conversación). En Colombia es barato: Marketing ~$0.0125/Utility ~$0.0008 por mensaje (ver 50).
- **Meta Business Agent**: bot de IA de Meta (3-jun-2026) que atiende WhatsApp/IG por el negocio (ver 51).
- **Lead ads / Advantage+ Leads**: formulario nativo dentro de Facebook/Instagram (sin landing); captura datos con dos taps (ver 52).
- **DPA / anuncios de catálogo**: anuncios dinámicos que muestran automáticamente los productos de tu catálogo a cada persona (ej. el producto exacto que dejó en el carrito, ver 56).
- **Advantage+ Sales (antes ASC)**: campaña de ventas casi totalmente automatizada: tú pones presupuesto, país y creativos; Meta hace el resto (ver 12).
- **Advantage+ Creative Suite**: variaciones automáticas del ad, incluido **image-to-video** (ver 90, 91).
- **WhatsApp Status ads**: inventario de anuncios en el Estado de WhatsApp (nuevo 2026, ver 02).
- **Partnership ads**: anuncios publicados en colaboración con un creador/influencer, desde su handle, con tu presupuesto (el viejo whitelisting).

## Errores comunes — blacklist

- **Confundir alcance con impresiones**: pagar 100.000 impresiones puede ser 20.000 personas viéndote 5 veces; revisa frecuencia.
- **Optimizar el negocio por ROAS de plataforma ignorando MER e incrementalidad**: la atribución infla; el banco no (ver 64, 65).
- **Usar CTR total en vez de outbound CTR**: los clics en "ver más" maquillan creativos que no mueven a nadie a tu canal.
- **Tratar el CPM como KPI**: CPM caro con CPA rentable es éxito; CPM barato con CPA caro es basura bien distribuida.
- **Hablar de "ROAS" sin decir ventana de atribución**: con la atribución solo-clic 2026, comparar contra números view-through viejos engaña; usa siempre la misma ventana.
- **Decir "píxel" creyendo que es distinto del dataset**: es el mismo objeto, renombrado.
- **Decir "audiencia" para todo**: custom ≠ lookalike ≠ broad; cada una tiene reglas y usos distintos (ver 20-22).

# 80 — Playbook: E-commerce

El vertical donde Meta Ads es más "ciencia exacta": hay píxel (hoy **Dataset**, ver `actualizacion-2026-06`), hay carrito, hay ROAS medible. También donde más gente quiebra por no saber su matemática. Aplica a cualquier tienda online que venda producto físico por web (ropa como D'BEST → ver 84, suplementos como BIO-SETA en su parte e-com → ver 83, hogar, tecnología, lo que sea). Si tu cierre es por WhatsApp y no por checkout, mezcla esto con el playbook CTWA (ver 50) — en LatAm casi todos terminan híbridos. La identidad del playbook: medir completo, conocer tu margen, dejar que el algoritmo amplio + creativo (ver 20, 30) haga el trabajo, y subir el AOV antes de pelear el CPA.

## Requisito no negociable: medición completa (jun-2026)

Antes del primer peso: **Dataset + CAPI** (Conversions API; envío server-side que sobrevive a bloqueadores e iOS — ver 05-06) con el embudo de catálogo `ViewContent → AddToCart → InitiateCheckout → Purchase`, cada uno con `value` y `currency`. Sin Purchase con valor no hay ROAS, no hay optimización por compra, no hay negocio escalable.

Novedades 2026 que debes activar (ver `actualizacion-2026-06`): el **EMQ útil subió a 8+** (manda 8+ identificadores hasheados; en LatAm el **teléfono es oro**); existe **CAPI de un clic Meta-hosted** ("Activate Conversions API" en Events Manager — pone el `event_id` para dedup solo); y Meta **quitó las ventanas view-through de 7/28 días** (12-ene-2026) → tu estándar de juicio es **7d-click / 1d-view**. Verifica todo en Events Manager (ver 62) ANTES de lanzar.

## Estructura por madurez — la cuenta concreta

| Etapa | Campañas | Tipo / objetivo | Creativos | Medición clave | COP/día |
|---|---|---|---|---|---|
| **Arranque** (0-50 ventas/mes) | 1× Advantage+ Sales | broad, presupuesto a nivel campaña, cap de clientes existentes 25-30% (ver `actualizacion-2026-06`) | 6-8 conceptos distintos en ángulo (ver 38) | Purchase + valor, CPA vs breakeven | $40k-$120k |
| **Creciendo** (50-300 ventas/mes) | 1× Advantage+ Sales (caballo) · 1× testing manual de creativos (ver 17) · 1× DPA retargeting (ver 56) | Sales broad · ABO testing · catálogo dinámico al carrito/PDP | 10-15 conceptos vivos (Entity ID los colapsa si son casi-iguales, ver `actualizacion-2026-06`) | ROAS real con rechazos restados (ver 64) | $120k-$500k |
| **Maduro** (300+ ventas/mes) | Advantage+ Sales principal · manual para lanzamientos/drops · DPA full-funnel · prospecting de catálogo | + Minimum ROAS / ROAS Goal cuando haya 100+ compras con valor (ver 15) | refresco semanal; vida útil del ad bajó a ~2-4 semanas | incrementalidad + geo-holdout (ver 65) | $500k+ |

No saltes etapas: Advantage+ Sales sin volumen de señal es un Ferrari sin gasolina. Y **1 campaña de $100k le gana a 10 de $10k**: fragmentar mata la señal (ver 10, 24).

## Creativos que venden producto físico (10-15 conceptos vivos)

- **Demo en uso**: el producto resolviendo el problema en video real, resultado en los primeros 3 segundos (ver 37).
- **Unboxing**: abrir la caja como el cliente — vende la experiencia de recibir.
- **UGC reseña** (ver 32): cliente real o creator contando qué cambió. El formato más rentable del e-com 2026.
- **Antes/después** solo si la categoría lo permite (ver 44 — en cosmética/salud es campo minado, ver 83; en limpieza u organización, perfecto).
- **Estática con oferta dura** (ver 35): foto impecable + precio/descuento/envío gratis en texto grande. Aburrida y efectiva.

Volumen: refresca cada 2-4 semanas porque la vida útil del ad cayó (ver 39). Usa el **Advantage+ Creative Suite** (image-to-video con hasta 20 fotos de producto, variaciones de texto, generación de fondo — vivo en Ads Manager, ver `actualizacion-2026-06`) para multiplicar variantes, pero el concepto sigue siendo humano. Anuncios con visuales 100% IA deben llevar etiqueta (política 2026).

## AOV: la palanca oculta

AOV (Average Order Value: ticket promedio). Subirlo 30% cambia TODA la matemática sin tocar un anuncio: si pasa de $80.000 a $104.000 con el mismo CPA, tu ROAS sube 30% gratis. Y el algoritmo de Sales premia AOVs más altos con mejor entrega. Palancas (ver 41):

- **Bundle/combo**: "kit de 3" con descuento — ya decidió comprarte, véndele más en el momento.
- **Umbral de envío gratis**: "envío gratis desde $120.000" cuando tu AOV es $90.000 — la gente agrega para llegar.
- **Upsell post-compra** en la página de gracias.

Antes de pelear por bajar el CPA $2.000, sube el AOV $20.000: es más fácil.

## Contraentrega: arma y riesgo (Colombia)

La contraentrega (pago al recibir) sube la conversión brutalmente — quita el miedo a pagar online. Pero tiene un costo oculto: el **% de rechazo en puerta** (pedidos que el cliente no recibe/no paga). Mídelo religiosamente: un 15% de rechazo se come el margen de la pauta. Mitigación: confirmación del pedido por WhatsApp antes de despachar (tu bot sirve aquí), cobro parcial por **Nequi/PSE** como anticipo en zonas de alto rechazo. Mete el rechazo en tu ROAS real (ver 64) — el ROAS de plataforma miente si no lo restas.

## Ofertas tipo del vertical

- **Envío gratis desde $X** (X = AOV objetivo): la oferta que sube ticket en vez de bajar margen.
- **Kit/combo de temporada**: "set de 3 con 15% off" — sube AOV y rota inventario.
- **Primer pedido -10% + envío gratis**: adquisición; el costo real es el descuento, no regalar el producto.
- **Recompra/anticipo Nequi** en alto rechazo: convierte sin tragar devoluciones.
- Descuento permanente del 20% NO es oferta: es tu precio nuevo (ver 41).

## Benchmarks honestos (e-com LatAm, referenciales)

- CVR web (visitas → compra): **1-3%**. Menos de 1% = problema de tienda u oferta, no de pauta.
- CPM Colombia: **$8.000-$25.000 COP** por mil impresiones según nicho/competencia.
- Costo por compra: depende tanto de AOV y categoría que cualquier número sin contexto es ruido.
- ROAS breakeven: se calcula desde TU margen (ver 64). Margen 50% → breakeven ROAS 2.0; margen 30% → 3.3. Conócelo antes de celebrar. Caveat permanente: estos rangos son brújula, no meta.

## Velocidad y checkout: el multiplicador silencioso

Una tienda que carga 6 segundos en datos móviles quema la mitad de tus clics antes de mostrar nada. Checkout con 8 campos y registro obligatorio mata otro tanto. La pauta amplifica lo que la tienda ES: optimiza velocidad y checkout primero (desingweb-lushows 11/21). Test rápido: abre tu tienda en tu celular con 4G — si te desespera a ti, desespera al cliente. La congruencia ad→landing es parte del CVR (ver 48).

## Calendario de promos

El e-com vive de picos: arma el año con anticipación (ver 19/77) — Hot Sale, Black Friday/BlackDays, Navidad, día de madre/padre, quincenas. Regla: la campaña de la promo se monta 5-7 días antes para salir de aprendizaje; el creativo se produce con 3 semanas de anticipación.

## Ruteo a skills hermanas

Cierre por WhatsApp del carrito abandonado y objeciones de precio → ventas_lushows. Tienda/PDP/checkout que convierten → desingweb-lushows. Foto de producto y marca que separa de un revendedor → directorcreativo_lushows. Margen, breakeven y unit economics → economist_lushows. Captura de intención de compra en Google Shopping → google_ads; UGC/TikTok Shop como segundo canal → tiktok_ads.

## Errores comunes — blacklist

- Pautar sin Purchase con valor configurado: vuelas a ciegas y el algoritmo también.
- Optimizar por AddToCart "porque Purchase no tiene volumen" de forma permanente: trae llenadores de carrito, no compradores (ver 14).
- Celebrar el ROAS de plataforma sin restar rechazos de contraentrega, devoluciones y envío (ver 64).
- 10 campañas de $10.000/día en vez de 1 de $100.000: fragmentas la señal (ver 10, 24).
- Juzgar retargeting por view-through cuando Meta ya lo quitó del reporte (ver `actualizacion-2026-06`).
- Dejar el cap de clientes existentes en 100% y celebrar un ROAS inflado por retargetear a quien ya iba a comprar.
- Descuento permanente del 20%: deja de ser oferta y se vuelve tu precio (ver 41).
- Escalar un ganador duplicando presupuesto de golpe: 20-30% cada 2-3 días (ver 70).
- Tienda lenta + checkout hostil + pauta agresiva: pagar por mostrar tu peor cara más rápido.

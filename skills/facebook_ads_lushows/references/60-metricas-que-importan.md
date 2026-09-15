# 60 — Las métricas que importan (y las que no)

Este módulo es tu diccionario de métricas con criterio: qué significa cada una, qué rango es normal y —lo más importante— qué decisión informa. Léelo antes de tocar el Ads Manager por primera vez y vuelve cada vez que dudes "¿este número está bien o mal?". Regla de oro: una métrica solo importa si cambia una decisión. Todo lo demás es ansiedad con tablero. Actualizado jun-2026 (ver `actualizacion-2026-06` para el changelog que afecta cómo se REPORTAN estas métricas: view-through casi extinto, atribución incremental, retención recortada).

## Las 4 capas (de la subasta al banco)

Todo lo que mides vive en una de estas capas. El error clásico es juzgar la capa equivocada (ver 61 para diagnóstico completo). La señal viaja de arriba (subasta) hacia abajo (tu cuenta bancaria); cada capa multiplica o destruye lo que la anterior produjo.

### Capa 1: ENTREGA — ¿cuánto te cuesta aparecer?
- **CPM** (costo por mil impresiones): el termómetro de la subasta. Sube por competencia (temporada, vertical saturada), audiencia estrecha, o calidad de cuenta/creativo penalizada. En Colombia: e-com masivo suele moverse en COP $8.000–$35.000; lead gen/nichos B2B puede superar $60.000. Varía MUCHO por vertical, país y época — Q4 (octubre–diciembre) puede duplicarlo. El CPM no es bueno ni malo por sí solo: es bueno o malo RELATIVO a tu margen (un CPM de $40.000 es ganga si vendes algo de $500.000 de margen).
- **Frequency** (frecuencia = impresiones ÷ alcance): >3-4 en prospección en una semana = estás quemando la misma gente (fatiga, ver 39). En 2026 la frecuencia en el reporte solo retiene **6 meses** de histórico (antes más); descárgala si la necesitas para series largas.
- **Alcance**: personas únicas. Conteos únicos ahora retienen solo **13 meses** en el API (ver `actualizacion-2026-06`). Útil para detectar audiencias agotadas o campañas de awareness.

### Capa 2: ATENCIÓN — ¿el anuncio funciona como anuncio?
- **CTR outbound** (clics salientes al sitio ÷ impresiones): ¿el ad genera acción? Rango típico 0.5%–2% según vertical/oferta (caveat: ofertas calientes o CTWA pueden ir más arriba; B2B frío más abajo). <0.5% sostenido = el creativo no conecta. Ojo: usa CTR **outbound** (clic que SALE a tu destino), no el CTR "todo" que infla con clics a la foto, "ver más" y el perfil.
- **Thumbstop ratio** (reproducciones de 3s ÷ impresiones, en video): ¿el hook detiene el scroll? Referencia honesta: 20–30% decente, >35% bueno. Esta métrica no viene como columna directa — se calcula (ver 63, 68).
- **Hold rate** (% que llega a 15s o al 50% del video): ¿sostiene la atención después del hook? (ver 68 para usarlas en decisiones de creativo). En la era GEM (el modelo que evalúa el ad dentro del journey completo, ver `actualizacion-2026-06`) la retención de video pesa más que nunca.

### Capa 3: CONVERSIÓN — ¿el clic se vuelve plata?
- **CVR de landing** (compras ÷ clics al sitio): e-com típico 1–3%; si vendes por WhatsApp, tu "CVR" es conversaciones que terminan en pedido (mídelo en tu CRM de chat, ver 53). Para CTWA: pedidos cerrados ÷ conversaciones iniciadas.
- **CPA** (costo por adquisición = gasto ÷ compras): el número que comparas contra tu margen. Es el rey operativo de esta capa.
- **ROAS** (retorno = ventas atribuidas ÷ gasto): útil entre campañas, inflado como verdad financiera (ver 64). En 2026, si activas **atribución incremental**, este número REPORTA MENOS (solo cuenta lo causado) — bájale la ansiedad: es más honesto.
- **AOV** (ticket promedio = ventas ÷ # pedidos): palanca olvidada — subir AOV con combos baja la presión sobre el CPA sin tocar la pauta.

### Capa 4: NEGOCIO — ¿la empresa gana?
- **MER** (ventas totales del negocio ÷ gasto publicitario total): el que no miente (ver 64). No depende de atribución.
- **nCAC** (costo de adquirir un cliente NUEVO, excluyendo recompras).
- **Margen bruto**: sin esto no puedes fijar ROAS objetivo. El modelado de viabilidad/unit economics es de **economist_lushows** — rutea ahí cualquier cálculo de margen, punto de equilibrio o LTV.

## ¿Qué miro según qué decido?

| Decisión | Métricas que mandan | Las demás (ignóralas aquí) |
|---|---|---|
| ¿Mato o escalo un ad? | CTR outbound + CPA/ROAS del ad (ver 68) | CPM casi igual entre ads del mismo ad set |
| ¿Tengo problema de cuenta/subasta? | CPM vs tu histórico y vs otras campañas | CTR no te dice nada aquí |
| ¿El problema es la landing/oferta? | CVR (clics buenos que no compran) | El ad puede estar perfecto |
| ¿El negocio va bien? | MER + nCAC + margen | El ROAS de plataforma solo, jamás |
| ¿Escalo presupuesto este mes? | MER tendencial al subir gasto (ver 65) | El ROAS de una sola campaña |

## Métricas de vanidad — no deciden nada solas
- **Likes/comentarios/compartidos**: señal social, no venta. Sirven solo como pista cualitativa (lee los comentarios para sacar objeciones y ángulos, no para decidir gasto).
- **Alcance e impresiones brutas**: gastar más siempre las sube. No es mérito.
- **CPC barato**: clics baratos de curiosos que no compran son carísimos. Mira CPA, no CPC. Un CPC de $200 con CVR 0% es infinitamente peor que un CPC de $2.000 que convierte.
- **ROAS de plataforma como cifra absoluta**: incluye view-through residual y modeled conversions (conversiones que Meta ESTIMA cuando no puede rastrear); compáralo, no lo prediques (ver 64, 65).

## Tabla maestra

| Métrica | Fórmula | Rango típico (caveat: varía por vertical/país/ticket) | Decisión que informa |
|---|---|---|---|
| CPM | (gasto ÷ impresiones) × 1000 | COP $8k–$60k+ | Salud de cuenta/subasta, temporada |
| Frequency | impresiones ÷ alcance | <3 prospección, <6 retargeting/sem | Fatiga, refrescar creativo |
| CTR outbound | clics salientes ÷ impresiones | 0.5%–2% | Vida o muerte del creativo |
| Thumbstop | 3s plays ÷ impresiones | 20–35% | Calidad del hook |
| Hold rate | 15s plays ÷ 3s plays | 25–50% | Calidad del cuerpo del video |
| CVR landing | compras ÷ clics | 1–3% e-com | Landing/oferta (ver 48) |
| CPA | gasto ÷ compras | depende de TU margen | Rentabilidad por campaña |
| ROAS | ventas atribuidas ÷ gasto | objetivo = según margen (ver 64) | Comparar campañas entre sí |
| AOV | ventas ÷ pedidos | tu histórico | Combos, upsell, presión sobre CPA |
| MER | ventas totales ÷ gasto total | >2–4 según margen | Salud real del negocio |
| nCAC | gasto ÷ clientes nuevos | < margen del primer pedido (o LTV) | ¿Puedo pagar por crecer? |

## Ejemplo resuelto — bajando una capa a la vez

Gastas COP $1.000.000, 50.000 impresiones → CPM $20.000 (capa 1, normal). 500 clics → CTR outbound 1% (capa 2, sano). 10 ventas de $120.000 promedio → CVR 2% (capa 3, ok), CPA $100.000, AOV $120.000, ROAS de plataforma 1.2. Si tu margen bruto es 60% ($72.000/pedido), pierdes $28.000 por venta: el ad "funciona" en atención y conversión, pero la matemática de negocio no cierra (capa 4 rota). Conclusión: el fix NO es otro creativo — es subir AOV con un combo, subir precio, o bajar costo (economist_lushows). Sin la capa 4, hubieras "optimizado" un motor que pierde plata más rápido.

Segundo ejemplo (triangulación rápida): mismo gasto, Ads Manager reporta ROAS 4 ($4M atribuidos) pero el backend solo registró $2.6M de ventas reales esa semana → factor de inflación 1.54×. Tu MER real es 2.6, no 4. Reportas y decides con 2.6 (ver 64).

## Hermanas y ruteo
- **Modelado de margen, breakeven, LTV, punto de equilibrio** → economist_lushows.
- **Cierre del lead en chat** (la conversación que no se vuelve pedido) → ventas_lushows + módulo 53.
- **La landing que mata la CVR** → desingweb-lushows (CRO).
- **Comparar contra Google/TikTok** → google_ads_lushows / tiktok_ads_lushows usan su propia caja de métricas; el MER total del negocio los suma a todos (ver 64).

## Errores comunes — blacklist
- Juzgar un ad por likes o por CPC barato en vez de CPA/ROAS.
- Comparar tu CPM contra benchmarks de gurús de otro país/vertical y entrar en pánico.
- Declarar muerto un ad con 2 días y COP $30.000 gastados (mínimo 1–2× CPA de gasto antes de juzgar, ver 68).
- Mirar ROAS de plataforma como si fuera el estado de resultados (ver 64).
- Optimizar CTR cuando el problema real es la landing (CVR) o el margen (capa equivocada, ver 61).
- No conocer tu margen bruto y aun así fijar "ROAS objetivo 3" porque lo dijo un video.
- Usar CTR "todo" (infla con clics a foto/perfil) en vez de CTR outbound y creerte que tu creativo es mejor de lo que es.
- Asustarse porque la atribución incremental "bajó las ventas": no bajaron, dejaron de contarse las que no causaste (ver `actualizacion-2026-06`, 65).

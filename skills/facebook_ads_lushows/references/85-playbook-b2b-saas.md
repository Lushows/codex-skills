# 85 — Playbook: B2B y SaaS en Meta

"Facebook no sirve para B2B" es mentira a medias. Meta NO es LinkedIn: no segmentas por cargo ni empresa con precisión. Pero cuando tu cliente es una **pyme/SMB** — el dueño de restaurante, la dueña de la tienda, el gerente del taller — esa persona ES usuario de Facebook e Instagram, y ahí scrollea relajada, no en modo "véndeme algo" como en LinkedIn. Para SaaS tipo AVISPA'O o FACTUM (cumplimiento/facturación a pyme) y GASTROWHATS, Meta es canal principal. Para enterprise (vender a bancos, multinacionales): no — ahí es LinkedIn + outbound (ventas_lushows). Este es el playbook de FACTUM/AVISPA'O: lead ads + chat calificador + OCI-equivalente (CAPI de leads de calidad).

## Cuándo Meta para B2B

✅ Cliente = dueño/decisor de pyme, profesional independiente, emprendedor. Ticket de suscripción $50.000-$2.000.000 COP/mes o servicios B2B a pyme. ❌ Cliente = comité de compras corporativo, ciclos de 12 meses con licitación.

## El funnel B2B en Meta (ver 27)

```
Creativo auto-filtrante → lead magnet de valor real → captura (form o CTWA)
  → nurturing (semanas) → demo/llamada → cierre (ventas_lushows)
```

1. **Creativo auto-filtrante** (ver 37): como no puedes segmentar "dueños de restaurante", el creativo lo hace: **"Si tienes un restaurante en Colombia…"** en el primer segundo. El que no tiene restaurante no hace clic — y eso es lo que quieres: el copy es tu targeting (ver 30).
2. **Lead magnet de valor real** (ver 88): plantilla de costos, calculadora ("¿cuánto pierdes al mes por X?"), guía descargable, checklist de cumplimiento, demo grabada. Tiene que resolver algo HOY.
3. **Captura**: **Instant form con filtro** (ver 52) — 1-2 preguntas calificadoras obligatorias ("¿Cuántos empleados tiene tu negocio?", "¿Usas factura electrónica?") que espantan curiosos — o **CTWA directo** (ver 50) a conversación consultiva con bot que califica y agenda. En LatAm pyme CTWA suele ganar: el dueño vive en WhatsApp.
4. **Nurturing**: el ciclo B2B es de semanas/meses. Secuencia de WhatsApp/email (ver 96) con valor (casos, tips, mini-clases), no con "¿ya te decidiste?". El lead de hoy compra en 60 días: el sistema de seguimiento ES el funnel.
5. **Demo/llamada y cierre**: oficio de ventas_lushows.

Novedades 2026 (ver `actualizacion-2026-06`): **Advantage+ Leads** automatiza la campaña de lead-gen; la **doble ubicación de conversión** sirve instant form a los rápidos y form web a los que buscan contexto (Meta reporta −60% CPL / +125% volumen vs solo-web); y hay **calificación de leads con IA + verificación** integradas al form.

## El OCI-equivalente: la señal de calidad de vuelta (ver 06/53)

La pieza que separa al B2B amateur del serio: **reportar a Meta la calidad del lead**, no solo que llegó. Equivalente a las "Offline Conversions" de Google. Dispara eventos CAPI escalonados — `lead` → `lead_calificado` → `demo_agendada` → `cliente` — con el `value` de la suscripción. Así el algoritmo deja de optimizar por "formularios llenos" y aprende a traer **decisores que pagan**. En CTWA, captura el `ctwa_clid` y manda `action_source = business_messaging` cuando el lead califica/paga. Sin esto, Meta te llena de curiosos baratos.

## La cuenta concreta

| Campaña | Tipo | Objetivo | Creativos | Medición | % presup. |
|---|---|---|---|---|---|
| **Adquisición** | Advantage+ Leads o Engagement→WhatsApp | lead calificado (CAPI) | 3-5 ángulos auto-filtrantes (dolor con números, costo de no resolver, caso de par) | costo por **lead calificado** | 70-80% |
| **Retargeting largo** | Leads / tráfico, 90-180 días | demo agendada | casos de cliente · objeciones en video · la demo | costo por demo | 15-25% |
| **Re-engagement** | Engagement→WhatsApp | reactivar leads fríos | "sigue abierto el cupo" · novedad de producto | reactivaciones | 5-10% |

## Ángulos B2B que funcionan (ver 38)

- **El dolor operativo con números**: "Cada mes que tu restaurante no responde WhatsApp en 5 minutos, pierdes ~30 pedidos. Eso son $2.4M."
- **El costo de no resolver**: "Una multa de Sayco-Acinpro arranca en $X. La inspección no avisa." (el ángulo madre de cumplimiento de AVISPA'O).
- **Caso de cliente par**: "Cómo un restaurante en Medellín como el tuyo pasó de 40 a 130 pedidos/mes" — el pyme cree en pares, no en logos corporativos.
- **Demo del producto en 15 segundos**: pantalla real, problema → clic → resuelto.
- **Founder-led content** (ver 32): la cara del fundador explicando por qué construyó esto. Pyme le compra a personas.

## Presupuesto, costos y ofertas (Colombia)

- Arranque: **$30.000-$100.000 COP/día**.
- **El lead B2B es más caro y está bien**: lead calificado $15.000-$80.000+ COP; CPM B2B $12.000-$30.000. La matemática se hace contra el **LTV de la suscripción**: un cliente de $150.000/mes con 18 meses vale $2.7M — un CAC de $400.000 es excelente (economist_lushows para CAC/LTV/payback). Caveat: el filtro del form mueve el CPL 3x en cualquier dirección.
- Evalúa al final del funnel: costo por demo → por cliente, no por lead (ver 64).
- Ofertas tipo: **prueba gratis 14 días**, **diagnóstico/auditoría gratis** ("revisamos tu cumplimiento sin costo"), **primer mes -50%**, **plan anual con 2 meses gratis** (sube LTV y baja churn), **migración asistida gratis**.

## Retargeting largo

El B2B madura lento: ventanas de 90-180 días (ver 23) sobre visitantes web, video viewers 50%+ y leads que no agendaron. Contenido: casos, objeciones en video, la demo. Recuerda que view-through ya no se reporta (ver `actualizacion-2026-06`) — juzga por 7d-click y por leads calificados, no por impresiones.

## Compliance específico

Si tu SaaS toca crédito, financiación o empleo, puede caer en **special ad categories** (ver 87/08) — decláralo (el enforcement de HEC es más duro en 2026). Claims de resultados de negocio ("aumenta tus ventas 40%") necesitan ser defendibles: usa casos reales con cifras reales o rangos honestos (ver 44).

## Ruteo a skills hermanas

Descubrimiento, demo, objeciones y cierre consultivo → ventas_lushows. Landing B2B con dolor + demo + prueba social de pares → desingweb-lushows. Identidad de producto y founder brand → directorcreativo_lushows. Modelo financiero, CAC/LTV, pricing del SaaS → economist_lushows. Captura de intención "software facturación electrónica" → google_ads (Search es oro en B2B); demo nativa y founder content → tiktok_ads.

## Estructura recomendada resumida

- 1 campaña Advantage+ Leads o Engagement→WhatsApp, broad, 3-5 ángulos auto-filtrantes (el grueso del presupuesto).
- 1 campaña de retargeting 90-180d con casos y demo (15-25%).
- Nada más hasta tener 50+ clientes pagos: la complejidad antes del product-market fit es procrastinación cara.
- Señal de calidad de vuelta a Meta vía CAPI (el OCI-equivalente de arriba): el upgrade que cambia todo.

## Errores comunes — blacklist

- Pedir "agenda una demo" en frío sin lead magnet: nadie agenda con desconocidos.
- Instant form sin preguntas de filtro: 200 leads de curiosos que ventas aprende a ignorar.
- Llamar al lead 3 días después: el B2B también se enfría — contacto el mismo día (ver 52).
- Evaluar la pauta por CPL a la semana 1 cuando el ciclo es de 60 días.
- Copy corporativo ("soluciones integrales para optimizar procesos"): el dueño de pyme habla plata, tiempo y multas.
- Targeting por "interés: emprendimiento" en vez de creativo auto-filtrante: te trae soñadores, no dueños.
- No reportar la calidad del lead a Meta (CAPI escalonado): el algoritmo optimiza hacia formularios baratos inútiles.
- No tener nurturing: capturas leads para que mueran en un Excel.

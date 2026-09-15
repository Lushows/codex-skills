# 98 — Playbook de lanzamiento

Lee este módulo cuando arranques una cuenta de Google Ads desde cero y necesites saber QUÉ hacer cada semana sin perderte, o cuando quieras un plan ordenado en vez de "lanzar y ver qué pasa". Este es el camino del día 1 al día 90: cimientos primero, marca y genérico después, frenos, expansión y escala. La regla que gobierna todo: **no se pasa a la semana siguiente sin cerrar la anterior.** El error #1 de los novatos es saltarse la medición y la marca para "lanzar ya"; eso entierra plata y le da datos basura al algoritmo (ver 13). Marco: Google **captura intención** — el playbook construye primero la tubería de medición, luego la captura barata (marca), luego la genérica, y solo al final suelta la IA (PMax/AI Max).

## Antes del día 1: el diagnóstico (no se salta)

Responde con honestidad brutal (ver 00, 07):
- ¿La gente **busca** tu categoría? (Keyword Planner, ver 20). Si no → esto es trabajo de Meta/TikTok primero (ver 03, 97).
- ¿Cuál es el **CAC máximo** que aguanta el negocio? (rutea a `economist_lushows`). Sin ese número no sabes si un CPA es bueno.
- ¿La venta **cierra por WhatsApp/llamada/web**? Define dónde cae el lead y quién cierra (ver `ventas_lushows`).
- ¿Cuánto presupuesto **real** tienes/mes? Sé honesto; con $300.000 COP/mes no haces lo mismo que con $5.000.000.
- ¿Tienes **verificación de anunciante** lista para hacer con datos reales? (ver 93). Empieza ya, tarda días.

## El plan de 90 días, semana a semana

### Semanas 1–2 · Cimientos y medición
**Nada se lanza sin esto (ver 04, 05, 06).**
- Crear cuenta + MCC (si manejas clientes, ver 95).
- **Verificación de anunciante** completa (ver 93) — empieza ya, tarda.
- Google tag + GA4 instalados y probados (dispara una conversión de prueba y confírmala).
- **Conversiones definidas**: la VENTA real, no el clic a WhatsApp (ver 64). Si cierras offline, planea OCI y captura de GCLID desde ya (ver 53, 96).
- **Enhanced Conversions + Consent Mode v2** activos (ver 06).
- Lista maestra de **negativos veneno** lista para aplicar (gratis, empleo, pdf, "como hacer", "qué es", ver 22).
- Landing revisada: carga rápido, coincide con el anuncio, convierte, tiene info de negocio visible (rutea a `desingweb-lushows`).

**Cierre semana 2:** si la medición no está confirmada, NO avanzas. Punto.

### Semanas 3–4 · Search marca + Search genérico
- **Campaña de marca** (tu nombre): barata, defiende tu marca de competidores que te pujan, captura al que ya te busca (ver 39, 94). Sepárala y mídela aparte.
- **Campaña Search genérico** con keywords de **intención comercial** en concordancia exacta/frase (ver 20, 21): "comprar X", "X precio", "X Bogotá/Colombia". Empieza acotado, no broad ni AI Max todavía.
- RSA bien hechos: titulares con tu propuesta, no genéricos; mete precio en COP y ciudad (ver 30, 31).
- Puja: empieza en **manual/maximizar clics** o tCPA conservador solo si ya tienes señal; con cuenta nueva sin conversiones, NO arranques con tROAS (no tiene de qué aprender, ver 13).
- Presupuesto modesto, **calienta la cuenta** (ver 93): no quemes el máximo el día 1.

### Semanas 5–6 · Negativos y limpieza (la palanca #1)
- **Revisa términos de búsqueda 2–3 veces esta etapa** (ver 22). Aquí es donde la cuenta se vuelve rentable o no.
- Agrega negativos de todo lo que no compra. Convierte búsquedas ganadoras nuevas en keywords propias.
- Ajusta RSA según qué titulares rinden; fija los buenos (ver 31).
- Empieza a ver el **CPA real** vs tu CAC máximo. Mata keywords que gastan sin convertir (ver 70).
- Si ya juntaste **≥30 conversiones/mes**, considera pasar a **Smart Bidding tCPA** (ver 13, 15).

### Semanas 7–9 · Expandir (PMax / AI Max / Demand Gen)
**Solo si las semanas 1–6 dejaron señal de conversión LIMPIA.**
- Si tienes catálogo/e-commerce: **PMax retail** con Merchant Center (ver 35) — su mejor caso.
- Si quieres más alcance sobre Search ganador: **AI Max for Search** con blindaje (negativos + brand exclusions + URLs controladas + assets fijados, ver 90). Revisa search terms 2x/semana al activarlo.
- Para llenar el funnel: **Demand Gen** (ver 41) con audiencias de Customer Match (ver 25).
- **SIEMPRE brand exclusions y negativas a nivel campaña en PMax** (ver 39, 90): que no canibalice tu marca ni infle el ROAS (ver 65).
- Empieza a cargar **Customer Match** desde tu CRM y a excluir compradores (ver 96, 25).

### Semanas 10–13 · Escalar sin romper
- Sube presupuesto **gradual** (no dupliques de golpe, reinicia aprendizaje, ver 73).
- Mueve tCPA/tROAS en pasos chicos (~10–15%) y **espera ~2 semanas** entre cambios (ver 13, 15).
- Cierra el loop: **OCI subiendo ventas reales** a Google con el GCLID (ver 53, 96) → el algoritmo va por más clientes como los que compraron.
- Gobierna por **MER global** si ya pautas multicanal (ver 97); mide incrementalidad de marca/PMax (ver 65).
- **Reporte ejecutivo** mensual en PDF (ver 99): inversión, conversiones, CPA, MER, qué se hizo, qué sigue.

## Checklist de "está listo para escalar"

| Señal | ¿Listo? |
|---|---|
| Medición confirmada (conversiones reales, no clics) | obligatorio |
| ≥30 conversiones/mes de señal limpia | para Smart Bidding/PMax/AI Max |
| CPA real ≤ CAC máximo del negocio | obligatorio para escalar |
| Negativos revisados cada semana | rutina viva |
| Brand exclusions + negativas a nivel campaña activas en PMax | obligatorio |
| OCI cerrando el loop con ventas reales | el diferenciador |
| Customer Match excluyendo compradores | recomendado (clave en pago único) |

## Calendario LatAm: cuándo apretar y cuándo soltar

| Momento | Acción |
|---|---|
| Quincenas / día de pago (Colombia: ~15 y 30) | Sube presupuesto; hay liquidez |
| Hot Sale / Black Friday / Cyber (nov) | Prepara desde oct: presupuesto, creativos, negativos limpios (ver 19) |
| Navidad / fin de año | Intención alta; defiende marca, sube tope |
| Enero (cuesta de enero) | Recorta; baja intención de compra, no quemes |

Detalle de estacionalidad en 19. La regla: aprieta cuando hay liquidez e intención, suelta cuando no.

## Presupuesto vs ambición: qué es realista por nivel

Con presupuesto chico no intentes el plan completo de golpe; concentra donde Google rinde más por peso:

| Presupuesto/mes (COP) | Hasta dónde llegar | Qué NO intentar todavía |
|---|---|---|
| $300.000 – $800.000 | Search marca + 1 campaña genérica exacta/frase, negativos | PMax, AI Max, Demand Gen (no hay oxígeno) |
| $800.000 – $2.000.000 | Lo anterior + tCPA si hay ≥30 conv/mes + Customer Match | PMax sin señal limpia |
| $2.000.000 – $5.000.000 | + PMax retail o AI Max con blindaje + Demand Gen | Escalar sin OCI cerrado |
| $5.000.000+ | Multicanal con MER, OCI, incrementalidad | — |

El error de presupuesto chico es repartirse en 5 campañas y no juntar señal en ninguna. **Concentra**: una campaña que junta 30 conversiones aprende; cinco que juntan 6 cada una, ninguna aprende (ver 13). Y nunca escales un CPA que ya está por encima de tu CAC máximo — escalar multiplica la pérdida (ver 64, `economist_lushows`).

## Errores comunes — blacklist

- **Saltarse las semanas 1–2 (medición) para "lanzar ya".** El error #1; el algoritmo aprende de datos basura y nunca optimiza bien (ver 13, 05).
- **Lanzar PMax/AI Max/Demand Gen en la semana 3** sin Search que genere señal limpia. Caja negra alimentada de basura (ver 90, 14).
- **Arrancar broad o AI Max el día 1 sin historial de negativos.** Quema presupuesto en búsquedas que no compran (ver 21, 22).
- **Poner tROAS en cuenta nueva sin conversiones.** No tiene de qué aprender; empieza manual/maximizar clics (ver 13).
- **No correr campaña de marca.** Dejas tu nombre desprotegido y regalas al cliente que ya te buscaba (ver 39, 94).
- **Escalar antes de tener CPA ≤ CAC máximo.** Escalas pérdidas, no ganancias; valida la economía primero (ver 64, `economist_lushows`).
- **Duplicar presupuesto de golpe.** Reinicia el aprendizaje; sube gradual ~10–15% (ver 73).
- **Olvidar capturar el GCLID desde la semana 1.** Sin él no hay OCI después y el loop nunca cierra (ver 96, 53).

# 96 — Benchmarks por industria

Un **benchmark** es un número de referencia que te dice si tu resultado es bueno, normal o malo comparado con el resto del mercado. Importa porque sin referencia estás ciego: un **reply rate** (tasa de respuesta) del 3% puede ser excelente o mediocre según a quién le escribes y por qué canal. Este módulo te da los rangos defendibles de 2026 para las métricas clave del outbound, **desglosados por sector y contexto**, para que sepas si tu campaña va bien o hay que arreglar algo — y dónde. Es la tabla de "¿mi número es bueno?" que usas junto al diagnóstico por métrica (ver `83`).

## El principio: el benchmark depende del contexto, no es universal

El mismo esfuerzo da números muy distintos según tres variables: **canal** (WhatsApp abre más que email frío), **tamaño de empresa objetivo** (pyme responde distinto que enterprise) y **calidad de lista/personalización** (lista quirúrgica personalizada bate a lista masiva genérica). Por eso un solo "buen reply rate" no existe. Regla: **compárate contra tu propio contexto, no contra el número de un caso de LinkedIn de otro país y otro sector.** Y cuando midas, que los números sean exactos → `Matematicas_lushows` (ver `05`, `80`).

## Las métricas que se benchmarquean

| Métrica | Qué mide | Dónde vive |
|---|---|---|
| **Reply rate** | % de contactados que responde (algo) | `80` |
| **Positive reply rate** | % de respuestas que son de interés real | `80` |
| **Meeting booked rate** | % de contactados que agenda | `81` |
| **Cost-per-meeting** | Cuánto te cuesta cada reunión agendada | `149` |
| **Reunión → SQL** | % de reuniones que califican de verdad | `72`, `81` |

## Benchmarks de reply rate por canal (2026)

| Canal | Reply rate sano | Notas |
|---|---|---|
| **Cold email** (bien hecho) | 3–8% | Con lista buena, deliverability sana y copy relevante (ver `40`, `52`) |
| Cold email genérico/masivo | <1% | Señal de lista o copy malos, o de estar en spam (ver `83`) |
| **LinkedIn** (connection + msg) | 15–30% aceptación, 5–15% responde | Más personal, menor volumen (ver `57`) |
| **Cold call** | 5–10% conecta a conversación | El número es de "conversaciones", no de ventas (ver `58`) |
| **WhatsApp frío** (LatAm, humano) | 10–25%+ | Alto pero frágil: riesgo de baneo (ver `47`, `59`, `93`) |

## Benchmarks por sector / tipo de negocio

| Sector / contexto | Reply rate email | Reuniones/mes por SDR | Notas |
|---|---|---|---|
| **SaaS mid-market** | 3–7% | 8–15 | Terreno rico en señales (ver `91`) |
| **SaaS enterprise** | 1–4% | 3–8 | Cuentas grandes, ABM, ciclos largos (ver `94`) |
| **Servicios / agencia (nicho)** | 5–12% | 4–10 (solista) | Lista pequeña personalizada bate volumen (ver `92`) |
| **Dev-tools (vender a técnicos)** | 2–5% | 6–12 | Audiencia escéptica al spam (ver `173`) |
| **Fintech / seguros** | 2–5% | 6–10 | Sector regulado, cuidado con compliance (ver `174`) |
| **Pyme LatAm (WhatsApp)** | 10–25% (WA) | varía | Ciclo corto, decisor único (ver `93`) |
| **Industrial / B2B tradicional** | 2–6% | 5–10 | Menos saturado de outbound, teléfono pesa (ver `176`) |
| **Reclutamiento / staffing** | 4–8% | 8–15 | Doble mercado (clientes y candidatos) (ver `178`) |

> Rangos de 2026 para outbound bien ejecutado (lista buena + deliverability sana + copy relevante). Tu número real depende de tu ejecución. Detalle por vertical en `170`–`179`.

## Cost-per-meeting (referencia)

El **costo por reunión** = todo lo que gastas (herramientas + dominios + tiempo/salario del SDR) dividido por reuniones agendadas en el periodo. Rangos muy variables, pero como orden de magnitud 2026:

- **Solista con stack básico** (Apollo + Instantly + dominios): el costo es sobre todo tu tiempo; en herramientas, decenas de dólares por reunión.
- **Con SDR pagado:** el salario domina; suele ir de USD 100 a 400+ por reunión calificada según sector y ticket.
- La pregunta que importa no es "¿es caro?" sino "¿el LTV del cliente lo paga?" — eso es economía de negocio → `economist_lushows`; el cálculo exacto → `Matematicas_lushows` (ver `149`).

## Cómo usar los benchmarks (no solo mirarlos)

1. **Mide tu número real** por etapa del funnel (ver `81`).
2. **Compáralo** contra la fila de tu sector/canal de arriba.
3. Si estás **por debajo**, usa el diagnóstico por métrica para saber dónde se rompe (ver `83`): reply bajo → lista o copy o deliverability; agenda baja → CTA o calificación.
4. Si estás **dentro o arriba**, no toques lo que funciona — escala (ver `89`).

## Errores comunes (qué NO hacer)

- Perseguir el benchmark de otro contexto ("un gurú dijo 15% de reply") y sentirte mal con un 5% que para tu sector es excelente.
- Optimizar reply rate ignorando el positive reply: 10% de respuestas donde todas dicen "quítame de tu lista" es un fracaso, no un éxito.
- Medir "correos enviados" como si fuera resultado. El resultado es la reunión calificada (ver `80`).
- No segmentar el benchmark por canal: mezclar email y WhatsApp en un solo promedio no dice nada.

## Siguiente paso

Saca tus números reales del último mes y compáralos fila por fila con la tabla de tu sector. Donde estés por debajo del rango, ve a `83` (diagnóstico por métrica) para encontrar la causa exacta. Para los anti-patrones que destruyen estos números ver `97`. Para el detalle por vertical, el Bloque 17 (`170`–`179`).

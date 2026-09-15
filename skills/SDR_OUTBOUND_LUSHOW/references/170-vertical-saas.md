# 170 — Vertical: SaaS (software B2B)

Este es el **playbook de campo** para prospectar software B2B por suscripción: a quién exactamente escribir, dónde sacar la lista, qué señal dispara el contacto y qué correo funciona. El módulo `91` te dio la estrategia (recurrencia, PLG, señales); aquí bajamos a lo operativo con filtros y plantillas listas para copiar. Si vendes SaaS, este es tu manual de tiraje diario.

## ICP típico del vertical

El comprador de SaaS depende del ticket y de a qué área le sirve. El patrón:

| Precio (ACV: valor anual del contrato) | Decisor real | Ciclo |
|---|---|---|
| **Self-serve / < $5k** | Líder del área que sufre el dolor (Head of X, gerente) | Días–semanas |
| **Mid-market $5k–$50k** | VP/Director del área + a veces Finanzas | 1–3 meses |
| **Enterprise > $50k** | Comité (área + IT + Seguridad + Compras) → ABM (`94`) | 3–9 meses |

Firmographics (`15`) que definen tu ICP SaaS: **tamaño** (empleados o headcount del equipo que usaría el producto), **etapa** (startup con ronda vs empresa establecida), **stack tecnológico** (technographics — qué herramientas ya usan), y **rol dueño del dolor** (a quién le arde el problema, no quién firma el cheque). Afina el ICP con `10`; construye el buyer persona y mapea el comité con `11`.

## Dónde encontrar las cuentas

- **LinkedIn Sales Navigator** (`26`): el filtro rey del SaaS. Combina "headcount growth", "job title" y "hiring on LinkedIn". Ejemplo de búsqueda booleana de puestos:
  ```
  ("Head of Customer Support" OR "Support Manager" OR
   "VP Customer Experience") AND NOT ("intern" OR "assistant")
  Filtros: Company headcount 51–500, Geography LATAM/US, Hiring
  ```
- **Apollo / Clay** (`25`, `31`): filtra por technographics — "usa Zendesk", "usa Salesforce", "usa Shopify Plus". Clay enriquece con datos de financiación y señales.
- **BuiltWith / Wappalyzer**: qué tecnología corre un sitio → lista de "usa X, así que necesita Y".
- **Crunchbase / Dealroom**: rondas de inversión recientes (empresa con capital fresco = presupuesto para software).
- **G2 / Capterra**: quién dejó review de tu competidor = candidato a displacement (`19`).
- **Product Hunt, comunidades, changelogs públicos**: quién lanzó producto, quién contrata.

## Señales / triggers propios del SaaS

El SaaS es el terreno **más rico en señales** — úsalas (detalle en `14`, `37`):

- **Ronda de inversión** (seed/A/B) → hay presupuesto y presión de crecer. Contacto en <1 semana.
- **Contratación en el área** que usaría tu producto (contratan 3 de soporte → el volumen creció).
- **Cambio de stack** (adoptaron/abandonaron una herramienta — technographic delta).
- **Uso de competidor** (review, caso público, integración listada) → ángulo "why switch".
- **PQL** (Product-Qualified Lead: se registró a tu trial/freemium y activó features) — la señal más caliente; no es frío, es una conversación tibia.
- **Nuevo directivo** (nuevo VP suele traer herramientas nuevas en sus primeros 90 días).

## Ángulo de mensaje que funciona

Regla de oro del SaaS en frío: **vende el resultado de negocio, no las features**. Nadie agenda por "tenemos dashboards en tiempo real"; agenda por "bajas el tiempo de respuesta 40% sin contratar más gente". Estructura: señal observada → problema que ese rol reconoce como propio → prueba corta (cliente parecido, número) → CTA de interés bajo (`54`, `55`).

```
Asunto: los 3 nuevos de soporte en {empresa}

Hola {nombre}, vi que {empresa} sumó 3 agentes de soporte este
trimestre. Cuando un equipo crece así de rápido, el tiempo de
primera respuesta suele dispararse antes de que los procesos
se acomoden — y eso pega en el CSAT.

Ayudamos a equipos de soporte de {sub-sector} a bajar la primera
respuesta ~40% sin sumar cabezas. {Cliente parecido} lo logró en
6 semanas.

¿Tiene sentido una llamada de 15 min para ver si aplica?
```

Para PQL el mensaje cambia por completo — no vendes, **ayudas**: "vi que te registraste y activaste {feature}; ¿te muestro cómo {cliente} sacó {resultado} con eso?".

## Canal preferido

**Email primario** (el SaaS vive en la bandeja profesional), **LinkedIn como segundo toque** (`57`) — muy efectivo con este público que vive en LinkedIn. Cold call (`58`) para mid-market/enterprise donde el ticket lo justifica. WhatsApp casi nunca en SaaS US/EU; sí en LatAm mid-market (`47`, `93`). Cadencia multicanal en `61`.

## Ratios esperables (2026)

| Métrica | Rango sano |
|---|---|
| Reply rate cold email | 3–7% mid-market · 1–4% enterprise |
| Positive reply | 20–40% de las respuestas |
| Reuniones/mes por SDR | 8–15 mid-market · 4–8 enterprise |

Comparativa completa en `96`; el cálculo de si el CAC aguanta tu ticket es decisión de negocio → `economist_lushows`, números exactos → `Matematicas_lushows`.

## Errores comunes

- Listar features en vez de vender el problema/resultado.
- Mandar lista fría cuando el SaaS está lleno de señales targeteables (`37`).
- Tratar un PQL como frío total: pierdes la conversación más caliente que tienes.
- Perseguir enterprise con tácticas de spray de mid-market → enterprise es ABM (`94`).

## Frontera y siguiente paso

Tú consigues y agendas la reunión. Cuando el prospecto entra en objeciones de precio, comparativa a fondo o negociación de contrato, eso es **cierre → `ventas_lushows`**. Estrategia SaaS completa en `91`; propuesta de valor por segmento en `18`; segmentación en `12`. **Siguiente paso:** elige un sub-vertical de SaaS (soporte, ventas, finanzas…), arma una lista de 200 cuentas con una señal común, y escribe una sola secuencia para ese segmento.

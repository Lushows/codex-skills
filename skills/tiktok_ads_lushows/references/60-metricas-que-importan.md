# 60 — Métricas que importan

Lee este módulo cuando abras Ads Manager y no sepas qué número mirar primero, cuando alguien te tire diez siglas y quieras saber cuál decide qué, o cuando un cliente te pregunte "¿cómo vamos?" y necesites contestar con datos, no con humo. Este módulo es el diccionario de medición de TikTok: qué mide cada métrica, **cómo se calcula**, qué rango es honesto en LatAm (jun-2026) y, sobre todo, **qué decisión toma cada una**. Es la base del bloque de medición (61–70). Frame que no se negocia: **TikTok es descubrimiento, no captura de demanda** (a diferencia de Google, que rutea a `google_ads_lushows`). La gente no te busca; tú interrumpes su scroll. Por eso el creativo es el 80% del resultado (ver 68, 30) y casi todas las métricas que importan son, en el fondo, **diagnóstico del creativo**.

## Las métricas que de verdad mueven la aguja

TikTok te muestra decenas de columnas. La mayoría son ruido. Estas son las que importan, en el orden en que el dinero se mueve por el embudo: subasta → creativo → oferta. Cada una con su fórmula, para que no la mires como magia.

| Métrica | Fórmula | Qué decide |
|---|---|---|
| **CPM** | (Gasto ÷ impresiones) × 1.000 | Si tu audiencia/subasta están caras (ver 09, 01) |
| **Thumbstop / hook rate** | Reproducciones de 2-3s ÷ impresiones | Si tu primer segundo (hook) sirve (ver 37). El #1 |
| **Hold rate / 6s view** | Reproducciones de 6s ÷ impresiones (o % visto promedio) | Si tu video retiene después del hook |
| **CTR** | Clics ÷ impresiones | Si tu video da ganas de actuar / oferta clara |
| **CVR** | Conversiones ÷ clics (o ÷ landing views) | Si tu oferta + landing + Shop convierten (ver 61) |
| **CPA / CPC** | Gasto ÷ conversiones (÷ clics) | El número que decide si ganas o pierdes |
| **ROAS** | Ingreso atribuido ÷ gasto | Rentabilidad… **pero infla** (ver 64) |
| **GMV** | Venta total generada (TikTok Shop) | El tamaño del negocio que mueves |
| **AOV** | GMV ÷ número de pedidos | Cuánto vale cada compra (entra al cálculo de margen) |
| **Frequency** | Impresiones ÷ alcance | Si vas a quemar la audiencia (fatiga, ver 39) |

Jerga: **CPM** = costo por mil impresiones, la "tarifa de entrada" a la subasta. **Thumbstop/hook rate** = el porcentaje de gente que frenó el dedo más de 2-3s. **Hold rate** = los que se quedaron hasta los 6s. **CVR** = conversion rate. **CPA** = costo por adquisición. **ROAS** = return on ad spend. **GMV** = gross merchandise value. **AOV** = average order value (ticket promedio). **Frequency** = veces que cada persona vio tu ad.

Regla de oro: **el thumbstop y el hold rate son el termómetro del creativo, y el creativo es el 80% del resultado** (ver 68). Si solo pudieras ver tres números, serían thumbstop, CPA y MER (no ROAS de panel — ver 64).

## La cadena del embudo en una ecuación

No memorices métricas sueltas; memoriza cómo se multiplican. Tu CPA sale de esta cadena, y cada eslabón es una métrica que puede romperse:

```
CPA = CPM ÷ 1000 ÷ (hook% × hold-factor × CTR × CVR)
```

En cristiano: para que una compra sea barata, mucha gente tiene que frenar (hook), quedarse (hold), hacer clic (CTR) y comprar (CVR), todo arrancando de un CPM bajo. Si el CPA está caro, **una de esas tasas se cayó**. El CPA aislado no te dice cuál; te dice *que* algo está mal, no *dónde* (eso es el módulo 61). Ejemplo numérico:

- CPM $10.000, hook 30%, hold-factor 0,5, CTR 1,5%, CVR 3% → CPA ≈ $10.000 ÷ 0,30 ÷ 0,5 ÷ 0,015 ÷ 0,03 ≈ **$14.800**.
- Subes solo el hook de 30% a 45% (mejor primer segundo, ver 37) → CPA baja a **$9.900**. Una sola palanca del creativo movió el costo por venta un 33%. Por eso el creativo es el 80%.

## Rangos honestos en LatAm (jun-2026)

Nadie te da estos números reales, así que aquí van. Varían por nicho, época (Q4 sube, ver 77) y calidad del creativo. Úsalos como semáforo, no como ley.

| Métrica | Mal | Aceptable | Bueno |
|---|---|---|---|
| **CPM** (Colombia, COP) | $30.000+ | $12.000–$25.000 | < $10.000 |
| **Thumbstop / hook rate** | < 20% | 25–35% | > 40% |
| **6s view rate / hold** | < 8% | 10–18% | > 20% |
| **CTR** (feed) | < 0,7% | 1–2% | > 2,5% |
| **CVR** (producto digital simple) | < 1% | 2–4% | > 5% |
| **Frequency** (semanal sano) | > 4 | 1,5–3 | — |

Dos verdades incómodas: (1) un thumbstop alto con CTR bajo significa "engancha pero no da ganas de actuar" → problema de oferta/CTA, no de hook. (2) Un CTR alto con CVR baja significa "clickbait" → la landing decepciona (ver 61, rutea `desingweb-lushows`). Y tres: en 2026 con Smart+ (ver 12) y la subasta más automatizada, el CPM puede subir mientras el CPA baja — no te asustes del CPM solo; mira el CPA y el MER al final de la cadena.

## Cómo se conectan (el embudo en una línea)

```
Impresión → (CPM) → ve 2s → (thumbstop) → se queda → (hold) → clic → (CTR) → compra → (CVR) → CPA → ROAS/GMV → MER
```

Cada flecha es una métrica que puede romperse. Diagnosticar es preguntar **en qué flecha se cae la gente** (ver 61). Métricas vanidad que NO deben guiar decisiones: impresiones totales, vistas totales, likes, seguidores ganados, "engagement rate". Se ven bonitas en un reporte y no pagan la nómina. Repórtalas solo como contexto (ver 67).

## Qué métrica usar para cada decisión

| Decisión | Métrica que manda |
|---|---|
| ¿Mato o escalo este creativo? | Thumbstop + CPA por creativo (ver 68) |
| ¿Subo presupuesto? | CPA estable bajo tu objetivo + MER sano (ver 72) |
| ¿La audiencia está cara? | CPM vs tu histórico |
| ¿El video aburre? | Hold rate / % visto |
| ¿La oferta o landing fallan? | CVR (ver 61) |
| ¿Estoy quemando a la gente? | Frequency subiendo + CPA subiendo (ver 39) |
| ¿El ticket aguanta el CPA? | AOV vs CPA y margen (rutea `economist_lushows`) |
| ¿Soy rentable de verdad? | MER triangulado con backend + banco (ver 64, rutea `economist_lushows`) |

## North-star según objetivo

No toda campaña se mide igual. Define tu **métrica norte** antes de abrir el panel:

| Objetivo de negocio | North-star | Métrica de apoyo |
|---|---|---|
| Venta directa / e-commerce | MER (ver 64) | CPA, AOV, CVR |
| TikTok Shop / GMV Max | GMV y ROAS Shop | AOV, CVR |
| Leads / WhatsApp (LatAm) | Costo por lead **calificado** | CPL, tasa de cierre (rutea `ventas_lushows`) |
| Descubrimiento / marca | Lift incremental (ver 65) | thumbstop, alcance único |

Ojo con el costo por lead barato: un CPL de $3.000 que no cierra es más caro que uno de $9.000 que sí. El lead se mide por lo que vende después, no por lo que cuesta entrar — el cierre vive en `ventas_lushows`.

## Errores comunes — blacklist

- **Mirar solo el CPA.** Te dice que algo falla, no dónde. Diagnostica por capas (ver 61).
- **Celebrar el ROAS de plataforma como verdad.** Infla por atribución generosa. Triangula con banco y MER (ver 64).
- **Decidir por likes, vistas o seguidores.** Métricas vanidad; no pagan. Decide por CPA/MER.
- **Ignorar el thumbstop.** Es el #1 del creativo y el creativo es el 80%. Míralo primero (ver 68).
- **Comparar tu CPM con el de otro país/nicho/plataforma.** No comparable. Compara contra TU histórico (no contra Meta — eso es `facebook_ads_lushows`).
- **No mirar frequency.** Subes presupuesto, la frequency se dispara, el CPA sube y no entiendes por qué (ver 39).
- **Confundir CTR alto con éxito.** Si la CVR está en el piso, es clickbait que quema plata (ver 61).
- **Optimizar a costo por lead sin medir el cierre.** Un lead barato que no compra es caro (rutea `ventas_lushows`).
- **No definir north-star antes de mirar.** Sin métrica norte, cada número te jala para un lado distinto.

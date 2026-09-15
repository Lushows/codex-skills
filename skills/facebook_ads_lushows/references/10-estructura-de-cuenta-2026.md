# 10 — Estructura de cuenta 2026

Cómo organizar campañas, conjuntos de anuncios (ad sets) y anuncios dentro de tu cuenta de Meta Ads. Lee este módulo ANTES de crear tu primera campaña o cuando tu cuenta sea un desorden de 15 campañas que nadie entiende. La filosofía 2026 es una sola palabra: **consolidación** — y en feb-2026 Meta la volvió casi obligatoria al **fusionar todo bajo Advantage+** (el "manual puro" desapareció como flujo separado; ahora la automatización viene encendida por defecto y tú la apagas por sección — opt-out, no opt-in — ver 90 y `actualizacion-2026-06`).

## Por qué consolidar (la física del asunto)

La jerarquía de Meta es: Campaña → Ad set (conjunto de anuncios: donde defines audiencia y presupuesto) → Anuncios (los creativos). El algoritmo aprende **por ad set**: necesita ~50 conversiones del evento de optimización en 7 días por ad set para salir de la fase de aprendizaje (ver 13). Si tienes 10 ad sets y generas 60 conversiones semanales, cada uno recibe ~6 y NINGUNO aprende. Si tienes 1 ad set, ese recibe las 60 y aprende bien.

Regla de oro: **pocas campañas, pocos ad sets, MUCHOS creativos**. Desde GEM (el modelo de recomendación que en 2026 sucede a Andromeda — el motor de ranking de anuncios de Meta, ver 92), la diversidad de creativos dentro de un mismo ad set es lo que le da al algoritmo material para encontrar audiencias distintas. **El creativo ES el targeting**: la segmentación ya no la haces tú con audiencias, la hacen tus anuncios. GEM lee cada creativo como una "puerta" a un tipo de persona; mientras más puertas distintas le des, a más gente puede llegar.

Número concreto 2026: **10-15 creativos genuinamente distintos** por campaña principal. No 12 variantes del mismo video (Meta los colapsa internamente bajo un mismo **Entity ID** — los reconoce como "el mismo anuncio" y compiten contra sí mismos sin sumar alcance). Vida útil de un creativo ganador: **2-4 semanas** antes de fatigarse (ver 39); por eso necesitas pipeline, no un lote único.

## Estructura recomendada por tamaño de inversión

### Micro (< $300 USD ≈ < $1.2M COP/mes)
```
CAMPAÑA ÚNICA (Ventas o Engagement-WhatsApp, presupuesto Advantage+ campaign budget = CBO)
└── Ad set 1: broad (solo país/ciudad + edad amplia, Advantage+ audience encendido)
    ├── Ad 1: video testimonio
    ├── Ad 2: imagen producto + precio
    ├── Ad 3: video demo/uso
    ├── Ad 4: carrusel beneficios
    └── Ad 5-6: variantes de hook del mejor
```
Nada más. No retargeting separado (no hay volumen), no testing separado (tu campaña ES el test). Rotas creativos: apagas el peor cada 1-2 semanas, metes uno nuevo. Con < $1.2M/mes ni intentes 15 creativos — 5-6 buenos rotando es lo realista (no hay presupuesto para alimentar más).

### Media ($300–$3.000 USD ≈ $1.2M–$12M COP/mes)
```
CAMPAÑA 1 — PROSPECTING (75-80% del presupuesto, CBO)
└── Ad set broad → 8-12 creativos distintos
CAMPAÑA 2 — RETARGETING LIGERO (10-15%, ABO)
└── Ad set: visitantes web 30d + engagers IG/FB 30d → 3-4 ads (oferta, prueba social, objeciones)
TESTING: dentro de Campaña 1 (creativos nuevos entran al mismo ad set)
  o un ad set ABO aparte con presupuesto fijo si los nuevos no reciben gasto (ver 17)
```

### Grande (> $3.000 USD/mes)
Portfolio: prospecting consolidado (1-2 campañas: ej. 1 Advantage+ Sales ver 12 + 1 manual broad de comparación), campaña de testing dedicada ABO, retargeting estructurado, y campañas separadas solo por las razones válidas de abajo. Detalle completo de escalado vertical en 72; producción de creativos en serie en 39.

## CBO vs ABO (en lenguaje 2026)

Meta renombró CBO a **Advantage+ campaign budget** (presupuesto a nivel campaña) y ABO sigue siendo presupuesto a nivel ad set. Misma mecánica de siempre:

- **CBO / Advantage+ budget**: defines el presupuesto en la campaña y Meta lo reparte entre ad sets según rendimiento. Úsalo para **escalar lo probado**: deja que la plata fluya al ganador.
- **ABO**: presupuesto fijo por ad set. Úsalo para **testear con control**: garantizas que cada variante gaste lo mismo y el test sea justo.

| Situación | Elige |
|---|---|
| Campaña principal de ventas con creativos probados | CBO (Advantage+ budget) |
| Test de 3 ángulos nuevos que deben gastar parejo | ABO |
| Retargeting pequeño con presupuesto fijo | ABO |
| Cuenta micro con 1 ad set | Da igual (es lo mismo) |

## Cuándo SÍ separar campañas (y cuándo no)

Separa solo si cambia algo estructural:
- **Ofertas/productos con economía distinta** (un producto de $50k COP y un servicio de $2M no comparten campaña: distinto CPA tolerable, ver 64).
- **Países distintos** (CPMs y monedas diferentes distorsionan el reparto CBO).
- **Funnels distintos** (venta directa web vs leads a WhatsApp: eventos de optimización diferentes, ver 14).
- **Prospecting vs retargeting** (presupuestos que no quieres que se mezclen).

NO separes por: género, edad, intereses, placement (ubicación), formato de creativo, ni "campaña de Instagram y campaña de Facebook". Todo eso lo resuelve mejor el algoritmo dentro de un solo ad set broad con Advantage+ placements (ubicaciones automáticas). Separar por placement en 2026 es regalarle al algoritmo menos inventario para optimizar.

## Tabla de decisión: ¿cuántas campañas debo tener?

| Tu situación | Campañas activas | Por qué |
|---|---|---|
| 1 producto, 1 país, vendo por WhatsApp, < $1.5M/mes | **1** | Todo el volumen a un solo cerebro de aprendizaje |
| E-com 1 catálogo, $1.5M–$12M/mes | **2-3** (prospecting + retarget + quizá testing) | Suficiente plata para alimentar capas |
| Multi-producto con economías distintas | **1 por economía** + retarget | CPA tolerable distinto no debe mezclarse |
| > $12M/mes, e-com maduro | **3-5** (Adv+ Sales, manual broad, testing, retarget, estacional) | Portfolio, ver 72 |

Si dudas, ten MENOS campañas. El error de la cuenta media siempre es de más, nunca de menos.

## Convención de nombres (para no perderte en 3 meses)

Nombra con un patrón fijo, ej: `[Objetivo]_[Audiencia]_[Fecha]` → `Ventas_Broad_Jun26`, `Retarget_Web30d_Jun26`, `Test_AnguloDolor_Jun26`. A nivel ad: `[Formato]_[Ángulo]_[v#]` → `Video_Testimonio_v3`. Sin convención, en la fila #20 ya no sabes qué es qué y tomas decisiones a ciegas. Esto no es estético: es la base para leer reportes rápido (ver 60).

## Errores comunes — blacklist

- Crear un ad set por interés ("yoga", "fitness", "bienestar"): fragmenta conversiones, las audiencias se solapan y compites contra ti mismo en la subasta.
- Cargar 12 creativos casi idénticos: Meta los colapsa bajo el mismo Entity ID, no ganas alcance y crees que "ya probaste mucho creativo". Necesitas variedad REAL (ver 30).
- Duplicar la campaña ganadora "para escalar": divides el aprendizaje en dos. Sube presupuesto en la original ≤20% cada 72h (ver 13 y 72).
- 15 campañas activas con $20k COP/día cada una: nada aprende nunca. Consolida en 1-2.
- Apagar y prender campañas cada día según el ánimo: cada pausa larga (≥7 días) degrada el aprendizaje.
- Meter retargeting y prospecting en el mismo CBO: el retargeting "se roba" el presupuesto porque convierte más barato, y dejas de alimentar el funnel (ver 24).
- Separar por placement o por formato "para tener control": le quitas inventario al algoritmo; eso era 2019.
- Usar ABO con 6 ad sets "para repartir y diversificar": hoy es regalarle plata a Meta en CPMs de aprendizaje eterno.
- Pelear contra el opt-out de Advantage+ desactivando todo por costumbre: en 2026 varias automatizaciones (placements, audiencia broad) sí ayudan — desactiva con criterio, no por nostalgia del manual (ver 90).

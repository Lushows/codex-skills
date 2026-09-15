# 100 — Apollo.io a fondo

Apollo (apollo.io) es la navaja suiza del outbound: en una sola herramienta te da la **base de datos de contactos** (para armar listas), el **enriquecimiento** (traer emails y teléfonos), el **sequencer** (mandar las cadencias) y un **CRM ligero**. Por eso es el punto de arranque más común para un solista o un equipo chico: pagas una cosa y tienes todo el flujo. Este módulo es el deep-dive de la herramienta que en el `30` (el stack) sale como "todo-en-uno" y en el `25` (sourcing) como fuente de datos. Aquí ves cómo exprimirla y dónde te va a quedar corta.

## El principio: una base de 270M+ contactos con filtros de venta

Apollo mantiene una base gigante de personas y empresas (cifra que la propia herramienta reporta en cientos de millones de contactos y decenas de millones de empresas). No es "internet scrapeado al azar": está estructurada con los **filtros que un vendedor necesita** — cargo, seniority, tamaño de empresa, industria, tecnología, ubicación, señales de contratación. Tú construyes una búsqueda, Apollo te devuelve la lista de personas que encajan, y con un clic revelas sus correos y los metes a una secuencia. La calidad del dato es **buena pero no perfecta** (60–80% de aciertos en email según el segmento; peor en LatAm que en EE. UU.), por eso siempre verificas (ver `28`) antes de enviar.

## Los cuatro módulos de Apollo

| Módulo | Qué hace | Con qué compite |
|---|---|---|
| **Search / base de datos** | Filtras personas y empresas por 60+ criterios | ZoomInfo, Lusha, Sales Nav (ver `25`, `26`) |
| **Enrichment** | Revela email/teléfono; enriquece un CSV o tu CRM | Clay como fuente única (ver `31`), Hunter |
| **Sequences** | Cadencias email + tareas de llamada/LinkedIn | Instantly/Smartlead ligero (ver `33`, `103`, `104`) |
| **Deals / CRM** | Pipeline básico, sincroniza con HubSpot/Salesforce | HubSpot (ver `105`), `32` |

La gracia es que fluyen entre sí: buscas → revelas → secuencias sin salir de la app ni exportar CSVs. La trampa es que **ninguno de los cuatro es el mejor de su categoría**; Apollo gana por integración, no por profundidad.

## Filtros que de verdad usas (Search)

Los que mueven la aguja al armar una lista por nicho (ver `21`, `12`):

- **Job titles** — cargos exactos. Usa varios: `"gerente de compras", "director de operaciones", "dueño"`.
- **Seniority** — Owner, C-Suite, VP, Director, Manager. Filtra ruido.
- **# Employees** — rangos (1-10, 11-50, 51-200…). Tu ICP de tamaño (ver `15`).
- **Industry & keywords** — industria + palabras del sitio/LinkedIn de la empresa.
- **Technologies** — qué software usa la empresa (technographics, ver `15`). Ej.: empresas con Shopify.
- **Location** — país/ciudad. Clave y débil a la vez en LatAm (cobertura despareja).
- **Buying intent / Job postings** — señales: empresas contratando cierto rol = están creciendo en esa área (ver `14`, `37`).

Guarda cada búsqueda como **Saved Search** y actívale alertas: Apollo te avisa cuando entran contactos nuevos que cumplen el filtro (lista viva, no foto fija).

## Límites que te van a doler (léelos antes de pagar)

Apollo se ve barato hasta que chocas con sus topes. Los reales en 2026:

- **Créditos de email/móvil por plan.** Revelar datos consume créditos; los planes baratos se quedan cortos rápido. Los **móviles** cuestan muchos más créditos que los emails.
- **Export caps.** Cuántos registros puedes exportar por vez/mes está limitado por plan; el plan gratis casi no exporta.
- **Envío desde Apollo.** El sequencer de Apollo manda desde **tus buzones conectados** y **no está pensado para volumen frío alto desde dominios quemables**. Si vas a mandar cientos/día en frío, la deliverability se cuida mejor en Instantly/Smartlead (ver `33`, `103`, `104`, y toda la fontanería del Bloque 4: `41`–`45`).
- **Calidad LatAm.** Emails y sobre todo teléfonos de Colombia/México/etc. tienen menos cobertura y más ruido que EE. UU. Verifica siempre (ver `28`).

| Plan (aprox 2026) | Precio/usuario/mes | Para quién |
|---|---|---|
| Free | $0 | Probar; casi sin export |
| Basic | ~$49 | Solista arrancando |
| Professional | ~$79–99 | El punto dulce: sequences + más créditos |
| Organization | ~$119+ (min. asientos) | Equipos, controles, más límites arriba |

Precios y topes cambian seguido; confírmalos en su pricing antes de comprar. Para decidir cuántos créditos necesitas según tu meta de reuniones → haz la cuenta con `05` (ecuación del pipeline) y si el número tiene que ser exacto → `Matematicas_lushows`.

## Ejemplo real: lista de 300 dark kitchens en México

```
Búsqueda en Apollo (Search → People):
  Job titles:   "dueño", "founder", "gerente general", "director de operaciones"
  Seniority:    Owner, C-Suite, Director
  # Employees:  11–50
  Industry:     Food & Beverage / Restaurants
  Keywords:     "cocina oculta", "dark kitchen", "delivery"
  Location:     Mexico (CDMX, Guadalajara, Monterrey)
  → ~300 contactos

Flujo:
  1. Select all → Save to list "Dark kitchens MX Q1"
  2. Reveal emails (gasta créditos solo de los que vas a usar)
  3. Export CSV  →  verificar en NeverBounce/ZeroBounce (ver 28)
  4. Los válidos → sequencer (Apollo o, mejor para volumen, Instantly ver 103)
```

## Apollo vs. el stack Clay + Instantly

- **Apollo solo:** más barato, más rápido de montar, un login. Techo de calidad de dato y de deliverability a volumen.
- **Clay (`31`) + Instantly (`103`):** más caro y con curva, pero waterfall de datos (80–90% cobertura, ver `29`) + envío frío serio. Apollo puede ser **una de las fuentes** que alimentan a Clay.

Regla: **arranca con Apollo para validar** que tu ICP y tu oferta funcionan; migra o complementa con Clay+Instantly cuando el volumen o la calidad del dato sea el cuello de botella.

## Errores comunes

- **Enviar frío a volumen desde el buzón principal vía Apollo** → quemas tu dominio. Volumen frío = infraestructura del Bloque 4.
- **Confiar en el email sin verificar.** Apollo marca "verified" pero igual rebota; pasa por verificador (ver `28`).
- **Gastar créditos revelando móviles a lo loco** — son carísimos en créditos; revela solo los de cuentas Tier A (ver `16`).
- **Usar Apollo como CRM serio.** Su CRM es ligero; si el negocio crece, sincroniza a HubSpot/Salesforce (ver `32`, `105`, `106`).

## Siguiente paso

Monta una Saved Search de tu ICP (ver `10`, `15`), guárdala como lista de 50, revela y verifica, y mándala como campaña de prueba. Cuando el dato o la deliverability te frenen, sube a Clay (`31`, `101`) + Instantly (`103`). Para escribir el copy de la secuencia → Bloque 5 (`50`+); la conversación tras la respuesta → `ventas_lushows`.

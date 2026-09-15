# 27 — Scraping ético y legal

Scraping (raspado = extraer datos de una web o plataforma de forma automatizada) es cómo consigues listas a escala cuando las bases de contactos (`25`) no cubren tu nicho — típico en PYMES y negocios locales de LatAm que no están en Apollo pero sí en Google Maps o Instagram. Es una herramienta poderosísima y legítima, **pero tiene una frontera legal y de reputación que debes conocer** para no quemar tus cuentas ni meterte en problemas de datos personales. Este módulo: qué herramientas, qué es legal y qué no, y cómo hacerlo sin arriesgarte.

## El principio: dato público de negocio ≠ vía libre total

Dos verdades que hay que sostener a la vez:
1. **Extraer información pública tiene respaldo legal** en varios precedentes (el caso *hiQ vs. LinkedIn* en USA sentó que raspar datos públicos no viola por sí mismo la ley de fraude informático).
2. **Pero** eso NO significa que puedas hacer lo que quieras: (a) violar los **Términos de Servicio (ToS)** de una plataforma puede costarte la **cuenta** (LinkedIn banea scrapers agresivos), y (b) los **datos personales** (nombre, correo, teléfono de una persona) están protegidos por leyes de privacidad — **Habeas Data** en Colombia, **GDPR** en Europa, etc. (ver `49`, `181`). Raspar datos de **empresa** (razón social, web, teléfono del negocio) es mucho más seguro que raspar datos **personales** sin base legítima.

Regla práctica: **raspa datos de negocio públicos, modera el volumen, y trata los datos personales con base legal y opt-out.** No compres ni raspes para revender bases de personas.

## Qué es más seguro y qué es más riesgoso

| Práctica | Riesgo | Nota |
|---|---|---|
| Scrapear Google Maps (negocios, teléfono, web) | **Bajo** | Datos de negocio públicos; la fuente más limpia para PYMES |
| Scrapear directorios/gremios públicos | **Bajo** | Listados que existen para ser vistos |
| Scrapear tu propia web / quién te visita (`132`) | **Bajo** | Tus datos |
| Extraer LinkedIn a volumen moderado con herramienta "humana" | **Medio** | Roza ToS; riesgo = tu cuenta LinkedIn |
| Extraer LinkedIn masivo/agresivo | **Alto** | Baneo de cuenta casi seguro |
| Raspar emails personales masivos para enviar sin base legal | **Alto (legal)** | Habeas Data/GDPR; multas y spam |
| Comprar/revender bases de personas | **Alto** | Muchas veces ilegal; siempre quemadas (`20`) |

## Las herramientas — qué hace cada una

| Herramienta | Qué hace | Mejor para | Precio aprox. 2026 |
|---|---|---|---|
| **Clay** | Orquestador: junta fuentes, corre waterfalls (`130`), enriquece, scrapea vía integraciones, con IA. El "Excel con superpoderes". | Montar toda la operación de datos en un lugar (`31`, `101`) | ~$149+/mes |
| **Apify** | Marketplace de "actors" (scrapers listos): Google Maps, Instagram, sitios web. Muy potente y flexible. | Maps, IG, webs a escala (`109`) | Pago por uso, desde ~$49/mes |
| **PhantomBuster** | "Phantoms" para LinkedIn, Instagram, Maps; automatiza acciones y extrae listas | Extraer Sales Nav (`26`), IG | ~$69–159/mes |
| **Evaboot** | Especialista en exportar y limpiar listas de Sales Navigator | Pasar Sales Nav a CSV limpio | ~$29+/mes |
| **Bardeen / Instant Data Scraper** | Extractores simples de navegador, no-code | Tablas y listados sueltos, rápido | Free / bajo |
| **Google Maps scraping** (via Apify/PhantomBuster) | Extrae fichas: nombre, categoría, dirección, teléfono, web, reseñas | **PYMES LatAm** — la joya | Por uso |

## Cómo scrapear sin quemarte — reglas operativas

1. **Prefiere datos de negocio.** Maps, directorios, webs corporativas: bajo riesgo y alto valor para LatAm.
2. **Modera el volumen y simula humano.** En LinkedIn: límites bajos por día, pausas, herramientas que respetan patrones humanos (PhantomBuster/Evaboot). Nunca "extrae 10.000 perfiles hoy".
3. **Usa cuentas y proxies dedicados** para LinkedIn/IG, no tu cuenta principal, si vas a escalar (aun así, con moderación).
4. **Ten base legal para el envío.** Que puedas obtener un correo no te autoriza a spamearlo. En B2B, el "interés legítimo" + opt-out claro es la vía más defendible (ver `49`). Documenta de dónde salió cada dato (columna `fuente`, `20`).
5. **Respeta el opt-out y no re-contactes** a quien pidió salir. Guarda una lista de supresión.
6. **Verifica lo scrapeado** (`28`) — el dato raspado suele venir sucio.

## Ejemplo real: 300 restaurantes con teléfono/WhatsApp, legal y limpio

```
1. Apify → "Google Maps Scraper"
   query: "restaurantes en Bogotá"  (repite por localidades)
   → CSV: nombre, categoría, dirección, teléfono, sitio_web, nº reseñas.
2. Filtro de fit: >150 reseñas y con sitio_web (proxy de negocio serio).
3. Valida WhatsApp del teléfono (`24`).
4. Decisor + correo nominal → `22`, `23`; verifica todo → `28`.
5. Documenta fuente = "Google Maps público" y prepara opt-out (`49`).
Datos de NEGOCIO públicos + volumen razonable = zona segura.
```

## Errores comunes (qué NO hacer)

- **Scraping masivo de LinkedIn** con la cuenta principal → baneo.
- **Raspar y enviar emails personales sin base legal ni opt-out** → riesgo Habeas Data/GDPR y spam (`49`).
- **No verificar** lo raspado → rebotes, caes en spam (`40`, `28`).
- **Revender bases** de personas → ilegal en la práctica y reputacionalmente tóxico.
- **Ignorar `robots.txt` / ToS** de forma temeraria en sitios que lo prohíben explícitamente.

## Frontera y siguiente paso

Conseguir los datos (aunque sea scrapeando) = esta skill; el cumplimiento legal a fondo del **envío** vive en `49` (CAN-SPAM/GDPR/Habeas Data) y `181` (Colombia). **Convencer y cerrar** al contacto → `ventas_lushows`. Con la lista scrapeada y verificada, enriquécela (`29`) para personalizar. Herramientas de scraping a fondo: `109`. Orquestar todo en Clay: `31` / `101`.

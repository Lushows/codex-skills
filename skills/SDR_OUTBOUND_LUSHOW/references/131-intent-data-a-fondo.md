# 131 — Intent data a fondo

El módulo `36` te presentó el intent data (datos de intención: señales de que una empresa está investigando tu categoría **ahora**). Este va a fondo en los **cuatro proveedores grandes** — Bombora, G2, 6sense y Clearbit — para que sepas exactamente qué señal da cada uno, cuánto cuesta, y cómo accionarla sin quemar plata. La decisión práctica no es "¿uso intent?" sino "¿cuál de estas cuatro fuentes vale para lo que vendo y mi tamaño?".

## El principio: cada proveedor mira un lugar distinto de internet

El intent no es una sola cosa; es **dónde miras la actividad de compra**:

- **Bombora** mira la **web abierta B2B** (miles de sitios de contenido).
- **G2** mira los **sitios de reseñas/comparación** de software.
- **6sense** **combina** varias fuentes (incluida Bombora) y le añade IA y predicción.
- **Clearbit (hoy Breeze Intelligence de HubSpot)** mira **tu propia web** + enriquecimiento.

Elegir bien = elegir la fuente donde tu comprador **realmente** deja rastro. Un SaaS que sale en G2 debe empezar por G2; un servicio B2B sin categoría en G2 empieza por su propia web (Clearbit/deanonimización, `132`).

## Los cuatro a fondo

| Proveedor | Qué señal da | Granularidad | Precio aprox. 2026 | Para quién |
|---|---|---|---|---|
| **Bombora** | "Surge": una cuenta consume más contenido de un tema que su base normal | Cuenta (anónimo a nivel persona) | Contrato, miles USD/año (a veces dentro de 6sense/ZoomInfo) | Mid-market/enterprise con TAM grande |
| **G2 Buyer Intent** | Empresas mirando TU categoría y a tus competidores en G2 | Cuenta, a veces persona | Add-on de tu perfil G2, cientos–miles/mes | SaaS listado en G2 (mejor ROI de intent) |
| **6sense** | Plataforma ABM: intent (Bombora+propio) + predicción de etapa de compra + IA | Cuenta + contacto priorizado | Enterprise, decenas de miles/año | Equipos ABM con presupuesto (`94`) |
| **Clearbit / Breeze** | Deanonimización de tu web + enriquecimiento sobre HubSpot | Cuenta y persona (visitas propias) | Incluido/add-on de HubSpot | Quien vive en HubSpot (`32`) |

### Bombora — el "Surge score"
Rastrea consumo de contenido en su red B2B y detecta cuándo una empresa **sube** (surge) su interés en un tema frente a su comportamiento normal. Te entrega un score 0–100 por cuenta y por tema. Es **amplio pero anónimo**: te dice la empresa, no la persona (todavía tienes que encontrar al decisor, `22`). Fuerte para **priorizar cuentas** en un TAM grande; caro y por contrato. No lo compres para validar una idea.

### G2 Buyer Intent — el de mejor ROI si eres software
Te dice qué empresas están **comparando tu categoría** en G2 justo ahora. Comparar en G2 es un acto de compra **tardío** (ya están evaluando proveedores), así que la señal es altísima. Si vendes software y tienes perfil en G2, activarlo suele pagar solo. Puedes ver incluso qué competidores está mirando la cuenta.

### 6sense — la plataforma, no solo el dato
No es una fuente de intent, es una **plataforma ABM** que ingiere intent (incluida Bombora), lo cruza con tu CRM y **predice en qué etapa de compra** está cada cuenta (desconoce / considera / decide). Potente pero caro y pesado de implementar; es para equipos con operación ABM montada (`94`, `06`), no para el que arranca.

### Clearbit / Breeze — first-party sobre HubSpot
Clearbit (adquirido por HubSpot, ahora **Breeze Intelligence**) hace deanonimización de **tu propia web** + enriquece tus registros. Si ya vives en HubSpot (`32`), es la vía más directa a intent first-party. Detalle de la familia deanonimización → `132`.

## Cómo accionar cada señal (no solo comprarla)

El dato sin acción no vende. Traducción señal → jugada:

```
Bombora surge alto en "software de facturación", cuenta = tu ICP:
  → Clay encuentra al CFO/decisor (`22`) → cadencia priorizada
  → ángulo = el tema del surge (facturación), SIN delatar el tracking

G2: cuenta vio tu perfil + el de Competidor X:
  → cadencia de "competitive displacement" (`19`)
  → ángulo = por qué te eligen vs ese competidor específico

6sense marca cuenta en etapa "decisión":
  → prioridad #1 para el AE, no para cold email masivo
  → handoff caliente (`73`)

Clearbit: visitante identificado en /precios:
  → outbound de "visitante web" (`132`), timing inmediato
```

**Regla de oro:** el intent **prioriza y sincroniza el timing**; nunca lo cites como amenaza. "Vi que investigabas facturación" espanta. Usa la señal para elegir a quién y cuándo escribir, y deja que el ángulo (no el tracking) hable (`36`, `128`).

## Cruzar intent con fit: el oro está en la intersección

Intent solo = ruido; una empresa "in-market" que no es tu ICP igual no compra. **Fit** (encaje: tamaño, industria — `10`, `15`) **+ intent** (está buscando) = tu lista prioritaria. Este cruce se hace en Clay o en tu scoring (`137`). Nunca dispares outbound por intent sin filtrar por fit primero.

## Errores comunes

- **Comprar Bombora/6sense para validar** una idea → es caro y para escalar, no para empezar. Arranca por first-party (tu web, `132`) que es casi gratis.
- **Intent sin fit** → contactas empresas "activas" que jamás comprarían.
- **Delatar el tracking** → "sé que nos estás mirando" mata la conversación.
- **Tratar el intent anónimo (cuenta) como persona** → Bombora te da la empresa; el decisor lo encuentras aparte (`22`).
- **Pagar 6sense sin equipo ABM** → la plataforma se desperdicia sin proceso detrás (`94`).

## Frontera y siguiente paso

El intent te dice **a quién y cuándo**; **convencer y cerrar** en la conversación es `ventas_lushows`. Si vendes software, activa G2 Buyer Intent (mejor ROI). Si no, empieza por tu propia web con deanonimización → `132`. Cruza siempre intent con fit → `137`. Para la otra familia de timing (señales de evento: cambio de cargo, funding) → `37`, `133`, `135`. Automatizar señal→contacto → `34`, `147`.

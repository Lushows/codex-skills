# 01 — Cómo funciona la subasta de Meta

Cada vez que alguien abre Facebook o Instagram, Meta corre una subasta en milisegundos para decidir qué anuncio mostrarle. Entender esa subasta explica por qué dos anunciantes idénticos pagan costos distintos, y por qué la palanca más barata para bajar costos es el creativo, no la puja. Lee este módulo cuando tus CPMs (costo por mil impresiones) parezcan caros o quieras entender qué premia el sistema.

## La fórmula: Total Value

Meta no le muestra el anuncio al que más paga. Cada anuncio compite con un puntaje:

```
Total Value = Bid × Estimated Action Rate + Ad Quality
```

- **Bid (puja)**: cuánto estás dispuesto a pagar por el resultado. Con puja automática (default y recomendado), Meta la calcula por ti según tu presupuesto.
- **Estimated Action Rate (EAR)**: la probabilidad estimada de que ESA persona haga la acción que pediste (comprar, escribir por WhatsApp, dejar el lead). La calcula el modelo de ML —en 2026, **GEM** (modelo generativo, nov-2025) corriendo sobre **Andromeda**, el motor de retrieval que preselecciona qué ads son candidatos para cada usuario— usando tu creativo, tu historial y la señal de tu dataset/CAPI.
- **Ad Quality**: calidad percibida del anuncio: feedback de usuarios (ocultar, reportar), señales de experiencia post-clic (landing lenta o engañosa) y penalizaciones.

**Gana la subasta el mayor Total Value, no el mayor Bid.** Un anuncio con EAR alto y buena calidad le gana a uno que puja el doble. En la práctica esto significa que un creativo que la gente ama puede costar la mitad de CPM que uno que ignora, aun pujando lo mismo.

## Cómo entra Andromeda (la pieza nueva)

Antes de la subasta hay un paso de **retrieval**: de los millones de anuncios elegibles, Andromeda preselecciona unos pocos miles candidatos para ESE usuario, leyendo el contenido de tu creativo (qué muestra el video, qué dice el copy). Por eso **el creativo es el targeting**: si tu ad "habla" de un dolor o un público, Andromeda lo enseña a quien encaja, sin que tú segmentes. Implicación dura: 10-15 creativos conceptualmente distintos le dan al motor 10-15 puertas de entrada a poblaciones distintas; 3 casi-duplicados colapsan en un **Entity ID** único y le dan una sola puerta (ver 92).

## Qué significa para ti (implicaciones prácticas)

| Situación | Lectura desde la subasta | Acción |
|---|---|---|
| CPM alto vs tu vertical | EAR o calidad bajos: el sistema te cobra "peaje" por mostrar algo que la gente ignora | Nuevo creativo, no nueva puja |
| CTR sube y CPM baja | El sistema premia relevancia con inventario más barato | Itera ese ángulo creativo (ver 38) |
| CPA sube con el mismo creativo tras semanas | Fatiga: el EAR cae para la audiencia ya expuesta | Rotar creativos (frecuencia >2-3 es alerta, ver 39) |
| Cuenta nueva paga más que la competencia | Sin historial, el modelo estima EAR con menos confianza | Paciencia + señal limpia vía CAPI (ver 06) |
| CPM disparado en noviembre | Subasta saturada por Q4/Black Friday | Esperado; sube pujas el negocio, no tú (ver 77) |

Regla de oro: **mejorar el creativo baja tu costo más que cualquier truco de puja**, porque mueve dos de los tres factores (EAR y Quality) a la vez.

## Benchmarks de CPM en Colombia (jun-2026, orientativos)

El CPM varía brutalmente por placement, vertical y temporada, pero para calibrar expectativas en COP:

| Contexto | CPM típico (COP) |
|---|---|
| Reels/Audience Network, audiencia amplia | ~4.000–9.000 |
| Feed FB/IG, audiencia amplia LatAm | ~9.000–22.000 |
| Retargeting (audiencia chica y caliente) | ~25.000–60.000+ |
| Q4 / Black Friday / diciembre | +30% a +80% sobre lo normal |

No persigas el CPM más bajo: un CPM de 5.000 COP que no vende es más caro que uno de 20.000 que sí. El CPM es termómetro de inventario, no KPI.

## Penalizaciones de calidad

Meta degrada (paga más o no entrega) anuncios con:
- **Clickbait**: titulares que ocultan información ("No creerás lo que pasó...").
- **Engagement bait**: pedir reacciones/comentarios/compartidos explícitamente ("comenta YO para...").
- **Quality ranking bajo**: en Ads Manager ves 3 diagnósticos relativos a competidores — quality ranking, engagement rate ranking, conversion rate ranking. "Below average" sostenido en quality = anuncio caro de por vida; reemplázalo.
- **Mala experiencia post-clic**: landing lenta, pop-ups agresivos, contenido que no coincide con el anuncio (si tu landing es el problema → desingweb-lushows).

## eCPM y pacing

- **eCPM** (effective CPM): lo que Meta efectivamente gana por mostrar 1.000 impresiones tuyas. Es la métrica interna con la que tu ad compite contra todos los demás (incluso contra anuncios con otros objetivos). Por eso una campaña de Awareness y una de Sales compiten en la misma subasta: Meta las normaliza a eCPM.
- **Pacing**: Meta no gasta tu presupuesto diario de golpe; lo reparte buscando las subastas más eficientes del día. Por eso un presupuesto recién subido gasta "raro" las primeras horas y por eso NO debes sacar conclusiones a las 10 a.m.
- Si tu presupuesto es muy alto para tu audiencia/creativo, el sistema entra a subastas más caras para gastarlo → CPA sube. Escalar despacio (ver 00 fase 7, 72) respeta el pacing.

## Estrategias de puja (5 en 2026)

La puja automática (Highest Volume / Highest Value) es el default y rinde en la mayoría de casos. Pero existen 5 estrategias; las relevantes:

| Estrategia | Qué hace | Cuándo |
|---|---|---|
| Highest Volume | Máximos resultados con tu presupuesto | Default, prospecting |
| Cost per result goal | Apunta a un CPA promedio | Cuando tienes CPA techo claro |
| Highest Value | Maximiza valor (ROAS), no volumen | E-commerce con catálogo |
| **Minimum ROAS / ROAS Goal** | No gasta bajo un ROAS mínimo que defines | Escalar protegiendo margen (ver 15) |
| Bid cap | Techo duro de puja | Avanzado, raro en pyme |

Súmale **Value Rules** (decirle a Meta que ciertos clientes valen más, ej. clientes nuevos vs recurrentes) — clave porque desde mar-2026 hay un **cap de clientes existentes del 25-30%** en Advantage+ Sales para que no canibalices tu base.

## Lo que NO controlas (y está bien)

No eliges contra quién compites, ni el precio del inventario (sube en Q4, Black Friday, elecciones), ni el usuario exacto. Controlas: oferta, creativo, señal de conversión, presupuesto y estructura. Enfócate ahí (ver 02 para el reparto humano vs máquina).

## Receta: diagnóstico de subasta en 5 minutos

1. Abre Ads Manager → columnas personalizadas: CPM, CTR (outbound), frecuencia, CPA, quality ranking.
2. CPA caro + CTR bajo (<0,8-1% outbound en frío; varía por vertical) → problema de gancho creativo: nuevo ad (ver 37).
3. CPA caro + CTR sano → problema post-clic: landing, oferta o cierre en WhatsApp (ver 03; cierre → ventas_lushows).
4. CPA subiendo + frecuencia >3 → fatiga: rota creativos (ver 39).
5. Quality ranking "below average" → reemplaza el ad; no se rehabilita, se reemplaza.

## Errores comunes — blacklist

- **Subir la puja manual para "ganar más subastas"**: pagas más por el mismo inventario; el problema casi siempre era EAR/creativo.
- **Pelear contra el CPM**: el CPM no es tu KPI; un CPM caro con CPA barato es un gran negocio. Optimiza CPA/ROAS.
- **Usar engagement bait para "subir interacción"**: penalización directa de calidad; pagas más en cada subasta futura.
- **Cambiar presupuesto varias veces al día**: rompes el pacing y fuerzas al sistema a comprar inventario caro.
- **Landing engañosa o lenta para "convertir más"**: Meta la huele (señales post-clic) y te degrada la cuenta entera.
- **Lanzar 3 creativos casi iguales**: colapsan en un Entity ID; le das a Andromeda una sola puerta de retrieval.
- **Juzgar entrega a primera hora de la mañana**: el pacing reparte el gasto; evalúa con días completos.

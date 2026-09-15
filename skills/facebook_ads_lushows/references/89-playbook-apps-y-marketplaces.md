# 89 — Playbook: Apps móviles y marketplaces

El vertical más técnico de Meta Ads y donde más fácil se quema plata con métricas de vanidad. Visión honesta por delante: pautar una app es más difícil de medir que pautar una web, instalar ≠ usar, y un marketplace son DOS negocios de pauta, no uno. Si tu producto puede vivir en web primero, probablemente debas pautar la web primero.

## App promotion: cómo funciona

Objetivo de campaña **App promotion**: optimiza por instalaciones o por **eventos in-app** (registro, compra, suscripción). En 2026 existe **Advantage+ App** (la versión automatizada — ver `actualizacion-2026-06`). Requisitos:

1. App registrada en Meta (Events Manager → app).
2. **SDK de Meta** instalado, o mejor: un **MMP** (Mobile Measurement Partner: medidor independiente tipo AppsFlyer/Adjust que atribuye instalaciones y eventos a cada canal). Para operación seria, MMP — Meta midiéndose a sí misma es juez y parte, y el MMP te deja comparar canales.
3. Eventos in-app configurados y verificados ANTES de pautar (el equivalente al Dataset/píxel — ver 05/62).

## El mundo post-iOS: expectativas honestas

Desde iOS 14.5, Apple bloqueó el tracking individual: en iOS la atribución va por **SKAdNetwork/AEM** — agregada y retrasada (sabes que la campaña generó X instalaciones, con retraso y sin detalle por usuario; ver 16). Implicaciones:

- **Android es mucho más medible** que iOS. En Colombia Android domina (~80%+): ventaja para LatAm.
- App iOS-first: acepta medición limitada, decide con cohortes y tendencias, no con atribución exacta.
- Optimización de eventos in-app en iOS: limitada por el esquema de SKAdNetwork — pocos eventos, priorízalos bien.

## Optimiza por VALOR, no por instalación

La trampa #1: campañas de instalaciones que traen installs a $800 COP… de gente que nunca abre la app. **Instalaciones baratas de usuarios que no usan = vanidad pura** (ver 14/60). La escalera:

1. Arranque: instala-y-registra (optimiza por **registro completado**, no por install).
2. Madurez: optimiza por el **evento de valor** (compra in-app, suscripción, primer pedido) apenas tengas volumen semanal decente.
3. El install es un costo intermedio, jamás el KPI. KPI real: costo por usuario ACTIVO a día 7, costo por primer pedido/compra.

## La cuenta concreta

| Campaña | Tipo | Objetivo | Creativos | Medición |
|---|---|---|---|---|
| **Adquisición Android** | App promotion / Advantage+ App | registro → evento de valor | uso real en pantalla (3s) · problema→app→resultado | costo por usuario activo D7 |
| **Adquisición iOS** | App promotion (SKAN) | install/registro (eventos priorizados) | demo nativa vertical + badge tienda | cohortes/tendencia (no exacto) |
| **Web-to-app** (jugada LatAm) | Advantage+ Sales (web, Dataset+CAPI) | Purchase/registro web | la misma demo, landing/PWA | CPA real medible |
| **Marketplace lado escaso** | Lead ads / CTWA (ver 50/52) | lead de proveedor | "gana plata haciendo X" | costo por proveedor activo |

## Creativos de app (ver 31)

- **El uso REAL de la app en pantalla en los primeros 3 segundos** (ver 37): screen recording del flujo clave — el usuario quiere ver QUÉ hace la app antes de cualquier logo.
- **Problema → app → resultado** en 15-20s: la situación molesta → la app resolviéndola en pantalla → el resultado.
- UGC de usuario mostrando su pantalla ("así pido mi mercado en 2 minutos").
- Formato vertical nativo (ver 34); incluye el badge de la tienda y el CTA "Descargar".

## Marketplaces: dos lados, dos pautas

Un marketplace (Rappi-like, app de citas, plataforma de servicios) tiene **oferta y demanda — y se pautan por separado**: campañas, creativos y mensajes distintos ("gana plata haciendo domicilios" vs "tu mercado en 30 minutos").

- **El lado escaso primero**: el marketplace muere por el lado que falta. Sin oferta (proveedores/repartidores/perfiles), la demanda que compres se va decepcionada y no vuelve — pauta el lado difícil hasta tener densidad, luego balancea.
- El lado oferta suele ser más barato por **lead ads/CTWA** (ver 52/50) que por install: el proveedor se recluta conversando.
- Estrategia de arranque (densidad por zona, huevo-gallina): desingweb 62.

## Web-to-app y PWA: la jugada LatAm

El Dataset web mide MEJOR que SKAdNetwork. Alternativa pragmática: capturar al usuario en **web** (landing o web-app/PWA con Dataset + CAPI completos — ver 05-06) y migrarlo a la app después (banner "descarga la app", deep link post-compra). Beneficios: pauta medible con Sales web, retargeting normal, y CAC medido de verdad. Para muchos negocios LatAm la web-app ES el producto y la app nativa puede esperar (PWA vs nativa: engineer_visualopen_lushows si aplica).

## Ofertas tipo del vertical

- **Primer pedido/servicio gratis o con cupón** (apps de delivery/servicios): adquisición que se mide por retención, no por install.
- **Bono de bienvenida al proveedor** ("$X por tus primeros 10 domicilios"): llena el lado escaso.
- **Referido de doble lado** ("invita y ambos ganan $X"): crecimiento compuesto barato.
- **Suscripción primer mes gratis** (apps de membresía): siembra el evento de valor real.

## Cuándo NO pautar la app

**Sin retención probada, pautar es echar agua a un balde roto.** Si de 100 usuarios orgánicos solo 5 siguen activos al día 30, la pauta solo hace el hueco más caro. Antes de escalar:

- Mide **cohortes de retención** (D1/D7/D30: % que vuelve al día 1, 7 y 30) con tu analytics (posthog u otro; economist_lushows para unit economics).
- Referencia honesta (caveat: varía por categoría): D1 25-40%, D7 10-20%, D30 5-10% es "normal"; por debajo de la mitad, arregla producto primero.
- La pauta amplifica lo que existe: producto que retiene + pauta = crecimiento; producto que fuga + pauta = quema de capital con gráfica bonita de installs.

## Presupuesto y benchmarks honestos (Colombia)

Arranque: **$50.000-$150.000 COP/día** por lado/plataforma. CPI (costo por install) referencial: **$1.500-$8.000 COP** según categoría y plataforma — pero el CPI es vanidad; costo por usuario activo D7 o por primer pedido es la cifra real, y suele ser **5-20x el CPI**. CPM apps $6.000-$16.000. Caveat: los rangos de apps varían más que en cualquier otro vertical.

## El esquema de eventos: lo que decides ANTES de pautar

La pauta de apps se gana o se pierde en la configuración de eventos, no en el Ads Manager. En iOS el **SKAdNetwork** te da un número limitadísimo de "conversion values" (un esquema de prioridades que tú defines): no puedes medir 20 eventos, debes elegir los 3-4 que importan y ordenarlos por valor (ej. 1=install, 2=registro, 3=primer pedido, 4=suscripción). Si llenas ese esquema con eventos de vanidad ("abrió pantalla"), Meta optimiza hacia ruido. En Android tienes más libertad, pero la disciplina es la misma: define el **evento de valor** (el que correlaciona con plata: primer pedido, suscripción activa, no "registro vacío") y dáselo al algoritmo como objetivo apenas tengas ~30-50 de esos eventos por semana. Antes de ese volumen, optimiza por el paso anterior (registro completado) y sube de escalón cuando el algoritmo tenga señal suficiente. El MMP (AppsFlyer/Adjust) es el que te deja ver esto limpio por canal y comparar Meta vs Google vs TikTok sin que cada plataforma se atribuya todo. Sin este esquema definido y verificado, pautar una app es prender fuego a billetes con una gráfica de installs bonita encima.

## Ruteo a skills hermanas

Onboarding y activación que convierten el install en usuario → desingweb-lushows + engineer_visualopen_lushows (producto). Cierre del lado oferta del marketplace por chat → ventas_lushows. Identidad de la app y ASO visual → directorcreativo_lushows. Unit economics, retención y LTV → economist_lushows. App campaigns en Google (UAC) → google_ads; demo nativa y reclutamiento de creators → tiktok_ads.

## Errores comunes — blacklist

- Optimizar por instalaciones para siempre: compras descargas, no usuarios.
- Pautar iOS-first esperando atribución exacta: SKAdNetwork no te la va a dar (ver 16).
- Sin MMP ni eventos in-app verificados: decides a ciegas con el reporte del vendedor (Meta).
- Pautar los dos lados del marketplace con el mismo mensaje genérico.
- Comprar demanda sin densidad de oferta: usuarios que abren, no encuentran nada y desinstalan.
- Escalar con D7 de 4%: el balde roto, más caro y más rápido.
- Ignorar la opción web-to-app por orgullo de "somos una app": la medición web puede ser tu mejor arma en LatAm.

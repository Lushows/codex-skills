# 78 — Presupuestos grandes

Lee este módulo cuando manejes (o aspires a manejar) más de **~USD $10.000/mes** en Google Ads — sea propio o de un cliente. A esta escala el juego cambia: ya no optimizas una campaña, gestionas un **portafolio**; ya no basta con "el CPA está bien", tienes que probar que la pauta genera ventas **incrementales** (que no habrían pasado igual sin ella); y necesitas procesos y diversificación porque un solo punto de falla es mucha plata. Casi todo lo demás de esta skill aplica — aquí va lo específico de operar en grande.

Marco: Google captura demanda. Con presupuesto grande sueles haber **agotado la captura de alta intención** y empiezas a invertir en generación (PMax, Demand Gen, YouTube) — terreno que comparte lógica con Meta y TikTok (ver `facebook_ads_lushows`, `tiktok_ads_lushows`). Por eso a esta escala la pregunta deja de ser "¿convierte?" y pasa a ser "¿esto suma ventas reales o me estoy atribuyendo lo que ya iba a pasar?".

## Portafolio de campañas, no una campaña

Con plata grande estructuras por **rol estratégico**, cada uno con su presupuesto, su target y su métrica de éxito:

| Capa | Rol | Tipo | Métrica de éxito | Cuidado |
|---|---|---|---|---|
| **Marca** | Capturar a quien ya te busca | Search marca | CPA bajísimo | Poca incrementalidad (ver 65) |
| **Genérico alta intención** | Capturar demanda no-marca | Search genérico | CPA/ROAS objetivo | El núcleo rentable (ver 39) |
| **Competencia** | Robar demanda del competidor | Search sobre marcas rivales | CPA tolerablemente mayor | CPC caro, QS bajo |
| **PMax / AI Max** | Cubrir todo el inventario con datos | PMax / AI Max for Search | Volumen amplio | Necesita feed y ≥30 conv (ver 12) |
| **Demand Gen / YouTube** | Generar demanda nueva | Demand Gen, video | Incrementalidad, no last-click | No mide bien por last-click |
| **Remarketing** | Cerrar a quien ya te visitó | RLSA / PMax audiencias | ROAS alto | Atribución regalada |

La trampa de marca a esta escala: el Search de marca muestra un ROAS espectacular pero gran parte de esa gente **te iba a comprar igual** (ya te buscaron por nombre). No es plata "mal gastada" (defiendes la marca de competidores), pero no la confundas con crecimiento real. Mídelo (ver 65-incrementalidad).

## Incrementalidad: la métrica que separa lo grande de lo amateur

Con presupuestos chicos puedes guiarte por el CPA reportado. Con presupuestos grandes eso no basta, porque la atribución last-click (ver 16-atribucion) le **regala** a Google ventas que habrían ocurrido de todos modos. La pregunta correcta es de **incrementalidad**: ¿cuántas ventas EXTRA generó esta inversión que NO habrían pasado sin ella?

- **Usa experimentos** para medir el efecto real:
  - **Geo experiments / lift tests:** apagas la pauta en unas regiones (grupo de control) y las comparas con las que la mantienen (grupo de prueba). La diferencia de ventas es el incremento real (ver 65-incrementalidad).
  - **Drafts & Experiments** de Google para probar cambios de bidding/estructura con división de tráfico antes de aplicarlos a todo.
  - **Conversion lift / Brand lift** donde estén disponibles.
- **Vigila la canibalización:** PMax y Demand Gen a veces se atribuyen conversiones que el Search de marca ya estaba capturando barato. Sin medir incrementalidad, pagas dos veces por la misma venta. Usa exclusiones de marca en PMax donde aplique.
- **Conecta conversiones offline / valor real.** A esta escala, importa GA4 con conversiones offline y valores reales por venta (no solo "una conversión"), para que tROAS optimice por margen y no por conteo (ver 14-conversion, 64-ROAS-real).
- A esta escala, decisiones de presupuesto sin incrementalidad son apuestas caras. (Sobre el ROAS real vs. el reportado, ver 64-ROAS-real; sobre viabilidad, CAC/LTV y blended de toda la inversión, `economist_lushows`.)

## La métrica norte a escala: CAC blended y MER

No optimices canal por canal en silos. A escala mira el **negocio entero**:

- **MER (Media Efficiency Ratio) / ROAS blended:** ingresos totales ÷ gasto total en ads (todos los canales). Es la verdad que el CFO mira; el ROAS por plataforma engaña por solapamiento de atribución.
- **CAC blended:** costo de adquirir un cliente nuevo contando TODA la inversión, no solo el last-click de Google.
- Si el ROAS de cada plataforma "se ve bien" pero el blended se cae, hay canibalización y atribución inflada. Súbelo a `economist_lushows` para modelar CAC/LTV y payback real.

## Diversificación, equipo y procesos

A esta escala, la fragilidad cuesta caro:

- **Diversifica tipos y canales.** No pongas todo en PMax (caja parcialmente negra) ni todo en una campaña: si algo se rompe (cuenta suspendida, conversión rota, competidor agresivo), no puede tumbarte todo el revenue. Distribuye entre Search, PMax/AI Max, Demand Gen — y no tengas todo el budget en Google (Meta/TikTok como diversificación, ver `facebook_ads_lushows`, `tiktok_ads_lushows`).
- **Procesos escritos, no memoria.** Reglas de optimización (ver 70), kill criteria (ver 71) y troubleshooting (ver 75) documentados, para que la gestión sea consistente aunque la haga otra persona o tú en un mal día.
- **Cadencia de revisión, no micro-gestión.** Revisiones semanales con ventanas de datos correctas (1 ciclo de conversión), no toqueteo diario que reinicia aprendizajes (ver 70-reglas). El daño de micro-gestionar escala con el número de campañas.
- **Equipo / responsabilidades claras** cuando el volumen lo justifica: alguien dueño de creatividad/RSA/activos, alguien de medición (GA4/Enhanced Conversions/server-side, ver 14-conversion), alguien de estrategia de portafolio e incrementalidad.
- **Protege la cuenta.** A esta escala una suspensión es catastrófica: verificación de empresa al día, políticas cumplidas, MFA, accesos controlados, y respaldo de creatividades/estructura (ver módulos de cuenta/suspensión).
- **Escala con disciplina:** vertical en pasos del 20% (ver 72), horizontal abriendo de a uno (ver 73), protegiendo margen con tROAS/tCPA (ver 74). El tamaño no exime de las reglas — las hace más caras de romper.

## Errores comunes — blacklist

- **Confiar en el CPA reportado sin medir incrementalidad.** A gran escala la atribución te regala ventas que igual pasaban; mides crecimiento que no existe y escalas a pérdida (ver 65-incrementalidad).
- **Celebrar el ROAS gigante del Search de marca como si fuera crecimiento.** Mucha de esa gente te compraba igual; no lo confundas con captura nueva (ver 39-marca-generico).
- **Optimizar canal por canal ignorando el MER/CAC blended.** Cada plataforma "se ve bien" mientras el negocio pierde plata por solapamiento (ver `economist_lushows`).
- **Poner todo el presupuesto en PMax.** Caja parcialmente negra y único punto de falla; sin Search y Demand Gen al lado, no controlas ni diversificas (ver 12-PMax).
- **Micro-gestionar a diario una cuenta grande.** Multiplicas reinicios de aprendizaje por muchas campañas; el daño escala con el tamaño (ver 70-reglas).
- **No documentar procesos.** A esta escala la gestión "de memoria" es inconsistente y frágil; un error humano cuesta miles de dólares.
- **Ignorar la canibalización entre PMax/Demand Gen y Search.** Pagas dos veces por la misma venta sin darte cuenta.
- **No diversificar fuera de Google.** Una suspensión o un cambio de algoritmo no debería poder tumbar todo el revenue; ten otro canal (ver `facebook_ads_lushows`, `tiktok_ads_lushows`).
- **Descuidar la salud de la cuenta.** A esta escala una suspensión sin respaldo ni verificación es un golpe que tarda semanas en recuperarse.

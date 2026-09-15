# 09 — Glosario del outbound

El outbound está lleno de siglas en inglés que asustan pero significan cosas simples. Este módulo es tu diccionario: cada término en una frase clara, con el módulo donde se profundiza. Vuelve aquí cada vez que un módulo use una palabra que no reconoces. Está agrupado por tema para que encuentres rápido.

## El embudo y los estados del lead

- **Lead** — un contacto o empresa que *podría* ser cliente. Todavía sin calificar.
- **Prospecto** — un lead que encaja en tu ICP y estás trabajando activamente.
- **MQL** (Marketing Qualified Lead) — lead que marketing considera listo para vender porque mostró interés (descargó algo, visitó la web varias veces). Aún no validado por ventas. Ver `72`.
- **SAL** (Sales Accepted Lead) — lead que ventas **aceptó** trabajar (el SDR/AE dijo "sí, este vale la pena"). Puente entre MQL y SQL. Ver `72`.
- **SQL** (Sales Qualified Lead) — lead **calificado por ventas**: encaja, tiene necesidad y vale una reunión/oportunidad real. Es el output principal del SDR. Ver `70`, `72`.
- **Oportunidad (opp)** — un SQL que ya es un negocio potencial con un valor y una etapa en el CRM. La trabaja el AE.
- **Handoff** — el pase del lead calificado del SDR al AE, con todo el contexto. Ver `73`.

## Targeting y mercado

- **ICP** (Ideal Customer Profile / Perfil de Cliente Ideal) — la descripción exacta de la empresa/persona a la que le vendes mejor. El filtro que decide todo. Ver `10`.
- **Buyer persona** — el perfil de la *persona* dentro de la empresa a la que le hablas (su cargo, dolor, objetivos). Ver `11`.
- **TAM / SAM / SOM** — el tamaño del mercado: **TAM** (Total Addressable Market, todo el mercado posible), **SAM** (Serviceable Available Market, la parte que tú puedes servir), **SOM** (Serviceable Obtainable Market, la parte que realistamente puedes capturar). Ver `13`.
- **Firmographics** — datos de la *empresa* para filtrar: industria, tamaño, ubicación, ingresos. Ver `15`.
- **Technographics** — qué *tecnología* usa la empresa (ej. usa Shopify, usa Salesforce), útil para targetear. Ver `15`, `134`.
- **Trigger / señal (signal)** — un evento que indica buen momento para contactar: cambió de cargo, levantó inversión, está contratando, cambió de tecnología. Ver `14`, `37`.
- **Intent data** — datos que muestran que una empresa está *investigando* comprar algo como lo tuyo (ej. leyó reviews en G2). Ver `36`, `131`.
- **Tiering** — clasificar cuentas en A/B/C según qué tan bien encajan, para invertir tu mejor tiempo en las A. Ver `16`.

## Datos y listas

- **List building** — el proceso de armar la lista de cuentas y contactos a contactar. Ver `20`.
- **Enrichment (enriquecimiento)** — agregar datos a un contacto (correo, cargo, teléfono, señales) partiendo de poco. Ver `29`.
- **Waterfall enrichment** — encadenar varios proveedores de datos: si el primero no tiene el correo, prueba el segundo, luego el tercero. Maximiza cobertura. Ver `130`.
- **Email finding** — encontrar el correo de empresa de una persona (por patrón o herramienta). Ver `23`.
- **Verificación (email verification)** — comprobar que un correo existe antes de enviarle, para no rebotar. Ver `28`.
- **Bounce** — un correo que rebota porque la dirección no existe o no recibe. **Hard bounce** (no existe, permanente) y **soft bounce** (temporal, buzón lleno). Bounce alto quema tu dominio. Ver `28`, `40`.
- **Catch-all** — un dominio que "acepta" todos los correos aunque la dirección no exista; difícil de verificar, riesgoso. Ver `28`.
- **Scraping** — extraer datos automáticamente de una web/directorio (LinkedIn, Maps). Legal con matices. Ver `27`.

## Deliverability (que tus correos lleguen a la bandeja)

- **Deliverability** — que tus correos lleguen a la **bandeja de entrada** y no a spam. Si falla, nada más importa. Ver `40`.
- **Warmup (calentamiento)** — proceso de mandar poco correo desde un buzón nuevo e ir subiendo, para que los proveedores confíen en él. Ver `43`.
- **SPF / DKIM / DMARC** — los tres registros técnicos que prueban que tus correos son legítimos y no suplantados. Sin ellos vas a spam. Ver `42`.
- **Dominio secundario** — un dominio aparte (no el de tu empresa) que usas para cold email, para no arriesgar el principal si se quema. Ver `41`.
- **Reputación de dominio/IP** — el "puntaje de confianza" que Gmail/Outlook le dan a tu remitente. Ver `40`, `46`.
- **Blacklist (lista negra)** — lista de dominios/IPs marcados como spam; si caes, tus correos se bloquean. Ver `114`.
- **Spam complaint** — cuando alguien marca tu correo como spam. Pocas quejas hunden tu reputación. Ver `46`.
- **Spintax** — técnica de variar el texto del correo (varias versiones de cada frase) para que no todos sean idénticos y evitar filtros de spam. Ver `45`, `121`.
- **Google Postmaster** — herramienta gratis de Google para ver la reputación real de tu envío. Ver `46`, `113`.

## Copy y cadencias

- **Cold email / email en frío** — correo a alguien que no te conoce ni te buscó. Ver `50`.
- **Cadencia / secuencia** — la serie planificada de toques (correos, mensajes, llamadas) a lo largo de varios días. Ver `60`, `61`.
- **Toque (touch/touchpoint)** — cada intento de contacto individual dentro de la cadencia.
- **Opener** — la primera línea del mensaje; su único trabajo es ganar la segunda línea. Ver `53`.
- **Hook (gancho)** — el ángulo que capta el interés (un dolor, una señal, un dato relevante). Ver `53`.
- **CTA** (Call To Action) — la acción que pides al final ("¿tiene sentido hablar 15 min?"). En outbound pide una micro-conversación, no la venta. Ver `55`.
- **Follow-up** — los toques de seguimiento tras el primer mensaje sin respuesta. La mayoría de reuniones salen de aquí. Ver `63`.
- **Break-up email** — el último correo de la secuencia que anuncia que dejas de escribir; suele sacar respuestas. Ver `63`, `124`.
- **PAS / AIDA / BAB** — frameworks de copy: **PAS** (Problem-Agitate-Solution), **AIDA** (Attention-Interest-Desire-Action), **BAB** (Before-After-Bridge). Ver `56`.

## Métricas

- **Reply rate (tasa de respuesta)** — % de contactados que responden (incluye negativas). Ver `80`.
- **Positive reply rate** — % de respuestas que muestran interés real (lo que de verdad importa). Ver `80`.
- **Open rate (tasa de apertura)** — % que abre el correo. Cada vez menos confiable de medir. Ver `51`.
- **Show rate** — % de reuniones agendadas que de verdad ocurren (los demás son no-shows). Ver `75`.
- **Win rate** — % de oportunidades que se cierran. Es métrica del AE, no del SDR. Ver `05`.
- **Cost-per-meeting (costo por reunión)** — cuánto te cuesta generar una reunión calificada (infra + herramientas + tiempo). Ver `80`, `149`.
- **CAC** (Customer Acquisition Cost) — costo total de adquirir un cliente. Estrategia de negocio → `economist_lushows`.
- **Quota** — la meta de output de un SDR (ej. 10 SQL/mes). Ver `84`, `155`.
- **Ramp** — el tiempo que tarda un SDR nuevo en llegar a productividad plena. Ver `86`.

## Roles y modelo

- **SDR** (Sales Development Rep) — prospecta y agenda; no cierra. **BDR** casi lo mismo, más outbound puro. **AE** (Account Executive) cierra. **AM** (Account Manager) retiene/expande. **RevOps** hace funcionar el sistema. Todo en `03`.
- **Sequencer** — herramienta que envía y automatiza las cadencias (Instantly, Smartlead, Outreach). Ver `33`.
- **CRM** — sistema donde vive la info de leads/clientes (HubSpot, Pipedrive, Salesforce). Ver `32`.

## Estrategias

- **Outbound / Inbound / Allbound** — tú los buscas / ellos te buscan / ambos coordinados. Ver `02`.
- **ABM** (Account-Based Marketing) — outbound coordinado a pocas cuentas grandes, tratando cada cuenta como un mercado. Ver `94`, `160`.
- **Multi-threading** — contactar a varias personas dentro de una misma cuenta a la vez. Ver `162`.
- **Signal-based selling** — hacer outbound disparado por señales/eventos en vez de en frío total. Ver `37`.
- **Spray-and-pray** — el anti-patrón: rociar mensajes genéricos a miles al azar. No lo hagas. Ver `07`.

## Siguiente paso

Este glosario es de consulta: no hay que memorizarlo. Cuando un módulo use un término que se te escapa, vuelve aquí. Para empezar de verdad, el término clave es **ICP** — ve a `10`.

# 26 — Geo-targeting en LatAm

El geo-targeting (a qué lugares muestras tus anuncios) es de las POCAS cercas duras que te quedan en 2026: Advantage+ expande intereses pero respeta tu geografía (ver 20). Eso lo vuelve tu herramienta de control más importante — y donde más plata se quema en LatAm, porque un clic desde donde NO entregas es 100% pérdida. Lee este módulo al configurar cualquier campaña nueva o si vendes con contraentrega/logística limitada.

## País entero vs. ciudades principales

- **E-com con cobertura nacional real** (envías a todo Colombia vía Servientrega/Interrapidísimo/Coordinadora/TCC): **nacional broad**. Más audiencia = subasta más eficiente, CPMs menores fuera de Bogotá/Medellín (donde la subasta es más cara). No "optimices" recortando ciudades por intuición — deja que el breakdown por región (Ads Manager → Breakdown → Region) te diga dónde convierte y dónde no, con datos.
- **Logística limitada** (contraentrega solo en ciudades principales, negocio local, instalación presencial): **SOLO donde entregas**. Cada clic de Leticia cuando solo entregas en Bogotá es plata quemada y, peor, un cliente frustrado en tu WhatsApp ocupándole tiempo al equipo. Lista explícita de ciudades, no "Colombia menos lo lejano".
- Caso mixto (contraentrega en ciudades, anticipado al resto): dos campañas con mensaje distinto ("paga al recibir" vs envío estándar) o una nacional con el creativo aclarando cobertura.

## Presencia: "viven en" vs "recientemente en" — el ajuste que más plata salva

Al elegir ubicación, Meta ofrece (parámetro location_types): **personas que viven en** el lugar, **estuvieron recientemente en** él, o **de visita** (viajeros). Por defecto incluye residentes + recientes — y ese default te cuesta plata si tu negocio es de recurrencia.

- **Negocio local de recurrencia** (gym, mensualidades, domicilios, peluquería): "personas que viven en" — el turista de paso no se inscribe a un gym.
- **Negocio de paso/turismo** (restaurante en zona turística, hotel, experiencia): residentes + recientemente, o hasta "de visita" para captar turistas.
- E-com nacional con envío a domicilio: residentes; un colombiano "recientemente en" Bogotá que vive en Pasto te genera un pedido que igual envías a Pasto — déjalo por defecto solo si envías nacional.

## Radios para negocio local

Para restaurante, gym, clínica, tienda física (ver 57 y 81): pin en la dirección + radio.

| Densidad | Radio | Ejemplo |
|---|---|---|
| Zona densa de ciudad grande | 1-3 km | Chapinero, El Poblado — nadie cruza la ciudad por un café |
| Ciudad intermedia | 3-7 km | Armenia, Valledupar |
| Producto destino (la gente viaja por él) | 7-10 km+ | Clínica especializada, concesionario |

Ajusta por la realidad del tráfico: 5 km en Bogotá pueden ser 50 minutos. Piensa en **minutos de desplazamiento**, no en kilómetros. Y verifica el tamaño alcanzable: un radio que deja menos de ~25-30k personas dispara la frecuencia y el CPM (ver errores).

Nota 2026: **Omnichannel Advantage+** puede optimizar ventas online + tienda física juntas — útil si el negocio local también vende por web/domicilio (ver actualizacion §1).

## Exclusión de zonas (y el caso contraentrega)

Puedes EXCLUIR ubicaciones (botón Exclude). Úsalo cuando:
- **Contraentrega con fraude/devolución alta en una zona**: si tus datos muestran que cierta ciudad te devuelve el 40% de pedidos contraentrega, exclúyela de la campaña contraentrega y véndele solo con pago anticipado. Decisión de datos, no de prejuicio — revisa tus números de devoluciones por ciudad cada mes. Una devolución contraentrega te cuesta flete ida + vuelta + producto manoseado: esa "venta" es pérdida neta (unit economics en **economist_lushows**).
- Zonas donde tu transportadora no llega o cobra el doble.
- El borde de tu radio se come otra ciudad: un radio de 10 km desde Itagüí cubre media Medellín; si no atiendes allá, excluye o reduce el radio.

Tip de creativo local: nombra el lugar en el hook ("Si vives en Laureles...") — el geo-targeting pone la cerca, pero el anuncio que nombra el barrio se siente personal y dobla la atención (ver 37 y 57).

## Trampas clásicas en español

- **Miami/España fantasma**: si segmentas por idioma español o usas audiencias amplias heredadas, puedes terminar mostrando a colombianos en Miami o público en España. Si no vendes allá, la ubicación geográfica (Colombia) ya lo resuelve — pero revisa el breakdown por país si usas configuraciones viejas o targeting mundial por error.
- Dejar "ubicación: Worldwide" en campañas de engagement "para que sea barato": likes de países donde nunca venderás, que luego pudren tus públicos de engagement y tus semillas de LAL (ver 21/22).

## Multi-país (CO + MX + PE + ...)

- **Separa por campaña** si difiere algo estructural: moneda/precio (COP vs MXN vs PEN), oferta, disponibilidad de envío, o el CPM es muy distinto (México suele ser ~40-80% más caro de CPM que Colombia; en presupuesto conjunto el dinero fluye al país de CPA barato y desatiende al otro... lo cual a veces QUIERES y a veces no).
- **Júntalos** en una campaña si todo es igual (mismo precio en USD, producto digital, mismo embudo) y te falta presupuesto para separar: mides por Breakdown → Country y separas cuando un país justifique su propia campaña (regla práctica: cuando un país pueda sostener ~50 conversiones/semana solo, ver 13).
- Creativo: ojo con modismos ("chévere" no viaja a México; "platita" sí, "plata" sí, "lana" es MX); neutraliza o haz variantes por país. El precio en el creativo SIEMPRE en moneda local correcta.

| Mercado | CPM relativo | Nota geo |
|---|---|---|
| Colombia | base (barato LatAm) | contraentrega = revisa devoluciones por ciudad |
| México | más alto | mercado grande; vale campaña propia pronto |
| Perú / Ecuador | medio | dolarizado Ecuador: precio en USD |
| Chile / Argentina | alto / volátil | Argentina: inflación → revisa precios seguido |

## Plantilla: configuración geo por tipo de negocio

| Negocio | Ubicación | Presencia | Exclusiones |
|---|---|---|---|
| E-com nacional (envío todo el país) | País entero | por defecto | zonas de fraude contraentrega (con datos) |
| E-com contraentrega ciudades | Lista de ciudades donde entregas | por defecto | ciudades con devolución alta |
| Restaurante / café de barrio | Pin + radio 1-3 km | recientemente en (zona de paso) o viven en (barrio) | borde que toca otra zona |
| Gym / mensualidad | Pin + radio por minutos | **viven en** | turistas |
| Clínica / concesionario (destino) | Pin + radio 7-10 km+ | viven en + recientemente | — |
| Servicio a domicilio (plomería, etc.) | Ciudad o radio de cobertura real | viven en | fuera del radio de servicio |

## Rutina de revisión geo (primer mes, gratis)

1. Semana 1: Ads Manager → Breakdown → Region. ¿Dónde gastó y dónde convirtió?
2. Cruza con tus devoluciones por ciudad (si es contraentrega): ¿alguna ciudad gasta y devuelve mucho?
3. Decisión con datos: excluir la ciudad problema de la campaña contraentrega, o moverla a pago anticipado.
4. Si es local: ¿el radio alcanza ≥25-30k personas? Si no, amplíalo o el CPM se dispara.
5. Multi-país: Breakdown → Country; separa el país que ya sostiene ~50 conv/semana solo (ver 13).

## Errores comunes — blacklist

- Pautar nacional vendiendo solo en 3 ciudades "para que el algoritmo decida": el algoritmo optimiza clics, no tu logística. La cerca geográfica la pones tú.
- Excluir media Colombia por intuición ("allá no compran"): decisiones de geo con breakdown y datos de devoluciones, no con estereotipos.
- Radio de 1 km en zona poco densa: audiencia diminuta, frecuencia disparada, CPM alto. Mínimo viable: decenas de miles de personas alcanzables.
- "Recientemente en" para un gym: cobras la inscripción a alguien que estaba de paso. "Viven en".
- CO+MX+AR en un presupuesto conjunto con monedas locales distintas: el reparto se va al CPM barato y el reporte mezcla peras con manzanas.
- Olvidar revisar Breakdown → Region/Country el primer mes: es gratis y te dice exactamente dónde se va la plata.
- No excluir la zona de fraude en contraentrega "para no perder ventas": esa venta devuelta es pérdida.
- Copiar la campaña de Colombia a México cambiando solo el país: precios en COP en el creativo, modismos locales y oferta sin ajustar — cada país merece su revisión completa.

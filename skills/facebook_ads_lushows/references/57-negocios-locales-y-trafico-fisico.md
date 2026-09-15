# 57 — Negocios locales y tráfico físico

Pauta para el negocio de barrio/ciudad: restaurante, peluquería, gimnasio, taller, consultorio, tienda física. La lógica cambia: tu mercado es un radio de kilómetros, tu "conversión" es una reserva por WhatsApp o alguien entrando por la puerta, y casi nunca hay píxel que la vea. Lee este módulo si tu cliente tiene que LLEGAR físicamente a ti. Jerga: "dayparting" = programar la pauta por franjas horarias; "GBP" = *Google Business Profile*, el Perfil de Negocio de Google.

## Geo por radio: la decisión #1

En el ad set, segmenta por **pin + radio** sobre tu ubicación (no por "ciudad" completa). El radio correcto depende de categoría y densidad (fundamentos de geo: ver 26):

| Categoría | Radio típico |
|---|---|
| Comida / café / domicilios | 2-4 km (nadie cruza la ciudad por un almuerzo) |
| Belleza, gimnasio, retail de barrio | 3-6 km |
| Servicios especializados (clínica, taller, academia) | 10 km+ o ciudad completa — por algo único sí se desplazan |

- Densidad manda: 3 km en Chapinero son 200.000 personas; 3 km en un pueblo no llenan el aprendizaje (ver 13) — amplía el radio antes que el presupuesto.
- Usa "personas que viven en o estuvieron recientemente en" (default) para domicilios; para turismo/zonas de paso, "personas recientemente en esta ubicación".

## Objetivo correcto según el caso

- **Reservas / pedidos / cotizaciones** → **Engagement → WhatsApp (CTWA, ver 50)**: el barrio reserva por WhatsApp, no por web. Atiende en minutos (ver 51/54).
- **Awareness de apertura / "existo"** → Alcance (Awareness) geolocalizado: frecuencia 2-3/semana sobre el radio. Una de las pocas excepciones donde Awareness sí es para pymes (ver 11/59).
- **El contenido vende solo** (food porn, antes/después) → tráfico al perfil de IG puede funcionar para construir audiencia local que luego retargeteas (ver 21) — pero es el plan B, no el A.
- Leads con instant form (ver 52) para servicios con cotización (odontología, academias): pregunta filtro de zona SIEMPRE.

> 2026: **Omnichannel Advantage+** optimiza ventas online + tienda física juntas, y existe la opción de objetivo de **tráfico a tienda / store traffic** para cadenas con varias sedes (ver `actualizacion-2026-06` §1). Para el negocio de una sola sede, CTWA + Awareness local sigue siendo lo que más rinde.

## Formatos locales que funcionan

Lo local gana con autenticidad, no con producción (anatomía del ad: ver 31):

- **El dueño a cámara**: "Soy Carlos, del taller de la 45. Esta semana...". La cara del dueño es targeting emocional de barrio.
- **El producto saliendo de cocina/proceso**: el plato emplatándose, el corte de pelo terminándose, el antes/después del servicio.
- **Reseñas de vecinos**: pantallazo de reseña real + "a 10 minutos de tu casa".
- Menciona la zona EN el copy: "Domicilios en Laureles y alrededores" — el filtro geográfico también es creativo.

### Plantilla de copy local

```
🍔 ¿Antojo en [Zona]? Domicilio en 30 min o recoge en la 45 con 30.
Esta semana: [oferta con fecha de fin] 👇
Escríbenos "[PALABRA-CLAVE]" por WhatsApp y te lo despachamos ya.
📍 A [X] minutos de [referencia del barrio]
```

## Promociones con fecha y horarios de pauta

- Promos de apertura/fechas (Día de la Madre, aniversario): campaña con **lifetime budget y fecha de fin** (ver 18) — gasta todo dentro de la ventana y muere sola.
- **Programación por horas** (dayparting): solo disponible con lifetime budget. Si el presupuesto es chico y vendes almuerzos, pauta 10am-1pm y 5-8pm en vez de regar 24h. Con presupuesto holgado, déjalo abierto: Meta ya modula por hora.
- Restaurante: el ad visto a las 11:40am vale 5× el de las 4pm. Sincroniza pauta con momento de decisión.

### Dayparting por tipo de negocio (referencia)

| Negocio | Franjas que más rinden |
|---|---|
| Restaurante almuerzos | 10:30am-1:30pm |
| Restaurante cena / domicilios noche | 5:30-9:00pm + fin de semana |
| Peluquería / belleza | Jueves-sábado, 9am-6pm |
| Gimnasio (captación) | Lunes-martes + arranques de mes/año |

## El combo con Google Maps / Perfil de Negocio

Meta y Google juegan posiciones distintas: **Meta trae el antojo** (demanda que no te buscaba), **Maps cierra la ruta** (el que ya decidió ir te busca, mira reseñas y llega). Necesitas ambos:

- Perfil de Negocio de Google (GBP) completo: horario, fotos, botón de WhatsApp, y un flujo constante de reseñas — el local con 4.8★ y 200 reseñas cosecha lo que tu pauta siembra.
- CTA "Cómo llegar" existe en ads de Meta con objetivo de awareness local; útil para apertura.
- La búsqueda local con intención ("restaurante cerca de mí") se captura en Google, no en Meta: **Local Services Ads y Search local → google_ads_lushows**. La presencia local completa (GBP, reseñas, SEO local): rutea a desingweb 85/42.

## Medir sin píxel de tienda física

No hay píxel en la puerta. Soluciones honestas:

1. **Cupón/palabra clave por WhatsApp**: "Escribe PROMO2X1" o "vi el anuncio del 2x1" → cada mención es una conversión atribuible. La palabra cambia por campaña.
2. **Conteo honesto semanal**: ventas/reservas de la semana vs gasto, comparado contra las semanas sin pauta. Burdo y suficiente para decidir (mismo espíritu que 53 nivel 1).
3. Pregunta de rigor al cliente nuevo: "¿cómo nos conociste?" — que el equipo la haga y la anote, siempre.
4. Si capturas la reserva por WhatsApp, ya tienes el `referral`/`ctwa_clid` (ver 53): atribuyes la reserva al ad exacto aunque la entrega sea física.

## La matemática del negocio local (ejemplo)

Restaurante de almuerzos, ticket promedio $25.000 COP, margen 60% ($15.000), cliente que vuelve ~4 veces/mes:

```
Presupuesto pauta: $300.000 COP/mes (radio 3 km, dayparting almuerzo)
Conversaciones/reservas atribuibles: ~120 (palabra clave + conteo)
Clientes nuevos que pisan el local: ~40 (33% de los que escriben)
CPA primera visita: $300.000 / 40 = $7.500
```

A primera vista $7.500 por traer a alguien que deja $15.000 de margen parece ajustado. Pero el cliente local **vuelve**: si regresa 4 veces el primer mes y luego es habitual, su LTV de 3 meses son ~$180.000 de margen. El CPA de $7.500 es regalado. En negocio local **la primera visita es la inversión, la recompra es el negocio** — por eso awareness local + pauta sostenida valen la pena donde no valdrían para una venta única (modela el LTV con economist_lushows).

## Calendario local: las fechas que mueven caja

| Fecha | Negocio que más explota |
|---|---|
| Día de la Madre (may) | Restaurantes, belleza, floristerías, regalos |
| Amor y Amistad (sep, Colombia) | Restaurantes, regalos, planes en pareja |
| Aniversario de apertura | Cualquier local — promo + awareness de saturación |
| Quincenas (15 y 30) | Casi todo: la caja del cliente se llena, sincroniza promos |
| Diciembre / novenas | Restaurantes, eventos, regalos |

Pauta estas fechas con **lifetime budget + fecha de fin** (ver 18) para que la promo gaste dentro de la ventana y muera sola — nada de "2x1 de mayo" corriendo en junio.

## Errores comunes — blacklist

- Pautar a toda la ciudad un negocio de barrio: pagas impresiones de gente a 40 minutos que jamás irá.
- Radio de 1 km en zona poco densa: audiencia mínima, aprendizaje que nunca arranca, CPM por las nubes (ver 13).
- CTWA local sin nadie respondiendo en horas pico: el que pide almuerzo a las 12:10 no espera a las 2pm (ver 51).
- Awareness eterno sin nunca pedir la venta: a la semana 3, el barrio ya te vio; pasa a CTWA con oferta.
- Promo con fecha en campaña de presupuesto diario sin fecha de fin: el "2x1 de mayo" corriendo en junio.
- Ignorar Google/reseñas porque "ya pauto en Meta": el antojo que Meta crea se pierde si Maps te muestra con 3.2★ y fotos de 2019 (google_ads_lushows).
- No usar palabra clave por campaña: sin ella no sabes qué ad llenó las mesas el sábado.

# 86 — Playbook: Eventos y entretenimiento

Conciertos, fiestas, festivales, obras de teatro, talleres presenciales, stand-up, ferias (un lanzamiento de Bendita Pola entra aquí). El vertical con la ventaja que todos los demás fingen tener: **la urgencia es REAL**. La fecha no se mueve, las boletas se acaban de verdad, el FOMO es honesto (ver 41). El playbook es una carrera contra el calendario: fases de precio, mensaje por fase, y capturar el público del evento para que el siguiente cueste la mitad. Este es el playbook de Bendita Pola: urgencia/FOMO honestos + captura de la base.

## Las fases de venta

| Fase | Cuándo | Precio | Mensaje |
|---|---|---|---|
| **Early bird** | Apertura (6-10 semanas antes) | El más bajo, limitado | "Precio de lanzamiento para los primeros X" — premia a la base fiel |
| **General** | El grueso del periodo | Precio pleno | La experiencia, el lineup, la prueba social |
| **Última semana** | 7 días antes | Pleno o last-minute | Urgencia logística real: "quedan N", "cierre de venta online el jueves" |
| **Día del evento** | Si hay puerta | Puerta (más caro) | "Aún alcanzas" — solo si conviene operativamente |

Implementación: **lifetime budget con fechas por fase** (ver 18) — una campaña/ad set por fase, programada de antemano. El presupuesto NO es lineal: carga 30-40% en early bird (la base compra barato y financia), baja en general, vuelve a subir la última semana (cuando la urgencia convierte mejor).

## La cuenta concreta — públicos en paralelo

| Campaña / ad set | Tipo | Objetivo | Creativos | Medición |
|---|---|---|---|---|
| **Frío amplio** | Advantage+ Sales (ticketera) o Engagement→WhatsApp | Purchase / conversación | aftermovie · lineup+venue en video | costo por boleta |
| **Engagers** (IG/FB/artista 90-365d) | Sales / tráfico | Purchase | prueba social "ya se fue el 70%" (si es verdad) | ROAS por fase |
| **Compradores pasados** (custom audience) | Sales | Purchase | "vuelve, esta edición es más grande" | el público que convierte a 5-10x |
| **Carrito de ticketera** (retargeting) | Sales, 1-14 días | Purchase | "tu boleta te espera, cierra hoy" | la venta más barata del funnel |

**Geo**: la ciudad del evento + alrededores según el "draw" (poder de convocatoria): fiesta local = la ciudad; festival grande = región/país con el ángulo "vale la pena viajar".

## Creativos por fase

- **Inicio**: el **aftermovie** del año pasado (video-resumen de la experiencia) o, si es primera edición, lineup + venue + la promesa en video vertical (ver 34). Vendes la noche, no la boleta.
- **Medio**: prueba social de boletas volando — "ya se fue el 70% de early bird" — **SOLO si es verdad** (ver 43/44; la escasez falsa se descubre el día del evento medio vacío y mata tu credibilidad para el siguiente).
- **Final**: logística y urgencia — "últimas boletas", "esto es lo que te espera el sábado", recordatorio de fecha/lugar/hora. Testimonios de quien ya compró ("nos vemos allá").

## Venta: ¿WhatsApp o ticketera?

- **CTWA con cierre en chat** (ver 50/55): el promotor vende por WhatsApp, cobra por **Nequi/transferencia** y manda la boleta digital. Muy LatAm, cero comisión de ticketera, ideal para eventos chicos/medianos (<1.500 personas). Contra: medición manual — reporta ventas vía CAPI de chat capturando el `ctwa_clid` (ver 53, `actualizacion-2026-06`) — y carga operativa: necesitas quien responda (o bot) viernes en la noche. La **ventana gratis de 72h del CTWA** hace la mensajería casi gratis.
- **Ticketera con píxel** (ver 05): medible, escalable, Purchase real para optimizar. Contra: comisión 8-15% y checkout con fricción. Para eventos grandes, no hay debate: ticketera + Dataset + CAPI.
- Híbrido común: early bird por WhatsApp a la base, general por ticketera.

## El día después: el activo compuesto

El error del promotor amateur: el evento termina y la data muere. El de élite captura: lista de compradores (custom audience), asistentes registrados por WhatsApp, engagers del contenido del evento, videos del evento como creativo del siguiente. **Cada evento abarata el siguiente**: a la 4a edición, el 60% de boletas sale de públicos propios casi gratis. Pide el dato (correo/WhatsApp) en la compra y en la entrada. Ojo 2026: si usas custom audiences puede pedirse **declaración de origen del dato y consentimiento** (ver `actualizacion-2026-06`).

## Ofertas tipo del vertical

- **Early bird limitado** ("primeras 100 a precio de lanzamiento"): escasez real que financia.
- **Combo de mesa/grupo** ("mesa para 6 con botella"): sube el ticket promedio.
- **2x1 entre semana** o **preventa por fases**: urgencia honesta sin regalar.
- **Pack de temporada/abono** (varios eventos): asegura recurrencia de la base.

## Presupuesto y benchmarks honestos (Colombia)

- Regla de bolsillo: **8-15% del revenue objetivo de boletería** en pauta total. Evento de $30M COP en boletas → $2.5-4.5M de pauta repartida en fases.
- Costo por boleta vendida vía Meta: **5-15% del valor de la boleta** (boleta de $80.000 → $4.000-$12.000 de pauta). CPM eventos $7.000-$18.000.
- Caveat fuerte: depende del draw del artista, la base previa y la ciudad; una primera edición sin marca puede costar el doble, un artista con fans la mitad.
- Mide ventas por fase, no al final: si early bird no se mueve, el problema es la oferta o el draw — ajusta YA, no en la semana final.

## Compliance

Eventos con alcohol (cervezas, fiestas): respeta las políticas de alcohol de Meta — targeting 18+ obligatorio en Colombia, sin menores en creativos, sin incitar exceso (ver 08; landing de bebidas: desingweb 84). Sorteos de boletas: reglas de promociones de Meta + términos visibles.

## El draw manda: lee el termómetro temprano

El "draw" (poder de convocatoria del artista/marca del evento) define si la pauta es fácil o cuesta arriba — y se mide en los primeros 3-5 días de early bird, no al final. Termómetro: si la pauta de early bird vende boletas a 5-10% del valor de la boleta, el draw es sano y solo tienes que dosificar presupuesto por fase. Si está al 25%+ del valor de la boleta y las conversaciones son tibias, el problema NO es la pauta: es el lineup, el precio o la fecha — y se arregla con oferta (más artistas anunciados, combo de grupo, fecha mejor comunicada), no subiendo presupuesto. El error caro es "meterle más plata" a un evento que el mercado no quiere: amplificas el rechazo. La pauta de eventos es honesta brutalmente rápido — úsala como sensor de demanda real desde el día 3 y decide ahí si sigues, ajustas la oferta o recortas pérdidas. Esa lectura temprana es lo que separa al promotor que escala del que pierde el depósito del venue.

## Ruteo a skills hermanas

Cierre de boleta por chat y manejo de "¿y si llueve / puedo pagar después?" → ventas_lushows. Landing del evento con fecha/lineup/precios y compra en 2 clics → desingweb-lushows. Cartel, identidad del evento y aftermovie → directorcreativo_lushows. Presupuesto del evento y punto de equilibrio de boletería → economist_lushows. Búsquedas "boletas [artista] [ciudad]" → google_ads; teaser y FOMO nativo → tiktok_ads.

## Errores comunes — blacklist

- Arrancar pauta 10 días antes del evento: las fases existen porque la venta temprana financia y la urgencia tardía cierra — tarde pierdes ambas.
- "Últimas boletas" con el 60% sin vender: te lo cobran en la próxima edición.
- Presupuesto lineal en vez de cargado en early bird y última semana.
- No capturar compradores: pagar público frío completo para el evento siguiente.
- Olvidar el remarketing al carrito de la ticketera: la venta más barata del funnel.
- Geo nacional para una fiesta de barrio: nadie viaja 8 horas por un cover de $30.000.
- Vender por WhatsApp sin nadie respondiendo viernes en la noche — justo cuando la gente decide su fin de semana.
- No capturar el `ctwa_clid` y juzgar la pauta por "conversaciones" en vez de boletas (ver 53).

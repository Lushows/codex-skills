# 77 — Q4 y temporada alta

Lee este módulo cuando se acerque una temporada de alta demanda: Black Friday / Cyber Monday (BFCM), Navidad, prima de fin de año en LatAm (la prima de diciembre que infla el bolsillo del comprador colombiano), día de la madre, Hot Sale (México), Amazon Prime Day, vuelta a clases. En estas fechas todo cambia a la vez — más demanda, pero también más competencia y CPCs más caros — y la campaña que volaba en octubre puede ahogarse en noviembre si la manejas igual. La clave es **prepararte antes, ajustar fino durante, y no entrar en pánico cuando los costos suban (porque van a subir).**

Recuerda el marco: Google captura demanda. En temporada alta la demanda explota — mucha más gente buscando con intención de compra — así que Google suele ser el canal **más eficiente para capturar esa ola**, mientras Meta y TikTok empujan la generación y el descubrimiento (ver `facebook_ads_lushows`, `tiktok_ads_lushows`). El problema no es falta de demanda; es que todos los competidores pujan por la misma.

## Qué cambia en temporada (y por qué)

| Variable | Qué pasa | Implicación |
|---|---|---|
| **CPCs** | Suben (más competidores pujando) | Tu CPA sube aunque hagas todo bien |
| **Volumen de búsqueda** | Explota | Hay mucha más demanda que capturar |
| **Tasa de conversión** | Suele subir (gente en modo compra) | Compensa parte del CPC más caro |
| **Presupuesto** | Se agota antes (más clics caros) | Riesgo de quedarte sin plata a media campaña |
| **Comportamiento del bidding** | Aprende del pasado, que NO se parece al pico | Riesgo de que llegue desprevenido |

El error mental clásico: ver el CPC subir en BFCM y apretar el target en pánico. Pero si la conversión también sube y el ticket está, el CPA mayor puede seguir siendo rentable. **Juzga por CPA/ROAS final, no por el CPC asustadizo** (ver 60-metricas, 64-ROAS-real).

## Calendario LatAm de referencia (jun-2026)

| Evento | Fecha aprox. | Empieza a calentar |
|---|---|---|
| Día de la madre (CO/MX) | mayo | 2–3 semanas antes |
| Hot Sale (MX) | mayo | 1 semana antes |
| Amazon Prime Day | jul | días antes |
| Vuelta a clases | ene / ago | 2 semanas antes |
| Black Friday / Cyber Monday | finales nov | 1–2 semanas antes |
| Prima + Navidad (CO) | dic | desde inicios de dic |

Conoce los picos de TU mercado y producto; no todos aplican. (Calendario detallado y ajuste de presupuesto mensual, ver 19-calendario.)

## Preparación: ajusta el algoritmo ANTES (semanas, no días)

Smart Bidding aprende del pasado reciente — y el pasado reciente NO se parece a Black Friday. Para que no lo agarre desprevenido:

1. **Seasonality adjustments (ajustes estacionales).** Herramienta de Google donde le avisas: "estos días esperaré una tasa de conversión más alta de lo normal". Úsala para **eventos cortos e intensos (1–7 días**, tipo BFCM o un flash sale), NO para temporadas largas. Le dice al bidding que puje más agresivo durante el pico sin esperar a "darse cuenta" tarde. Para subidas de demanda largas y graduales (toda la temporada decembrina), NO la uses — deja que el bidding aprenda solo o ajusta target/presupuesto en pasos.
2. **Sube el presupuesto ANTES del pico, en pasos.** No esperes al viernes de BFCM para subir presupuesto de golpe (reinicia el aprendizaje justo en el peor momento). Empieza a subir en pasos del ~20% (ver 72-esc-vertical) **una o dos semanas antes** para que el sistema esté estable y entrenado cuando llegue la ola.
3. **Revisa presupuestos compartidos.** Si varias campañas comparten un mismo presupuesto, en temporada una se puede comer la plata de las otras. Sepáralos o ajústalos antes del pico.
4. **Entra antes, sal después.** La demanda empieza a calentar días antes del evento oficial y sigue caliente días después (rezagados, segundas compras, gente que esperó descuentos). Estar arriba antes que la competencia te da clics más baratos al inicio; quedarte un poco después captura cola barata cuando otros ya apagaron.
5. **Prepara las landings y la oferta.** El tráfico caro de temporada se desperdicia si la landing no refleja la promo, o si el stock/checkout se cae bajo carga (ver `desingweb-lushows`). Y ten al equipo de cierre listo para el WhatsApp que entra (ver `ventas_lushows`).
6. **Sube los activos/feed creativos de temporada.** En PMax/AI Max actualiza imágenes y textos con mensaje de la promo; el algoritmo necesita activos frescos para el momento (ver 12-PMax, `actualizacion-2026-06`).

## Checklist de preparación (2 semanas antes)

- [ ] Verificar tracking 100% sano (conversión rota en temporada = desastre, ver 14-conversion)
- [ ] Subir presupuesto en pasos del 20%, empezando ya
- [ ] Configurar seasonality adjustments solo si hay evento corto (1–7 días)
- [ ] Separar presupuestos compartidos
- [ ] Refrescar RSA/activos con mensaje de promo
- [ ] Landing y checkout probados bajo carga
- [ ] Negativas al día (la basura estacional llega)
- [ ] Equipo de cierre/atención listo

## Durante el pico: disciplina, no pánico

- **No reinicies el aprendizaje en pleno evento.** Cambios bruscos de target/presupuesto durante BFCM = aprendizaje errático en las 48 horas más caras del año. Prepara antes, ajusta fino durante (ver 70-reglas).
- **Vigila que no te quedes sin presupuesto a medio día.** Si IS Lost por budget se dispara en horas pico, súbelo en pasos — pero idealmente ya lo subiste antes.
- **Mira el reporte de términos de búsqueda más seguido.** En temporada entra tráfico nuevo y broad/PMax/AI Max pueden traer basura estacional; limpia con negativas (ver 22-negativas).
- **No aprietes el target porque el CPC asusta.** El CPC sube para todos; juzga por CPA/ROAS final (ver 74).

## Después del pico: aterriza en pasos

- **Baja el presupuesto en pasos**, no de golpe (bajar brusco también sacude el aprendizaje).
- **Retira los seasonality adjustments** cuando termine el evento. Si los dejas puestos, el bidding seguirá pujando agresivo sin la demanda que lo justificaba, quemando plata.
- **Espera la resaca:** tras el pico la demanda y la conversión bajan unos días; no es que se rompió nada, es la cola del evento.

## Errores comunes — blacklist

- **Subir el presupuesto de golpe el día del evento.** Reinicia el aprendizaje en las horas más caras y competidas del año; prepara una o dos semanas antes en pasos (ver 72-esc-vertical).
- **Apretar el target en pánico porque el CPC subió.** El CPC sube para todos en temporada; si la conversión y el ticket acompañan, el CPA mayor puede ser rentable. Juzga por CPA/ROAS final (ver 64-ROAS-real).
- **Usar seasonality adjustments para temporadas largas.** Están diseñados para eventos cortos (1–7 días); mal usados distorsionan el bidding por semanas.
- **Olvidar quitar los seasonality adjustments al terminar.** El bidding sigue pujando agresivo sin la demanda real, quemando plata después del pico.
- **No revisar presupuestos compartidos.** Una campaña se come la plata de las otras justo cuando todas necesitan rendir.
- **Entrar tarde y salir temprano.** Pierdes los clics baratos del calentamiento previo y la cola barata posterior; la competencia los captura por ti.
- **Tratar el pico como un mes normal.** Misma gestión = quedarte sin presupuesto, no capturar la ola y dejar ventas a la competencia.
- **Mandar tráfico caro de temporada a una landing/checkout que se cae bajo carga.** Quemas el momento más rentable del año (ver `desingweb-lushows`).

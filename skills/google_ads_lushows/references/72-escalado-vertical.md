# 72 — Escalado vertical

Lee este módulo cuando una campaña esté funcionando — CPA bajo control, ROAS sano — y quieras meterle más dinero para conseguir más ventas **del mismo tipo**. Eso es escalado vertical: subir el presupuesto de lo que ya gana, sin abrir nada nuevo. Suena fácil y es donde más gente se estrella: suben el presupuesto de golpe, reinician el aprendizaje de Smart Bidding, y la campaña que iba perfecta se vuelve errática justo cuando querían crecer. La clave es **subir despacio para no romper lo que funciona, y solo cuando hay demanda sin capturar.**

Escalar vertical solo tiene sentido cuando hay demanda esperando. Google captura demanda existente (no la genera, eso es Meta — ver `facebook_ads_lushows`); si ya estás capturando casi toda la búsqueda disponible, subir presupuesto solo encarece los clics sin traer ventas nuevas. Por eso antes de escalar hay que saber **si queda espacio.**

## ¿Hay techo o hay espacio? La métrica que decide

La señal maestra es el **Impression Share perdido (IS Lost)** — el porcentaje de subastas en las que tu anuncio NO apareció, y por qué. Hay dos versiones, y significan cosas OPUESTAS:

| Métrica | Qué significa | ¿Hay espacio para escalar vertical? |
|---|---|---|
| **Search Lost IS (budget)** alto | Te quedaste sin presupuesto; perdiste subastas por plata | **SÍ — hay demanda esperando. Sube presupuesto.** |
| **Search Lost IS (rank)** alto | Perdiste por Ad Rank bajo (QS/puja, no plata) | **NO — más presupuesto no ayuda. Mejora QS/landing/puja** (ver 36-QS, 15-pujas) |

Regla práctica de decisión:

| IS Lost (budget) | Diagnóstico | Acción |
|---|---|---|
| > 15% | Mucha demanda sin capturar | Escalar vertical agresivo (pasos del 20%) |
| 5–15% | Algo de espacio | Escalar vertical moderado, vigilar CPA |
| < 5% (≈0%) | Casi topado | Parar vertical → pasar a horizontal (ver 73) |

Si tu IS Lost por presupuesto es ~0% y el de rank es alto, subir presupuesto no traerá casi nada: el problema es competitividad, no dinero. Ahí mejoras Quality Score, oferta o landing antes de gastar más (ver 36-QS, 94-auction-insights).

## Cómo subir: pasos del ~20%

La mecánica para no romper Smart Bidding:

1. **Sube el presupuesto en pasos de ~20%**, nunca más. De $100.000 COP/día a máximo ~$120.000, no a $200.000. Un salto grande sacude el modelo de puja y entra en aprendizaje (ver 13-smart-bidding).
2. **Espera ~1 ciclo de conversión + unos días** entre subidas (mínimo varios días; idealmente ~1–2 semanas si el ciclo es largo). No subas otra vez "porque el primer día fue bueno".
3. **Verifica que el CPA/ROAS se mantuvo** tras estabilizarse. Si el CPA se mantuvo y sigues con IS Lost por presupuesto, repite el paso del 20%.
4. **Si el CPA empezó a subir al escalar**, llegaste a demanda más cara o menos calificada: ahí decides si aflojar el tROAS/tCPA conscientemente para ganar volumen (ver 74-tROAS-escalar) o si paras de escalar.
5. **Nunca subas presupuesto Y aflojes target el mismo día.** Uno, estabiliza, mide, luego el otro (ver 70-reglas).

### Ejemplo numérico (paso a paso)

Campaña de captura GastroLatam a $80.000 COP/día, CPA $25.000, IS Lost (budget) 22%:

| Semana | Presupuesto/día | CPA observado | IS Lost budget | Decisión |
|---|---|---|---|---|
| 0 | $80.000 | $25.000 | 22% | Subir +20% |
| 1–2 | $96.000 | $26.000 | 14% | CPA estable, sigue espacio → subir |
| 3–4 | $115.000 | $27.000 | 8% | Margen aún ok → subir un paso más |
| 5–6 | $138.000 | $33.000 | 3% | CPA saltó, IS casi 0 → parar, ir horizontal |

Así escalas sin nunca disparar el aprendizaje, y reconoces el techo cuando el CPA sube y el IS budget se acerca a cero al tiempo.

## Señales de que llegaste al techo

Deja de escalar vertical y pasa a horizontal (ver 73-esc-horizontal) cuando:

- **IS Lost por presupuesto cae cerca de 0%** — ya capturas casi toda la demanda disponible para esas keywords; más plata solo sube el CPC.
- **El CPA sube de forma sostenida** con cada paso — estás raspando el fondo del barril de intención.
- **El IS Lost que queda es de rank, no de presupuesto** — el problema ya no es plata, es competitividad (ver 94).

En ese punto, la respuesta NO es más presupuesto en la misma campaña: es abrir nuevas keywords, geos o tipos de campaña (Search → PMax → Demand Gen, ver 73-esc-horizontal). Forzar más plata en una campaña topada es quemar dinero.

## Verifica que el margen aguanta antes de cada paso

Escalar vertical sube el volumen pero a menudo a peor CPA marginal: las primeras conversiones del día son las baratas (alta intención), las últimas son las caras. Antes de cada paso pregúntate: **¿el CPA al que voy a comprar las conversiones extra sigue dejando margen?** Si el CPA marginal supera tu CPA máximo viable, más volumen es más pérdida, no más ganancia. Valida unit economics y CPA máximo (ver 64-ROAS-real, `economist_lushows`). Y si el cuello de botella real es el cierre (leads que llegan pero no compran), no es problema de Google — es de `ventas_lushows`.

## Errores comunes — blacklist

- **Subir el presupuesto de golpe (50–100%).** Reinicia el aprendizaje de Smart Bidding; la campaña ganadora se vuelve errática justo cuando querías crecer (ver 13-smart-bidding).
- **Escalar sin mirar el IS Lost.** Si pierdes por rank y no por presupuesto, más plata no trae ventas — solo encarece. Diagnostica primero (ver 94-auction-insights).
- **Subir otra vez al día siguiente porque "fue un buen día".** No estabilizaste; estás apilando shocks de aprendizaje. Espera el ciclo (ver 70-reglas).
- **Forzar plata en una campaña ya topada (IS budget ~0%).** Solo sube el CPC. Toca escalar horizontal, no vertical (ver 73-esc-horizontal).
- **Subir presupuesto Y apretar/aflojar el target el mismo día.** Dos cambios juntos = diagnóstico imposible. Uno a la vez.
- **Confundir IS Lost de rank con IS Lost de budget.** Significan cosas opuestas; actuar sobre el equivocado desperdicia presupuesto o esfuerzo.
- **Escalar sin verificar que el margen aguanta el CPA mayor.** Más volumen a peor CPA puede dejar de ser rentable; valida unit economics (ver 64-ROAS-real, `economist_lushows`).
- **Subir presupuesto justo antes de Q4 de golpe.** En temporada hazlo en pasos y con antelación, no de un salto en el día pico (ver 77-Q4).

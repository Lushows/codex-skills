# 17 — Framework de testing

Lee este módulo cuando quieras "probar cosas" y no sepas por dónde empezar, cuando hayas cambiado 5 cosas a la vez y ahora no sepas cuál funcionó, o cuando alguien te diga "prueba públicos" y tu instinto (correcto) sea probar creativos primero. En TikTok el testing tiene un orden sagrado: **creativo > oferta > audiencia > ajustes**. Testear en el orden equivocado quema presupuesto buscando la respuesta en el lugar incorrecto — como buscar las llaves bajo el poste porque ahí hay luz, no porque ahí las perdiste.

## El frame: en TikTok el creativo PESA MÁS que en Meta

En Meta el público y el algoritmo cargan buena parte del peso; en TikTok **el creativo ES el targeting** (ver 20) y carga casi todo. El video decide a quién le aparece tu anuncio y si esa persona compra. Por eso el testing de TikTok es, ante todo, una **fábrica de creativos**: descubres ganadores baratos en una campaña de testing y los migras a tu motor de escala (Smart+, ver 12). El 70% de tu energía de testing va al creativo. Este es el orden, de mayor a menor impacto:

| Prioridad | Qué testeas | Por qué pesa tanto | Cruce |
|---|---|---|---|
| **1. Creativo** | Hooks, formatos, ángulos, UGC vs marca, sonido | El video decide a quién le llega y si compra | ver 68, 39 |
| **2. Oferta** | Precio, bono, garantía, urgencia, bundle | Cambia la conversión más que cualquier ajuste de cuenta | ver 41 |
| **3. Audiencia** | Broad vs interés, retargeting, exclusiones | En TikTok importa poco; broad suele ganar | ver 20 |
| **4. Ajustes de cuenta** | Puja, evento, presupuesto | Optimización fina, no descubrimiento | ver 14, 15 |

Si tu campaña no jala, el 80% de las veces el problema es el **creativo o la oferta**, NO el público ni la puja. La gente pierde semanas testeando públicos cuando el video simplemente no engancha en los primeros 3 segundos.

## El hook lo es casi todo

Dentro del creativo, lo que más mueve la aguja es el **hook** (el gancho: los primeros 1–3 segundos). Si el hook no detiene el scroll, nada más importa — nadie ve tu oferta ni tu CTA. La métrica que delata un hook flojo es el **hold rate / 3-second view rate** y la retención a 6s (ver 68): si la gente abandona en el segundo 2, el hook está roto, no la oferta.

Testea **muchos hooks distintos sobre el mismo cuerpo de video** antes de producir 10 videos completos. Es la forma más barata de descubrir qué ángulo engancha. Plantilla de hooks para probar (sobre el mismo cuerpo):

1. **Hook de dolor** — "Si tu restaurante vende y vende pero no te queda plata, mira esto."
2. **Hook de resultado** — "Así supe que estaba perdiendo $1.200.000 al mes sin darme cuenta."
3. **Hook de demostración** — empieza con la pantalla del Excel llenándose solo.
4. **Hook de pregunta/callout** — "¿Sabes cuánto te cuesta de verdad un plato? El 90% no."
5. **Hook de contraste/antes-después** — "Antes adivinaba mis precios. Ahora los calculo en 2 minutos."

Variables creativas que vale la pena testear, en orden:
1. **Hook** (gancho de apertura) — el de mayor impacto.
2. **Ángulo / mensaje** (problema, resultado, demostración, testimonio).
3. **Formato** (UGC, voz en off, texto en pantalla, creador vía Spark, ver 34).
4. **CTA y oferta en pantalla**.

## A/B nativo y creative testing: no contamines las variables

TikTok tiene **A/B test nativo** (*split test*): divide la audiencia en grupos sin solapamiento para comparar limpio. La regla número uno del testing científico: **cambia UNA variable a la vez**.

| Si quieres saber… | Cambia SOLO… | Deja igual… |
|---|---|---|
| Qué hook engancha | El hook | Cuerpo, oferta, público, presupuesto |
| Qué oferta convierte | La oferta | Creativo, público |
| Si broad gana a interés | El público | Creativo, oferta, presupuesto |

Si cambias hook + oferta + público al mismo tiempo y mejora, **no sabes qué lo causó** — y no puedes repetir el éxito. Eso no es testing, es lotería.

Dos enfoques válidos, elige según tu presupuesto:

- **A/B nativo (split test):** ideal para decisiones limpias de una variable (creativo A vs B). Más riguroso, pero más caro porque necesita volumen en cada brazo. Úsalo para decisiones grandes (¿UGC o marca? ¿oferta A u oferta B?).
- **Creative testing dentro de un ad group broad:** metes 5–8 creativos en un mismo ad group y dejas que TikTok reparta hacia los ganadores. Más barato y rápido, menos "limpio" (TikTok no reparte parejo) pero suficiente para descubrir ganadores creativos con presupuesto colombiano. Es el caballo de batalla del día a día.

## El flujo de testing semanal (la fábrica)

| Día | Acción |
|---|---|
| Lunes | Entran 3–5 creativos nuevos al ad group de testing (broad, lowest cost) |
| Mar–Jue | No tocar. Dejar correr (varianza alta, ver 13) |
| Viernes | Revisar hold rate y CPA por creativo (ver 68); marcar 1–2 posibles ganadores |
| Siguiente sem. | Ganadores migran al motor de escala (Smart+/CBO); los muertos se cortan |

Meta: que **2–5 creativos nuevos** entren a prueba cada semana (ver 18). Sin ese flujo, cuando el ganador actual se fatigue (ver 39) la cuenta se apaga sola. La producción de esos videos se trabaja con `directorcreativo_lushows` (estética, identidad de marca) y los guiones nativos con el enfoque "haz TikToks, no ads" (ver 30).

## Significancia práctica (no esperes el laboratorio perfecto)

Con presupuestos colombianos no vas a tener significancia estadística de manual. Usa **significancia práctica**:

- Deja correr **mínimo 3–7 días** y hasta gastar **~2–3× tu CPA objetivo por variante** antes de declarar ganador (ver 13). Menos que eso es ruido por la varianza alta de TikTok.
- No declares ganador con 1 conversión de diferencia. Busca diferencias **claras** (un creativo con la mitad del CPA del otro), no empates técnicos.
- Si dos variantes empatan, gana la **más simple/escalable** o la que mejor representa tu marca (ver `directorcreativo_lushows`).
- Usa señales tempranas para abortar rápido: un creativo con hold rate pésimo a las 24–48h difícilmente se recupera; córtalo y libera presupuesto sin esperar los 7 días (esto es triaje, no veredicto final).

Regla de cordura: testea pocas variables, dales aire, y mide contra tu MER real (ver 16), no contra el ROAS optimista del panel.

## Errores comunes — blacklist

1. **Testear públicos antes que creativos.** En TikTok el creativo es el targeting; el público importa poco (ver 20). Empieza por el video.
2. **Cambiar varias variables a la vez.** Si mejora, no sabes por qué; no es testing, es azar.
3. **Producir 10 videos completos antes de testear hooks.** Testea hooks baratos primero; el gancho decide el 80%.
4. **Declarar ganador el día 1 o con 1 conversión.** La varianza de TikTok es alta; espera 3–7 días y ~2–3× el CPA (ver 13).
5. **Tocar el A/B test a mitad de camino.** Resetea el aprendizaje y contamina el resultado; déjalo correr.
6. **Buscar significancia estadística perfecta** con presupuesto chico. No la vas a tener; usa significancia práctica y diferencias claras.
7. **Juzgar el test por el ROAS del panel.** Sobre-atribuye; cruza con backend/MER (ver 16).
8. **No tener fábrica de creativos.** Sin 2–5 videos nuevos/semana, ganas un test y mueres cuando ese creativo se fatiga (ver 18, 39).
9. **Confundir test de creativo con test de oferta.** Si cambiaste el precio Y el video, no sabes cuál movió la aguja; una variable a la vez.

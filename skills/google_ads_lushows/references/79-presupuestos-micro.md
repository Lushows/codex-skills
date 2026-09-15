# 79 — Presupuestos micro

Lee este módulo cuando el presupuesto sea pequeño — digamos **menos de ~USD $1.000/mes**, o el caso típico de la pyme colombiana: unos cientos de miles de pesos al mes, a veces menos. La mayoría del contenido de Google Ads asume cuentas con plata. Con presupuesto micro las reglas son distintas y la honestidad es obligatoria: **con poca plata solo hay UNA estrategia que funciona, casi todo lo demás es quemar dinero, y a veces la respuesta correcta es "Google no es tu canal todavía".**

Marco que lo explica todo: Google **captura** demanda existente. Con poca plata no puedes permitirte **generar** demanda (eso es lento, caro y es terreno de Meta/TikTok — ver `facebook_ads_lushows`, `tiktok_ads_lushows`). Tu única jugada rentable es ponerte frente a la gente que **ya está buscando exactamente lo que vendes, justo cuando lo busca.** Eso es captura de alta intención, y es lo único que rinde con micro-presupuesto.

## La única estrategia honesta: alta intención + marca

| SÍ (con poca plata) | NO (con poca plata) |
|---|---|
| **Search de alta intención** — keywords donde la persona ya quiere comprar/contratar | **PMax / AI Max** — necesitan volumen de conversiones y feed que no tienes |
| **Search de marca** — quien busca tu nombre (clics baratísimos, alta conversión) | **Display** — barato por clic pero baja intención; quema plata sin vender |
| Pocas keywords, muy específicas, concordancia controlada | **Demand Gen / YouTube** — generación de demanda, no captura |
| Negativas agresivas para no gastar en basura (ver 22-negativas) | Listas enormes de keywords genéricas y caras |
| Una landing impecable (ver `desingweb-lushows`) | Diversificar en 5 tipos de campaña a la vez |

**Por qué NO PMax/AI Max/Display con poca plata:** reparten tu presupuesto entre muchos canales de baja intención y necesitan **volumen de datos** para optimizar. Con $300.000 COP/mes nunca juntas conversiones suficientes (necesitarías ≥30/mes, ver 13-smart-bidding) para que aprendan — gastan a ciegas y no venden. Concentrar toda la plata en Search de captura + marca le da a cada peso la mayor probabilidad de tocar a alguien listo para comprar.

**Por qué marca importa tanto en micro:** quien busca tu nombre tiene la intención más alta posible y los clics son baratísimos. Es la captura más rentable que existe (cuidado con la incrementalidad a mayor escala — ver 39-marca-generico, 65 — pero con poca plata es defensa básica: si no pujas por tu marca, un competidor te roba al cliente que ya iba hacia ti).

## Cómo operar con micro-presupuesto (paso a paso)

1. **Concentra, no diversifiques.** Una o dos campañas Search, no cinco tipos. La diversificación es lujo de presupuestos grandes (ver 78); con poca plata, dispersar = que ninguna campaña junte datos para optimizar.
2. **Elige la puja con cuidado según las conversiones que tengas:**

| Conversiones/mes | Estrategia de puja recomendada |
|---|---|
| 0 (cuenta nueva) | Maximizar clics con CPC máximo (tope), o CPC manual mejorado |
| 1–15 | Maximizar conversiones SIN tCPA (deja que junte señal) |
| 15–30 | Maximizar conversiones; probar tCPA suave |
| ≥30 | tCPA estable (ya hay data) |

   Con muy pocas conversiones, un tCPA agresivo ahoga la entrega (Google no entra a subastas). Empieza laxo, junta señal, luego aprieta (ver 13-smart-bidding, 74).
3. **Negativas desde el día uno.** Cada peso cuenta; una sola búsqueda basura que se lleve $5.000 COP duele. Revisa términos de búsqueda seguido y corta lo irrelevante (ver 22-negativas). Con poca plata, una negativa bien puesta rinde más que cualquier "optimización".
4. **Concentra por horario/día si el patrón es claro.** Si tus ventas pasan entre semana en horario laboral, no riegues el poco presupuesto a las 3 a.m. del domingo (ver 18-presupuesto).
5. **Ten la landing impecable ANTES de pagar tráfico.** Con poca plata no puedes desperdiciar clics caros en una página que no convierte. La página de destino es tan importante como el anuncio (ver `desingweb-lushows`). Y prepara el cierre por WhatsApp si el lead llega por ahí (ver `ventas_lushows`).
6. **Juzga con paciencia pero realismo.** Con poco volumen, los datos tardan más en ser significativos; no mates al tercer día (ver 71-kill), pero tampoco insistas meses si el canal claramente no da.

## Cuándo Google NO es tu canal (la verdad incómoda)

Honestidad sobre hype: Google Ads **no sirve para todo el mundo**, y menos con poca plata. Considera que NO es tu canal (todavía) si:

- **Nadie busca lo que vendes.** Si tu producto es tan nuevo o tan de impulso que la gente no lo busca en Google, no hay demanda que capturar — necesitas **generar** demanda, y eso es Meta/TikTok (ver `facebook_ads_lushows`, `tiktok_ads_lushows`). Ejemplo: un snack novedoso que nadie sabe que existe → la gente no busca "snack que no conozco". Genera demanda primero.
- **Tu margen no aguanta el CPC.** Si el clic cuesta más de lo que tu producto puede pagar por venta, ninguna optimización lo arregla. Es matemática de viabilidad — valídala antes de gastar (ver 64-ROAS-real, `economist_lushows`).
- **El presupuesto es tan chico que ni Search junta datos.** Con muy poca plata, a veces lo honesto es ahorrar, validar el producto por otros medios, y volver a Google cuando haya con qué.

## Mini-cálculo de viabilidad antes de gastar (hazlo siempre)

1. ¿Cuánto deja cada venta? (precio − costos) = margen unitario.
2. ¿Cuánto puedo pagar por venta? = margen × (fracción que estoy dispuesto a invertir).
3. ¿Cuánto cuesta el clic en mis keywords? (estimación de Google / Keyword Planner).
4. CPA estimado ≈ CPC ÷ tasa de conversión de la landing.
5. **Si CPA estimado > lo que puedo pagar por venta → Google no es viable a ese precio/margen.** Repensar precio, oferta o canal (ver `economist_lushows`).

Ejemplo GastroLatam (Calculadora $10.000 COP): la gente SÍ busca "cómo calcular costos de mi restaurante" o "plantilla costos cocina" — hay intención que capturar. Pero el margen sobre $10.000 es mínimo, así que el CPA viable es muy bajo (quizás $2.000–$4.000 COP). Estrategia: Search de marca + keywords ultra-específicas de alta intención, negativas agresivas, landing que convierta fuerte, y NADA de PMax/Display. Si el CPC real supera el margen, Google no es el canal — toca subir el ticket, agrupar productos o repensar la oferta (ver `economist_lushows`).

## Errores comunes — blacklist

- **Prender PMax / AI Max o Display con poca plata.** Reparten el presupuesto en baja intención y necesitan volumen que no tienes; gastan a ciegas y no venden. Solo Search de captura + marca.
- **Diversificar en cinco tipos de campaña.** Con poca plata, dispersar = que ninguna junte datos para optimizar. Concentra (ver 78 para cuándo SÍ diversificar).
- **No pujar por tu propia marca.** Dejas la captura más barata y rentable sobre la mesa (y abierta a competidores, ver 39-marca-generico).
- **Poner tCPA agresivo sin conversiones suficientes.** Ahoga la entrega; empieza laxo y aprieta cuando haya data (ver 13-smart-bidding).
- **Mandar tráfico caro a una landing floja.** Cada clic cuenta; una página que no convierte desperdicia el poco presupuesto (ver `desingweb-lushows`).
- **Insistir en Google cuando nadie busca tu producto.** Sin demanda que capturar, Google no funciona — genera demanda en Meta/TikTok primero (ver `facebook_ads_lushows`, `tiktok_ads_lushows`).
- **Ignorar las negativas.** Con poca plata, una búsqueda basura que se lleve unos miles de pesos es un golpe real (ver 22-negativas).
- **Gastar sin validar que el margen aguanta el CPC.** Si el clic cuesta más de lo que el producto deja, es pérdida matemática garantizada; haz el mini-cálculo de viabilidad primero (ver 64-ROAS-real, `economist_lushows`).
- **Regar el poco presupuesto en 24/7 sin mirar horarios.** Concentra donde están las ventas (ver 18-presupuesto).

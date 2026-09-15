# 97 — Omnicanal

Lee este módulo cuando ya pautes en más de un lado (o quieras hacerlo) y no sepas cuánto darle a cada canal, cuando Google y Meta "se peleen el crédito" de la misma venta, o cuando un cliente pregunte "¿pauto en Google o en Facebook?" y la respuesta honesta sea "en los dos, pero para cosas distintas". Cada plataforma hace un trabajo diferente en el viaje del cliente. Mezclarlas sin entender quién hace qué es como tener tres vendedores peleándose por el mismo cliente y cobrando todos la comisión. En 2026, con cada plataforma metiendo IA que se auto-atribuye conversiones (PMax, Advantage+, Smart+), gobernar por la métrica equivocada es más fácil y más caro que nunca.

## El reparto de roles (la idea central)

| Canal | Su trabajo | Skill |
|---|---|---|
| **Meta** (Facebook/Instagram) | **GENERA demanda**: crea deseo en gente que no te buscaba; interrumpe con creativo | `facebook_ads_lushows` |
| **Google** | **CAPTURA demanda**: atrapa a quien YA busca con intención; está abajo del funnel | esta skill |
| **TikTok** | **DESCUBRIMIENTO**: gente descubre productos por entretenimiento; muy arriba del funnel | `tiktok_ads_lushows` |

La regla que lo explica todo: **nadie busca en Google algo que no sabe que existe.** Si vendes algo nuevo, Google no tiene a quién capturar — primero Meta/TikTok crean el deseo y la búsqueda, y *después* Google atrapa a quien ya te busca por marca o categoría (ver 03, 39). Por eso no es "Google O Meta"; es Meta/TikTok arriba generando y descubriendo, Google abajo capturando. Excepción: si vendes algo que la gente **ya busca** (servicio local, categoría conocida), Google va primero porque la demanda ya existe.

## El mix por etapa del funnel

| Etapa | Qué necesitas | Canal principal |
|---|---|---|
| **Descubrimiento** (no te conocen) | Que existan y te conozcan | TikTok (ver `tiktok_ads_lushows`), Meta creativo, YouTube/Demand Gen (ver 41, 42) |
| **Consideración** (te conocen, dudan) | Recordarles, resolver objeciones | Meta retargeting, Demand Gen, Display (ver 41, 43) |
| **Intención** (buscan activamente) | Estar cuando escriben "comprar/precio/cerca de mí" | **Google Search** (tu fuerte, ver 11, 20) |
| **Marca** (te buscan por nombre) | Defender tu nombre, no perder al que ya quiere | **Google Search marca** (ver 39) |

Para un negocio LatAm con presupuesto chico que vende algo que **la gente ya busca**: empieza por Google Search (captura barata, intención alta), y cuando funcione, suma Meta para generar más demanda y llenar el funnel. Si vendes algo que **nadie busca todavía**, al revés: empieza generando en Meta/TikTok, y prende Google Search de marca para capturar la demanda que esos crearon. El cuello de botella manda (ver abajo).

## MER global: la métrica que evita que te engañen

Aquí está la trampa del multicanal: **cada plataforma se atribuye la misma venta.** El usuario ve un anuncio en TikTok, otro en Instagram, busca tu marca en Google y compra. Las TRES plataformas reportan "yo generé esa venta". Si sumas los ROAS de cada una, te da una cifra fantástica... y falsa. La IA de cada una (PMax, Advantage+, Smart+) infla aún más esa auto-atribución.

La solución es mirar el **MER** (Marketing Efficiency Ratio, eficiencia de marketing global):

```
MER = Ingresos TOTALES del negocio ÷ Gasto TOTAL en TODA la pauta
```

| Métrica | Qué mide | Problema |
|---|---|---|
| ROAS por plataforma | Lo que cada canal SE atribuye | Se solapan; suman de más |
| **MER global** | Ventas reales del negocio / toda la inversión | La verdad de si la pauta total es rentable |

Ejemplo: gastas $1.000.000 en Google + $1.500.000 en Meta = $2.500.000 total. El negocio vendió $10.000.000 ese mes. MER = 4. Eso es real. No importa que Google reporte ROAS 6 y Meta ROAS 5 (sumarían ventas imposibles); el MER te dice que cada peso de pauta trajo $4 de venta total. **Decide con MER, ajusta canales con su ROAS relativo** (cuál sube o baja cuando muevo presupuesto). Para saber qué MER necesitas para que el negocio gane plata, rutea a `economist_lushows`.

## No canibalizar marca (el error clásico)

El solapamiento más caro: **pagar por la intención de marca que ya tenías gratis.** Si Meta generó que alguien te busque por nombre, y luego Google (Search marca + PMax sin brand exclusions) cobra esa conversión barata, parece que Google "vendió" — pero esa venta ya estaba ganada. Blindaje:

- **Brand exclusions en PMax** (ver 39, 90): que PMax NO toque tu marca.
- **Search marca como campaña aparte**, medida aparte: sabes cuánto cuesta defender tu nombre, no la mezclas con la captura genérica.
- **Mide incrementalidad** (ver 65): ¿la venta TOTAL subió al prender un canal, o solo se movió el crédito? Apaga marca/PMax una semana y mira si la venta total baja o no — si no baja, no era incremental.

## Cómo orquestarlo en la práctica

1. **Define el rol de cada canal** antes de gastar (genera/captura/descubre). No pongas a Google a "dar a conocer la marca" — no es su trabajo (ver 03).
2. **Empieza por donde está tu cuello de botella**: ¿falta gente que te conozca (genera → Meta/TikTok) o falta capturar a quien ya busca (Google)? Diagnostica antes de repartir.
3. **Cierra la medición primero** (ver 96, 05, 06): GA4 + OCI + MER, o el multicanal es niebla.
4. **Gobierna por MER**, ajusta el reparto entre canales mirando su aporte incremental (ver 65).
5. **El lead siempre vuelve al mismo lugar** (WhatsApp/CRM) y la venta se devuelve a quien la originó (OCI con el GCLID correcto, ver 53, 96). El cierre lo hace `ventas_lushows`.
6. **Marca consistente entre canales**: mismo mensaje y look (rutea a `directorcreativo_lushows`); demanda de marca generada en Meta = captura barata en Google.

## Reparto inicial sugerido (presupuesto chico LatAm)

| Escenario | Reparto de arranque |
|---|---|
| Producto que la gente YA busca | 70% Google (Search + marca) / 30% Meta para generar más |
| Producto nuevo que nadie busca | 60% Meta/TikTok (genera/descubre) / 40% Google marca + Demand Gen |
| E-commerce con catálogo | Meta para demanda + Google PMax retail + Search marca; gobierna por MER |

No es fórmula; es punto de partida. Mueve presupuesto al canal cuyo aporte incremental sube el MER total.

## Cómo prueba incrementalidad un negocio chico (sin herramientas caras)

No necesitas un estudio de geo-experimento de agencia grande. El test del pobre, honesto y suficiente:

1. **Apaga un canal una semana** (ej. Search marca o PMax) y mira si la venta TOTAL del negocio baja. Si no baja → ese canal no era incremental, solo se atribuía crédito (ver 65).
2. **Mira el MER, no el ROAS de la plataforma.** Si prendes Meta y el MER global sube, Meta aporta; si el MER se queda igual pero Meta "reporta" ROAS 5, está robando crédito de otro canal.
3. **Pregunta a los que compran** "¿dónde nos viste primero?" — barato, imperfecto, pero te da la forma del funnel real.

La trampa que esto destapa: PMax y Search de marca casi siempre "reportan" el mejor ROAS porque capturan a quien YA iba a comprar. Apágalos un rato y verás cuánto era de verdad incremental. El élite hace esto antes de creerle al panel (ver 99).

## Errores comunes — blacklist

- **Sumar los ROAS de cada plataforma.** Se atribuyen la misma venta; el total es falso. Gobierna por **MER global** (ver arriba).
- **Poner a Google a generar demanda.** No crea deseo de la nada; eso es Meta/TikTok. Google captura intención que ya existe (ver 03).
- **PMax/Search marca robándose conversiones de marca ya ganadas.** Brand exclusions + campaña de marca aparte, mide incrementalidad (ver 39, 65, 90).
- **Elegir "Google O Meta" como si fueran lo mismo.** Hacen trabajos distintos; el funnel los necesita a los dos en su etapa (ver 03).
- **Lanzar multicanal sin medición unificada.** Sin GA4/OCI/MER no sabes qué funciona; cierras la medición primero (ver 96).
- **Empezar por el canal de moda en vez del cuello de botella real.** Si nadie te conoce, Google no tiene a quién capturar; genera primero.
- **No devolver la venta al canal que la originó.** Cada algoritmo optimiza a ciegas; usa OCI con el GCLID correcto (ver 53, 96).
- **Creerle al ROAS inflado por la IA de cada plataforma.** PMax/Advantage+/Smart+ se auto-atribuyen de más; valida con incrementalidad y MER (ver 65).

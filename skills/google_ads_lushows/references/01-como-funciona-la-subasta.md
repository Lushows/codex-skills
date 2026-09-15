# 01 — Cómo funciona la subasta

Cada vez que alguien busca algo en Google, se dispara una **subasta en tiempo real** (milisegundos) para decidir qué anuncios aparecen y en qué orden. Entender esto es lo que separa a quien "le sube la puja a ver si sale" del que paga **menos** por **mejor** posición. Lee este módulo cuando no entiendas por qué tu competidor aparece arriba pagando menos, cuando quieras bajar tu CPC sin perder posición, o antes de tocar pujas.

## Ad Rank: por qué NO gana el que más paga

La posición de tu anuncio la decide el **Ad Rank** (puntaje de subasta), no la puja sola. Fórmula práctica:

> **Ad Rank ≈ Puja × Quality Score × impacto esperado de los assets/formatos (+ umbrales mínimos y contexto de la búsqueda)**

Esto significa que un anuncio **más relevante y barato** puede ganarle a uno que paga el doble pero es malo. Google premia la relevancia porque un anuncio bueno = usuario contento = Google gana a largo plazo (más gente confía en hacer clic).

| Anunciante | Puja máx | Quality Score (1–10) | Ad Rank (relativo) | Resultado |
|---|---|---|---|---|
| A | $2.000 COP | 4 | 8.000 | pierde / abajo |
| B | $1.200 COP | 9 | 10.800 | **gana / arriba** |
| C | $1.500 COP | 7 | 10.500 | 2º lugar |

B paga menos y aparece más arriba. Esa es la palanca real: subir **Quality Score** (ver 36), no subir la puja a lo bruto. Subir la puja tiene rendimientos decrecientes; subir QS baja el CPC Y mejora la posición a la vez.

## El CPC real es MENOR que tu puja máxima

No pagas tu puja máxima. Pagas **lo mínimo necesario para superar el Ad Rank del de abajo**. Fórmula simplificada del CPC real:

> **CPC real ≈ (Ad Rank del competidor de abajo ÷ tu Quality Score) + $1 peso**

Consecuencia directa: si **subes tu Quality Score**, tu CPC real **baja** aunque mantengas la misma puja. Dos anunciantes con la misma puja pueden pagar CPCs muy distintos según su calidad. Ejemplo numérico en COP:

| Tu QS | Ad Rank del de abajo | CPC real aprox |
|---|---|---|
| 4 | 8.000 | $2.001 COP |
| 7 | 8.000 | $1.143 COP |
| 10 | 8.000 | $801 COP |

Mismo competidor abajo, misma intención de pujar: el de QS 10 paga **60% menos por clic** que el de QS 4. Por eso un especialista invierte en relevancia y landing antes que en subir budget.

## El Quality Score: los 3 componentes y cómo moverlos

| Componente del Quality Score | Qué mide | Cómo mejorarlo | Ver |
|---|---|---|---|
| **CTR esperado** | si la gente hará clic | mejor copy/oferta, número en el titular, la keyword en el H1 | 30, 38 |
| **Relevancia del anuncio** | si el anuncio coincide con la búsqueda | keyword → anuncio congruentes, grupos ajustados | 37 |
| **Experiencia en landing** | si la página cumple lo prometido y carga rápido | landing rápida, relevante, móvil-first | 33 → `desingweb-lushows` |

El CTR esperado pesa más que los otros dos. Y ojo: el Quality Score que ves en la interfaz (1–10, por keyword) es un **diagnóstico histórico**; la subasta usa una versión en tiempo real ajustada a la búsqueda exacta, dispositivo y contexto. No te obsesiones con el número visible; úsalo para detectar keywords flojas.

## Qué decide la subasta (y qué NO controlas)

| Tú controlas | La subasta/Google decide |
|---|---|
| Puja / target de Smart Bidding | CPC final exacto de cada clic |
| Quality Score (vía calidad real) | quién aparece en cada búsqueda |
| Keywords, concordancia, negativas | si pasas los **umbrales mínimos** de Ad Rank |
| Assets (sitelinks, callouts, etc.) | qué formatos/assets se muestran |
| Landing y oferta | el contexto (hora, dispositivo, ubicación, intención) |

Hoy con **Smart Bidding** (ver 13) tú no pones un CPC fijo: pones un objetivo (tCPA/tROAS) y Google calcula la puja óptima por subasta usando señales (dispositivo, hora, intención, historial, audiencia). Pero la mecánica Ad Rank sigue corriendo por debajo: **relevancia barata > puja cara.** El Smart Bidding no te exime de tener buen QS — al contrario, un QS alto le da más margen al algoritmo para pujar fuerte donde conviene sin disparar el CPA.

## AI Overviews y la subasta en 2026

Con **AI Overviews / AI Mode** (la respuesta IA arriba de los resultados), hay ahora inventario de anuncios **dentro** de esas respuestas generativas (ver 92). La subasta sigue siendo la misma mecánica de Ad Rank, pero el contexto cambia: en consultas informacionales el clic baja, así que pelea las consultas **comerciales** donde la intención de compra mantiene el clic. La relevancia importa más, no menos, porque Google decide si tu anuncio merece aparecer junto a una respuesta que ya "resolvió" parte de la duda.

## Auction Insights: tu radar competitivo

Para ver tu posición real frente a competidores usa **Auction Insights / Estadísticas de la subasta** (ver 94). Métricas clave:

| Métrica de Auction Insights | Qué te dice |
|---|---|
| **Cuota de impresiones (IS)** | % de veces que apareciste sobre las que podías aparecer |
| **Posición media / cuota superior** | qué tan arriba sales vs. ellos |
| **Tasa de solapamiento** | con qué frecuencia tú y un competidor aparecen en la misma subasta |
| **Cuota de superación (outranking)** | cuántas veces le ganas la posición |

Si tu IS es baja, el diagnóstico es: o te falta presupuesto (perdido por budget) o te falta Ad Rank (perdido por ranking → trabaja QS/puja). Esa distinción la da el reporte de "cuota de impresiones perdida" (ver 60, 94).

## Errores comunes — blacklist

- **Creer que subir la puja te garantiza salir arriba.** Si tu Quality Score es bajo, pagas más y sigues abajo. Fix: ataca Quality Score (relevancia + landing), no solo la puja (ver 36).
- **Ignorar el Quality Score "porque con Smart Bidding ya no importa".** Sí importa: alimenta el Ad Rank y por tanto tu CPC real. Fix: mantén keyword→anuncio→landing congruentes (ver 37).
- **Una landing genérica que no menciona lo que buscó el usuario.** Mata la experiencia de la landing → baja QS → sube CPC. Fix: landing alineada al término (ver 33 → `desingweb-lushows`).
- **Meter 50 keywords distintas en un solo grupo de anuncios.** El anuncio no puede ser relevante a todas → CTR esperado bajo. Fix: grupos temáticos ajustados (ver 10, 37).
- **Pausar todos los assets (sitelinks, callouts) para "simplificar".** Los assets suman al Ad Rank y a la posición, y son gratis. Fix: usa el set completo de assets (ver 32).
- **Mirar solo el CPC máximo y no el CPC real ni el costo por conversión.** El CPC barato no sirve si no convierte. Fix: optimiza por CPA/ROAS, no por CPC (ver 60, 64).
- **Obsesionarse con el QS visible en la interfaz.** Es un diagnóstico histórico, no el número exacto de la subasta. Fix: úsalo para hallar keywords flojas, no como meta vanidosa (ver 36).
- **No revisar Auction Insights y no saber por qué perdiste posición.** Vuelas a ciegas. Fix: diagnostica IS perdida por budget vs. ranking (ver 94).

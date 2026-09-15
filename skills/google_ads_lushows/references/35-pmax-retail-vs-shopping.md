# 35 — PMax retail vs Shopping

Lee este módulo cuando vendas con catálogo y no sepas si correr Shopping estándar o Performance Max, tu PMax esté "vendiendo" pero sospeches que se está llevando ventas que igual ibas a tener, o un experto te diga "métele PMax" sin explicarte el costo escondido.

Cuando tienes un feed sano (ver 34), tienes dos caminos para venderlo. Los dos usan tu catálogo, pero son filosofías opuestas: **Shopping estándar = control; PMax retail = alcance.** No es que uno sea mejor; es que sirven para cosas distintas y, mal combinados, se pisan. El error caro número uno en e-commerce colombiano es prender PMax sin entender que puede estar cobrándote por ventas de tu propia marca que ya tenías ganadas. Este módulo te ahorra ese dinero.

## Las dos opciones, frente a frente

| | **Shopping estándar** | **PMax retail (con feed)** |
|---|---|---|
| Qué es | campañas de Shopping que tú controlas | Performance Max: una sola campaña que usa tu feed y se mete en Search, Shopping, Display, YouTube, Gmail, Maps, Discover |
| Control | alto: ves búsquedas, pujas por producto, qué muestras | bajo: Google decide casi todo, caja negra |
| Alcance | solo red de Shopping/Search | TODO el ecosistema Google |
| Visibilidad | ves términos de búsqueda (ver 68) | reportes limitados (mejoraron en 2026, pero siguen flacos) |
| Riesgo | poco | canibaliza marca si no la excluyes |
| Cuándo usarlo | quieres control, datos, proteger marca | tienes volumen, quieres escala y delegar a la IA |

PMax (Performance Max) es la campaña "todo en uno" de Google: le das el feed, las imágenes, los textos y un objetivo (normalmente ROAS, ver 13, 15), y la IA reparte tu presupuesto por todos los canales buscando conversiones. Es potente para escalar, pero es una caja negra: no decides dónde ni a quién, y los reportes son flacos. En 2026 Google sumó **AI Max** (capa de IA generativa que crea variantes de creativos y amplía términos), lo cual sube alcance pero baja aún más tu control — más razón para vigilar la canibalización (ver 90).

## El problema de la canibalización de marca

Aquí está el truco que cuesta plata. Cuando alguien busca **tu marca** ("calculadora gastrolatam", "tienda X"), ese cliente YA te iba a comprar — es demanda que ya tenías. PMax, hambrienta de conversiones fáciles, se lanza a capturar esas búsquedas de marca porque convierten carísimo bien. Resultado: tu reporte de PMax muestra un ROAS hermoso... pero buena parte son ventas que ibas a tener GRATIS (o casi) por tráfico orgánico/directo. Estás pagando por demanda ya ganada y creyendo que PMax la "generó".

Ejemplo numérico (COP):

| Escenario | Ventas totales/mes | Gasto Google | "ROAS" que reporta PMax |
|---|---|---|---|
| Sin PMax (solo orgánico + Search marca) | $30.000.000 | $2.000.000 | — |
| Con PMax SIN excluir marca | $32.000.000 | $5.000.000 | reporta 6x (¡falso!) |
| Con PMax CON marca excluida | $36.000.000 | $5.000.000 | refleja crecimiento real |

En el caso del medio, PMax dice "6x" pero las ventas totales solo subieron $2M con $3M más de gasto: te canibalizó. En el de abajo, con marca excluida, PMax fue por demanda NUEVA y el total creció $6M de verdad. La lección: **mira ventas TOTALES del negocio, no el reporte de la campaña.**

Cómo lo detectas rápido: si prendes PMax y tus ventas totales NO suben tanto como dice el reporte de PMax, te está canibalizando. La venta se movió de "gratis" a "pagada", no creció.

### La solución: excluir tu marca de PMax

Pide a Google (o a tu agencia, o actívalo tú en la campaña) la **exclusión de marca** ("brand exclusions") en la campaña PMax: una lista de términos de tu marca que PMax NO debe capturar. Así PMax va por demanda NUEVA (gente que no te conoce) y dejas tu propia marca para una campaña de Search de marca, que es baratísima y la controlas tú (ver 39). Separar marca de genérico es la base de toda cuenta sana. En 2026 las brand exclusions de PMax son autoservicio en la interfaz — no hay excusa para no activarlas.

## Cómo decidir (la regla práctica)

| Tu situación | Empieza con |
|---|---|
| Catálogo nuevo, poco volumen, quieres aprender qué busca la gente | **Shopping estándar** — control y datos primero |
| Ya tienes ventas (>30 conv./mes), quieres escalar y delegar el reparto | **PMax retail** — pero con exclusión de marca SÍ o SÍ |
| Quieres lo mejor de ambos | Shopping estándar para control + PMax para alcance, con marca excluida de PMax |

Orden recomendado para alguien que empieza en Colombia: **primero Shopping estándar** unas semanas para entender términos, márgenes y qué productos jalan (ver 68); **después** PMax para escalar, ya con la marca protegida. No al revés. Prender PMax de primero te deja ciego y canibalizado. PMax también necesita un mínimo de conversiones para que su Smart Bidding aprenda (apunta a ~30 conversiones/mes antes de esperar estabilidad, ver 13).

### Señales de audiencia: ayuda a PMax a arrancar

PMax no usa keywords, pero sí acepta **señales de audiencia** (audience signals): le dices "mi cliente se parece a esta lista de compradores / busca estos términos" y eso le da un punto de partida mientras aprende. No es segmentación dura (PMax puede salirse), pero acelera el arranque. Usa tus datos propios (Customer Match, ver 25) como señal — es lo más potente que tienes.

## Cómo se relaciona con el resto

Para la versión a fondo de PMax (todos los tipos de campaña, AI Max, señales de audiencia) ver 12, 90. Para la decisión de bidding dentro de PMax (tROAS) ver 13, 15. Para defender tu marca con Search ver 39. Para el feed que alimenta a ambos, ver 34. Para construir la landing que reciba ese tráfico, `desingweb-lushows`.

## Errores comunes — blacklist

- **Prender PMax de primero sin datos**: empiezas ciego, sin saber qué busca tu cliente ni qué producto jala; arranca con Shopping estándar (ver 68).
- **No excluir la marca en PMax**: pagas por ventas de marca que ya tenías y crees que PMax las "generó"; activa brand exclusions siempre (es autoservicio en 2026).
- **Creer el ROAS de PMax sin mirar ventas TOTALES**: si las ventas globales no suben como dice el reporte, hay canibalización; compara el total del negocio, no el reporte de la campaña.
- **Pensar que PMax reemplaza Shopping**: son control vs alcance; muchos corren ambos a propósito, con marca dividida.
- **Tratar PMax como "configúralo y olvídalo"**: es caja negra pero igual necesita exclusiones, buen feed, señales de audiencia y vigilancia de canibalización.
- **No darle señales de audiencia a PMax**: arranca más lento y explora peor; aliméntala con tus datos propios (ver 25).
- **Correr cualquiera de los dos con feed sucio**: ningún formato salva un catálogo malo; feed sano primero (ver 34).
- **No tener una campaña de Search de marca aparte**: si excluyes marca de PMax pero no la cubres con Search de marca, dejas la puerta abierta al competidor (ver 39).

# 12 — Smart+ campaigns

Lee este módulo cuando veas la opción "Smart+" al crear una campaña y no sepas si confiar en la automatización, cuando alguien te diga "deja que TikTok haga todo solo", o cuando vengas de Meta y quieras el equivalente de Advantage+ Shopping. Smart+ es la apuesta de TikTok a que su algoritmo decide mejor que tú — y en 2026, con la suite madura, muchas veces tiene razón. Pero solo si le das lo correcto y entiendes qué le estás cediendo. Smart+ no es magia: es una máquina que amplifica buena señal y buen creativo, y amplifica igual de bien la basura.

## Qué es Smart+ (y el equivalente que ya conoces)

**Smart+** (lanzado 2024, maduro y por defecto en 2026) es la campaña automatizada de TikTok: tú das **creativo + presupuesto + evento** y TikTok automatiza **audiencia, ubicaciones (placements), pujas y optimización de entrega**. Es el primo de **Advantage+ Shopping de Meta** y de **Performance Max de Google** (ver `facebook_ads_lushows` y `google_ads_lushows` — la misma filosofía: tú das insumos, la máquina arma la campaña). La diferencia con PMax: Smart+ es más transparente (ves los creativos que jalan) y vive 100% dentro del ecosistema TikTok, sin canibalizar búsqueda.

Viene en sabores según tu objetivo (ver 90 para la suite completa):

| Tipo de Smart+ | Para qué | Evento típico |
|---|---|---|
| **Smart+ Web Campaign** | Ventas/conversiones en tu sitio web (vía Pixel) | Complete payment (ver 14) |
| **Smart+ Catalog** | Anuncios dinámicos de catálogo / retargeting de productos | Purchase sobre catálogo |
| **Smart+ App** | Instalaciones y eventos in-app | Install / in-app purchase |
| **Smart+ Lead** | Generación de leads (formularios nativos) | Form submit (ver 54) |
| **GMV Max** (TikTok Shop) | Maximizar ventas dentro de Shop | GMV (ver 52) |

## Qué controlas y qué cedes

La pregunta clave antes de prender Smart+: ¿estoy dispuesto a soltar el volante?

| Controlas TÚ | Cede a TikTok |
|---|---|
| Los **creativos** (lo más importante — ver 17, 68) | A quién le aparece (audiencia) |
| El **presupuesto** | En qué placement se muestra |
| El **evento de optimización** (ver 14) | La estrategia de puja (dentro de tu meta) |
| **Exclusiones** (audiencias a evitar, listas de clientes) | El reparto del gasto |
| La **meta de CPA/ROAS** (si usas cost cap o ROAS goal, ver 15) | El detalle del targeting fino |

Lo que NO puedes hacer: micro-segmentar públicos, separar placements a mano, ni "ayudar" al algoritmo con 15 ad groups. Smart+ vive de la consolidación (ver 10). Si tu instinto es controlar todo, Smart+ te va a frustrar — y probablemente vas a rendir peor que dejándolo solo. La automatización castiga al que la manosea.

## Cuándo SÍ usar Smart+ (la checklist de las 4 condiciones)

Smart+ brilla cuando se cumplen estas condiciones. Si te falta una, arregla eso primero:

1. **Tienes el Pixel/Events API bien instalado** y mandando el evento de compra limpio (ver 57). Sin señal de calidad, la automatización optimiza a ciegas y trae basura a escala.
2. **Tienes munición creativa** — mínimo 4–6 videos buenos y nativos, idealmente 8–10+. Smart+ es una máquina que devora creativos; si le das 1 video se ahoga (ver 17). En 2026 la recomendación interna de TikTok ronda los 5+ creativos activos por Smart+.
3. **Tienes volumen de conversiones** o presupuesto para alcanzarlo (~50 conv/sem, ver 13). Con 3 ventas a la semana, la automatización no tiene de qué aprender. Regla de bolsillo: presupuesto diario ≈ 20× tu CPA real para darle aire (CPA $30.000 → ~$600.000/día ideal; menos funciona pero aprende más lento).
4. **Quieres escalar lo que ya valida** una campaña manual. Smart+ es excelente para crecer, riesgoso para descubrir desde cero.

**Cuándo NO:** presupuesto muy chico (<$50.000 COP/día), un solo creativo, Pixel a medio instalar, o producto sin validación previa. En esos casos arranca con una campaña Sales manual y broad (ver 20), valida creativo y oferta, y *después* mueves a Smart+. Smart+ amplifica; primero ten algo que valga la pena amplificar.

## Cómo arrancarlo bien (receta paso a paso)

| Paso | Acción |
|---|---|
| 1 | Crea **un Smart+ por evento/economía**, no diez. Consolida (ver 10) |
| 2 | Carga **8–10 creativos variados** desde el inicio (hooks, ángulos, formatos distintos); deja que TikTok elija ganadores |
| 3 | Evento = el más cercano a la venta que tu volumen permita (ver 14) |
| 4 | Puja **lowest cost** (sin cap) para no estrangular el aprendizaje; pon cost cap o ROAS goal solo cuando tengas CPA real medido (ver 15) |
| 5 | Carga exclusiones (compradores recientes, empleados) y sube tu lista de clientes para lookalike implícito |
| 6 | **No lo toques 3–7 días.** Smart+ con su varianza alta necesita aire; tocarlo reinicia el aprendizaje (ver 13) |
| 7 | A los 7 días: corta los 2–3 peores creativos, mete 2–5 nuevos, NO toques presupuesto si va bien |

## Cómo convivir Smart+ con tu campaña manual

En 2026 lo habitual no es "todo Smart+ o todo manual", sino **ambos**: una campaña **manual de testing** que descubre creativos ganadores baratos (ver 17), y un **Smart+ Web** que es el motor de escala donde migras los ganadores. El manual es tu laboratorio; Smart+ es tu fábrica. Cuida que no se canibalicen feo: si ambos persiguen el mismo broad con los mismos creativos, suben tu propio CPM. Diferéncialos por función (testing vs escala), no por público.

## Mide contra tu backend, no contra el panel de Smart+

Smart+ **sobre-atribuye más que el promedio** porque se cuelga ventas view-through generosamente. Mide contra tu **MER** real (ver 16, 64), no contra el ROAS que te muestra el panel. Si el panel grita ROAS 5 pero tu facturación total no se movió al subir el gasto de Smart+, la automatización se está robando crédito (ver 16).

## Errores comunes — blacklist

1. **Prender Smart+ con un solo creativo.** Es una máquina de creativos sin combustible; necesita 5+ videos, idealmente 8–10.
2. **Usarlo con el Pixel a medias.** Optimiza sobre señal sucia y trae tráfico basura (ver 57).
3. **Esperar que "arregle" un producto u oferta que no vende.** Smart+ amplifica lo que funciona; no resucita lo que no (la viabilidad la juzga `economist_lushows`).
4. **Pelear con la automatización** creando 10 Smart+ o metiendo exclusiones por todo. Consolida y suelta el volante.
5. **Ponerle cost cap agresivo desde el día 1.** Estrangulas la entrega y nunca sale de aprendizaje; arranca en lowest cost (ver 15).
6. **Tocarlo cada día** porque "no veo ventas en 12 horas". La varianza de TikTok es alta; dale 3–7 días (ver 13).
7. **Creerte el ROAS del panel de Smart+ al pie de la letra.** Sobre-atribuye; cruza con tu MER real (ver 16, 64).
8. **No alimentarlo con creativos nuevos.** Smart+ fatiga creativos rápido (ver 39); mete 2–5 nuevos por semana o la máquina se queda sin combustible.
9. **Correr Smart+ y manual sobre el mismo broad/creativos** sin diferenciar función: te subastas contra ti mismo y subes tu CPM.

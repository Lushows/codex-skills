# 64 — Data storytelling & dataviz narrativa

Complementa 13 (dashboards/charts): allí construyes el panel (exploratory); **aquí cuentas una historia con datos** (explanatory). **Léelo para infografías, reportes, piezas de datos, presentar números que persuadan honestamente.** Pareja de 13 (dataviz), 26 (scrollytelling), 17 (copy). Regla de oro: **un número solo no significa nada — el contexto y la comparación SON el insight.**

## 1. Explanatory vs exploratory (la decisión que lo gobierna todo)

La distinción raíz de **Cole Nussbaumer Knaflic**: **exploratory** = buscar las perlas en las ostras (tú hurgando los datos por lo interesante); **explanatory** = comunicar *esa perla concreta* a una audiencia. Un dashboard es exploratory ("encuéntralo tú"); una pieza narrativa es explanatory ("yo ya encontré el punto y te lo hago ver"). **El error #1:** entregar exploratory cuando pedían explanatory — volcar las 50 cosas que descubriste en vez de las 2 que importan.
**Principios operativos:** **audiencia-first** (¿a quién hablas, qué necesitas que *haga*, qué dato lo sustenta?) · **elige UN mensaje** (una pieza = una idea; si tienes tres, son tres piezas) · **el "so what"** (la comparación —vs mes pasado, vs meta, vs competidor, vs lo esperado— es el insight) · **arco narrativo** (*setup* contexto → *tension* la anomalía/brecha → *resolution* insight + acción; sin tensión no hay historia, solo un gráfico) · **el gráfico no es la historia** (el título y la anotación cargan la narrativa; el gráfico es la evidencia). Define el "Big Idea" en *una* frase declarativa con punto de vista.

## 2. Elegir y diseñar el gráfico para el mensaje

El mensaje dicta el chart. Mapeo canónico: **comparación → barras** (horizontales si etiquetas largas) · **tendencia → línea** · **distribución → histograma/boxplot/beeswarm** · **parte-de-un-todo → barra apilada** (pie SOLO con 2-3 categorías; con más, barras siempre — el ojo compara longitudes, no ángulos) · **relación → scatter**.
**El eje honesto:** las barras DEBEN empezar en cero (su longitud codifica magnitud; truncar = mentir). Las líneas *pueden* no empezar en cero (codifican cambio) pero declara la escala. El "lie factor" de Tufte: el efecto visual debe igualar el efecto en los datos.
**Atributos pre-atentivos** (lo que el cerebro procesa en <250ms): color, tamaño, posición, orientación → tu herramienta para **dirigir el ojo**. Regla: casi todo en gris, *un solo* elemento en color = ahí va la atención.
**Decluttering (Tufte, data-ink ratio):** maximiza la tinta que representa datos, mata el *chartjunk* (3D, sombras, fondos, gridlines pesados, leyendas redundantes). Matiz 2026 (Frank Elavsky): no es minimalismo dogmático — anotaciones, etiquetas directas y guías mejoran comprensión y a11y; "menos tinta" nunca debe sacrificar legibilidad.
**La anotación es el arma secreta** (el gráfico que se explica solo): título declarativo que enuncia el insight (no "Ventas por mes" sino "Las ventas caen cada enero desde 2021"), etiquetado directo sobre la línea en vez de leyenda, flecha + nota en el pico, sombrear la zona relevante. **Un gráfico sin anotación delega en el lector un trabajo que era tuyo.**

## 3. Formatos narrativos e infografía interactiva

Géneros (Segel & Heer + práctica editorial): **annotated chart** (un gráfico estático con texto/flechas — el 80% de los casos, empieza aquí) · **scrollytelling NYT/Pudding** (gráfico *sticky* mientras el texto avanza; cada "step" revela/transforma) · **interactive explorer** (el lector filtra su caso, "encuentra tu barrio") · **dashboard-as-story** · **explainer** paso a paso.
**Estructura Martini Glass** (la más útil): empieza *author-driven* (el "tallo": intro, el punto que quieres dar), luego se abre al *bowl* — exploración *reader-driven* (filtros, hover). Das el punto primero, *después* dejas explorar. Error: abrir a exploración sin dar contexto (el lector se pierde).
**Revelado progresivo:** no muestres el dataset completo de golpe. Step 1: ejes + un punto. Step 2: la tendencia. Step 3: el outlier resaltado. Step 4: la explicación. Cada scroll = una frase visual.

## 4. Herramientas e implementación

**D3.js** — el power tool (control total, transiciones a medida, lo no-estándar; caro en tiempo, úsalo para diseño bespoke) · **Observable Plot** — capa alta sobre D3, el sweet spot para gráficos editoriales rápidos y correctos · **Vega-Lite** — declarativo (JSON), reproducible · **ECharts/Chart.js/Recharts** — para producto/dashboards React. **Scrollytelling stack:** **Scrollama** (usa IntersectionObserver, no eventos de scroll → suave) + D3/Plot para el gráfico sticky (la receta NYT/Pudding).
**SVG vs Canvas:** SVG por defecto (cada elemento es un nodo del DOM → accesible, estilable, animable; ideal <1.000-5.000 elementos); Canvas con decenas de miles de puntos (rinde mejor, pierdes DOM/a11y).
**Transiciones — object constancy:** cuando los datos cambian, los elementos se *transforman* (la barra se estira), no desaparecen y reaparecen. Mantén identidad con la *key function* de D3 (`.data(data, d => d.id)`). Anima posición/tamaño, no opacidad por defecto.
**Responsive — repiensa, no encojas** ("rethink, not reshrink"): en móvil rota barras a horizontal, reduce ticks, mueve leyenda a etiquetas directas, convierte hover (no existe en touch) en tap o estado siempre-visible. A veces el móvil necesita *otro* gráfico.
**A11y (ya no opcional):** tabla de datos alternativa (`<table>` oculta o `<details>`), `role="img"` + `aria-label` con el insight, paletas color-blind-safe, **nunca codificar solo por color** (añade forma/patrón/etiqueta), y emergente: *sonification*.

## 5. El look "caro/creíble" y la honestidad

**Estética editorial (NYT, The Pudding, The Economist, FT):** tipografía con jerarquía clara (sans para datos, serif para narrativa), **restricción cromática** (gris + 1-2 acentos), generoso whitespace, kicker/título/dek estructurados, fuente y metodología siempre al pie. La sofisticación viene de *quitar*.
**Color para datos (ColorBrewer es el estándar):** **sequential** (claro→oscuro) para magnitud · **diverging** (dos hue, centro neutro) para datos con punto medio crítico (déficit/superávit) · **categorical** para nominales (limítate a ~6-7, verifica color-blind-safe) · color semántico (rojo=malo/pérdida — cuidado, invertido en finanzas asiáticas). **Nunca rainbow/jet sobre datos secuenciales** (bandas falsas, no perceptualmente uniforme) → usa **viridis/cividis**.
**Transparencia = credibilidad:** cita la fuente, declara la metodología, muestra n, marca estimaciones/proyecciones. Es lo que separa periodismo de datos de propaganda con gráficos.
**Honestidad (graphical integrity de Tufte):** sin ejes truncados en barras, sin rangos cherry-picked, sin dual-axis que fabrica correlaciones espurias, sin manipular el aspect ratio para exagerar/aplanar pendientes.

## 6. 2026 y ética

**Generación de charts con IA y sus peligros:** la IA elige el gráfico *equivocado*, alucina insights que el dato no respalda y trunca ejes sin avisar. Investigación 2025-26 muestra que los MLLMs caen a nivel de azar evaluando gráficos engañosos y *premian* estéticamente ejes manipulados salvo que se les pida revisar integridad. **Verifica siempre:** ¿el gráfico responde la pregunta? ¿el eje es honesto? ¿el insight existe en el dato?
**Real-time dataviz** e **historias personalizadas** ("tu" consumo, "tu" barrio) — gran engagement, mayor riesgo ético (lo personalizado persuade más y se audita menos).
**La ética de la persuasión** (la línea fina entre storytelling y manipulación): resaltar tu punto es legítimo; ocultar lo que lo contradice no. Regla: *podrías mostrarle al lector el dato completo y tu conclusión seguiría sosteniéndose.* Si no, manipulas. **Data feminism / critical viz** (D'Ignazio & Klein): los datos no son neutrales — examina quién cuenta, qué se omite, qué grupos quedan invisibles en el agregado.

## Data-storytelling anti-patterns — blacklist
**exploratory cuando necesitabas explanatory** (volcar todo en vez del punto) · **eje Y truncado en barras** / dual-axis que fabrica correlaciones · **pie con >3 segmentos** (o 3D pie/dona ilegible) · **rainbow/jet sobre datos secuenciales**; codificar *solo* por color · **chartjunk** (3D, sombras, fondos, gradientes decorativos, gridlines pesados) · **sin anotación / título genérico** ("Ventas por mes") en vez de declarativo · **número sin contexto** (sin comparación, sin "so what") · **sin fuente, sin metodología, sin n** · **cherry-picking** del rango temporal o aspect ratio que exagera pendientes · **más de un mensaje por pieza** · **animación decorativa** sin object constancy (barras que saltan) · **móvil "reshrink"** (encoger el desktop) · **confiar en el chart generado por IA sin verificar** gráfico/eje/insight.

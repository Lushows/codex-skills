# 01 — Cómo funciona la subasta

Lee este módulo cuando no entiendas por qué un anuncio con buen presupuesto rinde mal y otro con poca plata vuela, o cuando alguien te diga "es que TikTok te cobra más por puja". La verdad incómoda: en TikTok **no gana el que más paga, gana el que más entretiene**. Entender la subasta te ahorra miles de pesos en pujas mal puestas y te explica por qué obsesionarte con el creativo (ver 30) es lo más rentable que puedes hacer. Si interiorizas un solo módulo técnico de esta skill, que sea este: la subasta es la física del sistema, y el creativo es la palanca que la dobla a tu favor.

## Qué es la subasta y cómo se decide el ganador

Cada vez que un usuario abre el For You, TikTok corre una subasta en milisegundos para decidir qué anuncio mostrarle. El ganador no es el de la puja más alta, sino el de mayor **valor total** para esa impresión. La fórmula conceptual:

**Valor total = Puja (Bid) × Tasa de acción estimada × Calidad del creativo y relevancia**

| Componente | Qué significa | Quién lo controla |
|---|---|---|
| **Bid (puja)** | Cuánto estás dispuesto a pagar por el resultado | Tú (o automático, ver 15) |
| **Tasa de acción estimada** | Probabilidad de que ESE usuario haga la acción que pediste (compra, lead) | El algoritmo, según tu Pixel/Events API (ver 05, 06) |
| **Calidad / relevancia** | ¿El video engancha? ¿Es nativo? ¿La gente lo ve, comenta, no lo salta? | Tu creativo (ver 31, 37) |

Un anuncio con un hook que retiene en los primeros 3 segundos (ver 37) puede ganarle a un competidor que puja el doble, porque su **tasa de acción estimada × calidad** es mucho mayor. TikTok prefiere mostrar lo que la gente sí quiere ver: así retiene al usuario en la app y vende más impresiones a futuro. La subasta es de **segundo precio ajustado**: ganas, pero pagas apenas lo necesario para superar al siguiente — por eso "pujar alto" rara vez es lo que te cobra de más; lo que te cobra de más es un creativo flojo que obliga a la máquina a subir el precio para colocarte.

## Por qué el creativo pesa MÁS que en Meta

En Meta, los públicos y el píxel hacen mucho del trabajo. En TikTok, **el contenido ES la segmentación**: el algoritmo decide a quién mostrarte según quién reacciona a tu video (ver 20). Esto cambia todo:

- Un mal creativo no se arregla subiendo la puja — solo gastas más rápido sin resultados.
- Un buen creativo **baja tu CPM** porque TikTok te recompensa con tráfico más barato por retener al usuario.
- El "thumbstop" (que la gente frene el dedo y no te salte) y el "hold rate" (cuánto retienes) son las señales que más mueven tu costo (ver 37, 49).

Regla práctica: si tu CPA está caro, el 80% de las veces el problema es el creativo, no la puja (ver 39). Antes de tocar la puja, mira el hook rate y el 6-second view rate (ver 09).

## El CPM real en LatAm (números honestos)

CPM = costo por mil impresiones (ver 09). Es la "tarifa de entrada" a la subasta. Rangos típicos en Colombia/LatAm a jun-2026 (varían por nicho, época y competencia):

| Mercado / situación | CPM aproximado (COP) |
|---|---|
| Colombia, nicho amplio, creativo decente | $8.000 – $18.000 |
| Colombia, nicho competido o Q4 (campaña navideña) | $18.000 – $35.000 |
| Creativo nativo viral / Spark Ad con tracción orgánica | puede bajar a $5.000 – $10.000 |
| Creativo tipo "ad" obvio, baja retención | se dispara, $30.000+ |
| TopView / Top Feed (premium reservado) | otra liga, $cientos de miles — branding (ver 02) |

El CPM no es algo que pones: es el **resultado** de qué tan bien tu creativo compite. Bajas el CPM mejorando el video, no negociando. Por eso TikTok es descubrimiento barato (ver 03) — *si* haces contenido nativo. Un dato útil para diagnosticar: si tu CPM está 2-3× sobre el rango del nicho con un público amplio, no tienes un problema de puja ni de audiencia, tienes un creativo que parece anuncio (ver 30).

## La densidad de subasta: por qué Q4 y los nichos calientes duelen

La subasta es un mercado: cuando más anunciantes pujan por la misma atención (Q4, Black Friday, Hot Sale, lanzamientos de temporada), el CPM sube para todos. No es que TikTok "te castigue": es competencia. En esos picos, el único anunciante que mantiene el costo a raya es el del creativo más nativo, porque su calidad/relevancia compensa la puja inflada. Planea producción extra de creativo para los meses calientes, no más presupuesto a secas.

## Cómo influir en la subasta a tu favor

| Palanca | Acción concreta |
|---|---|
| Mejorar tasa de acción estimada | Optimiza al evento correcto y aliméntalo con Events API + buen EMQ (ver 06, 14) |
| Subir calidad/relevancia | Hook fuerte 1-3s, sound-on, formato nativo vertical (ver 33, 37) |
| Usar Spark Ads | Impulsa posts orgánicos con prueba social real — la subasta los premia con CPM más bajo (ver 34) |
| Puja correcta | Empieza con puja automática (lowest cost); pasa a cost cap solo con datos (ver 15) |
| Volumen creativo | Más creativos = más oportunidades de que uno gane barato; alimenta a Smart+ (ver 12, 17) |
| Señal limpia | Eventos bien mapeados y deduplicados = la máquina estima mejor (ver 05, 06) |

## Errores comunes — blacklist

- **Subir la puja para "ganar más".** Solo gastas más rápido con el mismo mal creativo. Fix: arregla el video primero (ver 37).
- **Creer que CPM caro = TikTok malo.** El CPM caro es síntoma de creativo no-nativo. Fix: hazlo parecer un TikTok, no un anuncio (ver 30).
- **Poner cost cap desde el día 1.** Sin datos, ahogas la entrega y no sales de aprendizaje. Fix: arranca automático (ver 15).
- **Ignorar thumbstop / hold rate.** Optimizas el CPA sin ver la causa raíz. Fix: lee retención de 2s/6s en analytics (ver 49).
- **Mismo creativo para todos los públicos.** El algoritmo ya segmenta por reacción. Fix: confía en broad + buen creativo (ver 20).
- **Pensar que ganas por presupuesto.** El presupuesto te da escala, no victoria en la subasta. Fix: gana con relevancia, escala con presupuesto (ver 64).
- **No renovar creativo.** El que ganaba hoy pierde la subasta en 2 semanas por fatiga. Fix: pipeline constante de 5-15/semana (ver 39).
- **Meter más plata en Q4 sin más creativo.** El CPM sube y solo el creativo nativo lo aguanta. Fix: produce más videos para los picos, no solo más budget.

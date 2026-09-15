# 15 — Pujas (bidding)

Lee este módulo cuando TikTok te pregunte por la estrategia de puja y veas palabras como *lowest cost*, *cost cap*, *bid cap* o *ROAS goal*, cuando tu CPA esté subiendo y quieras "ponerle un techo", o cuando alguien te diga "pon un cost cap" sin explicarte qué número. La puja es **cómo TikTok compite por ti en la subasta** (cada vez que hay un espacio publicitario disponible, las marcas pujan y la que ofrece el mejor combo de oferta + relevancia + creativo gana ese impreso). Elegir mal la puja estrangula la entrega o quema el presupuesto — y casi siempre el problema no es la puja, sino el creativo o la oferta detrás.

## Las estrategias de puja

| Estrategia | Qué hace | Cuándo usarla |
|---|---|---|
| **Lowest cost** (default) | Consigue el máximo de conversiones al menor costo posible, sin techo | Arranque, fase de aprendizaje, cuando no conoces tu CPA real |
| **Cost cap** | Mantiene el CPA promedio **alrededor** de un techo que tú pones | Ya conoces tu CPA y quieres proteger márgenes al escalar |
| **Bid cap** | Pone un **tope duro** a lo que pagas por evento en la subasta | Avanzado, control férreo, riesgo de entrega baja |
| **Value / ROAS goal (VBO)** | Optimiza por **valor** (ROAS objetivo), no por cantidad de conversiones | E-commerce con tickets variados y buena señal de valor |
| **Max delivery** | Gasta el presupuesto lo más rápido posible | Urgencias, lanzamientos cronometrados, ofertas relámpago |

**VBO** = *Value-Based Optimization* (optimización por valor): en vez de pedir "muchas compras", le pides a TikTok "compras que sumen el mayor valor", útil cuando un cliente te deja $20.000 y otro $300.000. Requiere que el Pixel mande el value real (ver 14, 57). **ROAS goal** es el número objetivo que le das a VBO (ej. "quiero ROAS 2.5").

## Cuándo usar cada una (la decisión real)

Para el 90% de los casos en Colombia, la secuencia es esta — y es una secuencia, no un menú para elegir al azar:

1. **Arranca SIEMPRE en lowest cost.** En fase de aprendizaje (ver 13) no conoces tu CPA y cualquier cap estrangula la entrega antes de que el algoritmo aprenda. Deja que TikTok respire y encuentre compradores. Lowest cost = "consíguemelas lo más barato que puedas, sin atarte las manos".
2. **Cuando la campaña está estable** (salió de aprendizaje, ya tiene ≥50 conv) y sabes tu CPA real, considera **cost cap** para proteger márgenes al escalar. El cost cap es tu freno de mano cuando subes presupuesto y el CPA tiende a inflarse.
3. **ROAS goal (VBO)** solo cuando tienes buen volumen de compras con valores distintos y el Pixel manda el valor correcto (ver 57). Sin esa señal, VBO optimiza a ciegas.
4. **Bid cap** es para operadores avanzados con datos sólidos; mal usado, casi no entrega y te deja sin volumen para aprender.
5. **Max delivery** solo para gastar rápido en una ventana corta (día sin IVA, ver 19); fuera de eso, quema plata a CPA alto.

Tabla mental: ¿la campaña ya conoce su CPA real?
- **No** → lowest cost. Siempre.
- **Sí, y quiero escalar sin que el CPA se dispare** → cost cap calibrado.
- **Sí, y mis tickets varían mucho** → ROAS goal / VBO.
- **Necesito gastar X antes de mañana** → max delivery (y solo por eso).

## Calibrar el cap sobre el CPA REAL, no el deseado

Este es el error que más arruina los cost cap. La gente pone el cap en el CPA que **desea**, no en el que **tiene**.

Ejemplo brutal: tu CPA real estable es $35.000 COP, pero tú "quieres" pagar $18.000. Pones cost cap en $18.000. Resultado: TikTok **no encuentra** compradores a ese precio, **deja de entregar casi por completo**, la campaña muere de hambre, pierdes el aprendizaje acumulado y te quedas sin ventas Y sin datos. El cap no le ruega a la subasta; simplemente apaga la entrega cuando no puede cumplirlo.

Cómo calibrar bien:

| Paso | Acción |
|---|---|
| 1 | Corre en **lowest cost** hasta tener CPA real medido (≥50 conv, ver 13) |
| 2 | Pon el cost cap **ligeramente por encima o igual** a ese CPA real (CPA real $35k → cap $35–40k) |
| 3 | Si entrega bien y quieres bajar costo, **baja el cap de a poco** (~10% cada 3 días), vigilando que no se apague |
| 4 | Si la entrega cae, **sube el cap** — el algoritmo te está diciendo que tu objetivo no es realista a ese volumen |

Regla: el cap negocia con la realidad de la subasta, no con tus ganas. Si tu economía no cierra al CPA real, el problema es la **oferta o el creativo** (ver 41, 17), no la puja — y ese problema se valida con `economist_lushows` (¿el margen aguanta este CPA?), no bajando un número en TikTok hasta apagar la campaña.

## La puja no es la palanca principal en TikTok

A diferencia de Google Ads (donde Smart Bidding tCPA/tROAS hace gran parte del trabajo, ver `google_ads_lushows`), en TikTok la puja es **secundaria frente al creativo**. Un creativo que engancha baja tu CPM y tu CPA solo, porque el algoritmo lo distribuye más barato a más gente relevante. Antes de tocar la puja para "arreglar" un CPA caro, pregúntate si el problema real no es un hook flojo (ver 17, 68). La puja afina; el creativo define.

## Un cambio de puja resetea el aprendizaje

Cambiar de lowest cost a cost cap, o mover el cap fuerte (>~20%), **reinicia la fase de aprendizaje** (ver 13). No andes cambiando puja cada semana. Decide la estrategia, dale 3–7 días, y ajusta el número con calma en pasos chicos. Cada cambio de estrategia es una cirugía, no un ajuste de volumen.

## Errores comunes — blacklist

1. **Poner cost cap en el CPA deseado, no en el real.** TikTok deja de entregar; matas la campaña de hambre.
2. **Arrancar con cost cap o bid cap desde el día 1.** Estrangulas el aprendizaje antes de que empiece; arranca en lowest cost.
3. **Bajar el cap de golpe** para "ahorrar". La entrega se desploma; baja ~10% cada 3 días o no bajes.
4. **Usar ROAS goal (VBO) sin mandar el valor de compra al Pixel.** Optimiza por un valor que no recibe; trae basura (ver 14, 57).
5. **Cambiar de estrategia de puja cada semana.** Cada cambio resetea el aprendizaje (ver 13); decide y aguanta.
6. **Usar Max delivery como default.** Gasta rapidísimo y caro; es solo para ventanas cortas con urgencia real (ver 19).
7. **Culpar a la puja cuando el problema es la oferta o el creativo.** Ningún cap arregla un producto que no convierte (ver 41, 17).
8. **Tratar la puja como en Google.** En TikTok el creativo manda; la puja afina al final, no resuelve un CPA caro de raíz.
9. **Bajar el cap hasta apagar la campaña y creer que "no funciona TikTok".** Funcionaba; lo estrangulaste. Sube el cap y observa.

# 36 — Quality Score y relevancia

Lee este módulo cuando pagues más por clic que tu competidor por las mismas palabras, te aparezca un Quality Score de 3-4 y no sepas qué tocar, o quieras entender por qué dos cuentas con el mismo presupuesto rinden tan distinto.

El **Quality Score (QS, "Nivel de calidad", del 1 al 10)** es la nota que Google le pone a cada keyword según qué tan relevante y útil es tu anuncio para esa búsqueda. No es vanidad: es **tu descuento de CPC**. Un QS alto te deja pagar MENOS por clic y aparecer MÁS arriba que un competidor que puja más que tú pero tiene anuncios mediocres. Es la palanca que separa a quien "compra clics" de quien "gana la subasta con inteligencia". Recuerda la fórmula del Ad Rank (ver 30): posición = puja × QS + assets. Subir el QS es subir posición sin subir el gasto.

## Los 3 componentes (lo único que controlas)

El QS se arma de tres factores. Google los muestra como "Por encima del promedio / Promedio / Por debajo del promedio" en la columna de keywords:

| Componente | Qué mide | Cómo subirlo |
|---|---|---|
| **CTR esperado** | qué tan probable es que clickeen tu anuncio para esa búsqueda | mejor copy con la keyword en el título, más assets (ver 31, 32) |
| **Relevancia del anuncio** | qué tan bien tu anuncio responde a la búsqueda | keyword en el grupo correcto, anuncio que la mencione (ver 37) |
| **Experiencia de la landing** | qué tan buena, rápida y relevante es la página de destino | message match + velocidad (ver 33) |

El más pesado suele ser el **CTR esperado**: si la gente no clickea tu anuncio, Google asume que no eres relevante y te castiga. Por eso subir CTR (con copy y assets) es la vía más directa para subir QS. Es importante saber: el QS que ves en la interfaz es un **diagnóstico simplificado** (escala 1-10). En la subasta real, Google calcula la calidad en vivo para cada búsqueda concreta, considerando dispositivo, hora, ubicación e intención del query exacto. O sea: el número 1-10 es tu termómetro, pero la calidad real se recalcula en cada subasta (ver 01).

## Cómo verlo y diagnosticarlo

En Google Ads, en la vista de keywords, agrega las columnas: **Quality Score**, **CTR esp.**, **Relevancia del anuncio** y **Exp. de la página de destino**. Eso te dice EXACTAMENTE cuál de los tres está flojo. No adivines: la columna te lo señala.

| Lo que ves | Significa | Qué arreglar |
|---|---|---|
| CTR esp. "Por debajo" | tu anuncio no llama al clic | reescribe títulos con la keyword + beneficio + assets (31, 32) |
| Relevancia "Por debajo" | la keyword está en el grupo equivocado | reagrupa por tema, un anuncio por tema (37) |
| Exp. página "Por debajo" | landing lenta o irrelevante | mejora velocidad y message match (33 → `desingweb-lushows`) |

Truco de diagnóstico: si las TRES columnas están "Por debajo" en muchas keywords, el problema no es el anuncio — es la estructura: tienes temas mezclados en un mismo grupo (ver 37). Reagrupar arregla las tres de un golpe.

## Por qué el QS es tu descuento de CPC (con números)

Dos anunciantes pujan por la misma palabra. El de QS alto puede pagar menos Y salir más arriba, porque Google premia la relevancia para que el usuario tenga buena experiencia. Cifras ilustrativas en COP (no exactas, para que captes la lógica):

| Anunciante | Puja máx | QS | Ad Rank (puja×QS) | Resultado |
|---|---|---|---|---|
| A | $1.500 | 8 | 12.000 | sale #1 pagando ~$900 por clic |
| B | $2.000 | 3 | 6.000 | sale #2 pagando ~$1.900 por clic |

A puja MENOS y gana, porque su relevancia le da un Ad Rank mejor con menos plata. Encima A paga menos por clic. Esto, multiplicado por miles de clics al mes, es la diferencia entre una cuenta rentable y una que quema presupuesto. Si A y B gastan $3.000.000/mes cada uno: A compra ~3.300 clics, B compra ~1.580 clics. Mismo presupuesto, A trae el DOBLE de tráfico — y más arriba. Por eso obsesionarse con "subir la puja" sin tocar el QS es el camino caro.

Y se retroalimenta: mejor anuncio → más CTR → mejor QS → CPC más barato → más clics con el mismo presupuesto → más datos → mejor optimización. El QS no es una nota suelta; es el motor de eficiencia de toda la cuenta. Por eso los tres módulos que lo alimentan — anuncio (31, 32), estructura (37) y landing (33) — son los que más mueven la aguja, más que cualquier ajuste de puja.

## QS y Smart Bidding: ¿sigue importando en 2026?

Sí, aunque uses Smart Bidding (tCPA/tROAS, ver 13, 15). El mito moderno es "ya la IA puja por mí, el QS no importa". Falso: el QS sigue determinando el Ad Rank, y un QS bajo encarece cada clic que la IA compra. La IA optimiza DENTRO de las reglas de la subasta; no las rompe. Darle a Smart Bidding anuncios relevantes y landings rápidas es darle mejor materia prima para que rinda. Un QS pobre obliga a la IA a pagar de más para conseguir las mismas conversiones, y te sube el CPA. La relevancia nunca dejó de pagar.

## Errores comunes — blacklist

- **Subir la puja para "salir arriba" ignorando el QS**: pagas de más cuando podías subir posición gratis mejorando relevancia (ver Ad Rank, 30).
- **No agregar las columnas de los 3 componentes**: diagnosticas a ciegas; Google ya te dice cuál falla, míralo.
- **Meter keywords de temas distintos en un mismo grupo**: baja la relevancia del anuncio porque ningún anuncio le queda bien a todas; reagrupa por tema (37).
- **Culpar al QS de la landing pero nunca tocar la página**: la experiencia de destino es 1 de los 3 factores; si está "por debajo", el problema es la web, no el anuncio (33).
- **Creer que el QS sube de un día para otro**: necesita tráfico nuevo con el anuncio/landing mejorados para recalcularse; dale tiempo y datos.
- **Perseguir QS 10 en todo**: con 7-8 ya tienes buen descuento; gastar horas por 1 punto extra rinde menos que arreglar un grupo en 4.
- **Olvidar que CTR esperado es el factor más pesado**: si descuidas el copy y los assets, ningún arreglo de landing salva el QS (ver 31, 32).
- **Creer que con Smart Bidding el QS ya no cuenta**: sigue fijando el Ad Rank; un QS bajo encarece cada clic que la IA compra (ver 13).

# 288 — Escribir con IA sin que se note

> Un modelo escribe rápido, escribe correcto y escribe **plano**. Ese texto plano tiene una firma: se
> reconoce en dos frases, y cuando alguien lo reconoce, todo lo que dice el video pierde valor de golpe.
> No porque esté mal, sino porque suena a que a nadie le importó lo suficiente como para escribirlo.

Esto no es un módulo en contra de usar un modelo. Es un módulo sobre **usarlo en el sitio correcto**:
un modelo es un buen ayudante de estructura y un pésimo autor de la frase final.

---

## Dónde sirve y dónde no

| El modelo es bueno para | El modelo es malo para |
|---|---|
| Vaciar todos los datos que sabes en una lista (`282` paso 1) | Escribir la frase que va a decir una persona a cámara |
| Proponer 20 ganchos para elegir uno | Elegir cuál sirve |
| Reordenar un guion por tensión | Encontrar el dato que engancha (`283`) |
| Detectar frases largas o trabadas | Decidir el tono |
| Traducir la ficha a lenguaje sencillo | Sonar como tú |
| Sacar 10 variantes del remate para escoger (`287`) | Saber cuál de las 10 es la buena |
| Recordarte lo que dejaste sin resolver | Inventar la anécdota que no le contaste |

> **Regla de reparto: el modelo produce cantidad, tú decides. Nunca al revés.**
> Un texto que ningún humano eligió palabra por palabra sale plano siempre.

Y una advertencia que vale por todo el módulo: **el modelo no puede inventar el material que solo tú
tienes**. Lo del relieve de la botella, lo de los seis meses malos del bar, lo de las 40 cervezas del
primer mes: eso no está en ningún modelo. Si le pides que escriba sin darle nada tuyo, te devuelve lo
que le sirve a cualquiera, que es exactamente lo que no sirve.

---

## LAS MULETILLAS DELATORAS

Estas son las marcas que hacen que un texto se lea como generado. Búscalas y bórralas **todas**, siempre,
sin excepción.

### 1. La estructura "no es X, es Y"

> "No se trata solo de vender cerveza, se trata de crear momentos."
> "Esto no es una tabla de Excel, es tranquilidad."

Es la construcción número uno. Suena profunda y no dice nada. Aparece cuatro veces en cualquier texto
generado si no la prohíbes.

**Arreglo:** di solo la parte concreta. *"Es una tabla de Excel. Te dice cuánto te cuesta el plato."*

### 2. El tricolon perfecto

Tres elementos con la misma estructura y la misma longitud: "más rápido, más simple, más rentable".
La repetición de tres funciona (`285`) — pero cuando los tres elementos son **abstractos y del mismo
tamaño**, es firma de modelo.

**Arreglo:** que los tres sean cosas, no adjetivos, y que uno sea más largo o más raro que los otros.
*"La papa que pelas, el tomate que botas, el aceite que cambias antes de tiempo."*

### 3. El vocabulario de folleto

| Palabra delatora | Qué usar |
|---|---|
| "descubre", "sumérgete", "explora" | "mira", "prueba" |
| "eleva tu negocio", "lleva tu X al siguiente nivel" | *(bórralo)* |
| "en un mundo donde…" | *(bórralo)* |
| "la clave está en…" | *(bórralo)* |
| "no es casualidad que…" | *(bórralo)* |
| "cada detalle cuenta" | un detalle concreto |
| "una experiencia única" | qué pasa exactamente |
| "verdaderamente", "realmente", "genuinamente" | *(bórralo)* |
| "transformar", "potenciar", "optimizar" | "cambiar", "mejorar", "gastar menos" |
| "el arte de…", "la magia de…" | *(bórralo)* |
| "desde X hasta Y, pasando por Z" | una lista normal |

### 4. La simetría excesiva

Todos los párrafos del mismo tamaño. Todas las frases entre 10 y 14 palabras. Cada sección con
exactamente tres puntos. **El texto humano es desparejo**: tiene un párrafo de una línea, otro de seis,
una frase de dos palabras. La regularidad perfecta es firma de máquina (`285`).

### 5. El cierre que resume y se despide

> "En definitiva, lo importante es entender tus costos para tomar mejores decisiones."

Es la cola verbal escrita (`287`). Un modelo cierra resumiendo porque así se cierran los ensayos. Un
video no se cierra así nunca.

### 6. Los conectores de redacción escolar

"Además", "asimismo", "por otro lado", "en conclusión", "cabe destacar", "es importante mencionar".
Son los mismos que arruinan el guion hablado (`280`, `281`). Doble motivo para borrarlos.

### 7. El entusiasmo sin causa

Signos de exclamación, "¡increíble!", "¡lo mejor de todo es que…!". Nadie está tan emocionado a las
tres de la tarde y se nota (`284`).

### 8. La precisión falsa

"Aumenta tus márgenes hasta un 30%", "más de 200 negocios ya lo usan" — cuando nadie midió eso. Un
modelo rellena los huecos con cifras plausibles. **Toda cifra que salga de un modelo se verifica o se
borra** (`283`).

### 9. Emoji de decoración

Un emoji cada dos líneas, sobre todo 🔥✨🚀. Firma inmediata.

### 10. El "tú" de coach

"Tú puedes lograrlo", "es hora de que tomes el control de tu negocio". Es segunda persona, sí, pero de
autoayuda. La segunda persona buena es concreta: *"tu plato te cuesta 21"*.

---

## CÓMO PEDIRLE (el prompt que sí da material usable)

El problema no suele ser el modelo: es que le pides "escríbeme un guion para un reel de mi bar" y le
das cero materia prima. Con nada tuyo, devuelve lo de todos.

### Los cinco ingredientes de un buen encargo

**1. Dale tu material crudo.** Lo más importante. Pégale la transcripción de esos 15 minutos hablando
suelto (`284`), tus datos verificados (`283`), tus números reales.

**2. Dale la voz por escrito.** Las dos listas —PALABRAS DE LA CASA y NUNCA— y la frase patrón y la
prohibida (`284`). Sin esto, inventa una voz.

**3. Dale las restricciones duras.** Número de palabras, largo máximo de frase, plataforma, que sea para
decirse en voz alta.

**4. Pídele cantidad, no calidad.** "Dame 15 versiones del gancho" produce mejor material que "dame el
mejor gancho". De 15, dos sirven. De 1, ninguna.

**5. Prohíbe explícitamente las muletillas.** Si no las prohíbes, salen.

### Encargo de ejemplo (funciona)

```
Contexto: bar-restaurante en Tocancipá, Colombia. Serie "Historias de Cerveza",
video vertical de 45 s para Reels.

Material crudo (transcripción de mí hablando suelto):
[pegar los 15 minutos transcritos]

Dato verificado que es el eje: el relieve de la botella de Cusqueña está
inspirado en la piedra de los doce ángulos, un muro inca del Cusco.

Voz: hablo de tú. Palabras de la casa: fría, mira, ojo, salud, nos tocó.
Nunca uso: descubre, experiencia única, no te lo pierdas, premium, calidad.
Frase patrón: "Nadie se fija en el relieve de esta botella."
Frase prohibida: "Descubre la experiencia premium que tenemos para ti."

Restricciones:
- 100 palabras de voz máximo
- ninguna frase de más de 12 palabras
- una sola idea por frase
- se va a decir en voz alta: nada de incisos, paréntesis ni subordinadas
- un solo nombre propio por frase y al final de la frase
- cifras exactas van en rótulo, no en voz

Prohibido: "no se trata de X sino de Y", "en un mundo donde", "descubre",
"eleva", "la clave está en", emojis, signos de exclamación, cifras que yo
no te di, cerrar resumiendo.

Dame 8 versiones distintas del bloque de apertura (2 frases cada una).
No escribas el guion completo todavía.
```

Fíjate en la última línea: **se pide por partes**. Un guion completo generado de un tirón sale
uniforme; pedido por bloques y escogido a mano sale desparejo, que es como suena lo escrito por
alguien.

---

## LO QUE SIEMPRE HAY QUE CORREGIRLE

Aunque el encargo esté perfecto. Esta es la pasada obligatoria, en orden:

1. **Bórrale el primer párrafo.** Casi siempre es preámbulo. El video empieza en la segunda frase.
2. **Búscale "no es X, es Y"** y mátala.
3. **Quítale las cifras que no le diste.** Todas.
4. **Cámbiale los verbos de folleto** por los tuyos.
5. **Rómpele la simetría**: parte una frase en dos, junta otras dos en una acumulación (`285`).
6. **Métele una palabra tuya que él nunca usaría.** Una sola cambia el registro del párrafo entero:
   "nos tocó", "bacano", "ojo".
7. **Cámbiale el remate.** El suyo resume y se despide. Escribe tú las diez versiones (`287`).
8. **Reemplázale un genérico por un específico tuyo.** Donde diga "muchos negocios", pon "el bar de la
   esquina de mi cuadra". Ahí es donde el texto deja de ser de nadie.
9. **Léelo en voz alta** (`280`). Este paso no es negociable y es el que decide.
10. **Pásale `281`**: nombres propios, oclusivas, subordinadas.

> Si haces solo dos de estos diez, haz el 8 y el 9: **meterle lo específico tuyo y leerlo en voz alta**.

---

## La prueba de las dos frases

Cómo saber si un texto quedó con firma de modelo:

> **Lee las dos primeras frases y las dos últimas. Si podrían ser de cualquier otro negocio del mismo
> rubro, es texto de modelo, aunque lo hayas escrito tú.**

*"En Bendita Pola creemos que cada cerveza cuenta una historia."* → puede ser de cualquier bar del país.
*"Nadie se fija en el relieve de esta botella."* → solo puede ser de este video.

---

## Dos usos que sí valen mucho la pena

Para no quedarse solo con las prohibiciones:

**1. El modelo como corrector, no como autor.**
Escribe tú el guion. Después pídele: *"Marca las frases de más de 12 palabras, las que tengan
subordinada, las que tengan más de una sibilante cada cuatro palabras y las que tengan dos nombres
propios."* Es rápido, es aburrido, lo hace bien y no toca tu voz.

**2. El modelo como generador de variantes para pauta.**
Dale tu gancho bueno —el tuyo, el humano— y pídele 10 variantes con la misma estructura. Para probar
ganchos en anuncios (`30`, `159`) eso es exactamente lo que se necesita: volumen a partir de algo que ya
funciona.

---

## Errores comunes

1. **Pedirle un guion sin darle material tuyo.** Devuelve lo que le sirve a cualquiera.
2. **Publicar lo que salió.** Nunca. Ni siquiera cuando "quedó bien": *quedó bien* y *suena a ti* son
   cosas distintas.
3. **No darle la voz por escrito.** Si no se la das, se inventa una.
4. **Pedir "el mejor gancho"** en vez de 15 para elegir.
5. **Pedir el guion completo de un tirón.** Sale uniforme. Se pide por bloques.
6. **Dejar "no se trata de X, sino de Y".** La firma más reconocible que existe.
7. **Dejar las cifras que inventó.** Toda cifra se verifica o se borra.
8. **Dejar el cierre que resume.** Es la cola verbal escrita.
9. **Dejar la simetría perfecta.** El texto humano es desparejo.
10. **No meterle ni una palabra propia.** Una sola cambia el párrafo entero.
11. **No leerlo en voz alta** porque "ya está bien escrito". Bien escrito ≠ decible (`281`).
12. **Usarlo para decidir.** Produce cantidad; decides tú.
13. **Creer que le puede sacar la anécdota buena.** Lo específico tuyo solo lo tienes tú.

---

## Checklist

- [ ] Se le dio **material crudo propio**: transcripción, datos verificados, números reales
- [ ] Se le dio la **voz escrita**: palabras de la casa, palabras prohibidas, frase patrón y prohibida
- [ ] Se le dieron **restricciones duras**: palabras totales, largo de frase, "se dice en voz alta"
- [ ] Se le **prohibieron las muletillas** explícitamente en el encargo
- [ ] Se pidió **cantidad** (10–15 versiones) y **por bloques**, no el guion completo
- [ ] Se borró el **primer párrafo** de lo que devolvió
- [ ] Cero "no se trata de X, sino de Y"
- [ ] Cero "descubre", "eleva", "en un mundo donde", "la clave está en", "cada detalle cuenta"
- [ ] Cero cifras que no salieron de una fuente verificada (`283`)
- [ ] Se **rompió la simetría** de frases y párrafos (`285`)
- [ ] Hay al menos **una palabra propia** que el modelo nunca habría usado
- [ ] Hay al menos **un específico tuyo** donde había un genérico
- [ ] El **remate lo escribiste tú**, con diez versiones (`287`)
- [ ] Pasa la **prueba de las dos frases**: no podría ser de otro negocio
- [ ] Se **leyó en voz alta** completo (`280`) y se pasó el filtro de decibilidad (`281`)

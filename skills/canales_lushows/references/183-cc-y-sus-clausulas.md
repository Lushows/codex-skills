# 183 · CC y sus cláusulas

**Qué resuelve:** las licencias Creative Commons no son una cosa: son **cuatro piezas
que se combinan**. Saber qué exige cada pieza evita dos errores caros — incumplir una
atribución trivial, y meter en el episodio una cláusula que se contagia a todo lo demás.

> ⚠️ **Esto no es asesoría legal.** Es cómo tratamos las cláusulas en producción. Las
> interpretaciones difíciles se resuelven descartando la pieza, no razonándola.

---

## Las cuatro piezas

| Pieza | Qué exige | Para nosotros |
|---|---|---|
| **BY** — Atribución | Dar crédito al autor | ✅ obligatorio y barato (§ 184) |
| **SA** — Compartir igual | La obra adaptada se comparte bajo la misma licencia | ⚠️ cláusula vírica |
| **NC** — No comercial | Nada dirigido a ventaja comercial | ❌ el canal monetiza (§ 180) |
| **ND** — Sin obra derivada | No se comparte material adaptado | ❌ el montaje siempre adapta |

De ahí salen seis licencias, y **todas llevan BY**: no existe una CC sin atribución.
CC0 no es una licencia sino una renuncia, y por eso no exige crédito (aunque nosotros lo
anotamos igual). Fuente: [About CC Licenses](https://creativecommons.org/share-your-work/cclicenses/).

## BY: la parte fácil que se incumple por pereza

Atribuir cuesta una línea en la descripción y es la única obligación de CC BY. La
práctica recomendada por Creative Commons se resume en **TASL**: *Title, Author, Source,
License* — título, autor, fuente y licencia, con enlace donde sea posible
([Recommended practices for attribution](https://wiki.creativecommons.org/wiki/Recommended_practices_for_attribution)).

Esos cuatro campos son exactamente los que ya guarda `fuentes.json` (`titulo`, `autor`,
`url`, `licencia`). No es casualidad: el registro se diseñó para poder escribir los
créditos sin volver a buscar nada (§ 184).

## SA: la cláusula vírica, explicada para un montaje

**Qué dice.** Si adaptas una obra BY-SA y compartes la adaptación, tienes que publicarla
bajo la misma licencia o una compatible. Aplicada a un vídeo, esa obligación podría
alcanzar **al episodio entero**, que es trabajo propio: locución, montaje, música
sintetizada, tipografía. Publicar un episodio bajo BY-SA significa que cualquiera puede
reutilizarlo comercialmente. Es una decisión de negocio, no un detalle técnico.

**El matiz que todo el mundo cita.** Creative Commons distingue entre **adaptación** y
**colección**: una colección reúne obras separadas e independientes en un conjunto, y
**una colección no es una adaptación**; en ese caso no hace falta licenciar la obra
entera bajo SA, aunque sí cumplir la licencia del material incorporado
([4.4 Remixing CC-Licensed Work](https://creativecommons.org/course/cc-cert-edu/unit-4-using-cc-licenses-and-cc-licensed-works/4-4-remixing-cc-licensed-work/)).
La propia CC admite que esta distinción es **uno de los conceptos más difíciles** del
derecho de autor.

**Dónde nos deja eso.** En una zona gris que no queremos habitar. Un documental de
collage no es un caso limpio de «colección»: recortamos en silueta, viramos el color,
añadimos grano, animamos y superponemos la pieza con otras. Eso se parece mucho más al
batido que a la caja de frutas.

🔴 **Pendiente de verificar, caso por caso:** si un episodio concreto llega a depender de
una pieza BY-SA irreemplazable, la pregunta «¿esto es adaptación o colección?» hay que
llevarla a alguien cualificado, no resolverla en el manual. No hay una respuesta
universal y este documento no la inventa.

## La regla operativa del canal

En orden de preferencia, y sin excepciones informales:

1. **Dominio público, por origen o por plazo** (§ 181, § 182).
2. **CC0.**
3. **CC BY** — se acepta siempre; el precio es una línea de crédito.
4. **CC BY-SA** — se acepta **solo si no hay sustituto** y siempre que la pieza sea
   secundaria: fondo, textura, un plano de apoyo. Nunca el plano protagonista de un
   bloque, nunca la miniatura, nunca la pieza que se convierte en el cartel del
   episodio.
5. **NC, ND y todo lo reservado** — fuera, sin conversación (§ 180).

Y una regla añadida de sentido común: **si dos piezas cuentan lo mismo y una es PD y la
otra BY-SA, entra la PD**. Con 60 piezas por episodio, casi siempre hay sustituto.

## Las versiones y los puertos

`CC BY 2.0`, `CC BY 3.0 ES`, `CC BY 4.0`: el número es la versión de la licencia y el
sufijo, la adaptación a una jurisdicción. Para nuestro criterio (comercial + modificar)
las tres se comportan igual, pero **el texto que se copia a `fuentes.json` es el exacto,
con versión**, porque es lo que después se escribe en los créditos y lo que se enseña si
hay reclamación (§ 189).

## Lo que la licencia CC **no** te da

Aunque la pieza sea CC BY perfecta, la licencia cubre el derecho de autor del
fotógrafo. **No** cubre:

- Derechos de imagen de las **personas reconocibles** que aparecen.
- Marcas registradas visibles (logotipos, rótulos comerciales).
- Obras protegidas **dentro** de la foto (un cuadro, un cartel, una escultura moderna).
- El uso que sugiera **respaldo o vínculo** del autor con nuestro canal: CC pide
  explícitamente no dar a entender que el autor te avala.

Por eso el chequeo de contenido (§ 96) es una comprobación distinta de la de licencia, y
las dos son obligatorias.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Leer «CC BY-NC» y quedarse en el «BY» | Pieza inutilizable en canal monetizado |
| Usar BY-SA en el plano protagonista | El episodio entero queda expuesto a la cláusula vírica |
| Resolver «¿adaptación o colección?» por intuición | Es de los conceptos más difíciles del derecho de autor: no se decide en el montaje |
| Atribuir «Wikimedia Commons» como autor | Commons es el repositorio, no el autor: incumple BY |
| Anotar «CC BY» sin versión | Los créditos quedan incompletos y la prueba, débil |
| Dar por hecho que CC cubre marcas y caras | Son derechos distintos que la licencia no toca |
| Publicar la pieza recortada sin crédito «porque ya no se reconoce» | Adaptar no exime de atribuir |

## Relacionado

`180` las familias de licencia · `184` la atribución en la descripción ·
`185` lo que parece libre y no lo es · `188` `fuentes.json` como compuerta ·
`96` verificación de datos

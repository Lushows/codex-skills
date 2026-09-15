# 363 — Gancho visual, hablado o de texto: quién lleva la pelota

> Los tres canales están siempre presentes. La pregunta no es "cuál uso", es **cuál manda**. Un gancho
> tiene un canal líder y dos de apoyo, y cuando los tres intentan liderar a la vez el resultado es ruido.
> Este módulo es el criterio para decidir quién lleva la pelota en cada video.

---

## Los tres canales y su velocidad real

| Canal | Cuándo llega al espectador | Qué hace bien | Qué hace mal |
|---|---|---|---|
| **Visual** | Inmediato (fotograma 0) | Provocar pregunta, mostrar estado, dar contexto físico | Explicar, dar cifras, matizar |
| **Hablado** | 0,1 – 0,4 s de retraso (y solo si hay sonido) | Acusar, confesar, contradecir, dar el matiz | Sobrevivir al mudo |
| **Texto** | 0,15 – 0,30 s por palabra hasta ser legible | Fijar una idea, dar el número, sobrevivir al mudo | Cargar emoción, matizar |

Ese retraso del audio no es teoría: el video se muestra antes de que el sonido esté sonando de verdad.
Por eso **el fotograma 0 nunca puede depender de una frase**.

Y el texto tiene un costo temporal que en tu gramática es medible: palabras sueltas entrando cada
**0,15–0,30 s**, hasta 6 en cascada. Seis palabras = entre **0,9 y 1,8 segundos** para estar completas.
Eso es todo el gancho. Por eso el texto no puede llevar la pelota con seis palabras: la lleva con **dos
o tres**.

---

## La regla del reparto

> **Un canal declara el conflicto. Los otros dos lo refuerzan diciendo algo distinto.**

El error más común y más caro es la **redundancia total**: la imagen muestra la cerveza, la voz dice "la
cerveza" y el texto dice **CERVEZA**. Tres canales gastados para transmitir una sola cosa. Es como
mandar tres meseros a llevar el mismo plato.

Ejemplo del reparto correcto:

| Canal | Contenido | Función |
|---|---|---|
| Visual | Un vaso desbordándose | La situación |
| Hablado | "Llevo tres años sirviendo mal" | La confesión (el conflicto) |
| Texto | **TRES AÑOS** | El número que se fija |

Tres cosas distintas que juntas dicen una cuarta. Ese es el trabajo.

---

## Un paréntesis honesto: el efecto Kuleshov

Se cuenta siempre que dos planos juntos crean un significado que ninguno tiene solo, y se cita el
experimento de Kuleshov (misma cara neutra + sopa / ataúd / mujer) como prueba.

Dos precisiones:

1. **El material original se perdió.** Lo que sabemos es de segunda mano, sobre todo del relato de
   Pudovkin años después.
2. Cuando se ha intentado replicar, **el efecto aparece mucho más débil** de lo que cuenta la leyenda.
   La yuxtaposición influye, pero no reprograma la cara.

Qué te llevas de esto, práctico: **no confíes en que el montaje solo va a fabricar el sentido**. Si
necesitas que el espectador entienda que el vaso desbordado es un problema, no basta con ponerlo al lado
de una cara neutra. La cara tiene que hacer algo, o la voz tiene que decirlo, o el texto tiene que
nombrarlo. El montaje suma; no inventa de la nada.

---

## Cuándo lleva la pelota el canal VISUAL

**Úsalo cuando:**

- La cosa se puede mostrar y es rara, fea, imposible o hermosa de verdad.
- El video es de proceso: se prepara algo, se arma algo, se destruye algo.
- El público es amplio y no comparte contexto (turistas, gente que pasa por Tocancipá).
- No tienes buen audio ese día. Un gancho visual salva un bruto con audio malo.

**Cómo se monta:**

- El fotograma 0 es la cosa, ya en movimiento (ver `360`).
- **Silencio de voz los primeros 1,5 s**, o solo sonido real (el *chac*, el *pssshhh*, el freidor).
- La primera frase hablada llega después y **no explica lo que se vio**: lo profundiza o lo niega.
- El texto, si va, es una sola palabra confirmando lo raro: **BOCA ABAJO**, **SIN HORNO**, **A LAS 4 AM**.

**El error típico:** enseñar la cosa rara y explicarla en la misma respiración. Se cierra la pregunta
antes de que el espectador termine de formulársela.

---

## Cuándo lleva la pelota el canal HABLADO

**Úsalo cuando:**

- El conflicto es una idea, no una imagen: un precio, una creencia, una decisión, una confesión.
- Hay matiz. La voz es el único canal que puede decir "en parte tienen razón" sin sonar tibia.
- Ya tienes público que te conoce la cara y la voz.

**Cómo se monta:**

- La frase empieza **antes de los 0,25 s** y el conflicto queda cerrado **antes de 1,2 s**.
- Cortar todo el aire de adelante del bruto. El "bueno, entonces" no existe.
- **Nunca dependas solo de la voz.** Un gancho hablado sin texto de respaldo se pierde entero con quien
  ve en mudo (ver `368`).
- El texto de apoyo lleva **las 2 o 3 palabras clave** de la frase, no la frase.

**La prueba de fuego:** exporta sin audio y míralo.

```bash
ffmpeg -y -i reel.mp4 -an -c:v copy prueba_muda.mp4
```

Si en mudo no se entiende qué está en juego en los primeros 2 segundos, el gancho hablado está
desprotegido.

---

## Cuándo lleva la pelota el canal TEXTO

**Úsalo cuando:**

- El gancho es un **número** o una **comparación**. Los números se leen mejor de lo que se oyen.
- Estás en un ambiente ruidoso y grabaste sin voz aprovechable.
- El video es de lista, precio, antes/después o dato duro.
- Sabes que ese contenido lo ven en el trabajo, en el bus o en la cama (o sea, casi todo).

**Cómo se monta, con tu gramática:**

- **Máximo 3 palabras en el arranque**, no 6. Las cascadas de 6 son para el cuerpo del video, no para el
  gancho.
- Entrada de **0,15 s** entre palabra y palabra en el gancho (el extremo rápido de tu rango), porque son
  pocas y cortas.
- Primera palabra en el **fotograma 3 o 4**, jamás en el 0.
- Cuerpo de letra grande de verdad: la palabra clave debe ocupar **entre el 12% y el 20% de la altura**
  del cuadro en 9:16 (ver `44` y `45`).
- La palabra que carga el conflicto va **sola en su línea** y se queda un poco más (0,4–0,6 s) antes de
  que entre la siguiente.

**El error típico:** subtítulos corridos como gancho. Un renglón completo obliga a leer de izquierda a
derecha mientras la imagen se mueve. Las palabras sueltas en cascada existen justamente para evitar eso.

---

## La tabla de decisión

Responde en orden. La primera que dé "sí" decide.

| Pregunta | Si es sí → lleva la pelota |
|---|---|
| ¿Hay una imagen que por sí sola provoca una pregunta? | **Visual** |
| ¿El conflicto es un número o una comparación exacta? | **Texto** |
| ¿El conflicto es una creencia, una confesión o una acusación? | **Hablado** (con texto de respaldo) |
| ¿El audio del bruto es malo o hay mucho ruido? | **Visual** o **Texto** |
| ¿No pasa ninguna? | No tienes gancho. Vuelve a `361` |

---

## Combinaciones que sí funcionan (y una que no)

**Visual líder + hablado de apoyo** — el más robusto. Sobrevive al mudo, sobrevive al ruido, no depende
de tu día de voz. Es el que más se debería usar en un bar.

**Hablado líder + texto de apoyo** — el de más personalidad. Construye marca personal. Obligatorio poner
las palabras clave en pantalla.

**Texto líder + visual de apoyo** — el más barato y el más frío. Perfecto para precio, horario, promoción
y dato. Cuida que la imagen no sea un fondo muerto.

**Los tres a la vez diciendo lo mismo** — no funciona. Se siente publicidad, se siente plantilla, y se
salta.

---

## Un detalle que casi nadie mira: el volumen no es tuyo

Se repite que "el 85% ve sin sonido". Ese dato es de **mayo de 2016**, de Digiday, y no era un estudio:
eran tres editores contando cuánto de **su** video de Facebook se veía en mudo, cuando Facebook
autorreproducía **sin sonido por defecto**. TikTok y Reels no funcionan así: arrancan **con sonido**, si
el celular no está en silencio.

O sea: ni "todo el mundo ve en mudo" ni "el sonido se oye siempre". Una parte real de tu público te va a
ver en silencio (en el trabajo, en la cama, en el bus) y **no hay un número público confiable para Reels
o TikTok en 2026**. Por eso la regla no es estadística, es de diseño: **el video tiene que funcionar
mudo y mejorar con sonido.** Ver `368`.

---

## Errores comunes

1. Los tres canales diciendo lo mismo. Se gastan tres recursos para transmitir uno.
2. Un gancho hablado sin ninguna palabra en pantalla: se pierde entero con quien ve en mudo.
3. Seis palabras en cascada en el gancho: tardan hasta 1,8 s en estar completas y tapan la imagen.
4. Poner texto en el fotograma 0. No se lee y arruina la portada real del video.
5. Mostrar la cosa rara y explicarla en la misma frase: se cierra la pregunta antes de tiempo.
6. Confiar en que el montaje solo va a fabricar el sentido (la lectura ingenua de Kuleshov).
7. Usar subtítulos corridos como gancho, en vez de palabras sueltas.
8. Elegir canal por gusto y no por material: si el audio del bruto es malo, el gancho no puede ser
   hablado ese día.
9. Texto pequeño "para que se vea elegante". En 9:16 y en un celular, elegante es ilegible.
10. Poner la palabra clave en medio de la cascada, donde se pierde entre las otras cinco.
11. No probar el video en mudo antes de publicar. Cuesta un comando.
12. Cambiar de canal líder a mitad del gancho: empieza visual, sigue hablado, remata en texto, y no queda
    nada claro.

---

## Checklist

- [ ] Sé cuál de los tres canales lleva la pelota en este gancho
- [ ] Los otros dos dicen cosas **distintas** que suman
- [ ] El fotograma 0 no depende de ninguna frase
- [ ] Si el gancho es hablado, hay 2 o 3 palabras clave en pantalla como respaldo
- [ ] Si el gancho es de texto, son 3 palabras o menos y entran cada 0,15 s
- [ ] La primera palabra entra en el fotograma 3 o 4, no en el 0
- [ ] La palabra que carga el conflicto va sola y se queda 0,4–0,6 s
- [ ] Si el gancho es visual, la primera frase hablada no explica: profundiza o niega
- [ ] Exporté sin audio y el gancho sigue entendiéndose
- [ ] El cuerpo de letra de la palabra clave ocupa al menos el 12% de la altura del cuadro
- [ ] El canal líder es coherente con la calidad real del bruto de ese día

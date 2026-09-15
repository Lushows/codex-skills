# 211 — Efectos y filtros en CapCut: la biblioteca, la paleta y la disciplina

CapCut trae decenas de miles de efectos. Esa es su mayor fortaleza y su trampa más grande.

La fortaleza: cualquier cosa que se te ocurra, probablemente ya existe con un clic.
La trampa: cualquier cosa que se te ocurra, probablemente ya existe con un clic — y terminás con un
video que parece una vitrina de efectos en vez de una pieza con voz propia.

Este módulo te enseña a navegar la biblioteca, a entender cómo está organizada por dentro, y sobre
todo a **construir una paleta corta y repetirla**, que es lo que separa a un editor con estilo de
alguien que le puso filtros a un video.

---

## Efecto vs. filtro: no son lo mismo

CapCut los pone en pestañas distintas y hace bien.

| | **Filtro** | **Efecto** |
|---|---|---|
| Qué hace | Cambia el **color** de la imagen | Añade **algo** encima o deforma la imagen |
| Ejemplo | "Cine mudo", un look cálido, un B/N | Destellos, glitch, VHS, zoom pulsante, luces |
| Cómo se ve | Discreto, se aplica a todo | Notorio, llama la atención |
| Se usa | En todo el video o en bloques largos | En momentos puntuales |
| Se controla con | Un solo deslizador de intensidad | A veces varios parámetros |
| En el archivo del proyecto | pista `filter` | pista `effect` o dentro del segmento |

Regla de oro: **el filtro es el vestuario, el efecto es el gesto.** El vestuario es uno y dura todo el
video. El gesto se usa cuando hay algo que decir.

En la práctica real de tus 51 proyectos, la mezcla es exactamente esa: 9 pistas de tipo `filter`
contra apenas 2 de tipo `effect` como pista propia — la mayoría de los efectos van aplicados
directamente sobre segmentos.

---

## Cómo se aplica cada cosa

### Filtro

Tres formas, y cada una hace algo distinto:

1. **Pestaña *Filtros* → arrastrar a la línea de tiempo.** Crea una **pista de filtro** propia que
   afecta a todo lo que esté debajo, en el tramo que dure la pista. Es la mejor forma si querés un
   look para todo el video: lo estirás de punta a punta y listo.
2. **Clip seleccionado → panel derecho → *Filtros*.** Se aplica solo a ese clip.
3. **Panel *Ajustar*.** No es un filtro prehecho, son los controles manuales (exposición, contraste,
   saturación, temperatura, tono, luces, sombras, nitidez, viñeta). Va en su propia pista `adjust` si
   lo arrastrás, o dentro del clip si lo aplicás seleccionado.

**Consejo real:** casi siempre querés **pista de filtro estirada a todo el video, al 40–70 % de
intensidad**. Los filtros al 100 % casi siempre se ven baratos.

### Efecto

1. **Pestaña *Efectos* → *Efectos de video* → arrastrar a la línea de tiempo.** Crea una pista de
   efecto. Afecta a lo que esté debajo durante el tramo que dure.
2. **Pestaña *Efectos* → *Efectos de cuerpo*.** Detectan a la persona. Más pesados, menos confiables.
3. **Clip seleccionado → aplicar.** Se pega al clip y viaja con él si lo movés. **Esta es la forma
   que más te conviene** cuando el efecto pertenece a un momento específico del montaje: si después
   movés el corte, el efecto se mueve con él.

La diferencia entre "pista de efecto" y "efecto en el segmento" te va a morder cuando reordenes
clips. Pista de efecto = ancla al tiempo. Efecto en segmento = ancla al clip.

---

## Cómo está organizada la biblioteca

Las categorías que vas a ver arriba en el panel de *Efectos*:

- **Destacado** — lo que CapCut está empujando esta semana. Rota. Es donde vive lo "de moda".
- **Tendencias** — lo que está sonando en TikTok. Rota rápido.
- **Básico** — desenfoques, zooms, brillos. **Lo aburrido y lo que más vas a usar.**
- **Vlog / Vida** — cositas suaves, luces, partículas.
- **Retro / Vintage** — VHS, cassette, película rayada, grano.
- **Glitch / Distorsión** — cortes digitales, RGB split, ruido.
- **Luz / Bokeh** — destellos, halos, círculos desenfocados.
- **Fiesta / Música** — pulsos, estroboscopios, cosas que reaccionan al beat.
- **Texto / Divertido / Estación** — temáticos y estacionales.

**Cómo se ve por dentro.** Un efecto, en el archivo del proyecto, queda registrado así:

```json
{
  "name": "Bokeh",
  "effect_id": "7442221880838197777",
  "category_id": "25498",
  "category_name": "Destacado",
  "path": "C:/Users/user/AppData/Local/CapCut/User Data/Cache/effect/<id>/<hash>",
  "adjust_params": [],
  "apply_target_type": 0
}
```

Lo importante de eso, sin ser técnico:

- **`effect_id` es el nombre verdadero del efecto.** El nombre en español que ves en pantalla es solo
  una etiqueta que puede cambiar con el idioma o con una actualización. El id, no.
- **`path` apunta a una caché en tu disco.** La primera vez que usás un efecto, CapCut lo **descarga**
  a esa carpeta. De ahí en adelante ya está local. Esto es clave para el módulo 218.
- **`category_name`** te dice de dónde salió, y sirve para reencontrarlo.

Consecuencia práctica que casi nadie sabe: **si un efecto no está en tu caché, un proyecto que lo
pida no lo va a mostrar hasta que CapCut lo baje.** Y si CapCut lo retiró de la biblioteca, no lo baja
nunca. Efectos "de tendencia" desaparecen. Ver *Errores comunes*.

---

## La verdad sobre cuáles valen la pena

Vamos a mirar datos reales, no opiniones. En 51 proyectos tuyos aparecen **28 efectos distintos**,
pero la distribución de uso es brutalmente desigual:

| Efecto | Veces usado |
|---|---|
| Blanco y negro brillante | 32 |
| Badbunny | 24 |
| Noches de Río | 23 |
| Cassette defectuoso | 13 |
| Iluminar | 9 |
| …otros 23 efectos | 1–5 cada uno |

Leé eso otra vez. **Cinco efectos cargan con el 80 % del trabajo.** Los otros 23 son experimentos que
se usaron una o dos veces y nunca volvieron.

Eso no es un defecto. **Eso es un estilo.** Sin darte cuenta, ya construiste una paleta. Lo que sigue
es hacerla consciente.

### Por qué esos cinco funcionan

Fijate qué tienen en común los que sobrevivieron:

- **Blanco y negro brillante** — un cambio de *estado*. Sirve para marcar "antes / después", para un
  golpe seco, para un remate. No decora: **significa**.
- **Badbunny** y **Noches de Río** — luz y color con carácter. Dan atmósfera sin tapar la imagen.
- **Cassette defectuoso** — textura de "esto es un recuerdo / esto es imperfecto". También significa.
- **Iluminar** — subraya. Es un dedo apuntando.

Los que no sobrevivieron eran, casi con seguridad, efectos que se ven **espectaculares** pero no
**dicen** nada. Duran una moda.

### El criterio para elegir uno nuevo

Antes de meter un efecto a tu paleta, pasalo por estas tres preguntas:

1. **¿Qué significa?** Si la respuesta es "se ve chévere", no entra.
2. **¿Se va a ver igual de bien dentro de seis meses?** Si es de *Tendencias*, probablemente no.
3. **¿Lo puedo usar tres veces en la misma pieza sin cansar?** Si no, es un efecto de una sola bala.

---

## Construir tu paleta corta

Una paleta es **entre 4 y 8 efectos, más 1 o 2 filtros**, que usás en todo tu contenido. Nada más.

### Cómo se arma

**Paso 1 — Auditá lo que ya usás.** Abrí tus últimos 10 proyectos y anotá qué efectos aparecen. Los
que se repiten ya son tu paleta, aunque no lo hayas decidido.

**Paso 2 — Asigná una función a cada uno.** Esto es lo que convierte un efecto en gramática:

| Función en el montaje | Tu recurso |
|---|---|
| Look base de toda la pieza | *(un filtro, al 50 %)* |
| Golpe / cambio de estado | Blanco y negro brillante |
| Atmósfera nocturna / cálida | Noches de Río |
| Energía / momento alto | Badbunny |
| Recuerdo / textura imperfecta | Cassette defectuoso |
| Subrayar un dato | Iluminar |

Cuando tenés esa tabla, editar deja de ser "a ver qué efecto le pongo" y pasa a ser "acá necesito un
golpe → uso el de golpe". Es diez veces más rápido y el resultado es coherente.

**Paso 3 — Guardá la paleta donde la puedas recuperar.** CapCut te deja marcar favoritos (el corazón
en cada efecto). Hacelo. Además, anotá los nombres exactos en un archivo de texto en tu carpeta de
proyecto — porque si CapCut cambia el nombre traducido, el favorito te salva.

**Paso 4 — Armá un proyecto plantilla.** Un proyecto de CapCut con un clip de prueba y **cada uno de
los efectos de tu paleta ya aplicado una vez**. Eso hace dos cosas: (a) fuerza a que todos queden
descargados en tu caché, y (b) te da un archivo de proyecto del que podés copiar las referencias
exactas cuando generés drafts por código (módulo 218). Es la jugada más útil de este módulo entero.

---

## Intensidad: el error que más se nota

Casi todos los efectos y filtros de CapCut tienen un deslizador de intensidad, y casi todo el mundo lo
deja donde viene.

Regla práctica:

- **Filtro de color: 40–70 %.** Al 100 % se ve a filtro de app de fotos de 2014.
- **Efecto de textura (grano, VHS, cassette): 30–60 %.** La textura tiene que sentirse, no verse.
- **Efecto de golpe (B/N, flash, glitch fuerte): 100 %, pero corto.** 4 a 10 fotogramas. Si dura un
  segundo, ya no es golpe, es decoración.
- **Efecto de luz / bokeh: 20–50 %.** Es lo que más rápido se ve barato.

Y una regla más dura: **si dudás si el efecto está muy fuerte, está muy fuerte.**

---

## Duración: el segundo error que más se nota

Un efecto de pista se estira arrastrando sus bordes, igual que un clip. Nadie lo ajusta.

- Un efecto que dura **todo el video** ya no es un efecto, es parte de la imagen. Si eso querías,
  usá un filtro.
- Un efecto que dura **exactamente lo que dura un clip** se lee como decoración del clip.
- Un efecto que **empieza justo en el corte y dura 5 fotogramas** se lee como puntuación. Eso es lo
  que querés el 90 % de las veces.

Truco: poné el efecto **cruzando el corte** — que empiece 2 fotogramas antes del corte y termine 3
después. Disimula el corte y lo enfatiza al mismo tiempo.

---

## Efectos y ritmo: el vínculo que casi nadie hace

Los efectos no van "donde se ve bonito". Van **donde el audio manda**.

- En un golpe de música → efecto de golpe.
- En un cambio de tema en la voz en off → cambio de filtro o B/N breve.
- En el remate de un chiste → congelado + efecto.
- En un dato duro que decís → *Iluminar* + el texto entrando.

Si ponés los efectos sin mirar la forma de onda del audio, se van a sentir arbitrarios aunque sean
lindos. Ver módulo 217 para marcar el beat.

---

## Efectos de cuerpo y de rostro: la letra chica

CapCut tiene una familia aparte que detecta personas (siluetas, auras, deformaciones de cara). Cosas
que tenés que saber:

- **Son mucho más pesados.** La previsualización se traba y el render tarda más.
- **Fallan con poca luz, con la persona de espaldas o parcialmente tapada.** El aura parpadea.
- **Varios se procesan en la nube.** Necesitás internet, y tu material sube a servidores de ByteDance.
- **No los uses en el segundo 1 de un reel.** Si parpadea justo en el gancho, perdiste al espectador.

Úsalos cuando el sujeto está bien iluminado, de frente, y el plano es estable. Si no, olvidate.

---

## Errores comunes

- **Usar un efecto porque se ve chévere y no porque signifique algo.** Es la causa número uno de que
  un video "se sienta amateur" aunque esté bien cortado.
- **Dejar la intensidad en el valor por defecto.** Los valores por defecto están calibrados para que
  el efecto se note en la vista previa del catálogo, no para que se vea bien en tu pieza.
- **Confundir pista de efecto con efecto en el segmento.** Reordenás dos clips, y el efecto se queda
  donde estaba porque estaba anclado al tiempo, no al clip. Revisá siempre después de reordenar.
- **Apoyarse en efectos de *Tendencias*.** Rotan. En seis meses puede que ya no estén en la
  biblioteca, y un proyecto viejo que los pida no los va a poder bajar. Si un efecto es central en tu
  estilo, tiene que ser de una categoría estable (Básico, Retro), no de la vitrina de la semana.
- **Acumular 15 efectos distintos en una pieza de 40 segundos.** Ninguno significa nada porque todos
  compiten. Menos efectos, mejor colocados.
- **Poner filtro sobre filtro sobre ajuste.** Se te va el color y no sabés cuál fue. Un filtro, y los
  ajustes finos aparte.
- **Aplicar el filtro a cada clip por separado.** Es lento, y cuando querés cambiar el look tenés que
  tocar 40 clips. Usá **una** pista de filtro estirada.
- **Usar efectos de cuerpo en material oscuro o inestable.** Parpadea y se ve peor que no ponerle
  nada.
- **No dejar constancia de qué efectos usaste.** Seis meses después querés repetir el estilo y no te
  acordás del nombre. Anotalo.

---

## Checklist

- [ ] Sé la diferencia entre filtro (color, todo el video) y efecto (gesto, momento puntual).
- [ ] El look base va en **una** pista de filtro estirada, no clip por clip.
- [ ] Bajé la intensidad de todo lo que apliqué; nada quedó al valor por defecto sin pensarlo.
- [ ] Mi paleta tiene entre 4 y 8 efectos, y **cada uno tiene una función escrita**.
- [ ] Cada efecto que puse responde a algo del audio (un golpe, un cambio de tema, un remate).
- [ ] Los efectos de golpe duran menos de 10 fotogramas y cruzan el corte.
- [ ] Marqué mis efectos como favoritos **y** anoté sus nombres exactos en un archivo de texto.
- [ ] Tengo un proyecto plantilla con toda mi paleta aplicada, para que quede en caché y para poder
      copiar sus referencias cuando genere drafts por código.
- [ ] Ningún efecto central de mi estilo viene de la categoría *Tendencias*.
- [ ] Miré la pieza completa una vez sin tocar nada y me pregunté: ¿sobra algún efecto? (Sí. Siempre
      sobra al menos uno. Quitalo.)

# 175 — Continuidad en rodaje

**Qué resuelve:** que el material se pueda unir. El módulo `26` habla de cómo el editor **detecta y
tapa** los errores de continuidad cuando ya no se puede volver a grabar. Este habla de cómo **no
producirlos**, que es infinitamente más barato.

La idea central del módulo cabe en una frase: **se graba por locación, no por orden del guion.**

---

## 1. Qué se rompe cuando no hay continuidad

> **Continuidad:** que los elementos de la escena se mantengan coherentes de un plano al siguiente. Si
> en la toma A tiene la manga arremangada, en la toma B sigue arremangada.

El espectador no lleva una lista mental. Lo que hace su cerebro es peor: registra la inconsistencia sin
identificarla y la traduce en **"esto no me convence"**. En un video de ventas eso se paga en
desconfianza, y nadie te va a saber decir por qué no le gustó.

**En video de redes en 2026, la continuidad importa menos que en cine.** El jump cut es aceptado y hasta
esperado. Pero hay tres tipos de error que **siguen doliendo mucho** y de esos trata este módulo:

1. **La luz** — el más grave, casi no se arregla
2. **El audio de fondo** — se oye más de lo que se ve un cambio de camisa
3. **La ropa y el aspecto** — cuando el cambio es dentro de la misma frase

---

## 2. El error del rodaje real: la misma frase en tres sitios

Rodaje verdadero, bar-restaurante, agosto de 2026. La misma frase del guion se grabó en:

- El **pasillo** con neón morado
- La **barra**, con bombillos cálidos
- La **terraza**, a plena luz del día

Cada toma, por separado, se veía bien. El problema apareció en el montaje.

**Qué hace el editor con las tomas de una frase:** las alterna. Toma 1 hasta la palabra 5, toma 3 desde
la palabra 6, toma 2 para el remate. Eso es montaje normal: se arma la mejor versión de la frase
juntando pedazos de varias tomas (`14`, `23`).

**Qué pasó al hacerlo:** cada corte era un salto de luz brutal. Morado → ámbar → azul de mediodía en
medio segundo. La cara cambiaba de color, el fondo cambiaba de mundo, y el video se veía roto.

**Por qué no se arregló:** emparejar planos (`62`) funciona con diferencias de grado — un plano un poco
más frío, otro un poco más contrastado. **No funciona** con luces de naturaleza distinta. Para llevar la
cara morada del pasillo al mismo sitio que la cara de la terraza habría que inventar información que no
se grabó.

**Consecuencia real:** el editor tuvo que usar solo el material de una locación y descartar el resto. Dos
tercios del rodaje se perdieron.

> **La regla que sale de ahí:**
> **Una frase = una locación.** Se decide antes de grabar. No se cambia.

La variedad de sitios se pone **entre frases**, no dentro de una frase. Frase 1 en la barra, frase 2 en
la terraza, frase 3 en el pasillo: eso sí funciona, porque el corte entre frases se lee como cambio de
escena y el ojo lo acepta con gusto (le da variedad al video, que es lo que se buscaba).

---

## 3. Agrupar por locación: el método

Esta es la diferencia entre un rodaje que sale en 40 minutos y uno que sale en 3 horas y no se puede
montar.

**Como lo hace todo el mundo (mal): en orden de guion**

```
Frase 1 → barra
Frase 2 → terraza      ← se mueven todos
Frase 3 → barra        ← se mueven todos otra vez
Frase 4 → pasillo      ← y otra vez
Frase 5 → terraza      ← y otra
```

Cada movimiento significa: reencuadrar, volver a bloquear exposición y foco, la luz del sol ya cambió, el
ruido de fondo es otro. Y como se vuelve a la barra dos veces, **la barra de la frase 1 no se ve igual
que la barra de la frase 3** (pasó una hora).

**Como se hace bien: por locación**

```
BLOQUE BARRA     → frases 1 y 3  + b-roll de barra + ambiente puro
BLOQUE TERRAZA   → frases 2 y 5  + b-roll de terraza + ambiente puro
BLOQUE PASILLO   → frase 4       + b-roll de pasillo + ambiente puro
```

**Lo que se gana:**

- Una sola configuración de luz, exposición y foco por bloque
- Los planos de un bloque son intercambiables entre sí (misma luz, mismo color, mismo sonido)
- Se graba mucho más rápido: no hay tiempo muerto de traslado
- El editor tiene bloques coherentes que puede emparejar en un solo paso (`62`)
- El ambiente puro de cada sitio (`172`) sirve para todo el bloque

**La hoja de rodaje sale así:**

| Bloque | Locación | Frases | B-roll a grabar aquí | Ambiente puro |
|---|---|---|---|---|
| 1 | Barra | 1, 3, 7 | destape, servido, detalle vaso, manos | ✅ 5 s |
| 2 | Terraza | 2, 5 | mesa, gente, fachada, ambiente | ✅ 5 s |
| 3 | Pasillo neón | 4 | neón, caminata, textura pared | ✅ 5 s |

**Y no se vuelve.** Cuando se cierra el bloque 1, se cierra. Si después falta algo de la barra, se graba
en un bloque nuevo asumiendo que **no va a coincidir** con el primero — y el editor lo trata como
material distinto.

---

## 4. Los cinco tipos de continuidad, ordenados por cuánto duelen

### 1) Luz — 🔴 crítica, casi no se arregla

Ya cubierta arriba. Reglas de rodaje:

- Todo lo de un sitio, **seguido**. El sol se mueve: la luz de las 10 no es la de las 2.
- **Bloquear exposición y balance de blancos** (`171`) para todo el bloque, no plano a plano.
- Si el rodaje se parte en dos días, **anota la hora** de cada bloque y trata de repetirla.
- Un día **nublado es mejor** que uno soleado: la luz no cambia.

**Cómo lo mide el editor después:**

```bash
# Brillo promedio de cada bloque
ffmpeg -hide_banner -i bloque_barra.mp4 -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG" \
  -f null - 2>&1 | head -3
```

Si un bloque da 118 y otro 76, hay un salto de exposición fuerte. Menos de 10 puntos de diferencia es
zona sana.

### 2) Audio de fondo — 🔴 crítica, se oye mucho

El cambio de ruido ambiente entre cortes se nota **más** que un cambio visual. Si una toma tiene la
nevera zumbando y la siguiente no, el corte se oye.

Reglas:
- **Mismo ruido de fondo dentro de un bloque**: no apagues la nevera a mitad de bloque.
- **5 segundos de ambiente puro por locación** (`172`): es la herramienta que le permite al editor poner
  una cama continua debajo de todo y borrar los saltos.
- Si hay música del local (que no debería, `172`), **jamás** dentro de una misma frase, porque la canción
  va en su tiempo y cada corte salta a otro punto de la melodía.

### 3) Ropa y aspecto — 🟠 importante dentro de una frase, tolerable entre escenas

Manga arremangada, delantal puesto/quitado, pelo, gorra, un botón, gafas.

- **Foto de referencia** con el celular al empezar cada bloque. Es lo que hace un equipo de cine con la
  "continuista", y aquí cuesta 2 segundos.
- Si la persona se quita el delantal para descansar, **se lo vuelve a poner igual**.
- Entre escenas distintas del video, cambiar de ropa **es una ventaja**: le dice al espectador "esto es
  otro momento".

**Cómo lo revisa el editor sobre el bruto:**

```bash
# Grilla de fotogramas: uno cada 2 segundos de toda la toma
ffmpeg -hide_banner -i toma_completa.mp4 -vf "fps=0.5,scale=200:-1,tile=8x6" -frames:v 1 revision.png
```

Un vistazo y los cambios de aspecto saltan.

### 4) Posición y encuadre — 🟠 importante

Si la persona está a la izquierda del cuadro en una toma y a la derecha en la siguiente, el corte da un
brinco.

- **Marca el piso.** Cinta, una servilleta, la pata de una silla. La persona vuelve exactamente al mismo
  punto.
- **Marca el celular.** Si está en trípode, no lo muevas dentro del bloque. Si está apoyado, deja el
  apoyo puesto.
- Si vuelves a grabar una frase después de descansar, **revisa la última toma** antes de repetir.

### 5) Props y objetos — 🟡 menor, pero se ve

El vaso lleno en una toma y medio vacío en la siguiente. La botella que cambió de lado de la mesa.

- Fotografía el "set" antes de empezar.
- **Cuidado especial con las bebidas:** la espuma baja, el hielo se derrite. Si vas a grabar la copa
  llena varias veces, prepara varias copas o rellénala igual cada vez.
- Lo que está **en la mano o en primer plano** importa. Lo del fondo, casi nunca lo ve nadie.

---

## 5. El eje: la única regla de cine que sí hay que respetar

> **Cruzar el eje:** si en una toma la persona mira hacia la derecha del cuadro y en la siguiente mira
> hacia la izquierda, el espectador siente que "cambió de lado" y se desorienta.

Con una sola persona hablando a cámara casi no aplica. Aplica cuando:

- Hay **dos personas hablando** (entrevista, brindis, atención al cliente)
- Hay un **corte por mirada**: alguien mira algo, y luego se ve lo que mira

**La regla práctica:** imagina una línea entre las dos personas (o entre la persona y lo que mira). La
cámara se queda **siempre de un solo lado de esa línea**. Puedes acercarte, alejarte, subir, bajar — pero
no cruzar al otro lado.

Si se cruza, el editor tiene un parche feo: espejar el plano con `hflip`. Y eso solo funciona si **no hay
texto ni logos en cuadro**, porque quedan al revés.

---

## 6. Lo que sí puede cambiar sin problema (para no volverse loco)

Hay gente que se paraliza con la continuidad. Esto es lo que **no** importa en video vertical de redes:

- La silla del fondo que se movió
- El vaso de otra mesa
- La gente que pasa por atrás (siempre y cuando no sea la misma persona pasando dos veces)
- Una sombra que cambió un poco
- Que la persona parpadee en distinto momento
- El jump cut visible entre dos tomas de la misma frase — **en 2026 eso es lenguaje, no error** (`21`)

**Dónde va el esfuerzo:** luz, audio de fondo, y lo que la persona tiene puesto o en la mano. Lo demás es
tiempo que se le quita al gancho (`30`).

---

## 7. Las herramientas de continuidad que cuestan cero

**La foto de referencia.** Al empezar cada bloque, una foto de la persona de cuerpo entero y una del set.
Se guardan en el mismo álbum. Si hay que volver a grabar mañana, esa foto vale oro.

**La claqueta de pobre.** Antes de cada toma, alguien dice en voz alta: "bloque 2, terraza, frase 5,
toma 3". Queda en el audio, aparece en la transcripción (`13`) y el editor sabe exactamente qué es cada
cosa sin abrir los archivos.

**La marca en el piso.** Cinta de enmascarar en forma de T donde van los pies. Vale $3.000 y resuelve la
continuidad de posición para siempre.

**La libreta.** Tres columnas: bloque, qué se grabó, qué faltó. Cinco minutos al final del rodaje
revisándola evita el "se nos olvidó grabar el remate".

**No apagar el celular entre tomas del mismo bloque.** Si se apaga y se vuelve a abrir la cámara, el
bloqueo de exposición y balance se pierde y el bloque deja de ser homogéneo.

---

## 8. Cuando hay que grabar en dos días

A veces no queda de otra. Reglas para que el material del día 2 pegue con el del día 1:

1. **Misma hora del día.** Si el día 1 fue a las 10 a.m., el día 2 a las 10 a.m. La luz de ventana es
   otra a las 3 p.m.
2. **Misma ropa.** Foto de referencia del día 1 en la mano.
3. **Mismo celular y mismos ajustes.** Anota resolución, fps y balance de blancos.
4. **Misma posición.** Foto del set del día 1.
5. **Ambiente puro otra vez.** El ruido del sitio no es el mismo dos días distintos.
6. **Avísale al editor.** Que sepa qué es de qué día para poder emparejar por bloques.
7. **Asume que va a haber diferencia** y planea el montaje para que los dos días no se toquen dentro de
   la misma frase. Día 1 = primera mitad del video. Día 2 = segunda mitad.

---

## Errores comunes

1. **Grabar en orden de guion.** Es el error madre del bloque. Produce saltos de luz que no se arreglan y
   alarga el rodaje. Se graba **por locación**.
2. **Grabar la misma frase en tres sitios distintos.** Pasó de verdad y costó dos tercios del rodaje. Una
   frase, una locación.
3. **Volver a una locación después de haberla cerrado.** La luz ya cambió. Si no queda de otra, trátalo
   como material nuevo y no lo mezcles dentro de la misma frase.
4. **Repartir un bloque a lo largo del día.** El sol se mueve. Todo lo de un sitio, seguido.
5. **Apagar la cámara entre tomas del mismo bloque.** Se pierde el bloqueo de exposición y foco y el
   bloque deja de ser homogéneo.
6. **No marcar el piso.** La persona vuelve a un sitio ligeramente distinto y el corte brinca.
7. **Olvidar la foto de referencia de ropa y set.** Es lo único que te salva si hay que volver a grabar.
8. **Cambiar el ruido de fondo a mitad de bloque** (apagar la nevera, prender el extractor). El salto se
   oye más que un cambio visual.
9. **No grabar ambiente puro por locación.** Sin esa cama, todos los saltos de audio quedan expuestos.
10. **Obsesionarse con la silla del fondo.** Nadie la ve. El esfuerzo va a luz, audio y lo que está en la
    mano.
11. **Cruzar el eje en una escena de dos personas.** El entrevistado "cambia de lado" en cada corte y el
    espectador se desorienta sin saber por qué.
12. **Grabar el segundo día a otra hora.** Misma hora, misma ropa, mismos ajustes, o el material no pega.
13. **No decir "bloque X, toma Y" en voz alta.** Sin claqueta, el editor pierde media hora ordenando
    archivos que no sabe de dónde salieron.

---

## Checklist

- [ ] El plan de rodaje está **ordenado por locación**, no por orden del guion.
- [ ] **Cada frase del guion tiene asignada UNA sola locación**, decidida antes de grabar.
- [ ] Cada bloque incluye: frases + b-roll de ese sitio + **5 s de ambiente puro**.
- [ ] Todo lo de una locación se graba **seguido**, sin repartirlo durante el día.
- [ ] **Exposición, foco y balance de blancos bloqueados** para todo el bloque, sin apagar la cámara.
- [ ] Hay **marca en el piso** para la posición de la persona.
- [ ] Hay **foto de referencia** de la ropa y del set al empezar cada bloque.
- [ ] Se dice en voz alta **"bloque, locación, frase, toma"** antes de cada intento.
- [ ] El **ruido de fondo no cambia** dentro de un bloque (nevera, extractor, aire).
- [ ] Los **props en primer plano** se mantienen coherentes (nivel del vaso, espuma, hielo).
- [ ] **No se cruzó el eje** en escenas con dos personas o con corte por mirada.
- [ ] Si hubo que volver a una locación, quedó **anotado** y el editor lo sabe.
- [ ] Si el rodaje se parte en dos días: **misma hora, misma ropa, mismos ajustes, mismo sitio**.
- [ ] Se revisó la **libreta de rodaje** antes de irse: qué se grabó, qué faltó.
- [ ] El editor midió el **YAVG por bloque** y ninguno difiere más de ~10 puntos.

# 204 — Composición en capas avanzada

**Qué resuelve:** ya sabes superponer (`80`) y ya sabes recortar el fondo (`81`). Pero cuando pones el
gráfico encima del video, **se ve pegado**. Como una calcomanía. Nítido de más, plano de más, ajeno.
Este módulo es sobre la diferencia entre poner algo **encima** de un plano y meterlo **dentro** de un
plano, que es lo que separa un video con stickers de un video compuesto.

---

## 1. El modelo de las cuatro capas

Deja de pensar "el video y las cosas que le puse encima". Piensa que cada plano tuyo tiene **cuatro
niveles**, cada uno con un trabajo distinto:

```
CAPA 4  TEXTO          lo que hay que leer
CAPA 3  GRAFICO        lo que hay que ver (flechas, marcos, personaje, logo)
CAPA 2  SUJETO         lo que hay que mirar (la persona, la cerveza, el plato)
CAPA 1  FONDO          donde pasa (el bar, la pared, la calle)
```

Lo importante no es el orden — eso es obvio — sino **que cada capa tenga un dueño y una función**. La
mayoría de los videos amateur tienen dos capas: "video" y "cosas". Cuando separas en cuatro, empiezan
a pasar cosas útiles:

| Capa | Su único trabajo | Qué la arruina |
|---|---|---|
| **Fondo** | dar contexto y contraste | estar tan cargado que compite con el sujeto |
| **Sujeto** | ser lo que se mira | estar tapado por el gráfico o el texto |
| **Gráfico** | señalar, marcar, reaccionar | estar tan nítido que se ve pegado |
| **Texto** | ser legible sin sonido | ocupar la zona del sujeto |

**La regla de oro de las cuatro capas:**

> Ninguna capa puede hacer el trabajo de otra. Si tu texto está explicando lo que el sujeto ya muestra,
> sobra. Si tu gráfico está donde está el sujeto, tapa. Si tu fondo tiene más movimiento que el sujeto,
> la gente mira el fondo.

---

## 2. El orden de render: por qué importa de verdad

En cualquier editor, las capas se dibujan de abajo hacia arriba. Lo de arriba tapa lo de abajo. Hasta
ahí, obvio. Lo que casi nadie usa es la consecuencia:

**Los efectos también tienen orden, y ese orden cambia el resultado.**

Ejemplo concreto. Tienes un plano de la barra, le pones "Blanco y negro brillante" y encima pones tu
logo dorado.

- Si el efecto está **en la capa del fondo**: el fondo queda en blanco y negro, el logo sigue dorado.
  El logo se ve pegado encima, como stickers en un cuaderno.
- Si el efecto está **aplicado al conjunto** (en CapCut: sobre una pista de ajuste que cubre todo,
  o exportando y volviendo a entrar): el logo también se pone en blanco y negro. Ahora el logo
  **pertenece a la imagen**.

Las dos opciones son válidas y significan cosas distintas:

| Quieres que el gráfico… | Aplica el efecto… |
|---|---|
| destaque, sea claramente un elemento gráfico | solo al fondo |
| **pertenezca a la escena**, se sienta filmado | a todo el conjunto, gráfico incluido |

Con tu paleta de efectos esto es directamente accionable. "Blanco y negro brillante" (32 usos),
"Noches de Río" (23) y "Cassette defectuoso" (13) son efectos **de imagen completa**. Si tienes un
gráfico o un texto que quieres que se sienta parte del plano, tiene que recibir el mismo efecto. Si lo
dejas fuera, se nota inmediatamente aunque nadie sepa decir por qué.

**Cómo se hace en CapCut sin volverse loco:** los efectos que aplicas a la pista de efectos afectan a
todo lo que está por debajo de esa pista. Entonces:

- Gráfico **debajo** de la pista de efectos → recibe el efecto → pertenece a la escena.
- Gráfico **encima** de la pista de efectos → no lo recibe → destaca como elemento gráfico.

Es una decisión de un arrastre, y casi nadie la toma conscientemente.

**Excepción importante:** el texto de información (precio, dirección, horario) **nunca** recibe el
efecto. Un precio en blanco y negro sobre "Cassette defectuoso" no se lee, y ese texto existe para
leerse. La información va siempre arriba de todo, limpia.

---

## 3. Las seis cosas que hacen que un gráfico "viva" en la escena

Aquí está el corazón del módulo. Un gráfico se ve pegado porque le faltan las propiedades que tiene
todo lo que fue filmado. Estas seis, en orden de rendimiento:

### 3.1. Color — la más importante

Tu video tiene una dominante de color. Un bar de noche es ámbar y ligeramente verde. Tu gráfico salió
de un programa de diseño y es de un color puro, sin dominante ninguna. El ojo lo detecta al instante.

**El arreglo:** dale al gráfico una pizca del color del ambiente. Baja la saturación un 10–20% y
súbele la temperatura hacia donde va el plano.

```bash
ffmpeg -i base.mp4 -i grafico.png -filter_complex "\
[1:v]format=rgba,colorbalance=rs=0.06:gs=0.01:bs=-0.05,eq=saturation=0.85[g];\
[0:v][g]overlay=x=W-w-70:y=H*0.68" \
  -map 0:a -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

Ese `colorbalance` empuja los medios hacia cálido y quita azul: mete el gráfico en la luz del bar. En
CapCut es el panel de **Ajustar** aplicado al clip del gráfico: temperatura +8, saturación -12.

### 3.2. Nitidez — el gráfico está demasiado perfecto

Tu video, grabado con celular y comprimido por WhatsApp o por Instagram, tiene bordes blandos. Tu PNG
tiene bordes matemáticamente perfectos. Esa diferencia grita "pegado".

**El arreglo:** un desenfoque de medio píxel. Uno solo. No se ve, pero cambia todo.

```bash
[1:v]format=rgba,gblur=sigma=0.5[g]
```

En CapCut no hay control tan fino; lo más cercano es escalar el gráfico al 99% desde un tamaño mayor,
que ablanda ligeramente los bordes.

### 3.3. Grano — el gráfico está demasiado limpio

Un video real tiene ruido, sobre todo grabado de noche en un bar. Un gráfico no tiene ninguno. Añadir
un poco de grano **al conjunto** (no solo al gráfico) une todo bajo la misma textura:

```bash
ffmpeg -i compuesto.mp4 -vf "noise=alls=6:allf=t+u" \
  -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p final.mp4
```

`alls=6` es sutil; por encima de 12 ya se ve sucio. Es el paso final, después de todo lo demás.

### 3.4. Sombra — el gráfico no proyecta nada

Todo lo que existe en un espacio con luz proyecta algo. Una sombra suave y muy leve debajo del gráfico
lo asienta en la escena.

**Los números:** desplazamiento de 4–10 píxeles hacia abajo, desenfoque grande (12–25 px), opacidad
baja (20–35%). Si ves la sombra conscientemente, está muy fuerte.

En CapCut, el panel de texto tiene sombra directa. Para gráficos, se hace duplicando el PNG, poniéndolo
debajo, oscureciéndolo a negro, desenfocándolo y bajándole la opacidad.

> **Ojo con tu estilo de texto.** Tus textos van con **contorno y sin sombra**, y eso es correcto para
> subtítulos: el contorno los salva sobre cualquier fondo y la sombra los ensuciaría. La sombra de esta
> sección es para **gráficos e ilustraciones**, no para tus subtítulos.

### 3.5. Oclusión — algo de la escena debería taparlo

Este es el truco caro que cuesta poco y es el que de verdad hace decir "¿cómo hizo eso?".

La idea: si el gráfico está *dentro* de la escena, algo de la escena tiene que pasar **por delante**.
La mano que sirve la cerveza tapa parcialmente el número que pusiste.

Cómo se hace sin software costoso:

1. Pon el gráfico en su capa.
2. **Duplica el plano de video** y ponlo en una capa **encima** del gráfico.
3. En esa copia de arriba, recorta con máscara solo la parte que debe tapar (la mano, la botella, el
   hombro).
4. Resultado: el gráfico queda entre el fondo y ese pedazo del sujeto.

Es tedioso si el objeto se mueve mucho (ahí entra `205`), pero cuando el objeto está casi quieto, son
cinco minutos y el efecto es desproporcionado.

**Dónde vale la pena:** una sola vez por video, en el momento importante. Nunca en todos los gráficos.

### 3.6. Movimiento compartido — si la cámara tiembla, el gráfico también

Si tu plano fue grabado en mano, la imagen tiene un temblor leve permanente. Un gráfico
perfectamente inmóvil encima de una imagen que tiembla se despega inmediatamente.

**El arreglo barato:** ponle al gráfico un loop de flotación mínimo (`202`): 4–8 píxeles, ciclo lento.
No imita el temblor real, pero rompe la inmovilidad absoluta y ya no se lee como calcomanía.

**El arreglo bueno:** estabiliza el plano primero. Si el fondo está quieto, el gráfico quieto encima ya
no molesta.

---

## 4. La zona segura por capa

Cada capa tiene un territorio distinto en el cuadro vertical (1080 × 1920). Respetarlo evita el 90% de
los problemas de composición.

```
0    - 250 px   ZONA MUERTA SUPERIOR
                la tapan el usuario, el nombre de cuenta, la interfaz
                aqui NO va nada que importe

250  - 700 px   ZONA DE GRAFICO
                aqui viven marcos, flechas, datos, el personaje
                el sujeto casi nunca esta aqui

700  - 1450 px  ZONA DEL SUJETO
                la cara, las manos, el producto
                aqui NO se pone texto NUNCA

1450 - 1650 px  ZONA DE TEXTO
                los subtitulos viven aqui
                es la franja mas legible del formato

1650 - 1920 px  ZONA MUERTA INFERIOR
                la tapan el pie de foto, los botones, el usuario
                aqui NO va nada que importe
```

**El error de composición número uno en vertical:** poner los subtítulos demasiado abajo. Se los come
la interfaz de Instagram o TikTok y tú nunca lo ves porque los revisas en el editor, no en la app.

**El segundo error:** poner el gráfico en la zona del sujeto porque "ahí hay espacio vacío". Ese
espacio vacío no está vacío: es el aire alrededor de la cara, y es lo que hace legible la cara.

---

## 5. La jerarquía de atención: solo una cosa gana

En cada segundo de tu video, **exactamente una capa tiene que ser la protagonista**. Las otras tres se
subordinan.

| Momento | Protagonista | Las demás |
|---|---|---|
| Gancho | sujeto | fondo neutro, sin gráfico, sin texto o una palabra |
| Explicación | texto | sujeto sigue, gráfico ausente |
| Golpe visual | gráfico | texto desaparece un instante |
| Dato duro | texto | todo lo demás se apaga u oscurece |
| Cierre | marca | lo demás se detiene |

**La herramienta más potente para forzar jerarquía es apagar, no encender.** Cuando quieres que el
precio se lea, no lo hagas más grande: **oscurece el fondo un 30% y baja el sujeto de contraste**. El
precio gana sin cambiar de tamaño.

```bash
ffmpeg -i base.mp4 -filter_complex "\
[0:v]eq=brightness=-0.12:saturation=0.6:enable='between(t,18.0,21.0)'[bg]" \
  -map "[bg]" -map 0:a -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

Durante los tres segundos del cierre, todo el plano se apaga un poco. El texto que va encima,
limpio y a color, se lee sin esfuerzo. Es un truco de teatro: no iluminas al actor, apagas la sala.

---

## 6. Disciplina de pistas

Un proyecto con quince pistas desordenadas es un proyecto que no vas a poder repetir la semana que
viene. La estructura que se sostiene:

```
PISTA 6   texto de informacion (precio, direccion) -- limpio, sin efectos
PISTA 5   subtitulos
PISTA 4   efectos globales (blanco y negro, cassette, etc.)
PISTA 3   graficos, personaje, marcos, logo
PISTA 2   b-roll y superposiciones
PISTA 1   plano principal
```

Con esa estructura, la decisión de la sección 2 se vuelve mecánica: el gráfico está en la pista 3, o
sea **debajo** del efecto global, o sea que pertenece a la escena. El texto de información está en la
6, **encima** del efecto, o sea que se lee siempre.

**La regla que ahorra horas:** una pista, un tipo de contenido. Nunca mezcles subtítulos y gráficos en
la misma pista aunque haya espacio. El día que quieras cambiar todos los subtítulos, vas a agradecerlo.

---

## Errores comunes

1. **Pensar en dos capas ("video" y "cosas") en vez de cuatro.** Todo lo demás del módulo depende de
   este cambio.
2. **Dejar el gráfico fuera del efecto global.** Si todo el plano está en blanco y negro y tu logo
   está a color, se ve pegado. Decide conscientemente de qué lado de la pista de efectos va.
3. **Meter el texto de información dentro del efecto.** Un precio en "Cassette defectuoso" no se lee.
   La información va arriba de todo, limpia.
4. **Gráfico con color puro sobre un plano con dominante.** Bájale saturación y súbele temperatura
   hacia la del plano.
5. **Bordes matemáticamente perfectos.** Medio píxel de desenfoque y deja de gritar "PNG".
6. **Sombra visible.** Si la ves conscientemente, está al doble de lo que debería.
7. **Poner sombra a los subtítulos.** Tu estilo es contorno sin sombra y es el correcto. La sombra es
   para gráficos.
8. **Texto en la zona del sujeto.** Ese aire alrededor de la cara no está vacío, es lo que hace
   legible la cara.
9. **Subtítulos por debajo de 1650 px.** Se los come la interfaz de la app y tú no lo ves en el editor.
10. **Algo importante arriba de 250 px.** Lo tapa el nombre de cuenta.
11. **Dos protagonistas en el mismo segundo.** Texto grande + gráfico entrando = nadie ve ninguno.
12. **Hacer más grande el elemento que quieres destacar.** Es mejor apagar lo demás.
13. **Gráfico perfectamente inmóvil sobre plano en mano.** Se despega. Loop leve o estabiliza el plano.
14. **Oclusión en todos los gráficos.** Es una jugada por video. Diez oclusiones es una tarde perdida.
15. **Mezclar tipos de contenido en la misma pista.** Se paga caro el día de la corrección.

---

## Checklist

Antes de dar por buena la composición de un plano:

- [ ] Puedo nombrar **quién ocupa cada una de las cuatro capas** en este plano.
- [ ] Solo **una capa es protagonista** en este segundo; las otras tres se subordinan.
- [ ] Decidí conscientemente si el gráfico va **debajo o encima** de la pista de efectos.
- [ ] El **texto de información** está limpio, arriba de todo, sin efecto de imagen encima.
- [ ] El gráfico tiene la **dominante de color** del plano (saturación bajada, temperatura ajustada).
- [ ] El gráfico tiene **medio píxel de desenfoque** o equivalente, no bordes perfectos.
- [ ] Si hay sombra, **no la veo conscientemente**.
- [ ] Nada importante está arriba de **250 px** ni abajo de **1650 px**.
- [ ] Ningún texto invade la **zona del sujeto** (700–1450 px).
- [ ] Si el plano es en mano, el gráfico **no está perfectamente inmóvil**.
- [ ] Para el dato duro, **apagué el fondo** en vez de agrandar el texto.
- [ ] Las pistas están ordenadas por tipo de contenido, **una pista un tipo**.
- [ ] Si usé oclusión, es **una sola vez** en el video y en el momento que importa.
- [ ] Revisé el resultado **en el celular, dentro de la app**, no solo en el editor.

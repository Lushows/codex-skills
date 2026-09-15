# 206 — Tipografía en movimiento avanzada

**Qué resuelve:** tu texto ya funciona. Palabras sueltas, tamaño 15, contorno, sin sombra: es la
configuración correcta para vertical y no hay que tocarla. Este módulo es sobre lo que viene después
del subtítulo que aparece y desaparece — **cuatro técnicas de texto animado que se ven caras y no
cuestan casi nada**: el revelado por máscara, el texto que se escribe, el texto que responde al audio y
el texto que se sale del cuadro.

No son adornos: cada una resuelve un problema distinto de lectura.

---

## 1. Por qué tu base ya es correcta (y por qué importa)

Antes de agregar nada, vale la pena entender por qué lo que ya haces funciona, porque todo lo demás se
construye encima.

**Palabras sueltas.** El ojo lee una palabra corta de un vistazo, sin movimiento sacádico. Dos palabras
ya obligan a barrer. En un plano que dura 1,2 segundos, ese barrido es la diferencia entre leer y no
leer.

**Contorno sin sombra.** El contorno garantiza legibilidad sobre cualquier fondo: pared clara, madera
oscura, cerveza ámbar, todo. La sombra sola falla sobre fondos oscuros y, combinada con contorno,
ensucia la forma de la letra. Tu decisión es la correcta y no depende del gusto: es física de la
lectura.

**Tamaño 15 (en la escala de CapCut).** Es un tamaño donde una palabra corta ocupa aproximadamente
entre el 40% y el 60% del ancho del cuadro. Ese es el rango donde el texto es protagonista sin tapar
la cara.

> **La única regla dura de tipografía en vertical:** si tienes que entrecerrar los ojos para leerlo en
> un celular a un brazo de distancia, está mal, sin importar lo bonito que se vea en el monitor.

Lo que sigue son técnicas de **énfasis**. Se usan en 2 o 3 momentos de un reel, no en los subtítulos
completos.

---

## 2. Revelado por máscara: el que más se nota y menos cuesta

> **Revelado por máscara:** el texto no aparece ni crece — se **descubre**, como si una cortina se
> corriera. El texto ya está completo detrás; lo que se mueve es lo que lo tapa.

Es la animación de texto que más lee como "producción cara" y es una de las más simples. Se usa para
títulos, nombres, el cierre de marca. **Nunca para subtítulos**: es demasiado lenta.

### Las cuatro direcciones y qué significan

| Dirección | Se siente | Para qué |
|---|---|---|
| **De izquierda a derecha** | natural, sigue la lectura | títulos, nombres. El valor seguro |
| **De abajo hacia arriba** | el texto "sube", tiene peso | precios, cifras, cierres |
| **Desde el centro hacia los lados** | simétrico, ceremonioso | logo, cierre de marca |
| **De derecha a izquierda** | incómodo, va contra la lectura | casi nunca |

### Cómo se hace en CapCut

CapCut no tiene "máscara de texto" como tal, pero tiene dos caminos:

**Camino A — con la animación de entrada.** Busca en las animaciones de entrada de texto las que se
llaman de tipo *barrido*, *cortina*, *revelado* o *máquina de escribir*. Varias son máscaras aunque no
lo digan.

**Camino B — el manual, que se ve mejor.** Pon el texto. Encima de él, en otra pista, pon un
rectángulo de color (una forma o un fondo sólido) que lo tape completamente. Anima ese rectángulo con
dos keyframes de posición para que se corra y descubra el texto. Ese rectángulo, si es del color de tu
marca, deja además una barra de color un instante: es el detalle que hace que se vea de estudio.

### Cómo se hace en ffmpeg

La máscara es un `crop` animado sobre una capa de texto pre-renderizada. La forma limpia:

```bash
ffmpeg -f lavfi -i color=black@0:s=1080x260:d=6,format=rgba \
  -vf "drawtext=fontfile=/ruta/fuente.ttf:text='BENDITA POLA':fontsize=96:\
fontcolor=white:borderw=6:bordercolor=black:x=(w-tw)/2:y=(h-th)/2" \
  -c:v qtrle titulo.mov
```

Eso te deja el texto con alfa en `titulo.mov`. Ahora el revelado, que es recortar cada vez más ancho:

```bash
ffmpeg -i base.mp4 -i titulo.mov -filter_complex "\
[1:v]crop=w='min(iw, iw*clip((t-2.0)/0.55,0,1))':h=ih:x=0:y=0[rev];\
[0:v][rev]overlay=x=0:y=H*0.42:enable='between(t,2.0,6.0)'" \
  -map 0:a -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

El `crop` va de ancho 0 a ancho completo en 0,55 segundos. Es un revelado de izquierda a derecha
lineal; para que quede con carácter, cámbialo por una curva:

```
w='min(iw, iw*(1-pow(1-clip((t-2.0)/0.55,0,1),3)))'
```

Ahora arranca rápido y frena, que es como se corre una cortina de verdad.

**Los números que funcionan:** duración de 0,45 a 0,7 segundos para una línea de texto. Más rápido no
se aprecia; más lento y el espectador se impacienta.

---

## 3. Texto que se escribe

> **Máquina de escribir:** las letras van apareciendo una por una, como si alguien las tecleara.

Tiene mala fama porque se abusa de él. Bien usado, sirve para dos cosas muy concretas:

1. **Simular un mensaje.** Una reseña de un cliente, un WhatsApp, un comentario. Ahí es literal y
   funciona.
2. **Sostener una frase larga que no cabe en una palabra suelta.** El texto que se escribe le da al ojo
   una razón para quedarse mirando el mismo sitio varios segundos.

**Los números:** entre **18 y 30 caracteres por segundo**. Más lento se vuelve insoportable; más
rápido no se lee como escritura sino como parpadeo. Para una frase de 40 caracteres, eso son 1,5 a 2,2
segundos.

**El detalle que lo salva:** el cursor. Una barra vertical que parpadea al final y **desaparece cuando
termina la frase**. Sin cursor se ve como una animación; con cursor se ve como alguien escribiendo. Y
si dejas el cursor parpadeando después de terminar, se ve como que el video se colgó.

En ffmpeg, el truco es usar `text` con una subcadena calculada por tiempo. La forma más robusta es
generar un archivo con las líneas por tiempo (`106`) o encadenar `drawtext` con `enable`, uno por cada
estado del texto. Es feo pero es fiable:

```bash
ffmpeg -i base.mp4 -vf "\
drawtext=fontfile=f.ttf:text='ABI':fontsize=72:fontcolor=white:borderw=5:x=90:y=1500:enable='between(t,2.00,2.12)',\
drawtext=fontfile=f.ttf:text='ABIER':fontsize=72:fontcolor=white:borderw=5:x=90:y=1500:enable='between(t,2.12,2.24)',\
drawtext=fontfile=f.ttf:text='ABIERTO':fontsize=72:fontcolor=white:borderw=5:x=90:y=1500:enable='between(t,2.24,4.50)'" \
  -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

Para frases largas eso son treinta `drawtext` y conviene generarlos con un script (`134`). En CapCut,
la animación de entrada *Máquina de escribir* ya lo hace y es más rápido de aplicar; solo revisa la
velocidad, porque por defecto suele ir demasiado lenta.

**Dónde NO usarlo:** en el gancho. Los primeros 3 segundos no pueden gastarse esperando a que una
frase termine de escribirse.

---

## 4. Texto que reacciona al audio

Esta es la que hace que un reel se sienta editado por alguien con oído. La idea:

> El texto **golpea en el beat**. No aparece cuando el clip empieza: aparece cuando la música pega.

No hace falta ninguna herramienta de "texto reactivo". Hace falta **saber dónde están los golpes** y
poner el texto ahí. Dos formas de averiguarlo:

### Forma A — a ojo, en la línea de tiempo

En CapCut, con la música en la pista de audio, la **forma de onda** ya te dice dónde están los golpes:
son los picos. Amplía la línea de tiempo al máximo y pon los cortes de texto en los picos. Además,
CapCut tiene **Marcar ritmo** (beat detection) que pone marcas automáticas sobre el audio; son un buen
punto de partida aunque hay que corregirlas a mano.

### Forma B — sacar los tiempos por código

Si estás generando el video por pipeline, puedes extraer los momentos fuertes del audio:

```bash
ffmpeg -i musica.mp3 -af "silencedetect=noise=-24dB:d=0.12" -f null - 2> golpes.txt
```

Eso te da los momentos de silencio, y los finales de silencio son arranques de sonido. Para música con
percusión marcada funciona sorprendentemente bien. Para algo más fino, mide el volumen en ventanas
cortas:

```bash
ffmpeg -i musica.mp3 -af "astats=metadata=1:reset=0.1,ametadata=print:key=lavfi.astats.Overall.RMS_level:file=rms.txt" -f null -
```

Ese archivo te da el nivel cada 0,1 segundos. Los saltos grandes hacia arriba son golpes. Con eso
generas la lista de tiempos y de ahí salen tus `enable='between(...)'`.

### Los tres niveles de reacción al audio

| Nivel | Qué hace | Cuándo |
|---|---|---|
| **Aparición en el beat** | la palabra entra exactamente en el golpe | el 90% de los casos; es lo que hay que hacer siempre |
| **Escala en el beat** | la palabra ya está y da un pulso de 100% a 112% | énfasis en una palabra que se repite |
| **Cambio de color en el beat** | la palabra cambia de blanco a tu color de marca | cierre, una vez por video |

**El error de sincronía que arruina todo:** poner el texto *después* del golpe. Aunque sean tres
fotogramas, se lee como retraso y desafina el video entero. Si dudas, ponlo **un fotograma antes**: el
cerebro perdona la anticipación y no perdona el atraso.

---

## 5. Texto que sale del cuadro

La técnica menos usada y una de las más elegantes: el texto **es más grande que la pantalla** y solo se
ve un pedazo.

Por qué funciona: rompe la regla de que todo tiene que caber, y eso llama la atención por sí solo.
Además, una palabra cortada obliga al cerebro a completarla, y esa milésima de esfuerzo es enganche.

**Los tres usos que valen:**

1. **Palabra enorme que atraviesa el cuadro.** "GRATIS", "HOY", "ABIERTO". La letra ocupa casi toda la
   pantalla y se sale por los dos lados. Se usa **una vez por video**, en el momento de más energía.
2. **Texto que se va deslizando** de un lado al otro durante todo el plano, como una marquesina lenta.
   Sirve de fondo textural detrás del sujeto.
3. **Salida por el borde en vez de por opacidad.** El texto no se desvanece: se va del cuadro. Da
   dirección y sensación de continuidad hacia el siguiente plano.

**La regla que hace que no se vea como error:** si una palabra se corta, tiene que ser **evidente qué
palabra es**. "ABIERT" con la O cortada por el borde funciona. "BIER" en el centro no: parece un
accidente.

```bash
ffmpeg -i base.mp4 -vf "\
drawtext=fontfile=f.ttf:text='ABIERTO':fontsize=340:fontcolor=white@0.92:\
borderw=10:bordercolor=black:\
x='-120 + 90*(1-pow(1-clip((t-5.0)/0.5,0,1),3))':y=760:enable='between(t,5.0,7.4)'" \
  -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

Ese texto de 340 px arranca desbordado por la izquierda y se acomoda con frenado, quedando cortado por
los dos lados. Es agresivo, se ve caro y solo aguanta una vez por video.

---

## 6. La disciplina que hace que todo esto funcione

Cuatro técnicas nuevas es exactamente el número que puede arruinar un video si se usan todas a la vez.
La proporción que funciona en un reel de 25 segundos:

```
SUBTITULOS          palabra suelta, entrada canonica, corte duro
                    el 90% del texto del video

ENFASIS 1           una tecnica avanzada, en el momento fuerte
                    revelado por mascara O palabra desbordada

ENFASIS 2           opcional, en el cierre
                    revelado por mascara sobre el dato duro

MAQUINA DE ESCRIBIR solo si hay una resena o un mensaje que mostrar
                    nunca en el gancho
```

**Una técnica avanzada por video, dos como máximo.** Si en un solo reel hay revelado, máquina de
escribir, texto desbordado y pulso en el beat, no hay jerarquía: todo grita y nada destaca.

Y la comprobación final, que vale para todo el módulo: **reproduce el video sin sonido a tamaño de
celular**. Si el texto no se lee, no importa cuán elegante sea la animación. La legibilidad le gana a
la técnica todas las veces.

---

## Errores comunes

1. **Aplicar técnicas avanzadas a los subtítulos.** Los subtítulos son palabra suelta, corte duro, y
   ya. Lo avanzado es para 2 o 3 momentos.
2. **Más de dos técnicas avanzadas en el mismo video.** Todo grita, nada destaca.
3. **Máquina de escribir en el gancho.** Los primeros 3 segundos no se gastan esperando.
4. **Máquina de escribir demasiado lenta.** El rango es 18–30 caracteres por segundo.
5. **Dejar el cursor parpadeando después de terminar la frase.** Parece que el video se colgó.
6. **Revelado por máscara de más de 0,7 segundos.** El espectador ya se impacientó.
7. **Revelado de derecha a izquierda.** Va contra la dirección de lectura y se siente incómodo.
8. **Texto que entra después del golpe.** Aunque sean tres fotogramas, desafina el video. Si dudas,
   ponlo un fotograma antes.
9. **Confiar ciegamente en la detección automática de ritmo.** Es un punto de partida, hay que
   corregirla a mano.
10. **Palabra cortada que no se adivina.** "ABIERT" funciona; "BIER" parece un error.
11. **Texto desbordado más de una vez por video.** Pierde todo el impacto.
12. **Agregar sombra al texto que ya tiene contorno.** Ensucia la forma de la letra. Tu configuración
    actual es la correcta.
13. **Dos palabras donde cabía una.** Obliga a barrer con el ojo y en 1,2 segundos eso se paga.
14. **Juzgar la legibilidad en el monitor.** Se juzga en el celular, a un brazo, sin sonido.
15. **Poner el texto avanzado en la zona del sujeto.** Ver zonas seguras en `204`.

---

## Checklist

Antes de dar por bueno el texto animado de un reel:

- [ ] Los **subtítulos** siguen siendo palabra suelta, con contorno, sin sombra, a corte duro.
- [ ] Hay **una o dos** técnicas avanzadas en todo el video, no cuatro.
- [ ] Ninguna técnica avanzada está en los **primeros 3 segundos**.
- [ ] Si hay revelado por máscara: dura entre **0,45 y 0,7 s** y va con curva, no lineal.
- [ ] Si hay revelado: va de **izquierda a derecha** o de abajo hacia arriba, no al revés.
- [ ] Si hay máquina de escribir: va a **18–30 caracteres por segundo** y el cursor desaparece al
      terminar.
- [ ] El texto de énfasis entra **exactamente en el golpe** de la música, o un fotograma antes.
- [ ] Revisé los golpes **a mano**, no solo con la detección automática.
- [ ] Si hay palabra desbordada: es **una sola vez** y la palabra **se adivina** aunque esté cortada.
- [ ] Ningún texto invade la **zona del sujeto** ni las zonas muertas (`204`).
- [ ] Reproduje el video **en el celular, sin sonido**, y todo el texto se leyó.
- [ ] Si repitiera este video la semana que viene, sabría **qué técnica usar y cuándo**.

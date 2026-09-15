# 368 — Ver sin sonido: diseñar un video que se entiende mudo

> La regla no es "todo el mundo ve en silencio". La regla es: **una parte importante de tu público te va
> a ver mudo y no sabes cuál.** Así que el video tiene que funcionar sin sonido y **mejorar** con sonido.
> Ese es el diseño. Todo lo demás de este módulo es cómo se consigue.

---

## Primero, la verdad sobre el dato

Vas a encontrar en todas partes que "el 85% ve sin sonido". De dónde sale, exactamente:

- **Digiday, mayo de 2016.** No era un estudio: eran **tres editores** (LittleThings, Mic, PopSugar)
  contando cuánto de **su propio** video se veía en mudo. PopSugar, en el mismo artículo, reportaba entre
  50% y 80%. O sea: ni siquiera entre ellos coincidía.
- Era sobre **Facebook**, que en esa época autorreproducía **sin sonido por defecto**. El dato medía el
  comportamiento por defecto de una plataforma, no una preferencia humana.

TikTok e Instagram Reels **arrancan con sonido** si el celular no está en silencio. Así que el 85% de
2016 no se puede trasladar. Y **no hay ningún número público confiable de 2026** para Reels o TikTok:
ni Meta ni TikTok lo publican.

Lo que sí sabemos, sin necesidad de estadística:

- Hay gente viendo en el trabajo, en clase, en el bus, al lado de alguien durmiendo.
- Hay celulares en silencio todo el día por costumbre.
- Hay gente sorda y con pérdida auditiva.
- El sonido a veces tarda una fracción de segundo en entrar, incluso cuando está activo.

**Conclusión de diseño, no de estadística:** el video se diseña mudo y se le agrega sonido encima. Nunca
al revés.

---

## La prueba del mudo (hazla siempre, cuesta un comando)

```bash
ffmpeg -y -i reel.mp4 -an -c:v copy prueba_muda.mp4
```

Pásalo al celular y míralo entero, **sin haberlo visto antes con sonido si es posible** (o después de un
café, para que se te olvide). Tres preguntas:

1. ¿Entiendo **de qué va** en los primeros 2 segundos?
2. ¿Entiendo **qué está en juego** antes del segundo 6?
3. ¿Entiendo **cómo terminó**?

Si falla la 1, no tienes gancho para media audiencia. Si falla la 3, no tienes pago para media audiencia.

---

## El reparto: qué información NO puede vivir solo en el audio

| Información | ¿Puede ir solo en audio? |
|---|---|
| El conflicto / la promesa | **No** |
| Los números (precios, cantidades, tiempos) | **No** |
| Los nombres propios (el plato, el bar, la calle) | **No** |
| El veredicto o la respuesta final | **No** |
| El chiste o el remate | **No** |
| El matiz ("bueno, en parte") | Sí |
| El tono, la emoción, la ironía | Sí |
| El detalle secundario | Sí |
| La atmósfera del lugar | Sí |

Regla corta: **lo que no se puede perder, se ve. Lo que da sabor, se oye.**

---

## Cómo se hace mudo un video con tu gramática

Tu sistema —palabras sueltas, hasta 6 en cascada vertical, entrando cada 0,15–0,30 s— es, de hecho, un
sistema **pensado para el mudo**. Es más legible que los subtítulos corridos porque no obliga a leer un
renglón mientras la imagen se mueve. Solo hay que usarlo bien.

### Las cinco reglas del texto mudo

1. **Las palabras que carguen información nunca son las de relleno.** Si la frase es "este plato nos
   costaba nueve mil cuatrocientos", en pantalla van **PLATO** · **9.400** · **PÉRDIDA**, no "este" ·
   "plato" · "nos" · "costaba".
2. **Los números van en cifra, no en letra.** `9.400` se lee de un golpe; "nueve mil cuatrocientos" hay
   que procesarlo.
3. **La palabra clave se queda más tiempo.** 0,4–0,6 s sola, mientras las demás ya se fueron.
4. **Máximo 6 palabras simultáneas, y solo en el cuerpo.** En el gancho, 3. En el pago, 2 o 3.
5. **Nunca texto en el fotograma 0.** La primera palabra entra en el fotograma 3 o 4 (ver `360`).

### Los tres momentos que sí o sí llevan texto

- **El gancho** (2 o 3 palabras con el conflicto)
- **El dato** (la cifra, siempre)
- **El pago** (la respuesta, en 2 o 3 palabras)

Si un video solo puede llevar texto en tres sitios, son esos tres.

---

## Lo que reemplaza al sonido: los sustitutos visuales

Cuando algo importante estaba en el audio, hay una versión visual. Casi siempre existe y casi siempre es
más barata que un subtítulo.

| Lo que se oye | Sustituto visual |
|---|---|
| El *chac* de la chapa | La chapa saltando, en primer plano |
| El chisporroteo | El humo subiendo, el movimiento del aceite |
| El tono de sorpresa | La cara reaccionando (medio segundo más de plano) |
| La ironía | Un corte a alguien que mira raro |
| "Está muy caliente" | La mano apartándose |
| El silencio dramático | Un plano que se sostiene sin cortar 1 s más |
| El golpe musical | Un corte duro en ese fotograma exacto |

Ese último es clave: **el ritmo musical se puede ver**. Si cortas en el golpe, quien ve mudo percibe el
pulso igual, porque lo ve.

---

## El guion mudo: la prueba de las capturas

La forma más rápida de auditar un video para mudo, y la única que no requiere ver nada:

```bash
# una captura cada 2 segundos, en cuadrícula
ffmpeg -y -i reel.mp4 -vf "fps=1/2,scale=200:-1,tile=6x4" -frames:v 1 guion_mudo.png
```

Ahora lee la cuadrícula **como si fuera una historieta**. Si con esas imágenes —y el texto que se ve en
ellas— alguien puede contar de qué va el video, está diseñado para mudo. Si la cuadrícula es "una persona
hablando ×24", no lo está.

**El objetivo mínimo:** que la historieta se entienda con **6 de las 24** viñetas.

---

## Legibilidad real: la interfaz se come tu texto

Un texto perfecto en el export puede quedar tapado por los botones de la app. Zonas peligrosas en 9:16
(1080×1920), aproximadas y variables según versión:

- **Arriba:** ~250 px (barra de estado, buscador)
- **Abajo:** ~500 px (descripción, usuario, sonido, barra de progreso)
- **Derecha:** ~200 px (columna de botones de me gusta / comentarios / compartir)

Comprueba qué queda dentro de la zona segura recortándola:

```bash
# el rectángulo que casi siempre se ve limpio
ffmpeg -y -i reel.mp4 -vf "crop=880:1170:0:250" -an zona_segura.mp4
```

Si en `zona_segura.mp4` tu texto clave está completo, vas bien. Si se sale, muévelo. Detalle de zonas por
plataforma en `45`.

**El error más caro:** poner el texto abajo, "como los subtítulos de siempre". Abajo es donde la app pone
todo lo suyo. En vertical, el texto vive en el **tercio central-alto**.

---

## Contraste: que se lea sobre la penumbra del bar

Un bar es oscuro, con luces cálidas puntuales. El texto blanco sobre eso se pierde en cuanto pasa por
delante una lámpara.

Tres soluciones, en orden de calidad:

1. **Fondo sólido detrás de la palabra** (caja). Fea pero infalible. En un bar oscuro, es la correcta más
   veces de las que uno quisiera.
2. **Contorno grueso + sombra.** Contorno de 4–6 px y sombra desplazada. Se lee sobre casi todo.
3. **Solo sombra.** Solo si el fondo es estable y oscuro de verdad.

Y una verificación numérica del peor fotograma: recorta la zona del texto y mira el brillo.

```bash
ffmpeg -y -ss 12.0 -i reel.mp4 -frames:v 1 -vf "crop=880:300:100:700,signalstats,metadata=print" -f null - 2>&1 | grep YAVG
```

Si el fondo detrás del texto tiene un `YAVG` alto (fondo claro) y tu letra es blanca, no se lee. Cámbiala
o ponle caja.

---

## Y aun así: el sonido sigue siendo la mitad del trabajo

Diseñar para mudo **no** es publicar sin cuidar el audio. Es lo contrario: como el video se sostiene
solo, el sonido queda libre para hacer lo que mejor hace —dar emoción, ritmo y verdad— sin cargar con la
obligación de explicar.

Y hay un detalle práctico: en TikTok y Reels, el sonido influye en distribución y en el uso del audio por
otros. Un video mudo por dentro (sin ambiente, sin música) se siente muerto para quien sí tiene volumen.

**La fórmula:** información completa en imagen y texto, emoción completa en sonido.

---

## Accesibilidad, que además es lo correcto

Las palabras sueltas no son subtítulos: no transcriben todo lo que se dice. Para quien no oye nada, un
video de tu estilo puede quedar incompleto.

Dos cosas concretas, baratas:

- Activar los **subtítulos automáticos** de la plataforma además de tu texto de marca (van en otra capa,
  no se pelean si dejas la zona baja libre).
- Poner en la descripción una línea con lo esencial: el dato, el precio, la dirección.

Ver `95` para el detalle de metadatos y accesibilidad.

---

## Errores comunes

1. Citar el 85% de Digiday como si fuera ley de 2026: es de 2016, es de Facebook y eran tres editores
   contando lo suyo.
2. Diseñar el video con sonido y "agregarle subtítulos" al final. Se nota y se lee mal.
3. Dejar el número, el precio o el nombre del plato **solo** en el audio.
4. Poner el remate o el chiste solo en la voz: quien ve mudo se queda sin pago.
5. Poner el texto abajo, donde la app pone la descripción y la barra de progreso.
6. Texto blanco sin caja ni contorno sobre la penumbra del bar.
7. Números escritos en letra en vez de en cifra.
8. Poner en pantalla las palabras de relleno de la frase y no las que llevan la información.
9. Seis palabras simultáneas en el gancho o en el pago. Ahí van 2 o 3.
10. No hacer nunca la prueba del mudo antes de publicar.
11. Confundir "diseñar para mudo" con "descuidar el audio": el que sí oye se lleva un video muerto.
12. No mirar la cuadrícula de capturas: es la auditoría más rápida que existe y toma 30 segundos.
13. Olvidar los subtítulos automáticos y la línea de descripción para quien no oye nada.

---

## Checklist

- [ ] Exporté una copia sin audio y la vi entera en el celular
- [ ] En mudo se entiende de qué va antes del segundo 2
- [ ] En mudo se entiende qué está en juego antes del segundo 6
- [ ] En mudo se entiende cómo terminó
- [ ] Los números están en pantalla, en cifra
- [ ] Los nombres propios (plato, bar, lugar) están en pantalla
- [ ] El pago/remate tiene 2 o 3 palabras en pantalla
- [ ] Las palabras en pantalla son las que llevan información, no las de relleno
- [ ] La palabra clave se queda 0,4–0,6 s sola
- [ ] Todo el texto importante cae dentro de la zona segura (comprobado con el recorte)
- [ ] El texto tiene caja o contorno suficiente para la penumbra del bar
- [ ] Saqué la cuadrícula de capturas y la historieta se entiende con 6 viñetas
- [ ] El audio sigue estando bien hecho para quien sí lo oye
- [ ] Dejé libre la zona baja para los subtítulos automáticos de la plataforma

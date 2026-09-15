# 173 — Iluminación básica

**Qué resuelve:** que la imagen se vea bien **sin comprar nada**, y que el editor no reciba tres bloques
de material con luces distintas que no se pueden emparejar. Este módulo está escrito desde la mesa de
montaje: no habla de esquemas de tres puntos, habla de qué luz produce material montable y qué luz
produce un problema de tres horas.

---

## 1. Lo que la luz mala le hace al editor

| Situación de rodaje | Qué pasa en el montaje | ¿Arreglo? |
|---|---|---|
| Poca luz | Imagen con grano; al corregir, el grano se dispara | 🟡 Parcial, se nota |
| Contraluz (ventana detrás) | Cara negra sobre fondo quemado | ❌ La cara no vuelve |
| Zonas quemadas (blanco puro) | No hay información: queda un parche blanco | ❌ No |
| Neón morado sobre la piel | Piel violeta; al corregir, todo el plano se desarma | 🟡 Difícil |
| Luz de día + luz de bombillo en el mismo cuadro | Media cara cálida, media azul | 🟡 Difícil |
| **La misma frase grabada con luces distintas** | **Salto brutal en cada corte** | ❌ Se pierde el montaje limpio |

La última fila es la que ocurrió en el rodaje real. Volveremos a ella en la sección 6.

---

## 2. La regla que resuelve el 80%: la luz de ventana

La mejor luz gratis del mundo es una ventana con luz indirecta.

**Cómo se usa:**

```
        VENTANA
           |
           |  (luz suave entrando)
           ↓
      [ PERSONA ]  ← mirando hacia la ventana o a 45°
           |
        [ CÁMARA ]  ← de espaldas a la ventana
```

**La regla en una frase:** **la ventana adelante de la persona, la cámara de espaldas a la ventana.**

Nunca al revés. Si la ventana queda detrás de la persona, la cámara mide la luz de la calle (muchísima),
baja la exposición, y la cara queda negra. Eso es el contraluz, y es el error de iluminación número uno.

**Qué ventana sirve:**

| Tipo | ¿Sirve? |
|---|---|
| Ventana grande con **luz indirecta** (día nublado, sombra, lado sin sol directo) | ✅ La mejor |
| Ventana con **sol directo pegando** | ❌ Sombras duras, ojos entrecerrados. Poner una cortina blanca. |
| Puerta abierta hacia un patio en sombra | ✅ Excelente |
| Ventana pequeña muy lejos | 🟡 Poca luz, mejor acercar a la persona |

**Truco de bar-restaurante:** una mesa junto a la ventana de la fachada, con la persona sentada mirando
hacia adentro y la cámara desde adentro, da luz de calidad de estudio a las 10 de la mañana. Gratis.

**Cuidado con el sol que se mueve.** Si el rodaje dura dos horas, la luz de la ventana cambia de
dirección y de temperatura. Graba todo lo de la ventana **seguido**, no repartido durante el día
(`175`). Un día nublado es mejor que uno soleado: la luz es constante y suave.

---

## 3. Contraluz: cómo se detecta y cómo se salva

**Se detecta en 2 segundos:** mira la pantalla del celular. Si la cara se ve más oscura que el fondo, hay
contraluz.

**Se salva de tres formas, en orden de preferencia:**

1. **Girar 180 grados.** La persona en el lugar de la cámara y la cámara en el lugar de la persona. Es
   gratis, instantáneo y es la solución correcta el 90% de las veces.
2. **Tocar la cara en la pantalla y bloquear la exposición ahí** (`171`). El celular expone para la cara;
   el fondo se quema (queda blanco) pero la cara se ve. En un video de redes eso es aceptable — un fondo
   quemado detrás de una cara bien expuesta se lee como "está afuera", no como error.
3. **Rebotar luz a la cara.** Una cartulina blanca, un mantel, una servilleta grande sostenida por
   alguien fuera de cuadro, devolviendo la luz de la ventana hacia la cara. Sirve, pero necesita una
   persona más.

**Lo que NO funciona:** subir el brillo en post. Cuando la cara está muy oscura no hay información en el
archivo. Al subirla aparece ruido de color (manchas verdes y magenta en la piel) y se ve peor que dejarla
oscura.

```bash
# Medir si una cara está subexpuesta: brillo promedio del plano
ffmpeg -hide_banner -i clip.mp4 -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG" \
  -f null - 2>&1 | head -3
```

`YAVG` por debajo de ~50 en un plano de cara = está muy oscuro. Entre 90 y 140 es zona sana.

---

## 4. El neón de color: bonito en vivo, problemático al montar

Los bares tienen neón porque se ve espectacular a simple vista. En video pasan cuatro cosas.

### a) La piel se tiñe y no hay vuelta atrás

Un neón morado sobre la cara pone la piel violeta. El problema no es estético: es que **la información
de color de la piel no se grabó**. La cámara solo recibió luz morada, así que en el archivo no existe el
tono naranja/rojizo de la piel. Corregirlo en post significa inventarlo, y se ve inventado (`67`).

**La solución de rodaje, que es la única real:** que la cara reciba una **luz neutra** y que el neón
quede **de fondo**. O sea:

```
   [ NEÓN MORADO ]  ← detrás, en la pared, como ambiente
          ...
      [ PERSONA ]
          ↑
   [ luz neutra ]  ← ventana, bombillo blanco, lámpara de escritorio, otro celular con la linterna
      [ CÁMARA ]
```

Así consigues lo mejor de los dos mundos: la piel se ve bien **y** el fondo tiene el morado que da
carácter. Es exactamente como lo hacen los videos que te gustan.

**La luz neutra puede ser:** un panel LED de $60.000, una lámpara de escritorio con bombillo blanco, la
linterna de otro celular con una servilleta encima para suavizarla, o simplemente pararse cerca de una
ventana con el neón detrás.

### b) El neón parpadea

Muchos LED y neones parpadean a 60 Hz. Grabando a 24 fps aparecen bandas que suben por la imagen. Graba
a **30 fps** en interiores (`171`).

### c) El neón satura el sensor

Un letrero de neón brillante en cuadro sale **quemado**: una mancha de color plano sin detalle. No es
grave si es decorativo, pero si el letrero dice el nombre del bar y quieres que se lea, tienes que bajar
la exposición general o encuadrar para que no domine.

### d) El neón cambia el balance de blancos automático

La cámara se pelea consigo misma decidiendo de qué color es la luz. El tono del morado cambia dentro de
la misma toma. Fija el balance de blancos (`171`) o al menos bloquea AE/AF.

**Lo que sí hace bien el neón:** dar **profundidad**. Un neón detrás de la persona separa la figura del
fondo y le da al plano una sensación de tridimensionalidad que la luz plana no da. Úsalo de fondo, nunca
como luz principal de la cara.

---

## 5. Mezclas de luz: el problema silencioso

> **Temperatura de color:** cuán "cálida" (anaranjada) o "fría" (azulada) es una luz. Se mide en Kelvin.
> Los bombillos de bar suelen ser ~2.800 K (naranja). La luz de día es ~5.500–6.500 K (azul en
> comparación).

Cuando en el mismo cuadro hay **luz de ventana por un lado y bombillo cálido por el otro**, la cámara
tiene que elegir una y la otra se ve mal. Si el balance está en luz de día, el lado del bombillo queda
naranja intenso. Si está en interior, la ventana queda azul eléctrico.

Eso ocurre naturalmente en la terraza de un bar: mitad techo con bombillos, mitad cielo abierto.

**Cómo se resuelve en rodaje (elige una):**

1. **Apaga los bombillos** y usa solo luz de día. La opción limpia.
2. **Cierra la cortina** y usa solo bombillos. También limpia.
3. **Ubica a la persona en una sola de las dos luces**, con la otra lejos y fuera del encuadre.
4. Si no hay remedio, **fija el balance de blancos manualmente** en un punto intermedio (~4.500 K) y
   avisa al editor para que lo corrija en un solo paso.

**Cómo se ve el problema al montar:** la piel de un lado de la cara naranja y del otro azul, que es el
tipo de imagen que el ojo lee como "video mal hecho" aunque no sepa por qué.

---

## 6. El error del rodaje real: la misma frase con tres luces

Este merece su propia sección porque fue el problema más caro del rodaje.

**Qué pasó:** la misma frase se grabó en tres sitios:
- El **pasillo** con neón morado
- La **barra**, con luz cálida de bombillos
- La **terraza**, a plena luz del día

Cada sitio es defendible por separado. El problema es que al montar, el editor va a alternar entre tomas
para armar la frase completa — y cada corte era un **salto de luz brutal**: morado → ámbar → azul de
mediodía, en medio segundo.

**Por qué no se arregla:**

Emparejar planos (`62`) funciona cuando las diferencias son de grado: un plano un poco más frío, otro un
poco más contrastado. **No funciona** cuando la luz es de naturaleza distinta. Para llevar la cara
morada del pasillo al mismo lugar que la cara de la terraza tendrías que reconstruir información que no
existe, y en el intento el fondo, la ropa y todo lo demás se desarman.

**Lo que el editor terminó teniendo que hacer:** usar solo el material de una locación y botar el resto.
Es decir, dos tercios del rodaje se perdieron.

**La regla que sale de esto:**

> **Cada frase del guion pertenece a UNA locación. Se decide antes de grabar y no se cambia.**

Si quieres variedad de sitios en el video, la variedad va **entre frases distintas**, no dentro de la
misma frase. Frase 1 en la barra, frase 2 en la terraza, frase 3 en el pasillo. Eso sí funciona, porque
el corte entre frases es un cambio de escena y el ojo lo acepta. Detalle completo en `175`.

---

## 7. Iluminación con presupuesto cero: el kit real de un bar

| Herramienta | Dónde está | Para qué |
|---|---|---|
| **Ventana** | Ya la tienes | Luz principal. Gratis y la mejor. |
| **Cartulina blanca / mantel** | Papelería, $2.000 | Rebotar luz a la cara |
| **Linterna de otro celular + servilleta** | Ya la tienes | Relleno de emergencia en la cara |
| **Lámpara de escritorio con bombillo blanco** | Ferretería, $25.000 | Luz neutra sobre la cara con neón de fondo |
| **Panel LED pequeño con batería** | ~$60–120 mil | Ya es "equipo". Aguanta cualquier rodaje. |
| **Cortina blanca delgada** | La del baño sirve | Suavizar sol directo en la ventana |

**Con la ventana y una cartulina ya tienes el 90% de lo que necesitas.** El panel LED es lo primero que
comprarías si el bar va a hacer video más de una vez al mes.

**Dónde poner el panel LED cuando lo tengas:** al frente de la persona, **arriba de la línea de los
ojos** y a unos 45° de lado, no a la altura de la cara y de frente. La luz frontal plana aplana los
rasgos y se ve a videollamada. Un poco de lado y arriba da forma.

---

## 8. Lo que el editor puede y no puede hacer con la luz

Para que el briefing sea honesto, esta es la frontera:

**Sí puede:**
- Subir o bajar brillo y contraste general (`61`)
- Cambiar la temperatura de color de un plano completo
- Emparejar dos planos parecidos hacia un punto común (`62`)
- Poner un look, una viñeta, textura (`63`, `66`)
- Forzar la paleta de marca sobre el material (`64`)
- Recuperar algo de las sombras si la exposición estaba solo un poco baja

**No puede:**
- Devolver detalle a una zona **quemada** (blanco puro). No hay información.
- Devolver detalle a una zona **negra**. Al subirla sale ruido de color.
- Quitar el tinte de un neón de la piel sin destruir el resto del plano
- Arreglar un cambio de exposición **dentro** de la misma toma (por eso se bloquea AE/AF)
- Hacer que un plano con luz de neón y otro con luz de día se sientan del mismo momento

**Cómo se le dice esto al que graba:** "La luz es lo único que no puedo arreglar del todo. Si la cara se
ve bien en la pantalla del celular, quedamos bien. Si se ve oscura o rara, no lo arreglo después."

---

## 9. La prueba de 30 segundos antes de grabar

Antes de la primera toma real, en cada locación:

1. Pon a la persona donde va a estar.
2. Encuadra como vas a encuadrar.
3. Graba 10 segundos hablando.
4. **Míralos en la pantalla, al 100% de brillo, tapando el reflejo con la mano.**

Preguntas:
- ¿Se le ven los **ojos**? (si están en sombra, sube o mueve la luz)
- ¿La cara está **más clara que el fondo**? (si no, hay contraleuz)
- ¿La piel se ve de **color piel**? (si está morada, verde o naranja, arregla el balance o la luz)
- ¿Hay algo **quemado** en cuadro que distraiga? (una ventana blanca, un letrero)

Si las cuatro respuestas están bien, graba. Si no, mueve algo. Mover a la persona dos metros cuesta 20
segundos; arreglarlo en post cuesta dos horas y queda peor.

---

## Errores comunes

1. **Poner a la persona de espaldas a la ventana.** Es el error #1. La cara queda negra y no se
   recupera. Gírala.
2. **Usar el neón de color como luz principal de la cara.** La piel se tiñe y esa información no se
   grabó. El neón va **de fondo**, con luz neutra en la cara.
3. **Grabar la misma frase en locaciones con luces distintas.** Produce saltos que no se emparejan. Una
   frase = una locación (`175`).
4. **Mezclar luz de día y bombillo cálido en el mismo cuadro.** Media cara azul, media naranja. Apaga
   una de las dos.
5. **Creer que "en post se sube el brillo".** Subir una cara oscura saca ruido de color en la piel. Se
   ve peor que dejarla oscura.
6. **Repartir el rodaje de una locación a lo largo del día.** El sol se mueve: la luz de las 10 no es la
   de las 2. Todo lo de un sitio, seguido.
7. **Sol directo en la cara.** Sombras duras, ojos entrecerrados, la persona incómoda. Cortina blanca o
   sombra.
8. **Dejar exposición y balance de blancos en automático bajo neón.** El tono cambia dentro de la misma
   toma y eso es peor que cualquier salto entre planos.
9. **Grabar a 24 fps bajo LED o neón.** Bandas de parpadeo. En Colombia (60 Hz), graba a 30.
10. **No mirar la toma de prueba en la pantalla.** Los cuatro chequeos de la sección 9 toman 30 segundos
    y salvan el material.
11. **Iluminar de frente y a la altura de la cara.** Aplana los rasgos y se ve a videollamada. Un poco de
    lado y por encima de los ojos.
12. **Confiar en el "modo noche" del celular para video.** El modo noche es para fotos; en video la
    imagen queda con arrastre y ruido. Si hay poca luz, agrega luz.

---

## Checklist

- [ ] La **ventana está delante** de la persona y la cámara de espaldas a la ventana.
- [ ] La **cara está más clara que el fondo** (no hay contraluz).
- [ ] Se le **ven los ojos** en la toma de prueba.
- [ ] La **piel se ve de color piel** (ni morada, ni verde, ni naranja).
- [ ] Si hay neón de color, está **de fondo** y hay **luz neutra en la cara**.
- [ ] **No hay mezcla** de luz de día y bombillo cálido sobre la persona.
- [ ] **No hay zonas quemadas** que distraigan en el encuadre.
- [ ] **Exposición y balance de blancos bloqueados** para ese plano.
- [ ] Se graba a **30 fps** bajo luz artificial (sin bandas de parpadeo).
- [ ] Todo el material de **una locación se grabó seguido**, sin repartirlo durante el día.
- [ ] **Cada frase se grabó en una sola locación**, no en tres.
- [ ] Se hizo la **prueba de 10 segundos** y se revisó en pantalla con las cuatro preguntas.
- [ ] Si el sol es directo, se **suavizó con una cortina** o se movió a la sombra.
- [ ] El editor sabe qué locaciones se usaron y con qué luz, **antes** de empezar a montar.

# 260 — Qué es compositing

**Qué resuelve:** juntar en un mismo plano cosas que nunca estuvieron juntas —una persona grabada con
el celular, un texto, un fondo generado por IA, un logo, una chispa— y que el resultado se vea como
**un solo plano**, no como tres cosas pegadas. Este módulo es el marco: qué es compositing, cuál es el
orden correcto de operaciones, y los **tres problemas que aparecen siempre**, sin excepción: el borde,
la luz y la perspectiva.

Los módulos `80` y `204` te enseñaron a superponer capas y a ordenarlas. Este bloque (260–269) es otra
cosa: aquí el objetivo no es que la capa se vea bonita encima, es que **la capa desaparezca como capa**.

---

## 1. La definición que importa

> **Compositing:** combinar imágenes de orígenes distintos en una sola imagen que el ojo acepte como
> capturada de una vez.

La palabra clave es **acepte**. No "que sea perfecta". El espectador de Instagram no está haciendo
peritaje forense: está pasando el dedo. Tu trabajo no es engañar a un supervisor de efectos de Marvel,
es que en los primeros 1,5 segundos nadie sienta el pinchazo de "esto está pegado".

Y ese pinchazo es sorprendentemente barato de evitar. **El 80% de la credibilidad viene de tres arreglos
que juntos toman 5 minutos**: sombra de contacto, un poco de desenfoque y grano encima de todo. El otro
20% cuesta horas y casi nunca vale la pena en un reel (ver `269`).

### Compositing NO es efectos especiales

- **Efecto especial** = algo que llama la atención. Una explosión, un rayo, un portal.
- **Compositing** = algo que NO llama la atención. Un texto que pasa detrás de la persona, un cielo
  cambiado, un micrófono borrado.

**Casi todo lo que te sirve para vender en redes es lo segundo.** El compositing invisible es el que
hace que un video de celular se sienta caro. El efecto especial visible casi siempre se siente barato,
porque el listón lo puso el cine y tu celular no lo alcanza.

---

## 2. Con qué se hace esto (tu caja de herramientas real)

Este bloque está escrito para lo que tú tienes:

| Herramienta | Qué hace bien en compositing | Qué NO hace |
|---|---|---|
| **CapCut escritorio** | recortar el sujeto (matting por IA), máscaras de forma, croma, modos de fusión, seguimiento, keyframes | máscaras animadas complejas, nodos, capas de ajuste reales, canal alfa de salida |
| **ffmpeg 8.1.2** | todo lo medible y repetible: sombras, grano, desenfoque, color, croma, parches, mezclas | nada interactivo; no ves lo que haces hasta que renderizas |
| **Modelos de IA** (imagen/video) | generar el elemento o el fondo, quitar objetos, recortar | precisión al píxel, repetir el mismo resultado dos veces |

Todo lo de este bloque se puede hacer con esas tres. **Cuando una técnica necesite algo que no tienes
—After Effects, Nuke, Fusion, Mocha—, lo voy a decir de frente y te voy a dar la alternativa que sí
puedes hacer.** No hay nada más inútil que un tutorial que arranca con "abre After Effects".

> ⚠️ **Los comandos de ffmpeg de este bloque están escritos para tu compilación (8.1.2 con frei0r,
> vidstab, zimg, libplacebo y opencl).** Aun así, pruébalos sobre un clip corto de 2 segundos antes de
> meterlos en un render final. Un filtro encadenado mal puede tardar 20 minutos y salir negro.

---

## 3. El orden de operaciones (no lo cambies)

El compositing tiene un orden. Saltárselo es la razón número uno por la que la gente pelea horas con
algo que debería tomar diez minutos.

```
1. SEPARAR      →  sacar el sujeto de su fondo                     (261)
2. LIMPIAR      →  arreglar el borde: halo, sierra, agujeros       (81, 261)
3. COLOCAR      →  posición, escala, perspectiva, seguimiento      (264)
4. INTEGRAR     →  color, desenfoque, sombra, luz de borde         (263)
5. UNIFICAR     →  grano y grado de color SOBRE TODO el plano      (263)
```

Los pasos 1 y 2 son de **la capa**. El 3 es de **la relación** entre la capa y el fondo. El 4 es de
**la física**. Y el 5 —el que todo el mundo se salta— es el que amarra el plano: aplicar una sola cosa
encima de la mezcla ya terminada.

**Por qué el orden importa:** si le pones grano al recorte antes de escalarlo, el grano se escala
también y queda del tamaño equivocado. Si le ajustas el color antes de integrarlo, lo vas a tener que
volver a ajustar. Si le pones sombra antes de decidir la posición, la sombra queda apuntando a ningún
lado. Cada paso fuera de orden se paga con hacerlo dos veces.

---

## 4. El problema 1: el borde

El borde es donde el ojo humano es implacable. Llevamos toda la vida viendo objetos contra fondos: el
cerebro tiene un detector de bordes de fábrica y nota lo que está mal en milisegundos, aunque la persona
no sepa decir qué.

**Las cinco formas en que un borde delata que algo está pegado:**

| Síntoma | Qué se ve | Causa | Se arregla en |
|---|---|---|---|
| **Halo de color** | contorno verdoso o azuloso | derrame del croma | `81` (despill) |
| **Borde de sierra** | escalera de píxeles en las diagonales | recorte sin suavizado (`blend=0`) | `81` |
| **Borde demasiado nítido** | el sujeto está más definido que el fondo | no se igualó el foco | `263` |
| **Borde oscuro** | línea negra de 1 píxel | alfa premultiplicado mal manejado | sección 6 |
| **Contorno que respira** | el borde vibra fotograma a fotograma | matting por IA inestable | `261` |

El más traicionero es el último. Un recorte por IA en video no calcula lo mismo en cada fotograma: el
contorno **hierve**. En una foto se ve perfecto; en movimiento, tiembla. Se nota sobre todo en el pelo y
en los dedos.

> **La regla del borde:** un borde perfecto sobre un fondo que no le corresponde se ve peor que un borde
> mediocre sobre un fondo bien integrado. Si tienes 10 minutos, gástalos en la luz, no en el borde.

---

## 5. El problema 2: la luz

Es el problema más importante y el que la gente ignora más, porque no se ve como un error: se siente
como "algo raro".

Cuatro cosas de la luz tienen que coincidir entre el elemento y el fondo:

1. **La dirección.** Si en el fondo la luz entra por la izquierda y tu sujeto está iluminado desde la
   derecha, está mal. Y no hay filtro que lo arregle: la sombra de la nariz apunta al lado contrario.
   Esto se arregla **eligiendo otro fondo**, no en post.
2. **La dureza.** Sol directo = sombras con borde definido. Día nublado o interior = sombras difusas.
   Un sujeto de sol duro sobre un fondo nublado grita mentira.
3. **La temperatura.** Luz de bombillo (cálida, anaranjada) vs. luz de ventana (fría, azulada). Esto
   **sí** se arregla en post, y es fácil (`263`).
4. **El nivel.** Un sujeto más brillante que el fondo se ve recortado, literalmente. Igualar el negro y
   el blanco es el ajuste de mayor rendimiento por minuto invertido.

**La jerarquía honesta:** dirección y dureza se deciden **al grabar** o **al elegir el fondo**.
Temperatura y nivel se arreglan **en post** en dos minutos. Si tienes que escoger un fondo generado por
IA, escógelo por la dirección de la luz, no por lo bonito que sea.

---

## 6. El problema 3: la perspectiva

Tres cosas que casi nadie mira y que rompen el plano:

**La altura de la cámara.** Si el fondo está grabado a la altura del pecho y tú grabaste a la altura de
los ojos, el horizonte no cuadra. Regla práctica: **la línea del horizonte del fondo tiene que pasar por
la altura de los ojos del sujeto** si ambos están de pie en el mismo suelo.

**El lente.** Un celular en gran angular deforma: la cara se agranda de cerca, las líneas de los lados
se curvan. Un fondo generado por IA con aspecto de teleobjetivo (todo comprimido, plano) mezclado con un
sujeto en gran angular no cuadra nunca. Al pedirle el fondo a la IA, pídeselo con el mismo lente:
"fotografía con lente de 26 mm de celular".

**El punto de contacto con el suelo.** Es lo que más delata. Si el sujeto flota —aunque sea 3 píxeles—
todo el plano se cae. La solución no es matemática: es la **sombra de contacto** (`263`), que le dice al
ojo dónde toca el piso. Es el truco de mejor relación esfuerzo/resultado de todo el bloque.

---

## 7. El detalle técnico que sí tienes que conocer: alfa recto vs. premultiplicado

Es la única trampa técnica del compositing que te va a morder de verdad.

> **Alfa recto (straight):** el color del píxel es el color real, y el alfa se guarda aparte.
> **Alfa premultiplicado:** el color ya viene multiplicado por el alfa (los bordes semitransparentes
> vienen oscurecidos hacia el negro).

Si mezclas los dos, pasa esto: **un borde negro fino** alrededor del elemento (tratar premultiplicado
como recto) o **un borde claro/fantasma** (al revés).

El `overlay` de ffmpeg trabaja con alfa **recto** por defecto. Si tu PNG viene premultiplicado —cosa
frecuente cuando sale de un render o de ciertos exportadores— pasa por `unpremultiply` antes:

```bash
# Si ves un contorno negro delgado alrededor del recorte, prueba esto:
ffmpeg -y -i elemento.png -vf "format=rgba,unpremultiply=inplace=1" elemento_recto.png
```

Y si necesitas lo contrario (para trabajar con `blend`, que a veces quiere premultiplicado):

```bash
ffmpeg -y -i elemento_recto.png -vf "format=rgba,premultiply=inplace=1" elemento_pm.png
```

> ⚠️ **Verifica esto en tu equipo antes de usarlo en producción.** El comportamiento de
> `premultiply`/`unpremultiply` con `inplace=1` cambia entre versiones. La prueba es de 5 segundos: pon
> el elemento sobre un fondo blanco y sobre uno negro. Si en blanco aparece un contorno oscuro, es
> premultiplicado mal tratado.

```bash
# La prueba de los dos fondos
ffmpeg -y -f lavfi -i "color=c=white:s=1080x1080" -i elemento.png \
  -filter_complex "[0:v][1:v]overlay=(W-w)/2:(H-h)/2" -frames:v 1 sobre_blanco.png
ffmpeg -y -f lavfi -i "color=c=black:s=1080x1080" -i elemento.png \
  -filter_complex "[0:v][1:v]overlay=(W-w)/2:(H-h)/2" -frames:v 1 sobre_negro.png
```

**En CapCut esto no lo controlas** y tampoco te hace falta: CapCut maneja su propio recorte
internamente. El problema aparece solo cuando metes PNG o `.mov` con alfa hechos por fuera.

---

## 8. La prueba del espectador (cómo saber si quedó bien)

No confíes en tu ojo después de dos horas mirando el mismo plano. Usa estas cuatro pruebas, en este
orden, y te ahorras publicar algo que se ve pegado:

**1. La prueba de los 3 segundos.** Cierra el proyecto. Mira el video una vez, a tamaño de celular,
sin pausar. ¿Sentiste algo raro? Si no, terminaste. Si sí, anota EN QUÉ SEGUNDO y recién ahí investiga.

**2. La prueba del volteo.** Voltea el plano en espejo y míralo:

```bash
ffmpeg -y -i compuesto.mp4 -vf "hflip" -c:v libx264 -crf 20 -pix_fmt yuv420p prueba_espejo.mp4
```

El cerebro deja de "leer" la escena como la conoce y empieza a ver formas. Los errores de borde y de
luz saltan de inmediato. Es un truco viejo de pintores y funciona igual acá.

**3. La prueba de la miniatura.** Reduce el video a 200 px de ancho. Si a ese tamaño el elemento se
sigue viendo como parte de la escena, ganaste. Si a 200 px ya se ve un rectángulo pegado, el problema no
es de detalle fino: es de luz o de nivel.

```bash
ffmpeg -y -i compuesto.mp4 -vf "scale=200:-2" -c:v libx264 -crf 20 -pix_fmt yuv420p mini.mp4
```

**4. La prueba de la tira de fotogramas.** Para cazar el borde que hierve:

```bash
ffmpeg -y -ss 2.0 -i compuesto.mp4 -t 1.6 -vf "fps=25,scale=200:-1,tile=8x5" -frames:v 1 tira.png
```

Cuarenta fotogramas en una imagen. Si el contorno cambia de forma entre cuadros, el matting está
inestable y toca acortar el tramo o cambiar de técnica (`261`).

---

## 9. Lo que ninguna técnica arregla

Sé honesto contigo mismo antes de empezar. Estas cinco cosas no se arreglan en post, se arreglan
grabando otra vez:

1. **Luz que viene del lado contrario.** No existe el filtro.
2. **Sujeto quemado** (blanco puro en la cara). No hay información que recuperar; el recorte se come el
   borde y no hay cómo integrar lo que no existe.
3. **Sujeto del mismo color que el fondo.** El matting no lo puede separar y tú tampoco.
4. **Desenfoque de movimiento fuerte.** Un brazo que es un borrón no tiene contorno que recortar. Se ve
   el pedazo del brazo cortado en seco.
5. **Grabado vertical un fondo que necesitas horizontal** (o al revés). Estirar no es una opción; se ve
   y se ve mal.

> **La regla del costo cero:** dos minutos pensando ANTES de grabar valen más que dos horas de
> compositing. Párate contra una pared lisa, con luz pareja, sin ropa del color del fondo, y el 90% de
> este bloque se vuelve innecesario. Esto está desarrollado en `261`.

---

## 10. Mapa del bloque

| Módulo | Qué resuelve |
|---|---|
| `260` | este: el marco, el orden, los tres problemas |
| `261` | separar el sujeto: croma, IA, rotoscopia, y cómo grabar para que salga limpio |
| `262` | **la técnica del sándwich** — la que más vas a usar |
| `263` | integrar: que lo pegado no se vea pegado |
| `264` | seguimiento a nivel VFX: anclar, corner pin, movimiento de cámara |
| `265` | borrar cosas del plano |
| `266` | cambiar el fondo y el cielo |
| `267` | partículas y luz: humo, polvo, destellos |
| `268` | qué hace la IA en VFX a agosto de 2026, verificado |
| `269` | **el presupuesto del esfuerzo** — qué NO vale la pena |

Si vas a leer solo dos: `262` (la técnica) y `269` (cuándo parar).

---

## Errores comunes

1. **Empezar por el borde.** Se pasan dos horas afinando el recorte y el elemento sigue pareciendo
   pegado porque la luz no cuadra. La luz primero, el borde después.
2. **Saltarse el paso 5 (unificar).** Grano y grado de color sobre la mezcla ya terminada, no sobre cada
   capa. Es el paso más barato y el que más amarra el plano.
3. **Poner grano al recorte antes de escalarlo.** El grano se escala con él y queda del tamaño
   equivocado. Grano siempre al final, sobre todo.
4. **Elegir el fondo por bonito y no por la dirección de la luz.** Después no hay cómo arreglarlo.
5. **Ignorar el punto de contacto con el suelo.** Un elemento flotando rompe el plano entero, aunque
   todo lo demás esté perfecto.
6. **Mezclar alfa recto con premultiplicado.** El contorno negro de 1 píxel viene de ahí. Prueba sobre
   fondo blanco y fondo negro.
7. **Juzgar el compositing en la pantalla del PC a tamaño completo.** Se publica en un celular. Míralo a
   tamaño de celular.
8. **Confiar en el ojo después de dos horas.** Usa las cuatro pruebas: 3 segundos, espejo, miniatura,
   tira de fotogramas.
9. **Intentar compositing sobre material quemado, borroso o del color del fondo.** Vuelve a grabar; es
   más rápido.
10. **Hacer efectos que se ven** cuando lo que te sirve es compositing que no se ve. Lo llamativo se
    siente barato en un celular; lo invisible se siente caro.
11. **Renderizar el proyecto completo para revisar un plano de 2 segundos.** Renderiza el tramo, míralo,
    y solo entonces el completo.

---

## Checklist

Antes de dar por bueno un plano compuesto:

- [ ] Seguí el orden: **separar → limpiar → colocar → integrar → unificar**.
- [ ] La **dirección de la luz** del elemento y del fondo coincide (o cambié el fondo).
- [ ] La **dureza de la sombra** coincide (sol duro con sol duro, difusa con difusa).
- [ ] Igualé **temperatura y nivel** (negros y blancos) entre elemento y fondo.
- [ ] El elemento **toca el suelo**: hay sombra de contacto o hay una razón visible por la que flota.
- [ ] El **borde** no tiene halo de color, ni sierra, ni contorno negro de 1 píxel.
- [ ] Revisé la **tira de fotogramas**: el contorno no hierve.
- [ ] Apliqué **grano y grado de color al final, sobre toda la mezcla**.
- [ ] Pasé la **prueba de los 3 segundos**, la del **espejo** y la de la **miniatura**.
- [ ] Lo vi a **tamaño de celular**, que es donde se va a ver de verdad.
- [ ] El efecto es **invisible**, no llamativo. Si se nota que es un efecto, revisa si eso es lo que
      querías.
- [ ] Si esto me tomó más de 15 minutos en un reel, leí `269` antes de seguir.

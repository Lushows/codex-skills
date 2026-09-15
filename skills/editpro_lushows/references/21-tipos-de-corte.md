# 21 — Tipos de corte

**Qué resuelve:** la mayoría de la gente solo conoce un corte: cortar aquí y pegar allá. Por eso sus
videos se sienten planos o entrecortados. Este módulo te da los nueve cortes que de verdad se usan, con
la regla de cuándo aplicar cada uno, para que dejes de "pegar clips" y empieces a montar.

---

## 0. Lo primero: el corte por defecto es duro

El 90% de los cortes de cualquier video profesional son **cortes duros** — sin transición, sin efecto,
sin nada. Un fotograma es un plano y el siguiente ya es otro.

Si estás poniendo una transición en cada corte, no estás editando: estás decorando. Las transiciones
tienen su propio módulo (`50`) y su regla es "casi nunca".

Lo que cambia entre un corte bueno y uno malo no es el efecto: es **dónde cae** y **por qué**.

---

## 1. Corte duro (hard cut)

**Qué es:** el corte simple. Termina el plano A, empieza el plano B, en el mismo fotograma para imagen
y audio.

**Cuándo:** por defecto. Siempre, salvo que tengas una razón concreta para otra cosa.

**Cómo se hace bien:** el corte duro se nota cuando cae en un momento muerto. No lo pongas en el silencio
entre dos frases: ponlo **justo cuando arranca la frase siguiente** o **en medio de un movimiento**.

```bash
# Corte duro exacto: del segundo 3.4 al 7.9
ffmpeg -hide_banner -ss 3.4 -to 7.9 -i entrada.mp4 -c:v libx264 -crf 18 -preset slow -c:a aac corte01.mp4
```

Nota técnica: poner `-ss` **antes** de `-i` es rápido pero se pega al fotograma clave más cercano; poner
`-ss` **después** de `-i` es exacto pero más lento. Para cortes de montaje quieres el exacto — y como
estás recodificando con `-crf`, el corte cae donde le dijiste.

---

## 2. J-cut (el audio entra antes que la imagen)

**Qué es:** oyes el plano siguiente **antes** de verlo. Se llama J por la forma que hace en la línea de
tiempo: el audio del clip B se estira hacia atrás por debajo de la imagen del clip A.

```
IMAGEN:   [ plano A ][ plano B ]
AUDIO:    [ audio A ][   audio B   ]
                    ↑ el audio B empezó antes
```

**Cuándo:** cuando quieres que el corte se sienta natural y no abrupto. Es el corte más usado en
entrevistas y documental. También cuando el plano B necesita contexto: oyes la sartén antes de ver la
cocina y tu cabeza ya está lista.

**Efecto real:** el J-cut hace que un montaje se sienta "fluido" sin usar ni una transición. Es el arma
número uno contra el video que se siente entrecortado.

---

## 3. L-cut (la imagen cambia y el audio sigue)

**Qué es:** el inverso. El audio del plano A sigue sonando mientras ya estás viendo el plano B.

```
IMAGEN:   [ plano A ][   plano B   ]
AUDIO:    [    audio A    ][audio B]
                          ↑ el audio A siguió
```

**Cuándo:** cuando alguien está hablando y quieres mostrar de qué habla sin interrumpirlo. Es la base
del **cutaway** y de toda la técnica de voz continua / imagen picada (módulo `23`).

**Esto es lo importante:** J-cut y L-cut son la razón por la que puedes tener un pulso de 1,5 s sin que
el video suene picado. La imagen corta; el audio no. Si tus cortes cortan audio e imagen siempre al
mismo tiempo, tu video va a sonar a diapositivas por más rápido que vaya.

### Cómo se hacen con ffmpeg

Se hacen separando pistas. El patrón: construyes la imagen por pedazos y le pegas encima el audio
continuo del bloque original.

```bash
# 1) Extraer el audio completo, sin cortar
ffmpeg -hide_banner -i toma.mp4 -vn -c:a pcm_s16le voz.wav

# 2) Construir la imagen a pedazos (ejemplo: 3 pedazos)
ffmpeg -hide_banner -ss 0    -to 2.2 -i toma.mp4 -an -c:v libx264 -crf 18 v1.mp4
ffmpeg -hide_banner -ss 12.0 -to 14.0 -i broll.mp4 -an -vf "scale=1080:1920" -c:v libx264 -crf 18 v2.mp4
ffmpeg -hide_banner -ss 2.2  -to 6.0 -i toma.mp4 -an -vf "scale=1242:2208,crop=1080:1920" -c:v libx264 -crf 18 v3.mp4

# 3) Unir la imagen
printf "file 'v1.mp4'\nfile 'v2.mp4'\nfile 'v3.mp4'\n" > lista.txt
ffmpeg -hide_banner -f concat -safe 0 -i lista.txt -c copy imagen.mp4

# 4) Pegarle el audio continuo
ffmpeg -hide_banner -i imagen.mp4 -i voz.wav -map 0:v -map 1:a -c:v copy -c:a aac -shortest final.mp4
```

Ahí la imagen cambió tres veces y el audio nunca se partió. Eso es un L-cut hecho a mano, y es el
esqueleto del módulo `23`.

> ⚠️ Al crear `lista.txt` en Windows PowerShell, **no** uses `Add-Content -Encoding utf8`: mete un BOM
> (tres bytes invisibles al inicio del archivo) y ffmpeg falla con un error que no dice nada útil.
> Usa `printf` desde bash, o `-Encoding ascii`.

---

## 4. Match cut (corte por coincidencia)

**Qué es:** cortas de un plano a otro donde **algo coincide**: la forma, el movimiento, el color, la
posición en el cuadro. Un plato redondo corta a un reloj redondo. Una mano que baja corta a otra mano
que baja.

**Cuándo:** cuando quieres que dos ideas se relacionen sin explicarlo con palabras. Es el corte más
"de autor" de la lista y el que más impresiona cuando está bien hecho.

**Cómo encontrarlo:** no se inventa, se busca. Saca la grilla de fotogramas de todo tu material y busca
formas repetidas:

```bash
ffmpeg -hide_banner -i bruto.mp4 -vf "fps=2,scale=200:-1,tile=12x8" -frames:v 1 contactos.png
```

Con esa imagen encima de la mesa los match cuts aparecen solos.

**Advertencia honesta:** un match cut forzado se ve peor que un corte duro. Si lo tienes que explicar,
no funcionó.

---

## 5. Jump cut (corte de salto)

**Qué es:** cortas dentro del mismo plano, quitando un pedazo. La persona "salta" porque estaba en una
posición y de repente está en otra.

En cine clásico esto es un error. **En video para redes es el estándar** — es exactamente lo que hace
que un YouTuber hablando 8 minutos no se sienta eterno.

**Por qué funciona:** el espectador de 2026 lee el jump cut como "me están quitando la paja", no como
"esto está mal editado". Le agradeces al editor por no hacerte perder tiempo.

**Cuándo:** para quitar muletillas, respiraciones, pausas de pensar y frases repetidas. Ver módulo `25`.

**Cómo hacerlo menos brusco:** tres opciones, de menor a mayor esfuerzo:

1. Que el corte caiga **en una respiración**, no a mitad de palabra.
2. Meter un **punch-in** en el segundo pedazo: como el encuadre cambió, el salto se justifica visualmente
   y desaparece. Este es el truco (módulo `22`).
3. Tapar el salto con un **cutaway** de medio segundo.

---

## 6. Cutaway (plano de corte)

**Qué es:** un plano que NO es el principal, metido encima mientras la voz sigue. Estás hablando de tu
carta y aparece la carta.

**Cuándo:**
- Para **tapar un salto** (jump cut feo, error de continuidad, muletilla eliminada).
- Para **mostrar** lo que se está diciendo.
- Para **subir el pulso** sin grabar más talking head.

**Cuánto dura:** entre 1 y 2,5 segundos. Menos de 1 s no da tiempo a leer la imagen; más de 3 s y la
gente se olvida de quién estaba hablando.

**Regla de oro:** el cutaway va con **L-cut** — la voz nunca se corta. Si el audio también cambia,
dejó de ser cutaway y es un corte a otra escena.

---

## 7. Insert (inserto)

**Qué es:** primo cercano del cutaway, pero **dentro de la misma escena y del mismo espacio**: un primer
plano de las manos, del producto, de la pantalla del celular, del papel que la persona está firmando.

**Diferencia práctica con el cutaway:** el cutaway te saca de la escena (te lleva a otro lado); el
inserto te acerca **dentro de la escena**. El inserto no rompe continuidad; el cutaway sí puede.

**Cuándo:** siempre que se mencione un objeto concreto. Es el recurso que hace que un video de producto
se sienta profesional: nadie aguanta 30 segundos de alguien describiendo un producto sin verlo.

**Consejo de rodaje:** los insertos casi nunca se graban en el momento. Se graban después, aparte, en
30 segundos, cuando ya sabes qué te falta. Por eso el módulo `170` existe.

---

## 8. Corte por acción (cut on action)

**Qué es:** cortas **en medio de un movimiento**, no antes ni después. La persona empieza a levantar el
vaso en el plano A y termina de levantarlo en el plano B.

**Por qué es la técnica más útil de toda esta lista:** el ojo está siguiendo el movimiento y no tiene
capacidad libre para notar el corte. El corte desaparece. Es el mecanismo del "montaje invisible".

**Cuándo:** siempre que haya un movimiento disponible. Puerta que se abre, mano que se extiende, persona
que se sienta, cámara que barre.

**Cómo encontrar el punto exacto:** exporta los fotogramas del movimiento y elige a ojo.

```bash
ffmpeg -hide_banner -ss 5.0 -to 6.0 -i plano.mp4 -vf "fps=30" -q:v 2 frames/f_%03d.jpg
```

Treinta imágenes de un segundo de movimiento. Eliges el fotograma donde la acción está a la mitad y
cortas ahí. Ese número de fotograma se convierte en segundos: `5.0 + (numero_de_frame / 30)`.

---

## 9. Corte por mirada (eyeline match)

**Qué es:** la persona mira hacia algún lado; el plano siguiente muestra lo que está mirando.

**Por qué funciona:** una mirada fuera de cuadro abre una pregunta ("¿qué está viendo?") y el corte la
responde. Es el mismo mecanismo del bucle abierto (módulo `31`), pero a escala de un segundo.

**Cuándo:** cualquier video con una persona y un objeto. Es de lo más barato que existe y casi nadie
lo usa en redes.

**La regla que no se rompe:** si mira a la **derecha** del cuadro, el objeto tiene que aparecer en el
plano siguiente como si estuviera a la derecha. Si lo pones a la izquierda, el cerebro entiende que son
dos lugares distintos y se pierde. Eso es el **eje** (módulo `26`).

---

## 10. Tabla de decisión rápida

Cuando estés parado frente a un corte y no sepas cuál usar:

| Situación | Corte |
|---|---|
| Por defecto, no hay razón para otra cosa | **Duro** |
| Se siente entrecortado, quiero fluidez | **J-cut** |
| Hablan y quiero mostrar de qué hablan | **L-cut + cutaway** |
| Quité una muletilla y quedó un salto feo | **Jump cut + punch-in** |
| Se menciona un objeto concreto | **Insert** |
| Hay un movimiento en el plano | **Corte por acción** |
| Alguien mira algo fuera de cuadro | **Corte por mirada** |
| Dos ideas que quiero relacionar sin decirlo | **Match cut** |
| El video se siente lento y no tengo material | **Punch-in** (`22`) |
| Cambio de tema / de bloque completo | **Duro** + cambio de música o texto |

---

## 11. Los tres errores de ubicación

Más importante que el tipo de corte es **dónde cae**. Tres reglas duras:

1. **Nunca a mitad de palabra.** Se oye como un glitch y suena a amateur en medio segundo. Verifícalo
   contra la transcripción con timecodes, no de oído.
2. **Nunca en el silencio entre dos frases.** Suena a diapositiva. Corta **en la última sílaba** de la
   frase que termina o **en la primera** de la que empieza. Esa décima de segundo es toda la diferencia.
3. **Nunca justo antes del remate de un chiste o de un dato.** Cortar ahí le roba el impacto. El remate
   se dice completo en el mismo plano y el corte viene después.

---

## Errores comunes

1. **Cortar audio e imagen siempre juntos.** Es la causa número uno de que un video "no fluya". La
   solución no es más transiciones: son J-cuts y L-cuts.
2. **Poner una transición para tapar un corte que estaba mal ubicado.** El problema no era la falta de
   efecto: era que el corte caía en el silencio. Mueve el corte, quita el efecto.
3. **Usar cutaways solo para rellenar.** Un cutaway que no tiene nada que ver con lo que se dice
   distrae en vez de apoyar. Si no ilustra, no va.
4. **Match cuts forzados.** Dos círculos que no significan nada juntos no son un match cut, son una
   casualidad. Si lo tienes que señalar, no funcionó.
5. **Jump cuts sin punch-in.** Un jump cut a pelo se ve descuidado; con un 15% de acercamiento se ve
   intencional. Es la misma edición con dos lecturas distintas.
6. **Cortar por acción con el movimiento ya terminado.** El corte se tiene que comer el movimiento a la
   mitad. Si el plano A termina el gesto y el plano B lo repite, se ve doble y salta.
7. **Romper el eje en un corte por mirada.** Mira a la derecha y el objeto aparece a la izquierda: la
   escena deja de tener geografía y el espectador se desorienta sin saber por qué.
8. **Insertos demasiado largos.** Tres segundos de un primer plano de un producto quieto y la persona
   se olvidó de la escena. 1–2 s y de vuelta.

---

## Checklist

Antes de dar por buena la lista de cortes:

- [ ] Ningún corte cae **a mitad de palabra** (verificado contra transcripción con timecodes).
- [ ] Ningún corte cae **en el silencio muerto** entre frases.
- [ ] Al menos **un J-cut o L-cut** por cada 10 segundos, para que el montaje fluya.
- [ ] Cada **cutaway** ilustra algo que se está diciendo — ninguno es puro relleno.
- [ ] Cada **jump cut** está tapado con punch-in, cutaway o cae en una respiración.
- [ ] Cada objeto mencionado en la voz tiene su **inserto**.
- [ ] Donde hay movimiento, corté **por acción** (a mitad del gesto), no antes ni después.
- [ ] Los **cortes por mirada** respetan la dirección: mira derecha → objeto a la derecha.
- [ ] El **90% o más** de los cortes son duros; las transiciones están justificadas una por una.
- [ ] Ningún corte le roba el impacto a un remate, un dato o un chiste.

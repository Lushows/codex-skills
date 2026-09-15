# 361 — Anatomía de un gancho: seis ganchos desarmados plano a plano

> `30` te dio qué es un gancho y por qué funciona. Este módulo es el taller: seis ganchos abiertos en
> canal, con el reloj al lado, para que veas **en qué fotograma exacto pasa cada cosa**. Copiar la idea
> de un gancho no sirve; hay que copiar la **mecánica temporal**.

---

## La estructura interna de todo gancho que funciona

Un gancho no es una frase. Son **cuatro eventos** que ocurren en un orden fijo dentro de los primeros
1,5 segundos, y cada uno tiene un lugar:

| # | Evento | Cuándo | Qué hace |
|---|---|---|---|
| 1 | **Anclaje visual** | fotograma 0 | Da una razón para no seguir bajando el dedo |
| 2 | **Golpe de audio** | 0,10 – 0,35 s | Confirma que hay algo pasando; el oído llega después del ojo |
| 3 | **Declaración de conflicto** | 0,3 – 1,2 s | Dice qué está en juego. Es la promesa |
| 4 | **Primer corte** | 0,8 – 1,6 s | Prueba que el video se mueve. Renueva el permiso |

Si falta alguno, el gancho cojea:

- Sin **1**: el video no se ve, se oye. Ya lo saltaron.
- Sin **2**: parece muteado, o parece que no ha empezado.
- Sin **3**: es un comienzo bonito sin apuesta. Se ve 2 segundos y se sale.
- Sin **4**: el ojo detecta plano largo y se aburre en el segundo 3 (ver `365`).

Tu gramática medida —mediana de **2,93 s por plano**— es un problema justo aquí: **el primer plano no
puede durar 2,93 s.** El primer corte tiene que caer antes del segundo 1,6. Los planos largos empiezan
después, cuando ya te ganaste el derecho.

---

## Cómo se desarma un gancho (el método)

Para estudiar el gancho de cualquiera, tuyo o ajeno:

```bash
# tira de contactos de los primeros 2 segundos, 10 fotogramas por segundo, con reloj
ffmpeg -y -i referencia.mp4 -t 2 -vf \
"fps=10,scale=160:-1,drawtext=text='%{pts\:hms}':x=3:y=3:fontsize=13:fontcolor=yellow:box=1:boxcolor=black@0.6,tile=10x2" \
-frames:v 1 anatomia.png

# dónde están los cortes reales (cambios de plano)
ffprobe -v error -f lavfi "movie=referencia.mp4,select=gt(scene\,0.35)" \
  -show_entries frame=pkt_pts_time -of csv=p=0

# dónde entra el audio y con cuánta fuerza
ffmpeg -y -i referencia.mp4 -t 2 -af "astats=metadata=1:reset=5,ametadata=print:key=lavfi.astats.Overall.RMS_level" -f null -
```

Con eso llenas una tabla de cuatro columnas: **tiempo · imagen · audio · texto**. Esa tabla es el
gancho. Lo demás es opinión.

---

## Gancho 1 — La acusación (Bendita Pola, cerveza)

**Tipo:** hablado, conflicto contra una creencia del espectador.

| Tiempo | Imagen | Audio | Texto |
|---|---|---|---|
| 0,00 | Mano cerrando sobre la botella, ya en movimiento | silencio (2 fotogramas) | — |
| 0,07 | " | *chac* de la chapa saltando | — |
| 0,20 | " | "Estás tomando…" | — |
| 0,45 | Corte a cara, frontal, media sonrisa | "…la cerveza…" | **ESTÁS** |
| 0,60 | " | " | **TOMANDO** |
| 0,90 | " | "…equivocada." | **LA QUE NO ES** |
| 1,30 | Corte a la nevera con seis botellas | (música entra) | — |

**Por qué funciona:** el conflicto se declara contra *el espectador*, no contra un tercero. "Estás
tomando la que no es" obliga a comprobar. La palabra que cierra la acusación (`equivocada`) llega a los
0,9 s: dentro de la ventana. Y el primer corte cae a los 0,45 s, mucho antes de que el ojo se canse.

**Lo que se hizo en montaje y no se ve:** la toma original empezaba con él quieto diciendo "bueno,
entonces…". Se cortaron 1,4 s de adelante. El gancho estaba enterrado.

---

## Gancho 2 — El objeto raro (visual puro)

**Tipo:** visual. No hay voz en los primeros 2 segundos.

| Tiempo | Imagen | Audio | Texto |
|---|---|---|---|
| 0,00 | Un vaso de cerveza **boca abajo** sobre la barra, sin derramarse | ambiente del bar, alto | — |
| 0,50 | Corte cerrado al mismo vaso desde abajo | " | **BOCA** |
| 0,68 | " | " | **ABAJO** |
| 1,10 | Mano entra al cuadro y lo levanta 2 cm | *slurp* | — |
| 1,60 | Corte a cara del barman | "Esto no es un truco." | — |

**Por qué funciona:** una imagen imposible es una pregunta sin palabras. Nadie necesita entender el
idioma. Y la frase de los 1,6 s **no explica**: niega la explicación fácil, así que la pregunta sigue
abierta.

**Regla que sale de aquí:** cuando el gancho es visual, la primera frase hablada no debe resolver. Debe
**profundizar**.

---

## Gancho 3 — El número contra el sentido común

**Tipo:** texto + voz, dato.

| Tiempo | Imagen | Audio | Texto |
|---|---|---|---|
| 0,00 | Recibo de la caja registradora saliendo, ya en movimiento | *rrrrrt* de la impresora | — |
| 0,25 | " | "Este plato…" | **ESTE** |
| 0,40 | " | " | **PLATO** |
| 0,70 | Corte al plato, cenital | "…es el que más vendemos." | **EL QUE MÁS** |
| 0,90 | " | " | **VENDEMOS** |
| 1,25 | Corte a la cara | "Y el que nos está quebrando." | — |
| 1,60 | " | " | **NOS ESTÁ QUEBRANDO** |

**Por qué funciona:** la contradicción está *dentro* del gancho. La primera mitad establece una
expectativa normal (más vendido = bueno) y la segunda la rompe. El giro llega a 1,25 s.

**El error que casi se comete:** poner el giro a los 3 segundos, "para dar contexto". Habría muerto. El
contexto va después del giro, nunca antes.

---

## Gancho 4 — El medio de la acción (in medias res)

**Tipo:** visual, empezar por el desastre.

| Tiempo | Imagen | Audio | Texto |
|---|---|---|---|
| 0,00 | Espuma desbordándose de un vaso, cayendo por el borde | *pssshhh* | — |
| 0,30 | Corte a las manos limpiando rápido | ambiente | **OTRA VEZ** |
| 0,75 | Corte a cara, resignación | "Llevo tres años sirviendo mal." | — |
| 1,40 | " | " | **TRES AÑOS** |

**Por qué funciona:** empiezas después de que el problema ya ocurrió. El espectador tiene que
reconstruir qué pasó, y reconstruir es participar. Además la confesión ("llevo tres años sirviendo mal")
es alguien admitiendo algo en contra de sí mismo: eso se escucha.

**Lo que hace falta para que exista este gancho:** un bruto con el accidente adentro. Por eso se graba
antes de estar listo y se deja rodar la cámara.

---

## Gancho 5 — La pregunta con opciones a la vista

**Tipo:** texto principal, para ver sin sonido (ver `368`).

| Tiempo | Imagen | Audio | Texto |
|---|---|---|---|
| 0,00 | Dos vasos idénticos lado a lado en la barra | música ya en golpe | — |
| 0,20 | " | " | **UNO** |
| 0,38 | " | " | **CUESTA** |
| 0,56 | " | " | **EL TRIPLE** |
| 0,90 | Zoom brusco (corte, no animación) a los dos vasos | golpe | **¿CUÁL?** |
| 1,50 | Corte a la mano señalando uno | "Casi todo el mundo se equivoca." | — |

**Por qué funciona:** el espectador **elige mentalmente** antes del segundo 2. Quien eligió, se queda a
ver si acertó. Es el gancho más barato de producir de los seis: dos vasos y una mesa.

**Ojo con la variante rota:** "¿Sabías que…?" no es una pregunta con opciones. No obliga a elegir nada.
Ver `362`.

---

## Gancho 6 — La negación del clic (anti-gancho)

**Tipo:** hablado, contra la expectativa del formato.

| Tiempo | Imagen | Audio | Texto |
|---|---|---|---|
| 0,00 | Cara muy cerca, mirando a cámara, ya hablando | "No veas esto si…" | — |
| 0,55 | Corte a plano medio, brazos cruzados | "…vas a pedir domicilio hoy." | **NO VEAS ESTO** |
| 1,20 | Corte a la comida en la mesa | (música) | — |

**Por qué funciona:** filtra y provoca a la vez. Quien iba a pedir domicilio hoy se queda por
contradicción, y quien no, se queda por curiosidad.

**Por qué se quema rápido:** es una fórmula muy visible. Úsala una vez cada muchos videos o se convierte
en tic. Ver `362`.

---

## Los cuatro patrones que se repiten en los seis

1. **El fotograma 0 siempre tiene movimiento ya empezado.** Ninguno abre con alguien esperando.
2. **El primer corte cae entre 0,30 y 0,90 s.** Ninguno aguanta un plano de 2,93 s al inicio.
3. **El texto entra después del fotograma 3, nunca en el 0**, y en palabras sueltas de 1 a 3 sílabas.
4. **Ninguno resuelve.** Todos dejan algo pendiente, y ese pendiente se paga después (ver `364`).

---

## La plantilla en blanco

Para cada video, antes de montar, llena esto. Si no lo puedes llenar, no tienes gancho.

```
FOTOGRAMA 0    : ____________________  (qué se ve, en movimiento)
GOLPE DE AUDIO : ____________________  (a los ___ s)
CONFLICTO      : "___________________"  (termina antes de 1,2 s)
PRIMER CORTE   : a los ___ s
QUÉ QUEDA ABIERTO: ______________________
DÓNDE SE PAGA  : segundo ___
```

---

## Errores comunes

1. Copiar la frase del gancho de otro y no su estructura temporal. La frase sin el reloj no funciona.
2. Dejar que el primer plano dure lo mismo que los demás (2,93 s). El primer plano es la excepción de tu
   propia gramática.
3. Meter el contexto antes del conflicto: "en este video les voy a contar…". Eso es un comienzo, no un
   gancho.
4. Poner el giro después del segundo 2. Llega tarde a la única gente que importaba.
5. Que el gancho hablado y el texto en pantalla digan **lo mismo palabra por palabra**: se desperdicia
   un canal entero (ver `363`).
6. Un gancho visual que la primera frase hablada resuelve. Se cierra la pregunta antes de tiempo.
7. Cargar seis palabras en cascada en los primeros 0,5 s: no se alcanzan a leer y tapan la imagen.
8. Grabar el gancho al principio de la sesión, cuando todavía estás frío. El mejor gancho suele salir
   al final; grábalo aparte y móntalo delante.
9. No cortar el arranque muerto del bruto ("bueno, entonces…"). El gancho casi siempre está enterrado a
   1 o 2 segundos de donde crees.
10. Usar el mismo tipo de gancho en todos los videos. El feed te enseña a alguien varias veces; la
    fórmula repetida se detecta y se salta.
11. Prometer en el gancho algo que el video no va a pagar. Sube la vista y hunde la retención y la
    reputación de la cuenta.
12. No dejar por escrito qué gancho usaste, y no poder cruzarlo después con la tasa de salto (ver `369`).

---

## Checklist

- [ ] El fotograma 0 tiene movimiento ya empezado
- [ ] Hay golpe de audio antes de 0,35 s
- [ ] El conflicto queda declarado antes de 1,2 s
- [ ] El primer corte cae entre 0,30 y 0,90 s
- [ ] La primera palabra de texto entra después del fotograma 3
- [ ] Imagen, voz y texto dicen cosas distintas que suman, no la misma
- [ ] Queda algo abierto y sé en qué segundo se paga
- [ ] Desarmé mi propio gancho con la tira de contactos y llené la tabla de cuatro columnas
- [ ] El tipo de gancho es distinto al de mi video anterior
- [ ] Escribí en el diario qué gancho usé, para cruzarlo con los datos

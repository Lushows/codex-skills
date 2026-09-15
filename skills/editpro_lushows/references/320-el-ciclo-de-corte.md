# 320 — El ciclo de corte: qué es una unidad rítmica y cómo se encadena

**Qué resuelve:** el módulo `20` te dio el pulso —cuántos cambios visuales hay por segundo— y con eso
arreglas un video lento. Pero el pulso es un promedio, y un promedio no explica **por qué un plano de 4
segundos se siente eterno y otro de 4 segundos se siente corto**. Este módulo baja un nivel: deja de
contar cortes y empieza a mirar la unidad que hay *entre* dos cortes, cómo está construida por dentro, y
cómo se encadena con la siguiente.

Es la puerta del bloque 320–329. Todo lo demás del bloque (cadencia, aceleración, ruptura, sílaba, texto,
la regla de tres, medición, diagnóstico) opera sobre esta unidad.

---

## 1. Un plano no es un ciclo

Un **plano** es un dato técnico: el trozo de video entre dos cortes. Dura lo que dura.

Un **ciclo de corte** es un dato perceptual: el tiempo que el espectador tarda en **entrar, entender y
agotar** lo que ese plano tenía para darle. Termina cuando ya no hay nada nuevo que mirar.

Los dos números casi nunca coinciden, y toda la diferencia entre un montaje que respira y uno que
arrastra vive en esa brecha:

| Situación | Plano | Ciclo | Qué siente el espectador |
|---|---|---|---|
| Plano de 4,0 s, la información se agota en 1,8 s | 4,0 s | 1,8 s | **2,2 s de vacío.** "Se siente lento" |
| Plano de 1,2 s con tres cosas nuevas dentro | 1,2 s | ~2,5 s de contenido | **Atropellado.** "No alcancé a ver" |
| Plano de 2,9 s, la información se agota en 2,9 s | 2,9 s | 2,9 s | No siente nada. Está viendo el video |

**El objetivo del montaje rítmico es cerrar esa brecha, plano por plano.** No "cortar más rápido". Cortar
*cuando toca*.

> **Término nuevo — ciclo de corte:** el intervalo entre dos cortes, medido no por su duración sino por
> la vida útil de la información que contiene. Un plano cuya información se agotó ya terminó, aunque el
> video siga corriendo.

---

## 2. La anatomía interna: entrada, carga, salida

Todo ciclo tiene tres partes. Saber cuál es cuál es lo que te permite recortar sin romper.

```
│◄── ENTRADA ──►│◄──────── CARGA ────────►│◄── SALIDA ──►│
│   0,2–0,4 s   │      lo que importa     │   0–0,3 s    │
│  reconocer    │   la información nueva  │  soltar      │
```

**ENTRADA (0,2–0,4 s).** El tiempo que le toma al ojo entender *dónde está*. Cambió el encuadre, cambió
la luz, cambió el sujeto: hay un costo de reconocimiento y es real. Es lo que hace que un plano de 0,3 s
sea ilegible salvo que sea la repetición de algo que ya viste.

**CARGA.** La razón por la que ese plano existe. La cerveza que se sirve, la frase que se dice, el dato
que se revela, la cara que reacciona. Si no sabes decir en una frase cuál es la carga de un plano, ese
plano probablemente sobra.

**SALIDA (0–0,3 s).** El respiro después de que la carga se entregó. En un reel casi siempre vale **cero**:
cortas exactamente cuando la carga termina. La salida solo se justifica cuando quieres que algo repose
(ver `322`, desaceleración) o cuando el sonido todavía está terminando aunque la imagen ya no aporte.

### La prueba operativa para encontrar el final del ciclo

Congela el plano en el segundo que sospechas y pregúntate: **¿qué información nueva hay en pantalla desde
hace medio segundo?** Si la respuesta es "ninguna", el ciclo ya terminó ahí y todo lo que sigue es grasa.

Para hacerlo con evidencia y no de memoria, saca una tira del plano a 4 fotogramas por segundo:

```bash
# Un solo plano, del segundo 12,0 al 16,0, en tira de 16 imágenes
ffmpeg -hide_banner -y -ss 12.0 -t 4.0 -i bruto.mp4 \
  -vf "fps=4,drawtext=text='%{pts\:hms}':fontcolor=yellow:fontsize=22:box=1:boxcolor=black@0.6:x=6:y=6,scale=180:-1,tile=8x2" \
  -frames:v 1 -q:v 2 ciclo_12-16.jpg
```

Miras la tira de izquierda a derecha. **El primer par de imágenes prácticamente idénticas marca dónde
murió el ciclo.** Ese es tu punto de corte, no el que te sugirió el ojo mientras veías el video corriendo.

---

## 3. Los seis tipos de ciclo que usas de verdad

No todos los ciclos duran lo mismo porque no todos hacen el mismo trabajo. Estos son los seis que
aparecen en un reel de negocio local, con su duración natural.

| Tipo de ciclo | Qué hace | Duración natural | Cómo se sabe que terminó |
|---|---|---|---|
| **Frase** | alguien dice una idea completa | 1,5–3,5 s | terminó la unidad de sentido (ver `325`) |
| **Proceso** | una acción continua: servir, cocinar, montar | 1,5–3,0 s **acelerado** | terminó el movimiento, no la acción real (ver `201`) |
| **Revelación** | se muestra algo que no se sabía | 0,8–2,0 s | el ojo ya lo registró: ~0,6 s después de que entra |
| **Reacción** | una cara responde a algo | 0,6–1,2 s | el gesto llegó a su pico |
| **Dato** | un texto o número en pantalla que hay que leer | 0,9–1,8 s | tiempo de lectura + 0,3 s (ver `46`) |
| **Remate** | el cierre, el chiste, la frase final | 1,5–4,0 s | cuando el sonido termina, no antes (ver `33`) |

Estas duraciones no son objetivos: son **el rango donde suele caer la carga real**. Si un plano tuyo se
sale mucho del rango de su tipo, hay una razón —y si no la sabes decir, es grasa.

Fíjate que la mediana medida en tus 51 proyectos, **2,93 s por plano**, cae justo en el rango de "frase"
y "proceso", que es exactamente lo que grabas: gente hablando y cosas pasando en el bar. No es
casualidad; es que tu gramática ya está calibrada al contenido que produces.

---

## 4. Cómo se encadenan: frases rítmicas

Los ciclos no viven sueltos. Se agrupan en **frases rítmicas** de 2 a 5 ciclos, y la frase es la unidad
que el espectador realmente percibe.

```
CICLO   CICLO   CICLO        CICLO CICLO CICLO CICLO      CICLO
├─────┤ ├────┤ ├──────┤      ├──┤ ├──┤ ├─┤ ├──┤           ├──────────┤
└──── FRASE 1 ────────┘      └───── FRASE 2 ─────┘        └─ FRASE 3 ┘
   presentación                   la ráfaga                el respiro
```

Hay tres formas honestas de encadenar dos ciclos, y solo tres:

**1. Encadenado por continuidad.** El segundo ciclo continúa físicamente al primero: la mano que agarra
el vaso → el vaso que llega a la mesa. El corte es invisible porque la acción no se interrumpe. Es lo que
`324` llama cortar sobre movimiento.

**2. Encadenado por consecuencia.** El segundo ciclo es la respuesta al primero: la frase → la cara del
que la escucha. El corte se nota pero se justifica solo.

**3. Encadenado por contraste.** El segundo ciclo choca con el primero a propósito: el local vacío → el
local lleno. El corte se nota **y esa es la idea**. Es donde vive el chiste, el antes/después y el remate.

Si un corte tuyo no es ninguna de las tres, es un corte "porque sí" — y esos son los que hacen que un
video se sienta arbitrario aunque cada plano por separado esté bien. Ver `21` para el catálogo de tipos
de corte y `26` para continuidad.

---

## 5. Por qué el corte duro es tu unidad correcta

En 51 proyectos tuyos hay **una sola transición**. Eso, que podría parecer una carencia, es en realidad
la decisión estilística correcta para el formato, y conviene entender por qué en términos de ciclo:

Una transición **estira la entrada del ciclo siguiente**. Un fundido de 0,5 s significa que durante medio
segundo el espectador no está mirando ni el plano A ni el plano B: está mirando una mezcla que no contiene
información. En un reel de 22 segundos, medio segundo es el 2,3% del video gastado en nada.

El corte duro tiene entrada de **cero**: el fotograma siguiente ya es el plano nuevo, completo y legible.

> **Regla:** la transición solo se justifica cuando el salto de contexto es tan grande que el corte duro
> se leería como error, o cuando la transición *es* el contenido (una transición de marca, ver `52`). En
> todo lo demás, el corte duro gana por definición. Ver `50`.

---

## 6. El ritmo no es lo más importante, y hay que decirlo

Walter Murch, en *In the Blink of an Eye*, ordenó por importancia los seis criterios para decidir dónde
cortar y les puso peso: **emoción 51%, historia 23%, ritmo 10%**, y por debajo el recorrido del ojo (7%),
el plano bidimensional de la pantalla (5%) y el espacio tridimensional de la acción (4%).

Es una lista de prioridades, no una fórmula medida en laboratorio: Murch la propuso como criterio de
oficio. Pero el orden importa y es un antídoto contra este bloque entero: **si por cuadrar el ritmo tienes
que sacrificar el momento donde la persona se ríe de verdad, sacrificas el ritmo.** Siempre.

La forma sana de leer los módulos 320–329 es: el ritmo es la décima parte de la decisión, pero es la
décima parte que **sí se puede medir y arreglar en frío**. Por eso vale la pena estudiarla. No porque sea
lo más importante.

---

## 7. El procedimiento, en cinco pasos

Esto es lo que haces un domingo, con el celular y CapCut, sobre un reel ya armado:

1. **Nombra la carga de cada plano.** Una frase por plano, escrita. Si no puedes nombrarla, marca el
   plano con una X.
2. **Borra los X.** No los acortes: bórralos. Un plano sin carga no mejora recortado.
3. **Clasifica cada plano restante** en uno de los seis tipos de la tabla de la sección 3.
4. **Compara la duración real contra el rango del tipo.** Los que se pasan por más de 1 segundo son tus
   candidatos a recorte. Empieza por el más largo: casi siempre uno o dos planos explican toda la
   sensación de lentitud (ver `27`).
5. **Recorta por el final, no por el principio.** La entrada del ciclo es cara y no se puede comprimir;
   la salida casi siempre vale cero. Ver `321` antes de tocar nada.

Ese proceso, en un reel de 8 planos, toma quince minutos y suele quitar entre 2 y 4 segundos de grasa.

---

## Errores comunes

1. **Confundir plano con ciclo.** Medir duraciones y no preguntarse nunca cuánto duró la información. Un
   video de planos cortos puede ser lentísimo si todos los planos están vacíos.
2. **Recortar por el principio.** Te comes la entrada, el espectador no alcanza a reconocer dónde está, y
   el plano queda ilegible aunque el número de segundos mejore.
3. **Dejar la salida "por si acaso".** El famoso medio segundo de más al final de cada plano. Ocho planos
   × 0,5 s = 4 segundos de grasa en un reel de 22. Es la causa #1 de lentitud.
4. **Planos sin carga que sobreviven porque "se ven bonitos".** Si no puedes nombrar qué información nueva
   entrega, no importa lo bien fotografiado que esté.
5. **Meter dos cargas en un plano corto.** El espectador procesa una a la vez. Dos cosas nuevas en 1,2 s
   es una que se pierde. Sepáralas en dos ciclos.
6. **Poner transición para "suavizar" un corte que se siente feo.** El corte no se siente feo por falta de
   transición: se siente feo porque el encadenado no es continuidad, consecuencia ni contraste. Arregla la
   causa.
7. **Tratar todos los ciclos como si duraran lo mismo.** Una reacción no dura lo que una frase. Ver `329`.
8. **Cortar antes de que termine el sonido del remate.** El ciclo del remate lo cierra el audio, no la
   imagen. Es el defecto #3 del módulo `98`, y es el que más caro sale.
9. **Optimizar ritmo destruyendo emoción.** Si el corte "perfecto" te obliga a cortar la risa real por la
   mitad, el corte perfecto está mal. 51% contra 10%.
10. **Medir el ciclo mientras el video corre.** A velocidad normal tu cerebro rellena los huecos. Los
    huecos se ven en la tira de fotogramas, congelados.
11. **Creer que este análisis reemplaza al oído.** Es el paso previo. La decisión final se toma
    reproduciendo el video completo, a velocidad normal, en un celular (ver `98`, punto 15).

---

## Checklist

- [ ] Puedo nombrar en una frase la **carga** de cada plano del corte
- [ ] Ningún plano marcado con X sobrevivió al corte final
- [ ] Cada plano está clasificado en uno de los **seis tipos de ciclo**
- [ ] Ningún plano se pasa más de 1 s del rango natural de su tipo sin una razón que sé decir
- [ ] Saqué la **tira a 4 fps** de los dos planos más largos y confirmé dónde muere la información
- [ ] Recorté por el **final** de cada plano, nunca por el principio
- [ ] Cada corte se explica por **continuidad, consecuencia o contraste** — ninguno es "porque sí"
- [ ] Los planos están agrupados en **frases de 2 a 5 ciclos** y sé cuál es cuál
- [ ] No hay ninguna transición que no esté justificada por salto de contexto o por marca
- [ ] El ciclo del **remate** termina cuando termina el sonido, no cuando termina la imagen
- [ ] Ninguna decisión de ritmo se comió un momento emocional real
- [ ] Vi el resultado completo, a velocidad normal, en el celular

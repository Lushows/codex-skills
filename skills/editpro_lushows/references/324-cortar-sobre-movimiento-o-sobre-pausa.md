# 324 — El corte sobre movimiento vs. el corte sobre pausa

**Qué resuelve:** dos cortes en el mismo video, hechos con el mismo cuidado, y uno se siente invisible y el
otro se siente como un tropiezo. La diferencia casi nunca es el encuadre ni el color: es **qué estaba
pasando en la imagen en el fotograma exacto del corte**.

Este módulo es el más "de manos" del bloque. Es la decisión que tomas doscientas veces por reel sin darte
cuenta, y la única del bloque que tiene investigación seria detrás.

---

## 1. Los dos estados de un plano

En cualquier momento, un plano está en uno de dos estados:

- **En movimiento** — algo se desplaza: una mano, la cámara, un líquido, una cabeza que gira.
- **En reposo** — el encuadre está estable y nada cambia de posición.

Y hay una asimetría fuerte entre cortar en uno o en otro:

| | Cortar sobre movimiento | Cortar sobre pausa |
|---|---|---|
| Se percibe el corte | poco o nada | mucho |
| Sensación | fluidez, continuidad | puntuación, capítulo |
| Riesgo | que la acción no case y se sienta un salto | que se sienta lento y entrecortado |
| Para qué sirve | avanzar sin que se note | separar ideas, marcar un antes/después |
| Dónde va | dentro de una frase rítmica | **entre** frases rítmicas (`320` §4) |

Los dos son correctos. Lo que está mal es no elegir.

---

## 2. La investigación: por qué el movimiento esconde el corte

Esto no es folclore de editores. Tim Smith (Birkbeck, Universidad de Londres) lo midió.

En sus trabajos sobre **edit blindness** —la incapacidad de detectar un corte aunque estés mirando la
pantalla— y en su *Attentional Theory of Cinematic Continuity* (AToCC, 2012), los resultados relevantes
para nosotros son:

- Los cortes que respetan las reglas de continuidad **se detectan menos** que los que no las respetan.
- Alrededor de **una cuarta parte** de los cortes que unen dos vistas de la misma escena pasa sin ser
  detectada por el espectador.
- Esa proporción sube a **cerca de un tercio** cuando el corte **coincide con el inicio súbito de un
  movimiento**.
- Parte de esos cortes se pierden porque coinciden con parpadeos o con movimientos sacádicos del ojo, pero
  la mayoría se pierden por **ceguera por inatención**: el espectador está atendiendo a la narración, no a
  la película.

La lectura práctica es directa y bastante fuerte: **el movimiento no "disimula" el corte por una cuestión
estética; captura la atención del ojo hacia un punto concreto de la pantalla, y mientras el ojo persigue
ese punto, el cambio de encuadre no se registra.**

Y el corolario que casi nadie aplica: **si quieres que el corte SE NOTE, corta en reposo.** Un corte
visible es una herramienta, no un defecto. Es el punto y aparte del montaje.

---

## 3. Dónde exactamente, dentro del movimiento

No es "cortar mientras algo se mueve". Es cortar en un punto específico de la curva del movimiento.

```
             ┌── pico
             │
velocidad    │
del          │        ▲ ZONA BUENA: primer tercio de la aceleración
movimiento   │      ╱ │
             │    ╱   │
             │  ╱     │        ╲
             │╱       │          ╲___
             └────────┴──────────────► tiempo
              inicio  pico       final
                ▲
                └── ZONA ÓPTIMA: 20–35% del recorrido
```

**La regla del primer tercio:** el corte cae cuando el movimiento **ya arrancó pero no llegó al pico**.
Entre el 20% y el 35% del recorrido total de la acción.

Por qué ahí y no en el pico: en el pico el ojo ya está siguiendo la trayectoria y **predice** dónde va a
estar el objeto. Si el plano nuevo no lo pone ahí, la predicción falla y el corte salta. Al 25%, el ojo
todavía está enganchándose y la predicción es débil.

### El solapamiento en fotogramas

Cuando cortas de un plano abierto a uno cerrado en medio de una acción, el plano nuevo debe **repetir**
un poco de la acción, porque el ojo necesita 0,1–0,15 s para reconocer el encuadre nuevo:

| Salto de encuadre | Solapamiento a 30 fps | En segundos |
|---|---|---|
| Cerrado → cerrado, mismo eje | 0–1 fotograma | ~0,03 s |
| Abierto → cerrado (punch-in, `22`) | 2–3 fotogramas | ~0,08 s |
| Abierto → muy cerrado (detalle) | 3–4 fotogramas | ~0,12 s |
| Cambio de locación con acción similar | 4–6 fotogramas | ~0,17 s |

Repetir 3 fotogramas de acción se siente **más continuo** que cortar exacto, aunque técnicamente sea un
error de continuidad. En reel vertical, con un solo celular, es la diferencia entre un corte que fluye y
uno que da un tirón.

**En CapCut:** después de hacer el corte, arrastra el punto de entrada del clip siguiente 2–3 fotogramas
hacia atrás. Con el zoom de la línea de tiempo al máximo, es un arrastre de un milímetro. Ver `214`.

---

## 4. Encontrar el movimiento con datos, no con el ojo

El ojo es malísimo para localizar el fotograma exacto donde arranca un movimiento. Esto no:

```bash
# Curva de movimiento fotograma a fotograma de un plano
ffmpeg -hide_banner -i plano.mp4 -vf \
 "format=gray,tblend=all_mode=difference,signalstats,metadata=print:key=lavfi.signalstats.YAVG:file=mov.txt" \
 -an -f null -

# Convertir a "tiempo <TAB> movimiento"
awk -F'[: =]+' '/pts_time/{t=$(NF)} /YAVG/{printf "%.3f\t%.3f\n", t, $NF}' mov.txt > curva.tsv
```

`tblend=all_mode=difference` construye un fotograma que es la diferencia entre el actual y el anterior;
`signalstats` mide su brillo promedio. **Más brillo = más cambió la imagen = más movimiento.** Es una
medida cruda pero muy útil y no cuesta nada.

Cómo leerla:

```bash
# Los 10 momentos de más movimiento del plano
sort -k2 -nr curva.tsv | head -10 | sort -n

# Dónde ARRANCA un movimiento: primer fotograma que supera 3x el reposo
awk 'NR<=15{base+=$2; n++} NR==15{umbral=(base/n)*3}
     NR>15 && $2>umbral {printf "arranque de movimiento en t=%.2f s\n", $1; exit}' curva.tsv
```

Ese `t` es tu punto de partida. El corte va **0,1–0,2 s después** (el 20–35% del recorrido).

Ojo con dos falsos positivos que esta medida tiene siempre:

- **Cambios de luz.** Una nube, un flash, alguien que enciende algo: sube el valor sin que nada se mueva.
- **Grano y compresión.** En material oscuro de celular, el ruido eleva el piso. Por eso el umbral se
  calcula contra el reposo del propio plano y no contra un número fijo.

Para el reposo, la operación inversa:

```bash
# Los tramos más quietos: candidatos a corte sobre pausa
sort -k2 -n curva.tsv | head -20 | sort -n
```

---

## 5. Cuándo cortar sobre pausa (y hacerlo bien)

El corte sobre reposo se ve. Úsalo cuando quieres que se vea:

| Situación | Por qué en pausa |
|---|---|
| Cambio de tema o de bloque | El corte visible funciona como punto y aparte |
| Antes de la ruptura de patrón (`323`) | El freno necesita entrar limpio, no colado |
| Antes y después del remate | El remate no debe "fluir": debe llegar |
| Entre dos ideas del guion | El espectador necesita cerrar una antes de abrir otra |
| Antes/después (`155`) | El salto **es** el contenido. Que se note |

Tres reglas para que un corte sobre pausa no se sienta a error:

1. **Que la pausa sea de verdad.** Al menos 4–5 fotogramas de quietud a cada lado del corte. Cortar en un
   micro-reposo entre dos movimientos es lo peor de los dos mundos.
2. **Que el sonido lo respalde.** Un corte visible sin evento sonoro se siente huérfano. Un golpe suave, un
   corte de música, el arranque de una frase: algo tiene que pasar en el audio en ese fotograma (`76`).
3. **Que el plano siguiente sea claramente distinto.** Si cortas en reposo a un encuadre parecido, no es
   puntuación: es un salto de continuidad y se lee como error.

---

## 6. El caso especial de tu estilo: el jump cut sobre la misma persona

Tu formato dominante es alguien hablando, en el mismo encuadre, con cortes duros que quitan las pausas.
Ahí no hay movimiento que aprovechar ni reposo que respetar: hay una persona hablando.

Ese corte se rige por **otra** regla, y es la del módulo `325`: el punto lo manda la sílaba, no el
movimiento. Pero hay dos cosas de este módulo que sí aplican y que arreglan el 80% de los jump cuts feos:

- **La cabeza.** Si en el fotograma antes del corte la cabeza está inclinada a la izquierda y en el
  siguiente a la derecha, el salto se ve muchísimo. Busca dos puntos donde la posición de la cabeza sea
  parecida, aunque eso te desvíe 0,2 s del punto ideal. Vale más que la precisión.
- **El punch-in de rescate.** Si no consigues dos posiciones parecidas, **cambia el tamaño de plano** en el
  corte: escala el clip siguiente al 112–118% (`22`). El cambio de encuadre justifica el salto de posición
  y el corte deja de leerse como error. Es la solución más usada y la más barata.

---

## Errores comunes

1. **Cortar en el pico del movimiento.** El ojo ya predice la trayectoria y el corte salta. Al 20–35%,
   no al 100%.
2. **Cortar exacto sin solapamiento.** En un cambio de tamaño de plano, cortar "perfecto" se siente como un
   tirón. Repite 2–3 fotogramas.
3. **Solapar demasiado.** Más de 6 fotogramas y se ve la acción repetida. Se nota más que el error que
   estabas evitando.
4. **Creer que cortar sobre movimiento sirve siempre.** Cuando quieres puntuación, el movimiento te la
   roba: el corte se vuelve invisible justo donde querías que se viera.
5. **Cortar en un micro-reposo entre dos movimientos.** No es reposo ni es movimiento. Es el peor punto
   posible.
6. **Buscar el arranque del movimiento a ojo, reproduciendo el video.** A 30 fps el arranque dura 2
   fotogramas. Usa la curva.
7. **Confundir cambio de luz con movimiento en la curva.** Un flash sube el YAVG sin que nada se mueva.
   Cruza siempre con la hoja de contactos (`17`).
8. **Jump cut sin mirar la posición de la cabeza.** Es la causa número uno de jump cuts que se sienten
   amateur, y se arregla eligiendo otro punto o metiendo punch-in.
9. **Corte visible sin nada en el audio.** El silencio en el corte hace que se lea como error de montaje.
10. **Usar transición para tapar un corte que casaba mal.** El problema es el punto de corte. Muévelo 3
    fotogramas y prueba otra vez antes de tapar nada (`50`).
11. **Aplicar la regla del primer tercio a un movimiento de cámara en vez de a la acción.** Si la cámara se
    mueve y el sujeto no, el ojo sigue al sujeto. La curva que importa es la del sujeto.
12. **Tratar el hallazgo de edit blindness como permiso para cortar mal.** Que una cuarta parte de los
    cortes pase inadvertida no significa que los tuyos vayan a pasar: significa que los que respetan
    continuidad pasan más.

---

## Checklist

- [ ] Para cada corte sé si lo quise **invisible** o **visible**
- [ ] Los cortes invisibles caen sobre movimiento, en el **primer tercio** del recorrido
- [ ] Los cambios de tamaño de plano tienen **2–4 fotogramas de solapamiento**
- [ ] Los cortes visibles caen en reposo real, con **≥4 fotogramas de quietud** a cada lado
- [ ] Cada corte visible tiene un **evento sonoro** que lo respalda
- [ ] Saqué la **curva de movimiento** de los planos donde el corte no me convencía
- [ ] En los jump cuts sobre la misma persona, la **posición de la cabeza** casa, o hay punch-in
- [ ] Ningún corte se "arregló" metiendo una transición sin haber probado moverlo
- [ ] Verifiqué el corte a velocidad normal, no fotograma a fotograma
- [ ] Ningún corte sobre movimiento partió una palabra (`325` manda sobre este módulo)

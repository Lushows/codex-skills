# 329 — El error de cortar cada X segundos por regla fija

**Qué resuelve:** el consejo más repetido de internet sobre edición de video corto es "corta cada 2
segundos" —o cada 3, o cada 1,5, según quién lo diga— y es el consejo que más videos ha arruinado. Este
módulo desmonta de dónde salió, por qué falla mecánicamente, en qué casos concretos sí es legítimo un
intervalo fijo, y con qué se reemplaza.

Es el módulo de cierre del bloque 320–329 porque es el antídoto contra usar mal todos los anteriores.

---

## 1. El mito de los 8 segundos, y por qué importa

Casi toda la regla del intervalo fijo se apoya, directa o indirectamente, en una cifra: que la atención
humana dura 8 segundos, menos que la de un pez dorado.

**Es falso, y el rastro está documentado.**

- La cifra se popularizó con un informe de consumidores de **Microsoft Canadá (2015)** que decía que la
  atención había bajado de 12 segundos en el año 2000 a 8 en 2013.
- Ese informe **no midió eso**. La cifra estaba tomada de un sitio web llamado **Statistic Brain**, que
  agregaba estadísticas sin fuentes primarias verificables. Al rastrear el origen no aparece un estudio:
  aparece, en el mejor de los casos, material de analítica web sobre cuánto tardaba gente en abandonar
  páginas que no le gustaban.
- El dato del pez dorado (9 segundos) tampoco tiene respaldo. Hay trabajo experimental que muestra
  memoria de peces a escala de días y meses.
- Los investigadores de atención llevan años señalando el problema de fondo: **"la atención" no es una
  cantidad única que se mida en segundos.** Depende de la tarea, la motivación, el contenido y el contexto.
  No existe "el número" de la atención humana.

Y hay una refutación que no necesita ninguna cita: **la gente ve películas de dos horas, partidos
completos y pódcast de cuarenta minutos.** Si la atención durara 8 segundos, nada de eso existiría. El
módulo `359` lo lista entre las señales de que una guía no verificó nada; aquí está el rastro completo.

Lo que sí es cierto, y es otra cosa completamente distinta: **la decisión de quedarse o irse se toma
rápido**, sobre todo en un feed donde hay costo cero en irse. Eso justifica invertir en el gancho (`30`,
`140`). No justifica cortar cada 2 segundos durante todo el video.

> **La confusión que hay que romper:** "decide rápido si se queda" ≠ "no puede prestar atención más de X
> segundos". La primera es cierta y es sobre el arranque. La segunda es falsa y es sobre todo el video.

---

## 2. Qué dicen las plataformas, de verdad

Ni Meta ni TikTok publican una recomendación de cortes por minuto ni de duración de plano. Lo que publican
es guía sobre el gancho, el formato vertical, el sonido y la duración total de la pieza. **Todo número de
cadencia de corte que veas atribuido a una plataforma viene de un blog de agencia, no de la plataforma.**

Eso no significa que esos números sean inútiles: significa que son **observaciones de terceros sobre lo que
les funcionó a ellos**, y que la única forma de saber si aplican a tu bar en Tocancipá es medirlo en tus
propios videos (`304`, `328` §5).

---

## 3. Los cuatro daños concretos del intervalo fijo

No es que el intervalo fijo sea "poco creativo". Es que rompe cosas medibles.

### Daño 1 — Fabrica el metrónomo

Un intervalo fijo produce dispersión ≈ 1,0 (`321`). El patrón se aprende en tres o cuatro repeticiones,
deja de dar información, y a partir de ahí el ritmo es fondo. Además hace imposible la ruptura (`323`),
porque no queda ningún contraste disponible: si todo dura igual, nada puede destacar.

### Daño 2 — Corta dentro de las palabras

Un corte colocado por reloj cae donde caiga. En español una sílaba dura 4 o 5 fotogramas (`325`), así que
la probabilidad de aterrizar en medio de una palabra es alta. Es literalmente el defecto #2 documentado en
`98`: *"las principales carac—"*. El comando corrió sin errores y el video quedó roto.

### Daño 3 — Ignora el movimiento

El corte cae al azar sobre movimiento o sobre reposo (`324`). Unos cortes serán invisibles y otros
saltarán, sin ninguna relación con lo que el video quería decir en ese momento. El resultado es un montaje
que se siente **inconsistente**, que es peor que uno que se siente lento.

### Daño 4 — Desacopla el corte del contenido

Este es el daño de fondo. Un corte es una afirmación: *lo que sigue es más importante que lo que había*. Si
los cortes suceden por reloj, esa afirmación se vuelve ruido y el espectador deja de leerla. Pierdes la
herramienta entera, no solo unos cuantos cortes.

---

## 4. La regla correcta

> **Cortas cuando el ciclo termina, no cuando el reloj lo dice.**

Y el ciclo termina cuando se agotó la información del plano (`320` §2). Ese es el criterio, y es de
contenido, no de tiempo.

El papel correcto del número es otro, y es la formulación que hay que memorizar:

> **El número es una VERIFICACIÓN, no una INSTRUCCIÓN.**

| | Instrucción (mal) | Verificación (bien) |
|---|---|---|
| Cuándo se usa | mientras montas | **después** de montar |
| Qué hace | dicta dónde cae el corte | te avisa de que algo se salió de rango |
| Qué pasa si no cuadra | fuerzas el corte | **investigas por qué** |
| Ejemplo | "corta cada 2,9 s" | "mi mediana salió 4,1 s; ¿qué plano me está arrastrando?" |

Tu mediana de 2,93 s es un resultado de tu gramática, no un objetivo. Si un reel tuyo sale con mediana
2,1 s porque el contenido lo pedía, está bien. Si sale con 4,8 s, eso es una **alarma que te manda a mirar
el video**, no una orden de cortar más.

---

## 5. Los tres casos donde el intervalo fijo sí es legítimo

### Caso A — El intervalo lo pone la música, no un reloj

Si cortas al compás, el intervalo no es arbitrario: sale del material. Es la única fuente honesta de
regularidad.

```
duración del pulso  = 60 / BPM
duración del compás = 60 / BPM × 4      (en 4/4)
```

| BPM | Pulso | Compás | Cortes cada 2 compases |
|---|---|---|---|
| 90 | 0,667 s | 2,67 s | 5,33 s |
| 100 | 0,600 s | 2,40 s | 4,80 s |
| 120 | 0,500 s | 2,00 s | 4,00 s |
| 128 | 0,469 s | 1,88 s | 3,75 s |
| 140 | 0,429 s | 1,71 s | 3,43 s |

Fíjate que con música a 100–120 BPM, cortar cada compás da **2,0–2,4 s**, sospechosamente cerca de tu
mediana. No es coincidencia: la música de reel vive en ese rango y el montaje se acopla a ella.

Y aun así: **cortar en cada compás durante 25 segundos vuelve a ser un metrónomo.** Lo que se hace es
cortar *en* compases, pero no en *todos*: 1 compás, 1 compás, 2 compases, medio compás. La rejilla la pone
la música; la selección la pones tú. Ver `24`.

### Caso B — El primer armado

Repartir el material en trozos iguales para ver qué hay es un procedimiento válido de armado bruto. Lo que
no es válido es publicarlo así. El primer armado se hace por reloj; el corte se hace por contenido.

### Caso C — Montaje sin habla, generado en lote

Un lapso de tiempo, una secuencia de fotos, un montaje de b-roll sin voz: ahí no hay sílabas que romper ni
sentido que respetar, y un intervalo regular con variación programada es aceptable. Sigue necesitando
ruptura, así que ni siquiera ahí es completamente fijo:

```bash
# Montaje de b-roll con duraciones variadas por diseño, no por reloj
DURS=(1.2 1.2 1.2 3.0 0.9 0.9 0.9 2.6)   # RRRL RRRL, no todo igual
i=0; > lista.txt
for f in broll/*.mp4; do
  d=${DURS[$((i % ${#DURS[@]}))]}
  ffmpeg -hide_banner -y -ss 0.5 -t "$d" -i "$f" -an -c:v libx264 -crf 18 "corte_$i.mp4" -loglevel error
  echo "file 'corte_$i.mp4'" >> lista.txt
  i=$((i+1))
done
ffmpeg -hide_banner -y -f concat -safe 0 -i lista.txt -c copy montaje.mp4
```

Ese arreglo `1,2 · 1,2 · 1,2 · 3,0` es la ráfaga-más-ruptura de `323` escrita como datos. Es lo mínimo que
debe tener un montaje automatizado para no salir plano.

---

## 6. El caso especial: pedirle un corte a un modelo

Cuando le pides a una IA que monte, la tentación es dar una regla de tiempo porque es lo más fácil de
expresar. **Es exactamente cómo se producen los cuatro defectos documentados en `98`.**

| Instrucción mala | Instrucción buena |
|---|---|
| "corta cada 2 segundos" | "corta al final de cada frase; usa los timecodes por palabra de la transcripción" |
| "haz 10 planos de 2,5 s" | "usa estos 10 tramos, definidos por sus segundos de inicio y fin, tomados de la transcripción" |
| "que dure 25 segundos" | "prioriza estas 3 ideas; si sobra tiempo, quita la tercera entera, no recortes las otras" |
| "acelera el final" | "los 4 planos antes del remate con ratio 0,78 sobre el anterior, **sin partir palabras**" |

Y después, siempre, el bucle de verificación de `98`. Un montaje calculado que no se ha oído no es un
montaje: es una hipótesis.

---

## 7. El procedimiento de reemplazo, completo

1. **Transcribe con timecodes por palabra** (`13`, `124`). Sin esto, todo lo demás es adivinar.
2. **Marca los límites de sentido:** dónde termina cada idea. Esos son tus candidatos a corte (`325` §3).
3. **Corta por contenido:** cada plano termina cuando su carga se agota (`320`).
4. **Coloca cada corte al fotograma** según movimiento o pausa (`324`).
5. **Mide** (`328`). Mediana, dispersión, patrón R/N/L.
6. **Si un número está fuera de rango, ve a mirar el video**, no a mover cortes. Casi siempre es un plano
   concreto.
7. **Construye la rampa y la ruptura a propósito** (`322`, `323`), que es lo que un intervalo fijo nunca te
   va a dar.
8. **Verifica el audio** (`98`). Ninguna palabra partida sobrevive.

---

## Errores comunes

1. **Repetir el dato de los 8 segundos.** No tiene fuente primaria; el rastro termina en un agregador sin
   estudio detrás. Y la gente ve pódcast de 40 minutos.
2. **Confundir "decide rápido si se queda" con "no puede atender".** Lo primero justifica invertir en el
   gancho; no justifica cortar cada 2 segundos durante todo el video.
3. **Atribuir a Meta o TikTok un número de cadencia de corte.** No lo publican. Viene de blogs.
4. **Usar la mediana como objetivo en vez de como verificación.** El número describe lo que hiciste; no
   decide lo que debes hacer.
5. **Forzar un corte para cuadrar una duración objetivo, partiendo una palabra.** La sílaba gana siempre
   (`325`).
6. **Cortar en todos los compases de la música.** La rejilla musical es una fuente honesta de intervalos,
   pero usarla entera te devuelve al metrónomo.
7. **Publicar el primer armado.** El armado por reloj es un paso de trabajo, no un entregable.
8. **Automatizar un montaje con duraciones todas iguales.** Si lo generas por código, escribe la variación
   y la ruptura en los datos.
9. **Pedirle a un modelo "corta cada X segundos".** Produce exactamente los defectos de `98`, con código de
   salida 0.
10. **Copiar la cadencia de un reel ajeno que funcionó.** Mediste su gramática, no la causa de su
    resultado (`328` §5).
11. **Creer que un ritmo rápido compensa un contenido vacío.** Cortar más rápido un video sin nada que
    decir solo hace que el vacío llegue antes.
12. **Aplicar tu propia mediana a un formato distinto.** Un tutorial de 3 minutos y un reel de 20 segundos
    no comparten gramática, aunque los grabe la misma persona con el mismo celular.

---

## Checklist

- [ ] Ningún corte de este video existe porque "tocaba cortar"
- [ ] Todos los cortes están colocados sobre **límites de sentido** de la transcripción
- [ ] Ningún corte partió una palabra, verificado con el bucle de `98`
- [ ] Cada corte cayó a propósito sobre **movimiento** o sobre **pausa** (`324`)
- [ ] Medí **después** de montar, y usé los números como alarma, no como orden
- [ ] Si algún número salió fuera de rango, fui a mirar el video y encontré el plano culpable
- [ ] La rampa y la ruptura están puestas **a propósito**, no salidas por casualidad
- [ ] Si usé la rejilla musical, **no** corté en todos los compases
- [ ] Si automaticé el montaje, la variación y la ruptura están escritas en los datos
- [ ] No repetí a nadie el dato de los 8 segundos
- [ ] Tengo mi propio archivo de referencias medido sobre mis propios videos (`328` §5)

# 470 — Cuántos efectos por minuto

> **Un presupuesto de efectos es una tasa, no un total.** «Este vídeo lleva ocho efectos» no dice nada:
> ocho en cuarenta segundos es una discoteca y ocho en doce minutos es un documental sobrio. Lo que se
> presupuesta es **cuántos efectos por minuto**, y ese número se decide antes de montar, no se descubre
> al final contando lo que uno metió.

Este bloque (470–479) es el de la contención. El `269` te dijo cuánto **tiempo tuyo** vale la pena
gastar en un efecto. Este te dice cuántos efectos **caben en el vídeo**, que es otra pregunta y tiene
otra respuesta.

**Frontera, primero.** El presupuesto de **un recurso concreto** ya tiene dueño: `439` fija el cupo de
destellos por duración de la pieza, y `458` el coste del movimiento sobre imagen fija. Lo que se
presupuesta aquí es **la suma de todas las familias** —destello, textura, movimiento, transición— y su
proporción con lo demás que ocurre en pantalla. Si tu pregunta es «¿cuántos fogonazos?», la respuesta
está en `439` y no aquí.

---

## 1. Tres contadores que casi todo el mundo mezcla

| Contador | Qué cuenta | Dónde vive | Módulo dueño |
|---|---|---|---|
| **Corte** | cambio de plano | el ritmo | `20`, `328` |
| **Evento** | cualquier cosa que cambia en pantalla (entra un elemento, sale, se mueve) | la densidad | `canales/10` |
| **Efecto** | algo **procesado**: destello, glow, glitch, rampa de velocidad, transición con filtro | el presupuesto | **este** |

Los tres suben y bajan por separado. Un montaje puede ir a 60 eventos por minuto y llevar cinco efectos
en total; otro puede tener cuatro cortes y un efecto encima de cada uno. **Contarlos juntos es la causa
número uno de un vídeo que se siente recargado sin que nadie sepa decir por qué.**

---

## 2. Medirlos en un archivo que ya existe

```bash
V=final.mp4
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")

# cortes: cambios de escena detectados
ffmpeg -hide_banner -i "$V" -filter:v "select='gt(scene,0.3)',showinfo" -f null - 2> e.txt
N=$(grep -c "pts_time" e.txt)
awk -v d="$DUR" -v n="$N" 'BEGIN{printf "cortes %d - %.1f/min - pulso %.2f s\n", n, n/d*60, d/(n+1)}'
```

Los efectos no los detecta ffmpeg: **los cuentas tú, del proyecto**, porque un efecto es una decisión,
no una señal. Si el montaje vive en código, se cuentan solos. En el piloto del canal documental el
guion visual declara los destellos en un diccionario, así que la cuenta es exacta y no opinable.

---

## 3. El techo medido en un episodio real

Medido con `python auditar.py ep01-lustig` sobre el piloto de PAPER EMPIRES
(`Desktop\CANALES-LUSHOWS\piloto\`), un episodio de **63,45 s**:

| Medida | Valor | Objetivo del canal |
|---|---|---|
| Escenas | 5 | — |
| Elementos | 61 | — |
| **Eventos/min** | **62,4** | ≥ 44 |
| Simultaneidad media | 2,02 | ≥ 2,00 |
| Duración media del elemento | 2,34 s | 1,6 – 2,4 |
| Cobertura media del cuadro | 38,0 % | 22 – 38 % |
| Huecos (tramos sin nada) | 0 | 0 |
| **Destellos** | **5** (uno por bloque) | 1 por bloque |
| Tramos con más de 4 elementos a la vez («ruido») | **0,2 s** | lo mínimo posible |

Ahora la división que importa. Los eventos totales del episodio son `5 escenas + 61 entradas = 66`.
Los efectos son **5 destellos**:

```
5 efectos / 63,45 s * 60  =  4,7 efectos por minuto
5 efectos / 66 eventos     =  7,6 % de lo que pasa en pantalla
```

> Nota de coherencia: `439` cita el mismo piloto como «5 destellos en 62,98 s». Esa cifra es la de la
> locución; la de aquí, 63,45 s, es la de la tabla de escenas que devuelve `auditar.py`. Medio segundo
> de diferencia, dos relojes distintos, ninguna contradicción.

**Siete y medio por ciento.** Un montaje que se percibe cargadísimo —dos elementos vivos de media, el
cuadro al 38 % de superficie ocupada, cero huecos— sostiene todo eso con **menos de un efecto por cada
trece cosas que ocurren**. La energía no la dan los efectos: la dan los eventos. Los efectos solo
marcan cuáles importan.

---

## 4. El 10 % aparece dos veces, por caminos distintos

El módulo `29` fija, desde el ritmo, que **menos del 10 % de los cortes lleven transición**. El piloto
llega, desde la densidad, al **7,6 % de eventos con efecto**. Son dos cocinas distintas que dan el
mismo orden de magnitud, y eso es lo más parecido a una constante que tiene este oficio:

> **Uno de cada diez momentos puede llevar efecto. Los otros nueve son los que hacen que ese uno
> signifique algo.**

---

## 5. La tabla de techos

La primera fila está **medida**. Las demás están **derivadas** de esa proporción y de las reglas ya
escritas de la casa (`29`, `269`), y se marcan como tales: son puntos de partida para discutir, no
resultados de laboratorio.

| Formato | Duración | Efectos totales | Efectos/min | Origen |
|---|---|---|---|---|
| Episodio documental de collage | 63,45 s | 5 | 4,7 | **medido** |
| Reel de venta | 20–45 s | 2–3 | ~4 | derivado |
| Anuncio para pauta | 15–30 s | 1–2 | ~4 | derivado |
| Talking head / explicativo | 60–180 s | 3–6 | ~2 | derivado |
| Episodio largo | 12 min | **no multiplica** | ver `439` | ver `475` |

Si tu número real dobla el de su fila, no necesitas una opinión: necesitas quitar la mitad y volver a
mirar. Y si te queda por debajo, probablemente el problema no sea la falta de efectos sino la falta de
eventos, que es mucho más barato de arreglar.

**Ojo con la última fila, que es una trampa.** La tasa no se extrapola a piezas largas: `439` mide que
por encima de los tres minutos el cupo de destellos **baja** —de 9 a 12 en total, no más—, porque el
espectador ya aprendió el recurso y necesita menos. La tasa de este módulo describe piezas cortas. En
`475` está lo que pasa cuando el vídeo se va a doce minutos, y no es una multiplicación.

---

## 6. El aviso de saturación

El techo por minuto no impide el atasco local: puedes cumplir la media y aun así apilar seis cosas en
un segundo concreto. Por eso el auditor del piloto lleva una alarma aparte:

```python
# picos de saturacion: mas de 4 elementos a la vez ya es ruido
sat = [v for v in vivos if v > 4]
if sat:
    print(f"\n  ! {len(sat)*paso:.1f} s con mas de 4 elementos a la vez (ruido)")
```

En el episodio medido salta con **0,2 s**, o sea el 0,3 % del metraje. Ese es el aspecto de una alarma
sana: existe, se dispara, y lo que reporta es despreciable. Una alarma que nunca se dispara está mal
calibrada; una que reporta veinte segundos está describiendo el problema, no avisándolo.

---

## 7. Poner el tope antes

Tres líneas escritas antes de abrir el proyecto, y ninguna de ellas se renegocia a mitad de montaje:

```
Efectos totales:      5
Reparto:              1 por bloque, el mas fuerte en el golpe del gancho
Lo que NO lleva:      el tramo explicativo, los planos de menos de 1 s
```

Cuando el sexto efecto pida entrar —y va a pedir—, la pregunta no es «¿queda bien?». Es **«¿a cuál de
los cinco sustituye?»**. Esa pregunta mata sola al 90 % de los candidatos, y al 10 % que sobrevive lo
convierte en una mejora real en vez de una adición.

---

## Errores frecuentes

1. **Contar efectos en total en vez de por minuto.** Ocho efectos no significa nada sin la duración.
2. **Sumar cortes, eventos y efectos en un solo número.** Son tres presupuestos independientes.
3. **Decidir el techo al final, contando lo que uno metió.** Eso no es un presupuesto, es un inventario.
4. **Creer que la energía la dan los efectos.** La dan los eventos: 62,4 por minuto con solo 4,7 efectos.
5. **Cumplir la media y apilar seis cosas en un segundo.** El techo por minuto no cubre el pico local.
6. **No tener alarma de saturación**, o tenerla tan laxa que jamás se dispara.
7. **Meter un efecto sin decir a cuál sustituye.** Sin esa pregunta el presupuesto no existe.
8. **Poner efecto en un plano de menos de un segundo.** No da tiempo a verse (`269`).
9. **Subir el techo porque el vídeo «se siente flojo».** Casi siempre faltan eventos, no efectos.
10. **Aplicar el techo de un formato a otro.** Un reel y un episodio de doce minutos no comparten tasa.
11. **Contar a mano un montaje que vive en código.** Si el proyecto declara sus efectos, la cuenta es
    exacta y gratis; contarla a ojo introduce un error que luego se defiende.

---

## Relacionado

- `269` — el presupuesto del **esfuerzo**: cuánto tiempo tuyo vale un efecto. Este es el otro
  presupuesto, el del vídeo.
- `471` — dónde rinden los pocos efectos que caben.
- `475` — qué pasa con esta tasa cuando el vídeo pasa de un minuto a doce.
- `29` — el corte final: la regla del 10 % de transiciones y las señales de sobre-edición.
- `20`, `328` — el pulso y la medición del ritmo, que es el contador de cortes.
- `209` — cuándo el motion sobra.
- `420` — un efecto es una hipótesis: el instrumento con el que se decide si un candidato entra.
- `422` — coste en render y en atención: el presupuesto de atención, que es la otra cara de esta tasa.
- `429` — cuándo quitar un efecto, cuando el techo ya está lleno y entra uno nuevo.
- `56`, `460` — la lista negra cualitativa y su versión medida: efectos que no deberían ocupar plaza.
- `canales/10-densidad-de-eventos`, `canales/18-densidad-por-tipo-de-bloque` — el contador de **eventos**
  del motor documental y sus umbrales por tipo de bloque. Esa métrica vive ahí; aquí solo se usa de
  contraste.
- `canales/17-medir-el-montaje` — el auditor completo del que salen los números de este módulo.
- `canales/141-elegir-un-umbral` — cómo se calibra un número de estos en vez de ponerlo a ojo.

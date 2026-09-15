# 475 — Escalar a doce minutos

> **Nada de lo que funciona en un minuto escala multiplicando por doce.** Ni el número de elementos, ni
> el tiempo de render, ni el cajón de material, ni tu capacidad de mirarlo entero. Este módulo pone los
> cuatro muros con números medidos, para que cuando alguien diga «hagamos episodios de doce minutos» la
> conversación empiece por lo que cuesta y no por lo que ilusiona.

Todo lo que sigue está medido sobre `ep01-lustig`, el piloto de PAPER EMPIRES
(`Desktop\CANALES-LUSHOWS\piloto\`): **63,45 segundos**, cinco bloques, corriendo en la máquina real de
casa.

---

## 1. La foto del minuto

```
$ python auditar.py ep01-lustig

  duracion               63.45 s
  escenas                    5
  elementos                 61
  EVENTOS/min             62.4   (objetivo >= 44)
  simultaneidad media     2.02   (objetivo >= 2,00)
  duracion media          2.34 s (objetivo 1,6 - 2,4)
  COBERTURA media        38.0 %  (objetivo 22 - 38 %)
  HUECOS                     0   (objetivo 0)

  ! 0.2 s con mas de 4 elementos a la vez (ruido)
```

Un minuto que cumple todo. Ahora los cuatro muros que aparecen al multiplicar por 11,35 (720 ÷ 63,45).

---

## 2. Muro 1 — el número de elementos

```
61 elementos / 63,45 s = 0,961 elementos por segundo
0,961 * 720 s = 692  ->  unos 700 elementos
```

**Setecientos elementos.** Cada uno con su recurso, su ancla, su tamaño, su sitio y su duración. En un
minuto, colocar sesenta y uno a mano es viable y hasta agradable. Setecientos a mano no es un montaje:
es una jornada laboral de mecanografía con setecientas oportunidades de equivocarse.

Consecuencia, y es la de fondo: **a doce minutos la colocación tiene que ser generada, no escrita.** El
piloto ya lo hace —capa clave a mano, capa auto desde el diccionario— y por eso la pregunta al escalar
no es «¿aguanto setecientos?» sino «¿qué proporción puedo generar?».

| | 1 minuto | 12 minutos |
|---|---|---|
| Elementos | 61 | ~700 |
| Bloques | 5 | ~57 |
| Destellos (1 por bloque) | 5 | ~57 |
| Eventos totales | 66 | ~750 |

---

## 3. Muro 2 — el render

Medido dos veces, con cronómetro, sobre el mismo episodio:

| Condición | Tiempo | Veces el tiempo real |
|---|---|---|
| Máquina libre | **832 s** (13 min 52 s) | **13,1×** |
| Con otro ffmpeg compitiendo | 1.074 s (17 min 54 s) | 16,9× |

Y la extrapolación honesta a doce minutos, que depende de la máquina:

| Ratio | De dónde sale | 12 minutos tardan |
|---|---|---|
| 9,2× | referencia previa del proyecto (582 s) | **1 h 50 min** |
| 13,1× | medido aquí, máquina libre | **2 h 37 min** |
| 16,9× | medido aquí, con carga | 3 h 23 min |

En cualquiera de los tres casos la conclusión operativa es la misma y es dura:

> **A doce minutos ya no puedes renderizar para ver si algo quedó bien.** Un ciclo de prueba pasa de
> «me levanto a por un café» a «se acabó la tarde». Todo lo que se pueda comprobar **antes** de
> renderizar hay que comprobarlo antes, y lo que no se pueda comprobar antes hay que convertirlo en
> algo que sí.

Por eso el auditor existe y por eso se corre siempre primero: lee la tabla de eventos y responde en
segundos lo que el render responde en horas.

**Y un corolario de presupuesto:** el render por escena permite reconstruir solo lo que cambió. Si
tocas un bloque de doce, renderizas un bloque, no doce. Un episodio largo sin render por tramos es
inviable, no incómodo.

---

## 4. Muro 3 — el cajón (este es el que mata)

El umbral de la serie es **1,25 usos por recurso**. A setecientos elementos:

```
700 gestos / 1,25 = 560 recursos distintos, como minimo
```

Y esto es lo que hay hoy, contado:

| | Cuántos |
|---|---|
| Recursos que **cita el vocabulario** de `ep01-lustig` | **56** |
| Ficheros de imagen en las carpetas del episodio | 200 |
| Ficheros de imagen en el banco común | 216 |
| **Total en disco** | **416** |
| **Necesarios a 12 minutos** | **560** |

Léelo dos veces. **Aunque el vocabulario conociera todos y cada uno de los 416 ficheros que ya existen
en disco**, doce minutos saldrían a `700 / 416 = 1,68` usos por recurso, muy por encima del umbral. El
cajón no da. Y el vocabulario real solo conoce 56 de esos 416, así que el problema es doble: falta
material **y** falta diccionario.

Añade la ventana antirrepetición:

```python
if _ultima(recurso, t) < 25.0:
    continue        # hasta la mas olvidada salio hace nada
```

En 63,45 s el episodio dura **2,5 ventanas**; en 720 s dura **28,8**. La misma regla que casi no se nota
en un minuto se convierte en el cuello de botella permanente en doce. Y con **35 de las 48 palabras del
vocabulario teniendo una sola opción**, cada una de esas palabras que vuelva dentro de la ventana deja
un hueco o una repetición.

> **La tentación, a los doce minutos, es bajar la ventana de 25 s a 10 s. No lo hagas.** Los 25 s no son
> una preferencia: son donde el ojo deja de reconocer la imagen. Bajarlos no resuelve la sequía, la hace
> visible. A doce minutos hace falta **material**, no reglas más laxas.

---

## 5. Muro 4 — la revisión humana

El cuarto muro no tiene una métrica bonita y es el que más episodios largos ha matado.

La salida del auditor de un minuto cabe en una pantalla: cinco bloques, cero huecos, cuatro lavados,
0,2 s de ruido. Se lee en treinta segundos y se actúa sobre todo. La de doce minutos tiene cincuenta y
siete bloques y listas once veces más largas. Y la verificación del corte (`98`) —escuchar el audio
entero, a velocidad normal, en un móvil— pasa de un minuto a doce, **por vuelta**.

Lo que escala y lo que no:

| Tarea | ¿Escala? |
|---|---|
| Colocar elementos | sí, si está generada |
| Auditar antes de renderizar | sí, es código |
| Renderizar | sí, pero cuesta horas |
| **Elegir el material** | **no** |
| **Escuchar el corte entero** | **no** |
| **Decidir dónde va cada efecto** | **no** |

Las tres que no escalan son exactamente las tres que deciden si el episodio es bueno.

---

## 6. La forma correcta de escalar

No se produce un episodio de doce minutos: **se producen doce tramos de un minuto y se encadenan.**
Cada tramo se cierra del todo —material, montaje, auditoría, render de escena— antes de empezar el
siguiente. Las razones son las cuatro de arriba, en orden:

```
1. Un tramo cabe en tu cabeza. Doce, no.
2. Un tramo se renderiza en 14 minutos. El episodio entero, en dos horas y media.
3. Un tramo agota 56 recursos; el cajon se rellena entre tramo y tramo, no al final.
4. Un tramo se escucha entero sin hacer trampa.
```

### Y el presupuesto de efectos tampoco se multiplica

La tentación es obvia: si es uno por bloque y hay cincuenta y siete bloques, son cincuenta y siete
destellos. **Es falso, y es el quinto muro.** `439` lo tiene medido: por encima de los tres minutos el
cupo de un mismo recurso de luz **baja** a 9–12 en total, porque el espectador ya aprendió a leerlo y
un fogonazo más deja de puntuar para pasar a informar de que hay fogonazos.

Así que a doce minutos hay que elegir entre dos cosas, y las dos cuestan:

| Opción | Qué implica |
|---|---|
| **Menos efectos** | ~10 destellos en 12 min: uno cada 70 s, no uno por bloque |
| **Más familias** | bloom (`434`), pulso de exposición (`436`), fuga sobre costura (`435`) |

La segunda es la que usan los documentales largos, y tiene su propio peaje: cada familia nueva es un
sistema nuevo que documentar y vigilar (`473`, `478`). **Nada escala multiplicando, ni siquiera lo que
parecía que sí.**

---

## Errores frecuentes

1. **Multiplicar por doce y creer que ya está.** Tres de los cuatro muros no son lineales en la práctica.
2. **Renderizar para ver si algo quedó bien.** A doce minutos eso son dos horas y media por intento.
3. **No tener render por escena.** Cambiar un bloque obliga a reconstruir el episodio entero.
4. **Bajar la ventana antirrepetición** para que el aviso se calle. Hace la sequía visible, no la quita.
5. **Subir el umbral de usos por recurso.** Mismo error con otro número.
6. **Escalar el montaje sin escalar el cajón.** Hacen falta 560 recursos y hay 416 en disco, de los que
   el vocabulario conoce 56.
7. **Buscar material fuera antes de inventariar el de dentro.** Hay 416 ficheros y el diccionario cita 56.
8. **Colocar setecientos elementos a mano.** A esa escala la colocación tiene que ser generada.
9. **Auditar después de renderizar.** El auditor responde en segundos lo que el render responde en horas.
10. **Saltarse la escucha completa** porque el episodio es largo. Es justo cuando más defectos hay.
11. **Empezar por el minuto doce.** Se cierra el tramo uno del todo, y luego el dos.
12. **Prometer doce minutos antes de haber hecho tres.** El coste no se intuye: se mide.

---

## Relacionado

- `470` — la tasa de efectos de las piezas cortas, y por qué no se extrapola.
- `439` — **el cupo de destellos por duración**: de dónde sale el quinto muro de este módulo.
- `458` — lo que cuesta el movimiento sobre imagen fija, que es el otro coste que explota al escalar.
- `474` — el presupuesto anclado a la estructura, y dónde deja de valer.
- `98` — verificación del corte: la tarea que no escala y que no se puede saltar.
- `132` — render reproducible; `134` — procesar por lotes; `139` — mantener un pipeline vivo.
- `422` — **coste en render**: `utime` frente al reloj, y cómo se extrapola el coste de un filtro a un
  episodio de doce minutos. Los números de render de este módulo se leen con ese criterio.
- `137` — cuándo NO automatizar: la otra cara de «todo generado».
- `269` — el presupuesto del esfuerzo por vídeo.
- `canales/98-episodios-largos` — **el método de producción por tramos cerrados de un minuto.** Ahí está
  el procedimiento completo; aquí están los números que lo justifican.
- `canales/17-medir-el-montaje`, `canales/140-medir-antes-de-renderizar` — auditar antes de renderizar.
- `canales/253-la-ventana-antirrepeticion` — por qué 25 s y por qué no se bajan.
- `canales/174-el-umbral-de-piezas`, `canales/170-el-sondeo-de-media-hora` — cómo se llena el cajón.

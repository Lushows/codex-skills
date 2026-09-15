# 92 · El aporte original

**Qué resuelve:** "se incautaron doscientos millones de dólares en efectivo" no
significa nada para nadie. El aporte original es el trabajo que convierte una cifra
en algo que el espectador puede **ver**. Es lo que separa a este canal de un
recopilador de noticias — y lo que YouTube premia como contenido propio.

---

## Qué es un aporte original

Todo lo que el canal **produce** y no encuentra hecho:

| Tipo | Ejemplo de forma |
|---|---|
| **Cálculo propio** | Cuánto pesa, cuánto ocupa, cuánto tiempo llevaría contarlo |
| **Comparación** | La misma cifra expresada en algo que el espectador conoce |
| **Reconstrucción** | Diagrama de cómo circulaba el dinero, paso a paso |
| **Cronología** | Fechas de varios documentos puestas en una sola línea |
| **Agregación** | Sumar lo que está disperso en veinte páginas de anexos |
| **Escala** | Un gráfico donde dos magnitudes se ven juntas por primera vez |

Todo aporte original se **rotula como tal** en pantalla: *cálculo propio · Paper
Empires*, o *reconstrucción a partir de <documento>*. No es humildad: es lo que
permite que la pieza sea nuestra y sea defendible.

## El método del cálculo propio

1. **Elegir la cifra ancla.** Una por episodio, dos como mucho. Debe ser la cifra que
   el espectador va a recordar.
2. **Elegir la dimensión física.** Peso, volumen, superficie, tiempo, distancia,
   repetición. La dimensión debe tener sentido con la historia: en un caso de efectivo,
   el peso; en uno de transferencias, el tiempo.
3. **Buscar la constante en una fuente citable.** No de memoria. Cada constante
   (peso de un billete, densidad del oro, capacidad de un contenedor, salario medio)
   tiene que venir de un organismo y quedar registrada en `archivo/fuentes.json`.
4. **Ejecutar la cuenta en código**, con unidades explícitas, y verificarla dos veces.
   Nunca a ojo, nunca mentalmente.
5. **Redondear hacia abajo** y decirlo como aproximación. Un cálculo conservador es
   inatacable; uno ajustado al alza se convierte en el comentario que desmonta el vídeo.
6. **Comprobar el orden de magnitud** con una segunda ruta distinta. Si las dos rutas
   no coinciden en el orden de magnitud, hay un error de unidades.
7. **Escribirlo en pantalla como operación**, no sólo como resultado: el espectador ve
   la cuenta y la cree.

### La plantilla del cálculo

```
CIFRA ANCLA .......... <valor> <unidad>   fuente: <documento, página>
CONSTANTE ............ <valor> <unidad>   fuente: <organismo>
OPERACIÓN ............ <la fórmula, con unidades>
RESULTADO ............ <valor redondeado a la baja>
COMPROBACIÓN ......... <segunda ruta que da el mismo orden de magnitud>
RÓTULO EN PANTALLA ... "cálculo propio · Paper Empires"
```

> Las constantes de este módulo se dejan a propósito sin valor: **cada una se busca en
> su organismo antes de usarla**. Un manual que memoriza constantes acaba propagando
> una constante equivocada por veinte episodios.

## Las familias de comparación que funcionan

| Familia | Cuándo | Forma de la frase |
|---|---|---|
| **Peso** | Efectivo, oro, mercancía | "pesaba tanto como…" |
| **Volumen** | Efectivo, contenedores, almacenes | "no cabía en…" |
| **Tiempo** | Flujos, transferencias, producción | "cada minuto entraban…" |
| **Vida cotidiana** | Cualquier cifra grande | "el salario de X personas durante un año" |
| **Ritmo** | Negocios que producían sin parar | "un envío cada N días durante N años" |
| **Fracción** | Cifras institucionales | "una de cada N…" |
| **Contraste interno** | Cuando hay dos cifras del mismo caso | Lo declarado frente a lo real |

**La mejor comparación es la que sale de la propia historia.** Si el negocio tapadera
exportaba harina de pescado, la unidad de medida del episodio es la lata, el saco o el
contenedor de harina de pescado — no un estadio de fútbol. La comparación genérica se
olvida; la comparación interna es la marca del episodio.

## Lo que NO es aporte original

- Repetir la comparación que ya hizo un periódico (es su trabajo, no el nuestro).
- Una cifra "estimada por analistas" sin nombre ni método.
- Una infografía copiada con otros colores.
- Multiplicar dos números sin verificar qué mide cada uno (§ `91`).
- Una comparación absurda por espectacular: "daría N vueltas a la Tierra" con billetes
  puestos en fila no le da al espectador ninguna intuición real.

## Del cálculo al plano

Un cálculo propio es **una escena entera**, no un rótulo:

1. La cifra bruta aparece y se queda corta a propósito ("doscientos millones").
2. Entra la constante como objeto (un billete, una balanza, un saco).
3. La operación se escribe en pantalla, en tipografía monoespaciada (§ `44`).
4. El resultado aterriza con un golpe de sonido y un cambio de escala.
5. Debajo, en pequeño: la fuente de la cifra y el sello de cálculo propio.

Ese bloque dura entre 8 y 14 segundos y es el trozo del episodio que más se comparte.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Constante de memoria | Un error de fábrica se propaga a todos los episodios |
| Mezclar unidades (tonelada corta vs métrica, billete vs fajo) | El resultado se va por un factor y el vídeo queda desmentido |
| Redondear al alza para que suene mejor | Un comentario con la cuenta bien hecha destruye la autoridad del canal |
| Calcular sobre la cifra reclamada creyendo que es la incautada | Aporte original construido sobre un dato equivocado (§ `91`) |
| No rotular el cálculo como propio | Parece un dato oficial inventado; es el peor de los dos mundos |
| Comparación genérica de catálogo | Se olvida al instante; no diferencia al canal |
| Poner sólo el resultado | Sin ver la operación, el espectador no lo cree |

## Relacionado

`91` leer un expediente · `63` comparaciones visuales · `36` contadores y cifras
animadas · `44` la cifra en pantalla · `96` verificación de datos

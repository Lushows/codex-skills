# 471 — Dónde pagan

> **Los minutos de un vídeo no valen lo mismo.** El `470` te dio cuántos efectos caben. Este te dice
> dónde ponerlos, que es la decisión que de verdad separa un montaje con criterio de uno decorado.
> Un efecto puesto donde la atención ya está ganada es un efecto tirado, por bonito que sea.

La regla, en una frase:

> **Un efecto se paga donde se está decidiendo la atención, no donde ya la tienes.**

**Frontera.** El reparto de papeles de un recurso concreto tiene dueño: para el destello es `430` §3, y
su cupo por duración es `439`. Aquí se da el **principio general**, válido para cualquier familia de
efecto, y se usa el destello del piloto como el caso medido que lo ilustra.

---

## 1. Los cinco sitios donde un efecto rinde

| Sitio | Qué está pasando ahí | Qué hace el efecto |
|---|---|---|
| **El golpe de la promesa** | el espectador decide si esto va con él | subraya la frase que lo compra |
| **El cambio de terreno** | se acaba un bloque y empieza otro | avisa de que cambió el asunto |
| **La cifra** | entra un dato que tiene que quedarse | le da peso a un número que si no pasa de largo |
| **El giro** | lo que creías resulta que no era | marca el punto exacto de la vuelta |
| **El remate** | última frase, último recuerdo | cierra en vez de desvanecerse |

Y los cinco tienen algo en común: **son momentos de la narración, no momentos del montaje**. Ninguno se
localiza mirando la línea de tiempo; se localizan leyendo el guion. Por eso el reparto de efectos se
decide con el guion delante y no con el proyecto abierto.

---

## 2. Los cinco sitios donde no rinde

1. **En medio de una explicación.** El espectador está procesando; el destello le roba el hilo.
2. **Debajo de un texto que se está leyendo.** Leer ya consume la atención entera (`376`).
3. **En un plano de menos de un segundo.** No da tiempo a que se vea (`269`).
4. **Encima de un elemento lavado contra su fondo.** Si el elemento ya no se separa, el efecto realza
   una mancha. El auditor del piloto reporta esto aparte, y encontró cuatro casos: `torre_citroen_noche`
   a 1,1 puntos de luz de su fondo, `bajo_la_torre` a 2,5.
5. **En el primer segundo.** Este es el contraintuitivo y tiene datos. Ver abajo.

---

## 3. Lo que hizo el piloto: cinco efectos, cinco sitios

Medido resolviendo los destellos declarados en `ep01-lustig/guion_visual.py` contra los tiempos reales
de la locución (`tiempos.json`). Estos son los cinco únicos efectos del episodio, en un montaje de
63,45 s con 61 elementos:

| Bloque | Palabra ancla | Segundo | Fuerza | Ancho |
|---|---|---|---|---|
| muerte | «hombre» | 6,88 | 0,15 | 0,075 s |
| **oficio** | **«aprendiz»** | **20,55** | **0,22** | **0,090 s** |
| nombre | «broma» | 33,02 | 0,14 | 0,075 s |
| torre | «Eiffel» | 41,85 | 0,18 | 0,075 s |
| metodo | «consta» | 62,93 | 0,20 | 0,075 s |

Tres cosas que leer en esa tabla y que no son obvias:

**a) No hay efecto en los primeros 6,88 segundos.** El bloque del arranque es el más largo (16,15 s) y
el segundo más denso (66,9 eventos/min), y aun así el primer destello no entra hasta el segundo 6,88:
más de la décima parte del episodio sin un solo efecto. Los primeros segundos ya tienen toda la
atención del mundo, gastarla en un
fogonazo es pagar por algo que te estaban dando gratis. El efecto entra cuando la atención empieza a
poder irse.

**b) El efecto más fuerte está en el bloque más corto.** `oficio` dura 6,73 s —menos de la mitad que el
que le sigue— y se lleva la fuerza 0,22 y el ancho 0,090, los dos máximos del episodio. Es el golpe de
la promesa. **La fuerza del efecto sigue a la importancia de la frase, no a la duración del bloque.**

**c) El último cae a 0,52 s del final.** El remate lleva 0,20, el segundo valor más alto. Un vídeo que
se apaga sin marcar su última frase desperdicia el único momento que el espectador se lleva entero.

---

## 4. El reparto contra la densidad del bloque

Los cinco bloques, medidos con `python auditar.py ep01-lustig`:

| Bloque | Duración | Elementos | Eventos/min | Simultaneidad | Fuerza del efecto |
|---|---|---|---|---|---|
| muerte | 16,15 s | 17 | 66,9 | 2,22 | 0,15 |
| oficio | 6,73 s | 7 | 71,3 | 2,27 | **0,22** |
| nombre | 11,53 s | 9 | 52,0 | 1,67 | 0,14 |
| torre | 15,88 s | 16 | 64,2 | 2,09 | 0,18 |
| metodo | 13,16 s | 12 | 59,3 | 1,87 | 0,20 |

El bloque más flojo del episodio en densidad —`nombre`, con 52,0 eventos/min y 1,67 de simultaneidad—
es también el que menos fuerza de efecto lleva (0,14). **La tentación es exactamente la contraria:
poner el efecto gordo en el tramo flojo para taparlo.** No funciona: un bloque flojo con un fogonazo
encima sigue siendo un bloque flojo, y ahora además tiene un fogonazo que no viene a cuento. El tramo
flojo se arregla con eventos (`canales/10`), no con efectos.

---

## 5. El efecto llega antes que la palabra

Los cinco destellos del piloto llevan `offset` negativo: −0,04 o −0,05 segundos. No es un capricho.

```python
# guion_visual.py
"oficio": [{"ancla": "aprendiz", "offset": -0.05, "fuerza": 0.22, "ancho": 0.09}],
```

Y el mismo criterio gobierna la entrada de los elementos en el diccionario del motor:

```python
# el elemento entra ANTES de su palabra: justo a tiempo llega tarde
t0 = max(ini, t - 0.16)
```

Un efecto sincronizado «exacto» con la palabra se percibe **tarde**, porque el oído la reconoce antes de
que termine de sonar. Cuarenta o cincuenta milisegundos de adelanto es la diferencia entre un golpe que
acompaña y uno que llega a recoger. Se nota, y no se ve en ningún fotograma: se oye y se siente.

---

## 6. Cómo se reparte, en la práctica

Con el guion delante y antes de tocar nada:

```
1. Marca en el guion los momentos de decision: promesa, giro, cifra, remate.
2. Cuenta cuantos son. Si son mas que tu techo del 470, ordenalos y corta por el techo.
3. Asigna la fuerza por importancia, no por duracion del bloque.
4. Deja el arranque limpio: ahi la atencion ya la tienes.
5. Comprueba que ninguno cae sobre texto que se este leyendo ni sobre un plano corto.
```

El paso 2 es el que duele y el que hace el trabajo. Casi siempre salen ocho o nueve candidatos para
cinco plazas, y elegir cinco obliga a decidir cuál es de verdad el momento más importante del vídeo,
que es una pregunta que casi nadie se hace explícitamente.

---

## Errores frecuentes

1. **Repartir los efectos de forma pareja** a lo largo del vídeo. Un reparto uniforme es un reparto sin
   criterio: si todos los momentos son igual de importantes, ninguno lo es.
2. **Poner el efecto más fuerte en el tramo más flojo** para taparlo. El tramo flojo necesita eventos.
3. **Gastar efecto en el primer segundo.** Ahí la atención ya está ganada; se decide justo después.
4. **Terminar sin marcar el remate.** Es el único trozo que el espectador se lleva completo.
5. **Sincronizar el efecto exacto con la palabra.** Llega tarde. Cuarenta milisegundos antes.
6. **Poner efecto encima de un elemento lavado** contra su fondo. Realzas una mancha.
7. **Poner efecto debajo de un texto que se está leyendo.** Compiten por la misma atención.
8. **Decidir el reparto con el proyecto abierto** en vez de con el guion delante. Los sitios donde un
   efecto paga son sitios de la narración, no de la línea de tiempo.
9. **No ordenar los candidatos.** Si tienes nueve para cinco plazas y no los ordenas, entran los cinco
   que estaban más a mano.
10. **Confundir fuerza con duración.** Un fogonazo de 0,09 s con fuerza 0,22 pesa más que uno de medio
    segundo y fuerza 0,10, y molesta menos.
11. **Subir la fuerza de todos cuando uno se queda corto.** Si todos suben, el contraste vuelve a cero y
    solo has añadido cansancio.

---

## Relacionado

- `470` — cuántos efectos caben. Este módulo reparte esos.
- `472` — cómo se prueba si un efecto concreto merece su plaza.
- `476` — qué puede y qué no puede hacer un efecto por la retención.
- `30`, `361`, `364` — el gancho y la mecánica de la promesa: el sitio número uno de la tabla.
- `33`, `287` — el remate, el sitio número cinco.
- `379` — números y cifras en pantalla.
- `430` — **el destello como puntuación**: por qué un fogonazo dice dónde acaba la frase, y el reparto
  de papeles entre los destellos de una pieza. `439` — su cupo por duración.
- `423` — el efecto que no se ve; `424` — el efecto que tapa un problema. Los dos sitios donde un efecto
  parece que paga y no paga.
- `422` — el presupuesto de atención del espectador.
- `376` — legibilidad real en el móvil; por qué no se pone efecto bajo un texto que se lee.
- `canales/10-densidad-de-eventos` — cómo se arregla de verdad un bloque flojo.
- `canales/125-musica-y-destello` — el fogonazo mudo se lee como un error; cada destello lleva su golpe.
- `canales/163-contraste-elemento-fondo` — la medida de «lavado» que descalifica un sitio para efecto.

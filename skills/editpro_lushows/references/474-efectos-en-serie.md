# 474 — Efectos en serie

> **En un vídeo suelto el enemigo es el exceso. En una serie el enemigo es el agotamiento.** Son
> problemas distintos y se arreglan al revés: el exceso se arregla quitando, y el agotamiento solo se
> arregla comprando material. Este módulo es cómo se lleva un presupuesto de efectos a lo largo de
> ocho, veinte o cien episodios sin que se desmadre y sin que se quede seco.

---

## 1. Dos cosas que se repiten y solo una es un problema

| Se repite | Cómo se llama | Qué significa |
|---|---|---|
| **El efecto** | firma | tienes un sistema (`473`) |
| **El material** | agotamiento | te quedaste sin cajón |

El espectador distingue las dos sin esfuerzo aunque no sepa nombrarlas. Ver el mismo destello en el
episodio 9 le dice «esto es de ellos». Ver la misma foto de un martillo tres veces en ochenta segundos
le dice «esta gente no tenía más fotos». Y la segunda lectura, una vez instalada, contamina todo lo
demás.

**La diferencia operativa es la declaración.** Un motivo se declara **antes**; una repetición se
descubre **después**. Lo mismo en pantalla, dos cosas opuestas en el proceso.

---

## 2. El presupuesto se ancla a la estructura, no al minuto

Los dos episodios que existen hoy en el piloto, medidos con `auditar.py`:

| | ep01-lustig | episodio01 |
|---|---|---|
| Duración | 63,45 s | 80,25 s |
| Bloques | 5 | 6 |
| **Destellos** | **5** | **6** |
| Efectos/min | 4,7 | 4,5 |
| Elementos | 61 | 71 |
| Eventos/min | 62,4 | 50,8 |
| Simultaneidad | 2,02 | 1,79 ❌ |
| Huecos | 0 | 5 ❌ |

La regla declarada es **uno por bloque**, y mira lo que consigue: dos episodios de duración distinta,
con seis y cinco bloques, acaban en 4,5 y 4,7 efectos por minuto **sin que nadie haya calculado nada**.
El presupuesto se escala solo porque está anclado a la estructura de la narración, no a un número de
minutos ni a un total.

Es la forma correcta de escribir un presupuesto de serie:

> **Un presupuesto anclado a un total («cinco efectos») se rompe en cuanto cambia la duración. Uno
> anclado a la estructura («uno por bloque») aguanta mientras las piezas sean parecidas.**

Con un límite que conviene saber desde ya: **el anclaje a la estructura deja de valer en piezas largas.**
`439` mide que por encima de los tres minutos el cupo de un mismo recurso baja a 9–12 en total, aunque
haya treinta bloques. Para una serie de piezas de uno a tres minutos, «uno por bloque» es la regla; para
episodios largos hay que volver a decidir (`475`).

Y fíjate en la otra columna: `episodio01` es el episodio **peor montado** de los dos —falla la
simultaneidad y tiene cinco huecos— y lleva **más** efectos. Otra vez lo mismo: los efectos no tapan un
montaje flojo.

---

## 3. La medida del agotamiento

El auditor la calcula sola, y es la métrica más importante de una serie:

```
ep01-lustig:  61 gestos · 55 recursos distintos · 1,11 usos por recurso   (objetivo <= 1,25) ✅
episodio01:   61 gestos · 48 recursos distintos · 1,27 usos por recurso   (objetivo <= 1,25) ❌
```

Siete recursos de diferencia, el mismo número de gestos, y el umbral se cae. Y esto es lo que reporta
el que falla:

```
--- recursos que salen demasiadas veces ---
 3x  martillo                 en 4.6, 7.2, 67.1
 3x  dinero_real              en 0.2, 14.6, 48.2
 3x  boveda                   en 9.8, 19.3, 36.9
--- mismo recurso repetido a menos de 25 s ---
   2.6 s  martillo                 (4.6 y 7.2)
   3.0 s  herramientas             (43.7 y 46.7)
   4.3 s  planta_pescado2          (71.9 y 76.2)
```

El martillo vuelve **2,6 segundos** después. Nadie lo decidió: el vocabulario del episodio tenía una
sola opción para esa palabra y el sistema puso lo único que tenía. **El agotamiento no se manifiesta
como un aviso: se manifiesta como una decisión que el sistema toma por ti porque no le diste
alternativa.**

---

## 4. Por qué se agota: el cajón, medido

El vocabulario de `ep01-lustig` tiene **48 palabras**. De ellas:

| | Cuántas | Qué implica |
|---|---|---|
| Con **una sola** opción | **35** | esa palabra siempre pone la misma imagen |
| Con **lista** de opciones | 13 | esas sí pueden rotar |

Y la ventana antirrepetición es de 25 segundos:

```python
recurso = max(opciones, key=lambda o: _ultima(o, t))
if _ultima(recurso, t) < 25.0:
    continue                      # hasta la mas olvidada salio hace nada
                                  # (25 s es donde el ojo deja de notarlo)
```

Junta las dos cosas: **35 de 48 palabras no pueden rotar**, así que en cuanto una de ellas vuelve a
aparecer dentro de la ventana, el elemento simplemente no entra —y ahí tienes un hueco— o entra
repetido. Las reglas están bien; lo que falta es cajón.

La confirmación, en un comentario del propio vocabulario:

```python
# "segun todo lo que se ha contado de el durante cien anos": el tramo que el
# antirrepeticion dejo desnudo al no poder repetir. Hay 69 recortes y solo se
# usaban 46, asi que no hacia falta repetir: hacia falta mirar el banco.
```

**Casi siempre el problema no es que falte material: es que el vocabulario no lo conoce.** Antes de
salir a buscar más, cuenta lo que ya tienes y compáralo con lo que el diccionario cita.

---

## 5. Las tres listas de una serie

Se escriben una vez y se revisan en cada episodio:

```
FIJO      el efecto de marca y sus numeros    -> nunca cambia (473)
MOTIVOS   lo que vuelve a proposito           -> declarado, excluido del contador
ROTA      el material de archivo              -> crece episodio a episodio
```

En el piloto, la segunda lista es literalmente tres nombres:

```python
MOTIVOS = {"m_consta", "m_cuenta", "linea"}
```

Y el auditor los excluye del recuento de repetición porque **vuelven a propósito**: son la gramática
del episodio, las marcas de columna que le enseñan al espectador a leer el vídeo. Declararlas es lo que
convierte «sale tres veces» en «vuelve tres veces».

---

## 6. El ritual por episodio

```
1. Corre el auditor ANTES de renderizar.
2. Mira 'usos por recurso'. Si pasa del umbral, es material, no reglas.
3. Mira la lista de repetidos dentro de la ventana. Cada uno es una palabra
   del vocabulario que solo tiene una opcion: dale una segunda.
4. Comprueba que el efecto de marca sigue con los mismos numeros (473).
5. Cuenta los efectos: uno por bloque, ni uno mas.
```

El paso 2 es el que todo el mundo quiere saltarse subiendo el umbral de 1,25 a 1,4. Funciona, en el
sentido de que el aviso desaparece. Lo que no desaparece es el martillo saliendo tres veces.

---

## Errores frecuentes

1. **Confundir firma con agotamiento.** El efecto repetido es marca; la imagen repetida es sequía.
2. **No declarar los motivos.** Sin declararlos, lo que vuelve a propósito se cuenta como error y lo que
   vuelve por sequía se justifica como intención.
3. **Anclar el presupuesto a un total** en vez de a la estructura. Se rompe en cuanto cambia la duración.
4. **Subir el umbral cuando el episodio no lo cumple.** El aviso desaparece; el problema no.
5. **Buscar material nuevo sin haber contado el que ya hay.** 69 recortes disponibles, 46 usados.
6. **Dar una sola opción a la mayoría de las palabras.** 35 de 48 sin alternativa es una serie con fecha
   de caducidad.
7. **Meter más efectos en el episodio flojo.** El flojo aquí es el que ya llevaba más.
8. **Revisar la repetición mirando el vídeo.** Falla en silencio: el sistema imprimía «sin repeticiones»
   mientras salía cuatro veces la misma imagen.
9. **Cambiar el efecto de marca entre episodios** porque el material del nuevo es más oscuro.
10. **No correr el auditor antes de renderizar.** Después cuesta dos horas de render (`475`).
11. **Tratar la serie como vídeos sueltos.** El coste de un episodio se decide en el anterior.

---

## Relacionado

- `473` — el efecto como sistema de marca: lo que en esta serie no cambia nunca.
- `475` — el mismo problema llevado al extremo: doce minutos en vez de uno.
- `37` — series y formato: que el episodio 8 se vea hermano del 1. Ahí viven las decisiones de formato.
- `242`, `245`, `357` — diseñar una serie, reciclar y multiplicar, series y episodios.
- `88` — plantillas reutilizables: cómo se capitaliza lo que ya resolviste.
- `439` — el cupo de destellos por duración, que es el techo que este anclaje no puede saltarse.
- `429` — cuándo quitar un efecto que ya se ha vuelto la firma de la serie.
- `canales/253-la-ventana-antirrepeticion` — la regla de los 25 s, su implementación y su fallo silencioso.
- `canales/254-motivos-lo-que-vuelve-a-proposito` — la declaración que separa motivo de repetición.
- `canales/257-vocabulario-por-episodio`, `canales/252-alternativas-y-rotacion` — cómo se le dan más
  opciones a una palabra.
- `canales/174-el-umbral-de-piezas`, `canales/190-curar-por-escenario` — cómo se llena el cajón.

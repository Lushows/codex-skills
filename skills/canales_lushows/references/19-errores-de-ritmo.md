# 19 · Errores de ritmo

**Qué resuelve:** "no me gustó cómo quedó" no es un diagnóstico. Aquí están los ocho
síntomas de un montaje flojo, la firma que deja cada uno en el auditor y la causa
concreta que hay que corregir.

---

## Diagnóstico rápido

Se lee la salida de `auditar.py` (`17`) y se busca la fila que coincide:

| Lo que dice el auditor | Síntoma |
|---|---|
| `0 elem` por encima de 0% | 1 · Agrupado |
| duración media < 1,2 s | 2 · Parpadeo |
| huecos siempre en el último tercio de cada escena | 3 · Cola vacía |
| `ANCLA HUERFANA` | 4 · Apilado al inicio |
| simultaneidad > 4,0 o dos principales a la vez | 5 · Amontonado |
| eventos/min alto y simultaneidad < 1,5 | 6 · Relevo seco |
| ev/min del remate ≥ ev/min del desarrollo | 7 · Remate sin golpe |
| duración media > 2,6 s | 8 · Clavado |

---

## 1 · Agrupado: "se siente lento aunque hay muchos elementos"

**Causa:** los elementos están bien pero repartidos a bandazos. Hay tramos densos y
tramos de fondo solo, y el ojo se queda con la impresión del tramo vacío.
**Corrección:** cerrar huecos por relevo y sustitución (`14`), no añadir material.

## 2 · Parpadeo: "no da tiempo a leer nada"

**Causa:** se subió la densidad acortando las vidas en vez de solapar. Elementos por
debajo de 0,55 s aislados; el ojo los registra como fallo de render, no como montaje.
**Corrección:** devolver las duraciones a su tipo (`13`) y recuperar la densidad
solapando: un suelo por escena y un rótulo por principal (`12`).

## 3 · Cola vacía: "cada plano empieza bien y termina en nada"

**Causa:** todos los elementos anclados a las primeras palabras de la escena. El motor
los reparte donde dice el ancla, y las últimas palabras se quedan sin nada.
**Corrección:** anclar al menos un elemento a una palabra del **último tercio** de cada
escena, y darle `dura` suficiente para llegar al corte.

## 4 · Apilado al inicio: "todo entra de golpe y luego nada"

**Causa:** anclas que no existen en `tiempos.json`. `motor.py` avisa por consola pero
sigue: tira el elemento al inicio de la escena. Suele ser puntuación no normalizada, la
palabra escrita distinto en el guion visual, o una palabra que está fuera de la ventana
`ini − 0,6 ≤ t ≤ fin` de esa escena.
**Corrección:** leer la salida del auditor y arreglar todas antes de tocar nada más.
Un elemento mal colocado falsea las otras cuatro métricas.

## 5 · Amontonado: "se ve cargado y no se entiende"

**Causa:** más de cuatro elementos vivos, o dos principales compitiendo. La cifra clave
llega mientras hay tres cosas más en pantalla.
**Corrección:** aplicar el reparto de papeles (`12`): un principal y sólo uno. Lo que
sobra baja a apoyo (380-420 px) o se retrasa 0,4 s.

## 6 · Relevo seco: "va rápido pero se ve pobre"

**El error más caro y el que tiene hoy el piloto.** Eventos/min por encima de la meta y
simultaneidad de 1,12: uno entra, uno sale, nunca dos a la vez. El montaje es correcto
en el papel y en pantalla es un pase de diapositivas rápido.
**Corrección:** no tocar el número de eventos. Añadir capas: suelo, rótulos y solapes
de 0,2-0,4 s en cada relevo (`12`, `14`).

## 7 · Remate sin golpe: "el final no cierra"

**Causa:** el remate se montó a la misma densidad —o más— que el desarrollo, y sin
frenada detrás. Sin contraste, la revelación es una frase más.
**Corrección:** escalada de 3-4 acentos y frenada de 1,2-2,0 s con un solo elemento
(`15`, `16`). Bajar el remate a 30-38 ev/min (`18`).

## 8 · Clavado: "los planos están muertos"

**Causa:** elementos de más de 2 s sin deriva ni cambio de estado. Da igual que el
fondo se mueva: un recorte inmóvil sobre un fondo que se acerca se lee como una pegatina.
**Corrección:** deriva de 6-12 px/s, o trocear en estados (`13`). Y si un elemento
necesita durar 4 s, casi siempre es que le falta un rótulo encima.

---

## Los dos síntomas que se confunden

| | Agrupado (1) | Relevo seco (6) |
|---|---|---|
| eventos/min | correcto o alto | alto |
| simultaneidad | media, con picos | plana, cerca de 1,0 |
| huecos | varios | pocos o ninguno |
| Qué se ve | tirones: rápido, vacío, rápido | uniforme y pobre |
| Corrección | cerrar huecos | añadir capas |

Confundirlos cuesta una tarde: se cierran huecos que no existen y el vídeo sigue igual.
La fila que los separa es la **simultaneidad**, no los eventos por minuto.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Diagnosticar viendo el vídeo | Se detecta el síntoma y se acierta la causa una de cada tres veces |
| Corregir dos síntomas a la vez | No se sabe cuál de los dos cambios funcionó |
| Añadir material antes de auditar | Se compra archivo para un problema que era de reparto |
| Tratar el relevo seco subiendo eventos | Se llega a 80 ev/min y el vídeo sigue viéndose pobre |
| Dar por buena una escena porque su ev/min pasa | El umbral es el de su tipo de bloque, no el global (`18`) |

## Relacionado

`10` densidad de eventos · `11` el hueco prohibido · `12` capas simultáneas ·
`13` ciclo de vida del elemento · `15` rampa de ritmo · `17` medir el montaje · `18` densidad por bloque

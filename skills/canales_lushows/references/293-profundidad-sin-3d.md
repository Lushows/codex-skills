# 293 · Profundidad sin 3D: el dominio del cuadro

**Qué resuelve:** en un collage **no hay lente**. No hay diafragma, no hay plano de foco,
y desenfocar un recorte de archivo no lo aleja: lo estropea. Así que de los cuatro ejes de
profundidad que mide `editpro/390`, aquí solo hay uno de verdad —**el escalón de
tamaño**—, y la pregunta cambia: no es cuánto separa un elemento de otro, sino **si hay
alguien mandando en el cuadro**.

Frontera, para no perder el tiempo:

- `22` tiene la receta prescriptiva del canal: cuántos planos, qué anchos, qué derivas.
- `26` tiene la oclusión, que es la otra prueba de quién está delante.
- `editpro/391` tiene la unidad y el escalón mínimo medido (75 % o menos de altura),
  `editpro/395` el reparto cuando el desenfoque está prohibido y `editpro/396` el
  diagnóstico eje por eje contra el plano frente.

Aquí va lo que ninguno de ellos tiene: la medida **del cuadro entero**, instante a
instante, y cómo la aplica el motor sin que nadie la escriba a mano.

---

## La medida: dominio

```python
# auditar.py
DOMINIO_MIN = 0.42

areas = sorted((ar for a, b, _, _, ar, _ in vidas if a <= t < b and ar > 0), reverse=True)
chato = len(areas) >= 2 and areas[0] / sum(areas) < DOMINIO_MIN
```

**Dominio = la parte de la superficie ocupada que se lleva el elemento mayor.** No es una
distancia entre dos piezas: es el reparto del cuadro en ese instante. Su aritmética es
elemental y por eso el umbral se puede defender:

| Qué hay en pantalla | Dominio |
|---|---|
| Dos elementos iguales | **0,50** |
| Tres elementos iguales | **0,33** |
| Cuatro iguales | 0,25 |
| Dos, con el mayor al doble de área | 0,67 |
| Dos, con el mayor un 35 % más de área | 0,57 |

`editpro/391` demuestra que el escalón mínimo en **ancho** es del 25 %, y que eso son un
44 % menos de **área**. Un cuadro con dos elementos en el que uno cumple ese escalón da
dominio 0,64. Con tres, dos en la cota de atrás y uno delante, sale 0,47. **Por debajo de
0,42 no cabe ningún reparto con escalón: es la firma aritmética de la rejilla.**

Un tramo cuenta solo si dura **1 s o más**. Medio segundo de empate mientras uno entra y
otro sale no es un cuadro plano; es una transición.

## Medido hoy en `ep01-lustig`

```
--- cuadro PLANO: ningun elemento manda (2.3 s) ---
    29.80 -  30.90  (1.10 s)  nombre   aviso_falsos, jefes_servicio_secreto, telegrafista
    48.80 -  50.00  (1.20 s)  torre    monton_chatarra, torre_citroen_noche, trenes_chatarr
```

**2,3 s de 63,45 s: el 3,6 % del episodio.** Los dos tramos son tres elementos a la vez, y
los dos aparecen en el mismo sitio del ciclo: cuando una pieza está muriendo, otra vive y
la tercera acaba de entrar. Es el momento en que el reparto se decide solo.

Y el segundo tramo tiene una lectura más: `torre_citroen_noche` es el mismo elemento del
caso de `292`. Una pieza puede fallar dos medidas independientes por causas distintas —no
se separaba del fondo *y* no manda en el cuadro— y **dos medidas señalando la misma pieza
es la señal más fiable que da la auditoría**.

## Cómo lo evita el motor sin que nadie lo escriba

El escalón no se escribe elemento a elemento: lo aplica `diccionario.py` al colocar.

```python
# el area del mayor que ya esta vivo y comparte tiempo con el que entra
mayor = max((o[2]-o[0]) * (o[3]-o[1]) for a, b, o, _ in vivos
            if o is not None and _solapan(t0, t1, a, b))
if mayor and pr:
    propia = ancho * ancho * pr
    if 0.74 <= propia / mayor <= 1.35:
        ancho = max(int(ancho * 0.79), suelo)     # se encoge, NUNCA se agranda
```

Cuatro decisiones dentro, y todas tienen motivo:

- **La banda 0,74–1,35 de área.** Es la zona de empate: por debajo ya hay escalón, por
  encima el que entra manda él. Coincide con el 0,563 de área que `editpro/391` fija como
  escalón mínimo, con holgura por los dos lados.
- **×0,79 de ancho, o sea ×0,62 de área.** Sale de la banda por abajo de una sola pasada.
  Un ×0,90 devolvería el problema al siguiente elemento.
- **Se encoge, nunca se agranda.** Crecer saca la pieza del lienzo por la sangría (`245`)
  o la mete encima de otra. Es la asimetría que hace que el algoritmo converja.
- **El suelo manda sobre el escalón.** `max(..., suelo)`: si encoger dejase el gráfico por
  debajo de su ancho legible (`297`), no se encoge. Cambiar un cuadro plano por un texto
  ilegible es cambiar un defecto por otro peor.

## El otro techo, el que nadie ve venir

Antes del escalón hay un techo de altura, y es el que más mueve los números:

```python
if pr and e.get("w", 400) * pr > 0.78 * 1080:
    e["w"] = int(0.78 * 1080 / pr)
```

`torre_citroen_noche` está escrito en el guion visual con `w: 1000`. Es una foto vertical
(proporción 1,55), así que a 1000 px de ancho mediría 1.556 de alto y se saldría del
cuadro. El techo lo deja en **542**. Quien escribió 1000 creía estar poniendo el elemento
que manda en la escena; lo que hay en pantalla es poco más de la mitad.

**Antes de acusar al escalón de aplanar un cuadro, hay que mirar qué `w` sobrevivió al
techo.** El guion visual imprime los anchos finales; son esos y no los escritos los que
entran en el dominio.

## Qué se hace con un tramo plano

En este orden, que es el barato primero:

1. **¿Se solapan dos de los tres?** Sin una sola oclusión no hay prueba de quién está
   delante, por mucho escalón que haya (`26`, `editpro/396` §3.5).
2. **Alargar al mayor, no encoger a los pequeños.** Subirle 0,3 s de vida al que manda
   suele cerrar el tramo sin tocar ningún ancho.
3. **Quitar el tercero.** Tres elementos de tamaño parecido durante 1,1 s no comunican
   tres cosas: comunican ruido. Y si al quitarlo el cuadro no cambia, sobraba (`299`).
4. **Solo al final, mover anchos a mano.** Es lo que rompe el equilibrio del cuadro
   (`246`) y obliga a recolocarlo todo.

## Lo que aquí no se puede hacer

El velo atmosférico de `editpro/395` —mezclar el elemento hacia el color del fondo— sí
funciona en este motor y es el segundo eje disponible. El desenfoque no: un recorte de
archivo desenfocado dentro de un collage de papel no se lee como lejano, se lee como una
foto mal escaneada. `22` lo permite para el plano medio cocinado en el PNG y funciona
porque va acompañado de sombra corta y deriva propia; suelto, sin parallax, es un defecto.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Pensar la profundidad como distancia entre dos piezas | En un cuadro de tres, las dos parejas pueden cumplir y el cuadro ser plano |
| Medir el escalón en ancho y no en área | Un 92 % de ancho es un 85 % de área: nada (`editpro/391`) |
| Cinco anchos distintos creyendo que son cinco planos | Nube de tamaños: ninguna cota separa |
| Agrandar el elemento que debe mandar | Se sale por la sangría o pisa a otro: hay que encoger al resto |
| Encoger un gráfico con texto por debajo de su suelo | Se cambia un cuadro plano por un texto ilegible (`297`) |
| Acusar al escalón sin mirar el techo de altura | `w: 1000` puede estar saliendo a 542 |
| Contar tramos planos de menos de 1 s | Eso es una transición, no un defecto |
| Desenfocar para alejar | Sin lente no hay desenfoque creíble: se lee como escaneo malo |

## Relacionado

`22` profundidad por capas (la receta del canal) · `26` superposición y oclusión ·
`21` peso visual y jerarquía · `246` equilibrio del cuadro · `245` la sangría ·
`294` la sombra que convence · `297` documentos como imagen · `299` cuándo una foto no
aporta · `editpro/390` la profundidad es separación medida · `editpro/391` el escalón de
tamaño · `editpro/395` profundidad sin desenfoque · `editpro/396` el plano que no separa

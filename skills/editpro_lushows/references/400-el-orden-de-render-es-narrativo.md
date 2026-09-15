# 400 — El orden de render es una decisión narrativa

**Qué resuelve:** el apilado se trata como fontanería —«pon el logo arriba»— cuando es la decisión más
barata y más poderosa del plano: **decidir quién tapa a quién es decidir quién importa.** Este bloque
(`400`–`409`) convierte esa decisión en un mecanismo que se puede leer, medir y depurar. Todo lo que sigue
está ejecutado hoy sobre el motor real del canal documental, `CANALES-LUSHOWS\piloto`.

> **Frontera.** `directorcreativo_lushows` decide el look. `canales_lushows/12` es la versión
> **prescriptiva** del apilado (cuántos elementos a la vez, qué papel tiene cada uno, quién se declara
> después de quién). `204` §2 explica el orden **de los efectos** frente al de las capas, y `80` es la
> introducción. **Este bloque es la versión mecánica y medida:** cómo se ejecuta el orden, qué se rompe en
> él y cómo se caza. Nada de eso se repite aquí.

---

## 1. El orden no es una propiedad: es una secuencia

En un editor con pistas, el orden parece una propiedad espacial: la pista 6 está «encima» de la 5. En un
filtergraph no hay pistas. Hay **una cadena**, y cada eslabón se come el resultado del anterior:

```python
ultimo = "bg"
for ele in esc["elementos"]:
    filtros.append(f"[{ultimo}][e{n}]overlay=x='{x}':y='{y}':"
                   f"enable='between(t,{e0:.2f},{e1:.2f})'[v{n}]")
    ultimo = f"v{n}"                 # motor.py:208 — el z es esta variable
```

`ultimo` **es** el eje z. No existe ningún campo `z`, ninguna capa numerada, ningún atributo de
profundidad: el orden de apilado es, literalmente, el orden de la lista `elementos` del guion visual. Esto
tiene tres consecuencias que valen por todo el bloque:

1. **Mover un elemento de sitio en la tabla lo mueve de plano.** No hay que tocar nada más.
2. **El orden es lineal, nunca un árbol.** Una capa solo puede ir encima de *todo* lo anterior, no
   encima de una cosa y debajo de otra. Para eso hace falta `402`.
3. **El orden se paga.** Cada eslabón es un `overlay` más que se ejecuta en cada fotograma, esté visible
   o no (`408`).

---

## 2. Las tres preguntas que deciden el orden

No son técnicas. Se contestan mirando el guion, no el código.

| Pregunta | Quién manda | Consecuencia en la lista |
|---|---|---|
| ¿Quién es el protagonista de **este** segundo? | la narración (`204` §5) | va el último de los grandes |
| ¿Qué es lo que **subraya** a otra cosa? | el sello, la flecha, el tachado | se declara **después** de lo que subraya |
| ¿Qué no puede estar debajo de nada **nunca**? | la cifra, el texto de servicio | último de todos (`406`) |

La segunda es la que más se rompe y la más fácil de arreglar: un acento declarado **antes** del elemento
que subraya queda enterrado debajo de él y no se ve. El síntoma no es un error, es «al sello le falta
fuerza».

---

## 3. Lo que el apilado del episodio real dice de la narración

Medido sobre `ep01-lustig` (5 escenas, 63,45 s, 59 elementos vivos), cruzando cada pareja que comparte
sitio **y** tiempo:

```
=== ep01-lustig ===  parejas vivas a la vez que se solapan: 31
escena    debajo                encima                 % tapado   s juntos
muerte    casilla_nombre        sin_padre                 28,0      1,07
torre     chatarreria           calle_paris               27,9      1,79
muerte    casilla_nombre        huella_expediente         26,8      0,44
metodo    columna_doble         boveda_servicio           23,7      0,33
torre     torre_construccion    hotel_crillon             18,9      1,74
por encima del 42%: 0 · por encima del 5%: 19
```

Treinta y una parejas se pisan y **ninguna pasa del 28%**. Eso no es suerte: es el colocador automático de
`diccionario.py` rechazando cualquier posición que supere el 42% (`383`). El orden de declaración decide
*quién* se lleva el mordisco; el umbral decide *cuánto*.

En el otro episodio del repo la foto es distinta: **9 de 23 parejas pasan del 42%, y 6 son el contador
sustituyéndose a sí mismo** (`cont_02` bajo `cont_05` bajo `cont_08` bajo `cont_10`, 100% cada una). No es
una pisada: es una sustitución, y confundirlas es el falso positivo clásico de cualquier auditoría de
apilado (`404`).

---

## 4. Por qué el z vive en una cadena y no en un árbol

El motor arma **un comando ffmpeg por escena** y concatena. Medido hoy, espiando el comando real sin
renderizar:

| escena | entradas `-i` | filtros | caracteres del filtergraph | comando completo |
|---|---|---|---|---|
| muerte | 16 | 33 | 4.896 | 7.180 |
| oficio | 8 | 17 | 2.296 | 3.510 |
| nombre | 10 | 21 | 3.024 | 4.670 |
| **torre** | **19** | **39** | **5.813** | **8.658** |
| metodo | 13 | 27 | 3.908 | 5.844 |

Unos **320 caracteres de filtergraph por elemento**. Un episodio de 12 minutos con los ~400 eventos que
pide el formato sería un único filtergraph de ~128.000 caracteres: **cuatro veces el límite de 32.767 de
la línea de comandos de Windows.** La arquitectura de «una escena, un comando» no es elegancia, es la
única que cabe. Y por eso el z es una secuencia corta y repetida, no una jerarquía global.

---

## 5. La regla de la casa, en una frase

> **El último declarado gana.** Así que la lista de elementos de una escena se lee de abajo arriba como se
> lee un collage: primero lo que sostiene, luego lo que va encima, y al final lo que hay que leer.

Si al mirar la tabla del guion visual no puedes decir en voz alta por qué el elemento *n* va después del
*n−1*, el orden es accidental y se nota en pantalla aunque nadie sepa señalar por qué.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Tratar el orden como detalle técnico y no como decisión | El plano tiene protagonista por azar |
| Declarar el acento (sello, flecha, tachado) antes de lo que subraya | Queda enterrado; «al sello le falta fuerza» |
| Reordenar la lista para arreglar una pisada | Se arregla el z y se rompe la jerarquía; la pisada se arregla moviendo, no apilando (`384`) |
| Suponer que un elemento puede ir encima de uno y debajo de otro | La cadena es lineal; eso exige dos `overlay` (`402`) |
| Contar pisadas sin comprobar que coinciden en el tiempo | El contador que se sustituye sale como 6 pisadas del 100% |
| Intentar montar el episodio entero en un filtergraph | 128.000 caracteres contra un límite de 32.767 |

## Relacionado

`401` quién gana cuando dos coinciden · `402` el z dinámico · `403` índices que se corren ·
`404` acumular o sustituir · `405` el fondo no es una capa más · `406` el texto siempre arriba ·
`408` lo que cuesta cada capa · `409` depurar un apilado · `80` capas y composición ·
`104` filter_complex · `105` superponer capas · `204` §2 el orden de render · `380` qué es pisar ·
`383` umbrales por tipo de contenido · `386` el elemento enterrado ·
`canales_lushows/12` capas simultáneas

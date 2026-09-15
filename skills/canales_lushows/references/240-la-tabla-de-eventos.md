# 240 · La tabla de eventos

**Qué resuelve:** el montaje deja de ser una lista de planos y pasa a ser **una tabla
de datos**. Un episodio de doce minutos son unos cuatrocientos eventos: colocarlos a
mano es inviable, declararlos y que el motor los monte no.

---

## El contrato

`motor.py` no sabe nada del episodio. Lee dos diccionarios y con eso construye un
comando de ffmpeg por escena. Todo lo que el montaje necesita decir tiene que caber
ahí dentro.

**La ESCENA** — seis claves, ninguna opcional salvo dos:

```python
{"id": "oficio", "ini": 16.15, "fin": 22.88, "fondo": "f_oficio",
 "mov": ("in", 0.10), "elementos": [...], "destellos": [...]}
```

`ini` y `fin` no los pone el montaje: salen de los silencios medidos de la locución ya
aprobada (`tiempos.json`). El montaje se cuelga de la voz, nunca al revés.

**El ELEMENTO** — tres claves obligatorias (`r`, `x`, `y`) y el resto con valor por
defecto. Lo que `motor.py` lee hoy, sacado del propio fichero:

```bash
grep -o 'ele\.get("[a-z_]*"\|ele\["[a-z_]*"\]' motor.py | sort -u
```

| Clave | Qué es | Defecto | Usada en `ep01-lustig` |
|---|---|---|---|
| `r` | alias del recurso (sin extensión) | — | 61 de 61 |
| `x`, `y` | esquina superior izquierda, en px o `"W*0.26"` | — | 61 de 61 |
| `w` | ancho en pantalla | 400 | 61 de 61 |
| `dura` | segundos que vive | 2.0 | 61 de 61 |
| `entrada` | `izq` `der` `arriba` `abajo` `fade` | `fade` | 61 de 61 |
| `rot` | grados | 0 | 61 de 61 |
| `ancla` | palabra del guion de la que cuelga | — | 45 de 61 |
| `offset` | adelanto/retraso respecto al ancla | 0 | 45 de 61 |
| `fade_out` | rampa de salida | 0.4 | 41 de 61 |
| `deriva` | `(dx, dy)` px por segundo | `(0,0)` | 27 de 61 |
| `desde` | alternativa al ancla: segundos desde `ini` | 0 | 16 de 61 |
| `ancla_n` | qué aparición de la palabra (0 = la primera) | 0 | 1 de 61 |
| `dur_entrada` | duración del gesto de entrada | 0.36 | 0 |
| `op` | opacidad | 1.0 | 0 |

Dos de ellas no aparecen nunca en el episodio y **siguen estando bien**: son la puerta
de salida para el caso raro. Una clave con defecto no cuesta nada; una clave que hay
que inventar a mitad de episodio cuesta un rediseño.

## Anclar a la palabra, no al segundo

`ancla` es lo que hace que la tabla sobreviva a un recorte de locución. Si la voz se
vuelve a grabar y «aprendiz» se desplaza 0,4 s, los elementos anclados se mueven con
ella; los que van por `desde` se quedan donde estaban. En `ep01-lustig` **45 de 61 van
por palabra y 16 por tiempo**, y los 16 son casi todos contrapesos, que por definición
no cuelgan de nada que se diga.

`offset` negativo es la regla, no la excepción: el elemento entra **antes** de su
palabra porque justo a tiempo llega tarde. La capa automática usa `-0.16` fijo.

## Las tres capas que llenan la tabla

La tabla no la escribe una sola mano. En `ep01-lustig` se reparte así:

| Capa | Quién la pone | Elementos |
|---|---|---|
| CLAVE | escrita a mano en `guion_visual.py` | 20 |
| AUTO | `diccionario.generar()`, palabra por palabra | 27 |
| peso | `diccionario.contrapeso()`, segunda pasada | 14 |
| | **total** | **61** |

La frontera es nítida y no se negocia: **todo lo que lleva cifras o rótulos propios va
a mano**. Un recurso con «1,00 m × 1,00 m» impreso colgado de la palabra «altura»
contradice a una voz que dice «trece mil setecientos metros», y eso hunde un canal de
documentales. El motor no sabe leer lo que hay dentro del PNG; quien escribe, sí.

## Lo que la tabla NO lleva

- **Rutas.** Se declara `"r": "ficha_policial"`, no una ruta. `buscar()` recorre las
  carpetas del episodio primero y el banco después (`192`, `248`).
- **Orden de pintado explícito.** El que entra después se pinta encima, y punto. Si eso
  importa, se ordena la lista.
- **Capas ni grupos.** La composición sale de los rectángulos, no de una jerarquía
  declarada (`242`).
- **Nada dependiente del render.** La tabla se puede auditar entera sin generar un solo
  fotograma, y ahí está su valor: `auditar.py` mide sobre ella (`140`).

## Los destellos van aparte

Un destello no es un elemento: es un filtro sobre **todo el cuadro**, así que vive en
su propia lista con su propio esquema (`ancla`, `offset`, `fuerza`, `ancho`). En
`ep01-lustig` hay 5, uno por bloque. Mezclarlos con los elementos obligaría a que el
motor distinga por tipo dentro del mismo bucle, y ese es el primer paso para que los
índices se corran (`153`, `249`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Poner tiempos absolutos en vez de anclas | Un recorte de locución desplaza todo el montaje |
| `offset` positivo por defecto | El elemento llega tarde a su propia palabra |
| Colgar del diccionario un recurso con cifras propias | La imagen contradice a la voz |
| Añadir una clave sin valor por defecto | Revienta todo elemento anterior de la tabla |
| Declarar la ruta en vez del alias | El episodio deja de poder pisar el banco común |
| Mezclar destellos y elementos en una lista | Bucle con casos, índices corridos (`153`) |

## Relacionado

`13` ciclo de vida del elemento · `29` plantillas de escena · `241` resolución de
anclas · `242` colocación por rectángulo · `249` extender el motor sin romperlo ·
`250` palabra → imagen: el método

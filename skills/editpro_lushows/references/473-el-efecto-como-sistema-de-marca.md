# 473 — El efecto como sistema de marca

> **Un efecto repetido con disciplina es una firma. Cinco efectos distintos son ruido.** Esa frase es
> todo el módulo. Lo difícil no es entenderla: es aguantarla en el episodio siete, cuando el mismo
> fogonazo de siempre te aburre a ti —que lo has visto cuatrocientas veces— y no le aburre a nadie más.

**Frontera, y es importante.** *Cuál* es el efecto de la marca lo decide el director creativo: eso
vive en `directorcreativo_lushows/84-motion-branding` y `.../141-sistemas-de-motion-de-marca`, junto
con el manual (`.../80-manual-de-marca`) y el principio de que la restricción es el motor
(`.../225-restricciones-como-motor`). **Aquí no se decide: aquí se ejecuta y se mide.** Este módulo es
cómo se convierte esa decisión en parámetros escritos, código que los aplica y una comprobación de que
no derivan.

Y una frontera interna: el destello que se usa de ejemplo en todo el módulo tiene su propio bloque.
**Qué puntúa** es `430`, **la forma de su curva** es `431`, **cómo se miden sus cuatro números** es
`432` y **por qué nunca va mudo** es `433`. Aquí no se enseña a hacer un destello: se enseña a
convertirlo en sistema.

---

## 1. Lo que se vuelve marca no es el efecto: son sus parámetros

Un destello lo tiene cualquiera. Lo que nadie puede copiarte sin proponérselo es **tu** destello: el de
0,075 segundos de medio ancho, campana de Gauss, contraste al 1,4 del brillo, anclado 40 ms antes de la
palabra. Esos cuatro números repetidos cien veces son el activo. El efecto es genérico; la
parametrización es propiedad.

De ahí sale la prueba de si tienes sistema o tienes costumbre:

> **Si no puedes escribir tu efecto como una tabla de números, no tienes un sistema de marca: tienes un
> hábito.** Y los hábitos derivan, porque dependen de tu memoria y tu memoria cambia de humor.

---

## 2. El destello del piloto, escrito

El canal documental tiene **un** efecto. Uno. Así está declarado, bloque por bloque, en
`ep01-lustig/guion_visual.py`:

```python
# ── LOS DESTELLOS ────────────────────────────────────────────────────────────
# Uno por bloque como maximo. El mas fuerte cae en "aprendiz", que es el golpe del
# gancho. Cada uno lleva su sonido: un fogonazo mudo se lee como un error.
DESTELLOS = {
    "muerte": [{"ancla": "hombre",   "offset": -0.04, "fuerza": 0.15}],
    "oficio": [{"ancla": "aprendiz", "offset": -0.05, "fuerza": 0.22, "ancho": 0.09}],
    "nombre": [{"ancla": "broma",    "offset": -0.04, "fuerza": 0.14}],
    "torre":  [{"ancla": "Eiffel",   "offset": -0.05, "fuerza": 0.18}],
    "metodo": [{"ancla": "consta",   "offset": -0.05, "fuerza": 0.20}],
}
```

Fíjate en la forma de la declaración, que es la parte transferible:

| Campo | Qué es | Fijo o variable |
|---|---|---|
| la técnica | campana de Gauss sobre brillo y contraste | **fijo para siempre** |
| `ancho` | medio ancho del fogonazo, 0,075 s por defecto | fijo salvo excepción justificada |
| la relación contraste/brillo | 1,4 | **fijo** |
| `offset` | −0,04 / −0,05 s | fijo |
| `ancla` | la palabra a la que se engancha | variable, es el contenido |
| `fuerza` | 0,14 a 0,22 | **variable, y es la única que dice algo** |

**Un solo parámetro lleva el significado.** Todo lo demás es constante. Ese es el aspecto de un sistema:
una perilla, y todas las demás soldadas.

---

## 3. La implementación, y las dos trampas que tiene

Esto es lo que construye el filtro, de `motor.py`, ejecutado en cada escena del piloto:

```python
if picos:
    bri = "+".join(f"{f:.3f}*exp(-pow((t-{td:.2f})/{s:.3f}\\,2))"
                   for td, f, s in picos)
    con = "+".join(f"{f*1.4:.3f}*exp(-pow((t-{td:.2f})/{s:.3f}\\,2))"
                   for td, f, s in picos)
    filtros.append(f"[{ultimo}]eq=brightness='{bri}':contrast='1+{con}':"
                   f"eval=frame[fx]")
```

**Trampa 1 — `eval=frame` no es opcional.** `eq` solo evalúa expresiones si se lo pides explícitamente.
Sin eso lee el valor una vez al iniciar, se queda con él, y **el destello simplemente no ocurre**. No
falla, no avisa, no devuelve error: el vídeo sale entero y sin efecto. Es exactamente la clase de fallo
silencioso que te hace revisar la fuerza, el ancla y el ancla_n durante media hora.

**Trampa 2 — la coma de `pow()` hay que escaparla.** Dentro de un filtro de ffmpeg la coma separa
filtros, así que `pow(x,2)` rompe el grafo entero. Por eso el `\\,` en la cadena de Python. El mensaje
de error que devuelve ffmpeg cuando esto pasa no menciona la coma por ninguna parte.

**Y la decisión de oficio:** la campana de Gauss, no un escalón. Un destello cuadrado —subir el brillo
durante N fotogramas y bajarlo— se lee como un fotograma corrupto, no como luz. La forma de la curva es
la diferencia entre un efecto y un defecto, y está desarrollada en `431`.

---

## 4. Un sonido por cada destello

```python
# los destellos de luz llevan su golpe: un fogonazo mudo se lee como un error
```

Está en `acabar.py` del episodio, y para el sistema de marca lo que importa es esto: **si el efecto es
visual, su pareja sonora forma parte del efecto**, no es una capa aparte que a veces se pone. Se
declaran juntos, se verifican juntos y se retiran juntos. El porqué —qué le hace el cerebro a un salto
de luz sin causa— y qué sonido exactamente están en `433`.

---

## 5. La prueba del tercer episodio

| Cuántas veces ha aparecido | Qué es | Qué haces |
|---|---|---|
| 1 vez | un experimento | mídelo (`472`) y decide |
| 2 veces | una coincidencia | escríbelo o mátalo |
| **3 veces con los mismos números** | **un sistema** | documéntalo (`478`) y no lo toques |
| 3 veces con números distintos | **deriva** | vuelve a la tabla, no a tu memoria |

La deriva es el fallo real de los canales que se ven «casi» iguales. Nadie decidió cambiar nada: es que
en el episodio 4 el destello salió a 0,18 porque ese día se veía mejor, y en el 7 a 0,25 porque el
material era más oscuro. Cuatro decisiones razonables, una sola consecuencia: la marca dejó de existir.

---

## 6. Cómo se comprueba que no ha derivado

Si los efectos viven declarados en código, la comprobación es trivial y hay que correrla en cada
episodio:

```bash
# todos los destellos declarados en todos los episodios, con sus numeros
grep -h -A10 '^DESTELLOS = {' */guion_visual.py \
  | grep -oE '"(fuerza|ancho|offset)": [-0-9.]+' | sort | uniq -c
```

Corrido sobre los dos episodios que existen hoy en el piloto (11 destellos entre los dos), devuelve:

```
      1 "ancho": 0.09         <- dos valores distintos para el mismo parametro "fijo"
      1 "ancho": 0.095
      1 "fuerza": 0.12 ... 2 "fuerza": 0.22   <- once valores distintos de fuerza
      2 "offset": -0.03
      4 "offset": -0.04
      5 "offset": -0.05
```

Léelo columna a columna. `offset` está sano: tres valores muy juntos, todos negativos, todos en la misma
horquilla. `fuerza` **debe** variar, porque es la perilla del significado. Pero `ancho` es el parámetro
declarado como fijo y **ya tiene dos valores**: 0,09 y 0,095. Cinco milésimas de segundo que nadie
decidió y que nadie va a ver — y así es exactamente como empieza siempre. Con dos episodios se corrige
en treinta segundos; con veinte, ya no hay sistema que reconstruir.

Esta comprobación cuesta un segundo y es la que hace que el episodio 20 se parezca al 1 sin que nadie
tenga que acordarse de nada.

---

## Errores frecuentes

1. **Inventar un efecto nuevo por episodio.** Eso no es variedad, es no tener sistema.
2. **Cambiar los números «porque hoy se ve mejor».** Ese es el mecanismo exacto de la deriva.
3. **Tener el sistema en la cabeza y no en una tabla.** La memoria cambia de humor; la tabla no.
4. **Dejar más de un parámetro variable.** Si varían tres, ninguno significa nada.
5. **Aburrirte de tu propio efecto y matarlo.** Tú lo has visto cuatrocientas veces; el espectador, dos.
6. **Usar un escalón en vez de una curva.** Se lee como fallo de codificación, no como luz.
7. **Olvidar `eval=frame`.** El efecto desaparece en silencio y el archivo sale perfecto.
8. **Olvidar escapar la coma de `pow()`.** Rompe el grafo y el error no menciona la coma.
9. **Dejar el efecto visual mudo.** Un fogonazo sin golpe se lee como un parpadeo del reproductor.
10. **Decidir aquí cuál es el efecto de la marca.** Esa decisión es de dirección creativa; este módulo
    la ejecuta y la vigila.
11. **No comprobar la deriva en cada episodio.** Cuesta un segundo y es lo único que mantiene la serie.

---

## Relacionado

- `directorcreativo_lushows/84-motion-branding` y `.../141-sistemas-de-motion-de-marca` — **quién decide
  cuál es el efecto de la marca**. Ahí, no aquí.
- `directorcreativo_lushows/80-manual-de-marca` — dónde se escribe el sistema para que exista fuera de ti.
- `directorcreativo_lushows/225-restricciones-como-motor` — por qué una sola perilla produce más que diez.
- `430`, `431`, `432`, `433` — **el destello**: cuándo puntúa, la forma de su campana, cómo se miden sus
  cuatro números y por qué nunca va mudo. El oficio del efecto vive ahí; aquí vive su gobierno.
- `208` — sistema de motion de marca en editpro: tiempos, curvas, entrada y salida canónicas.
- `429` — cuándo quitar un efecto, incluso uno que ya es la firma del canal.
- `88` — plantillas reutilizables: el efecto parametrizado y listo para instanciar.
- `478` — la ficha escrita del efecto, con sus costes medidos.
- `474` — qué pasa con el sistema cuando son ocho episodios y no uno.
- `52` — transiciones de marca; `77` — sonido real contra efecto, para la pareja sonora del destello.
- `canales/125-musica-y-destello` — el golpe que acompaña al fogonazo.
- `canales/254-motivos-lo-que-vuelve-a-proposito` — la diferencia entre repetir y quedarse sin material.

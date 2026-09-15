# 249 · Extender el motor sin romperlo

**Qué resuelve:** `motor.py` son 282 líneas que montan un episodio entero. Tocarlo es
inevitable —cada efecto nuevo pasa por ahí— y hay una forma de hacerlo que no
desincroniza el episodio de la voz.

---

## La regla de oro

**El índice de entrada de ffmpeg lo lleva un contador propio, y ese contador solo avanza
cuando la entrada se añade de verdad.**

```python
n = 0
for ele in esc.get("elementos", []):
    ...
    if e1 <= e0:
        continue
    # El indice lo manda la posicion REAL en 'entradas', no el del bucle: si un
    # elemento se descarta arriba, enumerate() sigue contando y ffmpeg acaba
    # pidiendo una entrada que no existe.
    n += 1
    entradas += ["-loop", "1", "-framerate", str(FPS), "-t", f"{dur:.3f}",
                 "-i", escalado(buscar(ele["r"]), anchura)]
```

Probado con una escena de cuatro elementos, uno de ellos con `dura: 0` (el motor lo
descarta porque `e1 <= e0`):

```
elementos declarados: 4 (uno con dura=0)
contador propio -> OK
  FALLO PRUEBA:
    Error binding filtergraph inputs/outputs: Invalid argument
enumerate()     -> FALLO
```

El mismo montaje, cambiando solo quién lleva el índice. Y el mensaje sale por el
`stderr` de un subproceso, no como excepción de Python: si no se mira `returncode`, el
bucle sigue tan tranquilo (`153`).

## Y la red debajo

```python
if len(partes) != len(ESCENAS):
    raise SystemExit(
        f"\nABORTADO: {len(ESCENAS)-len(partes)} escena(s) fallaron. "
        f"Concatenar las demas dejaria el episodio desincronizado de la voz "
        f"desde ahi hasta el final.")
```

Un episodio corto pero sincronizado es recuperable; uno completo y desfasado hay que
verlo entero para descubrirlo. **No se concatena si falta una escena**, y punto.

## Qué se puede añadir gratis

El esquema del elemento está construido casi entero sobre `ele.get(clave, defecto)`.
Añadir una clave nueva no rompe ni un elemento anterior: los 61 de `ep01-lustig` siguen
funcionando con `dur_entrada` y `op` declaradas, que ninguno usa (`240`).

Lo mismo vale para la escena: `esc.get("destellos", [])` y `esc.get("mov", ("in", 0.12))`
permiten que un guion visual antiguo se monte sin tocarlo.

**Una clave con defecto es barata. Una clave obligatoria nueva obliga a reescribir toda
tabla existente.** Ante la duda, defecto.

## Qué NO se puede añadir gratis

Un filtro nuevo **sí** tiene coste, porque la cadena de etiquetas es un hilo:

```python
filtros.append(f"[{ultimo}][e{n}]overlay=...[v{n}]")
ultimo = f"v{n}"
...
if picos:
    filtros.append(f"[{ultimo}]eq=brightness='{bri}':contrast='1+{con}':eval=frame[fx]")
    ultimo = "fx"
filtros.append(f"[{ultimo}]format=yuv420p[out]")
```

La variable `ultimo` es el contrato: **todo filtro que se inserte tiene que leer de
`ultimo` y volver a asignarlo**. Un filtro que escribe una etiqueta que nadie consume es
un filtro que ffmpeg rechaza; uno que lee de una etiqueta ya consumida, también.

Y hay un detalle de ffmpeg que cuesta una tarde si no se sabe: **`eq` solo evalúa
expresiones si se le pide `eval=frame`**. Sin eso lee el valor una vez al iniciar y el
destello sencillamente no ocurre, sin error.

## La lista de comprobación

Antes de dar por bueno un cambio en `motor.py`:

1. **¿Algún `continue` nuevo dentro del bucle de elementos?** Si lo hay, comprobar que
   el contador no ha avanzado todavía en ese punto.
2. **¿El filtro nuevo lee de `ultimo` y lo reasigna?**
3. **¿La clave nueva tiene defecto?** Probar montando un guion visual anterior sin
   tocarlo.
4. **¿`auditar.py` sigue midiendo lo mismo que el motor renderiza?** Si el cambio afecta
   a la vida o al rectángulo de un elemento, hay que replicarlo en el auditor o el
   montaje medido deja de ser el montaje renderizado (`241`, `242`).
5. **Correr `auditar.py` antes y después.** Las ocho cifras del cuadro de mando son la
   prueba de regresión de este canal: si un cambio «de forma» mueve la simultaneidad,
   no era de forma.
6. **Renderizar una escena, no el episodio.** `render_escena()` es llamable suelta y
   tarda un minuto y medio; el episodio entero, mucho más.

## Dos cosas que no hay que refactorizar todavía

**Las tres copias de `resolver()`.** Están duplicadas y hoy coinciden al milisegundo
(`241`). Unificarlas es correcto, pero es un cambio que toca los tres ficheros a la vez y
que hay que hacer con la comprobación cruzada delante, no de pasada mientras se añade un
efecto.

**El `scale=4320` del fondo.** Es el 44 % del tiempo de render de una escena (`248`) y es
el sitio evidente donde ganar velocidad. También es lo que da la calidad del movimiento
de fondo. Se toca con una comparación de fotogramas al lado, no a ojo.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| `enumerate()` sobre una lista con `continue` | ffmpeg pide una entrada que no existe y la escena falla entera |
| `capture_output=True` sin mirar `returncode` | El fallo se traga dentro del bucle |
| Concatenar las escenas que sí salieron | Episodio desincronizado de la voz hasta el final |
| Filtro nuevo que no reasigna `ultimo` | Etiqueta huérfana y filtergraph rechazado |
| `eq` sin `eval=frame` | El destello no ocurre, sin un solo error |
| Clave nueva sin valor por defecto | Toda tabla anterior deja de montar |
| Cambiar la vida de un elemento solo en el motor | El auditor aprueba un montaje que no es el renderizado |

## Relacionado

`153` índices corridos · `150` el catálogo del fallo silencioso · `240` la tabla de
eventos · `241` resolución de anclas · `248` pre-escalado y caché · `232` presupuesto de
render

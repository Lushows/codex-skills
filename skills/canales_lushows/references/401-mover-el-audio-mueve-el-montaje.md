# 401 · Mover el audio mueve el montaje

**Qué resuelve:** qué se rompe cuando la locución cambia de duración después de estar
montado el episodio, y cómo trasladarlo todo sin volver a mirar el vídeo con un
cronómetro. Es la contrapartida obligatoria de § `400`.

---

## Lo que sobrevive solo y lo que no

Medido en el episodio 1, que tiene **276 elementos escritos a mano**:

| Cómo está anclado | Cuántos | Qué pasa al cambiar el audio |
|---|---|---|
| `"ancla": "palabra"` | **244 (88%)** | se recolocan solos al realinear (`tiempos.py`) |
| `"desde": 16.15` | **61** | apuntan a un segundo que ya no significa lo mismo |
| límites de `BLOQUES` | ~119 números | idem: el último bloque acaba antes que el audio |
| `cuando("x", 6.92)` en `acabar.py` | 11 | el defecto deja de cuadrar y la alarma se vuelve ruido |

**Esa proporción es el argumento de fondo para anclar por palabra siempre que se pueda**
(§ `241`). Un elemento colgado de «Eiffel» sigue cayendo en «Eiffel» aunque el audio se
rehaga entero. Uno colgado del segundo 34,41 no sabe que el mundo se movió.

## El reloj

`pausas.py` escribe `reloj-minN.json` al recomponer: la lista exacta de silencios con su
posición vieja y su posición nueva. De ahí sale una función monótona `viejo → nuevo` que
es **exacta dentro del habla** (allí sólo hay un desplazamiento) y reparte
proporcionalmente dentro de una pausa acortada.

```python
f = pausas.reloj(json.load(open("reloj-min3.json")))
f(34.41)   # -> 30.92
```

## Migrar el fichero, no aplicar el reloj al vuelo

La tentación es aplicar el reloj en el ensamblador y no tocar los minutos. **No.** Si se
hace así, `min3.py` dice `16.15` y el vídeo enseña `14.89` para siempre, y nadie que lea
el fichero puede creerse un número.

> Un número que no se puede creer es peor que un número que hay que migrar.

`piloto/trasladar.py` reescribe los ficheros **una vez**, y el reloj queda como registro
de lo que se hizo. Tiene `--ver` para enseñar el cambio antes de tocar nada, y conviene
usarlo: los límites de bloque deben quedar **encadenados** (el fin de uno es el inicio del
siguiente) y el último debe morir **exactamente** donde muere el audio, no dos centésimas
antes por redondeo.

## Lo que NO se traslada

- **`dura` de un elemento anclado a palabra.** Es una decisión visual («esta lámina se ve
  tres segundos»), no una posición en el audio. Para eso está el compás (§ `402`).
- **Las duraciones del contrapeso.** Existen para tapar un hueco concreto y se recalculan
  solas en el montaje siguiente.

## El efecto secundario que hay que medir después

Encoger el audio sin encoger las imágenes **ralentiza el montaje en términos relativos**:
la misma lámina de 3,2 s pasa a cubrir más palabras que antes. Después de trasladar hay
que volver a auditar los diez minutos, y casi seguro habrá que bajar el compás (§ `402`).

## Relacionado

§ `400` (el silencio) · § `241` (resolución de anclas) · § `402` (el compás) · § `236`
(memoria entre escenas) · § `240` (la tabla de eventos)

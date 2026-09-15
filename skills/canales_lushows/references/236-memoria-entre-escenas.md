# 236 · Memoria entre escenas

**Qué resuelve:** el choque entre las dos reglas buenas del canal. La producción se hace
**por tramos cerrados de un minuto** (`98`), y la memoria antirrepetición **dura todo el
episodio** (`253`). A un minuto las dos caben en el mismo proceso y nadie nota la
contradicción. A doce minutos, cada tramo se monta en su propio proceso y en su propio día
— y entonces la memoria se reinicia once veces sin que nada avise.

---

## Dónde vive la memoria hoy

Un diccionario global de módulo, vaciado una sola vez desde el guion visual:

```python
# diccionario.py
_VISTO = {}

def olvidar():
    """Reinicia la memoria de recursos usados. Se llama UNA vez por episodio."""
    _VISTO.clear()
```

```python
# ep01-lustig/guion_visual.py:153-162
diccionario.MOTIVOS = MOTIVOS
diccionario.olvidar()                      # la memoria dura todo el episodio
for _nom, _ini, _fin, _f, _m in BLOQUES:   # PRIMERO toda la mano, del episodio entero
    recordar(CLAVE.get(_nom, []), PALABRAS, _ini, _fin)
```

Vive en la memoria del proceso. **Muere con él.** Mientras el episodio entero se importe
de una vez, eso es exactamente lo que hay que hacer y no hay nada que arreglar. El
problema empieza cuando «el episodio» deja de caber en una importación.

## Lo que cuesta reiniciarla en cada frontera

Se monta el mismo piloto dos veces: una en un solo proceso —como hoy— y otra llamando a
`olvidar()` al empezar cada bloque, que es lo que pasa de hecho cuando cada tramo se monta
por separado. Mismo guion, mismo vocabulario, mismo material:

| | Elementos | Recursos distintos | Usos/recurso | Choques entre tramos |
|---|---|---|---|---|
| **Un proceso** (hoy) | 59 | **56** | 1,05 | **0** |
| **Tramo a tramo** | 62 | 52 | 1,19 | **7** |

Lo que se ve en pantalla al reiniciar, con la distancia real entre las dos apariciones:

```
titular_prensa      nombre -> torre      6,70 s
ficha_identidades   oficio -> nombre     6,73 s
casilla_nombre      muerte -> nombre    12,93 s
columna_doble       torre  -> metodo    14,17 s
titular_prensa      torre  -> metodo    17,36 s
mapa_ruta           torre  -> metodo    21,51 s
titular_prensa      nombre -> metodo    24,06 s
```

`titular_prensa` **cuatro veces** en sesenta y tres segundos, dos de ellas a menos de siete.
Y ahora lo grave, que es lo mismo que enseñó `253`:

> **Las dos versiones pasan la métrica.** 1,19 usos por recurso está por debajo del umbral
> de 1,25 del canal. El montaje roto **gana** en densidad —62 elementos contra 59, porque
> reutilizar es más fácil que buscar— y la única señal de que algo va mal es que hay cuatro
> recursos menos en pantalla. Nadie mira ese número.

## Por qué a doce minutos es peor de lo que parece

Dos apariciones sólo chocan si están a menos de 25 s. Con tramos de un minuto, la zona de
riesgo es **la cola de un tramo y la cabeza del siguiente**: unos 50 s alrededor de cada
frontera. Un episodio de doce minutos tiene once fronteras:

```
11 fronteras x 50 s de zona ciega = 550 s de 720  ->  el 76 % del episodio
```

Tres cuartas partes del episodio con el antirrepetición parcialmente ciego. Y el defecto
se concentra justo donde más canta, porque la frontera entre tramos es también donde el
espectador acaba de oír una promesa y está decidiendo si sigue.

## El arreglo: que la memoria viaje en un fichero

No hay que cambiar la regla ni el tamaño de la ventana. Hay que sacar `_VISTO` del proceso.

```python
MEM = os.path.join(EPI, "salida", "_visto.json")

def cargar_memoria():
    diccionario.olvidar()
    try:
        diccionario._VISTO.update(json.load(io.open(MEM, encoding="utf-8")))
    except Exception:
        pass                                  # el primer tramo no tiene de donde cargar

def guardar_memoria():
    io.open(MEM, "w", encoding="utf-8").write(json.dumps(diccionario._VISTO))
```

Y el tramo se monta así, en su proceso, sin saber nada de los demás:

```python
cargar_memoria()
for n, i, f, _a, _b in BLOQUES:              # la mano del episodio ENTERO sigue yendo primero
    recordar(CLAVE.get(n, []), PAL, i, f)
... generar() ... contrapeso() ...
guardar_memoria()
```

Ejecutado sobre el piloto, montando los cinco bloques en secuencia con carga y guardado en
cada uno:

```
TRAMO A TRAMO + memoria en disco: 59 elementos · 56 recursos · 0 choques
tamano de _visto.json: 3009 bytes para 59 gestos
```

**Idéntico al proceso único.** Los mismos 59 elementos, los mismos 56 recursos, cero
choques. Y cuesta 3 KB: a 700 gestos son unos 36 KB, que es nada al lado de los gigabytes
que ocupa el resto del episodio (`239`).

## Las tres reglas que hay que respetar al persistirla

1. **La mano se anota entera, siempre.** `recordar()` recorre **todos** los bloques del
   episodio antes de generar, también en el tramo 7. La capa escrita a mano se conoce de
   antemano y mirar sólo hacia atrás fue el fallo 2 y 3 de `253`. Persistir la memoria no
   sustituye a eso: se hacen las dos cosas.
2. **Se guarda al terminar el tramo, no al terminar el episodio.** Si el montaje se
   interrumpe, lo guardado es lo que ya está decidido y renderizado.
3. **Rehacer un tramo obliga a rehacer su memoria.** Si se reescribe el tramo 5, lo que
   anotó queda en el fichero y bloquea recursos que ya no usa. La forma limpia es guardar
   **un fichero por tramo** (`_visto_t05.json`) y cargar la unión de los anteriores, para
   poder tirar el del tramo que se rehace.

## Lo que la memoria NO debe recordar

- **Los motivos.** `m_consta`, `m_cuenta` y `linea` vuelven a propósito: son la gramática
  del episodio. `_anotar()` ya los excluye, y el fichero hereda esa exclusión (`254`).
- **Nada de otro episodio.** La ventana de 25 s es para el ojo dentro de un vídeo. Entre
  episodios el problema es distinto y se lleva con el banco, no con esta memoria (`231`).
- **Los tiempos absolutos si se reordena el guion.** La memoria guarda segundos del
  episodio. Si se mueve un tramo de sitio, el fichero miente y hay que rehacerlo entero.

## Cómo comprobar que la memoria cruzó la frontera

```python
# antes de montar el tramo N, con la memoria ya cargada
print(len(diccionario._VISTO), "recursos recordados de los tramos anteriores")
```

Si en el tramo 7 ese número es cero, la memoria no viajó y los seis tramos anteriores son
material libre para repetir. Es una línea de `print` y caza el fallo entero.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Montar cada tramo en su proceso sin persistir `_VISTO` | 7 repeticiones visibles por cada 63 s de frontera |
| Fiarse de «usos por recurso» para detectarlo | 1,19 pasa el umbral de 1,25 con cuatro repeticiones en pantalla |
| Alegrarse de que salen más elementos | Salen más porque repite: la densidad subió con la moneda que se nota |
| Anotar la mano sólo del tramo que se monta | Vuelve el fallo 2 de `253`, ahora entre tramos |
| Guardar la memoria al final del episodio | Una interrupción la pierde entera |
| No tirar la memoria del tramo que se rehace | Bloquea recursos que ese tramo ya no usa |
| Arrastrar la memoria de un episodio al siguiente | Se agota el cajón por una regla que no aplica (`231`) |
| Dos montajes a la vez sobre el mismo episodio | Se pisan el fichero y la caché (`158`) |

## Relacionado

`253` la ventana antirrepetición · `254` motivos: lo que vuelve a propósito · `252`
alternativas y rotación · `235` palabras repetidas y anclaje · `230` el tramo cerrado ·
`231` el banco acumulativo · `239` el episodio como proyecto · `98` episodios largos ·
`158` procesos que se pisan · `150` catálogo del fallo silencioso

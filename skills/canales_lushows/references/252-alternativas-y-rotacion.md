# 252 · Alternativas y rotación

**Qué resuelve:** que una palabra que se repite no traiga siempre la misma imagen. Una
entrada del diccionario puede declarar varias opciones, y el generador elige entre ellas
la que lleva más tiempo sin salir. Suena trivial y no lo es: **la memoria que decide eso
estuvo viviendo dentro de la escena**, y esa fue la causa raíz de la repetición que se
vio en pantalla.

---

## La forma de una entrada

```python
V = {
    "parís":  (["calle_paris", "grandes_bulevares", "opera_1920s"], "objeto"),
    "torre":  (["torre_postal", "torre_citroen"],                   "heroe"),
    "cien":   ("panorama_paris_1926",                               "objeto"),
}
```

Una cadena o una lista. En el episodio 01: **48 entradas, 13 con alternativa (27%), 56
recursos nombrados**. Las alternativas están donde la palabra se repite —«parís»,
«torre», «eiffel», «llamaba»— y no donde la palabra es única.

## La elección

```python
opciones = [o for o in opciones if o not in NUNCA_AUTO]
if not opciones:
    continue
recurso = max(opciones, key=lambda o: _ultima(o, t))   # la MÁS olvidada
if _ultima(recurso, t) < 25.0:
    continue                                           # ni la más olvidada sirve
```

Dos decisiones en cuatro líneas. La primera: gana la más olvidada, no la primera de la
lista; si ganase la primera, las otras dos serían decorativas. La segunda, y es la que
salva el montaje: **si ni siquiera la más olvidada respeta la ventana, no se pone nada**.
Repetir para tapar un hueco es peor que el hueco.

## Qué opción gana, medido

De los 27 elementos que la capa AUTO coloca en el minuto 1:

| Entrada | Veces | Lectura |
|---|---|---|
| opción 1 de 1 | 17 | entradas sin alternativa |
| opción 1 de 2 | 8 | la lista existía y ganó la primera |
| opción 2 de 2 | 1 | la rotación se usó de verdad |
| opción 1 de 3 | 1 | |

Una sola rotación efectiva en sesenta y tres segundos. Eso **no** significa que las
alternativas sobren: significa que en un minuto casi nada se repite, y que las listas
están para el episodio de doce minutos, donde «torre» suena catorce veces. Lo que sí
dice el número es que las alternativas no son un sustituto de tener material (`259`).

## La memoria vive en el módulo, no en la escena

```python
# ── MEMORIA DE LO YA VISTO, PARA TODO EL EPISODIO ──────────────────────────
# Estaba dentro de generar(), o sea que se reiniciaba EN CADA ESCENA: el
# antirrepeticion funcionaba dentro de un plano y no hacia nada entre escenas.
_VISTO = {}

def olvidar():
    """Reinicia la memoria de recursos usados. Se llama UNA vez por episodio."""
    _VISTO.clear()
```

Reproducido: basta con volver a poner el `_VISTO.clear()` dentro de `generar()` para
recuperar el fallo original.

| Memoria | Elem | ev/min | Simult | Recursos distintos | Usos por recurso |
|---|---|---|---|---|---|
| por escena (el fallo) | 63 | 63,4 | 2,13 | 47 | **1,32** |
| de módulo (actual) | 61 | 62,4 | 2,02 | **55** | **1,11** |

Y lo que el espectador ve, con la memoria por escena:

```
   3x  columna_doble     en 20.7, 46.1, 59.9       6.7 s  ficha_identidades  (16.3 y 23.0)
   3x  balanza           en 33.0, 57.2, 61.5       7.2 s  torre_citroen_noche(39.6 y 46.8)
  12.0 s titular_prensa  (33.7 y 45.8)            12.9 s  casilla_nombre     (10.7 y 23.6)
  13.8 s columna_doble   (46.1 y 59.9)            19.4 s  sin_padre          ( 9.1 y 28.5)
```

Ocho parejas por debajo de la ventana. Fíjate en que **el montaje mejora en los números
de densidad** (63 elementos, simultaneidad 2,13): la versión rota parece mejor en todo
salvo en lo único que el ojo nota. Una métrica que sube mientras el vídeo empeora es la
definición de métrica peligrosa (`147`).

## Dónde se limpia

`olvidar()` se llama una vez, en el guion visual, antes del bucle de bloques. Ni en
`generar()`, ni en `contrapeso()`, ni al cambiar de escena. Si un día hace falta montar
dos episodios en el mismo proceso, la llamada es el único punto que hay que tocar.

```python
diccionario.MOTIVOS = MOTIVOS
diccionario.olvidar()   # la memoria de repeticion dura todo el episodio
```

## La lista se ordena por calidad, no por capricho

Aunque gane la más olvidada, el orden importa: con empate —todas sin usar, que es lo
normal al principio del episodio— `max` devuelve la primera. Así que la primera de la
lista es la que se verá en el primer uso, y debe ser la mejor pieza. Las siguientes son
el plan B y el plan C.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Reiniciar la memoria por escena | 1,32 usos por recurso y ocho parejas repetidas |
| Elegir siempre la primera de la lista | Las alternativas no existen; vuelve la repetición |
| Poner alternativas que no significan lo mismo | La palabra deja de mandar sobre la imagen |
| Rellenar con la más olvidada aunque incumpla la ventana | Repetición visible por tapar un hueco |
| Ordenar la lista al azar | La mejor pieza no se ve nunca en el primer uso |
| Llamar `olvidar()` dentro de `generar()` | Es el mismo fallo con otro nombre |

## Relacionado

`253` · `250` · `254` · `259` · `147` · `10`

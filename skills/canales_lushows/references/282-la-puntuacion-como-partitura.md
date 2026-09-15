# 282 · La puntuación como partitura

**Qué resuelve:** en este canal la puntuación no es ortografía. Hace **dos trabajos
técnicos** distintos, y los dos deciden dónde cae la imagen:

1. **Le dice a la voz dónde respirar.** Las pausas no se editan después: se escriben.
2. **Le dice al alineador dónde cortar.** `tiempos.py` parte el texto en grupos fónicos
   por los signos, y sobre esos grupos reparte los segundos de cada palabra.

Si un signo falta en la lista del alineador, la segunda función se rompe **aunque la voz
haya hecho la pausa perfectamente**. Y no avisa.

---

## Lo que compra cada signo, medido

Dos palabras, `es-MX-JorgeNeural` a `-6%`, hueco medido con `silencedetect` sobre el MP3:

| Escrito | Silencio real | Nota |
|---|---|---|
| `uno dos` | **0,000 s** | Sin signo no hay hueco |
| `uno, dos` | **0,342 s** | La coma |
| `uno; dos` | 0,381 s | Igual que la coma, a efectos prácticos |
| `uno: dos` | 0,383 s | Igual |
| `uno — dos` | 0,341 s | Igual |
| `¿uno? dos` | **0,397 s** | ⚠️ **No es una pausa de punto** |
| `¡uno! dos` | 0,383 s | ⚠️ Tampoco |
| `uno... dos` | 0,361 s | ⚠️ Tampoco, si van dentro de la frase |
| `uno… dos` (un solo carácter) | 0,398 s | Igual |
| `«uno» dos` | 0,347 s | Igual |
| `uno. dos` | **1,057 s** | **El punto es el único signo largo** |
| `uno.\n\ndos` | 1,057 s | El párrafo **no** añade nada al punto |
| `uno.. dos` · `uno.... dos` | 1,057 s · 1,048 s | Repetir puntos tampoco añade |

Dos conclusiones que valen para todo el guion:

- **Sólo hay dos duraciones de pausa: ≈0,36 s y ≈1,06 s.** Todo lo que no sea punto
  compra lo mismo. Las combinaciones raras (`....`, `\n\n`, `···`) no compran más.
- **Para una pausa de verdad —dos, tres, cuatro segundos— la puntuación no sirve.** Hay
  que construir el silencio en el audio (§ `288`).

En el guion real esto se ve: el `···` de `guion.md` se convierte en `...` **pegado a la
frase anterior**, o sea `hombre....`, y el hueco medido ahí es **1,128 s**. Es un punto,
no un suspiro largo.

## 🔴 El fallo del alineador: 47 palabras fuera de sitio

`tiempos.py` parte el texto en grupos fónicos así:

```python
trozos = [t.strip() for t in re.split(r"(?<=[.,;:?!…»])\s+", texto) if t.strip()]
```

Durante meses esa clase de caracteres fue `[.,;:]`. **Sin `?`, sin `!`, sin `…`, sin
`»`.** Y el alineador, que empareja los grupos de texto con los silencios más largos que
ha medido en el audio, se encontraba con **más silencios reales que grupos de texto**:
la voz respiraba en un `?` que para el alineador no existía.

Reproducido sobre `piloto/episodio01` —201 palabras, una interrogación y un `…`—,
comparando las dos versiones de la expresión regular contra el mismo MP3:

| Medida | Resultado |
|---|---|
| Palabras que se mueven | **51 de 201** |
| Palabras desplazadas más de 0,3 s | **47** |
| Desplazamiento medio (todas) | 0,694 s |
| **Peor caso** | «Son» entra en **23,24 s** cuando se dice en **28,51 s**: −5,27 s |

Un elemento anclado a «Son» aparecía **cinco segundos antes** de que la voz llegara a la
frase. Sobre pantalla eso no se lee como un desfase: se lee como un error de guion.

El arreglo es una línea:

```python
re.split(r"(?<=[.,;:?!…»])\s+", texto)
```

**La regla general:** todo signo que produzca ≥0,35 s de silencio —y la tabla de arriba
dice que son todos— tiene que estar en esa clase de caracteres. Si la voz respira ahí, el
alineador tiene que cortar ahí.

### El mecanismo, y cómo se comprueba sin fe

El alineador no usa los signos para *poner* la pausa: los usa para saber **cuántos
grupos** hay. Después toma los `n − 1` silencios más largos que ha medido y los reparte
como fronteras entre esos grupos. Un signo de menos es un grupo de menos, una frontera
de menos, y **todo el emparejamiento se corre una casilla**. Ahí están los 5,27 s.

En `episodio01`, contado:

| | grupos de texto | silencios medidos |
|---|---|---|
| Clase antigua `[.,;:]` | **28** | 31 |
| Clase corregida `[.,;:?!…»]` | **29** | 31 |

Un solo grupo de diferencia —la interrogación del gancho— y 51 palabras se mueven.

```python
import re, sys, io
sys.path.insert(0, "piloto")
import tiempos as T

texto = io.open("piloto/episodio01/guion.txt", encoding="utf-8").read().strip()
CLASE = set(".,;:?!…»")

# 1) ¿queda algún signo de cierre que la voz respete y el alineador no conozca?
fuera = sorted({c for c in texto if not c.isalnum() and not c.isspace()} - CLASE)
print(fuera)              # → ['¿']  (signo de apertura: correcto que no corte)

# 2) grupos frente a silencios
print(len(re.split(r"(?<=[.,;:?!…»])\s+", texto)),
      len(T.detectar_silencios("piloto/episodio01/locucion.mp3")))   # → 29 31
```

Que sobren silencios es sano: el alineador se queda con los más largos. Lo que **no**
se puede tolerar es un signo de cierre fuera de la clase: ése es el fallo silencioso.

## Qué signo se usa para qué, en este canal

| Intención | Signo | Por qué |
|---|---|---|
| Respiración dentro de la frase | `,` | 0,34 s, no rompe la entonación |
| Anunciar lo que viene | `:` | Igual de largo que la coma, pero la entonación sube |
| Cerrar idea | `.` | El único que compra un segundo |
| Pausa dramática | `···` en el guion → `...` pegado | Se convierte en punto: 1,06-1,13 s |
| Pregunta retórica del gancho | `¿…?` | ⚠️ Compra sólo 0,40 s: si quieres que quede en el aire, **añade el punto y aparte después** |
| Silencio de 2 s o más | **ninguno** | Se construye en el audio (§ `288`) |

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Un signo que la voz respeta y el alineador no conoce | 47 de 201 palabras desplazadas; el peor, 5,3 s |
| Creer que `?` y `!` pausan como un punto | Compran 0,4 s: la pregunta no queda en el aire |
| Poner `\n\n` esperando más silencio | No añade nada sobre el punto |
| Repetir puntos (`....`) para alargar | Tampoco añade nada |
| Insertar el silencio a mano después de la fase 4 | Todos los tiempos posteriores se corren (§ `284`) |
| Cambiar la puntuación del guion sin regenerar voz y tiempos | Lo grabado deja de ser lo alineado |
| Puntuar «como se escribe» y no «como se dice» | La voz respira donde no toca y el montaje la sigue |

## Relacionado

`281` ritmo en ppm · `284` una sola pasada · `288` cuando la voz sobra ·
`123` música anclada a palabra · `240` la tabla de eventos · `250` palabra a imagen ·
`95` escribir para el oído

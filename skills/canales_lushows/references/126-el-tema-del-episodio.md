# 126 · El tema del episodio

**Qué resuelve:** que 12 minutos de documental tengan una identidad sonora y no cinco
piezas sueltas. Un tema es una frase melódica corta que el espectador reconoce sin saber
que la reconoce, y que vuelve **transformada** en los momentos que importan.

---

## Qué es un tema y qué no

| Es un tema | No es un tema |
|---|---|
| 4-6 notas dentro de una quinta | Una progresión de acordes entera |
| Un ritmo que sobrevive al cambio de altura | Un arreglo concreto |
| Reconocible tocado con un dedo | Algo que necesita tres capas para existir |
| Vuelve 4-6 veces en 12 min | Suena todo el rato |

La prueba: si no se puede tararear después de oírlo dos veces, no es un tema, es material
de relleno. El ostinato del bajo **no** es el tema: es el suelo. El tema es lo que la mano
derecha toca encima.

## El tema del episodio 01

En `_expediente()` la mano derecha entra a partir del segundo compás:

```python
mel = [("A4", 0.0), ("F4", 0.85), ("E4", 1.70)] if c % 2 else \
      [("D4", 0.0), ("E4", 1.10)]
```

Son **cinco notas** repartidas en dos compases: `A–F–E` y `D–E`. Todo dentro de una quinta
(`D4`–`A4`), sobre un bajo en re. Y el diseño clave: **termina en `E4`**, la segunda del
modo. Nunca toca la tónica en tiempo fuerte. La frase no cierra, y esa es la razón por la
que se puede repetir sin que suene a final falso.

## Los cuatro requisitos para que aguante 12 minutos

| # | Requisito | En el episodio 01 |
|---|---|---|
| 1 | **Ámbito estrecho** — cabe en una quinta | `D4`–`A4` |
| 2 | **Ritmo asimétrico** — 0,85 s y 1,10 s, no todo a tiempo | los offsets no son múltiplos |
| 3 | **No resuelve** — evita la tónica en el uno | acaba en `E4` |
| 4 | **Sobrevive al registro** — funciona dos octavas arriba o abajo | probado en `_cierre` |

Un tema que cumple los cuatro se puede transformar sin dejar de ser él. Uno que falla el
1 o el 3 solo puede repetirse idéntico, y entonces cansa a la tercera vuelta.

## Cómo se declara aparte para poder transformarlo

El error de arquitectura es escribir el tema **dentro** de cada pieza, como está en
`piano.py` hoy. Si el tema vive en una constante, las variantes son funciones de una línea.

```python
# grado del modo (0 = tónica) y desplazamiento en segundos. NO notas absolutas:
# escribirlo en grados es lo que permite transportarlo sin reescribirlo.
TEMA = [(4, 0.00), (2, 0.85), (1, 1.70), (0, 2.90), (1, 4.00)]
MODO = ["D", "E", "F", "G", "A", "Bb", "C"]          # re menor natural

def tema(t0, octava=4, dur=1.6, vel=0.52, grados=None):
    """Devuelve las notas del tema empezando en t0. `grados` permite alterarlo."""
    g = grados or TEMA
    return [(t0 + off, f"{MODO[gr % 7]}{octava + gr // 7}", dur, vel) for gr, off in g]
```

## Las cuatro vueltas del tema, y cómo se transforma cada una

| Vuelta | Momento | Transformación | Código |
|---|---|---|---|
| 1 | Presentación (bloque 1) | Tal cual, bajo la voz | `tema(3.2)` |
| 2 | El golpe del gancho | **Octava arriba**, más fuerte | `tema(t, octava=5, vel=0.62)` |
| 3 | Lo que no consta | **Alterado**: el 4.º grado sube medio tono | ver abajo |
| 4 | Remate | **Aumentación**: notas del doble de largo | `dur=3.0` y offsets ×1,6 |

La vuelta 3 es la que hace el trabajo narrativo. Basta alterar un grado:

```python
# el grado 3 (Sol) pasa a Sol# — la cuarta aumentada contra el bajo en Re.
# Es el intervalo que el oído lee como "algo no encaja", y cae exactamente donde
# el episodio deja de estar probado.
MODO_SOSPECHA = ["D", "E", "F", "G#", "A", "Bb", "C"]
```

Es el mismo recurso que ya usa `_sospecha()` con el acorde `Ab3–D3–F3`, pero aplicado al
tema en vez de al colchón: el espectador oye **su propia melodía puesta en duda**.

## El presupuesto del tema en un episodio de 12 minutos

```
  4 a 6 apariciones          por debajo de 4 no se establece; por encima de 6 cansa
  ≥ 90 s entre apariciones   dos seguidas lo gastan
  nunca dos veces igual      cada vuelta cambia al menos un eje (`127`)
  la 1.ª, en los primeros 90 s   si no, la última no reconoce nada
  la última, en el remate    es la única que puede ir por encima de 0,85 de intensidad
```

Regla dura: **la primera y la última vuelta son obligatorias**. Un tema que se presenta y
no vuelve es peor que no tener tema, porque promete una estructura que el episodio no
cumple.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Tema de más de una quinta de ámbito | No se puede transportar ni tararear |
| Termina en la tónica en tiempo fuerte | Cierra: cada aparición suena a final del vídeo |
| Escrito en notas absolutas dentro de la pieza | Transformarlo obliga a reescribir la pieza entera |
| El tema suena continuamente | Deja de ser un tema y pasa a ser el colchón |
| Dos apariciones a menos de 90 s | Se gasta; la tercera ya no significa nada |
| Presentarlo y no cerrarlo | El episodio promete una estructura y no la cumple |
| Confundir el ostinato del bajo con el tema | El bajo es el suelo: no se transforma, se mantiene |

## Relacionado

`127` variación · `121` una pieza por bloque · `82` componer por código · `119` lenguaje
de época · `93` estructura de episodio

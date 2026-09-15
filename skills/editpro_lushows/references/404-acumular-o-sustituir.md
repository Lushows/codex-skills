# 404 — Capas que se acumulan frente a capas que sustituyen

**Qué resuelve:** dos elementos en el mismo sitio pueden ser dos cosas opuestas. O **se acumulan** —el
sello encima del documento, y hay que leer los dos— o **se sustituyen** —la cifra 20.000 dejando paso a la
50.000, y solo hay que leer la última—. Se escriben igual en el guion visual y se renderizan igual en el
filtergraph, pero se miden distinto, cuestan distinto y se rompen distinto.

---

## 1. Las dos relaciones, en la cadena

El filtergraph solo sabe acumular: cada `overlay` se come la salida del anterior (`400` §1). La
sustitución **no es un mecanismo distinto, es un caso particular**: dos elementos con el mismo rectángulo
y vidas consecutivas.

| | Acumulan | Sustituyen |
|---|---|---|
| Rectángulos | distintos, o solapan poco | **el mismo** |
| Vidas | coinciden en el tiempo | **consecutivas**, con solape solo en el cruce |
| Qué hay que leer | los dos | solo el último |
| Cómo se audita | pisada (`380`) | **no es una pisada** |
| Ejemplo real | `casilla_nombre` + `sin_padre` | `cont_02 → cont_05 → cont_08 → cont_10` |

---

## 2. Por qué no se puede hacer un abanico

La tentación es componer cada capa contra el fondo limpio y «juntarlas después». No se puede: **una
etiqueta de filtergraph se consume una sola vez.**

```
[bg][a]overlay=250:75[v1];[bg][b]overlay=250:75[v2];[v2]format=rgb24[out]
→ Error binding filtergraph inputs/outputs: Invalid argument
```

Con `split` el grafo sí se construye, pero delata el problema de fondo:

```
[0:v]format=rgba,split=2[bg1][bg2];
[bg1][a]overlay=250:75[v1];[v1]nullsink;          # ← esta rama se tira a la basura
[bg2][b]overlay=250:75[v2];[v2]format=rgb24[out]
píxel medido = (60, 189, 118)                      # solo se ve B
```

Y si no se manda a `nullsink`, ffmpeg aborta con el mismo mensaje por dejar una rama sin consumir. La
lección no es sintáctica: **componer contra el fondo limpio no es sustituir, es descartar.** Para que el
espectador vea que una cifra da paso a otra, las dos tienen que estar en la misma cadena, con sus
fundidos cruzándose.

---

## 3. La sustitución envenena la auditoría de pisadas

Es el falso positivo clásico. Medido sobre el episodio del piloto, comparando todas las parejas de cada
escena:

```
escena   el de abajo       lo tapa          % tapado
tunel    cont_02           cont_05            100,0
tunel    cont_02           cont_08            100,0
tunel    cont_02           cont_10            100,0
tunel    cont_05           cont_08            100,0
tunel    cont_05           cont_10            100,0
tunel    cont_08           cont_10            100,0
gancho   desaparecido      planeta_cara       100,0
penal    helicoptero       planta              91,5
penal    esposas           planta              58,8
parejas que se solapan: 23 · por encima del 42%: 9
```

**Seis de las nueve alarmas son un contador sustituyéndose a sí mismo.** El mismo rectángulo cuatro veces
es exactamente lo que se quiere: una cifra que cambia en su sitio. El arreglo no es subir el umbral, es
comparar **solo parejas vivas a la vez**:

```python
if min(b, b2) - max(a, a2) <= 0:
    continue          # no coinciden en el tiempo: no es una pisada
```

Con esa línea, `ep01-lustig` pasa de un montón de ruido a **31 parejas reales y ninguna por encima del
28%**. `canales_lushows/12` da la regla; aquí está lo que cuesta no aplicarla.

---

## 4. Sustituir no sale gratis

La intuición dice que si cada cifra solo vive una fracción de la escena, el conjunto cuesta como una. Es
falso. Medido con 8 capas de 600 px, 75 fotogramas, 1920×1080:

| montaje | CPU |
|---|---|
| 8 capas visibles todo el rato | 49,89 s |
| 8 capas, cada una visible 1/8 del tiempo (sustitución pura) | **49,53 s** |

Lo mismo. El `enable` apaga la mezcla, no la cadena: `scale`, `format`, `rotate` y `fade` se ejecutan en
cada fotograma para las ocho. **Un contador de diez posiciones cuesta diez capas**, viva cada una dos
décimas. Si el coste aprieta, la salida no es acortar vidas: es pre-renderizar la secuencia entera como
un único elemento animado (`408`).

---

## 5. Cómo se escribe cada una

**Acumulación** — vidas que coinciden, rectángulos que no:

```python
{"r": "documento", "ancla": "expediente", "dura": 2.4, "x": "W*0.18", "y": "H*0.30", "w": 620},
{"r": "sello_falso", "ancla": "expediente", "offset": 0.5, "dura": 1.6,
 "x": "W*0.34", "y": "H*0.52", "w": 260},     # declarado DESPUÉS: va encima
```

**Sustitución** — mismo rectángulo, vidas encadenadas y solape solo en el cruce de fundidos:

```python
for i, (cifra, palabra) in enumerate(PASOS):
    ELEMENTOS.append({"r": cifra, "ancla": palabra, "dura": 1.2, "fade_out": 0.25,
                      "x": "W*0.62", "y": "H*0.38", "w": 420})
```

El `fade_out` corto es lo que convierte el relevo en sustitución legible: sin él, la cifra nueva aparece
de golpe encima de la vieja y se lee como error de render (`canales_lushows/13`).

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Componer cada capa contra el fondo limpio y unirlas después | La etiqueta se consume dos veces: render abortado |
| Sacar la rama sobrante con `nullsink` y dar el grafo por bueno | Solo se ve la última capa; el resto del trabajo se tira |
| Auditar pisadas sin comprobar coincidencia en el tiempo | El contador sale como seis pisadas del 100% |
| Subir el umbral de pisada para callar esas alarmas | Se callan también las pisadas de verdad |
| Sustituir sin `fade_out` | El relevo se lee como fallo, no como cambio |
| Contar con que la capa apagada no cuesta | Diez cifras cuestan diez capas: 49,53 s frente a 49,89 s |
| Sustituir con rectángulos que no coinciden | Ni acumula ni sustituye: salta de sitio |

## Relacionado

`400` el orden de render es narrativo · `401` quién gana cuando dos coinciden · `402` el z dinámico ·
`408` lo que cuesta cada capa · `409` depurar un apilado · `104` filter_complex · `105` superponer capas ·
`380` qué es pisar en números · `384` medir el solape antes de renderizar ·
`canales_lushows/12` capas simultáneas · `canales_lushows/13` ciclo de vida del elemento ·
`canales_lushows/36` contadores y cifras animadas

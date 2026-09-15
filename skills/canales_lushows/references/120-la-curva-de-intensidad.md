# 120 · La curva de intensidad

**Qué resuelve:** que la música deje de sonar igual todo el rato. Un colchón plano es el
sonido de un vídeo hecho por defecto: no molesta y tampoco empuja. La intensidad se
declara bloque a bloque y sigue al relato — sube donde el guion aprieta, baja donde la voz
lleva información densa.

---

## La intensidad no es capricho: es la misma curva del guion

| El guion está… | La música | Por qué |
|---|---|---|
| Leyendo un documento, dando cifras | **baja** | El espectador decodifica: competir le hace perder la frase |
| Enunciando el golpe del gancho | **arriba** | El oído necesita que algo confirme que esto importa |
| Contando la leyenda | media-alta | Sostiene la atención sin tapar |
| Rematando el método | **máximo** | El único sitio donde la música puede ser protagonista |

## La tabla real del episodio 01

```python
# bloque -> (pieza, intensidad 0-1)
MUSICA = {
    "muerte": ("mus_expediente", 0.55),   # el documento: sobrio
    "oficio": ("mus_expediente", 0.85),   # "aprendiz de vendedor": el golpe
    "nombre": ("mus_expediente", 0.45),   # se retira: aquí manda la voz
    "torre":  ("mus_sospecha",   0.72),   # la leyenda
    "metodo": ("mus_cierre",     0.88),   # el método del episodio
}
```

**Caso real:** el tramo explicativo (`nombre`) va a **0,45** y el enunciado del método
(`metodo`) a **0,88**: **5,83 dB** de recorrido. Eso hace que el final se sienta final.

## De intensidad a dB (la tabla que hay que tener delante)

La intensidad multiplica una ganancia base: `0,34`. Medido sobre los stems reales del
episodio 01 (voz procesada **−23,3 LUFS**, música sola **−42,8 LUFS**, colchón entero
**−38,9 LUFS**):

| Intensidad | `volume=` | dB rel. a la base | Bloque | Colchón bajo la voz (medido) |
|---|---|---|---|---|
| 0,45 | 0,153 | **−6,9 dB** | `nombre` | **16,8 LU** |
| 0,55 | 0,187 | −5,2 dB | `muerte` | 16,4 LU |
| 0,72 | 0,245 | −2,9 dB | `torre` | 15,4 LU |
| 0,85 | 0,289 | −1,4 dB | `oficio` | 15,2 LU |
| 0,88 | 0,299 | −1,1 dB | `metodo` | **14,7 LU** |
| 1,00 | 0,340 | 0 dB | — | *techo, no se pasa de aquí* |

**El hallazgo:** la música recorre **5,8 dB** entre el bloque más flojo y el más fuerte,
pero el colchón entero solo se mueve **2,1 LU** (16,8 → 14,7). El room tone (`amb_sala`,
−48,6 LUFS subido +7,6 dB) es la capa más alta del colchón y **sostiene el suelo mientras
la música cambia de color**: lo que mueve la curva es el carácter, no el nivel base.

🔴 Por eso la regla de **12-15 LU bajo la voz** (`80`) es del **colchón entero**, nunca de
la música sola: la música sola está a 19,5 LU y es correcto. Quien la mida aislada
concluirá que "no se oye" y la subirá hasta taparlo todo.

**Corrección medida y verificada:** el colchón daba 15,6 LU de media, por debajo del
objetivo. Subiendo el bloque entero **+1,6 dB** (base `0.34 → 0.409`, room tone
`2.40 → 2.885`), sin tocar la forma de la curva, pasa a **14,0 LU** y todos los bloques
caen dentro de la banda: 13,1 (`metodo`) a 15,2 (`nombre`).

Comprobación de que la curva hace lo que dice: con `expediente` en bucle, el tramo a 0,55
mide **−42,50 dB** RMS y el tramo a 0,85 **−38,70 dB** — **+3,80 dB medidos frente a
+3,78 predichos**. La expresión no miente.

## Implementación A — una pista por bloque (la del canal)

La que usa `acabar.py`: cada bloque es una entrada independiente en `PISTAS`, con su
ganancia `0.34 * fuerza` ya calculada y su ventana propia. Auditable, y permite además
cambiar de pieza en la frontera (`121`, donde está `pistas_musica()` completa).

```python
fuera.append((pieza, ini, dur, round(0.34 * fuerza, 3), True))   # archivo, ini, dur, gan, bucle
```

## Implementación B — una sola pista con la curva como expresión de `t`

Cuando **toda** la música del episodio es la misma pieza, sale más barato (un decodificador
en vez de cinco) automatizar el nivel en un único `volume` con `eval=frame`.

El ladrillo es el **trapecio**, nunca `between()`:

```
TRAP(a,b,r) = max(0, min(1, min( (t-(a-r/2))/r , ((b+r/2)-t)/r )))
```

Cada bloque se extiende `r/2` por cada lado, de modo que en la frontera los dos trapecios
valen 0,5 y la suma es un **fundido lineal** entre las dos intensidades. Si no se extienden,
en el límite los dos valen 0 y se abre un hueco de nivel audible.

```python
def curva_musica(bloques, r=1.2, base=0.34):
    """bloques = [(id, ini, fin), ...]  ->  expresión para volume=..:eval=frame"""
    t = []
    for bid, a, b in bloques:
        g = base * MUSICA[bid][1]
        t.append(f"{g:.3f}*max(0\\,min(1\\,min((t-({a:.2f}-{r/2}))/{r}\\,"
                 f"(({b:.2f}+{r/2})-t)/{r})))")
    return "+".join(t)
```

Y en la cadena — las comas del `min`/`max` van **escapadas**, o ffmpeg parte el filtro:

```bash
ffmpeg -hide_banner -stream_loop -1 -i sonido/mus_expediente.wav \
  -filter_complex "[0:a]atrim=0:63.45,asetpts=PTS-STARTPTS,\
volume='0.187*max(0\,min(1\,min((t-(0.00-0.6))/1.2\,((16.15+0.6)-t)/1.2)))\
+0.289*max(0\,min(1\,min((t-(16.15-0.6))/1.2\,((22.88+0.6)-t)/1.2)))':eval=frame[o]" \
  -map "[o]" -y musica_curva.wav
```

`eval=frame` no es opcional: sin él la expresión se evalúa **una sola vez** al arrancar y
todo el episodio suena al nivel del segundo 0.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Colchón plano todo el episodio | Nada destaca; el remate no se siente como remate |
| `volume=` con `between(t,a,b)` | Escalón instantáneo: un **clic** medible (`124`) |
| Trapecios sin solape en la frontera | Los dos valen 0 en el límite: bache de nivel |
| Olvidar `eval=frame` | La curva no existe: todo suena al nivel inicial |
| Comas sin escapar dentro de `min()` | ffmpeg lee argumentos de más y rechaza el grafo |

## Relacionado

`121` una pieza por bloque · `122` el cruce · `124` el silencio · `129` medir si estorba ·
`80` arquitectura · `87` voz

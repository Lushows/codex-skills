# 285 · El relieve se construye

**Qué resuelve:** una voz sintética sale plana y **no se puede arreglar comprimiendo
menos**. El error de diagnóstico está ahí: parece falta de dinámica por culpa del
compresor, y no lo es — la señal ya viene sin relieve. El relieve no se recupera:
**se construye**, subiendo la voz donde el guion aprieta y bajándola donde explica.

---

## El diagnóstico, con números

`LRA` (Loudness Range) es cuánto recorrido dinámico hay entre lo flojo y lo fuerte de un
programa. Medido con `loudnorm` sobre el material real del piloto:

| Señal | LUFS | LRA | Qué dice |
|---|---|---|---|
| `edge-tts` crudo (`ep01-lustig`) | −19,4 | **3,2** | Ya nace plana |
| `edge-tts` crudo (`episodio01`) | −19,5 | **2,6** | Y depende del texto, no del proceso |
| Stem de voz tras la cadena de mezcla | −23,3 | **2,7** | El compresor **no** es el culpable |
| **Stem con la curva de relieve** | −22,7 | **5,1** | +2,4 LU, construidos |
| Máster del minuto entero | **−14,5** | **3,8** | Con música y efectos dentro |

Una locución humana de documental se mueve entre 6 y 10 de LRA. Partimos de 2,7 y
llegamos a 5,1 en el stem. **No se llega quitando compresión** —el experimento de arriba
mide exactamente la misma cadena, con y sin curva— sino automatizando el nivel.

## El diccionario de relieve

En `acabar.py`, un valor en dB por bloque del guion. Cinco números para todo el minuto:

```python
RELIEVE = {
    "muerte": +1.4,      # el gancho: el documento y la fecha
    "oficio": +1.8,      # "aprendiz de vendedor" es el golpe del tramo
    "nombre": -0.6,
    "torre":  -1.0,      # la leyenda se cuenta más bajo: suena a confidencia
    "metodo": +1.2,      # se enuncia el método, sube otra vez
}
```

Es una decisión narrativa escrita en decibelios, y se lee como un mapa del episodio:

| Bloque | dB | Qué hace el guion ahí |
|---|---|---|
| `muerte` | **+1,4** | Gancho: la fecha y el documento. Entra alto |
| `oficio` | **+1,8** | «aprendiz de vendedor». El golpe del minuto |
| `nombre` | −0,6 | Se explica quién no era. Información densa: baja |
| `torre` | **−1,0** | La leyenda. Más bajo = confidencia, no desgana |
| `metodo` | +1,2 | Se enuncia el método del episodio. Vuelve a subir |

**El rango total es de 2,8 dB.** Parece poco y es muchísimo: por encima de ±3 dB entre
bloques deja de sonar a intención y empieza a sonar a fallo de nivel.

La regla de reparto: **la voz sube donde el guion aprieta y baja donde el guion
informa.** Bajar no es esconder — una frase 1 dB por debajo con el colchón intacto se
percibe como que alguien se acerca a contarte algo.

## La curva, como expresión de `t`

No hay automatización por fotogramas ni envolventes dibujadas: se construye una expresión
de `t` para un solo `volume`, con `eval=frame`.

```python
def curva_voz():
    """Nivel como expresión de 't', con rampas de 0,5 s entre bloques."""
    tramos = []
    for e in ESCENAS:
        db = RELIEVE.get(e["id"], 0.0)
        if abs(db) < 0.05:
            continue
        g = 10 ** (db / 20.0)
        a, b, r = e["ini"], e["fin"], 0.5
        tramos.append(f"({g:.4f}-1)*max(0\,min(1\,min((t-{a:.2f})/{r}\,"
                      f"({b:.2f}-t)/{r})))")
    return "1+" + "+".join(tramos) if tramos else "1"
```

Lo que sale para el minuto del piloto (recortado):

```
1+(1.1749-1)*max(0,min(1,min((t-0.00)/0.5,(16.15-t)/0.5)))
 +(1.2303-1)*max(0,min(1,min((t-16.15)/0.5,(22.88-t)/0.5)))
 +(0.9333-1)*max(0,min(1,min((t-22.88)/0.5,(34.41-t)/0.5)))…
```

Tres detalles que no son adorno:

- **Suma de trapecios sobre una base de 1.** Cada bloque aporta `(ganancia − 1)` y fuera
  de su ventana aporta 0. Así no hay que encadenar condicionales ni preocuparse del orden.
- **Las comas van escapadas (`\,`)** porque dentro de un `filter_complex` la coma separa
  filtros. Sin el escape, ffmpeg parte la expresión y falla con un error que no menciona
  la expresión.
- **`eval=frame`** o el `volume` se evalúa una sola vez al arrancar y la curva no existe.

## Las rampas de 0,5 s

La subida y la bajada tardan medio segundo. Lo que se comprobó, y conviene decirlo con
precisión porque la explicación fácil es falsa:

| Frontera | Salto máx. entre muestras (rampa 0,5 s) | Con escalón de 1 ms | RMS local |
|---|---|---|---|
| 16,15 s | 213 | 249 | 1.842 |
| 22,88 s | 457 | 556 | 1.981 |
| 34,41 s | 105 | 98 | 1.083 |
| 50,29 s | 255 | 227 | 2.177 |

**El escalón no produce un clic medible.** Un cambio de 2,4 dB es un 32% de amplitud, y
sobre una onda de voz eso no es una discontinuidad: los saltos son del mismo orden con
rampa y sin ella. El motivo de la rampa es **perceptivo**: un cambio instantáneo de nivel
en mitad de una frase se oye como un empalme de dos tomas distintas. Medio segundo lo
vuelve invisible, y cuesta cero.

Donde la rampa sí es obligatoria es en las fronteras que **caen dentro de una frase**. En
este episodio las fronteras coinciden con pausas y por eso el escalón no delata; en el
momento en que un bloque empiece a mitad de oración, el escalón se oye.

## El orden importa: la curva va DESPUÉS del compresor

Medido sobre la misma voz y la misma curva, cambiando sólo el orden de la cadena:

| Orden | LRA del stem |
|---|---|
| `highpass → compresor → volume → **curva**` | **5,1** |
| `highpass → **curva** → compresor → volume` | 4,0 |

Poner la curva antes del compresor le regala al compresor **1,1 LU del relieve que
acabas de construir**: lo sube donde tú lo habías subido. Es exactamente el trabajo que
un compresor hace bien y que aquí no queremos. (La cadena completa, en § `286`.)

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Bajar la compresión para «recuperar dinámica» | No hay dinámica que recuperar: la voz nace en LRA 2,7 |
| Poner la curva de relieve antes del compresor | El compresor se come 1,1 LU del relieve |
| Saltos de más de ±3 dB entre bloques | Deja de sonar a intención y suena a fallo de nivel |
| Escalones sin rampa en fronteras dentro de una frase | Se oye como un empalme de dos tomas |
| Olvidar `eval=frame` | La expresión se evalúa una vez: no hay curva, hay una ganancia fija |
| No escapar las comas dentro de la expresión | ffmpeg falla con un error que no habla de la expresión |
| Subir el bloque explicativo «para que se entienda» | La inteligibilidad es EQ (§ `286`), no volumen |
| Retocar el relieve a oído sin medir el LRA | Se cree haber hecho algo y el número no se mueve |

## Relacionado

`286` la cadena de proceso · `280` escribir para una voz sintética · `120` la curva de
intensidad · `84` picos dramáticos · `86` medir el audio · `85` ducking ·
`editpro:73` compresión y loudness

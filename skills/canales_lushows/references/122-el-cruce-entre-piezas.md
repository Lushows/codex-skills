# 122 · El cruce entre piezas

**Qué resuelve:** que el cambio de pieza (`121`) no se oiga. Un cambio a corte seco suena
a fallo de edición, y una pieza que arranca en 0,25 s se oye como un pegote. El cruce es
lo único que separa "la música cambió" de "aquí pasó algo con el archivo".

---

## Los tres números

```python
CRUCE = 1.2          # segundos de solape entre bloques
r_in  = 1.2          # rampa de entrada de una pieza musical
r_out = 1.4          # rampa de salida  (siempre más larga que la de entrada)
```

| Material | Rampa entrada | Rampa salida | Por qué |
|---|---|---|---|
| **Música** | **1,2 s** | **1,4 s** | Tiene cola de sala. Necesita tiempo para dejar de existir |
| Ambiente / room tone | 1,2 s | 1,4 s | Igual: es material continuo |
| Objeto, pico, transición | **0,25 s** | **0,4 s** | Es un evento. Una rampa larga lo convierte en fundido |

La salida siempre es más larga que la entrada. La cola de reverberación de `piano.py`
(`aecho=0.90:0.62:420|830`) dura cerca de un segundo: cortarla en 1,2 s deja un borde
audible; en 1,4 s se apaga sola.

## Cómo se solapa: medio cruce por cada lado

El bloque no arranca en su frontera, arranca **medio cruce antes**, y dura **medio cruce
más**. Así la pieza saliente y la entrante conviven 1,2 s a caballo del límite.

```python
ini = max(0.0, e["ini"] - CRUCE / 2)      # entra 0,6 s antes de su bloque
dur = (e["fin"] - ini) + CRUCE / 2        # y se va 0,6 s después
```

```
bloque A  ──────────────────────╲__________
bloque B                ________╱──────────────────
                        |<- 1,2 s ->|
                   ini_B          fin_A
```

## `curve=qsin` no es una preferencia estética: está medido

Dos piezas distintas son señales **no correlacionadas**. Cuando se suman, la potencia se
suma, no la amplitud. Un fundido lineal (`curve=tri`) deja las dos a 0,5 en el centro:
`0,5² + 0,5² = 0,5` de potencia, es decir **−3 dB**. Un bache de 3 dB justo en la frontera
es exactamente lo que el oído lee como "el vídeo se rompió un momento".

Medición real con dos fuentes de idéntico nivel y un cruce de 1,2 s:

| Curva | Nivel estable | Centro del cruce | Hundimiento |
|---|---|---|---|
| `tri` (lineal) | −24,73 dB | **−28,10 dB** | **−3,37 dB** 🔴 |
| **`qsin`** | −24,73 dB | −25,09 dB | **−0,36 dB** ✅ |

`qsin` usa un cuarto de seno: `g(x) = sin(x·π/2)`, que en el centro vale `0,707` para cada
lado y suma potencia unidad. Es la curva de equipotencia, y es la que va en todo cruce
entre materiales distintos.

**Excepción:** si los dos bloques comparten la misma pieza y solo cambia la intensidad
(`120`), las dos señales SÍ están correlacionadas — son la misma onda — y entonces la suma
es de amplitud. Ahí el trapecio lineal es lo correcto y `qsin` sobrepasaría 1,0.

| Caso | Curva |
|---|---|
| Pieza A → pieza B | **`qsin`** |
| Misma pieza, cambio de intensidad | **trapecio lineal** (`120`) |

## La cadena completa de una pista

```python
es_mus = arch.startswith("mus_")
r_in  = 1.2 if es_mus else 0.25
r_out = 1.4 if es_mus else 0.4
f = (f"[{n}:a]aformat=channel_layouts=stereo,volume={gan},"
     f"atrim=0:{dur:.2f},asetpts=PTS-STARTPTS,"
     f"afade=t=in:st=0:d={r_in}:curve=qsin,"
     f"afade=t=out:st={max(0.1, dur - r_out):.2f}:d={r_out}:curve=qsin,"
     f"adelay={int(ini*1000)}|{int(ini*1000)}[s{n}]")
```

El **orden importa** y no es negociable:

1. `volume` antes de `atrim` — así la ganancia se aplica al material, no a un recorte ya hecho
2. `atrim` + `asetpts=PTS-STARTPTS` — sin el `asetpts`, el `adelay` posterior se suma a un
   PTS que ya no empieza en cero y la pieza aterriza en el segundo equivocado
3. `afade` **antes** de `adelay` — las rampas se calculan sobre el tiempo local de la pieza
   (`st=0` es su propio inicio). Después del `adelay` habría que sumar el offset a mano
4. `adelay` al final, en **milisegundos** y con un valor **por canal** (`ms|ms`); con un
   solo valor, el canal derecho queda sin retrasar y la pieza se abre en estéreo falso

## `-stream_loop -1` y el cruce

Las piezas duran 22-27 s y los bloques más. Con `-stream_loop -1` el `atrim=0:dur` corta
donde haga falta, pero el punto de corte cae en cualquier parte del compás. **Eso no
importa**: el `afade` de salida lo tapa. Lo que no se puede es prescindir del `afade`
confiando en que el bucle "cierra bien" — no cierra.

Comprobación rápida de que un cruce está bien hecho, sin oírlo:

```bash
ffmpeg -hide_banner -i mezcla.wav -af "atrim=<frontera-0.05>:<frontera+0.05>,\
astats=metadata=1:reset=0" -f null - 2>&1 | grep "RMS level dB"
```

Compárese con el RMS de un tramo estable del mismo bloque: más de **1,5 dB** de diferencia
es un cruce mal hecho.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Cambio de pieza a corte seco | Se oye como un fallo de codificación, no como una transición |
| `curve=tri` entre piezas distintas | Bache medido de 3,37 dB en la frontera |
| `qsin` en un cambio de intensidad de la misma pieza | La suma pasa de 1,0: sobresalto de nivel |
| Rampa de música de 0,25 s | La pieza "aparece": se oye como un pegote |
| `afade` después de `adelay` | Las rampas caen en el segundo equivocado |
| `adelay=1200` (un solo valor) | Solo se retrasa el canal izquierdo: estéreo roto |
| Olvidar `asetpts=PTS-STARTPTS` | El `adelay` se suma al PTS heredado; la pieza llega tarde |
| Cruces de 3-4 s "para que quede suave" | Dos piezas peleando durante 4 s: se oyen las dos armonías a la vez |

## Relacionado

`121` una pieza por bloque · `120` intensidad · `124` el silencio · `79` xfade · `80`
arquitectura

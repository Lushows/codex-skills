# 79 · `xfade` a fondo

**Qué resuelve:** usar el filtro de transiciones de ffmpeg sin descuadrar el episodio.
Cuáles de sus ~58 transiciones sirven en este canal, cuáles no se tocan nunca, y las
cuatro trampas que hacen que el vídeo salga más corto que la voz.

---

## Sintaxis

```
xfade=transition=fade:duration=0.50:offset=11.60
```

| Opción | Qué es |
|---|---|
| `transition` | Nombre de la transición (lista abajo) |
| `duration` | Cuánto dura el cruce, en segundos |
| `offset` | **Segundo, contado desde el inicio del PRIMER vídeo, en que empieza el cruce** |

Las tres consecuencias que hay que tener siempre en la cabeza:

```
duración_salida = d1 + d2 − duration
el fotograma 0 del segundo vídeo aparece en la salida en el segundo `offset`
requisito duro: offset + duration <= d1   (si no, ffmpeg congela o falla)
```

## Trampa nº 1 — el vídeo se acorta y la voz se descuadra

Cada `xfade` se come `duration` segundos del total: con cuatro cruces de 0,5 s el vídeo
termina **2 s antes** que la locución y todo lo posterior al primero queda desplazado. En
un montaje anclado palabra por palabra (`audio/tiempos.json`) eso lo rompe todo.

**La solución: renderizar con solape.** Cada escena menos la última lleva `duration`
segundos de **cola extra** (el `zoompan` sigue su curso) y el `offset` de cada cruce es la
**suma de las duraciones nominales** de las escenas anteriores:

```
escena_i renderizada con  dur_i + D     (la última, sin cola)
offset_k = dur_0 + dur_1 + ... + dur_{k-1}
```

Con eso, la salida vuelve a durar exactamente `Σ dur_i` y cada escena empieza en su
segundo de siempre. Cadena para N escenas:

```python
def cadena_xfade(escenas, D=0.50, trans="fade"):
    """escenas: [(ruta, dur_nominal), ...]  — todas menos la última con D de cola extra."""
    f = [f"[{i}:v]fps=25,format=yuv420p,setsar=1[v{i}]" for i in range(len(escenas))]
    prev, off = "v0", escenas[0][1]
    for i in range(1, len(escenas)):
        f.append(f"[{prev}][v{i}]xfade=transition={trans}:"
                 f"duration={D}:offset={off:.3f}[x{i}]")
        prev, off = f"x{i}", off + escenas[i][1]
    return ";".join(f), prev, off      # off = duración total esperada
```

Se comprueba **siempre** al terminar:

```bash
ffprobe -v error -show_entries format=duration -of csv=p=0 salida/_mudo.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 audio/locucion.mp3
```

Más de **0,08 s** de diferencia = hay un `offset` mal puesto.

## Trampa nº 2 — las entradas tienen que ser gemelas

`xfade` exige que los dos vídeos coincidan en **tamaño, fps, formato de píxel y SAR**.
El mensaje típico es `First input link parameters (size 1920x1080) do not match the
corresponding second input link parameters (size 1920x1082)`. Se previene poniendo el mismo prefacio a las dos entradas:

```
[0:v]fps=25,format=yuv420p,setsar=1[a];
[1:v]fps=25,format=yuv420p,setsar=1[b];
[a][b]xfade=transition=fade:duration=0.50:offset=11.60[v]
```

El `-2` de `scale=4320:-2` (`motor.py`) puede dar una altura distinta si el fondo no tiene
la proporción exacta: por eso `fps` y `setsar` van siempre, aunque "deberían" sobrar.

## Trampa nº 3 — se acabó el `concat -c copy`

Cualquier `xfade` obliga a recodificar. Se recodifica **sólo el par implicado**
(`e03+e04` → un archivo que sustituye a los dos en `_escenas.txt`), nunca el episodio
entero: 90 s reencodeados por medio segundo de cruce cuestan minutos y una generación
de calidad.

## Trampa nº 4 — el audio va aparte

`xfade` es sólo vídeo. Aquí no importa (las escenas salen mudas y el sonido se monta en
`acabar.py`), pero si se cruzan dos pistas de audio:

```
[0:a][1:a]acrossfade=d=0.90:c1=tri:c2=tri[a]
```

`acrossfade` **también acorta**: `d1+d2−d`. Para los ambientes del episodio se usa
`afade`+`adelay`, que no toca la duración (`75`).

## Cuáles sirven

| Transición | Uso | Duración | Por qué |
|---|---|---|---|
| `fade` | **Sí** — salto de tiempo | 0,40-0,50 s | El único fundido cruzado admitido; neutro y legible |
| `fadeblack` | **Sí** — fin de episodio o de capítulo | 0,60-0,80 s | Es el punto y aparte del canal |
| `fadewhite` | **Sí** — sólo con `ob_obturador` | 0,20 s | Fuera de un flash motivado se ve barato (`74`) |
| `wipeleft` / `wiperight` | **Sí** — imitando el barrido de papel | 0,32-0,40 s | Funciona porque el idioma del canal es el papel que barre |
| `slideleft` / `slideright` | **A veces** — empuje entre dos documentos | 0,30 s | Sólo si los dos fondos son papel; si no, parece una app |
| `smoothleft` / `smoothright` | **A veces** | 0,36 s | Wipe de borde difuso, cuando el del `wipe` se ve duro |
| `dissolve` | **A veces** — 4 a 6 fotogramas, nunca más | 0,16-0,24 s | Su granulado empasta con el grano del canal; largo parece error |
| `circleopen` / `circleclose` | **A veces** — sólo motivado (una mira) | 0,50 s | Sin motivo en pantalla es cortinilla de presentación |

## Cuáles no se usan nunca

`pixelize` · `radial` · `distance` · `hblur` · `fadegrays` · `squeezeh` · `squeezev` ·
`zoomin` · `hlwind` · `vuwind` · `vdwind` · `hlslice` · `vuslice` · `rectcrop` ·
`circlecrop` · `vertopen` · `vertclose` · `horzopen` · `horzclose` · `coverup` ·
`revealup` · `wipetl` · `wipebr` · `fadefast` · `fadeslow`

Todas tienen el mismo defecto: **son efectos de software**. Se reconocen al instante como
"transición de programa de edición" y ninguna se puede motivar con algo que esté pasando
en la historia. Queda `transition=custom` con `expr` (variables `X`, `Y`, `W`, `H`, `P`,
`A`, `B`) para escribir el cruce a mano; para el tachado rojo se prefiere `geq`, que da
más control (`77`).

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| No compensar la duración con cola extra | El vídeo se acorta y todo lo posterior queda desfasado con la voz |
| `offset` calculado sobre el segundo vídeo | El cruce cae en el sitio equivocado o ffmpeg falla |
| `offset + duration > d1` | El primer vídeo se agota: fotograma congelado o error |
| Recodificar el episodio entero por una transición | Minutos de render y una generación de calidad perdida |
| Olvidar `fps` / `setsar` en una de las dos entradas | Error de "input link parameters do not match" |

## Relacionado

`70` · `71` · `74` · `75` · `77` · `78` · `01`

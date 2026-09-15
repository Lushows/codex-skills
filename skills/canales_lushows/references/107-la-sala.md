# 107 · La sala

**Qué resuelve:** un instrumento sintetizado sin sala suena **pegado a la cara**. No es
un defecto de timbre: es que no tiene sitio. El oído necesita las reflexiones para
situar el sonido en un espacio, y sin ellas lo lee como algo artificial pegado al
micrófono. Con `aecho` se construye ese espacio en una línea.

---

## Qué es cada número de `aecho`

```
aecho = in_gain : out_gain : retardos_ms : caídas
aecho = 0.88    : 0.62     : 90|145|210  : 0.35|0.22|0.14
```

| Parámetro | Qué hace | Rango útil |
|---|---|---|
| `in_gain` | Cuánta señal directa entra al eco | 0,75–0,92 |
| `out_gain` | **Cuánto sale en total.** Es el volumen de la sala | 0,45–0,75 |
| retardos (ms) | Distancia a cada pared | 15 (cuarto) a 1100 (nave) |
| caídas | Cuánto sobrevive cada reflexión | 0,10–0,62 |

**Los retardos son geometría.** El sonido recorre ~34 cm por milisegundo: un eco de
90 ms es una pared a unos 15 m. Tres retardos **no múltiplos entre sí** (90, 145, 210)
suenan a habitación; tres múltiplos (100, 200, 300) suenan a tubo metálico.

## Las cinco salas del canal

```bash
# el golpe seco de referencia, sin sala
GOLPE="anoisesrc=c=white:a=0.9:d=3.0:r=44100:seed=1729,\
bandpass=f=240:width_type=h:w=90,equalizer=f=240:width_type=q:w=8:g=14,\
volume='pow(max(0,1-t/0.075),3.0)':eval=frame,volume=3.0"

ffmpeg -filter_complex "$GOLPE,aecho=0.85:0.55:17|29|41:0.30|0.18|0.11,\
alimiter=limit=0.75:level=disabled[out]" -map "[out]" -ar 44100 -ac 1 -y cuarto.wav
```

| Nombre | `aecho` | Cola medida (−30 dB) | Para qué |
|---|---|---|---|
| **seco** | — | 65 ms | Nunca solo; solo mezclado con otra capa |
| **cuarto** | `0.85:0.55:17\|29\|41:0.30\|0.18\|0.11` | 65 ms | Documento, papel, golpe de mesa |
| **sala** | `0.88:0.62:90\|145\|210:0.35\|0.22\|0.14` | **254 ms** | Por defecto del canal: piano, cuerda |
| **iglesia** | `0.85:0.72:320\|510\|780\|1100:0.45\|0.34\|0.24\|0.16` + `lowpass=f=4200` | **1142 ms** | El remate, la revelación |
| **lejos** | `0.75:0.70:150\|240\|360:0.62\|0.46\|0.32` + `lowpass=f=2400,volume=0.55` | 419 ms | Algo que pasa en otra habitación |

La cola se mide como **el último instante en que la señal sigue por encima de −30 dB del
pico**. Ojo: con `aecho` los ecos son discretos, así que buscar el *primer* cruce del
umbral da una cifra absurdamente corta — 45 ms para la iglesia, que tiene 1142. Hay que
buscar el **último**.

## Los tres trucos de la distancia

Alejar algo no es sólo bajarle el volumen. Son tres cosas a la vez, y sin las tres el
oído lee «flojo», no «lejos»:

| # | Qué | Cómo | Por qué |
|---|---|---|---|
| 1 | Menos agudos | `lowpass=f=2400` | El aire se come lo agudo con la distancia |
| 2 | Más sala que directo | `caídas` altas (0,62) con `in_gain` bajo (0,75) | De lejos llega más reflexión que sonido directo |
| 3 | Menos volumen | `volume=0.55` | Lo evidente, y lo único que suele hacerse |

Sólo el punto 3 = «alguien bajó el fader». Los tres = «eso pasó en otro cuarto».

## 🔴 `aecho` alarga el archivo

```
entrada 3,00 s + sala      -> 3,21 s
entrada 3,00 s + iglesia   -> 4,10 s   (1,10 s más)
```

Si el render lleva `-t 3` o un `atrim` a la duración original, **la cola se corta en
seco** y ese corte se oye peor que no tener sala. Regla: el `atrim` va **antes** del
`aecho`, nunca después; y la duración final se calcula sumando el retardo mayor.

## 🔴 La sala baja el nivel, y no poco

Mismo golpe, mismo `volume` de entrada:

| Sala | Integrado | Pico real |
|---|---|---|
| seco | −28,3 LUFS | −10,2 dBFS |
| cuarto | −33,0 LUFS | −16,3 dBFS |
| sala | −34,9 LUFS | −15,5 dBFS |
| iglesia | −38,3 LUFS | −14,7 dBFS |
| lejos | −39,0 LUFS | −21,5 dBFS |

Más de **10 LU** entre lo seco y la nave. Son dos motivos sumados: el `out_gain` (0,62
son −4 dB) y que la misma energía se reparte en más tiempo. Por eso el nivel **se ajusta
después de la sala, nunca antes** — si no, cada instrumento acaba en un sitio distinto
de la mezcla (`109`).

## Dos salas anidadas

El piano del canal lleva **dos**, y no sobra ninguna:

```
aecho=0.92:0.35:55|110:0.10|0.05      dentro de la nota  -> la CAJA (madera)
aecho=0.90:0.62:420|830:0.22|0.13     sobre la pieza     -> la SALA  (aire)
```

La caja es parte del instrumento y viaja con cada nota. La sala es parte del sitio y se
aplica una sola vez a la mezcla. Ponerlas al revés — la sala dentro de cada nota —
multiplica la reverberación por el número de notas y embarra la pieza entera.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Sin sala | Todo pegado a la cara; se lee como artificial |
| Retardos múltiplos (100\|200\|300) | Suena a tubo metálico, no a habitación |
| `-t` o `atrim` después del `aecho` | La cola se corta en seco: peor que no tener sala |
| Ajustar el volumen antes de la sala | Cada instrumento acaba en un nivel distinto |
| Sala larga en cada nota en vez de en la pieza | La reverberación se multiplica y embarra todo |
| «Lejos» sólo bajando el volumen | Se oye flojo, no lejano |
| Medir la cola por el primer cruce del umbral | La iglesia da 55 ms en vez de 1122 |

## Relacionado

`101` piano · `104` percusión · `106` texturas · `108` por qué suena a pitido · `80` arquitectura de la mezcla

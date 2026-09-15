# 128 · Música para el vertical

**Qué resuelve:** en 60 segundos no cabe una progresión de 24 s. Reutilizar tal cual la
banda del episodio largo produce un vertical que empieza en mitad de una frase musical,
no llega a establecer nada y se corta a la mitad. La música del corto se monta con otras
reglas, no con las mismas reducidas.

---

## Lo que cambia respecto al largo

| | Episodio largo | Vertical 60 s |
|---|---|---|
| Piezas distintas | 3-4 | **1. Siempre 1** |
| Cambios de intensidad | 5-7 | **2, como mucho 3** |
| Rampa de entrada | 1,2 s | **0,25 s** |
| Rampa de salida | 1,4 s | 1,0 s, y **reservada** |
| Colchón bajo la voz | 12-15 LU | **10-12 LU** |
| Ganancia base | 0,34 (o 0,409 corregida) | **0,48** (+3,0 dB) |
| `LRA` objetivo | 4-9 LU | **3-5 LU** |

## 1 · Entrada inmediata

En el largo la música se toma 1,2 s para aparecer porque hay 12 minutos por delante. En un
vertical, 1,2 s son **el 2 % del vídeo** y caen justo en el fotograma que decide si alguien
se queda. La música tiene que estar ya ahí.

```python
ES_VERTICAL = True
r_in  = 0.25 if ES_VERTICAL else 1.2
r_out = 1.00 if ES_VERTICAL else 1.4
INICIO_VOZ = 0.40            # la locución arranca aquí; la música, en 0,00
PISTAS = [("mus_expediente", 0.0, 60.0, 0.48, True)]
```

Y entra **antes que la voz**: 0,3-0,5 s de música sola. Es lo único que distingue un corto
montado de un clip recortado.


## 2 · Una sola idea

Una pieza, sin cambio de pieza: en 60 s cambiar de material solo desorienta. Lo que sí
cabe es **una** curva de intensidad de tres escalones:

```python
# el vertical tiene dos partes y nada más: el gancho y el desarrollo
MUSICA_V = [("gancho",  0.0, 12.0, 0.85),     # entra fuerte: hay que retener
            ("cuerpo", 12.0, 52.0, 0.55),     # se retira: aquí manda la voz
            ("cierre", 52.0, 60.0, 0.88)]     # sube para el remate
```

Se implementa con el trapecio de `120` en un único `volume` — probado:

```bash
ffmpeg -hide_banner -stream_loop -1 -i sonido/mus_expediente.wav \
  -filter_complex "[0:a]atrim=0:60,asetpts=PTS-STARTPTS,\
volume='0.408*max(0\,min(1\,min(t/0.25\,(12.6-t)/1.2)))\
+0.264*max(0\,min(1\,min((t-11.4)/1.2\,(52.6-t)/1.2)))\
+0.422*max(0\,min(1\,min((t-51.4)/1.2\,(60.0-t)/1.0)))':eval=frame[o]" \
  -map "[o]" -y mus_vertical.wav
```

## 3 · El cierre que no se corta

Es el error más visible del formato. El vertical dura 60,0 s exactos y la música se corta
en 60,0 con la cola a medio sonar: el último fotograma lleva un borde audible que se lee
como "se acabó el archivo", no como "se acabó el vídeo".

**La regla: el último acorde entra a los 56 s y la rampa de salida termina EN el último
fotograma.** Reservar 1,0 s y tratar el final como un evento, no como un corte.

```python
DUR = 60.0
CIERRE = 1.0
# la rampa de salida ARRANCA en DUR-CIERRE y acaba exactamente en DUR
f_out = f"afade=t=out:st={DUR - CIERRE:.2f}:d={CIERRE}:curve=qsin"
```

Y comprobar que el último cuarto de segundo baja de verdad:

```bash
ffmpeg -hide_banner -i vertical.mp4 -af "atrim=59.75:60.0,astats=metadata=1:reset=0" \
  -f null - 2>&1 | grep "RMS level dB"     # debe estar 20 dB bajo el nivel del cuerpo
```

## 4 · El altavoz del móvil: por qué sube la música

Un altavoz de teléfono no reproduce por debajo de unos 400 Hz. El ostinato del canal vive
en `D2` = **73,4 Hz**: en el móvil **no existe**. Calibrar con cascos y publicar significa
que el colchón desaparece entero para la mitad de la audiencia.

Dos consecuencias:

1. La ganancia base sube de 0,34 a **0,48** (+3,0 dB): lo que se pierde en graves se
   compensa arriba, y el ducking (`85`) sigue protegiendo la voz.
2. El ostinato se **dobla una octava arriba** sin quitar el grave (que sí se oye en cascos):

```python
def doblar_bajo(notas):
    """Añade una copia una octava arriba de cada nota por debajo de C3, a -9 dB."""
    extra = [(t, n[:-1] + str(int(n[-1]) + 1), d, v * 0.35)
             for t, n, d, v in notas if int(n[-1]) <= 2]
    return notas + extra
```

🔴 Lo que **no** se hace es un `highpass=f=120` sobre la música "para aprovechar el
margen": se pierde el grave en cascos y no se gana nada en el altavoz.

## 5 · Loudness del corto

Mismo destino que el largo, **menos recorrido**:

```
loudnorm=I=-14:TP=-1.5:LRA=4
```
Un `LRA` de 4 LU frente a los 7-9 del largo: en 60 s no hay tiempo para que el oído se
adapte, y el vertical se ve en la calle. Lo que en el largo es relieve, aquí es "no oigo".


## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Cortar en el segundo 60 sin rampa | Borde audible: se lee como archivo truncado |
| `highpass` sobre la música "para el móvil" | Se pierde el grave en cascos y no se gana en altavoz |

## Relacionado

`120` la curva de intensidad · `122` el cruce · `200` el vertical se renderiza ·
`208` el cierre que devuelve al largo · `129` medir si estorba

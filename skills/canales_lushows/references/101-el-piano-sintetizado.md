# 101 · El piano sintetizado

**Qué resuelve:** el instrumento central del canal. La composición clásica es libre
(Satie murió en 1925), pero **la grabación no lo es**: bajar una interpretación es pedir
una reclamación de Content ID. Sintetizando el piano, la obra es libre y la grabación es
nuestra. Cero riesgo — y encima suena a lo que queremos.

Vive en `piloto/piano.py`. Este módulo explica por qué funciona y qué medir.

---

## La idea en una frase

**Un piano es un golpe con cola, y los armónicos se apagan antes que la fundamental.**
Por eso una nota de piano se «redondea» al morir: empieza brillante y termina redonda.
Todo lo demás es contabilidad.

## Los cinco armónicos y sus caídas

```python
# armónico -> (multiplicador de frecuencia, ganancia, factor de caída)
ARMONICOS = [(1.0, 1.000, 1.0), (2.0, 0.380, 1.7), (3.0, 0.180, 2.4),
             (4.0, 0.085, 3.2), (5.0, 0.040, 4.1)]
```

La tercera columna es la que hace el trabajo. `tau = (dur · 0,55) / caída`: **el 5.º
armónico se apaga 4,1 veces más rápido que la fundamental.**

## Medido: cómo se redondea la nota

Do4 (261,6 Hz), 3 s. Nivel de cada armónico **bajo la fundamental de ese mismo
instante** (FFT sobre ventanas de 140 ms):

| t | H1 | H2 | H3 | H4 | H5 |
|---|---|---|---|---|---|
| 0,02 s | 0,0 dB | −8,7 | −15,5 | −22,3 | −29,2 |
| 0,80 s | 0,0 dB | −11,6 | −21,2 | −31,4 | −42,0 |
| 1,60 s | 0,0 dB | −14,5 | −27,1 | −40,6 | −55,1 |
| 2,40 s | 0,0 dB | −17,5 | −33,0 | −49,9 | **−68,4** |

El 5.º armónico pierde **39 dB** respecto de la fundamental en 2,4 s; el 2.º pierde 8,8.
Eso es el redondeo, y es medible. Con caídas iguales la tabla sería plana y el resultado
suena a órgano de juguete (`108`).

## La nota, completa

```python
def muestra(nota, dur=5.0):
    f0 = hz(nota)
    partes, etiquetas = [], []
    for i, (mult, gan, caida) in enumerate(ARMONICOS):
        f = f0 * mult
        if f > 16000:                      # inaudible y gasta margen
            continue
        tau = (dur * 0.55) / caida         # caída exponencial: cuerda golpeada
        partes.append(
            f"sine=f={f:.3f}:d={dur:.2f}:sample_rate=44100,"
            f"volume='{gan:.4f}*exp(-t/{tau:.3f})':eval=frame[h{i}]")
        etiquetas.append(f"[h{i}]")
    partes.append(
        "".join(etiquetas) + f"amix=inputs={len(etiquetas)}:normalize=0,"
        f"afade=t=in:st=0:d=0.008,"                       # el ataque
        f"afade=t=out:st={dur-0.35:.2f}:d=0.35,"
        f"aecho=0.92:0.35:55|110:0.10|0.05,"              # el cuerpo de la caja
        f"volume=0.55[out]")
    subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-f","lavfi",
        "-i","anullsrc=r=44100:cl=mono:d=0.01",
        "-filter_complex",";".join(partes),"-map","[out]",
        "-ar","44100","-ac","1","-y",ruta], check=True)
```

> **`:eval=frame` no es opcional.** Sin él, ffmpeg 8.x no «congela» la expresión: falla
> en seco con `Invalid value NaN for volume` y `Error configuring filter graph`. Es un
> fallo ruidoso, que es una suerte: en versiones anteriores se quedaba callado.

## 🔴 El ataque de 8 ms no evita un chasquido — define el instrumento

El comentario original de `piano.py` dice «sin esto la nota empieza con un chasquido».
Medido, es falso:

| Señal | 1.ª muestra | Salto máx. entre muestras |
|---|---|---|
| `sine` con o sin `afade` de 8 ms | +0,0000 | 0,0094 |
| `atrim=start=0.5001` sobre un tono en marcha | **−0,4473** | 0,0187 |

**`sine` arranca siempre en fase cero** y por sí solo no chasquea nunca. El chasquido
aparece al **cortar dentro de una señal que ya sonaba**: ahí la primera muestra vale
0,45 de fondo de escala, un escalón 24 veces mayor que el paso natural entre muestras.

Lo que el `afade` de 8 ms sí hace es **el ataque**: lleva el tiempo hasta el 90 % del
pico de 5 ms a 12 ms. Es la diferencia entre un golpe y un pellizco, y se oye.

## La sala, en dos niveles

`aecho=0.92:0.35:55|110:0.10|0.05` dentro de cada nota es la **caja** del instrumento
(madera). `aecho=0.90:0.62:420|830:0.22|0.13` sobre la pieza entera es la **sala** donde
se toca (aire). Son dos cosas distintas y hacen falta las dos (`107`).

## Medida de la pieza real

`mus_expediente.wav`, generado con `python piano.py expediente`:

```
  50 notas · 27,0 s · 2,4 MB
  integrado   -30,1 LUFS      (objetivo del colchón bajo voz: -30 ± 1)
  pico real   -16,1 dBFS
  recorrido     2,0 LU        correcto: un colchón NO debe tener relieve
```

El `loudnorm=I=-30:TP=-6:LRA=6` del final de `tocar()` garantiza ese número pieza a
pieza. Sin él, cada una sale a un volumen distinto según cuántas notas tenga.

## La caché de notas

`muestra()` guarda cada nota en `sonido/_piano/NOTA_DUR.wav`; el `round(dur, 1)` de
`tocar()` hace que 2,17 s y 2,23 s compartan la muestra de 2,2 s. Sin caché, una pieza
de 50 notas lanza 50 grafos de cinco `sine` cada uno.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Quitar `:eval=frame` | El grafo no arranca: `Invalid value NaN for volume` |
| Caídas iguales para todos los armónicos | Órgano de juguete; la nota no se redondea |
| Quitar el `aecho` corto de la nota | La nota suena pegada a la cara, sin caja |
| Nota de menos de 0,40 s | El `afade` de salida arranca en negativo: `muestra()` la rechaza |

## Relacionado

`100` anatomía · `107` la sala · `108` por qué suena a pitido · `109` banco · `82` música por código

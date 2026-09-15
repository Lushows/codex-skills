# 127 · Variación sin repetición

**Qué resuelve:** que una pieza de 27 s cubra 12 minutos sin que el espectador la
identifique como un bucle. No se arregla componiendo más música: se arregla cambiando un
eje cada vez que vuelve.

---

## El problema, en números del canal

Las piezas del episodio 01, medidas:

| Pieza | Compases × duración | Medido |
|---|---|---|
| `expediente` | 8 × 3,2 s | **26,99 s** |
| `sospecha` | 8 × 3,2 s | 26,61 s |
| `cierre` | 6 × 3,6 s | 22,57 s |

Un bloque de 16 s no llega a agotar la pieza. Un episodio de 12 minutos la haría girar
**27 veces**. El umbral empírico: **tres vueltas del bucle** (≈ 80 s) es lo máximo que
pasa desapercibido bajo una voz. A partir de ahí hay que mover algo.

## Los cuatro ejes, y cuánto compra cada uno

| Eje | Qué se cambia | Vueltas que compra | Coste |
|---|---|---|---|
| **Intensidad** | La ganancia (`120`) | +1 | Cero: ya está en el diccionario |
| **Registro** | La octava de la melodía | +2 | Una línea |
| **Densidad** | Cuántas notas suenan por compás | +2 | Una línea |
| **Instrumento** | El perfil de armónicos de `piano.py` | +3 | Una constante |

Combinar dos ejes no suma, **multiplica**: registro + densidad da material para 6-8 vueltas.

## 1 · Registro

Subir una octava aclara y tensa; bajarla oscurece. Funciona porque el tema conserva su
perfil de intervalos (`126`) y el oído lo reconoce como "lo mismo, más arriba".

```python
def octavar(notas, n=+1):
    """Sube (o baja) `n` octavas SOLO la melodía: el bajo se queda donde está."""
    fuera = []
    for t, nota, dur, vel in notas:
        oct_ = int(nota[-1])
        fuera.append((t, nota[:-1] + str(oct_ + n), dur, vel) if oct_ >= 4
                     else (t, nota, dur, vel))
    return fuera
```

🔴 El bajo **no** se octava nunca. El ostinato es el suelo del episodio: moverlo cambia la
pieza entera, no la varía. Por eso el filtro `oct_ >= 4`.

## 2 · Densidad

La variante más rentable y la que menos se nota que es una variante: se quitan notas.

```python
def aclarar(notas, dejar=0.6):
    """Quita notas de melodía manteniendo bajo y acordes. 1.0 = todo, 0.5 = la mitad."""
    mel = [n for n in notas if int(n[1][-1]) >= 4]
    paso = max(1, round(1 / dejar))
    guardar = set(id(n) for i, n in enumerate(mel) if i % paso == 0)
    return [n for n in notas if int(n[1][-1]) < 4 or id(n) in guardar]
```

| `dejar` | Efecto | Dónde |
|---|---|---|
| 1,0 | La pieza completa | Bloque de presentación |
| 0,6 | Se abre, entra aire | Bajo voz densa |
| 0,3 | Casi solo ostinato | Tramo de cifras |
| 0,0 | Solo el suelo | Antes de un golpe (`124`) |

Aclarar y **bajar intensidad no es lo mismo**: bajar el volumen aleja la pieza entera;
quitar notas la deja al mismo volumen y le abre huecos por donde pasa la voz. Bajo una
enumeración densa, aclarar funciona mejor que bajar.

## 3 · Instrumento

`piano.py` define el timbre en una constante. Tocando los tres números de cada armónico
sale otro instrumento con las mismas notas:

```python
# (multiplicador de frecuencia, ganancia, factor de caída)
ARMONICOS = [(1.0, 1.000, 1.0), (2.0, 0.380, 1.7), (3.0, 0.180, 2.4),
             (4.0, 0.085, 3.2), (5.0, 0.040, 4.1)]                    # piano

CAJA     = [(1.0, 1.000, 1.6), (2.0, 0.520, 2.2), (3.0, 0.300, 3.0),
            (4.0, 0.160, 3.8), (5.0, 0.090, 4.6)]      # caja de música: más brillo,
                                                       # caída más rápida, nota corta
CUERDA   = [(1.0, 1.000, 0.6), (2.0, 0.240, 0.9), (3.0, 0.120, 1.2),
            (4.0, 0.060, 1.5), (5.0, 0.030, 1.9)]      # arco: caída lenta, sostiene
```

Más ganancia en los armónicos altos = más brillo. Caída más rápida (número mayor) = nota
más corta. La cuerda frotada sostiene porque **todos** sus factores de caída bajan de 2.

> Y ojo: el instrumento es el eje que más cambia el episodio. Cambiarlo dos veces ya se
> lee como dos bandas sonoras distintas. Una vez por episodio, en el remate.

## 4 · La combinación, en una tabla de vueltas

Así se escribe un episodio de 12 min con **tres** piezas compuestas:

| # | s | Pieza | Registro | Densidad | Intensidad |
|---|---|---|---|---|---|
| 1 | 0–80 | `expediente` | base | 1,0 | 0,55 |
| 2 | 80–170 | `expediente` | base | **0,6** | 0,45 |
| 3 | 170–260 | `expediente` | **+1** | 0,6 | 0,80 |
| 4 | 260–400 | `sospecha` | base | 1,0 | 0,72 |
| 5 | 400–520 | `sospecha` | **−1** | **0,3** | 0,50 |
| 6 | 520–640 | `cierre` | base | 1,0 | 0,88 |
| 7 | 640–720 | `cierre` | +1 | 0,6 + **CAJA** | 0,70 |

Siete tramos, tres archivos compuestos, **ningún tramo suena dos veces igual**. Cada fila
cambia al menos un eje respecto a la anterior: es la única regla que hay que verificar.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Dejar la misma pieza sin variar más de 3 vueltas (≈80 s) | El espectador oye el bucle y ya no lo puede des-oír |
| Octavar también el bajo | Deja de ser una variación: es otra pieza |
| Bajar el volumen en vez de aclarar bajo voz densa | La música se aleja pero sigue tapando los mismos huecos |
| Cambiar de instrumento dos veces por episodio | Suena a dos bandas sonoras pegadas |
| Componer una pieza nueva para cada bloque | 5 piezas, ninguna reconocible, cero identidad (`121`) |

## Relacionado

`126` el tema · `121` una pieza por bloque · `120` intensidad · `82` componer por código ·
`89` biblioteca de sonido

# 118 · Cuándo NO debe haber música

**Qué resuelve:** los tramos en que la música resta. Son pocos y son siempre los mismos,
y son justo los que más importan del episodio. Callar ahí no es ahorrar trabajo: es el
recurso más fuerte que tiene la banda sonora.

---

## 🔴 Silencio de música ≠ silencio de audio

| | Silencio de música | Silencio digital |
|---|---|---|
| Qué se apaga | La pieza de piano | Todo |
| Qué sigue sonando | **Room tone (`amb_sala`), siempre** | Nada |
| Cómo se percibe | Atención, gravedad, "esto es importante" | Se cortó el vídeo |

La capa de sala **nunca se apaga** (`80`, `16`). En `acabar.py` va con bucle a lo largo
de todo el episodio:

```python
("amb_sala", 0.0, T, 2.40, True),    # medido -48,6 LUFS -> +7,6 dB
```

Un tramo sin música y sin sala es un fallo de mezcla, no un recurso.

## Los seis sitios donde la música resta

| # | Tramo | Por qué | Duración |
|---|---|---|---|
| 1 | **La cifra ancla** (`93`, 5:00) | La cifra es el evento. Con acorde debajo, la cifra pasa a ser ilustración del acorde | 3-6 s |
| 2 | **La cita literal** de un documento (`48`, `91`) | Con música se oye a dramatización; sin música, a prueba | La cita entera |
| 3 | **Los 2-4 s antes de un pico** (`84`) | El impacto crece más con silencio delante que con cualquier riser | 2-4 s |
| 4 | **La corrección forense** — *"eso no consta"* | Es el método del canal. Música = te estoy contando. Silencio = te estoy diciendo la verdad | La frase |
| 5 | **Enumeración densa**: fechas, nombres, cifras seguidas | La voz necesita toda la banda para que se entiendan (`117`) | El tramo |
| 6 | **Los últimos 2-3 s** tras la frase final | La pieza muere antes que el vídeo, no a la vez | 2-3 s |

En el piloto, el caso 4 está anclado a la palabra exacta:

```python
("dr_golpe", cuando("consta", 62.98) - 0.10, 1.4, 0.50, False),
```

El guion termina con *"separar lo que se cuenta de lo que consta"*. Ahí no hay que
añadir música: hay que quitarla y dejar el golpe.

## Callar en la composición

```python
def callar(notas, tramos):
    """Quita toda nota que EMPIECE dentro de un tramo (inicio, fin)."""
    return [x for x in notas
            if not any(a <= x[0] < b for a, b in tramos)]

base    = ostinato(compases=6, cima=["A4","F4","E4","D4","E4"])   # 29 notas
cortada = callar(base, [(6.8, 13.6)])                             # 19 notas
tocar(cortada, "118_con_silencio.wav")                            # 21,27 s
```

⚠️ **`callar()` no produce silencio en el segundo que se le pide.** Quita las notas que
*empiezan* dentro del tramo, pero las que empezaron antes siguen sonando:

| Evento | Empieza | Acaba |
|---|---|---|
| Bajo del compás anterior | 3,40 | 6,40 |
| Acorde del compás anterior | 4,50 | 6,70 |
| **Cola del `aecho` de sala** (`piano.py:109`) | — | **≈ 7,67** |

Se pide silencio en **6,80** y el silencio real empieza en **≈ 7,67**: casi un segundo
tarde, justo encima de la frase que se quería dejar limpia. **Hay que adelantar el corte
2,5 - 3,0 s** respecto del punto que se quiere limpio.

## Callar en la mezcla (lo correcto en producción)

El sitio bueno para callar no es la composición: es `pistas_musica()` en `acabar.py`,
donde la pieza ya tiene ganancia y rampas. Ahí se controla la cola.

```python
SILENCIOS = [
    (62.20, 66.40, "el metodo: 'lo que se cuenta y lo que consta'"),
    (94.10, 97.00, "la cifra ancla"),
]

def pistas_musica():
    fuera = []
    for e in ESCENAS:
        pieza, fuerza = MUSICA.get(e["id"], ("mus_expediente", 0.5))
        for a, b, motivo in SILENCIOS:
            if a < e["fin"] and b > e["ini"]:
                fuerza = 0.0                     # la sala sigue: solo calla el piano
        ini = max(0.0, e["ini"] - CRUCE / 2)
        fuera.append((pieza, ini, (e["fin"] - ini) + CRUCE / 2,
                      round(0.34 * fuerza, 3), True))
    return fuera
```

Escribir el **motivo** al lado no es burocracia, es el filtro: igual que en `DESCANSOS`
(`16`), un silencio que no se puede justificar en media línea es pereza con nombre.

## Cuánto silencio cabe

| Reparto | Umbral |
|---|---|
| Silencios de música por episodio de 10 min | **3 a 5** |
| Duración de cada uno | 2 - 6 s (la cita puede ser más larga) |
| Distancia mínima entre dos | 45 s |
| En los primeros 20 s (gancho) | **ninguno.** El gancho no calla |
| Al final | 1, obligatorio: la pieza muere 2-3 s antes que el vídeo |

Más de cinco y el silencio deja de significar: se lee como que la música se olvidó.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Apagar también el room tone | Se oye como corte de reproducción, no como pausa |
| Cortar la música en el segundo exacto de la frase | Llega ~1 s tarde por la cola del `aecho`: hay que adelantar 2,5-3 s |
| Poner música bajo una cita literal | La prueba se oye a dramatización y se pierde la autoridad del canal |
| Riser antes del pico en vez de silencio | El silencio pega más y no gasta un efecto |
| Silencio en el gancho | Se pierde al espectador antes de haberlo ganado |
| Más de 5 silencios en un episodio | Dejan de leerse como decisión y se leen como olvido |
| Bajar la música a 0,05 en vez de a 0 | Ni suena ni calla: es el peor de los dos mundos |

## Relacionado

`111` la armonía que no resuelve · `115` progresiones por tramo · `117` dejarle sitio a
la voz · `16` el plano de descanso · `80` arquitectura de la mezcla · `84` picos dramáticos

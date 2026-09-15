# 109 · Banco de instrumentos

**Qué resuelve:** el catálogo cerrado del canal — qué instrumento va en qué tramo, con
su código y su medida. Todo sintetizado: **una pista sintetizada no puede recibir un
reclamo de Content ID**, que es la causa número uno de muerte de estos canales.

---

## Las diez voces, medidas

Generadas con `banco.py`, cada una con su sala y su modo de nivelado:

| Instrumento | Nota | Dur | Sala | I | Pico real | Ataque | LRA |
|---|---|---|---|---|---|---|---|
| Piano | Do4 | 3,11 s | seco | −23,0 LUFS | −11,6 dBFS | **7 ms** | 20,3 |
| Violonchelo | Do3 | 3,40 s | sala | −23,0 LUFS | −14,1 dBFS | 266 ms | 0,4 |
| Violín | La4 | 2,80 s | sala | −23,0 LUFS | −14,3 dBFS | 278 ms | 0,0 |
| Flauta | La5 | 2,60 s | sala | −23,0 LUFS | −14,4 dBFS | 241 ms | 0,0 |
| Clarinete | Re4 | 2,84 s | cuarto | −23,0 LUFS | −17,5 dBFS | 65 ms | 0,0 |
| Bajo | Re2 | 3,40 s | — | −23,0 LUFS | −8,7 dBFS | 41 ms | 2,1 |
| Timbal | — | 1,81 s | sala | *(no aplica)* | **−12,0 dBFS** | 92 ms | — |
| Caja | — | 0,64 s | cuarto | *(no aplica)* | **−12,0 dBFS** | 4 ms | — |
| Golpe de mesa | — | 0,39 s | cuarto | *(no aplica)* | **−12,0 dBFS** | 3 ms | — |
| Colchón (pad) | Re2 | 14,00 s | — | −23,0 LUFS | −9,4 dBFS | 434 ms | 2,9 |

Los siete sostenidos caen **exactamente en −23,0 LUFS**; los tres golpes, exactamente en
−12,0 dBFS de pico. Esa es la condición para que el banco sea usable: se pueden cambiar
unos por otros sin retocar la mezcla.

## 🔴 Un banco se nivela por SONORIDAD, no por pico

Antes de esa tabla el banco se niveló al mismo **pico** (−12 dBFS) para los diez, y el
clarinete salió a −17,5 LUFS mientras la flauta salía a −37,0: **19,5 LU entre dos
instrumentos «nivelados»**. El pico mide la cresta, no lo que el oído oye — un ruido con
puntas y un tono denso con el mismo pico suenan a mundos distintos. Se nivela por `I`
(LUFS) y se comprueba que el pico no pase de −1 dBFS.

La excepción son los golpes: por debajo de ~1 s la puerta del integrado no abre y
devuelve −70 LUFS (`104`). **Lo sostenido por LUFS, lo percusivo por pico.**

## 🔴 `alimiter` no sirve de red de seguridad

Dos problemas, los dos comprobados:

```bash
volume=24,alimiter=limit=0.90                  # pico medido:  0,00 dBFS  ❌ no limita
volume=24,alimiter=limit=0.90:level=disabled   # pico medido: -0,91 dBFS  ✅
```

`level` viene **activado por defecto** y re-normaliza la salida hasta el techo. Y aun
con él desactivado, su reducción de ganancia es **no monótona**: el mismo violín con
`volume=0.5` sale a −6,02 dB y con `volume=2.255` sale a −12,01 dB. Más entrada, menos
salida.

Por eso el banco **no lleva limitador**: se mide en `pcm_f32le` (en `s16` el propio
recorte del formato falsea la medida justo cuando importa) y se reescala con un `volume`
plano. Lineal, reproducible, auditable.

## El motor: medir y reescalar

```python
def render(cadena, salida, sala="", modo="lufs", objetivo=None):
    """modo="lufs" para lo sostenido, modo="pico" para lo que dura menos de 1 s."""
    if objetivo is None:
        objetivo = -23.0 if modo == "lufs" else -12.0
    fc  = cadena + (("," + SALA[sala]) if SALA.get(sala) else "")
    tmp = salida + ".f32.wav"
    subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-filter_complex",
        fc + "[out]","-map","[out]","-c:a","pcm_f32le","-ar","44100","-ac","1",
        "-y",tmp], check=True)
    pk, lu = _medida(tmp)                      # pico en dB y sonoridad en LUFS
    g = 10 ** ((objetivo - (lu if modo == "lufs" else pk)) / 20.0)
    if pk + 20*math.log10(g) > -1.0:           # el pico manda sobre la sonoridad
        g = 10 ** ((-1.0 - pk) / 20.0)
    subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-i",tmp,
        "-af","volume=%.6f" % g,"-c:a","pcm_s16le","-ar","44100","-ac","1",
        "-y",salida], check=True)
    os.remove(tmp)
    return salida
```

El guardia del pico salvó un fallo real: mientras la flauta arrastraba los `NaN` de
`vibrato` (`102`) pedía subir hasta 0 dBFS para llegar a −23 LUFS, y el guardia avisó en
vez de publicar basura.

## Qué instrumento para qué tramo

| Tramo | Voz principal | Debajo |
|---|---|---|
| Gancho | Piano, notas sueltas | — |
| Exposición / documento | Piano (`expediente`) | Colchón a −30 LUFS |
| Lo que se cuenta y no consta | Piano (`sospecha`) + clarinete grave | — |
| Un dato que pesa | Chelo grave sostenido | — |
| Tensión que crece | Violín agudo, notas largas | Timbal espaciado |
| **Antes de una cifra** | **Nada: silencio** | **Nada** |
| La cifra | Golpe de mesa o timbal, seco | — |
| Remate | Piano (`cierre`), sala larga | Colchón con cola de 4–5 s |

Dos reglas duras que salen de la mezcla, no del gusto: **el bajo y la mano izquierda del
piano ocupan las mismas notas** (Re2, Si♭1), así que no van juntos; y **antes de una
cifra se calla todo**, porque el silencio es lo que da el golpe (`84`).

## Reproducibilidad

Tres cosas hacen que el banco de hoy sea el mismo que el de dentro de seis meses:

1. **`seed=1729` en toda fuente de ruido.** Sin semilla, el mismo comando da picos que
   varían 17 dB entre pasadas (`108`).
2. **`atrim=start=0.005,asetpts=PTS-STARTPTS` detrás de cada `vibrato`**, que emite
   muestras `NaN` al arrancar (`102`).
3. **Medir en float32, nivelar con `volume` plano**, sin limitador.

Sin las tres, «medir y corregir» mide una cosa y publica otra.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Nivelar el banco por pico | 19,5 LU entre el más alto y el más bajo |
| Nivelar un golpe por LUFS | −70 LUFS y pánico injustificado |
| Confiar en `alimiter` como red | No limita sin `:level=disabled`, y aun así no es monótono |
| Medir sobre `s16` | El recorte del formato falsea la medida donde más importa |
| Ruido sin `seed` | La pasada que mides no es la que se publica |
| `vibrato` sin `atrim` detrás | `NaN` que contamina la mezcla entera sin dar error |
| Bajo y mano izquierda del piano juntos | Barro: las dos ocupan Re2 |
| Música debajo de la cifra | Se come el golpe |

## Relacionado

`100` anatomía · `101` piano · `104` percusión · `107` la sala · `108` por qué suena a pitido · `86` medir el audio

# 289 · Errores de locución

**Qué resuelve:** el catálogo de fallos de la fase 3, ordenado por **síntoma**, porque es
así como aparecen. Casi ninguno hace ruido al producirse: la locución sale, el pipeline
sigue y el problema se descubre tres fases después, con el montaje hecho. Este módulo
cierra el bloque de voz y sirve de lista de revisión antes de aprobar.

---

## Síntoma → causa → arreglo

| Lo que se oye o se ve | Causa real | Arreglo |
|---|---|---|
| La voz dice una frase que no está en el guion | El extractor arrastró la cola de una línea de título: `split("## MINUTO 1")[1]` deja colgando `— guion cerrado` | `md.split("\n", 1)[1]` y, de cinturón, `txt.split("guion cerrado")[-1]` (§ `280`) |
| **Falta una frase entera** de la locución | El filtro descartó lo que empieza por `*` — y una línea en negrita empieza por `*` | Exigir el espacio: `("- ", "* ", "+ ")` |
| La voz lee «nota de pronunciación» | Las notas viven dentro del bloque locutable y el extractor no las filtra | Sacarlas fuera de la sección del minuto |
| Un elemento entra **5 s antes** de su frase | `tiempos.py` no cortaba en `?`, `!`, `…`, `»`: un grupo de menos descoloca todo el emparejamiento | Clase completa `[.,;:?!…»]` (§ `282`) |
| Todos los elementos entran algo tarde o pronto | Se cambió el `rate` después de la fase 4 | Se rehacen las fases 4-7. No hay atajo (§ `281`) |
| Un efecto suena 7 s antes de su palabra | Ancla a una palabra que se repite; `cuando()` devolvía la primera | `cuando("años", 38.49, n=2)` (§ `123`) |
| Un efecto cae en el segundo 0 | El ancla no casó (puntuación o tilde distinta) y se fue al defecto `0.0` | Defecto = el valor correcto conocido, y mirar el `print` |
| La locución suena cortada, cada frase empieza igual | Se generó frase por frase | Una sola pasada (§ `284`) |
| El MP3 pesa 0 bytes y nadie se enteró | El servicio rechaza la voz y **devuelve el flujo vacío sin excepción** | El `raise RuntimeError("edge-tts no devolvio audio")` de `voz.py` |
| La voz dice «uno punto cuatrocientos treinta y siete…» | Quedó una cifra en dígitos: lee el separador de miles | Números en letra (§ `283`) |
| Una pregunta no queda en el aire | `?` compra 0,40 s, no una pausa de punto | Punto y aparte después de la pregunta (§ `282`) |
| El párrafo no pausa más que el punto | Es así: `\n\n` no añade nada | Silencio fabricado (§ `288`) |
| La voz sube o baja de golpe entre bloques | Curva de relieve sin rampa, o frontera dentro de una frase | Rampas de 0,5 s (§ `285`) |
| La curva de relieve no hace nada | Falta `eval=frame`: la expresión se evalúa una sola vez | Añadirlo |
| ffmpeg falla con un error raro sobre la expresión | Las comas de la expresión no van escapadas (`\\,`) dentro del `filter_complex` | Escaparlas |
| La voz suena 5 dB por encima de todo | Se tocó la cadena de `voz.py` (típico: quitar el `aecho`) sin recalibrar el `volume=1.85` | Volver a medir el stem (§ `286`) |
| ffmpeg se queja de etiquetas y no se entiende por qué | La voz se usa dos veces —mezcla y llave del sidechain— sin `asplit` | `asplit=2[voz][vozsc]` (§ `85`) |
| Los tiempos no cuadran con el audio y todo parece bien | `tiempos.json` es de una versión y `locucion.mp3` de otra | Regenerar las dos juntas, siempre |
| Un nombre propio suena distinto en dos bloques | Se generó en dos pasadas, o se escribió de dos maneras | Una sola pasada y una sola grafía (§ `280`) |
| «se oye raro» y no se sabe dónde | Nadie ha escuchado la locución entera de una vez | Escucharla. Es la única parte que no se automatiza |

## La revisión de la fase 3, ejecutable

Se pasa **antes** de tocar la imagen. Devuelve avisos, no opiniones:

```python
# -*- coding: utf-8 -*-
"""Revisión de la fase 3: se pasa ANTES de tocar la imagen."""
import io, os, re, subprocess, sys
sys.path.insert(0, "piloto")
from tiempos import detectar_silencios

EPI = sys.argv[1]
txt = io.open(os.path.join(EPI, "guion.txt"), encoding="utf-8").read().strip()
mp3 = os.path.join(EPI, "locucion.mp3")
fallos = []

# 1 · el fichero existe y tiene audio
if not os.path.exists(mp3) or os.path.getsize(mp3) < 10000:
    fallos.append("locucion.mp3 vacío o inexistente")
d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
    "-of", "default=nw=1:nk=1", mp3], capture_output=True, text=True).stdout.strip())

# 2 · ninguna cifra en dígitos
cifras = re.findall(r"[$€]?\d[\d.,/%-]*[A-Za-z%]?", txt)
if cifras: fallos.append("cifras en dígitos: %s" % cifras[:5])

# 3 · ningún signo de cierre fuera de la clase del alineador
CLASE = set(".,;:?!…»")
fuera = {c for c in txt if not c.isalnum() and not c.isspace()} - CLASE - set("¿¡«-—()")
if fuera: fallos.append("signos que el alineador no corta: %s" % sorted(fuera))

# 4 · restos del markdown del guion
for marca in ("**", "guion cerrado", "···", "|", "#"):
    if marca in txt: fallos.append("resto de markdown en la locución: %r" % marca)

# 5 · ritmo
ppm = len(txt.split()) / d * 60
if not 130 <= ppm <= 160: fallos.append("ritmo fuera de rango: %.0f ppm" % ppm)

# 6 · grupos frente a silencios
grupos = len(re.split(r"(?<=[.,;:?!…»])\s+", txt))
sil = detectar_silencios(mp3)
if grupos > len(sil) + 1:
    fallos.append("más grupos (%d) que silencios (%d): revisar puntuación" % (grupos, len(sil)))

print("%s · %.2f s · %d palabras · %.0f ppm · %d grupos / %d silencios"
      % (EPI, d, len(txt.split()), ppm, grupos, len(sil)))
for f in fallos: print("   ! " + f)
print("   OK" if not fallos else "   %d AVISOS" % len(fallos))
```

Ejecutado sobre los dos episodios del piloto:

```
piloto/ep01-lustig · 63.45 s · 155 palabras · 147 ppm · 25 grupos / 27 silencios
   OK
piloto/episodio01  · 80.25 s · 201 palabras · 150 ppm · 29 grupos / 31 silencios
   OK
```

**Lo que este script no puede comprobar** —y por eso la revisión no acaba aquí— es si los
nombres propios suenan bien, si una cifra en letra dice lo que debe y si alguna frase se
atropella. Eso sólo lo caza el oído, escuchando la locución **entera y de una vez**.

## Los cuatro fallos que no avisan de ninguna manera

De todo el catálogo, estos cuatro renderizan un vídeo perfectamente válido y equivocado:

1. **El ancla que no casa** y se va a su valor por defecto. Imprime un aviso en consola
   que nadie lee.
2. **El `tiempos.json` de otra versión.** Todo funciona; todo cae mal.
3. **La cifra en dígitos.** El vídeo sale; la voz dice otra cosa.
4. **El signo fuera de la clase del alineador.** El desplazamiento no es uniforme, así que
   no se lee como un desfase de sincronía sino como un montaje mal hecho.

Los cuatro tienen el mismo antídoto: **medir y comparar contra un valor esperado**, no
comprobar que el proceso terminó sin error.

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Dar por buena la fase 3 porque el script terminó | La mitad de los fallos de voz salen sin error |
| No escuchar la locución entera antes de la fase 4 | Los nombres propios y las cifras en letra sólo se cazan oyendo |
| Ignorar los `print` de aviso de las anclas | Es la única señal que emiten los fallos silenciosos |
| Arreglar un fallo de voz en la mezcla | Se tapa el síntoma y el desfase sigue |
| Regenerar el audio sin regenerar los tiempos | Fallo silencioso garantizado |
| Repetir la revisión sólo del bloque tocado | Un cambio de palabra mueve todo lo posterior (§ `284`) |

## Relacionado

`280` escribir para una voz sintética · `281` ritmo en ppm · `282` la puntuación como
partitura · `283` cifras al oído · `284` una sola pasada · `285` el relieve se construye ·
`286` la cadena de proceso · `150` catálogo del fallo silencioso · `140` medir antes de
renderizar

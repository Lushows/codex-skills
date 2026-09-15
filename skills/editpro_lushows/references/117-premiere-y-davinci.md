# 117 — Hablar con editores profesionales: EDL, XML, AAF y OTIO

CapCut sirve cuando el revisor usa CapCut. Pero si al otro lado hay un editor con Premiere Pro, un
colorista con DaVinci Resolve, o una agencia con Final Cut, el puente de CapCut no les sirve de nada.

Para esos casos existen los **formatos de intercambio**: archivos que describen un montaje sin
depender del programa que lo hizo. Son viejos, están mal documentados, y funcionan a medias. Pero son
lo que hay, y saber cuál usar te ahorra días.

---

## Los cuatro formatos

| Formato | Nació | Qué lleva | Quién lo lee |
|---|---|---|---|
| **EDL** (CMX3600) | Años 70 | Solo cortes: qué clip, de dónde a dónde, en qué pista | Todos. Absolutamente todos. |
| **XML** (FCP7 XML / FCPXML) | 2000s / 2011 | Cortes + efectos básicos + transiciones + texto (parcial) | Premiere, Resolve, FCP |
| **AAF** | Años 90 | Cortes + audio con procesamiento + medios embebidos | Avid, Pro Tools, Premiere |
| **OTIO** | 2018, Academy | Cortes + pistas + marcadores + metadatos, extensible | Resolve, herramientas modernas, Blender |

La regla mental:

> **EDL = lo mínimo que siempre funciona.
> XML = lo práctico entre Premiere/Resolve/FCP.
> AAF = para el que hace el audio.
> OTIO = el moderno y el más limpio de generar por código.**

---

## EDL: el mínimo común denominador

Un EDL es un archivo de texto plano. Se ve así:

```
TITLE: REEL GASTROLATAM V1
FCM: NON-DROP FRAME

001  A001     V     C        01:00:12:12 01:00:14:27 00:00:00:00 00:00:02:15
* FROM CLIP NAME: entrevista_A001.mp4

002  A001     V     C        01:00:45:03 01:00:48:21 00:00:02:15 00:00:06:03
* FROM CLIP NAME: entrevista_A001.mp4

003  B004     V     C        02:00:03:00 02:00:05:06 00:00:06:03 00:00:08:09
* FROM CLIP NAME: broll_B004.mp4
```

Columna por columna:

| Columna | Qué es |
|---|---|
| `001` | Número de evento (correlativo, siempre 3 dígitos) |
| `A001` | Nombre de la cinta / clip (máximo 8 caracteres en el estándar estricto) |
| `V` | Canal: `V` video, `A` audio, `A1`, `A2`, `AA` (ambos), `B` (los dos) |
| `C` | Tipo: `C` corte, `D` disolvencia, `W` wipe |
| `01:00:12:12` | **Source In** — dónde empieza en el material original |
| `01:00:14:27` | **Source Out** |
| `00:00:00:00` | **Record In** — dónde cae en la línea de tiempo |
| `00:00:02:15` | **Record Out** |

El formato de timecode es `HH:MM:SS:FF` (horas, minutos, segundos, **fotogramas**).

### Lo bueno y lo malo del EDL

**Bueno:**
- Lo lee absolutamente todo. Es el esperanto del montaje.
- Es texto plano trivial de generar por código.
- No se rompe. Un EDL de 1985 abre hoy.

**Malo:**
- **Solo una pista de video.** Si tu montaje tiene b-roll encima, hacen falta varios EDL (uno por
  pista) y el editor los ensambla a mano.
- **Nada de texto, efectos, color, escala ni posición.** Nada.
- Nombres de clip cortos y sin caracteres raros.
- El `Source Out` y el `Record Out` son **exclusivos** (el último fotograma no se incluye), y eso genera
  errores de un fotograma si no lo tenés en cuenta.

**Cuándo usarlo:** cuando lo único que querés transmitir es *dónde van los cortes*. Y sorprendentemente,
eso es lo que más vale. Un editor profesional prefiere recibir el orden y los puntos de corte y hacer
él el resto, que recibir un XML medio roto lleno de efectos que tiene que borrar.

### Timecode y fotogramas

Para convertir microsegundos (lo que usa CapCut) a timecode:

```python
def us_a_timecode(us, fps):
    total_frames = round(us * fps / 1_000_000)
    f = total_frames % round(fps)
    s = (total_frames // round(fps)) % 60
    m = (total_frames // (round(fps) * 60)) % 60
    h = total_frames // (round(fps) * 3600)
    return f"{h:02d}:{m:02d}:{s:02d}:{f:02d}"
```

**Drop frame:** a 29.97 y 59.94 fps existe una convención donde el timecode "salta" números para
mantenerse pegado al reloj real. Se escribe con punto y coma: `01:00:12;12`. En el EDL se declara con
`FCM: DROP FRAME` o `FCM: NON-DROP FRAME`.

**Consejo:** grabá y trabajá a 30 o 25 fps exactos y evitás todo el tema. El drop frame es una herencia
de la televisión NTSC que solo trae problemas si no la necesitás. CapCut tiene el campo
`is_drop_frame_timecode` justamente para esto.

---

## XML: el que se usa en la práctica

Hay dos cosas distintas que la gente llama "XML":

**FCP7 XML** (también "XML legacy") — el formato de Final Cut Pro 7. A pesar de que ese programa
murió en 2011, **sigue siendo el formato de intercambio más usado** entre Premiere y Resolve, porque
ambos lo leen y lo escriben bien.

**FCPXML** — el de Final Cut Pro X/moderno. Distinto, más nuevo, más limpio, pero peor soportado fuera
del mundo Apple.

### Qué lleva un XML

- Múltiples pistas de video y audio ✅
- Puntos de corte exactos ✅
- Rutas a los archivos ✅
- Velocidad de clips ✅ (a veces)
- Transiciones básicas (disolvencias) ⚠️ parcial
- Escala, posición, rotación ⚠️ parcial, se traduce mal
- Volumen y fades de audio ⚠️ parcial
- Texto y títulos ❌ casi nunca sobrevive
- Efectos y color ❌ no

### Cómo generarlo

Escribir FCP7 XML a mano es posible pero tedioso: es un XML anidado con estructuras heredadas de los
años 90. **La forma sensata es generar OTIO y convertirlo**, o usar una librería que lo escriba.

Estructura mínima, para que sepas qué estás mirando:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xmeml version="5">
  <sequence>
    <name>Reel GastroLatam v1</name>
    <duration>1152</duration>
    <rate><timebase>30</timebase><ntsc>FALSE</ntsc></rate>
    <media>
      <video>
        <track>
          <clipitem>
            <name>entrevista_A001.mp4</name>
            <start>0</start>      <!-- en la timeline, en FOTOGRAMAS -->
            <end>75</end>
            <in>372</in>          <!-- en el archivo original, en FOTOGRAMAS -->
            <out>447</out>
            <file id="f1">
              <pathurl>file://localhost/C:/media/reel001/entrevista_A001.mp4</pathurl>
            </file>
          </clipitem>
        </track>
      </video>
    </media>
  </sequence>
</xmeml>
```

**Todo va en fotogramas, no en microsegundos ni en segundos.** Ese es el primer ajuste mental al venir
de CapCut.

**Cuándo usarlo:** cuando el destino es Premiere o Resolve y necesitás pasar más de una pista. Es el
punto dulce entre "no llega nada" (EDL) y "nada funciona" (formatos exóticos).

---

## AAF: para el que hace el audio

AAF (Advanced Authoring Format) es un formato binario, pesado, del mundo Avid. Su razón de existir hoy
es una: **entregarle el audio al que va a mezclar en Pro Tools.**

Lo que lo hace útil:
- Lleva **todas las pistas de audio** con sus niveles, fades y panorámicas.
- Puede **embeber los medios** dentro del propio archivo, así que no hay que mandar los archivos
  aparte ni preocuparse por rutas rotas.
- Lleva "handles" (colas extra antes y después de cada corte) para que el mezclador tenga margen.

Lo que lo hace incómodo:
- Es binario. No lo generás con un script casero.
- Los archivos pesan mucho (con medios embebidos, gigas).
- El soporte de video/efectos es peor que el de audio.

**Cuándo usarlo:** solo cuando hay una persona de audio de verdad, con Pro Tools, esperando el corte.
Si no, no lo toques. Se genera desde Premiere o Resolve, no desde código.

---

## OTIO: el formato moderno

**OpenTimelineIO** es un proyecto de la Academy Software Foundation (la misma gente de OpenEXR y
Alembic). Nació para resolver exactamente este problema: describir una línea de tiempo de forma
neutral y con adaptadores hacia todos los demás formatos.

Un `.otio` es **JSON**, o sea que se genera y se lee con la misma facilidad que un `draft_content.json`:

```json
{
  "OTIO_SCHEMA": "Timeline.1",
  "name": "Reel GastroLatam v1",
  "tracks": {
    "OTIO_SCHEMA": "Stack.1",
    "children": [
      {
        "OTIO_SCHEMA": "Track.1",
        "kind": "Video",
        "children": [
          {
            "OTIO_SCHEMA": "Clip.1",
            "name": "entrevista_A001",
            "source_range": {
              "OTIO_SCHEMA": "TimeRange.1",
              "start_time": { "OTIO_SCHEMA": "RationalTime.1", "value": 372, "rate": 30 },
              "duration":   { "OTIO_SCHEMA": "RationalTime.1", "value": 75,  "rate": 30 }
            },
            "media_reference": {
              "OTIO_SCHEMA": "ExternalReference.1",
              "target_url": "file:///C:/media/reel001/entrevista_A001.mp4"
            }
          }
        ]
      }
    ]
  }
}
```

**Fijate en `RationalTime`:** el tiempo se guarda como un número **y su tasa** (`value: 372, rate: 30`
= fotograma 372 a 30 fps). Es la forma correcta de guardar tiempo en video, porque no hay redondeo:
no se convierte a segundos nunca. Es más limpio que los microsegundos de CapCut.

### Por qué OTIO es el mejor punto de salida

1. Es JSON: se genera por código sin dolor.
2. Tiene **adaptadores** a EDL, FCP7 XML, FCPXML, AAF y más. Generás una vez y convertís a lo que
   necesite el destino.
3. Resolve lo importa directamente.
4. Es abierto, mantenido por la industria, y no depende de ningún vendedor.
5. `capcut-cli` **exporta a OTIO**, o sea que hay un camino directo de CapCut a Resolve.

```bash
pip install opentimelineio
otiocat mi_montaje.otio                          # verlo
otioconvert -i mi_montaje.otio -o corte.edl      # convertir a EDL
otioconvert -i mi_montaje.otio -o corte.xml      # a FCP7 XML
otioview mi_montaje.otio                          # verlo gráficamente
```

**La arquitectura recomendada:** generá **OTIO como formato interno** y convertí al vuelo a lo que
pida cada destino. Así tenés una sola representación del montaje y no mantenés cinco generadores.

```
tu montaje (datos)
   ├──→ draft_content.json  → CapCut  (el revisor de marketing)
   └──→ .otio  ─┬──→ .edl   → cualquiera
                ├──→ .xml   → Premiere / Resolve
                └──→ directo → Resolve
```

### La advertencia sobre OTIO

OTIO transmite bien lo **estructural**: clips, pistas, tiempos, marcadores, metadatos. Los efectos, las
transiciones complejas, el retiming con curvas, los clips compuestos y los conceptos propios de cada
programa **requieren adaptación caso por caso o directamente no viajan**.

En la práctica: **OTIO es un formato de intercambio estructural, no una garantía de ida y vuelta.**
Probá si tu par origen-destino conserva lo que a vos te importa, en vez de asumir que sí.

---

## Qué formato para qué destino

| El otro usa… | Mandale | Nota |
|---|---|---|
| **CapCut** | El proyecto de CapCut (módulos 110-115) | El puente directo |
| **Premiere Pro** | FCP7 XML | Y el máster de referencia |
| **DaVinci Resolve** | OTIO o FCP7 XML | Resolve importa OTIO nativo |
| **Final Cut Pro** | FCPXML | |
| **Avid Media Composer** | AAF | Generado desde Premiere/Resolve, no desde código |
| **Pro Tools (audio)** | AAF con medios embebidos y handles | |
| **No sabés / da igual** | EDL + máster + recursos sueltos | Siempre funciona (módulo 118) |

---

## Reglas que salvan la entrega

**1. Mandá siempre el máster junto al proyecto.** Un MP4 del corte como estaba cuando lo entregaste.
Si el intercambio falla, el otro por lo menos ve qué querías. Sin eso, un XML roto es papel.

**2. Rutas absolutas y una carpeta plana.** Todos los medios en un solo lugar, sin subcarpetas
profundas, sin acentos, sin espacios si podés. El relink va a fallar igual, pero va a ser más fácil de
arreglar.

**3. Nombres de archivo estables y cortos.** El EDL trunca a 8 caracteres. Nombrá `A001.mp4`,
`B004.mp4`, no `Grabación día 2 - toma buena (final).mp4`.

**4. Un solo fps en todo.** Mezclar 24, 30 y 60 en la misma línea de tiempo genera errores de
conversión en cada intercambio. Unificá antes.

**5. Probá el intercambio con un corte de prueba de tres clips** antes de mandar el montaje real. Diez
minutos de prueba ahorran un día de conform.

**6. Documentá lo que sabés que se pierde.** Si tu montaje tiene textos y sabés que el XML no los
lleva, decilo en la entrega y mandá los textos aparte en un archivo. Es el tema del módulo 118.

---

## Errores comunes

**Mandar un XML y asumir que llegó todo.** Los textos, los efectos y el color casi nunca sobreviven.
El otro abre, ve el corte sin nada encima, y piensa que le mandaste basura.

**Confundir FCP7 XML con FCPXML.** Son formatos distintos con nombres casi iguales. Premiere y Resolve
prefieren el viejo.

**Trabajar en microsegundos y escribir fotogramas sin convertir.** En EDL y XML todo va en fotogramas.
Es la conversión que más errores de un fotograma genera.

**Ignorar el drop frame.** A 29.97 fps, un timecode non-drop se desvía del reloj real casi 4 segundos
por hora. En un video de un minuto no importa; en una entrega de televisión sí.

**Olvidar que el Out del EDL es exclusivo.** Un fotograma de diferencia en cada corte, cincuenta veces.

**Nombres de archivo largos, con acentos o espacios en un EDL.** Se truncan o se rompen.

**Mezclar frame rates.** Cada conversión redondea y el error se acumula.

**Generar AAF por código.** Es binario y complejo. Se genera desde un NLE.

**Mandar el intercambio sin el máster de referencia.** Si algo falla, el otro no tiene con qué
comparar.

**No probar el intercambio antes.** Cada par de programas tiene sus manías. Probá con tres clips.

**Asumir que OTIO es ida y vuelta sin pérdida.** Es estructural. Los efectos requieren trabajo caso por
caso o no viajan.

---

## Checklist

- [ ] Sé qué programa usa la persona que va a recibir el corte
- [ ] Elegí el formato según ese destino, no según mi comodidad
- [ ] Todo el proyecto está a un solo frame rate
- [ ] Los nombres de archivo son cortos, sin acentos y sin espacios
- [ ] Los medios están en una carpeta plana con ruta estable
- [ ] Convertí los tiempos de microsegundos a fotogramas correctamente
- [ ] Declaré bien drop frame vs. non-drop si estoy a 29.97 o 59.94
- [ ] Tuve en cuenta que el Out del EDL es exclusivo
- [ ] Si uso OTIO, verifiqué que el adaptador de destino conserva lo que me importa
- [ ] Probé el intercambio con tres clips antes de mandar el montaje completo
- [ ] Mando el **máster de referencia** junto con el archivo de intercambio
- [ ] Documenté por escrito qué se pierde en este formato y qué mando aparte
- [ ] Si hay un mezclador de audio, le mando AAF con handles, no el mismo XML

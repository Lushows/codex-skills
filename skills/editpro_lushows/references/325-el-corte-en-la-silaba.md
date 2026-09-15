# 325 — El corte en la sílaba: dentro de la palabra, entre palabras, entre frases

**Qué resuelve:** el módulo `98` documenta cuatro defectos reales encontrados en videos ya montados, y dos
de los cuatro eran cortes que cayeron dentro de una palabra. No fue mala suerte: fue **cortar por
aritmética en material hablado**. Este módulo es la escala fina del ritmo —por debajo del plano, por debajo
del fotograma de acción— donde el que manda es el habla.

Es el nivel donde tu formato dominante (alguien hablando a cámara, jump cuts, sin transiciones) se gana o
se pierde.

---

## 1. Cuánto dura una sílaba en español

Pellegrino, Coupé y Marsico (*Language*, 2011, "A cross-language perspective on speech information rate")
midieron velocidad silábica y densidad de información en siete idiomas, con ~60 hablantes nativos leyendo
los mismos textos traducidos:

| Idioma | Sílabas por segundo | Densidad de información por sílaba |
|---|---|---|
| Japonés | 7,84 | 0,49 |
| **Español** | **7,82** | **0,63** |
| Francés | 7,18 | 0,74 |
| Italiano | 6,99 | 0,72 |
| **Inglés** | **6,19** | **0,91** |
| Alemán | 5,97 | 0,79 |
| Mandarín | 5,18 | 0,94 |

El español es de los idiomas más rápidos en sílabas por segundo **y** de los que menos información mete en
cada una. Trabajo posterior del mismo grupo (Coupé, Oh, Dediu y Pellegrino, *Science Advances*, 2019)
encontró que el caudal de información resultante ronda los **39 bits por segundo en todos los idiomas
medidos**: los que hablan rápido compensan con sílabas menos densas.

**Lo que eso significa en tu línea de tiempo:**

```
7,8 sílabas/segundo  →  1 sílaba ≈ 128 ms  →  ≈ 3,8 fotogramas a 30 fps
```

Ese número es de habla leída en laboratorio. En habla espontánea de reel, con pausas y muletillas, vas a
medir entre **5,5 y 7 sílabas por segundo**, es decir **entre 143 y 182 ms** por sílaba: **de 4 a 5,5
fotogramas**.

> **La consecuencia operativa que hay que interiorizar:** una sílaba en español mide **entre 4 y 5
> fotogramas**. Un error de dos fotogramas al colocar un corte te mete media sílaba adentro.

Por eso "corta más o menos por ahí" no existe en material hablado. La tolerancia real de un corte de voz
en español es de **±2 fotogramas (±0,07 s)**, y por eso los tiempos se manejan como dice `15`: en segundos
con decimales, nunca en minuto:segundo.

Mídelo en tu propio material antes de creerle a nadie — cuenta las sílabas de un tramo y divide:

```bash
awk 'BEGIN{silabas=47; dur=7.4; printf "%.2f sil/s → %.0f ms por sílaba → %.1f fotogramas a 30 fps\n",
  silabas/dur, 1000/(silabas/dur), 30/(silabas/dur)}'
```

---

## 2. Por qué no hay silencio entre las palabras

El error mental más caro de este módulo es creer que el habla viene separada en palabras, como la escritura.
No lo está.

En español, además, ocurre **resilabificación** a través del límite de palabra: la consonante final de una
palabra se pega como ataque de la sílaba siguiente.

```
escrito:   "los  amigos"      →  hablado:  lo-sa-mi-gos
escrito:   "el  agua"         →  hablado:  e-la-gua
escrito:   "un  año"          →  hablado:  u-na-ño
```

**No hay ningún punto físico entre "los" y "amigos" donde puedas cortar.** El límite de palabra existe en
tu cabeza, no en la señal. Si cortas ahí, te llevas la /s/ y queda "lo... amigos", que suena a defecto.

Dónde SÍ hay bordes reales que puedes usar:

| Borde real | Qué es | Calidad del corte |
|---|---|---|
| **Pausa de respiración** | 150–500 ms de casi-silencio | ✅ El mejor. Corte limpio garantizado |
| **Inicio de oclusiva** (p, t, k, b, d, g) | hay un micro-silencio de 30–80 ms *antes* del golpe | ✅ Excelente. Corte inaudible |
| **Fin de grupo entonativo** | la entonación baja y hay pausa breve | ✅ Bueno. Se siente como punto |
| **Inicio de sílaba tónica** | pico de energía | 🟡 Aceptable si el sonido inicial es consonante |
| Dentro de una vocal | energía continua | ❌ Chasquido garantizado |
| Dentro de /s/, /f/, /r/ | ruido continuo | ❌ Se oye el corte como un "tsch" |
| Mitad de palabra | — | ❌ Defecto siempre (`98`) |

**El truco práctico más útil de todo el módulo:** busca las **oclusivas**. Antes de una p, t, k, b, d, g
hay un silencio físico real de 30 a 80 ms, porque la boca cierra para acumular presión. Cortar justo ahí
es cortar en un silencio, aunque suene continuo. Si tienes que empezar una frase por corte, empezar en
palabra que arranca con oclusiva ("**p**orque", "**t**odo", "**c**uando", "**b**ueno") es dos veces más
limpio que empezar en vocal.

---

## 3. Qué hace cada tipo de corte

Aquí está la pregunta del módulo respondida directamente.

### Cortar DENTRO de la palabra

**Qué hace:** rompe. Sin excepciones estéticas.

La escritura y el habla se procesan por unidades léxicas; media palabra no es media información, es cero
información más una señal de error. El espectador no piensa "qué corte interesante": piensa "esto está mal
editado", casi siempre sin saber por qué.

Es el defecto #2 documentado en `98` (`"las principales carac—"`), y es el resultado típico de cortar por
tiempos calculados en vez de por contenido.

**La única excepción real:** cuando el corte a media palabra **es** el chiste — alguien interrumpido, un
corte brusco cómico, un remate que se corta a propósito. Y ahí hay que hacerlo evidente: partir la palabra
al principio (dos sílabas mínimo, no una consonante suelta) y acompañarlo con un evento visual, o se lee
como error.

### Cortar ENTRE palabras, dentro de la misma frase

**Qué hace:** **comprime y acelera**. Es el motor de tu estilo.

Quitar los 200–400 ms de aire entre palabras, o pegar dos tramos de habla sin la pausa que había en medio,
produce una sensación de urgencia y densidad. La persona suena más segura, más rápida, más segura de lo que
dice. Es lo que hace que un video de alguien hablando frente a la cámara no se sienta como un video de
alguien hablando frente a la cámara.

Costo: se pierde la respiración, y un video entero cortado así **agota** porque el espectador tampoco
respira. Deja respiraciones a propósito cada 8–12 segundos.

### Cortar ENTRE frases (fin de grupo entonativo)

**Qué hace:** **da comprensión y jerarquía**. Es el punto y aparte.

Es donde debe caer un corte que quieres que se note (`324` §5), donde debe entrar un bloque de texto nuevo,
y donde el espectador procesa lo que acaba de oír. Si tu video tiene un dato importante, la frase que lo
contiene necesita un borde limpio a ambos lados o el dato se pierde en el flujo.

Costo: alarga. Tres cortes de frase seguidos con sus pausas intactas y ya se siente lento.

> **La mezcla correcta en un reel de 25 s:** la mayoría de los cortes entre palabras (velocidad), **dos o
> tres** en fin de frase (los que separan bloques), **cero** dentro de palabra.

---

## 4. Encontrar los bordes con datos

### Los micro-silencios

`silencedetect` con parámetros agresivos encuentra respiraciones y pausas entre palabras, no solo los
silencios largos que busca `98`:

```bash
ffmpeg -hide_banner -i plano.wav -af "silencedetect=noise=-32dB:d=0.06" -f null - 2>&1 \
  | grep -E "silence_(start|end)" \
  | awk '/start/{s=$NF} /end/{printf "pausa %.3f → %.3f  (%.0f ms)\n", s, $(NF-2), ($(NF-2)-s)*1000}'
```

`d=0.06` = 60 ms, que es del orden de una oclusiva. `noise=-32dB` es el umbral: súbelo a −28 dB si tu
grabación tiene ruido de bar, bájalo a −38 dB si grabaste en silencio.

Cada pausa que salga es **un punto de corte gratis**. Corta en su mitad, no en su borde.

### La onda, para verla

```bash
# Onda del plano con rejilla de tiempo: se ven las sílabas a ojo
ffmpeg -hide_banner -y -i plano.wav -filter_complex \
 "showwavespic=s=1920x300:colors=white|white,drawgrid=w=64:h=300:t=1:c=red@0.4" \
 -frames:v 1 onda.png
```

Con `s=1920` y una rejilla cada 64 px, si el plano dura 6 s cada casilla vale 0,2 s. **Cada joroba es una
sílaba.** Los valles entre jorobas son tus puntos de corte. Es la herramienta más rápida que existe para
esto y no requiere nada más. Si quieres el número en vez de la imagen, `astats=metadata=1:reset=1` con
`ametadata=print:key=lavfi.astats.Overall.RMS_level` te da la energía cada ~20 ms: resolución de sobra para
una sílaba de 128–180 ms.

### Timecodes por palabra

La vía rápida y la mejor: transcripción con marcas de tiempo por palabra (`124`, `13`). Con eso no
estimas nada — sabes que la palabra "porque" empieza en 4,382 s y termina en 4,791 s, y cortas en 4,36.

---

## 5. Los dos arreglos que hay que saber

### El chasquido

Todo corte de audio en un punto que no es silencio produce un salto de amplitud, y un salto de amplitud es
un chasquido. Se arregla con un fundido de **10–30 ms**, imperceptible:

```bash
# Fundido de entrada de 20 ms y de salida de 20 ms en un tramo cortado
ffmpeg -hide_banner -i tramo.wav -af "afade=t=in:st=0:d=0.02,afade=t=out:st=2.48:d=0.02" tramo_limpio.wav
```

En CapCut: fundido de audio al mínimo (0,1 s) en los dos extremos del clip. Es más largo de lo ideal pero
sirve, y es un arrastre de dos segundos.

### El corte partido (L-cut / J-cut)

El corte de imagen y el corte de audio **no tienen que caer en el mismo fotograma**, y en material hablado
casi nunca deberían.

```
AUDIO   ────────────────────────┼──────────────────
VIDEO   ──────────────┼─────────────────────────────
                      ▲         ▲
              corta la imagen   corta el audio
              (sobre movimiento) (en la pausa)
```

Esto resuelve el conflicto que atraviesa todo el bloque: la imagen quiere cortar sobre movimiento (`324`) y
el audio sobre pausa (este módulo). **Con el corte partido los dos ganan.** Ver `21` y `23`.

En un reel de jump cuts sobre la misma persona esto no aplica (es la misma toma continua), pero en cuanto
metes un plano de apoyo —el producto, las manos, el local— aplica siempre.

---

## Errores comunes

1. **Cortar por aritmética en material hablado.** "Este plano debe durar 1,2 s" te lleva directo a media
   palabra. El habla manda sobre la duración objetivo (`322` §5).
2. **Creer que hay silencio entre las palabras.** En español la resilabificación pega las palabras. El
   borde de palabra escrito no existe en el audio.
3. **Cortar dentro de una vocal o de una /s/.** Chasquido garantizado. Busca la oclusiva más cercana.
4. **Empezar una frase por corte en una palabra que arranca en vocal.** Suena a arranque cortado. Si puedes
   elegir, arranca en p, t, k, b, d o g.
5. **No poner fundido de 10–30 ms en los empalmes de voz.** Es el 90% de los chasquidos de un reel amateur
   y se arregla en dos segundos por corte.
6. **Quitar todas las respiraciones.** El video se vuelve asfixiante a los 15 segundos. Deja una cada
   8–12 s, o déjala baja de fondo.
7. **Cortar imagen y audio en el mismo fotograma siempre.** El corte partido resuelve el conflicto entre
   `324` y este módulo y casi nadie lo usa.
8. **Fiarse del ojo para colocar un corte de voz.** La tolerancia es de ±2 fotogramas y el ojo no llega
   ahí. Usa la onda o los timecodes por palabra.
9. **Usar `silencedetect` con los parámetros de `98` para esto.** `d=1.5` busca huecos; para bordes de
   sílaba necesitas `d=0.06`.
10. **Partir una palabra "porque queda gracioso" sin marcarlo.** Sin evento visual que lo acompañe, se lee
    como error, no como chiste.
11. **Aplicar el dato de 7,82 sílabas por segundo como si fuera tu velocidad.** Es habla leída de
    laboratorio. Mide la tuya: casi seguro estás entre 5,5 y 7.
12. **Verificar el resultado a 2× de velocidad.** A esa velocidad no se oye una palabra partida. Es
    literalmente el error que documenta `98`.

---

## Checklist

- [ ] Medí las **sílabas por segundo** de mi propio material y sé cuántos fotogramas dura una sílaba
- [ ] Ningún corte del video cae **dentro de una palabra** (verificado con `98`, no con el ojo)
- [ ] Los cortes de compresión caen en **micro-pausas reales**, localizadas con `silencedetect d=0.06` o
      con timecodes por palabra
- [ ] Los cortes que quiero que se noten caen en **fin de grupo entonativo**
- [ ] Todo empalme de voz tiene **fundido de 10–30 ms** en los dos extremos
- [ ] Las frases que empiezan por corte arrancan, cuando se puede, en **consonante oclusiva**
- [ ] Hay al menos una **respiración audible** cada 8–12 segundos
- [ ] Donde hay plano de apoyo, usé **corte partido**: imagen y audio no cortan en el mismo fotograma
- [ ] Saqué la **onda con rejilla** de los planos donde el empalme no me convencía
- [ ] Escuché el corte final completo, a velocidad normal, con audífonos

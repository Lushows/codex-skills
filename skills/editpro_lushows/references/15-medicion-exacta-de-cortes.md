# 15 — Medición exacta de cortes

## Qué resuelve

Que el corte caiga donde tiene que caer, al décimo de segundo, y que la instrucción que le das a otra
persona o a un modelo signifique una sola cosa. Este módulo es corto en concepto y largo en consecuencias:
casi todos los defectos visibles de un montaje amateur — palabras partidas, respiraciones cortadas,
frases que arrancan a mitad — son errores de medición, no de gusto.

Dos errores reales, los dos caros, gobiernan este módulo:

1. **Se pidió "la toma cerca del minuto 1:29" y el modelo devolvió el segundo 128,3.** Leyó `1:29` como
   `129` segundos. Nadie mintió: la instrucción era ambigua.
2. **Se pidió el tramo 128–136 s de un clip que duraba 101 s.** El comando corrió sin queja visible y
   produjo basura.

De ahí salen las dos leyes del módulo: **una sola unidad** y **comprobar antes de cortar**.

---

## Ley 1 — Habla siempre en segundos, nunca en minuto:segundo

`1:29` puede significar:

- 1 minuto 29 segundos = **89 s**
- 129 segundos (si alguien lo leyó como número) = **129 s**
- 1 hora 29 minutos, en un timecode de largometraje
- el fotograma 29 del segundo 1, en notación `SS:FF`

Cuatro lecturas distintas de la misma cadena. Cuando la instrucción va a un modelo, a un script o a otra
persona, esa ambigüedad se cobra tarde: cuando ya renderizaste.

**Regla:** en todo el proyecto, en transcripciones, tablas, prompts y conversaciones, el tiempo se
escribe en **segundos con un decimal**.

| No escribas | Escribe |
|---|---|
| "la toma del minuto 1:29" | "la toma que empieza en el segundo 89.0" |
| "corta en 0:45" | "corta en el segundo 45.0" |
| "los últimos 10 segundos" | "del segundo 51.4 al 61.4" |
| "por la mitad" | "en el segundo 30.7" |

Si necesitas mostrarle minutos a un humano para que se ubique, escribe las dos cosas y deja clarísimo
cuál manda:

```
segundo 89.0 (≈ 1 min 29 s) — manda el 89.0
```

Cuando el número va dentro de un comando de ffmpeg, **solo segundos**. ffmpeg acepta `00:01:29.0` y lo
interpreta bien, pero mezclar notaciones dentro de un mismo proyecto es exactamente cómo aparece el error.

---

## Ley 2 — Comprueba la duración antes de cortar

Nunca escribas un `-ss` o un `-t` sin haber leído la duración real del archivo.

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 entrada/clip-07.mp4
```

Y en cualquier script que corte en lote, la comprobación va **antes** del corte, no después:

```powershell
function Cortar-Seguro {
  param(
    [string]$Origen,
    [double]$Inicio,
    [double]$Duracion,
    [string]$Destino
  )
  $dur = [double](& ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 $Origen)
  $fin = $Inicio + $Duracion

  if ($Inicio -lt 0) { throw "Inicio negativo: $Inicio" }
  if ($Inicio -ge $dur) { throw ("Inicio {0} s fuera del clip (dura {1} s)" -f $Inicio, [math]::Round($dur,2)) }
  if ($fin -gt $dur) { throw ("Pide hasta {0} s pero el clip dura {1} s" -f [math]::Round($fin,2), [math]::Round($dur,2)) }
  if ($Duracion -le 0) { throw "Duracion no positiva: $Duracion" }

  & ffmpeg -y -hide_banner -loglevel error -ss $Inicio -i $Origen -t $Duracion -c:v libx264 -crf 20 -preset veryfast -c:a aac -b:a 128k $Destino
  Write-Output ("OK {0}: {1} s -> {2} s" -f (Split-Path $Destino -Leaf), $Inicio, $fin)
}

Cortar-Seguro -Origen "entrada\clip-07.mp4" -Inicio 8.0 -Duracion 6.6 -Destino "trabajo\cortes\b03.mp4"
```

Que lance excepción es intencional: **quieres que se caiga ruidosamente**, no que produzca un archivo
raro que descubras en el render final.

---

## Ley 3 — Pide siempre "qué se oye después"

Este es el truco que más errores atrapa y casi nadie usa. Cuando le pides a un modelo (o a ti mismo) un
punto de corte, pide **tres cosas**, no una:

```
Para el bloque "de que esta hecha la botella", dame:

- inicio: segundo con un decimal donde arranca la primera palabra
- fin: segundo con un decimal donde termina la ultima palabra
- que_se_oye_antes: las 5 palabras justo ANTES del inicio
- que_se_oye_despues: las 5 palabras justo DESPUES del fin

Si en que_se_oye_despues la primera palabra es una continuacion de la frase
(un "y", un "porque", una palabra a medias), avisame: significa que el fin esta corto.
```

Por qué funciona: un número solo no se puede verificar. Un número **con su contexto de audio** sí. Si te
devuelve:

```
fin: 49.9
que_se_oye_despues: "porque cada botella fue otra"
```

sabes inmediatamente que te pasaste de corto: la frase seguía. Y si te devuelve:

```
fin: 49.9
que_se_oye_despues: "[SILENCIO] bueno, otra vez"
```

sabes que cortaste limpio, en la pausa, justo antes de la siguiente toma.

Esa columna `que_se_oye_despues` es lo que después alimenta la compuerta de validación del módulo 16.

---

## Dónde va exactamente el corte

### El aire de entrada y de salida

Nunca cortes pegado a la primera y la última palabra. Deja **aire**: un colchón de silencio antes y
después.

| Situación | Aire antes | Aire después |
|---|---|---|
| Toma hablada suelta | 0,15–0,30 s | 0,25–0,50 s |
| Corte que entra sobre música | 0,10 s | 0,20 s |
| Frase de gancho (arranque del video) | 0,05 s | 0,30 s |
| Remate final | 0,20 s | 0,60–1,00 s |

Sin aire, la palabra suena mocha aunque el corte esté técnicamente después de la última sílaba: el final
de una palabra tiene una cola de resonancia que no está en el texto pero sí en el oído.

Con demasiado aire (más de 0,8 s en video corto) el ritmo se cae. Ver módulo 20.

### Cortar en la respiración, no en el silencio absoluto

El mejor punto de corte de una frase hablada es **durante la inhalación** que precede a la siguiente
frase, no en el silencio muerto. Se oye natural porque así se oye el habla real. Se encuentra con
`silencedetect`:

```bash
ffmpeg -hide_banner -i entrada/clip-03.mp4 -af "silencedetect=noise=-38dB:d=0.25" -f null -
```

Cada `silence_start` es un candidato a punto de corte. El corte va unos 0,1 s **después** del
`silence_start`, no en el `silence_end`.

### Fotogramas y por qué el décimo de segundo alcanza

A 30 fps, un fotograma dura 0,033 s. A 24 fps, 0,042 s. Un décimo de segundo son 3 fotogramas a 30 fps:
suficiente resolución para cualquier decisión de montaje de voz, y lo bastante grueso para que no te
vuelvas loco.

Si necesitas precisión de fotograma exacto (match cut sobre un movimiento, sincronía con un golpe
musical), convierte:

```
segundo = fotograma / fps
fotograma 47 a 29.97 fps = 47 / 29.97 = 1.568 s
```

Y verifica el fps real, que casi nunca es redondo:

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of default=nw=1:nk=1 entrada/clip-03.mp4
```

Devuelve una fracción como `30000/1001` = 29,97. Ese `1001` es la razón de que "30 fps" casi nunca sea
30 exacto en material grabado en América.

---

## `-ss` antes o después de `-i`: la trampa clásica

```bash
# Rapido: busca en el contenedor antes de decodificar
ffmpeg -ss 44.1 -i entrada/clip-03.mp4 -t 5.8 -c:v libx264 -crf 20 -c:a aac salida.mp4

# Exacto pero lento: decodifica desde el inicio y descarta
ffmpeg -i entrada/clip-03.mp4 -ss 44.1 -t 5.8 -c:v libx264 -crf 20 -c:a aac salida.mp4
```

En ffmpeg moderno (5.x en adelante), `-ss` antes de `-i` **con recodificación** ya es preciso al
fotograma en la gran mayoría de los casos, y es mucho más rápido. Úsalo así.

Dos advertencias que sí importan:

- **Con `-c copy` (sin recodificar) el corte salta al fotograma clave más cercano**, y puede desplazarse
  hasta 2 segundos. Para cortes finos **siempre recodifica**. `-c copy` es para partir archivos grandes,
  no para montar.
- **`-t` es duración, `-to` es punto final.** Con `-ss` antes de `-i`, el comportamiento de `-to` cambió
  entre versiones de ffmpeg. Para no pensar: **usa siempre `-t` (duración)** y calcula la duración tú
  mismo como `fin - inicio`. Es la forma que nunca falla.

---

## La tabla de cortes: el formato canónico

Todo corte del proyecto vive en una sola tabla, y esa tabla es la fuente de verdad. Nada de números
sueltos en el chat.

```csv
bloque,texto,clip,inicio,fin,duracion,se_oye_antes,se_oye_despues
b01,"En Cusco hay una piedra famosa",clip-12,24.9,33.1,8.2,"[SILENCIO] se te olvido","[SILENCIO] bueno ya"
b02,"Vidrio reciclado. Todo.",clip-03,44.1,49.9,5.8,"a ver otra vez","[SILENCIO] perfecto corte"
b03,"Cada botella fue otra botella",clip-03,50.2,54.0,3.8,"todo","[RISA] quedo bien"
```

Reglas de la tabla:

- `duracion` siempre igual a `fin - inicio`. Si no cuadra, hay un error de dedo.
- `inicio` y `fin` con **un decimal**, en segundos, relativos al clip.
- `se_oye_antes` y `se_oye_despues` **obligatorias**. Sin ellas no se puede validar (módulo 16).
- Un `se_oye_despues` que arranca con conjunción o palabra a medias es una alerta roja.

Verificación aritmética inmediata:

```powershell
$csv = Import-Csv "C:\Users\user\Desktop\VIDEO-BOTELLA\analisis\cortes.csv"
foreach ($f in $csv) {
  $calc = [math]::Round([double]$f.fin - [double]$f.inicio, 2)
  $decl = [math]::Round([double]$f.duracion, 2)
  if ([math]::Abs($calc - $decl) -gt 0.05) {
    Write-Output ("DESCUADRE {0}: declara {1} s pero fin-inicio = {2} s" -f $f.bloque, $decl, $calc)
  }
}
$total = ($csv | ForEach-Object { [double]$_.duracion } | Measure-Object -Sum).Sum
Write-Output ("Duracion total del montaje: {0} s" -f [math]::Round($total,1))
```

Ese total es dato duro: te dice si el video va a durar 47 o 78 segundos **antes** de renderizar nada.

---

## Cómo pedirle cortes a un modelo sin ambigüedad

Plantilla de prompt lista para copiar:

```
Con base en la transcripcion que te pase de clip-03, dame el corte para el bloque
"de que esta hecha la botella".

FORMATO DE RESPUESTA (solo esto, nada mas):
inicio: <segundos con un decimal>
fin: <segundos con un decimal>
duracion: <fin menos inicio>
se_oye_antes: <las 5 palabras previas al inicio, literales>
se_oye_despues: <las 5 palabras posteriores al fin, literales>

REGLAS
- Los tiempos son en SEGUNDOS y relativos a clip-03. Nunca uses minuto:segundo.
- El clip dura 101.4 segundos. Ningun valor puede pasar de ahi.
- Deja 0.2 s de aire antes de la primera palabra y 0.3 s despues de la ultima.
- Si la frase que pido esta partida entre dos tomas, dilo y no inventes un corte.
```

Las dos líneas que evitan los errores caros: **"nunca uses minuto:segundo"** y **"el clip dura 101.4
segundos, ningún valor puede pasar de ahí"**. Darle la duración en el prompt es lo más barato que puedes
hacer.

---

## Errores comunes

- **Usar `minuto:segundo` en cualquier parte del flujo.** Es el origen del error de 1:29 → 128,3 s. Una
  sola unidad: segundos.
- **Pedir un tramo sin comprobar la duración del clip.** El error de 128–136 s en un clip de 101 s. La
  comprobación va antes del corte, siempre, y debe fallar ruidosamente.
- **Pedir solo el número, sin contexto de audio.** Un número solo no se puede verificar. Pide siempre
  `se_oye_antes` y `se_oye_despues`.
- **Cortar pegado a la palabra.** Sin aire, el final suena mocho aunque el número esté "bien".
- **Cortar con `-c copy` para cortes finos.** Salta al fotograma clave y te mueve el corte hasta 2 s.
- **Mezclar `-t` y `-to` sin tener claro cuál es cuál.** Usa siempre `-t` con la duración calculada.
- **Asumir que el fps es redondo.** 29,97 no es 30. En cortes largos la deriva se nota.
- **Dejar los números en el chat en vez de en una tabla.** Los números sueltos se contradicen; la tabla
  se valida.
- **No verificar que `duracion = fin - inicio`.** Un error de dedo en una columna produce un montaje que
  no cuadra y que cuesta media hora encontrar.
- **Corregir un corte y no actualizar la tabla.** A partir de ahí la tabla miente y todo lo que se
  construya sobre ella hereda el error.

---

## Checklist

- [ ] Todos los tiempos del proyecto están en segundos con un decimal, en cero lugares en `minuto:segundo`
- [ ] Cada corte tiene `clip`, `inicio`, `fin`, `duracion` en la tabla `analisis/cortes.csv`
- [ ] Cada corte tiene `se_oye_antes` y `se_oye_despues` con palabras literales
- [ ] Ningún `se_oye_despues` arranca con conjunción o palabra partida sin estar marcado como alerta
- [ ] Se comprobó con ffprobe que cada `fin` cabe dentro de la duración real de su clip
- [ ] Se verificó que `duracion = fin - inicio` en todas las filas
- [ ] Cada corte tiene aire de entrada (0,15–0,30 s) y de salida (0,25–0,50 s)
- [ ] Los cortes caen en pausa o en respiración, no en medio de una palabra
- [ ] Los cortes finos se hacen con recodificación, nunca con `-c copy`
- [ ] Se usó `-t` (duración) y no `-to`, para evitar diferencias entre versiones de ffmpeg
- [ ] Se conoce la duración total sumada del montaje antes de renderizar
- [ ] Si se le pidieron cortes a un modelo, el prompt incluía la duración real del clip y la regla de unidad

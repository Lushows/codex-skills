# 13 — Transcribir y marcar

## Qué resuelve

Convertir 10 minutos de audio en un documento de texto con tiempos, donde además ya están marcadas las
tomas falsas y los momentos de risa. De una sola pasada obtienes tres cosas que normalmente cuestan tres
trabajos distintos: **el contenido**, **la selección de tomas** y **el material cómico**.

Sin transcripción no hay montaje serio. Todo lo demás en esta skill — la minería, la selección, el mapa
de bloques, la validación de cortes — funciona sobre el texto. El video se monta leyendo, no mirando.

**Timecode** = la marca de tiempo de dónde ocurre algo. Aquí siempre en **segundos**, nunca en
`minuto:segundo`. La razón está en el módulo 15 y es un error que ya costó caro.

---

## Primero: abaratar la transcripción

El bruto de un rodaje son cientos de megabytes. Subir eso a un modelo es lento, caro y muchas veces ni
siquiera entra por límite de tamaño. Pero el modelo solo necesita **oír**, no ver.

Un dato real: **un clip de 80 MB se convirtió en 1 MB de audio** con este comando, sin perder nada de lo
que un transcriptor necesita.

```bash
ffmpeg -i entrada/clip-01.mp4 -vn -ac 1 -ar 16000 -c:a libmp3lame -b:a 48k analisis/audio/clip-01.mp3
```

Qué hace cada bandera y por qué no pierdes calidad útil:

| Bandera | Qué hace | Por qué está bien |
|---|---|---|
| `-vn` | quita el video | el transcriptor no mira |
| `-ac 1` | mezcla a **mono** (un solo canal) | la voz no es estéreo; dos canales es el doble de peso por nada |
| `-ar 16000` | remuestrea a **16 kHz** | el habla vive por debajo de 8 kHz. Es el estándar de reconocimiento de voz |
| `-b:a 48k` | 48 kilobits por segundo | a 16 kHz mono, 48k es holgado. Suena a teléfono, se entiende perfecto |

**Qué es un sample rate (kHz):** cuántas veces por segundo se mide el sonido. Más alto = más agudos
posibles. La música necesita 44,1 o 48 kHz. La voz humana inteligible cabe en 16 kHz de sobra. Bajar de
48 kHz a 16 kHz recorta el peso a un tercio sin tocar una sola palabra.

### Convertir todo el bruto de un golpe

```powershell
$proyecto = "C:\Users\user\Desktop\VIDEO-BOTELLA"
$destino  = Join-Path $proyecto "analisis\audio"
New-Item -ItemType Directory -Force -Path $destino | Out-Null

Get-ChildItem (Join-Path $proyecto "entrada") -Filter *.mp4 | Sort-Object Name | ForEach-Object {
  $out = Join-Path $destino ($_.BaseName + ".mp3")
  & ffmpeg -y -hide_banner -loglevel error -i $_.FullName -vn -ac 1 -ar 16000 -c:a libmp3lame -b:a 48k $out
  $mb = [math]::Round((Get-Item $out).Length / 1MB, 2)
  Write-Output ("{0} -> {1} MB" -f $_.Name, $mb)
}
```

### Si prefieres un solo archivo con todo el rodaje

A veces conviene transcribir todo de una vez para que el modelo vea la continuidad entre clips. Se
concatenan los audios y se guarda la tabla de dónde empieza cada clip:

```powershell
$proyecto = "C:\Users\user\Desktop\VIDEO-BOTELLA"
$audios   = Join-Path $proyecto "analisis\audio"
$lista    = Join-Path $audios "_lista.txt"

$lineas = Get-ChildItem $audios -Filter *.mp3 | Sort-Object Name | ForEach-Object { "file '$($_.FullName -replace '\\','/')'" }
[System.IO.File]::WriteAllLines($lista, $lineas, (New-Object System.Text.UTF8Encoding($false)))

& ffmpeg -y -hide_banner -f concat -safe 0 -i $lista -c copy (Join-Path $audios "_todo.mp3")
```

**Atención al detalle del BOM:** se usa `[System.IO.File]::WriteAllLines` con `UTF8Encoding($false)` y no
`Set-Content -Encoding utf8`. PowerShell 5.1 escribe UTF-8 **con BOM** (tres bytes invisibles al inicio),
y ffmpeg falla al leer una lista de concat con BOM con un error confuso. Es una de las trampas clásicas
(ver `109-ffmpeg-trampas-y-errores.md`).

Y guarda el desplazamiento de cada clip, o los timecodes del archivo unido no te sirven para nada:

```powershell
$acum = 0.0
Get-ChildItem $audios -Filter "clip-*.mp3" | Sort-Object Name | ForEach-Object {
  $d = [double](& ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 $_.FullName)
  [PSCustomObject]@{ clip=$_.BaseName; inicio_global=[math]::Round($acum,2); duracion=[math]::Round($d,2) }
  $acum += $d
} | Export-Csv (Join-Path $proyecto "analisis\offsets.csv") -NoTypeInformation -Encoding utf8
```

En la práctica, **transcribir clip por clip es más seguro**: los timecodes salen relativos al clip, que es
justo lo que necesitas para cortar. El archivo unido solo vale para leer la sesión completa de corrido.

---

## El prompt de transcripción

Este es el corazón del módulo. Se le pasa el audio a un modelo que lee sonido (Gemini, GPT con audio,
Whisper con post-proceso) junto con estas instrucciones. Cópialo tal cual y cambia el nombre del clip.

```
Te paso el audio de UN clip de rodaje llamado clip-01.
Transcribelo COMPLETO, palabra por palabra, en espanol de Colombia.

REGLAS DE TIEMPO
- Marca el tiempo en SEGUNDOS con un decimal, siempre. Nunca uses minuto:segundo.
- El tiempo es relativo al INICIO DE ESTE CLIP, no de la sesion.
- Formato de linea: [12.4] texto dicho aqui
- Una linea por frase o por pausa clara, no por parrafo.

REGLAS DE CONTENIDO
- Transcribe literal. No corrijas la gramatica, no completes frases, no quites muletillas.
  Si dijo "o sea, o sea, esto es", escribe "o sea, o sea, esto es".
- Si no entiendes una palabra, escribe [?] en su lugar. No adivines.
- No resumas nada. No agregues nada que no se haya dicho.

MARCAS OBLIGATORIAS
- >>TOMA FALSA  al inicio de la linea, cuando la persona se equivoca, se corta,
  se rie de si misma, dice "otra vez", "espera", "perdon", "lo repito",
  o cuando arranca una frase y la abandona.
- >>TOMA BUENA  al inicio de la linea, cuando arranca un intento que llega completo hasta el final.
- [RISA]        donde alguien se rie, incluyendo risas fuera de camara.
- [SILENCIO N]  cuando hay mas de 2 segundos sin voz, con N = segundos redondeados.
- [RUIDO]       donde hay un ruido fuerte que tapa la voz.
- [OTRA VOZ]    cuando habla alguien distinto al protagonista.

AL FINAL DEL DOCUMENTO
Agrega tres listas:
1. TOMAS BUENAS: segundo de inicio, segundo de fin, y la primera frase de cada una.
2. TOMAS FALSAS: segundo de inicio y por que fallo, en cuatro palabras.
3. MOMENTOS DE RISA: segundo, quien se rie, y que la provoco.
```

### Por qué este prompt hace tres trabajos en uno

- **Transcribe** → material para el guion y para los subtítulos.
- **Marca `>>TOMA FALSA` / `>>TOMA BUENA`** → la selección de tomas queda hecha (módulo 14). En un rodaje
  real de 16 clips esto arrojó **28 tomas falsas y 6 buenas** en una sola pasada. Sin eso, alguien tenía
  que ver 10 minutos con el dedo en la barra.
- **Marca `[RISA]`** → el catálogo de bloopers queda sembrado (módulo 18). Las risas son el índice del
  material cómico: donde alguien se rió, algo pasó.

Pedir las tres cosas juntas cuesta lo mismo que pedir solo la transcripción. Pedirlas en tres pasadas
cuesta el triple y las marcas quedan desalineadas entre sí.

---

## Cómo se ve el resultado

```markdown
# clip-12 — transcripcion

[0.0] >>TOMA FALSA Bueno, esta botella... no, espera.
[3.2] [RISA]
[4.8] >>TOMA BUENA Esta botella no es solo un empaque, es una decision de diseno.
[9.1] El relieve que ves aqui esta inspirado en la piedra de los doce angulos.
[14.0] [SILENCIO 3]
[17.2] >>TOMA FALSA O sea, en el Cusco hay una... como se llama... [?]
[22.5] [RISA] [OTRA VOZ] Se te olvido otra vez.
[24.9] >>TOMA BUENA En Cusco hay una piedra famosa con doce angulos perfectos, y de ahi salio esto.

## TOMAS BUENAS
- 4.8 a 13.8 — "Esta botella no es solo un empaque"
- 24.9 a 33.1 — "En Cusco hay una piedra famosa"

## TOMAS FALSAS
- 0.0 — arranca y se corta
- 17.2 — no recuerda el nombre

## MOMENTOS DE RISA
- 3.2 — el protagonista, se rie de su propio arranque
- 22.5 — alguien fuera de camara lo molesta
```

Nota lo que pasó en ese ejemplo: la joya (la piedra de los doce ángulos) está en el segundo 9,1, dentro
de una toma buena, pero la versión **mejor contada** está en el segundo 24,9, en la toma que vino después
de una falsa. Sin la transcripción completa, con las dos versiones a la vista, esa comparación no existe.

---

## Guardar y organizar las transcripciones

```
analisis/
  audio/
    clip-01.mp3
    clip-12.mp3
  transcripciones/
    clip-01.md
    clip-12.md
  transcripcion.md      <- concatenacion de todas, para leer de corrido
```

Concatenar todas para la lectura de la pasada 3 del módulo 12:

```powershell
$proyecto = "C:\Users\user\Desktop\VIDEO-BOTELLA"
$dir = Join-Path $proyecto "analisis\transcripciones"
$out = Join-Path $proyecto "analisis\transcripcion.md"
$sb = New-Object System.Text.StringBuilder
Get-ChildItem $dir -Filter *.md | Sort-Object Name | ForEach-Object {
  [void]$sb.AppendLine("")
  [void]$sb.AppendLine("=====================  " + $_.BaseName + "  =====================")
  [void]$sb.AppendLine((Get-Content $_.FullName -Raw))
}
[System.IO.File]::WriteAllText($out, $sb.ToString(), (New-Object System.Text.UTF8Encoding($false)))
Write-Output "Transcripcion unificada en $out"
```

---

## Verificar la transcripción antes de confiar en ella

Un modelo puede alucinar tiempos. Dos comprobaciones baratas antes de montar sobre esos números:

**1. Ningún timecode puede pasarse de la duración del clip.**

```powershell
$clip = "C:\Users\user\Desktop\VIDEO-BOTELLA\entrada\clip-12.mp4"
$txt  = "C:\Users\user\Desktop\VIDEO-BOTELLA\analisis\transcripciones\clip-12.md"
$dur  = [double](& ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 $clip)

$malos = Select-String -Path $txt -Pattern "\[(\d+\.?\d*)\]" -AllMatches |
  ForEach-Object { $_.Matches } |
  ForEach-Object { [double]$_.Groups[1].Value } |
  Where-Object { $_ -gt $dur }

if ($malos.Count -gt 0) {
  Write-Output ("ALERTA: {0} timecodes exceden la duracion real ({1} s): {2}" -f $malos.Count, [math]::Round($dur,2), ($malos -join ", "))
} else {
  Write-Output "Timecodes dentro de rango"
}
```

**2. Los timecodes deben ir en orden creciente.** Si una línea retrocede en el tiempo, el modelo se
perdió y hay que retranscribir ese tramo.

**3. Prueba de oído puntual.** Toma dos timecodes al azar, extrae esos 5 segundos y escúchalos:

```bash
ffmpeg -y -ss 24.9 -i entrada/clip-12.mp4 -t 5 -vn -c:a libmp3lame trabajo/prueba-24.9.mp3
```

Si lo que se oye no coincide con lo transcrito, todos los tiempos de ese clip están corridos y no se
puede montar sobre ellos.

---

## Costo real

Con audio a 16 kHz mono 48 kbps, 10 minutos de bruto pesan unos **3,6 MB**. Eso son centavos de dólar en
cualquier modelo que lea audio. Sin la conversión, esos mismos 10 minutos son 300–800 MB de video: lento,
caro, y en varios modelos ni siquiera se puede subir.

La conversión de audio no es una optimización menor. Es lo que hace que "transcribir el 100% del bruto"
sea una política sostenible en vez de un lujo.

---

## Errores comunes

- **Subir el video completo a transcribir.** 80 MB por clip cuando 1 MB basta. Extrae audio mono 16 kHz
  48 kbps primero, siempre.
- **Pedir timecodes en `minuto:segundo`.** Genera la ambigüedad que ya costó caro: "1:29" se leyó como
  129 segundos. Pide segundos y nada más. Ver módulo 15.
- **Transcribir con timecodes globales de la sesión y cortar con ellos sobre un clip individual.** Los
  tiempos son relativos al clip que transcribiste. Si uniste los audios, necesitas la tabla de offsets.
- **Dejar que el modelo corrija la gramática.** Un "o sea, o sea" que se limpió en la transcripción es un
  corte que después no cuadra con el audio real.
- **No pedir las marcas de toma falsa.** Es gratis pedirlas y ahorra la pasada completa de selección.
- **No pedir las marcas de risa.** Es el índice del material cómico y del arco de bloopers.
- **Confiar en los timecodes sin verificarlos.** Dos comprobaciones (rango y orden) más una prueba de
  oído puntual toman dos minutos y evitan un montaje entero corrido.
- **`Set-Content -Encoding utf8` para la lista de concat.** El BOM rompe ffmpeg. Usa
  `[System.IO.File]::WriteAllLines` con `UTF8Encoding($false)`.
- **Transcribir solo los clips que parecen buenos.** El sesgo que entierra la joya (módulo 12).
- **Borrar los `.mp3` de análisis al terminar.** Pesan poco y son la base de cualquier revisión posterior.

---

## Checklist

- [ ] Todo el bruto tiene su `.mp3` mono, 16 kHz, 48 kbps en `analisis/audio/`
- [ ] Se verificó que el peso bajó de cientos de MB a pocos MB
- [ ] Está transcrito el 100% de los clips, no una selección
- [ ] Todos los timecodes están en segundos con un decimal, nunca en `minuto:segundo`
- [ ] Los timecodes son relativos al clip, y si hay archivo unido existe `analisis/offsets.csv`
- [ ] La transcripción es literal: incluye muletillas, repeticiones y `[?]` donde no se entendió
- [ ] Cada clip tiene marcadas `>>TOMA FALSA` y `>>TOMA BUENA`
- [ ] Cada clip tiene marcados los `[RISA]`, `[SILENCIO N]`, `[RUIDO]`, `[OTRA VOZ]`
- [ ] Cada transcripción cierra con las tres listas: tomas buenas, tomas falsas, momentos de risa
- [ ] Se corrió la verificación de rango (ningún timecode excede la duración real del clip)
- [ ] Se verificó que los timecodes van en orden creciente
- [ ] Se hizo al menos una prueba de oído puntual por clip largo
- [ ] Existe `analisis/transcripcion.md` unificada para leer de corrido

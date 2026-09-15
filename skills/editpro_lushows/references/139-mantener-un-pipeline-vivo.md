# 139 — Mantener un pipeline vivo

## Qué resuelve

Que dentro de seis meses `.\edit.ps1 todo` siga funcionando. Sin drama, sin una tarde de arqueología, sin
descubrir que el modelo que usabas se apagó y nadie lo anotó.

Un pipeline no es un edificio: es un jardín. Nadie lo rompe a propósito. Se rompe porque **el mundo de
afuera se mueve**: ffmpeg saca versión, Node cambia de mayor, el modelo de IA cambia el formato de
respuesta, alguien mueve una carpeta, Windows actualiza algo.

Los cinco frentes, y este módulo cubre los cinco:

1. Congelar las versiones de las herramientas
2. Tener una prueba de humo que corre en menos de un minuto
3. Escribir las trampas donde se van a leer
4. Actualizar a propósito, de a una cosa
5. Dejarlo entendible para quien lo herede (incluido tú en seis meses)

---

## 1. Congelar y registrar las versiones

Lo que rompe un pipeline casi nunca es tu código. Es una versión.

### Registrar

Un archivo `ENTORNO.md` en la raíz, generado por script, no escrito a mano:

```powershell
# entorno.ps1 -- deja constancia de con que se hizo funcionar esto.
# Sin este archivo, cuando algo se rompa en seis meses no vas a poder ni comparar.

param([string]$Proyecto = (Get-Location).Path)

$lineas = @()
$lineas += "# ENTORNO -- generado el " + (Get-Date -Format "yyyy-MM-dd HH:mm")
$lineas += ""
$lineas += "Sistema: " + (Get-CimInstance Win32_OperatingSystem).Caption
$lineas += ""

$ffm = (& ffmpeg -version 2>&1 | Select-Object -First 1)
$lineas += "ffmpeg:  $ffm"
$lineas += "ffprobe: " + (& ffprobe -version 2>&1 | Select-Object -First 1)
$lineas += "node:    " + (& node --version)
$lineas += "PowerShell: " + $PSVersionTable.PSVersion.ToString()
$lineas += ""

# Los codificadores y filtros concretos que usa el pipeline. Si manana falta uno,
# el mensaje de ffmpeg no dice "te falta el filtro", dice algo mucho peor.
$lineas += "## Filtros y codecs que este pipeline necesita"
foreach ($f in @("libx264","aac","libass","afftdn","loudnorm","sidechaincompress","ebur128","freezedetect")) {
  $hay = (& ffmpeg -hide_banner -filters 2>&1 | Select-String -SimpleMatch $f) -ne $null
  if (-not $hay) { $hay = (& ffmpeg -hide_banner -encoders 2>&1 | Select-String -SimpleMatch $f) -ne $null }
  $lineas += ("- {0}: {1}" -f $f, $(if ($hay) { "presente" } else { "FALTA" }))
}

$lineas += ""
$lineas += "## Modelos de IA usados"
$lineas += "- transcripcion: (anotar nombre y version exacta)"
$lineas += "- imagen: (anotar nombre y version exacta)"
$lineas += "- musica: (anotar nombre y version exacta)"

$lineas | Out-File (Join-Path $Proyecto "ENTORNO.md") -Encoding utf8
Write-Output "ENTORNO.md actualizado."
```

### Congelar de verdad

| Herramienta | Cómo se congela |
|---|---|
| Node | `package.json` con `"engines": { "node": ">=20 <23" }` y `package-lock.json` en git |
| Dependencias de Node | versiones exactas, sin `^`, y `npm ci` en vez de `npm install` |
| ffmpeg | guardar el binario usado, o anotar la versión y no actualizar sin correr la prueba de humo |
| Modelos de IA | nombre **completo con versión** en un solo archivo de configuración, nunca "el último" |
| Fuentes tipográficas | copiadas dentro de `assets/fuentes/`, jamás dependiendo de las del sistema |

Esa última muerde más de lo que parece: un `.ass` que pide una fuente instalada en tu máquina se renderiza
distinto (o con la fuente de reemplazo) en cualquier otra. Las fuentes viajan con el proyecto.

Los modelos, en un solo sitio:

```js
// pipeline/modelos.mjs -- version exacta, nunca "el mas nuevo".
// Si esto dice "ultimo", el video de octubre no se parece al de agosto y nadie
// sabe por que. Actualizar aqui es una decision, no un accidente.
export const MODELOS = {
  transcripcion: { nombre: "modelo-audio-v3", desde: "2026-05-12" },
  imagen:        { nombre: "modelo-imagen-v4", desde: "2026-07-02" },
  musica:        { nombre: "modelo-musica-v2", desde: "2026-06-18" },
};
```

---

## 2. La prueba de humo

Lo más rentable de todo el módulo. Un **proyecto semilla** minúsculo que ejercita el pipeline entero en
menos de un minuto.

```
pruebas/semilla/
  entrada/
    clip-01.mp4      5 s, con voz, generado por script
    clip-02.mp4      4 s, sin audio (caso borde: el bloque de imagen)
  montaje.csv        3 bloques: video, imagen, negro
  esperado.json      duracion 8.4 s, 1080x1920, con audio
```

Los clips de prueba se **generan**, no se guardan: así no engordan el repositorio y siempre son iguales.

```powershell
# pruebas/generar-semilla.ps1 -- fabrica material sintetico para la prueba de humo.
# Sintetico y no real: pesa kilobytes, siempre es identico, y no depende de
# tener a mano el bruto de un cliente.

$dir = "pruebas\semilla\entrada"
New-Item -ItemType Directory -Force -Path $dir | Out-Null

# clip-01: patron de barras + tono de 440 Hz. Sirve para probar corte, escala y audio.
& ffmpeg -hide_banner -loglevel error -y `
  -f lavfi -i "testsrc2=size=1280x720:rate=30:duration=5" `
  -f lavfi -i "sine=frequency=440:duration=5:sample_rate=48000" `
  -c:v libx264 -crf 23 -pix_fmt yuv420p -c:a aac -b:a 128k `
  "$dir\clip-01.mp4"

# clip-02: SIN audio a proposito. Este caso borde tumbo el pipeline real una vez:
# el concat descuadraba porque un segmento no tenia pista de sonido.
& ffmpeg -hide_banner -loglevel error -y `
  -f lavfi -i "smptebars=size=1280x720:rate=30:duration=4" `
  -c:v libx264 -crf 23 -pix_fmt yuv420p "$dir\clip-02.mp4"

Write-Output "Semilla generada en $dir"
```

Y la prueba:

```powershell
# pruebas\humo.ps1 -- corre el pipeline entero sobre la semilla y compara con lo esperado.
# Se corre: antes de actualizar cualquier herramienta, despues de tocar cualquier
# paso, y el primer dia de cada mes. Cuesta 40 segundos.

param([switch]$Regenerar)

$raiz = "pruebas\semilla"
if ($Regenerar -or -not (Test-Path "$raiz\entrada\clip-01.mp4")) {
  & "pruebas\generar-semilla.ps1"
}

Remove-Item "$raiz\segmentos\*","$raiz\salida\*" -Force -ErrorAction SilentlyContinue

$env:PROYECTO = (Resolve-Path $raiz).Path
& node "pipeline\montar.mjs" 99
if ($LASTEXITCODE -ne 0) { Write-Output "HUMO: fallo el montaje."; exit 1 }

$video = "$raiz\salida\v99-corte.mp4"
$esperado = Get-Content "$raiz\esperado.json" | ConvertFrom-Json
$real = & ffprobe -v error -show_entries format=duration -show_entries stream=width,height,codec_type -of json $video | ConvertFrom-Json

$dur = [double]$real.format.duration
$v = $real.streams | Where-Object { $_.codec_type -eq "video" } | Select-Object -First 1
$hayAudio = ($real.streams | Where-Object { $_.codec_type -eq "audio" }).Count -gt 0

$fallos = 0
if ([math]::Abs($dur - $esperado.duracion) -gt 0.2) {
  Write-Output ("HUMO ROJO: duracion {0} s, se esperaba {1} s" -f [math]::Round($dur,2), $esperado.duracion)
  $fallos++
}
if ($v.width -ne $esperado.ancho -or $v.height -ne $esperado.alto) {
  Write-Output ("HUMO ROJO: {0}x{1}, se esperaba {2}x{3}" -f $v.width, $v.height, $esperado.ancho, $esperado.alto)
  $fallos++
}
if (-not $hayAudio) { Write-Output "HUMO ROJO: el resultado no tiene audio"; $fallos++ }

if ($fallos -eq 0) { Write-Output "HUMO OK: el pipeline sigue vivo."; exit 0 }
Write-Output ("HUMO: {0} fallos. NO actualices nada hasta arreglarlo." -f $fallos)
exit 1
```

**El valor real de la prueba de humo** no es encontrar errores. Es que te da permiso para actualizar
herramientas sin miedo: corres, actualizas, vuelves a correr. Si pasa, seguiste. Si no, sabes exactamente
qué actualización lo rompió.

---

## 3. `TRAMPAS.md`: donde vive lo que muerde

Un archivo en la raíz del proyecto, al lado del código, que responde una sola pregunta: **"¿qué me va a
morder y qué hago?"**.

No es documentación. Es una lista de cicatrices.

```markdown
# TRAMPAS -- VIDEO-BOTELLA

## ffmpeg
- `-ss` DESPUES de `-i` en bloques con voz. Antes corta al fotograma clave y parte palabras.
  Probado: con `-ss` antes, b05 entraba 0.4 s tarde y se comia "vidrio".
- El `concat` por copia exige que TODOS los segmentos tengan audio. clip-02 no tenia
  y el video salio 3 s mas corto sin ningun error. Por eso los bloques de imagen
  llevan `anullsrc`.
- En PowerShell hay que escapar las comas de `crop=` con backtick o el filtro se parte.

## PowerShell 5.1
- No existe `&&`. El encadenado va por `$LASTEXITCODE`.
- `Set-Content` escribe en la codificacion del sistema: siempre `-Encoding utf8`,
  o las tildes del .ass salen como basura.
- No redirigir `2>&1` de ffmpeg: envuelve la salida en objetos de error y rompe `$?`.

## Subtitulos
- La fuente vive en `assets/fuentes/`. Si el `.ass` pide una fuente instalada,
  en otra maquina se renderiza con otra y el texto se desborda.

## IA
- El modelo de transcripcion devuelve a veces mm:ss en vez de segundos cuando el
  clip pasa de 60 s. Por eso `validarSegmentos` compara contra la duracion real.
- Plan B si el API cae: medir cortes a mano con la onda de `analisis/ondas/`.

## Windows
- Ruta de proyecto corta. Con `C:\Users\user\Desktop\CLIENTES\...` se pasa de 260
  caracteres en los nombres de segmento y falla con "no se encuentra el archivo".
```

Regla: **cada vez que pierdas más de veinte minutos con algo, escribe la trampa antes de seguir.** Ese es
el momento en que lo entiendes mejor y en que menos ganas tienes de escribirlo. Escríbelo igual.

---

## 4. Actualizar a propósito

El error clásico: actualizar Windows, Node, ffmpeg y las dependencias en la misma tarde, y al día
siguiente algo falla sin saber qué fue.

El procedimiento, siempre igual:

```
1. Correr la prueba de humo.               Verde? Sigue. Roja? Arregla primero.
2. Actualizar UNA cosa.                    Una. No dos.
3. Correr la prueba de humo.
4. Verde   -> anotar en ENTORNO.md y CAMBIOS.md. Siguiente.
   Roja    -> revertir esa cosa. Anotar en TRAMPAS.md por que no se puede subir.
5. Correr un proyecto real completo antes de usarlo con un cliente.
```

Cuándo conviene actualizar:

| Situación | Decisión |
|---|---|
| Entre proyectos, con calma | sí, es el momento |
| Con una entrega mañana | **no**. Nunca |
| Porque salió una versión nueva | no, si lo que tienes funciona |
| Porque necesitas un filtro o modelo nuevo | sí, con prueba de humo antes y después |
| Porque el proveedor apaga el modelo que usas | sí, y con tiempo (avisan con semanas) |

Un `CAMBIOS.md` de tres líneas por entrada basta:

```markdown
## 2026-08-04
- ffmpeg 7.1 -> 7.2. Humo verde. Sin cambios visibles.
- Modelo de imagen v3 -> v4. Humo verde, pero el duotono queda mas contrastado:
  se bajo el parametro de `forzar-marca` de 0.85 a 0.78.
```

---

## 5. Que lo entienda quien lo herede

Incluido tú en seis meses, que no vas a recordar nada.

### El `README.md` de diez líneas

```markdown
# VIDEO-BOTELLA -- pipeline de edicion

Convierte los clips de `entrada/` en un video vertical de marca.

    .\edit.ps1 todo            corre el pipeline completo
    .\edit.ps1 montar -Ayuda   ayuda de cualquier paso

El montaje vive en `montaje.csv`. Para cambiar el video, se cambia esa tabla
y se corre `.\edit.ps1 montar`. NUNCA se ajusta un tiempo dentro de un script.

Requiere: ffmpeg y ffprobe en el PATH, Node 20+. Ver ENTORNO.md.
Antes de actualizar cualquier herramienta: `.\pruebas\humo.ps1`.
Lo que muerde: TRAMPAS.md.
```

Diez líneas. Si necesitas cuarenta, el pipeline es demasiado complicado.

### Git, aunque trabajes solo

Qué va y qué no:

```gitignore
# .gitignore
entrada/          el bruto pesa gigas y no cambia; respaldarlo aparte
segmentos/        reconstruible
trabajo/          taller
salida/           reconstruible
assets/generado-ia/*.png   pesado; se respalda aparte
!assets/generado-ia/*.prompt.txt   el prompt SI va: es lo unico irremplazable
!assets/generado-ia/*.meta.json
```

Va a git: los scripts, `montaje.csv`, `formatos.csv`, `TRAMPAS.md`, `ENTORNO.md`, `CAMBIOS.md`, `README.md`
y los prompts. Todo eso pesa kilobytes y **es el proyecto**. Lo demás son archivos.

### Los respaldos que sí importan

| Qué | Dónde | Cada cuánto |
|---|---|---|
| `entrada/` (el bruto) | disco externo o nube | al terminar el rodaje, una vez |
| El repositorio (scripts + tablas) | git remoto | en cada cambio |
| `assets/` (marca, música, generados) | nube | al cerrar el proyecto |
| `salida/entregas/` | donde vive lo publicado | al entregar |

`analisis/`, `segmentos/`, `trabajo/` y `salida/` intermedia no se respaldan: se reconstruyen. Esa es
justamente la ventaja de tener un pipeline.

---

## Revisión trimestral: quince minutos, cuatro veces al año

```
[ ] Correr la prueba de humo
[ ] Correr un proyecto viejo completo y comparar el resultado con el que se entregó
[ ] Actualizar ENTORNO.md
[ ] Revisar si algún modelo de IA cambió de versión o quedó marcado como obsoleto
[ ] Borrar los scripts que nadie corrió en el trimestre
[ ] Leer TRAMPAS.md entero (recuerda cosas que ya olvidaste)
[ ] Revisar analisis/costos.csv: ¿el costo por video se disparó?
```

La segunda línea es la que de verdad detecta la descomposición silenciosa: un proyecto viejo que hoy sale
distinto significa que algo cambió sin que nadie lo notara.

---

## Cómo mueren los pipelines (las cinco causas reales)

| Causa | Se previene con |
|---|---|
| Una actualización lo rompió y nadie supo cuál | prueba de humo + actualizar de a una cosa |
| El modelo de IA se apagó | versión anotada + plan B escrito |
| La persona que lo escribió se fue | README + TRAMPAS + comentarios con el porqué |
| Se llenó de excepciones hasta ser inservible | módulo `137`: podar lo que no aplica |
| Nadie lo corrió en tres meses y se pudrió en silencio | revisión trimestral |

Ninguna de las cinco es un problema técnico difícil. Las cinco son falta de mantenimiento.

---

## Errores comunes

- **No registrar las versiones de las herramientas.** Cuando algo se rompa, no vas a tener con qué comparar.
- **Apuntar a "el último modelo" en vez de a una versión exacta.** El video de octubre no se parece al de
  agosto y nadie sabe por qué.
- **Depender de fuentes instaladas en el sistema.** En otra máquina el texto se renderiza distinto o se
  desborda.
- **No tener prueba de humo.** Sin ella, cada actualización es una apuesta y prefieres no actualizar nunca.
- **Guardar clips reales como material de prueba.** Pesan, cambian y dependen de un cliente. Genera
  sintéticos.
- **Actualizar varias cosas a la vez.** Cuando algo falla, no sabes cuál fue.
- **Actualizar con una entrega encima.** Nunca. Se hace entre proyectos.
- **No escribir las trampas.** Vuelves a perder veinte minutos con lo mismo dentro de dos meses.
- **Escribir la trampa en un chat o en una nota suelta.** Va en `TRAMPAS.md`, al lado del código.
- **Meter `entrada/` y `salida/` en git.** El repositorio se vuelve inmanejable por unos archivos que ni
  siquiera cambian.
- **No versionar los prompts.** Las imágenes se pueden volver a pedir; el prompt perdido no vuelve.
- **Un README de cuarenta líneas.** Nadie lo lee. Si hacen falta cuarenta, simplifica el pipeline.
- **Dejar scripts que nadie corre.** Se rompen en silencio y confunden al siguiente que llegue.
- **No correr nunca un proyecto viejo.** Es la única forma de detectar que el pipeline cambió de resultado
  sin avisar.

---

## Checklist

- [ ] Existe `ENTORNO.md` generado por script, con versiones de ffmpeg, Node y PowerShell
- [ ] `ENTORNO.md` verifica que estén los filtros y códecs que el pipeline necesita
- [ ] Los modelos de IA están declarados con versión exacta en un solo archivo
- [ ] Las fuentes tipográficas viven dentro de `assets/fuentes/`, no en el sistema
- [ ] Existe un proyecto semilla y sus clips se generan por script, no se guardan
- [ ] La prueba de humo corre el pipeline entero en menos de un minuto
- [ ] La prueba de humo compara contra valores esperados y devuelve código de salida
- [ ] Existe `TRAMPAS.md` en la raíz y se actualiza cada vez que algo cuesta más de 20 minutos
- [ ] Cada paso de IA tiene su plan B escrito
- [ ] Las actualizaciones se hacen de a una y con prueba de humo antes y después
- [ ] Existe `CAMBIOS.md` con lo que se actualizó y qué efecto tuvo
- [ ] Existe `README.md` de diez líneas que dice cómo se corre y dónde vive el montaje
- [ ] Los scripts, las tablas y los prompts están en git; el bruto y las salidas no
- [ ] El bruto está respaldado fuera del proyecto
- [ ] Hay revisión trimestral y en ella se corre un proyecto viejo para comparar
- [ ] Los scripts que nadie corre se borran

# 19 — Mapa de bloques

## Qué resuelve

Convertir todo lo aprendido del bruto en **una sola tabla** que ya es el montaje. No un guion, no un
storyboard, no notas en un chat: una tabla con bloque, texto, clip, inicio, fin y duración.

La afirmación fuerte de este módulo, y la razón por la que existe: **la tabla ES el montaje.** Cuando la
tabla está completa y validada, armar el video es mecánica. Un script recorre las filas, corta y pega. Si
el resultado no gusta, se cambia la tabla y se vuelve a generar — no se toca el video.

Esto es lo que separa un proceso reproducible de un proceso artesanal donde nadie recuerda por qué el
corte del segundo 34 quedó así.

---

## Qué es un bloque

Un **bloque** es la unidad mínima de sentido del video: una idea, dicha o mostrada, que se sostiene sola.
No es un plano y no es una frase — es una unidad narrativa.

Un video de 60 segundos tiene típicamente **6 a 9 bloques**. Menos de 5 y se siente lento; más de 12 y no
se entiende nada.

```
b01  gancho         8.2 s
b02  contexto       5.8 s
b03  el dato        6.6 s
b04  proceso        7.1 s
b05  prueba         5.4 s
b06  objecion       6.0 s
b07  cierre         4.8 s
b08  blooper        4.2 s
                  ------
                   48.1 s
```

Ese total sumado es dato duro antes de renderizar. Si te da 48 y necesitas 60, sabes exactamente cuánto
material te falta y de qué tipo — no lo descubres en el render.

---

## Las columnas de la tabla

```csv
bloque,rol,texto,clip,inicio,fin,duracion,se_oye_antes,se_oye_despues,imagen,texto_pantalla,intencional,motivo_intencional,estado
```

| Columna | Qué lleva | Por qué está |
|---|---|---|
| `bloque` | `b01`, `b02`... | orden y referencia estable |
| `rol` | gancho, contexto, dato, proceso, prueba, objeción, cierre, blooper | la estructura narrativa, explícita |
| `texto` | lo que se dice, literal | para leer el video sin verlo |
| `clip` | `clip-12.mp4` | de dónde sale |
| `inicio` / `fin` | segundos con un decimal | el corte |
| `duracion` | `fin - inicio` | control aritmético y suma total |
| `se_oye_antes` / `se_oye_despues` | palabras literales del contexto | la compuerta del módulo 16 |
| `imagen` | `directo`, `punch-in`, `broll:clip-07@22.0`, `texto` | qué se ve mientras se oye |
| `texto_pantalla` | la palabra o frase que va en pantalla | el canal principal (módulo 40) |
| `intencional` / `motivo_intencional` | `si` + motivo | excepciones justificadas |
| `estado` | `ok`, `falta`, `debil`, `verificar` | qué está resuelto y qué no |

La columna `imagen` es la que convierte la tabla de guion a montaje: separa **lo que se oye** de **lo que
se ve**, que es la técnica del módulo 23 (voz continua, imagen picada).

---

## Cómo se llena: de arriba abajo, no de izquierda a derecha

El orden importa. Llenar fila por fila te lleva a montar en el orden del rodaje. Se llena por columnas:

### Paso 1 — Los roles primero, sin material

Escribe la estructura vacía. Solo la columna `rol`. Esto es decidir qué video vas a hacer.

```csv
bloque,rol
b01,gancho
b02,contexto
b03,el dato
b04,proceso
b05,prueba
b06,cierre
b07,blooper
```

Si no sabes qué roles poner, mira `32-estructuras-narrativas.md`. Pero decídelo **antes** de mirar el
material, porque si no, la estructura se la impone lo que sobró del rodaje.

### Paso 2 — Asignar joyas a roles

De las joyas del módulo 12 y las tomas elegidas del módulo 14, cada una va a un rol. Aquí es donde se
descubre que sobra material de un tipo y falta de otro. Marca `estado=falta` sin miedo: es información,
no fracaso.

### Paso 3 — Timecodes

Del módulo 15: `inicio`, `fin`, `duracion`, `se_oye_antes`, `se_oye_despues`. Con la duración del clip
comprobada antes.

### Paso 4 — Imagen

Para cada bloque decide qué se ve. Y aquí la pregunta clave: **¿la cara hablando aporta algo en este
bloque?** Si la respuesta es no, va b-roll o texto encima. Un video donde todos los bloques son `directo`
se siente como una videollamada.

Repartición sana en un video de 60 s:

| `imagen` | Cuántos bloques |
|---|---|
| `directo` | 2–3 (gancho, cierre, el momento emocional) |
| `punch-in` | 1–2 (cambia el plano sin cambiar el material) |
| `broll:...` | 2–4 (lo tangible: manos, producto, lugar) |
| `texto` | 1–2 (los datos, las cifras) |

### Paso 5 — Texto en pantalla

La palabra clave de cada bloque, no la frase completa. Ver `41-subtitulos-vs-palabras-clave.md`.

### Paso 6 — Pasar la compuerta

Módulo 16. Cero rojos. Después de eso, y solo después, se monta.

---

## Ejemplo real completo

```csv
bloque,rol,texto,clip,inicio,fin,duracion,se_oye_antes,se_oye_despues,imagen,texto_pantalla,intencional,motivo_intencional,estado
b01,gancho,"En Cusco hay una piedra famosa con doce angulos perfectos",clip-12,24.9,31.4,6.5,"[SILENCIO] se te olvido","y de ahi salio esto",broll:clip-04@3.0,"la piedra de los 12 angulos",,,ok
b02,el dato,"Y de ahi salio el relieve de esta botella",clip-12,31.4,35.2,3.8,"doce angulos perfectos","[SILENCIO] bueno ya",directo,,,,ok
b03,contexto,"Vidrio reciclado. Todo. Cada botella fue otra botella antes",clip-03,44.1,51.0,6.9,"a ver otra vez","[SILENCIO] perfecto",broll:clip-07@12.0,"100% reciclado",,,ok
b04,proceso,"Se hace a mano, una por una, aca en Tocancipa",clip-07,8.0,14.6,6.6,"[SILENCIO]","[RUIDO]",directo,"hecho a mano",,,ok
b05,prueba,"Nos tomo catorce meses y la primera version era horrible",clip-09,52.3,58.1,5.8,"la verdad","[RISA]",punch-in,"14 meses",,,verificar
b06,cierre,"Si te la tomas, mira el relieve. Ahi esta la historia",clip-15,31.2,36.0,4.8,"[SILENCIO]","[SILENCIO 4]",directo,,,,ok
b07,blooper,"El eucalip— el arbolito ese",clip-08,15.0,17.4,2.4,"a ver","perdon perdon",directo,,si,"blooper: corte en seco es el remate",ok

TOTAL: 36.8 s
```

Qué se lee en esa tabla sin ver un solo fotograma:

- **Dura 36,8 s.** Para un reel de 60 faltan ~23 s: hay que agregar 3 o 4 bloques, o alargar b-roll.
- **b05 está en `verificar`**: el dato "catorce meses" hay que confirmarlo con el cliente antes de
  publicarlo. Esa columna evita publicar una cifra inventada.
- **b02 arranca donde termina b01, en el mismo clip.** Es una frase encadenada partida en dos bloques
  para poder cambiar la imagen en la mitad. Eso es exactamente voz continua / imagen picada.
- **Hay 3 `directo`, 2 `broll`, 1 `punch-in`.** Repartición sana.
- **b07 es el único intencional**, con motivo escrito. Una sola excepción en todo el proyecto: bien.

---

## Generar el montaje desde la tabla

La tabla se ejecuta. Este script corta cada bloque, valida que quepa, y arma la lista de concatenación:

```powershell
param([string]$Proyecto = "C:\Users\user\Desktop\VIDEO-BOTELLA")

$mapa   = Join-Path $Proyecto "analisis\mapa-bloques.csv"
$cortes = Join-Path $Proyecto "trabajo\cortes"
New-Item -ItemType Directory -Force -Path $cortes | Out-Null

$lista = @()
$total = 0.0

Import-Csv $mapa | Where-Object { $_.estado -ne "falta" } | ForEach-Object {
  $src = Join-Path $Proyecto ("entrada\" + $_.clip)
  $dur = [double](& ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 $src)
  $ini = [double]$_.inicio
  $len = [double]$_.duracion

  if ($ini + $len -gt $dur) {
    throw ("{0}: pide hasta {1} s pero {2} dura {3} s" -f $_.bloque, ($ini+$len), $_.clip, [math]::Round($dur,2))
  }

  $out = Join-Path $cortes ($_.bloque + ".mp4")
  & ffmpeg -y -hide_banner -loglevel error -ss $ini -i $src -t $len `
    -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1" `
    -c:v libx264 -crf 20 -preset medium -pix_fmt yuv420p `
    -c:a aac -b:a 192k -ar 48000 -ac 2 $out

  $lista += "file '" + ($out -replace '\\','/') + "'"
  $total += $len
  Write-Output ("{0} -> {1} s" -f $_.bloque, $len)
}

$txt = Join-Path $cortes "_lista.txt"
[System.IO.File]::WriteAllLines($txt, $lista, (New-Object System.Text.UTF8Encoding($false)))

$final = Join-Path $Proyecto "salida\v01-corte-bruto.mp4"
& ffmpeg -y -hide_banner -f concat -safe 0 -i $txt -c copy $final
Write-Output ("MONTAJE: {0} bloques, {1} s -> {2}" -f $lista.Count, [math]::Round($total,1), $final)
```

Cuatro detalles que hacen que esto funcione y no falle en el paso de concatenar:

1. **Todos los bloques se normalizan igual**: misma resolución (`scale` + `crop`), mismo fps (`fps=30`),
   mismo SAR (`setsar=1`), mismo audio (48 kHz, estéreo). Sin eso, `concat -c copy` falla o produce
   audio desincronizado.
2. **La lista se escribe sin BOM** con `WriteAllLines` + `UTF8Encoding($false)`. Con BOM, ffmpeg da un
   error críptico.
3. **Las rutas usan `/`** aunque sea Windows: ffmpeg las prefiere y evita problemas de escape.
4. **`throw` si el tramo no cabe.** Falla ruidosamente en vez de producir basura silenciosa.

---

## La tabla como conversación con el cliente

Un beneficio que no es técnico: **la tabla se le puede mostrar al cliente antes de montar.** Le mandas
las columnas `bloque`, `rol`, `texto`, `duracion` y `texto_pantalla`, y le preguntas si esa es la
historia. Cinco minutos de lectura de su parte.

Es infinitamente más barato que mandarle un corte de 60 segundos y que te diga "no, es que yo quería que
empezara con lo del vidrio". Ver `182-rondas-de-notas.md`.

---

## Reordenar sin rehacer

Como el orden del video es el orden de las filas, probar una estructura distinta es reordenar filas y
volver a correr el script:

```powershell
$m = Import-Csv "C:\Users\user\Desktop\VIDEO-BOTELLA\analisis\mapa-bloques.csv"
$orden = @("b03","b01","b02","b04","b05","b06","b07")   # el vidrio de gancho, la piedra despues
$nuevo = foreach ($id in $orden) { $m | Where-Object { $_.bloque -eq $id } }
$nuevo | Export-Csv "C:\Users\user\Desktop\VIDEO-BOTELLA\analisis\mapa-bloques-v2.csv" -NoTypeInformation -Encoding utf8
```

Dos versiones estructurales en dos minutos. Eso es lo que compra tener el montaje como dato.

---

## Cuándo la tabla no basta

Sé honesto sobre los límites. La tabla resuelve **qué va, en qué orden y de dónde sale**. No resuelve:

- El **timing fino** de una transición o de un golpe de texto (eso se ajusta viendo).
- Si el **ritmo se siente** bien (módulo 20, y al final lo juzga un humano).
- Si la **música** pega con el tono.
- Si el **chiste da risa**.

La tabla te lleva al 85% del video con cero desperdicio. El 15% restante es oficio y oído, y hay que
verlo. Lo que no puede pasar es gastar el oficio en corregir errores que la tabla debió atrapar.

---

## Errores comunes

- **Montar sin tabla, directo en el editor.** Funciona para 30 segundos y colapsa a los 60. Y nadie
  recuerda por qué quedó así.
- **Llenar la tabla fila por fila.** Se llena por columnas: primero los roles, después el material.
- **Decidir la estructura mirando el material.** Entonces la estructura te la impone lo que sobró del
  rodaje. Los roles se deciden antes.
- **No poner la columna `rol`.** Sin ella la tabla es una lista de cortes, no una historia, y no se
  detecta que faltan gancho o cierre.
- **No poner la columna `imagen`.** El video queda todo en plano directo y se siente como videollamada.
- **Olvidar la columna `estado`.** Sin `falta` / `verificar` no sabes qué está resuelto, y publicas un
  dato sin confirmar.
- **No sumar las duraciones antes de montar.** Descubrir en el render que el video dura 36 s y necesitas
  60 es descubrirlo tarde.
- **Corregir el video sin corregir la tabla.** A partir de ahí la tabla miente y deja de servir.
- **Normalizar mal antes de concatenar.** Distinto fps, resolución o sample rate entre bloques rompe
  `concat -c copy` o desincroniza el audio.
- **Escribir la lista de concat con BOM.** `Set-Content -Encoding utf8` en PowerShell 5.1 lo mete y
  ffmpeg falla.
- **Montar antes de pasar la compuerta.** Se hereda el ciclo infinito del módulo 16.
- **Creer que la tabla hace el video sola.** Lleva al 85%. El resto es ver, oír y ajustar.

---

## Checklist

- [ ] Existe `analisis/mapa-bloques.csv` con todas las columnas del formato canónico
- [ ] Los roles se decidieron antes de asignar material
- [ ] Cada bloque tiene rol, texto literal, clip, inicio, fin y duración
- [ ] La suma de duraciones está calculada y comparada contra el objetivo del entregable
- [ ] Si falta metraje, está marcado con `estado=falta` y hay plan (regrabar, alargar b-roll, quitar bloque)
- [ ] Cada bloque tiene decidida su columna `imagen` y no todos son `directo`
- [ ] Cada bloque tiene su `texto_pantalla` o está marcado explícitamente como sin texto
- [ ] Los datos por confirmar están en `estado=verificar` y se le preguntaron al cliente
- [ ] Las excepciones `intencional=si` tienen motivo escrito
- [ ] La tabla pasó la compuerta del módulo 16 con cero rojos
- [ ] El cliente vio la tabla (bloque, rol, texto, duración) antes del primer render
- [ ] El script de montaje normaliza resolución, fps, SAR y audio en todos los bloques
- [ ] La lista de concat se escribe sin BOM y con rutas en `/`
- [ ] El script falla ruidosamente si un tramo no cabe en su clip
- [ ] Si se ajustó algo en el video, la tabla se actualizó para reflejarlo

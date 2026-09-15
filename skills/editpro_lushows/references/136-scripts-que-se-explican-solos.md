# 136 — Scripts que se explican solos

## Qué resuelve

Que cuando algo falle a las once de la noche, el script te diga qué pasó y cómo arreglarlo, en vez de
mandarte a cazar el problema.

La lección real, aprendida en el caso maestro y a costa de varias horas:

> **Un script que dice "FALLO" sin explicar por qué obliga a ir a cazar el problema.**
> **Un script que dice "se pidió hasta el segundo 136 pero el clip dura 101" se explica solo.**

Y la hermana de esa lección, para el código:

> **Los comentarios deben decir POR QUÉ, no QUÉ.**

Estas dos cosas no son estilo ni buenas maneras. Son lo que decide si el pipeline sigue vivo dentro de seis
meses o si lo abandonas porque "da errores raros".

---

## Anatomía de un mensaje de error útil

Un buen mensaje responde cuatro preguntas, en este orden:

| # | Pregunta | Ejemplo |
|---|---|---|
| 1 | **¿Qué** pasó | "el corte no cabe en el clip" |
| 2 | **¿Dónde** | "fila 7 de montaje.csv, bloque b05" |
| 3 | **Con qué números** | "se pidió hasta 136.0 s, clip-07.mp4 dura 101.4 s" |
| 4 | **Cómo se arregla** | "busca el bloque en otro clip o corrige la salida a 101.4 o menos" |

Los números son la parte que nadie pone y la que más sirve. Sin ellos, el mensaje es una opinión.

### La misma falla, tres veces

```
Nivel 0 -- inútil:
    Error: no se pudo procesar el bloque.

Nivel 1 -- mejor, pero todavía te manda a investigar:
    ERROR en b05: rango invalido.

Nivel 2 -- se explica solo:
    ROJO  fila 7  b05
          Se pidio de 51.3 a 136.0 s, pero clip-07.mp4 dura 101.4 s.
          ARREGLO: el tramo no existe. Corrige la columna salida (max 101.4)
                   o busca ese bloque en otro clip.
```

El nivel 2 se arregla en veinte segundos sin abrir nada. El nivel 0 cuesta media hora.

### Escribirlo, en Node

```js
// Mal: el mensaje no lleva el numero que causo el problema.
if (fin > duracion) throw new Error("rango invalido");

// Bien: el mensaje lleva QUE, DONDE, LOS NUMEROS y COMO se arregla.
if (fin > duracion) {
  throw new Error(
    `fila ${f.__linea} (${f.bloque}): se pidio hasta ${fin.toFixed(1)} s ` +
    `pero ${f.fuente} dura ${duracion.toFixed(1)} s.\n` +
    `  ARREGLO: baja la columna salida a ${duracion.toFixed(1)} o menos, ` +
    `o busca ese bloque en otro clip.`
  );
}
```

Y en PowerShell:

```powershell
if ($fin -gt $duracionClip) {
  $max = [math]::Round($duracionClip, 1)
  Write-Output ("ROJO  fila {0}  {1}" -f $fila, $bloque)
  Write-Output ("      Se pidio hasta {0} s, pero {1} dura {2} s." -f $fin, $clip, $max)
  Write-Output ("      ARREGLO: baja 'salida' a {0} o menos, o usa otro clip." -f $max)
  $rojos++
}
```

---

## La regla de la línea

Todo error que venga de una tabla **debe decir el número de línea del archivo**. Con 40 filas en el CSV,
"el bloque b05 falló" te obliga a buscarlo; "fila 7" te lleva de un salto.

```js
// Al leer el CSV se guarda el numero de linea REAL del archivo (cabecera + 1).
// Sin esto, todo error obliga a buscar la fila a ojo en un archivo de 40 lineas.
return lineas.map((l, i) => ({ ...parsear(l), __linea: i + 2 }));
```

---

## Comentarios que dicen POR QUÉ

Este es el comentario que no sirve:

```js
// Cortar de 51.3 a 58.4
spawnSync("ffmpeg", ["-i", clip, "-ss", "51.3", "-to", "58.4", destino]);
```

Ya se ve en el código que corta de 51.3 a 58.4. El comentario repite y ocupa espacio.

Este es el comentario que salva el proyecto:

```js
// 58.4 exacto: en 57.7 cortaba "caracteristicas"; en 58.5 entra "Listo, cortemos esa"
spawnSync("ffmpeg", ["-i", clip, "-ss", "51.3", "-to", "58.4", destino]);
```

Ahora el número tiene historia. Nadie lo va a "optimizar" a 57.7 dentro de tres semanas creyendo que es
un valor arbitrario.

### La prueba del comentario

Antes de escribir un comentario, pregúntate: **¿esto se ve leyendo el código?**

- Si la respuesta es sí, no lo escribas (o reescribe el código para que se vea mejor).
- Si la respuesta es no, escríbelo, y que empiece por el porqué.

### Los cinco porqués que sí hay que escribir

| Tipo | Ejemplo real del pipeline |
|---|---|
| **Un número mágico** | `// -18 dB: a -15 la musica tapaba la voz en el bloque del dato` |
| **Una decisión contraintuitiva** | `// -ss va DESPUES de -i aunque sea mas lento: antes corta al keyframe y parte palabras` |
| **Un rodeo** | `// Se escribe a .tmp y se renombra porque un ffmpeg cortado deja un mp4 truncado que la cache da por bueno` |
| **Una trampa de la herramienta** | `// PowerShell 5.1 no tiene && ; el encadenado va por codigo de salida` |
| **Algo que ya se intentó y falló** | `// Probado con NVENC: 3x mas rapido pero la calidad varia entre corridas. Master en x264` |

El quinto es el más valioso y el que casi nadie escribe. Un comentario que dice "esto ya se intentó y no
funcionó, por esto" evita que la misma persona lo vuelva a intentar en seis meses.

---

## Salvaguardas: fallar temprano y en el sitio correcto

Una **salvaguarda** es una comprobación al principio del script que evita un fallo confuso más adelante.
El principio: **fallar en el segundo 1 con un mensaje claro es infinitamente mejor que fallar en el
minuto 8 con un mensaje del codificador.**

Las seis que todo paso del pipeline debería tener:

```powershell
# montar.ps1 -- salvaguardas antes de tocar nada.

# 1. Herramientas externas
foreach ($h in @("ffmpeg","ffprobe")) {
  if (-not (Get-Command $h -ErrorAction SilentlyContinue)) {
    Write-Output "FALTA $h en el PATH."
    Write-Output "ARREGLO: winget install Gyan.FFmpeg  y abre una consola nueva."
    exit 1
  }
}

# 2. Insumos
if (-not (Test-Path $tabla)) {
  Write-Output "NO EXISTE montaje.csv en $Proyecto"
  Write-Output "ARREGLO: corre  .\edit.ps1 cortes  para generarla."
  exit 1
}

# 3. Forma de los insumos: mejor detectar la columna que falta ahora que
#    descubrir a mitad del render que 'inserto' venia vacia en todas las filas.
$cab = (Get-Content $tabla -TotalCount 1) -split ","
foreach ($col in @("bloque","tipo","fuente","entrada","salida")) {
  if ($cab -notcontains $col) {
    Write-Output ("A montaje.csv le falta la columna '{0}'." -f $col)
    Write-Output ("Columnas encontradas: {0}" -f ($cab -join ", "))
    exit 1
  }
}

# 4. Espacio en disco: un render que muere por disco lleno deja un mp4 a medias
#    y un mensaje de ffmpeg que no menciona el disco.
$libreGB = (Get-PSDrive ($Proyecto[0])).Free / 1GB
if ($libreGB -lt 5) {
  Write-Output ("Quedan {0} GB libres. Un render vertical de 60 s con segmentos pide ~3 GB." -f [math]::Round($libreGB,1))
  Write-Output "ARREGLO: borra trabajo\ o libera espacio antes de seguir."
  exit 1
}

# 5. No pisar lo entregado sin permiso
if ((Test-Path $destinoFinal) -and -not $Forzar) {
  Write-Output ("YA EXISTE {0}. No se pisa." -f $destinoFinal)
  Write-Output "ARREGLO: sube el numero de version, o pasa -Forzar si de verdad quieres reemplazarlo."
  exit 1
}

# 6. Modo simulacion: imprime lo que haria sin hacerlo.
if ($Simular) { Write-Output "SIMULACION: no se codifica nada." }
```

### El modo simulación

Es la salvaguarda más subestimada. `-Simular` (en inglés *dry run*) imprime lo que el script haría sin
hacerlo. Sirve para revisar un lote de 30 renders **antes** de gastar 40 minutos de CPU.

```js
const SIMULAR = process.argv.includes("--simular");

function correrFfmpeg(args, contexto) {
  if (SIMULAR) { console.log(`  [simulado] ffmpeg ${args.join(" ")}`); return; }
  // ...
}
```

---

## Nunca tragarse un error en silencio

El patrón que más daño hace en un pipeline:

```js
// MAL: si ffmpeg falla, el catch se lo come y el pipeline sigue como si nada.
// El video sale sin ese bloque y nadie se entera hasta que lo ve un cliente.
try { correrFfmpeg(args, bloque); } catch (e) { console.log("no se pudo, sigo"); }
```

Lo correcto es decidir **explícitamente** entre dos comportamientos, y decirlo:

```js
try {
  correrFfmpeg(args, bloque);
} catch (e) {
  if (MODO_LOTE) {
    // En lote, un elemento que falla no tumba los otros 49. Pero se anota,
    // se cuenta, y el proceso termina con codigo distinto de 0.
    fallidos.push({ bloque: f.bloque, linea: f.__linea, error: e.message });
    console.log(`FALLO ${f.bloque} (fila ${f.__linea}): ${e.message}`);
  } else {
    // En un montaje unico, seguir sin un bloque produce un video incompleto
    // que parece bueno. Se para.
    throw e;
  }
}
```

Regla: **un error suprimido tiene que dejar rastro contable.** Si no se cuenta y no cambia el código de
salida, es como si no hubiera pasado — y eso es exactamente lo peligroso.

---

## Códigos de salida y encadenado

| Código | Significado en este pipeline |
|---|---|
| `0` | todo bien |
| `1` | fallo de contenido (compuerta en rojo, insumos malos, error de datos) |
| `2` | fallo de entorno (falta ffmpeg, falta disco, falta una variable) |

Separar 1 de 2 sirve: el 1 lo arreglas tú editando la tabla; el 2 lo arregla instalando algo. Con esa
distinción, un lote puede reintentar los `2` y no los `1`.

En PowerShell 5.1 **no existe `&&`**. El encadenado va así:

```powershell
.\edit.ps1 validar-cortes
if ($LASTEXITCODE -eq 0) { .\edit.ps1 montar }
```

---

## Ayuda dentro del propio script

Si hay que abrir el archivo para saber cómo se usa, el script está incompleto.

```powershell
param([switch]$Ayuda, [switch]$Simular, [switch]$Forzar, [int]$Version = 1)

if ($Ayuda) {
  Write-Output @"
montar.ps1 -- arma el video a partir de montaje.csv

  -Version <n>   numero de version de salida (default 1) -> salida\v01-corte.mp4
  -Simular       imprime lo que haria, sin codificar
  -Forzar        rehace los segmentos aunque la cache los tenga, y pisa la salida
  -Ayuda         esto

Ejemplos:
  .\montar.ps1 -Version 6
  .\montar.ps1 -Simular

Requiere: ffmpeg y ffprobe en el PATH, montaje.csv en la raiz del proyecto.
"@
  exit 0
}
```

---

## Un registro que sirva

Cada corrida deja un archivo en `trabajo/logs/` con fecha en el nombre. No para leerlo siempre, sino para
el día que alguien pregunte "¿qué pasó el jueves?".

```powershell
$log = Join-Path $Proyecto ("trabajo\logs\montar-{0}.txt" -f (Get-Date -Format "yyyy-MM-dd-HHmmss"))
New-Item -ItemType Directory -Force -Path (Split-Path $log) | Out-Null
Start-Transcript -Path $log | Out-Null
# ... el trabajo ...
Stop-Transcript | Out-Null
```

Qué registrar: versión de ffmpeg, tabla usada, cada bloque con su decisión (caché o render), tiempos y
resultado final. Con eso se depura casi cualquier cosa sin volver a reproducirla.

---

## Errores comunes

- **Mensajes sin números.** "Duración inválida" no dice nada; "se pidió 136.0 s, el clip dura 101.4 s" se
  arregla solo.
- **Errores que no dicen la fila.** Con 40 filas, el bloque no basta.
- **Comentarios que repiten el código.** `// cortar de 51.3 a 58.4` encima de un comando que corta de 51.3
  a 58.4 es ruido.
- **Números mágicos sin porqué.** El `-18 dB` de la música sin comentario se va a "corregir" y va a tapar
  la voz.
- **No escribir lo que ya se intentó y falló.** Garantiza que alguien lo intente otra vez.
- **`catch` que solo imprime "no se pudo".** El error se traga, el pipeline sigue, y el defecto aparece en
  el video final.
- **Fallar en el minuto 8 por algo que se podía comprobar en el segundo 1.** Todas las salvaguardas van
  arriba.
- **No tener modo simulación.** Cada revisión de un lote grande cuesta el lote entero.
- **Pisar la salida sin avisar.** Un `-y` alegre borra la versión que el cliente ya aprobó.
- **Un solo código de salida para todo.** No se puede distinguir "arregla la tabla" de "instala ffmpeg".
- **No poder ver cómo se usa el script sin abrirlo.** `-Ayuda` cuesta diez líneas.
- **Redirigir `2>&1` de un ejecutable nativo en PowerShell 5.1.** Envuelve la salida en objetos de error y
  rompe `$?` aunque el comando haya ido bien.

---

## Checklist

- [ ] Todo mensaje de error dice qué pasó, dónde, con qué números y cómo se arregla
- [ ] Los errores que vienen de una tabla incluyen el número de línea del archivo
- [ ] Ningún comentario repite lo que el código ya dice
- [ ] Todo número mágico tiene un comentario con su porqué
- [ ] Está escrito lo que ya se intentó y no funcionó, con el motivo
- [ ] El script comprueba las herramientas externas antes de empezar
- [ ] El script comprueba que existan los insumos y que tengan las columnas esperadas
- [ ] El script comprueba el espacio en disco antes de un render largo
- [ ] Nada pisa una salida existente sin `-Forzar`
- [ ] Existe modo `-Simular` que imprime sin ejecutar
- [ ] Ningún `catch` se traga un error sin contarlo y sin cambiar el código de salida
- [ ] Los códigos de salida distinguen fallo de contenido (1) de fallo de entorno (2)
- [ ] El encadenado usa el código de salida, no `&&` (que no existe en PowerShell 5.1)
- [ ] Existe `-Ayuda` con uso, opciones, ejemplos y requisitos
- [ ] Cada corrida deja un registro con fecha en `trabajo/logs/`

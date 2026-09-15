# 130 — Diseñar un pipeline de edición

## Qué resuelve

Que editar el próximo video no cueste lo mismo que costó este. Un **pipeline** (tubería) es una cadena
de pasos donde cada paso lee archivos de disco, hace una sola cosa, y escribe archivos de disco. Nada
vive en tu cabeza, nada vive "en el programa abierto". Todo vive en carpetas y en tablas.

La diferencia práctica: un montaje artesanal se hace una vez y se muere. Un pipeline se corre otra vez
mañana con material distinto, o con el mismo material y una decisión distinta, y tarda minutos.

Este módulo es el mapa del bloque 13. Los nueve módulos siguientes desarrollan cada pieza.

---

## El caso maestro: el pipeline que se construyó y funcionó

Todo este bloque se apoya en un proyecto real (`VIDEO-BOTELLA`, un video vertical de marca de ~50 s
armado desde 14 clips en bruto). Estos son los doce comandos que quedaron, en el orden en que corren:

| # | Comando | Qué hace | Entra | Sale |
|---|---|---|---|---|
| 1 | `analizar` | ffprobe de cada clip + hoja de contactos de 20 fotogramas + onda de audio | `entrada/` | `analisis/ficha-tecnica.json`, `analisis/hojas-contacto/`, `analisis/ondas/` |
| 2 | `transcribir` | audio a texto con timecodes usando un modelo que lee audio; marca tomas falsas y risas | `entrada/` | `analisis/transcripcion.md`, `analisis/segmentos.json` |
| 3 | `cortes` / `medir-uno` | tiempos exactos de entrada y salida al décimo de segundo | `analisis/segmentos.json` | `analisis/cortes.csv` |
| 4 | `validar-cortes` | **la compuerta**: revisa TODOS los cortes antes de montar y propone arreglos | `analisis/cortes.csv` | informe + código de salida 0/1 |
| 5 | `subtitulos` | genera `.ass` con animación de golpe palabra por palabra | `analisis/cortes.csv` | `trabajo/subtitulos/*.ass` |
| 6 | `limpiar-voz` | cadena de 9 módulos de audio sobre la voz | `entrada/` | `trabajo/voz/*.wav` |
| 7 | `generar-ilustracion` / `generar-recorte` | arte de marca con IA usando los archivos de marca como referencia | prompt + `assets/marca/` | `assets/generado-ia/*.png` |
| 8 | `forzar-marca` | duotono que obliga cualquier fuente a la paleta | cualquier imagen o clip | `trabajo/marcado/` |
| 9 | `generar-musica` | música original | prompt + duración | `assets/musica/*.wav` |
| 10 | `montar` | **la línea de tiempo**: una tabla de bloques; se cambia un número y se reconstruye el video entero | `montaje.csv` + todo lo anterior | `salida/vNN-corte.mp4` |
| 11 | `musicalizar` | mezcla con ducking | video + música | `salida/vNN-mezcla.mp4` |
| 12 | `verificar` | transcribe el resultado final y reporta defectos | `salida/*.mp4` | informe |

Dos de esos doce son los que cambian el juego: **`validar-cortes`** (nada defectuoso llega al render) y
**`montar`** (el montaje es una tabla, no un archivo binario). Los demás son trabajo honesto.

---

## La regla de oro: cada paso deja rastro en disco

Un paso del pipeline es válido si cumple tres cosas:

1. **Lee de disco, escribe a disco.** Nada se pasa "en memoria" entre pasos. Si `transcribir` no deja un
   archivo, `cortes` no puede correr solo, y ya perdiste la mitad del valor.
2. **Se puede correr solo.** Sin haber corrido los anteriores en la misma sesión. Si los insumos existen,
   corre.
3. **Correrlo dos veces da lo mismo.** Esto se llama **idempotencia**: repetir la operación no cambia el
   resultado ni rompe nada. Si `montar` la segunda vez pega el video encima del anterior y duplica
   segmentos, el paso está mal escrito.

Consecuencia útil: puedes borrar `trabajo/` entero y reconstruirlo. Si no puedes, hay algo que solo existe
ahí y no está en ninguna tabla.

---

## Las cinco fases y qué se automatiza en cada una

Los doce comandos se agrupan en cinco fases. La columna que importa es la última.

| Fase | Comandos | Qué se automatiza bien | Qué sigue siendo humano |
|---|---|---|---|
| **A. Leer** | `analizar`, `transcribir` | todo: medir duración, fps, códec, sacar fotogramas, transcribir | nada. Es 100% máquina |
| **B. Decidir** | `cortes`, `medir-uno` | proponer tiempos, calcular duraciones, detectar silencios | **elegir la toma buena.** La máquina propone, tú apruebas |
| **C. Blindar** | `validar-cortes` | todo: las siete reglas del módulo 16 | juzgar las excepciones intencionales |
| **D. Producir** | `subtitulos`, `limpiar-voz`, `generar-*`, `forzar-marca`, `generar-musica` | todo lo repetible: cadena de audio, duotono, `.ass` | **el gusto**: qué ilustración sirve, qué música pega |
| **E. Armar y probar** | `montar`, `musicalizar`, `verificar` | todo el render y toda la medición | mirar el resultado una vez, completo, con audio |

Ese patrón se repite en cualquier pipeline serio: **lo aburrido y medible se automatiza; lo que requiere
gusto se le presenta al humano ya masticado, para que decida rápido.** El módulo `137` desarrolla dónde
está exactamente esa frontera.

---

## El despachador: un solo punto de entrada

No quieres acordarte de doce nombres de script. Quieres un comando y un verbo.

`edit.ps1`, en la raíz del proyecto:

```powershell
# edit.ps1 -- punto de entrada unico del pipeline.
# Uso:  .\edit.ps1 analizar
#       .\edit.ps1 montar -Version 3
# Por que un despachador y no doce scripts sueltos: para que el orden de las fases
# viva en un solo archivo y no en la memoria de quien lo corre.

param(
  [Parameter(Mandatory=$true, Position=0)]
  [ValidateSet("analizar","transcribir","cortes","medir-uno","validar-cortes",
               "subtitulos","limpiar-voz","generar-ilustracion","generar-recorte",
               "forzar-marca","generar-musica","montar","musicalizar","verificar","todo")]
  [string]$Comando,

  [Parameter(ValueFromRemainingArguments=$true)]
  $Resto
)

$raiz = Split-Path -Parent $MyInvocation.MyCommand.Path
$pasos = Join-Path $raiz "pipeline"

# Salvaguarda 1: sin ffmpeg no hay nada que hacer. Fallar aqui, con mensaje claro,
# es mejor que fallar dentro del paso 8 con "el sistema no encuentra el archivo".
if (-not (Get-Command ffmpeg -ErrorAction SilentlyContinue)) {
  Write-Output "FALTA ffmpeg en el PATH."
  Write-Output "ARREGLO: instala con  winget install Gyan.FFmpeg  y abre una consola nueva."
  exit 1
}

function Correr([string]$nombre) {
  $ps1 = Join-Path $pasos "$nombre.ps1"
  $mjs = Join-Path $pasos "$nombre.mjs"

  if (Test-Path $ps1) {
    & $ps1 @Resto
  } elseif (Test-Path $mjs) {
    & node $mjs @Resto
  } else {
    Write-Output ("NO EXISTE el paso '{0}'. Busque: {1} y {2}" -f $nombre, $ps1, $mjs)
    exit 1
  }
  return $LASTEXITCODE
}

if ($Comando -eq "todo") {
  # El orden esta aqui y en ningun otro lado. Si una fase falla, se para:
  # seguir montando con cortes invalidos es el error mas caro del oficio.
  $secuencia = @("analizar","transcribir","cortes","validar-cortes",
                 "subtitulos","limpiar-voz","montar","musicalizar","verificar")
  foreach ($p in $secuencia) {
    Write-Output ""
    Write-Output ("=== {0} ===" -f $p)
    $codigo = Correr $p
    if ($codigo -ne 0) {
      Write-Output ("SE DETUVO EN '{0}' (codigo {1}). No se sigue." -f $p, $codigo)
      exit $codigo
    }
  }
  Write-Output ""
  Write-Output "PIPELINE COMPLETO."
  exit 0
}

exit (Correr $Comando)
```

Tres cosas de este script no son adorno:

- **`ValidateSet`** hace que `.\edit.ps1 montr` falle al instante con la lista de comandos válidos, en vez
  de decir "no encuentro el archivo".
- **La verificación de `ffmpeg`** ocurre una vez, arriba, no repetida en doce scripts.
- **`todo` se detiene al primer código distinto de 0.** En PowerShell 5.1 no existe `&&`; el encadenado
  se hace con el código de salida, como aquí, o con `paso1.ps1; if ($?) { paso2.ps1 }`.

---

## Anatomía de un paso bien hecho

Cualquiera de los doce tiene la misma forma. Ejemplo mínimo en Node (`pipeline/analizar.mjs`):

```js
// analizar.mjs -- ficha tecnica de cada clip de entrada/.
// Sale a analisis/ficha-tecnica.json. Corre solo, no depende de pasos previos.

import { readdirSync, existsSync, mkdirSync, writeFileSync } from "node:fs";
import { spawnSync } from "node:child_process";
import { join } from "node:path";

const RAIZ = process.env.PROYECTO || process.cwd();
const ENTRADA = join(RAIZ, "entrada");
const ANALISIS = join(RAIZ, "analisis");

if (!existsSync(ENTRADA)) {
  console.log(`NO EXISTE la carpeta ${ENTRADA}.`);
  console.log("ARREGLO: crea la estructura con el script del modulo 10 y copia el bruto ahi.");
  process.exit(1);
}
mkdirSync(ANALISIS, { recursive: true });

function ficha(archivo) {
  const r = spawnSync("ffprobe", [
    "-v", "error",
    "-show_entries", "format=duration,size,bit_rate",
    "-show_entries", "stream=codec_type,codec_name,width,height,r_frame_rate,sample_rate,channels",
    "-of", "json", archivo,
  ], { encoding: "utf8" });

  if (r.status !== 0) {
    // El mensaje lleva el archivo Y lo que dijo ffprobe. Ver modulo 136.
    throw new Error(`ffprobe fallo en ${archivo}:\n${r.stderr.trim()}`);
  }
  return JSON.parse(r.stdout);
}

const clips = readdirSync(ENTRADA).filter((f) => /\.(mp4|mov|mkv|m4v)$/i.test(f)).sort();
if (clips.length === 0) {
  console.log(`La carpeta ${ENTRADA} no tiene videos (.mp4 .mov .mkv .m4v).`);
  process.exit(1);
}

const salida = {};
for (const c of clips) {
  const j = ficha(join(ENTRADA, c));
  const v = j.streams.find((s) => s.codec_type === "video") || {};
  const a = j.streams.find((s) => s.codec_type === "audio") || {};
  salida[c] = {
    duracion: Number(j.format.duration),
    ancho: v.width, alto: v.height,
    fps: v.r_frame_rate,
    codec_video: v.codec_name,
    codec_audio: a.codec_name || null,
    canales: a.channels || 0,
    tiene_audio: Boolean(a.codec_name),
  };
  console.log(
    `${c.padEnd(16)} ${salida[c].duracion.toFixed(2)} s  ` +
    `${v.width}x${v.height}  ${v.r_frame_rate}  audio: ${salida[c].tiene_audio ? "si" : "NO"}`
  );
}

writeFileSync(join(ANALISIS, "ficha-tecnica.json"), JSON.stringify(salida, null, 2), "utf8");
console.log(`\nOK ${clips.length} clips -> analisis/ficha-tecnica.json`);
```

La forma, siempre: **comprobar insumos → fallar temprano con arreglo → procesar → escribir a disco →
imprimir un resumen que se pueda leer de un vistazo.**

---

## Cómo empezar pequeño (y no construir un monstruo inútil)

La tentación es diseñar los doce pasos de una. No lo hagas. El pipeline del caso maestro no se diseñó:
**se sedimentó**, en este orden:

1. Primero se hizo **un video entero a mano**, con comandos sueltos de ffmpeg pegados en la consola.
2. El segundo video repitió los mismos comandos. Ahí se guardó `analizar` en un archivo, porque ya se
   había escrito dos veces.
3. El tercero reveló el dolor real: los cortes con palabras partidas y los cinco renders seguidos. De ahí
   nació `validar-cortes`, que es el paso que más valor dio y que nadie habría diseñado desde el escritorio.
4. `montar` con tabla llegó al cuarto, cuando el `filter_complex` a mano se volvió imposible de tocar.
5. Los pasos de IA (`generar-ilustracion`, `generar-musica`) llegaron de últimos porque son los menos
   repetibles.

**La regla de las tres veces:** no automatices nada que no hayas hecho a mano tres veces. La primera vez
no sabes qué haces. La segunda crees que sabes. La tercera ya viste las excepciones — y las excepciones
son lo que hace que un script sirva o estorbe.

**El orden de prioridad para automatizar**, cuando ya tienes varias opciones:

| Prioridad | Criterio | Ejemplo del caso |
|---|---|---|
| 1 | Lo que **evita rehacer trabajo** | `validar-cortes`: ahorró 5 renders de 8 minutos |
| 2 | Lo que se hace **en cada video sin excepción** | `analizar`, `limpiar-voz` |
| 3 | Lo que es **largo y mecánico** | `subtitulos` palabra por palabra: a mano son 2 horas |
| 4 | Lo que **cambia mucho durante la edición** | `montar`: se corre 15 veces por proyecto |
| 5 | Lo que se hace **una vez por proyecto y ya** | portada, metadatos: casi no vale la pena |

---

## Cuánto cuesta y cuánto devuelve

Números del caso maestro, medidos, no estimados:

| Paso | Tiempo a mano | Tiempo automatizado | Veces por proyecto |
|---|---|---|---|
| `analizar` (14 clips) | 25 min | 40 s | 1 |
| `transcribir` | 90 min | 4 min | 1 |
| `cortes` | 60 min | 12 min (IA propone, humano aprueba) | 2–3 |
| `validar-cortes` | no se hacía | 3 s | 5–10 |
| `subtitulos` | 120 min | 20 s | 3–4 |
| `limpiar-voz` | 30 min | 1 min | 1–2 |
| `montar` | 45 min por versión | 6 min | 10–15 |
| `verificar` | 20 min | 3 min | 3–5 |

Construir los doce pasos costó unas 20 horas. Se pagaron en el tercer video. Lo que no se pagó en horas
sino en calidad fue `validar-cortes` y `verificar`: no ahorran tiempo, **evitan publicar defectos**.

---

## Cuándo un pipeline es demasiado

Si el video es único (un documental de una sola pieza, un evento que no se repite), el pipeline te va a
costar más de lo que devuelve. Ahí se hace a mano y se guardan los comandos en un archivo de texto, nada
más. El módulo `137` da el criterio numérico.

---

## Errores comunes

- **Diseñar los doce pasos antes de haber editado un video completo a mano.** Sale un pipeline que
  automatiza lo que creías que hacías, no lo que haces.
- **Pasos que se comunican en memoria.** Si `cortes` solo funciona corriendo justo después de
  `transcribir`, no tienes un pipeline: tienes un script largo partido en pedazos.
- **Un paso que hace tres cosas.** "Transcribe, elige tomas y monta" es imposible de depurar: cuando falla,
  no sabes cuál de las tres falló.
- **No guardar los productos intermedios.** Volver a transcribir cuesta dinero y minutos. `analisis/` existe
  para eso.
- **Que el pipeline no se detenga cuando la compuerta falla.** Si `todo` sigue montando después de un
  `validar-cortes` en rojo, la compuerta no sirve de nada.
- **Automatizar la selección de tomas.** Es la fase B, la de gusto. La máquina propone; tú apruebas.
- **Rutas absolutas escritas dentro de cada paso.** El día que copies el pipeline a otro proyecto,
  se rompe todo. Usa la raíz del proyecto como variable.
- **No tener un solo punto de entrada.** Doce scripts sueltos se corren en el orden equivocado tarde o
  temprano.
- **Construir el pipeline mientras tienes una entrega encima.** Se hace entre proyectos, con calma, sobre
  material que ya conoces.

---

## Checklist

- [ ] Edité al menos un video completo a mano antes de escribir el primer script
- [ ] Cada paso lee de disco y escribe a disco, sin estado en memoria entre pasos
- [ ] Cada paso se puede correr solo si sus insumos existen
- [ ] Correr un paso dos veces da el mismo resultado y no rompe nada
- [ ] Existe un despachador único (`edit.ps1`) con la lista de comandos válidos
- [ ] El despachador comprueba las herramientas externas (ffmpeg) una sola vez, arriba
- [ ] El modo `todo` se detiene al primer paso que devuelve código distinto de 0
- [ ] La compuerta (`validar-cortes`) está antes de `montar`, no después
- [ ] Ningún paso automatiza una decisión de gusto: la máquina propone, el humano aprueba
- [ ] Los productos intermedios caros (transcripción, análisis) se guardan en `analisis/`
- [ ] `trabajo/` se puede borrar entero y reconstruir corriendo el pipeline
- [ ] Cada paso imprime un resumen legible: qué procesó, cuánto, dónde quedó
- [ ] Solo automaticé cosas que ya había hecho a mano tres veces
- [ ] Sé cuánto tiempo ahorra cada paso, medido, no supuesto

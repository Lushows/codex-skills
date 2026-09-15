# 133 — Verificación automática

## Qué resuelve

Que no se publique nada roto, y que descubrirlo no dependa de que alguien tuviera la paciencia de ver el
video completo con audífonos a las once de la noche.

Un pipeline serio tiene **dos compuertas**, no una:

| | Compuerta de entrada (`validar-cortes`) | Compuerta de salida (`verificar`) |
|---|---|---|
| Cuándo | antes de montar | después de renderizar |
| Sobre qué | la tabla (`montaje.csv`, `cortes.csv`) | el archivo `.mp4` terminado |
| Qué caza | palabras partidas, tramos imposibles, números incoherentes | audio saturado, silencios, negros, congelados, duración, texto perdido |
| Costo de arreglar | cambiar una celda | rehacer el render |

La primera está desarrollada en el módulo `16`. Este módulo es la segunda, más la idea que las une:
**medir lo medible por máquina, y llevarle al humano solo lo que de verdad requiere un juicio.**

---

## Lo que una máquina SÍ puede verificar

Todo esto sale de ffprobe, de filtros de ffmpeg o de volver a transcribir el resultado. Nada de esto
requiere ojo ni oído:

| Defecto | Cómo se mide | Umbral típico (vertical, redes) |
|---|---|---|
| Duración distinta de la esperada | `ffprobe format=duration` | diferencia > 0,3 s contra la suma del CSV |
| Resolución o fps equivocados | `ffprobe stream=width,height,r_frame_rate` | debe ser exactamente 1080x1920 @30 |
| Sin pista de audio | `ffprobe stream=codec_type` | falla si no hay `audio` |
| Audio solo en un canal | `astats` por canal | diferencia de RMS > 12 dB entre canales |
| Volumen general fuera de norma | `ebur128` (LUFS integrado) | −16 a −13 LUFS para redes |
| Picos que saturan | `astats` peak level | > −1,0 dBTP |
| Silencios largos | `silencedetect` | cualquier silencio > 1,2 s no marcado en la tabla |
| Fotogramas en negro | `blackdetect` | > 0,5 s de negro no previsto |
| Imagen congelada | `freezedetect` | > 1,5 s |
| Palabras partidas | retranscribir y comparar contra el texto esperado | cualquier palabra incompleta |
| Peso del archivo desproporcionado | tamaño / duración | > 5 MB por 10 s en 1080p vertical |
| Texto fuera de zona segura | posición declarada en el `.ass` vs límites de la plataforma | módulo `45` |

Doce defectos que se cazan solos, en menos de tres minutos, sin que nadie mire nada.

---

## Lo que una máquina NO puede verificar

Esta lista es igual de importante, y hay que decirla en voz alta para no vender humo:

- **Si el gancho engancha.** Se mide con retención real, después de publicar (módulo `140`).
- **Si el chiste da risa.** Ni una IA que lea la transcripción lo sabe.
- **Si la música pega con la marca.** Se puede medir el BPM; no si "suena a nosotros".
- **Si el color se siente bien.** Se pueden medir vectorscopio y niveles; el gusto no.
- **Si el ritmo respira.** Se puede contar cambios por segundo; que "se sienta apurado" es humano.
- **Si el corte cuenta la historia.** El montaje puede ser técnicamente impecable y no decir nada.

Regla honesta: **la verificación automática garantiza que no hay defectos, no que el video sea bueno.**
Son cosas distintas, y confundirlas produce videos correctos y muertos.

---

## El script `verificar`

PowerShell, corre sobre el archivo final e imprime un semáforo. Devuelve código 1 si hay rojos, para que
se pueda encadenar.

```powershell
# verificar.ps1 -- compuerta de salida. Mide el archivo terminado.
# Devuelve 0 si esta limpio, 1 si hay rojos. Nunca dice "todo bien" sin numeros:
# un informe sin cifras no se puede discutir ni comparar entre versiones.

param(
  [Parameter(Mandatory=$true)][string]$Video,
  [double]$DuracionEsperada = 0,
  [int]$AnchoEsperado = 1080,
  [int]$AltoEsperado = 1920,
  [double]$LufsMin = -16.5,
  [double]$LufsMax = -12.5
)

if (-not (Test-Path $Video)) {
  Write-Output "NO EXISTE el archivo: $Video"
  Write-Output "ARREGLO: corre primero  .\edit.ps1 montar"
  exit 1
}

$rojos = 0; $amarillos = 0
function Rojo($m, $arreglo)   { Write-Output ("ROJO      {0}" -f $m); if ($arreglo) { Write-Output ("          ARREGLO: {0}" -f $arreglo) }; $script:rojos++ }
function Amarillo($m)         { Write-Output ("AMARILLO  {0}" -f $m); $script:amarillos++ }
function Verde($m)            { Write-Output ("ok        {0}" -f $m) }

# --- 1. Ficha tecnica -------------------------------------------------------
$json = & ffprobe -v error -show_entries format=duration,size -show_entries stream=codec_type,width,height,r_frame_rate,channels -of json $Video | ConvertFrom-Json
$dur  = [double]$json.format.duration
$peso = [double]$json.format.size / 1MB
$v    = $json.streams | Where-Object { $_.codec_type -eq "video" } | Select-Object -First 1
$a    = $json.streams | Where-Object { $_.codec_type -eq "audio" } | Select-Object -First 1

Verde ("duracion {0} s   peso {1} MB" -f [math]::Round($dur,2), [math]::Round($peso,1))

if ($DuracionEsperada -gt 0 -and [math]::Abs($dur - $DuracionEsperada) -gt 0.3) {
  Rojo ("duracion {0} s, la tabla suma {1} s" -f [math]::Round($dur,2), $DuracionEsperada) `
       "un bloque no entro o entro dos veces. Revisa trabajo/segmentos/lista.txt"
}
if ($v.width -ne $AnchoEsperado -or $v.height -ne $AltoEsperado) {
  Rojo ("resolucion {0}x{1}, se esperaba {2}x{3}" -f $v.width, $v.height, $AnchoEsperado, $AltoEsperado) `
       "revisa la constante de formato en montar.mjs"
} else { Verde ("resolucion {0}x{1}" -f $v.width, $v.height) }

if (-not $a) {
  Rojo "el video NO tiene pista de audio" "revisa que los bloques de imagen lleven anullsrc"
} elseif ($a.channels -lt 2) {
  Amarillo ("audio en {0} canal" -f $a.channels)
}

# --- 2. Volumen (LUFS) ------------------------------------------------------
# ebur128 escribe a stderr; PowerShell ya lo captura, no hay que redirigir.
$eb = & ffmpeg -hide_banner -nostats -i $Video -filter_complex ebur128=peak=true -f null NUL 2>&1 | Out-String
if ($eb -match "I:\s*(-?\d+\.?\d*)\s*LUFS") {
  $lufs = [double]$Matches[1]
  if ($lufs -lt $LufsMin) {
    Rojo ("volumen {0} LUFS: suena bajito frente a los demas videos del feed" -f $lufs) `
         ("sube con  -af loudnorm=I=-14:TP=-1.0:LRA=11")
  } elseif ($lufs -gt $LufsMax) {
    Rojo ("volumen {0} LUFS: la plataforma lo va a bajar y va a sonar apretado" -f $lufs) `
         ("normaliza a -14 LUFS con loudnorm")
  } else { Verde ("volumen {0} LUFS" -f $lufs) }
} else { Amarillo "no se pudo leer LUFS" }

if ($eb -match "Peak:\s*(-?\d+\.?\d*)\s*dBFS") {
  $pk = [double]$Matches[1]
  if ($pk -gt -1.0) { Rojo ("pico {0} dBFS: satura" -f $pk) "baja 1 dB o pon un limitador (modulo 73)" }
  else { Verde ("pico {0} dBFS" -f $pk) }
}

# --- 3. Silencios -----------------------------------------------------------
$sil = & ffmpeg -hide_banner -nostats -i $Video -af "silencedetect=noise=-42dB:d=1.2" -f null NUL 2>&1 | Out-String
$huecos = [regex]::Matches($sil, "silence_start:\s*(\d+\.?\d*)")
foreach ($m in $huecos) {
  Amarillo ("silencio de mas de 1.2 s empezando en el segundo {0}" -f $m.Groups[1].Value)
}
if ($huecos.Count -eq 0) { Verde "sin silencios largos" }

# --- 4. Negros y congelados -------------------------------------------------
$blk = & ffmpeg -hide_banner -nostats -i $Video -vf "blackdetect=d=0.5:pix_th=0.10" -f null NUL 2>&1 | Out-String
foreach ($m in [regex]::Matches($blk, "black_start:(\d+\.?\d*)")) {
  Rojo ("pantalla en negro desde el segundo {0}" -f $m.Groups[1].Value) "casi siempre es un bloque con fuente equivocada"
}
$frz = & ffmpeg -hide_banner -nostats -i $Video -vf "freezedetect=n=-60dB:d=1.5" -f null NUL 2>&1 | Out-String
foreach ($m in [regex]::Matches($frz, "freeze_start:\s*(\d+\.?\d*)")) {
  Amarillo ("imagen congelada desde el segundo {0} (puede ser una imagen fija a proposito)" -f $m.Groups[1].Value)
}

# --- Veredicto --------------------------------------------------------------
Write-Output ""
Write-Output ("=== VERIFICACION: {0} rojos, {1} amarillos ===" -f $rojos, $amarillos)
if ($rojos -gt 0) { Write-Output "NO SE PUBLICA."; exit 1 }
Write-Output "Tecnicamente limpio. Falta el ojo humano: ritmo, gusto, marca."
exit 0
```

Fíjate en la última línea. **El script nunca dice "aprobado".** Dice "técnicamente limpio" y recuerda que
falta lo que no puede medir. Esa honestidad evita que la gente confíe de más.

---

## La verificación que más vale: retranscribir el resultado

Todos los defectos anteriores son técnicos. El defecto que de verdad se lleva videos al aire roto es
**la palabra partida**, y la única forma de cazarla en el archivo final es volver a transcribirlo y
comparar contra lo que la tabla decía que debía decir.

```js
// verificar-texto.mjs -- extrae el audio del video final, lo transcribe y lo compara
// contra la columna texto de montaje.csv.
// Por que existe: la compuerta de entrada valida la INTENCION; esto valida el RESULTADO.
// Entre las dos hay un render, y ahi es donde aparecen los desfases.

import { readFileSync, writeFileSync } from "node:fs";
import { spawnSync } from "node:child_process";
import { join } from "node:path";

const RAIZ = process.env.PROYECTO || process.cwd();
const video = process.argv[2];
if (!video) {
  console.log("Uso: node verificar-texto.mjs salida\\v06-mezcla.mp4");
  process.exit(1);
}

// 1. Audio mono 16 kHz: es lo que piden casi todos los modelos de transcripcion
//    y pesa 10 veces menos que mandar el mp4 entero.
const wav = join(RAIZ, "trabajo", "verificacion.wav");
const r = spawnSync("ffmpeg", ["-hide_banner", "-loglevel", "error", "-y",
  "-i", video, "-vn", "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le", wav], { encoding: "utf8" });
if (r.status !== 0) {
  console.log(`No se pudo extraer el audio de ${video}\n${r.stderr.trim()}`);
  process.exit(1);
}

// 2. Aqui va la llamada al modelo que lee audio (ver modulo 124 y 138).
//    Devuelve { texto, palabras: [{ palabra, inicio, fin }] }
const dicho = JSON.parse(readFileSync(join(RAIZ, "analisis", "verificacion.json"), "utf8"));

// 3. Normalizar para comparar: sin tildes, sin puntuacion, minusculas.
const norm = (s) => s.toLowerCase()
  .normalize("NFD").replace(/[\u0300-\u036f]/g, "")
  .replace(/[^\w\s]/g, " ").replace(/\s+/g, " ").trim();

const esperado = readFileSync(join(RAIZ, "montaje.csv"), "utf8")
  .split(/\r?\n/).slice(1).filter(Boolean)
  .map((l) => (l.match(/"([^"]*)"/g) || []).join(" "))
  .join(" ");

const pe = norm(esperado).split(" ").filter(Boolean);
const pd = norm(dicho.texto).split(" ").filter(Boolean);

// 4. Palabras del guion que no aparecen en el resultado = candidatas a corte malo.
const faltantes = pe.filter((p) => p.length > 3 && !pd.includes(p));
if (faltantes.length) {
  console.log(`FALTAN ${faltantes.length} palabras del guion en el video final:`);
  console.log("  " + faltantes.join(", "));
  console.log("  Suele significar que un corte entro tarde o salio temprano.");
}

// 5. Palabras cortadas: fragmentos cortos pegados al inicio o fin de un bloque.
const sospechosas = dicho.palabras.filter((p) => p.palabra.length <= 2 && (p.fin - p.inicio) < 0.12);
for (const s of sospechosas) {
  console.log(`SOSPECHA en ${s.inicio.toFixed(1)} s: "${s.palabra}" dura ${(s.fin - s.inicio).toFixed(2)} s`);
  console.log("  Puede ser el resto de una palabra cortada por el corte anterior.");
}

process.exitCode = faltantes.length > 0 ? 1 : 0;
```

---

## Los tres niveles del semáforo

| Nivel | Qué significa | Qué hace el pipeline |
|---|---|---|
| **ROJO** | defecto objetivo, verificable, indiscutible | **bloquea**. Código de salida 1 |
| **AMARILLO** | puede estar bien a propósito | avisa y sigue; lo mira un humano |
| **ok** | medido y dentro de norma | se imprime igual, con el número |

Imprimir los verdes con su número no es relleno: es lo que te deja comparar `v05` contra `v06` y ver que
el volumen bajó 2 LUFS sin que nadie lo pidiera.

Y el amarillo tiene que existir. Un sistema que solo tiene rojo y verde termina en uno de dos sitios:
bloquea por tonterías y la gente lo desactiva, o afloja los umbrales y deja pasar defectos reales.

---

## Dónde encajan las dos compuertas

```
cortes (15)
    v
+---------------------------+
|  COMPUERTA DE ENTRADA     |  validar-cortes -> si hay rojos, vuelve a la tabla
+---------------------------+
    v
montar (131)  ->  musicalizar
    v
+---------------------------+
|  COMPUERTA DE SALIDA      |  verificar -> si hay rojos, vuelve a la tabla
+---------------------------+
    v
ojo humano: una pasada completa con audio
    v
publicar
```

Las dos flechas de retorno apuntan a **la tabla**, no al video. Ese es el punto del bloque entero.

---

## El ojo humano sigue siendo obligatorio

Después de que el semáforo salga limpio, alguien ve el video **una vez, entero, con sonido, en el
teléfono**. Esa pasada busca lo que ninguna medición ve:

- ¿El primer segundo engancha?
- ¿Se entiende sin sonido?
- ¿La música cansa?
- ¿El texto se puede leer con el pulgar encima?
- ¿Se siente de la marca?

Una sola pasada. Si tienes que verlo cinco veces para decidir, el problema no es la verificación: es el
video (módulo `29`).

---

## Errores comunes

- **Verificar solo al final.** Sin la compuerta de entrada, cada defecto cuesta un render completo.
- **Un script que dice "FALLO" sin el número.** "Volumen fuera de norma" no sirve; "−19,4 LUFS, se espera
  entre −16,5 y −12,5" se arregla solo (módulo `136`).
- **Solo rojo y verde.** Sin amarillo, o bloqueas por cosas intencionales o aflojas los umbrales.
- **Que el script diga "aprobado".** Nunca. Di "técnicamente limpio", que es lo que de verdad comprobaste.
- **No comparar la duración final con la suma de la tabla.** Es el chequeo más barato y caza el bloque que
  se duplicó o el que no entró.
- **Ignorar los amarillos siempre.** A las tres semanas nadie los lee y son ruido. Si un amarillo nunca es
  relevante, quítalo; si siempre lo es, súbelo a rojo.
- **Verificar el master y publicar la versión comprimida sin verificar.** Cada entrega se verifica.
- **Confiar en que "verificado" significa "bueno".** Garantiza ausencia de defectos, no calidad.
- **Redirigir `2>&1` de ffmpeg en PowerShell 5.1.** Envuelve cada línea en un objeto de error y te rompe
  el `$?` aunque el comando haya salido bien. La salida de error ya se captura sola.
- **No guardar el informe.** Guarda `analisis/verificacion-v06.txt`: comparar informes entre versiones es
  la forma más rápida de ver qué se rompió.

---

## Checklist

- [ ] Hay compuerta de entrada (sobre la tabla) y compuerta de salida (sobre el archivo)
- [ ] La compuerta de salida mide duración, resolución, fps, presencia de audio y canales
- [ ] Mide LUFS integrado y pico verdadero, con umbrales escritos
- [ ] Detecta silencios largos, negros y congelados
- [ ] Compara la duración final contra la suma de la tabla
- [ ] Retranscribe el resultado y lo compara con el texto esperado
- [ ] Cada mensaje incluye el número medido y el umbral, no solo el nombre del chequeo
- [ ] Cada rojo propone un arreglo concreto
- [ ] Existen tres niveles: rojo bloquea, amarillo avisa, ok imprime el número
- [ ] El script devuelve código 1 si hay rojos y el pipeline se detiene ahí
- [ ] El script nunca dice "aprobado": dice "técnicamente limpio"
- [ ] El informe se guarda en `analisis/` con el número de versión
- [ ] Después del semáforo, un humano ve el video una vez entero, con sonido, en el teléfono
- [ ] Cada entrega por plataforma se verifica, no solo el master

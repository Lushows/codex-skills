# 134 — Procesar por lotes

## Qué resuelve

Cuando ya no es un video: son 50 clips que analizar, 10 ganchos que probar en pauta, o el mismo corte en
tres formatos. Hacerlo de a uno es una tarde entera y garantiza que uno salga distinto de los demás.

**Lote** (en inglés *batch*): correr la misma operación sobre muchos insumos con un solo comando. La
ventaja no es solo velocidad, es **uniformidad**: los 30 archivos salen con los mismos parámetros porque
los parámetros están escritos una vez.

---

## Los tres tipos de lote

Se confunden, y cada uno se resuelve distinto:

| Tipo | Qué varía | Ejemplo | Cómo se resuelve |
|---|---|---|---|
| **Muchos insumos** | el archivo de entrada | 50 clips de cámara a analizar | recorrer la carpeta |
| **Muchas variantes** | una decisión del montaje | 10 ganchos distintos, mismo cuerpo | una tabla de variantes |
| **Muchas salidas** | el formato final | 9:16, 1:1, 16:9 desde el mismo master | una tabla de formatos |

Los tres se pueden combinar y ahí es donde explota: 10 ganchos × 3 formatos = 30 renders. Por eso el
número importa antes de arrancar.

---

## Lote tipo 1: muchos insumos

El más simple. Recorrer y aplicar. Con dos exigencias: **que uno que falle no tumbe el lote**, y **que se
pueda reanudar**.

```powershell
# lote-analizar.ps1 -- ficha tecnica de todos los clips de entrada/.
# Reanudable: si el .json del clip ya existe, lo salta. Un lote de 50 que se
# cae en el 47 y hay que empezar de cero es la razon por la que la gente odia
# los lotes.

param(
  [string]$Proyecto = (Get-Location).Path,
  [switch]$Forzar
)

$entrada = Join-Path $Proyecto "entrada"
$destino = Join-Path $Proyecto "analisis\fichas"
New-Item -ItemType Directory -Force -Path $destino | Out-Null

$clips = Get-ChildItem "$entrada\*" -Include *.mp4,*.mov,*.mkv | Sort-Object Name
if ($clips.Count -eq 0) { Write-Output "No hay videos en $entrada"; exit 1 }

$hechos = 0; $saltados = 0; $fallidos = @(); $i = 0

foreach ($c in $clips) {
  $i++
  $salida = Join-Path $destino ($c.BaseName + ".json")
  if ((Test-Path $salida) -and -not $Forzar) { $saltados++; continue }

  Write-Output ("[{0}/{1}] {2}" -f $i, $clips.Count, $c.Name)
  try {
    $json = & ffprobe -v error -show_entries format=duration,size `
              -show_entries stream=codec_type,codec_name,width,height,r_frame_rate `
              -of json $c.FullName
    if ($LASTEXITCODE -ne 0) { throw "ffprobe devolvio $LASTEXITCODE" }
    $json | Out-File -FilePath $salida -Encoding utf8
    $hechos++
  } catch {
    # No se corta el lote: se anota y se sigue. El informe del final dice que fallo.
    $fallidos += [pscustomobject]@{ archivo = $c.Name; motivo = $_.Exception.Message }
  }
}

Write-Output ""
Write-Output ("LOTE: {0} procesados, {1} ya estaban, {2} fallidos" -f $hechos, $saltados, $fallidos.Count)
foreach ($f in $fallidos) { Write-Output ("  FALLO {0}: {1}" -f $f.archivo, $f.motivo) }
if ($fallidos.Count -gt 0) { exit 1 }
```

Tres decisiones que se repiten en todo lote:

1. **Saltar lo ya hecho.** Reanudable por defecto, con `-Forzar` para rehacer.
2. **Un fallo no tumba el lote.** Se anota y se sigue.
3. **El informe va al final, agrupado.** No mezclado entre 50 líneas de progreso donde nadie lo ve.

---

## Lote tipo 2: variantes del montaje

Aquí se ve por qué la tabla del módulo `131` vale tanto. Diez ganchos distintos no son diez proyectos:
son **diez veces la misma tabla con la fila `b01` cambiada**.

`variantes.csv`:

```csv
variante,bloque,tipo,fuente,entrada,salida,texto_pantalla,nota
g1,b01,video,clip-03.mp4,12.4,20.6,MIRA ESTO,"gancho directo a camara"
g2,b01,video,clip-05.mp4,3.1,9.8,NADIE TE LO DICE,"gancho de secreto"
g3,b01,video,clip-11.mp4,30.2,36.0,3 SEMANAS,"gancho de dato duro"
g4,b01,imagen,assets/generado-ia/portada.png,0.0,2.0,,"gancho grafico, sin voz"
```

Y el generador:

```js
// lote-variantes.mjs -- una variante = el montaje base con b01 reemplazado.
// El cuerpo del video (b02..b08) NO se recodifica entre variantes: la cache por
// huella del modulo 132 lo reutiliza tal cual. Diez variantes cuestan un cuerpo
// mas diez ganchos, no diez videos.

import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { spawnSync } from "node:child_process";
import { join } from "node:path";

const RAIZ = process.env.PROYECTO || process.cwd();
const base = readFileSync(join(RAIZ, "montaje.csv"), "utf8").trim().split(/\r?\n/);
const cab = base[0];
const cuerpo = base.slice(1).filter((l) => !l.startsWith("b01,"));

const variantes = readFileSync(join(RAIZ, "variantes.csv"), "utf8").trim().split(/\r?\n/).slice(1);
mkdirSync(join(RAIZ, "trabajo", "variantes"), { recursive: true });
const informe = [];

for (const v of variantes) {
  const id = v.split(",")[0];
  const tabla = join(RAIZ, "trabajo", "variantes", `montaje-${id}.csv`);
  writeFileSync(tabla, [cab, v.split(",").slice(1).join(","), ...cuerpo].join("\n") + "\n", "utf8");

  console.log(`\n=== variante ${id} ===`);
  const r = spawnSync("node", [join(RAIZ, "pipeline", "montar.mjs"), id],
    { stdio: "inherit", env: { ...process.env, PROYECTO: RAIZ, TABLA: tabla } });
  informe.push({ variante: id, codigo: r.status });
}

console.log("\n=== INFORME DEL LOTE ===");
for (const r of informe) console.log(`${r.variante}  ${r.codigo === 0 ? "OK" : "FALLO codigo " + r.codigo}`);
process.exitCode = informe.some((r) => r.codigo !== 0) ? 1 : 0;
```

Para pauta esto es oro: diez creativos que solo difieren en el gancho, todos con exactamente el mismo
cuerpo, mismo color, mismo audio. Cuando uno gane, sabes que ganó **por el gancho** y no por diecisiete
diferencias que nadie controló (ver `facebook_ads_lushows` para la lectura del test).

---

## Lote tipo 3: formatos de salida

Desde **el master**, nunca desde otra entrega (módulo `132`).

`formatos.csv`:

```csv
formato,ancho,alto,encuadre,crf,nota
9x16,1080,1920,centro,20,"reels tiktok shorts"
1x1,1080,1080,centro,20,"feed instagram"
16x9,1920,1080,pan:0.35,20,"youtube. pan 0.35 porque el sujeto esta a la izquierda"
4x5,1080,1350,centro,20,"feed vertical, el que mas area ocupa"
```

```powershell
# lote-formatos.ps1 -- exporta el master a todos los formatos de formatos.csv.
# El master se codifico una sola vez; cada formato es UNA generacion, nunca dos.

param(
  [Parameter(Mandatory=$true)][string]$Master,
  [string]$Proyecto = (Get-Location).Path
)

$formatos = Import-Csv (Join-Path $Proyecto "formatos.csv")
$salida = Join-Path $Proyecto "salida\entregas"
New-Item -ItemType Directory -Force -Path $salida | Out-Null
$nombre = [System.IO.Path]::GetFileNameWithoutExtension($Master)

foreach ($f in $formatos) {
  $w = [int]$f.ancho; $h = [int]$f.alto
  # 'centro' recorta al medio; 'pan:0.35' corre el recorte al 35% del ancho sobrante,
  # que es lo que hace falta cuando el sujeto no esta centrado en el master.
  if ($f.encuadre -match "^pan:(.+)$") {
    $p = [double]$Matches[1]
    $crop = "crop=iw*min(1\,($w/$h)/(iw/ih)):ih*min(1\,(iw/ih)/($w/$h)):(iw-ow)*$p:(ih-oh)/2"
  } else {
    $crop = "crop=iw*min(1\,($w/$h)/(iw/ih)):ih*min(1\,(iw/ih)/($w/$h)):(iw-ow)/2:(ih-oh)/2"
  }
  $destino = Join-Path $salida ("{0}-{1}.mp4" -f $nombre, $f.formato)

  Write-Output ("-> {0}  {1}x{2}" -f $f.formato, $w, $h)
  & ffmpeg -hide_banner -loglevel error -y -i $Master `
    -vf "$crop,scale=${w}:${h}:flags=lanczos" `
    -c:v libx264 -crf $f.crf -preset medium -pix_fmt yuv420p `
    -c:a copy -movflags +faststart $destino

  if ($LASTEXITCODE -ne 0) { Write-Output ("   FALLO en {0}" -f $f.formato) }
}
Write-Output "Entregas en $salida"
```

---

## Paralelismo: cuánto, y por qué no más

La tentación es lanzar los 30 renders a la vez. Sale peor: **ffmpeg ya usa todos los núcleos.** Con
`libx264 -preset medium` la CPU ya está al 90%, así que cuatro procesos en paralelo no van cuatro veces
más rápido; se pelean. La regla que funciona en la práctica:

| Tipo de tarea | Concurrencia recomendada | Por qué |
|---|---|---|
| Codificar video (x264) | 2, o `núcleos / 4` | cada proceso ya es multihilo |
| ffprobe / analizar | 8 o más | son lecturas cortas, casi no usan CPU |
| Extraer fotogramas | 4 | limitado por disco |
| Llamadas a API de IA | 3–4 | limitado por cuota, no por tu máquina (módulo `138`) |
| Copiar / concatenar | 1 | limitado por disco; en paralelo va más lento |

Y una regla de oro: **mide antes de creerlo.** En el caso maestro, con 8 núcleos, procesar 14 clips con
concurrencia 2 tomó 3 min 10 s; con concurrencia 6 tomó 3 min 40 s. Más paralelismo dio menos velocidad.

### Cola con límite, en Node

```js
// cola.mjs -- ejecuta tareas con un tope de procesos simultaneos.
// Sin tope, 30 ffmpeg a la vez se pelean por CPU y disco y el total tarda MAS
// que en serie. Medido en el caso maestro: 6 en paralelo fue 15% mas lento que 2.

import { spawn } from "node:child_process";
import { cpus } from "node:os";

export async function cola(tareas, limite = Math.max(2, Math.floor(cpus().length / 4))) {
  const resultados = [];
  let siguiente = 0;

  async function trabajador() {
    while (siguiente < tareas.length) {
      const i = siguiente++, t = tareas[i], t0 = Date.now();
      const codigo = await new Promise((res) => {
        const p = spawn(t.cmd, t.args, { stdio: ["ignore", "ignore", "pipe"] });
        let err = "";
        p.stderr.on("data", (d) => { err += d.toString(); });
        // Solo las 3 ultimas lineas de stderr: el error util de ffmpeg esta al final.
        p.on("close", (c) => { if (c !== 0) t.error = err.trim().split("\n").slice(-3).join("\n"); res(c); });
      });
      const seg = ((Date.now() - t0) / 1000).toFixed(1);
      console.log(`[${i + 1}/${tareas.length}] ${t.nombre}  ${codigo === 0 ? "OK" : "FALLO"}  ${seg} s`);
      resultados[i] = { ...t, codigo, segundos: Number(seg) };
    }
  }

  await Promise.all(Array.from({ length: limite }, () => trabajador()));
  return resultados;
}
```

Uso, con informe al final:

```js
import { cola } from "./cola.mjs";

const tareas = clips.map((c) => ({
  nombre: c, cmd: "ffmpeg",
  args: ["-hide_banner", "-loglevel", "error", "-y", "-i", `entrada/${c}`,
         "-vf", "fps=1/5,scale=320:-1,tile=5x4", `analisis/hojas-contacto/${c}.jpg`],
}));

const r = await cola(tareas, 4);
const malos = r.filter((x) => x.codigo !== 0);
console.log(`\n${r.length - malos.length} OK, ${malos.length} fallidos`);
for (const m of malos) console.log(`  ${m.nombre}\n    ${m.error}`);
process.exitCode = malos.length ? 1 : 0;
```

---

## Los límites reales que te van a morder

| Límite | Síntoma | Qué hacer |
|---|---|---|
| **Disco** | el CPU al 40% y todo lentísimo | bajar concurrencia; usar SSD; no leer y escribir en el mismo disco lento |
| **RAM** | el sistema se congela, ffmpeg muere sin mensaje | bajar concurrencia; evitar filtros que cargan el clip entero |
| **Codificador por hardware** | "OpenEncodeSessionEx failed" | NVENC tiene tope de sesiones simultáneas en tarjetas de consumo. Para lotes, x264 en CPU |
| **Temperatura** | los últimos del lote tardan el doble | portátiles: el procesador se frena solo. No es tu script |
| **Ruta de más de 260 caracteres** | "no se encuentra el archivo" con la ruta visible en pantalla | Windows. Carpetas de proyecto cortas (módulo `135`) |
| **Cuota de API** | error 429 a mitad del lote | concurrencia 3, reintentos con espera (módulo `138`) |

---

## Cuánto va a tardar: dilo antes de arrancar

Un lote que empieza sin estimación es un lote que alguien mata a la mitad porque "se colgó".

```powershell
# Medir el primero y multiplicar. Estimacion tosca, pero evita que alguien mate
# el proceso a los 10 minutos creyendo que se colgo.
$unitario = ((Get-Date) - $t0).TotalSeconds
Write-Output ("Primer elemento: {0} s. Estimado total: ~{1} min para {2} elementos." -f `
              [math]::Round($unitario,1), [math]::Round($unitario * $clips.Count / 60, 1), $clips.Count)
```

Y siempre imprime `[7/50]`. Una barra de progreso no hace falta; saber en cuál va, sí.

---

## Nombres de salida y manifiesto

El nombre dice versión, variante y formato: `v06-g1-9x16.mp4` (convención completa en el módulo `135`).
Y el mismo lote genera `salida/entregas/manifiesto.csv`:

```csv
archivo,variante,formato,duracion,peso_mb,lufs,fecha
v06-g1-9x16.mp4,g1,9x16,48.1,7.4,-14.2,2026-08-04
v06-g2-9x16.mp4,g2,9x16,47.6,7.2,-14.1,2026-08-04
```

Ese manifiesto es lo que le pasas a quien sube la pauta. Sin él, treinta archivos en una carpeta son un
acertijo.

---

## Errores comunes

- **Lanzar 30 ffmpeg a la vez.** Se pelean por CPU y disco y el lote total tarda más que con dos.
- **Un lote que se cae entero cuando falla el elemento 47.** Captura, anota, sigue, informa al final.
- **Un lote no reanudable.** Si no salta lo ya hecho, un corte de luz cuesta la tarde completa.
- **Errores impresos mezclados con el progreso.** Se pierden entre 50 líneas. El informe va al final,
  agrupado.
- **Renderizar cada variante desde cero.** Con la caché por huella, el cuerpo común se codifica una vez.
- **Exportar los formatos desde otra entrega y no desde el master.** Pérdida generacional multiplicada.
- **No decir cuánto va a tardar.** Alguien lo mata a la mitad creyendo que se colgó.
- **Usar NVENC para lotes grandes en tarjeta de consumo.** Tope de sesiones simultáneas y calidad
  irregular entre archivos.
- **Nombres de salida que no dicen la variante.** Treinta archivos indistinguibles y hay que volver a
  renderizar para saber cuál era cuál.
- **No verificar las salidas del lote.** El módulo `133` corre sobre cada entrega, no solo sobre el master.
- **Carpetas de proyecto muy anidadas.** En Windows la ruta de 260 caracteres te tumba el lote en el
  archivo con el nombre más largo.

---

## Checklist

- [ ] El lote salta lo ya procesado y se puede reanudar
- [ ] Existe una opción `-Forzar` para rehacer todo a propósito
- [ ] Un elemento que falla no detiene el lote: se anota y se sigue
- [ ] Al final hay un informe agrupado con los fallidos y su motivo
- [ ] El lote imprime `[n/total]` en cada elemento
- [ ] Se estima el tiempo total después del primer elemento
- [ ] La concurrencia está limitada y el límite se eligió midiendo, no suponiendo
- [ ] Las tareas de codificación usan concurrencia baja (2 o núcleos/4)
- [ ] Las variantes reutilizan los segmentos comunes por caché
- [ ] Todos los formatos se exportan desde el master, no unos de otros
- [ ] Los nombres de salida incluyen versión, variante y formato
- [ ] Se genera un manifiesto con duración, peso y LUFS de cada entrega
- [ ] Cada entrega del lote pasa por la verificación del módulo `133`
- [ ] El lote devuelve código distinto de 0 si algún elemento falló

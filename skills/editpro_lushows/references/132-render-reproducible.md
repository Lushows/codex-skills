# 132 — Render reproducible

## Qué resuelve

Que el mismo insumo dé siempre el mismo resultado. Ni parecido: **el mismo**. Y que reconstruir el video
después de cambiar un bloque no cueste el render entero, sino ese bloque.

Dos promesas distintas que se apoyan la una en la otra:

1. **Determinismo** — correr `montar` hoy y dentro de un mes, con la misma tabla y el mismo material,
   produce un archivo equivalente. Idealmente, byte por byte.
2. **Caché** — si un bloque no cambió, su segmento no se vuelve a codificar. Se reutiliza.

Sin lo primero, lo segundo es peligroso: reutilizarías segmentos que ya no corresponden. Por eso van juntos.

---

## Por qué el mismo comando puede dar archivos distintos

Corre el mismo `ffmpeg` dos veces sobre el mismo clip y compara el hash. Casi siempre da distinto. No es
magia negra: son cuatro causas concretas.

| Causa | Qué mete de ruido | Se apaga con |
|---|---|---|
| **Metadatos del contenedor** | fecha de creación, versión del encoder escrita en el archivo | `-map_metadata -1 -fflags +bitexact -flags:v +bitexact -flags:a +bitexact` |
| **Multihilo del codificador** | el reparto entre hilos cambia decisiones de codificación | `-threads 1` (lento) o aceptar diferencia de bytes, no de imagen |
| **Versión de la herramienta** | x264 0.164 no codifica igual que 0.165 | congelar la versión y anotarla (módulo `139`) |
| **Aceleración por hardware** | NVENC/QuickSync varían entre drivers y GPUs | usar `libx264` (CPU) para el master |

La versión honesta: **con `-bitexact` y `-threads 1` obtienes bytes idénticos; sin `-threads 1` obtienes
imagen idéntica pero bytes distintos.** Para producción, lo segundo basta y es 6 veces más rápido. Lo
primero sirve para comprobar de vez en cuando que el pipeline sigue determinista.

### El comando de referencia

```powershell
# Segmento determinista. -bitexact quita la fecha y la firma del encoder del archivo,
# que son las dos cosas que cambian en cada corrida aunque el video sea el mismo.
ffmpeg -hide_banner -loglevel error -y `
  -i "entrada\clip-07.mp4" `
  -ss 51.3 -to 58.4 `
  -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30" `
  -af "aresample=48000" `
  -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p `
  -c:a aac -b:a 192k -ar 48000 -ac 2 `
  -map_metadata -1 -fflags +bitexact -flags:v +bitexact -flags:a +bitexact `
  "trabajo\segmentos\b05.mp4"
```

Comprobar el determinismo (correrlo dos veces a archivos distintos y comparar):

```powershell
$a = Get-FileHash "trabajo\segmentos\b05.mp4" -Algorithm SHA256
# ... vuelve a correr el mismo comando a b05-bis.mp4 ...
$b = Get-FileHash "trabajo\segmentos\b05-bis.mp4" -Algorithm SHA256
if ($a.Hash -eq $b.Hash) { Write-Output "DETERMINISTA" } else { Write-Output "VARIA (revisa -bitexact y -threads)" }
```

---

## El otro enemigo del determinismo: `-ss` antes o después de `-i`

Esto no es cosmético, cambia el corte:

| Forma | Qué hace | Cuándo usarla |
|---|---|---|
| `ffmpeg -ss 51.3 -i clip.mp4` | busca **rápido**, pero salta al fotograma clave anterior | previsualizaciones, b-roll donde el frame exacto da igual |
| `ffmpeg -i clip.mp4 -ss 51.3` | decodifica y corta **exacto** | siempre que haya voz. Un desfase de 0,3 s parte una palabra |

Regla del caso maestro: **si el bloque tiene voz, `-ss` va después de `-i`.** El costo es unos segundos de
decodificación; el beneficio es que el corte cae donde dice la tabla.

Y una trampa asociada: si mezclas las dos formas entre bloques, unos cortes caen donde dice la tabla y
otros no, y vas a creer que la tabla está mal.

---

## Segmentos intermedios: la unidad de caché

La estructura del módulo `131` ya deja el terreno listo: cada bloque se codifica a su propio archivo en
`trabajo/segmentos/` y al final se unen por copia.

```
trabajo/segmentos/
  b01.mp4
  b02.mp4
  b03.mp4
  ...
  lista.txt
```

Unir por copia (`-c copy`) es **instantáneo** y **sin pérdida**: no vuelve a codificar nada. Para que
funcione, todos los segmentos deben compartir exactamente resolución, fps, pixel format, códec, sample
rate y número de canales. Por eso el formato del master vive en una sola constante del script.

Y de ahí sale la ventaja: **cambiar el bloque `b05` obliga a recodificar `b05` y nada más.** Ocho bloques
que costaban 6 minutos pasan a costar 40 segundos.

---

## La caché por huella

¿Cómo sabe el script que `b05` cambió y `b04` no? Calculando una **huella** (hash) de todo lo que afecta a
ese segmento. Si la huella es la misma, el archivo sirve.

Qué entra en la huella:

1. La fila entera del CSV (fuente, entrada, salida, tipo, inserto)
2. La fecha de modificación y el tamaño del archivo fuente
3. La versión de la receta (una constante que subes a mano cuando cambias el script)
4. El formato del master (W, H, FPS, CRF)

```js
// pipeline/cache.mjs
// La huella responde una sola pregunta: "si vuelvo a codificar este bloque,
// saldria distinto?". Si algo de lo que entra aqui cambia, el segmento se rehace.

import { createHash } from "node:crypto";
import { statSync, existsSync } from "node:fs";

// RECETA sube cuando cambio el script de montaje de forma que afecte la imagen
// (filtros, crf, escalado). Si no la subo, la cache me devuelve segmentos viejos
// hechos con la receta anterior y el video queda mezclado. Paso por esto una vez.
export const RECETA = "3";

export function huella(fila, rutaFuente, formato) {
  const h = createHash("sha1");
  h.update(RECETA);
  h.update(JSON.stringify(formato));
  h.update([fila.tipo, fila.fuente, fila.entrada, fila.salida, fila.inserto].join("|"));
  if (rutaFuente && existsSync(rutaFuente)) {
    const s = statSync(rutaFuente);
    h.update(String(s.size));
    h.update(String(Math.floor(s.mtimeMs))); // si reemplazan el clip, la huella cambia
  }
  return h.digest("hex").slice(0, 12);
}
```

Y en `montar.mjs`:

```js
const hue = huella(f, join(RAIZ, "entrada", f.fuente), { W, H, FPS, CRF: 18 });
const destino = join(SEG, `${f.bloque}-${hue}.mp4`);

if (existsSync(destino) && !process.env.FORZAR) {
  console.log(`${f.bloque}  CACHE  ${hue}`);
} else {
  correrFfmpeg([...], `${f.bloque} (linea ${f.__linea})`);
  console.log(`${f.bloque}  RENDER ${hue}  ${dur.toFixed(1)} s`);
}
lista.push(`file '${destino.replace(/\\/g, "/")}'`);
```

El nombre del segmento **incluye la huella**. Eso da tres cosas gratis:

- No hay que guardar un índice aparte: el nombre del archivo *es* el índice.
- Las versiones viejas conviven; puedes volver atrás sin recodificar.
- Un vistazo a la carpeta te dice qué se rehizo.

### Cuándo la caché miente

Tres casos, y sus tres defensas:

| Caso | Por qué la caché falla | Defensa |
|---|---|---|
| Reemplazaste `clip-07.mp4` por otro con el mismo nombre | la fila del CSV no cambió | la huella incluye tamaño y fecha del fuente |
| Cambiaste el script de montaje (otro filtro, otro CRF) | la fila tampoco cambió | subir `RECETA` |
| Cortaste el render a media codificación | quedó un `.mp4` truncado que la caché da por bueno | escribir a `.tmp` y renombrar al terminar |

La tercera es la que muerde de verdad. La defensa correcta, en Node:

```js
// Escribir a temporal y renombrar: un archivo con el nombre definitivo solo
// existe si ffmpeg termino bien. Si mato el proceso a la mitad, queda un .tmp
// que la cache ignora, en vez de un mp4 truncado que da por bueno.
const tmp = destino + ".tmp.mp4";
correrFfmpeg([...args, tmp], contexto);
renameSync(tmp, destino);
```

---

## Limpiar la caché sin pensarlo demasiado

```powershell
# limpiar-cache.ps1 -- borra segmentos que ya no aparecen en la lista actual.
# No borra la carpeta entera: los segmentos vigentes cuestan minutos de CPU.

param([switch]$Todo)

$seg = "trabajo\segmentos"
if ($Todo) {
  Remove-Item "$seg\*" -Force -Confirm:$false
  Write-Output "Cache vaciada."
  exit 0
}

$vigentes = @{}
Get-Content "$seg\lista.txt" | ForEach-Object {
  if ($_ -match "file '(.+)'") { $vigentes[[System.IO.Path]::GetFileName($Matches[1])] = $true }
}

$borrados = 0
Get-ChildItem "$seg\*.mp4" | ForEach-Object {
  if (-not $vigentes.ContainsKey($_.Name)) {
    Remove-Item $_.FullName -Force -Confirm:$false
    $borrados++
  }
}
Write-Output ("Borrados {0} segmentos huerfanos. Quedan {1}." -f $borrados, $vigentes.Count)
```

---

## Generación: por qué no se recodifica dos veces

Cada vez que un video se codifica de nuevo pierde calidad. Se llama **pérdida generacional**. Si el
segmento se codifica al cortar, otra vez al ponerle subtítulos, otra vez al musicalizar y otra vez al
exportar, llevas cuatro generaciones encima y se nota en las zonas oscuras y en los degradados.

Cómo lo evita el pipeline:

| Paso | ¿Recodifica? | Por qué |
|---|---|---|
| `montar` (cortar bloques) | sí, 1 vez, a CRF 18 | inevitable: hay que escalar y recortar |
| unir segmentos | **no**, `-c copy` | por eso se exige formato idéntico |
| `subtitulos` quemados | sí | los subtítulos van en el mismo paso que el corte, no aparte |
| `musicalizar` | solo audio | `-c:v copy` y se toca únicamente la pista de sonido |
| entrega por plataforma | sí, 1 vez desde el master | nunca desde una versión ya exportada |

**El master se hace una vez a CRF 18 y de ahí salen todas las entregas.** Exportar la versión de
Instagram a partir de la de TikTok es la receta para que la tercera plataforma se vea mal.

`musicalizar` sin tocar el video:

```powershell
# -c:v copy: la imagen NO se vuelve a codificar. Solo se mezcla el audio.
ffmpeg -hide_banner -loglevel error -y `
  -i "salida\v06-corte.mp4" -i "assets\musica\tema.wav" `
  -filter_complex "[1:a]volume=-18dB[m];[0:a][m]sidechaincompress=threshold=0.05:ratio=8:attack=20:release=400[a]" `
  -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k `
  "salida\v06-mezcla.mp4"
```

---

## Un mezzanine cuando hay muchas pasadas

Si el proyecto exige varias pasadas de imagen (color, luego composición, luego texto), no encadenes MP4.
Usa un **mezzanine**: un archivo intermedio de calidad casi intacta.

| Códec intermedio | Peso aproximado por minuto en 1080p | Cuándo |
|---|---|---|
| ProRes 422 (`-c:v prores_ks -profile:v 3`) | ~1,1 GB | estándar, compatible con todo |
| DNxHR SQ (`-c:v dnxhd -profile:v dnxhr_sq`) | ~0,9 GB | alternativa libre |
| x264 CRF 12 | ~0,3 GB | cuando el disco importa más que el último 1% |

Ocupa mucho, y esa es exactamente la razón por la que vive en `trabajo/` y se borra al entregar.

---

## Lo que NUNCA es reproducible: la IA

Un modelo generativo no da lo mismo dos veces, aunque le pases la misma semilla, porque el modelo detrás
del API puede cambiar sin aviso. Por eso la regla del módulo `138`:

> La salida de IA se genera **una vez**, se guarda como archivo en `assets/generado-ia/` y **el pipeline
> consume el archivo, no el modelo.**

Si `montar` llamara a un generador de imágenes, el video dejaría de ser reproducible ese mismo día. La
ilustración es un insumo, igual que un clip de cámara.

---

## Errores comunes

- **Creer que el render es reproducible sin comprobarlo.** Corre el mismo bloque dos veces y compara
  hashes una vez al mes. Cuesta un minuto.
- **Mezclar `-ss` antes y después de `-i` entre bloques.** Unos cortes caen donde dice la tabla y otros no.
- **Cachear sin incluir la fecha del archivo fuente en la huella.** Reemplazas un clip y el pipeline te
  devuelve el segmento viejo, tan tranquilo.
- **No subir el número de receta al cambiar el script.** Sale un video mitad con la receta vieja y mitad
  con la nueva, y es dificilísimo de ver.
- **Escribir el segmento directo al nombre final.** Si cortas el proceso, queda un archivo truncado que la
  caché da por bueno para siempre.
- **Unir segmentos con `-c copy` sin haber unificado el formato.** El resultado se desincroniza o se corta
  a la mitad, y el mensaje de error de ffmpeg no dice por qué.
- **Exportar una plataforma desde la versión de otra plataforma.** Pérdida generacional acumulada.
- **Recodificar el video en `musicalizar`.** Solo se toca el audio: `-c:v copy`.
- **Usar NVENC para el master.** Es más rápido, pero varía entre drivers y GPUs y rompe el determinismo.
  Para entregas rápidas sirve; para el master, no.
- **Guardar los mezzanines en `salida/`.** Se entregan por error y pesan diez veces lo que deben.

---

## Checklist

- [ ] Los comandos de master llevan `-map_metadata -1` y `-bitexact`
- [ ] Comprobé al menos una vez, con hashes, que el mismo insumo da el mismo segmento
- [ ] `-ss` va después de `-i` en todos los bloques con voz
- [ ] Cada bloque se codifica a su propio segmento en `trabajo/segmentos/`
- [ ] Todos los segmentos comparten resolución, fps, pixel format, códec, sample rate y canales
- [ ] La unión final es `-c copy`, sin recodificar
- [ ] El nombre del segmento incluye la huella de sus insumos
- [ ] La huella incluye la fila del CSV, el tamaño y la fecha del fuente, y la versión de la receta
- [ ] Existe una constante `RECETA` y la subo cuando cambio el script de forma que afecte la imagen
- [ ] Los segmentos se escriben a `.tmp` y se renombran al terminar
- [ ] Existe una forma de forzar el render ignorando la caché (`FORZAR=1`)
- [ ] Todas las entregas salen del master, nunca de otra entrega
- [ ] `musicalizar` no recodifica la imagen
- [ ] Las salidas de IA están congeladas como archivos, no se generan durante el render
- [ ] Los mezzanines viven en `trabajo/` y no se entregan

# 135 — Nomenclatura y estructura de carpetas

## Qué resuelve

Que los scripts no tengan que adivinar dónde está nada, y que dentro de seis meses un nombre de archivo
te diga de dónde salió sin abrirlo.

El módulo `10` explica la organización desde el punto de vista del editor (el bruto es sagrado, no
sobrescribir, respaldar). **Este módulo es la misma estructura vista desde el pipeline**: qué carpeta
puede escribir cada paso, qué se puede borrar, y por qué los nombres se derivan en vez de inventarse.

La afirmación que gobierna todo:

> **Si un script tiene que preguntar dónde está algo, la estructura está mal.**

---

## La estructura completa

```
VIDEO-BOTELLA/
  edit.ps1                    punto de entrada unico
  montaje.csv                 LA TABLA. El montaje vive aqui
  variantes.csv               opcional: variantes de gancho
  formatos.csv                opcional: formatos de entrega
  TRAMPAS.md                  las cosas que muerden en este proyecto
  pipeline/                   los doce pasos
    analizar.mjs
    transcribir.mjs
    validar-cortes.ps1
    montar.mjs
    verificar.ps1
    cache.mjs
  entrada/                    el bruto. SOLO LECTURA. Ningun paso escribe aqui
    clip-01.mp4
    clip-14.mp4
  analisis/                   lo que el pipeline APRENDIO del bruto. Caro de regenerar
    ficha-tecnica.json
    transcripcion.md
    segmentos.json
    cortes.csv
    hojas-contacto/
      clip-01.jpg
    ondas/
      clip-01.png
    verificacion-v06.txt
  assets/                     lo que NO vino del rodaje. Caro o imposible de regenerar
    marca/                    logo, paleta, tipografia (fuente: directorcreativo)
    musica/
    fuentes/
    generado-ia/
      frasco-duotono.png
      frasco-duotono.prompt.txt
  subs/                       subtitulos generados
    v06.ass
  segmentos/                  bloques codificados. BORRABLE, se reconstruye
    b01-8f3a91c22e4d.mp4
    lista.txt
  trabajo/                    taller: pruebas, temporales, mezzanines. BORRABLE
    voz/
    marcado/
    logs/
  salida/                     lo que se entrega
    v06-corte.mp4
    v06-mezcla.mp4
    entregas/
      v06-g1-9x16.mp4
      manifiesto.csv
```

### Quién escribe dónde (esto es lo que hace que funcione)

| Carpeta | Quién escribe | ¿Se puede borrar? | Qué cuesta reconstruirla |
|---|---|---|---|
| `entrada/` | **nadie**. Solo tú, copiando el bruto | jamás | imposible: el rodaje no vuelve |
| `analisis/` | pasos 1–4 | sí, pero duele | minutos de CPU y dinero de API |
| `assets/` | pasos 7 y 9, y tú | no | dinero de IA, o trabajo de diseño |
| `subs/` | paso 5 | sí | segundos |
| `segmentos/` | paso 10 | sí, sin miedo | minutos de CPU |
| `trabajo/` | cualquiera | sí, sin miedo | minutos |
| `salida/` | pasos 10–11 | sí | un render |

**La prueba del fuego:** borra `segmentos/` y `trabajo/`, corre `.\edit.ps1 todo` y tienes que llegar al
mismo video. Si no llegas, algo importante estaba viviendo en una carpeta borrable. Haz esa prueba una vez
por proyecto.

---

## Por qué `segmentos/` está fuera de `trabajo/`

Detalle pequeño con consecuencia grande. `trabajo/` es el basurero: se borra sin pensar. `segmentos/` es
caché válida: borrarla cuesta minutos de CPU en cada cambio.

Tenerlas separadas te deja hacer `Remove-Item trabajo\* -Recurse` a ciegas sin perder la caché.

---

## Las siete reglas de nombres

### 1. Sin espacios, sin tildes, sin ñ

```
mal:   Clip Final Botella (versión 2).mp4
bien:  clip-14.mp4
```

No es purismo. Los espacios obligan a comillas en cada comando y rompen las listas de `concat` de ffmpeg.
Las tildes y la ñ se corrompen cuando un script escribe un archivo de texto en una codificación y otro lo
lee en otra — el clásico `caracterÃ­sticas` en medio de un `.ass`.

**El nombre del archivo, en ASCII. El contenido, en español con todas sus tildes.**

### 2. Minúsculas siempre

Windows no distingue mayúsculas, Linux sí, y los servicios en la nube tampoco perdonan. Si mezclas,
funciona en tu máquina y falla en cualquier otra parte. Minúsculas y se acabó.

### 3. Números con ceros a la izquierda

```
mal:   clip-1.mp4, clip-2.mp4, clip-10.mp4     ordena: 1, 10, 2
bien:  clip-01.mp4, clip-02.mp4, clip-10.mp4   ordena: 01, 02, 10
```

Dos dígitos hasta 99, tres si esperas más. El orden alfabético tiene que coincidir con el orden real,
porque es el que usan `Get-ChildItem`, `readdirSync` y la lista de `concat`.

### 4. Guion medio separa conceptos, guion bajo separa palabras del mismo concepto

```
v06-g1-9x16.mp4          version 06, gancho 1, formato 9x16
frasco_de_vidrio-duotono.png    concepto "frasco de vidrio", tratamiento duotono
```

Con esa convención puedes partir el nombre por `-` y obtener los campos. Es lo que hace que un manifiesto
se pueda generar automáticamente.

### 5. Fechas en ISO: `2026-08-04`

Nunca `04-08-2026` ni `4ago26`. La forma ISO ordena sola y no se confunde entre países.

### 6. Versiones con `v` y dos dígitos, y nunca "final"

```
mal:   final.mp4, final2.mp4, FINAL_BUENO.mp4, final_cliente_ok.mp4
bien:  v01-corte.mp4, v06-mezcla.mp4
```

`v06` no es un número de moral, es un contador. La versión que se entrega se marca en el manifiesto o se
copia a `entregas/`, no cambiándole el nombre a "final".

### 7. El nombre dice de dónde salió

Esta es la regla que más ahorra:

| Nombre | Se lee como |
|---|---|
| `b05-8f3a91c22e4d.mp4` | bloque b05, huella de sus insumos (módulo `132`) |
| `v06-g2-1x1.mp4` | versión 06, variante de gancho 2, formato cuadrado |
| `clip-07.jpg` en `hojas-contacto/` | la hoja de contactos de `clip-07.mp4` |
| `frasco-duotono.prompt.txt` | el prompt que generó `frasco-duotono.png` |

**Los nombres derivados nunca se escriben a mano.** Se calculan:

```js
// Un solo lugar decide como se llama cada cosa. Si el nombre se arma en tres
// scripts distintos, el dia que cambie la convencion quedan tres convenciones.
export const nombres = {
  segmento: (bloque, huella) => `${bloque}-${huella}.mp4`,
  hojaContacto: (clip) => clip.replace(/\.\w+$/, ".jpg"),
  promptDe: (imagen) => imagen.replace(/\.\w+$/, ".prompt.txt"),
  entrega: (version, variante, formato) =>
    `v${String(version).padStart(2, "0")}${variante ? "-" + variante : ""}-${formato}.mp4`,
};
```

---

## El bruto: renombrar sin tocar el original

El bruto llega con nombres de cámara (`IMG_4471.MOV`, `VID_20260731_141233.mp4`). Se renombra al ingresar,
pero **queda constancia de qué era cada uno**, porque el cliente va a hablar del "video del jueves".

```powershell
# ingestar.ps1 -- copia el bruto a entrada/ con nombres limpios y deja el mapa.
# COPIA, no mueve: el original se queda donde estaba hasta que el proyecto se entregue.

param(
  [Parameter(Mandatory=$true)][string]$Origen,
  [string]$Proyecto = (Get-Location).Path
)

$entrada = Join-Path $Proyecto "entrada"
New-Item -ItemType Directory -Force -Path $entrada | Out-Null

$archivos = Get-ChildItem "$Origen\*" -Include *.mp4,*.mov,*.MOV,*.MP4 | Sort-Object LastWriteTime
$mapa = @()
$i = 0

foreach ($a in $archivos) {
  $i++
  $nuevo = "clip-{0:D2}{1}" -f $i, $a.Extension.ToLower()
  $destino = Join-Path $entrada $nuevo

  if (Test-Path $destino) {
    Write-Output "YA EXISTE $nuevo. No se pisa. Revisa si estas ingestando dos veces."
    continue
  }
  Copy-Item $a.FullName $destino
  $mapa += [pscustomobject]@{
    nuevo    = $nuevo
    original = $a.Name
    grabado  = $a.LastWriteTime.ToString("yyyy-MM-dd HH:mm")
    mb       = [math]::Round($a.Length / 1MB, 1)
  }
  Write-Output ("{0}  <-  {1}" -f $nuevo, $a.Name)
}

$mapa | Export-Csv (Join-Path $Proyecto "analisis\mapa-ingesta.csv") -NoTypeInformation -Encoding utf8
Write-Output ("`n{0} clips en entrada/. Mapa en analisis/mapa-ingesta.csv" -f $mapa.Count)
```

Ordenar por fecha de grabación y no por nombre de cámara importa: así `clip-01` es de verdad lo primero
que se grabó, y la numeración cuenta la historia del rodaje.

---

## El verificador de nombres

Un script corto que caza las violaciones antes de que rompan un render:

```powershell
# revisar-nombres.ps1 -- caza nombres que van a romper algo mas adelante.
# Existe porque un espacio en un nombre no falla al copiarlo: falla tres pasos
# despues, dentro de una lista de concat, con un error que no menciona el espacio.

param([string]$Proyecto = (Get-Location).Path)

$problemas = 0
$carpetas = @("entrada", "assets", "subs", "segmentos", "salida")

foreach ($c in $carpetas) {
  $ruta = Join-Path $Proyecto $c
  if (-not (Test-Path $ruta)) { continue }

  Get-ChildItem $ruta -Recurse -File | ForEach-Object {
    $n = $_.Name

    if ($n -match "\s")             { Write-Output ("ESPACIO   {0}" -f $_.FullName); $problemas++ }
    if ($n -match "[áéíóúñÁÉÍÓÚÑ]") { Write-Output ("TILDE/N   {0}" -f $_.FullName); $problemas++ }
    if ($n -cmatch "[A-Z]")         { Write-Output ("MAYUSCULA {0}" -f $_.FullName); $problemas++ }
    if ($n -match "final|FINAL|nuevo|definitivo|ok_?bueno") {
      Write-Output ("NOMBRE MORAL  {0}  -> usa vNN" -f $_.FullName); $problemas++
    }
    if ($_.FullName.Length -gt 240) {
      Write-Output ("RUTA LARGA ({0} chars) {1}" -f $_.FullName.Length, $_.FullName)
      Write-Output ("          Windows corta en 260. Mueve el proyecto a una carpeta mas corta.")
      $problemas++
    }
  }
}

if ($problemas -eq 0) { Write-Output "Nombres limpios."; exit 0 }
Write-Output ("`n{0} problemas de nomenclatura. Arreglalos antes de montar." -f $problemas)
exit 1
```

---

## La trampa de Windows: 260 caracteres

Una ruta completa de más de 260 caracteres falla en Windows con un mensaje que no dice "es muy larga",
dice "no se encuentra el archivo" — y la ruta está ahí, en pantalla, existiendo.

Sumas rápido: `C:\Users\user\Desktop\CLIENTES\GASTROLATAM\CAMPANA-AGOSTO-2026\VIDEO-BOTELLA-VERTICAL\trabajo\segmentos\b05-8f3a91c22e4d.mp4` ya son 130. Con dos carpetas más de anidamiento, llegas.

Regla: **la raíz del proyecto, corta.** `C:\v\botella` es mejor que la ruta bonita y descriptiva. La
descripción va dentro, en un `README.md` de cinco líneas.

---

## La carpeta `assets/generado-ia/` y su regla especial

Todo lo generado por IA se guarda **con su prompt al lado**, mismo nombre base:

```
assets/generado-ia/
  frasco-duotono.png
  frasco-duotono.prompt.txt
  frasco-duotono.meta.json     modelo, fecha, costo, semilla si la hubo
```

Porque el modelo no da lo mismo dos veces (módulo `138`). Si pierdes el PNG, con el prompt tienes una
oportunidad de acercarte. Sin el prompt no tienes nada, y esa imagen costó dinero.

---

## Errores comunes

- **Espacios en los nombres.** No fallan al copiar; fallan tres pasos después, dentro de una lista de
  concat, con un error que no menciona el espacio.
- **Tildes y ñ en nombres de archivo.** Se corrompen al cruzar codificaciones y aparecen como `Ã­`.
- **Numerar sin ceros a la izquierda.** `clip-10` se ordena antes que `clip-2` y el montaje sale al revés.
- **`final.mp4`, `final2.mp4`, `FINAL_BUENO.mp4`.** Nadie sabe cuál es. Usa `vNN` y un manifiesto.
- **Escribir en `entrada/`.** El bruto es de solo lectura. Si un paso escribe ahí, algún día pisa material
  que no se puede recuperar.
- **Meter los segmentos dentro de `trabajo/`.** Borras el basurero y te llevas la caché por delante.
- **Armar el nombre derivado a mano en tres scripts distintos.** El día que cambias la convención quedan
  tres convenciones conviviendo.
- **Rutas de proyecto muy largas y anidadas.** Windows te tumba el render en el archivo con el nombre más
  largo, con un mensaje que no dice por qué.
- **Guardar una imagen de IA sin su prompt.** La imagen costó dinero y no se puede volver a producir igual.
- **No probar nunca a borrar `segmentos/` y `trabajo/`.** Es la única forma de saber si algo importante
  estaba viviendo en una carpeta borrable.
- **Renombrar el bruto sin dejar mapa.** El cliente dice "el del jueves" y nadie sabe cuál es.

---

## Checklist

- [ ] La estructura es igual en todos los proyectos, sin excepciones "porque este es distinto"
- [ ] `entrada/` es de solo lectura y ningún paso escribe ahí
- [ ] `segmentos/` está fuera de `trabajo/`
- [ ] Borrar `segmentos/` y `trabajo/` y correr el pipeline devuelve el mismo video (probado)
- [ ] Ningún nombre de archivo tiene espacios, tildes, ñ ni mayúsculas
- [ ] Los números llevan ceros a la izquierda y el orden alfabético coincide con el real
- [ ] Las fechas están en formato ISO `2026-08-04`
- [ ] No existe ningún archivo llamado `final`, `nuevo` o `definitivo`
- [ ] Los nombres derivados se calculan en un solo módulo, no a mano
- [ ] Cada entrega dice en el nombre su versión, variante y formato
- [ ] El bruto se ingestó con `ingestar.ps1` y existe `analisis/mapa-ingesta.csv`
- [ ] Cada archivo de `generado-ia/` tiene su `.prompt.txt` al lado
- [ ] La ruta completa más larga del proyecto está por debajo de 240 caracteres
- [ ] `revisar-nombres.ps1` corre sin problemas antes de montar

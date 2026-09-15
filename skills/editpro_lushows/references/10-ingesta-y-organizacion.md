# 10 — Ingesta y organización

## Qué resuelve

Que no se pierda nada y que dentro de tres semanas puedas volver al proyecto y entender qué es cada
archivo. El 80% del sufrimiento en edición no es creativo: es no encontrar la toma buena, sobrescribir
el archivo original, o tener seis versiones llamadas `final`, `final2`, `final_BUENO`.

**Ingesta** (en inglés *ingest*) es el paso de meter el material grabado al proyecto: copiarlo, revisarlo,
nombrarlo y respaldarlo antes de tocar nada. Es el equivalente a lavar y picar los ingredientes antes de
prender la estufa.

Regla que gobierna todo este módulo: **el bruto es sagrado y es de solo lectura.** El bruto (el material
tal como salió de la cámara o del celular) nunca se renombra en su sitio, nunca se recorta encima, nunca
se "arregla". Si lo tocas y algo sale mal, no hay vuelta atrás — no existe un botón de deshacer para un
archivo borrado.

---

## La estructura de carpetas

Una sola estructura, siempre igual, en todos los proyectos. La ventaja de repetirla no es estética: es
que puedes escribir scripts que funcionen en cualquier proyecto sin cambiar rutas.

```
PROYECTO/
  entrada/        el bruto tal como llego. SOLO LECTURA.
    clip-01.mp4
    clip-02.mp4
  analisis/       todo lo que yo genero para entender el bruto
    ficha-tecnica.json
    transcripcion.md
    hojas-contacto/
      clip-01.jpg
    mapa-bloques.csv
  assets/         lo que NO vino del rodaje
    musica/
    logos/
    fuentes/
    generado-ia/
  trabajo/        piezas intermedias: recortes, capas, pruebas
    cortes/
    subtitulos/
  salida/         lo que se entrega
    v01-corte-bruto.mp4
    v02-con-musica.mp4
    MASTER-9x16.mp4
```

Cuatro carpetas de primer nivel que se explican solas: `entrada` (lo que llegó), `analisis` (lo que
aprendí), `assets` (lo que traje), `salida` (lo que entrego). `trabajo` es el taller: se puede borrar
entero y reconstruir con los scripts.

### Por qué `analisis` es una carpeta y no notas sueltas

Porque el análisis del bruto cuesta dinero y tiempo (transcribir con IA, generar hojas de contacto,
medir audio). Si lo guardas en un chat, se pierde. Si lo guardas en `analisis/`, la segunda vez que
abras el proyecto arrancas donde quedaste.

---

## Crear la estructura de un golpe

PowerShell, Windows. Pégalo tal cual cambiando el nombre del proyecto:

```powershell
$proyecto = "C:\Users\user\Desktop\VIDEO-BOTELLA"
$carpetas = @(
  "entrada",
  "analisis\hojas-contacto",
  "assets\musica",
  "assets\logos",
  "assets\fuentes",
  "assets\generado-ia",
  "trabajo\cortes",
  "trabajo\subtitulos",
  "salida"
)
foreach ($c in $carpetas) {
  New-Item -ItemType Directory -Force -Path (Join-Path $proyecto $c) | Out-Null
}
Write-Output "Estructura creada en $proyecto"
```

---

## Nomenclatura: cómo se nombran los archivos

### El bruto

Se renombra **una sola vez**, al copiarlo, y con un patrón plano y ordenable:

```
clip-01.mp4
clip-02.mp4
...
clip-16.mp4
```

Sin espacios, sin tildes, sin paréntesis, sin emoji. Dos dígitos siempre (`01`, no `1`) para que el
orden alfabético coincida con el numérico. Los nombres de cámara tipo `IMG_4471.MOV` o
`VID_20260803_141255.mp4` no dicen nada y además rompen scripts cuando traen mayúsculas mezcladas.

Si el rodaje tiene varios días o varias cámaras:

```
d1-camA-clip-01.mp4
d1-camB-clip-01.mp4
d2-camA-clip-01.mp4
```

**No metas la descripción en el nombre.** `clip-07-la-buena-donde-habla-de-la-piedra.mp4` se ve útil el
primer día y es un desastre el tercero, porque la descripción cambia cuando entiendes mejor el material.
La descripción vive en el mapa de bloques (módulo 19), que sí se puede editar sin renombrar nada.

### La salida

Versión + qué es + formato:

```
v01-corte-bruto.mp4
v02-con-musica.mp4
v03-notas-cliente.mp4
MASTER-9x16.mp4
MASTER-1x1.mp4
```

Nunca `final`. `final` es una mentira que siempre se rompe. Los números no mienten. Detalle en
`96-versiones-y-nomenclatura.md`.

### Script de renombrado seguro

Este script copia (no mueve) desde la tarjeta o la carpeta de descargas hacia `entrada/`, renombrando en
orden por fecha de creación, y deja un registro de qué era cada cosa:

```powershell
$origen  = "C:\Users\user\Downloads\rodaje"
$destino = "C:\Users\user\Desktop\VIDEO-BOTELLA\entrada"
$registro = Join-Path $destino "_nombres-originales.csv"

New-Item -ItemType Directory -Force -Path $destino | Out-Null
$i = 0
$filas = @()
Get-ChildItem -Path $origen -Include *.mp4,*.mov,*.MP4,*.MOV -Recurse |
  Sort-Object CreationTime |
  ForEach-Object {
    $i++
    $nuevo = "clip-{0:D2}{1}" -f $i, $_.Extension.ToLower()
    Copy-Item $_.FullName (Join-Path $destino $nuevo)
    $filas += [PSCustomObject]@{
      nuevo    = $nuevo
      original = $_.Name
      creado   = $_.CreationTime.ToString("s")
      mb       = [math]::Round($_.Length / 1MB, 1)
    }
  }
$filas | Export-Csv -Path $registro -NoTypeInformation -Encoding utf8
Write-Output "$i clips copiados. Registro en $registro"
```

Tres cosas que hace bien este script y que importan:

1. **Copia, no mueve.** Si algo falla, la tarjeta sigue intacta.
2. **Ordena por fecha de creación**, no por nombre. El orden cronológico del rodaje es información: en un
   rodaje, la toma 5 casi siempre es mejor que la toma 1 (ver módulo 14).
3. **Deja el registro** `_nombres-originales.csv`. Si mañana el cliente dice "el archivo IMG_4471", sabes
   cuál es.

---

## Marcar el bruto como solo lectura

Es un seguro barato contra el error caro. En Windows:

```powershell
$entrada = "C:\Users\user\Desktop\VIDEO-BOTELLA\entrada"
Get-ChildItem -Path $entrada -File | ForEach-Object { $_.IsReadOnly = $true }
Write-Output "Bruto marcado como solo lectura"
```

Si después necesitas escribir ahí (raro, pero pasa), lo quitas con `$_.IsReadOnly = $false`.

---

## Respaldo: la regla 3-2-1 en versión realista

La regla profesional dice 3 copias, en 2 medios distintos, 1 fuera del sitio. Para un negocio pequeño la
versión práctica es:

| Copia | Dónde | Cuándo |
|---|---|---|
| 1 | Disco del computador (`entrada/`) | al ingestar |
| 2 | Disco externo o segunda unidad | el mismo día del rodaje |
| 3 | Nube (Drive, R2, S3) — solo el bruto y el máster | antes de borrar la tarjeta |

**No borres la tarjeta de la cámara hasta tener las copias 2 y 3.** Es la única regla de respaldo que hay
que memorizar. Una tarjeta llena cuesta 60 mil pesos; volver a montar un rodaje cuesta un día.

Verificar que la copia quedó bien no es mirar que "está el archivo": es comparar tamaño y hash.

```powershell
$a = "C:\Users\user\Desktop\VIDEO-BOTELLA\entrada"
$b = "E:\respaldo\VIDEO-BOTELLA\entrada"

$ha = Get-ChildItem $a -File | ForEach-Object { [PSCustomObject]@{ n=$_.Name; h=(Get-FileHash $_.FullName -Algorithm SHA256).Hash } }
$hb = Get-ChildItem $b -File | ForEach-Object { [PSCustomObject]@{ n=$_.Name; h=(Get-FileHash $_.FullName -Algorithm SHA256).Hash } }

foreach ($x in $ha) {
  $y = $hb | Where-Object { $_.n -eq $x.n }
  if ($null -eq $y) { Write-Output "FALTA en respaldo: $($x.n)" }
  elseif ($y.h -ne $x.h) { Write-Output "DIFERENTE: $($x.n)" }
}
Write-Output "Comparacion terminada"
```

**Hash** = una huella digital del archivo. Si dos archivos tienen el mismo hash, son idénticos byte por
byte. Es la única forma seria de decir "la copia está bien".

---

## Inventario: la primera tabla del proyecto

Antes de analizar nada a fondo, saca la lista de qué llegó. Con esto ya sabes si tienes 3 minutos o 30.

```powershell
$entrada = "C:\Users\user\Desktop\VIDEO-BOTELLA\entrada"
$filas = Get-ChildItem $entrada -Filter *.mp4 | Sort-Object Name | ForEach-Object {
  $dur = & ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 $_.FullName
  [PSCustomObject]@{
    clip     = $_.Name
    segundos = [math]::Round([double]$dur, 1)
    mb       = [math]::Round($_.Length / 1MB, 1)
  }
}
$filas | Format-Table -AutoSize
$total = ($filas | Measure-Object -Property segundos -Sum).Sum
Write-Output ("TOTAL: {0} clips, {1} minutos" -f $filas.Count, [math]::Round($total/60,1))
```

Este número — minutos totales de bruto — es el que define la estrategia. Un dato real de un proyecto:
**16 clips, 10 minutos de bruto, para 60 segundos de video final.** Relación 10:1. A esa proporción no
puedes "ver todo con calma": necesitas las herramientas de los módulos 13 y 17 (transcripción y hoja de
contactos) para mapear el material sin reproducirlo entero.

Guarda el inventario:

```powershell
$filas | Export-Csv "C:\Users\user\Desktop\VIDEO-BOTELLA\analisis\inventario.csv" -NoTypeInformation -Encoding utf8
```

---

## Qué hacer con el material que llega mal

| Situación | Qué hacer |
|---|---|
| Llega por WhatsApp (comprimido, 480p) | Pide el original. WhatsApp destruye el video. Si no hay original, avísale al cliente ANTES de montar que la calidad final está limitada por la fuente. |
| Llega en `.MOV` de iPhone con HEVC | Se puede editar, pero conviene transcodificar a H.264 para trabajar. Ver `90-formatos-y-codecs.md`. |
| Llegan 40 GB por Drive | Descarga con el cliente de escritorio, no por el navegador: el navegador corrompe descargas grandes con más frecuencia. Verifica hash. |
| Vienen clips con el mismo nombre de cámaras distintas | Prefijo de cámara antes de renombrar (`camA-`, `camB-`). |
| Un clip no abre | No lo botes. Anótalo y sigue. Muchas veces es un archivo truncado que `ffmpeg -i roto.mp4 -c copy recuperado.mp4` rescata parcialmente. |

---

## El archivo de contexto del proyecto

Un solo archivo de texto en la raíz, `CONTEXTO.md`, que responde lo que dentro de un mes no vas a
recordar:

```markdown
# VIDEO-BOTELLA

Cliente: Bendita Pola
Fecha rodaje: 2026-08-02
Entregable: 1 reel 9:16 de 60 s para Instagram + version 1:1 para Meta Ads
Quien aparece: Luis (dueño)
Marca: paleta y tipografia en assets/logos/manual-marca.pdf
Musica: licencia comprada, factura en assets/musica/_licencia.pdf
Fecha limite: 2026-08-08

## Material
16 clips, 10 minutos de bruto. Grabado con iPhone vertical, luz de tarde.
Audio: microfono de solapa en clips 01-10, microfono del telefono en 11-16 (peor).

## Decisiones tomadas
- 2026-08-04: el gancho sale del clip 12 (la piedra de los 12 angulos), no del clip 01.
```

Ese archivo es el que hace que el proyecto sea retomable. Cuesta cinco minutos escribirlo y ahorra horas.

---

## Errores comunes

- **Editar sobre el bruto.** Recortar, rotar o "arreglar" el archivo original destruye la única copia
  buena. El bruto es de solo lectura, siempre.
- **Borrar la tarjeta antes de verificar el respaldo.** Ver que el archivo aparece en el explorador no es
  verificar. Verificar es comparar tamaño y hash.
- **Nombres con tildes, espacios y emoji.** Rompen ffmpeg, rompen los scripts, rompen las listas de
  concat. `clip-01.mp4` no falla nunca; `Toma buena (la mejor) ñ.mp4` falla en algún punto siempre.
- **Meter la descripción en el nombre del archivo.** La descripción cambia; el nombre no debería.
  La descripción vive en la tabla, no en el sistema de archivos.
- **Un solo dígito en la numeración.** `clip-1, clip-2, ..., clip-10` se ordena como
  `clip-1, clip-10, clip-2`. Siempre dos dígitos.
- **Mezclar assets con bruto.** El logo, la música y lo generado por IA no son material de rodaje. Si se
  mezclan, un día vas a "limpiar el bruto" y borrar la música licenciada.
- **No dejar registro de los nombres originales.** El cliente siempre pregunta por un archivo con el
  nombre de la cámara.
- **Trabajar directo desde la tarjeta SD o desde Drive montado.** Es lento y una desconexión a mitad de
  render arruina el archivo de salida. Copia primero al disco local.
- **Nombrar el entregable `final`.** Siempre hay un `final_v2`. Usa números de versión.

---

## Checklist

Antes de pasar al análisis técnico (módulo 11), confirma:

- [ ] Existe la estructura `entrada/ analisis/ assets/ trabajo/ salida/`
- [ ] El bruto está copiado (no movido) a `entrada/`
- [ ] Los clips están renombrados `clip-NN.ext`, dos dígitos, sin tildes ni espacios
- [ ] Existe `_nombres-originales.csv` con el mapeo al nombre de cámara
- [ ] El bruto está marcado como solo lectura
- [ ] Hay copia en un segundo medio (disco externo) verificada por hash
- [ ] Hay copia en nube del bruto, o está agendada antes de borrar la tarjeta
- [ ] Existe `analisis/inventario.csv` con clip, segundos y MB
- [ ] Sabes el número total: cuántos minutos de bruto para cuántos segundos de entregable
- [ ] Existe `CONTEXTO.md` con cliente, entregable, marca, música y fecha límite
- [ ] Los assets (música, logos, fuentes, IA) están fuera de `entrada/`
- [ ] Si hay material dañado o de mala calidad, está anotado y el cliente avisado

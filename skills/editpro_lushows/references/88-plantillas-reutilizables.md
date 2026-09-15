# 88 — Plantillas reutilizables

**Qué resuelve:** la segunda vez que armas el mismo rótulo, la misma entrada de logo o el mismo bloque
de dato, ya perdiste. Este módulo enseña a construir una pieza de motion **una sola vez**, dejarla
parametrizada (color, texto, duración, posición) y reusarla cien veces sin volver a pensar. Es la
diferencia entre editar videos y tener un sistema que produce videos.

---

## 1. Qué es una plantilla en este contexto

> **Plantilla:** un fragmento de trabajo ya resuelto donde lo único que cambia son **valores**, no
> estructura. Le pasas el texto, el color y el momento; te devuelve la pieza terminada, idéntica en
> calidad a la anterior.

No es un preset de CapCut ni un archivo de After Effects. Aquí una plantilla es tres cosas juntas:

1. **Una cadena de filtros de ffmpeg** con huecos donde van los valores.
2. **Un script** (PowerShell o Bash) que rellena esos huecos.
3. **Una tabla de valores por defecto** — los números buenos, ya decididos, que no se vuelven a discutir.

La tercera es la que más valor tiene y la que casi todos olvidan. La plantilla no solo te ahorra
escribir: **te ahorra volver a tomar decisiones que ya tomaste bien.**

---

## 2. Qué se parametriza y qué NO

Este es el criterio central del módulo. Parametrizar de más es tan malo como no parametrizar.

| Parametriza | No parametrices |
|---|---|
| Texto | La curva de animación |
| Color de marca | El desfase entre elementos (0,08 s) |
| Momento de entrada (`t`) | La duración de la entrada (0,35 s) |
| Duración en pantalla | El margen de seguridad |
| Posición (arriba / centro / abajo) | La tipografía |
| Archivo de entrada y de salida | El tamaño relativo |

**La razón:** lo que parametrizas es lo que cambia entre videos. La curva, el desfase y el timing son
**la identidad del motion de esa marca**: si los dejas ajustables, en el video 7 alguien los va a tocar
y se rompe la coherencia. Se congelan a propósito.

> **Regla:** parametriza el CONTENIDO, congela el CARÁCTER.

---

## 3. La plantilla más simple: variables en un script

Empieza así. No hace falta más al principio.

### En Bash

```bash
#!/usr/bin/env bash
set -euo pipefail

# ---- parametros del video ----
ENTRADA="bruto/clip01.mp4"
SALIDA="salidas/reel_01.mp4"
TEXTO="Sin costos, no hay negocio"
COLOR="0x2742F5"
T_IN="1.20"
DURACION="2.60"
POS_Y="1180"

# ---- caracter de marca (NO tocar) ----
FUENTE="C\\:/Windows/Fonts/Poppins-Bold.ttf"
TAM=78
ENTRADA_DUR=0.28
MARGEN=64

T_OUT=$(awk "BEGIN{print $T_IN + $DURACION}")

ffmpeg -y -i "$ENTRADA" -filter_complex "\
[0:v]drawbox=x=$MARGEN:y=$((POS_Y-24)):w='min(iw-2*$MARGEN, 940)':h=124:color=${COLOR}@0.92:t=fill:\
enable='between(t,$T_IN,$T_OUT)',\
drawtext=fontfile='$FUENTE':text='$TEXTO':fontsize=$TAM:fontcolor=white:\
x=$((MARGEN+32)):y=$POS_Y:\
alpha='clip((t-$T_IN)/$ENTRADA_DUR,0,1)*clip(($T_OUT-t)/0.20,0,1)'[vout]" \
  -map "[vout]" -map 0:a -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p "$SALIDA"
```

### En PowerShell (Windows)

```powershell
$Entrada  = "bruto\clip01.mp4"
$Salida   = "salidas\reel_01.mp4"
$Texto    = "Sin costos, no hay negocio"
$Color    = "0x2742F5"
$TIn      = 1.20
$Duracion = 2.60
$PosY     = 1180

# caracter de marca (NO tocar)
$Fuente  = "C\:/Windows/Fonts/Poppins-Bold.ttf"
$Tam     = 78
$EntDur  = 0.28
$Margen  = 64

$TOut = $TIn + $Duracion
$Filtro = "[0:v]drawbox=x=${Margen}:y=$($PosY-24):w='min(iw-2*$Margen,940)':h=124:color=${Color}@0.92:t=fill:enable='between(t,$TIn,$TOut)',drawtext=fontfile='$Fuente':text='$Texto':fontsize=${Tam}:fontcolor=white:x=$($Margen+32):y=${PosY}:alpha='clip((t-$TIn)/$EntDur,0,1)*clip(($TOut-t)/0.20,0,1)'[vout]"

& ffmpeg -y -i $Entrada -filter_complex $Filtro -map "[vout]" -map 0:a -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p $Salida
```

**Ojo con la coma decimal.** En un Windows configurado en español, `$TIn + $Duracion` puede imprimirse
como `3,8` en vez de `3.8` y ffmpeg no lo entiende. Fuerza el formato:

```powershell
$TOut = ($TIn + $Duracion).ToString([System.Globalization.CultureInfo]::InvariantCulture)
```

Este bug se lleva media hora la primera vez y es invisible: el filtro simplemente no se activa.

---

## 4. Separar el filtro del script: `-filter_complex_script`

Cuando el filtro pasa de diez líneas, meterlo en una variable del script es infierno para depurar.
ffmpeg permite leerlo de un archivo:

```bash
ffmpeg -y -i entrada.mp4 -filter_complex_script filtros/rotulo.txt \
  -map "[vout]" -map 0:a -c:a copy -c:v libx264 -crf 18 salida.mp4
```

Y `filtros/rotulo.txt` es un archivo de texto plano con la cadena, que sí puede tener saltos de línea
para leerse cómodo.

**La trampa que cuesta una tarde:** ese archivo **no puede tener BOM**. Si lo generas en PowerShell con
`Set-Content -Encoding utf8` o con `>`, Windows le mete tres bytes invisibles al principio y ffmpeg
falla con un error que no dice nada útil. Es el mismo problema que rompe las listas de `concat`
(ver `109`).

```powershell
# Correcto: UTF-8 SIN BOM
$utf8SinBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText("$PWD\filtros\rotulo.txt", $Filtro, $utf8SinBom)
```

### La plantilla con marcadores

El archivo de filtro se escribe con marcadores y el script los reemplaza:

`filtros/rotulo.tpl`:
```
[0:v]drawbox=x={MARGEN}:y={BOXY}:w=940:h=124:color={COLOR}@0.92:t=fill:enable='between(t,{TIN},{TOUT})',
drawtext=fontfile='{FUENTE}':text='{TEXTO}':fontsize=78:fontcolor=white:
x={TEXTOX}:y={POSY}:
alpha='clip((t-{TIN})/0.28,0,1)*clip(({TOUT}-t)/0.20,0,1)'[vout]
```

```powershell
$tpl = Get-Content "filtros\rotulo.tpl" -Raw
$filtro = $tpl -replace '\{TEXTO\}', $Texto -replace '\{COLOR\}', $Color `
               -replace '\{TIN\}', $TIn -replace '\{TOUT\}', $TOut `
               -replace '\{POSY\}', $PosY -replace '\{MARGEN\}', $Margen `
               -replace '\{BOXY\}', ($PosY-24) -replace '\{TEXTOX\}', ($Margen+32) `
               -replace '\{FUENTE\}', $Fuente
$filtro = $filtro -replace "`r`n", ""
```

El último `-replace` quita los saltos de línea antes de pasárselo a ffmpeg si lo vas a usar inline.
Si usas `-filter_complex_script`, los saltos se pueden quedar.

---

## 5. El manifiesto: una tabla que produce el video

El salto de calidad viene cuando dejas de correr el script a mano por cada rótulo y describes el video
entero como **datos**. Es la idea de "la línea como dato" (`131`).

`piezas/reel_01.csv`:
```
tipo,texto,t_in,duracion,pos
rotulo,Sin costos no hay negocio,1.20,2.60,bajo
dato,78,6.40,3.20,centro
rotulo,Calculadora de costos,12.10,2.80,bajo
```

Y el script recorre la tabla y encadena:

```bash
#!/usr/bin/env bash
set -euo pipefail
IN="bruto/clip01.mp4"; OUT="salidas/reel_01.mp4"
CADENA="[0:v]"; N=0

while IFS=, read -r TIPO TEXTO TIN DUR POS; do
  [ "$TIPO" = "tipo" ] && continue
  TOUT=$(awk "BEGIN{print $TIN + $DUR}")
  case "$POS" in
    bajo)   Y=1180 ;;
    centro) Y=900  ;;
    alto)   Y=520  ;;
  esac
  N=$((N+1))
  CADENA="${CADENA}drawtext=fontfile='C\\:/Windows/Fonts/Poppins-Bold.ttf':text='${TEXTO}':fontsize=78:fontcolor=white:borderw=5:bordercolor=black@0.5:x=(w-text_w)/2:y=${Y}:alpha='clip((t-${TIN})/0.28,0,1)*clip((${TOUT}-t)/0.20,0,1)',"
done < piezas/reel_01.csv

CADENA="${CADENA%,}[vout]"

ffmpeg -y -i "$IN" -filter_complex "$CADENA" -map "[vout]" -map 0:a -c:a copy \
  -c:v libx264 -crf 18 -pix_fmt yuv420p "$OUT"
```

**Por qué esto vale tanto:** para hacer el video 2, no tocas el script. Escribes otro CSV. Y cuando el
cliente pide "cambia el segundo rótulo", editas una celda y vuelves a correr. Sin rehacer nada.

---

## 6. La biblioteca de plantillas: qué construir primero

No construyas veinte. Construye estas seis, que son las que se repiten en todo proyecto de marca:

| Plantilla | Qué hace | Módulo de referencia |
|---|---|---|
| `rotulo` | pastilla de color + texto, entra y sale | `48` |
| `palabra-clave` | palabra grande centrada con golpe | `42` |
| `dato` | número gigante + etiqueta + respiro | `86` |
| `firma` | marca de agua en esquina segura, intermitente | `87` |
| `entrada-logo` | logo con anticipación y sobre-impulso | `84`, `85` |
| `remate` | cierre de marca: fondo + logo + CTA | `33` |

Con esas seis armas el 90% de las piezas. Guárdalas en una carpeta con esta estructura:

```
plantillas/
  rotulo/
    filtro.tpl
    valores.json      <- los defaults congelados
    ejemplo.png       <- como se ve, para no adivinar
  dato/
  firma/
  ...
```

El `ejemplo.png` es clave: en seis meses no vas a recordar qué hace `rotulo-b`. Un fotograma lo resuelve.

---

## 7. El archivo de marca: un solo lugar para el color

Nunca escribas `0x2742F5` dentro de una plantilla. Va en un archivo de marca, y todas las plantillas lo
leen. El día que la marca cambie de color (y va a pasar), cambias un archivo.

`marca/gastrolatam.json`:
```
{
  "nombre": "GastroLatam",
  "color_primario": "0x2742F5",
  "color_texto": "0xFFFFFF",
  "color_apoyo": "0x111318",
  "fuente_titulo": "C:/Windows/Fonts/Poppins-Bold.ttf",
  "fuente_texto": "C:/Windows/Fonts/Poppins-Medium.ttf",
  "margen": 64,
  "logo": "marca/logo_blanco.png"
}
```

```powershell
$M = Get-Content "marca\gastrolatam.json" -Raw | ConvertFrom-Json
$Color = $M.color_primario
$Fuente = $M.fuente_titulo -replace ':', '\:'
```

Ese `-replace ':', '\:'` es necesario: `drawtext` usa `:` como separador de parámetros, así que la
`C:` de una ruta de Windows hay que escaparla. Es el error número uno de `drawtext` en Windows.

---

## 8. Versionar las plantillas

Una plantilla que cambia sin control te rompe la coherencia de una campaña a la mitad.

- **Guarda las plantillas en el repositorio del proyecto**, no en el escritorio.
- **Cuando cambies una, cambia el nombre o la versión**: `rotulo_v2.tpl`. Los videos ya entregados se
  hicieron con `v1` y si mañana hay que rehacer uno, tiene que salir idéntico.
- **Anota en el JSON de valores qué cambió y cuándo.** Una línea.
- **No borres la versión vieja.** Pesa 2 KB.

Esto no es burocracia: es lo que permite que la pieza 12 de una campaña se vea hermana de la 1 (`37`,
`159`).

---

## 9. Cuándo NO usar plantilla

Sé honesto con el límite:

- **La primera vez.** Construir la plantilla cuesta 3–5 veces lo que cuesta hacer la pieza a mano. Si es
  una sola vez, hazla a mano. La plantilla se paga a partir de la tercera repetición.
- **Cuando el video es el concepto.** Una pieza de autor, un remate único, un chiste visual: eso no se
  plantilla. La plantilla es para lo que se repite, no para lo que se inventa.
- **Cuando todavía no sabes cómo debe verse.** No parametrices algo que no has resuelto. Primero
  resuélvelo a mano hasta que quede bien; **después** congélalo. Parametrizar una decisión mala la
  multiplica por cien.
- **Cuando el cliente cambia de criterio cada pieza.** Ahí la plantilla te pelea. Primero se cierra el
  criterio (`181`), después se automatiza.

---

## Errores comunes

1. **Parametrizar la curva y el timing.** Eso es el carácter de la marca. Se congela. Si es ajustable,
   alguien lo va a ajustar y se rompe la coherencia.
2. **Construir la plantilla antes de resolver la pieza a mano.** Multiplicas por cien una decisión que
   todavía no estaba bien.
3. **Escribir el color de marca dentro de cada plantilla.** El día que cambie, tocas veinte archivos.
   Va en el archivo de marca.
4. **BOM en el archivo de filtro.** ffmpeg falla con un error que no dice nada. `UTF8Encoding($false)`.
5. **No escapar los `:` de las rutas de Windows en `drawtext`.** `C:/...` rompe el filtro. Va `C\:/...`.
6. **Coma decimal en PowerShell con configuración regional en español.** `3,8` no es `3.8` para ffmpeg,
   y el filtro simplemente no se activa. Fuerza `InvariantCulture`.
7. **Olvidar quitar la coma final de la cadena** cuando encadenas filtros en un bucle. ffmpeg falla con
   "Invalid filtergraph".
8. **No guardar un `ejemplo.png` de cada plantilla.** En tres meses no vas a saber cuál es cuál.
9. **Modificar una plantilla en medio de una campaña sin versionarla.** La pieza 9 deja de parecerse a
   la 1 y nadie sabe por qué.
10. **Parametrizar de más.** Una plantilla con 22 parámetros no es una plantilla: es el trabajo otra vez,
    pero con sintaxis peor.
11. **Guardar las plantillas fuera del repositorio.** Se pierden, se pisan, o quedan solo en un
    computador.
12. **Correr la plantilla sin verificar el resultado.** Automatizar sin verificar es producir errores más
    rápido (`98`, `133`).

---

## Checklist

Antes de dar por buena una plantilla:

- [ ] La pieza ya la resolví **a mano** y quedó bien antes de parametrizarla.
- [ ] Parametricé el **contenido** (texto, color, tiempos, posición) y congelé el **carácter** (curvas,
      desfases, tipografía, márgenes).
- [ ] El color y la tipografía salen del **archivo de marca**, no están escritos dentro.
- [ ] Las rutas de Windows llevan los `:` **escapados** en `drawtext`.
- [ ] Los números decimales se generan con **punto**, no con coma (InvariantCulture).
- [ ] Si uso `-filter_complex_script`, el archivo está en **UTF-8 sin BOM**.
- [ ] La cadena encadenada **no termina en coma**.
- [ ] La plantilla tiene su **`ejemplo.png`** y su archivo de valores por defecto.
- [ ] Está **versionada** y guardada en el repositorio del proyecto.
- [ ] Corrí la plantilla con **dos juegos de valores distintos** y ambos salieron bien.
- [ ] Verifiqué el resultado con `98` antes de darla por lista.
- [ ] Si esto se hace una sola vez, **decidí no hacer plantilla** y lo hice a mano.

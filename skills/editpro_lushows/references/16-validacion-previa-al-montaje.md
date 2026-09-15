# 16 — Validación previa al montaje (la compuerta)

## Qué resuelve

Que ningún corte defectuoso llegue al render. Este módulo existe por una lección grande, aprendida en un
proyecto real y a un costo alto:

> **Corregir cortes de a uno, cada vez que el verificador encuentra una palabra partida DESPUÉS de
> renderizar, es un ciclo infinito.**

El patrón que se vivió: se montó el video, se verificó, apareció una palabra cortada, se arregló ese
corte, se volvió a renderizar (8 minutos), se volvió a verificar, apareció otra palabra cortada, se
arregló, se renderizó... cinco vueltas. Cada vuelta cuesta el render completo, la revisión completa y la
atención completa. Y como cada arreglo mueve la línea de tiempo, cada vuelta puede crear un defecto nuevo.

La solución no es verificar mejor al final. Es **una compuerta**: un paso obligatorio que revisa **todos**
los cortes **antes** de armar nada, y que no deja pasar hasta que todos estén limpios o justificados.

**Compuerta** (en inglés *gate*): un punto del proceso que solo se cruza si se cumple una condición.
Aquí la condición es "cero cortes rojos sin justificar".

---

## La diferencia entre validar y verificar

| | Validación previa (módulo 16) | Verificación final (módulo 98) |
|---|---|---|
| Cuándo | antes de montar | después de renderizar |
| Sobre qué | la tabla de cortes | el archivo terminado |
| Qué caza | palabras partidas, tramos imposibles, tiempos que no cuadran | color, texto fuera de zona segura, audio, ritmo, el resultado real |
| Costo de un fallo | reescribir una fila del CSV | rehacer el render |

Las dos hacen falta. Pero si la validación previa hace su trabajo, la verificación final casi nunca
devuelve el proyecto al principio.

---

## Las siete reglas de la compuerta

Cada corte de la tabla `analisis/cortes.csv` (formato del módulo 15) tiene que pasar estas siete:

| # | Regla | Falla si |
|---|---|---|
| R1 | El clip existe | no hay archivo con ese nombre en `entrada/` |
| R2 | El tramo cabe en el clip | `fin` mayor que la duración real medida con ffprobe |
| R3 | Los números son coherentes | `inicio` negativo, `fin` menor o igual a `inicio`, `duracion` distinta de `fin - inicio` |
| R4 | La entrada no arranca a mitad de palabra | `se_oye_antes` termina en palabra partida, o el texto del bloque empieza en minúscula a mitad de frase |
| R5 | La salida no corta una palabra | `se_oye_despues` empieza con conjunción, con palabra partida, o el bloque termina sin puntuación |
| R6 | Hay aire suficiente | menos de 0,10 s entre el fin de la última palabra y el punto de corte |
| R7 | La duración es razonable | menos de 0,8 s (imposible decir algo) o más de 15 s (no es un bloque, es un clip entero) |

R4 y R5 son las que cazan la palabra partida, que es el defecto que generaba el ciclo infinito.

---

## El script de la compuerta

PowerShell. Lee la tabla de cortes, aplica las siete reglas, imprime un informe y **propone el arreglo**
en vez de solo quejarse.

```powershell
param(
  [string]$Proyecto = "C:\Users\user\Desktop\VIDEO-BOTELLA"
)

$cortes  = Join-Path $Proyecto "analisis\cortes.csv"
$entrada = Join-Path $Proyecto "entrada"

$conjunciones = @("y","e","o","u","pero","porque","que","cuando","donde","si","aunque","como","para","con","de","del","al","en","la","el","los","las","un","una","su","sus","le","lo","se","ni","mas","tambien")

$duraciones = @{}
function Get-Duracion([string]$archivo) {
  if ($duraciones.ContainsKey($archivo)) { return $duraciones[$archivo] }
  $p = Join-Path $entrada $archivo
  if (-not (Test-Path $p)) { $duraciones[$archivo] = -1; return -1 }
  $d = [double](& ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 $p)
  $duraciones[$archivo] = $d
  return $d
}

$rojos = 0
$amarillos = 0

Import-Csv $cortes | ForEach-Object {
  $f = $_
  $b = $f.bloque
  $ini = [double]$f.inicio
  $fin = [double]$f.fin
  $dur = [double]$f.duracion
  $antes   = ("" + $f.se_oye_antes).Trim()
  $despues = ("" + $f.se_oye_despues).Trim()
  $texto   = ("" + $f.texto).Trim()

  $dclip = Get-Duracion $f.clip

  # R1
  if ($dclip -lt 0) {
    Write-Output ("ROJO   {0}  R1 no existe el clip {1}" -f $b, $f.clip)
    Write-Output ("       ARREGLO: revisa el nombre en entrada/ o corrige la fila")
    $rojos++
    return
  }

  # R2
  if ($fin -gt $dclip) {
    Write-Output ("ROJO   {0}  R2 pide hasta {1} s pero {2} dura {3} s" -f $b, $fin, $f.clip, [math]::Round($dclip,2))
    Write-Output ("       ARREGLO: el tramo no existe. Busca el bloque en otro clip o corrige el timecode.")
    $rojos++
  }

  # R3
  if ($ini -lt 0 -or $fin -le $ini) {
    Write-Output ("ROJO   {0}  R3 numeros incoherentes: inicio {1}, fin {2}" -f $b, $ini, $fin)
    Write-Output ("       ARREGLO: fin debe ser mayor que inicio y ambos positivos")
    $rojos++
  }
  elseif ([math]::Abs(($fin - $ini) - $dur) -gt 0.05) {
    Write-Output ("ROJO   {0}  R3 duracion declarada {1} s, calculada {2} s" -f $b, $dur, [math]::Round($fin-$ini,2))
    Write-Output ("       ARREGLO: pon duracion = {0}" -f [math]::Round($fin-$ini,2))
    $rojos++
  }

  # R4 entrada a mitad de palabra
  if ($antes -ne "" -and $antes -notmatch "SILENCIO|RISA|OTRA VOZ|RUIDO") {
    $ultima = ($antes -split "\s+")[-1]
    if ($ultima -match "-$" -or $texto -cmatch "^[a-zñáéíóú]") {
      Write-Output ("ROJO   {0}  R4 entra a mitad de frase. Antes se oye: '{1}'" -f $b, $antes)
      Write-Output ("       ARREGLO: adelanta el inicio a la pausa anterior, o baja el inicio 0.3 s y vuelve a revisar")
      $rojos++
    }
  }

  # R5 salida corta palabra  <- la que causaba el ciclo infinito
  if ($despues -ne "") {
    $primera = (($despues -split "\s+")[0]).ToLower().Trim(".,;:!?")
    $cortaPalabra = $primera -match "^-" -or $primera.Length -le 2 -and $primera -notmatch "^\[" 
    if ($conjunciones -contains $primera -or $cortaPalabra) {
      Write-Output ("ROJO   {0}  R5 el corte parte la frase. Despues se oye: '{1}'" -f $b, $despues)
      Write-Output ("       ARREGLO: extiende el fin hasta el proximo silencio. Prueba fin = {0}" -f [math]::Round($fin + 1.0, 1))
      $rojos++
    }
    elseif ($texto -notmatch "[\.\!\?]$" -and $despues -notmatch "SILENCIO") {
      Write-Output ("AMARILLO {0}  R5 el bloque no cierra con puntuacion y despues sigue hablando" -f $b)
      Write-Output ("       REVISA: puede ser intencional (frase encadenada) o un corte corto")
      $amarillos++
    }
  }

  # R6 aire
  if ($despues -match "^\[SILENCIO (\d+)\]") { } # hay silencio, hay aire
  elseif ($dur -lt 1.2 -and $despues -ne "") {
    Write-Output ("AMARILLO {0}  R6 bloque muy pegado, revisa el aire de salida" -f $b)
    $amarillos++
  }

  # R7 duracion razonable
  if ($dur -lt 0.8) {
    Write-Output ("ROJO   {0}  R7 duracion {1} s: demasiado corto para decir algo" -f $b, $dur)
    Write-Output ("       ARREGLO: revisa si el timecode esta mal o si el bloque sobra")
    $rojos++
  }
  elseif ($dur -gt 15) {
    Write-Output ("AMARILLO {0}  R7 duracion {1} s: eso no es un bloque, es un clip entero" -f $b, $dur)
    $amarillos++
  }
}

Write-Output ""
Write-Output ("=== COMPUERTA: {0} rojos, {1} amarillos ===" -f $rojos, $amarillos)
if ($rojos -gt 0) {
  Write-Output "NO SE MONTA. Corrige los rojos en analisis/cortes.csv y vuelve a correr."
  exit 1
} else {
  Write-Output "Compuerta abierta. Se puede montar."
  exit 0
}
```

Tres decisiones de diseño que importan:

1. **Sale con código 1 si hay rojos.** Así se puede encadenar con el script de montaje: si la compuerta
   falla, el montaje ni siquiera arranca. En PowerShell 5.1 no hay `&&`, así que se encadena con:
   ```powershell
   .\compuerta.ps1; if ($?) { .\montar.ps1 }
   ```
2. **Propone el arreglo, no solo el error.** Un informe que dice "R5 falló" te obliga a pensar. Uno que
   dice "prueba fin = 50.9" te deja corregir en diez segundos.
3. **Distingue rojo de amarillo.** El rojo bloquea. El amarillo pide un ojo humano. Sin esa distinción,
   o bloqueas por tonterías o dejas pasar defectos.

---

## Falsos positivos: el blooper cortado a propósito

Aquí está la parte fina. La compuerta va a marcar en rojo cortes que están **bien**, porque el defecto
que detecta es exactamente el efecto que buscas. Los tres casos típicos:

| Caso | Por qué la compuerta lo marca | Por qué está bien |
|---|---|---|
| **Blooper cortado en seco** | R5: la frase sigue | el chiste ES que se corte a mitad. Ver `34-el-blooper-como-estructura` |
| **Frase encadenada entre bloques** | R5: `se_oye_despues` empieza con "y" | el bloque siguiente continúa esa frase, el corte es solo de imagen |
| **Gancho que entra a mitad de acción** | R4: entra en minúscula, sin arranque | *in medias res*: empezar en el medio es una técnica de gancho, no un error |

La compuerta no puede distinguirlos sola. Por eso existe la columna `intencional`:

```csv
bloque,texto,clip,inicio,fin,duracion,se_oye_antes,se_oye_despues,intencional,motivo_intencional
b07,"Espera, no, otra vez—",clip-09,12.4,14.1,1.7,"[SILENCIO]","perdon perdon ya",si,"blooper: el corte en seco es el remate"
b02,"Vidrio reciclado. Todo.",clip-03,44.1,49.9,5.8,"a ver otra vez","porque cada botella",si,"la frase sigue en b03, corte solo de imagen"
```

Y la compuerta la respeta, pero **con condición**: no basta con marcar `si`, hay que escribir el motivo.

```powershell
# Dentro del bucle, antes de contar el rojo:
if ($f.intencional -eq "si") {
  if (("" + $f.motivo_intencional).Trim().Length -lt 10) {
    Write-Output ("ROJO   {0}  marcado intencional pero sin motivo escrito" -f $b)
    $rojos++
  } else {
    Write-Output ("EXCEPCION {0}  intencional: {1}" -f $b, $f.motivo_intencional)
  }
  return
}
```

**Por qué exigir el motivo escrito:** porque marcar `intencional=si` es la salida fácil, y sin fricción se
usa para silenciar errores reales. Obligar a escribir por qué convierte la excepción en una decisión
consciente. Si al escribirla no se te ocurre un motivo, es que era un error.

Regla práctica: **si el video tiene más de 2 o 3 excepciones intencionales, algo está mal.** O el material
está muy roto, o se está usando la excepción para no corregir.

---

## Diferenciar en la práctica: cuatro preguntas

Cuando la compuerta marca algo y no sabes si es error o efecto:

1. **¿El corte en seco produce una reacción?** (risa, sorpresa, tensión) → intencional.
2. **¿Se entiende igual la idea sin lo que se cortó?** Si no se entiende, es error.
3. **¿Un espectador que no sabe nada notaría que "faltó algo"?** Si la respuesta es sí y no es el chiste,
   es error.
4. **¿Puedes escribir el motivo en una línea sin sonar a excusa?** Si no, es error.

---

## Qué hacer cuando la compuerta encuentra 12 rojos

No los arregles de a uno en el orden en que salieron. Agrúpalos, porque casi siempre tienen dos o tres
causas raíz:

| Patrón | Causa raíz probable | Arreglo de raíz |
|---|---|---|
| Muchos R2 en el mismo clip | los timecodes de ese clip están corridos (transcripción mala) | retranscribir ese clip y rehacer todas sus filas |
| Muchos R5 en todo el proyecto | se pidieron cortes sin `se_oye_despues` y se ajustaron a ojo | volver a pedir los fines con el prompt del módulo 15 |
| Muchos R3 | error de dedo al copiar la tabla, o se editó `fin` sin editar `duracion` | recalcular la columna `duracion` entera por fórmula |
| R2 en un solo clip con desfase constante | el clip que se transcribió no es el mismo que está en `entrada/` | verificar hash y nombre |

Arreglar la causa raíz cuesta una vez. Arreglar 12 síntomas cuesta 12 veces y deja los que no viste.

---

## Dónde encaja la compuerta en el flujo

```
transcribir (13)
    v
seleccionar tomas (14)
    v
medir cortes (15)  ->  analisis/cortes.csv
    v
+-------------------------+
|  COMPUERTA (16)         |   si hay rojos: vuelve a 15. NO se monta.
+-------------------------+
    v
mapa de bloques (19)
    v
montar y renderizar
    v
verificacion final (98)
```

La flecha que importa es la de retorno: **de la compuerta se vuelve a la tabla, no al render.** Corregir
una fila de CSV cuesta segundos. Corregir después del render cuesta el render.

---

## Errores comunes

- **Verificar solo después de renderizar.** Es el ciclo infinito: cada arreglo obliga a otro render y
  puede crear un defecto nuevo. Se valida antes, todo junto.
- **Arreglar los cortes de a uno según van apareciendo.** Sin ver el conjunto no ves las causas raíz y
  arreglas doce síntomas del mismo problema.
- **Correr la compuerta y montar igual "porque son pocos rojos".** Un rojo es un defecto que va a llegar
  al cliente. La compuerta bloquea o no sirve de nada.
- **No exigir `se_oye_antes` / `se_oye_despues` en la tabla.** Sin esas columnas la compuerta no puede
  detectar la palabra partida, que es justo el defecto más caro.
- **Usar `intencional=si` sin motivo escrito.** Se convierte en el botón de silenciar errores.
- **Tener seis o siete excepciones intencionales.** Señal de que el material está roto o de que se está
  evadiendo la corrección.
- **Marcar como error un blooper cortado a propósito y "arreglarlo".** Se mata el chiste. Por eso existe
  la columna, y por eso la revisa un humano.
- **Correr la compuerta sobre una tabla desactualizada.** Si corregiste un corte en el montaje pero no en
  el CSV, validaste otra cosa. La tabla es la fuente de verdad, siempre.
- **No encadenar compuerta y montaje.** Si son dos pasos manuales, algún día se monta sin validar.

---

## Checklist

- [ ] Existe `analisis/cortes.csv` con todas las columnas, incluidas `se_oye_antes` y `se_oye_despues`
- [ ] Existe la columna `intencional` y la columna `motivo_intencional`
- [ ] El script de compuerta corre sobre la tabla completa, no sobre una parte
- [ ] La compuerta comprueba R1 a R7 en cada fila
- [ ] La compuerta devuelve código de salida 1 si hay rojos, y el montaje está encadenado a ese código
- [ ] El informe propone un arreglo concreto por cada rojo, no solo el nombre de la regla
- [ ] Cero rojos sin resolver antes de armar la primera pieza
- [ ] Cada excepción `intencional=si` tiene motivo escrito de al menos una línea
- [ ] Hay 3 o menos excepciones intencionales en todo el proyecto
- [ ] Los rojos se agruparon por patrón y se atacó la causa raíz, no cada síntoma
- [ ] Después de corregir, la compuerta se volvió a correr entera (no solo sobre las filas tocadas)
- [ ] La tabla refleja exactamente lo que se va a montar: no hay cortes ajustados solo en el script de render

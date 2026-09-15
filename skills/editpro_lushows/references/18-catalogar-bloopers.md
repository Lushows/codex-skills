# 18 — Catalogar bloopers

## Qué resuelve

Convertir en material lo que todo el mundo bota. En un rodaje real de 16 clips hubo **28 tomas falsas y
6 buenas**: el 83% del bruto fue "error". Botarlo es tirar a la basura el 83% de lo que se grabó — y
justo la parte donde la persona es más ella misma.

**Blooper** = una toma fallida: el que se equivoca, se ríe, se le olvida, se le cae algo, o le pasa algo
imprevisto. En español a veces "toma falsa" o "bloopers" a secas.

La idea central de este módulo: **el error retiene**. En video corto, un blooper bien puesto hace tres
cosas que ninguna toma perfecta hace — humaniza a quien habla, corta la sensación de comercial, y da un
remate que la gente comparte. Pero solo si está **catalogado y elegido**, no si se pegan todos al final.

---

## Dos usos distintos del blooper

Confundirlos es el error de fondo.

| Uso | Qué es | Dónde va | Cuánto |
|---|---|---|---|
| **Sazón** | un error de medio segundo dentro del video "serio" | en el cuerpo, después de un bloque denso | 1 o 2, muy cortos |
| **Remate** | el bloque cómico al final | después del cierre, antes o después del CTA | 3–6 s, o un arco de 8–12 s |

El uso de sazón es el más subestimado: un tropiezo de 0,4 s en el segundo 25 de un video informativo
resetea la atención mejor que cualquier transición. El uso de remate es el más conocido y el peor
ejecutado, porque casi siempre se pegan seis bloopers seguidos sin criterio.

---

## De dónde sale el catálogo

Del módulo 13. La transcripción marcada ya trae `>>TOMA FALSA` y `[RISA]` con su timecode. Ese es tu
inventario en bruto. Sacarlo a una tabla:

```powershell
$proyecto = "C:\Users\user\Desktop\VIDEO-BOTELLA"
$dir = Join-Path $proyecto "analisis\transcripciones"
$filas = @()

Get-ChildItem $dir -Filter *.md | Sort-Object Name | ForEach-Object {
  $clip = $_.BaseName
  Get-Content $_.FullName | ForEach-Object {
    $linea = $_
    if ($linea -match "^\[(\d+\.?\d*)\]") {
      $t = [double]$Matches[1]
      $tipo = $null
      if ($linea -match ">>TOMA FALSA") { $tipo = "falsa" }
      if ($linea -match "\[RISA\]")     { $tipo = "risa" }
      if ($tipo) {
        $filas += [PSCustomObject]@{
          clip = $clip
          seg  = $t
          tipo = $tipo
          texto = ($linea -replace "^\[\d+\.?\d*\]\s*", "" -replace ">>TOMA FALSA\s*", "")
          gracia = ""
          categoria = ""
          usable = ""
        }
      }
    }
  }
}
$out = Join-Path $proyecto "analisis\bloopers.csv"
$filas | Export-Csv $out -NoTypeInformation -Encoding utf8
Write-Output ("{0} candidatos a blooper -> {1}" -f $filas.Count, $out)
```

Las columnas `gracia`, `categoria` y `usable` se llenan a mano (o con un modelo). Esa es la parte que
convierte un inventario en un catálogo.

---

## Categorías de blooper

No todos sirven igual. Clasificarlos es lo que te permite después construir un arco en vez de una pila.

| Categoría | Qué es | Valor típico |
|---|---|---|
| **Trabalenguas** | no le sale la palabra, la repite tres veces | alto: es universal, todo el mundo se identifica |
| **Se le olvidó** | se queda en blanco y lo dice | alto: muy humano |
| **Se ríe solo** | arranca y se le sale la risa | muy alto: la risa contagia |
| **Interrupción externa** | entra alguien, suena algo, se cae un objeto | alto si es visual, medio si es solo audio |
| **Error físico** | se le cae, se golpea, se tropieza | alto si no duele, cero si duele de verdad |
| **Cara de fastidio** | mira a cámara con hastío después de fallar | altísimo: es reacción, no error |
| **Falla técnica** | se acabó la batería, se desenfocó | bajo: aburre |
| **Se equivocó de dato** | dice el número mal | **cero, y peligroso**: nunca publiques a alguien diciendo un dato falso, aunque sea broma |
| **Palabrota o comentario privado** | lo que se dice creyendo que no graba | **prohibido sin permiso explícito** |

Las dos últimas filas no son sugerencias. La primera daña la credibilidad del cliente; la segunda daña la
relación con la persona que aparece.

---

## Puntuar por gracia

Una escala de 1 a 5, aplicada rápido y sin darle vueltas:

| Puntos | Criterio |
|---|---|
| 5 | te reíste solo, viéndolo por segunda vez |
| 4 | sonreíste, y se lo mostrarías a alguien |
| 3 | es simpático, funciona como sazón corto |
| 2 | se entiende que es un error, pero no da nada |
| 1 | solo interrumpe |

**La prueba de la segunda vez es la clave.** Un blooper que da risa la primera vez y nada la segunda no
sirve: tu público lo va a ver una sola vez, sí, pero tú vas a verlo cuarenta veces montándolo, y si a la
segunda ya no da risa es que la gracia era la sorpresa del contexto, no el momento.

**La prueba del contexto cero:** enséñaselo a alguien que no vio el resto del video. Si se ríe, el
blooper funciona solo. Si necesita que le expliques, no va como remate (puede ir como sazón, donde el
contexto ya lo dio el video).

Regla de corte: **solo entran los de 4 y 5.** Los de 3 quedan en reserva para sazón. Los de 1 y 2 se
archivan y se olvidan.

---

## Buscar el arco cómico

Aquí está la diferencia entre un remate que funciona y seis clips pegados.

**El error:** poner los cinco bloopers mejor puntuados uno detrás de otro. El resultado es plano — el
público se ríe con el primero y para el tercero ya entendió el juego. Es una lista, no una historia.

**Lo que funciona:** encontrar un **arco**, es decir, una progresión donde cada blooper escala sobre el
anterior. Los cuatro arcos que casi siempre están en el material:

### Arco 1 — La misma palabra que no sale

El más confiable. Si la persona tropezó tres veces con la misma palabra en tomas distintas, tienes un
arco regalado:

```
intento 1 (seg 12.4, clip-03)  "el eucalipto... euca... " -> se corrige
intento 2 (seg 48.1, clip-03)  "el eucal—" [RISA]         -> peor
intento 3 (seg 15.0, clip-08)  "el arbolito ese"          -> se rinde. REMATE.
```

La gracia no está en ningún intento suelto: está en la repetición y en la rendición final. Ese último
"el arbolito ese" es cinco veces más gracioso después de los dos anteriores.

### Arco 2 — De pequeño a grande

Empieza con el tropiezo mínimo y termina con el desastre. Ordena por escala, no por tiempo del rodaje.

### Arco 3 — La ilusión rota

Se muestra medio segundo del video "perfecto" (el mismo plano que la gente acaba de ver bien montado) y
justo después el mismo momento saliendo mal. El contraste es el chiste. Funciona muy bien porque el
público reconoce el plano.

### Arco 4 — La reacción de otro

Alguien fuera de cámara reacciona (se ríe, dice algo). El arco es error → reacción → cara de quien
falló. Tres piezas cortas. Es el que mejor cierra porque termina en una cara, no en una acción.

### Cómo buscarlo en el catálogo

Ordena los candidatos por texto, no por tiempo. Las repeticiones saltan solas:

```powershell
Import-Csv "C:\Users\user\Desktop\VIDEO-BOTELLA\analisis\bloopers.csv" |
  Where-Object { $_.gracia -ge 3 } |
  Sort-Object texto |
  Format-Table clip, seg, gracia, categoria, texto -AutoSize
```

Si ves tres filas con textos parecidos, ahí está el arco 1.

---

## Extraer los finalistas

```powershell
$proyecto = "C:\Users\user\Desktop\VIDEO-BOTELLA"
$dest = Join-Path $proyecto "trabajo\bloopers"
New-Item -ItemType Directory -Force -Path $dest | Out-Null

Import-Csv (Join-Path $proyecto "analisis\bloopers.csv") |
  Where-Object { $_.usable -eq "si" } |
  ForEach-Object {
    $src = Join-Path $proyecto ("entrada\" + $_.clip + ".mp4")
    $dur = [double](& ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 $src)
    $ini = [math]::Max(0, [double]$_.seg - 1.0)   # 1 s de contexto antes
    $len = 4.0
    if ($ini + $len -gt $dur) { $len = [math]::Round($dur - $ini - 0.05, 2) }
    if ($len -le 0.3) { Write-Output ("SALTADO {0}@{1}: no cabe" -f $_.clip, $_.seg); return }

    $out = Join-Path $dest ("{0}-{1}.mp4" -f $_.clip, ($_.seg -replace "\.", "_"))
    & ffmpeg -y -hide_banner -loglevel error -ss $ini -i $src -t $len -c:v libx264 -crf 20 -preset veryfast -c:a aac -b:a 128k $out
    Write-Output ("OK {0}" -f (Split-Path $out -Leaf))
  }
```

El segundo de contexto antes del momento marcado importa: la risa casi nunca empieza donde el
transcriptor la marcó — empieza en el gesto anterior.

---

## Cómo se corta un blooper

Reglas distintas a las de una toma seria:

1. **Entra tarde, sale seco.** Un blooper que arranca con dos segundos de preámbulo mata el chiste. Entra
   0,3–0,5 s antes del momento y **corta en seco** justo después del punto de gracia, sin dejar cola.
2. **El corte en seco es intencional.** Va a hacer saltar la regla R5 de la compuerta (módulo 16). Se
   marca `intencional=si` con motivo `blooper: corte en seco es el remate`.
3. **La reacción vale más que el error.** Si hay medio segundo de cara después del tropiezo, ese medio
   segundo es lo que hay que conservar por encima de todo.
4. **Sin música encima, o con la música cortada en seco.** El silencio abrupto después de un blooper es
   parte del chiste. Ver `74-musica.md`.
5. **Duración total del bloque de bloopers: 3 a 8 segundos** en un video de 60. Más allá de eso el
   remate se vuelve otro video.

---

## Permisos: la conversación que no se salta

Publicar los errores de alguien sin avisarle es la forma más rápida de perder un cliente o incomodar a un
amigo. La regla:

- **Siempre se pregunta.** "Voy a usar el momento donde te enredas con la palabra eucalipto, ¿te parece?"
- **Se muestra antes de publicar**, no después.
- **Nunca se usa** un momento donde la persona se ve mal físicamente, dice algo privado, o se equivoca en
  un dato que afecta al negocio.
- Si aparece un tercero (un empleado, alguien que pasó), **también hay que preguntarle a él**.

Una excepción que no es excepción: si el cliente es el que aparece y firmó cesión de imagen, sigue siendo
buena práctica mostrarle el blooper antes. Lo legal y lo prudente no siempre coinciden.

---

## El archivo de bloopers

Lo que no entró en este video no se borra: se guarda, porque es contenido propio.

```
analisis/bloopers.csv          catalogo completo con puntaje
trabajo/bloopers/              fragmentos extraidos
salida/EXTRA-bloopers.mp4      compilado aparte, si el cliente lo quiere
```

Un compilado de bloopers es contenido publicable por sí solo, y de los más baratos que existen: ya está
grabado, ya está catalogado, y funciona muy bien como segundo posteo de la misma campaña.

---

## Errores comunes

- **Borrar las tomas falsas al seleccionar.** Es el 83% del bruto y el material más humano que hay.
- **Pegar los cinco mejores bloopers seguidos.** Eso es una lista, no un remate. Se busca un arco.
- **Poner el blooper más gracioso primero.** El arco escala; el mejor va al final.
- **Dejar cola después del punto de gracia.** El blooper corta en seco. Un segundo de más lo mata.
- **Entrar demasiado temprano.** El preámbulo destruye la sorpresa. Entra 0,3–0,5 s antes.
- **Cortar antes de la reacción.** La cara después del error vale más que el error.
- **Usar un blooper donde la persona dice un dato equivocado.** El público se queda con el dato, no con
  el chiste. Cero valor y riesgo real.
- **Publicar sin preguntar.** Aunque sea el dueño, aunque haya cesión de imagen. Se muestra antes.
- **Poner 20 segundos de bloopers en un video de 60.** El remate es 3–8 s. Más es otro video.
- **Confundir "error simpático" con "error incómodo".** Si alguien se golpea de verdad o se ve humillado,
  no da risa: da vergüenza ajena y le pega a la marca.
- **No marcar el corte en seco como intencional en la tabla.** La compuerta lo va a marcar rojo y alguien
  lo va a "arreglar", matando el chiste.
- **No guardar lo descartado.** Es el contenido de la semana entrante, gratis.

---

## Checklist

- [ ] Ninguna toma falsa se borró: todas están en `analisis/bloopers.csv`
- [ ] Cada candidato tiene `clip`, `seg`, `tipo`, `texto`
- [ ] Cada candidato tiene puntaje de gracia de 1 a 5, aplicando la prueba de la segunda vez
- [ ] Cada candidato tiene categoría asignada
- [ ] Los candidatos con dato equivocado o comentario privado están marcados como no usables
- [ ] Solo entran al video los de 4 y 5; los de 3 quedan en reserva para sazón
- [ ] Se buscó un arco cómico (misma palabra, escalada, ilusión rota o reacción de otro)
- [ ] El remate es un arco de 2–4 piezas, no una pila de los mejores
- [ ] El bloque de bloopers dura entre 3 y 8 segundos en un video de 60
- [ ] Cada blooper entra 0,3–0,5 s antes del momento y corta en seco justo después
- [ ] Se conservó la reacción posterior al error donde existe
- [ ] Los cortes en seco están marcados `intencional=si` con motivo en la tabla de cortes
- [ ] Se le pidió permiso a quien aparece, y a los terceros que salen
- [ ] Los bloopers descartados quedan archivados para futuros posteos

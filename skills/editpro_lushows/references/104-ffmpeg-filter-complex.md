# 104 — filter_complex: grafos de filtros y cómo depurarlos

`-vf` y `-af` sirven cuando hay **una** entrada y **una** salida. En cuanto quieres superponer un
logo, mezclar dos audios, unir clips o hacer una transición, necesitas `-filter_complex`.

Un `filter_complex` no es una lista de filtros: es un **grafo**. Nodos que reciben flujos, los
transforman y los entregan a otros nodos. Entenderlo como grafo es la diferencia entre copiar
comandos de internet y escribir los tuyos.

---

## La sintaxis, en tres reglas

### Regla 1 — la coma encadena, el punto y coma separa

```
filtroA,filtroB,filtroC        <- una CADENA: la salida de A entra a B, la de B a C
cadena1;cadena2;cadena3        <- tres cadenas INDEPENDIENTES
```

```bash
-filter_complex "[0:v]scale=1080:1920,setsar=1[v];[0:a]volume=0.8[a]"
```

Ahí hay dos cadenas separadas por `;`. La primera tiene dos filtros encadenados por `,`.

### Regla 2 — los corchetes son etiquetas

- `[0:v]` al **principio** de una cadena: "esta cadena come del flujo de video de la entrada 0"
- `[algo]` al **final** de una cadena: "el resultado se llama `algo`"
- `[algo]` al principio de otra cadena: "come de lo que produjo la cadena anterior"

```bash
-filter_complex "[0:v]scale=640:360[chico];[1:v][chico]overlay=40:40[final]"
```

Lee así: escala la entrada 0 y llámala `chico`; luego toma la entrada 1 y `chico`, superpónlos, y
llama al resultado `final`.

Los nombres son libres: `[v]`, `[a]`, `[bg]`, `[logo_pequeno]`, `[v01]`. Usa nombres que digan qué
son. En un grafo de 15 cadenas, `[tmp3]` no te dice nada a las dos semanas.

### Regla 3 — lo que etiquetas, lo tienes que mapear

Si la última cadena termina con `[v]`, ffmpeg **no** lo escribe solo. Tienes que decírselo:

```bash
-map "[v]" -map "[a]"
```

Las comillas alrededor de `[v]` son obligatorias en la mayoría de shells: sin ellas, Bash y PowerShell
intentan interpretar los corchetes.

**Si no mapeas una etiqueta de salida**, ffmpeg falla con:

```
Output with label 'v' does not exist in any defined filter graph
```

o, peor, no falla y escribe otra cosa.

---

## Nombres de flujos de entrada

```
[0:v]     primer flujo de video de la entrada 0 (equivale a [0:v:0] si solo hay uno)
[0:v:0]   explícito
[0:a]     audio de la entrada 0
[1:a:1]   segundo flujo de audio de la entrada 1
[0]       el flujo 0 de la entrada 0, sin especificar tipo
```

Con `-map` fuera del grafo puedes usar el `?` de "si existe" (`-map 0:a?`). **Dentro del grafo no
existe ese `?`**: si referencias `[0:a]` y la entrada 0 es muda, el comando falla. Por eso, cuando
proceses lotes con clips mudos, o los normalizas antes con silencio (ver `101`), o generas el silencio
en el mismo comando:

```bash
ffmpeg -y -i quizas_mudo.mp4 -f lavfi -i anullsrc=r=48000:cl=stereo -filter_complex \
"[1:a]atrim=0:30,asetpts=PTS-STARTPTS[silencio]" \
-map 0:v -map "[silencio]" -shortest -c:v copy -c:a aac salida.mp4
```

---

## split y asplit — usar el mismo flujo dos veces

**Un flujo solo puede consumirse una vez.** Si intentas usar `[0:v]` en dos cadenas distintas, ffmpeg
falla con `Filter ... has an unconnected output` o con un error de reutilización.

La solución es duplicarlo:

```bash
[0:v]split=2[copia1][copia2]
[0:a]asplit=3[a1][a2][a3]
```

Ejemplo real, el fondo borroso:

```bash
ffmpeg -hide_banner -y -i horizontal.mp4 -filter_complex \
"[0:v]split=2[base][pip]; \
 [base]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=28,eq=brightness=-0.10[bg]; \
 [pip]scale=1080:-2:flags=lanczos[fg]; \
 [bg][fg]overlay=(W-w)/2:(H-h)/2,format=yuv420p[v]" \
-map "[v]" -map 0:a? -c:v libx264 -crf 20 -preset slow -c:a aac -b:a 192k salida.mp4
```

Sin `split`, ese grafo no compila.

---

## Filtros con varias entradas y varias salidas

| Filtro | Entradas | Salidas | Para qué |
|---|---|---|---|
| `overlay` | 2 video | 1 video | superponer |
| `concat` | 2n o más | 1 o 2 | unir en el tiempo |
| `xfade` | 2 video | 1 video | transición |
| `amix` | n audio | 1 audio | mezclar audio |
| `amerge` | n audio | 1 audio | combinar canales |
| `acrossfade` | 2 audio | 1 audio | fundido cruzado |
| `sidechaincompress` | 2 audio | 1 audio | ducking |
| `alphamerge` | 2 video | 1 video | máscara alfa |
| `hstack` / `vstack` | n video | 1 video | poner lado a lado |
| `split` / `asplit` | 1 | n | duplicar |
| `blend` | 2 video | 1 video | modos de fusión |

**El orden de las entradas importa** en casi todos. En `overlay`, la primera es el fondo. En
`sidechaincompress`, la primera es la que se comprime. En `concat`, van intercaladas por segmento.

---

## Fuentes generadas: entradas que no son archivos

Con `-f lavfi -i` puedes generar entradas de la nada:

```bash
-f lavfi -i color=c=black:s=1080x1920:r=30:d=5       # fondo negro de 5 segundos
-f lavfi -i color=c=0x1B4D3E:s=1080x1920:r=30        # fondo de color de marca
-f lavfi -i anullsrc=r=48000:cl=stereo               # silencio
-f lavfi -i sine=frequency=1000:duration=1           # tono de prueba de 1 kHz
-f lavfi -i testsrc2=s=1080x1920:r=30:d=10           # patrón de prueba con contador
-f lavfi -i smptebars=s=1920x1080:d=5                # barras de color
```

Y dentro del grafo, `nullsrc` y `color` también existen como filtros de origen:

```bash
-filter_complex "color=c=black:s=1080x1920:d=3[negro];[negro][0:v]concat=n=2:v=1[v]"
```

Esto sirve para poner un negro de arranque, un fondo sobre el que montar, o un lienzo del tamaño
exacto que quieras aunque ninguna fuente lo tenga.

---

## Un grafo completo, comentado

Un reel con: fondo borroso, video centrado, logo abajo a la derecha que aparece entre el segundo 2 y
el 8, música con ducking, y fundidos de entrada y salida.

```bash
ffmpeg -hide_banner -y \
  -i bruto.mp4 \
  -i logo.png \
  -i musica.mp3 \
  -filter_complex "\
[0:v]fps=30,split=2[base][frente]; \
[base]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=30,eq=brightness=-0.12[bg]; \
[frente]scale=1080:-2:flags=lanczos,setsar=1[fg]; \
[bg][fg]overlay=(W-w)/2:(H-h)/2[compuesto]; \
[1:v]scale=180:-1,format=rgba,colorchannelmixer=aa=0.85[lg]; \
[compuesto][lg]overlay=W-w-50:H-h-560:enable='between(t,2,8)'[conlogo]; \
[conlogo]fade=t=in:st=0:d=0.5,fade=t=out:st=27.5:d=0.5,format=yuv420p[v]; \
[2:a]volume=0.30,afade=t=in:st=0:d=1.5,afade=t=out:st=27:d=1.5[mus]; \
[mus][0:a]sidechaincompress=threshold=0.035:ratio=8:attack=15:release=400[duck]; \
[0:a][duck]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95,loudnorm=I=-14:TP=-1.0:LRA=11[a]" \
  -map "[v]" -map "[a]" \
  -t 28 \
  -c:v libx264 -crf 20 -preset slow -c:a aac -b:a 192k -ar 48000 \
  -movflags +faststart reel_final.mp4
```

Léelo cadena por cadena:

1. Fija 30 fps y duplica el video
2. Una copia se convierte en fondo vertical borroso y oscurecido
3. La otra copia se escala al ancho, manteniendo proporción
4. Se centra la copia nítida sobre el fondo borroso
5. El logo se escala y se le baja la opacidad al 85%
6. El logo se superpone abajo a la derecha, **solo entre el segundo 2 y el 8**
7. Fundidos de entrada y salida, y formato de píxel final
8. La música se baja, entra y sale suave
9. La música se agacha cuando la voz habla
10. Se mezclan voz y música, se limita y se normaliza a -14 LUFS

Es un montaje entero en un solo comando, una sola decodificación, una sola codificación.

---

## Escribir el grafo en un archivo aparte

Cuando el grafo pasa de 6 u 8 cadenas, meterlo en una sola línea de comando es un dolor. Usa
`-filter_complex_script`:

`grafo.txt`:
```
[0:v]fps=30,split=2[base][frente];
[base]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=30[bg];
[frente]scale=1080:-2:flags=lanczos,setsar=1[fg];
[bg][fg]overlay=(W-w)/2:(H-h)/2,format=yuv420p[v]
```

```bash
ffmpeg -hide_banner -y -i bruto.mp4 -filter_complex_script grafo.txt \
  -map "[v]" -map 0:a? -c:v libx264 -crf 20 -c:a aac salida.mp4
```

Ventajas: se puede versionar en git, se puede comentar mentalmente por líneas, y **desaparecen los
problemas de comillas y escapado del shell**, que son la mitad de los dolores en Windows.

**Ojo:** el archivo del script **no puede tener BOM** (misma trampa que `lista.txt` del concat, ver
`109`). Escríbelo con `-Encoding ascii` o con `UTF8Encoding($false)`.

---

## Comillas y escapado: el infierno de Windows

Hay **tres niveles** de interpretación y cada uno se come sus caracteres:

1. El shell (PowerShell, cmd o Bash)
2. El parser de `filter_complex` de ffmpeg, que usa `;` `,` `[` `]` como separadores
3. El parser de argumentos de cada filtro, que usa `:` y `=`

**Reglas que funcionan siempre:**

- Encierra **todo** el `filter_complex` en comillas dobles.
- Dentro, usa comillas simples para los valores que llevan caracteres especiales:
  `enable='between(t,2,8)'`, `text='Hola mundo'`.
- Para un carácter literal que el parser se comería, precédelo de barra invertida: `\:` `\,` `\'` `\[`.
- Rutas dentro de filtros (subtitles, movie, lut3d): escapa los dos puntos de la unidad y usa barras
  normales: `C\\:/ruta/archivo.ass`. Detalle en `106` y `109`.
- En PowerShell, para partir el comando en varias líneas usa la tilde invertida `` ` ``, no `\`.

**Comparación del mismo comando:**

```powershell
# PowerShell
ffmpeg -hide_banner -y -i base.mp4 -i logo.png -filter_complex `
"[1:v]scale=180:-1[lg];[0:v][lg]overlay=W-w-50:H-h-560:enable='between(t,2,8)'[v]" `
-map "[v]" -map 0:a? -c:v libx264 -crf 20 -c:a copy salida.mp4
```

```bash
# Bash / Git Bash
ffmpeg -hide_banner -y -i base.mp4 -i logo.png -filter_complex \
"[1:v]scale=180:-1[lg];[0:v][lg]overlay=W-w-50:H-h-560:enable='between(t,2,8)'[v]" \
-map "[v]" -map 0:a? -c:v libx264 -crf 20 -c:a copy salida.mp4
```

Si algo se pone feo, **cambia a `-filter_complex_script` y olvídate del escapado.** Es la salida
profesional.

---

## Cómo depurar un filter_complex que no corre

Esta es la parte que separa a quien copia comandos de quien los escribe.

### Paso 1 — lee el error, que es específico

| Mensaje | Qué significa de verdad |
|---|---|
| `Output pad "default" ... not connected to any destination` | etiquetaste una salida y no la usas ni la mapeas |
| `Output with label 'v' does not exist in any defined filter graph` | mapeaste `[v]` pero ninguna cadena la produce (revisa si la escribiste mal) |
| `Invalid file index 2 in filtergraph description` | referenciaste `[2:v]` pero solo hay 2 entradas (0 y 1) |
| `Stream specifier ':a' in filtergraph ... matches no streams` | esa entrada no tiene audio |
| `Filter overlay has an unconnected output` | conectaste mal: alguna cadena no consume lo que produce otra |
| `Cannot find a matching stream for unlabeled input pad` | una cadena empieza sin `[etiqueta]` y ffmpeg no sabe de dónde comer |
| `Media type mismatch between filter X and Y` | metiste audio a un filtro de video o al revés |
| `Error reinitializing filters` | dos entradas al mismo filtro con tamaños o formatos incompatibles |
| `Filtergraph 'X' was defined for stream 0:0 but codec copy was selected` | filtras y copias a la vez |

### Paso 2 — divide el grafo

Es la técnica que resuelve el 90% de los casos. **Corta el grafo por la mitad y escribe la mitad a un
archivo.** Si esa mitad funciona, el problema está en la otra.

```bash
# Solo la primera parte, para ver si el fondo compuesto sale bien
ffmpeg -y -i bruto.mp4 -filter_complex \
"[0:v]fps=30,split=2[base][frente]; \
 [base]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=30[bg]; \
 [frente]scale=1080:-2[fg]; \
 [bg][fg]overlay=(W-w)/2:(H-h)/2,format=yuv420p[v]" \
-map "[v]" -an -t 3 -c:v libx264 -crf 28 -preset ultrafast prueba1.mp4
```

`-t 3 -crf 28 -preset ultrafast -an` es el modo de prueba: 3 segundos, feo y rapidísimo. **Nunca
depures renderizando el video completo en calidad final.**

### Paso 3 — saca un fotograma

Cuando el grafo corre pero el resultado no es lo que esperabas, mira un fotograma en vez de todo:

```bash
ffmpeg -y -ss 4 -i bruto.mp4 -filter_complex "TU_GRAFO" -map "[v]" -frames:v 1 mirada.png
```

Un PNG en dos segundos te dice más que ver el render completo.

### Paso 4 — imprime el grafo que ffmpeg construyó

```bash
ffmpeg -v debug -i entrada.mp4 -filter_complex "..." -f null - 2>&1 | more
```

Entre el ruido verás líneas como:

```
[graph 0 input from stream 0:0 @ ...] w:1920 h:1080 pixfmt:yuv420p tb:1/30000 ...
[auto_scale_0 @ ...] w:1080 h:1920 fmt:yuv420p
```

Esas son las conversiones que ffmpeg **insertó por su cuenta** (`auto_scale`, `auto_aformat`,
`auto_resample`). Si ves un `auto_scale` donde no lo esperabas, ahí está tu incompatibilidad de
tamaños.

### Paso 5 — comprueba lo básico antes de culpar al grafo

- ¿Las entradas existen y ffprobe las lee?
- ¿La entrada que dices que tiene audio, lo tiene?
- ¿Los índices de entrada corresponden al orden de los `-i`?
- ¿Mapeaste **todas** las etiquetas finales?
- ¿Hay `format=yuv420p` al final de la cadena de video?
- ¿Estás mezclando `-vf` con `-filter_complex`?

### El truco del comentario

`filter_complex` no tiene comentarios. Pero puedes desactivar una cadena temporalmente reemplazándola
por `null` (video) o `anull` (audio), que no hacen nada:

```bash
# En vez de borrar el gblur para probar, lo sustituyes
[base]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,null[bg]
```

Así el grafo mantiene su forma y solo cambias una pieza. Es bisección de verdad.

---

## Conversiones automáticas: lo que ffmpeg hace sin decirte

ffmpeg inserta filtros por su cuenta cuando dos nodos no encajan:

- `auto_scale` — cuando los formatos de píxel no coinciden
- `auto_aresample` — cuando las frecuencias de muestreo no coinciden
- `auto_aformat` — cuando los formatos de muestra de audio no coinciden

Esto es cómodo y traicionero: **te salva del error, pero puede meterte una conversión de calidad que
no pediste**, o dejar algo en un formato que luego rompe la salida.

Por eso, en cualquier grafo serio, **fija las cosas tú**:

- `fps=30` al entrar cada video
- `scale=...` para igualar tamaños antes de `overlay`, `concat` o `xfade`
- `setsar=1` antes de unir
- `format=yuv420p` al final
- `aresample=48000` al entrar cada audio

Con eso, ffmpeg no tiene nada que adivinar y el resultado es reproducible.

---

## Errores comunes

- **Usar el mismo flujo dos veces sin `split`.** El grafo no compila.
- **Olvidar `-map "[v]"`.** ffmpeg no escribe las etiquetas por su cuenta.
- **Escribir `-map [v]` sin comillas.** El shell se come los corchetes.
- **Confundir `,` con `;`.** La coma encadena dentro de una cadena; el punto y coma separa cadenas.
- **Un `;` de sobra al final del grafo.** Deja una cadena vacía y falla.
- **Referenciar `[0:a]` en un clip mudo.** Dentro del grafo no existe el `?` de "si existe".
- **Índices de entrada mal contados.** Empiezan en 0, no en 1.
- **Mezclar `-vf` y `-filter_complex`** sobre el mismo flujo. Se excluyen.
- **Combinar `-filter_complex` con `-c copy`** en el flujo filtrado. No se puede.
- **Superponer clips de tamaños distintos** sin escalar primero: ffmpeg inserta un `auto_scale` que
  no controlas o falla al reinicializar.
- **Depurar renderizando el video completo.** Usa `-t 3 -preset ultrafast -crf 28`, o un solo
  fotograma.
- **Grafos larguísimos en una línea de PowerShell.** Pásalos a `-filter_complex_script` (sin BOM).
- **Nombres de etiqueta como `[tmp1]` `[tmp2]`.** A la semana no sabes qué era cada uno.
- **Olvidar `format=yuv420p` al final** porque el grafo "ya funcionaba". Funciona en tu PC, no en el
  celular de tu cliente.

---

## Checklist

- [ ] Dibujé mentalmente (o en papel) el grafo antes de escribirlo: qué entra, qué sale, en qué orden.
- [ ] Cada flujo que uso dos veces pasa por `split` o `asplit`.
- [ ] Cada cadena empieza con una etiqueta de entrada y termina con una de salida.
- [ ] Todas las etiquetas finales están mapeadas con `-map "[...]"`, con comillas.
- [ ] Los índices de entrada corresponden al orden real de los `-i`.
- [ ] Verifiqué con ffprobe que cada entrada tiene los flujos que estoy referenciando.
- [ ] Igualé tamaño, fps, SAR y formato **antes** de cualquier `overlay`, `concat` o `xfade`.
- [ ] Igualé frecuencia de muestreo antes de cualquier `amix` o `amerge`.
- [ ] `format=yuv420p` cierra la cadena de video.
- [ ] Si el grafo tiene más de 6 cadenas, está en un archivo con `-filter_complex_script`, sin BOM.
- [ ] Probé primero con `-t 3 -preset ultrafast -crf 28` o con `-frames:v 1`.
- [ ] Si falló, leí el mensaje específico y dividí el grafo en dos para aislar el problema.
- [ ] Revisé con `-v debug` si ffmpeg insertó conversiones automáticas que yo no pedí.

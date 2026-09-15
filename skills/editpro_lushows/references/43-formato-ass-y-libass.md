# 43 — El formato ASS y libass a fondo

## Por qué ASS y no otra cosa

Con ffmpeg tienes tres caminos. `drawtext` sirve para un rótulo fijo o una marca de agua, pero necesita un
filtro por texto: 60 golpes son 60 filtros encadenados. `.srt` no tiene estilo, ni posición, ni animación.
**`.ass` es todo lo demás**, a cambio de una curva de aprendizaje de un rato.

**ASS** significa *Advanced SubStation Alpha*. Nació en el fansub de anime a finales de los 90 y terminó
siendo el formato de subtítulos con estilo más potente que existe. **libass** es la librería que lo
renderiza, y ffmpeg la usa a través del filtro `subtitles`. Un `.ass` es texto plano: lo generas por
código, lo versionas en git y lo revisas leyéndolo. Es la pieza correcta de un pipeline (ver `131`).

---

## Estructura del archivo

Un `.ass` tiene tres secciones obligatorias, en este orden:

```
[Script Info]      -> configuración global del "lienzo"
[V4+ Styles]       -> definición de los estilos (como clases CSS)
[Events]           -> las líneas de texto con sus tiempos (como el HTML)
```

Debe guardarse en **UTF-8 sin BOM**. El BOM (esos tres bytes invisibles al inicio) hace que libass no
reconozca la primera línea `[Script Info]` y falle sin explicar por qué. En PowerShell esto es una trampa
constante — ver la sección de generación más abajo y `109`.

---

## `[Script Info]`

```
[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.709
```

- `ScriptType`: `v4.00+` siempre.
- `PlayResX` / `PlayResY`: **el lienzo de referencia**. Todos los tamaños y márgenes se interpretan sobre
  estas medidas. Ponlos iguales a la resolución del video.
- `WrapStyle: 2`: no parte líneas automáticamente, solo donde pongas `\N`. Tú controlas el corte.
- `ScaledBorderAndShadow: yes`: contorno y sombra escalan con el texto. Sin esto, al hacer el pop al 112%
  el borde no crece y se ve mal.
- `YCbCr Matrix: TV.709` para HD. Evita que los colores salgan levemente corridos.

**`PlayResX/Y` es el campo que más se equivoca.** Si pones `PlayResY: 1080` pero renderizas sobre un video
de 1920 de alto, libass escala todo x1,78 y tu fuente de 150 px sale de 267 px. Ponlo siempre igual a la
resolución real del video de salida.

---

## `[V4+ Styles]`

Un estilo es una plantilla reutilizable. La línea `Format:` declara el orden de los campos y la línea
`Style:` da los valores, separados por comas, **en ese orden exacto**.

```
[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Golpe,Anton,150,&H00FFFFFF,&H00FFFFFF,&H001C4FE8,&H00000000,0,0,0,0,100,100,0,0,1,14,9,2,60,60,520,1
```

Campo por campo, con el valor del ejemplo:

| # | Campo | Valor | Significado |
|---|---|---|---|
| 1 | `Name` | `Golpe` | Nombre con el que lo llamas desde `Dialogue` |
| 2 | `Fontname` | `Anton` | **Nombre de familia de la fuente**, no el del archivo |
| 3 | `Fontsize` | `150` | Píxeles, relativos a `PlayResY` |
| 4 | `PrimaryColour` | `&H00FFFFFF` | Color del relleno: blanco opaco |
| 5 | `SecondaryColour` | `&H00FFFFFF` | Solo se usa en efectos karaoke |
| 6 | `OutlineColour` | `&H001C4FE8` | Color del contorno: el naranja de marca |
| 7 | `BackColour` | `&H00000000` | Color de la sombra: negro opaco |
| 8-11 | `Bold` `Italic` `Underline` `StrikeOut` | `0,0,0,0` | 0 = no, -1 = sí. Con Anton no hace falta negrita |
| 12-13 | `ScaleX` `ScaleY` | `100,100` | Estiramiento horizontal y vertical en % |
| 14 | `Spacing` | `0` | Espaciado entre letras en px. `4` a `8` da aire en titulares |
| 15 | `Angle` | `0` | Rotación en grados |
| 16 | `BorderStyle` | `1` | **1 = contorno + sombra. 3 = caja de fondo sólido** |
| 17 | `Outline` | `14` | Grosor del contorno en px |
| 18 | `Shadow` | `9` | Desplazamiento de la sombra en px |
| 19 | `Alignment` | `2` | Anclaje (ver el teclado numérico abajo) |
| 20-21 | `MarginL` `MarginR` | `60,60` | Márgenes izquierdo y derecho en px |
| 22 | `MarginV` | `520` | Margen vertical (abajo si alineación 1/2/3, arriba si 7/8/9) |
| 23 | `Encoding` | `1` | 1 = por defecto. `0` es ANSI y puede romper tildes |

### El anclaje (`Alignment`) es un teclado numérico

Los valores van como en el teclado numérico: `7 8 9` arriba (izq, centro, der), `4 5 6` a media altura,
`1 2 3` abajo. En la práctica usas tres: **`2`** para subtítulos y golpes (abajo-centro, respeta `MarginV`
desde el borde inferior), **`5`** para resaltes centrados en pantalla (ignora `MarginV`), y **`8`** para
rótulos superiores (`MarginV` cuenta desde arriba).

### `BorderStyle: 3` — la caja

Si en vez de contorno quieres una caja de color detrás del texto (estilo "etiqueta"), usa `BorderStyle: 3`.
Entonces `Outline` pasa a ser el **relleno de la caja alrededor del texto** y `BackColour` su color.
Es el look de los rótulos de noticiero (ver `48`).

---

## Los colores: BGR, no RGB

**Este es el error número uno de quien viene del diseño web.**

ASS escribe los colores como `&HAABBGGRR`: alfa, azul, verde, rojo. Dos inversiones al mismo tiempo:
1. **El orden de los canales está al revés** del hex web (`#RRGGBB` → `BBGGRR`).
2. **El alfa está al revés** de lo intuitivo: `00` es totalmente visible, `FF` totalmente transparente.

### Cómo convertir tu color de marca

Tienes `#E84F1C` (un naranja):

```
#E84F1C  ->  RR=E8  GG=4F  BB=1C
Invierte:    BB=1C  GG=4F  RR=E8
Añade alfa opaco: 00
Resultado:   &H001C4FE8
```

Si te sale un color raro (tu naranja salió azul), casi seguro no invertiste.

Referencias rápidas: blanco `&H00FFFFFF`, negro `&H00000000`, rojo puro `&H000000FF`, azul puro
`&H00FF0000`, amarillo `&H0000FFFF`, negro al 50% `&H80000000`.

Conversión en una línea de Node, para el pipeline:

```javascript
const hexToAss = (hex, alpha = "00") => {
  const h = hex.replace("#", "");
  return `&H${alpha}${h.slice(4,6)}${h.slice(2,4)}${h.slice(0,2)}`.toUpperCase();
};
// hexToAss("#E84F1C") -> "&H001C4FE8"
```

---

## `[Events]` — las líneas de texto

```
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:01.20,0:00:02.08,Golpe,,0,0,0,,TU NEGOCIO
```

`Layer`: número mayor se dibuja **encima** (para superponer dos textos). `Style` debe coincidir exactamente
con un `Name` de `[V4+ Styles]`. `Name` es el hablante, decorativo. `MarginL/R/V` en `0` = usar los del
estilo; cualquier otro valor **los sobrescribe solo para esa línea**. `Effect` son efectos legacy que casi
nunca se usan.

**Trampa del timecode:** el formato es `H:MM:SS.cc`. `0:00:01.20` son 1 segundo y 20 **centésimas**. Si
escribes `0:00:01.200` pensando en milisegundos, libass lee mal o descarta la línea. Dos dígitos después
del punto, siempre, y una sola cifra de hora.

**Trampa del `Text`:** todo lo que va después de la novena coma es el texto, comas incluidas — por eso el
texto puede llevar comas sin escapar nada. Pero **no puede llevar saltos de línea reales**: para eso está
`\N`.

---

## Las etiquetas de override

Van entre llaves `{}` dentro del campo `Text`. Modifican el estilo solo para esa línea (o desde ese punto
hasta el final de la línea). Las que de verdad usas:

| Etiqueta | Qué hace | Ejemplo |
|---|---|---|
| `\fscx` `\fscy` | Escala horizontal / vertical en % | `\fscx112\fscy112` |
| `\alpha` | Transparencia global | `\alpha&H80&` (50%) |
| `\1a` `\3a` `\4a` | Alfa solo del relleno / contorno / sombra | `\3a&HFF&` (contorno invisible) |
| `\1c` `\3c` `\4c` | Color del relleno / contorno / sombra | `\3c&H001C4FE8&` |
| `\pos(x,y)` | Posición absoluta. **Anula los márgenes** | `\pos(540,900)` |
| `\move(x1,y1,x2,y2,t1,t2)` | Mueve de un punto a otro | `\move(540,1450,540,1400,0,140)` |
| `\frz` | Rotación en Z (grados) | `\frz-4` |
| `\frx` `\fry` | Rotación en X / Y (perspectiva 3D) | `\fry20` |
| `\bord` `\shad` `\blur` | Contorno, sombra y difuminado | `\bord20\shad0\blur3` |
| `\fs` `\fn` `\an` | Tamaño, fuente y anclaje | `\fs180\fnAnton\an5` |
| `\t(t1,t2,etiquetas)` | **Animar** de lo actual a lo indicado, entre t1 y t2 ms | `\t(0,140,\fscx100\fscy100)` |
| `\t(t1,t2,acel,etiquetas)` | Igual, con curva | `\t(0,140,0.5,\fscx100)` |
| `\N` | Salto de línea forzado | `PRIMERA\NSEGUNDA` |
| `\h` | Espacio duro (no colapsa) | `1\h000` |

### `\t()` y las curvas

El cuarto parámetro opcional de `\t()` es el **acelerador**: un exponente que curva la interpolación.

`1` (el defecto) es lineal. Menos de 1 (por ejemplo `0.5`) da ease-out: rápido al inicio, suave al frenar.
Más de 1 (por ejemplo `2`) da ease-in: arranca lento y acelera, sensación de caída.

Para el golpe estándar de 140 ms, **lineal está bien**: la duración es tan corta que la curva no se
percibe, y lo que da la sensación de física es el **sobre-impulso**, no la curva (ver `42`). Las curvas
importan en animaciones de 300 ms para arriba: rótulos, lower thirds, gráficos.

Ejemplo de rótulo que entra con ease-out:
`{\alpha&HFF&\pos(60,1600)\t(0,320,0.6,\alpha&H00&)}CHEF DIEGO MORA`

Tres cosas que hay que tener claras de `\t()`: **los tiempos son relativos al inicio de la línea
`Dialogue`**, no del video (causa #1 de "puse una salida y no pasa nada"); **solo anima propiedades
animables** — escalas, colores, alfas, rotaciones, `\bord`, `\blur`, `\fs`, `\shad`, `\fsp` — y **no
anima** `\pos` (para eso está `\move`) ni `\fn` ni `\an`; y puedes encadenar varios en el mismo bloque,
que se aplican en orden.

### `\pos` vs. márgenes

En el momento en que usas `\pos()` o `\move()`, **`MarginL/R/V` y `Alignment` dejan de posicionar**.
El punto que indicas se convierte en el punto de anclaje según el `Alignment` del estilo. Con `\an5`,
`\pos(540,960)` deja el texto centrado en el centro exacto de un lienzo 1080x1920.

Esto es la trampa que mete texto debajo del caption de Instagram: pones un `\move` bonito y de repente el
`MarginV: 520` que te protegía ya no aplica. Ver `45`.

---

## `fontsdir`: usar fuentes sin instalarlas

En Windows, instalar fuentes para que ffmpeg las vea es un dolor. `fontsdir` lo resuelve:

```bash
ffmpeg -i entrada.mp4 -vf "subtitles=texto.ass:fontsdir=fonts" \
  -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -c:a copy salida.mp4
```

Metes los `.ttf` en `fonts/` dentro de la carpeta del proyecto. libass la escanea, lee el **nombre de
familia interno** de cada archivo, y ese es el nombre que debes poner en `Fontname`. `Anton-Regular.ttf`
tiene familia `Anton`, no `Anton-Regular`. Para verlo:

```bash
fc-query --format "%{family}\n" fonts/Anton-Regular.ttf
```

### La sustitución silenciosa

**libass no falla si no encuentra la fuente.** Sustituye por la primera que encuentre (típicamente Arial o
DejaVu Sans) y renderiza feliz. Tú exportas, subes, y tres días después te dicen que el video se ve raro.
Detectarlo:

```bash
ffmpeg -v verbose -i entrada.mp4 -vf "subtitles=texto.ass:fontsdir=fonts" -frames:v 1 -y prueba.png 2>&1 | grep -i "font"
```

Busca líneas tipo `fontselect: (Anton, 400, 0) -> DejaVuSans.ttf`. Esa flecha hacia otra fuente es el
aviso. Y de todas formas: **abre el PNG y míralo**.

---

## Otras opciones del filtro `subtitles`

Además de `fontsdir`: `original_size=1080x1920` fuerza la resolución de referencia si el `.ass` no la trae
bien; `alpha=1` procesa el canal alfa para overlays transparentes; `charenc=UTF-8` fuerza la codificación
de lectura; y `force_style=` sobrescribe campos del estilo desde la línea de comandos, útil para probar
variantes sin editar el archivo:

```bash
ffmpeg -i entrada.mp4 -vf "subtitles=texto.ass:fontsdir=fonts:force_style='Fontsize=170,Outline=18'" \
  -frames:v 1 -y prueba.png
```

### Rutas en Windows

El filtro `subtitles` interpreta `\` como escape y `:` como separador de opciones. Una ruta como
`C:\videos\texto.ass` **revienta**. La solución correcta el 95% de las veces: **ejecuta ffmpeg desde la
carpeta del proyecto y usa rutas relativas** (`subtitles=texto.ass`). Si no puedes, usa barras normales y
escapa los dos puntos: `subtitles='C\:/videos/texto.ass'`.

---

## Generar el `.ass` por código (sin BOM)

Un video de 45 s son ~50 líneas. No se escriben a mano.

```javascript
const fs = require("fs");
const POP = "{\\fscx62\\fscy62\\alpha&HFF&\\t(0,70,\\fscx112\\fscy112\\alpha&H00&)\\t(70,140,\\fscx100\\fscy100)}";

const tc = (s) => {                       // segundos -> H:MM:SS.cc
  const m = Math.floor((s % 3600) / 60), sec = Math.floor(s % 60);
  const cs = Math.round((s - Math.floor(s)) * 100);
  const p = (n) => String(n).padStart(2, "0");
  return `${Math.floor(s / 3600)}:${p(m)}:${p(sec)}.${p(cs)}`;
};

const golpes = [
  { ini: 0.30, fin: 1.18, txt: "TU COCINA" },
  { ini: 1.18, fin: 2.05, txt: "TE ESTA" },
  { ini: 2.05, fin: 2.94, txt: "ROBANDO" }
];

const cuerpo = golpes
  .map(g => `Dialogue: 0,${tc(g.ini)},${tc(g.fin)},Golpe,,0,0,0,,${POP}${g.txt}`)
  .join("\n");

// CABECERA = las tres secciones de arriba de este modulo, como plantilla de texto
fs.writeFileSync("texto.ass", CABECERA + cuerpo + "\n", "utf8");
```

`fs.writeFileSync(..., "utf8")` en Node escribe **sin BOM**, que es lo correcto. **En PowerShell, cuidado:**
`Set-Content -Encoding utf8` en Windows PowerShell 5.1 escribe **con BOM** y rompe el archivo. Desde
PowerShell, la forma segura (el `$false` es el "sin BOM") — ver `109`:

```powershell
[System.IO.File]::WriteAllText("$PWD\texto.ass", $contenido, (New-Object System.Text.UTF8Encoding($false)))
```

---

## Errores comunes

- **Colores en RGB en vez de BGR.** El naranja sale azul. Convierte siempre, o usa la función `hexToAss`.
- **Alfa al revés.** `FF` es invisible, `00` es opaco. Todo el mundo lo pone al revés la primera vez.
- **`PlayResX/Y` distinto de la resolución real del video.** libass escala todo y tu fuente de 150 sale
  gigante o minúscula, y no entiendes por qué.
- **Guardar el `.ass` con BOM.** libass no lee `[Script Info]` y falla sin decir la causa real.
- **Timecodes con tres decimales.** El formato es `H:MM:SS.cc` — dos dígitos, centésimas.
- **`Fontname` con el nombre del archivo.** Es `Anton`, no `Anton-Regular` ni `Anton-Regular.ttf`.
- **Confiar en que la fuente se cargó.** libass sustituye en silencio. Verifica con `-v verbose` y con un
  PNG que abras y mires.
- **Rutas Windows con `\` y `:` dentro del filtro `subtitles`.** Corre desde la carpeta y usa rutas
  relativas.
- **Poner `\pos` y esperar que `MarginV` siga protegiendo.** Al usar coordenadas, los márgenes mueren.
- **Tiempos de `\t()` en absoluto del video.** Son relativos a la línea. Siempre.
- **Olvidar `ScaledBorderAndShadow: yes`.** El contorno no escala con el pop y se ve un borde que respira.
- **Menos campos de los declarados en `Format:`.** Si `Format` declara 23 campos y tu `Style` trae 22,
  libass descarta el estilo entero en silencio y usa el default.
- **Usar `\t()` sobre `\pos`.** No se anima. Usa `\move`.

---

## Checklist

- [ ] El archivo está en **UTF-8 sin BOM**.
- [ ] `[Script Info]`, `[V4+ Styles]` y `[Events]` están, en ese orden.
- [ ] `PlayResX`/`PlayResY` coinciden exactamente con la resolución del video de salida.
- [ ] `WrapStyle: 2` y `ScaledBorderAndShadow: yes` presentes.
- [ ] La línea `Style:` tiene exactamente el mismo número de campos que `Format:`.
- [ ] Todos los colores están en **BGR** y los verifiqué contra el hex de marca.
- [ ] Los alfas: `00` para opaco, `FF` para invisible. Confirmado.
- [ ] `Fontname` es el nombre de **familia** de la fuente, no el del archivo.
- [ ] La fuente está en la carpeta `fonts/` y el comando lleva `fontsdir=fonts`.
- [ ] Corrí con `-v verbose` y **no** hay sustitución de fuente en el log.
- [ ] Rendericé un PNG de prueba y **lo abrí y lo miré**.
- [ ] Los timecodes están en `H:MM:SS.cc` con dos decimales.
- [ ] Los tiempos dentro de `\t()` son relativos al inicio de cada línea.
- [ ] Si usé `\pos` o `\move`, verifiqué manualmente la zona segura (ver `45`).
- [ ] Ejecuté ffmpeg desde la carpeta del proyecto con rutas relativas.

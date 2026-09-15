# 40 — El texto es el canal principal, no un accesorio

## La idea que cambia todo

Cuando pones subtítulos por "accesibilidad", los pones al final, pequeños, blancos, abajo, y te da igual
cómo queden. Cuando entiendes que **la mayoría de la gente ve tu video sin sonido**, el texto deja de ser
un accesorio y pasa a ser **el canal por donde viaja tu mensaje**. La imagen acompaña. El audio adorna.
El texto vende.

Esto no es una opinión de diseño. Es una consecuencia del contexto de consumo:

- La gente ve videos en el bus, en la fila del banco, en la oficina, en la cama al lado de alguien que
  duerme, en el baño. Todos esos contextos son **contextos sin sonido**.
- El feed arranca en silencio o a volumen bajísimo en la mayoría de los casos.
- Aunque suba el volumen, el primer segundo ya pasó. Y el primer segundo es el que decide (ver `30`).

**Dato que debes tener en la cabeza:** un video con texto dinámico en pantalla retiene alrededor de
**35% más** que el mismo contenido como talking head pelado. No es un 3% de mejora marginal. Es la
diferencia entre un video que muere en el segundo 4 y uno que llega al final.

---

## El reencuadre mental

Deja de pensar así:

> "Grabo el video, y al final le pongo subtítulos por si acaso."

Piensa así:

> "El texto es la versión legible de mi video. El audio es la versión sonora. Ambas tienen que funcionar
> solas. Si le quito el sonido y no se entiende nada, el video está roto."

**La prueba del mute.** Antes de exportar, reproduce tu video en silencio de principio a fin. Si en algún
tramo no sabes qué está pasando o qué te están diciendo, ahí hay un hueco. No lo tapes con música: tápalo
con texto.

---

## Qué significa esto en la práctica

### 1. El texto no espera al audio, llega con él o antes

Un subtítulo que aparece 200 milisegundos después de que se dijo la palabra se siente lento y desconectado.
El texto tiene que **golpear con la sílaba tónica**, no después. Detalle en `46`.

### 2. El texto se ve, no se lee

Nadie "lee" un reel. Lo escanea. Por eso el texto en video corto no se comporta como texto de libro:

| Texto de libro | Texto de video corto |
|---|---|
| Renglones largos, muchas palabras | 2 palabras por golpe |
| Tipografía fina, elegante | Grotesca pesada, condensada |
| Quieto | Cambia cada 0,9 segundos |
| Minúsculas | MAYÚSCULAS o mayúsculas de caja alta forzadas |
| Sin contorno | Contorno grueso obligatorio |

### 3. El texto compite con la imagen, y tiene que ganar

Si el fondo es un plano lleno de detalle y color, tu texto de 40px blanco sin contorno desaparece.
El contorno grueso y la sombra dura no son adorno: son lo que hace que el texto **siga siendo legible
sobre cualquier fotograma**, incluso el peor. Detalle en `44`.

### 4. El texto es un elemento de marca

Aquí es donde la mayoría se queda corta. El subtítulo amarillo de karaoke con borde negro es el equivalente
visual del Comic Sans: funciona, pero grita "hecho con la plantilla que trae la app". Tu contorno lleva
**el color de tu marca**. Tu tipografía es **la tipografía de tu marca** (o su prima pesada). El video se
tiene que reconocer como tuyo aunque le quiten el logo.

> Si el proyecto no tiene identidad definida, pasa primero por `directorcreativo_lushows`. No inventes
> una paleta aquí.

---

## El estilo base que funciona (probado)

Este es el punto de partida para vertical 1080x1920. No es "un" estilo: es **el** estilo que sobrevive al
feed. Después lo personalizas.

| Parámetro | Valor | Por qué |
|---|---|---|
| Lienzo | 1080x1920 | El estándar vertical de todas las redes |
| Fuente | Anton | Grotesca pesada condensada: cabe más letra por línea sin perder peso |
| Tamaño | 150 px | Se lee en un celular de gama baja a brazo extendido |
| Color | Blanco | Máximo contraste contra cualquier cosa |
| Contorno | 14 px, color de marca | Separa el texto del fondo y firma la marca |
| Sombra | 9 px desplazada, sin difuminar | Da volumen; el blur la vuelve sucia |
| Margen inferior | 520 px | Deja el texto por encima de la interfaz de Instagram |
| Alineación | Centro-abajo (2 en ASS) | El ojo lo encuentra sin buscar |

Ese margen de 520 px no es capricho. La interfaz de Instagram (caption, audio, botones) come los
últimos ~400 px del alto. Si pones tu texto a 100 px del borde, el caption se le monta encima. Detalle
por plataforma en `45`.

---

## Cómo se hace, en concreto

El texto en video se pone con **subtítulos ASS renderizados por libass**, no con `drawtext` de ffmpeg.
`drawtext` sirve para un rótulo fijo; para texto que cambia 60 veces en 40 segundos, ASS es el formato
correcto (ver `43`).

### Estructura mínima de un archivo `.ass`

```
[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Golpe,Anton,150,&H00FFFFFF,&H00FFFFFF,&H001C4FE8,&H00000000,0,0,0,0,100,100,0,0,1,14,9,2,60,60,520,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.10,0:00:00.98,Golpe,,0,0,0,,{\fscx62\fscy62\alpha&HFF&\t(0,70,\fscx112\fscy112\alpha&H00&)\t(70,140,\fscx100\fscy100)}TU NEGOCIO
Dialogue: 0,0:00:00.98,0:00:01.86,Golpe,,0,0,0,,{\fscx62\fscy62\alpha&HFF&\t(0,70,\fscx112\fscy112\alpha&H00&)\t(70,140,\fscx100\fscy100)}PIERDE PLATA
```

Ojo con `&H001C4FE8`: en ASS los colores van en **BGR**, al revés del hex web. El color de marca
`#E84F1C` se escribe `&H001C4FE8`. Es el error número uno de quien viene del diseño web. Ver `43`.

### Quemarlo en el video

```bash
ffmpeg -i entrada.mp4 -vf "subtitles=texto.ass:fontsdir=fonts" \
  -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -c:a copy salida.mp4
```

`fontsdir=fonts` es la clave en Windows: le dice a libass que busque las fuentes en la carpeta `fonts/`
del proyecto **sin tener que instalarlas en el sistema**. Metes `Anton-Regular.ttf` ahí y funciona.
Sin eso, libass no encuentra Anton y te sustituye por Arial en silencio — y no te avisa.

### Comprobar que la fuente sí se usó

```bash
ffmpeg -i entrada.mp4 -vf "subtitles=texto.ass:fontsdir=fonts" -frames:v 1 -y prueba.png
```

Abre `prueba.png` y mira. Si la letra se ve ancha y con remates suaves, es Arial: la sustitución silenciosa
te pasó por encima. Anton es angosta y sin remates.

---

## Cuánto texto es demasiado

El error opuesto también existe: llenar la pantalla de texto hasta que el video parezca una diapositiva.

Reglas duras:

- **Máximo 2 líneas simultáneas.** Tres líneas ya obligan a leer y el ojo abandona.
- **Máximo 2 palabras por golpe** en modo subtítulo completo (ver `46`).
- **Nunca dos bloques de texto compitiendo.** Si tienes un rótulo arriba y subtítulo abajo, uno de los dos
  tiene que estar quieto y ser secundario (ver `48`).
- **El texto no tapa la cara.** Si la persona está hablando en cuadro, su boca y sus ojos son información.
  Un texto que le cruza la barbilla mata el video.

---

## Cuándo NO subtitular todo

Esta es una decisión de formato, no una regla universal. En un video con narrador en cámara mirando a
lente, transcribir cada palabra puede ser ruido: la cara ya está comunicando. Ahí funciona mejor
**resaltar solo las palabras clave** — fechas, cifras, nombres propios, el precio, el beneficio.

El criterio completo está en `41`. No lo decidas por costumbre: decídelo por formato.

---

## La regla del último control

Antes de dar por terminado cualquier video con texto:

1. Míralo **en silencio** de principio a fin.
2. Míralo en el **celular**, no en el monitor. Lo que en 27 pulgadas se ve grande, en 6 pulgadas se ve mediano.
3. Sobreponle mentalmente (o con una plantilla PNG) la **interfaz de Instagram** y confirma que nada
   importante queda debajo.

Si esas tres pasan, el texto está bien puesto. Si alguna falla, todavía no terminaste. Ver `98`.

---

## Errores comunes

- **Poner los subtítulos al final, como trámite.** El texto se piensa desde el guion, no se pega al render.
  Si escribes el guion sabiendo que va a ir en pantalla, escribes frases más cortas y mejores.
- **Texto blanco sin contorno.** Sobrevive contra un fondo oscuro y desaparece contra una pared clara,
  una camisa blanca o un cielo. Un solo fotograma malo arruina el golpe.
- **Fuente fina o elegante.** Las tipografías de peso Light o Regular con remates finos se deshacen en la
  compresión de Instagram. Usa peso Black/Heavy o una grotesca condensada pesada como Anton.
- **Confiar en que libass encontró la fuente.** Sustituye en silencio y exporta feliz con Arial. Verifica
  siempre un fotograma.
- **Colores en RGB dentro del ASS.** ASS usa BGR. Tu naranja de marca sale azul y te vuelves loco.
- **Margen inferior por defecto.** El valor típico deja el texto detrás del caption de Instagram. En
  vertical, 520 px es el punto de partida, no 20.
- **Subtitular todo por reflejo.** En algunos formatos resaltar 6 palabras clave funciona mejor que
  transcribir 300. Decide con `41`.
- **Texto de 4 a 6 palabras por golpe.** Deja el texto quieto 2 segundos y mata el pulso del video.
- **Tres líneas simultáneas.** Ya no es video, es una diapositiva.
- **Poner el texto encima de la cara.** La cara es información. Compite y pierde el video.

---

## Checklist

- [ ] Vi el video completo **en silencio** y se entiende todo sin audio.
- [ ] Lo revisé en pantalla de celular, no solo en el monitor.
- [ ] La fuente es pesada (Anton o equivalente Black/Heavy), no fina.
- [ ] Tamaño 150 px en lienzo 1080x1920 (o proporcional si otro lienzo).
- [ ] Contorno grueso (14) con el **color de marca**, no negro genérico.
- [ ] Sombra dura desplazada 9 px, **sin difuminar**.
- [ ] Margen inferior >= 520 px: nada queda bajo la interfaz de Instagram.
- [ ] Máximo 2 líneas simultáneas en pantalla.
- [ ] Máximo 2 palabras por golpe (si es subtitulado completo).
- [ ] El texto no tapa ojos ni boca de quien habla.
- [ ] Colores del ASS escritos en **BGR**, verificados contra el hex de marca.
- [ ] Rendericé un fotograma de prueba y **confirmé visualmente** que la fuente correcta se usó.
- [ ] Decidí conscientemente entre subtitulado completo y palabras clave (ver `41`), no por costumbre.
- [ ] `fontsdir=fonts` presente en el comando y la fuente dentro de esa carpeta.

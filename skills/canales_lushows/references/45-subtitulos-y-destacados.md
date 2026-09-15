# 45 · Subtítulos y destacados

**Qué resuelve:** "poner subtítulos" y "poner texto" se confunden todo el rato, y son
dos trabajos distintos con dos formatos distintos. Transcribirlo todo en el 16:9 tapa
el collage; no transcribir nada en el 9:16 mata el vídeo. Esto fija cuál va dónde.

---

## Los dos modos

| | **Transcripción** | **Destacado** |
|---|---|---|
| Qué es | Todo lo que dice la voz, palabra por palabra | 1-3 palabras, las que cargan la frase |
| Dónde | Vertical 9:16 · pistas de idiomas · YouTube CC | Horizontal 16:9, el episodio principal |
| Posición | Banda inferior fija | Donde la composición deja sitio |
| Cuerpo | 56-72 px (16:9) · 64-84 px (9:16) | 76-140 px |
| Familia | Dato (Consolas) o Titular | Titular |
| Cuántas a la vez | 1 bloque, máx. 2 líneas | 1 |
| Ritmo | Continuo | 4-8 por minuto, no más |

**La regla:** en el 16:9 el texto compite con el collage, así que **sólo se escribe lo
que la frase no puede perder**. En el 9:16 no hay collage que proteger y el vídeo se ve
mudo por sistema, así que **va todo**.

**Qué palabra se destaca:** la que cambia el sentido si se quita — una cifra, un
nombre, un verbo de acción o una negación. Nunca un artículo ni una frase entera.

**En YouTube, además, la pista de subtítulos va aparte y siempre.** Un `.srt` cargado
como CC no ocupa pantalla, es accesible y lo indexa el buscador. No sustituye al texto
en pantalla: es otra cosa (`40`).

---

## El formato: ASS con libass

`drawtext` no sirve para subtítulos —una llamada por bloque, sin partición de líneas,
sin estilos reutilizables—. Para esto está **ASS/libass**, que ffmpeg tiene compilado
(`--enable-libass`, filtros `subtitles` y `ass`).

```
[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: PEtrans,Consolas,60,&H00D6E6ED,&H000B12E3,&H000C1012,&H000C1012,-1,0,0,0,100,100,3,0,1,6,0,2,200,200,150,1
Style: PEdest,Arial Black,120,&H00C4DCE6,&H0047C5E8,&H000C1012,&H000C1012,-1,0,0,0,100,100,1,0,1,9,0,5,120,120,120,1

[Events]
Format: Layer, Start, End, Style, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:12.40,0:00:15.10,PEtrans,,,,,{\fad(120,120)}Ciento veintiséis toneladas\Nsalieron por ese túnel
Dialogue: 0,0:00:19.02,0:00:20.90,PEdest,,,,,{\fad(90,140)}{\c&H0047C5E8&}126 TONELADAS
```

**Lo que hay que saber para no perder media tarde:**

| Campo | Detalle |
|---|---|
| `PlayResX/Y` | **Obligatorio.** Sin esto libass asume 384×288 y todos los tamaños salen mal |
| Colores | `&HAABBGGRR` — **BGR invertido**, y `AA` es *transparencia* (00 = opaco) |
| `Bold` | `-1` es sí, `0` es no. No es `1` |
| `Alignment` | Teclado numérico: `2` abajo-centro, `5` centro-centro, `8` arriba-centro |
| `BorderStyle` | `1` contorno + sombra · `3` caja opaca detrás |
| `Outline` | Grosor del contorno en px de `PlayRes` (`46`); exige `ScaledBorderAndShadow: yes` |
| `\N` | Salto de línea duro. `\n` sólo funciona con `WrapStyle: 2` |
| Fuente | Por **nombre de familia**, no por archivo. Debe estar instalada o pasarse `fontsdir` |

Colores del canal ya convertidos a ASS:

| | hex | ASS |
|---|---|---|
| papel | `#EDE6D6` | `&H00D6E6ED` |
| papel 2 | `#E6DCC4` | `&H00C4DCE6` |
| oro | `#E8C547` | `&H0047C5E8` |
| rojo | `#E3120B` | `&H000B12E3` |
| tinta | `#12100C` | `&H000C1012` |

Se quema sobre el vídeo así:

```bash
ffmpeg -i salida/_mudo.mp4 -vf "subtitles='subs.ass'" \
  -c:v libx264 -crf 17 -preset medium -pix_fmt yuv420p -y con_texto.mp4
```

---

## Generarlo desde `tiempos.json`

El alineado palabra a palabra ya existe. El `.ass` no se escribe a mano: se genera.

```python
import io, json
T = json.load(io.open("audio/tiempos.json", encoding="utf-8"))["palabras"]

def hms(s):
    h, s = divmod(s, 3600); m, s = divmod(s, 60)
    return "%d:%02d:%05.2f" % (h, m, s)

# bloques de 2 s o de 7 palabras, lo que llegue antes
bloque, salida = [], []
for p in T:
    bloque.append(p)
    if len(bloque) >= 7 or bloque[-1]["t"] - bloque[0]["t"] >= 2.0:
        txt = " ".join(x["palabra"] for x in bloque)
        salida.append("Dialogue: 0,%s,%s,PEtrans,,,,,{\fad(120,120)}%s"
                      % (hms(bloque[0]["t"] - 0.08),
                         hms(bloque[-1]["t"] + 0.55), txt))
        bloque = []
io.open("subs.ass", "w", encoding="utf-8", newline="\n").write(CABECERA + "\n".join(salida))
```

**El desfase importa:** el bloque entra **0,08 s antes** de su primera palabra y sale
**0,55 s después** de la última. Salir a la vez que la voz se lee como que el subtítulo
se corta a media frase.

### Karaoke: resaltar la palabra que suena

Con `\k` (centésimas de segundo por palabra) el bloque va completo y se ilumina la
palabra en curso. Es lo que sostiene el formato vertical.

```
Dialogue: 0,0:00:12.40,0:00:15.10,PEtrans,,,,,{\k32}Ciento {\k28}veintiséis {\k44}TONELADAS
```

El color que "enciende" es `SecondaryColour` → `PrimaryColour`. Por eso el estilo
`PEtrans` lleva el oro en `SecondaryColour`: la palabra en curso llega en oro y se
apaga a papel. **En el 16:9 el karaoke no se usa** — demasiado movimiento debajo de un
collage que ya se mueve.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| `.ass` sin `PlayResX/PlayResY` | libass asume 384×288: todo sale diminuto |
| Colores en RGB | Sale el color complementario y parece un error de codificación |
| `Bold: 1` | `1` no es verdadero en ASS; hay que poner `-1` |
| Transcribir todo en el 16:9 | Tapa el collage y ninguna palabra destaca |
| Destacar una frase entera | Destacar todo es no destacar nada |
| Subtítulo que sale con la última palabra | Se percibe cortado |
| Fuente por ruta de archivo en `Fontname` | libass la ignora y cae a la de sistema |
| Quemar los subtítulos y no subir el `.srt` | Se pierde la indexación y la accesibilidad |

## Relacionado

`40` el texto como canal principal · `42` tipografía del canal ·
`46` texto sobre collage · `49` zona segura y tamaños · `88` sonido por idioma

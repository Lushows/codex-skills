# 252 — Leer scopes de verdad

El módulo `69` te enseñó qué es cada scope y cómo generarlo. Este módulo es lo siguiente: **qué mira
un colorista en cada uno y qué decide con eso**. La diferencia entre ver un scope y leerlo es la
misma que entre ver una radiografía y diagnosticar.

Regla de entrada, para que nada de esto se malinterprete:

> **El scope no te dice si el video está bonito. Te dice qué hay adentro.**
> La belleza la decides tú mirando. El scope evita que te equivoques por creer lo que tu monitor
> mal calibrado te está mostrando.

---

## 1. Los cuatro instrumentos y la pregunta de cada uno

| Instrumento | Pregunta que responde | Decisión que dispara |
|---|---|---|
| **Histograma** | ¿cuántos píxeles hay en cada nivel? | subir/bajar exposición general |
| **Forma de onda (waveform)** | ¿en qué **parte del cuadro** está cada brillo? | dónde recortar, qué zona levantar |
| **Parade RGB** | ¿los tres canales están alineados? | balance de blancos, tinte |
| **Vectorscopio** | ¿qué **matices** hay y cuánta saturación? | corrección de color, piel, look |

La clave que casi nadie entiende al principio: **el histograma y la forma de onda muestran lo mismo,
pero la forma de onda mantiene la posición horizontal**. El histograma dice "hay muchos píxeles
oscuros"; la forma de onda dice "los píxeles oscuros están en el lado izquierdo del cuadro". Uno te
dice que hay un problema; el otro te dice **dónde**.

Por eso el colorista vive en la forma de onda y el vectorscopio, y el histograma es de apoyo.

---

## 2. Forma de onda: dónde vive tu imagen

El eje horizontal de la forma de onda es **el ancho del cuadro**. El vertical es el brillo (0 abajo,
100 arriba, en unidades IRE).

```bash
# La forma de onda de luma, sola y grande
ffmpeg -y -ss 4 -i clip.mp4 \
  -vf "waveform=intensity=0.15:mirror=1:components=1:graticule=green:flags=numbers,scale=960:-1" \
  -frames:v 1 wf.png
```

`intensity` es cuánto "brilla" el trazo: con 0.004 (el defecto) casi no se ve; entre 0.10 y 0.25 es
lo usable. `mirror=1` pone el 0 abajo, que es como se lee siempre.

### Las cinco formas que tienes que reconocer

| Lo que ves | Qué significa | Qué haces |
|---|---|---|
| Todo el trazo apelotonado abajo (0–35) | subexpuesto | subir gamma/exposición **antes** de tocar contraste |
| Todo apelotonado arriba (75–100) | sobreexpuesto | bajar exposición; si está pegado a 100, ya no hay dato |
| Una línea plana pegada al techo 100 | **recorte de altas** — el dato se perdió | no se recupera. Solo se disimula bajando alrededor |
| Trazo que no baja de 25 ni sube de 70 | imagen lavada / log sin corregir | estirar contraste con `curves` |
| Trazo que llena de 0 a 100 uniformemente | contraste completo | tocar poco, ya está |

### Lo que un colorista mira de verdad

No mira "la forma general": mira **tres zonas** y las juzga por separado.

1. **El pie (0–10).** ¿Hay algo que toque el 0? Si sí, tienes negros recortados. Un poco de negro en
   0 es normal y sano (da profundidad). Una franja gruesa en 0 es detalle perdido.
2. **La cabeza (90–100).** ¿Hay algo pegado a 100? Una lámpara, un reflejo, una ventana: normal. Una
   cara: desastre.
3. **El bulto (30–70).** Aquí vive la piel, el producto, lo que importa. Si el bulto está en 20, tu
   sujeto está oscuro por más lindo que se vea el fondo.

En el caso del bar (`250`), los planos de neón tenían el bulto entero entre 15 y 35 IRE (Y = 70–78 en
escala 0–255 ≈ 27–30 IRE). El diagnóstico de la forma de onda era inequívoco: **imagen oscura con
todo el dato en el tercio bajo**. Y aun así se le aplicó `gamma=0.95`, que oscurece. El scope estaba
mostrando el error antes de que ocurriera. Nadie lo leyó.

---

## 3. Parade RGB: el detector de tinte, sin discusión

El parade dibuja tres formas de onda, una por canal, lado a lado.

```bash
ffmpeg -y -ss 4 -i clip.mp4 \
  -vf "waveform=intensity=0.15:mode=column:components=7:display=parade:graticule=green:flags=numbers,scale=960:-1" \
  -frames:v 1 parade.png
```

`components=7` = R + G + B (es una máscara de bits: 1=R/Y, 2=G/U, 4=B/V; 7 = las tres).

**Cómo se lee, en una frase:** busca una zona de la imagen que **debería ser gris o blanca** (una
pared blanca, una camisa blanca, una hoja de papel) y mira si los tres canales llegan a la misma
altura en ese punto horizontal.

| Lo que ves | Diagnóstico | Corrección |
|---|---|---|
| R más alto que G y B | tinte cálido / rojizo | `colorbalance=rm=-0.05` |
| B más alto | tinte frío / azul | `colorbalance=bm=-0.05` |
| R y B altos, G bajo | **magenta** | `colorbalance=rm=-0.05:bm=-0.05` o `gm=+0.04` |
| G alto, R y B bajos | verde (típico de luz fluorescente) | `colorbalance=gm=-0.05` |
| Los tres alineados arriba pero desalineados abajo | el tinte está solo en las sombras | usar `rs/gs/bs` (shadows), no los medios |

Ese último punto es lo que separa al que sabe: **el parade te dice en qué zona de brillo está el
tinte**. `colorbalance` tiene tres juegos de parámetros por eso:

```bash
# rs/gs/bs = sombras · rm/gm/bm = medios · rh/gh/bh = altas
ffmpeg -i clip.mp4 -vf "colorbalance=rs=-0.04:bs=0.03:rm=-0.06:bm=0.04" -c:v libx264 -crf 16 out.mp4
```

Un tinte que solo está en las sombras corregido con los medios te desbalancea el resto de la imagen.

---

## 4. Vectorscopio: matiz y saturación en un solo dibujo

El vectorscopio ignora el brillo. Solo dibuja croma: **el ángulo es el matiz, la distancia al centro
es la saturación**.

```bash
ffmpeg -y -ss 4 -i clip.mp4 \
  -vf "vectorscope=mode=color3:graticule=color:flags=name+white:envelope=peak,scale=600:600" \
  -frames:v 1 vs.png
```

Opciones que sí importan:

| Opción | Para qué |
|---|---|
| `mode=color3` | el trazo se pinta del color real. El más legible para trabajar |
| `mode=color5` | resalta según luminancia; útil para ver qué colores son brillantes |
| `graticule=color` | dibuja las cajas de las barras de color y la **línea de piel** |
| `flags=name+white` | etiqueta R, G, B, C, M, Yl y marca el punto blanco |
| `envelope=peak` | marca hasta dónde llegó el trazo en todo el clip; ideal para revisar un plano entero |

### Los tres diagnósticos que da

**a) ¿Está balanceado?** Si la nube de puntos está **centrada** en el punto blanco, no hay tinte
dominante. Si toda la nube está corrida hacia una esquina, ese es tu tinte y su dirección exacta.

En el bar: la nube estaba desplazada al cuadrante superior derecho (U alto + V alto). Ese cuadrante
es magenta. Los números —U 144–165, V 143–168— son ese desplazamiento, medido.

**b) ¿Cuánta saturación hay?** Distancia al centro. Si el trazo se sale de las cajas de las barras de
color, estás sobresaturado y probablemente recortando gamut (`251`).

**c) ¿La piel está en la línea?** Hay una línea diagonal a ~33° entre el rojo y el amarillo. **Toda
la piel humana, de cualquier tono, cae sobre esa línea.** Es la herramienta de diagnóstico más
poderosa que existe en color. Módulo `254` completo sobre eso.

---

## 5. Histograma: para lo que sirve y para lo que no

```bash
ffmpeg -y -ss 4 -i clip.mp4 -vf "histogram=display_mode=stack:levels_mode=linear,scale=640:-1" \
  -frames:v 1 hist.png
```

Sirve para dos cosas y solo dos:

1. **Ver de un vistazo si hay recorte** (una barra alta pegada al extremo izquierdo o derecho).
2. **Ver la distribución global** para decidir exposición.

No sirve para localizar nada, no sirve para juzgar la piel, y no sirve para emparejar planos. Si
alguien gradúa mirando solo el histograma, va a terminar con un video correcto y muerto.

Un truco honesto: `levels_mode=logarithmic` hace visible lo que el lineal esconde (unos pocos píxeles
recortados que en lineal no se ven porque son 200 píxeles entre dos millones).

---

## 6. La sala de control comparativa: leer dos planos a la vez

Aquí está el uso profesional de verdad. Para emparejar (`255`), no miras un plano: miras **dos, con
sus scopes, en la misma imagen**. Comando verificado:

```bash
ffmpeg -y -hide_banner \
  -ss 4 -i planoA.mp4 -ss 2 -i planoB.mp4 \
  -filter_complex "\
[0:v]scale=480:270,setsar=1,format=yuv444p,split=2[a1][a2];\
[a2]vectorscope=mode=color3:graticule=color:flags=name+white,scale=270:270,format=yuv444p[av];\
[a1][av]hstack[top];\
[1:v]scale=480:270,setsar=1,format=yuv444p,split=2[b1][b2];\
[b2]vectorscope=mode=color3:graticule=color:flags=name+white,scale=270:270,format=yuv444p[bv];\
[b1][bv]hstack[bot];\
[top][bot]vstack,format=yuv444p" \
  -frames:v 1 comparacion.png
```

**Trampa verificada:** sin los `format=yuv444p`, ffmpeg falla con
`The following filters could not choose their formats: Parsed_vectorscope_...`. El vectorscopio
entrega un formato que `hstack` no puede mezclar con el del video. Se normalizan los tres y listo.

Lo que buscas en esa imagen: que las dos nubes del vectorscopio **estén en el mismo sitio**. No que
sean idénticas —los planos tienen contenido distinto—, sino que su centro de masa coincida. Si la de
arriba está corrida al magenta y la de abajo está centrada, ahí tienes tu trabajo.

Para monitorear un clip completo mientras corre, en vez de un frame:

```bash
ffmpeg -y -i clip.mp4 -filter_complex "\
[0:v]scale=960:540,setsar=1,format=yuv444p,split=2[v1][v2];\
[v2]waveform=intensity=0.15:mirror=1:components=1:graticule=green:flags=numbers,scale=960:300,format=yuv444p[w];\
[v1][w]vstack,format=yuv420p" -c:v libx264 -crf 20 -c:a copy monitor.mp4
```

Ese `monitor.mp4` es tu "monitor de scopes": lo reproduces y ves el video con su forma de onda
debajo, cuadro a cuadro. Es lo más cerca que estás de un panel de colorista sin comprar software.

---

## 7. Cuándo el scope miente (o mejor: cuándo no ve)

Los scopes tienen dos puntos ciegos y los dos costaron trabajo en el caso real.

**Punto ciego 1 — El promedio no ve las zonas pequeñas.**

`signalstats` promedia todo el cuadro. Una cara ocupa el 3–5 % de los píxeles de un plano medio.
Puedes bajar el magenta general un 40 % (dato real del caso) y dejar la cara igual de morada. Los
cuatro indicadores quedaron en verde y **la piel seguía morada**.

Solución: mide la zona, no el cuadro.

```bash
# 1. saca un frame y mira dónde queda la mejilla
ffmpeg -y -ss 6 -i clip.mp4 -frames:v 1 frame.png

# 2. mide SOLO ese rectángulo (ancho:alto:x:y)
ffprobe -v error -f lavfi -i "movie=clip.mp4,crop=120:120:840:420,signalstats" \
  -show_entries frame_tags=lavfi.signalstats.YAVG,lavfi.signalstats.UAVG,lavfi.signalstats.VAVG,lavfi.signalstats.SATAVG \
  -of csv=p=0 -read_intervals "%+#3"
```

Y visualmente, la versión scope de lo mismo: recortas la cara y le sacas el vectorscopio solo a ella.

```bash
ffmpeg -y -ss 6 -i clip.mp4 \
  -vf "crop=200:200:800:380,vectorscope=mode=color3:graticule=color:flags=name+white,scale=500:500" \
  -frames:v 1 vs_cara.png
```

Ese vectorscopio de la cara sola es el instrumento honesto para juzgar piel. El del cuadro completo
está dominado por la pared.

**Punto ciego 2 — El scope no sabe qué es importante.**

Un plano donde el 70 % del cuadro es una pared morada de neón va a tener un vectorscopio corrido al
magenta **y eso puede estar perfecto**. El neón es el ambiente, es lo que hace lindo al bar. Si
"corriges" hasta centrar la nube, mataste el video.

> El scope mide. La jerarquía la pones tú: qué debe verse natural (la piel, el producto, la marca) y
> qué puede estar teñido (el ambiente).

---

## 8. La rutina de lectura, en orden

Cinco minutos por plano, siempre igual:

1. **Forma de onda de luma.** ¿Recorta arriba? ¿Recorta abajo? ¿Dónde está el bulto? → decides
   exposición.
2. **Parade RGB.** Buscas una zona neutra y miras si los tres canales coinciden ahí. → decides
   balance.
3. **Vectorscopio del cuadro.** ¿La nube está centrada? ¿Cuánta saturación? → decides color global.
4. **Vectorscopio de la cara recortada.** ¿Está sobre la línea de piel? → decides secundarias (`253`).
5. **Miras el video.** Sí, con los ojos. → apruebas o no.

El paso 5 no es opcional y no es simbólico. Los cuatro anteriores pueden estar todos en verde y el
video seguir viéndose mal, y ese es literalmente lo que pasó en el caso del bar.

---

## 9. Guardar la evidencia

Un colorista profesional guarda los scopes de antes y después. Sirve para tres cosas: defender el
trabajo ante el cliente (`08`), aprender de lo que hiciste, y detectar regresiones cuando vuelves a
exportar.

```bash
# hoja de scopes antes/después de un plano
for f in antes despues; do
  ffmpeg -y -v error -ss 4 -i $f.mp4 -filter_complex "\
[0:v]scale=480:270,setsar=1,format=yuv444p,split=3[v][w][s];\
[w]waveform=intensity=0.15:mirror=1:components=1:graticule=green:flags=numbers,scale=480:270,format=yuv444p[wf];\
[s]vectorscope=mode=color3:graticule=color:flags=name+white,scale=270:270,format=yuv444p,pad=480:270:105:0[vs];\
[v][wf]hstack[a];[a][vs]hstack,format=yuv444p" -frames:v 1 scopes_$f.png
done
```

Nómbralos con el plano y la fecha (`135`) y guárdalos junto al proyecto.

---

## Errores comunes

- **Graduar mirando solo el histograma.** No localiza nada. Es el scope menos útil de los cuatro para
  color, aunque sea el más famoso.
- **Dejar `intensity` en el valor por defecto (0.004)** y concluir que "el scope no muestra nada". Con
  0.10–0.25 se ve.
- **Buscar el balance en el parade sobre una zona que no es neutra.** Si la miras sobre una pared
  amarilla, vas a "corregir" el amarillo de la pared.
- **Corregir con los medios un tinte que está en las sombras.** El parade te dice la zona; usa
  `rs/gs/bs` para sombras.
- **Apilar un scope con video sin normalizar formatos.** Falla con
  `could not choose their formats`. Pon `format=yuv444p` en las tres ramas.
- **Juzgar la piel con el vectorscopio del cuadro completo.** El fondo domina. Recorta la cara.
- **Creer que la nube centrada = imagen correcta.** Un neón morado real debe correr la nube. El scope
  no sabe qué es intencional.
- **Aprobar por métricas sin mirar el video.** Los cuatro indicadores del caso del bar quedaron en
  verde con la cara morada.
- **Leer un solo cuadro de un plano y decidir por todo el plano.** Usa `envelope=peak`, o mide varios
  cuadros con `-read_intervals`.
- **No guardar los scopes de antes.** Después no puedes demostrar nada, ni a ti mismo.

---

## Checklist

- [ ] Generé la forma de onda con `intensity` entre 0.10 y 0.25, no con el valor por defecto.
- [ ] Revisé recorte arriba (pegado a 100) y abajo (pegado a 0) antes de tocar nada.
- [ ] Identifiqué dónde está el **bulto** (30–70) y confirmé que mi sujeto vive ahí.
- [ ] Usé el parade sobre una zona que **de verdad** debería ser neutra.
- [ ] Determiné si el tinte está en sombras, medios o altas, y corregí en esa zona.
- [ ] Miré el vectorscopio con `graticule=color` para tener la línea de piel dibujada.
- [ ] Saqué un vectorscopio de **la cara recortada**, no solo del cuadro.
- [ ] Cuando emparejo, veo los dos planos con sus scopes en la misma imagen.
- [ ] Normalicé formatos (`format=yuv444p`) antes de apilar scopes con video.
- [ ] Después de leer los scopes, **miré el video** y aprobé con los ojos.
- [ ] Guardé la hoja de scopes de antes y después junto al proyecto.

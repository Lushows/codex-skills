# 63 — El look cinematográfico

"Que se vea como cine" es la petición más común y la peor definida. Nadie te va a saber decir qué
quiere. Pero sí es medible: hay cinco o seis cosas concretas que hacen que una imagen se lea como
cine y no como video de celular. Este módulo las desarma una por una, con los números.

Recordatorio antes de empezar: **esto es gradación**. Solo se aplica sobre material ya corregido y
emparejado (`61`, `62`). Si le metes look a planos disparejos, amplificas la disparidad.

---

## 1. Qué es "cine", técnicamente

Cuando alguien dice que algo se ve cinematográfico, casi siempre está reaccionando a estas seis
señales, en este orden de peso:

1. **Contraste con negros densos** — el video de celular tiene negros grises (levantados por el
   procesamiento y por querer "mostrar todo"). El cine tapa. Deja zonas que no se ven.
2. **Saturación moderada y selectiva** — el celular satura todo parejo. El cine tiene colores muy
   saturados en pocos sitios y el resto casi neutro.
3. **Separación de sombras y luces por temperatura** — sombras hacia el frío, luces hacia el
   cálido. Es el famoso *teal & orange*, que está gastadísimo pero funciona porque imita cómo se
   comporta la luz natural (sombra = cielo azul, luz = sol cálido).
4. **Halación** — el brillo que se derrama alrededor de las luces fuertes. Es un defecto de la
   película fotoquímica y del vidrio de las lentes. Digitalmente hay que ponerlo a mano.
5. **Grano** — textura fina y constante. Sin ella la imagen se ve "de plástico".
6. **Menos nitidez de la que crees** — el celular mete nitidez artificial. El cine no. Un exceso de
   `unsharp` es lo que hace que un video se vea "de video".

Y una que no es de color pero pesa más que todas: **el encuadre y el movimiento**. Ningún grado
salva un plano mal compuesto y con la cámara temblando. Si el cliente pide "cine" y el problema es
de rodaje, dilo (ver bloque 17).

---

## 2. La curva en S: el corazón del look

La curva en S es el ajuste más importante de toda la gradación. Consiste en **bajar un poco las
sombras y subir un poco las luces**, dejando los medios donde están. Resultado: más contraste, pero
sin tocar el brillo general de la escena ni la piel.

En ffmpeg se hace con `curves`, dando puntos `entrada/salida` en escala 0–1:

```bash
# Curva en S suave — el punto de partida para casi todo
ffmpeg -i in.mp4 -vf "curves=all='0/0 0.25/0.20 0.5/0.5 0.75/0.80 1/1'" -c:v libx264 -crf 18 out.mp4
```

Léelo así: lo que entraba al 25% de brillo ahora sale al 20% (más oscuro), lo que entraba al 75%
ahora sale al 80% (más claro), el 50% se queda en 50%.

Tres intensidades para elegir:

| Intensidad | Curva | Cuándo |
|---|---|---|
| Suave | `0/0 0.25/0.22 0.5/0.5 0.75/0.78 1/1` | testimonios, corporativo, comida |
| Media | `0/0 0.25/0.20 0.5/0.5 0.75/0.80 1/1` | reels, contenido de marca, anuncios |
| Fuerte | `0/0 0.25/0.17 0.5/0.5 0.75/0.84 1/1` | dramático, música, noche |

### El "levante" de negros (lifted blacks / film fade)

Truco de look muy usado: en vez de llevar el negro a 0, lo dejas ligeramente levantado. Imita la
película, que nunca era negro puro, y da una sensación suave y "de época".

```bash
# Negro levantado + curva en S: el look "film" clásico
ffmpeg -i in.mp4 -vf "curves=all='0/0.045 0.25/0.23 0.5/0.5 0.75/0.79 1/0.98'" \
  -c:v libx264 -crf 18 out.mp4
```

Ojo con la dosis: `0/0.045` ya es visible. Pasado `0/0.08` se ve lavado, no cinematográfico. Y en
plataformas que recomprimen fuerte (`68`), el negro levantado se bandea más fácil.

---

## 3. Teal & orange sin que se note

El separado de tonos (*split toning*) mete color distinto en sombras y en luces. Se hace con
`colorbalance`, que tiene tres zonas: sombras (`s`), medios (`m`), luces (`h`), por canal.

```bash
# Sombras al teal, luces al cálido — dosis discreta
ffmpeg -i in.mp4 -vf \
  "colorbalance=rs=-0.06:bs=0.08:rh=0.05:bh=-0.04,curves=all='0/0.02 0.25/0.21 0.5/0.5 0.75/0.80 1/0.99'" \
  -c:v libx264 -crf 18 out.mp4
```

Qué significa cada uno:
- `rs=-0.06` → menos rojo en las **sombras**
- `bs=0.08` → más azul en las **sombras** → las sombras se van al teal
- `rh=0.05` → más rojo en las **luces**
- `bh=-0.04` → menos azul en las **luces** → las luces se van al cálido

**Nunca toques `rm/gm/bm` (los medios) en el split toning.** Los medios son donde vive la piel. Si
mueves los medios al teal, la cara se te pone verde; si los mueves al naranja, la cara se te pone
zanahoria. Ese es el error del módulo `67` y es el más feo de todos.

Dosis honesta: `0.04–0.08` se lee como look. `0.15` se lee como Instagram de 2014. Si te acercas a
`0.20` estás haciendo un filtro, no un grado.

---

## 4. Saturación selectiva: el detalle que separa a los buenos

Subir la saturación global es lo que hace todo el mundo y es lo que hace que se vea a filtro. Lo
que hacen los coloristas es **subir unos colores y bajar otros**.

`selectivecolor` te deja tocar familias de color por separado. Cada familia recibe cuatro valores:
cian, magenta, amarillo, negro (como en imprenta), en rango −1 a 1.

```bash
# Bajar el verde chillón de la vegetación y del fluorescente,
# subir un poco el rojo/naranja de la comida y de la piel cálida
ffmpeg -i in.mp4 -vf \
  "selectivecolor=greens=0.10 0 -0.15 0.05:reds=-0.05 0 0.08 0:yellows=0 0 0.06 0" \
  -c:v libx264 -crf 18 out.mp4
```

El patrón que más se usa en video de marca y de comida:

| Familia | Qué hacer | Por qué |
|---|---|---|
| **verdes** | bajar saturación, empujar a oliva/teal | el verde crudo de plantas y tubos fluorescentes se ve barato |
| **azules** | mantener o subir un poco | da profundidad a cielos y sombras |
| **rojos / naranjas** | subir con cuidado | comida, piel, madera — es el calor de la imagen |
| **amarillos** | vigilar | es donde vive la piel; sube poco |

Si `selectivecolor` te queda grande, la versión simple es `hue` con `colorchannelmixer`, pero
`selectivecolor` es la herramienta correcta y está en cualquier ffmpeg moderno.

---

## 5. Halación: el ingrediente que casi nadie pone

La halación es el halo suave y cálido que aparece alrededor de las luces fuertes: un bombillo, una
ventana, un reflejo. En película pasaba porque la luz atravesaba la emulsión y rebotaba. En digital
no pasa, y por eso el digital se ve "duro".

Ponerla es lo que más rápido acerca una imagen a "cine". Se hace en cuatro pasos: aislar las luces,
desenfocarlas, teñirlas de cálido, y mezclarlas encima con modo `screen`.

```bash
ffmpeg -i in.mp4 -filter_complex "\
[0:v]split=2[base][hi];\
[hi]curves=all='0/0 0.72/0 0.88/0.55 1/1',\
    gblur=sigma=22,\
    colorchannelmixer=rr=1.0:gg=0.55:bb=0.35[glow];\
[base][glow]blend=all_mode=screen:all_opacity=0.30[v]" \
  -map "[v]" -map 0:a? -c:v libx264 -crf 18 -c:a copy out_halacion.mp4
```

Qué hace cada línea:
- `split=2` → dos copias de la imagen.
- `curves=...0.72/0 0.88/0.55...` → mata todo lo que no sea muy brillante. Solo sobreviven las luces.
- `gblur=sigma=22` → las desenfoca en un halo grande.
- `colorchannelmixer=rr=1.0:gg=0.55:bb=0.35` → las tiñe de naranja-rojizo (la halación real es
  rojiza porque el rojo es el que más penetra).
- `blend=all_mode=screen:all_opacity=0.30` → las suma sobre la imagen original.

**Dosis:** `all_opacity` entre `0.18` y `0.35`. Pasado `0.45` parece que hay niebla en la
habitación. Si el plano no tiene luces fuertes, la halación no hace nada — y está bien, no la
fuerces.

---

## 6. Grano: la textura que une todo

El grano hace tres cosas a la vez y por eso es tan valioso:
1. da textura de película,
2. **esconde el banding** que produce la compresión de las plataformas,
3. **une** material de fuentes distintas (cámara, celular, IA) bajo una misma piel.

```bash
# Grano fino, temporal (cambia cada frame) y solo en luma
ffmpeg -i in.mp4 -vf "noise=alls=7:allf=t+u,format=yuv420p" -c:v libx264 -crf 18 out.mp4
```

- `alls=7` → intensidad. 4–6 discreto, 7–10 visible, +14 ya es efecto.
- `allf=t` → temporal: el grano cambia en cada fotograma. **Sin la `t` el grano queda quieto y se ve
  como suciedad en el lente.**
- `allf=u` → uniforme, más parecido al grano fotoquímico que el gaussiano por defecto.

Detalle importante: el grano **cuesta bitrate**. Si exportas con CRF alto, el compresor se pelea con
el grano y te devuelve bloques. Con grano, baja el CRF 1 o 2 puntos (de 23 a 21, por ejemplo).
Detalle en `66-viñeta-nitidez-y-textura.md`.

---

## 7. La cadena completa de un look "cine" honesto

Junta todo, en el orden correcto, sobre material ya corregido:

```bash
ffmpeg -i corregido/plano.mp4 -filter_complex "\
[0:v]curves=all='0/0.030 0.25/0.21 0.5/0.5 0.75/0.80 1/0.99',\
     colorbalance=rs=-0.05:bs=0.07:rh=0.04:bh=-0.03,\
     selectivecolor=greens=0.08 0 -0.12 0.04:reds=-0.04 0 0.06 0,\
     eq=saturation=1.04[graded];\
[graded]split=2[base][hi];\
[hi]curves=all='0/0 0.74/0 0.9/0.55 1/1',gblur=sigma=20,\
    colorchannelmixer=rr=1.0:gg=0.55:bb=0.35[glow];\
[base][glow]blend=all_mode=screen:all_opacity=0.24[hal];\
[hal]unsharp=5:5:0.35:5:5:0.0,vignette=PI/5,noise=alls=6:allf=t+u,format=yuv420p[v]" \
  -map "[v]" -map 0:a? \
  -c:v libx264 -crf 17 -preset slow \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
  -c:a copy final/plano_LOOK.mp4
```

Orden: curva → split toning → saturación selectiva → saturación global → halación → nitidez →
viñeta → grano → formato. **Ese orden importa**: la halación se calcula sobre la imagen ya
graduada, y el grano va de último para que no se desenfoque ni se le aplique nitidez encima.

---

## 8. Cómo NO caer en el look genérico

Lo que hace que un grado se vea de plantilla:

- **Teal & orange al 20%.** Se reconoce a un kilómetro.
- **Saturación global +25%.** Es el "filtro de Instagram".
- **Viñeta pesada** (`vignette=PI/3` o más). Grita amateur.
- **Negros levantados de más** con "mate" por todas partes.
- **La misma LUT gratuita que usan todos.** Si la bajaste de un pack, mil personas la tienen.

Lo que hace que se vea propio:

- **Salir de la paleta de la marca**, no de un preset. Ver `64-forzar-la-paleta-de-marca.md`.
- **Un solo color que "canta"** y el resto contenido. Elige uno.
- **Dosis pequeñas de muchas cosas** en vez de una dosis grande de una sola.
- **Consistencia entre piezas.** El look de la marca es el mismo en el reel 1 y en el reel 40.

---

## Errores comunes

- **Aplicar el look sin haber corregido y emparejado.** Todo lo de este módulo se cae. Ver `61`.
- **Mover los medios (`rm/gm/bm`) en el split toning.** La piel se te va a verde o a naranja. El
  error más feo del oficio (`67`).
- **Pasarse con la dosis.** `colorbalance` en 0.15+, saturación en 1.25+, viñeta en PI/3: eso ya no
  es cine, es filtro.
- **Poner grano estático** (sin `allf=t`). Parece polvo en el lente y en video se nota horrible.
- **Meter grano y exportar con CRF alto.** Bloques garantizados. Baja el CRF 1–2 puntos.
- **Abusar de `unsharp`.** El exceso de nitidez es literalmente lo contrario de "cine". Máximo
  `0.5` en luma, y `0.0` en croma siempre.
- **Poner halación en un plano sin luces fuertes.** No hace nada y solo te lava la imagen.
- **Cambiar el look entre planos "porque a este le queda mejor".** El look es uno para todo el
  video; si un plano lo necesita distinto es que le falta corrección.
- **Confundir "cine" con "oscuro".** Bajarle brillo a todo no es un look; es un video que no se ve
  en el celular a plena luz.
- **Ignorar que el problema era el encuadre o el temblor.** Ningún grado lo arregla; dilo.

---

## Checklist

- [ ] El material está corregido y emparejado antes de empezar (`61`, `62`).
- [ ] Apliqué una curva en S y elegí la intensidad a propósito (suave / media / fuerte).
- [ ] Si levanté los negros, la dosis está por debajo de `0/0.06`.
- [ ] El split toning solo toca **sombras** y **luces**. Los medios están intactos.
- [ ] Las dosis de `colorbalance` están entre 0.03 y 0.08.
- [ ] Usé saturación **selectiva** (`selectivecolor`), no solo la global.
- [ ] La saturación global está por debajo de 1.10.
- [ ] La halación, si la usé, está entre 0.18 y 0.35 de opacidad, y el plano tiene luces que la
      justifiquen.
- [ ] El grano es temporal (`allf=t+u`) y está entre 4 y 10.
- [ ] Bajé el CRF 1–2 puntos por el grano.
- [ ] `unsharp` está en 0.5 o menos, con croma en 0.0.
- [ ] Verifiqué la piel después del look (`67`).
- [ ] El look es **idéntico** en todos los planos y lo puedo reutilizar en la próxima pieza.

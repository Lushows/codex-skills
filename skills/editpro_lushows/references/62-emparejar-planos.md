# 62 — Emparejar planos

Emparejar (en inglés *shot matching*) es lograr que planos grabados en momentos, luces y cámaras
distintas **se sientan del mismo video**. No que se vean idénticos —eso sería falso—, sino que
pertenezcan al mismo mundo.

Es el trabajo menos glamoroso del color y el que más diferencia hay entre un video amateur y uno
profesional. Un espectador no sabe explicar por qué un video "se ve barato", pero lo que está
sintiendo casi siempre es esto: cada corte lo saca del video porque el color salta.

Este módulo es la parte más difícil de la corrección (`61`) y por eso tiene su propio archivo.

---

## 1. El caso real: el bar con neón morado y la terraza a plena luz

El ejemplo que vamos a usar es uno de verdad, de un video de un bar-restaurante:

- **Plano A** — interior del bar, luz de neón morado, oscuro, croma cargadísimo al magenta,
  sombras sin detalle.
- **Plano B** — terraza, mediodía, sol directo, contraste altísimo, blancos casi reventados,
  colores naturales.

Sin trabajo, cortar de A a B es un fogonazo. El espectador parpadea. Y el problema no es solo el
brillo: es que **son dos mundos de color distintos**.

La cadena que resolvió ese caso, aplicada al material del bar para acercarlo a la terraza ya
corregida, fue:

```
eq=contrast=1.10:saturation=1.06:gamma=0.98:gamma_r=0.99:gamma_b=1.02,unsharp=5:5:0.5:5:5:0.0,vignette=PI/5
```

Comando completo:

```bash
ffmpeg -i bruto/bar_neon.mp4 -vf \
  "eq=contrast=1.10:saturation=1.06:gamma=0.98:gamma_r=0.99:gamma_b=1.02,unsharp=5:5:0.5:5:5:0.0,vignette=PI/5,format=yuv420p" \
  -c:v libx264 -crf 15 -preset medium -c:a copy corregido/bar_neon.mp4
```

Vale la pena desarmarla pieza por pieza, porque cada número tiene una razón:

| Parte | Qué hace | Por qué en este caso |
|---|---|---|
| `contrast=1.10` | +10% de contraste | el neón aplana la imagen; le devuelve separación |
| `saturation=1.06` | +6% de saturación | compensa lo que el contraste "apaga" perceptualmente |
| `gamma=0.98` | oscurece un pelín los medios | el plano venía lechoso |
| `gamma_r=0.99` | baja el rojo en los medios | quita el exceso de magenta del neón |
| `gamma_b=1.02` | sube el azul en los medios | mete un poco de frío, aleja del magenta |
| `unsharp=5:5:0.5:5:5:0.0` | nitidez suave solo en luma | el interior oscuro se ve blando; croma en 0.0 para no ensuciar |
| `vignette=PI/5` | viñeta discreta | cierra la mirada al centro y disimula el desnivel de luz |

La lección importante: **el emparejamiento se hace con `gamma_r` / `gamma_g` / `gamma_b`, no con
`saturation` global**. La saturación global sube todo, incluido el problema. Los gammas por canal
mueven el equilibrio de color de la zona media, que es donde vive la mayoría de la imagen y donde
vive la piel.

---

## 2. El flujo paso a paso

### Paso 1 — Elige el plano de referencia (el "héroe")

Uno solo. El que:
- esté mejor expuesto,
- tenga piel visible y bien vista,
- represente el look que quieres para todo el video.

Todo lo demás se va a mover **hacia él**. Si eliges mal, te toca mover doce planos en vez de uno.
Escoge el que menos trabajo dé y más se parezca al destino.

> Si ningún plano sirve de referencia, corriges primero UN plano hasta que te guste, lo exportas, y
> **ese archivo corregido** es tu referencia. No se empareja contra un ideal mental.

### Paso 2 — Saca un fotograma representativo de cada plano

No un fotograma cualquiera: uno en el que se vea la escena típica, ni el más oscuro ni el más claro.

```bash
# Un frame a los 3 segundos de cada clip, con nombre legible
for f in bruto/*.mp4; do
  n=$(basename "$f" .mp4)
  ffmpeg -y -ss 3 -i "$f" -frames:v 1 -q:v 2 frames/"$n".png
done
```

Estos PNG son con lo que vas a comparar. Un modelo (yo) puede mirarlos lado a lado; tú también.
Ver 12 imágenes juntas te dice en dos segundos cuál plano se sale del grupo.

Y para verlos todos en una sola imagen (hoja de contactos, ver `17-hoja-de-contactos.md`):

```bash
ffmpeg -y -pattern_type glob -i "frames/*.png" -vf "scale=480:-1,tile=4x3" contactos.png
```

### Paso 3 — Mide, no adivines

Por cada plano, saca los números:

```bash
for f in bruto/*.mp4; do
  echo "=== $f ==="
  ffmpeg -hide_banner -ss 2 -t 4 -i "$f" \
    -vf "signalstats,metadata=mode=print:file=-" -f null - 2>&1 \
    | grep -E "lavfi\.signalstats\.(YMIN|YAVG|YMAX|UAVG|VAVG|SATAVG)" \
    | awk -F= '{s[$1]+=$2; n[$1]++} END{for(k in s) printf "%s %.1f\n", k, s[k]/n[k]}'
done
```

Te queda una tabla mental así:

| Plano | YAVG (brillo medio) | UAVG (azul↔) | VAVG (rojo↔) | SATAVG |
|---|---|---|---|---|
| terraza (**ref**) | 128 | 127 | 130 | 42 |
| bar_neon | 78 | 138 | 141 | 71 |
| barra_detalle | 96 | 133 | 136 | 58 |

Ahora ya no estás adivinando. Sabes que `bar_neon` está **50 puntos más oscuro**, con **+11 de
azul**, **+11 de rojo** (o sea magenta: azul y rojo arriba a la vez) y **casi el doble de
saturación**. Esa tabla te dicta los ajustes.

Regla de traducción rápida:

- **YAVG bajo** → sube `gamma` (no `brightness`).
- **UAVG alto** → el plano tira a azul → baja azul: `gamma_b` < 1 o `colorbalance` negativo en b.
- **VAVG alto** → tira a rojo → baja rojo: `gamma_r` < 1.
- **UAVG y VAVG altos a la vez** → magenta (el caso del neón) → baja rojo y sube azul relativo, que
  es exactamente `gamma_r=0.99:gamma_b=1.02`.
- **SATAVG muy distinto** → ajusta `eq=saturation` **de ese plano**, no de todos.

### Paso 4 — Empareja en tres capas, en este orden

Siempre en este orden, porque cada capa cambia la lectura de la siguiente:

1. **Exposición** (brillo general) — `eq=gamma`
2. **Contraste** (separación entre sombras y luces) — `eq=contrast` o `curves`
3. **Color** (equilibrio de tinte) — `gamma_r/g/b`, `colorbalance`, `colortemperature`

Si empiezas por el color, cada vez que muevas la exposición vas a tener que volver a hacer el color.
Un plano bien emparejado se hace en una pasada de estas tres, no en veinte iteraciones.

### Paso 5 — Verifica con el corte real, no con los frames sueltos

Dos planos pueden verse parejos en PNG y saltar en movimiento. Monta el corte de prueba:

```bash
# Une los dos planos vecinos con 1 s de cada lado y míralo
ffmpeg -y -i corregido/terraza.mp4 -i corregido/bar_neon.mp4 -filter_complex \
  "[0:v]trim=start=4:end=6,setpts=PTS-STARTPTS[a];[1:v]trim=start=1:end=3,setpts=PTS-STARTPTS[b];[a][b]concat=n=2:v=1:a=0[v]" \
  -map "[v]" -c:v libx264 -crf 18 prueba_corte.mp4
```

Y si quieres verlos **lado a lado** en la misma pantalla, que es la prueba más dura:

```bash
ffmpeg -y -i corregido/terraza.mp4 -i corregido/bar_neon.mp4 -filter_complex \
  "[0:v]scale=540:-1[l];[1:v]scale=540:-1[r];[l][r]hstack=inputs=2" \
  -frames:v 240 -c:v libx264 -crf 18 lado_a_lado.mp4
```

Si en el lado a lado no se distingue de cuál cámara viene cada uno por el color, terminaste.

---

## 3. Los cuatro casos difíciles y cómo se resuelven

### Caso A — Dos cámaras distintas (celular + cámara)

El celular procesa: satura, mete nitidez y contrasta de fábrica. La cámara entrega plano. No
intentes subir la cámara al nivel del celular: **baja el celular**. Casi siempre
`eq=saturation=0.92:contrast=0.96` sobre el material del celular lo acerca más que cualquier cosa
que le hagas a la cámara.

### Caso B — La misma escena a distintas horas

El sol se movió. Cambian temperatura Y dirección de la luz. La temperatura la arreglas; la dirección
**no**. Si la sombra en la cara cambia de lado, ningún color lo salva: es un problema de montaje
(no cortar directo entre esos dos, meter un plano intermedio, ver `26-continuidad.md`).

### Caso C — Material de archivo o de stock mezclado con lo tuyo

El stock viene graduado por otra persona. Lo primero es **desgraduarlo**: bajarle contraste y
saturación hacia neutro, y solo entonces meterlo en tu cadena.

```bash
ffmpeg -i stock.mp4 -vf "eq=contrast=0.93:saturation=0.90,format=yuv420p" \
  -c:v libx264 -crf 15 corregido/stock_neutro.mp4
```

### Caso D — Imágenes o video generados por IA mezclados con material real

Es el caso más frecuente hoy y el que más delata. Lo generado por IA viene con un contraste y una
saturación de "portada", además de rango completo y sRGB. Tratamiento: convertir espacio y rango
(ver `60`), bajarle contraste y saturación, **y meterle grano** para igualar la textura del material
filmado (ver `66`). Sin grano, el plano de IA se ve "limpio de más" y por eso se nota.

---

## 4. Emparejar audio-visualmente: el truco del corte de prueba invertido

Un método rápido para saber si dos planos están parejos: **haz el corte al revés**. Si el video va
A→B, monta B→A. Si el salto se siente igual de fuerte en las dos direcciones, el problema es de
color. Si solo se siente en una dirección, el problema es de brillo (el ojo se adapta más rápido de
claro a oscuro que al revés) y basta con acercar exposiciones.

---

## 5. Cuándo NO hay que emparejar

Emparejar no es uniformar. Hay casos donde la diferencia es la historia:

- **Antes y después** — el "antes" puede ser deliberadamente más frío y apagado.
- **Recuerdo / flashback** — cambio de color intencional.
- **Cambio de locación con salto de tiempo** — si el video dice "y al otro día", el color puede y
  debe cambiar.
- **Material de archivo presentado como archivo** — si se ve viejo a propósito, déjalo viejo.

La regla: **la diferencia de color tiene que ser una decisión, no un accidente.** Si no la puedes
justificar en una frase, es un accidente y hay que emparejar.

---

## Errores comunes

- **Emparejar a ojo, sin sacar frames ni medir.** Vas a iterar diez veces y a terminar peor.
- **No elegir un plano de referencia.** Sin referencia, cada plano se acerca a un ideal distinto y
  el conjunto queda igual de disparejo, pero ahora con trabajo encima.
- **Usar `brightness` para igualar exposición.** Ensucia los negros. Es `gamma`.
- **Corregir el tinte con saturación global.** Sube el problema junto con lo demás. Es `gamma_r/g/b`
  o `colorbalance`.
- **Emparejar después de aplicar el look.** El error del módulo `61`. Imposible de arreglar.
- **Comparar frames de momentos distintos del clip** (uno con la persona de espaldas y otro de
  frente). Elige frames comparables.
- **Subir el material bueno al nivel del material procesado del celular**, en vez de bajar el
  celular. Siempre es más fácil quitar que inventar.
- **Meter material de IA sin grano.** Se ve pegado encima, por más que el color esté igual.
- **Olvidar que la luz cambió de dirección.** El color no arregla continuidad de iluminación.
- **Emparejar planos que deberían ser distintos** (el antes/después, el flashback) y matar la
  narración por pulcritud.

---

## Checklist

- [ ] Elegí **un** plano de referencia y lo tengo exportado ya corregido.
- [ ] Saqué un frame representativo de cada plano y armé la hoja de contactos.
- [ ] Corrí `signalstats` en todos los planos y tengo la tabla YAVG / UAVG / VAVG / SATAVG.
- [ ] Emparejé en orden: exposición → contraste → color. No al revés.
- [ ] Usé `gamma_r/g/b` o `colorbalance` para el tinte, no `saturation` global.
- [ ] El material de otra cámara/stock/IA lo llevé a neutro **antes** de meterlo a la cadena.
- [ ] Al material de IA le puse grano para igualar textura.
- [ ] Monté el corte de prueba real (no solo frames) y lo revisé en las dos direcciones.
- [ ] Hice la prueba de lado a lado (`hstack`) en al menos el par más difícil.
- [ ] Las diferencias de color que quedan son **decisiones** que puedo justificar en una frase.
- [ ] Solo después de todo esto empecé a graduar (`63`, `64`).

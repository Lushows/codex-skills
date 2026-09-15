# 164 — Evento y aftermovie

**Qué resuelve:** cubriste un evento de cuatro horas — una fiesta, un lanzamiento, un congreso, un
matrimonio, la apertura de un local — y el cliente quiere "un video de 60 segundos que se sienta como
estuvo". Este módulo es cómo se busca el pico entre horas de nada, cómo la música dicta la estructura, y
cómo se graba pensando en el montaje para no llegar al computador con material inservible.

> **Término nuevo — aftermovie:** pieza corta y montada al ritmo de música que resume la sensación de un
> evento. No documenta el evento: **lo vende**. Su público principal es quien NO fue, para que quiera ir
> la próxima vez.

---

## 1. El aftermovie no cuenta, hace sentir

Esa es la diferencia con el documental. Nadie quiere saber a qué hora habló el gerente. Quieren saber
**cómo se sintió estar ahí**. El montaje persigue una sola cosa: densidad de energía.

```
Documental de evento  →  qué pasó, en orden, con contexto.        3–8 min.
Aftermovie            →  cómo se sintió, sin orden, con música.   45–90 s.
Recap para redes      →  los 3 mejores momentos, vertical.        15–30 s.
```

**Casi siempre el cliente pide "un video" y necesita los tres.** Se montan del mismo bruto y se cotizan
aparte. Ver `159-campaña-multipieza.md`.

---

## 2. Grabar un evento pensando en el montaje

Un aftermovie se gana o se pierde grabando. Lo que el editor necesita que le traigan:

### La lista mínima (sin esto no hay aftermovie)

| Plano | Cuántos | Por qué |
|---|---|---|
| **Detalles** (manos, copas, comida, decoración, letreros) | 20–30 | Son el 40% del montaje final |
| **Caras reaccionando** (riendo, aplaudiendo, sorprendidas) | 15+ | Es lo que produce emoción |
| **Plano general del lugar lleno** | 4–6 | Prueba de que hubo gente |
| **Movimiento de cámara lento** sobre algo | 8–10 | Da respiro entre cortes rápidos |
| **El momento clave** desde 2 ángulos | 1 momento | Corte de cinta, brindis, entrada |
| **Antes vacío** (montaje, preparativos) | 5–8 | Da arco: de vacío a lleno |
| **Timelapse del llenado** | 1–2 | Comunica magnitud en 2 segundos |

### Duración de cada toma en rodaje

**Mínimo 6 segundos por toma, quieto.** Suena obvio y nadie lo hace. Si grabas 2 segundos y mueves, no hay
nada usable: el editor necesita margen para entrar y salir del plano. Y las tomas cortas no se pueden
ralentizar.

### Frame rate

Graba los detalles y las reacciones a **60 fps mínimo**, ideal 120. En aftermovie se ralentiza mucho, y
ralentizar 30 fps produce tirones.

```bash
# Comprobar a qué fps vino cada archivo antes de montar
for f in bruto/*.mp4; do
  echo "$f: $(ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of csv=p=0 "$f")"
done
```

### Audio

El audio del evento casi nunca se usa (la música del lugar tiene derechos y suena mal grabada), **pero sí
se usan los sonidos sueltos**: el descorche, el aplauso, el grito, el vidrio. Grábalos a propósito. Ver
sección 7.

---

## 3. De 4 horas a 60 segundos: el proceso

### Paso 1 — El descarte técnico (2 h → 45 min de material)

Se bota sin ver el contenido: lo desenfocado, lo movido sin remedio, lo subexpuesto, lo tapado por una
cabeza.

```bash
# Detección de planos negros/perdidos para descarte rápido
ffmpeg -i camara1.mp4 -vf "blackdetect=d=0.5:pic_th=0.95" -f null - 2> negros.txt
```

### Paso 2 — La caza de picos

Un pico es un momento donde **pasa algo con energía visible**: alguien salta, se ríe fuerte, se abraza, se
descorcha, se prende la luz. Marca cada uno con su timecode.

En un evento de 4 horas hay entre **25 y 50 picos reales**. De ahí saldrá el 70% del aftermovie.

Truco: si grabaste con audio, los picos suelen coincidir con los máximos de volumen ambiente. La forma de
onda te da un mapa de dónde buscar:

```bash
# Forma de onda del audio completo: los "cerros" son los picos del evento
ffmpeg -i camara1.mp4 -filter_complex "aformat=channel_layouts=mono,showwavespic=s=3840x300" \
  -frames:v 1 onda_evento.png
```

### Paso 3 — La hoja de contactos

Los detalles y planos de textura se eligen mirando, no viendo:

```bash
ffmpeg -i bruto_concatenado.mp4 -vf "fps=1/5,scale=200:-1,tile=12x8" contactos_evento.png
```

De ahí sacas los detalles bonitos que jamás verías reproduciendo 4 horas.

### Paso 4 — El banco

Terminas con tres carpetas:

```
picos/       25–50 clips de 2–5 s  (energía)
detalles/    20–40 clips de 2–4 s  (textura)
generales/   6–12 clips de 4–8 s   (contexto y respiro)
```

Y **con eso se monta**. Nunca vuelves al bruto de 4 horas.

---

## 4. La música manda: montar sobre la canción

En aftermovie **la canción se elige primero y no se cambia**. Toda la estructura sale de ella.

### Cómo se elige

- **Que tenga estructura clara**: intro → build → drop → calma → drop final
- **Que dure 10–15 s más de lo que necesitas** (para cortarla bien)
- **Que sea licenciable**. Ver `78-derechos-de-musica.md`. Un aftermovie de cliente con música con
  Content ID es un video que no se puede publicar.
- **Sin voz** o con voz mínima. La letra compite con las imágenes.

### Mapear la canción

Antes de poner un solo clip, escribes el mapa:

```
0:00 – 0:08   intro, solo pad          → planos de vacío, preparativos, lento
0:08 – 0:16   entra percusión          → primeras caras, ritmo medio
0:16 – 0:24   build (sube tensión)     → cortes cada vez más cortos
0:24          DROP                     → EL PLANO MÁS FUERTE del evento
0:24 – 0:40   drop                     → picos, 0,4–0,8 s por plano
0:40 – 0:48   breakdown (baja)         → un plano largo, cámara lenta, respiro
0:48 – 1:00   drop final               → los mejores picos guardados
1:00 – 1:06   cola                     → logo / fecha / próxima edición
```

**El drop se decide antes que nada.** ¿Cuál es el plano que va exactamente en el drop? Ese plano es el
video. Si no tienes uno lo suficientemente fuerte, el aftermovie no va a funcionar y hay que decirlo.

### Encontrar los beats con precisión

```bash
# Detecta los golpes fuertes: cada línea es un beat candidato con su segundo
ffmpeg -i cancion.mp3 -af "highpass=f=100,lowpass=f=180,silencedetect=n=-24dB:d=0.05" \
  -f null - 2> beats.txt
```

Ese filtro aísla el bombo (100–180 Hz) y reporta cada golpe. También sirve el enfoque manual: BPM de la
canción → duración del beat.

```
BPM 128  →  60 / 128 = 0,469 s por beat
1 beat  = 0,469 s   (muy rápido, solo en el drop)
2 beats = 0,938 s   (el estándar del aftermovie)
4 beats = 1,875 s   (respiro)
8 beats = 3,750 s   (plano largo, breakdown)
```

**Los cortes van en múltiplos de beats, nunca en medios.** Un corte a 1,3 s cuando el beat es 0,94 se
siente mal aunque nadie sepa explicar por qué. Detalle en `24-ritmo-y-musica.md`.

---

## 5. Armar el corte al beat con ffmpeg

Con la lista de duraciones ya decidida (múltiplos de beat), se cortan los clips exactos y se pegan:

```bash
# Cada clip cortado a duración de beat exacto, mismo códec para poder concatenar
ffmpeg -ss 12.40 -i picos/03.mp4 -t 0.938 -vf "scale=1920:1080,fps=30" -an -c:v libx264 -crf 18 c03.mp4
ffmpeg -ss 04.10 -i picos/07.mp4 -t 0.938 -vf "scale=1920:1080,fps=30" -an -c:v libx264 -crf 18 c07.mp4
# ...

# Lista y concatenación
printf "file 'c03.mp4'\nfile 'c07.mp4'\n" > lista.txt
ffmpeg -f concat -safe 0 -i lista.txt -c copy montaje_mudo.mp4

# Pegar la canción encima
ffmpeg -i montaje_mudo.mp4 -i cancion.mp3 -map 0:v -map 1:a \
  -c:v copy -c:a aac -b:a 256k -shortest aftermovie.mp4
```

**Verificación obligatoria:** si el montaje mudo dura 61,2 s y la canción tiene el drop en 24,0 s, tu
plano del drop tiene que empezar exactamente en 24,0. Un desfase de 0,15 s ya se siente.

---

## 6. Cámara lenta: el recurso del formato

El aftermovie vive de la cámara lenta. Pero no toda:

| Momento | Velocidad |
|---|---|
| Detalles (copa, comida, tela) | 40–50% |
| Reacción de una cara | 50–60% |
| Movimiento de multitud | 60–70% |
| El plano del drop | **100% o incluso acelerado** |
| Breakdown / respiro | 30–40% |

**El plano del drop casi siempre va a velocidad normal.** Después de 20 segundos de cámara lenta, la
velocidad real golpea más que cualquier ralentí.

```bash
# Cámara lenta al 45% desde 120 fps, salida a 30 fps (fluida de verdad)
ffmpeg -i detalle_120fps.mp4 -vf "setpts=PTS/0.45,fps=30" -an detalle_lento.mp4
```

Si el material vino a 30 fps y hay que ralentizar, interpolación:

```bash
ffmpeg -i detalle_30fps.mp4 -vf "minterpolate=fps=60:mi_mode=mci,setpts=PTS/0.5,fps=30" \
  -an detalle_lento.mp4
```

---

## 7. Sonido: la capa que separa a un aftermovie bueno del promedio

El 90% de los aftermovies son solo la canción. El 10% que se siente profesional tiene **sonido real por
encima de la música en momentos puntuales**.

### La técnica

Escoges 4–6 momentos y en cada uno subes el sonido directo durante 0,5–1,5 s:

- El descorche
- El aplauso cuando corta la cinta
- El "¡uuuuh!" de la gente
- El vidrio que choca en el brindis
- La puerta que se abre

La música se agacha 4–6 dB durante ese instante y vuelve. Es exactamente lo que hacen los aftermovies
que se sienten caros.

```bash
# Sonido directo puntual por encima de la música, entre 18,2 s y 19,4 s
ffmpeg -i montaje_con_directo.mp4 -i cancion.mp3 -filter_complex \
 "[1:a]volume=enable='between(t,18.2,19.4)':volume=0.5[mus]; \
  [0:a]volume=enable='between(t,18.2,19.4)':volume=1.6[dir]; \
  [mus][dir]amix=inputs=2:duration=first:dropout_transition=0[a]" \
 -map 0:v -map "[a]" -c:v copy aftermovie_con_sonido.mp4
```

### Whoosh y transición sonora

Un whoosh corto (0,3 s) antes del drop hace que el drop pegue más. Uno solo, no diez. → `76-diseño-sonoro.md`.

---

## 8. Texto en el aftermovie

Poquísimo: el texto rompe el trance. **Apertura:** nombre del evento + fecha, 1,5 s. **Cierre:** logo,
fecha de la próxima edición, arroba. **Nada en el medio**, salvo un dato que impresione ("+800 personas")
1 s en el breakdown. Rótulos con nombres de personas: no. Eso es documental, no aftermovie.

---

## 9. Las tres piezas del mismo material

Del mismo banco de clips salen tres entregables:

| Pieza | Duración | Formato | Diferencia de montaje |
|---|---|---|---|
| **Aftermovie** | 60–90 s | 16:9 | Música completa, estructura de canción, para web y pantalla |
| **Recap vertical** | 15–30 s | 9:16 | Solo picos, sin breakdown, texto grande, subtítulos si hay voz |
| **Resumen documental** | 3–5 min | 16:9 | Con orden cronológico, discursos, testimonios, rótulos |

**No es reencuadrar el mismo corte.** El vertical necesita planos más cerrados y otro ritmo. Ver
`38-adaptar-un-video-a-varios-formatos.md`.

```bash
# Reencuadre inteligente a vertical con la acción centrada, no un simple crop centrado
ffmpeg -i aftermovie.mp4 -vf "crop=608:1080:656:0,scale=1080:1920" -c:a copy vertical_base.mp4
```

(La `x=656` se ajusta plano por plano; un crop centrado fijo corta cabezas la mitad del tiempo.)

---

## 10. Color en evento

El material de evento viene con luces de colores, mezcla de temperaturas y ISO alto. Lo mínimo:

1. **Emparejar temperatura** entre cámaras y momentos → `62`
2. **Contraste alto y negros levantados** — el look de aftermovie estándar
3. **Ruido:** el ISO alto se nota. Reducción suave, no total (mata el detalle)

```bash
# Look de aftermovie: contraste, negros levantados, saturación ligera, ruido controlado
ffmpeg -i corte.mp4 -vf \
 "hqdn3d=2:1.5:3:3,curves=all='0/0.04 0.25/0.20 0.75/0.82 1/1',eq=saturation=1.12,unsharp=5:5:0.5" \
 -c:a copy corte_color.mp4
```

---

## Errores comunes

1. **Llegar al montaje sin detalles.** Solo planos generales de gente parada. No hay aftermovie posible.
2. **Tomas de 2 segundos.** Sin margen no hay corte, y no se pueden ralentizar.
3. **Grabar todo a 30 fps** y pretender cámara lenta. Sale con tirones.
4. **Elegir la música al final.** Toda la estructura sale de la canción; escogerla al final obliga a
   rehacer el montaje.
5. **Música con Content ID.** El cliente no puede publicar el video que le entregaste.
6. **Cortes que no caen en el beat.** El error más audible del formato, aunque el espectador no sepa
   nombrarlo.
7. **No tener un plano lo suficientemente fuerte para el drop.** Hay que detectarlo antes de montar y
   avisarle al cliente.
8. **Cámara lenta en todo, incluido el drop.** El drop pega porque contrasta con lo anterior.
9. **Solo música, sin sonido directo puntual.** Es lo que separa el aftermovie de agencia del genérico.
10. **Meter los discursos.** Van en el resumen documental, no en el aftermovie.
11. **Rótulos con nombres de personas** en un aftermovie. Rompe el trance.
12. **Sin arco de vacío a lleno.** Los planos del montaje previo cuestan 30 segundos de grabación y dan
    estructura gratis.
13. **Entregar el vertical como crop centrado del horizontal.** Cabezas cortadas todo el video.
14. **Cerrar con fundido a negro largo.** Termina en el último golpe de la canción, seco.

---

## Checklist

- [ ] Bruto descartado técnicamente (desenfocado, movido, tapado, negro)
- [ ] Banco armado en tres carpetas: picos / detalles / generales
- [ ] Al menos 20 planos de detalle y 15 de reacción disponibles
- [ ] Canción elegida ANTES de montar, licenciable, con estructura clara
- [ ] Mapa de la canción escrito (intro / build / drop / breakdown / drop final)
- [ ] El plano del drop está decidido y es el más fuerte del evento
- [ ] Todos los cortes caen en múltiplos de beat, verificados
- [ ] El drop del montaje coincide con el drop de la canción dentro de ±0,05 s
- [ ] Cámara lenta variada según el momento; el drop va a velocidad normal
- [ ] 4–6 momentos de sonido directo por encima de la música
- [ ] Un solo whoosh antes del drop, no una batería de efectos
- [ ] Texto mínimo: apertura y cierre, nada en el medio
- [ ] Arco visual de vacío a lleno presente
- [ ] Color emparejado entre cámaras y momentos; ruido controlado sin matar el detalle
- [ ] Vertical reencuadrado plano por plano, no crop centrado fijo
- [ ] Termina en el golpe final de la canción, sin fundido largo
- [ ] Pasó `98-verificacion-del-corte.md`

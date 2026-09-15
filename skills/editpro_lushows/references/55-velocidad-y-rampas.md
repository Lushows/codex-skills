# 55 — Velocidad y rampas: cámara lenta, acelerado y speed ramp

> Cambiar la velocidad de un clip es una de las cosas más fáciles de hacer mal. Este módulo tiene los
> comandos verificados y, más importante, los números de cuándo cada método funciona y cuándo produce
> basura.

---

## Los dos filtros que hacen todo

| Filtro | Qué toca | Regla |
|---|---|---|
| `setpts` | La velocidad del **video** | Multiplicas para ir lento, divides para ir rápido |
| `atempo` | La velocidad del **audio** | Al revés: el factor es la velocidad, no el multiplicador |

Esa inversión es la primera trampa. Míralo así:

| Quiero... | `setpts` | `atempo` |
|---|---|---|
| Mitad de velocidad (lento) | `setpts=2.0*PTS` | `atempo=0.5` |
| Velocidad normal | `setpts=1.0*PTS` | `atempo=1.0` |
| Doble de velocidad (rápido) | `setpts=0.5*PTS` | `atempo=2.0` |
| 40% de velocidad | `setpts=2.5*PTS` | `atempo=0.4` |

**El número de `setpts` es el inverso del de `atempo`.** Si te equivocas, el audio se desfasa del
video y nada te lo avisa: el render sale bien, solo que la boca no coincide con la voz.

### La fórmula

```
factor_setpts = 1 / velocidad_deseada
factor_atempo = velocidad_deseada
```

---

## Cámara lenta sin interpolación (la básica)

Es la que se usa el 90% de las veces. `setpts` simplemente **estira los tiempos** de los fotogramas
que ya existen.

```bash
ffmpeg -y -i clip.mp4 -filter_complex \
"[0:v]setpts=2.0*PTS[v];[0:a]atempo=0.5[a]" \
  -map "[v]" -map "[a]" -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p -c:a aac lento.mp4
```

Verificado: un clip de 4,000 s sale en 8,007 s. Correcto.

### El límite real (esto es lo importante)

`setpts` **no inventa fotogramas**. Si tu clip tiene 30 fps y lo pones a la mitad, ahora tienes 15
fotogramas reales por segundo repartidos en el doble de tiempo. Se ve a saltos.

La regla dura:

> **Un clip solo aguanta cámara lenta hasta que sus fotogramas por segundo efectivos bajen de 24.**

| Grabado a | Lento máximo aceptable | Resultado en fps efectivos |
|---|---|---|
| 24 fps | Casi nada (0,95×) | Ya está en el límite |
| 30 fps | 0,80× (`setpts=1.25*PTS`) | 24 fps |
| 60 fps | 0,40× (`setpts=2.5*PTS`) | 24 fps |
| 120 fps | 0,20× (`setpts=5.0*PTS`) | 24 fps |
| 240 fps | 0,10× (`setpts=10*PTS`) | 24 fps |

**Conclusión práctica:** la cámara lenta no se arregla en edición. Se decide en el rodaje. Si el
cliente quiere cámara lenta, hay que grabar a 60, 120 o 240 fps. Ver `170` y `171`.

Cómo saber a cuántos fps se grabó:

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate,nb_frames -of default=nw=1 clip.mp4
```

### Y el audio, ¿qué?

`atempo` solo acepta factores entre **0,5 y 100**. Si necesitas menos de 0,5 (más lento que la mitad),
lo encadenas:

```bash
# 0.4x de velocidad = 0.5 * 0.8
atempo=0.5,atempo=0.8

# 0.25x = 0.5 * 0.5
atempo=0.5,atempo=0.5
```

Verificado y funciona. Pero atención: **audio en cámara lenta suena mal casi siempre.** Voz a 0,5×
suena a monstruo. En la práctica, para cámara lenta se hace esto:

```bash
# Video lento, audio original silenciado, musica encima
ffmpeg -y -i clip.mp4 -filter_complex "[0:v]setpts=2.5*PTS[v]" \
  -map "[v]" -an -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p lento_mudo.mp4
```

Y le pones música o un sonido diseñado. Ver `76-diseño-sonoro.md`.

---

## Cámara lenta CON interpolación (`minterpolate`)

Cuando no grabaste a alta velocidad y necesitas cámara lenta de verdad, ffmpeg puede **inventar los
fotogramas intermedios** analizando el movimiento entre cuadros.

```bash
ffmpeg -y -i clip.mp4 -an -filter_complex \
"[0:v]setpts=2.5*PTS,minterpolate=fps=60:mi_mode=mci:mc_mode=aobmc:vsbmc=1[v]" \
  -map "[v]" -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p lento_interpolado.mp4
```

Qué significa cada cosa:
- `mi_mode=mci` — modo de compensación de movimiento. Es el bueno; el otro (`blend`) solo mezcla.
- `mc_mode=aobmc` — compensación adaptativa por bloques solapados. Reduce los bloques feos.
- `vsbmc=1` — refinamiento adicional. Mejora bordes, cuesta tiempo.
- `fps=60` — a cuántos fotogramas quieres llegar.

### El costo real (medido)

**Un clip de 4 segundos a 640×360 tardó 61 segundos en procesarse.** En 1080×1920 el costo se
multiplica por unas 9 veces. Un clip de 10 segundos en vertical puede tardar 20–25 minutos.

Traducción: `minterpolate` **no es para el video completo**. Es para 1 o 2 segundos puntuales.

### Cuándo produce basura

`minterpolate` funciona por adivinanza de movimiento. Falla feo cuando:

- Hay **oclusión**: algo pasa delante de otra cosa. Se ve un chicle que se estira.
- Hay **movimiento muy rápido**: el algoritmo no encuentra la correspondencia.
- Hay **cambios de luz**: un flash, una luz que parpadea. Fabrica manchas.
- Hay **agua, humo, fuego, pelo**: cosas sin bordes definidos. Se derrite.
- Hay **texto en pantalla**: las letras se deforman de forma muy visible.

Funciona bien con: movimiento suave, un sujeto, fondo estable, buena luz.

### La versión barata (`mi_mode=blend`)

```bash
ffmpeg -y -i clip.mp4 -an -vf "minterpolate=fps=60:mi_mode=blend" \
  -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p suave.mp4
```

Esto solo mezcla fotogramas vecinos. Es rapidísimo pero produce un "fantasma" doble. **Se ve mal
casi siempre.** Sirve solo si quieres el fantasma a propósito (sueño, recuerdo).

### La regla honesta

> Si puedes grabar a 120 fps, hazlo y usa `setpts`. `minterpolate` es el plan B, cuesta 60 veces más
> de render y produce artefactos que el cliente sí nota.

---

## Acelerado

Es mucho más benigno que el lento: tirar fotogramas nunca produce artefactos.

```bash
ffmpeg -y -i clip.mp4 -filter_complex \
"[0:v]setpts=0.25*PTS[v];[0:a]atempo=4.0[a]" \
  -map "[v]" -map "[a]" -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p rapido.mp4
```

### Los rangos que funcionan

| Factor | Uso |
|---|---|
| 1,2× – 1,5× | **Retoque de ritmo.** Casi invisible. Sirve para apretar una explicación lenta. |
| 2× – 4× | Acelerado narrativo: montaje de preparación, alguien trabajando. |
| 8× – 20× | Timelapse de una escena. |
| 60×+ | Hyperlapse. Mejor con `fps` explícito para no generar archivos absurdos. |

**El truco más útil de todo este módulo:** cuando un talking head se siente lento, ponlo a 1,15×.
Cuesta un comando, nadie lo nota, y el video se siente notablemente más ágil.

```bash
ffmpeg -y -i entrevista.mp4 -filter_complex \
"[0:v]setpts=PTS/1.15[v];[0:a]atempo=1.15[a]" \
  -map "[v]" -map "[a]" -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p agil.mp4
```

Hasta 1,2× la voz no suena rara. Por encima de 1,3× empieza a sonar a locutor apurado.

### Para acelerados grandes, tira fotogramas explícitamente

```bash
# Timelapse 30x - se queda 1 de cada 30 fotogramas
ffmpeg -y -i largo.mp4 -an -vf "setpts=PTS/30,fps=30" \
  -c:v libx264 -crf 20 -preset veryfast -pix_fmt yuv420p timelapse.mp4
```

El `fps=30` al final es importante: sin él, ffmpeg puede intentar producir un archivo con tasa de
fotogramas absurda.

---

## Speed ramp (la rampa de velocidad)

**Qué es:** la velocidad cambia dentro del mismo plano. Va normal, entra en cámara lenta sobre el
momento importante, y vuelve a normal. Es el recurso que define el look de los últimos años en
contenido deportivo, de producto y de creador.

Hay dos formas de hacerlo. Las dos verificadas.

### Método A — expresión continua (rápido, sin audio)

Una sola expresión de `setpts` con un `if` que cambia el factor a partir de un momento:

```bash
ffmpeg -y -i clip.mp4 -an \
  -vf "setpts='if(lt(T,2), PTS, 2/TB + (PTS-2/TB)*2.5)'" \
  -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p rampa.mp4
```

Cómo se lee:
- `lt(T,2)` — mientras el tiempo sea menor a 2 segundos, deja los tiempos como están.
- A partir de ahí: `2/TB` es el punto de quiebre expresado en unidades internas, y todo lo que viene
  después se estira 2,5 veces.
- `TB` es la unidad de tiempo del stream. **No la quites**: sin ella los números no significan nada.

Verificado: clip de 4 s → sale de 6,87 s. Esperado 2 + 2×2,5 = 7. Cuadra.

**Limitación:** en `-vf` no puedes tratar el audio en paralelo. Para audio, método B.

### Método B — por segmentos (más largo de escribir, controla el audio)

Partes el clip en trozos, le pones velocidad a cada uno, y los vuelves a pegar. Es más código pero es
lo que se hace en producción real porque puedes tratar el audio.

```bash
ffmpeg -y -i clip.mp4 -filter_complex \
"[0:v]trim=0:2,setpts=PTS-STARTPTS[v1];\
 [0:v]trim=2:4,setpts=2.5*(PTS-STARTPTS)[v2];\
 [v1][v2]concat=n=2:v=1:a=0[v];\
 [0:a]atrim=0:2,asetpts=PTS-STARTPTS[a1];\
 [0:a]atrim=2:4,asetpts=PTS-STARTPTS,atempo=0.5,atempo=0.8[a2];\
 [a1][a2]concat=n=2:v=0:a=1[a]" \
  -map "[v]" -map "[a]" -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p -c:a aac rampa_seg.mp4
```

Verificado: sale 6,975 s. Esperado 7. Cuadra.

Detalles que hay que respetar:
- **`setpts=PTS-STARTPTS` después de cada `trim`.** Sin eso, el trozo conserva su tiempo original y
  el `concat` deja huecos negros. Es el error número uno de este método.
- El `atempo` encadenado (`0.5,0.8`) porque 0,4 está por debajo del mínimo de 0,5.
- El orden: primero `trim`, después `setpts`. Al revés no funciona.

### La rampa que se ve bien vs. la que se ve mal

| Aspecto | Bien | Mal |
|---|---|---|
| Duración del tramo lento | 0,5 – 1,5 s | Más de 3 s (se hace eterno) |
| Factor de lentitud | 0,4× – 0,5× | Menos de 0,25× (se ve a saltos) |
| Dónde entra | Justo antes del momento clave | Al azar |
| Cuántas por video | 1 o 2 | En cada plano |
| Sonido | Con un "riser" o un impacto al entrar | Mudo |

**El error más común no es técnico: es poner rampas donde no hay nada que enfatizar.** La rampa existe
para decir "mira esto". Si el momento no lo merece, la rampa se ve a capricho.

### Rampa de tres tramos (normal → lento → normal)

La forma completa. Solo se agrega un tercer segmento:

```bash
ffmpeg -y -i clip.mp4 -an -filter_complex \
"[0:v]trim=0:2,setpts=PTS-STARTPTS[v1];\
 [0:v]trim=2:2.8,setpts=2.5*(PTS-STARTPTS)[v2];\
 [0:v]trim=2.8:6,setpts=PTS-STARTPTS[v3];\
 [v1][v2][v3]concat=n=3:v=1:a=0[v]" \
  -map "[v]" -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p rampa3.mp4
```

Esos 0,8 s de material real se convierten en 2 s de cámara lenta. Con material a 60 fps queda limpio;
con material a 30 fps se va a ver a saltos y ahí es donde toca decidir si vale un `minterpolate`.

---

## Errores comunes

- **Invertir el factor de `atempo`.** `setpts=2.0*PTS` va con `atempo=0.5`, no con `atempo=2.0`. Nada
  te avisa: el render sale bien y el audio queda desfasado.

- **Pedir cámara lenta a material de 30 fps.** Por debajo de 0,8× ya se ve a saltos. La cámara lenta
  se decide en el rodaje grabando a 60/120/240 fps.

- **Usar `minterpolate` en el video completo.** Medido: 61 segundos de proceso por 4 segundos de clip
  en resolución baja. En vertical HD es media hora. Úsalo en 1–2 segundos puntuales.

- **Usar `minterpolate` sobre agua, humo, pelo, texto o algo que pasa por delante de otra cosa.**
  Produce deformaciones muy visibles.

- **Olvidar `setpts=PTS-STARTPTS` después de un `trim`.** El `concat` te deja huecos negros y el
  video queda con saltos. Error número uno del método por segmentos.

- **Usar `atempo` con factor menor a 0,5.** El filtro lo rechaza. Se encadena: `atempo=0.5,atempo=0.8`.

- **Quitar el `TB` de la expresión de rampa continua.** Los números dejan de significar segundos y la
  rampa cae donde sea.

- **Dejar el audio original en cámara lenta.** Voz a 0,5× suena a monstruo. Se silencia y se pone
  música o sonido diseñado.

- **Rampa sin sonido.** El cambio de velocidad sin apoyo sonoro se lee como un error de reproducción.

- **Rampas en cada plano.** Si todo es énfasis, no hay énfasis. Una o dos por video.

- **No verificar la duración final.** Es la comprobación que caza el 100% de los errores de factor.

---

## Checklist

- [ ] Comprobé a cuántos fps se grabó el material (`ffprobe`), no lo supuse.
- [ ] El factor de cámara lenta deja al menos 24 fps efectivos.
- [ ] El factor de `atempo` es el inverso del de `setpts`, y lo verifiqué escuchando.
- [ ] Si `atempo` es menor a 0,5, lo encadené en dos pasos.
- [ ] Si uso `minterpolate`, es sobre 1–2 segundos, no sobre el video completo.
- [ ] Si uso `minterpolate`, el plano no tiene agua, humo, pelo suelto, texto ni oclusiones.
- [ ] En el método por segmentos, cada `trim` va seguido de `setpts=PTS-STARTPTS`.
- [ ] La rampa dura entre 0,5 y 1,5 s en su tramo lento.
- [ ] Hay como máximo 1 o 2 rampas en toda la pieza.
- [ ] Cada rampa cae sobre un momento que de verdad merece énfasis.
- [ ] Cada rampa tiene apoyo sonoro (riser, impacto, o el audio original acompañando).
- [ ] Medí la duración final y coincide con la cuenta esperada.
- [ ] Miré el resultado buscando saltos, fantasmas o deformaciones (`98`).

# 53 — Whip, flash y golpe: las tres que dan sensación de comercial de TV

> Hay tres transiciones que separan un video que se ve "hecho en casa" de uno que se ve "de televisión".
> No son las 58 de `xfade`. Son tres recursos de tiempo y energía que se construyen a mano.

Las tres tienen algo en común: **son cortísimas**. Entre 3 y 9 fotogramas. Si duran más, se convierten
en efecto y pierden todo. La sensación de comercial no viene de que se vean bonitas: viene de que
pasan tan rápido que sientes el golpe sin alcanzar a analizarlo.

---

## 1. El FLASH (el más fácil y el más rentable)

**Qué es:** un destello blanco (o del color de marca) de 2 a 5 fotogramas en el punto de corte.

**Qué comunica:** energía, impacto, "atención acá". Es el equivalente visual de un golpe de caja.

**Dónde se usa de verdad:** publicidad de producto, antes/después, deportes, gimnasios, clínicas
estéticas, cualquier cosa que quiera sentirse rápida y positiva.

### Cómo se hace (método verificado)

El truco es no usar `xfade` sino **fundir cada clip por separado** a blanco y pegarlos duro. Así
controlas exactamente cuántos fotogramas dura el blanco.

```bash
# Clip que sale: se va a blanco en los ultimos 0.1 s
ffmpeg -y -i plano01.mp4 -vf "fade=t=out:st=1.9:d=0.1:color=white" \
  -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p flash_a.mp4

# Clip que entra: viene desde blanco en los primeros 0.1 s
ffmpeg -y -i plano02.mp4 -vf "fade=t=in:st=0:d=0.1:color=white" \
  -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p flash_b.mp4

# Se pegan duro
printf "file 'flash_a.mp4'\nfile 'flash_b.mp4'\n" > lista.txt
ffmpeg -y -f concat -safe 0 -i lista.txt -c copy flash.mp4
```

Ojo con `st=1.9`: ese número es **la duración del clip menos la duración del fundido**. Si tu clip
dura 2,0 s y el fundido dura 0,1 s, `st = 2.0 − 0.1 = 1.9`. Es la misma lógica del `offset` de
`xfade` (ver `51`). Si te equivocas, el fundido queda a mitad de plano o no se ve.

Verificado: duración final 4,000 s con dos clips de 2 s. El flash no roba tiempo — es la diferencia
con `xfade`, que sí acorta.

### Las dosis que funcionan

| Fotogramas de blanco | Sensación |
|---|---|
| 2 (0,07 s a 30 fps) | Casi subliminal. Solo se siente. **El mejor para reels.** |
| 3–4 (0,10–0,13 s) | Se ve pero no molesta. El estándar publicitario. |
| 6+ (0,20 s) | Ya es un fundido a blanco, no un flash. Se siente lento. |

### Variantes

- **Flash de color de marca** en vez de blanco: cambia `color=white` por `color=0xE10600`. Se ve
  intencional y refuerza la marca. Es el hermano pobre —y muy eficaz— de `52`.
- **Flash negro** (`color=black`): se lee como parpadeo o corte de energía. Sirve para tensión, no
  para positividad.
- **Flash sin sonido:** el flash sin un golpe de audio se siente hueco. Ver más abajo.

### El flash SIEMPRE lleva sonido

Un flash mudo se ve como un error de compresión. El flash necesita un impacto sonoro en el mismo
fotograma: un golpe grave, un "riser" que termina, un woosh que cae. Ver `76-diseño-sonoro.md`.

> Si solo pudieras hacer una cosa de este módulo, sería esta: **poner un golpe de audio en cada
> flash.** Sube la sensación de producción más que cualquier filtro de imagen.

---

## 2. El WHIP (el barrido de cámara)

**Qué es:** la cámara gira violentamente, la imagen se convierte en una mancha horizontal, y del otro
lado aparece otro plano. Imita un latigazo de cámara real.

**Qué comunica:** "nos movimos de sitio, rápido". Es la transición de los videos de viaje, de las
recetas rápidas y de casi todo el contenido de creador de los últimos años.

### La forma buena: filmarlo

El whip **de verdad** se graba. Al final del plano A, giras el celular rápido a la derecha; al empezar
el plano B, arrancas ya girando y frenas. En el montaje juntas los dos borrones y el corte desaparece.

Esto queda infinitamente mejor que cualquier simulación, y cuesta cero. Es una petición de rodaje —
ver `170-briefing-de-rodaje-desde-la-edicion.md`. Si vas a hacer muchos whips, **pídelos filmados.**

### La forma aceptable: simularlo con desenfoque direccional

Cuando no lo filmaron, se simula con un desenfoque **solo horizontal**. La clave es que sea horizontal:
un desenfoque en todas las direcciones se ve a "filtro", no a movimiento.

El filtro correcto es `gblur` con `sigmaV=0` (sigma vertical en cero = solo borra en horizontal):

```bash
# Ultimos 0.15 s del clip A: se emborrona horizontalmente
ffmpeg -y -i plano01.mp4 \
  -vf "gblur=sigma=40:sigmaV=0:steps=3:enable='gt(t,1.85)'" \
  -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p whip_a.mp4

# Primeros 0.15 s del clip B: entra emborronado y se resuelve
ffmpeg -y -i plano02.mp4 \
  -vf "gblur=sigma=40:sigmaV=0:steps=3:enable='lt(t,0.15)'" \
  -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p whip_b.mp4

printf "file 'whip_a.mp4'\nfile 'whip_b.mp4'\n" > lista.txt
ffmpeg -y -f concat -safe 0 -i lista.txt -c copy whip.mp4
```

Notas de sintaxis que cuestan tiempo si no las sabes:

- `enable='gt(t,1.85)'` usa **`t` minúscula**. Si escribes `T` mayúscula ffmpeg te responde
  `Undefined constant or missing '(' in 'T,0.8)'`. La `T` mayúscula existe en otros contextos
  (`geq`, `setpts`), pero en `enable` es `t`.
- `steps=3` mejora la calidad del desenfoque a costa de velocidad. Con 1 se ve a bloques.
- `sigma=40` es agresivo a propósito. Un whip tímido no lee.

### Para que se vea de verdad: añade movimiento

El desenfoque solo no basta. El whip real también **desplaza** la imagen. Súmale un `crop` que se corra:

```bash
ffmpeg -y -i plano01.mp4 -vf \
"scale=iw*1.15:ih*1.15,\
 crop=w=iw/1.15:h=ih/1.15:x='(iw-ow)/2 + if(gt(t,1.85), (t-1.85)/0.15*(iw-ow)/2, 0)':y='(ih-oh)/2',\
 gblur=sigma=40:sigmaV=0:steps=3:enable='gt(t,1.85)'" \
  -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p whip_a.mp4
```

Qué hace: agranda un 15% para tener margen, y en los últimos 0,15 s corre el recorte hacia un lado
mientras emborrona. Ese pequeño desplazamiento es lo que convierte el borrón en "movimiento".

### Duración del whip

| Fotogramas por lado | Resultado |
|---|---|
| 3–5 (0,10–0,17 s) | Correcto. Se siente el latigazo. |
| 8+ | Ya se ve el borrón y se lee como filtro. Mal. |

Total del whip (los dos lados juntos): **entre 6 y 10 fotogramas**. Nunca más.

### El whip también lleva sonido

Un "woosh". Sin él, es un borrón inexplicable. Con él, es un movimiento de cámara. El sonido hace
más por el whip que el filtro.

---

## 3. El GOLPE (el zoom de impacto)

**Qué es:** un salto brusco de escala en el punto de corte — la imagen "salta" un 10–20% más cerca
en un solo fotograma, o entra escalada y se asienta en 3 fotogramas.

**Qué comunica:** énfasis. Es el signo de admiración del montaje. Se usa sobre la palabra clave, sobre
el precio, sobre la cara de reacción.

### Variante A — el salto seco (punch-in de golpe)

Es el más simple: cortas el mismo plano consigo mismo, pero el segundo trozo está recortado más cerca.
No hay transición: hay dos planos distintos. Ver `22-punch-in-y-reencuadre.md`.

```bash
# Trozo 1: cuadro normal
ffmpeg -y -i toma.mp4 -t 2 -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p g1.mp4

# Trozo 2: mismo plano, 18% mas cerca
ffmpeg -y -i toma.mp4 -ss 2 \
  -vf "scale=iw*1.18:ih*1.18,crop=w=iw/1.18:h=ih/1.18:x=(iw-ow)/2:y=(ih-oh)/2" \
  -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p g2.mp4

printf "file 'g1.mp4'\nfile 'g2.mp4'\n" > lista.txt
ffmpeg -y -f concat -safe 0 -i lista.txt -c copy golpe.mp4
```

**El 18% importa.** Menos del 12% parece un error de encuadre; más del 30% parece otro plano y rompe
la continuidad. La zona segura es **12%–25%**.

### Variante B — el golpe elástico (entra grande y se asienta)

El plano nuevo entra un 20% más grande y en 3–4 fotogramas baja a su tamaño normal, con un pequeño
sobre-impulso. Es el "pop" de la tipografía cinética aplicado a la imagen (ver `42` y `84`).

```bash
ffmpeg -y -i plano02.mp4 -vf \
"scale=iw*1.25:ih*1.25,\
 zoompan=z='if(lt(in_time,0.13), 1.25 - (in_time/0.13)*0.25, 1)':d=1:\
 x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30" \
  -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p golpe_elastico.mp4
```

`zoompan` es un filtro difícil y lento; si el resultado te tiembla, revisa `84-keyframes-y-curvas.md`.
En la práctica, para vertical rápido, la variante A (salto seco) se ve mejor y cuesta la décima parte.

### El golpe también lleva sonido

Un impacto grave, corto, con cuerpo. Sin él es un salto de encuadre raro.

---

## Las tres juntas: la receta de "comercial de TV"

Un spot que se sienta de televisión no usa las tres al azar. Usa esta lógica:

| Momento del spot | Recurso |
|---|---|
| Entre bloques narrativos (problema → solución) | **Flash** |
| Entre lugares o entre productos | **Whip** |
| Sobre el dato, el precio, la reacción | **Golpe** |
| Todo lo demás (el 85%) | **Corte duro** |

Y la regla que lo sostiene todo: **cada uno de los tres cae en un golpe de la música.** Si tu whip cae
en un silencio, no se siente comercial: se siente accidente. Ver `24-ritmo-y-musica.md`.

---

## Por qué esto se ve caro y `zoomin` de xfade se ve barato

Las tres cosas de este módulo se construyen a mano, duran poquísimo y van acompañadas de sonido. La
transición `zoomin` de `xfade` es un preset que dura medio segundo y no trae sonido.

La diferencia no es el filtro. Es:

1. **Duración.** 3 fotogramas contra 15.
2. **Sonido.** Con impacto contra mudo.
3. **Colocación.** En el golpe musical contra donde cayó.
4. **Frecuencia.** Dos veces en el video contra en cada corte.

Puedes usar el mismo filtro y quedar en lados opuestos de esa línea.

---

## Errores comunes

- **Hacer el flash largo.** 6 fotogramas ya no es flash: es fundido a blanco. Se siente lento y
  cursi. 2 a 4 fotogramas.

- **Flash, whip o golpe sin sonido.** Es el error más caro del módulo. El recurso visual sin el golpe
  de audio se lee como falla técnica, no como decisión.

- **`enable='gt(T,...)'` con T mayúscula.** ffmpeg responde `Undefined constant or missing '('`.
  En `enable` la variable de tiempo es `t` minúscula.

- **Calcular mal el `st` del `fade`.** `st` = duración del clip − duración del fundido. Si pones
  `st=2` en un clip de 2 s, el fundido no se ve porque empieza cuando el clip terminó.

- **Whip con desenfoque en todas las direcciones.** Se ve a "filtro de app". El whip es horizontal:
  `gblur=sigma=40:sigmaV=0`.

- **Whip sin desplazamiento.** Solo emborronar no es moverse. Súmale el `crop` que se corre.

- **Golpe de menos del 12%.** Se lee como error de encuadre, no como énfasis.

- **Golpe de más del 30%.** Rompe la continuidad: parece otro plano y otro momento.

- **Simular whips cuando se podían filmar.** El whip filmado es gratis y siempre queda mejor. Pídelo
  en el rodaje.

- **Usar los tres en cada corte.** Si todo es énfasis, nada es énfasis. Máximo 2 a 4 en un spot de 30 s.

- **Ponerlos donde no hay golpe musical.** Se sienten desconectados. Móntalos sobre la pista, no sobre
  la imagen.

---

## Checklist

- [ ] Cada flash dura entre 2 y 4 fotogramas, no más.
- [ ] Cada whip completo (los dos lados) dura entre 6 y 10 fotogramas.
- [ ] Cada golpe está entre el 12% y el 25% de aumento de escala.
- [ ] **Los tres llevan sonido**: golpe grave el flash, woosh el whip, impacto el golpe.
- [ ] Cada uno cae exactamente sobre un acento de la música.
- [ ] El desenfoque del whip es horizontal (`sigmaV=0`), no isotrópico.
- [ ] El whip incluye desplazamiento además del desenfoque.
- [ ] Los `enable` usan `t` minúscula.
- [ ] Los `st` de los `fade` están calculados como duración − fundido, y los verifiqué.
- [ ] En una pieza de 30 s no hay más de 4 de estos recursos sumados.
- [ ] El resto de los cortes son duros.
- [ ] Verifiqué el render: los recursos caen en el fotograma exacto, no corridos (`98`).

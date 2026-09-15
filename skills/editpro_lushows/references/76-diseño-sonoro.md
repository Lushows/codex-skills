# 76 — Diseño sonoro

El diseño sonoro es todo el sonido que no es voz ni música: el whoosh de una transición, el golpe cuando
aparece el logo, el zumbido que sube antes de una revelación, el "tick" del texto que entra.

Bien hecho, nadie lo nota y todo el video se siente más caro. Mal hecho, es lo primero que delata a un
editor principiante: whooshes en cada corte, impactos donde no pasa nada, y un riser de cinco segundos
para revelar un precio.

**La regla que gobierna este módulo entero:** un efecto de sonido no acompaña la imagen, **le agrega
información**. Si el whoosh no te dice nada que la imagen no dijera ya, sobra.

---

## Los cuatro elementos básicos

| Elemento | Qué es | Cuándo va |
|---|---|---|
| **Whoosh** | Un barrido de aire, corto | En un movimiento: cámara que gira, objeto que cruza, transición con desplazamiento |
| **Impacto** | Un golpe grave y corto | Cuando algo aparece o se detiene: logo, texto grande, corte a negro |
| **Riser** | Un sonido que sube en tono o intensidad | Antes de una revelación. Crea expectativa |
| **Subrayado** | Un sonido corto y agudo | Marca un dato, un ítem de lista, un texto que entra |

Y una quinta categoría que no es efecto pero es diseño sonoro: **el silencio**. Cortar todo el sonido
medio segundo antes de un impacto lo hace tres veces más fuerte, sin subirle un decibel. Es el recurso
más barato y más subutilizado que existe.

---

## Construirlos desde cero con ffmpeg

Se puede. No siempre conviene (ver la última sección), pero saber hacerlo te da control total y no
depende de ninguna biblioteca.

### Whoosh

Base: ruido blanco filtrado, con un barrido de frecuencia y una envolvente de volumen.

```bash
# whoosh de 0,8 s: ruido rosa que sube de grave a agudo y se apaga
ffmpeg -f lavfi -i "anoisesrc=d=0.8:c=pink:a=0.5:r=48000" \
  -af "highpass=f=300,lowpass=f=6000,afade=t=in:st=0:d=0.25:curve=exp,afade=t=out:st=0.4:d=0.4:curve=exp,volume=1.5" \
  -c:a pcm_s16le whoosh.wav
```

Cómo se lee:
- `anoisesrc` genera ruido. `c=pink` (rosa) suena más natural que blanco; `c=white` es más filoso;
  `c=brown` es más grave y "de viento".
- `highpass` + `lowpass` le dan el carácter. Un whoosh de aire vive entre 300 Hz y 6 kHz.
- Los dos `afade` con `curve=exp` hacen la forma "entra rápido, sale despacio" que es lo que da la
  sensación de paso.

Para que **barra** de grave a agudo (más convincente), se anima el filtro con `asendcmd`:

```bash
ffmpeg -f lavfi -i "anoisesrc=d=0.8:c=pink:a=0.5:r=48000" \
  -af "asendcmd=0.0 lowpass frequency 800,asendcmd=0.4 lowpass frequency 9000,asendcmd=0.8 lowpass frequency 2000,lowpass=f=800,highpass=f=250,afade=t=in:st=0:d=0.2,afade=t=out:st=0.45:d=0.35" \
  -c:a pcm_s16le whoosh_barrido.wav
```

Alternativa más simple y a menudo mejor: **grabar el whoosh con la boca o con la mano**. Un soplido
suave frente al micrófono, procesado con los mismos filtros, suena mejor que cualquier ruido sintético
porque tiene irregularidad. Ver `77`.

### Impacto

Un impacto es un golpe de grave que decae rápido. Se construye con un tono senoidal que baja de
frecuencia y de volumen a la vez.

```bash
# impacto grave de 1,2 s
ffmpeg -f lavfi -i "sine=frequency=90:duration=1.2:sample_rate=48000" \
  -af "asendcmd=0.0 volume volume 1.0,afade=t=out:st=0.05:d=1.1:curve=exp,volume=2" \
  -c:a pcm_s16le impacto_tono.wav
```

Eso es la parte grave. Para que tenga "cuerpo" hay que sumarle un golpe de ruido corto arriba:

```bash
# capa de ataque: ruido muy corto
ffmpeg -f lavfi -i "anoisesrc=d=0.12:c=brown:a=0.7:r=48000" \
  -af "lowpass=f=2500,afade=t=out:st=0:d=0.12:curve=exp" -c:a pcm_s16le impacto_ataque.wav

# mezclar las dos capas
ffmpeg -i impacto_tono.wav -i impacto_ataque.wav \
  -filter_complex "[0][1]amix=inputs=2:duration=longest:dropout_transition=0,volume=2,alimiter=limit=0.9" \
  -c:a pcm_s16le impacto.wav
```

**Un impacto son siempre dos capas: el ataque (agudo, muy corto) y la cola (grave, que decae).** Si solo
pones la cola, suena a bombo apagado. Si solo pones el ataque, suena a palmada. Juntos suenan a impacto
de cine.

Para hacerlo más "cinemático", agrégale un barrido de frecuencia descendente:

```bash
ffmpeg -f lavfi -i "sine=frequency=140:duration=1.5:sample_rate=48000" \
  -af "asendcmd=0.0 highpass frequency 20,afade=t=out:st=0.02:d=1.45:curve=exp,aecho=0.8:0.7:60:0.3,volume=2" \
  -c:a pcm_s16le impacto_cine.wav
```

El `aecho` (eco corto de 60 ms al 30%) le da tamaño sin sonar a sala de conciertos.

### Riser

Un sonido que sube durante 2–4 segundos y desemboca en el impacto. Es lo que crea expectativa.

```bash
# riser de 3 s: ruido que sube de frecuencia y de volumen
ffmpeg -f lavfi -i "anoisesrc=d=3:c=white:a=0.4:r=48000" \
  -af "asendcmd=0.0 highpass frequency 200,asendcmd=1.0 highpass frequency 900,asendcmd=2.0 highpass frequency 2500,asendcmd=2.9 highpass frequency 6000,highpass=f=200,afade=t=in:st=0:d=2.8:curve=exp,volume=1.8" \
  -c:a pcm_s16le riser.wav
```

Versión tonal (más musical, menos "de tráiler"):

```bash
# tono que sube de 200 a 1200 Hz en 3 s, con phaser para darle textura
ffmpeg -f lavfi -i "sine=frequency=200:duration=3:sample_rate=48000" \
  -af "asendcmd=0.0 volume volume 0.2,aphaser=in_gain=0.6:out_gain=0.8:delay=3:decay=0.5:speed=1.5,afade=t=in:st=0:d=2.9:curve=exp" \
  -c:a pcm_s16le riser_tonal.wav
```

`aphaser` mueve la fase y crea ese barrido "líquido" que hace que un tono simple suene procesado y no
plano. Parámetros: `speed` es qué tan rápido barre, `decay` cuánta profundidad.

**La regla del riser:** el riser **termina exactamente donde empieza el impacto.** Ni un frame antes ni
uno después. Si el riser sigue sonando después del golpe, el efecto se deshace.

### Subrayado

Un tick corto y agudo para marcar texto que entra o un ítem de lista.

```bash
# tick de 90 ms
ffmpeg -f lavfi -i "sine=frequency=1800:duration=0.09:sample_rate=48000" \
  -af "afade=t=out:st=0:d=0.09:curve=exp,volume=0.6" -c:a pcm_s16le tick.wav

# versión con más cuerpo: dos tonos
ffmpeg -f lavfi -i "sine=frequency=1400:duration=0.12" -f lavfi -i "sine=frequency=2100:duration=0.06" \
  -filter_complex "[0]afade=t=out:st=0:d=0.12:curve=exp[a];[1]afade=t=out:st=0:d=0.06:curve=exp,volume=0.5[b];[a][b]amix=inputs=2:duration=longest:dropout_transition=0,volume=0.7" \
  -c:a pcm_s16le tick2.wav
```

Para una lista de 4 ítems, sube el tono en cada uno. Suena a progresión y el cerebro lo registra como
"esto avanza":

```bash
for f in 1200 1400 1600 1900; do
  ffmpeg -y -f lavfi -i "sine=frequency=$f:duration=0.1" \
    -af "afade=t=out:st=0:d=0.1:curve=exp,volume=0.6" -c:a pcm_s16le tick_$f.wav
done
```

### El silencio como efecto

```bash
# generar 0,4 s de silencio para insertar antes de un impacto
ffmpeg -f lavfi -i "anullsrc=r=48000:cl=stereo" -t 0.4 -c:a pcm_s16le silencio.wav
```

Y en la mezcla: baja todo (música incluida) 300–500 ms antes del golpe. El contraste hace el trabajo.

```bash
# bajar la música a cero entre el segundo 11,6 y el 12,0
ffmpeg -i musica.wav -af "volume='if(between(t,11.6,12.0),0,1)':eval=frame" musica_con_hueco.wav
```

---

## Colocarlos en el video

Insertar un efecto en un momento exacto de la mezcla:

```bash
# el impacto entra en el segundo 12,0
ffmpeg -i mezcla.wav -i impacto.wav \
  -filter_complex "[1]adelay=12000|12000,volume=-6dB[fx];[0][fx]amix=inputs=2:duration=first:dropout_transition=0[out]" \
  -map "[out]" mezcla_con_fx.wav
```

Varios efectos a la vez:

```bash
ffmpeg -i mezcla.wav -i whoosh.wav -i impacto.wav -i tick.wav \
  -filter_complex "\
[1]adelay=3400|3400,volume=-10dB[w]; \
[2]adelay=12000|12000,volume=-6dB[i]; \
[3]adelay=18200|18200,volume=-14dB[t]; \
[0][w][i][t]amix=inputs=4:duration=first:dropout_transition=0,alimiter=limit=0.9[out]" \
-map "[out]" mezcla_final.wav
```

`adelay` va en **milisegundos**, un valor por canal separado por `|`.

El `alimiter` al final es importante: cuando sumas cuatro pistas, los picos se suman y puedes pasar de 0
dB sin darte cuenta.

---

## Los niveles: dónde va cada efecto

Esta tabla salva videos. Los efectos casi siempre están más fuerte de lo que deberían.

| Efecto | Nivel respecto a la voz |
|---|---|
| Whoosh de transición | **−12 a −16 dB** |
| Impacto de logo / cierre | **−4 a −8 dB** (es el que puede sonar fuerte) |
| Riser | Arranca en −24 dB, termina en −8 dB |
| Subrayado / tick | **−14 a −18 dB** |
| Ambiente de fondo | −30 a −40 dB |

**Si el efecto te distrae de la voz, está muy fuerte.** Y si lo notas conscientemente cada vez que
suena, también.

---

## Cuándo NO usarlos

Aquí es donde se separa la gente con criterio.

**No pongas whoosh en cada corte.** Un whoosh en un corte duro no tiene sentido: no hay movimiento que
acompañar. El whoosh va cuando algo **se desplaza** en pantalla. Si tu video tiene 30 cortes y 30
whooshes, quítalos todos y vuelve a poner tres.

**No pongas impacto donde no pasa nada.** Un impacto anuncia. Si anuncia cada tres segundos, deja de
anunciar y se vuelve percusión de fondo mediocre.

**No uses riser para revelar algo pequeño.** Cuatro segundos de tensión creciente para mostrar un precio
de $10.000 es una promesa que el video no cumple. El público se siente estafado, aunque no sepa
nombrarlo. El riser es para el momento más grande del video, y hay uno solo.

**No apiles.** Whoosh + impacto + riser + tick en el mismo segundo no es "más impactante", es ruido.
Elige uno.

**Regla numérica que funciona:** en un reel de 30 segundos, **entre 3 y 6 efectos en total**. Si tienes
15, tienes un problema.

---

## Cuándo mejor conseguirlos

Ser honesto: **construir efectos con ffmpeg es útil para entender cómo funcionan, y para casos simples
(ticks, impactos básicos, whooshes de relleno). Para trabajo serio, casi siempre conviene conseguirlos.**

Razones concretas:

1. **Los sintéticos suenan sintéticos.** Un whoosh de `anoisesrc` es matemáticamente perfecto y por eso
   suena plano. Un whoosh grabado de verdad —una tela agitada, un soplido, un objeto pasando frente al
   micro— tiene irregularidades que el oído lee como "real".
2. **El tiempo.** Un impacto decente de biblioteca lo encuentras en 90 segundos. Construir uno bueno con
   ffmpeg te toma media hora de prueba y error.
3. **Las bibliotecas gratuitas son buenas.** No es 2010.

**Dónde conseguirlos (gratis y con licencia usable):**

| Fuente | Qué tiene | Ojo con |
|---|---|---|
| **Pixabay** | Efectos y música, uso comercial, sin atribución | Verificar la licencia de cada archivo |
| **Mixkit** | Efectos de calidad, gratis, uso comercial | Licencia propia, léela |
| **Freesound** | Enorme, muy variado | **Licencias mixtas**: cada archivo tiene la suya (CC0, CC-BY, etc.) |
| **YouTube Audio Library** | Efectos gratis desde YouTube Studio | No cubre TikTok ni Instagram |
| **Zapsplat / Soundsnap** | Bibliotecas grandes | Freemium; atribución en el tier gratis |

Ver `78` para el detalle de las licencias. Y **guarda un archivo de texto con la fuente y la licencia de
cada efecto que uses.** Cuesta 10 segundos y te salva de un dolor de cabeza dentro de un año.

**El orden de preferencia que uso:**

1. **Sonido del propio material.** Si en la toma hay un sonido real que sirve, ese gana siempre (ver `77`).
2. **Biblioteca gratuita con buena licencia.** El 80% de los casos.
3. **Grabado por mí con el celular.** Un soplido, un golpe en la mesa, una tela. Sorprendentemente bueno.
4. **Construido con ffmpeg.** Cuando necesito algo específico que no encuentro, o un tick simple.

---

## Un caso completo: revelación de producto

Video de 20 s. En el segundo 14 se revela el producto. Quiero: riser de 2,5 s, silencio de 0,3 s,
impacto en el 14,0.

```bash
# 1) riser que termina en 13,7
ffmpeg -f lavfi -i "anoisesrc=d=2.5:c=white:a=0.4:r=48000" \
  -af "asendcmd=0.0 highpass frequency 200,asendcmd=1.2 highpass frequency 1200,asendcmd=2.4 highpass frequency 5000,highpass=f=200,afade=t=in:st=0:d=2.3:curve=exp,afade=t=out:st=2.35:d=0.15" \
  -c:a pcm_s16le riser.wav

# 2) impacto de dos capas
ffmpeg -f lavfi -i "sine=frequency=100:duration=1.4" -af "afade=t=out:st=0.03:d=1.37:curve=exp" -c:a pcm_s16le imp_low.wav
ffmpeg -f lavfi -i "anoisesrc=d=0.1:c=brown:a=0.6" -af "lowpass=f=3000,afade=t=out:st=0:d=0.1:curve=exp" -c:a pcm_s16le imp_hi.wav
ffmpeg -i imp_low.wav -i imp_hi.wav -filter_complex "[0][1]amix=inputs=2:duration=longest:dropout_transition=0,volume=2,alimiter=limit=0.9" -c:a pcm_s16le impacto.wav

# 3) hueco de silencio en la música entre 13,7 y 14,0
ffmpeg -i musica.wav -af "volume='if(between(t,13.7,14.0),0,1)':eval=frame" musica_hueco.wav

# 4) mezclar todo
ffmpeg -i voz.wav -i musica_hueco.wav -i riser.wav -i impacto.wav -filter_complex "\
[1]volume=-14dB[m]; \
[m][0]sidechaincompress=threshold=0.025:ratio=8:attack=15:release=400[duck]; \
[2]adelay=11200|11200,volume=-10dB[r]; \
[3]adelay=14000|14000,volume=-6dB[i]; \
[0][duck][r][i]amix=inputs=4:duration=first:dropout_transition=0,alimiter=limit=0.9[out]" \
-map "[out]" mezcla.wav

# 5) normalizar
ffmpeg -i mezcla.wav -af "loudnorm=I=-14:TP=-1.5:LRA=11" audio_final.wav
```

Fíjate en el detalle: el riser arranca en 11,2 y dura 2,5 s → termina en 13,7. La música se apaga en
13,7. El impacto entra en 14,0. Hay 0,3 s de silencio total antes del golpe. **Ese silencio es lo que
hace el efecto**, más que el impacto mismo.

---

## Errores comunes

- **Whoosh en cada corte.** El whoosh acompaña movimiento, no cortes. Tres, no treinta.
- **Impacto donde no pasa nada.** Si anuncia todo el tiempo, no anuncia nada.
- **Riser largo para revelar algo pequeño.** Prometes más de lo que entregas.
- **Apilar efectos en el mismo segundo.** Whoosh + impacto + tick a la vez es ruido, no potencia.
- **Efectos muy fuertes.** Si te distraen de la voz, sobran 8 dB. Ver la tabla de niveles.
- **Impacto de una sola capa.** Sin ataque agudo suena a bombo apagado; sin cola grave suena a palmada.
- **Riser que sigue sonando después del golpe.** Termina exactamente donde empieza el impacto.
- **Olvidar el `alimiter` al sumar pistas.** Los picos se suman y saturas sin verlo venir.
- **No usar el silencio.** Es el recurso más potente y no cuesta nada.
- **`adelay` con un solo valor en estéreo.** Va uno por canal: `adelay=12000|12000`.
- **Construir todo con ffmpeg por orgullo.** Media hora peleando con `anoisesrc` para hacer un whoosh
  que en Mixkit está listo y suena mejor. Construye cuando aporta, consigue cuando no.
- **No anotar la licencia de cada efecto.** Dentro de un año no vas a acordarte de dónde salió.

---

## Checklist

- [ ] Cada efecto **agrega información** que la imagen no daba sola.
- [ ] En una pieza de 30 s hay entre **3 y 6 efectos**, no quince.
- [ ] Los whooshes están donde hay **movimiento**, no en cortes duros.
- [ ] Hay **un solo** momento de riser + impacto, y es el más importante del video.
- [ ] El **riser termina exactamente** donde empieza el impacto.
- [ ] Hay **silencio** (0,3–0,5 s) antes del golpe grande.
- [ ] Los impactos tienen **dos capas**: ataque agudo + cola grave.
- [ ] Los niveles siguen la tabla: whoosh −12/−16 dB, impacto −4/−8 dB, tick −14/−18 dB.
- [ ] No hay dos efectos apilados en el mismo segundo.
- [ ] Usé `adelay` en **milisegundos y por canal**.
- [ ] La mezcla lleva **`alimiter`** después del `amix`.
- [ ] Normalicé la mezcla completa a **−14 LUFS** al final (ver `73`).
- [ ] Antes de construir con ffmpeg, **revisé si el material ya tenía el sonido** (ver `77`) o si estaba
      en una biblioteca gratuita.
- [ ] Anoté **fuente y licencia** de cada efecto que bajé (ver `78`).
- [ ] Escuché la mezcla **sin mirar la pantalla**: los efectos no distraen de la voz.

# 295 — Frecuencias que pelean

Este es el módulo que resuelve la queja más frecuente del mundo: **"la música tapa la voz"**.

Y la respuesta que casi nadie da: si bajaste la música 20 dB y la voz todavía no se entiende, tu
problema **no es de volumen**. Es que la música y la voz están peleando por las mismas frecuencias. Vas
a poder bajar la música otros 10 dB y seguir sin entender bien — porque el enmascaramiento no se
resuelve con el fader.

---

## Qué es el enmascaramiento, en cristiano

El oído no analiza cada frecuencia por separado. Trabaja por zonas (bandas críticas). Cuando en una
zona hay un sonido fuerte, **los sonidos débiles de esa misma zona simplemente no existen** para tu
cerebro. No se oyen bajitos: no se oyen.

Por eso una música 20 dB más baja puede seguir tapando la voz: si toda la energía de esa música está
concentrada exactamente en la zona donde vive la inteligibilidad de la voz, el enmascaramiento gana.

La zona clave:

| Rango | Qué vive ahí | Quién más pelea por él |
|---|---|---|
| 80–150 Hz | cuerpo de la voz masculina | bombo, bajo, graves de la música |
| 150–400 Hz | cuerpo de la voz, calidez | guitarras, teclados, "barro" general |
| 400–1000 Hz | nasalidad, cartón | casi todos los instrumentos |
| **2.000–4.000 Hz** | **inteligibilidad: consonantes** | **caja, guitarras, sintes, platillos** |
| 5–8 kHz | sibilancia, aire | hi-hats, platillos |
| 8–16 kHz | brillo | platillos, aire de la producción |

**La franja de 2 a 4 kHz es donde se decide si tu video se entiende.** Ahí viven las consonantes: la t,
la p, la k, la s, la ch. Sin consonantes no hay palabras — solo un murmullo con entonación. Y la voz
humana tiene relativamente poca energía ahí, así que pierde la pelea fácil contra una música con
guitarras o caja.

---

## Diagnóstico: ¿es de nivel o de frecuencia?

Antes de tocar nada, haz esta prueba de 30 segundos. Corta la música exactamente en esa franja y
escucha. Si la voz aparece de golpe, el problema era espectral.

```bash
# corte quirúrgico y brutal de 12 dB en 3 kHz en la música — solo para diagnosticar
ffmpeg -i 02_MUSICA.wav -af "equalizer=f=3000:t=q:w=1.5:g=-12" test_hueco.wav

# mezclar con la voz al mismo nivel de siempre y escuchar
ffmpeg -i 01_VOZ.wav -i test_hueco.wav \
  -filter_complex "[1:a]volume=-20dB[m];[0:a][m]amix=inputs=2:normalize=0[o]" \
  -map "[o]" test_diagnostico.wav
```

Si con ese corte la voz sale clarísima: es enmascaramiento, y el resto del módulo es tu solución.
Si sigue igual de turbia: el problema está en la voz (revisa el EQ de `72`) o en el nivel.

También puedes verlo. El espectrograma no miente:

```bash
# imagen del espectro: eje X tiempo, eje Y frecuencia, color = energía
ffmpeg -i 02_MUSICA.wav -lavfi showspectrumpic=s=1280x480:legend=1 espectro_musica.png
ffmpeg -i 01_VOZ.wav   -lavfi showspectrumpic=s=1280x480:legend=1 espectro_voz.png
```

Ponlas una encima de otra. Donde las dos tienen color intenso a la misma altura, ahí está la pelea.

---

## Solución 1: EQ complementario (el hueco fijo)

La idea es sencilla: **lo que uno necesita, el otro lo cede.** No se le sube a la voz; se le hace hueco
en la música.

```bash
# la música cede la franja de la voz y le suelta los graves al bombo
ffmpeg -i 02_MUSICA.wav -af "
  highpass=f=90,
  equalizer=f=350:t=q:w=1.0:g=-2.5,
  equalizer=f=2800:t=q:w=1.1:g=-4.5,
  volume=-20dB
" musica_con_hueco.wav
```

Y el complemento en la voz, que refuerza justo lo que la música cedió:

```bash
ffmpeg -i 01_VOZ.wav -af "
  highpass=f=85,
  equalizer=f=350:t=q:w=1.0:g=-1.5,
  equalizer=f=3000:t=q:w=0.9:g=+2.5,
  highshelf=f=8000:g=1.5
" voz_complementaria.wav
```

**Las tres reglas del EQ complementario:**

1. **Corta más de lo que subes.** Un corte de −4,5 dB en la música vale más que un realce de +4,5 dB en
   la voz, y no le agrega ruido ni sibilancia a nada.
2. **Q ancho para cortar, Q estrecho solo para problemas puntuales.** `w=1.0` a `w=1.3` en el hueco. Un
   corte con Q estrecho hace un agujero que se oye como agujero.
3. **No pasar de −6 dB en el hueco.** Más que eso y la música pierde su carácter: se vuelve un lecho sin
   vida y el cliente dice "la música ya no suena bien" (y tiene razón).

La ventaja del hueco fijo: **es transparente**. No respira, no bombea, no hace nada raro. Está siempre.

La desventaja: cuando la voz calla, la música sigue con el hueco puesto y suena un poco apagada. Por eso
existe la solución 3.

---

## Solución 2: sidechain (el ducking del bloque 75) — y su límite

`sidechaincompress` baja **toda la música** cuando hay voz. Funciona, se usa siempre, y tiene un
problema conceptual:

Cuando la voz dice una "s", no hay razón para que el bombo de la música baje. Pero baja. El ducking de
banda completa es un martillo: resuelve el problema y de paso se lleva por delante la energía de la
música que **no** estaba estorbando.

Se nota como "la música respira" o "la música bombea con la voz". En una pieza de venta rápida no
importa. En un video de marca de 60 segundos con música protagonista, sí.

```bash
# ducking clásico de banda completa (bloque 75)
[mus][voz] sidechaincompress=threshold=0.05:ratio=8:attack=15:release=350 [musd]
```

---

## Solución 3: ducking multibanda — la técnica que separa a los que saben

Aquí está lo bueno. En vez de bajar toda la música, **partes la música en bandas y solo le haces ducking
a la banda que estorba**. El bombo y el bajo siguen igual de fuertes todo el tiempo; solo la franja de
2–4 kHz se aparta cuando hay voz.

El resultado: la música se siente igual de presente y la voz se entiende perfecta. Es el mejor truco de
mezcla de audio para video que existe, y ffmpeg lo puede hacer con el filtro `acrossover`.

```bash
ffmpeg \
  -i 01_VOZ.wav -i 02_MUSICA.wav \
  -filter_complex "
    # la voz se usa dos veces: como señal y como disparador del ducking
    [0:a] asplit=2 [voz][voz_key];

    # partir la música en 3 bandas: graves / medios (la zona de la voz) / agudos
    [1:a] acrossover=split=800 3500 [low][mid][high];

    # SOLO la banda media se aparta cuando hay voz
    [mid][voz_key] sidechaincompress=
        threshold=0.04:ratio=12:attack=10:release=300:makeup=1 [mid_duck];

    # volver a juntar las tres bandas
    [low][mid_duck][high] amix=inputs=3:normalize=0, volume=-18dB [mus_final];

    [voz][mus_final] amix=inputs=2:duration=longest:normalize=0 [mix]
  " \
  -map "[mix]" -ar 48000 -c:a pcm_s24le mezcla_multibanda.wav
```

Qué hace cada pieza:

- **`asplit=2`** duplica la voz. Una copia va a la mezcla, la otra sirve de disparador. Si no duplicas,
  ffmpeg te dice que el pad ya está consumido.
- **`acrossover=split=800 3500`** parte la música en tres: por debajo de 800 Hz, entre 800 y 3500, y por
  encima de 3500. Son filtros de cruce de fase coherente, así que al volver a sumarlas no hay huecos ni
  refuerzos raros.
- **`ratio=12`** es agresivo, pero solo actúa en una banda estrecha, así que no se nota como bombeo.
- El `volume=-18dB` al final va sobre la música completa, después de rearmarla.

**Compáralo con el ducking de banda completa.** Con multibanda puedes tener la música 4–6 dB **más
arriba** que con el ducking normal y aun así entender mejor la voz. Es decir: música más presente y voz
más clara al mismo tiempo. Ese es el negocio.

---

## Solución 4: EQ dinámico casero

El EQ dinámico es un hueco que **solo aparece cuando hace falta**. Es exactamente lo que acabas de
construir con `acrossover` + `sidechaincompress`: banda estrecha + reducción dependiente de la voz. En
ffmpeg no hay un filtro llamado "EQ dinámico", pero la construcción de arriba **es** un EQ dinámico.

Una versión más simple, con dos bandas, para cuando el multibanda de tres es demasiado:

```bash
ffmpeg -i 01_VOZ.wav -i 02_MUSICA.wav \
  -filter_complex "
    [0:a] asplit=2 [voz][key];
    [1:a] acrossover=split=1800 [bajo][alto];
    [alto][key] sidechaincompress=threshold=0.05:ratio=9:attack=12:release=320 [alto_d];
    [bajo][alto_d] amix=inputs=2:normalize=0, volume=-19dB [mus];
    [voz][mus] amix=inputs=2:duration=longest:normalize=0 [mix]
  " -map "[mix]" mezcla_2bandas.wav
```

---

## Comparativa: cuándo usar cuál

| Técnica | Cuándo | Ventaja | Costo |
|---|---|---|---|
| **Bajar la música** | siempre, como base | trivial | no resuelve enmascaramiento |
| **EQ complementario fijo** | siempre, como base | transparente, cero artefactos | la música pierde brillo también en los silencios |
| **Ducking banda completa** (`75`) | reel rápido, video de venta | simple, efectivo | la música bombea |
| **Ducking multibanda** | video de marca, música protagonista, pieza larga | música presente + voz clara | comando más largo |
| **Liberar el centro** (`stereotools`) | música muy estéreo | gratis, no toca el timbre | inútil si la música es casi mono |

Y se apilan. La receta completa de producción usa las cuatro:

```bash
ffmpeg -i 01_VOZ.wav -i 02_MUSICA.wav \
  -filter_complex "
    [0:a] equalizer=f=3000:t=q:w=0.9:g=2, asplit=2 [voz][key];
    [1:a] highpass=f=90,
          equalizer=f=2800:t=q:w=1.2:g=-3,
          stereotools=mlev=0.72:slev=1.25,
          acrossover=split=800 3500 [low][mid][high];
    [mid][key] sidechaincompress=threshold=0.04:ratio=10:attack=10:release=300 [midd];
    [low][midd][high] amix=inputs=3:normalize=0, volume=-18dB [mus];
    [voz][mus] amix=inputs=2:duration=longest:normalize=0 [mix]
  " -map "[mix]" -ar 48000 -c:a pcm_s24le mezcla_completa.wav
```

Cinco técnicas, cada una aportando 2–4 dB de claridad. Sumadas, la diferencia es enorme.

---

## El otro choque que nadie ve: graves

Toda la atención se va a 2–4 kHz, pero hay un segundo choque, en 80–250 Hz, y es el que hace que una
mezcla suene "sucia" o "con barro".

Ahí conviven: el cuerpo de la voz, el bajo, el bombo, el ruido de manejo del micrófono, el aire
acondicionado, el tráfico y la resonancia del cuarto. Todo junto. Y como el parlante del celular no
reproduce nada por debajo de 400 Hz, tú **no oyes** ese barro en tus audífonos de mezcla, pero sí come
margen de tu mezcla y te hace normalizar más bajo.

La solución es rutinaria y no falla:

```bash
# corta-graves en TODO lo que no sea la música
highpass=f=85    # voz  (85 Hz para voz masculina, 110 Hz para femenina)
highpass=f=120   # efectos (salvo los que son sub-graves a propósito)
highpass=f=150   # ambiente (el ambiente casi nunca necesita graves)
```

Nadie va a extrañar lo que hay debajo de 85 Hz en una voz. Y recuperas 2–3 dB de margen de mezcla
gratis.

---

## Verificar que funcionó, con números

```bash
# nivel de energía en la banda 2-4 kHz de cada pista
for f in 01_VOZ.wav musica_con_hueco.wav; do
  echo "--- $f (2-4 kHz) ---"
  ffmpeg -i "$f" -af "bandpass=f=3000:width_type=o:w=1,astats=metadata=1" \
    -f null - 2>&1 | grep "RMS level dB" | head -1
done
```

Lo que buscas: la voz debe tener **al menos 12 dB más de energía que la música en esa banda**. Si tienes
6, sigues teniendo problema. Si tienes 18, quizá te pasaste y la música quedó sin vida.

---

## Errores comunes

1. **Bajar la música una y otra vez.** Si a −24 dB todavía tapa la voz, el problema es espectral. Bajar
   más solo mata la música.
2. **Subir la voz en vez de hacerle hueco.** Subir la voz sube también su ruido, su sibilancia y su
   compresión. Corta en la música.
3. **Hueco con Q muy estrecho.** `w=0.3` hace un agujero que se oye. `w=1.0`–`1.3`.
4. **Hueco de más de 6 dB.** La música pierde carácter y el cliente lo nota.
5. **Realzar la voz en 3 kHz sin límite.** Más de +4 dB ahí y la voz se vuelve estridente y cansa a los
   15 segundos.
6. **Olvidar `asplit` al usar la voz como disparador.** ffmpeg falla o consume la voz de la mezcla.
7. **Usar `acrossover` y olvidar el `amix` con `normalize=0`.** Las tres bandas salen 9,5 dB abajo.
8. **No cortar graves.** El barro de 80–250 Hz no se oye en audífonos pequeños pero te come el margen.
9. **Ducking agresivo de banda completa en video de marca.** El bombeo se nota y abarata la pieza.
10. **Creer que el problema es la música cuando es la voz.** Una voz sin EQ ni compresión no gana
    ninguna pelea. Trata primero (`72`, `73`).
11. **No mirar el espectrograma.** Diez segundos de `showspectrumpic` te dicen dónde está el choque.
12. **Aplicar la misma receta a toda música.** Un tema de piano y uno de trap no chocan en el mismo
    lugar. Diagnostica cada vez.

---

## Checklist

- [ ] Se hizo el **diagnóstico**: ¿el problema es de nivel o de frecuencia? (prueba del corte de −12 dB)
- [ ] Se miró el **espectrograma** de voz y música y se identificó la zona de choque.
- [ ] La música tiene un **hueco de −3 a −5 dB entre 2,5 y 3,5 kHz**, con Q ancho (`w≈1.0–1.3`).
- [ ] La voz tiene un **realce moderado (máx. +3 dB)** en la misma zona, no más.
- [ ] **Se corta más de lo que se sube.**
- [ ] Hay **corta-graves** en voz (85–110 Hz), efectos (120 Hz) y ambiente (150 Hz).
- [ ] Si la música es protagonista, se usó **ducking multibanda** (`acrossover`) en vez de banda completa.
- [ ] Se usó `asplit` para tomar la voz como **disparador** sin perderla de la mezcla.
- [ ] Todos los `amix` llevan **`normalize=0`**.
- [ ] Se **liberó el centro** de la música con `stereotools` si aplicaba.
- [ ] Se **verificó con `bandpass` + `astats`**: la voz tiene al menos 12 dB más que la música en 2–4 kHz.
- [ ] La música **sigue sonando a música**: no quedó como un lecho sin carácter.

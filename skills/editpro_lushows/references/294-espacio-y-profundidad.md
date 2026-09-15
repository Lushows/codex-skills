# 294 — Espacio y profundidad

Hasta aquí la mezcla ha sido plana: cada elemento tiene un nivel y una zona de frecuencia. Falta la
tercera dimensión: **dónde está cada cosa en el espacio**. Izquierda o derecha. Cerca o lejos.

Es la diferencia entre una mezcla que suena a "archivos pegados" y una que suena a un lugar donde
pasaron cosas.

---

## Las cuatro perillas de la distancia

El cerebro decide si algo está cerca o lejos usando cuatro pistas, y todas se pueden falsificar. Van en
orden de importancia:

| Perilla | Cerca | Lejos |
|---|---|---|
| **1. Proporción reverb/directo** | casi todo directo | mucha reverb, poco directo |
| **2. Agudos** | brillante, completo | los agudos se pierden en el aire |
| **3. Nivel** | fuerte | bajo |
| **4. Primeras reflexiones** | llegan muy rápido (5–15 ms) | llegan tarde (30–80 ms) |

El error de todo el mundo es usar solo la número 3. Bajar el volumen no aleja nada: hace lo mismo que
alejarte tú del parlante. Suena "más bajito", no "más lejos".

**El truco que sí funciona:** si le quitas agudos y le sumas reverb, algo suena lejos **aunque esté al
mismo nivel**. Y al revés: una voz muy reverberada no se acerca subiéndole el volumen.

---

## El error de la voz seca flotando

Es el defecto de mezcla más común en video de negocio y el más fácil de arreglar.

Pasa así: grabas la voz con un micrófono de solapa, muy cerca de la boca. Le aplicas la cadena del
bloque 7: limpieza, gate, EQ, compresión. El resultado es una voz **perfectamente seca**: cero
reverberación, piso de ruido a −46,5 dB, cero información de espacio.

Y esa voz la pegas encima de un plano de un restaurante lleno de gente.

El oído hace la cuenta inmediatamente: *veo un salón grande, oigo una voz grabada en una caja*. No lo
puede articular, pero lo registra como "esto es un anuncio". La voz **flota** sobre la imagen en vez de
estar dentro de ella.

Y la trampa es que la voz, por sí sola, suena magnífica. El problema no aparece hasta que la juntas con
la imagen.

**La solución no es más reverb en la voz.** Es darle a la voz un mínimo de espacio y, sobre todo, poner
debajo un lecho de ambiente del lugar real (`296`). Con ambiente a −38 dB, la voz deja de flotar sin que
tengas que tocarla.

Si además necesitas un toque de sala:

```bash
# reverb muy corta y muy discreta sobre la voz: 8% de mezcla, cola de 40 ms
ffmpeg -i 01_VOZ.wav -af "aecho=0.9:0.35:40:0.08" voz_con_sala.wav
```

Los cuatro números de `aecho` son: `ganancia_entrada : ganancia_salida : retardos_ms : decaimientos`.
Con `0.08` de decaimiento estás sumando un eco 22 dB por debajo del original. **Eso es lo correcto.**
Si lo oyes claramente como eco, te pasaste diez veces.

---

## Reverberación: las tres maneras en ffmpeg

### 1. `aecho` — la barata, para toques sutiles

```bash
# sala pequeña: dos reflexiones cortas
aecho=0.8:0.9:25|45:0.12|0.07

# sala mediana: tres reflexiones
aecho=0.8:0.88:40|75|130:0.15|0.10|0.06

# espacio grande (bodega, iglesia): reflexiones largas
aecho=0.8:0.85:120|250|400:0.25|0.18|0.10
```

La sintaxis con `|` define varias reflexiones: `retardo1|retardo2|retardo3` y su decaimiento respectivo.

`aecho` no es una reverberación de verdad — es un eco. Para toques discretos nadie nota la diferencia.
Para una cola larga y densa suena metálico y se oye como efecto.

### 2. `afir` con una respuesta de impulso — la buena

Una respuesta de impulso (IR) es la grabación real de cómo suena un espacio. Con `afir` convolucionas
tu audio con ese espacio y suena **exactamente** a haber sido grabado ahí.

```bash
# aplicar una IR de sala real, mezclada al 18% con la señal seca
ffmpeg -i 01_VOZ.wav -i ir_sala_pequena.wav \
  -filter_complex "[0:a][1:a] afir=dry=10:wet=2:length=1 [out]" \
  -map "[out]" voz_convolucion.wav
```

`dry` y `wet` van de 0 a 10. `dry=10:wet=2` es señal seca completa más un 20% de sala. Para voz sobre
video, ese es el rango: `wet` entre 1 y 3. Por encima de 4 ya suena a estudio de radio de los 80.

Dónde conseguir IRs gratis y con licencia clara: **OpenAIR** (openairlib.net, universidad de York, CC),
y **EchoThief** (echothief.com, uso libre). Ambas son grabaciones de espacios reales.

### 3. `asubboost`, `stereotools` y compañía — para ancho, no para profundidad

`stereotools` ensancha o estrecha la imagen estéreo. Es útil pero **no crea profundidad**: mueve las
cosas de lado, no hacia atrás.

```bash
# ensanchar la música un poco para dejarle el centro a la voz
ffmpeg -i 02_MUSICA.wav -af "stereotools=mlev=0.7:slev=1.3" musica_ancha.wav
```

`mlev` es el nivel del centro (mid), `slev` el de los lados (side). Bajar el mid y subir el side abre un
hueco en el centro exactamente donde vive la voz. **Es una de las técnicas más efectivas de toda la
mezcla y casi nadie la usa.** Ver también `295`.

Cuidado: pasarse con `slev` destruye la compatibilidad mono (`299`). Con `slev` por encima de 1.6, en
un parlante de celular la música se desvanece.

---

## Paneo: dónde va cada cosa de izquierda a derecha

La regla, corta:

| Elemento | Posición | Motivo |
|---|---|---|
| **Voz** | **centro, siempre** | es la información. El centro sobrevive en mono. |
| Música | estéreo amplio | llena los lados, deja el centro |
| Efecto ligado a algo en pantalla | donde está en pantalla | solo si es evidente |
| Efecto de transición | centro o amplio | va con el corte, no con un objeto |
| Ambiente | estéreo amplio | envuelve |

**La voz nunca se panea.** Ni un poquito. Si el video se ve en un celular con un solo parlante (la
mayoría), todo se suma a mono y una voz paneada pierde nivel respecto a lo que está centrado.

Para paneos concretos, el filtro `pan`:

```bash
# un efecto mono, colocado 60% a la derecha
ffmpeg -i clic.wav -af "pan=stereo|c0=0.4*c0|c1=1.0*c0" clic_derecha.wav

# convertir un mono a estéreo centrado (lo normal para la voz)
ffmpeg -i 01_VOZ.wav -af "pan=stereo|c0=c0|c1=c0" voz_estereo.wav
```

En vertical (9:16) el paneo casi no aporta: la pantalla es angosta y la mayoría escucha por un parlante.
Úsalo con moderación o no lo uses. En horizontal 16:9 con audífonos sí se nota.

---

## La receta completa: tres planos de profundidad

Piensa la mezcla en tres planos, como un plano de cámara.

```
PRIMER PLANO      voz            seca, centro, brillante, nivel 0 dB
PLANO MEDIO       música, FX     algo de ancho, sin agudos extremos, -20 dB
FONDO             ambiente       lowpass 7 kHz, muy ancho, -38 dB
```

Y el comando que lo construye:

```bash
ffmpeg \
  -i 01_VOZ.wav -i 02_MUSICA.wav -i 03_FX.wav -i 04_AMB.wav \
  -filter_complex "
    # PRIMER PLANO: voz al centro, con un 8% de sala para que no flote
    [0:a] pan=stereo|c0=c0|c1=c0,
          aecho=0.9:0.35:35:0.07,
          volume=0dB                                       [voz];

    # PLANO MEDIO: música ancha con el centro liberado
    [1:a] stereotools=mlev=0.72:slev=1.25,
          volume=-20dB                                     [mus];

    # PLANO MEDIO: efectos, ligeramente más presentes
    [2:a] volume=-9dB                                      [fx];

    # FONDO: ambiente sin agudos (suena lejos) y muy ancho
    [3:a] lowpass=f=6500,
          stereotools=mlev=0.6:slev=1.4,
          volume=-38dB                                     [amb];

    [mus][voz] sidechaincompress=
        threshold=0.05:ratio=8:attack=15:release=350       [musd];
    [voz][musd][fx][amb] amix=inputs=4:duration=longest:normalize=0 [mix]
  " \
  -map "[mix]" -ar 48000 -c:a pcm_s24le mezcla_con_espacio.wav
```

Lo que hace cada decisión:

- La voz con `aecho` al 7%: deja de sonar a cabina, sin que se note la reverb.
- La música con `mlev=0.72`: el centro baja 2,9 dB, que es exactamente donde vive la voz.
- El ambiente con `lowpass=6500`: el oído lee "esto viene de lejos" sin necesidad de bajarle más.

---

## Cómo mover algo "hacia atrás" de verdad

Cuando quieras que un elemento se aleje sin bajar el volumen, mueve las cuatro perillas juntas. Esta es
la escala:

```bash
# MUY CERCA (voz al oído, ASMR, susurro de venta)
"highshelf=f=7000:g=2, aecho=0.9:0.2:12:0.03"

# CERCA (voz normal de locución)
"aecho=0.9:0.35:35:0.07"

# PLANO MEDIO (alguien hablando en el salón)
"lowpass=f=9000, aecho=0.85:0.5:55|95:0.16|0.10, volume=-5dB"

# LEJOS (alguien al fondo del local)
"lowpass=f=5500, highpass=f=180, aecho=0.8:0.6:90|170|260:0.28|0.20|0.12, volume=-12dB"

# MUY LEJOS (afuera, otra habitación)
"lowpass=f=2200, highpass=f=250, aecho=0.8:0.65:140|280:0.35|0.25, volume=-18dB"
```

Fíjate que "muy lejos" también lleva `highpass`: a mucha distancia se pierden los graves por las paredes
tanto como los agudos por el aire. Ese `highpass=250` es lo que hace que suene "a través de una puerta"
en vez de "bajito".

Ese último preset es, literalmente, cómo se hace que una música suene "como si viniera del local de al
lado", que es un recurso precioso para transiciones.

---

## El caso de la voz en off contra la voz en escena

Un video tiene dos tipos de voz y **no pueden sonar igual**:

- **Voz en off / narrador.** No está en la escena, está contándola. Va seca, centrada, cerca, sin
  ambiente. Es la voz de tu cabeza.
- **Voz en escena.** La persona que se ve hablando. Debe tener el espacio del lugar donde está: algo de
  sala, algo de ambiente debajo.

Si las dos suenan idénticas, el video se siente raro y nadie sabe por qué. La diferencia:

```bash
# narrador: seco, presente, sin sala
ffmpeg -i voz_off.wav -af "highshelf=f=8000:g=1.5" narrador.wav

# persona en escena: sala + el ambiente del lugar debajo
ffmpeg -i voz_escena.wav -af "aecho=0.85:0.45:45|80:0.18|0.11, lowpass=f=13000" en_escena.wav
```

---

## Cuándo NO poner espacio

- **Voz de venta directa a cámara.** Cuanto más seca y cerca, más íntima y más convincente. Nada de
  reverb.
- **Piezas de 6–10 segundos.** No hay tiempo de percibir el espacio; solo ensucia.
- **Cuando el material ya tiene reverb de la sala.** Sumarle más es apilar dos espacios distintos y suena
  a error. Si la toma se grabó en un salón con eco, ese es tu espacio.
- **Cuando el video se ve solo en celular con parlante.** La mitad del trabajo de espacio se pierde. No
  es que estorbe, es que no rinde.

---

## Errores comunes

1. **Creer que bajar el volumen aleja algo.** Aleja quitando agudos y sumando reverb, no bajando el
   fader.
2. **Voz seca sobre plano de un espacio real.** El defecto número uno. Se arregla con ambiente debajo
   (`296`), no con reverb encima.
3. **Reverb que se oye.** Si puedes identificar la reverb como reverb, te pasaste. Decaimiento 0,05–0,12
   en `aecho`, `wet` de 1 a 3 en `afir`.
4. **Panear la voz.** Nunca. El centro es de la voz.
5. **Apilar dos espacios.** Reverb encima de una toma que ya tiene eco de sala = confusión.
6. **Pasarse con `stereotools`.** `slev` por encima de 1.6 destruye la compatibilidad mono y en un
   celular la música desaparece.
7. **Usar `aecho` para colas largas.** Suena metálico. Para colas largas, `afir` con una IR real.
8. **Poner la misma reverb a todo.** Cada elemento vive en un plano distinto; si comparten reverb,
   comparten plano.
9. **Reverb en la música que ya viene con reverb.** Toda música producida ya tiene su espacio.
10. **Espacio en una pieza de 8 segundos.** No hay tiempo de percibirlo; solo enturbia.
11. **Narrador y persona en escena con el mismo tratamiento.** Se siente raro y nadie sabe por qué.
12. **No verificar en mono.** Todo el trabajo de ancho se juzga también en mono (`299`).

---

## Checklist

- [ ] La **voz está al centro** y no se paneó ni un grado.
- [ ] La voz **no flota**: hay ambiente debajo (`296`) o un toque mínimo de sala.
- [ ] La reverb **no se identifica como reverb** al escuchar la mezcla.
- [ ] Los elementos que deben sonar lejos tienen **menos agudos**, no solo menos volumen.
- [ ] La mezcla está pensada en **tres planos** (primer plano / medio / fondo) y cada elemento tiene el
      suyo asignado.
- [ ] La música tiene el **centro liberado** (`stereotools` con `mlev` bajo) si la voz cuesta entenderse.
- [ ] `slev` no pasa de **1.5**; se verificó en mono.
- [ ] **No se apilaron dos espacios** sobre la misma fuente.
- [ ] **Voz en off y voz en escena** tienen tratamientos distintos.
- [ ] Si la pieza dura menos de 10 segundos, **no se le puso espacio**.
- [ ] Las IRs usadas tienen **licencia clara** (OpenAIR, EchoThief).
- [ ] Se escuchó la mezcla **en un parlante de celular** y el espacio sigue teniendo sentido.

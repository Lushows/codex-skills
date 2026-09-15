# 290 — Qué es mezclar

El bloque 7 (70–79) te enseñó a arreglar cada elemento por separado: limpiar la voz, ecualizarla,
comprimirla, elegir la música, hacer ducking, construir efectos. Todo eso es **tratamiento**.

Mezclar es otra cosa. Mezclar es decidir **cómo conviven** esos elementos ya tratados en el mismo
minuto de tiempo. Una voz perfecta, una música perfecta y unos efectos perfectos pueden sonar a barro
cuando se juntan. La mezcla no es la suma de las partes: es el reparto del espacio entre ellas.

---

## La idea que resuelve el módulo: el espacio es finito

Imagínate un cuarto pequeño. Cabe una mesa, dos sillas y una lámpara. Si metes tres mesas, no es que
suenen mal las mesas: es que ya no puedes caminar.

Un video tiene exactamente el mismo problema. El "cuarto" tiene cuatro dimensiones y todas son
limitadas:

| Dimensión | Qué es | Cuánto hay |
|---|---|---|
| **Frecuencia** | de 20 Hz a 20.000 Hz | fijo, no se estira |
| **Tiempo** | los segundos del video | fijo |
| **Nivel** | de 0 dBFS hacia abajo | el techo es 0, no se pasa |
| **Espacio** | izquierda–derecha, cerca–lejos | dos ejes, y el centro es uno solo |

Cada elemento de tu video ocupa un pedazo de cada una de esas cuatro dimensiones. **Cuando dos
elementos quieren el mismo pedazo, uno de los dos tiene que ceder.** Eso es todo lo que es mezclar.

El editor novato intenta resolver los choques con el fader: sube la voz. Como la música quedó tapada,
sube la música. Como ahora la voz no se oye, sube la voz. A los cuatro pasos todo está en el techo, la
mezcla satura y suena a radio de bus.

El editor que sabe mezclar hace lo contrario: **baja lo que estorba y quita lo que sobra**. Si la voz no
se oye, no se sube la voz — se le hace hueco a la voz.

---

## El diagnóstico que hay que hacer antes de tocar nada

Antes de mezclar, mide. No opines sobre lo que no has medido.

```bash
# nivel medio y pico de un archivo
ffmpeg -i voz.wav -af volumedetect -f null - 2>&1 | grep -E "mean_volume|max_volume"

# radiografía completa: RMS, pico, piso de ruido, rango dinámico, muestras recortadas
ffmpeg -i voz.wav -af astats=metadata=1 -f null - 2>&1 | grep -E \
  "RMS level|Peak level|Noise floor|Dynamic range|Number of clipped"
```

Esto es lo que salió de un caso real, midiendo la misma voz antes y después de la cadena de 9 módulos
del bloque 7:

| Medición | Cruda | Procesada |
|---|---|---|
| RMS (nivel medio percibido) | **−16,4 dB** | — |
| Pico | **0,00 dB** ← saturando | **−1,6 dB** |
| Piso de ruido | **−25,7 dB** | **−46,5 dB** |

Leamos esos números como los lee un mezclador:

**Pico 0,00 dB en la toma cruda.** Eso no es "está fuerte": eso es que la grabación tocó el techo
digital y se aplanó. La forma de onda ahí arriba está cortada con tijera. Ese daño no se quita
después — se puede disimular con `adeclip`, pero la información se perdió en la grabación. Lección de
mezcla: **el techo se respeta desde la grabación, no en el render.**

**Piso de ruido a −25,7 dB.** Solo 9 dB por debajo del nivel medio de la voz. Eso quiere decir que el
"silencio" entre frases sonaba casi tan fuerte como la voz. En una mezcla eso es catastrófico: cuando
la voz calla y el ruido se queda, la música tiene que competir contra un colchón de ruido, no contra
silencio. No hay espacio.

**Después del proceso: pico −1,6 y piso −46,5.** El rango útil pasó de 9 dB a casi 45 dB. Eso es lo que
un mezclador llama "espacio". Ahora sí hay dónde meter música: cabe 25 dB por debajo de la voz sin
chocar con nada.

**La conclusión operativa:** la mezcla se hace sobre elementos ya tratados. Si intentas mezclar una voz
con piso a −25,7, no estás mezclando — estás negociando con basura.

---

## Las cuatro maneras de hacerle espacio a algo

Cuando dos elementos pelean, tienes exactamente cuatro herramientas. Se usan en este orden, de la más
barata a la más cara.

### 1. Espacio en el tiempo: que no suenen a la vez

La más simple y la que nadie usa. Si el efecto choca con la primera palabra, mueve el efecto 200 ms.
Si la música arranca encima de la frase de apertura, que arranque después.

```bash
# retrasar un efecto 250 ms (adelay va en milisegundos, uno por canal)
ffmpeg -i golpe.wav -af "adelay=250|250" golpe_movido.wav
```

Regla dura: **en cualquier instante hay un solo protagonista.** Si dos cosas importantes caen en el
mismo segundo, una de las dos no era importante. Ver `291`.

### 2. Espacio en nivel: que uno esté claramente debajo

Bajar es gratis. Subir cuesta.

```bash
# la música entera 18 dB por debajo de donde estaba
ffmpeg -i musica.wav -af "volume=-18dB" musica_lecho.wav
```

Con la voz a −16 dB RMS, una música a −34 dB RMS se oye perfectamente y no estorba. Los números
concretos están en `291`.

### 3. Espacio en frecuencia: que ocupen zonas distintas

Aquí es donde se gana la mezcla de verdad. La inteligibilidad de la voz vive entre 2 y 4 kHz. Si la
música tiene guitarras y platillos brillantes ahí, la voz desaparece aunque esté 20 dB más arriba.

```bash
# hueco de 4 dB en 3 kHz en la música, con Q ancho para que no se note
ffmpeg -i musica.wav -af "equalizer=f=3000:t=q:w=1.2:g=-4" musica_con_hueco.wav
```

Módulo completo: `295`.

### 4. Espacio en profundidad: que uno esté más lejos

Reverberación, retardo y pérdida de agudos hacen que algo suene atrás sin bajarle el volumen. Sirve
cuando necesitas que un elemento esté presente pero no adelante. Módulo completo: `294`.

---

## Por qué "todo al máximo" siempre suena peor

Hay una trampa perceptual: **más fuerte suena mejor durante tres segundos.** Por eso el instinto es
subir. Pero el oído se adapta al nivel general en unos segundos, y a partir de ahí solo percibe
diferencias *relativas*.

Es decir: no importa qué tan fuerte esté la voz. Importa cuánto más fuerte está **que la música**. Si
subes las dos, no ganaste nada — solo te quedaste sin techo.

Prueba esto para convencerte. Toma tu mezcla, haz dos versiones, iguálalas a la misma sonoridad y
compara:

```bash
# versión A: voz +6 dB, música +6 dB
# versión B: voz igual, música -6 dB
# ...las dos normalizadas al mismo LUFS para que la comparación sea honesta
ffmpeg -i mezcla_A.wav -af "loudnorm=I=-14:TP=-1" A_igualada.wav
ffmpeg -i mezcla_B.wav -af "loudnorm=I=-14:TP=-1" B_igualada.wav
```

Igualadas, la B siempre gana. Siempre. Porque la B tiene 12 dB de separación y la A tiene 0.

**Regla:** una mezcla se juzga a igual sonoridad. Si comparas dos versiones y una está más fuerte, no
estás comparando la mezcla, estás comparando el volumen. Ver `293`.

---

## El orden en que se mezcla

No se mezcla de arriba abajo. Se mezcla **desde el protagonista hacia afuera**.

1. **Voz sola, en el nivel definitivo.** Ya tratada (bloque 7). Este es tu punto de referencia y no se
   vuelve a mover. Todo lo demás se ajusta contra ella.
2. **Ambiente.** Debajo de todo, muy bajo, tapando los huecos entre planos (`296`). Se pone temprano
   porque cambia la percepción de todo lo demás.
3. **Música.** Se sube hasta que estorbe, y se baja 3 dB (`291`, `295`).
4. **Efectos.** Uno por uno, cada uno en el momento exacto (`297`).
5. **Espacio.** Reverb y paneo, al final, con el conjunto ya balanceado (`294`).
6. **Sonoridad final.** Una sola vez, sobre la mezcla completa, en dos pasadas (`293`).

El error de orden más común es normalizar antes de mezclar. Si normalizas la voz a −14 LUFS, luego le
metes música y efectos, la mezcla ya no está a −14. La sonoridad final es lo **último** que se toca.

---

## Un ejemplo completo, con números

Un reel de 30 segundos: voz de un dueño de restaurante, música, ambiente de local, dos efectos.

```bash
ffmpeg \
  -i voz_tratada.wav \
  -i musica.wav \
  -i ambiente_loop.wav \
  -i whoosh.wav \
  -i impacto.wav \
  -filter_complex "
    [0:a] volume=0dB [voz];
    [1:a] volume=-20dB, equalizer=f=3000:t=q:w=1.2:g=-4 [mus];
    [2:a] volume=-38dB, lowpass=f=7000 [amb];
    [3:a] adelay=1200|1200, volume=-10dB [fx1];
    [4:a] adelay=22400|22400, volume=-8dB [fx2];
    [mus][voz] sidechaincompress=threshold=0.05:ratio=8:attack=15:release=350 [mus_duck];
    [voz][mus_duck][amb][fx1][fx2] amix=inputs=5:duration=longest:normalize=0 [mezcla]
  " \
  -map "[mezcla]" -c:a pcm_s24le mezcla_cruda.wav
```

Lo importante de ese comando no son los filtros — es la columna de niveles:

```
voz          0 dB   ← la referencia, no se mueve
música     -20 dB   ← con hueco en 3 kHz y ducking
ambiente   -38 dB   ← debajo de todo, sin agudos (suena lejos)
efecto 1   -10 dB   ← puntual, en el segundo 1,2
efecto 2    -8 dB   ← puntual, en el segundo 22,4
```

Fíjate en `normalize=0` dentro de `amix`. **Sin eso, ffmpeg divide todo entre el número de entradas**
y tu mezcla de 5 pistas sale 14 dB más bajo de lo que pusiste. Es el error de mezcla más frecuente con
ffmpeg y no da ningún mensaje de advertencia.

Y fíjate en que ese comando **no normaliza**. Sale a `mezcla_cruda.wav` en 24 bits. La sonoridad se
ajusta en un paso aparte (`293`), sobre este archivo.

---

## Cómo saber si la mezcla está bien

Tres pruebas, en este orden, y ninguna necesita equipo caro.

**1. La prueba del volumen bajo.** Pon la mezcla muy bajita, casi al límite de lo audible. Lo que
sobrevive es lo que domina la mezcla. Si a volumen bajo lo que oyes es la música, tienes la jerarquía
al revés.

**2. La prueba del parlante de celular.** Un celular no reproduce nada por debajo de ~400 Hz. Si tu
mezcla depende de los graves para tener cuerpo, en un celular no queda nada. Simúlalo:

```bash
ffmpeg -i mezcla.wav -af "highpass=f=400,lowpass=f=8000,volume=-6dB" prueba_celular.wav
```

Si la voz sigue clarísima ahí, ganaste. Detalle completo en `299`.

**3. La prueba de la otra habitación.** Sal del cuarto y deja el video sonando. Desde afuera solo llega
el balance grueso. Si desde afuera oyes la música y no entiendes ni una palabra, vuelve a `291`.

---

## Lo que la mezcla NO arregla

Sé honesto contigo mismo antes de perder tres horas:

- **Grabación saturada** (pico en 0,00 como la del caso). `adeclip` disimula; no reconstruye.
- **Voz grabada en un cuarto con eco.** La reverb de la sala está pegada a la voz para siempre. Se puede
  atenuar; no se puede quitar.
- **Dos frases grabadas con micrófonos distintos.** Se pueden acercar con EQ, pero el salto de timbre se
  oye. La solución es de rodaje, no de mezcla.
- **Una toma en la que la persona lo dijo mal.** Ninguna cadena de filtros arregla una mala lectura.

Cuando el problema es de origen, la mezcla honesta es la que **esconde** el defecto (tapándolo con
música o ambiente en ese punto) o lo **corta**. No la que lo procesa hasta que suena raro.

---

## Errores comunes

1. **Mezclar subiendo en vez de bajando.** Cada "súbele" te acerca al techo y te quita margen. La mezcla
   se hace bajando lo que estorba.
2. **Usar `amix` sin `normalize=0`.** ffmpeg divide entre el número de entradas y la mezcla sale muy
   baja. Nadie te avisa.
3. **Normalizar la voz antes de mezclar.** La sonoridad final se mide sobre la mezcla completa, al final,
   una sola vez (`293`).
4. **Comparar dos versiones a distinto volumen.** La más fuerte siempre "suena mejor". Iguala primero.
5. **Intentar mezclar material sin tratar.** Con el piso de ruido a −25,7 dB no hay espacio para nada.
   Trata primero (bloque 7), mezcla después.
6. **Meter todo al centro y al mismo plano.** Voz, música, efectos y ambiente en el mismo punto del
   espacio = barro. Ver `294`.
7. **Creer que el problema es de nivel cuando es de frecuencia.** Si la voz no se entiende con la música
   20 dB abajo, el choque es espectral, no de volumen (`295`).
8. **Mezclar con audífonos caros solamente.** El 90% de tu público oye por el parlante del celular. Si no
   lo probaste ahí, no lo probaste.
9. **Dejar el pico en 0.** Cualquier compresión posterior (la de la plataforma) va a distorsionar. Techo
   en −1 dBTP.
10. **Mezclar cansado, en la misma sesión en que editaste.** El oído se adapta y ya no oye lo que hay.
    Media hora de descanso cambia todas las decisiones.
11. **Añadir un elemento más para arreglar la mezcla.** Casi siempre la solución es quitar uno, no meter
    otro.
12. **No dejar los stems.** Si mezclaste todo en un comando gigante y el cliente pide cambiar la música,
    rehaces todo. Ver `292`.

---

## Checklist

- [ ] Cada elemento entró a la mezcla **ya tratado** (limpio, ecualizado, comprimido — bloque 7).
- [ ] Se **midió** antes de mezclar: RMS, pico y piso de ruido de cada pista (`astats`).
- [ ] Ninguna fuente entra **saturada** (pico en 0,00 dB) a la mezcla.
- [ ] La **voz es la referencia** y su nivel no se movió una vez fijado.
- [ ] Todos los `amix` llevan **`normalize=0`**.
- [ ] En cada instante hay **un solo protagonista** (`291`).
- [ ] Cuando algo no se oía, se **bajó lo que estorbaba** en vez de subirlo.
- [ ] Se revisó si el choque era de **nivel o de frecuencia** antes de mover el fader (`295`).
- [ ] La mezcla salió a un archivo **sin normalizar**; la sonoridad se ajusta aparte (`293`).
- [ ] Se pasó la **prueba del volumen bajo**: lo que sobrevive es la voz.
- [ ] Se pasó la **prueba del parlante de celular** (`highpass=400,lowpass=8000`).
- [ ] Se dejaron los **stems** por si hay que rehacer una capa (`292`).

# 201 — La velocidad como ritmo

**Qué resuelve:** tienes un plano de 9 segundos donde alguien sirve una cerveza y el video se muere
ahí. La solución obvia es cortarlo en pedacitos. La solución buena, casi siempre, es **acelerarlo**.
Este módulo trata la velocidad como lo que de verdad es en video social: **el instrumento de ritmo más
barato y más potente que existe**, y el que tú ya usas más que cualquier otro.

Tus 51 proyectos tienen **49 velocidades distintas** aplicadas. Eso no es un accidente: es tu firma.
Este módulo la convierte en método.

---

## 1. Por qué acelerar le gana a cortar

Un plano largo aburre por dos motivos distintos, y confundirlos es el error de base:

- **Aburre porque no pasa nada interesante.** Ahí el problema es la toma. Acelerar no lo arregla.
- **Aburre porque lo interesante pasa demasiado lento.** Ahí acelerar lo arregla completamente.

Servir una cerveza es interesante. Servirla en tiempo real, durante 9 segundos, no. A 2,5x son 3,6
segundos y de repente es un plano que la gente mira completo.

Ahora, por qué acelerar gana contra la alternativa de cortar más:

| | Cortar el plano en 4 | Acelerarlo a 2,5x |
|---|---|---|
| Tiempo tuyo | 4 cortes, 4 decisiones, revisar continuidad | una acción |
| Continuidad | se rompe (saltos de mano, de espuma, de luz) | intacta, es el mismo movimiento |
| Sensación | video "picado", nervioso | video "ágil", con energía |
| Riesgo | cada corte puede saltar feo | ninguno |
| Audio | hay que arreglar 4 empalmes | uno solo, y hay solución (sección 5) |

**La regla operativa:** si el plano tiene un movimiento continuo (servir, caminar, cocinar, montar,
limpiar, llegar), **acelera**. Si el plano tiene momentos distintos separados por pausas muertas,
**corta**. Y si tiene las dos cosas: corta las pausas y acelera lo que queda.

Ese es el 80% del valor de este módulo y cabe en dos frases.

---

## 2. La tabla de velocidades: cuándo cada una

Estos son los rangos que tú ya usas, ordenados por para qué sirve cada uno de verdad.

| Velocidad | Se siente como | Para qué sirve | Tus usos |
|---|---|---|---|
| **1,2x – 1,3x** | nadie lo nota | quitarle grasa a alguien que habla lento | pocos |
| **1,4x – 1,5x** | ágil, aún natural | gente hablando, plano de acción normal | 13 |
| **1,6x – 1,8x** | claramente rápido, todavía legible | manos trabajando, caminar, montar mesa | 9 |
| **2,0x** | "esto va rápido" | el caballo de batalla; casi cualquier acción | 17 |
| **2,5x** | comprimido, con energía | procesos: servir, limpiar, cocinar | 10 |
| **3x – 4x** | montaje / lapso corto | tramos donde solo importa que "pasó algo" | pocos |
| **5x y más** | lapso de tiempo puro | montar el local, llenarse el bar, un día entero | pocos |

**El límite invisible está en 1,8x.** Debajo de eso, una persona hablando todavía se entiende y suena
casi normal. Encima, se convierte en ardilla y hay que tomar una decisión de audio (sección 5).

**El punto dulce de tu estilo es 2,0x.** Diecisiete usos, más que cualquier otra. Tiene sentido: 2x es
la velocidad donde el ojo todavía sigue la acción perfectamente pero el cerebro ya registra "esto es
un video con energía". Si no sabes qué velocidad poner, pon 2x y mira si sobra o falta.

**Cuidado con el vértigo del 5x.** Un lapso de tiempo funciona cuando el encuadre es **fijo** y lo que
se mueve es el contenido (gente llegando, luz cambiando). Si aceleras a 5x un plano con cámara en mano,
el resultado marea físicamente. Cámara en mano tiene techo práctico en 2,5x–3x.

---

## 3. Velocidad constante vs. rampa

**Velocidad constante:** todo el clip a 2x. Es lo que usas casi siempre y está bien.

**Rampa de velocidad (speed ramp):** la velocidad cambia *dentro* del clip. Arranca a 4x, frena a 1x
en el momento importante, vuelve a acelerar. Es lo que hace que un video se sienta editado por alguien
que sabe.

La rampa tiene un solo uso legítimo, y es este:

> **La rampa sirve para señalar.** Aceleras lo que no importa y frenas exactamente sobre lo que sí. El
> cambio de velocidad le dice al ojo "mira aquí" sin poner una flecha.

Ejemplos reales para tu caso:

- La mano toma la botella a 3x, **frena a 1x** justo cuando la espuma corona el vaso, vuelve a 2,5x
  para llevarse el vaso.
- La cámara recorre el local a 4x, **frena a 0,8x** sobre la mesa llena de gente riéndose.
- Alguien camina hacia la cámara a 2,5x y **frena a 1x** en el momento en que sonríe.

En los tres casos, el frenazo cae sobre **el fotograma que vale**. Si no tienes claro cuál es ese
fotograma, no hagas rampa: pon velocidad constante y ya.

### Cómo se hace en CapCut

En el panel de **Velocidad** hay dos pestañas: **Normal** (un número para todo el clip) y **Curva**.
Dentro de Curva vienen presets con nombres tipo *Montaje*, *Hero time*, *Bala*, *Salto* y la opción
**Personalizar**.

Los presets son una trampa cómoda: te ponen el frenazo donde el preset quiso, no donde está tu
momento. Úsalos solo si por casualidad coinciden. Lo que de verdad funciona:

1. Entra a **Curva → Personalizar**.
2. Encuentra primero el fotograma del momento (la espuma coronando) y anota el segundo.
3. Baja el punto de la curva a 1x **medio segundo antes** de ese momento y súbelo medio segundo
   después. La bajada tiene que estar *antes*, no encima: el ojo necesita alcanzar a frenar.
4. Deja los extremos arriba (rápido). La curva queda como una "V" ancha.

**El error que casi todo el mundo comete:** hacer la V muy angosta. Una rampa que baja y sube en 0,2
segundos no se lee como estilo, se lee como que el video se trabó.

### Cómo se hace en ffmpeg

Velocidad constante, video y audio:

```bash
ffmpeg -i entrada.mp4 -filter_complex "[0:v]setpts=PTS/2.0[v];[0:a]atempo=2.0[a]" \
  -map "[v]" -map "[a]" -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

`setpts=PTS/N` es "divide el tiempo entre N". Para 2x va `/2.0`, para 2,5x va `/2.5`. Es al revés de
lo que uno esperaría: números más grandes = más rápido, pero como está dividiendo, el clip dura menos.

Rampa hecha a mano (la forma honesta y sin dolor): **corta el clip en tres pedazos, acelera cada uno
distinto, y únelos.** Suena rústico y es exactamente lo que hace cualquier editor por debajo.

```bash
ffmpeg -i plano.mp4 -filter_complex "\
[0:v]trim=0:4.0,setpts=PTS/3.0,setsar=1[a1];\
[0:v]trim=4.0:5.6,setpts=PTS/1.0,setsar=1[a2];\
[0:v]trim=5.6:9.0,setpts=PTS/2.5,setsar=1[a3];\
[a1][a2][a3]concat=n=3:v=1:a=0[v]" \
  -map "[v]" -an -c:v libx264 -crf 18 -pix_fmt yuv420p rampa.mp4
```

Ese comando hace: 4 segundos a 3x, luego 1,6 segundos a velocidad real (el momento), luego el resto a
2,5x. Fíjate en `setsar=1`: sin eso, `concat` a veces se queja de que los trozos no coinciden.

**Nota importante:** cada `trim` empieza el reloj en cero otra vez, por eso hay que poner `setpts`
después de cada uno. Si lo olvidas, el resultado tiene congelados raros al principio de cada trozo.

---

## 4. El fotograma que se pierde: por qué acelerar puede verse a saltos

Un video a 30 fotogramas por segundo, acelerado a 2x, tira la mitad de los fotogramas: quedan 15
imágenes reales estiradas sobre 30. Si el plano tenía poco desenfoque de movimiento, eso se ve
**entrecortado**, como una animación barata.

Tres formas de que no pase:

1. **Graba a 60 fps lo que sabes que vas a acelerar.** A 2x, 60 fps se convierten en 30 fps reales:
   fluidez perfecta. Es el arreglo verdadero y es gratis: solo hay que acordarse al grabar.
2. **Acepta el saltito si es rápido.** Por encima de 3x, el ojo ya no espera fluidez, espera lapso de
   tiempo. Un time-lapse entrecortado se ve normal.
3. **Interpolación** (CapCut la llama *suavizado de fotogramas*, ffmpeg lo hace con `minterpolate`).
   Inventa fotogramas intermedios. Funciona bien con movimiento simple y **hace desastres con manos,
   espuma, humo y pelo**: derrite los bordes. Para un bar, donde todo es líquido y manos, casi nunca
   vale la pena.

```bash
ffmpeg -i entrada.mp4 -vf "setpts=PTS/2.0,minterpolate=fps=30:mi_mode=mci" \
  -an -c:v libx264 -crf 18 -pix_fmt yuv420p suave.mp4
```

Advertencia honesta: ese comando es **lento** (puede tardar más que el video mismo por varios) y hay
que revisar el resultado fotograma a fotograma antes de confiarse.

---

## 5. Cómo sobrevive el audio

Aquí está la parte que casi nadie explica y que separa un video acelerado que suena bien de uno que
suena a caricatura.

### Las tres decisiones posibles

**Decisión A — El audio se va.** El plano acelerado no lleva su sonido; encima va la música o la voz
de otro lado. **Es la decisión correcta el 80% de las veces** en un reel. Un plano de 2,5x sirviendo
cerveza no necesita su audio original: necesita la música pegando en el beat.

**Decisión B — El audio se acelera con corrección de tono.** Se usa cuando en ese plano alguien dice
algo que importa. Funciona bien hasta 1,8x; de ahí para arriba empieza a sonar procesado.

**Decisión C — El audio se queda a velocidad normal por debajo.** El video va a 3x, pero el ambiente
del bar (vasos, conversación, música del local) suena normal. Es el truco de sonido más elegante del
módulo: el ojo ve rápido y el oído oye tranquilo, y el resultado se siente *caro*. Requiere que el
audio no tenga que sincronizar con nada en pantalla.

### La aritmética de atempo

El filtro que acelera audio **sin volverlo ardilla** es `atempo`, y tiene un límite duro: solo acepta
valores entre **0,5 y 2,0**. Para ir más allá, se encadenan multiplicando.

| Velocidad que quieres | Cadena |
|---|---|
| 1,4x | `atempo=1.4` |
| 1,7x | `atempo=1.7` |
| 2,0x | `atempo=2.0` |
| 2,5x | `atempo=2.0,atempo=1.25` |
| 3,0x | `atempo=2.0,atempo=1.5` |
| 4,0x | `atempo=2.0,atempo=2.0` |
| 5,0x | `atempo=2.0,atempo=2.0,atempo=1.25` |
| 0,5x (lento) | `atempo=0.5` |
| 0,25x (lento) | `atempo=0.5,atempo=0.5` |

Multiplica los números de la cadena y tiene que darte tu velocidad. `2.0 × 1.25 = 2.5`. Si no da,
tu audio y tu video se van a desincronizar y lo vas a notar recién al final, que es lo peor.

Ejemplo completo a 2,5x con audio corregido:

```bash
ffmpeg -i entrada.mp4 -filter_complex \
  "[0:v]setpts=PTS/2.5[v];[0:a]atempo=2.0,atempo=1.25[a]" \
  -map "[v]" -map "[a]" -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

**Cada eslabón de la cadena degrada un poco.** Dos eslabones no se notan, tres empiezan a sonar
metálicos. Por eso a 4x y 5x la respuesta correcta casi siempre es la Decisión A: quítale el audio.

### El truco del tono bajado

Si aceleras a 1,5x–1,8x y la voz queda demasiado aguda aunque uses `atempo`, bájale un pelo el tono.
Media semitono es suficiente y no se nota:

```bash
ffmpeg -i entrada.mp4 -filter_complex \
  "[0:v]setpts=PTS/1.7[v];[0:a]rubberband=tempo=1.7:pitch=0.97[a]" \
  -map "[v]" -map "[a]" -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

`rubberband` hace tempo y tono en un solo filtro y suena mejor que `atempo` en voces, pero no viene en
todas las compilaciones de ffmpeg. Compruébalo con `ffmpeg -filters | grep rubberband`; si no está,
usa `atempo` y ya.

En CapCut esto es la casilla **"Tono"** dentro del panel de velocidad: si la dejas activada, mantiene
el tono original; si la desactivas, la voz se vuelve aguda. Para acelerar voz, activada siempre.

---

## 6. Velocidad y ritmo musical

Cuando el plano acelerado va sobre música, hay una jugada que multiplica el efecto: **ajustar la
velocidad para que el plano termine exactamente en un golpe**.

Cómo se hace sin herramientas:

1. Mira cuánto dura el hueco musical que tienes que llenar. Digamos de 4,0 a 5,6 segundos: 1,6 s.
2. Mira cuánto dura tu plano crudo: 4,1 s.
3. Divide: 4,1 ÷ 1,6 = 2,56. Esa es tu velocidad.
4. Ponla en 2,5x o 2,6x y ajusta el corte final unos fotogramas.

Ese "ajusta la velocidad al hueco, no el hueco a la velocidad" es la razón por la que tienes **49
velocidades distintas** y no cinco redondas. Los números raros (1,73x, 2,4x, 3,1x) son señal de que
estás editando contra la música, que es exactamente lo correcto. No las redondees por prolijidad.

---

## 7. Lo que la velocidad no arregla

Sé honesto con estos tres casos, porque acelerar los empeora:

- **Una toma mal encuadrada.** A 2x sigue mal encuadrada, y ahora además pasa rápido y confunde.
- **Una toma movida o desenfocada.** Acelerar multiplica el temblor. Lo que era incómodo se vuelve
  ilegible.
- **Un plano sin contenido.** Si no pasa nada, acelerarlo produce nada más rápido. Bórralo.

Y un cuarto que es de estilo: **si todo tu video está acelerado, nada está acelerado.** La velocidad
funciona por contraste. Un reel donde el 100% va a 2x se siente uniforme y raro. La proporción que
funciona es más o menos: 60% velocidad normal, 30% acelerado, 10% momento frenado.

---

## Errores comunes

1. **Acelerar un plano que no tiene contenido.** Produce nada, más rápido. Bórralo.
2. **Encadenar mal `atempo`.** Si los números no multiplican a tu velocidad, el audio se desincroniza y
   lo descubres al final.
3. **Un solo `atempo` para más de 2x.** El filtro lo rechaza o lo recorta. Hay que encadenar.
4. **Tres o más eslabones de `atempo`.** Suena metálico. A esa velocidad, quítale el audio.
5. **Desactivar la corrección de tono al acelerar voz.** Queda ardilla. En CapCut, casilla "Tono"
   activada.
6. **Acelerar cámara en mano por encima de 3x.** Marea de verdad, no es exageración.
7. **Rampa con la V muy angosta.** Bajar y subir en 0,2 s se lee como error técnico, no como estilo.
8. **Poner la bajada de la rampa encima del momento.** Va medio segundo *antes*: el ojo necesita
   alcanzar a frenar.
9. **Usar los presets de curva de CapCut sin mover nada.** Ponen el frenazo donde el preset quiso, no
   donde está tu momento.
10. **Olvidar `setpts` después de cada `trim` en una rampa por código.** Salen congelados al principio
    de cada trozo.
11. **Redondear las velocidades para que se vean prolijas.** 2,56x contra la música le gana a 2,5x
    prolijo. Los números raros son buena señal.
12. **Interpolar fotogramas en planos con manos, espuma o humo.** Los bordes se derriten. En un bar,
    casi nunca vale.
13. **Acelerarlo todo.** La velocidad funciona por contraste. Si todo va rápido, nada va rápido.
14. **No grabar a 60 fps lo que ya sabías que ibas a acelerar.** Es el arreglo gratis que se olvida
    siempre.

---

## Checklist

Antes de dar por buena la velocidad de un plano:

- [ ] El plano tiene **movimiento continuo** (por eso acelero) y no pausas muertas (que se cortan).
- [ ] La velocidad está justificada: sé qué quería lograr, no la puse por costumbre.
- [ ] Si hay voz que importa, la velocidad está **por debajo de 1,8x**.
- [ ] Si hay audio acelerado, la **cadena de `atempo` multiplica exactamente** a la velocidad del video.
- [ ] La **corrección de tono** está activada en toda voz acelerada.
- [ ] Si va por encima de 3x, decidí conscientemente **quitarle el audio** o dejar el ambiente a
      velocidad normal.
- [ ] Si es cámara en mano, no pasé de **2,5x–3x**.
- [ ] Si hice rampa, el frenazo empieza **medio segundo antes** del momento que quiero señalar.
- [ ] Si hice rampa, la V es **ancha**, no un bache.
- [ ] Revisé si el plano se ve **entrecortado**; si sí, decidí entre grabar a 60 fps la próxima,
      aceptarlo o interpolar.
- [ ] Si el plano va sobre música, la velocidad está calculada para **caer en el golpe**.
- [ ] El video completo tiene **contraste de ritmo**: no está todo acelerado.
- [ ] Revisé el resultado con audio, no solo en la línea de tiempo.

# 298 — Música con función dramática

El módulo `74` te enseñó a elegir un tema, cortarlo, hacerle loop y ponerlo a nivel. Este módulo es
sobre lo único que importa después: **qué hace la música por la historia**.

La pregunta que separa a un editor de alguien que le puso música a un video es esta:

> Si le quito la música, ¿el video cuenta lo mismo?

Si la respuesta es sí, la música no está haciendo nada. Está rellenando. Y una música que rellena es
peor que ninguna, porque ocupa espacio en la mezcla (`290`), obliga a pelear con la voz (`295`) y no
devuelve nada a cambio.

---

## Los cuatro trabajos de la música

Solo hay cuatro. Si tu música no está haciendo uno de estos, sobra.

**1. Fijar el tono en los primeros 2 segundos.** Antes de que se entienda una palabra, la música ya
dijo si esto es serio, divertido, urgente o caro. Es la información más rápida que tiene el video, y
llega antes que la imagen se procese.

**2. Sostener lo que la imagen no puede sostener sola.** Un plano de comida de 4 segundos sin voz y sin
música es incómodo. Con música es un respiro.

**3. Marcar la estructura.** Un cambio de música le dice al espectador "empezó otra parte" sin que nadie
lo anuncie. Es la puntuación del video.

**4. Empujar hacia el final.** La música que crece hacia el cierre es lo que hace que la gente se quede
los últimos 4 segundos, que son justo donde está el llamado a la acción.

Lo que la música **no** hace: no arregla un video aburrido, no reemplaza un buen guion, y no genera
emoción donde no hay nada. Un video sin historia con música épica es un video sin historia y ruidoso.

---

## La música tiene estados, no un nivel

El error conceptual más grande es pensar la música como "un fondo a −20 dB". La música tiene estados y
cambia entre ellos, y ese cambio **es** la función dramática.

| Estado | Nivel relativo | Cuándo |
|---|---|---|
| **Ausente** | silencio | antes de la entrada, y en el momento de énfasis |
| **Presente** | −6 a −9 dB | cuando nadie habla: intro, transición, cierre |
| **Debajo** | −20 a −24 dB | mientras hay voz |
| **Retirada** | −28 a −32 dB | en el dato importante: el precio, la promesa, el remate |
| **Muda** | silencio total | 300–600 ms antes del golpe |

Un reel de 30 segundos bien mezclado pasa por **cuatro o cinco estados**. Uno mal mezclado tiene un solo
nivel de principio a fin, y por eso se siente plano aunque la música sea buena.

---

## Cuándo entra la música: casi nunca en el segundo cero

Este es el ajuste que más cambia la sensación de una pieza, y cuesta cinco minutos.

**El instinto:** la música arranca en 00,0 junto con el video.

**Lo que funciona mejor:** la voz arranca primero, sola, y la música entra por debajo en el segundo 1,5
o 2, cuando la primera frase ya se entendió.

Por qué: en los primeros dos segundos el espectador está decidiendo si se queda. Si en ese momento le
llegan dos flujos de información (voz + música) tiene que repartir atención y la frase de apertura —
la más importante del video — pierde nitidez. Con la voz sola, esa frase entra limpia. Y cuando la
música aparece después, se percibe como que **algo empezó**, lo cual es una recompensa en sí misma.

```bash
# la música entra en el segundo 1,8, con un fundido de 0,8 s
ffmpeg -i musica_recortada.wav -af "
  adelay=1800|1800,
  afade=t=in:st=1.8:d=0.8:curve=qsin,
  volume=-21dB
" -c:a pcm_s24le 02_MUSICA.wav
```

La excepción, y es real: **si el video abre con imagen y sin voz** (un plano de producto, un logo, un
hook visual), la música sí entra en 00,0 y manda. En ese caso es ella la que fija el tono.

---

## El silencio: el recurso más poderoso y el más barato

Callar la música durante medio segundo antes de un momento importante hace más que cualquier efecto de
sonido que puedas comprar.

Funciona porque el oído está adaptado al nivel general. Cuando el fondo desaparece, todo lo que queda
—una voz, un golpe— se percibe subjetivamente mucho más fuerte de lo que mide. Ganas presencia sin
gastar un solo decibelio de margen.

Los tres momentos donde el silencio siempre funciona:

**1. Antes del precio o del dato clave.** La música se calla 400 ms, la persona dice "diez mil pesos",
la música vuelve.

**2. Antes de un impacto o una revelación.** El silencio hace el golpe. El golpe sin silencio es la
mitad del golpe.

**3. En el corte final.** La música resuelve, corta seco, y quedan 300 ms de nada antes del logo. Es
la manera más elegante de terminar un video.

```bash
# hueco de silencio en la música entre 21,9 y 22,3, con rampas cortas para que no chasquee
ffmpeg -i 02_MUSICA.wav -af "
  volume=enable='between(t,21.9,22.3)':volume=0,
  afade=t=out:st=21.82:d=0.08,
  afade=t=in:st=22.3:d=0.12
" musica_con_silencio.wav
```

Dos advertencias que hacen la diferencia entre que suene profesional o a error:

- **Las rampas son obligatorias.** Un corte de música a cero sin rampa hace un clic audible. 80 ms
  entrando al silencio, 120 ms saliendo.
- **El hueco es corto.** 300–600 ms. Un segundo entero de silencio ya no es un recurso: es un bache, y
  el espectador cree que se dañó el video.

---

## Sincronizar con la estructura: el mapa musical

La música debe cambiar de estado **exactamente** donde cambia la historia. No cerca: exactamente.

Toma la estructura narrativa de tu pieza (bloque 3: `30`–`39`) y escribe al lado el estado musical:

```
REEL CALCULADORA DE COSTOS — 28 s

seg     ESTRUCTURA                     MÚSICA
────────────────────────────────────────────────────────────────
00,0    hook: "no sabes cuánto ganas"  AUSENTE  (voz sola, entra limpia)
01,8    sigue el hook                  entra, -21 dB, fade 0,8 s
04,2    problema: la cuenta mal hecha  DEBAJO, -22 dB
11,5    giro: "hay una manera"         cambia de sección + sube a -17 dB
                                       durante 1,2 s, luego vuelve a -22
17,0    solución: la calculadora       DEBAJO, -20 dB
21,9    MUDA 400 ms                    silencio
22,3    el precio: "diez mil"          RETIRADA, -30 dB
25,0    cierre + logo                  PRESENTE, sube a -8 dB, resuelve
27,6    último tiempo fuerte           corte seco
```

Ese mapa es la mitad del trabajo. La otra mitad es traducirlo a comandos, y con `volume=enable` y
`afade` sale directo.

El punto clave está en el segundo 11,5: la música **cambia de sección** en el giro de la historia. Ese
es el mayor lujo que puedes darle a un video de 28 segundos, y solo cuesta elegir bien qué tramo del
tema usas. Ver abajo.

---

## Elegir el tramo del tema según lo que necesitas

Un tema de música tiene partes con energías distintas. La mayoría de la gente usa los primeros 30
segundos porque son los primeros. Casi siempre es la peor elección: el principio de un tema suele ser
la introducción, la parte más vacía.

| Lo que necesitas | Qué tramo del tema tomar |
|---|---|
| Que crezca hacia el final | el tramo que **entra al coro**: el pre-coro + el coro |
| Que sostenga sin llamar la atención | una **estrofa**, no el coro |
| Que tenga un cambio en la mitad | el punto donde el tema **cambia de sección** |
| Que resuelva al final | los **últimos 6 segundos** del tema, donde cierra |

Cómo encontrar los puntos de cambio sin abrir un editor:

```bash
# forma de onda del tema completo: los cambios de sección se ven como escalones
ffmpeg -i tema.mp3 -lavfi showwavespic=s=1600x300:colors=white tema_onda.png

# y el espectrograma: los cambios de instrumentación se ven como cambios de color
ffmpeg -i tema.mp3 -lavfi showspectrumpic=s=1600x400:legend=1 tema_espectro.png
```

Miras la imagen, ves dónde cambia el escalón, y cortas ahí. Diez segundos de trabajo.

**La técnica del final invertido:** si necesitas que la música resuelva exactamente cuando termina tu
video de 28 segundos, no busques dónde empezar — calcula hacia atrás desde el final del tema.

```bash
# el tema resuelve en 2:14,5 (=134,5 s). Video de 28 s → arrancar en 106,5
ffmpeg -ss 106.5 -t 28 -i tema.mp3 -c:a pcm_s24le musica_que_resuelve.wav
```

Ahora tu música termina de verdad, con el acorde de cierre del compositor, en vez de con un fundido que
suena a "se acabó el video".

---

## Cortar en el tiempo fuerte

Cuando el video corta al mismo tiempo que la música marca un tiempo fuerte, el corte se siente
inevitable. Cuando cae entre tiempos, se siente accidental.

La matemática es simple: si el tema va a **120 BPM**, hay un tiempo cada **0,5 s** y un compás cada
**2 s**.

```
duración de un tiempo (s) = 60 / BPM
duración de un compás 4/4 = 4 × (60 / BPM)
```

| BPM | Un tiempo | Un compás |
|---|---|---|
| 90 | 0,667 s | 2,667 s |
| 100 | 0,600 s | 2,400 s |
| 120 | 0,500 s | 2,000 s |
| 128 | 0,469 s | 1,875 s |
| 140 | 0,429 s | 1,714 s |

Con el primer tiempo fuerte en, digamos, 0,42 s y el tema a 120 BPM, los tiempos fuertes de compás caen
en 0,42 · 2,42 · 4,42 · 6,42... Los cortes importantes del video van ahí.

No todos los cortes: **los importantes**. Un video donde cada corte cae en el beat se vuelve mecánico y
cansa. Los cambios de sección y el remate final en el beat; el resto donde la historia mande. Bloque 2
(`20`–`29`) tiene el detalle del ritmo.

---

## Cuándo NO poner música

Es una decisión legítima y a veces la correcta:

- **Testimonio de un cliente real.** La música mete producción donde lo que vende es la falta de
  producción. Un testimonio con música épica se lee como comercial y pierde credibilidad.
- **Contenido de autoridad / explicativo.** Si estás enseñando algo, la música compite con la atención.
- **Cuando el sonido real es mejor.** El chisporroteo de una plancha, el chorro de una cerveza. Ver
  `77`. Poner música encima de eso es tapar tu mejor activo.
- **Cuando el video ya va lleno.** Voz + subtítulos + motion + efectos + música es demasiada
  información. Algo tiene que ceder.

En esos casos el video **no va en silencio**: va con ambiente (`296`). Sin música, el ambiente pasa a
ser el único pegamento y su nivel puede subir a −28 dB.

---

## Errores comunes

1. **Música que rellena.** Si quitarla no cambia nada, sobra. Es la prueba de una línea.
2. **Un solo nivel todo el video.** La música tiene estados; si no cambia nunca, no está contando nada.
3. **Entrar en el segundo 0 cuando hay voz.** La frase de apertura pierde nitidez justo donde se decide
   si se quedan.
4. **Terminar con fundido.** Suena a "se acabó el video". Busca el tramo donde el tema **resuelve** y
   córtalo ahí.
5. **Usar los primeros 30 segundos del tema.** Casi siempre es la introducción, la parte más vacía.
6. **Silencio sin rampas.** Un corte a cero hace clic. 80 ms de salida, 120 ms de entrada.
7. **Silencio demasiado largo.** Más de 700 ms se lee como error técnico, no como recurso.
8. **Cortar todos los planos en el beat.** Se vuelve mecánico y cansa. Solo los importantes.
9. **Música épica en un testimonio.** Le quita la credibilidad que era el punto entero de usar un
   testimonio.
10. **Cambiar de tema a mitad del video.** Salvo que la estructura lo pida claramente, se siente a
    parche. Mejor cambiar de sección del mismo tema.
11. **Que la música no baje en el dato clave.** El precio, el teléfono, la promesa: ahí la música se
    retira a −30 dB o se calla.
12. **Elegir la música al final.** La música se elige antes de montar, porque el ritmo del montaje debe
    salir de ella.
13. **Usar música sin verificar derechos.** Ver `78`; Instagram no lee licencias, lee huellas digitales.

---

## Checklist

- [ ] Se hizo la **prueba de la línea**: si quito la música, ¿cambia algo? Si no, sobra.
- [ ] La música está haciendo **uno de los cuatro trabajos** (tono, sostén, estructura, empuje).
- [ ] Existe un **mapa musical escrito** con el estado de la música en cada tramo.
- [ ] La música pasa por **al menos tres estados** distintos en la pieza.
- [ ] La música **entra después de la primera frase** (salvo que el video abra sin voz).
- [ ] Hay un **silencio de 300–600 ms** antes del momento clave, con rampas de 80/120 ms.
- [ ] La música **se retira a −28/−32 dB** en el dato importante (precio, promesa, contacto).
- [ ] El tramo elegido **resuelve** al final; no termina en fundido.
- [ ] Se calculó el **BPM** y los cortes importantes caen en tiempo fuerte.
- [ ] **No todos** los cortes están en el beat.
- [ ] La música se eligió **antes** de montar, no al final.
- [ ] Si se decidió no usar música, el video **sí lleva ambiente** (`296`).
- [ ] Los **derechos** están verificados y registrados (`78`).

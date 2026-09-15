# 291 — Jerarquía de la mezcla: quién manda en cada momento

En una mezcla siempre hay alguien al mando. Si no lo decides tú, lo decide el azar de los niveles y
suena a que nadie estaba manejando.

Este módulo es la respuesta concreta a "¿a cuántos dB pongo la música?". No es "bájala un poquito". Son
números, y se pueden verificar midiendo.

---

## La regla de un solo protagonista

En cualquier instante del video hay **un elemento al mando y todos los demás debajo**. No dos. No
"ambos importantes".

El oído humano puede seguir una sola línea de información a la vez. Cuando dos cosas compiten, no oyes
las dos: oyes ruido y te cansas. La sensación que la gente describe como "suena amateur" casi siempre es
esto: dos elementos peleando por el mando.

Los cuatro candidatos a mandar, en orden de autoridad natural:

| Rango | Elemento | Cuándo manda |
|---|---|---|
| 1 | **Voz** | siempre que haya alguien hablando. Sin excepción. |
| 2 | **Efecto puntual** | 0,2–1,5 s, y solo si subraya algo que se ve |
| 3 | **Música** | cuando nadie habla: intro, transición, cierre |
| 4 | **Ambiente** | nunca manda. Es el piso sobre el que caminan los demás. |

La voz gana siempre. Si la música es tan buena que te da pena bajarla, el problema es que el video
debería no tener voz ahí.

---

## La tabla de niveles: los números concretos

Todo se mide **relativo a la voz**. La voz es 0 dB de referencia: es el nivel al que quedó después de la
cadena del bloque 7 y no se vuelve a mover.

### Cuando hay voz (el estado por defecto del 80% de un reel)

| Elemento | Nivel relativo a la voz | RMS típico si la voz está a −16 dB |
|---|---|---|
| Voz | **0 dB** (referencia) | −16 dB |
| Música (con ducking activo) | **−20 a −24 dB** | −36 a −40 dB |
| Efecto puntual | **−8 a −12 dB** | −24 a −28 dB |
| Ambiente / room tone | **−34 a −42 dB** | −50 a −58 dB |

### Cuando NO hay voz (intro, transición, cierre)

| Elemento | Nivel relativo | Comentario |
|---|---|---|
| Música | **−6 a −9 dB** | sube, pero nunca al nivel de la voz |
| Efecto puntual | **−4 a −8 dB** | aquí sí puede brillar |
| Ambiente | **−30 a −38 dB** | sube un poco con la música |

### Momento de énfasis (el golpe, la revelación, el precio)

| Elemento | Nivel relativo | Comentario |
|---|---|---|
| Efecto | **−2 a −5 dB** | manda él, durante medio segundo |
| Música | **−16 dB o silencio** | se aparta o se calla (`298`) |
| Voz | silencio | si hay efecto al mando, nadie habla |

**Por qué la música con voz va 20 dB abajo y no 10.** A −10 dB la música se oye "bien" en audífonos y
tapa la voz en un parlante de celular, que comprime el rango dinámico. A −20 dB con ducking activo la
música se percibe presente en audífonos y sigue debajo en el celular. La diferencia entre un reel que se
entiende y uno que no suele estar en esos 10 dB.

---

## Cómo se aplica esto en ffmpeg

Los niveles relativos se traducen directo a filtros `volume` sobre cada pista.

```bash
ffmpeg \
  -i voz.wav -i musica.wav -i ambiente.wav -i fx_impacto.wav \
  -filter_complex "
    [0:a] volume=0dB                                    [voz];
    [1:a] volume=-20dB                                  [mus];
    [2:a] volume=-38dB                                  [amb];
    [3:a] adelay=18500|18500, volume=-9dB               [fx];
    [mus][voz] sidechaincompress=
        threshold=0.05:ratio=8:attack=15:release=350    [mus_d];
    [voz][mus_d][amb][fx] amix=inputs=4:duration=longest:normalize=0 [out]
  " \
  -map "[out]" -c:a pcm_s24le mezcla.wav
```

`normalize=0` es obligatorio. Sin él, `amix` divide entre 4 y toda la mezcla baja 12 dB.

---

## El mapa de mando: la herramienta que hace la diferencia

Antes de tocar un fader, escribe quién manda en cada tramo. Treinta segundos de video se resuelven en
seis líneas.

```
REEL RESTAURANTE — 28 s
────────────────────────────────────────────────
00,0 – 01,8   MÚSICA         intro, -7 dB, nadie habla
01,8 – 02,0   EFECTO         whoosh de entrada, -10 dB
02,0 – 11,4   VOZ            música a -22, ambiente a -38
11,4 – 12,0   EFECTO         impacto en el corte al plato, -6 dB
                             música baja a -30 durante 0,6 s
12,0 – 21,8   VOZ            música vuelve a -22
21,8 – 22,2   SILENCIO       música muda 400 ms antes del precio
22,2 – 25,0   VOZ            precio. música a -26, más abajo que antes
25,0 – 28,0   MÚSICA         cierre, sube a -6, resuelve
```

Este mapa hace tres cosas que ningún fader hace solo:

1. **Te obliga a decidir**, en vez de "ir viendo". Casi siempre, al escribirlo, descubres dos momentos
   donde tenías dos protagonistas a la vez.
2. **Se convierte en el comando.** Cada línea es un `volume=enable='between(t,a,b)'` o un `adelay`.
3. **Se puede revisar sin oír.** Si en el mapa hay dos elementos al mando en el mismo tramo, ya sabes
   dónde está el problema.

---

## Automatización por tramos: cuando el ducking no basta

El `sidechaincompress` (bloque `75`) es automático y resuelve la conversación general. Pero hay momentos
donde quieres una decisión **artística**, no automática: la música baja porque tú lo dices, no porque
haya voz.

```bash
# la música baja a -30 dB entre el segundo 11,4 y el 12,0 (el impacto manda)
# y baja a -26 dB desde el 22,2 (el precio manda)
ffmpeg -i musica.wav -af "
  volume=-22dB,
  volume=enable='between(t,11.4,12.0)':volume=-8dB,
  volume=enable='gte(t,22.2)':volume=-4dB
" musica_automatizada.wav
```

Los `volume` se **multiplican** en cadena: −22 dB base, y en el tramo del impacto entran −8 dB más
(total −30 dB). Es la manera más simple de escribir automatización en ffmpeg sin volverse loco.

Para rampas suaves en vez de saltos secos, usa fundidos encadenados:

```bash
# bajar suavemente en 0,3 s antes del segundo 22,2 y quedarse abajo
ffmpeg -i musica.wav -af "
  volume=-22dB,
  afade=t=out:st=21.9:d=0.3:curve=qsin,
  volume=enable='gte(t,22.2)':volume=0.25
" musica_rampa.wav
```

Un salto seco de más de 6 dB se oye como un error. Rampa de 0,25–0,5 s y desaparece.

---

## El caso especial: cuando la jerarquía se invierte a propósito

Hay tres momentos, y solo tres, donde la música puede pasar por encima de la voz:

**1. La voz se vuelve textura.** Si hay una frase que no necesitas que se entienda (gente de fondo,
alguien riéndose, la persona hablando mientras el texto en pantalla dice lo importante), esa voz deja de
ser voz y pasa a ser ambiente. Nivel: −25 a −35 dB.

**2. El momento emocional sin palabras.** El final de un video donde el plano habla solo. La música sube
a −4 dB y nadie dice nada. Dura 2–4 segundos, no más.

**3. El remate rítmico.** La música cierra en un tiempo fuerte y el video corta ahí. La música manda el
último medio segundo. Ver `298`.

En los tres casos la inversión **es una decisión escrita en el mapa**, no un accidente.

---

## Verificar la jerarquía con números, no con el oído cansado

El oído se adapta y te miente después de veinte minutos. Mide.

```bash
# medir el RMS de cada stem por separado (con el nivel de mezcla ya aplicado)
for s in voz musica ambiente; do
  echo "--- $s ---"
  ffmpeg -i ${s}_nivelado.wav -af astats=metadata=1 -f null - 2>&1 \
    | grep "RMS level dB" | head -1
done
```

Debe salir algo así:

```
--- voz ---       RMS level dB: -16.4
--- musica ---    RMS level dB: -37.1     (20,7 dB debajo — correcto)
--- ambiente ---  RMS level dB: -54.8     (38,4 dB debajo — correcto)
```

Si la música te sale a −24 dB RMS (solo 8 debajo de la voz), tienes el problema clásico y ya sabes
cuánto bajar exactamente: 12 dB más.

Y la prueba de escucha que sí funciona:

```bash
# escuchar solo lo que sobrevive a volumen bajo: si oyes la música, la jerarquía está mal
ffmpeg -i mezcla.wav -af "volume=-26dB" prueba_bajito.wav
```

---

## Tabla rápida por tipo de pieza

| Tipo de pieza | Música bajo voz | Ambiente | Efectos |
|---|---|---|---|
| Reel de venta / anuncio | −20 a −22 dB | −38 dB | −8 a −10 dB |
| Testimonio / entrevista | −24 a −28 dB | −34 dB | casi ninguno |
| Video de producto sin voz | música manda (−6 dB) | −30 dB | −4 a −8 dB |
| Tutorial / explicativo | −26 dB o sin música | −40 dB | −12 dB, sutiles |
| Comercial de TV / marca | −18 dB (música protagonista) | −36 dB | −6 dB |
| Podcast en video | −28 dB, solo intro/outro | no | no |

En testimonios la música va más abajo porque la credibilidad depende de que se oiga cada palabra. En
comerciales de marca sube porque la emoción la carga la música.

---

## Errores comunes

1. **No decidir quién manda.** Si no escribiste el mapa, tienes dos protagonistas en algún tramo y no lo
   sabes.
2. **Música a −10 dB "porque suena bien en audífonos".** En un parlante de celular esa música tapa la
   voz. −20 dB con ducking es el punto.
3. **Bajar la música sin ducking.** Un nivel fijo suena a nivel fijo: alto en los silencios y bajo en el
   énfasis. Fijo + ducking, no uno u otro (`75`).
4. **Ambiente demasiado alto.** Por encima de −30 dB deja de ser pegamento y se vuelve ruido.
5. **Efectos al mismo nivel que la voz.** Un efecto a 0 dB relativo asusta y suena a error. −8 a −12 dB.
6. **Saltos secos de nivel.** Más de 6 dB de golpe se oye como falla. Rampa de 0,3 s.
7. **Olvidar `normalize=0` en `amix`.** Tu jerarquía queda perfecta y toda la mezcla sale 12 dB abajo.
8. **Subir la voz en vez de bajar lo demás.** Te comes el techo y la jerarquía sigue igual de mala.
9. **Mantener el mismo nivel de música todo el video.** La música tiene estados, no un valor (`298`).
10. **Juzgar la jerarquía después de 40 minutos mezclando.** El oído ya se acostumbró a lo mal que está.
    Mide con `astats`.
11. **Poner la voz de fondo al mismo nivel que la voz principal.** Si no es lo importante, va a −30 dB o
    se corta.
12. **Aplicar la tabla sin pensar en el tipo de pieza.** Un testimonio y un comercial no llevan el mismo
    balance.

---

## Checklist

- [ ] Existe un **mapa de mando escrito** con los tramos y quién manda en cada uno.
- [ ] En **ningún tramo hay dos protagonistas** al mismo tiempo.
- [ ] La **voz es 0 dB de referencia** y su nivel no se movió durante la mezcla.
- [ ] Música bajo voz entre **−20 y −24 dB** relativos (más abajo en testimonios).
- [ ] Ambiente entre **−34 y −42 dB** relativos; nunca manda.
- [ ] Efectos puntuales entre **−8 y −12 dB**; solo el de énfasis sube a −4.
- [ ] La música **sube cuando nadie habla** y no se queda plana todo el video.
- [ ] Todo cambio de nivel mayor a 6 dB tiene **rampa de al menos 0,25 s**.
- [ ] `amix` lleva **`normalize=0`**.
- [ ] Se **verificó con `astats`** que la separación real coincide con la planeada.
- [ ] Se hizo la **prueba a volumen bajo**: lo que sobrevive es la voz.
- [ ] Las inversiones de jerarquía (música por encima) son **decisiones escritas**, no accidentes.

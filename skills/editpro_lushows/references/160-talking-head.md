# 160 — Talking head

**Qué resuelve:** una persona hablando a cámara. Es el 70% de lo que se graba en el mundo y el formato
más difícil de hacer entretenido, porque **no pasa nada**: un plano fijo, una boca moviéndose, y el
espectador con el dedo listo. Este módulo es cómo se monta eso para que se vea vivo — y sobre todo cómo
se salva a alguien que no es presentador.

> **Término nuevo — talking head:** literalmente "cabeza que habla". Plano de una persona dirigiéndose a
> la cámara o a un entrevistador, sin acción ni escenografía que cargue la atención. La información va
> toda por la voz.

---

## 1. La verdad incómoda del formato

En un talking head **el montaje no puede crear información que no está en el audio**. Si la persona dijo
algo aburrido, ningún punch-in lo arregla. Por eso el orden de trabajo es rígido y no se salta:

```
1. Transcribir todo            → 13-transcribir-y-marcar.md
2. Montar el AUDIO primero     ← aquí se define el video entero
3. Recién ahí, tapar los cortes con imagen
4. Texto, color, sonido
```

**Se monta con los oídos.** Si al escuchar el corte de audio con los ojos cerrados la cosa se cae, el
video está muerto y ninguna capa visual lo salva. Eso es lo que se llama **radio edit**: el corte de
audio solo, sin imagen. Es el entregable intermedio real de este formato.

### Cuánto se bota

Regla de campo: de 10 minutos de alguien hablando salen entre **60 y 100 segundos** usables. Si estás
usando más del 25% del bruto, casi seguro no cortaste suficiente.

| Bruto grabado | Corte final sano | Ratio |
|---|---|---|
| 3 min | 45–60 s | 3:1 – 4:1 |
| 10 min | 90–120 s | 5:1 – 7:1 |
| 30 min (charla) | 5–7 min | 5:1 |

---

## 2. El radio edit: cómo se corta el audio

Trabajas sobre la transcripción con timecodes, no sobre la línea de tiempo. Marcas en el texto:

- `[FUERA]` — divagación, repetición, la persona se perdió
- `[JOYA]` — la frase que sí, la que da el gancho o el remate
- `[MULETILLA]` — "eh", "este", "o sea", "¿me entiendes?"
- `[RESPIRO]` — pausa que hay que acortar pero no matar

Después reordenas. **Sí, puedes reordenar.** El orden en que la persona dijo las cosas casi nunca es el
orden en que se entienden. Lo habitual:

```
Lo que grabó:     contexto → contexto → dato fuerte → ejemplo → conclusión
Lo que se monta:  dato fuerte → ejemplo → contexto mínimo → conclusión
```

El gancho casi siempre está en el minuto 4, no en el 0. Ver `12-mineria-del-material.md`.

> **Límite ético:** reordenar sí, cambiar el sentido no. Si juntas dos frases que no iban juntas y la
> persona termina diciendo algo que no dijo, eso es manipulación, no montaje. Ver `197-etica-del-montaje.md`.

---

## 3. Quitar muletillas sin que se note

Este es el trabajo fino del formato. Una muletilla suelta no molesta; ocho en 40 segundos matan al video.

### Dónde cortar exactamente

No cortes "eh" pegado a la palabra. Cortas **desde el final del sonido anterior hasta el inicio del
sonido siguiente**, dejando 40–80 ms de aire. Si cortas al ras, la voz suena mecánica y "picada".

```
mal:   ...quiero |eh| decir...      → corte pegado, suena a robot
bien:  ...quiero  ‹40ms›  decir...  → suena natural
```

### Qué muletillas NO se quitan

- La que va **antes de una idea difícil** — es una pausa de pensamiento y da credibilidad
- La risa nerviosa cuando cuenta algo personal
- El "¿sí me entiendes?" cuando es el sello del personaje (a veces ES la marca)

### Cómo detectarlas rápido con ffmpeg

Los silencios te dan el mapa de dónde vive cada muletilla:

```bash
# Lista todos los silencios de más de 0,25 s bajo -32 dB
ffmpeg -i entrevista.mp4 -af silencedetect=noise=-32dB:d=0.25 -f null - 2> silencios.txt
```

Ese `silencios.txt` trae pares `silence_start` / `silence_end`. Las muletillas casi siempre viven pegadas
a esos bordes. Cruza esa lista con la transcripción y tienes tu hoja de cortes.

### Acortar todas las pausas de golpe (primer pase, no el definitivo)

```bash
# Deja máximo 0,35 s de silencio y baja el resto del aire
ffmpeg -i habla.mp4 -af "silenceremove=stop_periods=-1:stop_duration=0.35:stop_threshold=-34dB" \
  -c:v copy salida_apretada.mp4
```

⚠️ Esto **corta solo audio** y desincroniza la imagen. Sirve para oír cómo quedaría el ritmo, no para
entregar. El corte real se hace con la lista de cortes medida (ver `15-medicion-exacta-de-cortes.md`).

---

## 4. El jump cut: el corte que este formato inventó

> **Término nuevo — jump cut:** cortar dentro del mismo plano. La persona "salta" de una posición a otra
> porque quitaste el pedazo del medio. En cine es un error; en talking head moderno es el lenguaje.

Antes se tapaban todos. Hoy **se dejan a la vista a propósito**: comunican "esto está editado, vamos al
grano" y suben el pulso. Lo que no se perdona es el jump cut **feo**: cuando la persona salta 30 cm de
lado o cambia de mano el micrófono.

### Escala de disimulo

| Salto | Qué hacer |
|---|---|
| La cabeza casi no se movió | Déjalo duro. Se lee como energía. |
| Se movió un poco (hombros) | Punch-in del 15% en el segundo trozo → `22` |
| Se movió mucho / cambió de postura | Tápalo con b-roll o con un plano de texto |
| Cambió la luz (nube, otra hora) | No se pega. Emparejar color primero → `62` |

### Punch-in alternado: la técnica base

Con **un solo plano fijo** creas tres cámaras:

```
A = encuadre original
B = punch-in 15% centrado
C = punch-in 22% descentrado (la cara hacia un tercio, aire al otro lado)
```

Y alternas `A → B → A → C → B` cada 4–8 segundos. Nunca dos punch-ins seguidos del mismo valor: se lee
como error de render, no como cámara.

```bash
# Punch-in 15% en vertical 1080x1920, del segundo 12,4 al 18,9
ffmpeg -i plano_A.mp4 -ss 12.4 -to 18.9 \
  -vf "scale=1242:2208,crop=1080:1920:81:144" \
  -c:a copy trozo_B.mp4
```

El `crop` lleva `x:y`. Centrado sería `(1242-1080)/2 = 81` y `(2208-1920)/2 = 144`. Para el descentrado C
mueves la `x` unos 60–120 px hacia donde la persona mira **menos**, para dejarle aire de mirada.

---

## 5. B-roll: cuánto y dónde va

> **Término nuevo — b-roll:** imágenes de apoyo que no son la persona hablando. Se ponen encima mientras
> la voz sigue.

El error de todos: meter b-roll bonito donde no hace falta y dejar desnudo el momento donde sí.

### Las cuatro razones válidas para poner b-roll

1. **Tapar un corte** que quedó feo
2. **Mostrar lo que dice** — dijo "esta libreta", se ve la libreta
3. **Bajar la carga** — llevas 20 s de cara y el ojo se cansa
4. **Marcar un cambio de tema** — el b-roll funciona como punto y aparte

Si no es una de esas cuatro, **no va**. B-roll decorativo es ruido caro.

### Duración

| Tipo | Duración en pantalla |
|---|---|
| Tapar un corte | 0,8 – 1,5 s |
| Ilustrar un objeto | 1,5 – 2,5 s |
| Marcar cambio de bloque | 2 – 3 s |
| Nunca | más de 4 s sin volver a la cara |

**Regla del regreso:** vuelves a la cara antes de que el espectador se pregunte dónde quedó la persona.
En vertical eso es ~3 s.

### La entrada del b-roll

Entra **0,2–0,4 s antes** de que la voz nombre la cosa, no después. Si dice "mi libreta" en el segundo
10,0, el plano de la libreta entra en 9,7. Al revés se siente lento y explicativo.

---

## 6. Cuando la persona NO es presentador

El caso real: el dueño del negocio, el chef, el contador. Lee tieso, mira al lado, se traba. Aquí es
donde el editor gana el sueldo.

| Problema del bruto | Solución de montaje |
|---|---|
| Lee de un papel / teleprompter y se le nota | Cortar en cada frase y alternar encuadre; el jump cut rompe la cadencia de lectura |
| Habla monótono | Cortar TODAS las pausas a 0,25 s; el ritmo lo pone el corte, no la voz |
| Se traba y se ríe | **Deja la risa.** Es lo más humano del bruto y a veces es el gancho → `34` |
| Mira fuera de cámara | Usa esos trozos con b-roll encima; solo deja a cámara los momentos donde sí mira |
| Voz baja, sin energía | Compresión más agresiva + subir presencia 3 kHz → `72`, `73` |
| Dijo la idea buena en 4 pedazos separados | Reordenar y pegar con punch-in en cada empalme |
| No hay gancho | Sacar la frase más fuerte del minuto 5 y ponerla de arranque, aunque quede fuera de contexto |

### Truco: el arranque prestado

Si el primer segundo no existe en el bruto, se fabrica: pones la frase más fuerte del video como
apertura (2–3 s), cortas a negro o a un texto, y arrancas la introducción real. Es honesto — la persona
lo dijo — y sube retención sin inventar nada.

### Truco: cubrir el 40% con texto

Si el material es visualmente pobre, el texto en pantalla se vuelve el b-roll. Un dato en pantalla grande
sobre fondo de color de marca durante 1,5 s hace el mismo trabajo que un plano de apoyo y no cuesta nada.
Ver `40-texto-como-canal-principal.md`.

---

## 7. Texto en pantalla para talking head

- **Subtítulos siempre.** Este formato se consume sin sonido más que ningún otro.
- 2–4 palabras por golpe en vertical, frase completa en horizontal → `46`
- **Resalta la palabra que carga el sentido**, no la que suena bonito
- Los datos duros (precios, porcentajes, años) van SIEMPRE también en texto: el oído no retiene números

```bash
# Quemar subtítulos ASS ya sincronizados
ffmpeg -i corte.mp4 -vf "ass=subs.ass" -c:a copy final.mp4
```

---

## 8. Montaje de audio: lo específico del formato

El talking head vive o muere en la voz. La cadena completa está en `70-cadena-de-voz-profesional.md`,
pero lo propio de este formato:

- **Ambiente continuo.** Al cortar tanto, el fondo salta. Se arregla poniendo debajo una capa constante
  de "room tone" (los 5 s de silencio de la sala) a -45 dB.
- **Nunca dejes silencio absoluto** en un empalme. Se lee como archivo dañado.
- **Música a -22 / -26 LUFS bajo la voz**, y con ducking → `75`
- La música **entra después del gancho**, no desde el frame 0. Arrancar con música tapa la primera frase.

```bash
# Sacar 5 s de room tone y tenerlo listo como cama
ffmpeg -i bruto.mp4 -ss 00:00:02 -t 5 -vn -af "volume=-6dB" roomtone.wav
```

---

## 9. Estructura tipo (vertical, 45–60 s)

```
0,0 – 1,2 s   Gancho: la frase más fuerte. Cara grande. Texto ya en pantalla.
1,2 – 3,0 s   Promesa / bucle abierto ("te voy a decir por qué...")
3,0 – 8,0 s   Contexto mínimo. Primer b-roll. Primer punch-in.
8 – 35 s      Cuerpo. Un cambio visual cada 1,5–2 s. Alterna A/B/C + b-roll.
35 – 45 s     Cierre del bucle. Vuelve a plano abierto (baja el pulso a propósito).
45 – 55 s     Remate y CTA. Texto fijo. Sin música nueva.
```

El bajón de pulso antes del cierre es deliberado: sin él, el CTA se pierde en el ruido.

---

## 10. Comprobación con hoja de contactos

Antes de dar por bueno el corte, saca la parrilla de fotogramas y míralo como imagen fija:

```bash
# 1 fotograma cada 2 s, en cuadrícula 5x4
ffmpeg -i corte_v1.mp4 -vf "fps=1/2,scale=320:-1,tile=5x4" contactos.png
```

Si en la parrilla ves **20 cuadros casi idénticos**, el video se siente estático aunque tú lo hayas
"editado". Ese es el diagnóstico más rápido que existe para este formato.

---

## Errores comunes

1. **Montar la imagen antes que el audio.** Terminas defendiendo un corte visual bonito sobre un discurso
   que no se sostiene. El radio edit va primero, siempre.
2. **No cortar suficiente.** El talking head es el formato donde más material sobra. Si te dolió botar,
   probablemente todavía falta.
3. **Quitar muletillas al ras.** El corte pegado a la palabra deja la voz metálica y "digital". Deja
   40–80 ms de aire.
4. **Punch-in siempre del mismo valor.** Si A y B tienen el mismo acercamiento en todos lados, deja de
   leerse como cámara y se lee como falla.
5. **Punch-in sobre fuente 1080p al 40%.** Se pixela. Con 1080p el techo sano es 25%; con 4K puedes ir a 60%.
6. **B-roll decorativo.** Playas, tecleo genérico, gente en oficina. No tapa nada, no ilustra nada, y le
   quita la cara al espectador que vino por la persona.
7. **B-roll que entra tarde.** Después de que se nombró el objeto. Se siente lento. Entra 0,2–0,4 s antes.
8. **Dejar el silencio real en los empalmes.** Sin room tone debajo, cada corte suena a "tac".
9. **Empezar con música desde el segundo 0.** Se come el gancho. La música entra en el segundo 2–3.
10. **Cambiar el sentido al reordenar.** Pegar dos frases que no iban juntas para que diga algo más
    vendedor. Eso ya no es edición.
11. **No emparejar color entre trozos grabados en momentos distintos.** Si media grabación es de las 3 pm
    y la otra de las 5, el jump cut te delata → `62`.
12. **Olvidar los subtítulos** porque "se entiende bien". Sin sonido no se entiende nada.

---

## Checklist

- [ ] Transcripción completa con timecodes hecha antes de tocar la línea de tiempo
- [ ] Radio edit escuchado con los ojos cerrados y aprobado
- [ ] Muletillas quitadas dejando 40–80 ms de aire; las que dan credibilidad se quedaron
- [ ] El gancho está en los primeros 1,2 s (aunque venga del minuto 5 del bruto)
- [ ] Al menos 3 encuadres distintos (A, B, C) alternando cada 4–8 s
- [ ] Ningún punch-in por encima del 25% si la fuente es 1080p
- [ ] Cada b-roll cumple una de las 4 razones válidas; ninguno pasa de 4 s
- [ ] Todo b-roll entra 0,2–0,4 s antes de que la voz nombre la cosa
- [ ] Room tone continuo debajo de todos los empalmes
- [ ] Música entra después del gancho y va con ducking bajo la voz
- [ ] Subtítulos quemados, dentro de zona segura → `45`
- [ ] Números y precios repetidos en texto en pantalla
- [ ] Hoja de contactos revisada: no hay 20 cuadros idénticos
- [ ] Color emparejado entre trozos de distinta hora de grabación
- [ ] Pasó `98-verificacion-del-corte.md`

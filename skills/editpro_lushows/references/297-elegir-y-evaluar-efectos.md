# 297 — Elegir y evaluar efectos de sonido

El módulo `76` te enseñó a **construir** efectos con ffmpeg desde su física. Este módulo te enseña a
**juzgarlos**, y empieza confesando que aquel experimento salió mal.

---

## El experimento y su resultado

Se sintetizaron 16 efectos de sonido con ffmpeg, cada uno construido desde la física del fenómeno:

- **Whoosh** = ruido rosa filtrado con un barrido de frecuencia y una envolvente de volumen.
- **Impacto** = una senoidal grave con decaimiento exponencial, más una capa corta de ruido para el
  ataque.
- **Riser** = un tono que sube de 200 a 1200 Hz durante 3 segundos con el volumen creciendo.
- **Clic de interfaz** = un tono corto de 90 ms con envolvente rápida.

Todos técnicamente correctos. La física está bien. Los comandos funcionan y hacen lo que dicen.

Después se evaluaron con un modelo capaz de escuchar audio de verdad, pidiendo una nota de 1 a 5.

**Resultado: 12 de los 16 sacaron nota 1 o 2.** Y los comentarios fueron todos parecidos:

> "suena plástico"
> "de juguete"
> "como un preset por defecto de los 90"
> "sintético, no tiene cuerpo"

Esa es la lección, y es incómoda porque contradice el instinto de cualquiera que sepa programar:

> **La física correcta produce algo técnicamente válido que suena barato.**
> Un buen efecto de sonido no es matemática. Es una **grabación** con capas y textura orgánica.

---

## Por qué un sonido sintetizado suena a juguete

Cinco razones concretas, y todas se pueden verificar mirando el espectrograma:

**1. Le falta suciedad.** Un impacto real es una madera golpeando otra madera: hay astillas, hay aire
desplazado, hay resonancia del piso, hay el crujido del objeto asentándose después. Una senoidal con
decaimiento tiene un tono y nada más. El cerebro sabe la diferencia porque nunca ha oído en el mundo
real un sonido con un solo componente.

**2. Es demasiado periódico.** La naturaleza no repite. Un whoosh real (una mano pasando frente a un
micrófono) tiene irregularidades constantes en la velocidad, en el ángulo, en la turbulencia. Un
barrido de filtro es matemáticamente suave y el oído lo lee inmediatamente como artificial.

**3. Le falta el transiente complejo.** Los primeros 5 milisegundos de un sonido son los que el cerebro
usa para identificar qué lo produjo. En un sonido real, esos 5 ms contienen decenas de eventos
diminutos. En uno sintético, contienen una rampa.

**4. No tiene sala.** Todo sonido real ocurre en algún lugar y trae las primeras reflexiones de ese
lugar. Un sonido sintético nace sin espacio y suena a "pegado encima" (es el mismo problema de la voz
seca de `294`).

**5. Es una sola capa.** Un efecto de biblioteca profesional típicamente tiene entre 3 y 8 capas
grabadas por separado: el ataque, el cuerpo, la cola, la textura, el sub-grave. Una fórmula genera una.

---

## El hallazgo raro: los 4 que sí sirvieron estaban mal nombrados

De los 16, cuatro sacaron buena nota. Y aquí está lo interesante: **ninguno de los cuatro era lo que su
nombre decía.**

| Nombre que tenía | Lo que en realidad sonaba | Nota |
|---|---|---|
| `whoosh-inverso` | chispas mágicas, brillo ascendente | buena |
| `golpe-seco` | un clic de interfaz, seco y corto | buena |
| `chispa` | un sub-grave, un golpe de pecho | buena |
| (el cuarto, igual) | algo distinto de su etiqueta | buena |

O sea: se intentó hacer un whoosh, salió mal como whoosh, y resultó ser un excelente efecto de chispas
mágicas. Se intentó un golpe seco, no golpeó, pero quedó un clic perfecto para una animación de
interfaz.

**La lección operativa, y es enorme:**

> Nombra los efectos por **lo que suenan**, no por **lo que quisiste hacer**.

Un archivo llamado `whoosh-inverso.wav` que suena a chispas te va a hacer perder tiempo cada vez que lo
busques, y te va a hacer descartar un archivo bueno porque "el whoosh no me sirvió". Escuchas tu
biblioteca, la renombras por su sonido real, y de repente tienes cuatro efectos buenos en vez de
dieciséis malos.

Esto aplica también a las bibliotecas compradas: los nombres los puso alguien que estaba pensando en el
uso previsto, no en el timbre. Renombra lo que uses seguido.

---

## El método de evaluación

Este es el procedimiento que reveló el problema, y sirve para cualquier efecto: sintetizado, comprado o
grabado.

### Paso 1 — Escucha a ciegas y describe

La pregunta correcta **no** es *"¿esto suena como un whoosh?"*. Esa pregunta le da la respuesta al que
evalúa y lo sesga: va a buscar razones para decir que sí.

La pregunta correcta es:

> **"¿A qué suena esto?"**

Sin contexto, sin el nombre del archivo, sin decir qué se intentó hacer. Si la respuesta coincide con tu
intención, el efecto funciona. Si la respuesta es otra cosa, tienes dos opciones: descartarlo, o
renombrarlo y usarlo para lo que de verdad es (que es lo que salvó a los cuatro del caso).

### Paso 2 — Nota de 1 a 5 con criterio explícito

| Nota | Significa |
|---|---|
| 5 | Suena grabado. Lo pondría en un anuncio de marca. |
| 4 | Sirve. No llama la atención por malo. |
| 3 | Pasa desapercibido si está bajo y corto. |
| 2 | Se nota sintético. Abarata la pieza. |
| 1 | Suena a juguete. No usar. |

**Umbral de uso: 4 o más.** Un efecto de nota 3 se puede colar si va muy bajo y dura 150 ms. Nota 2 o 1
no se usa nunca, porque el costo no es "suena regular": el costo es que **un efecto barato abarata toda
la pieza**. Un video con buena imagen, buena voz y un whoosh de juguete se lee como amateur completo.

### Paso 3 — Evaluar con un modelo que entiende audio

Esta es la parte moderna y la que hizo posible el hallazgo. A agosto de 2026, hay modelos que procesan
audio de forma nativa (no transcribiéndolo: **escuchándolo**). Gemini 2.5 con entrada de audio nativa es
el más accesible por API; se le manda el archivo y se le pide una descripción y una nota.

Por qué sirve, siendo honestos sobre sus límites:

- **Es rápido y consistente.** 16 efectos evaluados en un minuto, con el mismo criterio para todos. Un
  humano se cansa y se vuelve indulgente al octavo.
- **No tiene el sesgo del autor.** Tú acabas de escribir el comando y quieres que suene bien. El modelo
  no tiene nada invertido.
- **Detecta bien lo obvio.** "Suena sintético", "le falta cuerpo", "es un tono puro" — eso lo acierta.
- **No es un oído de oro.** No sustituye escuchar el efecto **dentro** de la pieza, que es donde de
  verdad se decide. Úsalo para filtrar, no para aprobar.

El flujo práctico: el modelo descarta lo malo (y en este caso descartó 12 de 16, correctamente); tú
escuchas los sobrevivientes en el contexto real del video.

Prepara los archivos para evaluar así:

```bash
# normalizar todos los candidatos al mismo nivel para que la comparación sea justa
mkdir -p eval
for f in fx_originales/*.wav; do
  ffmpeg -y -i "$f" -af "loudnorm=I=-16:TP=-1" -ar 48000 "eval/$(basename "$f")" 2>/dev/null
done
```

Si no los igualas, el más fuerte va a "sonar mejor" y estarás evaluando volumen, no calidad (`290`).

---

## Qué hace que un efecto suene caro

Lo que tienen los efectos que sacan 5, y que puedes buscar activamente cuando eliges de una biblioteca:

| Característica | Cómo se reconoce |
|---|---|
| **Capas** | se oyen al menos dos eventos: un ataque y un cuerpo con timbre distinto |
| **Textura irregular** | el ruido no es parejo; tiene granos, chasquidos, variación |
| **Cola natural** | no se apaga con una rampa: decae con la sala, irregularmente |
| **Contenido en todo el espectro** | mira el espectrograma: hay energía de 40 Hz a 16 kHz |
| **Origen físico identificable** | puedes decir con qué se hizo, aunque no sepas qué es |
| **Sala** | trae reflexiones, no nació en el vacío |

Compruébalo tú mismo, es rápido:

```bash
# espectrograma de un efecto sintético vs uno grabado
ffmpeg -i fx_sintetico.wav -lavfi showspectrumpic=s=900x400:legend=1 esp_sintetico.png
ffmpeg -i fx_grabado.wav   -lavfi showspectrumpic=s=900x400:legend=1 esp_grabado.png
```

El sintético se ve como una línea o una mancha limpia con bordes definidos. El grabado se ve como una
nube desordenada que llena el cuadro. **Esa nube desordenada es lo que suena caro.**

---

## Dónde conseguir efectos que sí sirven

| Fuente | Modelo | Para qué sirve |
|---|---|---|
| **Freesound** (freesound.org) | gratis; CC0, CC-BY o CC-BY-NC según el archivo | enorme, desigual; filtra por CC0 y por calidad de grabación |
| **Epidemic Sound** | suscripción; licencia directa global, música + SFX | lo más práctico para creadores de contenido |
| **Artlist** | suscripción; música + SFX | competencia directa de Epidemic |
| **Soundly** | versión gratuita + suscripción desde ~15 USD/mes | biblioteca en la nube con buen buscador |
| **BOOM Library** | compra por paquete, 96 kHz/24 bit | calidad de cine; caro y excelente |
| **Grabarlos tú** | gratis + tiempo | ver abajo |

**Sobre Freesound**, que es la opción gratis realista: cada archivo tiene su propia licencia. CC0 es uso
libre sin atribución. CC-BY exige acreditar. CC-BY-NC **prohíbe uso comercial** — y un reel que vende un
producto es uso comercial. Verifica archivo por archivo y guarda el enlace y la licencia en un registro
(`78` tiene el formato del registro).

**Grabarlos tú es más viable de lo que parece.** Con el celular y cinco minutos consigues cosas que
ninguna biblioteca tiene: el sonido real de tu producto, de tu local, de tu máquina. Y siempre suena
mejor que lo sintético, porque es una grabación. Módulo `77` completo sobre esto.

---

## Cuándo la síntesis SÍ funciona

No todo se descarta. Hay una familia de sonidos donde la síntesis gana, y son justamente los que no
existen en el mundo real:

**1. Sub-graves y drops.** Un golpe de 40 Hz que se siente en el pecho no es un objeto: es una onda. La
síntesis es la manera correcta de hacerlo.

```bash
# sub-grave de 1,2 s: 55 Hz bajando a 30 Hz con decaimiento
ffmpeg -f lavfi -i "sine=frequency=55:duration=1.2" -af "
  asetrate=48000*0.9, aresample=48000,
  volume='exp(-3.2*t)':eval=frame,
  afade=t=out:st=1.0:d=0.2
" -c:a pcm_s24le sub_drop.wav
```

**2. Tonos de interfaz y notificaciones.** Un beep de interfaz es sintético en la vida real también. La
síntesis es fiel.

**3. El silencio como efecto.** El recurso más barato y más poderoso: un hueco de 300 ms antes del golpe
(`298`).

```bash
ffmpeg -f lavfi -i "anullsrc=r=48000:cl=stereo" -t 0.3 -c:a pcm_s24le silencio_300ms.wav
```

**4. El ambiente.** Como se explica en `296`: el ambiente es ruido filtrado por definición, así que un
ambiente sintético es indistinguible de uno real. Es la excepción.

**5. Capas de refuerzo.** Un sub-grave sintético **debajo** de un impacto grabado le da peso sin que se
note lo sintético. Esa combinación es cómo se hacen los impactos de tráiler de cine:

```bash
# impacto grabado + sub sintético alineado en el mismo instante
ffmpeg -i impacto_grabado.wav -i sub_drop.wav \
  -filter_complex "[0:a]volume=0dB[a];[1:a]volume=-5dB,lowpass=f=90[b];
                   [a][b]amix=inputs=2:normalize=0[out]" \
  -map "[out]" impacto_con_peso.wav
```

Ese `lowpass=90` en el sub es clave: lo mantiene debajo del impacto real en vez de competir con él.

---

## Juzgar para el parlante que va a sonar, no para el que uno imagina

Este error costó descartar buen material y vale más que cualquier truco de este módulo.

Al evaluar 107 efectos de biblioteca con el modelo, **63 salieron con nota 2**. Los motivos se
repetían: *"le falta subgraves potentes"*, *"sin cuerpo en graves"*, *"ahuecado"*. Todos legítimos —
**para cine**. Pero el destino era un reel vertical que se oye en el **parlante de un celular**.

**Un parlante de celular no reproduce nada por debajo de ~300 Hz.** Un efecto con subgraves enormes
no suena potente ahí: no suena. Y al revés: un clic delgado y brillante, que en una sala de cine
sería pobre, en un celular es **la elección correcta** — es lo único que se abre paso por encima de
una voz que no para de hablar.

Al reevaluar con el destino real declarado en el prompt, el reparto cambia por completo. No porque
el modelo se ablande: porque por fin está midiendo contra el trabajo que el sonido tiene que hacer.

### El contexto que hay que declarar SIEMPRE

Un evaluador sin contexto usa por defecto el estándar de cine, porque es el que domina la
bibliografía. Si no se le dice dónde va a sonar, juzga para una sala. Hay que darle:

- **Qué parlante.** Celular, audífonos, TV, sala. Cambia todo el rango útil.
- **Qué compite.** ¿Va solo o debajo de una voz? ¿Hay música?
- **Cuánto dura en pantalla.** Un efecto de 0,3 s no se juzga como uno de 3 s.
- **A qué volumen se consume.** La mitad del público de redes lo ve a medio volumen.

### Y la trampa de la palabra "sintético"

*"Suena sintético"* no es un defecto por sí solo, y usarlo como si lo fuera bota material bueno. Un
tono de interfaz **es** sintético en la vida real; un beep grabado de un microondas también es un
beep. El defecto real es sonar **barato**: desafinado, con cola fea, con distorsión no buscada, o tan
genérico que se reconoce como el sonido que trae la plantilla.

La distinción exacta es esta:

| No es defecto | Sí es defecto |
|---|---|
| Ser sintético | Sonar desafinado |
| Ser delgado (si va en celular) | Tener una cola que no cierra |
| No tener graves | Distorsionar sin que sea a propósito |
| Ser corto | Reconocerse como preset de fábrica |

**Guarda siempre la evaluación anterior antes de reevaluar con otro criterio.** La comparación entre
las dos tandas enseña más que cualquiera de las dos por separado: muestra qué estabas botando y por
qué.

---

## El efecto no se alinea por el archivo: se alinea por el GOLPE

Esta es la diferencia entre un efecto que "está ahí" y uno que **aterriza**. Y es la razón número uno
por la que un montaje con efectos buenos igual se siente flojo.

Un efecto **grabado** casi siempre trae aire antes del golpe: el micrófono estaba abierto antes de que
pasara algo. Medido sobre efectos reales de biblioteca, ese aire va de 10 a 200 ms. Si arrastras el
archivo y lo pegas justo en el corte, el golpe suena **tarde**. Nadie sabe decir qué pasa; solo se
siente desincronizado.

**La regla:** el segmento no empieza en el corte. Empieza en `corte − aire`.

```
línea de tiempo:   ────────────┬────────────    el corte está aquí
archivo pegado ahí: [aire..... GOLPE ......]    ← el golpe suena tarde
archivo adelantado: [aire.....]GOLPE......]     ← correcto
                    ↑ empieza antes
```

### Medirlo, no estimarlo

Al modelo se le puede preguntar si un sonido convence — eso es juicio estético y lo hace bien.
Preguntarle en qué milisegundo cae el golpe es pedirle una precisión que no tiene. **El modelo opina,
ffmpeg mide.**

```js
// decodifica a 8 kHz mono y busca el ATAQUE: el primer punto que llega
// al 60% del pico. No el pico: en un riser con cola larga el pico está
// al final, y alinear por ahí sería peor que no alinear.
const raw = execFileSync('ffmpeg',
  ['-v','error','-i',f,'-ac','1','-ar','8000','-f','s16le','-'],
  { maxBuffer: 64*1024*1024 });

let max = 0;
for (let i = 0; i + 1 < raw.length; i += 2)
  max = Math.max(max, Math.abs(raw.readInt16LE(i)));

const umbral = max * 0.6;
let iAtaque = 0;
for (let i = 0; i + 1 < raw.length; i += 2)
  if (Math.abs(raw.readInt16LE(i)) >= umbral) { iAtaque = i / 2; break; }

const golpeSeg = iAtaque / 8000;   // cuánto hay que adelantar el segmento
```

8 kHz sobra: el ataque de un transitorio se ubica igual de bien y el archivo pesa seis veces menos.

### El caso borde que rompe el montaje

Si el golpe va en el segundo 0,05 del video y el efecto trae 0,2 s de aire, el segmento tendría que
empezar en **−0,15 s**. CapCut y la mayoría de editores **ignoran en silencio** un segmento con inicio
negativo: no da error, simplemente el sonido no aparece.

La salida correcta no es mover el golpe: es **recortar el aire de la cabeza del archivo**.

```js
let inicioLinea  = momento - golpeUs;
let inicioFuente = 0;
if (inicioLinea < 0) {
  inicioFuente = -inicioLinea;   // se corta ese aire del archivo
  inicioLinea  = 0;              // y el segmento arranca en cero
}
```

Mismo resultado audible, sin segmento fantasma.

### Por qué esto importa más de lo que parece

Un efecto de nota 3 bien alineado se siente mejor que uno de nota 5 desalineado. La sincronía es más
perceptible que el timbre. Si tienes que elegir dónde poner el esfuerzo, **alinea primero**.

---

## Organizar la biblioteca: el catálogo por sonido

Después de renombrar por lo que suenan, guarda los buenos en una biblioteca propia con esta estructura:

```
mi-biblioteca-fx/
├── impactos/
│   ├── impacto_madera_seco_grave.wav      [5] freesound 412093 CC0
│   ├── impacto_metal_con_cola.wav         [4] epidemic
├── transiciones/
│   ├── whoosh_tela_rapido.wav             [5] grabado propio 2026-07
│   ├── chispas_ascendente.wav             [4] sintetizado (era "whoosh-inverso")
├── interfaz/
│   ├── clic_seco_corto.wav                [4] sintetizado (era "golpe-seco")
├── sub/
│   ├── sub_drop_55a30.wav                 [5] sintetizado
└── LICENCIAS.txt
```

La nota entre corchetes en el nombre o en un `.txt` al lado. Cuando estés montando y necesites un
impacto, vas a `impactos/`, tomas el de nota 5, y no vuelves a evaluar nada. **Evaluar una vez, usar
cien veces.**

Y `LICENCIAS.txt` con una línea por archivo: fuente, enlace, licencia, fecha. El día que un cliente
grande te pida el respaldo, existe.

---

## Errores comunes

1. **Creer que la física correcta basta.** Es la lección del caso: 12 de 16 técnicamente válidos y
   sonando a juguete.
2. **Nombrar por la intención y no por el sonido.** Pierdes archivos buenos porque están mal etiquetados.
3. **Preguntar "¿suena como un whoosh?"** en vez de "¿a qué suena?". La primera pregunta sesga la
   respuesta.
4. **Evaluar efectos a distinto volumen.** El más fuerte gana siempre. Iguala a −16 LUFS antes de
   comparar.
5. **Usar un efecto de nota 2 "porque va bajito".** Un efecto barato abarata toda la pieza, aunque esté
   a −20 dB.
6. **Aprobar un efecto solo con el modelo.** El modelo filtra; la decisión final es escucharlo dentro de
   la pieza.
7. **Evaluar el efecto aislado y no en contexto.** Un efecto glorioso solo puede ser horrible sobre esa
   imagen.
8. **Sintetizar lo que se puede grabar.** Un golpe en una mesa lo grabas con el celular en 30 segundos y
   siempre gana.
9. **No verificar la licencia en Freesound.** CC-BY-NC prohíbe uso comercial, y tu reel de ventas es
   comercial.
10. **Una sola capa siempre.** Los efectos caros tienen 3–8 capas. Sumar un sub sintético debajo de un
    grabado es la manera barata de subir de categoría.
11. **No guardar los buenos en una biblioteca.** Vuelves a evaluar 16 efectos cada proyecto.
12. **Efecto sin sala sobre una escena con sala.** Suena pegado encima. Un toque de `aecho` lo aterriza
    (`294`).
13. **Poner efecto en cada corte.** Ver `76` y `209`: el efecto subraya, no acompaña. Si están todos
    subrayados, no hay nada subrayado.
14. **Pegar el archivo en el corte sin medir el ataque.** El error más caro de todos, porque no se ve
    en ninguna revisión: el efecto está, se oye, y aun así el montaje se siente flojo.
15. **Poner un segmento con inicio negativo.** El editor lo ignora sin avisar. Se recorta la cabeza
    del archivo, no se empuja el segmento fuera de la línea.
16. **Fiarse de la licencia "gratis" sin leerla.** Verificado 6-ago-2026: la de Mixkit permite uso
    comercial y pauta pagada, sin atribución, pero **prohíbe redistribuir los archivos sueltos**
    ("as stock, in a tool or template"). O sea: dentro de tu video sí, compartir la carpeta no.

---

## Checklist

- [ ] Cada efecto fue evaluado con la pregunta **"¿a qué suena?"**, sin decir qué se intentó hacer.
- [ ] Se declaró el **destino real** antes de evaluar: qué parlante, qué compite, cuánto dura en
      pantalla, a qué volumen se consume. Sin eso, el evaluador juzga para cine por defecto.
- [ ] Ningún efecto se descartó por **"le faltan graves"** cuando el destino es un celular.
- [ ] Ningún efecto se descartó por **"suena sintético"** a secas: el defecto real es sonar *barato*.
- [ ] Los candidatos se **igualaron en sonoridad** antes de compararlos.
- [ ] Cada efecto tiene una **nota de 1 a 5** y solo se usan los de **4 o más**.
- [ ] Los archivos están **nombrados por lo que suenan**, no por la intención original.
- [ ] Cada efecto se escuchó **dentro de la pieza**, no solo aislado.
- [ ] Se prefirió **grabar o comprar** antes que sintetizar, salvo en sub-graves, tonos de interfaz,
      ambiente y capas de refuerzo.
- [ ] Los impactos importantes tienen **al menos dos capas** (ataque grabado + sub).
- [ ] Se miró el **espectrograma**: los buenos llenan el cuadro, los sintéticos son una línea limpia.
- [ ] Cada efecto de biblioteca tiene su **licencia verificada** y anotada en `LICENCIAS.txt`.
- [ ] Ningún archivo con licencia **CC-BY-NC** se usó en una pieza comercial.
- [ ] Los efectos aprobados están guardados en una **biblioteca propia con su nota**.
- [ ] Los efectos llevan un mínimo de **sala** si la escena tiene sala.
- [ ] Se **midió el ataque** de cada efecto y el segmento se adelantó esa cantidad, para que el golpe
      caiga en el corte y no después.
- [ ] Ningún segmento quedó con **inicio negativo**: donde no cabía hacia atrás, se recortó la cabeza.
- [ ] La licencia se leyó **completa**, incluida la cláusula de redistribución, no solo la palabra
      "gratis".

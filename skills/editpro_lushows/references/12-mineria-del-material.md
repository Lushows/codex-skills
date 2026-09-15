# 12 — Minería del material

## Qué resuelve

Encontrar lo que ya está grabado y nadie vio. La mayoría de los videos malos no son malos por el montaje:
son malos porque se montó el guion que alguien imaginó antes del rodaje, mientras la mejor frase del día
se quedó enterrada en el minuto 7 del clip 12.

**Minería del material** es tratar el bruto como una mina, no como una bodega. En una bodega vas a buscar
lo que sabes que está. En una mina no sabes dónde está la veta, así que abres todo y miras.

La ley de este módulo: **el guion está en el bruto.** Tu trabajo no es imponerle una estructura al
material; es descubrir cuál es la estructura que el material ya tiene y ordenarla.

---

## La historia real que hay que memorizar

Proyecto verdadero, agosto de 2026. Rodaje de 16 clips, 10 minutos de bruto, entregable de 60 segundos.
Se generó un resumen automático de cada clip para saber qué había. El resumen del clip 12 decía algo
como "el sujeto habla sobre el diseño del empaque". Aburrido. Se marcó como relleno.

Al transcribir el clip completo apareció esta frase, dicha de paso, sin énfasis, al final de una toma que
el propio protagonista consideró fallida:

> "El relieve de la botella está inspirado en la piedra de los doce ángulos."

Ese dato terminó siendo el gancho del video. No estaba en el guion. Nadie lo pidió. El resumen automático
lo había descrito como algo que no valía la pena.

**Tres lecciones que salen de ahí:**

1. La joya casi nunca está en la toma que la persona considera "la buena". Está en lo que dice cuando ya
   se relajó, entre tomas, o cuando cree que la cámara no cuenta.
2. Un resumen automático de un clip es una compresión con pérdida. Lo específico — el nombre propio, la
   cifra, la referencia cultural — es exactamente lo que un resumen bota, y es exactamente lo que hace
   memorable un video.
3. Nunca descartes un clip por su resumen. Descártalo por su transcripción completa, o por haberlo visto.

---

## Qué es una joya

No es "un momento bonito". Es un fragmento que cumple al menos una de estas condiciones:

| Tipo de joya | Cómo suena | Para qué sirve |
|---|---|---|
| **El dato específico** | "inspirado en la piedra de los doce ángulos", "tardamos catorce meses" | gancho, credibilidad |
| **La confesión** | "la verdad, la primera versión era horrible" | genera confianza, rompe el tono de folleto |
| **La frase corta involuntaria** | "esto no se hace así en Colombia" | titular, texto en pantalla |
| **La reacción real** | risa genuina, sorpresa, un "uy" | remate, blooper, humanidad |
| **El contraste** | dice una cosa y hace la contraria | material de humor y de estructura |
| **El proceso visible** | las manos haciendo algo difícil | b-roll con peso narrativo |
| **El error revelador** | se equivoca y al corregirse explica mejor que en la toma buena | muchas veces la mejor explicación del video |

Una regla operativa: **si al leerlo en la transcripción te dan ganas de contárselo a alguien, es joya.**
Si te da lo mismo, es relleno.

---

## El método: cuatro pasadas

No se busca la joya mirando el video de corrido. Se busca en pasadas, cada una más cara que la anterior,
y cada una descartando material para que la siguiente sea más barata.

### Pasada 1 — Mapa visual (barata, minutos)

Genera la hoja de contactos de cada clip (módulo 17): 20 fotogramas en rejilla 5x4. En una imagen ves 10
minutos de video. Con eso sabes **qué hay** en cada clip: quién sale, dónde, con qué encuadre, si la
cámara se movió, si hay algo que no esperabas.

Lo que esta pasada encuentra: planos que no sabías que existían, momentos de acción, cambios de
locación, personas que aparecen sin que nadie las anotara.

Lo que NO encuentra: nada de lo que se dice. Para eso está la pasada 2.

### Pasada 2 — Transcripción completa con marcas (media, minutos y centavos)

Transcribe **todo** el audio con timecodes y marcas de toma falsa y risa (módulo 13). Esta es la pasada
que encuentra la joya. Es literalmente donde apareció la frase de la piedra.

Regla dura: **se transcribe el 100% del bruto, no una muestra.** Transcribir "los clips que parecen
buenos" es exactamente el sesgo que entierra la joya, porque la joya vive en el clip que no parecía bueno.

Cuesta muy poco si extraes el audio bien (ver módulo 13: 1 MB en vez de 80 MB).

### Pasada 3 — Lectura humana de la transcripción (barata en dinero, cara en atención)

Lees la transcripción entera, de principio a fin, con un resaltador mental. No buscas "el guion":
buscas frases que te sorprendan. Marca con una convención simple mientras lees:

```
JOYA   frase que quiero en el video si o si
RISA   momento comico usable
DATO   cifra, nombre propio, referencia concreta
DUDA   dice algo que hay que verificar antes de publicar
```

Esta pasada no se automatiza bien. Un modelo puede proponerte candidatas, pero la decisión de qué es
interesante depende del negocio, del público y del contexto — y de si ya lo dijiste en otro video.

### Pasada 4 — Ver solo lo marcado (cara, pero corta)

Ahora sí abres el video, y **solo** en los tramos marcados. De 10 minutos de bruto vas a ver 90 segundos.
Aquí confirmas lo que la transcripción no dice: si la cara acompaña a la frase, si el encuadre sirve, si
se movió la cámara justo ahí, si el audio de ese tramo está limpio.

Muchas joyas mueren en esta pasada (la frase es buenísima pero está de espaldas a la cámara). Está bien:
para eso existe la pasada.

---

## Cómo pedirle a un modelo que busque joyas (y cómo no)

### Lo que NO funciona

```
Resume cada clip en una linea.
```

Eso es lo que produjo "habla sobre el diseño del empaque" y enterró la piedra de los doce ángulos. Un
resumen premia lo general y bota lo específico. Es lo contrario de lo que necesitas.

### Lo que sí funciona

```
Te paso la transcripcion completa de un rodaje.

NO la resumas.

Extrae y devuelve, con su timecode en segundos:

1. Toda frase que contenga un dato concreto: una cifra, una fecha, un nombre propio,
   una referencia cultural, historica o geografica, una comparacion inesperada.
2. Toda frase que suene a confesion, admision de error o duda.
3. Toda frase de menos de 12 palabras que funcione sola como titular.
4. Todo momento de risa, sorpresa o reaccion no actuada.
5. Toda vez que la persona diga lo mismo de dos maneras distintas
   (quiero comparar cual version quedo mejor).

Para cada hallazgo devuelve: segundo de inicio, cita literal, y por que la marcaste.
No opines sobre si es buena. No la mejores. No la parafrasees.
```

Las tres instrucciones que cambian el resultado: **no resumas**, **cita literal**, **no la mejores**. Un
modelo que parafrasea te devuelve una versión limada de la joya, y cuando vas a buscarla en el audio no
existe esa frase.

---

## La prueba de las dos versiones

Cuando alguien graba varias tomas del mismo contenido, casi siempre dice lo mismo de formas distintas.
La versión "buena" (la que él aprobó) suele ser la más pulida y la menos viva. Compara siempre:

| Toma 1 (cruda) | Toma 5 (pulida) |
|---|---|
| "esto nos costó como catorce meses, fue horrible" | "el proceso de desarrollo tomó poco más de un año" |

La primera vende. La segunda es un comunicado de prensa. Si el material tiene ambas, la decisión no es
automática — depende de la marca — pero **tienes que haberlas visto las dos** para decidir. La minería es
lo que te pone las dos sobre la mesa.

---

## Buscar en la transcripción con herramientas

Una vez tienes `analisis/transcripcion.md`, buscar es trivial y vale la pena hacerlo sistemático:

```powershell
$t = "C:\Users\user\Desktop\VIDEO-BOTELLA\analisis\transcripcion.md"

# Cifras y numeros: casi siempre son datos concretos
Select-String -Path $t -Pattern "\d+" | Select-Object LineNumber, Line

# Marcadores de historia y de opinion fuerte
$ganchos = "porque|la verdad|resulta que|nadie sabe|el secreto|lo que pasa es|me di cuenta|inspirad|la primera vez|nunca"
Select-String -Path $t -Pattern $ganchos | Select-Object LineNumber, Line

# Risas y reacciones marcadas por el transcriptor
Select-String -Path $t -Pattern "\[RISA\]|\[SORPRESA\]" | Select-Object LineNumber, Line
```

Estas búsquedas no reemplazan la lectura: la aceleran. La lista de "líneas con números" es
sorprendentemente buena para encontrar los datos duros de un video.

---

## Señales de que hay una joya cerca

Aprende a reconocer estos patrones en la transcripción. Casi siempre precede a algo bueno:

- **"Ay, espérate"** / **"perdón, otra vez"** → viene una toma falsa, y justo antes o después suele estar
  la versión relajada y buena.
- **Una risa sin motivo aparente** → pasó algo fuera de guion.
- **La persona baja la voz** (se nota en la transcripción porque el modelo marca duda o el texto se
  vuelve entrecortado) → está diciendo algo que no tenía planeado decir.
- **"Bueno, ya"** al final de una toma → lo que dijo después de eso, con la cámara todavía grabando, es
  oro con frecuencia sospechosa.
- **Un cambio de tema abrupto** → alguien fuera de cuadro preguntó algo. La respuesta a esa pregunta suele
  ser más natural que todo el guion.

---

## Cuándo parar de minar

La minería tiene rendimientos decrecientes. Para cuando:

- Tienes **al menos tres candidatos a gancho** distintos entre sí. No uno: tres. Con uno solo no puedes
  comparar y te casas con el primero que viste.
- Tienes material para cada bloque de la estructura que vas a usar (ver módulo 19).
- Llevas dos pasadas sin encontrar nada nuevo.

Y anota en `CONTEXTO.md` lo que encontraste y descartaste, con el motivo. En el video 2 de la serie vas a
querer la joya que no cupo en el video 1.

---

## Lo que la minería le entrega al resto del proceso

| Sale de aquí | Va a |
|---|---|
| Lista de joyas con timecode | `14-seleccion-de-tomas.md`, `19-mapa-de-bloques.md` |
| Candidatos a gancho | `30-el-gancho.md` |
| Momentos de risa | `18-catalogar-bloopers.md` |
| Frases titulares | `41-subtitulos-vs-palabras-clave.md` |
| Datos a verificar | el cliente, antes de publicar |

---

## Errores comunes

- **Montar el guion imaginado en vez del material grabado.** El guion previo sirve para saber qué grabar.
  Después del rodaje manda el material.
- **Descartar un clip por su resumen automático.** Un resumen bota lo específico, y lo específico es la
  joya. Se descarta por transcripción completa, no por resumen.
- **Transcribir solo "los clips buenos".** El sesgo que entierra la joya. Se transcribe el 100%.
- **Pedirle a un modelo "resume" cuando lo que necesitas es "extrae con cita literal".** Son tareas
  opuestas.
- **Dejar que el modelo parafrasee las citas.** Si mejora la frase, después no la encuentras en el audio.
  Exige cita literal.
- **Ver el video de corrido esperando que la joya salte.** A los cuatro minutos ya no estás mirando, estás
  esperando. Por eso el método es por pasadas.
- **Quedarse con el primer gancho que aparece.** Sin tres candidatos no hay comparación, y sin comparación
  no hay criterio.
- **Ignorar lo que se dice entre tomas.** Ahí vive lo bueno con más frecuencia que en las tomas oficiales.
- **No anotar lo descartado.** El material que no cupo hoy es el video de la semana entrante.
- **Confiar en la memoria del rodaje.** "Yo me acuerdo que él dijo algo bonito" no es un timecode. Si no
  está en la transcripción con su segundo, no existe.

---

## Checklist

- [ ] Hay hoja de contactos de todos los clips (pasada 1 hecha)
- [ ] Está transcrito el 100% del bruto, no una selección
- [ ] Se leyó la transcripción completa de principio a fin
- [ ] Las joyas están marcadas con timecode en segundos y cita literal
- [ ] Hay al menos tres candidatos a gancho, distintos entre sí
- [ ] Se revisaron en video los tramos marcados (pasada 4) y se confirmó imagen y audio de cada joya
- [ ] Se compararon las versiones cruda y pulida de las frases que se dijeron varias veces
- [ ] Los datos concretos (cifras, nombres, referencias) están anotados para verificarlos con el cliente
- [ ] Ningún clip fue descartado con base en un resumen automático
- [ ] Lo descartado quedó anotado en `CONTEXTO.md` con el motivo, para futuros videos
- [ ] Las joyas están volcadas al mapa de bloques antes de tocar un solo corte

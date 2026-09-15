# 210 — CapCut a fondo: qué se puede, qué no, y dónde te va a doler

Este módulo es el inventario honesto. No el folleto de ByteDance, no el video de YouTube que te
promete "edición nivel Hollywood en 3 minutos". Lo que CapCut Pro 8.x realmente hace en Windows en
agosto de 2026, con nombres reales de menú y con las trampas marcadas.

Si venís de los módulos 110–119, esos te enseñaron **dónde vive el proyecto y cómo escribirlo por
código**. Este bloque (210–219) es otra cosa: **cómo se usa la herramienta a fondo, con las manos**.
Son complementarios. El puente por código no sirve de nada si no sabés qué recurso pedirle.

---

## La foto rápida

| Área | ¿CapCut lo hace? | Nivel real |
|---|---|---|
| Cortar, ordenar, ritmar | Sí | **Excelente.** Rápido como ningún otro. |
| Subtítulos automáticos | Sí | **Muy bueno** en español. 90–95 % con audio limpio. |
| Efectos y filtros | Sí, biblioteca enorme | **Bueno**, pero es un catálogo, no un motor. |
| Animaciones prehechas | Sí | **Muy bueno** para redes. |
| Keyframes a mano | Sí | **Suficiente.** Limitado en curvas. |
| Velocidad y rampas | Sí | **Muy bueno.** De lo mejor que tiene. |
| Máscaras | Sí | **Básico.** Una máscara por clip, formas fijas. |
| Croma | Sí | **Aceptable.** No compite con Resolve. |
| Corrección de color | Sí | **Medio.** Sin curvas por canal serias, sin scopes reales. |
| Audio (limpiar voz, separar) | Sí | **Bueno.** Sorprendentemente bueno. |
| Mezcla de audio fina | Parcial | **Pobre.** No hay ducking manual decente ni EQ paramétrico. |
| Tracking de movimiento | Sí | **Inestable.** Funciona a veces. |
| Composición por capas | Sí | **Limitado.** No hay precomposiciones ni anidados reales. |
| Gestión de proyecto grande | No | **Malo.** Se pone lento pasando los ~20 min de línea. |
| Multicámara | No | No existe. |
| Trabajo colaborativo real | Parcial | Solo por la nube, con fricción. |

Regla que resume todo: **CapCut es el mejor editor del mundo para video vertical de menos de 3
minutos, y un editor mediocre para cualquier otra cosa.**

---

## Lo que hace muy bien (y por qué)

### 1. La velocidad de corte

El flujo cortar–borrar–arrastrar es el más rápido del mercado. `Ctrl + B` parte el clip donde está la
cabeza lectora, `Supr` lo borra y cierra el hueco, y la línea se re-acomoda sola. En Premiere eso son
tres decisiones (¿ripple o lift?, ¿qué pistas?, ¿está el snap activo?). En CapCut es una tecla.

Para contenido de redes, donde el 80 % del trabajo es **quitar** cosas, esa diferencia es real. Un
reel de 45 segundos que en Premiere te toma 40 minutos, en CapCut te toma 15.

### 2. Los subtítulos automáticos

*Texto → Subtítulos automáticos* transcribe el audio y te deja los subtítulos ya cortados en bloques,
ya sincronizados y ya estilizados. En español latino la precisión con audio limpio y micrófono cerca
está entre 90 y 95 %. Con audio de celular en la calle baja mucho — pero sigue siendo más rápido
corregir que escribir desde cero.

Esta sola función justifica CapCut para la mayoría de la gente. Ver módulo 216.

### 3. Las animaciones y efectos prehechos

Miles de recursos listos, agrupados por categoría, que se aplican con un clic y se ven bien. No
tenés que saber de curvas de Bézier para que un título entre con gracia. Ver módulos 211 y 212.

### 4. La curva de velocidad

Las rampas de velocidad (*Velocidad → Curva*) están mejor resueltas que en muchos editores caros:
preajustes con nombre (Montaje, Héroe, Bala, Salto…) y una curva editable a mano. Ver módulo 214.

### 5. Limpiar la voz

*Reducir ruido*, *Mejorar voz* y *Aislamiento de voz* funcionan de verdad. Un audio grabado con el
micrófono del celular en un local con música de fondo sale utilizable. Ver módulo 217.

### 6. El archivo de proyecto es texto plano

Ningún otro editor popular te deja generar el montaje desde afuera con tanta facilidad. Ese es todo
el bloque 110–119 y el módulo 218 de este bloque.

---

## Lo que hace mal (aunque diga que lo hace)

### El color

CapCut tiene *Ajustar* (exposición, contraste, saturación, temperatura, sombras, luces…) y una
biblioteca de filtros. Lo que **no** tiene:

- **Scopes de verdad.** Hay un histograma pobre. No hay waveform ni vectorscopio decentes. Estás
  corrigiendo color a ojo, en un monitor sin calibrar. Eso no es corrección de color, es tuneo.
- **Curvas por canal serias.** Hay algo de curva RGB, pero es tosca.
- **Nodos ni capas de corrección encadenables** como en Resolve.
- **Manejo real de log / raw.** Si grabaste en un perfil plano de cámara buena, CapCut te va a
  destruir el material. Cargá LUTs con cuidado o llevá el color a Resolve.

Veredicto honesto: para material de celular y para "que se vea bonito", CapCut alcanza. Para trabajo
de cliente donde el color importa, no.

### La mezcla de audio

Podés subir y bajar volumen, poner fundidos de entrada y salida, y hay un *ducking* automático que a
veces funciona. Lo que no hay:

- EQ paramétrico decente.
- Compresor con controles reales.
- Automatización de volumen por keyframes que sea cómoda (se puede, pero es dolorosa).
- Medidor de loudness en LUFS. **Esto importa:** las plataformas normalizan a ~-14 LUFS y vos
  estás exportando a ciegas.

Solución práctica: mezcla gruesa en CapCut, y si el proyecto lo merece, normalizá el master con
ffmpeg (`loudnorm`, ver módulo 103).

### La composición por capas

CapCut apila pistas, sí. Pero:

- **No hay precomposiciones ni clips anidados de verdad.** Si querés animar 5 elementos como un solo
  bloque, tenés que animarlos uno por uno o exportar y reimportar.
- **No hay efectos encadenables con orden explícito** por clip. El orden en que se aplican las cosas
  es el que CapCut decide.
- **Una máscara por clip.** Punto. Ver módulo 215.

### Proyectos largos

Pasando los 15–20 minutos de línea de tiempo con muchas pistas, CapCut se pone lento, la
previsualización se traba y el autoguardado empieza a demorar. No es un editor de documentales.

### El tracking de movimiento

Existe (*Seguimiento*), y cuando funciona es mágico. Pero se pierde con oclusiones, con movimiento
rápido, con poca luz. No hay tracking planar ni de 4 puntos. No lo pongas en el camino crítico de una
entrega.

---

## Lo que directamente no hace

- **Multicámara.** No existe sincronización automática de varias cámaras por audio.
- **Máscaras animadas con forma libre** (rotoscopia con Bézier animada). No.
- **Expresiones / scripting interno.** No hay nada tipo expresiones de After Effects.
- **3D real.** Hay una rotación 3D falsa. No hay cámara, ni luces, ni profundidad.
- **Gestión de medios profesional.** No hay bins anidados serios, ni metadatos, ni proxies que vos
  controlés, ni relink robusto cuando movés archivos.
- **Exportación a XML / AAF / EDL.** Esto es grande: **no podés llevar tu montaje a otro editor por
  la vía oficial.** Ver módulos 118 y 219.
- **Control de versiones del proyecto.** No hay historial más allá del deshacer de la sesión.
- **Renderizado por lotes / cola de exportación** decente.

---

## Las novedades de 2026 (y cuánto creerles)

El ciclo 2026 de CapCut Desktop metió una tanda grande de IA. Lo que hay que saber:

| Función | Qué promete | Realidad práctica |
|---|---|---|
| **AI Auto-Edit** | Le das el bruto y te arma el corte solo | Ambicioso. **No disponible en EE. UU.** — el despliegue global quedó pausado por temas de propiedad intelectual. Disponibilidad irregular por región. No construyas un flujo encima. |
| **Motor de efectos por IA** | Describís un efecto en palabras y lo genera | Interesante, resultados inconsistentes. La biblioteca fija (50.000+ recursos) sigue siendo lo confiable. |
| **Video largo a Shorts** | Escanea y sugiere cortes | Útil como punto de partida. No como entrega. |
| **Outpainting de video** | Cambia el formato pintando el fondo faltante | Funciona en planos simples y estáticos. En movimiento se nota. |
| **Color neural por referencia** | Le das una foto y copia el look | Sirve para inspirarte, no para igualar cámaras. |
| **Aislamiento de voz 2.0** | Reconstruye frecuencias de voz en ruido | **Esto sí es bueno.** De lo mejor del año. |
| **Texto a voz** | Locución desde texto escrito | Correcto, voces genéricas. Para voz de marca, ElevenLabs sigue ganando. |

Advertencia estructural: **las funciones de IA de CapCut se procesan en la nube.** Eso significa que
(a) necesitás internet, (b) tu material sube a servidores de ByteDance, y (c) pueden cambiar,
encarecerse o desaparecer sin aviso. Para trabajo de cliente con material sensible, tenelo presente.

---

## Los planes, sin humo

En 2026 la estructura quedó en tres niveles:

- **Gratis** — exporta a 1080p, la mayoría de efectos, subtítulos limitados (unos 10 minutos de audio
  por video), recursos marcados "Pro" que te meten marca de agua.
- **Standard** (~US$9,99/mes) — quita marcas de agua, orientado sobre todo a móvil.
- **Pro** (~US$19,99/mes o ~US$179,99/año) — 4K, toda la biblioteca, almacenamiento en la nube,
  licencia comercial.

Tres cosas que casi nadie te dice:

1. **Los precios son regionales.** En Latinoamérica suelen ser bastante más bajos que en EE. UU.
2. **Suscribirse desde el navegador (capcut.com) suele salir más barato** que desde la App Store o
   Google Play, que meten US$1–3 encima.
3. **Pro NO es una licencia comercial universal.** Cubre el contenido que vos creás dentro del
   editor, pero los recursos que CapCut te presta (música, plantillas, algunos efectos) están
   licenciados **uno por uno**. Si estás haciendo trabajo pago para un cliente, la música de la
   biblioteca de CapCut es la trampa clásica. Ver módulo 128.

---

## Cómo decidir si CapCut es la herramienta correcta

Preguntate esto, en este orden:

1. **¿El entregable dura menos de 5 minutos?** Si no, empezá a mirar Resolve.
2. **¿Es vertical / para redes?** Si sí, CapCut es la respuesta por defecto.
3. **¿El color es un criterio de aceptación del cliente?** Si sí, el color no se hace acá.
4. **¿Necesitás entregar el proyecto a otro editor?** Si sí, CapCut es un callejón sin salida
   (módulo 219).
5. **¿Hay material confidencial?** Si sí, apagá las funciones de IA en la nube.
6. **¿Vas a repetir este montaje 50 veces con distinto material?** Si sí, el puente por código
   (módulos 112 y 218) es tu ventaja competitiva.

---

## El atajo mental

Pensá en CapCut como **una moto en una ciudad con trancón**. Para moverte rápido en distancias
cortas, no hay nada mejor. Para llevar un trasteo, es la herramienta equivocada y no importa cuánto
la tunees.

La gente pierde meses tratando de convertir la moto en camión. No lo hagas. Aprendé a exprimir la
moto (módulos 211–218) y sabé exactamente cuándo bajarte de ella (módulo 219).

---

## Errores comunes

- **Creerle al marketing de IA.** "AI Auto-Edit" suena a que te ahorra el trabajo; en la práctica es
  irregular, cambia por región y a veces ni está disponible. Nunca lo pongas en el camino crítico de
  una entrega con fecha.
- **Corregir color en CapCut para trabajo de cliente.** Sin scopes reales y en un monitor sin
  calibrar, lo que "se ve bien" en tu portátil se ve terrible en el celular del cliente.
- **Asumir que Pro = puedo usar cualquier música.** Es el error legal más común. La licencia es por
  recurso, no por suscripción. Un reclamo de derechos en un anuncio pago te tumba la campaña.
- **Meter proyectos de 30 minutos.** CapCut no está hecho para eso. Se traba, y el archivo de
  proyecto corrupto es una posibilidad real.
- **Empezar el proyecto sin decidir el formato final.** Cambiar de 9:16 a 16:9 a mitad de camino te
  desarma todos los encuadres y todas las posiciones de texto.
- **Confiar en el tracking para algo que tiene fecha de entrega.** Falla justo el día que no tenés
  tiempo de rehacerlo a mano.
- **Actualizar CapCut en mitad de un proyecto grande.** Se actualiza solo si lo dejás. Si tenés algo
  crítico abierto, terminalo y exportalo antes.
- **No exportar un respaldo del corte.** CapCut no tiene versionado. Exportá un archivo intermedio en
  cada hito importante.

---

## Checklist

- [ ] Verifiqué mi versión exacta de CapCut (menú de cuenta → *Acerca de*) y la anoté.
- [ ] Sé si estoy en Gratis, Standard o Pro, y qué me limita cada uno.
- [ ] Decidí el formato (9:16 / 1:1 / 16:9) **antes** de poner el primer clip.
- [ ] El entregable dura menos de 5 minutos, o ya acepté que CapCut me va a costar.
- [ ] Si el color importa para el cliente, tengo plan B (Resolve) para esa etapa.
- [ ] Si hay música, verifiqué la licencia del recurso específico, no solo que tengo Pro.
- [ ] Si el material es sensible, sé cuáles funciones suben mi video a la nube.
- [ ] No tengo ninguna función de IA de CapCut en el camino crítico de la entrega.
- [ ] Tengo un respaldo exportado del último corte aprobado.
- [ ] Sé cuál es mi salida si CapCut se queda corto (módulo 219) y no la voy a descubrir el día de
      la entrega.

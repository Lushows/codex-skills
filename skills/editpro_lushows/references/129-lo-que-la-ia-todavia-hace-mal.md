# 129 — Lo que la IA todavía hace mal: la lista honesta a agosto de 2026

## Para qué sirve este módulo

Para dos cosas muy concretas:

1. **Decidir antes de gastar.** Si el plano que necesitas está en esta lista, no lo generes. Fílmalo,
   fotografíalo, hazlo en post o replantea el plano.
2. **Cotizar honesto.** Cuando un cliente te dice "hazme un video con IA de dos personas dándose la
   mano y hablando", saber que eso está en la lista de lo difícil te evita prometer lo que vas a
   incumplir.

El vendedor de humo dice "la IA ya hace todo". El profesional dice "esto sí, esto no, y esto se
resuelve así". La segunda respuesta vende mejor, además.

---

## 1. Las manos

**Estado**: mejoró mucho. No está resuelto.

Qué funciona: una mano en reposo, un gesto simple, una mano sosteniendo un objeto grande en plano
medio o general.

Qué falla:
- **primeros planos de manos** — ahí aparecen los dedos de más y las articulaciones imposibles;
- **manos que interactúan entre sí** — entrelazar dedos, aplaudir, un apretón de manos;
- **manos manipulando objetos pequeños** — un anillo, un botón, una tapa de frasco;
- **manos en clips largos** — un plano de 8 segundos tiene 192 fotogramas y en algún punto la mano
  se desarma.

**Qué haces:**
- Compón sin las manos. En serio: mira si el plano funciona con encuadre más cerrado o más abierto.
- Si necesitas manos, **fílmalas**. Un celular y luz de ventana bastan; las manos no tienen cara,
  no necesitas modelo.
- Si tienes que generarlas: plano corto (3–4 s), sin interacción, sin objetos pequeños, y **guarda
  la semilla del intento bueno**.

---

## 2. El texto

**Estado**: el peor de la lista, aunque Gemini 3 Pro Image mejoró notablemente.

Qué pasa: letras deformadas, palabras casi correctas, ortografía inventada. Y el problema no es solo
el texto que pides: **es el texto que aparece solo**, en letreros de fondo, etiquetas de producto,
pantallas, camisetas y carteles.

Lo grave no es que se vea feo. Es que **la marca del cliente salga mal escrita** en una pieza
entregada.

**Qué haces:**
- Prohíbelo siempre y de forma redundante, en inglés:
  `absolutely no text, no letters, no words, no numbers, no logos, no signage, no watermarks`
- Pon el texto **después**, con tipografía real, editable.
- El logo va superpuesto desde el archivo vectorial. Nunca generado. Nunca.
- Esto no tiene excepciones. Módulo `40` para cómo tratar el texto en pantalla.

---

## 3. La continuidad entre planos

**Estado**: el problema más caro de la lista para el editor, porque no se ve hasta que montas.

Cada generación es un universo independiente. Genera dos planos del mismo café y vas a tener:

- dos tazas con forma distinta,
- dos mesas de madera distinta,
- dos calidades de luz distintas,
- y si hay una persona, dos personas.

Esto convierte una secuencia en un collage.

**Qué haces:**
- **Misma imagen de referencia para todos los planos de la escena** (módulo `126`). Es lo que más
  ayuda.
- **Misma semilla + prompts hermanos.** Cambia solo la frase de cámara entre plano y plano.
- **Seedance 2.0** es el modelo con mejor control de referencia si esto es crítico. **Kling 3.0**
  tiene modo multi-plano con consistencia de sujeto.
- **Corta rápido.** Un plano de 4 segundos deja ver la inconsistencia; uno de 1,2 segundos no.
  Editorialmente esto no es trampa: el ritmo rápido es una decisión válida.
- **La misma LUT de marca a todo** (módulo `125`) empareja al menos el color.
- Diseña la secuencia para que **no dependa** de la continuidad: planos de detalle en vez de planos
  de conjunto repetidos.

---

## 4. Las paletas de color

**Estado**: no lo hace mal — **no lo hace, punto.**

Ya está desarrollado en el módulo `125`, pero merece estar en esta lista porque es la limitación que
más gente sigue intentando resolver por prompt. Prueba real: una marca de dos colores (azul marino y
blanco) devolvió piedras crema, chispas doradas y botellas marrones.

**Qué haces:** referencia visual, prohibición explícita por nombre de los colores intrusos, y
**forzar el duotono o la LUT en post**. La tercera es la única garantía.

---

## 5. La física

**Estado**: mejorando, todavía identificable.

Lo que sigue fallando:

- **Líquidos.** Servir, salpicar, verter. Un café que se sirve se ve mal en casi todos los modelos.
  Y esto duele especialmente en gastronomía y bebidas, que es medio mercado.
- **Telas.** Ropa al viento, una cortina, un mantel. Se mueven con una inercia que no existe.
- **Objetos que se tocan.** Un vaso que se pone en la mesa, un objeto que se recoge. El punto de
  contacto es donde se rompe.
- **Peso.** Un objeto pesado que se levanta como si no pesara nada, o al revés.
- **Fuego y humo.** Convincentes de lejos, raros de cerca.

Lo que sí funciona bien: movimiento de cámara sobre escenas estáticas, viento suave en vegetación,
partículas ambientales, movimiento humano simple de cuerpo entero.

**Qué haces:**
- **Filma el líquido.** Servir un café es lo más fácil del mundo de filmar y lo más difícil de
  generar. Es el mejor ejemplo de dónde está la frontera.
- Diseña planos donde la física no sea el sujeto: cámara moviéndose, sujeto quieto.
- Si tiene que ser generado, **acórtalo**. Un segundo de líquido cuela; cuatro no.

---

## 6. La duración larga

**Estado**: límite estructural, no un defecto que se vaya a arreglar pronto.

Casi todos los modelos generan entre 4 y 10 segundos por clip. Y dentro de esos segundos, **la
calidad decae**: el segundo 1 es excelente, el segundo 8 ya derivó de color, de estilo y a veces de
sujeto.

**Qué haces:**
- **Piensa en planos, no en videos.** Un video de un minuto son quince planos generados y montados,
  no un plano de un minuto. Eso además es cómo se edita de verdad.
- **Genera corto.** Si necesitas 3 segundos, genera 4, no 8. Más barato (módulo `127`) y menos
  derivación.
- Los "videos largos" que ofrecen algunas herramientas son encadenados internos. Prefiere encadenar
  tú, que controlas los cortes.

---

## 7. El lipsync

**Estado**: es donde más se separaron los modelos.

- **Veo 3.1** es el mejor, con diferencia, en diálogo con audio nativo a 48 kHz. Si tu plano es
  alguien hablando a cámara, es el que eliges.
- **Kling 3.0** tiene lipsync multilingüe desde febrero de 2026.
- El resto: variable, y el español latino suele estar peor entrenado que el inglés.

Lo que sigue costando:
- **Frases largas.** Cuatro o cinco segundos de habla continua se desincronizan hacia el final.
- **Consonantes explosivas** (p, b, m) — el cierre de labios es lo primero que se pierde.
- **Perfil y ángulos raros.** El lipsync está entrenado sobre todo con caras frontales.
- **El español con acento colombiano.** Menos material de entrenamiento que el inglés o el español
  neutro.

**Qué haces:**
- Frases cortas. Genera por frase, no por párrafo.
- Cara frontal o casi frontal.
- **Corta a b-roll en la mitad de la frase.** Es la solución de siempre: cuando el lipsync se
  degrada, tapa. Y editorialmente ni siquiera es un parche, es buen montaje (módulo `23`).
- Si es un locutor de verdad, considera **grabar la voz** y usar la IA solo para el resto.

---

## 8. Los bonus que nadie te cuenta

**Multitudes.** Más de tres o cuatro personas en cuadro y aparecen caras derretidas al fondo,
personas fusionadas y gente caminando sin piernas.

**Animales en movimiento.** Un perro corriendo tiene un patrón de patas que casi ningún modelo
acierta. Quieto, bien; corriendo, mal.

**Reflejos y espejos.** El reflejo no corresponde con lo reflejado. Se ve mal apenas alguien lo nota.

**Comida caliente y vapor.** El vapor se comporta como humo genérico, no como vapor de comida. Y en
gastronomía eso es exactamente el plano que quieres.

**Escalas.** Objetos que están del tamaño equivocado respecto a la mano o al cuerpo que los sostiene.

**Continuidad de vestuario.** Los botones cambian, el estampado se mueve, un bolsillo aparece y
desaparece.

**Texto pequeño en interfaces.** Cualquier pantalla de celular o computador que salga en cuadro va a
tener una interfaz que no existe, con texto ilegible.

---

## La tabla de decisión

| Necesitas... | ¿Generar? | Mejor camino |
|---|---|---|
| Fondo, textura, atmósfera | ✅ Sí | Es lo que mejor hace |
| Movimiento de cámara sobre escena estática | ✅ Sí | Excelente |
| Producto girando, plano hero | ✅ Sí, con referencia | Corto, con corrección de color en post |
| Persona hablando a cámara | ⚠️ Con cuidado | Veo, frases cortas, cara frontal, b-roll de rescate |
| Manos manipulando algo pequeño | ❌ No | Fílmalo con el celular |
| Servir un café, un líquido | ❌ No | Fílmalo. Es fácil de filmar |
| Texto o logo en pantalla | ❌ Nunca | Post, tipografía real |
| Secuencia de 5 planos del mismo lugar | ⚠️ Difícil | Misma referencia + semilla, cortes rápidos, LUT común |
| Multitud | ❌ No | Material de archivo o filmado |
| El color exacto de la marca | ❌ No lo hace | Forzar en post |
| Un plano de un minuto | ❌ No | Quince planos montados |
| Un espejo, un reflejo | ❌ No | Replantea el plano |
| Vapor de comida caliente | ❌ No | Fílmalo |

---

## Lo que la IA sí hace mejor que tú

Para que la lista sea honesta en las dos direcciones. En estas cosas la IA de 2026 le gana a un
editor haciéndolo a mano:

- **Transcribir y ubicar en el tiempo** (módulo `124`) — mil veces más rápido
- **Encontrar el mejor take entre cuarenta** — dos minutos contra cuarenta
- **Reducción de ruido y separación de voz** — mejor que cualquier plugin de hace tres años
- **Rotoscopia y máscaras** — lo que era una tarde ahora son segundos
- **Estabilización** — mejor que la estabilización clásica
- **Escalado y restauración** de material viejo o comprimido
- **Fondos y texturas** que nadie va a mirar fijo
- **Camas musicales** del largo exacto y sin reclamos de derechos (módulo `123`)
- **Variantes** — veinte versiones de un anuncio para testear pauta

El patrón es claro: **la IA es excelente en lo que es tedioso y verificable, y mediocre en lo que
requiere criterio y coherencia.** Eso es exactamente lo que tú aportas.

---

## Cómo hablarle al cliente de esto

Lo que **no** funciona: "la IA no puede hacer eso". Suena a excusa.

Lo que sí funciona:

> "Ese plano del café sirviéndose lo filmamos, sale mejor y sale más rápido. Los fondos y la
> atmósfera sí los generamos, ahí la IA es buenísima y nos ahorra la locación. Así tienes lo mejor
> de los dos."

Le estás dando una solución, no una limitación. Y le estás demostrando que sabes dónde está la
frontera, que es exactamente lo que te contrató.

---

## Errores comunes

- **Vender "la IA hace todo".** Te vas a comer el incumplimiento tú.
- **Generar primeros planos de manos.** Fílmalos. Las manos no necesitan modelo ni maquillaje.
- **Generar líquidos.** Es lo más fácil de filmar y lo más difícil de generar.
- **Dejar que el modelo escriba cualquier texto.** Incluida la marca del cliente.
- **Montar una secuencia sin verificar continuidad plano a plano.** No se ve hasta que montas, y
  entonces ya pagaste todo.
- **Usar planos largos para tapar la inconsistencia.** Es al revés: corta más rápido.
- **Generar 8 segundos esperando que el 8 se vea como el 1.** Deriva.
- **Generar un párrafo entero de diálogo.** Frase por frase, con b-roll de rescate.
- **Meter multitudes, espejos o animales corriendo en el plan.** Están en la lista por algo.
- **Insistir contra una limitación estructural.** Diez intentos no arreglan lo que el modelo no
  sabe hacer. Cambia de camino en el segundo intento fallido.
- **No aprovechar en qué sí es buena.** Si sigues transcribiendo a mano o rotoscopiando a mano,
  estás perdiendo tiempo que la IA te regala.
- **Presentar la limitación como excusa en vez de como solución.** "Eso lo filmamos y sale mejor"
  vende; "la IA no puede" no.

---

## Checklist

- [ ] Revisé el guion buscando planos que estén en la **lista de lo que falla**
- [ ] Los planos de **manos en detalle** y **líquidos** los voy a filmar, no a generar
- [ ] Ningún **texto ni logo** sale del modelo; todo va en post con archivos reales
- [ ] Los planos de una misma escena comparten **imagen de referencia y semilla**
- [ ] La secuencia está diseñada con **cortes rápidos** para que la inconsistencia no se lea
- [ ] Todo el material, generado y filmado, pasa por la **misma LUT de marca**
- [ ] Los clips son **lo más cortos** que la idea permite
- [ ] Si hay diálogo: **frases cortas, cara frontal**, y tengo b-roll para tapar
- [ ] No hay multitudes, espejos, animales corriendo ni pantallas con interfaz
- [ ] Después de **dos intentos fallidos** en el mismo plano, cambio de camino en vez de insistir
- [ ] Estoy usando la IA en lo que **sí** es buena: transcripción, minería de takes, ruido, roto,
      fondos, camas musicales, variantes
- [ ] Le expliqué al cliente la frontera **como solución** ("eso lo filmamos y sale mejor"), no como
      excusa
- [ ] La cotización refleja lo que de verdad se va a generar y lo que se va a filmar

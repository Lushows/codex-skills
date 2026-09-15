# 79 — Voz generada y doblaje

Una voz sintética buena cuesta unos centavos y sale en 20 segundos. Un locutor profesional cuesta entre
$150.000 y $600.000 COP por una pieza y se demora un día. Esa diferencia es tan grande que la pregunta
no es *si* vas a usar voz generada, sino **cuándo conviene y cuándo delata**.

Este módulo es sobre eso: qué hay disponible a agosto de 2026, dónde se nota, qué reglas éticas son
innegociables y qué obligaciones legales ya están vigentes.

---

## 1. Las tres cosas distintas que la gente confunde

| Cosa | Qué es | Riesgo ético |
|---|---|---|
| **TTS (texto a voz)** | Escribes texto, sale una voz que no es de nadie real | Bajo |
| **Clonación de voz** | Entrenas un modelo con la voz de una persona específica | **Alto**: es la voz de alguien |
| **Doblaje / traducción de voz** | Tomas un audio existente y lo pasas a otro idioma manteniendo la voz | Medio a alto |

Son tres decisiones distintas con tres conversaciones distintas. Mezclarlas es de donde salen los
problemas.

---

## 2. TTS — texto a voz

### Dónde está la tecnología en 2026

Muy bien. Las voces sintéticas actuales manejan entonación, pausas, énfasis y hasta respiraciones. En
español latinoamericano, las opciones buenas incluyen ElevenLabs, las voces neuronales de Azure y de
Google, y OpenAI. En una lectura corta y neutra, una voz sintética buena es **indistinguible** de un
locutor para el oyente promedio.

### Dónde SÍ se nota

Esto es lo importante, porque es lo que decide si tu video suena profesional o suena raro:

**1. En las frases largas.** La voz sintética mantiene una energía constante que un humano no mantiene.
Después de 15–20 segundos, el oído registra que "no respira como persona". Solución: escribe frases
cortas y mete pausas a propósito.

**2. En los nombres propios y las marcas.** "GastroLatam" puede salir "Gastro-la-tam" con acento en el
sitio equivocado. Los nombres de ciudades colombianas, los apellidos, las siglas: todos son campo minado.
Solución: escribirlos fonéticamente en el guion ("Gastro Látam") y escuchar antes de montar.

**3. En los números y precios.** "$10.000" puede leerse "diez punto cero cero cero". Escribe "diez mil
pesos" en el guion, no la cifra.

**4. En la emoción real.** Una voz sintética puede sonar "entusiasta", pero no puede sonar *conmovida*,
*a punto de llorar*, ni *genuinamente indignada*. Si tu pieza depende de que la voz transmita una
emoción difícil, la sintética se cae.

**5. En la ironía y el doble sentido.** El chiste depende del timing y de una inflexión mínima; la voz
sintética casi nunca la acierta.

**6. En el español colombiano.** Muchos modelos leen español "neutro", mexicano o peninsular. Si la
pieza es para Bogotá y la voz suena a doblaje de Netflix, se siente ajena. Escucha con esa oreja puesta.

### Cómo hacer que suene bien

**Escribe para ser oído, no para ser leído.** Un párrafo bien escrito para la vista suena mal dicho.
Frases de 8 a 14 palabras. Un verbo por frase. Sin subordinadas.

**Marca las pausas con puntuación.** Un punto vale ~400 ms de pausa; una coma ~200 ms. Si necesitas una
pausa larga, pon punto y aparte, o escribe la frase en dos líneas separadas.

**Escribe la pronunciación difícil como suena.** "GastroLatam" → "Gastro Látam". "IVA" → "iva" o "i ve a"
según lo que quieras. "2026" → "dos mil veintiséis".

**Graba varias tomas.** Cuesta centavos. Genera la misma línea 3 o 4 veces y elige la mejor. Los modelos
varían entre generaciones.

**Y procésala como una voz real.** Este es el paso que casi nadie da y el que más diferencia hace: una
voz de TTS sale técnicamente limpia pero **plana**. Pásala por parte de la cadena de `70`:

```bash
ffmpeg -i tts_crudo.wav -af "highpass=f=90,equalizer=f=2600:t=q:w=1.2:g=2.5,acompressor=threshold=-18dB:ratio=2.5:attack=20:release=200:makeup=1.5,highshelf=f=11000:g=-2:t=q:w=0.7,loudnorm=I=-14:TP=-1.5:LRA=11" tts_listo.wav
```

Nota que **no lleva reducción de ruido** (no hay ruido que quitar) ni gate (no hay silencios sucios). Sí
lleva EQ y compresión, porque lo que le falta a una voz de TTS es carácter, no limpieza.

**El truco del ambiente.** Una voz de TTS suena a vacío absoluto. Ponerle un lecho de ambiente muy suave
debajo (−45 dB, ver `77`) la aterriza y la hace pasar por grabada:

```bash
ffmpeg -i tts_listo.wav -stream_loop -1 -i ambiente_oficina.wav \
  -filter_complex "[0][1]amix=inputs=2:duration=first:dropout_transition=0:weights=1 0.05[out]" \
  -map "[out]" tts_con_ambiente.wav
```

Contraintuitivo y muy efectivo: le agregas ruido para que suene más real.

### Cuándo usar TTS y cuándo no

| Usar TTS | Contratar locutor / grabar tú |
|---|---|
| Contenido informativo, tutoriales | Pieza emocional, testimonio |
| Volumen alto de videos (20 al mes) | Pieza única e importante (comercial de marca) |
| Prototipar el guion antes de grabar | Cuando la voz **es** la marca |
| Traducir a idiomas que no hablas | Humor, ironía, tono conversacional |
| Presupuesto cero | Cuando el cliente lo puede pagar |

**Un uso de TTS que casi nadie aprovecha:** hacer la **maqueta** de la voz en off antes de grabar. Montas
el video entero con TTS, ves si el ritmo funciona, ajustas el guion, y **después** grabas al humano con
el guion ya probado. Te ahorra la mitad de las regrabaciones.

---

## 3. Clonación de voz

Aquí cambia la conversación. Ya no es "una voz genérica", es **la voz de una persona real**.

### Cómo funciona

Le das al sistema entre 30 segundos (clonación instantánea) y 30 minutos (clonación profesional) de
audio de alguien, y a partir de ahí puede hacerla decir cualquier cosa.

### La regla innegociable

**Solo se clona una voz con el consentimiento explícito y por escrito de su dueño.** No es una
recomendación: es la política de las plataformas serias, es requisito legal en un número creciente de
jurisdicciones (al menos 12 estados de EE.UU. tienen leyes específicas sobre clonación de voz a 2026), y
es lo mínimo decente.

ElevenLabs, por ejemplo, exige que confirmes que tienes derecho y consentimiento en la clonación
instantánea, y añade un paso de verificación en la profesional. Prohíbe clonar figuras públicas sin
consentimiento y suspende cuentas por violarlo.

**Qué debe incluir el consentimiento por escrito:**

```
Yo, [nombre, cédula], autorizo a [empresa] a crear un modelo de voz sintética
a partir de mis grabaciones y a usarlo para:
  - usos permitidos / NO permitidos:  [ej. redes de la marca X / política, avales de terceros]
  - plazo y territorio:               [ej. 24 meses desde la firma, Colombia]
  - revocación:                       con [30] días de aviso
  - remuneración:                     [monto y periodicidad, o "sin costo"]
Firma, fecha, cédula.
```

Sin eso, no clones. Y si un cliente te pide clonar la voz de un tercero "que seguro no le importa", esa
es tu señal para decir que no.

### Los usos legítimos

- **Tu propia voz**, para no tener que grabar cada corrección de guion. Es el uso más útil de todos:
  grabas una vez bien, y las 40 correcciones de texto salen de tu clon.
- **La voz del dueño del negocio**, con su permiso, para escalar contenido sin que tenga que grabar todo.
- **Locutor contratado**, con contrato que cubra explícitamente el uso del clon, plazo y remuneración.
  Un locutor que cede su voz para clonación está cediendo su oficio: eso se paga distinto a una sesión.
- **Continuidad**: corregir una palabra de una grabación que ya no se puede repetir.

### Los usos que no se hacen, y punto

- Clonar la voz de una figura pública o de un famoso.
- Clonar a alguien para hacerlo decir algo que no dijo.
- Cualquier cosa que suene a testimonio, aval o recomendación de una persona que no lo dio.
- Cualquier cosa que pueda pasar por la voz de un familiar o conocido pidiendo algo (es el fraude por
  voz clonada, y es delito).
- Sortear verificación biométrica por voz.

---

## 4. Doblaje y traducción de voz

Tomar un video en español y sacarlo en inglés, portugués o el idioma que sea, manteniendo el timbre de
la persona. La tecnología a 2026 lo hace bien.

**Lo bueno:** llegar a otros mercados sin regrabar y sin locutores por idioma.

**Los tres problemas prácticos:**

1. **El largo no coincide.** Una frase en español dura distinto que en inglés. El doblaje o queda apurado
   o queda con huecos. Solución: ajustar el video (repetir un plano, alargar un corte) en vez de forzar
   la voz.
2. **La sincronía labial.** Si la persona está en cámara, se ve el desfase. Para voz en off no importa;
   para talking head sí. Existen herramientas de lip sync, pero agregan otro problema (ver punto 3).
3. **No hablas el idioma.** No puedes verificar si el doblaje dice una barbaridad. **Que lo revise
   alguien que sí lo hable, siempre.** Esto no es opcional: hay casos documentados de traducciones
   automáticas que cambiaron el sentido de una promesa comercial.

**Recomendación práctica:** para redes, doblaje sobre planos que no sean primer plano de la cara, o
convertido a voz en off con b-roll. Se resuelve el problema de la sincronía y se ve mejor.

---

## 5. Divulgación: qué obliga la ley y qué obliga la decencia

### Lo legal (agosto 2026)

El **Reglamento de IA de la Unión Europea** — su **artículo 50** — entró en aplicación el **2 de agosto
de 2026**. Sus puntos relevantes para lo que haces:

- Quien **despliega** un sistema de IA para crear un *deepfake* debe **revelar** que el contenido fue
  generado o manipulado artificialmente.
- La obligación aplica **aunque no haya intención de engañar**, e incluso cuando no se represente a una
  persona real. Contenido que suena como una persona real debe estar etiquetado.
- Quien **provee** el sistema generativo debe marcar las salidas de forma **legible por máquina** y
  detectable (es lo que hace SynthID en el caso de Google).
- La divulgación tiene que ser **perceptible en la propia interacción**. Enterrarla en los términos y
  condiciones, o dejar solo una marca en los metadatos, no cumple.
- **Alcance extraterritorial:** aplica a proveedores y desplegadores establecidos fuera de la UE cuando
  la salida se usa dentro de la Unión. Un negocio colombiano que pauta hacia público europeo está en
  alcance.

Colombia no tiene a agosto de 2026 una norma equivalente específica, pero el Estatuto del Consumidor ya
prohíbe la publicidad engañosa, y un testimonio con voz sintética presentado como real cabe ahí sin
esfuerzo.

### Lo ético (que es más exigente que la ley)

Mi regla, y es simple:

> **Divulga cuando la persona, de haberlo sabido, se habría sentido engañada.**

Aplicada a casos:

| Situación | ¿Divulgar? |
|---|---|
| Voz en off genérica de TTS narrando un tutorial | **No hace falta.** Nadie asume que hay un humano detrás de una narración |
| Voz clonada del dueño diciendo cosas que él aprobó | **Recomendable.** No es engaño, pero la transparencia suma |
| Voz clonada de alguien en un **testimonio** | **Obligatorio.** Un testimonio vale por ser de una persona |
| Doblaje a otro idioma de una persona real | **Sí**, señalar que es doblaje con IA |
| Voz que imita a una persona conocida | **No se hace.** Punto |
| Cualquier pieza que se publique hacia la UE | **Sí**, por el artículo 50 |

**Cómo divulgar sin arruinar la pieza:** no hace falta un aviso legal de tres líneas. Basta con:
- Un texto pequeño en pantalla: "Voz generada con IA".
- Una línea al final de la descripción del post.
- En un doblaje: "Doblado con IA a partir del original en español".

Se lee en dos segundos, no rompe nada, y te cubre.

---

## 6. Cómo integrar una voz generada en la pieza

Flujo completo:

```bash
# 1) generar el TTS y guardarlo en WAV 48 kHz (no MP3)

# 2) darle carácter: EQ + compresión, SIN reducción de ruido ni gate
ffmpeg -i tts_crudo.wav -af "highpass=f=90,equalizer=f=350:t=q:w=1.5:g=-2,equalizer=f=2600:t=q:w=1.2:g=2.5,acompressor=threshold=-18dB:ratio=2.5:attack=20:release=200:makeup=1.5,highshelf=f=11000:g=-2:t=q:w=0.7" tts_eq.wav

# 3) aterrizarla con un lecho de ambiente muy suave
ffmpeg -i tts_eq.wav -stream_loop -1 -i ambiente.wav \
  -filter_complex "[0][1]amix=inputs=2:duration=first:dropout_transition=0:weights=1 0.05[out]" \
  -map "[out]" tts_ambiente.wav

# 4) mezclar con música y ducking (ver 75)
ffmpeg -i tts_ambiente.wav -i musica.wav \
  -filter_complex "[1]volume=-14dB[m];[m][0]sidechaincompress=threshold=0.025:ratio=8:attack=15:release=400[duck];[0][duck]amix=inputs=2:duration=first:dropout_transition=0[out]" \
  -map "[out]" mezcla.wav

# 5) normalizar (ver 73)
ffmpeg -i mezcla.wav -af "loudnorm=I=-14:TP=-1.5:LRA=11" audio_final.wav
```

**Ajustar el ritmo sin regenerar.** Si la voz va muy rápida o muy lenta, `atempo` la cambia sin alterar
el tono:

```bash
# 8% más lenta
ffmpeg -i tts.wav -af "atempo=0.92" tts_lento.wav
```

`atempo` acepta valores entre 0,5 y 2,0. Para cambios mayores, encadena: `atempo=0.5,atempo=0.8`.

**Agregar una pausa donde falta** (insertar 350 ms en el segundo 6,2):

```bash
ffmpeg -i tts.wav -ss 0 -t 6.2 a.wav
ffmpeg -f lavfi -i "anullsrc=r=48000:cl=stereo" -t 0.35 -c:a pcm_s16le pausa.wav
ffmpeg -i tts.wav -ss 6.2 b.wav
ffmpeg -i a.wav -i pausa.wav -i b.wav -filter_complex "[0][1][2]concat=n=3:v=0:a=1" tts_con_pausa.wav
```

Ese control manual del ritmo es lo que más acerca una voz de TTS a sonar humana. Los humanos hacen
pausas irregulares; los modelos hacen pausas regulares.

---

## 7. La pregunta honesta: ¿se nota?

Sí y no, y la respuesta depende de la duración.

- **Menos de 15 segundos**, frases cortas, tono informativo: **no se nota**.
- **30 a 60 segundos**: se nota si estás atento, y la mayoría de la gente no lo está.
- **Más de 2 minutos**: se nota. La energía constante y las pausas regulares se acumulan y el oído se
  cansa.
- **Cualquier duración con emoción real**: se nota mucho.

Y hay un factor social: **la gente de 2026 ya sabe cómo suena una voz de IA**. Lo que hace tres años
pasaba desapercibido, hoy activa el detector. Eso va a seguir moviéndose, y va a moverse en tu contra.

**La consecuencia comercial** es lo que importa: en contenido informativo, que la voz sea de IA no le
resta nada a la conversión. En contenido que depende de confianza —testimonios, la voz del dueño, un
mensaje personal— sí resta, y resta mucho, porque el público interpreta la voz sintética como señal de
que el negocio no puso la cara. En una marca pequeña, poner la cara es una ventaja competitiva; no la
regales por ahorrarte 20 minutos de grabación.

---

## Errores comunes

- **Clonar la voz de alguien sin consentimiento escrito.** Es el error que no tiene arreglo.
- **Escribir el guion de TTS como se escribe para leer.** Frases largas, subordinadas, párrafos. Suena
  fatal. Escribe para el oído: frases de 8–14 palabras.
- **Dejar los números y nombres propios sin escribir fonéticamente.** "$10.000" sale "diez punto cero
  cero cero".
- **No escuchar el TTS completo antes de montar.** Una palabra mal pronunciada en el segundo 14 te
  obliga a rehacer el montaje.
- **Usar la primera generación.** Cuesta centavos generar cuatro y elegir. Hazlo.
- **No procesar la voz de TTS.** Sale limpia y plana. Necesita EQ y compresión, no reducción de ruido.
- **Dejarla en el vacío absoluto.** Un lecho de ambiente a −45 dB la hace pasar por grabada.
- **Usar TTS en un testimonio.** Un testimonio vale por ser de una persona. Con voz sintética no vale
  nada, y si se descubre, resta.
- **Usar voz "neutra" o con acento ajeno para público colombiano.** Se siente extraño aunque nadie sepa
  explicar por qué.
- **Doblar a un idioma que no hablas sin que alguien lo revise.** Puedes estar prometiendo cualquier cosa.
- **Forzar el doblaje al largo original.** Ajusta el video, no la voz.
- **No divulgar cuando el público se sentiría engañado.** Aunque la ley de tu país no lo exija todavía.
- **Ignorar el artículo 50 europeo si publicas hacia la UE.** Aplica desde el 2 de agosto de 2026 aunque
  estés en Colombia.
- **Usar TTS de dos minutos y creer que no se nota.** Se nota.

---

## Checklist

- [ ] Tengo claro si esto es **TTS, clonación o doblaje** — son tres decisiones distintas.
- [ ] Si hay clonación, tengo **consentimiento por escrito** con usos, plazo, territorio, revocación y
      remuneración.
- [ ] No estoy clonando la voz de una **figura pública** ni de un tercero sin permiso.
- [ ] El guion está **escrito para el oído**: frases de 8–14 palabras, un verbo por frase.
- [ ] Los **números, marcas y nombres propios** están escritos fonéticamente.
- [ ] **Escuché el audio completo** antes de montar el video encima.
- [ ] Generé **varias tomas** y elegí la mejor.
- [ ] El **acento** corresponde al público (colombiano, no neutro genérico, si va para Colombia).
- [ ] Procesé la voz con **EQ + compresión** (no con reducción de ruido ni gate).
- [ ] Le puse un **lecho de ambiente** a −45 dB para que no flote en el vacío.
- [ ] Ajusté el **ritmo y las pausas** a mano donde el modelo las hizo regulares de más.
- [ ] Si es doblaje, **alguien que habla el idioma lo revisó**.
- [ ] Si es doblaje sobre alguien en cámara, resolví la **sincronía** (o pasé a voz en off con b-roll).
- [ ] **Divulgué** si la persona, de saberlo, se habría sentido engañada.
- [ ] Si el contenido llega a público de la **UE**, cumplo el **artículo 50** con una etiqueta perceptible.
- [ ] Para una pieza donde la voz **es** la marca, consideré grabar a un humano en vez de generar.
- [ ] Normalicé la mezcla final a **−14 LUFS** (ver `73`).

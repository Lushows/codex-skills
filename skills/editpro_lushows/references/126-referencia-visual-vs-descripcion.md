# 126 — Referencia visual vs descripción: enséñale el estilo, no se lo cuentes

## La lección maestra

Si de toda esta serie te llevas una sola cosa, que sea esta:

> **No le describas el estilo de tu marca con adjetivos. Pásale los archivos de la marca como
> imagen de referencia.**

Verificado en prueba real, agosto de 2026. La diferencia entre:

- pedir **"estilo retro cartoon"** → sale cualquier cosa que el modelo entienda por eso, y cambia
  en cada generación;
- pasarle **el diseño real de la marca** como referencia → sale **on-brand a la primera**;

…es **abismal**. No es "un poco mejor". Es la diferencia entre inservible y entregable.

Este módulo es sobre por qué pasa eso y cómo se hace bien.

---

## Por qué los adjetivos fallan

### Los adjetivos son promedios, no direcciones

Cuando escribes "retro", el modelo no busca tu retro. Busca **el centro de masa de todo lo que en
internet está etiquetado como retro**: los años 50 y los 80 mezclados, papel envejecido, neón,
tipografías de rótulo, colores desaturados y saturados al mismo tiempo. Te devuelve el promedio de
un territorio enorme.

Tu marca no es un promedio. Tu marca es **un punto específico** dentro de ese territorio. Ningún
adjetivo, ni diez adjetivos juntos, señalan un punto. Señalan una nube.

### Los adjetivos no son estables

"Cálido" para ti es una paleta ocre con luz de tarde. Para el modelo puede ser una fogata. Y para el
modelo **mañana** puede ser otra cosa, porque cambió de versión.

Una imagen de referencia no tiene esa ambigüedad. Es un hecho.

### Un archivo lleva mil veces más información

Piénsalo en términos brutos. Un párrafo de descripción son unas cincuenta palabras. Una imagen de
referencia lleva:

- la paleta exacta, con las proporciones exactas de cada color
- el grosor del trazo
- el nivel de detalle
- la textura del fondo
- el tipo de sombra
- la relación entre luz y contraste
- la manera concreta en que esa marca dibuja una curva

Nada de eso se escribe. Todo eso se ve.

### El razonamiento por analogía es más fuerte que el declarativo

Este es el punto técnico. Cuando le dices "haz esto en el estilo X", el modelo tiene que **resolver
qué significa X** antes de generar. Cuando le muestras una imagen y le dices "en este estilo", el
modelo **copia y transforma**, que es una tarea mucho más fácil y mucho más precisa.

Es la diferencia entre explicarle a alguien cómo se ve tu casa y mostrarle una foto.

---

## Cómo se hace

### El formato de la petición

Con los modelos multimodales (Gemini de imagen, Veo con imagen de referencia, Seedance con
referencias):

```jsonc
{
  "contents": [{
    "role": "user",
    "parts": [
      { "inlineData": { "mimeType": "image/png", "data": "<base64 de tu pieza real>" } },
      { "text": "Genera una escena nueva EN ESTE MISMO ESTILO gráfico: mismos colores exactos, mismo grosor de trazo, mismo nivel de detalle, misma textura de fondo. Sujeto nuevo: [lo que quieres]. Absolutely no text, no letters, no words." }
    ]
  }]
}
```

La estructura que funciona:
1. **primero la imagen**, después el texto
2. el texto dice **"EN ESTE MISMO ESTILO"**, señalando explícitamente a la referencia
3. el texto enumera **qué atributos copiar** (no confíes en que adivine cuáles importan)
4. el texto dice **qué es lo nuevo** (el sujeto, la acción, el encuadre)
5. las prohibiciones de siempre

### El error de redacción más común

```
❌ "Genera un frasco en estilo retro cartoon, como la imagen adjunta"
```

Esto es peor que no pasar imagen, porque le estás dando **dos instrucciones que compiten**: el
adjetivo "retro cartoon" (una nube) y la imagen (un punto). El modelo promedia las dos y se aleja de
tu punto.

```
✅ "Genera un frasco EN ESTE MISMO ESTILO: mismos colores, mismo trazo, misma textura."
```

**Si pasas referencia, quita los adjetivos de estilo del prompt.** Deja solo la acción y el
encuadre. La referencia manda; el texto ejecuta.

Regla mnemotécnica:

> **La imagen dice CÓMO se ve. El texto dice QUÉ pasa.**

---

## Cuántas referencias y cuáles

### El número: de una a tres

| Cantidad | Qué pasa |
|---|---|
| **1** | Control máximo del estilo. La opción por defecto |
| **2–3** | Refuerza lo que las imágenes tienen **en común**, ignora lo que las diferencia. Útil para que no copie la composición de una sola |
| **4–6** | Empieza a promediar. El estilo se desdibuja |
| **7+** | Barro. Además, cada imagen de entrada **se cobra** (Gemini 3 Pro Image cobra ~560 tokens por imagen de entrada) |

La regla mental: **el modelo extrae lo que las referencias comparten.** Si le pasas tres piezas de tu
marca en el mismo estilo pero con sujetos distintos, extrae el estilo (que es lo compartido) y no se
casa con ningún sujeto. Eso es exactamente lo que quieres.

### Cuáles elegir

**Sí:**
- Piezas **terminadas y aprobadas** de la marca, en el estilo exacto
- Fotogramas de un video anterior que quedó bien
- El fotograma cero que ya diseñaste tú
- Si es producto: fotos reales del producto, bien iluminadas, sobre fondo limpio

**No:**
- **Moodboards.** Un moodboard tiene seis estilos a propósito, para inspirar a un humano. Al modelo
  lo confunde: promedia los seis.
- **El logo suelto sobre blanco.** Le enseña "hay un logo", no "así se ve mi mundo".
- **Capturas de pantalla con interfaz alrededor.** Va a copiar la interfaz.
- **Imágenes de baja resolución o comprimidas.** Copia los artefactos de compresión también.
- **Referencias con marca de agua.** Adivina qué va a aparecer en la generación.
- **Piezas que a ti no te gustan del todo.** Si la referencia está al 70%, la salida está al 50%.

---

## Qué pasa si mezclas (y cómo se controla)

Mezclar referencias de tipos distintos es donde la gente se enreda. Cada tipo de referencia controla
una cosa distinta:

| Tipo de referencia | Qué controla | Riesgo si la mezclas mal |
|---|---|---|
| **Estilo** (una pieza gráfica) | Paleta, trazo, textura | El modelo copia también su composición |
| **Sujeto** (foto del producto) | Forma, proporciones, identidad | El modelo copia también su color y su fondo |
| **Composición** (un fotograma de encuadre) | Dónde va cada cosa | El modelo copia también su estilo |

Si le pasas una de estilo y una de sujeto, el modelo **no sabe cuál manda para el color** y va a
promediar. Resultado: un producto con el color equivocado en un estilo a medio camino.

### La solución: dile explícitamente qué copiar de cuál

Los modelos multimodales aceptan varias partes intercaladas. Etiquétalas:

```jsonc
"parts": [
  { "text": "REFERENCIA DE ESTILO — copia de aquí: paleta exacta, grosor de trazo, textura de fondo, tipo de sombra:" },
  { "inlineData": { "mimeType":"image/png", "data": "<estilo>" } },
  { "text": "REFERENCIA DE SUJETO — copia de aquí ÚNICAMENTE la forma y las proporciones del producto. NO copies su color ni su fondo ni su iluminación:" },
  { "inlineData": { "mimeType":"image/png", "data": "<producto>" } },
  { "text": "Genera: el producto de la segunda imagen, dibujado en el estilo de la primera, sobre fondo liso. Absolutely no text, no letters, no words." }
]
```

Funciona mucho mejor de lo que uno espera. El modelo respeta las etiquetas si son claras y si dices
también **qué NO copiar** de cada una. Ese "NO copies su color ni su fondo" es la frase que cambia
el resultado.

### Si aun así se confunde: parte el trabajo

Cuando la mezcla no cuadra, no insistas. Divide:

```
Paso 1: genera el producto solo, con la referencia de sujeto → producto_limpio.png
Paso 2: genera el fondo/escena solo, con la referencia de estilo → escena.png
Paso 3: compón las dos en post
```

Dos generaciones baratas y controladas le ganan a diez intentos de una generación compleja. Y
además tienes las piezas sueltas para reusarlas.

---

## Referencia en video: lo mismo, con más deriva

En video la referencia sigue siendo la herramienta más fuerte, pero con una advertencia:

**la referencia manda con fuerza en el fotograma 1 y va perdiendo fuerza a lo largo del clip.**

Para un clip de 6 segundos: el segundo 1 se parece mucho a tu referencia, el segundo 6 ya se
desvió. Es la deriva del módulo `125` en acción.

Consecuencias prácticas:

- **Clips más cortos derivan menos.** Si puedes contar el plano en 4 segundos, no generes 8.
- **Genera varios planos cortos en vez de uno largo.** Además te da más opciones de montaje.
- **Corrige el color del clip completo en post.** Sin excepción.
- Y recuerda la trampa de Veo: con imagen de referencia, **nada de `resolution`,
  `enhancePrompt:false` ni `negativePrompt`** (módulo `121`).

---

## La biblioteca de referencias: móntala una vez, úsala siempre

Si trabajas la misma marca de forma recurrente, arma esta carpeta y deja de improvisar:

```
marca/referencias/
  estilo/
    01-pieza-aprobada.png        ← la mejor pieza en el estilo canónico
    02-pieza-aprobada.png
    03-fotograma-video-ok.png
  producto/
    frasco-frontal.png
    frasco-tres-cuartos.png
  paleta/
    paleta.png                    ← muestras de color grandes y planas
    marca.cube                    ← la LUT (módulo 125)
  logo/
    logo.svg                      ← NUNCA se genera, siempre se superpone
  PROMPT-BASE.txt                 ← el bloque de estilo y prohibiciones que ya funciona
```

El `PROMPT-BASE.txt` es oro puro. Es el texto que ya probaste y que ya funciona, con las
prohibiciones específicas de esta marca (los colores que sabes que inventa). Cada proyecto nuevo
empieza copiando ese archivo, no desde cero.

---

## Cuándo la descripción sí es la herramienta correcta

Sé justo: los adjetivos no siempre están mal.

- **Cuando no hay marca todavía.** Explorando dirección de arte, los adjetivos son perfectos porque
  quieres la nube, no el punto.
- **Para la acción y el encuadre.** "Dolly lateral lento, plano cerrado, 85 mm" es texto y solo
  puede ser texto.
- **Para las prohibiciones.** "No text, no gold" es texto.
- **Para el sujeto.** "Un frasco ámbar de 60 ml" es texto.

La división es limpia:

> **Referencia → aspecto. Texto → acción, encuadre, sujeto y prohibiciones.**

---

## Errores comunes

- **Describir la marca con adjetivos cuando tenías el archivo a mano.** Es el error caro del módulo.
- **Pasar la referencia Y dejar los adjetivos de estilo en el prompt.** Compiten y el modelo
  promedia. Si pasas referencia, quita los adjetivos de estilo.
- **Pasar un moodboard.** Tiene seis estilos a propósito. El modelo promedia los seis.
- **Pasar el logo suelto como referencia de estilo.** Le enseña "logo", no "estilo".
- **Pasar más de tres referencias.** Promedia, se desdibuja, y cada entrada se cobra.
- **Mezclar referencia de estilo y de sujeto sin etiquetarlas.** El modelo no sabe cuál manda para
  el color.
- **Olvidar decir qué NO copiar de cada referencia.** Esa frase es la que cambia el resultado.
- **Insistir diez veces en una generación compleja.** Pártela en dos generaciones simples y compón
  en post.
- **Usar referencias de baja resolución o con marca de agua.** Copia los defectos y la marca de agua.
- **Usar como referencia una pieza que no te convence.** Referencia al 70% = salida al 50%.
- **Esperar que la referencia mande igual en el segundo 6 que en el 1.** Deriva. Clips cortos.
- **No montar la biblioteca de referencias.** Improvisar cada vez es cómo se pierde la coherencia
  entre piezas de la misma marca.
- **No guardar el `PROMPT-BASE.txt` que ya funcionó.** Lo vas a reescribir peor.

---

## Checklist

- [ ] Tengo el **archivo real** de la marca, no una descripción de la marca
- [ ] Pasé **de 1 a 3** referencias, no más
- [ ] Las referencias son **piezas aprobadas** en el estilo canónico, no moodboards
- [ ] Las referencias están en **buena resolución** y sin marca de agua
- [ ] **Quité los adjetivos de estilo** del texto del prompt
- [ ] El texto dice explícitamente **"EN ESTE MISMO ESTILO"** y enumera qué copiar
- [ ] Si mezclé tipos de referencia, las **etiqueté** y dije **qué NO copiar** de cada una
- [ ] Si la mezcla no cuadró, **partí el trabajo** en dos generaciones y compuse en post
- [ ] El texto se ocupa solo de **acción, encuadre, sujeto y prohibiciones**
- [ ] En video, el clip es lo **más corto** que la idea permite
- [ ] Corregí el color en post de todos modos (módulo `125`)
- [ ] Guardé la referencia usada junto al resultado
- [ ] La marca tiene su **carpeta de referencias** y su **`PROMPT-BASE.txt`**

# 216 — Texto y subtítulos: donde CapCut gana de calle

Si CapCut tuviera que sobrevivir con una sola función, sería esta. Los subtítulos automáticos son la
razón por la que millones de personas dejaron Premiere.

Este módulo cubre los subtítulos automáticos, el texto manual, las plantillas, las animaciones de
texto y —sobre todo— **los límites que nadie te cuenta hasta que te muerden en una entrega**.

Ojo: hay 44 pistas de tipo `text` en tus 51 proyectos y 47 animaciones de subtítulo. El texto es la
columna vertebral de tu contenido. Vale la pena hacerlo bien.

---

## Subtítulos automáticos

### El flujo

1. Pestaña **Texto** → **Subtítulos automáticos**.
2. Elegí el **idioma**. (Crítico, ver abajo.)
3. Elegí la fuente del audio: toda la línea de tiempo, o una pista específica.
4. Opcional: *Eliminar muletillas* (quita "eh", "mmm").
5. **Generar.** Tarda entre 30 segundos y un par de minutos.
6. Te aparecen todos los bloques en una pista de texto, ya sincronizados.

### La precisión real

Con **audio limpio y micrófono cerca**, en español, la precisión anda entre **90 y 95 %**. El español
está entre los idiomas mejor entrenados junto con inglés y chino, así que estás en buena posición.

Con audio de celular en un local con ruido, la precisión cae a 70–80 % y corregir toma más tiempo que
escribir.

**Lo que casi siempre falla, aunque el audio esté perfecto:**

- **Nombres propios.** Marcas, personas, lugares. Siempre.
- **Números y precios.** "diez mil" vs "10.000" vs "10 mil" — sale inconsistente.
- **Anglicismos.** "marketing", "reels", "brief" salen escritos como suenan.
- **Palabras técnicas de tu nicho.**
- **Tildes.** Mejoraron mucho, pero revisá.
- **Signos de apertura** (¿ ¡). A veces los omite.

### La trampa de la variante de idioma

Esto arruina días de trabajo y casi nadie lo sabe:

> **"Español (México)" y "Español (España)" producen transcripciones completamente distintas del
> mismo audio.**

No es una diferencia de ortografía. Son modelos distintos, con vocabularios distintos. Si tu contenido
es colombiano y elegís España, vas a corregir el doble.

**Elegí siempre la variante latinoamericana disponible** (México suele ser la más cercana para
Colombia) y **usá siempre la misma** en todos tus proyectos, para que tus correcciones sean
predecibles.

### El límite de minutos

En el plan **Gratis**, la generación de subtítulos está topada en aproximadamente **10 minutos de
audio por video**. Para reels no es problema. Para un podcast, lo es.

Con Pro el tope se levanta, pero sigue siendo un servicio en la nube: necesitás internet y tu audio
sube a servidores de ByteDance. Para material confidencial de cliente, tenelo en cuenta.

### Corregir rápido

- Doble clic en un bloque de subtítulo → editás el texto ahí mismo.
- **Hay una vista de lista** (el ícono de lista en el panel de texto) donde ves todos los subtítulos
  seguidos y los corregís en cadena, sin ir clip por clip. **Usá esa vista.** Es 5 veces más rápido.
- Si un bloque está mal cortado, podés partirlo (`Ctrl + B`) o arrastrar sus bordes.
- **Corregí el texto antes de estilizar.** Si primero le ponés estilo y después cambiás palabras, a
  veces se te desconfigura.

### Exportar / importar subtítulos

CapCut te deja **exportar los subtítulos** como `.srt` o `.txt` (en el panel de subtítulos, botón de
exportar). Esto es más útil de lo que parece:

- Sirve para subir el `.srt` a YouTube.
- Sirve para corregirlo cómodo en un editor de texto y volverlo a importar.
- Sirve como **transcripción del video**, para reutilizar el contenido como texto.

También **podés importar un `.srt`**, lo que significa que si transcribiste con Whisper (módulo 124),
podés traer esa transcripción —que suele ser más precisa— y usarla acá.

Ese es un flujo híbrido muy bueno: **Whisper transcribe, CapCut estiliza.**

---

## Texto manual

Pestaña **Texto** → **Texto por defecto** → arrastrar a la línea de tiempo.

### Los controles que importan

**Fuente.** CapCut trae muchas, incluidas fuentes marcadas "Pro". Dos advertencias:
- **Podés instalar tus propias fuentes** poniéndolas en el sistema (Windows: `C:\Windows\Fonts`) y
  reiniciando CapCut. Aparecen en la lista. Esto es clave para respetar la marca.
- **No todas las fuentes de CapCut tienen acentos y ñ.** Es el error número uno del contenido en
  español: elegís una fuente linda, escribís "año" y sale "an o" o un cuadrito. **Probá siempre con
  una palabra con tilde y con ñ antes de comprometerte con una fuente.**

**Tamaño.** Para vertical (9:16), el mínimo legible en celular es más grande de lo que creés. Regla:
si en la vista previa a tamaño real de tu monitor te cuesta leerlo, en un celular es ilegible.

**Color y contorno.** Sobre video, el texto blanco puro sobre fondo claro desaparece. Soluciones, en
orden de calidad:
1. **Sombra suave** — la más elegante.
2. **Contorno negro fino** (2–4 px) — la más segura.
3. **Fondo / caja** — la más legible, la menos bonita.
4. Nada — solo si el fondo es controlado.

**Espaciado y alto de línea.** Casi nadie los toca y hacen mucho. Un poco más de alto de línea (1,2–
1,4) hace que dos líneas se lean mejor.

**Posición.** Ojo con las zonas seguras: en Reels y TikTok, la interfaz de la app tapa la parte de
abajo (unos 250 px) y la de arriba. Ver módulo 141.

### Plantillas de texto

Pestaña **Texto** → **Plantillas de texto**. Son diseños ya armados con animación incluida.

Verdad incómoda: **la mayoría se ven a plantilla.** Las que llevan efectos brillantes, degradados y
mucho movimiento gritan "CapCut" y le quitan personalidad a tu marca.

Cuándo sí usarlas:
- Cuando necesitás velocidad y el contenido no es de marca.
- Como **punto de partida**: aplicás la plantilla y después le cambiás fuente, color y tamaño a los
  tuyos. Te quedás con la animación y el layout, y descartás el estilo.

Cuándo no:
- En contenido de marca con identidad definida.
- En anuncios pagos, donde parecerse a todo el mundo cuesta plata.

**La mejor jugada:** armá **tu propio estilo** una vez (fuente de marca, color, contorno, tamaño,
posición) y **guardalo**. CapCut Pro te deja guardar estilos de texto y de subtítulo personalizados.
De ahí en adelante, un clic y tenés tu identidad puesta.

---

## Animaciones de texto

Mismo sistema que el módulo 212: entrada, salida, bucle, combo — pero con catálogo propio para texto.

Lo que ya sabemos de tus datos: **Aparición progresiva** como entrada (49 usos) y **Flash
desactivado** como salida (18). Ese par funciona y no hay razón para cambiarlo.

Regla clave para texto específicamente:

> **La animación de entrada no debe superar el 25 % del tiempo que el texto está en pantalla.**

Si el texto vive 2 segundos, la entrada dura 0,5 s como máximo. Si dura más, el espectador está
esperando en vez de leyendo.

### Animaciones de subtítulo (las de karaoke)

Categoría aparte, específica para subtítulos. Con 47 usos, claramente son parte de tu vocabulario.

| Estilo | Qué hace | Efecto |
|---|---|---|
| **Resaltado / karaoke** | La palabra hablada se colorea | El estándar de TikTok. Muy efectivo. |
| **Palabra por palabra** | Cada palabra aparece al pronunciarse | Alta retención, alto ruido visual. |
| **Escala por palabra** | La palabra hablada crece | Enfático. Cansa rápido. |
| **Máquina de escribir** | Letra por letra | Solo frases muy cortas. |

Por qué funcionan para retención: **obligan al ojo a seguir el ritmo del habla.** El espectador no
puede leer adelante y perder interés; va al paso del audio.

Cuándo NO usarlas:
- Si la sincronización no está perfecta. Se ve peor que un subtítulo estático.
- En bloques largos. Máximo 3–6 palabras por bloque.
- Si ya hay mucho movimiento en pantalla (bucles, efectos, gráficos). Se satura.

---

## El sistema de texto de una marca

Igual que con efectos (211) y animaciones (212): la coherencia gana. Definí de una vez:

| Rol | Fuente | Tamaño | Color | Posición | Animación |
|---|---|---|---|---|---|
| **Gancho** (primeros 2 s) | *(la de marca, bold)* | Grande | *(color de marca)* | Centro-alto | Ninguna o Flash |
| **Subtítulos** | Legible, con ñ y tildes | Medio | Blanco + contorno | Centro-bajo, sobre la zona segura | Karaoke |
| **Dato / cifra** | Bold | Muy grande | Acento | Donde no tape | Ampliar + Flash desactivado |
| **Cierre / CTA** | La de marca | Grande | Acento | Centro | Aparición progresiva |

Escribí esa tabla una vez, guardá los estilos en CapCut, y no la vuelvas a pensar. El tiempo que te
ahorra a lo largo de 50 videos es enorme, y el resultado es que tu cuenta se ve de una sola mano.

---

## Los límites del texto en CapCut

- **No hay texto sobre trayectoria** (que siga una curva).
- **No hay texto en 3D real.** Hay una rotación falsa con perspectiva.
- **No hay tipografía fina:** no hay kerning por par de letras, no hay ligaduras controlables, no hay
  ajuste óptico de márgenes.
- **No hay estilos de párrafo enlazados.** Cambiar la fuente de 30 textos = tocar 30 textos, salvo
  que uses copiar/pegar atributos.
- **No hay corrección ortográfica.** Ninguna. Ni un subrayado rojo. **Vos sos el corrector.**
- **No hay control de viudas y huérfanas** ni corte de línea inteligente. Los saltos de línea los
  ponés a mano con Enter.
- **La animación de texto no se puede editar.** Es la del catálogo o nada. No podés cambiarle la
  curva ni el recorrido.

Ese "no hay corrección ortográfica" merece una advertencia aparte: **una falta de ortografía en un
subtítulo destruye credibilidad más rápido que cualquier problema técnico.** Leé todo en voz alta
antes de exportar.

---

## Truco: copiar atributos entre textos

Igual que con los clips: seleccionás el texto configurado → `Ctrl + C` → seleccionás el destino →
`Ctrl + Alt + V` (*Pegar atributos*). Lleva fuente, tamaño, color, contorno y animación.

Es la única forma sana de mantener consistencia si no guardaste el estilo. Úsala.

---

## Errores comunes

- **Elegir la variante de español equivocada.** España vs México dan transcripciones distintas.
  Elegí la latinoamericana y usá siempre la misma.
- **Elegir una fuente que no tiene ñ ni tildes.** Escribí "año" y "diseño" antes de comprometerte.
- **No corregir los nombres propios.** Es lo que más falla y lo que más se nota. Tu marca mal escrita
  en tus propios subtítulos es lamentable.
- **Estilizar antes de corregir el texto.** Corregí primero, estilizá después.
- **Corregir bloque por bloque en la línea de tiempo.** Usá la vista de lista. Es 5 veces más rápido.
- **Poner los subtítulos demasiado abajo.** La interfaz de Reels y TikTok los tapa. Subilos por
  encima de la zona segura.
- **Texto blanco sin contorno ni sombra sobre video.** Desaparece en cuanto el fondo se aclara.
- **Usar plantillas de texto tal cual vienen.** Se ve a CapCut. Cambiales fuente y color.
- **Animación de entrada más larga que el 25 % del clip.** Nadie alcanza a leer.
- **Karaoke con sincronización mala.** Peor que estático. Verificá antes.
- **Bloques de subtítulo de 12 palabras.** El ojo no alcanza. 3 a 6.
- **No exportar el `.srt`.** Es tu transcripción gratis, sirve para YouTube y para reutilizar el
  contenido. Exportalo siempre.
- **Confiar en que "el texto no tiene errores" sin leerlo en voz alta.** No hay corrector
  ortográfico. Ninguno.

---

## Checklist

- [ ] Elegí la variante latinoamericana de español y es la misma que uso siempre.
- [ ] Corregí el texto **antes** de estilizar, usando la vista de lista.
- [ ] Revisé específicamente: nombres propios, marcas, números, precios, anglicismos.
- [ ] La fuente que elegí muestra bien ñ, tildes y signos de apertura.
- [ ] Los subtítulos están por encima de la zona que tapa la interfaz de la app.
- [ ] Todo texto sobre video tiene contorno o sombra.
- [ ] Los bloques de subtítulo tienen entre 3 y 6 palabras.
- [ ] Las animaciones de entrada no pasan del 25 % de la duración del texto.
- [ ] Si usé karaoke, verifiqué que la sincronización esté bien.
- [ ] Tengo mis estilos de texto guardados y no los reinvento cada vez.
- [ ] Exporté el `.srt` como transcripción.
- [ ] **Leí todo el texto en voz alta buscando errores de ortografía**, porque CapCut no me va a
      avisar.

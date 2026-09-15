# 44 — Tipografía para pantalla pequeña

## El contexto real de lectura

Tu texto no se lee en un monitor de 27 pulgadas a 60 cm. Se lee:

- En una pantalla de **6 pulgadas**,
- a **40-50 cm** de la cara,
- sobre imagen en movimiento que cambia de brillo cada segundo,
- después de pasar por la **compresión de Instagram**, que come detalle fino,
- por alguien que le está dando **medio ojo** mientras hace otra cosa,
- con **0,9 segundos** para leer antes de que cambie.

Toda decisión tipográfica en video vertical sale de ahí. No de lo que se ve bonito en tu monitor.

**La prueba obligatoria:** exporta, mándate el archivo al celular, míralo en el celular. No en el monitor.
Si no hiciste esto, no verificaste nada.

---

## Peso: por qué las fuentes finas están prohibidas

Una tipografía de peso Light o Regular tiene trazos de 2 a 4 px de grosor a tamaño normal. En video pasa esto:

1. **La compresión los ataca primero.** H.264 y VP9 asignan bits donde hay más energía. Un trazo fino
   sobre un fondo con textura es exactamente lo que el codificador decide sacrificar. Los bordes se
   vuelven pastosos.
2. **El movimiento los borra.** Si el fondo se mueve detrás de un trazo de 3 px, el ojo pierde el contorno.
3. **El escalado los mata.** Instagram reescala tu video en varios pasos. Cada paso desgasta el trazo fino.

**Regla:** peso mínimo **Bold (700)**. Óptimo: **Black / Heavy (800-900)**, o una grotesca que ya nace
pesada, como Anton.

### Por qué Anton

Anton es una **grotesca condensada de peso único, muy pesado**. Sus dos virtudes en video vertical:

- **Condensada:** cabe más letra en el mismo ancho. En un lienzo de 1080 px, "PRESUPUESTO" a 150 px cabe
  en una línea con Anton y no cabe con una grotesca normal.
- **Pesada de fábrica:** no necesitas simular negrita (`Bold: -1`), que en ASS engorda artificialmente
  y deforma las letras.

Alternativas reales del mismo territorio: **Archivo Black**, **Oswald** (peso 700, más estrecha),
**Bebas Neue** (solo mayúsculas, más alta y angosta), **League Gothic**. Todas con licencia abierta —
ver `49`.

**Lo que NO sirve:** Montserrat Regular, Poppins Light, Lato, Open Sans, cualquier serif elegante,
cualquier script o manuscrita, cualquier fuente con remates finos.

---

## Tamaño: cuál es el mínimo legible

Sobre lienzo **1080x1920**:

| Tamaño | Uso | Veredicto |
|---|---|---|
| < 50 px | — | **Ilegible en celular.** Nunca |
| 50-70 px | Créditos, letra pequeña legal | Solo si no importa que se lea |
| 70-90 px | Subtítulo de servicio (formato híbrido) | Mínimo funcional |
| 90-120 px | Subtítulo normal, rótulos | Cómodo |
| **140-170 px** | **Golpes de subtitulado, resaltes** | **El punto dulce** |
| 180-260 px | Palabra única de impacto, gancho | Fuerte, úsalo poco |
| > 280 px | Un número, una palabra corta | Solo si es LA palabra |

El valor de referencia probado es **150 px**. Cabe una frase de 2 palabras en una línea, se lee de un
vistazo, y al hacer el pop al 112% (175 px efectivos) sigue sin salirse.

### Si tu lienzo no es 1080x1920

Escala proporcionalmente por el **alto**:

```
tamaño = 150 * (alto_real / 1920)
```

- 720x1280 → 100 px
- 1080x1920 → 150 px
- 2160x3840 → 300 px

Aunque lo más limpio es dejar `PlayResY: 1920` en el `.ass` y que libass escale (ver `43`).

---

## Mayúsculas: sí, pero con cuidado

En video corto, **mayúsculas ganan**. Razones:

- Altura uniforme: el bloque de texto tiene un perímetro rectangular, más fácil de detectar de reojo.
- Más peso visual por píxel.
- No hay ascendentes ni descendentes que compliquen el contorno grueso.

El contra clásico ("las mayúsculas se leen más lento") es cierto en párrafos largos. En **2 palabras**
no aplica: no estás leyendo, estás reconociendo.

**Excepciones donde las minúsculas funcionan mejor:**
- Testimonios y citas: se sienten más humanas, menos publicitarias.
- Rótulos de nombre propio: "Chef Diego Mora" se ve mejor que "CHEF DIEGO MORA" en un lower third serio.
- Textos de más de 6 palabras.

En español, ojo con las **tildes en mayúsculas**: se escriben. "MÁS", no "MAS". Anton las trae. Pero
verifica que tu fuente tenga los glifos acentuados y la `Ñ` — muchas gratuitas no. Ver `49`.

---

## Contorno: por qué 14 px y por qué del color de marca

El contorno (`Outline` en ASS) es lo que hace que tu texto sobreviva **al peor fotograma del video**.

Sin contorno, tu texto blanco:
- sobre cielo → desaparece
- sobre camisa blanca → desaparece
- sobre pared clara → desaparece
- sobre plato de arroz → desaparece

Un solo fotograma donde desaparece arruina el golpe entero, porque el golpe dura 0,9 s y el ojo necesita
los primeros 200 ms para engancharse.

### El grosor

Sobre 150 px de fuente, `Outline: 14` es un contorno que representa ~9% del cuerpo. Eso es **grueso**, y
es a propósito.

| Grosor | Sobre fuente 150 px | Se ve |
|---|---|---|
| 2-4 | Muy fino | El texto se pierde sobre fondos claros. Inútil |
| 6-8 | Estándar de app | Funciona, se ve genérico |
| **12-16** | **Bloque sólido** | **Se lee sobre cualquier cosa. Se ve deliberado** |
| 20+ | Las letras se empastan | Solo con `Spacing` alto y fuente muy abierta |

Con contornos gruesos y fuente condensada, las letras se tocan. Si eso pasa, sube `Spacing` a 4-8 px en
el estilo.

### El color: aquí está la marca

Un contorno **negro** funciona y no dice nada. Un contorno del **color de marca** funciona igual y firma
el video. Es la decisión más barata y más rentable de todo el diseño de texto: cero trabajo extra, y tu
contenido se reconoce sin logo.

```
OutlineColour: &H001C4FE8   -> naranja #E84F1C en BGR
```

**Cuidado con el contraste.** Un contorno amarillo alrededor de texto blanco no separa nada: los dos son
claros. Regla: el contorno tiene que ser **notablemente más oscuro o más saturado** que el relleno. Si tu
color de marca es un pastel claro, usa el negro para el contorno y pon el color de marca en la **sombra**.

---

## Sombra: dura, desplazada, sin difuminar

En ASS, `Shadow: 9` desplaza una copia del texto 9 px hacia abajo-derecha. Con `\blur` en 0 (el default),
esa sombra es **dura**: un borde neto, sin degradado.

Esto es una decisión de estilo, no un descuido.

| Sombra | Se lee como |
|---|---|
| Difuminada (blur alto) | Sombra "realista". Se ve web 2010, se ve sucia, ensucia el contorno |
| **Dura, desplazada 8-12 px** | **Gráfica, deliberada, con peso. Look de cartel** |
| Sin sombra | Plano. Funciona si el contorno es muy grueso |

La sombra dura además hace **doble trabajo de legibilidad**: sobre un fondo del mismo color que el
contorno, la sombra negra sigue separando el texto.

Recomendación: `Shadow: 9`, `BackColour: &H00000000` (negro opaco). Si quieres un look más gráfico
todavía, prueba la sombra **del color de marca** y el contorno negro. Invierte la jerarquía y se ve
distinto sin ser raro.

---

## Contraste: la única medida que importa

Todo lo anterior existe para una cosa: que el texto tenga contraste suficiente contra **cualquier**
fotograma.

### Cómo verificarlo de verdad

No lo juzgues a ojo sobre el fotograma que te gusta. Encuentra el fotograma **peor**.

```bash
ffmpeg -i salida.mp4 -vf "fps=2,scale=270:-1" -y contactos_%04d.png
```

Eso te da una hoja de contactos a 2 fotogramas por segundo, a escala reducida. **A escala reducida es
precisamente donde se ve si el texto se pierde** — porque simula la distancia de lectura real. Míralos
todos. Si en alguno el texto no se distingue, ese es el que hay que arreglar.

Si el problema es un tramo concreto (un plano muy claro), tienes tres salidas:

1. **Subir el contorno** solo en esas líneas: `{\bord20}`.
2. **Oscurecer el fondo** detrás del texto con un degradado (ver `105`).
3. **Mover el texto** a otra parte del cuadro en ese tramo.

La opción 2 es la más profesional. Un degradado sutil de negro al 45% en la franja inferior sube el
contraste de todo el video sin que se note:

```bash
ffmpeg -i entrada.mp4 -filter_complex \
  "[0:v]drawbox=x=0:y=1420:w=1080:h=500:color=black@0.35:t=fill[bg]; \
   [bg]subtitles=texto.ass:fontsdir=fonts[v]" \
  -map "[v]" -map 0:a -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -c:a copy salida.mp4
```

Para un degradado real en vez de una caja plana, se usa una PNG con alfa superpuesta (ver `105`).

---

## Interletraje y ancho de línea

- **`Spacing` (interletraje):** 0 por defecto. Con contorno grueso, subir a **4-8 px** evita que las
  letras se empasten. Con Anton y `Outline: 14`, `Spacing: 4` está bien.
- **Ancho máximo de línea:** deja `MarginL` y `MarginR` en 60 px como mínimo. Con `WrapStyle: 2` el
  quiebre no es automático — si una palabra no cabe, **se sale del cuadro**. Al agrupar los golpes,
  verifica que ninguna combinación de 2 palabras supere el ancho disponible.

Estimación rápida para Anton a 150 px: caben ~13-15 caracteres por línea en 960 px de ancho útil. Si tu
golpe es "PRESUPUESTO MENSUAL" (19 caracteres), no cabe: pártelo con `\N` o reagrupa.

### Verificar el ancho antes de renderizar todo

```bash
ffmpeg -f lavfi -i color=c=black:s=1080x1920:d=1 \
  -vf "subtitles=texto.ass:fontsdir=fonts" -frames:v 1 -y ancho_test.png
```

Sobre negro, sin video, ves solo el texto y detectas desbordes al instante. Repite cambiando el `Start`
del `.ass` para ver distintos golpes, o genera un `.ass` de prueba con todos los golpes apilados.

---

## Jerarquía: cuando hay más de un nivel de texto

Si tienes subtítulo + resalte + rótulo, la jerarquía debe ser **evidente al primer vistazo**. Se construye
con tres palancas, no con una:

| Nivel | Tamaño | Peso/color | Posición |
|---|---|---|---|
| Principal (resalte) | 150-180 px | Blanco + contorno de marca | Centro |
| Secundario (subtítulo) | 80-95 px | Blanco + contorno negro delgado | Abajo |
| Terciario (rótulo, fuente del dato) | 45-60 px | Gris claro, sin contorno | Esquina |

La diferencia de tamaño entre niveles debe ser de **al menos 1,6x**. Si el principal es 150 y el
secundario 130, el ojo no lee jerarquía, lee desorden.

---

## Errores comunes

- **Juzgar la tipografía en el monitor.** Se juzga en el celular. Siempre. Sin excepción.
- **Fuente fina o de peso Regular.** La compresión y el movimiento se la comen. Mínimo Bold, ideal Black.
- **Simular negrita con `Bold: -1` sobre una fuente ya pesada.** ASS engorda artificialmente y deforma las
  letras. Usa el archivo de la fuente en el peso correcto.
- **Texto por debajo de 70 px en vertical.** No se lee en celular, por más bien que se vea en tu pantalla.
- **Contorno de 2-4 px.** Existe pero no protege. El texto sigue desapareciendo sobre fondos claros.
- **Contorno claro sobre relleno claro.** Amarillo alrededor de blanco no separa nada.
- **Sombra difuminada.** Ensucia el contorno y se ve de otra época. Sombra dura, desplazada.
- **Olvidar `Spacing` con contorno grueso.** Las letras se tocan y se lee como una mancha.
- **No verificar el ancho de línea.** Con `WrapStyle: 2` el texto largo se sale del cuadro y libass no
  avisa.
- **Fuente sin tildes ni Ñ.** Muy común en fuentes gratuitas de sitios sospechosos. "MAS" en vez de "MÁS"
  es un error de ortografía en pantalla, no un detalle.
- **Jerarquía con diferencia de tamaño menor a 1,6x.** No se lee como jerarquía, se lee como error.
- **Escoger la fuente por bonita y no por legible.** En video corto la fuente tiene un trabajo: que se lea
  en 0,9 segundos en un celular. Todo lo demás es secundario.

---

## Checklist

- [ ] Vi el video **en el celular**, no en el monitor.
- [ ] La fuente es peso Bold (700) o superior; ideal Black/Heavy o grotesca condensada pesada.
- [ ] Tamaño >= 140 px en lienzo 1080x1920 para el texto principal.
- [ ] Ningún texto por debajo de 70 px salvo letra legal intencional.
- [ ] La fuente tiene tildes y Ñ y las verifiqué renderizando una palabra con ambas.
- [ ] Contorno de 12-16 px sobre fuente de 150 px.
- [ ] El color del contorno es el de marca **y** contrasta contra el relleno.
- [ ] Sombra dura desplazada 8-12 px, **sin difuminar**.
- [ ] `Spacing` ajustado (4-8) si el contorno grueso empasta las letras.
- [ ] Generé la hoja de contactos a escala reducida y **revisé el fotograma peor**.
- [ ] Si había un tramo de bajo contraste, lo resolví (contorno mayor, oscurecer fondo o mover el texto).
- [ ] Verifiqué que ningún golpe se sale del cuadro por ancho, renderizando sobre negro.
- [ ] Si hay varios niveles de texto, la diferencia de tamaño entre ellos es >= 1,6x.
- [ ] El texto sigue legible al escalar al 112% durante el pop.

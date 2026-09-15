# 46 · Texto sobre collage

**Qué resuelve:** el texto se ve perfecto sobre el fondo de prueba y desaparece cuando
entra el recorte. Un collage no tiene un fondo: tiene veinte, y cambian mientras el
texto está en pantalla. Aquí está la medida y la solución.

---

## El problema, medido

Contraste WCAG de la paleta del canal contra distintos fondos (relación de luminancia,
mayor es mejor):

| Color de texto | sobre tinta `#12100C` | sobre gris `#404040` | sobre gris `#808080` | sobre blanco |
|---|---|---|---|---|
| papel `#E6DCC4` | **15,40** | 7,60 | **2,90** ❌ | 1,36 ❌ |
| oro `#E8C547` | **12,51** | 6,18 | **2,35** ❌ | 1,68 ❌ |
| rojo `#E3120B` | 4,36 | **2,15** ❌ | **1,22** ❌ | 4,82 |
| tinta `#12100C` | 1,11 ❌ | 1,83 ❌ | 4,81 | **19,00** |

**Umbrales de trabajo:** ≥ 7:1 para texto de lectura, ≥ 4,5:1 para texto grande
(≥ 76 px). Por debajo de 3:1 el texto no existe.

Dos conclusiones que mandan sobre todo lo demás:

1. **Ningún color de la paleta aguanta solo sobre una foto.** El papel gana en oscuro y
   pierde en medio tono; la tinta gana en claro y pierde en oscuro. Una foto de archivo
   contiene los dos en el mismo cuadro. **Siempre hay que traer fondo propio.**
2. **El rojo `#E3120B` no llega a 5:1 contra nada.** No es un color de texto de
   lectura. Es un color de **marca**: sellos, tachados, subrayados, una palabra suelta
   sobre negro puro. Nunca una frase que haya que leer sobre una foto.

Medirlo sobre el episodio real, no sobre la paleta:

```bash
# recorta la zona donde va a ir el texto y saca su luminancia media y su recorrido
ffmpeg -i salida/_mudo.mp4 -vf "crop=760:120:120:880,signalstats,metadata=print:key=lavfi.signalstats.YAVG" \
  -f null - 2>&1 | grep YAVG | head -20
```

Si `YAVG` cruza la banda 90-170 en algún momento de la vida del texto, ahí hay que
proteger el texto sí o sí.

---

## Contorno vs sombra: gana el contorno

| | Contorno | Sombra proyectada |
|---|---|---|
| Protege | Los 360° del glifo | Un solo lado |
| Fondo que aclara por un lado | Aguanta | Se rompe en el lado sin sombra |
| Fondo con textura fina | Aguanta | Se confunde con la textura |
| Lectura estética | Impreso, estarcido, cartel | Plantilla de presentación |

**El contorno es lo único que trae su propio fondo.** Un contorno de tinta `#12100C`
garantiza 15,4:1 en el borde de cada letra pase lo que pase detrás.

**Grosor:** `fontsize / 12`, redondeado. A 60 px → 5 px. A 140 px → 12 px. Menos de
3 px no protege; más de `fontsize/8` engorda las letras y cierra las contraformas.

En ASS, campo `Outline` con `ScaledBorderAndShadow: yes` (`45`):

```
Style: PEdest,Arial Black,120,&H00C4DCE6,&H0047C5E8,&H000C1012,&H000C1012,-1,0,0,0,100,100,1,0,1,10,0,5,120,120,120,1
```
(`OutlineColour` = tinta `&H000C1012` · `BorderStyle` = 1 · `Outline` = 10)

En HTML/Chrome, el método que no falla — ocho sombras duras a radio 0:

```css
.prot{ --c:#12100C; --g:5px;
  text-shadow:
    var(--g) 0 0 var(--c), calc(var(--g)*-1) 0 0 var(--c),
    0 var(--g) 0 var(--c), 0 calc(var(--g)*-1) 0 var(--c),
    var(--g) var(--g) 0 var(--c), calc(var(--g)*-1) var(--g) 0 var(--c),
    var(--g) calc(var(--g)*-1) 0 var(--c), calc(var(--g)*-1) calc(var(--g)*-1) 0 var(--c);
}
```

Más limpio si sólo se renderiza en Chrome (el trazo va **detrás** del relleno, así que
se declara el doble del grosor visible):

```css
.prot{ -webkit-text-stroke:10px #12100C; paint-order:stroke fill; }
```

**Además del contorno, media sombra.** Contorno para leer, sombra suave para despegar
del plano: `0 6px 18px rgba(0,0,0,.55)`. Es la misma sombra que llevan los recortes de
papel — así el texto pertenece al mismo collage y no flota encima.

---

## Caja de fondo

Cuando el texto es largo (una cita, un párrafo de acta), el contorno no basta: ocho
sombras sobre 40 palabras se lee sucio. Ahí va **caja**.

| Parámetro | Valor |
|---|---|
| Relleno | tinta `#12100C` al **86%** (nunca 100%: se lee como cartón pegado) |
| Margen interior | 28 px horizontal, 20 px vertical |
| Borde y radio | 2 px papel al 30% o ninguno · radio **0**, el canal no redondea |
| Ángulo | −1,5° a +2°, como cualquier papel del collage |
| Sombra | `0 10px 26px rgba(0,0,0,.6)` |

En ASS: `BorderStyle: 3` con `BackColour` a `&H24 0C1012` (`24` hex ≈ 86% opaco).

**La caja tapa el collage.** Es una decisión, no un recurso por defecto: se usa para
documentos y citas (`48`), donde el texto *es* el plano, y no para rótulos ni cifras.

---

## El tachado

Es el gesto de marca del canal: la palabra que deja de ser verdad.

```
   IMPERIO INMOBILIARIO
   ━━━━━━━━━━━━━━━━━━━━   ← barra roja #E3120B
```

| Parámetro | Valor |
|---|---|
| Grosor | `fontsize / 9` (a 90 px → 10 px) |
| Color | rojo `#E3120B`, opacidad 1 |
| Posición | 46% de la altura de mayúscula desde la línea base |
| Desborde | +14 px por cada lado del texto |
| Ángulo | 1,5-3° respecto del texto, nunca paralelo perfecto |
| Entrada | se dibuja de izquierda a derecha en **0,16 s**, curva rápida |
| Sonido | `ob_obturador`, en el fotograma en que arranca |

Se anima con el revelado por máscara de `47`, sobre un PNG que sólo contiene la barra
— nunca con `strikeout` de la fuente, que no se puede animar ni engrosar.

---

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Texto plano sobre foto porque "se ve bien" en el fotograma de prueba | Desaparece en cuanto el fondo se mueve o entra un recorte |
| Sólo sombra proyectada | Se rompe en el lado por el que el fondo aclara |
| Rojo `#E3120B` para una frase sobre foto | No llega a 5:1 contra nada; es color de marca, no de lectura |
| Contorno de 2 px sobre 120 px de cuerpo | No protege nada y se ve como un defecto de render |
| Contorno más grueso que `fontsize/8` | Cierra las contraformas: la `e` y la `a` se vuelven manchas |
| Caja al 100% de opacidad | Se lee como recuadro pegado, no como papel del collage |
| Caja para un rótulo | Tapa el collage por un texto de tres palabras; ahí basta contorno |
| Caja con esquinas redondeadas | Rompe el sistema visual del canal |

## Relacionado

`42` tipografía del canal · `45` subtítulos y destacados · `48` citas y documentos ·
`49` zona segura y tamaños · `77` transiciones de marca · `25` el borde de papel

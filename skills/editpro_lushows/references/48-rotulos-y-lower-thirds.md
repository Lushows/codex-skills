# 48 — Rótulos y lower thirds

## Qué es un rótulo y en qué se diferencia de un golpe

Un **golpe** sigue a la voz: dura 0,9 s, entra con pop, y su trabajo es sostener el pulso.

Un **rótulo** sostiene un dato: dura 3-5 s, entra con calma, y su trabajo es que la información quede.

Son dos cosas distintas y se diseñan distinto. Confundirlas es el error base de este módulo.

| | Golpe (`42`) | Rótulo |
|---|---|---|
| Función | Ritmo y comprensión de la voz | Información que persiste |
| Duración | 0,9 s | 3-5 s |
| Entrada | Pop de 140 ms con sobre-impulso | Fundido o barrido de 250-400 ms |
| Salida | Ninguna (lo reemplaza el siguiente) | Fundido de 200-300 ms |
| Posición | Centro-abajo, fija | Fija en una esquina o franja |
| Tamaño | 150 px | 50-90 px |
| Jerarquía | Es el protagonista | Es servicio, secundario |

**Un rótulo con pop se ve mal.** El sobre-impulso comunica impacto, y un rótulo no impacta: informa.

---

## Los tipos de rótulo

### 1. Lower third de identificación

El clásico: nombre y cargo de quien habla. Entra a los 2-3 segundos de que la persona aparece, dura 4-5
segundos, y sale. **No vuelve** salvo que la persona reaparezca mucho después.

```
DIEGO MORA
Chef ejecutivo · Bogotá
```

Dos niveles: nombre grande, descriptor pequeño. Ratio de tamaño mínimo 1,6x (ver `44`).

### 2. Rótulo de dato

Una cifra, una fuente, un contexto. Aparece cuando se menciona el dato y se va.

```
30% del costo se pierde en merma
```

### 3. Rótulo de sección

Marca un cambio de capítulo. Suele ir en el centro, grande, sobre pantalla parcialmente oscurecida, y
dura 1,5-2 s.

```
PASO 2
Calcula el costo por porción
```

### 4. Marca de agua / firma

Permanente o casi. Logo, handle, o URL. Ver `87`.

### 5. Rótulo de traducción o aclaración

Para audio en otro idioma, jerga, o corregir algo que se dijo mal. Va arriba para no chocar con el
subtitulado de abajo.

### 6. Rótulo de urgencia (comercial)

"Solo hasta el viernes", "Últimas 48 horas". Va en el tercio superior, en color de marca saturado, y
suele acompañar todo el tramo final.

---

## Anatomía de un lower third que funciona

### La geometría

Sobre 1080x1920 vertical:

```
        x=100                              x=980
          ├──────────────────────────────────┤
          │                                  │
 y=1180   │  ████ DIEGO MORA                 │   <- nombre, 90 px
          │  ████ Chef ejecutivo · Bogota    │   <- descriptor, 50 px
 y=1300   │                                  │
          ├──────────────────────────────────┤
```

Componentes:
- **Barra de acento** de 12-16 px de ancho a la izquierda, en color de marca. Es el detalle que separa un
  lower third diseñado de uno improvisado. Cuesta nada.
- **Nombre** en 80-95 px, peso pesado, mayúsculas o caja normal según el tono.
- **Descriptor** en 45-55 px, peso medio, con un separador (`·`) entre elementos.
- **Fondo:** o una caja semitransparente, o nada si el plano detrás es oscuro y limpio.

### Dónde va, en vertical

**No abajo del todo.** El nombre "lower third" viene del video horizontal, donde el tercio inferior está
libre. En vertical, el tercio inferior lo ocupa la interfaz de la plataforma (ver `45`) y el subtitulado.

En vertical, el lower third va **a la altura del pecho de la persona**, es decir alrededor de y=1150-1300.
Ahí no tapa la cara, no choca con el subtitulado de y=1400+, y queda dentro de zona segura.

### En horizontal (16:9, 1920x1080)

Ahí sí va en el tercio inferior: entre y=780 y y=920. Deja 120 px abajo por la barra de controles del
reproductor.

---

## Implementación en ASS

### Lower third de dos niveles

```
[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Nombre,Anton,90,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,2,0,1,5,4,1,120,60,0,1
Style: Cargo,Inter Medium,50,&H00E0E0E0,&H00E0E0E0,&H00000000,&H00000000,0,0,0,0,100,100,1,0,1,3,2,1,120,60,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 1,0:00:02.50,0:00:07.50,Nombre,,0,0,0,,{\pos(120,1200)\alpha&HFF&\t(0,300,0.6,\alpha&H00&)\t(4700,5000,\alpha&HFF&)}DIEGO MORA
Dialogue: 1,0:00:02.65,0:00:07.50,Cargo,,0,0,0,,{\pos(120,1272)\alpha&HFF&\t(0,300,0.6,\alpha&H00&)\t(4700,5000,\alpha&HFF&)}Chef ejecutivo · Bogota
```

Detalles importantes de ese bloque:

- **Alineación 1** (abajo-izquierda) + `\pos`: el punto que das es la esquina inferior izquierda del texto.
- **El descriptor entra 150 ms después** que el nombre. Ese escalonamiento es lo que hace que se sienta
  compuesto y no que dos cosas aparecieron a la vez. Es un detalle de 150 ms que cambia la percepción.
- **`\t(0,300,0.6,...)`** — el `0.6` es la curva de aceleración (ease-out). En una animación de 300 ms
  la curva sí se percibe, a diferencia del pop de 140 ms (ver `43`).
- **La salida** está programada a los 4700-5000 ms de vida de la línea. Recuerda: **tiempos relativos al
  inicio de la línea**, no del video.
- **Layer 1** para que quede por encima del subtitulado si se solapan.

### La barra de acento

ASS puede dibujar formas con `\p1`. Una barra de 14x120 px en color de marca:

```
Dialogue: 0,0:00:02.50,0:00:07.50,Nombre,,0,0,0,,{\pos(100,1290)\p1\1c&H001C4FE8&\bord0\shad0\alpha&HFF&\t(0,220,\alpha&H00&)}m 0 0 l 14 0 14 -120 0 -120{\p0}
```

`\p1` activa el modo dibujo; `m 0 0 l 14 0 14 -120 0 -120` traza el rectángulo (mover a 0,0; línea a
14,0; a 14,-120; a 0,-120); `{\p0}` cierra el modo dibujo. Las coordenadas son relativas al `\pos`.

Alternativa más simple si te da pereza: una caja con `BorderStyle: 3` y un texto de un espacio duro (`\h`).
O superponer un PNG (ver `105`).

### Rótulo con caja de fondo

Cuando el fondo es ruidoso, una caja sólida detrás del texto es más legible que cualquier contorno:

```
Style: Caja,Inter Bold,60,&H00FFFFFF,&H00FFFFFF,&H001C4FE8,&H001C4FE8,0,0,0,0,100,100,2,0,3,16,0,1,120,60,0,1
```

`BorderStyle: 3` convierte `Outline` en el **relleno de la caja** (16 px de aire alrededor del texto) y
`BackColour` en su color. Aquí la caja queda naranja de marca con texto blanco.

---

## Reglas de oro

### 1. Un rótulo a la vez

Nunca dos rótulos simultáneos. Si necesitas dar dos datos, ponlos en secuencia o júntalos en uno.

### 2. El rótulo no compite con el subtitulado

Si hay subtitulado abajo, el rótulo va **arriba o a media altura**, más pequeño, sin animación agresiva,
y con menos contraste (gris claro en vez de blanco puro). Uno de los dos tiene que ceder jerarquía, y
siempre cede el rótulo.

### 3. Aparece cuando hace falta, no antes

El lower third de identificación entra **2-3 segundos después** de que la persona apareció, no en el
fotograma uno. Que el espectador la vea primero, se pregunte quién es, y ahí llegue la respuesta. Poner
el rótulo al mismo tiempo que el plano desperdicia el gesto.

Un rótulo de dato entra **cuando se menciona el dato**, no antes ni tres segundos después.

### 4. Se va

Un lower third que se queda 20 segundos deja de informar y empieza a estorbar. 4-5 segundos es el rango.
La excepción es la marca de agua (`87`), que es otra cosa.

### 5. Ortografía y datos verificados

Un rótulo con el cargo mal escrito o el apellido cambiado es peor que no poner rótulo. Es la parte del
video donde el error es más visible y más caro. Verifica el nombre con la persona.

Y en español: **tildes**. "Diego Martínez", no "Diego Martinez". Si tu fuente no tiene los glifos
acentuados, cambia de fuente (ver `49`).

### 6. Consistencia entre piezas

El lower third es un elemento de identidad. En el episodio 8 tiene que verse igual que en el 1: misma
posición, mismo tamaño, mismo color, misma animación. Guárdalo como plantilla (ver `88`).

---

## Rótulos en video horizontal (16:9)

Cuando produces para YouTube largo o TV, cambian las medidas pero no los principios.

Sobre 1920x1080:

```
Style: NombreH,Anton,64,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,2,0,1,4,3,1,160,60,0,1
Style: CargoH,Inter Medium,38,&H00E0E0E0,&H00E0E0E0,&H00000000,&H00000000,0,0,0,0,100,100,1,0,1,2,2,1,160,60,0,1

Dialogue: 1,0:00:02.50,0:00:07.50,NombreH,,0,0,0,,{\pos(160,860)\alpha&HFF&\t(0,300,0.6,\alpha&H00&)\t(4700,5000,\alpha&HFF&)}DIEGO MORA
Dialogue: 1,0:00:02.65,0:00:07.50,CargoH,,0,0,0,,{\pos(160,910)\alpha&HFF&\t(0,300,0.6,\alpha&H00&)\t(4700,5000,\alpha&HFF&)}Chef ejecutivo · Bogota
```

Margen izquierdo de 160 px (zona segura de título en broadcast: 10% de cada borde). Deja 120 px abajo por
la barra de controles.

---

## Verificación

```bash
ffmpeg -ss 4.0 -i salida.mp4 -frames:v 1 -y rotulo_test.png
```

Abre el PNG y revisa:
- ¿El nombre está bien escrito, con tildes?
- ¿El descriptor se lee o es demasiado pequeño?
- ¿Está dentro de la zona segura?
- ¿Choca con el subtitulado?
- ¿Se lee sobre ese fondo concreto?

Y luego mira el fotograma justo antes de la entrada y justo después de la salida, para confirmar que la
animación ocurre y que no quedó nada colgado.

---

## Errores comunes

- **Poner pop al rótulo.** El sobre-impulso comunica impacto; un rótulo informa. Fundido de 250-400 ms.
- **Nombre y descriptor entrando al mismo tiempo.** Escalona 150 ms y se siente diez veces mejor.
- **Lower third en el tercio inferior en video vertical.** Ahí está la interfaz y el subtitulado. En
  vertical va a la altura del pecho, y=1150-1300.
- **Dos rótulos simultáneos.** Uno a la vez, siempre.
- **Rótulo que compite con el subtitulado.** El rótulo cede: más pequeño, menos contraste, sin animación
  agresiva.
- **Poner el lower third en el fotograma uno del plano.** Deja 2-3 segundos para que se genere la
  pregunta.
- **Dejarlo 20 segundos.** Después de 5 segundos ya no informa, estorba.
- **Nombres sin tilde.** "Martinez" en vez de "Martínez" es un error de ortografía en pantalla.
- **No verificar el nombre y el cargo con la persona.** Es el error más caro y el más visible.
- **Cambiar el diseño del rótulo entre episodios.** Es un elemento de identidad. Se congela y se
  reutiliza.
- **Confundir tiempos relativos y absolutos en la salida del `\t`.** Los milisegundos cuentan desde el
  inicio de la línea.
- **Descriptor con el mismo tamaño que el nombre.** Sin jerarquía no hay lectura. Mínimo 1,6x de
  diferencia.
- **Fondo sin contraste.** Sobre plano claro y ruidoso, ni el mejor contorno salva. Usa caja
  (`BorderStyle: 3`) o oscurece la franja.

---

## Checklist

- [ ] El rótulo entra con **fundido de 250-400 ms**, no con pop.
- [ ] Nombre y descriptor entran **escalonados** (~150 ms de diferencia).
- [ ] La animación de entrada usa curva ease-out (`\t(0,300,0.6,...)`).
- [ ] Tiene salida programada, con tiempos **relativos al inicio de la línea**.
- [ ] Duración total: 4-5 segundos.
- [ ] Entra 2-3 segundos después de que aparece la persona o se menciona el dato.
- [ ] En vertical: está a la altura del pecho (y≈1150-1300), no en el tercio inferior.
- [ ] Está dentro de la zona segura de todas las plataformas donde publico (`45`).
- [ ] No hay dos rótulos simultáneos.
- [ ] Si hay subtitulado, el rótulo cede jerarquía: más pequeño, menos contraste, `Layer` distinto.
- [ ] Diferencia de tamaño nombre/descriptor >= 1,6x.
- [ ] Lleva la barra de acento o algún elemento de marca.
- [ ] **El nombre y el cargo están verificados con la persona.**
- [ ] Tildes y Ñ correctas, y la fuente las renderiza (verificado en un fotograma).
- [ ] El diseño coincide con el de las piezas anteriores de la serie.
- [ ] Extraje un fotograma con el rótulo visible y lo revisé.

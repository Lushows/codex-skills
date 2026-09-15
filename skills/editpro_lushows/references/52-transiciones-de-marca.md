# 52 — Transiciones de marca: convertir la identidad en recurso técnico

> La idea de este módulo es la más rentable de todo el bloque 5. Si la aplicas bien, tu cliente deja
> de tener "transiciones" y pasa a tener **una firma**.

---

## El principio

La mayoría de las marcas tienen un elemento gráfico que se repite: una franja, un patrón de damero,
un arco, una diagonal, una forma del logotipo, una textura, una trama de puntos. Ese elemento vive en
el empaque, en la web, en las piezas de Instagram — y casi siempre **muere ahí**, sin llegar al video.

La jugada es sencilla y casi nadie la hace:

> **Ese elemento gráfico se convierte en tu transición.**

Cuando lo haces, pasan tres cosas al mismo tiempo:

1. **Resuelves el corte.** Técnicamente hace lo que hace un barrido: tapa el cambio de plano.
2. **Refuerzas la marca.** Cada vez que el video cambia de tema, la marca aparece. Sin logo, sin
   locución, sin decir nada. Puro reconocimiento.
3. **Dejas de verte genérico.** Nadie más tiene esa transición, porque nadie más tiene esa franja.

Es identidad y recurso técnico a la vez. Ese doble uso es lo que la hace tan buena.

---

## Ejemplos reales de la idea

| Marca / rubro | Elemento repetitivo | Cómo se vuelve transición |
|---|---|---|
| Cafetería con damero en el piso y en las cajas | Damero blanco y negro | Una franja de damero barre el cuadro y detrás queda el plano nuevo |
| Marca deportiva con tres barras diagonales | Barras diagonales | Tres barras entran desfasadas y tapan el cuadro |
| Bar con chapa de cerveza en el logo | Círculo dentado | El círculo dentado se cierra sobre el plano viejo y se abre sobre el nuevo |
| Software con esquinas redondeadas y cobalto | Rectángulo cobalto | Un rectángulo de esquinas redondeadas entra desde abajo, como una tarjeta |
| Restaurante con arco en la fachada | Arco | El plano nuevo se revela dentro de la silueta del arco, que crece |
| Marca de hongos con trama orgánica | Trama de esporas | Puntos que crecen desde varios centros hasta cubrir, y se van sobre el plano nuevo |

**La prueba de que está bien elegido:** si le muestras la transición sola, sin video, a alguien que
conoce la marca, y la reconoce. Si no la reconoce, elegiste un elemento que no es característico.

---

## Cómo elegir el elemento (los cuatro filtros)

No cualquier cosa del manual de marca sirve. El elemento debe cumplir:

### 1. Es repetitivo, no único

Sirve un patrón, una franja, una trama, una forma modular. **No sirve el logotipo completo.** El logo
como transición se lee a publicidad de los noventa y satura: si el logo aparece 6 veces en 40 segundos,
la marca se vuelve insoportable.

> Regla: la transición usa el **sistema** de la marca, no la **firma** de la marca.

### 2. Cubre el cuadro sin ambigüedad

En algún fotograma tiene que tapar el 100% de la pantalla. Ese es el fotograma donde ocurre el corte
real: es lo que oculta el cambio. Si el elemento nunca cubre del todo, no es transición, es un adorno
que pasa por encima.

### 3. Se lee a 3 fotogramas

La transición va a durar entre 0,2 y 0,4 segundos, o sea entre 6 y 12 fotogramas, y la mitad de ese
tiempo está entrando o saliendo. Si tu elemento necesita medio segundo para entenderse, no funciona.
Formas simples, contraste alto, pocos detalles.

### 4. Funciona en el color de marca sobre cualquier fondo

Tu transición va a pasar sobre planos claros y oscuros. Si el elemento es beige claro y el video tiene
planos de cocina blanca, desaparece. Prueba el elemento sobre el fotograma más claro y el más oscuro
del material antes de comprometerte.

---

## Cómo se construye (el método correcto, verificado)

Hay dos formas. Una es lenta y mala; la otra es rápida y buena. Empiezo por la buena.

### Método A — pre-renderizar el elemento como PNG con transparencia (recomendado)

Generas el elemento **una sola vez** como imagen con canal alfa, y después solo lo mueves con
`overlay`. Es rapidísimo porque el cálculo pesado se hace una vez, no en cada fotograma.

**Paso 1: crear la franja de damero en el color de la marca, con fondo transparente**

```bash
ffmpeg -y -f lavfi -i "color=c=0xE10600:s=768x360" \
       -f lavfi -i "color=c=white:s=768x360" \
  -filter_complex \
"[1:v]format=gray,geq=lum='if(lt(mod(floor(X/48)+floor(Y/48),2),1),255,0)'[mascara];\
 [0:v][mascara]alphamerge[franja]" \
  -map "[franja]" -frames:v 1 franja.png
```

Qué hace, en simple:
- La primera entrada es un rectángulo del color de la marca (`0xE10600`).
- La segunda se convierte en una **máscara**: `geq` pinta blanco o negro en casillas de 48×48 píxeles
  alternadas. Eso es el damero.
- `alphamerge` usa esa máscara como transparencia: donde la máscara es blanca, el color se ve; donde
  es negra, es transparente.
- Resultado: un PNG de damero rojo con huecos transparentes.

El ancho `768` no es capricho: la franja debe ser **más ancha que el video** para que en algún momento
lo cubra por completo. Regla: ancho de la franja ≥ ancho del video × 1,2.

**Paso 2: pasar la franja por encima del punto de corte**

Supongamos que el corte duro está en el segundo 4,0 de un video ya pegado, y quieres que la franja
barra entre 3,75 y 4,25 (medio segundo):

```bash
ffmpeg -y -i pegado.mp4 -i franja.png -filter_complex \
"[0:v][1:v]overlay=x='if(between(t,3.75,4.25), -768+((t-3.75)/0.5)*1408, -3000)':y=0:eval=frame[v]" \
  -map "[v]" -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p marca.mp4
```

Cómo se lee la expresión de `x`:
- `between(t,3.75,4.25)` → solo durante ese medio segundo la franja está en pantalla.
- `-768` → empieza totalmente fuera por la izquierda.
- `((t-3.75)/0.5)` → un número que va de 0 a 1 durante la transición.
- `*1408` → recorre 1408 px = 640 (ancho del video) + 768 (ancho de la franja). Así entra completa,
  cubre, y sale completa.
- `-3000` → el resto del tiempo la mandas muy lejos, fuera del cuadro. Es más barato que activarla
  y desactivarla.
- `eval=frame` → **obligatorio.** Sin esto, ffmpeg evalúa la posición una sola vez al principio y la
  franja se queda quieta.

Verificado: el render conserva la duración original (8,000 s) y es prácticamente instantáneo.

### Método B — calcular el elemento en cada fotograma con `geq` (evítalo)

Se puede hacer todo en un solo comando poniendo el `geq` dentro del `filter_complex` del video. Lo
probé: **es entre 50 y 100 veces más lento** y el resultado es idéntico. `geq` evalúa una expresión por
píxel y por fotograma; en un video 1080×1920 a 30 fps eso son 62 millones de evaluaciones por segundo
de video.

> Regla del oficio: **lo que no cambia, se pre-renderiza.** Vale para transiciones de marca, para
> logos, para tramas y para cualquier gráfico fijo.

---

## Variantes que funcionan

### Barrido con franja (la base)

Es lo de arriba. Una franja del patrón cruza el cuadro. Simple, legible, sirve en el 80% de los casos.

### Doble franja desfasada

Dos franjas del mismo patrón que entran con 3 fotogramas de diferencia. Se siente más rico y más caro
sin costar nada más. Solo duplicas el `overlay`:

```bash
ffmpeg -y -i pegado.mp4 -i franja.png -i franja.png -filter_complex \
"[0:v][1:v]overlay=x='if(between(t,3.75,4.25), -768+((t-3.75)/0.5)*1408, -3000)':y=0:eval=frame[p1];\
 [p1][2:v]overlay=x='if(between(t,3.85,4.35), -768+((t-3.85)/0.5)*1408, -3000)':y=180:eval=frame[v]" \
  -map "[v]" -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p doble.mp4
```

La segunda va a media altura (`y=180`) y arranca 0,1 s después. Ajusta a tu resolución.

### El elemento que crece desde el centro

En vez de barrer, el elemento **crece** hasta cubrir y luego se abre sobre el plano nuevo. Se hace con
una máscara animada y `maskedmerge` (ver `58-mascaras-y-recortes.md`), que es el módulo hermano de
este.

### La transición que es literalmente el color de marca

La más simple de todas y de las que mejor funciona en anuncios: un fotograma completo del color de la
marca entre plano y plano. Dos o tres fotogramas, no más.

```bash
ffmpeg -y -f lavfi -i "color=c=0xE10600:s=1080x1920:r=30:d=0.1" \
  -c:v libx264 -preset veryfast -pix_fmt yuv420p golpe_color.mp4
```

Después lo pegas entre los dos planos con `concat`. Es el "flash" del módulo `53`, pero en el color de
la marca en vez de blanco. Cuesta cero y se ve deliberado.

---

## Cuántas veces usarla

Aquí es donde la buena idea se arruina. La transición de marca es fuerte; **si la usas en cada corte
se convierte en el video**.

| Duración de la pieza | Veces que puede aparecer |
|---|---|
| Reel / TikTok de 15–30 s | 1 vez, máximo 2 |
| Anuncio de 45–60 s | 2 – 3 |
| Video corporativo de 2–3 min | 3 – 5, una por bloque |
| Serie de episodios | 1 por episodio, siempre en el mismo lugar estructural |

Y siempre en un cambio de **bloque**, nunca dentro de una idea. Si la usas para separar dos planos que
cuentan lo mismo, estás partiendo una frase.

---

## La relación con directorcreativo

Este módulo aplica identidad; **no la inventa**. Si el proyecto no tiene un sistema visual definido —
si no sabes cuál es el elemento repetitivo de la marca porque la marca no tiene uno — la transición de
marca no se puede construir.

> Pasa primero por `directorcreativo_lushows` para definir el sistema (patrón, color exacto, formas),
> y vuelve acá con los archivos. Inventarte un damero que no está en el manual de marca es peor que
> no poner nada: creas un elemento que después nadie sostiene en las otras piezas.

Lo que necesitas traer de allá:
- El código hexadecimal exacto del color (no "rojo").
- El patrón o forma en vector o en PNG de alta resolución.
- La proporción del módulo (¿el damero es de casillas cuadradas? ¿de qué tamaño relativo?).

---

## Errores comunes

- **Usar el logotipo completo como transición.** Satura y se ve a publicidad vieja. La transición usa
  el sistema gráfico, no la firma.

- **Elegir un elemento que no cubre el cuadro.** Si nunca tapa el 100%, no está escondiendo el corte:
  es un adorno que pasa. El corte se ve igual.

- **Calcular el patrón con `geq` en cada fotograma.** Render eterno para un resultado idéntico al de
  pre-renderizar un PNG una vez.

- **Olvidar `eval=frame` en el `overlay`.** La franja se queda congelada en su posición inicial y
  parece un error de render. Es el fallo más frecuente de este módulo.

- **Hacer la franja del mismo ancho que el video.** Nunca llega a cubrir del todo porque en el momento
  en que su borde derecho llega al borde derecho, el izquierdo ya se salió. Hazla 1,2× más ancha
  como mínimo.

- **Usarla en cada corte.** La marca deja de ser un acento y se vuelve el contenido.

- **Elegir un elemento con poco contraste sobre el material.** Beige sobre cocina blanca = invisible.
  Prueba sobre el fotograma más claro y el más oscuro antes de decidir.

- **Inventarse el elemento gráfico.** Si no está en el manual de marca, no es de la marca. Es tuyo,
  y se va a caer en la siguiente pieza que haga otra persona.

- **Usar un color aproximado.** "Como rojito" no. El hexadecimal exacto o no lo hagas.

---

## Checklist

- [ ] El elemento sale del sistema visual real de la marca (manual, empaque, web), no de mi cabeza.
- [ ] Tengo el color en hexadecimal exacto y el patrón en alta resolución.
- [ ] Es un elemento repetitivo del sistema, **no** el logotipo completo.
- [ ] En algún fotograma cubre el 100% del cuadro.
- [ ] La franja es al menos 1,2× más ancha (o alta) que el video.
- [ ] Se lee en 3 fotogramas: forma simple, contraste alto.
- [ ] Probé el elemento sobre el fotograma más claro y el más oscuro del material.
- [ ] Pre-rendericé el elemento como PNG con alfa; no estoy calculando `geq` por fotograma.
- [ ] El `overlay` lleva `eval=frame`.
- [ ] La transición dura entre 0,2 y 0,4 s.
- [ ] Aparece solo en cambios de bloque, y no más veces de las que permite la duración de la pieza.
- [ ] Verifiqué en el render final que cae exactamente sobre el corte y no medio segundo antes (`98`).

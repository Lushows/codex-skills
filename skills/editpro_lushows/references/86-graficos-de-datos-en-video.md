# 86 — Gráficos de datos en video

**Qué resuelve:** tienes un número que vender ("ahorras 3 horas a la semana", "el 78% no lo sabe",
"$10.000") y lo pusiste en pantalla como si fuera una diapositiva. Nadie lo procesó. Este módulo enseña
a **hacer que un dato se entienda en dos segundos**, que es todo el tiempo que tienes, y a no convertir
tu reel en un Excel en movimiento.

---

## 1. La regla de los 2 segundos

En video social, un dato tiene **dos segundos** para entrar. No dos segundos en pantalla: dos segundos
para que el espectador lo **entienda**. Si en el segundo 2 todavía está descifrando qué mira, se fue.

De ahí salen tres consecuencias que gobiernan todo el módulo:

1. **Un dato por pantalla.** Uno. Si tienes tres datos, son tres momentos, no un cuadro con tres.
2. **El número protagonista es enorme.** Ocupa entre el 25% y el 40% del ancho del cuadro.
3. **La etiqueta es corta y va debajo.** Tres o cuatro palabras. "de tus ingresos", no "porcentaje
   promedio sobre los ingresos brutos mensuales".

> **El test:** enséñale un fotograma del gráfico a alguien durante dos segundos y quítalo. Si no te
> puede repetir el dato, el gráfico está mal, no la persona.

---

## 2. Por qué NO hacer un Excel en movimiento

El error más común es traer al video la lógica de una presentación: ejes, rejilla, leyenda, título,
cuatro series de datos, escala con decimales. Eso funciona en una diapositiva donde el espectador tiene
tres minutos y puede preguntar. En un reel es ruido.

| Lo que trae un gráfico de Excel | Qué pasa en video |
|---|---|
| Ejes con marcas y números | ruido ilegible en pantalla de 6 pulgadas |
| Leyenda con 4 colores | nadie va a cruzar leyenda con barras en 2 segundos |
| Título arriba | duplica lo que ya dice la voz |
| Rejilla de fondo | ensucia y no aporta |
| Decimales | "el 78,4%" se lee igual de bien como "78%" y ocupa menos |
| 4 series comparadas | ninguna se entiende |

**Lo que sí va en un gráfico de video:**

- El número, gigante.
- Una etiqueta corta.
- **Como máximo** un elemento de comparación (una barra contra otra, un antes contra un después).
- Color de marca en el dato protagonista; gris en lo demás.

Todo lo demás sobra. Si te duele quitar la rejilla, es porque estás pensando como analista y no como
editor.

---

## 3. El contador animado: el recurso rey

Un número que **sube** retiene muchísimo más que un número que aparece. El ojo se queda a ver dónde
para. Es el truco más rentable del módulo y se hace con una sola línea de `drawtext`.

```bash
ffmpeg -i base.mp4 -vf "drawtext=\
fontfile='C\:/Windows/Fonts/arialbd.ttf':\
text='%{eif\:clip(floor(1250*(t-1.0)/1.2)\,0\,1250)\:d}':\
fontsize=210:fontcolor=white:\
x=(w-text_w)/2:y=(h-text_h)/2-120:\
enable='gte(t,1.0)'" \
  -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

Cómo se lee la parte del número:

- `%{eif\:...\:d}` — "evalúa esta expresión y escríbela como entero (`d`)". Los `:` y las `,` de adentro
  van escapados con `\` porque `drawtext` los usa como separadores.
- `floor(1250*(t-1.0)/1.2)` — sube de 0 a 1250 en 1,2 segundos a partir del segundo 1,0.
- `clip(...,0,1250)` — lo recorta para que no siga subiendo después. **Sin esto el contador se dispara
  al infinito.** Es el error clásico.

### Con frenado (que se sienta vivo)

El contador lineal sube uniforme y se ve mecánico, igual que cualquier movimiento lineal (`84`). Con
frenado, arranca rápido y se demora en llegar a la cifra final: se siente como una máquina que se está
deteniendo.

```bash
text='%{eif\:clip(floor(1250*(1-pow(1-clip((t-1.0)/1.2\,0\,1)\,3)))\,0\,1250)\:d}'
```

### Con separador de miles

`drawtext` no formatea miles. Se resuelve armando el texto por partes: un `drawtext` para los miles y
otro para los cientos, con un punto fijo en medio. Para cifras hasta 999.999:

```bash
-vf "drawtext=text='%{eif\:clip(floor(1250*(t-1)/1.2/1000)\,0\,1)\:d}':fontsize=210:x=380:y=800,\
drawtext=text='.':fontsize=210:x=470:y=800,\
drawtext=text='%{eif\:clip(mod(floor(1250*(t-1)/1.2)\,1000)\,0\,999)\:d}':fontsize=210:x=510:y=800"
```

Se ve un poco artesanal, y lo es. Si necesitas formato fino de moneda, la ruta limpia es generar el
texto de cada fotograma fuera y usar un archivo de subtítulos ASS (`43`), o prerrenderizar el contador
como capa con alfa.

### El símbolo va aparte

El `$` o el `%` **no se animan**. Van fijos, en un `drawtext` propio, pegados al número. Si los metes
dentro del contador, bailan mientras el número cambia de ancho y se ve mal.

```bash
drawtext=text='\$':fontsize=210:fontcolor=white:x=(w-text_w)/2-260:y=(h-text_h)/2-120
```

---

## 4. Barras

Una barra sirve para **una** cosa: comparar dos cantidades. Si tienes cinco, no es video, es informe.

```bash
ffmpeg -i base.mp4 -filter_complex "\
[0:v]drawbox=x=120:y=980:w=840:h=96:color=0x2A2A2A@0.85:t=fill,\
drawbox=x=120:y=980:w='840*(1-pow(1-clip((t-1.2)/0.9\,0\,1)\,3))':h=96:color=0x2742F5@1:t=fill,\
drawtext=fontfile='C\:/Windows/Fonts/arialbd.ttf':text='78%%':fontsize=110:fontcolor=white:x=120:y=820:\
alpha='clip((t-1.5)/0.3\,0\,1)'[vout]" \
  -map "[vout]" -map 0:a -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p salida.mp4
```

Lo que hace:

1. Dibuja la **canaleta** (la barra vacía, gris oscuro al 85%). Sin canaleta, la barra que crece no
   tiene contra qué compararse y no se lee como proporción.
2. Dibuja la barra de marca cuyo ancho crece con **frenado** (`1-pow(1-p,3)`).
3. El porcentaje entra con opacidad animada, **después** de que la barra arrancó (desfase, `85`).

Notas prácticas:

- `%%` — en `drawtext` el `%` es carácter especial. Se escribe doble.
- `t=fill` — rellena la caja. Sin eso solo dibuja el contorno.
- La barra crece **de izquierda a derecha** porque así se lee en español. Una barra que crece de derecha
  a izquierda se siente al revés aunque nadie lo sepa explicar.

### Barra de comparación (antes / después)

```bash
[0:v]drawbox=x=120:y=900:w='300*(1-pow(1-clip((t-1.2)/0.7\,0\,1)\,3))':h=90:color=0x6B6B6B@1:t=fill,\
drawbox=x=120:y=1030:w='820*(1-pow(1-clip((t-1.5)/0.9\,0\,1)\,3))':h=90:color=0x2742F5@1:t=fill
```

El "antes" en gris, corto y primero. El "después" en color de marca, largo y con 0,3 s de desfase. Ese
desfase es lo que hace la comparación **narrativa** en vez de simultánea: el ojo ve el antes, y entonces
crece el después. Ver `155`.

---

## 5. El anillo de progreso

Un círculo que se llena. Se ve caro y en ffmpeg puro es incómodo (no hay filtro de arco). Dos rutas
honestas:

**Ruta A — prerrenderizar el anillo como secuencia PNG con alfa** desde una herramienta que sí dibuje
arcos, y superponerlo (`80`). Es lo que hace un pipeline serio (`88`).

**Ruta B — trampa visual con una máscara girando.** Funciona para anillos simples y se hace con
`rotate` + `overlay`, pero es frágil. Si el anillo importa, ve por la ruta A.

**Ruta C — cambiar de gráfico.** Muchas veces el anillo no aporta nada que la barra no dé, y la barra
cuesta una línea. Pregúntate si el círculo era necesidad o capricho.

---

## 6. Cómo entra un dato (la coreografía)

Un dato no "aparece". Un dato **se presenta**. La secuencia que funciona, en orden:

| Momento | Qué pasa | Duración |
|---|---|---|
| 0,00 | El fondo se oscurece un poco (`eq=brightness`) | 0,25 s |
| 0,10 | Entra el contenedor / la canaleta | 0,25 s |
| 0,25 | Arranca el número o la barra | 0,9 – 1,2 s |
| 0,60 | Entra la etiqueta debajo | 0,25 s |
| 1,50 | Todo quieto. **El respiro.** | 0,8 – 1,2 s |
| 2,60 | Sale todo junto, rápido | 0,25 s |

**El respiro es obligatorio.** Un contador que llega a su cifra y desaparece de inmediato no deja que
nadie lea el resultado. Todo el contador fue en vano. Mínimo 0,8 segundos quieto al final.

Oscurecer el fondo mientras el dato manda (puesta en escena, `85`):

```bash
[0:v]eq=brightness='-0.20*clip((t-1.0)/0.25,0,1)*clip((4.2-t)/0.25,0,1)'[bg]
```

Baja el brillo desde el segundo 1,0 y lo devuelve al 4,2. El producto de los dos `clip` hace la entrada
y la salida en una sola expresión.

---

## 7. Dónde va y de qué tamaño

En vertical 1080x1920:

- **El número protagonista:** centrado horizontalmente, entre `y=700` y `y=1100`. Tamaño de fuente de
  **180 a 260 px**. Sí, es enorme. Tiene que serlo.
- **La etiqueta:** justo debajo, 60–80 px, en el mismo eje. Peso medio, no bold: no compite.
- **Nunca** por debajo de `y=1540` (zona de interfaz y subtítulos, ver `45`).
- **Nunca** encima de la cara si hay alguien hablando (`82`).

**Contraste:** el número va en blanco puro o en el color de marca sobre fondo oscurecido. Si el fondo es
claro, el número lleva **sombra o contorno** o desaparece:

```bash
drawtext=...:fontcolor=white:borderw=6:bordercolor=black@0.55:shadowx=0:shadowy=5:shadowcolor=black@0.35
```

---

## 8. La honestidad del dato

Esto es parte del oficio, no un apéndice moral. Un gráfico en video es persuasión pura: el espectador no
tiene tiempo de auditarlo. Por eso:

- **La barra empieza en cero.** Siempre. Empezar una barra en 60 para que la diferencia se vea enorme es
  mentir con geometría. Si te lo piden, di que no y explica por qué (`197`).
- **Los porcentajes tienen denominador.** "78%" de qué y sobre cuántos. Si el dato salió de una encuesta
  de 12 personas, no es un dato: es una anécdota con porcentaje.
- **La fuente va en pantalla** si el dato es de un tercero. Chiquita, abajo, 32–38 px. No estorba y te
  cubre.
- **No inventes cifras redondas.** Si el ahorro real es de $47.300, no pongas "$50.000". El día que
  alguien haga la cuenta, perdiste más de lo que ganaste.
- **Los números de la propia empresa se verifican con quien los tiene.** Un dato mal puesto en un anuncio
  pagado es un problema legal, no un error de edición.

Si el número necesita cálculo o proyección, eso no lo hace el editor: lo hace
`Matematicas_lushows` o `economist_lushows`. Tu trabajo es que se entienda, no inventarlo.

---

## 9. Cuándo el gráfico sobra

- **Cuando la voz ya dice el número claro.** Un número dicho + escrito grande basta. La barra, el
  anillo y el icono son adorno.
- **Cuando el dato no es sorprendente.** Un gráfico existe para subrayar algo que sacude. "El 52% de los
  restaurantes usa Excel" no sacude a nadie. "7 de cada 10 restaurantes cierran antes de los 3 años" sí.
- **Cuando son más de dos datos seguidos.** El tercero ya no lo procesa nadie. Elige el mejor.
- **Cuando el video es un testimonio.** Un gráfico encima de alguien contando su experiencia rompe el
  registro (`154`).

---

## Errores comunes

1. **Meter tres datos en la misma pantalla.** Ninguno entra. Un dato por momento.
2. **Traer el gráfico de Excel tal cual** con ejes, leyenda, rejilla y título. Ruido ilegible.
3. **Número pequeño.** Si en el fotograma a 300 px de alto no lo lees, en el celular tampoco.
4. **Contador sin `clip`.** El número sigue subiendo después de llegar y se dispara al infinito.
5. **Contador sin respiro final.** Llega a la cifra y desaparece. Nadie alcanzó a leerla. Mínimo 0,8 s
   quieto.
6. **Animar el `$` o el `%` junto al número.** Bailan mientras el número cambia de ancho. Van aparte.
7. **Olvidar el `%%`** en `drawtext`. El `%` solo es carácter especial y te rompe el filtro o desaparece.
8. **Olvidar `t=fill` en `drawbox`.** Te dibuja el contorno en vez de la barra.
9. **Barra sin canaleta.** No hay contra qué compararla; deja de leerse como proporción.
10. **Barra que crece linealmente.** Igual que cualquier movimiento lineal, se ve barata. `1-pow(1-p,3)`.
11. **Barra que no empieza en cero.** Es manipulación, no diseño.
12. **Escapes mal puestos en `%{eif...}`.** Los `:` y las `,` de adentro van con `\`. Si el filtro falla
    o el número sale en cero, revisa eso antes que nada.
13. **Poner el dato en la zona muerta de la plataforma.** Queda tapado por la interfaz.
14. **Inventar o redondear la cifra "para que suene mejor".** Un dato mal puesto en pauta es un problema
    legal.

---

## Checklist

Antes de dar por bueno un gráfico en video:

- [ ] Hay **un solo dato** protagonista en pantalla.
- [ ] El número mide entre el **25% y el 40% del ancho** y se lee en el fotograma a 300 px.
- [ ] La etiqueta tiene **cuatro palabras o menos** y no compite con el número.
- [ ] No hay ejes, ni leyenda, ni rejilla, ni decimales innecesarios.
- [ ] El contador tiene **`clip`** y no se dispara.
- [ ] El contador tiene **frenado**, no sube lineal.
- [ ] Hay **respiro de 0,8–1,2 s** con la cifra final quieta antes de salir.
- [ ] El `$` / `%` están **fijos**, en su propio `drawtext`.
- [ ] Si hay barra: tiene **canaleta**, **empieza en cero**, crece **de izquierda a derecha** y con
      frenado.
- [ ] Los elementos entran **escalonados**, no todos a la vez.
- [ ] El dato **no invade** la zona de interfaz ni tapa la cara.
- [ ] Hay contraste suficiente (contorno o sombra si el fondo es claro).
- [ ] El dato es **verdadero**, tiene denominador, y si es de un tercero, la fuente está en pantalla.
- [ ] Exporté un fotograma y **lo entendí en dos segundos** sin saber de antemano qué decía.

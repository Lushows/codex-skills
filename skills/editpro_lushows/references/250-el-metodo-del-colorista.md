# 250 — El método del colorista

El bloque 6 (`60`–`69`) te enseñó a arreglar el color. Este bloque te enseña el **oficio**: cómo
trabaja alguien que se dedica a esto y cobra por ello. La diferencia no está en saber más filtros.
Está en el **orden**, en la **medición** y en saber cuándo dejar de tocar.

Un colorista profesional no "le mete color a un video". Ejecuta una secuencia fija, mide en cada
paso, y no avanza al siguiente hasta que el anterior está resuelto. Cuando algo sale mal, sabe
exactamente en qué escalón se rompió porque cada escalón es verificable por separado.

Este módulo es el mapa de todo el bloque 25.

---

## 1. Los siete escalones, en orden

```
1. BALANCE       ← quitar el tinte. Que el blanco sea blanco.
2. EXPOSICIÓN    ← poner la imagen en su nivel de brillo correcto.
3. CONTRASTE     ← definir dónde caen negros, medios y blancos.
4. SATURACIÓN    ← cuánto color, globalmente.
5. SECUNDARIAS   ← corregir SOLO una zona o un rango de color (módulo 253).
6. LOOK          ← la decisión creativa, el estilo (módulo 257).
7. ENTREGA       ← rango legal, espacio de color, plataforma (módulo 251, `68`).
```

Los pasos 1–4 son **corrección**: llevar la imagen a neutro y correcta. Los pasos 5–6 son
**gradación**: interpretar. El paso 7 es técnico y no negociable.

La regla de oro del oficio:

> **Nunca subas un escalón sin haber cerrado el anterior.**

Y su corolario, que es donde la gente se accidenta:

> **Si tienes que volver a bajar, borra todo lo de arriba y vuélvelo a hacer.**

No se "ajusta un poquito el balance" cuando ya tienes el look encima. El look está calculado sobre
una imagen que acabas de cambiar. Se cae. Esto ya lo dice `61`, y aquí lo llevamos al extremo: la
disciplina del colorista es **destruir trabajo sin dolor**.

---

## 2. Por qué ese orden y no otro

Cada escalón depende de que el anterior esté fijo. No es capricho.

| Escalón | Depende de | Qué pasa si lo haces antes |
|---|---|---|
| Balance | de nada | — |
| Exposición | del balance | subes brillo con tinte adentro; el tinte se amplifica |
| Contraste | de la exposición | estiras un rango que todavía se va a mover; recortas detalle |
| Saturación | del contraste | el contraste **cambia** la saturación percibida; saturas dos veces |
| Secundarias | de todo lo anterior | aíslas un rango de color que va a cambiar de sitio |
| Look | de la corrección completa | el look queda calculado sobre una base errónea |
| Entrega | del look | legalizas un rango y después lo vuelves a sacar |

Ese cuarto punto sorprende a mucha gente: **el contraste sube la saturación percibida**. Cuando
separas los tonos, el ojo lee más color aunque el valor de croma sea el mismo. Por eso el colorista
ajusta saturación DESPUÉS del contraste, y casi siempre termina bajándola respecto a lo que creía
que necesitaba.

---

## 3. El caso que usamos en todo el bloque

Video de un bar con neón morado. Se midieron **11 tramos** con `signalstats` antes de tocar nada.
Estos números aparecen en todos los módulos de este bloque, así que vale la pena grabárselos:

| Grupo de planos | Y (luma) | U (Cb) | V (Cr) | Saturación |
|---|---|---|---|---|
| **Neón (interior del bar)** | 70 – 78 | 144 – 165 | 143 – 168 | 32 – 57 |
| **Producto / día** | 99 – 104 | 120 – 124 | 138 – 140 | 13 – 15 |

Recordatorio: en U y V el neutro es **128**. Por encima de 128 en U hay exceso de azul; por encima
de 128 en V, exceso de rojo. Los planos de neón tenían **las dos cosas a la vez**: eso es magenta
puro, y estaba a 40 puntos del neutro.

Las dos cifras que definen el problema:

```
Dispersión de saturación:  13 → 57   = rango de 43,7
Dispersión de luminancia:  70 → 104  = rango de 34,4
```

**Dispersión** es la palabra clave del oficio. No importa el valor absoluto de un plano: importa
cuánto se separan los planos entre sí. Un video entero oscuro y morado puede ser precioso. Un video
que salta de oscuro-morado a claro-neutro cada tres segundos se ve amateur, siempre.

El objetivo del trabajo no fue "que se vea bonito". Fue: **cerrar la dispersión**.

Resultado medido después de la corrección:

| Métrica | Mejora |
|---|---|
| Dispersión de saturación | **−43 %** |
| Magenta (distancia de U y V al neutro) | **−40 %** |
| Dispersión de luminancia | **−55 %** |

Y aun así, el trabajo no estaba terminado. Por qué, en la sección 6.

---

## 4. Cómo se ve cada escalón en ffmpeg

Herramientas por escalón. El detalle está en los módulos indicados.

### Escalón 1 — Balance

```bash
# Automático, para arrancar: neutraliza negros y blancos
ffmpeg -i bruto.mp4 -vf "colorcorrect=analyze=average" -c:v libx264 -crf 16 balance.mp4

# A mano, cuando sabes hacia dónde: mueve medios por canal
ffmpeg -i bruto.mp4 -vf "colorbalance=rm=-0.06:bm=0.04" -c:v libx264 -crf 16 balance.mp4
```

`colorcorrect` es honesto como punto de partida, pero **no le creas de una**: analiza promedio de
cuadro, y si la escena está dominada por un color real (una pared roja, un neón morado) va a
"corregir" el neón, que era lo bonito. Míralo y decide.

### Escalón 2 — Exposición

```bash
ffmpeg -i balance.mp4 -vf "exposure=exposure=0.25:black=0.004" -c:v libx264 -crf 16 expo.mp4
```

`exposure` trabaja en luz lineal y es más limpio que `eq=brightness`, que solo suma un valor y
ensucia los negros. Alternativa: `eq=gamma=1.08` para levantar medios sin tocar los extremos.

### Escalón 3 — Contraste

```bash
ffmpeg -i expo.mp4 -vf "curves=all='0/0 0.25/0.22 0.75/0.79 1/1'" -c:v libx264 -crf 16 contra.mp4
```

### Escalón 4 — Saturación

```bash
ffmpeg -i contra.mp4 -vf "eq=saturation=1.06" -c:v libx264 -crf 16 sat.mp4
```

### Escalón 5 — Secundarias (módulo `253`)

```bash
ffmpeg -i sat.mp4 -vf "selectivecolor=correction_method=absolute:reds=0 -0.10 0.06 0:magentas=0 -0.14 0.04 0" \
  -c:v libx264 -crf 16 sec.mp4
```

### Escalón 6 — Look (módulo `257`)

### Escalón 7 — Entrega (módulo `251`)

```bash
ffmpeg -i look.mp4 -vf "limiter=min=16:max=235,format=yuv420p" \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
  -c:v libx264 -crf 18 -preset slow final.mp4
```

**En producción no encadenas siete archivos.** Eso es para aprender y para poder devolverte. Cuando
la cadena ya está decidida, se corre de una sola pasada sobre el original:

```bash
ffmpeg -i bruto.mp4 -vf "colorbalance=rm=-0.06:bm=0.04,exposure=exposure=0.25,\
curves=all='0/0 0.25/0.22 0.75/0.79 1/1',eq=saturation=1.06,\
selectivecolor=correction_method=absolute:reds=0 -0.10 0.06 0,\
limiter=min=16:max=235,format=yuv420p" -c:v libx264 -crf 16 -preset slow final.mp4
```

Una sola pasada = una sola generación de pérdida. Siete pasadas con CRF 16 encima de CRF 16 es un
video reprocesado siete veces.

---

## 5. Medir antes, medir después, siempre

El colorista no discute de gustos: pone números. La medición base, para cualquier plano:

```bash
ffprobe -v error -f lavfi -i "movie=plano.mp4,signalstats" \
  -show_entries frame_tags=lavfi.signalstats.YAVG,lavfi.signalstats.UAVG,lavfi.signalstats.VAVG,lavfi.signalstats.SATAVG \
  -of csv=p=0 -read_intervals "%+#10"
```

Sale una fila por cuadro, con `YAVG,UAVG,VAVG,SATAVG`. Con eso armas la tabla de todos tus planos
(así se armó la tabla de la sección 3) y ya sabes cuál está lejos de cuál.

Detalle completo del comando y de qué significa cada campo: `108`. Cómo leer scopes de verdad:
`252`.

**Y aquí viene la lección más importante de todo el bloque.**

---

## 6. Los cuatro indicadores en verde y la piel morada

En el caso del bar, después de la corrección los cuatro números globales quedaron bien:

- dispersión de saturación: −43 % ✅
- magenta: −40 % ✅
- dispersión de luminancia: −55 % ✅
- rango de luma dentro de lo legal ✅

Y al abrir el video, **la cara del muchacho seguía morada**.

La explicación es aritmética, no artística: `signalstats` promedia **todo el cuadro**. En un plano
medio de un bar, la cara ocupa quizá el 4 % de los píxeles. La pared, el neón, la barra y la sombra
ocupan el resto. Puedes bajar el magenta general un 40 % y dejar la cara exactamente igual de
morada, porque el 40 % salió de las paredes.

De ahí salen las dos reglas que definen el oficio:

> **Una métrica que promedia todo el cuadro no ve la cara.**
>
> **Medir no reemplaza mirar. Mide para decidir; mira para aprobar.**

Cuando quieras la verdad sobre una cara, mides **la cara**, no el cuadro:

```bash
# recorta la mejilla (ancho:alto:x:y) y mide solo eso
ffprobe -v error -f lavfi -i "movie=plano.mp4,crop=120:120:840:420,signalstats" \
  -show_entries frame_tags=lavfi.signalstats.YAVG,lavfi.signalstats.UAVG,lavfi.signalstats.VAVG \
  -of csv=p=0 -read_intervals "%+#3"
```

Módulo `254` a fondo sobre esto.

Y la solución en el caso real no fue tocar nada global: fue una **secundaria** que solo agarra el
rango donde vive la piel y deja el neón intacto:

```bash
ffmpeg -i corregido.mp4 -vf \
  "selectivecolor=correction_method=absolute:reds=0 -0.10 0.06 0:magentas=0 -0.14 0.04 0" \
  -c:v libx264 -crf 16 piel_ok.mp4
```

Eso es el escalón 5. Sin él, no hay oficio: hay filtros.

---

## 7. Los dos errores de método que costaron el día

Ambos ocurrieron en este proyecto y ambos son errores de **método**, no de gusto.

**Error 1 — Aplicar `gamma=0.95` a planos que ya estaban oscuros.**

`gamma` por debajo de 1 **oscurece** los medios. Se aplicó a toda la tanda, incluidos los planos de
neón que estaban en Y = 75. Resultado: Y = 52. Un plano que ya vivía en la penumbra se fue al fondo
y perdió el poco detalle de sombra que tenía.

Lo grave no es el valor. Es que **el dato ya estaba medido**. Estaba en la tabla, en la columna Y,
en 70–78. Nadie cruzó la decisión con la medición. Regla:

> Antes de aplicar un valor a un lote, cruza el valor con la tabla del lote. Si el filtro oscurece,
> mira la columna Y de los planos más oscuros y calcula dónde van a quedar.

**Error 2 — Curva en S con el punto de sombras en 0.22/0.19.**

Esa curva es correcta sobre material bien expuesto: hunde un poco las sombras y da cuerpo. Sobre
material que ya está oscuro, hunde lo que quedaba. En el bar, el detalle de las sombras se volvió
negro plano.

> Una curva no es "buena" o "mala". Es buena **para un rango de entrada**. Si tu material vive en la
> parte baja de la curva, la parte alta de la curva no existe para ti.

En material oscuro, la S se aplica al revés de lo que uno cree: se **levanta** el punto de sombras
(por ejemplo 0.15/0.20) para abrir la penumbra, y se controla arriba.

---

## 8. Cuánto tiempo lleva y cómo se reparte

Para un video social de 60 segundos con 12–15 planos, un trabajo honesto:

| Fase | Tiempo | Qué produce |
|---|---|---|
| Medir todos los planos | 15 min | la tabla de dispersión |
| Balance + exposición + contraste | 40 min | todos los planos en el mismo mundo |
| Emparejar contra el plano de referencia (`62`, `255`) | 40 min | continuidad entre cortes |
| Secundarias (piel, cielo, marca) | 30 min | lo que las globales no pudieron |
| Look | 20 min | la decisión creativa |
| Verificación y entrega | 15 min | rango legal, revisión en celular |

Lo que salta a la vista: **la parte creativa es la más corta**. El grueso del oficio es corrección y
emparejamiento. Quien empieza invierte esa proporción, se va directo al look, y por eso tiene que
rehacer todo.

---

## 9. Cuándo parar

Tres señales de que ya está:

1. **Pasas de plano en plano y no notas el corte por color.** Ese es el objetivo real.
2. **Los cambios que estás haciendo ya no se ven en el celular.** Si mueves saturación 0,02 y en un
   teléfono no hay diferencia, estás jugando.
3. **Llevas 20 minutos alternando entre dos versiones sin decidir.** Cuando dos opciones son
   indistinguibles, elige la más simple, la que tiene menos filtros. Se comprime mejor y se explica
   mejor.

Y la señal de que hay que parar y volver a grabar, que tiene módulo propio: `259`.

---

## Errores comunes

- **Ir directo al look** sin balance ni exposición. Es el error #1 del bloque entero: el look queda
  construido sobre una base torcida y no hay manera de arreglarlo después.
- **Ajustar el balance con el look ya puesto.** Todo lo que está encima se cae. Hay que rehacer.
- **Aplicar un valor a un lote sin cruzarlo con la medición del lote** (el `gamma=0.95` sobre Y = 75).
- **Usar la misma curva en S para material claro y material oscuro.** Una curva sirve para un rango
  de entrada, no para todo.
- **Creerle a un promedio de cuadro sobre una cara.** La cara son pocos píxeles; el promedio no la
  ve. Mide la cara recortada o mira.
- **Encadenar siete renders intermedios en la entrega final.** Para aprender está bien; para entregar
  es una sola pasada.
- **Resolver con globales lo que pide una secundaria.** Bajar saturación global para quitar el
  morado de la cara te apaga el neón, que era lo que le daba identidad al video.
- **Subir saturación antes del contraste.** El contraste vuelve a subir la saturación percibida y
  terminas con colores de plástico.
- **No dejar el original intacto.** Nunca sobreescribas el bruto. Nunca.
- **Aprobar el color solo en el monitor del computador.** El 90 % lo va a ver en un celular con
  brillo automático (`68`).

---

## Checklist

- [ ] Medí **todos** los planos con `signalstats` y tengo la tabla Y / U / V / SAT antes de tocar nada.
- [ ] Calculé la **dispersión** (máximo − mínimo) de luminancia y de saturación. Sé cuál es mi problema.
- [ ] Elegí el plano de referencia al que van a converger los demás.
- [ ] Ejecuté los escalones en orden: balance → exposición → contraste → saturación.
- [ ] Cada valor que apliqué a un lote lo crucé con la columna correspondiente de la tabla.
- [ ] No apliqué una curva en S de material claro sobre material oscuro.
- [ ] Después de las globales, **miré** las caras. No me quedé con los promedios.
- [ ] Lo que las globales no arreglaron lo resolví con secundarias (`253`), no forzando globales.
- [ ] El look va **al final**, sobre la corrección cerrada.
- [ ] La entrega es una sola pasada sobre el original, con `limiter` y las etiquetas de color puestas.
- [ ] Volví a medir después y puedo decir en números cuánto mejoró la dispersión.
- [ ] Lo revisé en un celular, no solo en el monitor.

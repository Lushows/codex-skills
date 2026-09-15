# 432 — Medir un destello

> "Se ve bien" no es un dato. Un destello tiene cuatro números — base, pico, anchura y número de
> fotogramas — y los cuatro se sacan en treinta segundos con ffmpeg. Sin ellos no se puede afinar nada,
> ni defender nada, ni detectar que el efecto no ocurrió.

`108` cuenta el catálogo general de medición en ffmpeg. Esto es el arnés concreto para luz.

---

## 1. El arnés, en dos comandos

**Extraer la luminancia media de cada fotograma:**

```bash
ffmpeg -hide_banner -i escena.mp4 \
  -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG:file=lum.txt" \
  -f null -
```

Sale un archivo con dos líneas por fotograma:

```
frame:251  pts:2570240  pts_time:10.04
lavfi.signalstats.YAVG=65.2800
```

> 🔴 **La trampa que hace perder la tarde.** `metadata=print` y `showinfo` escriben en el nivel de log
> **`info`**. Si lanzas el comando con `-loglevel error` — que es lo normal en un script de render —
> **no sale ni una línea** y parece que la medición ha fallado. Verificado: el mismo comando con
> `-loglevel error` devuelve cero líneas y con el nivel por defecto devuelve 336.
> Si necesitas silencio, `file=lum.txt` **tampoco te salva**: el archivo se crea, pero si además el
> `-i` falla no lo sabrás. Mide siempre con el nivel por defecto y filtra tú con `grep`.

**Medir sin recodificar.** Si sólo quieres la curva del filtro, no exportes: encadena `signalstats` al
final de la cadena y tira a `null`. Es más rápido y elimina el ruido del códec:

```bash
ffmpeg -hide_banner -i base.mp4 \
  -vf "eq=brightness='0.18*exp(-pow((t-1.0)/0.075\,2))':contrast='1+0.252*exp(-pow((t-1.0)/0.075\,2))':eval=frame,signalstats,metadata=print:key=lavfi.signalstats.YAVG" \
  -f null - 2>&1 | grep -o "YAVG=[0-9.]*"
```

Verificado: los valores con `libx264 -crf 12` y sin codificar coinciden hasta la segunda decimal
(+18,01 frente a +18,03), así que el códec **no** es la fuente de las rarezas que aparecen en §4.

---

## 2. Los cuatro números

Del archivo de luminancia se sacan, con cualquier script de veinte líneas:

| Número | Cómo | Para qué |
|---|---|---|
| **Base** | mediana (o percentil 12) de toda la serie | el suelo del plano, inmune a los picos |
| **Pico** | máximo | cuánto sube de verdad |
| **Δ** | pico − base | la dosis real, la única cifra comparable entre planos |
| **FWHM** | los dos cruces por base + Δ/2, interpolados | cuánto dura el destello |
| **Fotogramas** | cuántos superan base + 0,1·Δ | la duración que percibe el espectador |

La interpolación entre fotogramas importa: a 25 fps una campana de 0,125 s sólo tiene tres muestras.
Sin interpolar, la FWHM sale siempre en múltiplos de 0,04 s y no se puede comparar nada.

---

## 3. La curva, dibujada en la terminal

No hace falta una gráfica: una columna de almohadillas basta para ver la forma y detectar un escalón.
Medido sobre `e02_nombre.mp4` del piloto documental (25 fps, 1920×1080), alrededor del destello anclado
en la palabra *broma*:

```
 t= 9.96  Y= 62.72  #####################
 t=10.00  Y= 62.71  #####################
 t=10.04  Y= 65.28  ########################
 t=10.08  Y= 74.09  ##################################
 t=10.12  Y= 84.57  ################################################
 t=10.16  Y= 85.04  #################################################   <- pico
 t=10.20  Y= 75.42  ###################################
 t=10.24  Y= 67.37  ##########################
 t=10.28  Y= 65.27  ########################
```

Base 62,7 · pico 85,0 · **Δ +22,3** · FWHM 0,129 s · **6 fotogramas** por encima del 10 %. La campana es
simétrica y no hay meseta: es luz, no un interruptor (`431`).

**Lo que se ve de un vistazo en esta columna y no en el reproductor:** si hay meseta (interruptor), si
hay asimetría involuntaria, y si el pico cae donde tenía que caer.

---

## 4. La comprobación que hay que hacer siempre: ¿ocurrió?

El fallo más caro no es un destello mal afinado: es uno que **no existe**. `eq` sin `eval=frame` deja el
filtro en identidad, ffmpeg devuelve 0 y el vídeo sale perfecto.

Se detecta con una sola cifra — **el recorrido de luminancia**:

```bash
ffmpeg -hide_banner -i salida.mp4 -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG" \
  -f null - 2>&1 | grep -o "YAVG=[0-9.]*" | cut -d= -f2 | sort -n | sed -n '1p;$p'
```

| Render | Recorrido medido |
|---|---|
| Con `eval=frame` | **26,40 niveles** |
| Sin `eval=frame` | **0,04 niveles** |

Cero coma cero cuatro es ruido de codificación. **Si el recorrido de un plano con destello es menor que
1, el destello no ocurrió.** Esa comprobación de dos segundos debería estar en el script de render de
cualquiera que use `eq` con expresiones (`133`).

---

## 5. Comparar dos versiones sin engañarse

Cuando dudes entre dos dosis, no las mires seguidas: **móntalas lado a lado y mide las dos**. La mirada
se adapta en menos de un segundo y siempre prefiere la última que vio (`369`).

```bash
ffmpeg -y -i v_014.mp4 -i v_018.mp4 -filter_complex \
  "[0:v]scale=540:960[a];[1:v]scale=540:960[b];[a][b]hstack" -c:v libx264 -crf 20 ab.mp4
```

Y la regla de decisión: si la diferencia medida entre las dos versiones es menor que **4 niveles de Δ**,
no elijas por vista — elige la más baja, porque en la plataforma se van a ver iguales y la más baja
sobrevive mejor a la recompresión.

---

## Errores frecuentes

- **Medir con `-loglevel error`.** No sale nada y parece que el filtro falló. Es la trampa número uno.
- **Medir el vídeo exportado en vez de la cadena.** Funciona, pero es más lento y mete el códec en medio.
- **Usar la media de la serie como base.** Un plano con elementos que entran y salen tiene la media
  contaminada; usa la mediana o un percentil bajo.
- **No interpolar los cruces de media altura.** La FWHM sale cuantizada a 0,04 s y deja de servir.
- **Confundir un elemento que aparece con un destello.** Un PNG que entra con `fade` de 0,30 s también
  sube la luminancia: sube **despacio y se queda**. El destello sube en 3 fotogramas y vuelve.
- **No comprobar el recorrido.** Es la única prueba de que el efecto existe.
- **Medir el fotograma del pico y nada más.** Sin los vecinos no sabes si es campana o meseta.
- **Comparar dos versiones viéndolas seguidas.** Gana siempre la última. Lado a lado y con números.

---

## Relacionado

- `431` — de dónde salen la FWHM teórica y la respuesta no monótona de `eq`.
- `430`, `439` — qué hacer con los números: colocación y presupuesto.
- `433` — medir también el desfase con el sonido.
- `436`, `438` — el mismo arnés aplicado a pulsos lentos y al criterio de fotosensibilidad.
- `108` — medición y análisis en ffmpeg (catálogo general). `109` — trampas de ffmpeg.
- `98`, `133` — verificación del corte y verificación automática en el pipeline.
- `canales_lushows` `140-medir-antes-de-renderizar.md` y `150-catalogo-del-fallo-silencioso.md` — la
  misma disciplina del lado del motor del canal documental.

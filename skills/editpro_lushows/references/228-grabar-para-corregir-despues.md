# 228 — Grabar para corregir después

**Qué resuelve:** el colorista de tu proyecto eres tú, en CapCut, a las once de la noche. Este módulo
es la lista de decisiones que tomas **con el celular en la mano** y que determinan si esa sesión de
color va a durar diez minutos o dos horas — y si el resultado se va a ver bien o se va a ver
remendado.

La idea de fondo es una sola: **la corrección de color no crea información, la reparte**. Si la
información está, se acomoda rápido. Si no está, se inventa, y se nota.

---

## 1. Por qué el material de celular tiene menos margen del que crees

Tres límites técnicos que explican casi todos los fracasos de corrección. Vale la pena entenderlos
porque cambian lo que haces en rodaje.

### a) 8 bits: 256 escalones y ni uno más

> **Profundidad de bits:** cuántos escalones de brillo distintos puede guardar el archivo por cada
> canal de color. Tu celular graba **8 bits** = 256 escalones. Una cámara de cine graba 10 o 12 bits =
> 1.024 o 4.096 escalones.

Cuando en CapCut estiras el contraste o levantas las sombras, estás **separando** esos escalones. Con
256, se separan tanto que se empiezan a ver los saltos.

> **Banding (bandas):** cuando un degradado suave —una pared, un cielo, el halo de una lámpara— deja de
> ser suave y se ve como franjas de color escalonadas. Es la firma de haber estirado demasiado un
> archivo de 8 bits.

**Consecuencia de rodaje:** cada corrección que puedas evitar hacer después, evítala. Un plano bien
expuesto y bien balanceado sale de CapCut con dos toques y sin bandas.

### b) 4:2:0: el color se graba a un cuarto de resolución

> **Submuestreo de croma (4:2:0):** para ahorrar espacio, el video guarda el **brillo** a resolución
> completa pero el **color** a la mitad en cada dirección, o sea a **un cuarto** de los píxeles.

En tu archivo de 1080×1920, el color está guardado en algo así como 540×960. Se nota poco... hasta que
lo empujas.

**Consecuencia de rodaje, y es grande:** mientras más agresiva sea la corrección de color, más se
delatan esos píxeles de color estirados. Los bordes se ven sucios, y en escenas de **luz de color
saturada** —o sea, tu bar con neón— es donde peor se pone (`224`). Corregir un tinte morado fuerte
sobre 4:2:0 es exactamente el peor caso posible.

### c) Compresión: el bitrate que tienes

Un celular graba 1080/30 a unos 20–25 Mbps con H.264. Es suficiente para ver, y es justito para
corregir. Cada vez que estiras el color, la compresión aparece en forma de bloques en las zonas lisas.

**Cómo compruebas lo que tienes:**

```bash
ffprobe -v error -select_streams v:0 \
  -show_entries stream=codec_name,width,height,pix_fmt,bit_rate,r_frame_rate,color_transfer,color_primaries \
  -of default=nw=1 clip.mp4
```

```
pix_fmt = yuv420p       -> 8 bits, 4:2:0. Lo normal en celular.
pix_fmt = yuv420p10le   -> 10 bits. Tienes mas margen (celulares tope de gama).
color_transfer = bt709  -> normal, todo bien.
color_transfer = arib-std-b67 o smpte2084 -> es HDR. Problema (`171`).
bit_rate ~ 20000000     -> 20 Mbps. Lo normal.
```

---

## 2. Lo que sí le facilita la vida al colorista (o sea, a ti)

Seis decisiones. Todas gratis, todas en el celular, todas antes de grabar.

### Decisión 1 — Balance de blancos fijo, no automático

Ya está en `171` y en `224`, pero aquí está el porqué desde el lado del color: un plano con balance
automático **cambia de color dentro de la toma**. Corregirlo obliga a poner puntos clave y perseguir el
cambio cuadro a cuadro. En CapCut eso es un infierno. Un plano con balance fijo se corrige con un
deslizador y afecta a todo por igual.

**Regla:** un valor por sitio, fijo, escrito en un papel.

### Decisión 2 — Los 3 segundos de referencia de blanco

**Esta es la más rentable de todas y casi nadie la hace.**

Al empezar cada sitio, antes de la primera toma:

```
1. Pon una hoja de papel blanca (o una servilleta lisa) DONDE VA LA CARA,
   recibiendo exactamente la misma luz.
2. Graba 3 segundos.
3. Quitala y graba normal.
```

Para qué sirve: cuando estés corrigiendo, abres esos 3 segundos, ajustas hasta que **el papel se vea
blanco neutro**, y ya sabes exactamente cuánto hay que mover el color de todos los planos de ese sitio.
Sin la referencia, estás adivinando a ojo, con un monitor que no está calibrado, a las once de la noche
y con sueño.

**Bono:** si además metes tu **mano** en el mismo cuadro durante esos 3 segundos, tienes una referencia
de piel real de esa luz. Vale muchísimo bajo neón.

**Cómo lo mides después, en vez de adivinar:**

```bash
# Mide el color del papel blanco en la referencia. Los dos valores
# deberian salir cerca de 128 despues de corregir.
ffmpeg -hide_banner -i referencia.mp4 \
  -vf "crop=300:300:390:700,signalstats,metadata=print:key=lavfi.signalstats.UAVG:key=lavfi.signalstats.VAVG" \
  -frames:v 20 -f null - 2>&1 | grep -E 'UAVG|VAVG' | tail -4
```

Si sale UAVG=150 y VAVG=160, sabes que la escena está desviada exactamente eso, y sabes hacia dónde
tienes que empujar. Deja de ser opinión.

### Decisión 3 — Exposición consistente entre planos

Detalle completo en `222`. Aquí solo la consecuencia: dos planos del mismo sitio con exposiciones
distintas hay que corregirlos por separado y hacerlos coincidir a ojo. Diez planos así son la noche
entera. **Tu material medía de 70 a 104 de luminancia entre planos; eso es medio paso de diferencia y
es lo que hay que evitar.**

### Decisión 4 — Todo apagado: HDR, filtros, "mejoras" y belleza

Esta lista es de cosas que el celular hace **por defecto** y que hay que desactivar:

| Qué | Por qué apagarlo |
|---|---|
| **HDR / Dolby Vision** | Llega lavado o con colores raros a CapCut y a las redes (`171`) |
| **Filtros de la cámara** ("vívido", "cine", "retro") | Quedan **cocinados** en el archivo, no se quitan nunca |
| **Modo belleza / suavizado de piel** | Borra la textura de la piel de forma irreversible. Se ve a muñeco. |
| **Realce de color / IA de escena** | Sube la saturación de forma desigual entre planos |
| **Nitidez alta** | Deja halos blancos en los bordes que se agravan al corregir |
| **Modo noche** | Es para fotos; en video da arrastre y ruido |
| **Modo cine / retrato** | Desenfoque falso cocinado en el archivo (`221`) |

**La idea común:** todo lo que la cámara "mejora" sola, lo mejora **de forma distinta en cada plano**,
y eso rompe la coherencia. Y todo lo que cocina en el archivo, no se puede deshacer.

### Decisión 5 — Un solo perfil, un solo fps, todo el día

Si a mitad de rodaje cambias de app, de resolución, de fps o de perfil de color, tienes dos familias de
material que no se emparejan. Se decide al principio y no se toca (`171`).

### Decisión 6 — La hoja de color

Un archivo de texto de diez líneas que escribes en el celular mientras grabas y que te agradeces a ti
mismo dos días después:

```
RODAJE 2026-08-04 - Bar

SITIO 1: barra de noche
  Camara: 2x   Distancia: 2,6 m   1080/30
  Balance: 3200 K fijo (lampara calida sobre la cara)
  Exposicion: -1/3 respecto al automatico, bloqueada
  Luz: lampara del bar a 45 grados izquierda + carton derecha
       neon morado 2 m detras
  Referencia de blanco: clip IMG_0412 (primeros 3 s)
  Clips: IMG_0413 a IMG_0421

SITIO 2: terraza de dia
  Camara: 2x   Distancia: 2,6 m   1080/30
  Balance: 5600 K fijo
  Exposicion: -1/3 bloqueada
  Luz: ventana 45 grados + carton
  Referencia de blanco: clip IMG_0428
  Clips: IMG_0429 a IMG_0435
```

---

## 3. Perfiles planos y log: la respuesta honesta para tu caso

> **Perfil plano / log:** una forma de grabar donde la imagen sale **gris, lavada y sin contraste** a
> propósito. La idea es que así se conserva más información en las luces y en las sombras, y luego tú
> le das el contraste y el color que quieras en la edición.

En 2026, varios celulares lo ofrecen: los iPhone 15 Pro en adelante con **Apple Log**, la serie Galaxy
S24/S25 con **modo Log** en las opciones avanzadas de video, y algunas apps de terceros.

**Suena a la solución perfecta. Para ti, casi seguro que no lo es.** Aquí está el razonamiento
completo:

| A favor | En contra |
|---|---|
| Conservas más rango en luces y sombras | Solo tiene sentido si el celular graba **10 bits**; en 8 bits, el log produce bandas al recuperar el contraste |
| Más libertad de color | Los archivos pesan mucho más y llenan el celular |
| Se puede emparejar mejor entre planos | **Obliga** a corregir todos los planos: el material sin tocar es inusable |
| | CapCut no maneja Log de forma cómoda; hay que aplicar una LUT y ajustar (`65`) |
| | Se ve peor si te equivocas de exposición: el log castiga la subexposición |
| | Tú publicas 15–90 s en Instagram: la red recomprime y se come el margen extra |

**El veredicto:**

> **No uses log** para tu trabajo diario. Graba con el perfil normal, con el balance fijo, la exposición
> a −1/3 y sin filtros. Es más rápido, más seguro y el resultado final en Instagram es igual o mejor.
>
> **Cuándo sí:** si algún día haces una pieza importante (un video de marca, un comercial), tu celular
> graba 10 bits, tienes tiempo para corregir con calma, y sabes usar una LUT. Ahí el log da algo. En un
> reel de martes, no.

**Y ojo con la trampa intermedia:** poner el perfil "plano" o "natural" de la cámara nativa (que baja
contraste y saturación pero **no** es log de verdad) sí es una buena idea. Da un poquito más de margen
sin ninguno de los problemas del log. Si tu cámara lo tiene, úsalo.

---

## 4. Lo que arruina la corrección de forma irreversible

La lista negra. Cada uno de estos es un plano que no se salva:

1. **Altas quemadas.** Blanco puro = sin información. No vuelve (`222`).
2. **Sombras cortadas en negro.** Al subirlas, ruido de color verde y magenta.
3. **Un canal saturado por luz de color.** Bajo neón fuerte, el rojo y el azul pueden estar clavados en
   el tope aunque el brillo general parezca bien. Esa zona es una mancha lisa sin textura (`224`).
4. **Piel bañada en luz de color.** La luz roja que nunca la iluminó no se inventa (`224`).
5. **Balance automático que cambia dentro de la toma.** Se corrige perseguándolo con puntos clave y
   nunca queda del todo.
6. **Filtros y belleza cocinados en el archivo.** Lo que la cámara aplicó, se quedó.
7. **HDR sin tratar.** Colores desviados en todos lados menos en el celular que lo grabó.
8. **Material que pasó por WhatsApp.** Resolución baja, bitrate destruido, color aplastado (`171`).
9. **Dos locaciones con luz de naturaleza distinta en la misma frase.** No se emparejan (`173`).

---

## 5. La auditoría de 2 minutos, el mismo día del rodaje

Esto es lo que convierte todo lo anterior en un hábito útil: **medir el material el mismo día, mientras
todavía puedes regrabar.**

```bash
# Radiografia de todo el rodaje: exposicion, color y saturacion por clip
for f in *.mp4; do
  r=$(ffmpeg -hide_banner -i "$f" \
      -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG:key=lavfi.signalstats.UAVG:key=lavfi.signalstats.VAVG:key=lavfi.signalstats.SATAVG" \
      -frames:v 30 -f null - 2>&1 \
      | grep -oE '(YAVG|UAVG|VAVG|SATAVG)=[0-9.]*' | tail -4 | tr '\n' ' ')
  echo "$r  <- $f"
done
```

**Cómo se lee el resultado:**

```
YAVG    -> exposicion. Entre clips del MISMO sitio no deberia variar mas de +/-10.
UAVG    -> desviacion azul/amarillo. Lejos de 128 = escena tenida.
VAVG    -> desviacion rojo/verde.
SATAVG  -> intensidad de color. Por encima de 45 en una escena con caras = alarma.
```

**Las tres preguntas que respondes con esa tabla:**

1. ¿Los planos del mismo sitio tienen exposiciones parecidas? Si no, tengo trabajo de emparejamiento.
2. ¿Hay algún plano con SATAVG disparado? Ese es el plano de neón que va a pelear con todos los demás.
3. ¿Hay algún plano con UAVG por encima de 128 donde haya caras? Ese tiene la piel azulada o morada
   (`224`).

**Si algo sale mal y todavía es el mismo día: regraba.** Cuarenta segundos de regrabación valen más que
tres horas de corrección que además queda peor.

---

## 6. Y lo que sí puedes arreglar cómodo si grabaste bien

Para cerrar en positivo. Con material limpio (balance fijo, exposición consistente, sin filtros, piel
con luz neutra), en CapCut esto es rápido:

- **Ajustar la temperatura general** del plano: un deslizador.
- **Levantar o bajar el brillo** medio paso: un deslizador.
- **Emparejar dos planos del mismo sitio:** copiar el ajuste de uno al otro y afinar.
- **Poner un look de marca** (`63`, `64`): un ajuste sobre material ya coherente.
- **Bajar un poco la saturación general** para unificar.
- **Viñeta y textura** (`66`).

Todo eso son **diez minutos para un reel entero** si el material vino bien. Es el mismo software y el
mismo tú: la diferencia la hicieron los cinco minutos de preparación en el bar.

---

## Errores comunes

1. **Grabar con balance automático.** El color cambia dentro de la toma y perseguirlo en CapCut es lo
   más caro que hay. Fijo, un valor por sitio.
2. **No grabar los 3 segundos de papel blanco.** Es la acción con mejor relación esfuerzo/beneficio de
   todo el rodaje y cuesta tres segundos.
3. **Dejar filtros, "vívido", belleza o realce de IA activos.** Quedan cocinados en el archivo y no se
   quitan. Además cada plano queda cocinado distinto.
4. **Grabar en HDR.** Llega lavado a CapCut y a las redes.
5. **Grabar en log "porque es más profesional".** En 8 bits produce bandas, pesa el triple, obliga a
   corregir todo y en Instagram no se nota. Solo con 10 bits y para piezas importantes.
6. **Cambiar de app, fps o resolución a mitad de rodaje.** Quedan dos familias de material que no
   emparejan.
7. **Estirar mucho el color en post sobre material 4:2:0.** El color está guardado a un cuarto de
   resolución; cuanto más lo empujas, más se ensucia. Se resuelve grabando bien, no corrigiendo mejor.
8. **Levantar sombras muy oscuras.** Aparece ruido de color verde y magenta, sobre todo en la piel.
9. **No escribir la hoja de color.** Dos días después no te acuerdas de qué Kelvin usaste ni de qué
   clip era la referencia.
10. **No auditar el material el mismo día.** Es el único momento en el que un problema se arregla
    regrabando en vez de sufriendo.
11. **Pasar el material por WhatsApp.** Todo lo anterior se pierde de golpe.
12. **Creer que la corrección de color arregla la fotografía.** Reparte información; no la crea. Lo que
    no se grabó, no está.

---

## Checklist

- [ ] **Balance de blancos fijo**, un valor por sitio, anotado.
- [ ] **3 segundos de papel blanco** grabados al inicio de cada sitio, donde va la cara.
- [ ] En esa referencia sale también **mi mano** (referencia de piel).
- [ ] **Exposición consistente** entre todos los planos del mismo sitio (`222`).
- [ ] **HDR apagado.**
- [ ] **Filtros, belleza, realce de IA y modo noche apagados.**
- [ ] Mismo **fps, resolución y app** durante todo el rodaje.
- [ ] Si la cámara tiene perfil **"natural" o "plano"** (no log), lo estoy usando; **log no**.
- [ ] Comprobé con `ffprobe` que el material es **yuv420p / bt709** y no HDR.
- [ ] Escribí la **hoja de color** con sitio, Kelvin, exposición, luz y clips.
- [ ] Corrí la **auditoría de ffmpeg el mismo día** y revisé YAVG, UAVG, VAVG y SATAVG.
- [ ] Ningún plano con caras tiene **UAVG por encima de 128** ni **SATAVG por encima de 45**.
- [ ] El material llegó al PC **sin pasar por WhatsApp**.

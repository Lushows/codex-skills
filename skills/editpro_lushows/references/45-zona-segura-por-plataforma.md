# 45 — Zona segura por plataforma: dónde NO poner texto


> ## ⚠️ Este módulo es el DUEÑO de las cifras de zona segura
>
> Dentro de esta skill hay cinco módulos con tablas de zona segura (`45`, `92`, `87`,
> `38`, `376`) y sus números no coinciden. Para Instagram abajo circulan 400, 420,
> 480, 192 y 384-672 px. No es que cuatro estén mal: **están midiendo dos cosas
> distintas y ninguna lo decía.**
>
> | Qué se mide | Cambia? | De dónde sale |
> |---|---|---|
> | **Recorte geométrico** — lo que se pierde al pasar de 9:16 a 4:5 o a 1:1 | **Nunca.** Es aritmética de proporciones: 1920 − 1350 = 570, o sea 285 arriba y 285 abajo | Se calcula, no se mide |
> | **Interfaz encima** — la banda donde la app pinta botones, texto y barra | **Con cada versión de la app.** Cualquier cifra caduca | Se MIDE sobre una captura del reproductor real, con el método de `418` |
>
> **La regla:** el recorte geométrico se calcula y no se discute. La interfaz se mide
> el día que se necesita, se anota con fecha y dispositivo, y se vuelve a medir. Una
> tabla de interfaz sin fecha ni método es una trampa para dentro de seis meses.
>
> Los otros cuatro módulos conservan sus cifras como registro de cuándo se creyó qué.
> Para montar, la cifra que manda es la que midas hoy → `418-medir-la-zona-segura-de-verdad`.

> Medidas verificadas a **agosto de 2026**. Las interfaces cambian: si un video se ve raro, vuelve a
> medir con una captura real del celular antes de creerle a esta tabla.

## El problema, en una frase

Tú exportas un lienzo limpio de 1080x1920. La plataforma le pinta encima su propia interfaz: botones,
caption, nombre de usuario, botón de suscribirse, barra de progreso. **Ese pedazo de tu video ya no es
tuyo.** Si pusiste texto ahí, se lo comieron.

Y no te enteras nunca, porque tú ves tu video en el reproductor de tu computador, donde no hay interfaz.

---

## La regla universal (si no quieres memorizar nada)

Sobre 1080x1920, mantén todo lo importante dentro de este rectángulo:

```
        0                                    1080
        ┌────────────────────────────────────┐
        │        ZONA MUERTA (arriba)        │  0 a 250
    250 ├────────────────────────────────────┤
        │  ┌──────────────────────────────┐  │
        │  │                              │  │
        │  │      ZONA SEGURA REAL        │  │
        │  │      880 x 1230 px           │  │
        │  │                              │  │
        │  └──────────────────────────────┘  │
   1480 ├────────────────────────────────────┤
        │        ZONA MUERTA (abajo)         │  1480 a 1920
        └────────────────────────────────────┘
       100                                  980
```

- **Arriba:** 250 px libres
- **Abajo:** 440 px libres
- **Izquierda:** 100 px libres
- **Derecha:** 100 px libres (más si hay iconos)

Ese rectángulo sobrevive en Instagram, TikTok y YouTube Shorts **al mismo tiempo**. Si publicas la misma
pieza en las tres redes (lo normal), es el único que importa.

**El `MarginV: 520` del estilo base** deja la línea base del texto a 520 px del borde inferior. Con fuente
de 150 px, el texto ocupa de ~520 a ~700 px desde abajo, es decir de y=1220 a y=1400. Cómodamente dentro.

---

## Instagram Reels

Lienzo: **1080x1920** (9:16).

| Zona | Píxeles | Qué la ocupa |
|---|---|---|
| Superior | 0 a 250 | Nombre de usuario en algunos modos, indicador de audio, botón de cámara |
| Inferior | 1520 a 1920 (~400 px) | **Caption** (hasta 3 líneas visibles), nombre de cuenta, pista de audio |
| Derecha | 990 a 1080 (~90 px de ancho), desde y≈1100 hacia abajo | Me gusta, comentar, compartir, remix, menú |
| Izquierda inferior | 0 a 270 px de alto desde el borde | Caption y handle |

**Zona segura práctica de Instagram:** el rectángulo central de aproximadamente **1080 x 1350** centrado,
o dicho de otro modo, dejando **250 px arriba** y **320-400 px abajo**.

Notas específicas:

- El caption **crece hacia arriba** cuando el texto es largo. Un caption de 3 líneas con hashtags puede
  comerse hasta 400 px. Si tus captions son largos, sé conservador: 440 px abajo.
- Los iconos de la derecha **no llegan hasta arriba**: empiezan más o menos a la mitad. La franja derecha
  superior sí es utilizable.
- Instagram muestra Reels también en el feed (donde recorta a 4:5) y en el grid del perfil (donde recorta
  a 1:1 centrado). Si tu texto está en el tercio inferior, **en el grid no se ve**. Ver `38`.

---

## TikTok

Lienzo: **1080x1920** (9:16).

TikTok es la que **más interfaz pinta encima**. Sus medidas:

| Zona | Píxeles | Qué la ocupa |
|---|---|---|
| Superior | 0 a ~150 | Pestañas "Siguiendo / Para ti", buscador |
| Inferior | ~1600 a 1920 (~320 px) | Handle, caption, música, y el **botón de CTA** en anuncios |
| Derecha | ~915 a 1080 (~165 px de ancho) | Avatar, corazón, comentarios, favoritos, compartir, disco de audio |

**Zona segura práctica de TikTok:** aproximadamente **960 x 1386** px, es decir dejando ~140 px arriba,
~324 px abajo y ~164 px a la derecha.

Notas específicas:

- **La franja derecha de TikTok es la más ancha de las tres** (~165 px). Si centras el texto no hay
  problema, pero cualquier gráfico alineado a la derecha se lo comen.
- **En anuncios de TikTok el fondo inferior es peor**: aparece el botón de CTA ("Más información",
  "Comprar ahora") que ocupa una franja adicional. En TikTok Ads, deja **400 px abajo**, no 320.
- Un caption corto de una línea ocupa ~80 px; uno con hashtags puede llegar a 250 px o más.

---

## YouTube Shorts

Lienzo: **1080x1920** (9:16).

Shorts es engañosa: parece limpia y es la que más come abajo.

| Zona | Píxeles | Qué la ocupa |
|---|---|---|
| Superior | 0 a ~150 | Logo de YouTube, buscar, transmitir |
| Inferior | ~1500 a 1920 (**~420 px**) | Título del Short, nombre del canal, **botón Suscribirse**, descripción |
| Derecha | ~940 a 1080 (~140 px) | Me gusta, no me gusta, comentarios, compartir, remezclar, menú |

**Zona segura práctica de Shorts:** aproximadamente **880 x 1310** px, empezando en (40, 170) y terminando
en (920, 1480).

Notas específicas:

- **El botón de Suscribirse es grande y prominente** (~180x80 px) y vive abajo a la derecha. Si tienes
  logo o firma en esa esquina, se pierde.
- Cuando alguien **expande la descripción**, el bloque inferior crece todavía más. No pongas nada crítico
  ahí abajo.
- Shorts es **la más restrictiva de las tres**. Si tu pieza pasa la zona segura de Shorts, pasa las tres.

---

## Comparación de las tres (lo que hay que dejar libre)

| Borde | Instagram Reels | TikTok | YouTube Shorts | **Usa este** |
|---|---|---|---|---|
| Arriba | 250 px | 150 px | 170 px | **250 px** |
| Abajo | 400 px | 324 px (400 en Ads) | **420 px** | **440 px** |
| Izquierda | 60 px | 60 px | 60 px | **100 px** |
| Derecha | 90 px | **165 px** | 140 px | **100 px** (centrado) / **180 px** (si alineas a la derecha) |

---

## Otras superficies (no las olvides)

| Superficie | Formato | Cuidado |
|---|---|---|
| **Feed de Instagram** | Recorta a 4:5 (1080x1350) | Pierde 285 px arriba y abajo del 9:16 |
| **Grid del perfil (IG)** | Recorta a 1:1 centrado | **Solo se ve la franja central**. Tu texto inferior desaparece |
| **Stories** | 1080x1920 | Igual a Reels, pero el bloque superior es más agresivo (barra de progreso + handle): deja 250 px |
| **Anuncios de Meta (feed)** | 4:5 o 1:1 | Además hay CTA de Meta debajo del video. Deja 250 px abajo |
| **WhatsApp / CTWA** | Se ve dentro del chat, sin interfaz encima | Zona segura amplia, pero se ve **muy pequeño**: sube el tamaño de fuente |
| **YouTube largo (16:9)** | 1920x1080 | La barra de controles come ~90 px abajo cuando aparece. Deja 120 px |

Ver `38` para adaptar una misma pieza a varios formatos y `92` para especificaciones de exportación.

---

## Cómo verificarlo de verdad

No confíes en el número. Superpón la interfaz y mira.

### 1. Dibuja las zonas muertas sobre tu video

```bash
ffmpeg -i salida.mp4 -vf "drawbox=x=0:y=0:w=1080:h=250:color=red@0.4:t=fill,\
drawbox=x=0:y=1480:w=1080:h=440:color=red@0.4:t=fill,\
drawbox=x=900:y=0:w=180:h=1920:color=red@0.4:t=fill" \
  -c:v libx264 -crf 23 -preset fast -pix_fmt yuv420p -c:a copy -y prueba_zonas.mp4
```

Reproduce `prueba_zonas.mp4`. **Nada importante puede quedar bajo el rojo.** Este archivo es de control,
no se publica.

### 2. Un fotograma con la retícula

Si solo quieres revisar un momento concreto:

```bash
ffmpeg -ss 3.5 -i salida.mp4 -vf "drawbox=x=100:y=250:w=880:h=1230:color=lime@1:t=6" \
  -frames:v 1 -y prueba_zona.png
```

Eso dibuja el **borde** de la zona segura (`t=6` es grosor de línea, no relleno). Abre el PNG: todo lo
importante debe estar dentro del verde.

### 3. La prueba definitiva: captura real

Publica el video **en borrador o como privado**, ábrelo en el celular, y haz una captura de pantalla.
Esa captura es la verdad. Las medidas de esta tabla son un buen punto de partida; la captura es la prueba.

Guárdate esas capturas como plantillas PNG por plataforma. Se reutilizan para siempre.

---

## Trampas que rompen la zona segura sin que te des cuenta

### `\pos` y `\move` anulan los márgenes

En el momento en que una línea de ASS usa `\pos(x,y)` o `\move(...)`, el `MarginV: 520` del estilo deja de
aplicar. Las coordenadas mandan. Es la forma más común de meter texto bajo el caption sin querer.

Si usas `\move`, calcula: con anclaje 2 (abajo-centro) y fuente de 150 px, `\pos(540,1400)` deja el texto
aproximadamente entre y=1250 y y=1400. Dentro. `\pos(540,1650)` lo mete de lleno bajo el caption.

### El pop al 112% agranda el texto

El texto que a 100% cabía justo, al 112% se sale. Verifica la zona segura **con el texto en su tamaño
máximo**, no en reposo. Ver `42`.

### Reencuadrar de 16:9 a 9:16 mueve todo

Si tomas un video horizontal y lo recortas a vertical, el texto que estaba abajo en 16:9 termina en un
sitio distinto. Rehaz el posicionamiento, no lo heredes. Ver `38` y `22`.

### Reescalar cambia todo

Un `.ass` con `PlayResY: 1080` renderizado sobre un video de 1920 escala todo x1,78, incluidos los
márgenes. Tu `MarginV: 520` se vuelve 925. Ver `43`.

---

## Qué SÍ va en las zonas muertas

No son inútiles. Ahí puede ir:

- **Fondo, textura, degradado**: se ve, no informa.
- **Continuación visual del plano**: la cabeza de la persona, el cielo, la mesa.
- **Elementos decorativos sin información**: barras de color, formas de marca.
- **Cara**: una cara parcialmente cubierta por el caption sigue funcionando. Un texto no.

Lo que **nunca** va: texto, precio, logo, CTA, número de teléfono, dato que la persona necesita para
actuar.

---

## Errores comunes

- **Confiar en el reproductor del computador.** Ahí no hay interfaz encima. Es la ilusión que causa el 90%
  de estos errores.
- **Usar la zona segura de una sola plataforma cuando publicas en tres.** Usa la intersección: 250 arriba,
  440 abajo.
- **Poner el CTA final abajo.** Es exactamente donde está el caption y el botón de suscribirse. El CTA va
  al centro.
- **Poner la firma o el logo en la esquina inferior derecha.** Ahí vive el botón de Suscribirse de Shorts
  y el disco de audio de TikTok. Si firmas, firma arriba-izquierda o centro-abajo dentro de la zona segura.
- **Alinear gráficos a la derecha en TikTok.** Son 165 px de iconos. Se los come.
- **Usar `\pos` sin recalcular la zona segura.** Los márgenes del estilo dejan de aplicar y no te avisa nada.
- **Verificar en reposo y no durante el pop.** Al 112% el texto crece y se sale.
- **Olvidar el grid del perfil de Instagram.** Recorta a 1:1 centrado: tu texto del tercio inferior no
  existe ahí. Si el grid te importa, mete el gancho también en la franja central.
- **Asumir que las medidas de hace un año siguen vigentes.** Las interfaces crecen. Vuelve a capturar
  cada tanto.
- **No dejar margen extra en anuncios.** Los anuncios de TikTok y Meta añaden botones que no están en el
  contenido orgánico.

---

## Checklist

- [ ] Todo lo importante está dentro de: **250 px arriba, 440 px abajo, 100 px a los lados**.
- [ ] El `MarginV` del estilo es >= 520 px en vertical 1080x1920.
- [ ] Ninguna línea usa `\pos` / `\move` sin que haya recalculado la zona segura para esa línea.
- [ ] Verifiqué la zona segura **con el texto al 112%** (durante el pop), no solo en reposo.
- [ ] Si publico en TikTok Ads o Meta Ads, dejé **400+ px** abajo, no 320.
- [ ] Si alineo algo a la derecha, dejé **180 px** libres (por TikTok).
- [ ] El CTA final está en el **centro**, no abajo.
- [ ] La firma o logo **no** está en la esquina inferior derecha.
- [ ] Rendericé la versión de control con las zonas muertas en rojo y la revisé completa.
- [ ] Si la pieza va al grid de Instagram, el gancho también funciona recortado a 1:1 centrado.
- [ ] `PlayResX/Y` del `.ass` coinciden con la resolución real (si no, los márgenes escalan).
- [ ] Tengo una captura real de la interfaz de cada plataforma como plantilla, y la usé.

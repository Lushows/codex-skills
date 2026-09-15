# 94 — Miniatura y portada: la decisión que ocurre antes del video

> La portada es lo único de tu video que ve el 100% de la gente a la que se le muestra. El video lo ve el
> 3%. Piensa cuánto tiempo le dedicas a cada cosa y verás que lo tienes al revés.

---

## Portada, miniatura y primer fotograma: no son lo mismo

Tres cosas que se confunden todo el tiempo:

| Cosa | Qué es | Dónde manda |
|---|---|---|
| **Miniatura** (thumbnail) | Imagen fija que representa el video en un listado | YouTube largo, búsqueda, sugeridos |
| **Portada** (cover) | Imagen fija del video dentro de tu perfil/grilla | Instagram Reels, TikTok, perfil de YouTube |
| **Primer fotograma** | Literalmente el fotograma 0 del video | Feed en desplazamiento, autorreproducción, WhatsApp |

**En el feed nadie ve tu miniatura.** El video autorreproduce, así que lo que decide es **el primer
fotograma y el primer segundo**. La miniatura/portada manda en dos sitios: tu **perfil** (la grilla, donde
alguien decide si te sigue) y la **búsqueda/sugeridos** de YouTube.

Conclusión práctica que casi nadie aplica: **el primer fotograma y la portada tienen trabajos distintos y
deben diseñarse por separado.**

---

## Qué hace buena a una portada

Una portada buena responde en **menos de medio segundo** a una sola pregunta: *"¿esto es para mí?"*

Los cinco elementos, en orden de importancia:

### 1. Una cara con emoción legible

La cara humana es lo que el cerebro procesa más rápido. Y no cualquier cara: **una cara con una emoción
identificable** (sorpresa, incredulidad, alegría, preocupación). Una cara neutra rinde como un objeto.

- Ojos abiertos y mirando **a la cámara** o al elemento importante
- La cara ocupando **entre 25% y 40%** del encuadre
- Nada de perfiles, nada de mirando al piso, nada de ojos entrecerrados

### 2. Contraste brutal

La portada compite en una pantalla llena de portadas. El contraste es lo que la separa del vecino.

- Sujeto claro sobre fondo oscuro, o al revés
- Colores saturados (naranja, amarillo, rojo funcionan; el gris no)
- Si el fondo es ruidoso, **desenfócalo o oscurécelo**

### 3. Texto de 3 a 5 palabras, grandísimo

En una miniatura de YouTube vista en celular, tienes aproximadamente **el tamaño de una estampilla**.

- **Máximo 5 palabras.** Idealmente 3.
- Tamaño mínimo: el texto debe ocupar **al menos el 15% de la altura** de la imagen
- Fuente pesada (bold o black), nunca ligera
- Contorno o sombra para que se lea sobre cualquier fondo
- **El texto no debe repetir el título.** Debe complementarlo.

### 4. Un solo punto focal

Si hay tres cosas interesantes, no hay ninguna. Una cara, una cosa, un texto. Se acabó.

### 5. Coherencia con lo que promete el video

Si la portada promete algo que el video no da, la gente entra, se va a los 3 segundos, y la plataforma
aprende que tu contenido decepciona. **La retención destruida por una portada engañosa cuesta más que las
vistas que ganó.**

---

## La prueba de la uña

Este es el único control de calidad que importa para una portada:

**Reduce la imagen a 120 píxeles de ancho y míralas.** Si a ese tamaño no se entiende de qué va, la
portada no sirve. Punto. No importa lo bonita que se vea al 100%.

```bash
# Genera la versión miniatura de tu portada para hacer la prueba
ffmpeg -i portada.jpg -vf "scale=120:-1" prueba_uña.png
```

Ábrela y mírala al tamaño real que tiene en pantalla. Si no la entiendes en medio segundo, rehazla.

---

## Extraer el mejor fotograma del video

### Método 1 — El fotograma exacto que quieres

Si ya sabes el momento (viste el video y anotaste "segundo 4,2"):

```bash
ffmpeg -ss 00:00:04.200 -i video.mp4 -frames:v 1 -q:v 1 portada.jpg
```

Notas importantes:
- `-ss` **antes** del `-i` es rapidísimo pero salta al fotograma clave más cercano.
- `-ss` **después** del `-i` es exacto al fotograma pero lento. Úsalo si necesitas precisión:
  `ffmpeg -i video.mp4 -ss 00:00:04.200 -frames:v 1 -q:v 1 portada.jpg`
- `-q:v 1` es la máxima calidad JPEG (la escala va de 1 a 31, al revés).

Para calidad absoluta, saca PNG:
```bash
ffmpeg -i video.mp4 -ss 00:00:04.200 -frames:v 1 portada.png
```

### Método 2 — Hoja de contactos para escoger

Cuando no sabes dónde está el buen fotograma, sácalos todos en una grilla:

```bash
# 25 fotogramas en una grilla 5x5
ffmpeg -i video.mp4 -vf "select='not(mod(n,30))',scale=320:-1,tile=5x5" \
  -frames:v 1 -q:v 2 contactos.jpg
```

`mod(n,30)` toma uno de cada 30 fotogramas (uno por segundo a 30 fps). Ajusta el número según la duración.

**Con los tiempos marcados encima** (mucho más útil, porque puedes volver al momento exacto):

```bash
ffmpeg -i video.mp4 -vf "select='not(mod(n,30))',\
drawtext=text='%{pts\\:hms}':fontcolor=yellow:fontsize=28:box=1:boxcolor=black@0.7:x=6:y=6,\
scale=320:-1,tile=5x5" -frames:v 1 -q:v 2 contactos_tiempo.jpg
```

Un fotograma cada 2 segundos, para videos largos:
```bash
ffmpeg -i video.mp4 -vf "fps=1/2,scale=320:-1,tile=6x6" -frames:v 1 -q:v 2 contactos.jpg
```

### Método 3 — Que ffmpeg escoja los fotogramas "interesantes"

El filtro `thumbnail` analiza el video y saca los fotogramas más representativos (los que más se
diferencian del promedio):

```bash
# El fotograma más representativo de cada 100
ffmpeg -i video.mp4 -vf "thumbnail=100,scale=1280:-1" -frames:v 10 \
  -q:v 2 candidato_%02d.jpg
```

Es sorprendentemente bueno para encontrar los momentos con más "acción visual". No sabe nada de si la
persona tiene los ojos abiertos, pero te ahorra la mitad del trabajo.

### Método 4 — Solo los fotogramas clave (rapidísimo)

```bash
ffmpeg -skip_frame nokey -i video.mp4 -vsync vfr -frame_pts true \
  -q:v 2 clave_%04d.jpg
```

Extrae únicamente los fotogramas clave. Muy rápido en videos largos, y como los fotogramas clave suelen
caer en cambios de escena, suelen ser buenos candidatos.

---

## Detectar los fotogramas malos automáticamente

**Ojos cerrados, movimiento borroso y fotogramas oscuros** son los tres asesinos de portadas. Se pueden
filtrar sin verlos uno por uno.

**Fotogramas borrosos** — el borroso tiene poca variación de bordes. Este comando ordena los fotogramas
extraídos de más nítido a más borroso usando el tamaño del archivo JPEG como aproximación (un fotograma
nítido tiene más detalle y por tanto más peso):

```bash
ffmpeg -i video.mp4 -vf "fps=2,scale=640:-1" -q:v 2 f_%04d.jpg
ls -S f_*.jpg | head -10   # los 10 más nítidos primero
```

Es un truco sucio pero funciona sorprendentemente bien.

**Fotogramas oscuros** — detecta el brillo medio:
```bash
ffmpeg -i video.mp4 -vf "fps=1,signalstats,metadata=print:key=lavfi.signalstats.YAVG" \
  -f null - 2>&1 | grep YAVG
```
Valores de YAVG por debajo de ~60 (de 255) son fotogramas muy oscuros.

---

## El primer fotograma como portada

En Instagram Reels y TikTok, **el primer fotograma es el que autorreproduce en el feed** y también es la
portada por defecto en tu grilla si no eliges otra.

Reglas del primer fotograma (repaso, se detalla en el módulo 30):

- **Movimiento ya empezado**, nunca una persona quieta esperando
- Sin negro, sin fundido de entrada, sin logo
- Con el rótulo del gancho **ya presente**, no animándose a entrar
- Entendible reducido a 120 px

**Truco muy útil:** si el primer fotograma del corte no sirve como portada, puedes **pegar un fotograma
elegido al inicio del video**, de 1 a 2 fotogramas de duración. Es invisible al reproducir y toma el
control de la portada por defecto:

```bash
# 1. Genera la imagen de portada (o úsala ya diseñada)
ffmpeg -i portada_diseñada.png -vf "scale=1080:1920" -frames:v 1 p.png

# 2. Conviértela en un clip de 1 fotograma con audio silencioso
ffmpeg -loop 1 -i p.png -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=48000 \
  -t 0.04 -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -r 25 \
  -c:a aac -b:a 128k -shortest portada_clip.mp4

# 3. Pégalo al principio
printf "file 'portada_clip.mp4'\nfile 'reel.mp4'\n" > lista.txt
ffmpeg -f concat -safe 0 -i lista.txt -c copy reel_con_portada.mp4
```

**Advertencia honesta:** este truco funciona mejor en unas plataformas que en otras, y algunas apps ahora
escogen el fotograma "más representativo" y no el primero. Úsalo, pero **siempre selecciona la portada
manualmente en la app también**. Cinturón y tirantes.

---

## Especificaciones de portada por plataforma

| Plataforma | Dimensiones | Formato | Peso máx | Notas |
|---|---|---|---|---|
| **YouTube (miniatura)** | 1280 × 720 (16:9) | JPG, PNG, GIF | **2 MB** | Mínimo 640 px de ancho |
| **YouTube Shorts** | 1080 × 1920 | — | — | Se escoge un fotograma del video |
| **Instagram Reels** | 1080 × 1920 | JPG/PNG o fotograma | — | La grilla del perfil recorta a **1:1 centrado** |
| **Instagram Feed** | 1080 × 1350 | — | — | — |
| **TikTok** | 1080 × 1920 | fotograma del video | — | Se elige dentro de la app |
| **Facebook video** | 1200 × 675 | JPG/PNG | — | — |

**La trampa de la grilla de Instagram:** tu portada vertical de 1080 × 1920 se muestra en tu perfil
**recortada al centro en 1:1**. Si pusiste el texto arriba o abajo, en tu perfil **desaparece**.

Regla: **en Reels, el elemento clave de la portada va en el centro vertical de la imagen** (entre el 25% y
el 75% de la altura). Así sobrevive tanto al reel completo como al recorte cuadrado de la grilla.

Verifícalo:
```bash
ffmpeg -i portada.jpg -vf "crop=1080:1080:0:420" grilla_1x1.jpg
```
Ese es exactamente lo que se ve en tu perfil.

---

## Cómo diseñar la portada (flujo práctico)

1. **Escoge el fotograma** con la hoja de contactos. Busca cara + emoción + ojos abiertos.
2. **Extráelo a máxima calidad** (PNG, sin recomprimir).
3. **Súbele el contraste y la saturación.** Una portada plana no compite.
   ```bash
   ffmpeg -i base.png -vf "eq=contrast=1.15:saturation=1.25:brightness=0.02" portada_pop.png
   ```
4. **Separa el sujeto del fondo:** oscurece o desenfoca el fondo para que la cara salte.
5. **Pon el texto**: 3–5 palabras, grande, con contorno.
6. **Prueba de la uña** a 120 px.
7. **Prueba de recorte 1:1** si es Instagram.
8. **Exporta:** JPG calidad alta, bajo el límite de peso.
   ```bash
   ffmpeg -i portada_final.png -q:v 2 portada_final.jpg
   ls -lh portada_final.jpg   # verifica < 2 MB para YouTube
   ```

---

## Errores comunes

1. **Dejar que la plataforma escoja.** El algoritmo agarra un fotograma al azar y casi siempre pilla a la
   persona con los ojos cerrados o la boca abierta a media palabra.
2. **Poner una frase larga.** En una miniatura de celular, 8 palabras son una mancha gris. Máximo 5.
3. **Texto que repite el título.** Desperdicias el único espacio que tienes para agregar información.
4. **Poner el texto arriba o abajo en un reel.** El recorte 1:1 de la grilla del perfil se lo come.
5. **Cara neutra.** No genera curiosidad. Necesitas una emoción identificable.
6. **Portada mentirosa.** Sube el clic y destroza la retención. La plataforma lo nota y te castiga.
7. **Fondo saturado de cosas.** Si compite con el sujeto, no hay sujeto.
8. **Portada con calidad baja porque salió de un fotograma comprimido.** Extráela del máster, no del
   archivo ya subido.
9. **Miniatura de YouTube por encima de 2 MB.** La rechaza y te deja la automática sin avisarte bien.
10. **Usar `-ss` después de `-i` en videos largos y esperar sentado.** Para exploración usa `-ss` antes;
    para el corte final exacto, después.
11. **Olvidar que el primer fotograma es lo que autorreproduce.** Puedes tener la mejor portada del mundo
    y un primer fotograma en negro que mata el reel en el feed.
12. **Diseñar la portada al final, apurado.** Es el elemento con más rendimiento por minuto invertido de
    todo el proyecto.

---

## Checklist

Antes de publicar, para portada y primer fotograma:

- [ ] La portada la **escogí yo**, no la plataforma
- [ ] Salió del **máster**, no de un archivo recomprimido
- [ ] Hay una **cara con emoción legible**, ojos abiertos, mirando a cámara o al elemento clave
- [ ] Un solo punto focal, fondo controlado (oscurecido o desenfocado)
- [ ] Texto de **3 a 5 palabras**, ocupa ≥15% de la altura, con contorno o sombra
- [ ] El texto **complementa** el título, no lo repite
- [ ] **Prueba de la uña**: se entiende a 120 px de ancho
- [ ] Si es Instagram: sobrevive el **recorte 1:1 centrado** de la grilla del perfil
- [ ] Contraste y saturación reforzados respecto al fotograma crudo
- [ ] Dimensiones y peso dentro del límite de la plataforma (YouTube: 1280×720, <2 MB)
- [ ] El **primer fotograma del video** también funciona por su cuenta (movimiento empezado, sin negro,
      rótulo ya presente)
- [ ] La portada **no promete** nada que el video no entregue

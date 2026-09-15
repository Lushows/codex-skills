# 266 — Reemplazo de fondo y cielo

**Qué resuelve:** cambiar lo que está detrás. Grabaste en tu cuarto y quieres que se vea como una
cocina profesional. Grabaste un plato con un fondo feo y quieres uno limpio. El cielo salió blanco y
plano y quieres uno con nubes.

Es el efecto que más gente quiere hacer y el que **más se nota cuando está mal**. Este módulo dice qué
lo hace creíble, cómo se hace con CapCut y con ffmpeg, y —lo más útil— **cuándo la respuesta correcta es
no reemplazarlo.**

---

## 1. La pregunta que ahorra dos horas

**¿Por qué quieres cambiar el fondo?**

| Tu razón | Lo que deberías hacer |
|---|---|
| "el fondo está feo / desordenado" | **desenfócalo** (sección 2). 2 minutos, resultado mejor |
| "quiero que parezca otro sitio" | reemplazo real. Sigue leyendo |
| "quiero poner texto o color detrás" | **sándwich** (`262`). No es reemplazo de fondo |
| "el cielo salió blanco" | reemplazo de cielo (sección 6) |
| "el fondo distrae del producto" | fondo liso + desenfoque, o reencuadrar |
| "vi que un creador lo hace" | probablemente él grabó ahí de verdad |

**El 70% de las veces la respuesta es desenfocar, no reemplazar.** Un fondo real desenfocado siempre se
ve mejor que un fondo falso bien integrado, porque el real tiene la luz correcta por definición.

---

## 2. La alternativa que gana casi siempre: desenfocar el fondo real

Se hace con el mismo recorte del sándwich, cambiando qué va en medio.

**En CapCut:**
1. Duplicas el clip (pista de arriba).
2. Al de **arriba**: Quitar fondo → Eliminación automática.
3. Al de **abajo**: le aplicas **Desenfoque** (está en Efectos, o en Ajustar según versión).

Resultado: tú nítido, tu cuarto desenfocado. Se ve como un retrato de cámara buena y nadie sospecha
nada, porque **la luz coincide perfectamente: es la misma luz.**

**Con ffmpeg**, si tienes el recorte con alfa:

```bash
ffmpeg -y -i plano.mp4 -i sujeto_recortado.mov -filter_complex "\
[0:v]gblur=sigma=18[bg];\
[1:v]format=rgba[su];\
[bg][su]overlay=0:0:shortest=1[out]" \
  -map "[out]" -map 0:a? -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p desenfocado.mp4
```

`sigma` entre **12 y 25**. Menos de 10 no se nota; más de 30 parece filtro de videollamada.

**El truco que lo hace ver caro:** además del desenfoque, **oscurece un poco el fondo** y súbele el
contraste al sujeto. Así el ojo va directo a la persona.

```bash
[0:v]gblur=sigma=18,eq=brightness=-0.06:saturation=0.9[bg];
```

---

## 3. Qué hace creíble un reemplazo real

Cinco cosas, en orden de cuánto delatan si fallan:

**1. La luz (mata todo lo demás).** Si el fondo nuevo tiene sol de tarde entrando por la derecha y tú
estás iluminado de frente por una ventana, no hay arreglo. **Elige el fondo por la dirección de la luz,
no por lo bonito que sea.** Y si el fondo es cálido, calienta el sujeto (`263`).

**2. El desenfoque.** Un fondo perfectamente nítido detrás de una persona nítida = imposible. Ninguna
cámara real enfoca todo a la vez a esa distancia. **Siempre desenfoca el fondo nuevo**, aunque sea poco.
Es el arreglo de un minuto que más credibilidad da.

**3. La perspectiva y la altura.** La línea del horizonte del fondo tiene que pasar por la altura de tus
ojos si ambos están al mismo nivel. Y el lente tiene que ser parecido: si el fondo se ve comprimido
(teleobjetivo) y tú estás en gran angular de celular, no cuadra.

**4. El movimiento.** Si tu cámara tiembla y el fondo está clavado, el efecto se cae en el primer
segundo. O estabilizas el plano (`264`) o le das el mismo temblor al fondo.

**5. El rebote de color.** En la vida real, el color del entorno se refleja sobre la persona. Si te pongo
en una cocina con azulejos azules, deberías tener un toque azulado en los bordes. Es sutil y es lo que
separa "bien hecho" de "impecable". Se falsifica con una luz de borde del color del fondo (`263`,
sección 6).

---

## 4. El error de la luz, explicado

Es tan común que merece su propia sección.

**Lo que pasa:** eliges un fondo espectacular —una cocina profesional con luz de ventana lateral, una
playa al atardecer— y te pegas ahí. Y algo se siente mal aunque el recorte esté perfecto.

**Por qué:** tu cara tiene la luz de tu cuarto. Plana, de frente, temperatura de bombillo. El fondo tiene
luz lateral dura y anaranjada. El cerebro sabe cómo se ve una cara con luz lateral —con una mitad más
oscura— y la tuya no la tiene. **Te ve como un sticker aunque no sepa por qué.**

**Las tres soluciones, en orden de realismo:**

1. **Elige otro fondo.** Uno con luz frontal y suave, parecida a la tuya. Aburrido pero funciona.
2. **Grábate con luz parecida.** Si el fondo tiene luz por la izquierda, ponte una lámpara a la
   izquierda. Cinco minutos, y es la solución de verdad.
3. **Falsifícalo en post.** Oscurece un lado del sujeto con un degradado y ponle luz de borde del lado
   correcto. Funciona a medias y toma 15 minutos.

> **La regla:** el fondo se elige por la luz. Todo lo demás es negociable.

---

## 5. Cómo se hace el reemplazo

**En CapCut** (lo que vas a usar):
1. Pon el fondo nuevo (imagen o video) en la **pista de abajo**.
2. Pon tu clip en la pista de **arriba**.
3. Al de arriba: **Quitar fondo → Eliminación automática**.
4. Al fondo: **desenfócalo** y ajústale brillo/temperatura para que sea coherente.
5. A ti: ajusta temperatura y niveles para acercarte al fondo (`263`).

**Con ffmpeg**, con el recorte ya hecho:

```bash
ffmpeg -y -i fondo_nuevo.mp4 -i sujeto_recortado.mov -filter_complex "\
[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,\
gblur=sigma=14,eq=brightness=-0.04:saturation=0.94[bg];\
[1:v]scale=1080:1920,format=rgba,colortemperature=temperature=4600:mix=0.5[su];\
[bg][su]overlay=0:0:shortest=1,noise=alls=7:allf=t+u[out]" \
  -map "[out]" -map 1:a? -c:a copy -c:v libx264 -crf 18 -pix_fmt yuv420p reemplazo.mp4
```

Fíjate en el orden: el fondo se escala y recorta al vertical, se desenfoca y se apaga; el sujeto se
calienta para acercarlo al fondo; y **el grano va al final, sobre la mezcla**, que es lo que amarra las
dos capas (`263`).

### Fondo generado por IA: cómo pedirlo

Si vas a generar el fondo, el prompt tiene que incluir cosas que casi nadie pide:

```
cocina de restaurante, vacía, sin personas, fotografía con lente de 26 mm de celular,
luz suave frontal de ventana grande, temperatura neutra, profundidad de campo corta,
formato vertical 9:16, sin texto, sin marcas
```

Las cuatro partes que importan: **"vacía, sin personas"** (si no, te mete gente que después estorba),
**"lente de 26 mm de celular"** (para que la perspectiva cuadre con tu material), **"luz suave frontal"**
(para que coincida con tu luz de ventana) y **"profundidad de campo corta"** (ya viene desenfocado).

---

## 6. Reemplazo de cielo

Caso especial y el más agradecido: el cielo blanco y quemado de un día nublado mata cualquier plano
exterior.

**Cuándo se puede:** cuando el cielo es una zona clara, continua y bien separada de lo que hay abajo.
Un horizonte limpio: sí. Ramas de árbol contra el cielo: no, en absoluto.

**En CapCut:** no hay reemplazo de cielo dedicado. Lo que puedes hacer es **croma sobre el color del
cielo** (herramienta Croma, gotero sobre el azul) o una **máscara lineal** con el cielo arriba. La
máscara lineal es más fiable si el horizonte es recto.

**Con ffmpeg**, la vía de la luminancia:

```bash
# 1. Volver transparente lo muy claro (el cielo quemado)
ffmpeg -y -i plano.mp4 -vf "format=rgba,lumakey=threshold=0.88:tolerance=0.10:softness=0.12" \
  -c:v prores_ks -profile:v 4444 -pix_fmt yuva444p10le sin_cielo.mov

# 2. Poner el cielo nuevo detrás
ffmpeg -y -i cielo_nuevo.jpg -i sin_cielo.mov -filter_complex "\
[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=4[cielo];\
[1:v]format=rgba[fg];\
[cielo][fg]overlay=0:0:shortest=1,noise=alls=6:allf=t+u[out]" \
  -map "[out]" -c:v libx264 -crf 18 -pix_fmt yuv420p con_cielo.mp4
```

> ⚠️ **Verifica esto en tu equipo antes de usarlo en producción.** `lumakey` se come **todo** lo claro:
> una camisa blanca, un reflejo en el capó, un letrero. Míralo sobre magenta antes de seguir (`261`).
> Si te come cosas de abajo, combínalo con una máscara: aplica el `lumakey` solo a la mitad superior
> recortando, procesando y volviendo a pegar.

**Las tres cosas que delatan un cielo falso:**

1. **El cielo nuevo es demasiado nítido y contrastado.** Un cielo real, sobre todo con neblina, es suave.
   `gblur=sigma=3..6` y bájale la saturación.
2. **La luz del suelo no corresponde.** Cielo azul brillante sobre una escena gris de día nublado: el
   suelo debería tener sol. Si le pones un cielo espectacular, tienes que **calentar y contrastar la
   escena de abajo** para que se lo crea.
3. **El borde del horizonte es duro.** El cielo se funde con la tierra por la neblina de distancia. Sube
   el `softness` del `lumakey` y añade una franja clara en el horizonte.

**La honestidad:** el reemplazo de cielo en video es de las cosas que peor salen con herramientas
básicas. En una **foto** funciona muy bien y hay apps que lo hacen en un clic. En video, con árboles o
con la cámara moviéndose, es un dolor de cabeza que casi nunca vale para un reel (`269`).

---

## 7. La opción intermedia que nadie considera

Antes de reemplazar el fondo entero, mira estas tres, que cuestan mucho menos y suelen bastar:

**7.1. Cambiar solo el color del fondo.** Con el recorte hecho, en vez de poner una imagen nueva, pon un
**bloque de color** de la marca. Se ve intencional, moderno, y no hay ningún problema de luz porque no
hay ninguna escena que imitar. Es la vía más segura y la que mejor rinde en un reel de marca.

**7.2. Oscurecer el fondo real.** Bajarle brillo y saturación al fondo (sin recortarlo, con una viñeta
fuerte, o con recorte). El desorden desaparece en la penumbra y la luz sigue siendo real.

**7.3. Cambiar solo una parte.** No hace falta reemplazar todo: a veces basta con tapar la esquina fea
(`265`).

---

## 8. Verificar un reemplazo

```bash
# El comparativo honesto: original vs reemplazo, lado a lado
ffmpeg -y -i original.mp4 -i reemplazo.mp4 -filter_complex \
  "[0:v]scale=540:960[a];[1:v]scale=540:960[b];[a][b]hstack" \
  -c:v libx264 -crf 20 -pix_fmt yuv420p comparacion.mp4
```

Y las preguntas, en este orden:

1. **¿La luz del sujeto podría venir de ese fondo?** Si no, todo lo demás sobra.
2. **¿El fondo está más suave que el sujeto?** Si no, desenfócalo.
3. **¿El horizonte está a la altura de los ojos?** Si no, mueve el fondo en vertical.
4. **¿Se mueven igual?** Si el plano tiembla y el fondo no, se cae.
5. **¿Hay grano encima de todo?** Sin eso, dos texturas distintas.
6. **¿Se ve mejor que el fondo real desenfocado?** Si la respuesta es "parecido", usa el real.

---

## Errores comunes

1. **Reemplazar cuando bastaba desenfocar.** El fondo real desenfocado tiene la luz correcta por
   definición y cuesta dos minutos.
2. **Elegir el fondo por bonito y no por la dirección de la luz.** Es el error que arruina el 80% de los
   reemplazos y no tiene arreglo en post.
3. **Dejar el fondo nuevo perfectamente nítido.** Ninguna cámara real enfoca todo a la vez. Desenfócalo
   siempre, aunque sea `sigma=8`.
4. **Fondo generado sin especificar el lente.** Un fondo de teleobjetivo con un sujeto de celular no
   cuadra nunca.
5. **Fondo generado con gente dentro.** Pide "vacío, sin personas" o vas a tener figuras estorbando.
6. **Fondo clavado con cámara temblorosa.** Estabiliza el plano o dale el mismo movimiento al fondo.
7. **Horizonte a la altura equivocada.** Debe pasar por los ojos si ambos están al mismo nivel.
8. **Olvidar el rebote de color.** Un toque del color del fondo en los bordes del sujeto es lo que
   separa bien hecho de impecable.
9. **`lumakey` para el cielo sin revisar qué más se comió.** Camisas blancas, reflejos, letreros.
10. **Cielo espectacular sobre escena gris.** Si pones sol arriba, tiene que haber sol abajo.
11. **Intentar cielo nuevo con ramas de árbol en el borde.** Es el peor caso posible. No lo intentes.
12. **No poner grano al final.** Dos capas de orígenes distintos con dos texturas distintas.
13. **Descartar el bloque de color plano.** Es la opción más segura, más rápida y muchas veces la que
    mejor se ve en un reel de marca.

---

## Checklist

Antes de dar por bueno un reemplazo de fondo:

- [ ] Me pregunté **por qué** lo quiero cambiar y descarté que bastara **desenfocar el real**.
- [ ] Elegí el fondo por la **dirección de la luz**, no por lo bonito.
- [ ] El fondo nuevo está **desenfocado** (`sigma` 8–25) y con menos contraste que el sujeto.
- [ ] La **temperatura** del sujeto y del fondo coinciden.
- [ ] El **horizonte** cae a la altura de los ojos.
- [ ] La **perspectiva del lente** es compatible (fondo pedido con "lente de 26 mm de celular").
- [ ] Si el plano tiene movimiento, el fondo **se mueve igual** (o estabilicé el plano).
- [ ] Hay un toque de **rebote de color** del fondo sobre el sujeto.
- [ ] Puse **grano al final, sobre la mezcla**.
- [ ] Si es cielo: revisé qué más se comió el `lumakey`, suavicé el horizonte y el suelo es coherente.
- [ ] Comparé **lado a lado con el original desenfocado**, y el reemplazo se ve claramente mejor.
- [ ] Si se veía "parecido", me quedé con el **fondo real**.

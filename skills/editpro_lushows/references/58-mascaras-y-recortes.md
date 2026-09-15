# 58 — Máscaras y recortes: aparecer dentro de una forma

> Una máscara es la herramienta que le dice a ffmpeg **qué parte de una imagen se ve y qué parte no**.
> Con eso se hacen los revelados dentro de una forma, los recortes de marca, las transiciones que no
> están en `xfade`, y la mitad de lo que en las apps se llama "efectos".

---

## Cómo piensa una máscara

Una máscara es una imagen en escala de grises del mismo tamaño que tu video:

- **Blanco (255)** = se ve la imagen de arriba.
- **Negro (0)** = se ve la imagen de abajo (o transparencia).
- **Gris** = se mezclan proporcionalmente. Un gris al 50% da 50% de cada una.

Eso es todo. La dificultad no está en el concepto: está en **generar la imagen de grises correcta y
animarla**.

Hay dos filtros. Se confunden todo el tiempo, así que la diferencia primero:

| Filtro | Qué recibe | Qué hace |
|---|---|---|
| `alphamerge` | 1 video + 1 máscara | Le pone **transparencia** al video. Salida con canal alfa. |
| `maskedmerge` | 2 videos + 1 máscara | **Mezcla los dos** según la máscara. Salida opaca. |

**Regla simple:** si quieres un archivo con transparencia para usarlo encima de otra cosa → `alphamerge`.
Si quieres el resultado final de dos videos combinados → `maskedmerge`.

---

## Generar máscaras con `geq`

`geq` pinta el valor de cada píxel según una fórmula. Las variables que importan:

| Variable | Qué es |
|---|---|
| `X`, `Y` | Coordenadas del píxel |
| `W`, `H` | Ancho y alto |
| `T` | Tiempo en segundos (**mayúscula** aquí; en `enable` es minúscula) |
| `lum(x,y)` | Luminancia de la imagen de entrada en esa posición |

### Máscara de círculo que crece (verificada)

```bash
ffmpeg -y -f lavfi -i "color=black:s=640x360:r=30:d=4" \
  -vf "geq=lum='if(lt(hypot(X-W/2,Y-H/2), (T/2)*W), 255, 0)':cb=128:cr=128,format=gray" \
  -c:v libx264 -preset veryfast -pix_fmt yuv420p mascara_circulo.mp4
```

Cómo se lee: `hypot(X-W/2, Y-H/2)` es la distancia de cada píxel al centro. Si esa distancia es menor
que `(T/2)*W`, píxel blanco; si no, negro. Como `T` crece con el tiempo, el círculo crece.

`cb=128:cr=128` pone los canales de color en neutro (gris). Sin eso salen colores raros.

### Máscara de rectángulo que barre

```bash
ffmpeg -y -f lavfi -i "color=black:s=1080x1920:r=30:d=1" \
  -vf "geq=lum='if(lt(X, W*T), 255, 0)':cb=128:cr=128,format=gray" \
  -c:v libx264 -preset veryfast -pix_fmt yuv420p mascara_barrido.mp4
```

### Máscara con borde suave (mucho más elegante)

El borde duro delata la máscara. Con un degradado en el borde queda infinitamente mejor:

```bash
ffmpeg -y -f lavfi -i "color=black:s=1080x1920:r=30:d=1" \
  -vf "geq=lum='clip(255*(W*T*1.2 - X)/120, 0, 255)':cb=128:cr=128,format=gray" \
  -c:v libx264 -preset veryfast -pix_fmt yuv420p mascara_suave.mp4
```

El `120` es el ancho del degradado en píxeles. Súbelo para un borde más difuso.

Alternativa más simple: generar la máscara dura y pasarle un desenfoque:

```bash
ffmpeg -y -i mascara_barrido.mp4 -vf "gblur=sigma=25,format=gray" \
  -c:v libx264 -preset veryfast -pix_fmt yuv420p mascara_suave2.mp4
```

Esto es más rápido que calcular el degradado en `geq` y da el mismo resultado.

---

## `maskedmerge`: revelar un video dentro de una forma

Este es el uso principal. Ejemplo verificado completo: el plano B se revela dentro de un círculo que
crece sobre el plano A.

```bash
ffmpeg -y -i planoA.mp4 -i planoB.mp4 -f lavfi -i "color=black:s=640x360:r=30:d=4" \
  -filter_complex \
"[2:v]geq=lum='if(lt(hypot(X-W/2,Y-H/2), (T/2)*W), 255, 0)':cb=128:cr=128,format=gray[mascara];\
 [0:v][1:v][mascara]maskedmerge[v]" \
  -map "[v]" -an -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p revelado.mp4
```

El orden de las tres entradas de `maskedmerge` importa y no es intuitivo:

```
[base][encima][mascara]maskedmerge
```

- Donde la máscara es **negra** se ve `[base]`.
- Donde la máscara es **blanca** se ve `[encima]`.

Si te sale al revés, invierte la máscara con `negate` o cambia el `if`.

### Requisito estricto

Los tres (los dos videos y la máscara) deben tener **exactamente la misma resolución y el mismo
formato de píxel**. Si no, ffmpeg falla igual que con `xfade`. Normaliza antes:

```
[0:v]scale=1080:1920,fps=30,format=yuv420p,setsar=1[a]
```

---

## `alphamerge`: crear un elemento con transparencia

Este es el que se usa para fabricar gráficos de marca reutilizables. Ejemplo verificado: una franja
de damero con fondo transparente.

```bash
ffmpeg -y -f lavfi -i "color=c=0xE10600:s=768x360" \
        -f lavfi -i "color=c=white:s=768x360" \
  -filter_complex \
"[1:v]format=gray,geq=lum='if(lt(mod(floor(X/48)+floor(Y/48),2),1),255,0)'[m];\
 [0:v][m]alphamerge[franja]" \
  -map "[franja]" -frames:v 1 franja.png
```

Resultado: `franja.png` con damero rojo y huecos transparentes. Este PNG ya se puede usar en cualquier
`overlay` — es exactamente la técnica de `52-transiciones-de-marca.md`.

### Para video con transparencia (no imagen fija)

Un MP4 **no puede** llevar canal alfa. Si necesitas un video con transparencia, hay que usar otro
contenedor y otro códec. El más compatible:

```bash
ffmpeg -y -i color.mp4 -i mascara.mp4 -filter_complex \
"[1:v]format=gray[m];[0:v][m]alphamerge[v]" \
  -map "[v]" -c:v qtrle -pix_fmt argb elemento.mov
```

Verificado: sale `qtrle` / `argb`, o sea con alfa real. Advertencia: `qtrle` no comprime casi nada.
Un elemento de 5 segundos en 1080×1920 puede pesar cientos de megas. Es archivo intermedio, no
entregable.

Otras opciones con alfa: `prores_ks` con `-profile:v 4444`, o `libvpx-vp9` con `-pix_fmt yuva420p`.

---

## Casos de uso reales

### 1. El logo que revela el plano

El plano nuevo aparece dentro de la silueta del logotipo, que crece hasta llenar la pantalla. Se hace
con el logo en PNG (blanco sobre negro), escalado con `zoompan`, usado como máscara.

```bash
ffmpeg -y -i planoA.mp4 -i planoB.mp4 -loop 1 -i logo_blanco_sobre_negro.png \
  -filter_complex \
"[2:v]scale=1080:1920,zoompan=z='min(1+in_time*3, 12)':d=90:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30,format=gray[m];\
 [0:v][1:v][m]maskedmerge[v]" \
  -map "[v]" -an -t 3 -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p logo_revela.mp4
```

Es el cierre de marca más eficaz que hay. Ojo con la duración: 0,6–1,0 s, no más.

### 2. Texto que revela imagen dentro de las letras

El mismo principio, pero la máscara es texto blanco sobre negro:

```bash
ffmpeg -y -i fondo.mp4 -f lavfi -i "color=black:s=1080x1920:r=30:d=3" \
  -filter_complex \
"[1:v]drawtext=text='GASTRO':fontfile='C\\:/Windows/Fonts/arialbd.ttf':fontsize=220:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2,format=gray[m];\
 [1:v][0:v][m]maskedmerge[v]" \
  -map "[v]" -an -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p texto_relleno.mp4
```

En Windows la ruta de la fuente lleva la barra invertida escapando los dos puntos: `C\:/Windows/...`.
Es una de las trampas clásicas (ver `109`).

### 3. Recorte en forma para picture-in-picture

Un segundo video dentro de un círculo, encima del principal — el formato de reacción / comentario:

```bash
ffmpeg -y -i principal.mp4 -i pequeno.mp4 -f lavfi -i "color=black:s=400x400:r=30" \
  -filter_complex \
"[1:v]scale=400:400:force_original_aspect_ratio=increase,crop=400:400[peq];\
 [2:v]geq=lum='if(lt(hypot(X-200,Y-200),195),255,0)':cb=128:cr=128,format=gray,gblur=sigma=2[m];\
 [peq][m]alphamerge[circulo];\
 [0:v][circulo]overlay=x=W-450:y=100[v]" \
  -map "[v]" -an -t 5 -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p pip.mp4
```

El `gblur=sigma=2` sobre la máscara suaviza el borde del círculo. Sin él, el borde queda escalonado y
se ve amateur. **Ese detalle de 2 píxeles es la diferencia entre "recorte" y "recorte profesional".**

### 4. Transición que no existe en `xfade`

Si necesitas un revelado que no está en las 58, se construye con máscara animada. Ejemplo: revelado
en diagonal desde la esquina, con borde suave:

```bash
ffmpeg -y -i planoA.mp4 -i planoB.mp4 -f lavfi -i "color=black:s=1080x1920:r=30:d=4" \
  -filter_complex \
"[2:v]geq=lum='clip(255*((X+Y) - (T/1.5)*(W+H))/-200, 0, 255)':cb=128:cr=128,format=gray[m];\
 [0:v][1:v][m]maskedmerge[v]" \
  -map "[v]" -an -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p diagonal.mp4
```

Aquí `(X+Y)` define la diagonal y el `-200` el ancho del degradado del borde.

---

## Cuándo usar máscara y cuándo no

| Situación | Herramienta |
|---|---|
| Una de las 58 transiciones sirve | **`xfade`.** No compliques. |
| Necesitas una forma específica de la marca | Máscara |
| Quieres un elemento reutilizable con transparencia | `alphamerge` → PNG o MOV |
| Quieres separar a una persona del fondo | **Ni una ni otra.** Croma o `rembg`. Ver `81`. |
| Picture-in-picture redondo | `alphamerge` + `overlay` |
| Rellenar texto con video | `maskedmerge` con `drawtext` como máscara |

**Lo que las máscaras de ffmpeg NO hacen:** seguir a un objeto que se mueve. Para eso necesitas
rotoscopia o segmentación por IA. ffmpeg puede aplicar una máscara, no calcular dónde está la persona.

---

## El costo de `geq` (repetido porque es importante)

`geq` evalúa la expresión **por píxel y por fotograma**. En 1080×1920 a 30 fps son 62 millones de
evaluaciones por segundo de video. Las máscaras hechas con `geq` a resolución completa son lentísimas.

Estrategias, en orden de preferencia:

1. **Pre-renderiza la máscara una vez** como archivo aparte y reutilízala. Si la vas a usar varias
   veces, es gratis a partir de la segunda.
2. **Genera la máscara a resolución baja** y escálala:
   `geq=...,scale=1080:1920` — para formas grandes y suaves no se nota.
3. **Usa formas prefabricadas.** Un PNG del círculo o de la forma, animado con `zoompan` o `scale`, es
   muchísimo más rápido que calcularlo con `geq`.
4. **Solo usa `geq` en tiempo real** cuando la forma depende de la imagen de entrada (`lum(x,y)`) y no
   se puede pre-renderizar.

---

## Errores comunes

- **Confundir `alphamerge` con `maskedmerge`.** `alphamerge` da transparencia (1 video + máscara);
  `maskedmerge` combina dos videos. Si el resultado sale opaco cuando lo querías transparente, usaste
  el equivocado.

- **Orden invertido en `maskedmerge`.** Es `[base][encima][mascara]`. Blanco muestra el segundo, negro
  el primero. Si sale al revés, invierte la máscara con `negate`.

- **Olvidar `format=gray` en la máscara.** ffmpeg puede quejarse o dar resultados con color extraño.
  La máscara siempre en gris.

- **Olvidar `cb=128:cr=128` en `geq`.** Sin eso los canales de color quedan en valores raros y la
  máscara sale teñida.

- **Máscaras de resolución distinta a los videos.** Falla igual que `xfade`. Normaliza los tres.

- **Borde duro sin suavizar.** Un borde escalonado delata el recorte. Un `gblur=sigma=2` sobre la
  máscara lo arregla. Es el detalle que más sube la percepción de calidad en este módulo.

- **Intentar guardar transparencia en MP4.** No existe. Usa `.mov` con `qtrle` o `prores_ks -profile:v 4444`,
  o `.webm` con VP9 y `yuva420p`.

- **Confundir `T` con `t`.** En `geq` la variable de tiempo es `T` mayúscula. En `enable` es `t`
  minúscula. Cruzarlas produce `Undefined constant`.

- **Calcular `geq` a resolución completa cuando se podía pre-renderizar.** Renders eternos para un
  resultado idéntico.

- **Esperar que una máscara siga a una persona.** ffmpeg no rastrea. Para eso hace falta otra
  herramienta (ver `81`).

- **Usar máscara cuando `xfade` bastaba.** Complejidad gratis. Solo si la forma responde a la marca.

---

## Checklist

- [ ] Sé si necesito `alphamerge` (transparencia) o `maskedmerge` (combinar dos).
- [ ] El orden de `maskedmerge` es `[base][encima][mascara]` y comprobé que no está invertido.
- [ ] La máscara está en `format=gray`.
- [ ] Si generé la máscara con `geq`, incluí `cb=128:cr=128`.
- [ ] Los dos videos y la máscara tienen la misma resolución, fps y formato de píxel.
- [ ] El borde de la máscara está suavizado (`gblur=sigma=2` o degradado en la fórmula).
- [ ] Si la máscara se reutiliza, la pre-rendericé en vez de recalcularla.
- [ ] Si necesito transparencia en archivo, uso `.mov` con `qtrle` o ProRes 4444, no `.mp4`.
- [ ] Las variables de tiempo están bien: `T` en `geq`, `t` en `enable`.
- [ ] La forma de la máscara sale de la marca o de la narrativa, no es un capricho.
- [ ] Comprobé que `xfade` no resolvía esto más simple.
- [ ] Verifiqué el render buscando bordes escalonados o parpadeo en la máscara (`98`).

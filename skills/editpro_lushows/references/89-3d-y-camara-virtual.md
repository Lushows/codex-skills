# 89 — 3D y cámara virtual

**Qué resuelve:** la tentación de meter 3D porque se ve "de agencia". Este módulo es sobre todo un
filtro de decisión: cuándo el 3D resuelve algo que no se puede resolver de otra forma, cuándo es
capricho caro, y **qué trucos de dos dimensiones se ven caros sin serlo**. La mayoría de las veces la
respuesta correcta es el truco.

---

## 1. La pregunta antes de abrir nada

> **¿Qué información necesita el espectador que solo se puede dar en tres dimensiones?**

Si la respuesta es "ninguna, es que se ve bonito", no es 3D: es tiempo perdido. Casi siempre hay una
solución 2D que da el 80% del efecto por el 5% del trabajo.

Las tres respuestas legítimas:

1. **Mostrar un producto que hay que ver por todos lados** — un empaque, una máquina, un objeto que no
   existe todavía o que no puedes filmar.
2. **Explicar algo espacial** — cómo encaja una pieza, cómo se distribuye un local, un corte
   transversal.
3. **Un remate de marca con volumen** — el logo como objeto físico. Y ojo: esto se hace **una vez** y se
   reusa en todas las piezas (`88`), no se rehace cada video.

Todo lo demás — texto en 3D, cámaras volando por el espacio, planetas girando — es decoración de 2015.

---

## 2. Lo que cuesta el 3D de verdad

Números honestos para calibrar la decisión:

| Tarea | Tiempo realista |
|---|---|
| Modelar un empaque sencillo con su etiqueta | 3 – 6 horas |
| Iluminar para que no se vea plástico | 2 – 4 horas |
| Animar la cámara y afinar el timing | 1 – 2 horas |
| Renderizar 5 s en 1080x1920 (equipo normal) | 40 min – 4 horas |
| Corregir cuando el cliente cambia el color de la etiqueta | 1 – 2 horas más |

Y ese es el caso bueno: alguien que ya sabe. Si estás aprendiendo, multiplica por tres.

**Compáralo con la alternativa:** una fotografía buena del producto sobre fondo limpio, con parallax por
capas (`83`) y un empuje de cámara, cuesta **45 minutos** y en video social se ve igual de bien o mejor,
porque es real (`152`).

> **La ley que aplica:** real para lo tangible. Si el producto existe, se fotografía. El 3D es para lo
> que no existe.

---

## 3. Los cuatro trucos 2D que se ven caros

Aquí está el valor práctico del módulo. Estos cuatro dan sensación de volumen sin tocar 3D.

### a) Parallax por capas (el rey)

Ya está detallado en `83`. Tres capas moviéndose a velocidades distintas producen profundidad real en la
percepción. Es el truco con mejor retorno que existe en motion.

Para producto: recorta el producto (`81`), pon un fondo aparte, y muévelos distinto.

```bash
ffmpeg -loop 1 -framerate 25 -t 4 -i fondo.png -loop 1 -framerate 25 -t 4 -i producto.png \
  -filter_complex "\
[0:v]scale=1260:-2,crop=1080:1920:'(iw-1080)/2-26*(t/4)':'(ih-1920)/2'[bg];\
[1:v]scale=-1:1150,format=rgba[pr];\
[bg][pr]overlay=x='(W-w)/2-130*(t/4)':y='(H-h)/2+18*(t/4)',format=yuv420p[vout]" \
  -map "[vout]" -c:v libx264 -crf 18 -pix_fmt yuv420p producto_3d_falso.mp4
```

### b) Sombra de contacto

Un objeto sin sombra flota y se ve pegado; con una sombra suave debajo, se posa. Es lo que más rápido
convierte un recorte plano en un objeto con peso (principio de dibujo sólido, `85`).

```bash
-filter_complex "\
[1:v]scale=-1:1150,format=rgba,split=2[pr][sh];\
[sh]colorchannelmixer=rr=0:gg=0:bb=0:aa=0.34,boxblur=26:2,scale=w='iw':h='ih*0.16',setsar=1[shb];\
[0:v][shb]overlay=x=(W-w)/2:y=1420[c1];\
[c1][pr]overlay=x=(W-w)/2:y=(H-h)/2[vout]"
```

Aplasta la copia negra al 16% de su altura y la difumina: queda un óvalo bajo el objeto. Es el mismo
truco que usan los renders de catálogo.

### c) Perspectiva falsa con el filtro `perspective`

ffmpeg trae un filtro que deforma la imagen moviendo sus cuatro esquinas. Sirve para inclinar un
elemento plano y que parezca en un plano 3D: una pantalla, una tarjeta, una etiqueta.

```bash
ffmpeg -i captura.png -vf "\
format=rgba,\
perspective=x0=0:y0=60:x1=W:y1=0:x2=40:y2=H:x3=W-40:y3=H:sense=destination:eval=init,\
format=rgba" -y captura_inclinada.png
```

Las coordenadas son las cuatro esquinas destino: arriba-izquierda, arriba-derecha, abajo-izquierda,
abajo-derecha. Con `sense=destination` le dices "llévame estas esquinas a estas posiciones".

Para que la inclinación se **anime** hay que usar `eval=frame` con expresiones en `t`, pero es pesado y
frágil. Lo práctico: genera 2–3 posiciones fijas y encadena, o prerrenderiza la secuencia.

### d) Rotación con contacto

Girar levemente un elemento mientras entra da sensación de espacio. Con `c=none` para no perder alfa:

```bash
[1:v]format=rgba,rotate='0.10*(1-clip(t/0.5,0,1))':c=none:ow=rotw(0.12):oh=roth(0.12)[el]
```

Entra girado 0,10 radianes (unos 6 grados) y se endereza al llegar. Sutil, físico, gratis.

---

## 4. Cámara virtual sin 3D: `v360`

Si tienes una imagen panorámica o equirectangular (una foto 360, o una generada así), `v360` te deja
"mirar" hacia distintos lados como si tuvieras una cámara dentro de la escena. Es lo más parecido a una
cámara virtual que hay en ffmpeg puro.

```bash
ffmpeg -loop 1 -framerate 25 -t 5 -i panorama_equirect.jpg -vf "\
v360=input=equirect:output=flat:h_fov=68:v_fov=100:\
yaw='-18+7*t':pitch='2':w=1080:h=1920,\
format=yuv420p" -c:v libx264 -crf 18 recorrido.mp4
```

- `yaw` — giro horizontal, animado con `t`. Aquí barre 35 grados en 5 segundos.
- `pitch` — inclinación vertical.
- `h_fov` / `v_fov` — campo de visión. Más bajo = más teleobjetivo = más comprimido y más "cine".

Sirve para recorridos de local, escenas generadas, fondos ambientales. No sirve para producto.

---

## 5. Cuándo sí: el flujo con 3D real

Si de verdad hace falta, la ruta seria es **Blender** (gratis, abierto) renderizando secuencia PNG con
alfa, y ffmpeg componiendo. Detalle de infraestructura en `engineer_visualopen_lushows`; lo que te toca
como editor es esto:

```bash
# 1. Render desde Blender por linea de comandos, PNG con alfa
blender -b escena.blend -o "//render/frame_####" -F PNG -x 1 -a

# 2. Secuencia PNG -> video con alfa (ProRes 4444) para poder componer
ffmpeg -framerate 25 -i render/frame_%04d.png \
  -c:v prores_ks -profile:v 4444 -pix_fmt yuva444p10le -alpha_bits 16 elemento3d.mov

# 3. Componer sobre el plano real
ffmpeg -i base.mp4 -i elemento3d.mov \
  -filter_complex "[1:v]scale=-1:900,format=rgba[e3];\
[0:v][e3]overlay=x=(W-w)/2:y=560:enable='between(t,2.0,6.0)',format=yuv420p[vout]" \
  -map "[vout]" -map 0:a -c:a copy -c:v libx264 -crf 18 salida.mp4
```

**Lo crítico de este flujo:** en Blender, el fondo va **transparente** (Film > Transparent). Si
renderizas con fondo, vuelves al problema del módulo `81` y tienes que sacar croma de un render, que es
absurdo pudiendo tener alfa desde el origen.

**Nunca renderices directo a mp4 desde Blender** si vas a componer: pierdes el alfa y pierdes calidad.
Secuencia PNG siempre. Ocupa mucho y se borra después.

### Las tres cosas que delatan un 3D amateur

1. **Iluminación plana.** Una sola luz frontal = plástico. Mínimo tres: principal, relleno suave y una
   de contra que separe el objeto del fondo.
2. **Materiales sin imperfección.** Nada real es perfectamente liso. Un poco de rugosidad y una textura
   de huellas o polvo cambian todo.
3. **Movimiento de cámara lineal.** El mismo problema de `84`, pero en 3D se nota diez veces más porque
   la cámara real tiene inercia. Ease in-out siempre.

---

## 6. 3D generado por IA (agosto 2026)

Existen modelos de imagen a 3D y de texto a 3D que producen mallas en minutos. La evaluación honesta a
esta fecha:

- **Sirve** para objetos genéricos de fondo, formas simples, elementos que se ven de lejos o borrosos.
- **No sirve** para el producto protagonista: la topología es sucia, los detalles finos se pierden, y el
  texto de una etiqueta sale ilegible.
- **La alternativa que sí funciona:** generar el producto como **imagen** desde varios ángulos con un
  modelo de imagen y montar el giro como secuencia. No es 3D pero se ve como 3D, y el control de estilo
  es mucho mayor (`122`, `126`).

El riesgo de siempre: la IA no respeta la marca. Si el empaque tiene un logo, va a inventarlo. Para
producto real, la respuesta sigue siendo la fotografía.

---

## 7. Texto en 3D: casi siempre no

El texto con extrusión y bisel se ve a 2015. Si necesitas que el texto tenga presencia, hay caminos
mejores:

- **Peso tipográfico + escala.** Un texto grande en negra bien puesto pesa más que uno en 3D.
- **Sombra larga plana** (long shadow), que da volumen sin extrusión.
- **Máscara sobre video** — el texto recortado dejando ver material en movimiento por dentro (`58`).
  Este sí se ve caro y cuesta una línea:

```bash
ffmpeg -i base.mp4 -f lavfi -i "color=c=black:s=1080x1920" \
  -filter_complex "[1:v]drawtext=fontfile='C\:/Windows/Fonts/Poppins-Bold.ttf':\
text='GASTRO':fontsize=300:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2,format=gray[mask];\
[0:v][mask]alphamerge,format=yuva420p[vout]" \
  -map "[vout]" -c:v prores_ks -profile:v 4444 -pix_fmt yuva444p10le texto_ventana.mov
```

El video se ve **dentro** de las letras. Eso sí impresiona, y no hay un solo polígono involucrado.

---

## 8. La tabla de decisión

| Lo que necesitas | Solución | Costo |
|---|---|---|
| Producto real con volumen | foto + recorte + parallax + sombra | 45 min |
| Producto que no existe todavía | 3D real (Blender) | 6–12 h |
| Mostrar el producto por todos lados | secuencia de fotos en giro, o 3D si no existe | 2 h / 8 h |
| Recorrido por un espacio | video real, o `v360` sobre panorámica | 1 h |
| Logo con volumen para el remate | 3D real **una vez**, se reusa siempre | 4 h una vez |
| Pantalla o tarjeta inclinada | filtro `perspective` | 15 min |
| Texto con presencia | máscara sobre video, no extrusión | 20 min |
| "Que se vea de agencia" | no es un requisito, es un deseo. Pregunta qué significa | — |

---

## 9. Cuándo es capricho (dilo)

Parte del oficio es decir que no. Es capricho cuando:

- El video dura 20 segundos y el 3D aparece 1,5. Nadie lo va a apreciar.
- El producto existe y se puede fotografiar.
- El objetivo es un anuncio de rendimiento. En pauta, lo que rinde es el mensaje y el gancho, no el
  render (`145`). Un 3D bonito con un mal gancho pierde contra un celular con buen gancho.
- El presupuesto y el plazo no dan, y el resultado va a ser un 3D malo — que se ve **peor** que no tener
  3D. Un render mediocre grita "aficionado" más fuerte que una foto sencilla bien iluminada.
- Nadie sabe explicar qué comunica. "Se ve chévere" no es un objetivo.

Cuando digas que no, ofrece la alternativa concreta con el tiempo que toma. "No hagamos 3D del empaque:
con una foto buena, recorte y parallax lo tenemos en una hora y se ve real." Eso se acepta; un "no" solo,
no.

---

## Errores comunes

1. **Meter 3D porque "se ve de agencia".** No es un requisito, es un deseo sin definir. Pregunta qué se
   quiere comunicar.
2. **Modelar un producto que existe.** Fotográfialo. Sale mejor, más rápido y es real.
3. **Un render mediocre.** Se ve peor que no tener render. Si el tiempo no da, no lo hagas.
4. **Renderizar desde Blender directo a mp4.** Pierdes el alfa y no puedes componer. Secuencia PNG.
5. **Olvidar el fondo transparente en Blender.** Terminas sacando croma de un render, que es absurdo.
6. **Una sola luz.** El objeto se ve de plástico. Mínimo tres: principal, relleno y contra.
7. **Materiales perfectamente lisos.** Nada real es liso. Un poco de rugosidad cambia todo.
8. **Movimiento de cámara lineal.** En 3D se nota diez veces más que en 2D. Ease in-out siempre.
9. **Objeto sin sombra de contacto.** Flota. Un óvalo difuminado bajo el objeto lo posa.
10. **Texto extruido con bisel.** Se ve a 2015. Máscara sobre video en su lugar.
11. **Olvidar `c=none` al rotar** un elemento con alfa. Las esquinas se llenan de negro.
12. **Confiar en IA de 3D para el producto protagonista.** Topología sucia, etiquetas ilegibles, logos
    inventados.
13. **Rehacer el logo 3D en cada pieza.** Se hace una vez y se reusa (`88`).

---

## Checklist

Antes de meter 3D o cámara virtual:

- [ ] Respondí **qué información** necesita el espectador que solo se puede dar en 3D.
- [ ] Verifiqué que el objeto **no se pueda fotografiar** (si existe, se fotografía).
- [ ] Comparé el costo real contra la alternativa 2D (parallax + sombra + empuje) y la diferencia lo
      justifica.
- [ ] Si es 2D disfrazado: hay **parallax**, **sombra de contacto** y **empuje con curva**.
- [ ] Si es 3D real: renderizado a **secuencia PNG con alfa**, fondo transparente en Blender.
- [ ] La secuencia se convirtió a **ProRes 4444** antes de componer, no a mp4.
- [ ] Hay **al menos tres luces** y los materiales tienen imperfección.
- [ ] El movimiento de cámara tiene **ease in-out**, no es lineal.
- [ ] El objeto tiene **sombra de contacto**.
- [ ] Si es un elemento de marca, se guardó como **activo reutilizable**, no se rehace cada vez.
- [ ] Si decidí que era capricho, **lo dije y ofrecí la alternativa** con su tiempo estimado.

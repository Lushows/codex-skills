# 168 — Animación y explainer

**Qué resuelve:** hay que explicar algo que **no se puede filmar** — cómo funciona un software, qué es un
impuesto, cómo se mueve la plata en un negocio, un proceso invisible. No eres motion designer, no tienes
After Effects ni tres semanas. Este módulo es cómo se produce un explainer que se ve profesional con
recursos limitados y sin pretender ser un estudio de animación.

> **Término nuevo — explainer:** video corto (45 s a 3 min) que explica un concepto, producto o proceso
> usando gráficos animados y voz en off. No hay actores ni locaciones: todo se construye.

---

## 1. La decisión que define todo: ¿cuánta animación de verdad necesitas?

La mayoría de explainers no necesitan animación. Necesitan **movimiento**. Son cosas distintas y confundirlas
cuesta semanas.

| Nivel | Qué es | Cuánto cuesta | Cuándo |
|---|---|---|---|
| **1. Estático + movimiento de cámara** | Ilustraciones fijas con paneo y zoom | Horas | El 60% de los casos |
| **2. Elementos que entran y salen** | Cosas que aparecen, se desplazan, escalan | 1–2 días | El estándar profesional |
| **3. Personajes que se mueven** | Brazos, caminatas, expresiones | Semanas | Casi nunca lo justifica |
| **4. Animación cuadro a cuadro** | Dibujado frame por frame | Meses | No |

**El nivel 2 es donde vive el 90% del trabajo bueno.** Un explainer nivel 2 bien ritmado se ve mejor que
un nivel 3 mal ejecutado. La gente no juzga cuánto se movió; juzga si entendió.

---

## 2. Se empieza por la voz en off, no por la imagen

Esta es la inversión que casi nadie hace y la que resuelve el formato.

```
1. Guion escrito
2. Voz en off grabada y aprobada       ← aquí queda fija la duración
3. Storyboard sobre los tiempos de la voz
4. Recursos gráficos
5. Animación
6. Sonido y música
```

**Si animas antes de tener la voz, vas a rehacerlo todo.** La voz define cuántos segundos dura cada idea,
y cada segundo de animación cuesta.

### El guion del explainer

Reglas duras:

- **130–150 palabras por minuto.** Más rápido no se entiende, más lento aburre.
- Una idea por frase. Frases de 8–14 palabras.
- **Cada frase tiene que ser dibujable.** Si no puedes imaginar qué se ve mientras se dice, la frase está
  mal escrita. Reescríbela, no inventes un gráfico decorativo.
- Sin adjetivos de marketing. "Innovadora solución integral" no se puede dibujar.

```
MAL:   "Nuestra plataforma integral optimiza tus procesos operativos."
       (¿qué se ve? nada)
BIEN:  "Hoy anotas las facturas en un cuaderno. Y el cuaderno se pierde."
       (se ve: cuaderno, facturas, cuaderno que desaparece)
```

### La estructura de 4 actos

```
0:00 – 0:12   EL PROBLEMA. Concreto, de la vida real, con un personaje o situación.
0:12 – 0:20   POR QUÉ IMPORTA. La consecuencia. El costo de no resolverlo.
0:20 – 0:50   LA SOLUCIÓN. Cómo funciona, en 3 pasos máximo.
0:50 – 1:05   EL RESULTADO + CTA.
```

**Nunca más de 3 pasos.** Si el producto tiene 7 funciones, el explainer muestra 3 y las otras 4 viven en
otro lado.

### Medir la duración antes de dibujar nada

```bash
# Cuánto dura la voz grabada, exacto
ffprobe -v error -show_entries format=duration -of csv=p=0 vo.wav

# Mapa de dónde termina cada frase (silencios entre frases)
ffmpeg -i vo.wav -af silencedetect=noise=-35dB:d=0.35 -f null - 2> frases.txt
```

Ese `frases.txt` **es tu storyboard temporal**. Cada bloque entre silencios es una escena.

---

## 3. De dónde salen los gráficos sin ser diseñador

### Opción A — Sistema propio de formas (la más honesta)

Rectángulos, círculos, líneas y tipografía, en los colores de la marca. Suena pobre y no lo es: es el
lenguaje de los explainers de Stripe, Linear y media Silicon Valley. La clave es **consistencia absoluta**:
mismo radio de esquina, mismo grosor de línea, misma paleta de 3 colores.

Se generan como PNG con transparencia desde HTML/CSS renderizado, o directamente con ffmpeg para lo simple.

### Opción B — Ilustración generada con IA

Sirve, con dos condiciones:
1. **Mismo prompt de estilo en todas** las imágenes, o el video parece un collage
2. **Fondo transparente** para poder animarlas por capas → `81-recortes-sin-fondo.md`

Ver `122-generar-imagen-para-video.md` para cómo mantener coherencia de estilo entre generaciones.

### Opción C — Capturas reales del producto

Si el explainer es de software, **las capturas reales ganan a cualquier ilustración**. La gente quiere ver
la pantalla de verdad. Se limpian, se enmarcan y se animan por partes.

### Opción D — Iconos de librería

Rápido y aceptable si son de **una sola familia**. Mezclar dos familias de iconos se nota inmediatamente.
Ojo con las licencias → `49-fuentes-y-licencias-para-video.md`.

> **Regla anti-genérico:** nada de gente 3D azul flotando, nada de "corporate memphis" (los personajes de
> brazos larguísimos y colores planos). Se ve de plantilla desde el primer fotograma y le baja el nivel a
> la marca. → `56-efectos-que-se-ven-baratos.md`.

---

## 4. Los cinco movimientos que resuelven un explainer entero

No necesitas más que estos.

### 1. Entrada por desplazamiento + fundido

El elemento entra desde abajo 30–40 px mientras aparece. Duración: 0,3–0,4 s.

```bash
# Un PNG que sube y aparece entre el segundo 2,0 y el 2,35
ffmpeg -i fondo.mp4 -i elemento.png -filter_complex \
 "[1:v]format=rgba,fade=t=in:st=2.0:d=0.35:alpha=1[el]; \
  [0:v][el]overlay=x=340:y='if(lt(t,2.35), 620+40*(1-(t-2.0)/0.35), 620)':enable='gte(t,2.0)'[v]" \
 -map "[v]" -c:v libx264 -crf 18 salida.mp4
```

### 2. Escala con sobre-impulso

El elemento crece del 92% al 103% y vuelve al 100%. Ese rebote de 6% es lo que separa "animado" de
"aparecido". → `42-anatomia-del-golpe.md`, `84-keyframes-y-curvas.md`.

### 3. Paneo sobre imagen grande (efecto Ken Burns)

Una ilustración grande y la cámara se mueve sobre ella. Da vida sin animar nada.

```bash
# Zoom lento del 100% al 112% sobre 5 s, centrado
ffmpeg -loop 1 -i ilustracion.png -t 5 -vf \
 "scale=4000:-1,zoompan=z='min(zoom+0.0006,1.12)':d=125:x='iw/2-(iw/zoom/2)':\
y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25,format=yuv420p" -c:v libx264 -crf 18 panorama.mp4
```

⚠️ `zoompan` funciona mal si no escalas la imagen a gran tamaño primero: produce saltos. El `scale=4000`
previo es obligatorio.

### 4. Recorrido de línea (línea que se dibuja sola)

Para procesos y flujos. Se hace con una máscara rectangular que crece sobre la línea ya dibujada.

```bash
# La línea se revela de izquierda a derecha en 1,2 s
ffmpeg -i fondo.mp4 -i linea.png -filter_complex \
 "[1:v]format=rgba[l];[0:v][l]overlay=0:0[base]; \
  [base]crop=w='min(iw, iw*(t-1.0)/1.2)':h=ih:x=0:y=0,pad=1920:1080:0:0:black@0[v]" \
 -map "[v]" -c:v libx264 -crf 18 linea_anim.mp4
```

(En la práctica esto se arma mejor en el editor o con un GIF/WebM con alfa preparado aparte.)

### 5. Corte duro sincronizado con la voz

El movimiento más subestimado: **no animar nada** y simplemente cortar a la siguiente pantalla en la
palabra clave. Rápido, limpio, y rinde igual que una transición elaborada.

---

## 5. Ritmo del explainer

| Elemento | Tiempo en pantalla |
|---|---|
| Una idea completa | 4 – 7 s |
| Elemento que entra | 0,3 – 0,4 s de animación |
| Elemento que se queda solo | mínimo 1,2 s antes de que entre otro |
| Pantalla con 3 elementos | 5 – 8 s |
| Transición entre actos | 0,5 – 0,8 s |

**Nunca metas dos elementos a la vez.** Entran en cascada, con 0,15–0,25 s de diferencia. Eso es lo que se
llama *stagger* y es la diferencia entre una animación profesional y una amateur.

```
MAL:   [A][B][C] entran los tres en t=2,0
BIEN:  A en 2,00 · B en 2,18 · C en 2,36
```

### La regla del elemento que se queda

Todo lo que entra tiene que **quedarse el tiempo suficiente para leerse**. Un dato en pantalla 0,6 s no
existió. Mínimo:

```
Palabra suelta:      1,0 s
Frase corta:         1,8 s
Cifra con contexto:  2,2 s
```

---

## 6. Voz en off para explainer

- **Tono explicativo, no comercial.** El locutor de radio comercial mata el formato.
- **Segunda persona.** "Si tienes un restaurante, esto te pasa."
- **Pausas de 0,4–0,6 s entre ideas.** Sin eso, el explainer atropella.
- Grabada con micrófono decente, en una sala con cortinas o ropa (el eco arruina más que el ruido).

Si es voz generada (TTS o clonada), lo que la delata no es el timbre sino **la falta de variación de
ritmo**. Se arregla partiendo el texto en frases y generándolas por separado, con pausas manuales entre
ellas. → `79-voz-generada-y-doblaje.md`.

```bash
# Cadena para voz en off de explainer
ffmpeg -i vo_bruta.wav -af "highpass=f=85,afftdn=nr=10:nf=-30,\
equalizer=f=240:t=q:w=1.4:g=-2,equalizer=f=3500:t=q:w=1.2:g=3,\
acompressor=threshold=-19dB:ratio=3.5:attack=6:release=170:makeup=3,\
loudnorm=I=-15:TP=-1.5:LRA=6" vo_final.wav
```

`LRA=6` — muy pareja, a propósito. En explainer la voz no debe tener drama dinámico.

---

## 7. Sonido: lo que hace que la animación se sienta física

Un explainer sin efectos de sonido se siente muerto aunque la animación sea buena. Y con 6 sonidos ya está
resuelto:

| Momento | Sonido | Nivel |
|---|---|---|
| Elemento que entra | *pop* corto o *tick* | -22 dB |
| Elemento que se va | *whoosh* suave | -24 dB |
| Cifra que aparece | *ding* o *click* metálico | -20 dB |
| Cambio de acto | *whoosh* más largo | -18 dB |
| El dato importante | *impacto* grave | -16 dB |
| Cierre / logo | *swell* que resuelve | -18 dB |

**Uno por elemento, no dos.** Y todos a volumen bajo: los efectos acompañan, no protagonizan. →
`76-diseño-sonoro.md`.

### Música

Instrumental, sin percusión fuerte, a **-26 LUFS bajo la voz**, con ducking. La música de explainer debe
ser tan neutra que nadie la note. Si te acordás de la canción, está muy arriba.

---

## 8. Texto en pantalla

En explainer el texto **repite lo esencial de la voz**, no todo.

- **Cifras siempre en pantalla.** El oído no retiene números.
- **Los 3 pasos numerados**, visibles.
- **Nombres propios y términos nuevos**, escritos la primera vez.
- Tipografía: la de la marca. Un peso para títulos, uno para cuerpo. Nada más. → `44`.

Y subtítulos completos aparte, porque el explainer se ve en feed sin sonido.

---

## 9. Producción con herramientas reales

Sin After Effects, el flujo que funciona:

```
1. Diseñar cada "pantalla" (escena) como imagen o como HTML
2. Exportar los estados: pantalla_01_a.png, pantalla_01_b.png (con y sin el elemento)
3. Animar transiciones y movimientos con ffmpeg o con el editor
4. Montar sobre la voz
```

Para elementos con transparencia que se mueven, exporta **WebM con canal alfa** desde el navegador o desde
la herramienta que uses:

```bash
# Superponer un WebM con alfa sobre el fondo
ffmpeg -i fondo.mp4 -c:v libvpx-vp9 -i elemento_alfa.webm -filter_complex \
 "[0:v][1:v]overlay=x=200:y=300:enable='between(t,3,8)'[v]" \
 -map "[v]" -c:v libx264 -crf 18 compuesto.mp4
```

Ver `105-ffmpeg-superponer-capas.md` y `80-capas-y-composicion.md`.

### Alternativa honesta: CapCut o el editor del usuario

Si el explainer lo va a mantener alguien no técnico, entregar un proyecto de CapCut con las capas armadas
vale más que un mp4 perfecto que nadie puede modificar. → bloque 11 (110–119).

---

## 10. Verificación específica del formato

1. **Míralo sin sonido.** ¿Se entiende la idea principal? Debería, al menos a grandes rasgos.
2. **Óyelo sin imagen.** ¿La voz sola explica? Debería también. Los dos canales tienen que sostenerse.
3. **Pausa en cualquier fotograma.** ¿La pantalla está bien compuesta como imagen fija? En explainer cada
   fotograma es una lámina.
4. **Cuéntale la idea a alguien** que no sabe del tema, y después muéstrale el video. Si el video no le
   añade nada a tu explicación oral, el video sobra.

---

## Errores comunes

1. **Animar antes de tener la voz grabada.** Se rehace todo. Es el error más caro del formato.
2. **Frases que no se pueden dibujar.** Guion de marketing en vez de guion de explainer.
3. **Más de 3 pasos.** El espectador se pierde en el 4.
4. **Estilo inconsistente entre gráficos.** Distintos grosores de línea, distintos radios, dos familias de
   iconos. Es lo que hace que se vea amateur, más que la animación misma.
5. **Corporate memphis / gente 3D azul flotando.** Plantilla reconocible a un fotograma de distancia.
6. **Todos los elementos entrando a la vez.** Sin stagger, la animación se siente barata.
7. **Elementos que se van antes de poder leerse.** Un dato 0,6 s en pantalla no existió.
8. **Animación sin sonido.** Se siente muerta aunque esté bien hecha. Seis efectos lo resuelven.
9. **Efectos de sonido muy arriba.** Compiten con la voz y cansan.
10. **Música con percusión** en un explainer. Distrae de la explicación.
11. **Zoompan sin escalar la imagen antes.** Produce saltos visibles.
12. **Confundir "movimiento" con "animación"** y meterse en un proyecto de nivel 3 cuando el nivel 2
    resolvía.
13. **Voz TTS sin variación de ritmo.** Se delata en 5 segundos.
14. **No poner las cifras en texto.** El dato central del video queda solo en el audio.

---

## Checklist

- [ ] Guion escrito con frases dibujables, 130–150 palabras por minuto
- [ ] Máximo 3 pasos en el bloque de solución
- [ ] Voz en off grabada y aprobada ANTES de animar
- [ ] Mapa de frases generado (`silencedetect`) y usado como storyboard temporal
- [ ] Nivel de animación decidido conscientemente (casi siempre nivel 2)
- [ ] Sistema gráfico consistente: misma paleta, mismo grosor, mismo radio, una familia de iconos
- [ ] Nada de corporate memphis ni 3D genérico
- [ ] Elementos entran en cascada con 0,15–0,25 s de diferencia
- [ ] Todo elemento permanece el tiempo mínimo de lectura
- [ ] Cifras, pasos numerados y términos nuevos escritos en pantalla
- [ ] Subtítulos completos disponibles
- [ ] Seis efectos de sonido básicos colocados, todos a bajo volumen
- [ ] Música instrumental neutra a -26 LUFS con ducking
- [ ] Voz a -15 LUFS con LRA bajo
- [ ] Prueba sin sonido y prueba sin imagen: las dos superadas
- [ ] Cualquier fotograma pausado está bien compuesto
- [ ] Pasó `98-verificacion-del-corte.md`

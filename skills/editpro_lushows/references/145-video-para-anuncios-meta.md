# 145 — Video para anuncios de Meta: el creativo es la campaña

> Verificado a **agosto de 2026**. Meta cambia nombres de métricas y funciones de Advantage+ con
> frecuencia. Las horquillas de benchmark vienen de agencias y de datos agregados de terceros, **no de
> Meta**. Úsalas como semáforo. Tu cuenta es tu mejor referencia.

## La verdad incómoda de 2026

En 2026, con Advantage+ y la segmentación amplia, **el creativo hace casi todo el trabajo**. La
segmentación fina que se hacía hace años ya no mueve la aguja: el sistema encuentra a la gente. Lo que tú
controlas es **qué le muestras**.

Traducción práctica: **si tu anuncio no rinde, el problema es el video en el 80 % de los casos.**
No es el público, no es el presupuesto, no es la hora del día.

Y dentro del video, la mayoría del problema está en **los primeros 3 segundos**.

---

## Las cuatro métricas que tienes que armar tú

Meta no te da estas cifras hechas. Las calculas con las columnas que sí te da.

| Métrica | Fórmula | Qué mide | Referencia 2026 |
|---|---|---|---|
| **Hook rate** | reproducciones de 3 s ÷ impresiones | ¿El primer segundo detuvo el dedo? | <15 % mal · 25 % normal · >40 % excelente |
| **Hold rate** | ThruPlays ÷ reproducciones de 3 s | ¿El que se quedó, siguió? | 20–25 % objetivo |
| **ThruPlay rate** | ThruPlays ÷ impresiones | Completado real | 18–25 % en Reels/Stories |
| **CTR (salida)** | clics en el enlace ÷ impresiones | ¿Provocó la acción? | depende del objetivo |

**ThruPlay** = ver 15 segundos, o el video completo si dura menos de 15. Ojo con esto: **si tu video dura
12 segundos, un ThruPlay es una vista completa.** Si dura 40, un ThruPlay es solo el 37 % del video. No
compares ThruPlay rate entre videos de duración distinta.

### Cómo diagnosticar con esas cuatro

| Hook | Hold | CTR | Qué está pasando | Qué haces |
|---|---|---|---|---|
| Bajo | — | — | El primer segundo no detiene | Rehaz **solo** los 3 primeros segundos |
| Alto | Bajo | — | Gancho llamativo, contenido flojo | El gancho promete lo que el video no da |
| Alto | Alto | Bajo | Buen video, mala oferta o mal CTA | Cambia la oferta y el llamado a la acción |
| Alto | Alto | Alto, pero no venden | El problema está **después del clic** | Es tu WhatsApp, no el video (ver `146`) |

Este cuadro es el que evita gastar plata rehaciendo lo que estaba bien.

---

## Los primeros 3 segundos

Meta filtra a los 3 segundos. Lo que pase ahí decide si tu anuncio se reparte barato o caro.

### Qué funciona (probado, no teoría)

1. **El problema primero, no el producto.** "¿Otra vez sin plan un jueves?" antes que "Bendita Pola te
   invita".
2. **Movimiento en el primer fotograma.** Un plano fijo pierde contra uno que ya está en movimiento cuando
   aparece. Empieza el video con la acción ya empezada.
3. **Una cara mirando a cámara y hablando.** Sigue siendo de lo más fiable.
4. **Texto grande en el fotograma 1.** No a los 2 segundos. En el primero.
5. **Ruptura de patrón**: algo que no encaja en un feed. Un primerísimo plano, un color raro, un sonido.
6. **El precio.** "$12.000 la michelada" es un gancho legítimo y en Colombia funciona muy bien.

### Qué mata el gancho

- Logo animado. Cualquier logo animado. Siempre.
- Plano general estático del local.
- "Hola, ¿cómo están?"
- Fade in desde negro. Regalas medio segundo.
- Barras negras (16:9 dentro de un lienzo vertical).
- Que el primer fotograma sea oscuro. En el feed se ve como un hueco.

### La prueba de los 3 segundos

Corta tu anuncio a 3 segundos, míralo sin sonido y pregúntate: **¿entiendo de qué se trata y quiero ver
más?** Si no, no hay anuncio.

```bash
ffmpeg -i anuncio.mp4 -t 3 -c copy -y prueba_gancho.mp4
```

Y para verlo como lo verá el 85 % de la gente (sin sonido):

```bash
ffmpeg -i anuncio.mp4 -t 3 -an -c:v copy -y prueba_gancho_mudo.mp4
```

---

## Formatos por ubicación

Meta te va a poner el anuncio en varios sitios. Si subes un solo archivo, Meta lo recorta solo — y recorta
mal. Con **Advantage+ creative** activado, Meta genera recortes y variantes automáticamente; conviene
dejarlo, pero **revisando qué está generando**.

| Ubicación | Formato | Duración que rinde | Cuidado |
|---|---|---|---|
| **Reels (IG/FB)** | 9:16 — 1080x1920 | 5–15 s | Es donde va la mayoría de tus impresiones |
| **Stories** | 9:16 — 1080x1920 | 5–10 s | Interfaz encima; deja 250 arriba / 400 abajo |
| **Feed** | 4:5 — 1080x1350 | 6–15 s | 4:5 ocupa más pantalla que 1:1. Usa 4:5 |
| **Feed cuadrado** | 1:1 — 1080x1080 | 6–15 s | Solo si necesitas un solo archivo universal |

**La decisión práctica para ti:** haz el **9:16** como pieza principal y una versión **4:5** para feed.
Con esas dos cubres casi todo. Componer para que el mismo material sirva en las dos está en `147`.

### Especificaciones técnicas

| Qué | Valor |
|---|---|
| Códec | H.264 |
| Contenedor | MP4 o MOV (usa MP4) |
| Audio | AAC, 128 kbps mínimo, 48 kHz, estéreo |
| Resolución mínima | 1080p |
| Fotogramas por segundo | 30, constante |
| Bitrate | 8 Mbps o más para 1080p |
| Peso máximo | 4 GB |
| Duración máxima | 240 minutos (irrelevante) |

```bash
# Exportar 9:16 y 4:5 desde el mismo corte
ffmpeg -i corte.mov -c:v libx264 -b:v 10M -maxrate 12M -bufsize 20M \
  -pix_fmt yuv420p -r 30 -c:a aac -b:a 128k -ar 48000 \
  -movflags +faststart -y anuncio_9x16.mp4

ffmpeg -i corte.mov -vf "crop=ih*4/5:ih,scale=1080:1350" \
  -c:v libx264 -b:v 10M -maxrate 12M -bufsize 20M \
  -pix_fmt yuv420p -r 30 -c:a aac -b:a 128k -ar 48000 \
  -movflags +faststart -y anuncio_4x5.mp4
```

> El recorte automático de `crop` toma el centro. **Verifica que tu texto y tu sujeto sobrevivan.**
> Si no, reencuadra a mano (ver `147`).

---

## El texto quemado y la regla del 20 %

La vieja regla de "máximo 20 % de texto en la imagen" **ya no bloquea anuncios** — Meta la retiró como
regla dura hace años. Pero el efecto sigue: **anuncios con demasiado texto encima rinden peor**. No es
castigo, es que la gente los lee como carteles.

Lo práctico:

- Texto quemado en pantalla: **sí, siempre**, es tu canal principal sin sonido.
- Pero **poco a la vez**: 3–6 palabras por golpe (ver `42`).
- **No metas un párrafo.** No es una valla publicitaria.
- **No pongas texto donde Meta pone su interfaz.** En anuncios, Meta añade el botón de CTA abajo. Deja
  **400+ px libres abajo**, no 320.

---

## Cuántas variantes hacer y en qué se diferencian

Con Advantage+ y segmentación amplia, **el volumen de creativos es la palanca**. Las recomendaciones de
industria hablan de 10–20 variantes para campañas grandes. Para un bar con presupuesto de barrio eso es
irreal. Lo realista y suficiente:

### El paquete mínimo honesto: 4 variantes

Cambia **una sola cosa** por variante. Si cambias tres, no aprendes nada.

| Variante | Qué cambia | Todo lo demás |
|---|---|---|
| A | Gancho: problema ("¿jueves sin plan?") | idéntico |
| B | Gancho: precio ("michelada a $12.000") | idéntico |
| C | Gancho: cara hablando ("te voy a decir dónde") | idéntico |
| D | Gancho: producto en primerísimo plano (la cerveza sirviéndose) | idéntico |

Los cuatro comparten el mismo cuerpo y el mismo remate. **Solo cambian los primeros 3 segundos.** Es
barato de producir (un corte distinto del mismo material) y es exactamente donde está el 80 % de la
diferencia.

### La segunda ronda

Cuando sepas cuál gancho gana, mantén ese gancho y ahora cambia:

- **La oferta** ("2x1 hasta las 8" vs "entrada gratis")
- **La duración** (10 s vs 20 s)
- **El remate** (CTA hablado vs CTA solo escrito)
- **El formato** (9:16 vs 4:5)

Un cambio por ronda. Siempre.

### Cuánto dejar correr antes de decidir

No mires a las 6 horas. Referencia práctica: **espera a que cada variante tenga al menos 1.000
impresiones**, o 3 días, lo que llegue primero. Antes de eso el sistema todavía está aprendiendo y los
números mienten.

Y no apagues una variante porque "se ve fea". Apágala porque su hook rate es la mitad de la ganadora.

---

## Qué mide el sistema de Meta (y por qué importa para editar)

Meta optimiza hacia el evento que le pediste. Pero para **repartir barato** usa señales de calidad del
anuncio. Lo que sabemos que pesa:

| Señal | Efecto en tu edición |
|---|---|
| **Tasa de reproducción de 3 s** | El gancho decide tu costo por impresión |
| **Interacción positiva** (clic, comentario, guardar) | Un CTA claro y temprano ayuda |
| **Interacción negativa** ("ocultar anuncio", "es irrelevante") | Ganchos que engañan te suben el costo |
| **Frecuencia** | Cuando la gente ve el mismo anuncio 5 veces, el rendimiento cae. Por eso rotas creativos |

**La frecuencia es la razón real por la que necesitas variantes**, más que el "testeo". Un solo creativo
se quema en 1–2 semanas con público local pequeño (Tocancipá y alrededores no es un público infinito).
Ten siempre 3–4 creativos vivos y mete uno nuevo cada semana.

---

## Sonido y música en anuncios

- **85 % ve sin sonido.** Diseña para mudo, mejora con sonido.
- **La música con derechos hace que te rechacen el anuncio o te quiten el audio.** No uses música de la
  biblioteca de Instagram/TikTok en pauta. Usa librería con licencia o la biblioteca de sonidos de Meta.
- Si hay voz, **subtitúlala quemada**. Los subtítulos automáticos de Meta existen pero no controlas cómo se
  ven ni si aparecen.
- Nivelación: pico -1 dBTP, promedio cerca de -14 LUFS.

---

## Errores comunes

- **Culpar al público cuando el problema es el creativo.** En 2026 casi siempre es el creativo.
- **Empezar el anuncio con el logo.** Es el error más caro y el más común.
- **Fade in desde negro.** Medio segundo de tu gancho regalado.
- **Subir un solo archivo 16:9 y dejar que Meta lo recorte.** Sale con barras o con la cabeza cortada.
- **Cambiar tres cosas entre variantes.** No aprendes nada y no sabes qué funcionó.
- **Decidir a las 6 horas.** Ruido puro. Espera 1.000 impresiones por variante.
- **Comparar ThruPlay rate entre un video de 10 s y uno de 40 s.** No es la misma métrica.
- **Rehacer el video entero cuando el hold rate estaba bien y el hook mal.** Solo tocaba el principio.
- **Dejar el mismo creativo 4 semanas.** Se quema. Con público local se quema más rápido.
- **Música comercial.** Anuncio rechazado o mudo.
- **Texto pegado abajo.** El botón de CTA de Meta se lo come. 400 px libres.
- **No mirar el hook rate porque Meta no lo trae hecho.** Es una división. Hazla.
- **Optimizar el video cuando el problema es la conversación de WhatsApp.** Si el CTR es alto y no vendes,
  el video está bien. Ver `146`.

---

## Checklist

- [ ] El **primer fotograma tiene movimiento**, no es negro y no es el logo.
- [ ] Corté los 3 primeros segundos a un archivo aparte y **lo vi sin sonido**: se entiende.
- [ ] Hay **texto grande desde el fotograma 1**.
- [ ] Exporté **9:16 (1080x1920)** y **4:5 (1080x1350)**; verifiqué el recorte a mano.
- [ ] Dejé **400+ px libres abajo** (botón de CTA de Meta) y 250 arriba.
- [ ] H.264, MP4, 1080p, **30 fps constantes**, AAC 48 kHz, 8+ Mbps, `+faststart`.
- [ ] La música **no tiene derechos** — es de librería con licencia.
- [ ] Los subtítulos están **quemados**, no dependo de los automáticos.
- [ ] Tengo **4 variantes que solo cambian los primeros 3 segundos**.
- [ ] Voy a esperar **1.000 impresiones por variante** antes de decidir.
- [ ] Sé cómo calcular **hook rate** (3 s ÷ impresiones) y **hold rate** (ThruPlay ÷ 3 s).
- [ ] Tengo un creativo nuevo listo para meter **cada semana** (por frecuencia, no por gusto).
- [ ] Si el CTR es alto y no hay ventas, voy a revisar **el WhatsApp**, no el video.

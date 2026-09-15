# 141 — Instagram Reels: especificaciones y qué premia de verdad

> Verificado a **agosto de 2026** con documentación de Meta y fuentes de industria. Instagram cambia
> límites de duración y nombres de métricas sin avisar. Si algo no te cuadra, la app manda; esto es guía.

## Especificaciones que sí necesitas

| Qué | Valor |
|---|---|
| Lienzo | **1080 x 1920** px (9:16) |
| Ancho mínimo aceptado | 720 px (no lo uses; sube 1080) |
| Duración | 3 s a **3 minutos** |
| Duración que funciona | **7 a 25 segundos** para negocio local |
| Fotogramas por segundo | 30 mínimo; **30 o 60**, constante, nunca variable |
| Códec de video | H.264 (alto perfil) |
| Códec de audio | AAC, 128 kbps, 48 kHz, estéreo |
| Contenedor | MP4 (usa MP4, no MOV) |
| Peso máximo | 4 GB (irrelevante: tus reels pesan 5–20 MB) |
| Bitrate útil | 8–12 Mbps para 1080x1920 |

Export con ffmpeg que Instagram no vuelve a maltratar demasiado:

```bash
ffmpeg -i corte_final.mov \
  -c:v libx264 -profile:v high -level 4.2 -pix_fmt yuv420p \
  -b:v 10M -maxrate 12M -bufsize 20M -r 30 \
  -c:a aac -b:a 128k -ar 48000 -ac 2 \
  -movflags +faststart -y reel_final.mp4
```

`-movflags +faststart` mueve el índice al principio del archivo. Sin eso, la subida y la primera
reproducción son más lentas. Es gratis, ponlo siempre.

**Instagram va a recomprimir tu video de todos modos.** No puedes evitarlo. Lo que sí puedes es no darle
un archivo ya maltratado: si le subes algo comprimido dos veces, la recompresión de Instagram lo remata y
se te ve el bloqueo en las zonas oscuras — que en un bar de noche es justo donde vive tu imagen.

---

## Zona segura (resumen; el detalle está en `45`)

Sobre 1080x1920, deja libre:

- **250 px arriba**
- **400–440 px abajo** (el caption crece hacia arriba: si escribes captions largos, 440)
- **60–90 px a los lados**; **más de 90 px a la derecha** si vas a publicar lo mismo en TikTok

El rectángulo seguro para publicar en las tres redes con el mismo archivo es aproximadamente
**880 x 1230 px centrado**.

Dos trampas específicas de Instagram:

1. **El grid del perfil recorta a 1:1 centrado.** Todo tu texto del tercio inferior desaparece ahí. Si te
   importa cómo se ve tu perfil, mete el gancho también en la franja central.
2. **El feed muestra el reel recortado a 4:5.** Pierdes arriba y abajo respecto al 9:16.

---

## La portada

La portada del reel es lo que se ve en tu grid y en la vista previa. Instagram te deja elegir un
fotograma del video o subir una imagen aparte.

- Sube una **imagen aparte de 1080x1920**, no elijas un fotograma. Un fotograma congelado casi siempre
  agarra a alguien con los ojos medio cerrados.
- **Diseña la portada pensando en el recorte 1:1 del grid.** La franja central es lo único garantizado.
- Que se lea a tamaño uña: 3 o 4 palabras máximo, tipografía gorda.
- La portada **no afecta el reparto en el feed de Reels** (ahí la gente ve el video, no la portada).
  Sirve para tu perfil y para quien llega desde afuera. No inviertas horas en ella.

---

## Audio

- **La mayoría ve sin sonido.** El texto en pantalla es tu canal principal (ver `40`).
- Aun así, **pon audio siempre**. Un reel mudo se siente roto y algunos formatos de audio ausente causan
  problemas de reproducción.
- Usar audio de la biblioteca de Instagram (audio "en tendencia") tiene un efecto real pero pequeño y muy
  sobrevalorado. **Un audio en tendencia no salva un video malo.**
- **Cuidado legal y práctico con la música comercial en cuentas de empresa.** Las cuentas de empresa
  tienen catálogo restringido; una pista que un creador personal sí puede usar, a tu cuenta de bar le
  puede salir silenciada o bloqueada en algunos países. Si el video es para pauta, la música debe ser de
  librería con licencia o de la biblioteca de sonidos de Meta para empresas — **la música con derechos
  hace que el anuncio se rechace o se le quite el audio**.
- Nivel: pico en **-1 dBTP**, promedio alrededor de **-14 LUFS**. Ver `80`.

```bash
# Comprobar el nivel antes de subir
ffmpeg -i reel_final.mp4 -af loudnorm=I=-14:TP=-1:LRA=11:print_format=summary -f null -
```

---

## Qué premia Instagram en 2026

Instagram ha sido inusualmente público con esto. Lo confirmado por Adam Mosseri:

| Señal | Peso | Cómo se ve en tu edición |
|---|---|---|
| **Tiempo de visualización / % completado** | La más alta | Video corto y denso, sin relleno |
| **Envíos por DM (sends per reach)** | Muy alta — la que abre público nuevo | Contenido que da ganas de etiquetar a alguien |
| **Me gusta por alcance** | Media | — |
| **Que lo vuelvan a ver** | Alta | Bucle limpio, información densa |
| **Comentarios** | Media | Preguntas reales, no "🔥" |

En 2026 Instagram agregó a las estadísticas de cada reel un **gráfico de retención** y una **tasa de
salto (skip rate)**. Eso confirma en qué pone el ojo: en dónde te abandonan.

### Qué castiga

- **Marca de agua de TikTok.** Instagram lo ha dicho explícitamente: contenido reciclado con marca de agua
  visible se reparte menos. Si vas a publicar el mismo video en las dos, exporta el original limpio en tu
  editor y súbelo dos veces. No descargues de TikTok.
- **Video de baja resolución o borroso.**
- **Contenido que la gente reporta como "no me interesa".**
- **Barras negras.** Un 16:9 metido en un lienzo vertical con bandas es la forma más rápida de decir "esto
  no está hecho para aquí".
- **Ganchos que engañan** (prometes algo que no entregas). Genera salidas rápidas, y la tasa de salto es
  ahora una métrica visible.

---

## Duración: la decisión más rentable

Para Bendita Pola, esto:

| Tipo de video | Duración |
|---|---|
| Un plato, un trago, un antojo | **6–10 s** |
| Promoción del jueves / evento | **10–18 s** |
| Ambiente del bar un viernes | **12–20 s** |
| Historia (cómo nació, quién cocina) | **25–45 s** |
| Cualquier cosa "porque tengo mucho material" | **no** |

La razón es aritmética, no estética: el porcentaje visto baja casi automáticamente con la duración
(ver `140`). Un video de 45 s tiene que ser mucho mejor que uno de 12 s para conseguir el mismo reparto.

---

## Ritmo dentro del reel

El estándar 2026 y lo que se ve en lo que funciona:

- **Cambio visual cada 1,5–2 s.** 5 a 7 cambios cada 10 segundos.
- "Cambio visual" no siempre es corte: sirve un punch-in, un movimiento de cámara, un texto nuevo que
  entra, un cambio de plano de la comida.
- **Los 3 primeros segundos merecen su propio tratamiento**: ver `30`.
- **Nunca dejes un plano estático más de 2,5 s** en los primeros 10 segundos.

Un talking head estático con texto dinámico retiene notablemente más que uno sin texto. Si solo vas a
hacer una cosa por tus reels, que sea **poner texto grande y con ritmo** (ver `46`).

---

## El caption y los hashtags

- El caption **come 400 px de tu video**. Escríbelo corto o acepta perder esa franja.
- La primera línea del caption es el único texto que se ve sin tocar "más". Que sea el gancho escrito, no
  "🔥 Nuevo video 🔥".
- **Hashtags: 3 a 5, específicos.** El efecto de los hashtags en el reparto es hoy pequeño; sirven más
  como contexto que como distribución. 30 hashtags genéricos es una señal de cuenta de spam.
  Para ti: `#tocancipá #zipaquirá #sabana` valen más que `#food #viral #fyp`.
- **La ubicación (localización) sí importa** para negocio local. Márcala siempre.

---

## Publicar el mismo video en Instagram y TikTok

Sí, hazlo. Pero:

1. **Exporta dos veces desde tu editor.** No descargues de una plataforma para subir a la otra.
2. Usa la zona segura de intersección (880x1230).
3. Cambia el caption y los hashtags. Es cultura distinta (ver `142`).
4. Si tu video usa un audio de la biblioteca de una plataforma, en la otra ese audio no existe. Lleva la
   música pegada en el archivo o vuelve a montar con una pista disponible allá.

---

## Errores comunes

- **Subir el video con la marca de agua de TikTok.** Instagram lo penaliza y además se ve barato.
- **Elegir un fotograma del video como portada.** Sale alguien parpadeando. Sube una imagen hecha.
- **Poner el texto importante en el tercio inferior.** Ahí vive el caption. Se lo come.
- **Olvidar que el grid recorta a 1:1.** Tu portada perfecta en vertical queda decapitada en el perfil.
- **Videos de 45 segundos para anunciar una promoción de 6 palabras.**
- **Música comercial en cuenta de empresa.** Silenciado, bloqueado o anuncio rechazado.
- **Barras negras** de un video horizontal metido a la fuerza.
- **Confiar en el audio en tendencia como estrategia.** Es un condimento, no la comida.
- **30 hashtags genéricos.** Ruido. Para negocio local, la ubicación y 3–5 hashtags de zona valen más.
- **Recomprimir dos veces.** Exporta una sola vez desde el corte final, con bitrate alto.
- **No poner ubicación.** Eres un bar en Tocancipá; es la señal geográfica más barata que existe.
- **Publicar sin `-movflags +faststart`.** No te rompe nada pero te hace la vida más lenta gratis.

---

## Checklist

- [ ] El archivo es **1080x1920, MP4, H.264, 30 fps constantes, AAC 48 kHz**.
- [ ] Exporté con `-movflags +faststart` y bitrate de 8–12 Mbps.
- [ ] Es **el primer export desde el corte**, no una descarga de otra plataforma.
- [ ] **Cero marcas de agua** de TikTok o de cualquier app.
- [ ] Todo el texto está dentro de **250 px arriba / 440 px abajo / 90 px a los lados**.
- [ ] El gancho también se lee **recortado a 1:1** (por el grid del perfil).
- [ ] Subí una **portada 1080x1920 hecha aparte**, no un fotograma.
- [ ] La duración está entre **7 y 25 s**, salvo que tenga una razón concreta para más.
- [ ] Hay **cambio visual cada 1,5–2 s** y ningún plano estático de más de 2,5 s al principio.
- [ ] Hay **texto grande en pantalla**: el video se entiende sin sonido.
- [ ] El audio está a **-14 LUFS / -1 dBTP** y **no** es música comercial con derechos.
- [ ] La primera línea del caption **es el gancho**, no "nuevo video".
- [ ] Puse **ubicación** y 3–5 hashtags de zona.
- [ ] Revisé la vista previa en el celular antes de darle publicar.

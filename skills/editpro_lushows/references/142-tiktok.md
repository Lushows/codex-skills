# 142 — TikTok: especificaciones, cultura del formato y qué funciona en LatAm

> Verificado a **agosto de 2026**. TikTok cambia límites y funciones por país y por versión de la app;
> algunas cosas que existen en Estados Unidos aún no llegan a Colombia y viceversa. Cuando este módulo y
> tu app no coincidan, gana tu app.

## Especificaciones

| Qué | Valor |
|---|---|
| Lienzo | **1080 x 1920** px (9:16) |
| Resolución máxima real | **1080p**. Si subes 4K, TikTok lo baja igual |
| Otros formatos aceptados | 1:1 y 16:9 — pero se reparten peor en el "Para ti" |
| Duración grabando en la app | hasta 10 minutos |
| Duración subiendo archivo | hasta 60 minutos (en algunas cuentas) |
| Duración que funciona | **7 a 21 segundos** para negocio local |
| Peso máximo | ~287 MB desde celular; hasta 4 GB desde computador |
| Códec | H.264, MP4 (el más compatible y el que menos daño sufre) |
| Audio | AAC, 48 kHz |
| Fotogramas por segundo | 30 (60 también sirve; constante siempre) |

Export:

```bash
ffmpeg -i corte_final.mov \
  -c:v libx264 -profile:v high -pix_fmt yuv420p \
  -b:v 10M -maxrate 12M -bufsize 20M -r 30 \
  -c:a aac -b:a 128k -ar 48000 \
  -movflags +faststart -y tiktok_final.mp4
```

**Sube desde el computador cuando puedas.** La app del celular comprime antes de subir; el navegador en
computador entrega el archivo más limpio. Con planos de bar de noche, esa diferencia se nota.

---

## Zona segura: TikTok es la que más interfaz pinta encima

Sobre 1080x1920, deja libre:

| Borde | Orgánico | En anuncios |
|---|---|---|
| Arriba | ~130–150 px | igual |
| Abajo | ~330–480 px (el caption crece) | **~400–480 px** (botón de CTA) |
| Derecha | **~140–165 px** | igual |
| Izquierda | ~45–60 px | igual |

La franja derecha de TikTok es la más ancha de las tres plataformas: ahí van avatar, corazón, comentarios,
guardados, compartir y el disco de audio girando. **Cualquier gráfico alineado a la derecha se lo comen.**

Y ojo: TikTok ha estado empujando más elementos hacia abajo (recomendaciones, botones de búsqueda dentro
del video). Sé conservador: mantén todo lo importante en el rectángulo central. Detalle en `45`.

---

## La cultura del formato: por qué un reel bonito fracasa en TikTok

Esta es la parte que la gente se salta y por la que después dice "es que TikTok no funciona para mi negocio".

**Instagram tolera lo pulido. TikTok lo castiga.** En TikTok, un video que se ve como publicidad se lee
como publicidad en menos de un segundo y se desliza. Lo que funciona:

| Funciona | No funciona |
|---|---|
| Cámara en mano, movimiento real | Trípode, plano fijo, iluminación de estudio |
| Voz de una persona hablándole a la cámara | Voz en off locutada, tono comercial |
| Texto tipo "me pasó esto" | Texto tipo "Presentamos nuestra nueva…" |
| Errores, risas, ruido del local | Todo perfecto y silencioso |
| Empezar a mitad de frase | Presentación con logo animado |
| Grabado en el bar, con gente | Renders, mockups, plantillas |
| Precio dicho en voz alta | "Consulta nuestros precios" |

Esto no es "bajar la calidad". Es **cambiar el registro**. El video sigue estando bien enfocado, bien
expuesto, con buen audio y bien cortado. Lo que cambia es que no se disfraza de comercial de televisión.

### El logo animado al principio te mata

Si tu video empieza con la chapa de Bendita Pola girando 1,5 segundos, acabas de gastar el 100 % de tu
gancho en decir "esto es un anuncio". El logo va al final, si acaso. En TikTok, el primer fotograma tiene
que ser **la cosa**: la cerveza sirviéndose, la cara diciendo algo, el plato saliendo.

---

## Qué funciona en LatAm y en Colombia específicamente

Sé honesto sobre lo que puedo verificar: no existe un reporte público confiable con métricas por país para
bares en Colombia. Lo que sigue viene de observar contenido que circula y de patrones repetidos, no de un
estudio. Tómalo como hipótesis para probar, no como dato.

**Lo que se repite en contenido gastronómico colombiano que rinde:**

1. **Precio en pantalla, desde el segundo 1.** "Michelada $12.000" hace más que cualquier adjetivo. El
   público de acá busca precio antes que estética.
2. **El nombre del municipio, escrito.** "TOCANCIPÁ" grande. La gente filtra por cercanía. Un video
   perfecto sin ubicación es un video para nadie.
3. **Voz colombiana, sin acento neutro.** El acento neutro de doblaje suena a comercial. Habla como hablas.
4. **El chisme / la primicia.** "Abrieron esto y nadie sabe", "el sitio que todos preguntan dónde queda".
5. **Plan concreto y fechado.** "Jueves de trivia, 7 pm" rinde más que "ven a disfrutar".
6. **Reacción de gente real** comiendo o tomando. La cara de alguien mordiendo funciona mejor que el plano
   del plato solo.
7. **Sonido del local.** Fritura, hielo, gente riéndose. TikTok premia el sonido propio más que Instagram.

**Lo que se repite en lo que no rinde:**

- Recorridos del local sin nada pasando ("aquí está la barra, aquí las mesas").
- Contenido de "trend" sin relación con el negocio: sube likes, no llena mesas.
- Textos motivacionales sobre el emprendimiento.
- Fotos fijas con música y transiciones (eso es un carrusel disfrazado de video).

---

## Duración y ritmo

TikTok reparte por porcentaje visto igual que las demás. Referencias 2026 de retención:

| Duración | Promedio | Bueno |
|---|---|---|
| menos de 15 s | 60–70 % | +75 % |
| 15–30 s | 50–60 % | +65 % |
| 30–60 s | 40–55 % | +60 % |

Ritmo: **cambio visual cada 1,5–2 s**, igual que en las otras. La diferencia es que en TikTok los cortes
pueden ser más bruscos y no pasa nada — la audiencia está entrenada. Un corte seco es más nativo que una
transición con efecto.

**Las transiciones con efecto (giros, zooms 3D, "velocity edit") ya se leen como 2022.** Ver `148`.

---

## Audio: aquí sí es distinto

En TikTok el audio pesa más que en Instagram, por dos razones:

1. Más gente ve con sonido (no la mayoría, pero más que en IG).
2. El audio es un **eje de descubrimiento**: la gente entra a ver "otros videos con este sonido".

Prácticamente:

- **Tu sonido original bien grabado es un activo.** El chisporroteo de la parrilla, el hielo cayendo.
- Si usas audio de la biblioteca, úsalo **bajo tu voz**, no en lugar de ella.
- **Cuenta de empresa = catálogo restringido.** Igual que en Instagram, si tu cuenta está marcada como
  negocio, buena parte de la música comercial no te aparece. Si te importa el catálogo completo, esa es una
  decisión que tomas al elegir el tipo de cuenta — y perder funciones de negocio a cambio de música
  rara vez vale la pena.
- Subtitula siempre. Los subtítulos automáticos de TikTok existen y son decentes en español, pero son
  feos y quedan donde TikTok quiera. Quema los tuyos (ver `41`, `43`).

---

## Publicar en TikTok lo que ya hiciste para Instagram

Se puede, con tres ajustes:

1. **Exporta limpio desde tu editor.** Nunca descargues de Instagram (queda con marca de agua).
2. **Reajusta la derecha**: TikTok come ~165 px, Instagram ~90. Si tenías algo pegado a la derecha, muévelo.
3. **Cambia el primer segundo.** El gancho que funciona en IG suele ser demasiado presentado para TikTok.
   Empieza más adentro, más crudo.

Y al revés: lo que hiciste para TikTok casi siempre funciona tal cual en Reels. **La dirección
TikTok → Instagram es más fácil que Instagram → TikTok.** Si tienes que elegir un solo registro para
grabar, graba en registro TikTok.

---

## Errores comunes

- **Empezar con el logo animado.** Gastas el gancho en decir "soy publicidad".
- **Registro de comercial de TV.** Iluminación de estudio, voz locutada, plano fijo. Muere.
- **Alinear texto o gráficos a la derecha.** 165 px de iconos encima.
- **Subir con marca de agua de Instagram o de una app de edición.** Se ve barato y se reparte peor.
- **Subir desde el celular cuando podías subir desde el computador.** Doble compresión gratis.
- **No poner el precio.** En Colombia el precio es el gancho, no el secreto.
- **No poner el municipio escrito.** Si no dice Tocancipá, no te encuentra quien vive cerca.
- **Hacer el trend de moda sin conexión con el bar.** Likes que no se comen.
- **Recorridos del local sin acción.** Nadie ve un video de mesas vacías.
- **Transiciones con efecto.** Se leen viejas. El corte seco es más nativo hoy.
- **Confiar en los subtítulos automáticos.** Feos y mal ubicados. Quema los tuyos.
- **Asumir que TikTok es "para jóvenes" y no te sirve.** Para un bar-restaurante en la sabana, es el canal
  de descubrimiento más barato que hay.

---

## Checklist

- [ ] Archivo **1080x1920, MP4, H.264, 30 fps constantes, AAC 48 kHz**.
- [ ] Subo **desde el computador**, no desde la app.
- [ ] **Cero marcas de agua** de otras plataformas o apps.
- [ ] Nada importante a menos de **165 px del borde derecho**.
- [ ] Nada importante en los **480 px de abajo** si el video va a llevar CTA o caption largo.
- [ ] El **primer fotograma es la cosa**, no el logo.
- [ ] El **precio** aparece escrito, temprano.
- [ ] **"TOCANCIPÁ"** (o el municipio) aparece escrito y grande.
- [ ] Registro crudo: cámara en mano, voz real, sonido del local.
- [ ] Cambio visual cada **1,5–2 s**; cortes secos, sin transiciones de efecto.
- [ ] **Subtítulos quemados** por mí, no los automáticos.
- [ ] Duración entre **7 y 21 s** salvo razón concreta.
- [ ] La música no es comercial con derechos (o es de la biblioteca disponible para mi cuenta).
- [ ] Si el video va también a Instagram, exporté **dos veces desde el editor**.

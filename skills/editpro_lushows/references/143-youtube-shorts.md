# 143 — YouTube Shorts: en qué se parece y en qué NO a Reels y TikTok

> Verificado a **agosto de 2026**. YouTube documenta sus reglas mejor que las otras dos, pero también las
> cambia. Los números de retención son referencias de industria, no cifras oficiales de YouTube.

## Por qué vale la pena aunque no tengas canal

Shorts es la plataforma que más gente ignora y donde hay menos competencia local. Para un bar en
Tocancipá, YouTube tiene dos ventajas que las otras no tienen:

1. **Los videos siguen apareciendo meses después.** TikTok e Instagram tienen una vida útil de días.
   Un Short bueno te sigue trayendo gente en enero.
2. **YouTube es un buscador.** Alguien escribe "restaurante Tocancipá" en YouTube y tu Short puede salir.
   En TikTok también hay búsqueda, pero en YouTube la intención de búsqueda es más fuerte.

La desventaja: **el porcentaje de gente que hace algo después de ver es menor.** YouTube es descubrimiento
pasivo. No esperes que un Short llene mesas el mismo día como sí puede pasar con un TikTok local.

---

## Especificaciones

| Qué | Valor |
|---|---|
| Lienzo | **1080 x 1920** px (9:16). También acepta cuadrado 1:1 |
| Duración máxima | **3 minutos** |
| Duración que funciona | **20 a 45 segundos** |
| Qué convierte un video en Short | Ser **vertical o cuadrado** y durar **3 minutos o menos** |
| Fotogramas por segundo | 24, 30 o 60. Constante |
| Códec / contenedor | H.264 / MP4 |
| Audio | AAC 48 kHz |
| Bitrate recomendado 1080p | 8–12 Mbps (YouTube acepta mucho más; sube generoso) |

**YouTube es la plataforma que menos daña tu archivo.** Acepta bitrates altos y recomprime con criterio.
Si tienes un solo export de máxima calidad, súbelo aquí sin miedo.

```bash
ffmpeg -i corte_final.mov \
  -c:v libx264 -profile:v high -pix_fmt yuv420p \
  -b:v 16M -maxrate 20M -bufsize 32M -r 30 \
  -c:a aac -b:a 192k -ar 48000 \
  -movflags +faststart -y short_final.mp4
```

---

## Diferencia número uno: el sonido

**En YouTube más gente ve con sonido que en Instagram o TikTok.** No tengo una cifra oficial que citar,
pero es consistente con el hábito: mucha gente llega a YouTube desde el televisor, desde el computador o
con audífonos, no deslizando en silencio en la fila del banco.

Consecuencia práctica: **la voz importa más aquí.** Un Short con audio sucio (eco del local, viento,
volumen bajo) se castiga más en YouTube que en TikTok. Limpia el audio (ver `81`, `82`).

Pero **sigue poniendo texto**. "Más gente" no es "toda la gente".

---

## Diferencia número dos: el bucle

Shorts reproduce en bucle automáticamente y **una repetición vale como visualización adicional**. Es la
plataforma donde el bucle bien hecho tiene más rendimiento directo.

Un bucle bien hecho significa que **el último fotograma y el primero encajan**, de modo que la persona no
nota dónde termina y vuelve a empezar. Cuando funciona, la gente ve el video 2 o 3 veces sin darse cuenta
y tu porcentaje visto pasa del 100 %.

### Cómo se construye

**Bucle visual:** el video termina en el mismo plano, mismo encuadre, misma luz con que empezó.

```
Segundo 0:  vaso vacío en la barra, mano entra
Segundo 18: vaso vacío en la barra, mano entra   ← el mismo encuadre
```

**Bucle de frase:** la última palabra dicha completa la primera.

```
Inicio: "…y por eso nadie sabe que existe."
Final:  "El mejor sitio de Tocancipá está escondido detrás de una puerta de madera…"
```

Al repetirse, la frase final empalma con la inicial y la persona se queda enganchada.

**Bucle de pregunta:** abres con una pregunta y el final la contesta de forma que provoca volver a mirar
el principio ("¿viste lo que había en la mesa del fondo?").

### Verificar el bucle con ffmpeg

Pega el video consigo mismo y míralo:

```bash
# Crear una lista y concatenar el video 3 veces
printf "file 'short_final.mp4'\nfile 'short_final.mp4'\nfile 'short_final.mp4'\n" > lista.txt
ffmpeg -f concat -safe 0 -i lista.txt -c copy -y prueba_bucle.mp4
```

Reproduce `prueba_bucle.mp4`. **Si notas la costura, el bucle no está.** Ese archivo es de control, no se
publica.

Y para ver los dos fotogramas clave lado a lado:

```bash
ffmpeg -i short_final.mp4 -vf "select=eq(n\,0)" -frames:v 1 -y primero.png
ffmpeg -sseof -0.1 -i short_final.mp4 -frames:v 1 -y ultimo.png
```

Ábrelos juntos. Deberían poder pasar por el mismo plano.

---

## Diferencia número tres: la duración óptima es mayor

Reels y TikTok premian lo cortísimo. Shorts tolera y hasta prefiere **30–45 segundos**. Referencias de
industria hablan de que la franja de 30–45 s consigue los mejores porcentajes de finalización en Shorts.
No puedo verificar esa cifra con fuente oficial de YouTube, pero es consistente con que el público de
YouTube llega con más paciencia.

Traducción para ti: **el mismo material se corta distinto para cada red.**

| Plataforma | Tu video del jueves de trivia |
|---|---|
| TikTok | 12 s — solo el momento con más energía |
| Reels | 15 s — el momento + el precio + la hora |
| Shorts | 35 s — hay espacio para una mini historia con inicio y remate |

---

## Zona segura

Shorts es **la más restrictiva abajo** de las tres. Deja libre:

- **Arriba:** ~150–170 px
- **Abajo:** **~420–500 px** (título del Short, canal, botón Suscribirse, descripción)
- **Derecha:** ~140 px
- **Izquierda:** ~60 px

El botón **Suscribirse** es grande y vive abajo. Si firmas tus videos en la esquina inferior derecha, ahí
no existe tu firma. Detalle completo en `45`.

> **Si tu pieza pasa la zona segura de Shorts, pasa las tres plataformas.** Es la buena regla de trabajo.

---

## Título, descripción y miniatura

- **El título del Short sí importa**, más que el caption de Instagram, porque YouTube lo usa para búsqueda
  y recomendación. Escríbelo con palabras que alguien buscaría: "Bar en Tocancipá con música en vivo",
  no "Vibras del viernes ✨".
- **Los hashtags en el título** (`#shorts`) ya no son necesarios. YouTube detecta el formato solo. No hace
  daño, tampoco ayuda.
- **La miniatura de Shorts se puede elegir** en la mayoría de las cuentas, pero solo importa para la
  pestaña de Shorts de tu canal y para el listado del canal — no para el feed, donde la gente ve el video
  directo. Prioridad baja.
- **La descripción** casi nadie la lee, pero YouTube sí. Pon la dirección del bar y el enlace de WhatsApp.
  Es gratis.

---

## Métricas de Shorts: lo que YouTube te da y las otras no

En YouTube Studio tienes la **curva de retención de audiencia real**, con más detalle que en las demás.
Ahí puedes ver el segundo exacto donde la gente se va (ver `149`).

También te da:

| Métrica | Qué te dice |
|---|---|
| **Visualizaciones** | Se cuentan al iniciar la reproducción (cambió en 2025) — infladas respecto a antes |
| **Espectadores** | Personas distintas. Más honesto que visualizaciones |
| **Retención de audiencia** | La curva. La joya |
| **Duración media de la reproducción** | Divídela por la duración → tu porcentaje visto |
| **Porcentaje de "vistos" vs "deslizados"** (swipe away) | La versión YouTube de la tasa de salto |

Cuidado con las visualizaciones: desde 2025 YouTube cuenta la visualización de un Short cuando empieza a
reproducirse, no cuando alguien la ve un rato. **Tus números de vistas subieron sin que mejoraras nada.**
No compares vistas de antes y después de ese cambio.

---

## Subir el mismo video a las tres

Funciona, con estos cuidados:

1. **Cero marcas de agua.** YouTube también penaliza contenido reciclado con marca de agua visible.
2. **Considera un corte más largo para Shorts.** Es la que más lo aguanta.
3. **El audio tiene que estar limpio.** Lo que pasa desapercibido en TikTok aquí se nota.
4. **Título con palabras de búsqueda**, distinto al caption de las otras.

---

## Errores comunes

- **Tratar Shorts como "el basurero donde tiro lo que ya publiqué".** Es donde el contenido vive más tiempo.
- **No cerrar el bucle.** Es la plataforma donde el bucle más rinde, y casi nadie lo hace.
- **Poner algo importante en los últimos 450 px.** Ahí vive el botón de Suscribirse.
- **Audio sucio.** Aquí más gente escucha; el eco del local se nota.
- **Título de red social ("vibras ✨") en vez de título de búsqueda.**
- **Cortar el video igual que para TikTok.** Shorts aguanta 35 s; le estás dando 10 y desperdiciando.
- **Comparar tus vistas de 2024 con las de 2026.** YouTube cambió cómo cuenta. No son la misma cifra.
- **Obsesionarse con la miniatura del Short.** En el feed no se ve.
- **Dejar la descripción vacía.** Es el único sitio de las tres donde puedes poner un enlace sin trampas.
- **Esperar que un Short llene mesas hoy.** Es siembra a mediano plazo, no pauta.

---

## Checklist

- [ ] **1080x1920, MP4, H.264**, fps constantes, AAC 48 kHz, bitrate generoso (16 Mbps).
- [ ] Dura **3 minutos o menos** y es vertical (si no, no entra a Shorts).
- [ ] **Cero marcas de agua.**
- [ ] Nada importante en los **500 px de abajo** ni en los **140 px de la derecha**.
- [ ] **El bucle cierra**: verifiqué concatenando el video 3 veces y no se nota la costura.
- [ ] Comparé el **primer y el último fotograma** como imágenes.
- [ ] La duración está en la franja **20–45 s** (o tengo razón para salirme).
- [ ] El **audio está limpio**: sin eco, sin viento, voz clara, nivelada.
- [ ] Hay texto en pantalla igualmente (no todos escuchan).
- [ ] El **título tiene palabras que alguien buscaría**, incluyendo el municipio.
- [ ] La **descripción** tiene dirección y enlace de WhatsApp.
- [ ] Voy a mirar la **curva de retención en YouTube Studio** a los 3 días, no el conteo de vistas.

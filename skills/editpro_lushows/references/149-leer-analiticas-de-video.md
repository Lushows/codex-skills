# 149 — Leer analíticas de video: cómo saber qué falló y qué cambiar

> Verificado a **agosto de 2026**. Los nombres de las métricas cambian; el método de lectura no. Este
> módulo es la contraparte práctica de `140`: allá está la teoría de qué mide qué, aquí está qué hacer el
> lunes por la mañana con el panel abierto.

## La pregunta que estás contestando

No es "¿cómo le fue?". Es:

> **¿Qué cambio concreto hago en el próximo video?**

Si terminas de mirar los números y no tienes una acción escrita, perdiste el tiempo. Todo este módulo
existe para llegar a una frase del tipo "el próximo video empieza con el precio en pantalla".

---

## Cuándo mirar

| Momento | Qué miras | Qué NO miras |
|---|---|---|
| **Primeras 2 horas** | Nada. Cierra la app | Todo |
| **24 horas** | Si arrancó o no (¿pasó de 500 vistas?) | Retención (aún es ruido) |
| **72 horas** | **Aquí se lee de verdad**: curva, retención, reenvíos | — |
| **7 días** | Confirmación; comparación con otros videos | — |
| **30 días** | Solo en YouTube (los Shorts siguen creciendo) | En IG/TikTok ya está muerto |

**Mirar a las 2 horas es la forma más eficiente de tomar decisiones malas.** El reparto inicial de las
plataformas es ruidoso y depende de a quién le tocó primero. Aguántate.

---

## Los tres diagnósticos posibles

Todo video que rinde mal tiene una de estas tres enfermedades. Tu trabajo es identificar cuál.

### Diagnóstico 1 — El gancho falló

**Cómo se ve:**
- Instagram: **tasa de salto alta**; la curva de retención se derrumba antes del segundo 3.
- TikTok: menos del 45 % sigue ahí a los 3 segundos.
- Meta Ads: **hook rate por debajo del 15 %**.
- YouTube: menos del 60 % a los 30 segundos.
- Síntoma indirecto: **pocas vistas totales**. La plataforma probó, salió mal, dejó de repartir.

**Qué NO es:** no es la música, no es el color, no es el final, no es la hora de publicación, no es el
hashtag. Es el primer fotograma y la primera frase.

**Qué haces:**
1. Abre el mismo material.
2. Haz **tres arranques distintos** para el mismo cuerpo del video.
3. Publica el que más te incomode (suele ser el mejor: el que se siente "demasiado directo").

Los tres arranques típicos que puedes probar con cualquier material de bar:
- **Problema:** "¿otra vez sin plan?"
- **Precio:** "$12.000"
- **Cara:** alguien mirando a cámara diciendo la primera frase
- **Objeto:** primerísimo plano de la cosa, en movimiento

### Diagnóstico 2 — El desarrollo falló

**Cómo se ve:**
- La curva **se sostiene los primeros segundos y luego cae en un punto concreto**.
- Meta Ads: **hook rate bien, hold rate mal**.
- Muchas vistas, poca retención promedio.

**Qué haces:**
1. Anota el **segundo exacto** donde cae.
2. Abre el video en ese segundo y mira qué hay.
3. Casi siempre es una de estas cuatro:

| Lo que hay en el segundo del derrumbe | Arreglo |
|---|---|
| Un plano que dura más de 3 s sin cambio | Corta o mete un punch-in |
| Relleno hablado ("bueno, entonces, eh…") | Corta la frase entera |
| El momento en que se vuelve publicidad | Mueve la venta más adelante o hazla más natural |
| Información que ya se sabía | Elimínala |

4. **Corta ese pedazo del video existente y republica.** No hace falta grabar de nuevo.

### Diagnóstico 3 — El remate falló

**Cómo se ve:**
- La curva llega bien al final: buena retención, buen porcentaje completado.
- **Pero no pasa nada**: pocos reenvíos, pocos mensajes de WhatsApp, ninguna reserva.

Este es el diagnóstico **bueno**, porque significa que el video funciona y solo falta la conversión.

**Qué haces:**
- Revisa que haya **una sola acción pedida**, no tres.
- Revisa que la acción sea **concreta**: "escríbeme *hola*" en vez de "contáctanos".
- Revisa que **quepa en la zona segura** — un CTA bajo el caption no existe.
- Revisa que el CTA aparezca **antes del último segundo**: si sale en el segundo 14,8 de un video de 15,
  nadie lo lee.
- Revisa que **haya un motivo para actuar hoy**: cupos, hora, promoción con fecha.

---

## Dónde está cada cosa, plataforma por plataforma

### Instagram
`Reel → Ver estadísticas`

| Qué buscar | Cómo interpretarlo |
|---|---|
| **Gráfico de retención** | La curva. Lo más útil que dan. Busca dónde cae |
| **Tasa de salto (skip rate)** | Alta = gancho roto |
| **Tiempo medio de visualización** | Divídelo por la duración → porcentaje visto |
| **Compartidos / envíos** | La métrica que abre público nuevo. Míralo siempre |
| **Guardados** | Interés real, intención de volver |
| **Cuentas alcanzadas vs seguidores** | Si el % de no-seguidores es alto, el video sí se repartió |

### TikTok
`Perfil → Herramientas de creador → Analíticas → Contenido → el video`

| Qué buscar | Cómo interpretarlo |
|---|---|
| **Retención de espectadores** (la curva) | Igual que arriba |
| **Vieron el video completo** | El porcentaje de finalización directo. La métrica reina |
| **Tiempo de visualización promedio** | ÷ duración = porcentaje visto |
| **Fuentes de tráfico** | Si "Para ti" es bajo, no se repartió. Si es alto y aun así pocas vistas, el gancho falló |
| **Búsquedas que llevaron al video** | Oro para negocio local: te dice qué busca la gente |

### YouTube
`YouTube Studio → el video → Participación`

| Qué buscar | Cómo interpretarlo |
|---|---|
| **Retención de audiencia** | La curva más detallada de todas las plataformas |
| **Picos hacia arriba** | Gente rebobinando: algo interesante o algo confuso |
| **Duración media de reproducción** | ÷ duración = porcentaje |
| **CTR de impresiones** | Solo en largo. 4–10 % es normal |
| **Fuentes de tráfico** | ¿Búsqueda, sugeridos, feed de Shorts? Cambia lo que optimizas |

### Meta Ads
`Administrador de anuncios → columnas → Personalizar columnas`

Añade estas columnas y guárdalas como vista propia:

```
Impresiones
Reproducciones de video de 3 segundos
ThruPlays
Reproducciones hasta el 25 % / 50 % / 75 % / 100 %
Clics en el enlace
CTR (de clics en el enlace)
Costo por resultado
```

Y calcula a mano en una hoja:

```
Hook rate  = reproducciones 3 s ÷ impresiones
Hold rate  = ThruPlays ÷ reproducciones 3 s
```

Las **reproducciones al 25/50/75/100 %** son tu curva de retención pobre pero suficiente:

| Ejemplo | Valor | Lectura |
|---|---|---|
| Impresiones | 20.000 | — |
| 3 s | 3.400 | hook rate 17 % → **flojo** |
| 25 % | 2.100 | del que se quedó, la mayoría sigue |
| 50 % | 1.700 | pérdida suave |
| 75 % | 1.500 | — |
| 100 % | 1.350 | 40 % de los que pasaron el gancho terminaron → **el video está bien** |

Ese anuncio no necesita video nuevo. Necesita **gancho nuevo**.

---

## La hoja que de verdad te sirve

Ninguna plataforma mide lo que a ti te importa. Arma esta tabla y llénala cada lunes. Diez filas y ya vas
a saber más de tu negocio que cualquier consultor.

| Fecha | Video | Plataforma | Dur. | Vistas | % visto | Reenvíos | **Msjs WhatsApp** | **Reservas** | Gancho usado |
|---|---|---|---|---|---|---|---|---|---|
| 2 ago | chorizo | IG | 12 s | 3.400 | 71 % | 88 | 14 | 4 | precio |
| 3 ago | trivia | IG | 28 s | 9.100 | 22 % | 6 | 2 | 0 | logo+recorrido |
| 5 ago | michelada | TikTok | 9 s | 12.000 | 68 % | 210 | 31 | 9 | primer plano |

Después de 10 filas, mira la columna del **gancho usado** y la de **mensajes**. Ahí está tu respuesta, no
en ningún blog.

---

## Cómo saber si un cambio funcionó

El error clásico: cambias cinco cosas, mejora, y no sabes cuál fue.

**Regla: un cambio por vez, tres videos por cambio.**

```
Semana 1:  3 videos con gancho de precio       → promedio 62 % visto, 24 mensajes
Semana 2:  3 videos con gancho de cara         → promedio 48 % visto, 11 mensajes
```

Con eso ya puedes decidir. Con un video de cada uno, no.

Y compara siempre **contra tu propio promedio**, no contra números de internet. Tu 45 % puede ser
excelente para tu categoría y tu público.

---

## Señales de alarma que no son lo que parecen

| Lo que ves | Lo que crees | Lo que suele ser |
|---|---|---|
| Muchas vistas, cero mensajes | "La gente no compra" | El video no pedía nada, o el CTA estaba tapado |
| Pocas vistas, buena retención | "Fracasó" | **Formato ganador con poco reparto.** Repítelo; y considera meterle pauta |
| Muchas vistas de golpe y luego nada | "Se murió" | Normal. El reparto es a oleadas |
| Comentarios negativos | "Salió mal" | Los comentarios son señal de reparto. Peor es el silencio |
| Retención altísima con 200 vistas | "¡Excelente!" | Muestra insuficiente. Espera más datos |
| Un video explota una vez | "Encontré la fórmula" | Puede ser suerte. Repítelo 3 veces antes de creerlo |

**El caso "pocas vistas, buena retención" es el más importante y el que más se ignora.** Es un video bueno
que no le tocó a la gente correcta. Es exactamente el candidato a convertirse en anuncio pagado: ya
sabes que retiene, solo le falta alcance. Ver `145`.

---

## El ciclo de una semana

```
Lunes     Abres el panel. Miras los videos de la semana pasada (>72 h).
          Escribes UNA frase de diagnóstico por video.
          Decides UN cambio para esta semana.

Martes    Grabas. Documentas, no produces.

Miércoles Montas 3–5 piezas con el cambio decidido.

Jueves    Publicas la primera. A viernes y sábado el resto.

Domingo   No miras nada.

Lunes     Vuelves a empezar.
```

El ciclo es más importante que cualquier técnica. **Un editor mediocre que itera cada semana supera a un
editor bueno que publica cuando se acuerda.**

---

## Errores comunes

- **Mirar a las 2 horas.** Ruido. Decisiones malas garantizadas.
- **Terminar de mirar los números sin escribir una acción.** Entonces no miraste nada.
- **Cambiar cinco cosas a la vez.** No aprendes cuál sirvió.
- **Sacar conclusiones con un solo video.** Tres videos del mismo tipo, mínimo.
- **Celebrar vistas.** Vistas con retención baja es la plataforma decidiendo que no.
- **Confundir "el gancho falló" con "el video es malo".** El cuerpo suele estar bien; solo tocaba el inicio.
- **Grabar de nuevo cuando bastaba con cortar 4 segundos.** El material ya lo tienes.
- **Ignorar el caso "pocas vistas, buena retención".** Es tu mejor candidato para pauta.
- **Comparar tus números con los de una cuenta de entretenimiento.** No es tu categoría ni tu duración.
- **No anotar los mensajes de WhatsApp y las reservas.** Es la única métrica que paga la nómina.
- **Mirar solo la métrica resumen y no la curva.** El resumen te dice que algo está mal; la curva te dice dónde.
- **Dejar de publicar porque un video salió mal.** El ciclo importa más que cualquier video individual.

---

## Checklist

- [ ] Estoy mirando el video **72 horas después** de publicarlo, no antes.
- [ ] Tiene al menos **1.000 reproducciones** (si no, no concluyo).
- [ ] Miré **la curva de retención**, no solo el número resumen.
- [ ] Identifiqué el diagnóstico: **gancho / desarrollo / remate**.
- [ ] Si es el gancho: anoté los **3 arranques alternativos** que voy a probar.
- [ ] Si es el desarrollo: anoté el **segundo exacto** de la caída y qué hay ahí.
- [ ] Si es el remate: verifiqué que el CTA es **uno solo, concreto, dentro de la zona segura y con motivo
      para actuar hoy**.
- [ ] Calculé el **porcentaje visto** = tiempo promedio ÷ duración.
- [ ] Anoté **reenvíos**, **mensajes de WhatsApp** y **reservas** en mi hoja.
- [ ] Estoy cambiando **una sola cosa** esta semana, y voy a hacer **3 videos** con ese cambio.
- [ ] Comparé contra **mi propio promedio**, no contra cifras de blogs.
- [ ] Revisé si hay algún video con **pocas vistas y buena retención** para meterle pauta.
- [ ] Escribí **una frase de acción** por cada video revisado. Si no, vuelvo a empezar.

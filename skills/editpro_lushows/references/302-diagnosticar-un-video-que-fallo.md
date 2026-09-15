# 302 — Diagnosticar un video que falló: el árbol completo

> Verificado a **agosto de 2026**. `149` te dio tres diagnósticos rápidos (gancho / desarrollo / remate).
> Este módulo es el árbol completo con **seis sospechosos**, en el orden correcto de descarte, y con la
> prueba concreta que confirma o descarta cada uno. Porque el error caro no es diagnosticar mal: es
> **diagnosticar en el orden equivocado** y terminar cambiando la música de un video que murió porque
> nadie lo vio.

## Regla número uno: "falló" hay que definirlo antes

"Le fue mal" no es un diagnóstico, es un sentimiento. Antes de abrir el árbol, escribe **contra qué está
fallando**:

| Comparación | Cuándo usarla |
|---|---|
| Contra **tu propio promedio** de los últimos 10 videos | Siempre. Es la única honesta |
| Contra el **mismo formato** publicado antes | Cuando estás iterando un formato |
| Contra **el objetivo escrito** antes de grabar | Cuando el video tenía un trabajo concreto |
| Contra números de blogs | Nunca como juez. Solo como orientación gruesa |

Un video con 42 % visto "falló" si tu promedio es 58 %. Y "ganó" si tu promedio es 31 %. **El mismo
número.** Sin tu promedio, no tienes diagnóstico, tienes opinión.

---

## El árbol, en orden de descarte

El orden importa porque cada nivel **invalida** los siguientes. No tiene sentido analizar el remate de un
video que la plataforma nunca repartió.

```
                    ¿SE REPARTIÓ?
                    (¿llegó a gente?)
                     │
        NO ──────────┴────────── SÍ
        │                        │
   SOSPECHOSO 6            ¿PASARON DEL SEGUNDO 3?
   distribución             │
                  NO ───────┴─────── SÍ
                  │                  │
             SOSPECHOSO 1       ¿LLEGARON AL FINAL?
             gancho              │
             (o 4: portada)  NO ──┴─── SÍ
                             │         │
                        SOSPECHOSO 2   ¿HIZO ALGO ALGUIEN?
                        desarrollo      │
                                   NO ──┴─── SÍ
                                   │         │
                              SOSPECHOSO 3   NO FALLÓ
                              remate         (ver abajo)
                              (o 5: tema)
```

---

## Nivel 0 — ¿Se repartió? (Sospechoso 6: distribución)

**Prueba:** mira las vistas totales contra tu promedio, y las **fuentes de tráfico**.

| Señal | Lectura |
|---|---|
| Vistas muy por debajo de tu promedio **y** tasa de salto normal | La plataforma no lo repartió. No es problema de edición |
| TikTok: "Para ti" muy bajo | No entró al reparto |
| Instagram: casi todo el alcance son seguidores | No salió del círculo |
| Vistas bajas **pero** retención altísima | **Video bueno, reparto malo.** El caso más valioso |

**Causas reales de que no se reparta**, en orden de frecuencia:

1. **Música con derechos** en una cuenta de empresa. Es la causa #1 y la más invisible: el video se publica
   sin error visible y simplemente no se reparte. Usa la biblioteca comercial.
2. **Marca de agua de otra app** (el logo de CapCut/TikTok en un reel de Instagram). Penalización directa.
3. Texto que la plataforma lee como spam ("link en bio", promesas de dinero, palabras sensibles).
4. Publicar 3 videos en 20 minutos: se canibalizan.
5. Cuenta con una advertencia activa por algo que subiste hace semanas.
6. **Nada.** A veces simplemente le tocó mal. Pasa.

**Cómo confirmar:** vuelve a publicar el mismo video (sin música con derechos, sin marca de agua) tres días
después. Si esta vez se reparte, era distribución. Si vuelve a morir, sigue bajando en el árbol.

> Este nivel se salta muchísima gente y por eso rehace videos que estaban perfectos.

---

## Nivel 1 — ¿Pasaron del segundo 3? (Sospechoso 1: gancho)

**Prueba:** tasa de salto en Instagram; % que sigue a los 3 s en TikTok; hook rate en Meta Ads.

Referencias 2026 en pauta de Meta (de agencias, no oficiales de Meta — úsalas como semáforo):

| Hook rate | Lectura |
|---|---|
| menos de **15 %** | Roto. Mátalo, no lo optimices |
| **25–28 %** | Normal. La mediana del mercado ronda ahí |
| más de **40 %** | Excelente. El top ~10 % |

En orgánico la señal equivalente es la tasa de salto de Instagram: **cuanto más alta, peor**. Compárala
contra tu propio promedio antes que contra cualquier tabla.

### Las seis razones por las que un gancho falla

| Razón | Cómo se ve en el video | Arreglo |
|---|---|---|
| **Arranca con logo/intro** | Los primeros 1,5 s son la marca | Bórralos. La marca va al final |
| **Primer fotograma sin información** | Plano general, mesa vacía, cielo | Empieza con lo más interesante que tengas |
| **La primera frase es un saludo** | "Hola a todos, cómo están" | Empieza por la mitad de la frase importante |
| **Nada se mueve** | Plano fijo de algo quieto | Movimiento en el primer segundo, aunque sea un push-in |
| **No se entiende qué estoy viendo** | Plano cerradísimo sin contexto | Un fotograma de contexto y luego el detalle |
| **Promete algo aburrido** | "Hoy les traigo un dato" | Promete algo específico y concreto |

### El truco de descarte más barato que existe

**Republica el mismo video con solo los primeros 2 segundos cambiados.** No regrabes nada.

```bash
# Quitar el primer segundo y medio (el logo, el saludo)
ffmpeg -ss 1.5 -i reel.mp4 -c:v libx264 -crf 18 -c:a aac reel_v2.mp4
```

Si el segundo intento se reparte y retiene, el diagnóstico está confirmado y ya tienes la lección más
rentable de tu mes: **tu material sirve, tu arranque no.**

---

## Nivel 2 — ¿Llegaron al final? (Sospechoso 2: desarrollo)

**Prueba:** la curva de retención y la forma que tenga (ver `301`).

Ya sabes localizar el segundo culpable. Aquí está el catálogo de qué encuentras cuando llegas ahí:

| Lo que hay en el segundo del derrumbe | Frecuencia | Arreglo |
|---|---|---|
| Un plano de más de 2 s sin cambio visual | Altísima | Corta o mete punch-in |
| Relleno hablado ("bueno", "eh", "entonces") | Altísima | Corta la frase entera |
| Una segunda idea que nadie pidió | Alta | Bórrala. El video termina antes |
| El momento en que se nota que es comercial | Alta | Mueve la venta o vuélvela parte de la acción |
| Un texto largo que no da tiempo a leer | Media | Menos palabras, más tiempo |
| Silencio o bajón de audio | Media | El audio plano expulsa |
| Información que ya se sabía | Media | Elimínala |
| Un corte confuso (no se entiende dónde estamos) | Baja | Plano de reubicación |

### La prueba del "sin sonido"

Ve el video en silencio. Si en la ventana del derrumbe la pantalla no cuenta nada por sí sola, ahí está tu
respuesta: **el video depende del audio y la mayoría lo ve mudo o a medias.**

### La prueba del reloj

Cronometra cada bloque de tu montaje. Estándar 2026: **cambio visual cada 1,5–2 s**. Si un bloque dura 5
segundos con un solo encuadre, no necesitas más análisis.

---

## Nivel 3 — ¿Hizo algo alguien? (Sospechoso 3: remate)

**Prueba:** retención buena, finalización buena, **pero** reenvíos, guardados, mensajes o reservas en cero.

Este es el mejor diagnóstico posible, porque el video ya funciona. Las causas:

| Causa | Cómo se detecta | Arreglo |
|---|---|---|
| No pediste nada | Ves el video y no hay acción | Una acción, una sola |
| Pediste tres cosas | "Síguenos, comenta y comparte" | Escoge una |
| La acción es abstracta | "Contáctanos" | "Escríbeme *hola* al WhatsApp" |
| El CTA está tapado | Se cruza con la UI o el caption | Zona segura (ver `147`) |
| El CTA sale en el último medio segundo | El video corta encima | Que aparezca antes y se quede |
| No hay motivo para actuar hoy | "Vengan cuando quieran" | Fecha, hora, cupo, precio |
| El remate cambia de tono | Se pone locutor de radio | Que lo diga la misma persona igual |

---

## Sospechoso 4 — La portada (solo Instagram y YouTube)

En Instagram la portada importa en tu **perfil** y en la pestaña de Reels, no tanto en el feed donde
autorreproduce. En YouTube importa muchísimo (CTR de impresiones).

**Cómo se detecta:** vistas bajas + la mayoría del alcance viene de **perfil** o **búsqueda** en vez del
feed. Y en YouTube: CTR por debajo del 4 %.

**Arreglo:** una portada legible a tamaño de uña, con una sola cara o un solo objeto grande, texto de tres
palabras máximo.

**No apliques este diagnóstico si tu tráfico viene del feed.** Ahí la portada casi no existe.

---

## Sospechoso 5 — El tema

El más incómodo, porque no se arregla editando. Señal:

> El video está bien hecho (buen gancho, buena curva, buen remate) y aun así **a nadie le importó**.

Cómo confirmar: publica el **mismo tema** con otro formato y otro gancho. Si vuelve a morir, no era el
montaje. **A tu público no le interesa ese tema.**

Temas que suelen morir en una cuenta de bar-restaurante:

- El aniversario del local (le importa a ti, no a ellos).
- "Ya tenemos nueva carta" sin mostrar un plato específico.
- Agradecimientos genéricos.
- Contenido "motivacional" sin relación con el bar.
- El equipo saludando (funciona solo si el equipo ya es conocido).

Temas que suelen jalar:

- Un plato específico en primer plano y en movimiento.
- Precio explícito.
- Algo que pasó anoche.
- Una persona real diciendo algo real.
- El detrás de cámara de cómo se hace algo.

---

## Sospechoso 6 bis — La hora y el día

Lo pongo aparte porque **es el sospechoso más sobrevalorado del mundo**. La gente culpa a la hora antes
que a cualquier otra cosa, y casi nunca es la hora.

**La verdad honesta:** en 2026 las plataformas reparten contenido durante días, no durante la hora
siguiente. La hora afecta el **empujón inicial**, no el techo del video.

**Cuándo la hora SÍ importa:**
- Contenido con caducidad ("hoy hay música en vivo a las 9").
- Cuentas muy pequeñas donde el empujón inicial de los seguidores es todo el reparto que hay.

**Cómo probarlo de verdad:** publica el mismo tipo de video en dos franjas, tres veces cada una. Seis
videos. Si la diferencia es menor al 20 %, es ruido (ver `304`).

---

## Cuando el diagnóstico es "no falló"

Existe y hay que saber reconocerlo:

| Situación | Lectura |
|---|---|
| Métricas normales, dentro de tu promedio | No falló. Fue un video promedio. La mayoría lo son |
| Pocas vistas, retención excelente | **Video ganador con mal reparto.** Repítelo y considera pauta |
| Buen video de marca sin ventas esa semana | No falló. Estabas midiendo con la vara equivocada (`300`) |
| Un solo video malo entre diez buenos | Ruido. No cambies nada (`308`) |

> **La reacción exagerada a un video malo destruye más cuentas que los videos malos.** Alguien tira un
> formato que funcionaba porque una publicación salió floja. Tres videos mínimo antes de matar un formato.

---

## La ficha de diagnóstico

Llénala en cinco minutos. Con diez de estas fichas ya sabes más de tu contenido que cualquier agencia.

```
VIDEO: reel_chorizo_v2          FECHA: 12 ago 2026    PLATAFORMA: IG
OBJETIVO ESCRITO ANTES: venta (mensajes de WhatsApp)
DURACIÓN EXACTA: 14,87 s

MI PROMEDIO (últimos 10): 31 % salto · 54 % visto · 47 reenvíos · 8 msjs

ESTE VIDEO:               44 % salto · 51 % visto · 12 reenvíos · 2 msjs

NIVEL 0 ¿se repartió?      SÍ (2.900 vistas, normal)
NIVEL 1 ¿pasó del 3 s?     NO  ← 44 % de salto vs 31 % mío
NIVEL 2 ¿llegó al final?   (no aplica, se cae antes)
NIVEL 3 ¿hizo algo?        (no aplica)

SOSPECHOSO: 1 — gancho
RAZÓN ESPECÍFICA: el primer plano es la barra vacía, nada se mueve, y la primera
frase es "bueno, les cuento".

ACCIÓN: republicar cortando los primeros 1,8 s y arrancando en el chorizo en la parrilla.
HIPÓTESIS: la tasa de salto baja de 44 % a menos de 35 %.
```

Esa última línea — **la hipótesis** — es la que convierte un diagnóstico en un aprendizaje. Sin ella, solo
arreglaste un video. Con ella, estás construyendo conocimiento (ver `304` y `306`).

---

## Errores comunes

- **Diagnosticar sin tener tu propio promedio.** Sin línea base, "falló" no significa nada.
- **Empezar por el sospechoso 5 (el tema) o por la hora.** Son los últimos, no los primeros.
- **Culpar a la hora de publicación.** El sospechoso más acusado y el menos culpable.
- **Saltarse el nivel 0.** Rehacer un video que murió por música con derechos es tiempo tirado.
- **Analizar el remate de un video que muere en el segundo 2.** No existe ese remate para nadie.
- **Regrabar cuando bastaba con cortar 1,8 segundos del inicio.**
- **Cambiar cinco cosas en la nueva versión.** Entonces no vas a saber cuál sirvió (`304`).
- **Diagnosticar la portada cuando el tráfico viene del feed.** Ahí casi no existe.
- **Matar un formato por un solo video flojo.** Tres videos mínimo.
- **No escribir la hipótesis.** Sin predicción, el siguiente video no te enseña nada.
- **Confundir "video promedio" con "video fallido".** La mayoría de tus videos van a ser promedio, y está
  bien: el promedio es lo que sostiene la cuenta.

---

## Checklist

- [ ] Escribí **mi promedio de los últimos 10 videos** antes de juzgar este.
- [ ] Tengo el **objetivo escrito antes de grabar** a la vista.
- [ ] **Nivel 0:** verifiqué si se repartió (vistas vs promedio, fuentes de tráfico).
- [ ] Descarté música con derechos y marca de agua de otra app.
- [ ] **Nivel 1:** miré la tasa de salto / hook rate contra mi propio promedio.
- [ ] **Nivel 2:** clasifiqué la forma de la curva y localicé el segundo culpable (`301`).
- [ ] **Nivel 3:** revisé que hubiera **una sola** acción, concreta, visible y con motivo para hoy.
- [ ] Consideré la portada **solo si** el tráfico viene de perfil o búsqueda.
- [ ] Consideré el tema **solo después** de descartar todo lo demás.
- [ ] No culpé a la hora sin haberlo probado con 6 videos.
- [ ] Llené la **ficha de diagnóstico** completa.
- [ ] Escribí **una hipótesis medible** para el siguiente intento.
- [ ] Voy a cambiar **una sola cosa** en la nueva versión.

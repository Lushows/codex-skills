# 128 — Mensaje trigger-based (disparado por una señal)

El correo con la tasa de respuesta más alta del outbound no es el más ingenioso: es el que llega **en el momento exacto** en que el prospecto tiene el problema. Un mensaje trigger-based (disparado por un *trigger* = un evento o señal observable que indica que la necesidad se acaba de abrir) aprovecha esa ventana. La lógica de qué señales existen y cómo detectarlas está en `14` (triggers y eventos de compra) y `37` (signal-based selling); este módulo es lo que va **después de detectar la señal**: cómo se escribe el correo "vi que…" para que el timing se convierta en respuesta. La conversación de venta que se abre → `ventas_lushows`.

## El principio: relevancia por timing, no por ingenio

Un cold email frío pelea contra "no te conozco y no es prioridad". Un trigger-based email cambia la premisa: llegas justo cuando **algo cambió** en la empresa del prospecto y ese cambio activa tu relevancia. Ya no interrumpes; apareces oportuno. La señal responde por sí sola la pregunta de `52` — *"¿por qué me escribes A MÍ, HOY?"* — porque literalmente pasó hoy.

El resultado: reply rates muy por encima del promedio (a menudo 2–3× una campaña genérica), porque el prospecto piensa "qué oportuno" en vez de "otro más". El precio: requiere detectar la señal a tiempo y actuar rápido — un trigger de hace 4 meses ya no es trigger.

## La anatomía del correo "vi que…"

Cuatro movimientos, en este orden:

```
1. LA SEÑAL — nombra el evento concreto que viste. Específico, verificable.
   "Vi que abrieron sede en Chapinero este mes."

2. EL PUENTE — conecta ESA señal con el problema que resuelves.
   "Cuando se crece a dos cocinas, el costeo a ojo empieza a fallar."

3. EL VALOR + PRUEBA — qué resuelves, con un similar (ver 123).
   "Ayudamos a [similar que vivió lo mismo] a costear cada plato en minutos."

4. CTA SUAVE — bajo compromiso, atado al momento (ver 55).
   "¿Le hace sentido verlo ahora que están en plena apertura?"
```

La bisagra es el **puente** (paso 2). Muchos ven la señal y saltan directo al pitch, dejando al prospecto pensando "¿y a mí qué?". El puente hace explícita la conexión señal → dolor → tu solución. Sin puente, el trigger es solo un dato curioso.

## Catálogo de triggers y el gancho que dispara cada uno

(La detección se trabaja en `14` y `37`; aquí, el ángulo del mensaje.)

| Trigger (señal) | El gancho "vi que…" |
|---|---|
| **Abrió sede / expansión** | "crecer a dos operaciones rompe lo que funcionaba con una" |
| **Contrató para un rol X** (vacante) | "vi que buscan [rol] — señal de que están escalando [área]" |
| **Ronda de inversión / crecimiento** | "con capital fresco, [problema] se vuelve prioridad" |
| **Nuevo directivo en el cargo** | "los primeros 90 días son para dejar huella en [su área]" |
| **Lanzó producto / menú nuevo** | "cada lanzamiento mete incertidumbre en [tu métrica]" |
| **Post/queja pública sobre el dolor** | "vi tu post sobre [tema] — justo lo que resolvemos" |
| **Usa tecnología X** (technographic, ver `15`) | "vi que usan [X]; solemos complementarlo con…" |
| **Cambio regulatorio / de mercado** | "con [cambio], [problema] pesa más este año" |

## Ejemplos reales (dos triggers, LatAm)

**Trigger: vacante de cocinero (señal de crecimiento)**
```
Hola Andrés,

Vi que están buscando cocineros en Computrabajo — señal de que la cocina
va a full y siguen creciendo.

Cuando el volumen sube, el costeo de platos que se llevaba en la cabeza
empieza a escaparse el margen sin que nadie lo note.

Ayudamos a restaurantes en pleno crecimiento a saber el costo exacto por
plato en minutos. [Similar] lo hizo justo al expandirse.

¿Le hace sentido verlo ahora que están sumando gente?
— Luis
```

**Trigger: post público quejándose del dolor**
```
Hola Marcela,

Me crucé con tu post del martes sobre cómo el alza de la proteína te está
comiendo el margen — se nota que es un dolor real ahorita.

Justo eso resolvemos: saber el costo exacto de cada plato para ajustar
precios con datos y no a ojo. [Similar] recuperó 6% de margen así.

¿Te muestro cómo quedaría con tu carta? 15 min.
— Luis
```

## La velocidad importa: la ventana del trigger

Un trigger tiene fecha de vencimiento. Reglas prácticas:
- **Trigger "caliente"** (post, queja, noticia del día): actúa en 24–72 h. Después se enfría.
- **Trigger "estructural"** (abrió sede, contrató, nuevo directivo): la ventana es semanas, no meses.
- **Automatiza la detección** para no llegar tarde: Clay + fuentes de señal alimentan una lista que se refresca (ver `31`, `36` intent data, `37`). La IA puede redactar el "vi que…" a partir de la señal (ver `120`).
- **No fuerces triggers viejos.** "Vi que abrieron sede" seis meses después suena a que recién te enteras — resta en vez de sumar.

## Errores comunes (qué NO hacer)

- **Señal sin puente.** Nombrar el evento y saltar al pitch deja al prospecto sin ver la conexión.
- **Trigger vencido.** Llegar tarde mata el efecto "qué oportuno".
- **Trigger de vanidad.** "Vi que cumpliste años en la empresa" — irrelevante para tu problema (mismo error que la personalización de vanidad, ver `52`).
- **Inventar la señal.** Si no viste algo real, no digas "vi que…". Se descubre y quema la confianza (ver `07`, `120`).
- **Un solo trigger para todo.** Distintas señales piden distintos puentes. Ten un ángulo por trigger.

## Siguiente paso

Elige UN trigger que puedas detectar de forma repetible para tu segmento (vacantes y aperturas son los más fáciles en LatAm), y escribe su plantilla "vi que…" con los 4 movimientos. La detección y el catálogo de triggers → `14`; signal-based selling → `37`; intent data → `36`; automatizar la señal → `intent` en `31`/`36` y la redacción → `120`. La prueba social que va en el paso 3 → `123`; el CTA del paso 4 → `55`. Cuando responda, la venta la lleva `ventas_lushows`.

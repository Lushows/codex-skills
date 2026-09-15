# 127 — Mensajería multicanal coherente

Una cadencia moderna toca al prospecto en varios canales: correo, LinkedIn, WhatsApp, a veces llamada (la mecánica de esa secuencia multicanal está en `61`). El error de fondo no es *qué* canales usar, sino que muchos SDR mandan **mensajes desconectados**: un correo que dice una cosa, un InMail que arranca de cero como si nunca hubieran escrito, un WhatsApp que repite lo mismo palabra por palabra. El prospecto recibe tres monólogos sueltos y ninguno construye sobre el anterior. Este módulo es sobre el **hilo narrativo**: un solo relato que avanza a través de canales distintos, adaptando el formato a cada uno sin perder la continuidad. La conversación de venta cuando responde → `ventas_lushows`.

## El principio: una historia, varias ventanas

Piensa en tu cadencia como **una sola conversación** que el prospecto ve por distintas ventanas. Cada toque debe:

1. **Reconocer los anteriores** ("te escribí por correo la semana pasada…") — así no parece que empiezas de cero cada vez, y refuerza presencia (efecto de mera exposición: cuantas más veces te ve con coherencia, más familiar y confiable te vuelves).
2. **Avanzar el relato**, no repetirlo — cada toque agrega un ángulo nuevo (un dato, una prueba, un recurso), no re-manda lo mismo.
3. **Respetar el formato del canal** — un correo puede ser 5 líneas; un WhatsApp son 2; un comentario en LinkedIn es una frase. Mismo mensaje, distinto envase.

La coherencia genera dos efectos: el prospecto **te reconoce** ("ah, el del costeo de platos") y percibe **profesionalismo** (alguien organizado, no un bot disparando a ciegas). La incoherencia hace lo contrario: pareces spam multiplicado.

## El hilo: qué se mantiene y qué cambia por canal

| Elemento | ¿Cambia por canal? |
|---|---|
| **El problema/ángulo central** | No — es el hilo. El mismo dolor en todos lados |
| **La promesa de fondo** | No — mismo resultado prometido |
| **El tono** | Se adapta: correo semiformal, WhatsApp casual, LinkedIn profesional |
| **La longitud** | Sí — cada canal su formato |
| **El "gramo" nuevo de cada toque** | Sí — cada canal aporta un ángulo distinto |
| **El CTA** | Se adapta al canal (correo pide reunión; LinkedIn, conectar; WhatsApp, un sí/no) |

Regla: **el QUÉ (problema, promesa) es constante; el CÓMO (formato, tono, longitud) se adapta.** Si cambias el qué, ya no es un hilo, son mensajes sueltos.

## El cómo: mapear el relato antes de escribir

Antes de montar la cadencia, escribe el **arco** en una línea por toque, viendo que progrese:

```
Toque 1 (Email)     → Presento el problema con observación de su cuenta
Toque 2 (LinkedIn)  → Conecto; menciono el correo; agrego un dato
Toque 3 (Email)     → Prueba social: un similar que lo resolvió
Toque 4 (WhatsApp)  → Recordatorio casual + pregunta binaria fácil
Toque 5 (Email)     → Break-up (ver 124)
```

Cada fila referencia la anterior y suma algo. Léelo de corrido: ¿parece UNA conversación o cinco desconocidos? Si es lo segundo, reescribe hasta que fluya.

## Ejemplo real (hilo coherente cross-canal, LatAm gastronomía)

```
1. EMAIL (día 1)
   Hola Andrés, vi que abrieron sede en Chapinero. Cuando se crece a dos
   cocinas el costeo de platos a ojo empieza a escaparse el margen.
   Ayudamos a saber el costo exacto por plato en minutos. ¿Le muestro?
   — Luis

2. LINKEDIN — solicitud de conexión (día 3)
   "Hola Andrés, te escribí por correo sobre el costeo de platos al abrir
   segunda sede. Me gustaría conectar por acá también."

3. EMAIL (día 6) — suma prueba social
   Hola Andrés, retomo lo del costeo. La Esquina, aquí en Bogotá, tenía el
   mismo lío al abrir su segundo local y encontró 3 platos en pérdida.
   ¿Tiene sentido 15 min esta semana? — Luis

4. WHATSAPP (día 9) — casual, corto
   Hola Andrés, soy Luis (te escribí sobre el costeo de platos 🙂).
   ¿Le sirve que le muestre en 15 min o mejor le paso un video corto?

5. EMAIL (día 12) — break-up (ver 124)
   Hola Andrés, cierro el tema por mi lado. Si algún día quieren ver cómo
   costear cada plato en minutos, me escribe y retomamos. Éxitos — Luis
```

Un solo relato ("el costeo de platos al crecer"), cinco ventanas, cada toque reconoce al anterior y agrega algo. Nunca repite palabra por palabra.

## Coordinación con rol y multi-threading

Si tocas a **varias personas** de la misma cuenta (multi-threading, ver `125`, `94`), el hilo se vuelve una malla: cada persona recibe SU ángulo por rol (`125`), pero todos apuntan al mismo resultado de negocio. El dueño ve el hilo "margen", el jefe de cocina ve el hilo "tu número", el técnico ve "menos Excel" — y si comparan, encajan en la misma historia. Coherencia horizontal (mismo relato en el tiempo) + vertical (mismo relato entre personas).

## Errores comunes (qué NO hacer)

- **Cada canal empieza de cero.** Sin "te escribí por correo", pareces tres spammers distintos. Reconoce siempre lo anterior.
- **Repetir el mismo texto en cada canal.** Copy-paste del correo al WhatsApp huele a bot. Adapta formato y agrega algo nuevo.
- **Cambiar el ángulo entre canales.** Si el correo habla de margen y el WhatsApp de otra cosa, no hay hilo. El qué es constante.
- **Ignorar el registro del canal.** Un WhatsApp con longitud y formalidad de correo choca. WhatsApp es corto y humano.
- **Descoordinar el multi-threading.** Personas de la misma cuenta con historias contradictorias. Una malla, no un enredo.

## Siguiente paso

Toma tu cadencia actual (ver `60`) y escribe el arco de una línea por toque; léelo de corrido y verifica que sea UNA historia que progresa. La mecánica y los tiempos de la secuencia multicanal → `61`; el timing entre toques → `62`; adaptar por rol → `125`; el break-up que la cierra → `124`; la infraestructura para operar varios canales → `48`; la orquestación ABM para Tier A → `94`. Cuando el prospecto entra en conversación real, el cierre es de `ventas_lushows`.

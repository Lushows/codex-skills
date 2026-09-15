# 59 — WhatsApp y DM outbound

En LatAm, WhatsApp es EL canal. Un correo se ignora días; un WhatsApp se lee en minutos. Por eso el outbound latinoamericano es **WhatsApp-first** (ver `08`, `180`, `181`). Pero justo por ser tan personal, el WhatsApp frío mal hecho se siente **invasivo** y te ganas un bloqueo (o un reporte que quema tu número, ver `47`, `119`). Este módulo te da los frameworks de WhatsApp y DM (mensaje directo en Instagram/redes) en frío que **no suenan a spam**: cortos, humanos, con permiso y con salida fácil.

## La mecánica: WhatsApp es la casa del prospecto

El correo es un buzón público; WhatsApp es la sala de la casa. Escribir ahí en frío es **entrar a un espacio íntimo**, así que las reglas son más estrictas que en email:

1. **Más corto que el email.** Un WhatsApp frío pasa de 40–60 palabras y ya cansa. Se lee en el celular, de pasada. Una idea, una pregunta.
2. **Tono de persona, no de empresa.** WhatsApp es conversación humana. "Estimado cliente, en GastroLatam nos complace…" muere al instante. Escribe como le escribes a un conocido: "Hola [Nombre], una pregunta rápida…".
3. **Nada de muros ni catálogos en el primer toque.** Ni imágenes, ni PDF, ni links, ni audios de 2 minutos. Solo texto corto. El activo (foto, demo) llega **después** de que respondan.
4. **Permiso y salida fácil.** Como no te esperan, reconocerlo y dar salida ("si no es para ustedes, sin problema me dice") baja la sensación de invasión.

Riesgo técnico: mandar WhatsApp frío a volumen desde un número quema el número (bloqueos → baneo de Meta). La infraestructura (API oficial vs no oficial, calentar número, límites) es un tema aparte → `47`, `119`. Aquí va el **copy**; la fontanería, allá.

## La estructura del WhatsApp frío (4 partes mini)

```
1. Saludo + nombre (humano, breve).
2. Micro-contexto / permiso: por qué le escribe (una frase, honesta).
3. Gancho: el problema o la observación (ver 52, 53), en una línea.
4. CTA de interés + salida fácil (ver 55).
```

## Plantillas listas para copiar

**WhatsApp frío — versión observación (la más segura):**
```
Hola [Nombre] 👋 Le escribo de GastroLatam. Vi que [restaurante] está
creciendo fuerte en Bogotá.

Ayudamos a restaurantes así a saber el costo y margen exacto de cada
plato sin hacer cuentas a mano.

¿Le hace sentido que le cuente en dos líneas? Si no es para ustedes,
me dice sin problema 🙂
```
(~50 palabras, un emoji máximo, cero links, salida fácil.)

**WhatsApp frío — versión pregunta (arranca diálogo):**
```
Hola [Nombre], soy Luis de GastroLatam 👋 Pregunta rápida:
¿hoy cómo llevan el costeo de los platos en [restaurante] —a mano,
en Excel, o más bien al ojo?

Lo pregunto porque ayudamos a varios restaurantes con justo eso.
```

**DM de Instagram frío (aún más informal, engancha con su contenido):**
```
Hola! Me encantó el reel del menú nuevo 🔥 Una duda de negocio:
¿tienen claro qué margen les deja cada plato? Ayudamos a restaurantes
a costearlos sin cuentas a mano. Si les interesa les cuento, si no
igual éxitos con la sede nueva 🙌
```

**Malos (qué NO hacer):**
```
❌ [Mensaje de 6 párrafos con el catálogo completo y 3 links]
❌ Buenos días estimado cliente. GastroLatam, líder en soluciones...  → tono corporativo frío
❌ [Empezar con un audio de 2 minutos sin permiso]                    → invasivo, nadie lo oye
❌ ¡PROMOCIÓN! 50% HOY. Escriba YA. 🔥🔥🔥                            → spam puro, bloqueo seguro
❌ [Un PDF/imagen de entrada sin una palabra]                         → spam, se ignora
```

## Reglas de oro del WhatsApp/DM frío

- **Un emoji, máximo dos.** Humaniza; en exceso, grita spam.
- **Sin links en el primer toque.** El link llega cuando ya hay conversación (y baja el riesgo de reporte).
- **Responde rápido cuando contesten.** La ventaja de WhatsApp es la inmediatez; si tardas horas, la pierdes.
- **Identifícate siempre.** Nombre + empresa. El número desconocido sin contexto = bloqueo.
- **Respeta el horario.** Nada de WhatsApp de trabajo un domingo a las 9pm. Horario laboral (timing → `62`).
- **Opt-out real.** Si dice "no me interese" o "no escriba más", paras. Es ley (Habeas Data en Colombia, ver `49`) y es reputación de número.

## El DM en Instagram/redes: el matiz

El DM frío en Instagram funciona cuando **enganchas con su contenido** (un reel, un post): eso es tu opener natural y hace que no parezca frío. El negocio gastronómico vive en Instagram, así que suele ser un canal caliente. Pero las mismas reglas: corto, humano, una pregunta, salida fácil. Ojo: Instagram también limita/banea DMs masivos desde cuentas nuevas.

## La frontera con ventas

El WhatsApp/DM es donde más rápido pasas de "frío" a "conversación" — y esa conversación es larga y humana. Tú consigues el **primer "sí, cuéntame"**. En el momento en que empieza el ida y vuelta de convencer, responder "¿cuánto cuesta?", "déjame pensarlo", rebatir dudas y cerrar por chat → eso es **venta por WhatsApp = `ventas_lushows`** (el oficio de vender por chat, con su ritmo, sus objeciones y su cierre). Tú abres y calientas el canal; ventas lo convierte en venta.

## Errores comunes (qué NO hacer)

- Mandar el catálogo/PDF/imagen de entrada, sin permiso. Spam instantáneo.
- Tono corporativo ("estimado cliente"). WhatsApp es humano o no es.
- Volumen alto desde un número sin calentar → baneo (ver `47`, `119`).
- Insistir tras un "no". Un follow-up educado sí (ver `63`); acosar, nunca.
- Escribir igual de largo que un email. Aquí, la mitad de largo.

## Siguiente paso

Adapta tu correo base (de `50`) a un WhatsApp de ≤60 palabras con salida fácil, y prepara una variante de DM que enganche con el contenido del prospecto. Antes de mandar a volumen, resuelve la infraestructura del número → `47` y `119`. La cadencia que combina WhatsApp con email y llamada → `61`. La conversación de venta después del "sí" → `ventas_lushows`.

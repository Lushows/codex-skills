# 185 — Multi-idioma y localización

El momento en que tu outbound cruza fronteras, el idioma deja de ser un detalle y se vuelve el factor #1 de credibilidad. Un mensaje traducido a máquina, o escrito en "español neutro" que no es de ningún lado, o en un inglés con estructura de hispanohablante, delata en dos segundos que eres un extranjero mandando spam — y mata la respuesta antes del primer punto. Este módulo es sobre cómo correr secuencias de outbound en varios idiomas **sin sonar traducido**: localizar de verdad, no traducir. Localización (adaptar el mensaje a cómo habla y piensa el mercado local) ≠ traducción (cambiar las palabras de un idioma a otro).

## El principio: se responde a lo que suena local, no a lo correcto

La gente responde a mensajes que parecen escritos por alguien de su mundo. No es cuestión de gramática perfecta — es cuestión de **modismos, referencias, tono y estructura mental** del idioma destino. Un inglés gramaticalmente correcto pero con orden de frase español ("I write you to present our solution…") grita "no nativo" y se lee como spam. Un "español neutro" de manual no genera la cercanía que sí da el español de la región (ver `189`). La localización es lo que separa una campaña internacional que convierte de una que solo gasta.

## Traducir ≠ localizar (la diferencia que decide)

| Traducción (mata la respuesta) | Localización (genera respuesta) |
|---|---|
| Mismo texto, palabras cambiadas | Mensaje repensado para el mercado |
| "Español neutro" de ningún lado | Español de México / Colombia / España específico |
| Modismos calcados del original | Modismos nativos del destino |
| Ejemplos y monedas del país origen | Ejemplos, ciudades y moneda locales |
| Tono uniforme global | Tono ajustado a la cultura (formal/cálido/directo) |

Localizar un cold email a México no es traducirlo del inglés: es reescribirlo como lo escribiría un vendedor mexicano — "platicar", "te late", pesos, una ciudad mexicana de ejemplo, "tú" en vez de "usted".

## Cómo correr secuencias multi-idioma sin sonar traducido

1. **Un nativo (o casi) por idioma principal.** Para tus idiomas clave, que un hablante nativo escriba o al menos revise las plantillas maestras. La IA (ver `35`) traduce bien la base, pero un humano nativo detecta lo que suena raro. No lances a un idioma que nadie de tu equipo pueda leer con oído nativo.
2. **Plantillas maestras por idioma, no una traducida.** Escribe la secuencia pensando en cada mercado desde cero, no traduzcas la inglesa. Reutiliza la *estructura* (opener, hook, CTA; ver `50`, `56`), no las palabras.
3. **Segmenta la lista por idioma/país** antes de enviar (ver `12`, `16`). Cada segmento recibe su versión localizada. Nunca mandes la misma plantilla a España y a México.
4. **Localiza las variables, no solo el cuerpo.** Ciudad, moneda ($ vs. € vs. MXN vs. COP), nombre de cliente de referencia local, ejemplo del sector en ese país. Un {{cliente_referencia}} gringo en un correo a Bogotá no ayuda.
5. **Detecta y responde en el idioma del prospecto.** Si contestan en portugués, sigue en portugués. Configura tu bandeja/CRM para rutear por idioma (ver `38`, `64`).
6. **La IA como acelerador con supervisión.** Claude/GPT localizan borradores decentes rápido; úsalos para volumen, pero pasa las plantillas maestras por ojo nativo. Nunca envíes traducción automática cruda a producción.

## Los idiomas de tu mundo (LatAm + expansión)

- **Español**: NO es uno solo. México, Colombia, España, Argentina y Chile hablan variantes que se notan (ver `189`). Localiza por país, no "neutro".
- **Portugués (Brasil)**: el gigante que muchos ignoran. Brasil es enorme, WhatsApp-first como el resto de LatAm, y el portugués brasileño es distinto del de Portugal. Nunca le escribas en español a un brasileño esperando que "entienda" — es señal de desprecio. Localiza a português do Brasil.
- **Inglés (USA/UK)**: directo, estructura nativa; cuida no calcar el orden del español (ver `183`).
- **Inglés como segunda lengua** (mercados nórdicos, Benelux): el inglés B2B funciona, pero sobrio y correcto.

## Ejemplo: mismo mensaje, tres localizaciones

```
[MÉXICO - "tú", cálido]
¡Qué tal! 👋 Vi Café Nube en Instagram y me encantó su barra.
Ayudo a cafeterías aquí en la CDMX a sacar el costo real de cada
bebida sin batallar con Excel. ¿Te late que te platique cómo?

[ESPAÑA - "usted", formal, sobrio]
Buenos días. Vi Café Nube y me llamó la atención su carta de
especialidad. Ayudo a cafeterías en Madrid a controlar el coste
real de cada producto sin las hojas de cálculo. ¿Le encajaría una
llamada breve?

[USA - inglés nativo, directo]
Hi — noticed Café Nube on Instagram, love the specialty bar. I
help coffee shops in {city} see true per-drink cost without the
spreadsheet mess. Worth a quick chat?
```

Misma estructura (observación → valor → CTA suave), tres mensajes que suenan escritos por un local. La conversación de venta que abra cualquiera → `ventas_lushows`.

## Errores comunes (qué NO hacer)

- Traducción automática cruda a producción: el error de estructura o modismo se nota y te marca spam.
- "Español neutro" para toda LatAm: no genera cercanía; localiza por país (ver `189`).
- Escribirle en español a un brasileño: portugués o nada.
- Reciclar la moneda/ciudad/cliente del país origen: rompe la ilusión de local.
- Lanzar a un idioma que nadie en tu equipo lee con oído nativo: no detectas lo que suena raro.

## Siguiente paso

Define tus 2–3 idiomas/mercados prioritarios, escribe una plantilla maestra localizada por cada uno (estructura de `50`/`56`, tono de `189`), segmenta tu lista por idioma (`12`) y configura el ruteo de respuestas por idioma (`38`, `64`). Usa la IA para acelerar borradores (`35`) con revisión nativa. Para el detalle cultural que informa cada localización ver `189`; para coordinar el envío entre husos ver `186`. La venta → `ventas_lushows`.

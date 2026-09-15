# 45 — Evitar el spam: contenido que llega a bandeja

Este módulo es el pilar "contenido" de la deliverability (ver `40`): cómo escribir el correo para que los filtros lo lean como un mensaje humano real y no como spam. Importa porque puedes tener dominios perfectos (ver `41`), autenticación 10/10 (ver `42`) y buzones calientes (ver `43`), y aun así caer en spam si el correo se ve como spam. Ojo con la frontera: **este módulo cubre el contenido para deliverability** (qué elementos técnicos evitar). El arte de escribir un correo que *convence y consigue la respuesta* —el ángulo, el hook, la propuesta de valor— vive en el Bloque 5 (`50`–`59`) y el cierre profundo en `ventas_lushows`. Aquí: que el correo **llegue**; allá: que **funcione**.

## La mecánica: qué leen los filtros

Los filtros de spam puntúan cada correo por elementos que históricamente correlacionan con basura. Ninguno solo te condena, pero sumados sí. Las señales de contenido que más pesan:

1. **Palabras spam** (spam words / spam triggers) — términos de venta agresiva.
2. **Relación texto/imagen** — muchas imágenes, poco texto.
3. **Cantidad de links** — muchos enlaces, o dominios sospechosos.
4. **HTML pesado** — plantillas de newsletter recargadas.
5. **Uniformidad** — 500 correos idénticos palabra por palabra (por eso el spintax).

## 1. Palabras spam: qué evitar

Los correos de outbound frío deben sonar como un humano escribiéndole a otro, no como un anuncio. Evita el vocabulario de "oferta":

| Categoría | Palabras a evitar (ejemplos) | Por qué |
|---|---|---|
| Dinero/urgencia | gratis, 100% gratis, gana dinero, oferta, descuento, promoción, ¡ya!, urgente, última oportunidad | Gatillos clásicos de spam |
| Garantías | garantizado, sin riesgo, resultados asegurados | Lenguaje de estafa |
| Presión | actúa ahora, no te lo pierdas, solo hoy, click aquí | Marketing agresivo |
| Símbolos | $$$, !!!, MAYÚSCULAS COMPLETAS, 🔥💰 en exceso | Se ven a promoción |

En su lugar: lenguaje neutro y conversacional. "Descuento del 50%" → "una forma de bajar tu costo por X". "Click aquí" → un link con texto natural o simplemente pega el enlace.

## 2. HTML vs texto plano: gana el texto plano

**Para outbound frío, envía texto plano (plain text), no HTML.** Un correo de una persona real a otra no lleva plantilla con banners, botones y colores. Razones:

- El texto plano se ve **1-a-1, personal** — como si lo escribiste tú, ahora, para esa persona.
- El HTML pesado (imágenes de cabecera, botones, pie corporativo) grita "correo masivo de marketing" y activa filtros + la pestaña Promociones de Gmail.
- El texto plano **carga más rápido y no tiene elementos que rastrear** (los pixeles de tracking de HTML también son señal de spam; ver abajo).

Regla: si tu correo se ve como una campaña de Mailchimp, va a Promociones. Si se ve como un correo que le mandarías a un colega, va a Principal.

## 3. Links, imágenes y tracking

- **Links: máximo 1** en un correo de primer toque, idealmente 0 en el primer correo (pide la conversación, no que hagan clic; ver `55`). Cada link extra suma riesgo. Nunca uses acortadores (bit.ly) — son bandera roja de spam.
- **Imágenes: cero** en frío. Un correo con imágenes se ve a marketing y pesa más. Si necesitas mostrar algo, lo mandas cuando ya haya conversación.
- **Tracking de apertura (open tracking):** apágalo o úsalo con cuidado. El pixel de apertura inserta una imagen invisible con un link de rastreo → eso mete un dominio de tracking en tu correo que puede ensuciar la reputación. En 2026 muchos operadores serios **desactivan el open tracking** y miden por respuestas (que es la métrica que importa igual; ver `80`). El tracking de clics es menos problemático pero igual suma un redirect.

## 4. Spintax: variar para no verte masivo

**Spintax** = escribir variaciones de una misma frase para que la plataforma elija una al azar en cada envío, de modo que no salgan 500 correos idénticos (patrón que los filtros detectan como campaña masiva). Sintaxis estándar en Instantly/Smartlead con llaves y pipe `|`:

```
{Hola|Buenas|Qué tal} {nombre},

vi que {tu equipo|ustedes} {está|están} {contratando meseros|abriendo otra sede}
en {ciudad}. {Suele venir con|Normalmente trae} un dolor de cabeza: {cuadrar los
costos|saber cuánto cuesta de verdad cada plato}.
```

Cada envío genera una combinación distinta. **Ojo:** el spintax NO reemplaza la personalización real (ver `52`); es una capa técnica anti-detección, no el mensaje relevante. Y no abuses: variaciones que cambian el sentido o que suenan raras dañan la respuesta. Úsalo en frases de relleno, no en tu propuesta de valor.

## 5. Otros factores de contenido

- **Largo:** corto gana. 50–125 palabras. Un muro de texto se ve a spam y no se lee (ver `54` sobre estructura).
- **Un solo idioma, bien escrito:** errores de ortografía y mezclas raras suben el score de spam.
- **Firma simple:** nombre + empresa + un dato de contacto. Sin banner, sin 5 iconos de redes, sin logo pesado.
- **Asunto (subject):** corto, en minúsculas, sin "RE:" falso ni clickbait ni emojis. Que parezca escrito por un humano (ver `54`).
- **Nada de adjuntos** en frío: los adjuntos disparan filtros y casi nunce se abren.

## Checklist antes de enviar (pásalo siempre)

```
[ ] Texto plano, sin HTML de plantilla
[ ] 0-1 links, ninguno acortado, ninguna imagen
[ ] Cero palabras spam (revisa la tabla de arriba)
[ ] 50-125 palabras, un solo párrafo o dos cortos
[ ] Asunto corto, humano, sin emojis ni MAYÚSCULAS
[ ] Firma simple (nombre + empresa + contacto)
[ ] Sin adjuntos
[ ] Spintax en frases de relleno (no en la propuesta)
[ ] Open tracking apagado o consciente del riesgo
[ ] Pasado por Mail-Tester → 9-10/10 (ver 42)
[ ] Leído en voz alta: ¿suena a humano o a anuncio?
```

## Errores comunes (qué NO hacer)

- Mandar en HTML bonito con logo y botón "Agenda aquí". Directo a Promociones o spam.
- Meter 3 links y un calendario embebido en el primer correo. Pide la conversación primero (ver `55`).
- Usar palabras de venta agresiva por "sonar profesional". Suena a spam.
- Confiar en el spintax como si fuera personalización. Son cosas distintas (ver `52`).
- No probar en Mail-Tester y asumir que llega.

## Siguiente paso

Con el contenido limpio, monta el **monitoreo** para confirmar que de verdad estás llegando y detectar caídas a tiempo (ver `46`: bounce/spam rate, blacklists, Google Postmaster). Para *qué decir* que consiga la respuesta (no solo que llegue), ver el Bloque 5 (`50`–`59`). Para técnicas avanzadas de contenido y evasión de filtros a gran escala, ver `110`–`119`.

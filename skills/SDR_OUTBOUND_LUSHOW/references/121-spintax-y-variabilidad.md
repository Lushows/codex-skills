# 121 — Spintax y variabilidad

Cuando mandas el MISMO texto exacto desde muchos buzones a muchos destinatarios, los filtros de spam de Google y Microsoft lo notan: ven un patrón idéntico repetido miles de veces y lo marcan como envío masivo (bulk). El spintax (de *spin* = girar + *syntax*; sintaxis que "gira" el texto generando variantes automáticamente) es la técnica para que cada correo salga con palabras ligeramente distintas, de modo que no haya dos idénticos. Es una palanca de **deliverability** (que tus correos lleguen a la bandeja y no a spam, ver `40`), no de conversión. No hace que vendas más por correo; hace que más correos *lleguen*.

## La mecánica: por qué el texto idéntico te delata

Los proveedores de correo aplican un principio simple: comunicación humana real = variada; comunicación automatizada masiva = idéntica. Si 500 personas reciben carácter por carácter el mismo cuerpo, es una huella de bulk sending. Además, dentro de tu propia infraestructura de varios buzones (ver `41`, `44`), si los 8 buzones mandan el texto calcado, los algoritmos correlacionan esos envíos como una sola campaña masiva y castigan a todos juntos.

El spintax rompe esa firma: introduce variación léxica controlada para que cada envío sea, a ojos del filtro, un mensaje único. No cambia el sentido; cambia las palabras.

## La sintaxis: cómo se escribe el spintax

Se usan llaves `{ }` con opciones separadas por barra `|`. La herramienta de envío (Instantly, Smartlead, Lemlist — ver `33`) elige una opción al azar por cada correo:

```
{Hola|Buenas|Qué tal} [Nombre],

{Vi que|Me crucé con|Noté que} {abrieron|inauguraron} su
{segunda sede|nuevo local} este mes.
```

Ese bloque genera automáticamente decenas de combinaciones. `3 × 2 × 2 = 12` variantes solo en esas dos frases; con spintax repartido en todo el correo llegas a cientos o miles de versiones únicas, todas con el mismo mensaje.

Regla de calidad: **cada opción dentro de una llave debe sonar natural y significar lo mismo.** `{Hola|Buenas|Qué tal}` está bien; `{Hola|Estimado señor|Ey}` mezcla registros (formal, informal, tosco) y algunas combinaciones sonarán raras. Prueba que CUALQUIER combinación que salga sea un correo que tú mandarías.

## Dónde poner spintax (y dónde no)

| Zona del correo | ¿Spintax? | Por qué |
|---|---|---|
| Saludo | Sí | Fácil de variar sin cambiar sentido |
| Conectores y verbos ("vi que"/"noté que") | Sí | Muchos sinónimos naturales |
| Frases de transición | Sí | Bajo riesgo de sonar raro |
| CTA (llamada a la acción) | Con cuidado | Variar la forma, no la claridad (ver `55`) |
| La observación personalizada | No hace falta | Ya es única por prospecto (ver `52`, `120`) |
| Nombres, cifras, la oferta | Nunca | No inventes variantes de datos duros |

Si ya personalizas la línea 1 con IA (ver `120`), esa línea **ya es única** y aporta variabilidad gratis: cada correo difiere en su parte más visible. El spintax refuerza el resto del cuerpo (que sí es plantilla).

## Cuánta variación necesitas

No hace falta convertir cada palabra en spintax — eso vuelve el correo ilegible de mantener y arriesga combinaciones raras. Apunta a que **no haya dos correos idénticos en una tanda**, con variación repartida:

- 3–5 puntos de spintax en un correo corto ya generan cientos de combinaciones.
- Regla práctica: si mandas 500 correos/día, quieres al menos unos cientos de variantes posibles para que casi ningún par sea igual.
- Combina spintax + línea 1 personalizada (ver `120`) + firma que rota entre buzones → variabilidad de sobra.

## Ejemplo real (cold email con spintax, LatAm PYME gastronómica)

```
Asunto: {costo por plato|el costo de tus platos|margen del menú}

{Hola|Buenas} [Nombre],

{Vi|Me crucé con|Noté} {en sus reseñas|en su Instagram} que
{están vendiendo muy bien|tienen full la cocina} — {felicitaciones|qué bueno}.

{El problema que aparece cuando eso pasa|Lo que suele pasar ahí} es que
el costeo de cada plato se hace {a ojo|a la carrera} y el margen
{se escapa|se pierde} sin que nadie lo note.

{Ayudamos a|Trabajamos con} negocios así para {saber|tener claro}
el costo exacto de cada plato en minutos.

¿{Le hace sentido|Tiene sentido} que le {muestre|cuente} cómo?

— Luis
```

Cada envío sale con una combinación distinta; el mensaje y la oferta no cambian nunca.

## Errores comunes (qué NO hacer)

- **Opciones que cambian el sentido o el registro.** Toda combinación debe ser un correo válido. Léelas.
- **Spintax en los datos** (nombre, empresa, precio, oferta). Solo varías la envoltura, no el contenido.
- **Sintaxis rota.** Una llave sin cerrar `{a|b` manda literalmente los símbolos al prospecto. Usa el previsualizador de la herramienta y genera 10 muestras antes de lanzar.
- **Creer que el spintax arregla un correo malo.** Es deliverability, no persuasión. Si el copy no convierte, variarlo tampoco venderá (el copy que convierte → `50`, `56`).
- **Confundirlo con personalización.** Spintax = misma idea con otras palabras para todos. Personalización = dato distinto por cuenta (ver `52`). Son cosas diferentes; usa las dos.

## Siguiente paso

Toma tu mejor plantilla (ver `56`) y mete 4–5 puntos de spintax en saludo, conectores y CTA. Genera 10 previsualizaciones en tu plataforma (ver `33`) y lee que todas suenen naturales. Combínalo con la línea 1 de `120` para máxima variabilidad. El resto de la defensa de deliverability (dominios, warmup, volumen) → `41`, `43`, `44`; evitar el spam a nivel de contenido → `45`.

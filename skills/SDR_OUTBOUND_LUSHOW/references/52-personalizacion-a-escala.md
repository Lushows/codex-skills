# 52 — Personalización a escala

Aquí está la tensión central del outbound moderno: **personalizar convierte, pero personalizar 1-a-1 no escala**. Este módulo resuelve esa tensión. La clave que casi nadie entiende: no se trata de personalizar el **correo**, se trata de personalizar la **observación** — la línea que demuestra que sabes algo real de SU cuenta. El resto del correo puede ser una plantilla. Personalizas el gancho, no todo el texto.

## La mecánica: por qué "Hola {nombre}" NO es personalización

Meter el nombre y la empresa con variables (`Hola {primer_nombre}, vi que {empresa}...`) es lo que hace todo el mundo, y el prospecto lo detecta al instante: sabe que 5.000 personas recibieron el mismo correo con su nombre pegado. Eso no es personalización; es **mail merge** (combinación de correspondencia), y el cerebro lo lee como spam.

La personalización real responde a una pregunta en la mente del prospecto: **"¿por qué me escribes A MÍ, hoy?"**. Si tu correo tendría exactamente el mismo sentido para cualquier otra empresa de la lista, no está personalizado. La prueba ácida: **si puedes copiar tu correo, cambiar el nombre de la empresa y sigue teniendo sentido → no está personalizado, es spam con nombre.**

## Los tres niveles: 1:1, 1:few, 1:many

| Nivel | Qué personalizas | Esfuerzo | Cuándo usarlo | Reply rate típico |
|---|---|---|---|---|
| **1:1** | Correo escrito a mano, todo único | 10–20 min/correo | Cuentas Tier A, enterprise, ABM (ver `16`, `160`) | 15–30% |
| **1:few** | Plantilla + observación por **segmento** (nicho/rol/trigger) | ~30–60 seg/correo | El caballo de batalla del outbound PYME | 5–12% |
| **1:many** | Solo variables básicas (nombre/empresa) | 0 | Casi nunca; solo volumen bajísimo valor | 1–3% |

El punto dulce para la mayoría (y para LatAm/PYME) es **1:few**: una plantilla sólida donde lo único que cambia es **una línea de observación relevante** por segmento o por señal. Ahí está el equilibrio volumen/personalización (el trade-off central se trabaja en `66`).

## El truco operativo: personalizar la variable de OBSERVACIÓN

En vez de reescribir el correo, insertas una variable `{observacion}` en el opener y **llenas esa columna** para cada prospecto (o cada segmento). El cuerpo es plantilla; la observación es el alma.

```
Hola [Nombre],

{observacion}                          ← la ÚNICA parte personalizada

Normalmente cuando [pasa eso], el costeo   ← plantilla fija por segmento
de platos se hace a ojo y el margen se
escapa. Ayudamos a negocios así a saber
el costo exacto de cada plato en minutos.

¿Le hace sentido que le cuente cómo?

[Firma]
```

Ejemplos de `{observacion}` para el mismo cuerpo:
- `Vi que abrieron su segunda sede en Chapinero este mes — felicitaciones.`
- `Vi en su Instagram que lanzaron un menú nuevo de 22 platos.`
- `Noté que están contratando cocineros en Computrabajo, señal de que están creciendo.`
- `Vi que tienen 4.7 en Google con 600 reseñas — están vendiendo bien.`

Todas caben en la MISMA plantilla. Ese es el escalado real.

## Cómo generar observaciones a escala (sin escribir 500 a mano)

Aquí entra la maquinaria (ver `31`, `35`, `120`):
1. **Fuente de señal por segmento** — en vez de investigar cada empresa, eliges un **trigger** que aplica a muchas a la vez: "todas las que contrataron cocinero este mes" (LinkedIn/Computrabajo), "todas las que abrieron sede" (prensa local, Google Maps nuevo), "todas con >500 reseñas" (Google Maps scraping). Una observación por segmento sirve para decenas de cuentas (ver `14`, `37`).
2. **Clay + IA** (ver `31`, `120`) — Clay enriquece cada fila (saca la reseña, el post de LinkedIn, la vacante) y una columna de IA redacta la línea 1 personalizada a partir de ese dato real. Es "1:1 a escala": la máquina hace la investigación que tú harías a mano.
3. **Plantillas por vertical/rol** — el cuerpo cambia por nicho (restaurante vs cafetería vs dark kitchen) y por rol (dueño vs administrador), no por individuo (ver `125`, `126`).

Advertencia: la IA que genera la observación debe partir de un **dato real** (una reseña, una vacante, un post). Si la IA "inventa" para rellenar, produce personalización falsa que suena peor que ninguna. Verifica la fuente. Para bajar el costo de esa IA a escala → `optimizer_tokens_lushows`.

## Errores comunes (qué NO hacer)

- **Confundir mail merge con personalización.** `{empresa}` pegado no engaña a nadie.
- **Personalización de vanidad.** "Vi que estudiaste en la Javeriana" — irrelevante para el negocio, suena a stalkeo. La observación debe conectar con **el problema que resuelves**, no ser un dato al azar.
- **Sobre-personalizar cuentas de bajo valor.** No gastes 15 minutos investigando a un lead Tier C. Reserva el 1:1 para las cuentas que lo valen (tiering en `16`).
- **Plantilla tan rígida que la observación no encaja.** El cuerpo debe fluir con cualquier observación del segmento.

## Siguiente paso

Elige UN trigger para tu segmento (ej. "restaurantes que abrieron sede en los últimos 3 meses"), escribe UNA plantilla de cuerpo fija y 5 observaciones de ejemplo, y prueba que todas encajen. Cómo redactar esa línea 1 a fondo → `53`. Cómo automatizar la generación de observaciones → `31` y `120`. El trade-off volumen vs personalización → `66`.

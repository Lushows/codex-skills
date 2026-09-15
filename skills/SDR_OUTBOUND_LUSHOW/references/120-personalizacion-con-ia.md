# 120 — Personalización con IA

El módulo `52` te enseñó *qué* personalizar (la observación, no todo el correo). Este módulo es el *cómo* industrial: usar IA para hacer, a escala de miles, la investigación y la redacción de la línea 1 que un SDR haría a mano en 10 minutos por cuenta. La promesa es "1:1 a escala": cada prospecto recibe una primera línea que parte de un **dato real y específico de SU cuenta**, generada por máquina, sin que tú escribas 2.000 líneas. Bien hecho, es la diferencia entre 3% y 9% de reply rate. Mal hecho, es la forma más rápida de sonar como un robot y quemar tu dominio.

## La mecánica: research → dato → línea, en una tabla

La personalización con IA no es "pídele a ChatGPT que escriba un correo bonito". Es una tubería de tres etapas sobre una hoja donde **cada fila es un prospecto**:

1. **Research automatizado** — una herramienta (Clay, ver `31`) sale a buscar una señal real por cada fila: la última reseña de Google, un post reciente de LinkedIn, una vacante abierta, una nota de prensa, el stack tecnológico del sitio (technographics, ver `15`).
2. **Extracción del dato** — de ese material crudo se saca **un hecho concreto**: "abrió sede en Chapinero en marzo", "publicó sobre food cost la semana pasada", "tiene 4.8 con 620 reseñas".
3. **Redacción de la línea** — una columna de IA convierte ese hecho en **una sola frase natural** que conecta con el problema que resuelves.

La regla de oro: **la IA redacta A PARTIR de un dato verificado, nunca inventa el dato.** Si le pides a la IA que "personalice" sin darle materia prima real, rellena con humo genérico o alucina hechos falsos — y una personalización falsa suena peor que ninguna (ver la advertencia de `52`).

## El cómo, paso a paso (con Clay + IA)

| Paso | Herramienta | Qué hace |
|---|---|---|
| 1. Lista base | Apollo / Sales Nav → Clay | Empresa, dominio, nombre, rol, LinkedIn |
| 2. Enriquecer con señal | Clay (integraciones + scraping) | Trae reseñas, posts, vacantes, prensa a columnas |
| 3. Extraer el hecho | Columna IA (Claygent / GPT) | "Resume en 1 frase el dato más relevante de X" |
| 4. Redactar la línea | Columna IA con prompt de estilo | Convierte el hecho en opener natural |
| 5. Validar | Filtro / revisión humana | Descarta filas sin dato real o con línea rara |
| 6. Exportar | Clay → Instantly/Smartlead (ver `33`) | La columna `{observacion}` entra a la plantilla |

El cuerpo del correo sigue siendo la plantilla fija por segmento de `52`; la IA solo llena la variable `{observacion}`.

## El prompt que evita el "olor a robot"

El 90% del problema de "suena a IA" está en el prompt. Un mal prompt produce: "¡Espero que este correo te encuentre bien! Noté con gran interés que tu prestigiosa empresa...". Un buen prompt produce una frase que parece escrita por un humano apurado. Instrucciones que debes meterle:

```
Eres un SDR escribiendo la PRIMERA LÍNEA de un correo en frío.
DATO REAL de esta cuenta: {dato_scrapeado}

Escribe UNA sola frase, máximo 15 palabras, que:
- mencione ese dato concreto de forma casual
- suene a persona real, NO a marketing
- NO use: "espero que estés bien", "noté con interés", "prestigiosa",
  "en el dinámico mundo de", signos de exclamación, adjetivos vacíos
- si el dato no da para una frase natural, responde exactamente: SIN_DATO

Ejemplos del tono que quiero:
- "Vi que abrieron sede en Chapinero el mes pasado."
- "Me crucé con su post sobre food cost del martes."
```

Claves anti-robot en el prompt:
- **Límite de palabras duro** (12–15). La IA sin límite se explaya y suena artificial.
- **Lista negra de frases** ("espero que este correo…", "en el dinámico mundo de…"). Son las huellas dactilares del texto de IA.
- **Salida de escape `SIN_DATO`.** Si no hay materia prima buena, que la IA lo *diga* en vez de inventar. Luego filtras esas filas a una plantilla 1:many o las descartas.
- **Ejemplos de tono (few-shot).** Dos ejemplos del estilo exacto valen más que diez adjetivos describiéndolo.

Para bajar el costo de correr esta IA sobre miles de filas (caching, batching, elegir modelo barato para la extracción y uno bueno solo para la redacción) → `optimizer_tokens_lushows`.

## Ejemplo real (fila de Clay → correo final)

```
FILA (prospecto):
  empresa: "Cafetería La Esquina"
  rol: dueño
  señal_scrapeada (Google Reviews): "4.9 estrellas, 340 reseñas,
    varias mencionan 'porciones generosas' y 'precios que subieron'"

IA extrae el dato: "reseñas elogian porciones pero notan alza de precios"
IA redacta {observacion}:
  "Vi en sus reseñas que la gente ama las porciones pero notó el alza de precios."

CORREO FINAL (plantilla de 52 + observación):
  Hola Andrés,

  Vi en sus reseñas que la gente ama las porciones pero notó el alza de precios.

  Cuando el costo de los insumos sube, subir el menú a ojo espanta clientes;
  saber el costo exacto de cada plato deja ajustar sin perder margen ni gente.
  Ayudamos a cafeterías a tener ese número en minutos.

  ¿Le hace sentido que le muestre cómo?
  — Luis
```

La observación es única y verdadera; el resto es plantilla. Eso es 1:1 a escala.

## Errores comunes (qué NO hacer)

- **Dejar que la IA invente el dato.** Sin fuente real, alucina. Verifica o usa `SIN_DATO`.
- **Personalizar todo el correo con IA.** El cuerpo probado convierte; no dejes que la IA lo reescriba cada vez. Solo la línea 1.
- **No revisar una muestra.** Antes de mandar 2.000, lee 30 líneas generadas a mano. Si 1 de cada 10 es rara o falsa, ajusta el prompt.
- **Personalización de vanidad automatizada** (ver `52`): "vi que estudiaste en la Nacional" — irrelevante, suena a stalkeo. El dato debe conectar con TU problema.
- **Ignorar deliverability.** Aunque el copy sea perfecto, si no cuidas volumen y warmup (ver `43`, `44`) igual caes en spam. La IA no arregla una infraestructura mala.

## Siguiente paso

Arma en Clay una tabla de 50 filas de tu segmento, engánchale UNA señal (ej. reseñas de Google) y una columna IA con el prompt de arriba. Lee las 50 líneas a mano y afina el prompt hasta que 9 de 10 pasen. La mecánica completa de Clay → `31`; el panorama de IA en outbound 2026 → `35`; qué personalizar y los niveles 1:1/1:few/1:many → `52`; redactar el opener a fondo → `53`. Convencer/cerrar en la conversación que se abre → eso ya es `ventas_lushows`.

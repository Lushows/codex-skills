# 164 — Personalización profunda enterprise (research serio por cuenta)

En volumen personalizas a escala con variables y una línea investigada (ver `52`). En ABM Tier A eso no alcanza: le escribes a pocas empresas que valen mucho, así que inviertes **research serio por cuenta** —leer sus reportes, su prensa, sus iniciativas públicas— para escribir un mensaje que solo tiene sentido para ESA empresa. Este módulo es dónde buscar, qué buscar y cómo convertir el research en un ángulo que abre la puerta. La diferencia entre "personalizar" (meter `{empresa}` en la plantilla) y **investigar** (referenciar una iniciativa real de la cuenta) es la diferencia entre un correo ignorado y una reunión.

## El principio: relevancia > halago

Personalización profunda no es escribir "vi que trabajas en {empresa}, ¡qué gran empresa!". Eso es ruido. Es demostrar que **entiendes un movimiento concreto de la cuenta y conectas tu solución con la consecuencia de ese movimiento**. El decisor enterprise recibe decenas de correos; solo abre conversación con quien parece ya entender su mundo. El research te compra ese "este sí sabe de qué habla". Regla: cada correo Tier A debe contener **una observación que no podrías haber escrito sobre ninguna otra empresa**.

## Dónde investigar (las fuentes, de más a menos jugosa)

| Fuente | Qué sacas | Dónde |
|---|---|---|
| **Reportes anuales / 10-K** (si cotiza) | Prioridades declaradas, riesgos, iniciativas, en qué van a gastar | SEC EDGAR, sección "inversionistas" de su web |
| **Earnings calls / presentaciones** | Qué le dice el CEO al mercado; palabras que repiten | Seeking Alpha, YouTube, IR deck |
| **Prensa y noticias** | Expansión, adquisición, nuevo ejecutivo, ronda, nueva línea | Google News, Crunchbase, medios sectoriales |
| **LinkedIn de la empresa** | Contrataciones (señal de crecimiento/dolor), posts, foco | Sales Nav (`26`), página de la empresa |
| **LinkedIn del contacto** | Su trayectoria, sus posts, qué le importa, en qué habla | Perfil del contacto |
| **Ofertas de empleo** | Qué están construyendo/dónde les duele (contratan por dolor) | Su página de empleo, LinkedIn Jobs |
| **Reseñas** (G2, Glassdoor, reviews de clientes) | Qué les critican los clientes/empleados = tu ángulo | G2, Glassdoor |
| **Web / changelog / blog** | Lanzamientos, cambios de estrategia, tono | Su sitio |

**En LatAm y empresas privadas** (sin 10-K): apóyate más en prensa sectorial, LinkedIn, ofertas de empleo, cámaras/gremios y el perfil del contacto. La señal está; hay que rascar más.

## De research a ángulo (cómo se convierte en mensaje)

El research crudo no sirve; tienes que destilarlo en **un ángulo**: iniciativa de la cuenta → consecuencia para el área del contacto → cómo tú ayudas justo ahí.

1. **Encuentra el "evento" o prioridad** (expansión, nueva planta, meta pública, contratación masiva, adquisición). Señales tipo trigger en `14` y `37`.
2. **Traduce a consecuencia operativa** para el rol al que escribes: "abren 3 sedes nuevas" → "operaciones va a tener que estandarizar costos entre sedes".
3. **Conecta con tu resultado**, idealmente con un caso comparable en su sector (prueba social `18`, displacement `19`).
4. **Cierra con un CTA suave** (ver `55`). La conversación profunda y el cierre → **`ventas_lushows`**.

Plantilla de destilado (una línea por cuenta):
```
[Iniciativa real]  →  [Consecuencia para el área de {contacto}]  →  [Cómo ayudo + caso]
Ej: "abren operación en México"  →  "control de costos multi-país se vuelve un dolor"
    →  "montamos eso para {competidor comparable} en 6 semanas"
```

## Ejemplo: correo Tier A con research real

```
Asunto: expansión a México + costos entre sedes

Hola Andrea, vi que {Empresa} anunció la apertura de su primera
operación en México este trimestre. Cuando una cadena pasa de
operar en un país a dos, el control de costos por sede casi
siempre se desordena los primeros meses —recetas, mermas y
precios dejan de ser comparables entre países.

Ayudamos a {Cadena comparable} justo en ese salto: estandarizaron
costeo entre sus sedes de CO y MX y recortaron X% de merma en el
primer trimestre. Estoy hablando también con {rol} de tu equipo,
porque esto los toca a ambos.

¿Tiene sentido una llamada de 20 min esta semana para mostrarte cómo?
```

Ese correo **no funciona para ninguna otra empresa**: eso es personalización profunda.

## IA para escalar el research (con cuidado)

La IA (ver `35`) acelera el research pero no lo reemplaza en Tier A:
- **Úsala para:** resumir un reporte largo, extraer las 3 prioridades de un earnings call, encontrar noticias recientes, redactar borradores de ángulo. Clay (`31`, `101`) + un LLM puede enriquecer decenas de cuentas 1:few con una línea investigada.
- **NO la uses para:** disparar "personalización" genérica que suena a IA. En Tier A, un humano valida y afina cada ángulo. Un correo "personalizado por IA" mal hecho es peor que uno honesto y simple.
- El punto de equilibrio volumen/profundidad está en `66`; en Tier A siempre gana profundidad.

## Errores comunes (qué NO hacer)

- **Halago vacío** ("gran empresa", "admiro su trabajo"): no es research, es relleno.
- **Research que no lleva a nada:** mencionas un dato curioso pero no lo conectas con su dolor ni con tu valor. El dato debe pagar.
- **Dato viejo:** referenciar una noticia de hace dos años te hace ver desactualizado. Usa lo reciente.
- **Mismo ángulo para toda la cuenta:** el ángulo se ajusta por rol también (usuario vs decisor; ver `162`).
- **IA sin revisión humana en Tier A:** suena a plantilla y quema la cuenta.

## Frontera y siguiente paso

El research te da el ángulo para **abrir**. Usar ese contexto en la **conversación de descubrimiento, profundizar el dolor y cerrar** es venta consultiva → **`ventas_lushows`**. Números del caso de negocio exactos → `Matematicas_lushows`.

**Siguiente paso:** por cada cuenta Tier A, dedica 15–30 min a las fuentes de arriba, destila **una línea de ángulo** y úsala en el multi-threading (`162`). Escala el research 1:few con Clay + IA en `31`/`35`, y coordina con el aire de marketing en `163`.

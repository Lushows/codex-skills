# 120 — Panorama de la IA de video (agosto 2026): quién hace qué y cuál te sirve

## Lo primero: esto caduca

Este módulo tiene fecha. Está escrito el **4 de agosto de 2026** y describe un mercado que en los
últimos doce meses cambió de líder cuatro veces. Si lo estás leyendo mucho después, úsalo como mapa
de categorías, no como catálogo de precios.

Regla de higiene: **antes de recomendarle un modelo a alguien, verifica que siga existiendo y que
siga costando lo que crees.** En 2026 ya se murió un modelo grande (Sora 2 quedó deprecado en abril)
y apareció uno anónimo que subió al #1 y desapareció en 72 horas (HappyHorse).

---

## El estado del mercado en una frase

Lo que en 2024 eran dos o tres modelos usables hoy son una docena de modelos de frontera, el **audio
sincronizado nativo dejó de ser un lujo** y la diferencia de calidad entre un plan de consumidor de
$10 al mes y una API empresarial se estrechó mucho.

Eso significa algo incómodo para el que vende edición: **la generación ya no es el diferencial**.
Cualquiera genera un plano bonito. El diferencial es el montaje, el ritmo, la marca y el criterio.
La IA te da materia prima; el editor sigue siendo el que decide.

---

## Los jugadores, por familia

### Google — Veo 3.1 (y la familia Gemini/Lyria alrededor)

- **Qué es**: el modelo de Google, disponible por Vertex AI (`veo-3.1-generate-001` y variantes),
  por la API de Gemini, y por la interfaz Flow.
- **En qué es el mejor**: **diálogo y audio**. Veo genera voz sincronizada a 48 kHz y es, con
  diferencia, el que mejor hace hablar a alguien sin que suene a robot enlatado. También es el más
  "cinematográfico" de fábrica: entiende lenguaje de cámara (dolly, plano contrapicado, 35 mm) sin
  que tengas que rogarle.
- **En qué falla**: deriva de color y de estilo (ver módulo `125`), y tiene una trampa de parámetros
  que rechaza peticiones sin decirte por qué (ver módulo `121`).
- **Precio (Vertex, ago-2026)**: aproximadamente **$0.03–$0.05/segundo** en la variante Lite sin
  audio, **~$0.10/s** en Fast a 720p, y **~$0.40/s** en la estándar con audio a 720p/1080p. 4K sale
  más caro (rango citado $0.30–$0.60/s). Un clip de 8 segundos con audio en la variante buena ronda
  los **$6 USD**. Verifica siempre en la página oficial de precios de Vertex: estos números se
  mueven.
- **Cuándo lo eliges**: cuando el plano lleva voz, cuando necesitas control de cámara, o cuando ya
  estás dentro de Google Cloud y no quieres abrir otra cuenta.

### ByteDance — Seedance 2.0

- **Qué es**: reconstrucción total de Seedance, lanzada en febrero de 2026. Arquitectura de doble
  rama (una genera video, otra genera audio, y se cruzan a nivel de milisegundo).
- **En qué es el mejor**: **control por referencia**. Es el más obediente cuando le pasas imágenes
  de referencia de personaje, producto o estilo, y el más predecible en ejecución de cámara. Para
  publicidad de producto eso vale oro.
- **Precio**: muy variable según revendedor. Se ven cifras desde **~$0.022/s** en tiers rápidos hasta
  **$0.06–$0.08/s** en calidad normal, y hasta $0.50/s en tiers premium de algunos revendedores.
  Ojo: casi nadie lo vende directo; llegas por fal, OpenRouter, PiAPI y similares.
- **Cuándo lo eliges**: cuando tienes que mantener un producto o una cara igual entre planos.

### Alibaba — HappyHorse 1.0

- **Qué es**: apareció anónimo en el Video Arena de Artificial Analysis el 7 de abril de 2026, se
  puso #1 y desapareció a las 72 horas. Alibaba admitió que era suyo semanas después y abrió API por
  fal el 27 de abril.
- **En qué es el mejor**: **calidad visual pura** por Elo. Si solo miras qué tan bonito se ve un
  plano suelto, gana.
- **En qué falla**: ecosistema joven, menos control de dirección, y una historia de disponibilidad
  errática que no me deja recomendártelo para un cliente con fecha de entrega.
- **Cuándo lo eliges**: pieza de portafolio, plano hero, algo donde la belleza importa más que el
  control.

### Kuaishou — Kling 3.0

- **Qué es**: el chino grande y barato. Versión 3.0 con lip sync multilingüe desde febrero de 2026.
- **En qué es el mejor**: **secuencias multi-plano con consistencia de sujeto**, y relación
  calidad/precio.
- **Precio**: el más disperso del mercado según por dónde entres. Se citan **$0.084/s** estándar y
  **$0.112/s** pro sin audio en fal; **~$0.20/s** para la modalidad multi-plano con audio nativo; y
  precios mucho más bajos en revendedores. Verifica antes de presupuestar.
- **Cuándo lo eliges**: volumen. Cuando tienes que generar 30 variantes de un anuncio y no puedes
  pagar Veo estándar 30 veces.

### Runway — Gen-4.5

- **Qué es**: el modelo dentro de una **suite de edición**, no un generador suelto.
- **Dónde está**: lideró el benchmark de texto→video a finales de 2025 con ~1247 Elo y ya se cayó
  del top 10 por calidad pura. Eso **no** lo vuelve inútil.
- **En qué es el mejor**: **control de producción**. Herramientas de expansión de plano, borrado de
  objetos, control de cámara, versionado, trabajo en equipo. Si tu problema es "necesito iterar 40
  veces con un cliente encima", Runway sigue siendo la opción más segura.
- **Cuándo lo eliges**: equipos, clientes, revisiones. No cuando quieres el plano más bonito posible.

### OpenAI — Sora 2 (⚠️ moribundo)

- **Estado a agosto de 2026**: **deprecado desde el 26 de abril de 2026**; la API se apaga el **24 de
  septiembre de 2026**.
- **Traducción práctica**: **no construyas nada nuevo sobre Sora 2.** Si tienes un flujo que depende
  de él, tienes semanas, no meses. Su precio además era el más alto del mercado (~$0.75/s en Sora 2
  Pro).
- Si OpenAI saca sucesor, verifícalo tú; a la fecha de este módulo no puedo confirmarte cuál es ni
  qué cuesta.

### Luma — Ray3

- **En qué es único**: **HDR nativo de 16 bits, exportable a EXR**. Es el único pensado para entrar
  a un pipeline de color profesional de verdad.
- **Cuándo lo eliges**: cuando el material generado va a convivir con material filmado y tiene que
  aguantar una gradación seria. Para un reel de Instagram es sobreingeniería.

### Pika

- **En qué es único**: **Pikaframes** — le das imagen inicial e imagen final y él genera la
  transición entre las dos (1 a 10 segundos).
- **Cuándo lo eliges**: puentes entre dos diseños fijos, morphs de producto, transiciones imposibles.
  Es la herramienta más barata del mercado para ese trabajo específico (~$8/mes de entrada).

### Higgsfield

- **Qué es**: **no es un modelo, es un mostrador.** Por dentro te da acceso a Veo 3, Runway Gen-4.5,
  Luma Ray3 y Kling 3.0 con una sola suscripción y un pozo de créditos.
- **Precios (anual)**: ~$15/mes Starter (~200 créditos), ~$39/mes Plus (~1.000), ~$99/mes Ultra
  (~3.000).
- **Cuándo lo eliges**: cuando quieres probar cuatro modelos sin abrir cuatro cuentas y sin meter
  tarjeta en Google Cloud. Cuando ya sabes cuál usas, sale más barato ir directo a la API.

### SkyReels V4

Aparece en el top del arena (#3 en algunos cortes de 2026). No lo he verificado en producción; si un
cliente te lo menciona, dile la verdad: está bien rankeado y no tienes pruebas propias.

---

## La tabla de decisión (la que de verdad usas)

| Lo que necesitas | Modelo | Por qué |
|---|---|---|
| Alguien hablando a cámara, con voz | **Veo 3.1** | Nadie más hace diálogo así de bien |
| Mantener un producto idéntico en 5 planos | **Seedance 2.0** | Control por referencia |
| 30 variantes baratas para testear pauta | **Kling 3.0** | Precio por segundo |
| Iterar con cliente, borrar objetos, versionar | **Runway Gen-4.5** | Es una suite, no un modelo |
| El plano más bonito que exista, sin control | **HappyHorse 1.0** | Elo más alto |
| Que aguante gradación junto a material real | **Luma Ray3** | HDR 16 bits / EXR |
| Transición entre dos imágenes que ya tienes | **Pika (Pikaframes)** | Hace exactamente eso |
| Probar todos sin abrir 4 cuentas | **Higgsfield** | Agregador |
| Nada nuevo | ~~Sora 2~~ | Deprecado, se apaga en septiembre |

---

## Tres verdades incómodas del mercado

**1. Los benchmarks miden lo que a ti no te importa.**
El Elo del Video Arena mide "cuál de estos dos clips sueltos te gusta más". Tu trabajo no es un clip
suelto: es que el plano 3 pegue con el plano 4, que el color sea el de la marca y que el producto
sea el producto. Un modelo #4 en Elo con buen control de referencia te sirve más que el #1.

**2. El precio publicado casi nunca es el precio real.**
Entre "$0.05/s" y tu factura hay: intentos fallidos, variantes descartadas, resolución, audio sí o
no, y el hecho de que casi todo se cobra por segundo **generado**, no por segundo **usado**. Si
generas 8 segundos y usas 2, pagaste 8. Ver módulo `127`.

**3. Cambiar de modelo cuesta más de lo que parece.**
Cada modelo tiene su dialecto de prompt, sus parámetros y sus manías. Cambiar de proveedor a mitad
de un proyecto te obliga a re-tunear todo. Elige uno por proyecto y quédate ahí.

---

## Cómo verificar tú mismo, en 10 minutos

1. **Página oficial de precios del proveedor.** No un blog. Los blogs de "precios 2026" copian entre
   ellos y arrastran errores meses.
2. **Artificial Analysis** (`artificialanalysis.ai/video`) para calidad comparada. Es la referencia
   menos sesgada disponible.
3. **La documentación del modelo**, sección de parámetros. Ahí está lo que de verdad puedes pedirle.
4. **Una prueba propia de 3 clips.** El único dato que vale es el tuyo. Genera el mismo prompt en dos
   modelos y compara. Cuesta menos de $2 y te ahorra una recomendación equivocada.

Y cuando no puedas verificar algo, dilo. "No sé cuánto cuesta hoy" es una respuesta profesional;
inventar un número no lo es.

---

## Errores comunes

- **Recomendar un modelo por su Elo.** El Elo mide belleza de plano suelto. Tu trabajo es
  continuidad, marca y control. Son cosas distintas.
- **Construir sobre un modelo deprecado.** Sora 2 se apaga el 24 de septiembre de 2026 y hay gente
  todavía escribiendo tutoriales de Sora 2 como si nada.
- **Citar precios de blogs.** La mitad de los "precios agosto 2026" que circulan son copias de
  enero. Ve a la página del proveedor.
- **Creer que "tiene audio nativo" resuelve el audio.** El audio nativo te da referencia y ambiente.
  La música, la voz limpia y el diseño sonoro los sigues haciendo tú.
- **Usar el modelo más caro para todo.** El 80% de tus planos son b-roll de 2 segundos que nadie
  mira fijo. Ese b-roll no necesita Veo estándar con audio a $0.40/s.
- **Suscribirte a un agregador y a tres APIs.** O usas el agregador para explorar, o usas la API para
  producir. Las dos al tiempo es quemar plata.
- **Confundir "modelo" con "producto".** Higgsfield no es un modelo. Runway es más producto que
  modelo. Confundirlos hace que compares peras con el supermercado.
- **Prometerle a un cliente un modelo que no has probado.** Especialmente HappyHorse, que ya
  desapareció una vez.

---

## Checklist

- [ ] Verifiqué en la página **oficial** del proveedor que el modelo existe hoy y a qué precio
- [ ] Confirmé que el modelo **no está deprecado** ni con fecha de apagado cercana
- [ ] Elegí el modelo por **el trabajo que tiene que hacer** (diálogo / referencia / volumen /
      iteración), no por su puesto en un ranking
- [ ] Sé si el plano necesita **audio nativo** o no (cambia el precio 3× o más)
- [ ] Calculé el costo con **intentos fallidos incluidos**, no solo el clip final
- [ ] Elegí **un solo modelo** para este proyecto y no voy a cambiar a mitad de camino
- [ ] Hice **una prueba propia** antes de recomendarlo o presupuestarlo
- [ ] Si el material va a mezclarse con video filmado, verifiqué que el formato de salida aguante
      la gradación
- [ ] Le dije al cliente **qué no puedo verificar**, en vez de rellenar con datos inventados

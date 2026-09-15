# 89 — Playbook apps

Lee este módulo cuando promocionas una **app móvil** (Android/iOS) y quieres instalaciones o, mejor, **usuarios que hagan algo de valor dentro de la app** (compren, se suscriban, completen un registro). Las apps tienen su propio tipo de campaña en Google — **App campaigns** (antes UAC, hoy también llamadas AC, App Campaigns) — que funciona muy distinto a Search: das pocos insumos y Google decide TODO (dónde mostrar, a quién, qué creativo). Eso lo hace fácil de lanzar y difícil de controlar. Aquí Google **captura** intención (busca tu app en Play Store, busca "app de X") Y genera alcance en sus redes. Antes de pautar: la pregunta más honesta es **¿de verdad necesitas pautar una app, o estás quemando plata?** (lo respondo abajo). La viabilidad del modelo y el LTV: `economist_lushows`. El producto que retiene (sin retención, ningún ads salva): es trabajo de producto, no de pauta.

## App campaigns (UAC/AC): cómo funcionan de verdad

App campaigns son **casi totalmente automatizadas**. No eliges keywords, ni pujas por red, ni segmentas como en Search. Le das insumos y Google optimiza a través de **todas sus superficies**: Búsqueda, Play Store, YouTube, Display, Discover.

**Lo que TÚ controlas (los únicos insumos):**

| Insumo | Detalle |
|---|---|
| **Objetivo** | Instalaciones, o acciones in-app (más valioso) |
| **Puja** | tCPI (costo por instalación) o tCPA/tROAS de acción in-app |
| **Presupuesto** | Diario |
| **Geo / idioma** | Dónde |
| **Assets** | Textos, imágenes, **videos**, HTML — Google los combina |

- **Los assets son tu única palanca creativa.** Google arma anuncios combinando tus textos, imágenes y videos. **Dale variedad y dale VIDEO** — gran parte del inventario (YouTube) necesita video; sin video, te limitas a Display y Search y pierdes alcance. Sube varios de cada tipo, distintos ángulos (problema/solución, demo de pantalla, testimonio, social proof). El brief creativo → `directorcreativo_lushows`.
- **No esperes control fino.** No verás "cuánto vino de YouTube vs Search" con detalle ni podrás excluir mucho. Aceptas la caja negra a cambio de simplicidad y alcance. Es la campaña más automatizada de todo Google, en línea con la dirección 2026 de "todo a IA" (ver actualizacion-2026-06).

## Optimizar a eventos in-app, no a instalaciones

El error #1 en apps: optimizar a **instalaciones**. Una instalación NO es valor — la mitad de la gente instala, abre una vez y nunca vuelve. Si optimizas a tCPI (costo por instalación), Google te trae instaladores baratos y basura.

**Optimiza a la acción que SÍ vale (ver 53 OCI/eventos):**

| Objetivo | Cuándo usarlo | Riesgo |
|---|---|---|
| **Instalaciones (tCPI)** | App nueva, aún sin datos de eventos | Trae instalaciones que no usan la app |
| **Acción in-app (tCPA)** | Cuando ya mides eventos (registro, compra) | El bueno: optimiza a usuarios reales |
| **Valor in-app (tROAS)** | E-commerce/suscripción en app | El mejor: optimiza a ingreso |

- **Necesitas medir eventos in-app** para esto: integra una herramienta de atribución móvil (Firebase, AppsFlyer, Adjust) que le diga a Google cuándo alguien se registró, compró o se suscribió. Sin esa medición, estás ciego y solo puedes optimizar a instalaciones (lo malo).
- **Define el evento de valor real:** no "abrió la app" sino "completó registro", "hizo primera compra", "se suscribió". Optimiza a ESE.
- **Periodo de aprendizaje:** App campaigns necesitan datos. Si optimizas a un evento que pasa pocas veces, dale presupuesto suficiente para que Google aprenda (regla práctica: el evento debería ocurrir decenas de veces por semana), o arranca con instalaciones y migra a evento cuando tengas volumen.
- **iOS y privacidad (ATT/SKAdNetwork):** en iOS la señal post-ATT es modelada y más demorada; espera ventanas de atribución más cortas y menos granularidad que en Android. No compares iOS y Android con la misma vara, y separa campañas por sistema operativo para presupuestar bien.

**ASO antes que ads.** La ficha de Play Store / App Store (título, ícono, capturas, descripción, reseñas) es el "landing" de tu app: si está pobre, pagas el clic y el usuario no instala. Optimízala ANTES de pautar — es gratis y multiplica la conversión de todo el tráfico pago. App campaigns también rotan elementos de la ficha, así que una ficha fuerte sube el rendimiento de la campaña entera. Reseñas y calificación pesan tanto aquí como en un negocio local (ver 81 para la lógica de reseñas).

## Retención: el agujero por donde se va la plata

Antes de subir un peso de presupuesto, mírate la **retención** (cuánta gente vuelve al día 1, 7, 30). Si tu D7 es 5%, estás pagando por instalar un balde con hueco: por más barato que sea el tCPI, el usuario se va y no monetiza. Google puede traerte instalaciones todo el día, pero no puede arreglar una app que no engancha — eso es producto. La secuencia honesta es: primero retención decente, luego monetización medible, luego ads para escalar lo que YA funciona. Pautar para "crecer" una app que no retiene es la forma más cara de descubrir que el producto no estaba listo (la viabilidad de esto es `economist_lushows`).

## ¿Google SÍ para tu app? La pregunta honesta

No toda app debe pautar en Google. Sé honesto antes de gastar:

**Google SÍ tiene sentido cuando:**
- La app **monetiza de verdad** (compras, suscripción, ads) y conoces el **LTV** del usuario — solo así sabes cuánto puedes pagar por instalación/acción.
- Hay **demanda de búsqueda**: la gente busca "app de [tu categoría]" o tu app por nombre.
- Tienes **medición de eventos in-app** lista (Firebase/AppsFlyer). Sin esto, no pautes aún.

**Google NO (o todavía no) cuando:**
- App nueva sin monetización clara — pagar por instalaciones que no generan ingreso es quemar plata. Primero valida que la app retiene y monetiza (eso es producto + `economist_lushows`).
- No tienes medición de eventos — estarías optimizando a ciegas a instalaciones basura.
- Tu crecimiento real es orgánico/viral o por otro canal más barato (en muchas apps de consumo joven, TikTok orgánico + Meta mueven más barato que Google — ver `tiktok_ads_lushows`, `facebook_ads_lushows`).

**Presupuesto:** calcula tu **tCPI o tCPA máximo desde el LTV**. Si un usuario que se suscribe te deja $30.000 de valor y conviertes 1 de cada 10 instalaciones en suscriptor, tu instalación puede valer hasta ~$3.000 antes de perder (y menos si quieres ganar). Ese cálculo manda tu puja — no lo saques de "se siente bien" (ver 60, 64, `economist_lushows`). Benchmark COP de referencia: tCPI en Colombia puede ir de unos cientos a $2.000+ según categoría; el tCPA de evento real (suscripción/compra) es bastante más alto y es el número que de verdad importa.

## Errores comunes — blacklist

1. **Optimizar a instalaciones.** Traes gente que instala, abre una vez y se va. Optimiza a evento in-app de valor (registro, compra) — ver 53.
2. **Pautar sin medición de eventos.** Sin Firebase/AppsFlyer estás ciego y solo puedes optimizar a instalaciones basura. Integra la atribución primero.
3. **Subir pocos assets / sin video.** Google necesita variedad y video para todo su inventario (YouTube). Sin video pierdes alcance. Sube varios ángulos.
4. **Pautar una app que no monetiza/retiene.** Pagar instalaciones sin LTV claro es quemar plata. Valida producto antes (ver `economist_lushows`).
5. **No calcular el tCPI/tCPA máximo desde el LTV.** Sin saber cuánto vale un usuario, no sabes cuánto puedes pagar. Calcula desde el ingreso (ver 64).
6. **Esperar control fino.** App campaigns son caja negra; no podrás segmentar/excluir como en Search. Acéptalo o usa otro tipo (ver 11).
7. **Migrar a evento raro sin volumen.** Optimizar a un evento que pasa poquísimo deja a Google sin datos. Dale presupuesto o arranca con instalaciones y migra (ver 13).
8. **Comparar iOS y Android con la misma vara.** Post-ATT la señal de iOS es modelada y demorada; no esperes la misma granularidad ni atribución que en Android.

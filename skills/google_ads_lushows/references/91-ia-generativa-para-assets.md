# 91 — IA generativa para assets

Lee este módulo cuando vas a usar las herramientas de IA de Google para crear titulares, descripciones, imágenes o video de tus anuncios, cuando un cliente te pida "hazlo rápido con la IA", o cuando un PMax/Demand Gen te esté **autogenerando** creativos sin que tú lo hayas pedido. Google integró **Gemini** (su modelo de IA) dentro de Google Ads: genera texto, imágenes y hasta **image-to-video** (convierte una foto en un clip corto) para Demand Gen y YouTube (ver 41, 42). Es una palanca de velocidad real. También es la forma más fácil de poner en la calle un anuncio genérico que daña tu marca y te mete en problemas de política. Marco: Google **captura intención**; la IA solo te ayuda a producir el envase del mensaje, no la estrategia ni la marca.

## Qué genera Gemini dentro de Google Ads (2026)

| Tipo de asset | Qué hace la IA | Dónde aparece |
|---|---|---|
| **Texto** (titulares, descripciones) | Escribe variantes desde tu landing/keywords; reescribe assets en AI Max | RSA (ver 31), PMax, AI Max (ver 90) |
| **Imágenes** | Crea/edita fondos, amplía encuadre (outpainting), quita objetos, genera variantes de formato | PMax, Demand Gen, Display |
| **Image-to-video** | Anima una foto fija en un clip de pocos segundos | Demand Gen, YouTube (ver 42) |
| **Asset enhancements** (mejoras automáticas) | "Mejora" tus titulares/imágenes en tiempo de subasta si lo dejas activo | Search, PMax — revisa si quieres ese control |
| **Autogeneración silenciosa** | Si NO subes video/imagen, PMax y Demand Gen crean uno solos | Cuando dejas assets vacíos |

La autogeneración silenciosa es la trampa: si lanzas un PMax sin subir tu propio video, Google **rellena el hueco** con uno feo armado de tus imágenes. No es una opción que activaste; es lo que pasa por defecto cuando no haces tu trabajo creativo. Lo mismo "asset enhancements": viene activo y puede reescribir tu titular — revísalo en la configuración de la campaña y desactívalo si quieres firmar tú cada palabra.

## Disclosure, política y lo que te suspende

Hay reglas que no son opcionales (ver 08, 93):

- **Verificación de anunciante obligatoria**: Google exige verificar tu identidad/negocio para correr anuncios. Sin esto, ni la IA te salva (ver 93). Hazla el día 1.
- **Contenido sensible y temas regulados** (política, salud, finanzas, apuestas): aplican reglas de divulgación más duras; la IA no te exime de cumplirlas.
- **No inventar claims**: la IA, generando texto, tiende a meter superlativos ("el #1", "garantizado", "resultados en 7 días", "100% efectivo"). Eso es **misrepresentation** (tergiversación) y te puede costar la cuenta entera (ver 93). TÚ eres responsable de lo que la IA escribió, no Google.
- **Imágenes de personas/marcas que no son tuyas**: no dejes que la IA genere caras realistas usadas como "cliente real" ni logos ajenos. Riesgo legal y de política. Para contenido sensible, Google puede exigir divulgación de "contenido alterado/sintético".

Regla de oro: **la IA redacta borradores; tú firmas lo que sale.** Lee cada asset antes de aprobarlo como si lo hubieras escrito tú (porque ante Google, así es).

## Control de calidad: lo que se nota y daña marca

La IA generativa de Google es rápida, no es buena directora de arte. Lo que delata un anuncio "hecho con IA sin curaduría":

| Señal de baja calidad | Por qué daña | Qué hacer |
|---|---|---|
| Imagen con manos/texto deformes, objetos derretidos | Grita "fake", baja confianza | Descártala, no la publiques |
| Titular genérico ("La mejor solución para ti") | Indistinguible de cualquier competidor | Reescribe con tu propuesta real (ver 30) |
| Video image-to-video con movimiento robótico | Se siente barato, contradice marca premium | Solo úsalo para tests, no como hero |
| Colores/tipografía fuera de tu identidad | Rompe coherencia de marca | Pásalo por `directorcreativo_lushows` |
| Texto sobre-prometedor | Riesgo de suspensión + desconfianza | Bórralo; usa solo lo que puedas probar |
| Mismo asset para toda LatAm | Ignora modismos/moneda locales | Localiza por país (ver 47) |

**Flujo sano para usar la IA sin quemarte:**
1. **Genera 5–10 variantes** de texto con Gemini para no partir de cero.
2. **Filtra a mano**: borra las genéricas, las con claims, las que no suenan a ti.
3. **Edita las 2–3 buenas** para que digan tu propuesta real, no la plantilla. Mete precio en COP, ciudad, beneficio concreto.
4. **Imágenes/video**: úsalos para *probar* ángulos baratos. El creativo que va a escalar y representar la marca lo diriges con criterio (rutea a `directorcreativo_lushows`); el video bueno de verdad casi nunca es el autogenerado.
5. **Mide**: deja correr, mira qué asset rinde (ver 60) y mata los flojos.

Para e-commerce LatAm con presupuesto chico, la IA de Google sirve para **producir volumen de variantes de texto barato** y tapar huecos, no para reemplazar una buena foto de producto ni un video con guion. La lógica de "volumen creativo gana en la subasta de IA" es la misma que en `facebook_ads_lushows` (era Andromeda/creative volume) — pero volumen de basura sigue siendo basura.

## Plantilla: prompt para que Gemini (o cualquier LLM) te dé buenos titulares

> "Eres copywriter de respuesta directa para Google Search en Colombia. Producto: [qué es, precio en COP, para quién]. Propuesta única: [diferencial real]. Escribe 10 titulares de máx 30 caracteres y 4 descripciones de máx 90, en español neutro-colombiano, SIN claims que no pueda probar (nada de 'garantizado', '#1', '100%'). Incluye al menos 3 con intención comercial (precio, comprar, cotizar) y 2 con la ciudad/país. Tono: claro, directo, sin relleno."

Eso te da material que filtras a mano. Si vas a generar a escala (decenas de cuentas/clientes) y el gasto en tokens de TU propio LLM se sube, ese es otro problema: rutea a `optimizer_tokens_lushows` para bajar el costo de la IA de tu stack sin perder calidad (caching, batch, routing). Dentro de Google Ads la generación no te cuesta tokens aparte; pagas el clic igual.

## Decisión rápida: cuándo usar IA generativa y cuándo no

| Necesidad | ¿IA de Google? | Qué hacer |
|---|---|---|
| Llenar 15 titulares de un RSA para que el algoritmo combine | Sí, con curaduría | Genera, filtra, edita los buenos (ver 31) |
| Tapar el hueco de assets en PMax para que no autogenere | Sí | Sube los tuyos; genera variantes de texto, no el hero visual |
| Foto de producto que va a escalar y representar marca | NO | Foto real / dirección de arte (`directorcreativo_lushows`) |
| Video hero de una campaña importante | NO | Guion + producción (ver 42; arte → `directorcreativo_lushows`) |
| Localizar copy por país (CO/MX/PE) | Sí, con revisión humana | Genera por mercado, revisa modismos y moneda (ver 47) |
| Claim de eficacia/resultado | NUNCA inventado | Solo lo que puedas probar; si no, no va (ver 93) |

La regla de fondo: la IA es para **volumen y velocidad de borradores**, no para las dos cosas que sostienen un negocio — la identidad visual y la verdad de los claims. Esas se curan a mano, siempre.

## Errores comunes — blacklist

- **Publicar lo que la IA escribió sin leerlo.** Tú eres responsable de los claims; un "garantizado" inventado te suspende (ver 93).
- **Dejar que PMax/Demand Gen autogenere el video por no subir el tuyo.** Sale uno feo que daña marca; súbelo tú (ver 90, 42).
- **No revisar "asset enhancements" / mejoras automáticas.** Vienen activas y reescriben tu titular sin avisar; decide si quieres ese control (ver 31).
- **Usar imágenes IA con artefactos visibles** (manos raras, texto deforme). Gritan "fake" y bajan la confianza; descártalas.
- **Tratar la IA como director de arte.** Genera borradores, no identidad. Lo que escala se cura a mano (rutea a `directorcreativo_lushows`).
- **Generar caras/personas realistas como "clientes reales".** Riesgo legal y de política; no lo hagas.
- **Saltarse la verificación de anunciante** creyendo que la IA acelera todo. Sin verificación no corres nada (ver 93).
- **Confundir velocidad con calidad.** Producir 50 anuncios genéricos en una tarde no es ventaja si ninguno vende ni se distingue del competidor.

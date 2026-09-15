# 48 — Congruencia ad→landing/Shop

Lee este módulo cuando tu anuncio tiene buen CTR (la gente hace clic) pero la conversión en la landing o en el Shop es un desastre — porque el problema casi nunca es el anuncio, es el SALTO entre lo que prometió el video y lo que encuentra la persona al hacer clic. Eso se llama **message match** (congruencia de mensaje): que la landing/Shop continúe la misma promesa, el mismo tono y la misma oferta del anuncio. En TikTok, donde el usuario está scrolleando rápido y desconfiado, **el scroll no perdona el salto de mensaje**: si el video dice una cosa y la landing dice otra, se va en 2 segundos.

La congruencia es la costura invisible entre la pauta y la venta. Un anuncio brillante que manda a una landing genérica, lenta o que habla de otra cosa quema tu plata: pagaste el clic y lo perdiste en la llegada. La regla: **la primera pantalla de la landing debe sentirse como la continuación del video**, no como un sitio web distinto.

## Qué debe coincidir (el checklist de message match)

| Elemento | En el anuncio | En la landing/Shop debe… |
|---|---|---|
| **Promesa principal** | "Sabe cuánto te deja cada plato en 5 min" | Repetir esa misma promesa en el título, no otra |
| **Oferta** | "$10.000, incluye plantillas + tutorial" | Mostrar exactamente esa oferta y precio (ver 41) |
| **Visual / tono** | Estética del video, colores, vibra | Continuar el mismo look, mismo frame del video si se puede |
| **CTA** | "Escríbeme COSTOS" / "Compra ahora" | Ofrecer ese mismo paso, sin pasos extra sorpresa |
| **Idioma / registro** | Colombiano / neutro (ver 47) | Hablar igual, no cambiar a corporativo |
| **Moneda** | COP en Colombia | El mismo signo y cifra, no otra moneda (ver 47) |

Si el video promete X y la landing entrega Y, la persona siente que la engañaron y se va. La congruencia no es estética: es confianza. Truco 2026 que sube conversión: usa el MISMO frame o clip del ad como hero de la landing — el cerebro reconoce "es de lo mismo" en menos de un segundo.

## El scroll no perdona — los 3 segundos de la landing

Igual que el video tiene 1-3s para enganchar (ver 37), la landing tiene ~3s para confirmar "sí, llegué al lugar correcto". En esos segundos la persona verifica inconscientemente:

1. **¿Es de lo mismo que vi?** (la promesa coincide) — si no, rebota.
2. **¿Carga rápido?** En móvil con datos, una landing lenta = abandono masivo. La velocidad es conversión.
3. **¿Veo el precio/oferta y cómo lo consigo?** Sin buscar, sin scroll infinito.

Si tu landing tarda 6 segundos en cargar en un celular gama media con datos de Claro o Tigo, perdiste a la mitad antes de que lean nada. En 2026 Google penaliza y los usuarios abandonan landings con LCP (Largest Contentful Paint) sobre ~2.5s; en móvil LatAm con red irregular esto es brutal. La construcción técnica de esa landing — velocidad, Core Web Vitals, claridad, CRO, que cargue rápido en móvil — NO es trabajo de la pauta. Rutea a **`desingweb-lushows`**: ahí se construye la landing rápida y congruente.

## Casos según destino

| Destino del clic | Riesgo de incongruencia | Cómo cuidarlo |
|---|---|---|
| **Landing propia** | El más común: landing genérica que no matchea | Landing dedicada a ESA oferta, hecha por `desingweb-lushows` |
| **TikTok Shop** (ver 50) | Ficha de producto con fotos/precio distintos al video | Ficha alineada al video: mismo precio, mismas fotos/promesa |
| **WhatsApp** | El mensaje inicial no retoma el anuncio | Mensaje de bienvenida que retome el gancho; cierre con `ventas_lushows` |
| **Perfil de TikTok** | El perfil no tiene el link visible ni explica nada | Bio clara con el link, contenido fijado coherente |
| **Instant Form (lead)** | Formulario largo que no se parece al ad | Formulario corto, con la misma promesa arriba |

Para el caso WhatsApp (muy común en Colombia): si el anuncio dice "escríbeme COSTOS", el primer mensaje del bot/persona debe reconocer eso — "¡Hola! Veo que vienes por la calculadora de costos 👇" — no un genérico "¿en qué te ayudo?". Si entra por la palabra clave, el bot debería arrancar ya con el contexto. Ese guion de bienvenida y cierre lo afina `ventas_lushows`.

## Congruencia visual: el "ad-to-page" en la práctica

Tres niveles, de mínimo a ideal:

1. **Mínimo**: el título de la landing = la promesa del ad, palabra por palabra. ("¿Sabes cuánto te deja cada plato?" en el video → mismo título arriba.)
2. **Bueno**: + mismos colores, mismo tono, el precio/oferta visible sin scroll.
3. **Ideal**: + el mismo clip/frame del ad como hero, el mismo creador o voz, mismo CTA. La persona ni siente que cambió de app.

## Una oferta = una landing

No mandes tres anuncios con tres ofertas distintas a la misma landing genérica. Cada ángulo/oferta importante merece su propia llegada congruente. Si testeas ángulos (ver 49), idealmente cada ángulo ganador tiene su landing que matchea. Esto multiplica conversión y además te deja medir limpio qué ángulo+landing funciona. Implementar varias variantes de landing rápido es trabajo de `desingweb-lushows`; decidir si vale la pena tantas variantes (esfuerzo vs retorno) es viabilidad con `economist_lushows`.

## Cómo diagnosticar dónde se rompe

Usa el embudo de métricas (ver 49, 68): CTR bueno + CVR malo = el hueco está DESPUÉS del clic, casi siempre congruencia o velocidad de la landing. Antes de tocar el creativo, abre tu propia landing desde un celular con datos móviles y hazte las 3 preguntas de arriba. Si tú dudas "¿esto es de lo mismo?", el usuario ya rebotó.

## Errores comunes — blacklist

- **Anuncio brillante → landing genérica.** Pagaste el clic y lo perdiste en la llegada. Fix: landing dedicada y congruente (`desingweb-lushows`).
- **Promesa del video ≠ título de la landing.** La persona siente engaño y rebota. Fix: repite la misma promesa arriba, palabra por palabra.
- **Precio/oferta distintos entre ad y landing/Shop.** Rompe la confianza. Fix: misma oferta exacta en ambos (ver 41).
- **Landing lenta en móvil con datos.** Abandono masivo antes de leer. Fix: velocidad/Core Web Vitals como prioridad (`desingweb-lushows`).
- **WhatsApp con bienvenida genérica.** "¿En qué te ayudo?" mata el contexto. Fix: mensaje que retome el anuncio (`ventas_lushows`).
- **Cambiar de tono colombiano a corporativo en la landing.** Se siente otro lugar. Fix: mismo registro y moneda (ver 47).
- **Tocar el creativo cuando el hueco está en la landing.** CTR bueno + CVR malo = revisa la llegada, no el video. Fix: diagnostica con el embudo (ver 49).
- **Una landing genérica para muchas ofertas.** Diluye y mide sucio. Fix: una oferta, una landing (ver 49).

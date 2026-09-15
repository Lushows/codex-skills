# 33 — Landing pages para Search

Lee este módulo cuando tus anuncios reciban clics pero nadie compre, te aparezca "experiencia de la página de destino: baja" en Google, o estés decidiendo a qué página mandar el tráfico de Search.

En Search pagas por el clic. Lo que pase después del clic decide si ese dinero se vuelve venta o se evapora. La landing (página de destino) es el último metro del embudo y el más descuidado: la gente pule el anuncio durante horas y manda el clic a una home genérica. Aquí está el punto clave que casi nadie entiende: **una buena landing sube DOS cosas al mismo tiempo** — tu Quality Score (te abarata el CPC, ver 36) Y tu tasa de conversión (CVR, vendes más con el mismo tráfico). Es la única palanca que mejora costo y resultado a la vez. Si tuvieras que elegir una sola cosa que arreglar en una cuenta que sangra, sería esta antes que la puja.

Importante: este módulo es la ESTRATEGIA de la landing para Search. La construcción real (diseño, código, velocidad, animación, móvil) se hace en **`desingweb-lushows`**, que produce páginas premium y rápidas. Aquí defines qué debe cumplir; allá lo construyes. No intentes programar la landing desde aquí.

## Las 3 cosas que Google evalúa en la landing

Google califica la "experiencia de la página de destino" como uno de los 3 componentes del Quality Score (ver 36). Mira:

| Factor | Qué evalúa Google | Qué hacer |
|---|---|---|
| **Relevancia** | ¿la página trata de lo que el usuario buscó? | la keyword del grupo debe aparecer en el H1 y el texto |
| **Velocidad** | ¿carga rápido, sobre todo en móvil? | Core Web Vitals en verde (ver abajo) |
| **Transparencia/utilidad** | ¿es clara, navegable, sin trampas? | precio visible, sin pop-ups molestos, política de privacidad |

Una landing lenta o irrelevante baja tu Quality Score → subes el CPC → pagas más por cada clic. Google literalmente te cobra más por mandar gente a una página mala. No es castigo arbitrario: si tu página frustra al usuario, Google pierde confianza en mostrar tu anuncio, y te lo cobra.

### Velocidad: Core Web Vitals (en cristiano)

Son 3 métricas de Google que miden experiencia de carga. En 2026 estas son las que cuentan:
- **LCP** (Largest Contentful Paint — lo más grande tarda en aparecer): ideal < 2,5 segundos.
- **INP** (Interaction to Next Paint — qué tan rápido responde a un toque): ideal < 200 ms. *Nota: INP reemplazó a FID; si lees guías viejas que hablan de FID, están desactualizadas.*
- **CLS** (Cumulative Layout Shift — que no salten los elementos mientras carga): ideal < 0,1.

En Colombia mucha gente entra con datos móviles y celulares de gama media. Si tu landing tarda 5 segundos, la mitad se va antes de verla — pagaste el clic para nada. Mídelas gratis en **PageSpeed Insights** (mira la pestaña "móvil", no "escritorio"). La optimización técnica para ponerlas en verde va en `desingweb-lushows`.

## Message match: el clic debe sentirse continuo

El **message match** es que la keyword, el anuncio y la landing digan LO MISMO. El usuario buscó algo, el anuncio se lo confirmó, y al llegar la página debe rematarlo sin sorpresas. Si hay desconexión, el cerebro siente "esto no es lo que pedí" y se va en menos de 3 segundos.

| Eslabón | Ejemplo coherente |
|---|---|
| Keyword | calculadora de costos para restaurante |
| Título del anuncio | Calculadora de Costos para Restaurante |
| H1 de la landing | Calculadora de Costos para tu Restaurante |
| Oferta visible arriba | $10.000 COP · pago único · descarga inmediata |
| CTA dominante | "Descargar ahora" / "Pedir por WhatsApp" |

Reglas del message match:
- **Un grupo de anuncios = una landing (o sección) dedicada.** No mandes todos los temas a la home (ver 37 para la estructura). Si tienes grupos de restaurante, cafetería y dark kitchen, idealmente son 3 landings (o 1 con secciones ancladas por URL).
- **La promesa del anuncio debe estar visible SIN hacer scroll** (above the fold). Si el anuncio dice "pago único $10.000", el precio se ve apenas carga. En móvil "above the fold" son los primeros ~600px: ahí va H1 + oferta + CTA.
- **Un solo CTA dominante** que coincida con la intención: "Descargar ahora", "Pedir por WhatsApp". No 5 botones compitiendo. El CTA secundario (si existe) va abajo y discreto.
- **Quita el ruido**: menú gigante, banners de otros productos, pop-ups de "suscríbete a la newsletter". Cada distracción es una fuga de conversión.

### Anatomía de una landing de Search que cierra (orden vertical)

1. **H1 con la keyword** + subtítulo de beneficio. (message match)
2. **Oferta + precio + CTA** visible sin scroll. (corta la duda "¿cuánto?")
3. **Prueba social**: "+2.000 negocios", logos, testimonios. (mata el miedo a estafa)
4. **Cómo funciona** en 3 pasos. (baja la fricción percibida)
5. **Objeciones** respondidas (FAQ): "¿es pago único?", "¿sirve para mi tipo de negocio?". (apóyate en `ventas_lushows`)
6. **CTA final** repetido. (el que se convenció abajo no debe volver a buscar el botón)

Cuando el match es perfecto, sube el CVR (vendes más) Y Google ve relevancia (sube Quality Score, baja CPC). Por eso vale más arreglar la landing que subir la puja: la puja solo trae más clics caros; la landing convierte los que ya tienes.

## Lead form vs landing propia

Google ofrece capturar el lead dentro del anuncio (asset de lead form, ver 32) sin que el usuario salga a tu web. Tentador, pero ojo: el lead form suele dar leads **más baratos pero de menor calidad** — gente que dejó el dato por impulso sin ver tu propuesta completa. La landing propia filtra mejor: quien llega, lee, se convence y convierte está más caliente. Regla: si vendes algo que necesita explicación o confianza (como un producto digital de $10.000 que el cliente no conoce), prioriza landing propia. Prueba el lead form como complemento, no como reemplazo, y compara la calidad del lead, no solo el costo.

## Cómo construirla (ruteo)

Para diseñar y programar la landing — estructura visual, copy persuasivo, velocidad, móvil, animación — usa **`desingweb-lushows`**, que produce páginas premium tipo Awwwards y rápidas. Para el copy que cierra y maneja objeciones dentro de la página, apóyate en `ventas_lushows`. Para la coherencia de marca (colores, tipografía, tono), `directorcreativo_lushows`. Para validar que el precio y la oferta tienen sentido económico, `economist_lushows`. Tu trabajo como media buyer es definir el message match, el CTA y qué debe responder la página; el equipo de diseño lo materializa.

## Errores comunes — blacklist

- **Mandar el tráfico a la home**: la home habla de todo, así que no es relevante para ninguna búsqueda; baja Quality Score y CVR. Manda a una landing dedicada.
- **Landing lenta en móvil**: si tarda más de 3 segundos en celular pierdes la mitad del tráfico que ya pagaste; mide Core Web Vitals en la pestaña móvil de PageSpeed (optimización → `desingweb-lushows`).
- **Romper el message match**: el anuncio promete una cosa y la página muestra otra; el usuario se va y Google te penaliza el Quality Score.
- **Esconder el precio o la oferta**: si el anuncio dijo "$10.000" y hay que cazar el precio en la página, se rompe la confianza; ponlo above the fold.
- **Cinco CTAs distintos**: el usuario no sabe qué hacer y no hace nada; un solo CTA dominante alineado a la intención.
- **Pop-ups y menús gigantes**: cada distracción es una fuga; quita el ruido del último metro.
- **Optimizar la landing sin tocar el anuncio (o al revés)**: el match es de la cadena completa keyword→anuncio→landing; arreglar solo un eslabón no cierra el círculo (ver 37).
- **Asumir que el lead form rinde igual que la landing**: suele dar leads más baratos pero peores; mide la calidad, no solo el costo.

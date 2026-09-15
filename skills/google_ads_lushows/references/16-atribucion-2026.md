# 16 — Atribución 2026

Lee este módulo cuando los números de Google Ads no cuadran con los de GA4, cuando no entiendes "a quién le da el crédito" una venta que pasó por varios anuncios, o cuando tu CRM dice una cosa y la plataforma otra. La atribución es **cómo se reparte el crédito** de una conversión entre los clics/anuncios que la persona tocó antes de comprar. En 2026 el modelo cambió de raíz: el **last-click se retiró en 2025** y el default es **atribución data-driven (DDA)**. Entender esto es lo que separa al que optimiza con la verdad del que persigue números que nunca van a cuadrar.

## Data-driven attribution (DDA) es el default

| Modelo | Cómo reparte el crédito | Estado 2026 |
|---|---|---|
| **Data-driven (DDA)** | IA reparte según el aporte real de cada punto de contacto, con tus propios datos | **DEFAULT** |
| Last-click | Todo el crédito al último clic | **Retirado en 2025** |
| First-click, lineal, posición, decay | Reglas fijas | **Retirados** (ya no se eligen) |

DDA es mejor porque reconoce que una venta rara vez viene de un solo clic: alguien busca tu marca (ver 39), luego ve un anuncio genérico, luego vuelve por remarketing (ver 24), y compra. Last-click le daba todo el crédito al último toque y te hacía subestimar lo que abre el embudo. DDA reparte **fraccionalmente**: vas a ver conversiones con decimales (0.4, 1.7) — es normal, es el crédito parcial de cada campaña en el recorrido.

**Implicación práctica enorme:** no compares campañas por "conversiones enteras". Una campaña genérica que abre embudos puede mostrar 0.6 conversiones por venta y aun así ser esencial; si la pausas, las campañas de "abajo del embudo" (marca, remarketing) se quedan sin gente que alimentar. Mira el **conjunto**, no la campaña aislada (ver 64, 65). Bajo DDA, matar al que abre el embudo porque "tiene pocas conversiones enteras" es el error analítico más caro de 2026.

## Ventanas de conversión (conversion windows)

La **ventana de conversión** es cuánto tiempo después del clic Google sigue atribuyendo una venta a ese clic.

| Parámetro | Default típico | Cuándo ajustar |
|---|---|---|
| Ventana de clic | 30 días (configurable 1-90) | Ciclo de compra largo (B2B, high-ticket) → amplía a 60-90 (ver 27, 58) |
| Ventana de engagement de vista (video) | 1-3 días | Según tu ciclo |

Si vendes algo que la gente decide en horas (la calculadora a $10.000 COP), una ventana corta refleja la realidad. Si vendes un servicio B2B que toma 6 semanas de decisión, una ventana de 30 días **subestima** tus conversiones: la venta cae fuera de la ventana y parece que el anuncio no sirvió (ver 58). Ajusta la ventana a tu ciclo real **antes** de juzgar rentabilidad, porque cambiar la ventana después reescribe el histórico y confunde.

## Google Ads vs GA4: por qué nunca coinciden

Ambos miden, pero **atribuyen distinto**, y por eso jamás te van a dar el mismo número. No es un bug, es diseño.

| | Google Ads | GA4 |
|---|---|---|
| Qué atribuye | Conversiones a **clics de Google Ads** | Conversiones a **todos los canales** (orgánico, directo, redes, email…) |
| Momento del crédito | Por **fecha del clic** (la venta se suma al día del clic) | Por **fecha de la conversión** |
| Modelo | DDA propio de Ads | DDA propio de GA4 (puede diferir) |
| Para qué sirve | Optimizar el bidding de Ads (ver 13) | Ver el cuadro completo multicanal |

**Regla:** usa **Google Ads** para optimizar campañas (es lo que alimenta el bidding) y **GA4** para entender el rol de Google dentro de todo tu marketing. Si GA4 te da menos conversiones de Google que Ads, suele ser por la diferencia de modelo/fecha y por pérdida de cookies; por eso necesitas Enhanced Conversions y Consent Mode v2 (ver 06). GA4 es la **única analítica** desde el retiro de Universal Analytics en jul-2023 (ver 62) — si alguien te habla de "Universal Analytics", está en 2022.

## gclid: el hilo que conecta todo

El **gclid** (Google Click Identifier) es un código único que Google agrega a la URL en cada clic (`?gclid=Cj0K...`). Es la pieza que permite **triangular con el backend** y cerrar el loop offline:

1. Tu sitio/CRM **captura el gclid** del clic (campo oculto en el form, o cookie) y lo guarda con el lead/pedido.
2. Cuando esa persona compra —incluso semanas después, incluso offline por WhatsApp o teléfono— subes la venta a Google con su gclid vía **Offline Conversion Import (OCI)** (ver 53, 66).
3. Google une la venta real al clic original → el bidding aprende qué clic **cierra venta**, no cuál solo abre chat (ver 14).

Sin gclid + OCI, en negocios que cierran offline/WhatsApp (la mayoría en LatAm) **el algoritmo optimiza a ciegas**: persigue clics-a-WhatsApp que no facturan. El cierre de la venta rutea a `ventas_lushows`, pero el dato de que cerró **debe volver a Google** o estás desperdiciando la inteligencia del bidding. Variante moderna: si capturas datos de primera parte (email/teléfono) puedes usar **Enhanced Conversions for Leads** en vez de gclid puro para casar el lead con la venta (ver 53).

## Triangular: la verdad está en 3 fuentes

Nunca confíes en una sola pantalla. Cruza:

1. **Google Ads** — qué optimiza el algoritmo (la fuente del bidding).
2. **GA4** — rol multicanal, comportamiento en sitio, asistencias.
3. **Backend/CRM** — ¿el lead pagó? ¿cuánto? ¿devolvió? ¿se quedó?

Si Ads dice "ROAS 600%" pero el backend dice que la mitad de esos leads no cierran, tu ROAS real es la mitad (ver 64). **El backend manda.** La plataforma reporta clics-que-se-volvieron-conversión-medida; el backend reporta plata-en-la-cuenta. Optimiza con Ads, decide con el backend.

## Errores comunes — blacklist

- **Esperar que Google Ads y GA4 cuadren** al peso: atribuyen distinto por diseño; perseguir el match es perder tiempo.
- **Juzgar una campaña genérica por conversiones enteras** bajo DDA: muestra crédito fraccional y parece floja aunque abra embudos (ver 39).
- **Pausar al que abre el embudo** porque "tiene pocas conversiones": dejas sin gente a marca y remarketing; cae todo el sistema.
- **Ventana de conversión corta en ciclo largo** (B2B/high-ticket): las ventas caen fuera de la ventana y matas campañas rentables (ver 58).
- **No capturar el gclid** en el sitio/CRM: imposible importar ventas reales; el bidding va ciego (ver 66).
- **Optimizar solo con datos de la plataforma** sin cruzar backend: ROAS inflado por leads que no cierran (ver 64).
- **Creer que DDA arregla la pérdida de cookies**: necesitas Enhanced Conversions + Consent Mode v2 como piso de medición (ver 06).
- **Confiar en el crédito de PMax sin medir incrementalidad**: DDA puede darle crédito a marca canibalizada (ver 12, 65).
- **Hablar de Universal Analytics o last-click** en 2026: ambos retirados; estás operando con un mapa viejo.

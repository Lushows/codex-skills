# 62 — GA4 y debugging de conversiones

Lee este módulo cuando tus conversiones "no llegan", cuando los números de Google Ads y GA4 no cuadran y no sabes a cuál creerle, cuando registraste una compra de prueba y no apareció, o cuando vas a confiar tu Smart Bidding (ver 13) a una señal de conversión que nunca verificaste. **Si la medición está rota, todo lo demás miente** (ver 61). Esta es la capa 0, y en 2026 es la capa que más cuentas tienen sucia sin saberlo.

GA4 (Google Analytics 4) es **la única analítica de Google** hoy — Universal Analytics está muerto y enterrado desde 2024. Es la fuente de verdad de eventos del sitio, y de ahí salen muchas de tus conversiones hacia Ads. Pero "fuente de verdad" no significa "perfecta": significa que si está mal configurada, optimizas a ciegas con confianza falsa.

## Eventos vs conversiones (key events): no son lo mismo

Confusión número uno. Aclárala antes de seguir. Ojo: Google renombró "conversiones" a **"key events"** en GA4 (las "conversiones" ahora viven en Google Ads); en la práctica la gente usa los dos términos.

| Concepto | Qué es | Ejemplo |
|---|---|---|
| **Evento (event)** | Cualquier cosa que pasa en el sitio, registrada por GA4 | `page_view`, `scroll`, `add_to_cart`, `purchase`, `form_submit` |
| **Key event / conversión (GA4)** | Un evento que **tú marcaste como importante** | Marcas `purchase` o `lead_form` como key event |
| **Conversión en Google Ads** | La que **importas** a Ads para optimizar pujas | Importas `purchase` desde GA4 a Ads |

El flujo completo: GA4 registra el **evento** → tú lo marcas como **key event** → lo **importas a Google Ads** como conversión → Smart Bidding optimiza hacia él. Si cualquier eslabón se rompe, el bidding optimiza a ciegas. Y un bidding ciego no avisa que está ciego: simplemente gasta mal.

## DebugView: verifica antes de confiar

**DebugView** es la herramienta de GA4 para ver eventos **en tiempo real** mientras navegas. Es tu detector de mentiras. Úsala SIEMPRE antes de dar una conversión por buena, y de nuevo cada vez que toquen el sitio (un cambio de tema, un plugin nuevo o un dev "que no tocó nada" rompen tracking constantemente).

Cómo verificar una conversión, paso a paso:
1. Activa el modo debug (extensión **Google Analytics Debugger** en Chrome, o GA4 → Admin → DebugView con `debug_mode` activo).
2. En tu sitio, haz el camino completo: clic en anuncio (o simúlalo con un `gclid` de prueba en la URL), agrega al carrito, compra de prueba.
3. En GA4 → Admin → **DebugView**, mira que el evento `purchase` aparezca **una sola vez**, con su valor y moneda correctos (COP).
4. Confirma que trae los parámetros: `value`, `currency`, `transaction_id`.

Lo que buscas: el evento llega, **una vez**, con valor correcto. Si llega dos veces → duplicación (infla tu ROAS). Si llega sin `value` → tu ROAS será 0 o basura. Si llega con `currency: USD` cuando vendes en pesos → tu valor está 4.000x mal.

## Enhanced Conversions: por qué ya no es opcional (2026)

**Enhanced Conversions** (conversiones mejoradas) envía datos de primera parte **hasheados** (email, teléfono — irreversibles) junto a la conversión, para recuperar atribución que los navegadores rompen (Safari ITP, bloqueo de cookies, etc.). En 2026, con cookies de tercera parte cada vez más muertas y privacidad apretando, **sin Enhanced Conversions subreportas y tu Smart Bidding aprende con menos señal**. Actívalo (Ads → Goals → Conversions → Settings → Enhanced Conversions), normalmente vía Google tag o GTM con consentimiento. El detalle de implementación de la señal de conversión y OCI va en (ver 53).

## Consent Mode v2 y conversiones modeladas

**Consent Mode v2** le dice a Google si el usuario aceptó cookies. Si no aceptó, Google **no** pone cookies pero recibe pings anónimos y **modela** (estima estadísticamente) las conversiones que probablemente ocurrieron. Resultado clave para 2026: **parte de tus conversiones son modeladas, no contadas una a una.** Eso es normal y es mejor que perderlas, pero significa que tu conteo nunca será 1:1 con el backend. Sin Consent Mode bien configurado, subreportas fuerte (y peor con tráfico sujeto a normativas de privacidad).

## Dedup, importación y conversiones que no llegan

**Deduplicación (dedup):** evitar contar la misma venta dos veces. Causa típica: el usuario recarga la página de gracias, o el evento se dispara por dos sistemas (GA4 + un píxel viejo + GTM). El `transaction_id` es lo que permite a Google deduplicar — **siempre** mándalo en `purchase`.

**Importar a Ads:** Google Ads → Goals → Conversions → New → Import → Google Analytics 4. Marca solo las conversiones que quieres que Smart Bidding persiga (normalmente la venta o el lead final, **no** `add_to_cart`).

**Conversiones que no llegan — checklist de causas:**

| Síntoma | Causa probable | Fix |
|---|---|---|
| Cero conversiones en Ads, sí en GA4 | No la importaste, o import recién hecho (24–48 h de lag) | Revisa import; espera la ventana |
| Conversión en GA4 pero no en DebugView | Evento mal nombrado o no dispara | Revisa el tag/evento en la página de gracias |
| Llega doble | Sin `transaction_id`, o doble disparo (GA4 + píxel) | Agrega `transaction_id` único; quita disparos duplicados |
| Valor en 0 o raro | Falta `value`/`currency`, o moneda mal | Asegura `value` numérico y `currency: COP` |
| Consentimiento bloquea | Consent Mode v2 sin configurar | Configúralo; activa conversiones modeladas |
| Subreporte en Safari/iOS | Sin Enhanced Conversions | Actívalas (ver arriba, 53) |

## Discrepancias Ads vs GA4: por qué y cuánto es normal

Te van a dar **números distintos** y eso es **normal y esperado**, no un error. Razones:

- **Modelo de atribución distinto** (ver 16): Ads usa data-driven a su manera; GA4 a la suya.
- **Ventana de conversión distinta:** Ads puede contar una conversión hasta 90 días después del clic; GA4 usa otra ventana por defecto.
- **Momento de registro:** Ads atribuye la conversión al **día del clic**; GA4 al **día de la conversión**. Si alguien hace clic el lunes y compra el jueves, los reportes la ponen en días distintos.
- **Qué cuentan:** Ads solo cuenta lo que viene de Ads; GA4 cuenta todas las fuentes.
- **Modelado:** ambos modelan parte (Consent Mode), pero con métodos distintos.

**¿Cuánto es normal?** Diferencias del **5–20%** entre Ads y GA4 son normales. Si ves 2x o 3x, ahí sí hay problema de configuración (doble conteo, atribución mal, import roto, auto-tagging apagado — ver 66). **No persigas el cuadre perfecto: persigue consistencia y tendencia**, no que coincidan al decimal. Para la verdad financiera, ninguna de las dos sirve: backend + banco + MER (ver 64).

## Errores comunes — blacklist

1. **Confiar en una conversión que nunca viste en DebugView.** Si no la verificaste en tiempo real, no sabes si funciona. Smart Bidding optimiza a ciegas con datos malos (ver 13).
2. **Mandar `purchase` sin `transaction_id`.** Es la causa #1 de doble conteo y ROAS inflado.
3. **Importar `add_to_cart` como conversión principal.** El bidding optimizará a carritos, no a ventas. Importa la acción que de verdad vale plata.
4. **Pánico porque Ads y GA4 no coinciden.** El 5–20% de diferencia es normal por atribución y ventanas. Solo investiga si es 2x+ (ver 66).
5. **Olvidar `currency: COP`.** Sin moneda correcta, los valores y el ROAS son basura.
6. **No configurar Consent Mode v2 ni Enhanced Conversions en 2026.** Sin ellos subreportas y el bidding aprende con menos señal (ver 53).
7. **Optimizar campañas mientras la medición está rota.** Capa 0 primero (ver 61); todo diagnóstico sobre datos falsos es trabajo perdido.
8. **No re-verificar tras un cambio en el sitio.** Un plugin nuevo, un cambio de tema o un dev "que no tocó nada" rompen tracking. Re-corre DebugView después de cada cambio.

# 134 — Technographics (targetear por la tecnología que usan)

Los **technographics** (perfil tecnológico) son el dato de **qué tecnología usa una empresa**: su CRM, su plataforma de e-commerce, su pasarela de pago, su hosting, su chat, sus píxeles de ads. Saberlo te deja segmentar y personalizar con una precisión que los firmographics (tamaño, industria — `15`) no dan: si sabes que una tienda usa Shopify, sabes su volumen aproximado, su stack, y puedes hablarle de dolores **específicos de Shopify**. Este módulo cubre las fuentes (BuiltWith, Wappalyzer, Clay) y cómo convertir "usa X tecnología" en un ángulo de venta.

## El principio: la tecnología revela el dolor y la calificación

Los technographics sirven para dos cosas distintas:

1. **Calificar (fit).** Tu producto encaja o choca con ciertas tecnologías. Si te integras **solo** con Shopify, targetear a quien usa Shopify multiplica tu tasa de cierre y evita quemar leads que nunca podrían comprarte (`10`, `78`). Si compites contra Salesforce, "usa Salesforce" es tu lista de displacement (`19`).
2. **Personalizar (ángulo).** La tecnología revela un dolor probable. "Con Shopify a ese volumen normalmente pasa {dolor}" es infinitamente más relevante que "Hola {nombre}". El stack es munición de personalización (`29`, `52`).

La mecánica de detección: la mayoría del stack de una empresa es **visible en el código de su web** (scripts, píxeles, meta tags, DNS, certificados). Las herramientas escanean eso y te dicen qué corre. Lo que **no** es visible desde la web (CRM interno, ERP) requiere fuentes más caras o inferencia.

## Qué se detecta y qué no

| Detectable desde la web (fácil/barato) | Difícil (caro/inferido) |
|---|---|
| Plataforma e-commerce (Shopify, WooCommerce, VTEX) | CRM interno (Salesforce, HubSpot) — a veces sí por chat/forms |
| CMS (WordPress, Webflow) | ERP / contabilidad |
| Analytics y píxeles (GA4, Meta Pixel, TikTok) | Herramientas internas sin huella web |
| Chat, pop-ups, reviews (Intercom, Zendesk, Klaviyo) | Contratos y renovaciones (nadie los publica) |
| Pasarela de pago, hosting, CDN, framework JS | |

## Las herramientas

| Herramienta | Qué hace | Precio aprox. 2026 | Nota |
|---|---|---|---|
| **BuiltWith** | Base enorme de qué tecnología usa cada web + **listas** ("dame todas las empresas con Shopify en Colombia") | Desde ~$295/mes para listas; lookup puntual gratis | El estándar para construir listas por tecnología |
| **Wappalyzer** | Detecta el stack de una web; API + extensión de navegador + listas | Extensión gratis; API/listas desde ~$250/mes | Más barato para verificación puntual y API en Clay |
| **Clay** (`31`) | Columna que corre BuiltWith/Wappalyzer sobre tu lista + waterfall (`130`) | Créditos | Para enriquecer una lista que ya tienes |
| **Apollo / ZoomInfo** | Traen technographics dentro de sus filtros de búsqueda | Incluido en el plan | Cómodo si ya es tu base (`100`, `106`) |
| **Datanyze** | Technographics + firmographics | Pago | Alternativa clásica |

**Dos flujos distintos:** para **construir una lista desde cero** por tecnología → BuiltWith (te exporta "todas las que usan X"). Para **enriquecer una lista que ya tienes** con su stack → Wappalyzer/BuiltWith API dentro de Clay.

## Cómo usarlo, paso a paso

1. **Define la tecnología clave** para tu producto: la que indica encaje (te integras con ella) o dolor (la que crea el problema que resuelves).
2. **Construye o enriquece:**
   - Lista desde cero: BuiltWith → "empresas con {tech} en {país}" → exporta.
   - Lista existente: Clay + Wappalyzer → columna `usa_shopify: sí/no`.
3. **Filtra:** quédate con las que encajan; descarta las que usan una tecnología incompatible (evitas leads basura, `78`).
4. **Cruza con firmographics** (`15`): "Shopify **+** más de 20 empleados **+** Colombia".
5. **Escribe el ángulo específico** de esa tecnología (ejemplos abajo).
6. **Verifica antes de enviar:** los technographics envejecen (una empresa migra de plataforma); no asumas que el dato de hace 8 meses sigue vigente (`139`).

## De tecnología a ángulo de mensaje

```
Dato: usa Shopify + tráfico alto
→ "Con Shopify a ese volumen, el costo de {proceso} suele dispararse.
   Ayudamos a tiendas Shopify a {resultado}…"

Dato: usa WooCommerce (self-hosted, suele = negocio que cuida costos)
→ "Vi que manejan la tienda en WooCommerce; a ese nivel el dolor
   normalmente es {X}. Lo resolvemos sin que migres nada…"

Dato: usa Competidor X (displacement, `19`)
→ "Muchos equipos que usaban {Competidor X} se pasaron a nosotros
   por {diferenciador}. ¿Vale una comparación de 10 min?"

Dato PYME: la web NO tiene píxel de Meta ni GA4
→ "Vi que aún no miden el tráfico de la web; sin eso, cada peso de
   pauta va a ciegas…" (para quien vende marketing/medición)
```

## Ejemplo real: lista Shopify + enriquecimiento en Clay

```
Objetivo: vender una app que se integra solo con Shopify.
  1. BuiltWith → "tiendas Shopify en México y Colombia, +10 empleados"
     → exporta 2.400 dominios.
  2. Clay: enriquece decisor (fundador/e-commerce manager) + email (`130`).
  3. Wappalyzer en Clay: confirma que HOY siguen en Shopify (no migraron).
  4. IA en Clay: lee la tienda → categoría de producto → ángulo por vertical.
  5. Filtro: Shopify vigente + email valid (`28`) → campaña segmentada.
Resultado: 100 % de la lista puede realmente comprarte. Cero leads basura.
```

## Errores comunes

- **Datos viejos** → una empresa migró de plataforma y le hablas de la anterior. Reverifica (`139`).
- **Targetear tecnología irrelevante** → "usa WordPress" no dice casi nada si vendes a cualquiera; elige la tecnología que **de verdad** indica encaje o dolor.
- **Presumir el "stalking" técnico** → "vi que usas Shopify" está bien; entrar en detalle de su código asusta.
- **Solo technographics, sin fit de tamaño** → una tienda Shopify de 1 persona quizá no te sirve; cruza con firmographics (`15`).
- **Inferir CRM interno desde la web** → no siempre es visible; no asumas.

## Frontera y siguiente paso

Los technographics te dan una lista **precalificada por encaje**; convertirla en conversación y cierre es `ventas_lushows`. Define la tecnología clave de tu producto y saca tu primera lista en BuiltWith, o enriquece la que tienes con Wappalyzer en Clay (`31`, `130`). Cruza con firmographics (`15`), escribe el ángulo por tecnología (`52`), y mantén el dato fresco (`139`). Si la señal es "acaban de **adoptar** una tecnología" (no solo "la usan"), eso es una señal de evento → `37`, `135`.

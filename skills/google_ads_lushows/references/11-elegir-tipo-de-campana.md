# 11 — Elegir el tipo de campaña

Lee este módulo cuando vas a crear una campaña y Google te muestra varias opciones con nombres bonitos, o cuando alguien te dijo "todo PMax y ya" o "ponle Display que es más barato". Elegir mal el tipo es el error que más plata quema en Google Ads: no porque la plataforma falle, sino porque pones a un tipo de campaña a hacer un trabajo para el que no fue diseñado. El principio de toda la skill: **Google CAPTURA demanda existente** (intención). Cuando no hay demanda que capturar, los tipos que "generan" (Display, Video, Demand Gen) rinden parecido a Meta — y para generar demanda desde cero, Meta o TikTok suelen ser mejores (rutea a `facebook_ads_lushows` / `tiktok_ads_lushows`).

## Los tipos y para qué sirve cada uno

| Tipo | Qué hace | Dónde aparece | Captura o genera |
|---|---|---|---|
| **Search** | Aparece cuando alguien busca tu producto/servicio | Resultados de Google | **CAPTURA** (el rey) |
| **Performance Max** | IA reparte tu gasto entre Search, Shopping, Display, YouTube, Gmail, Maps, Discover | Toda la red Google | Mixto (ver 12) |
| **Shopping** | Anuncios con foto+precio para e-commerce | Pestaña Shopping, Search | CAPTURA (retail, ver 34) |
| **Demand Gen** | Reemplazó a Discovery (jul-2023); creativos visuales en feeds | YouTube, Shorts, Gmail, Discover | **GENERA** (ver 41) |
| **Video** | Anuncios en YouTube (in-stream, in-feed, Shorts) | YouTube | Genera / awareness (ver 40) |
| **Display** | Banners en sitios web | Red de Display (millones de sitios + apps) | Genera / remarketing (ver 43) |
| **App** | Promociona descargas/eventos de app | Play, Search, YouTube, Display | Captura (instalación) |
| **Local Services** | Pago-por-lead para servicios locales (LSA) | Top de Search, con badge "Garantizado por Google" | CAPTURA local (ver 50) |

Nota 2026: **Discovery ya no existe**, lo reemplazó Demand Gen — si ves "Discovery" en una guía vieja, tradúcelo a Demand Gen. **Smart Shopping y los antiguos Local campaigns** ya migraron dentro de PMax hace tiempo.

## Matriz por objetivo (qué elegir según qué vendes)

| Tu situación | Empieza con | Después suma |
|---|---|---|
| Servicio/producto con **demanda buscada** (la gente ya googlea esto) | **Search** (genérico + marca) | PMax una vez tengas conversiones limpias (ver 12) |
| **E-commerce con catálogo** y Merchant Center | **PMax retail** o **Shopping estándar** | Search marca, Demand Gen remarketing (ver 35) |
| **Servicio local** (plomero, abogado, dentista, restaurante) | **Local Services (LSA)** + Search | Call ads, PMax local (ver 51) |
| **Leads B2B** (cotización, demo) | **Search** + lead form o landing | PMax con OCI desde CRM (ver 27, 52, 53) |
| Producto **nuevo que nadie busca** (categoría nueva) | **Demand Gen / Video** para crear demanda — **o mejor Meta/TikTok** (rutea a `facebook_ads_lushows`) | Search cuando empiecen a buscarte |
| Quiero **re-impactar** a quien ya me visitó | **Demand Gen** o **Display** remarketing | (ver 24) |

## El error #1: usar el tipo equivocado para el trabajo

**PMax para todo.** PMax es potente pero opaco: cede mucho control (ver 12) y, sin Search de marca separada + brand exclusions, **canibaliza** tu tráfico de marca y se lleva el crédito de ventas que ya eran tuyas. Inflama el ROAS reportado y te engaña. Regla: **nunca PMax como primera y única campaña.** Primero Search para capturar la intención clara y generar señal de conversión limpia; PMax para expandir cuando ya tienes esa señal (ver 14).

**Display/Video para "vender directo".** Display tiene CPMs baratísimos (en Colombia puedes ver CPM de $3.000-8.000 COP) y por eso tienta. Pero el clic en Display es de baja intención: la persona no te buscaba, estaba leyendo otra cosa. Conviertes 5-20x peor que Search. Display y Video **brillan en remarketing y awareness**, no en venta directa a frío. Si alguien te promete "ventas baratas con Display a frío", está vendiendo humo.

**Saltarse Shopping/PMax retail en e-commerce.** Si vendes productos físicos con catálogo y no tienes presencia en Shopping/Merchant Center, estás dejando la mitad del SERP de compra (la fila de productos con foto y precio, lo primero que ve el comprador) sobre la mesa (ver 34).

## Search vs PMax: el cruce que más confunde en 2026

| | Search | Performance Max |
|---|---|---|
| Control | Keywords, negativos a nivel de grupo, RSA visibles | Asset groups, señales, negativos solo a nivel cuenta |
| Transparencia | Alta (términos de búsqueda, QS, subasta) | Baja (reporte por canal mejorado pero parcial) |
| Mejor para | Capturar intención específica, B2B, leads | Catálogo retail, escalar alcance sobre señal madura |
| Riesgo | Menor; tú ves todo | Canibaliza marca si no la blindas (ver 39) |
| Volumen mínimo | Funciona con poco | ~30 conv/mes para calibrar (ver 13) |

En 2026 hay un puente: **AI Max for Search** (ver 90) mete potencia tipo-PMax (matching ampliado, assets generados, mejores términos) *dentro* de tu campaña Search, sin perder la transparencia de Search. Para muchos anunciantes LatAm pequeños, **Search + AI Max** entrega gran parte del alcance de PMax conservando control. No confundas AI Max (capa dentro de Search) con PMax (campaña aparte de toda la red).

## Regla de secuencia (orden de despliegue)

1. **Search marca** — protege tu nombre con CPC de centavos (ver 39).
2. **Search genérico** — captura la intención real; es tu motor de aprendizaje de conversiones (ver 14).
3. **Shopping / PMax** — expande sobre la señal que ya generó Search (con brand exclusions).
4. **Demand Gen / Video / Display** — remarketing primero; awareness solo con presupuesto que sobre.

No saltes pasos. Cada tipo posterior se apoya en la señal de conversión que generó el anterior (ver 14). Lanzar el paso 3 o 4 antes del 2 es alimentar a la IA con datos sucios.

## Errores comunes — blacklist

- **Lanzar PMax sin Search de marca** que la proteja: canibaliza y reporta ROAS inflado (ver 12, 39).
- **Display/Video a frío esperando ventas directas**: CPM barato, conversión basura; es awareness, no performance (ver 64).
- **"Demand Gen porque está de moda"** cuando tu producto SÍ se busca: estás pagando por generar demanda que ya existe; usa Search y captúrala más barato.
- **Un solo PMax mezclando catálogo entero + generación de leads + marca**: objetivos incompatibles, señal sucia, optimización imposible (ver 14).
- **Confundir AI Max (dentro de Search) con PMax** (campaña aparte): activas lo que no querías y pierdes control sin saberlo (ver 90).
- **Ignorar Local Services siendo negocio local**: es pago-por-lead, con badge de Google, arriba de todo; lo dejas para que un agregador te coma el lead (ver 50).
- **Elegir tipo por "lo barato del clic"** en vez de por intención: el clic barato sin intención es caro por conversión (ver 64).
- **No usar Shopping/PMax retail en e-commerce con catálogo**: regalas el espacio visual de compra a la competencia (ver 34, 35).
- **Buscar "Discovery"** en una guía 2026: ya no existe, es Demand Gen; estás leyendo material caducado.

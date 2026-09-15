# 51 — Video Shopping Ads / Product Sales

Lee este módulo cuando tengas TikTok Shop activo y quieras vender con video + catálogo, cuando un cliente de e-commerce te pregunte "¿cómo etiqueto el producto en el video?", o cuando vengas de pensar en términos de "anuncio de tráfico" y necesites el formato que cierra la venta dentro de la app. Esto solo aplica donde TikTok Shop existe (verifica país, ver 50). Si no hay Shop, salta a 55 (cierre por WhatsApp). Recuerda el frame: TikTok es **descubrimiento** (ver 00). El VSA convierte ese descubrimiento en compra sin sacar al usuario del feed — es el formato comercial central del e-commerce en TikTok.

## Qué son los Video Shopping Ads (VSA / Product Sales)

**Video Shopping Ads (VSA)**, dentro del objetivo de campaña **Product Sales**, son anuncios que combinan **un video nativo + tu catálogo de productos**. El video se ve como un TikTok normal, pero lleva el producto **etiquetado** (con icono de carrito y precio); el usuario toca y compra dentro de la app, sin salir.

La diferencia con un ad de tráfico normal:

| Ad de tráfico | Video Shopping Ad (VSA) |
|---|---|
| Lleva a una landing externa | Vende dentro de TikTok |
| Optimiza por clic / visita | Optimiza por **compra** (Complete Payment del Shop) |
| No usa catálogo | **Requiere catálogo** sincronizado (ver 56) |
| Mide en tu web | Mide con eventos de Shop + pixel/Events API (ver 57) |

VSA es el "anuncio que vende" cuando tienes Shop. Le dices a TikTok "optimiza por compra del producto X" y el sistema busca compradores, no curiosos. El objetivo de campaña asociado es **Product Sales** (ver 11 sobre elegir objetivo). Dentro de Product Sales tienes dos modos de venta:

| Modo | Qué hace | Cuándo |
|---|---|---|
| **Video Shopping Ads (manual)** | Tú eliges video, producto y público; más control | 1 producto o pocos, quieres control fino |
| **GMV Max** | TikTok automatiza todo el Shop en una campaña | Catálogo amplio, operación simple (ver 52) |
| **Product Shopping Ads (PSA)** | Anuncio basado solo en la ficha del catálogo, sin video propio | Retargeting de catálogo, complemento |
| **LIVE Shopping Ads** | Empuja tráfico al live mientras transmites | Venta en vivo (ver 53) |

Este módulo es el VSA manual con video. GMV Max y Live tienen sus propios módulos.

## Cómo se arma un VSA — requisitos y pasos

Antes de armarlo necesitas, sin excepción:

1. **TikTok Shop activo y verificado** en el país (ver 50).
2. **Catálogo sincronizado y sano** — productos con foto, título humano, precio, stock, atributos (ver 56). Sin catálogo no hay VSA.
3. **Pixel + Events API midiendo el evento de compra** del Shop (ver 05, 06, 57).
4. **Al menos un video nativo** donde el producto se vea en uso (no foto de estudio — ver 30, 33 sobre formato).

Pasos en Ads Manager, en orden:

1. Crea campaña con objetivo **Product Sales**.
2. Fuente de venta (*sales source*): **TikTok Shop**.
3. Conecta el **catálogo** y elige los productos a promocionar (o deja que GMV Max gestione todo el Shop — ver 52).
4. Sube el **video** y etiqueta el producto (el sistema enlaza el SKU del catálogo a la pieza).
5. Deja el público **broad** (amplio) — el creativo segmenta, no el targeting (ver 20, 30). Smart+ puede gestionar audiencia, puja y ubicación automáticamente (ver 12).
6. Evento de optimización: **Complete Payment** (pago completado), no clic ni vista.
7. Presupuesto y puja: arranca con presupuesto que permita ~**20–50 conversiones/semana** para salir del aprendizaje; puja en *lowest cost* primero, luego target ROAS si hay datos (ver 15, 64).

### Plantilla de estructura de cuenta (VSA manual)

```
Campaña: Product Sales — [Producto/Línea]
 ├─ Grupo de anuncios A (broad, Complete Payment)
 │   ├─ Video 1 (UGC, producto en uso, gancho 0–3s)
 │   ├─ Video 2 (demo/antes-después)
 │   └─ Video 3 (reseña/testimonio)
 └─ Grupo de anuncios B (retargeting AddToCart / ViewContent)
     └─ Product Shopping Ad (ficha de catálogo)
```

Regla de creativo: el video debe **mostrar el producto resolviendo algo** en los primeros 3 segundos. UGC de alguien usándolo > toma de catálogo de estudio. El catálogo es la ficha; el video es el vendedor (ver 30, 39 sobre volumen creativo).

## Números de referencia (orientativos, LatAm, COP)

No son promesas — dependen de producto, margen y creativo. Sirven para saber si algo va bien o mal:

| Métrica | Rango sano orientativo | Señal de alarma |
|---|---|---|
| CTR (clic) | 0,8% – 2% | < 0,5% → creativo débil |
| CPM | $8.000 – $25.000 COP | muy alto sin volumen → público angosto |
| Tasa de conversión a compra | 1% – 3% del clic | < 0,5% → catálogo/precio/ficha mala |
| ROAS objetivo inicial | 1,5x – 2,5x | < 1x sostenido → para y revisa |

El ROAS sano depende de tu margen: si tu margen bruto es 40%, necesitas ROAS > 2,5x solo para no perder, y eso **antes** de descontar la comisión del Shop (5–8%). Valida la unit economics con `economist_lushows` (ver 64 sobre ROAS, 16 sobre atribución — TikTok se sobre-atribuye).

## Cuándo usar VSA (y cuándo no)

**Úsalo cuando:**
- Vendes productos de ticket bajo-medio donde la decisión es rápida (impulso).
- Tienes Shop activo y catálogo limpio.
- Tu producto se entiende viéndolo: moda, belleza, gadgets, alimentos, accesorios (ver 80, 84).
- Tienes creativos suficientes para no quemar el mismo video (ver 39).

**No lo uses cuando:**
- No hay TikTok Shop en el país → cierra por WhatsApp (ver 55).
- Vendes high-ticket que necesita conversación → lead calificado (ver 58).
- Tu catálogo está incompleto → arréglalo primero (ver 56), o pierdes plata mostrando productos sin stock.
- Tienes un solo producto y catálogo amplio NO → el VSA manual te sirve; si tuvieras muchos productos, evalúa GMV Max (ver 52).

VSA es la columna del e-commerce en TikTok cuando hay Shop. Si quieres que TikTok automatice TODO el Shop en una sola campaña, eso es GMV Max (ver 52). VSA te da más control producto por producto; GMV Max cede control a cambio de simplicidad y velocidad de aprendizaje. Regla práctica: **no corras VSA manual y GMV Max sobre el mismo producto al tiempo** — se canibalizan la puja.

## Rutas a skills hermanas

- Web/checkout fuera del Shop → `desingweb-lushows`.
- Cierre por WhatsApp cuando no hay Shop → 55 + `ventas_lushows` (módulo 82).
- Validar ROAS y márgenes con comisión incluida → `economist_lushows`.
- Equivalente en Meta (Advantage+ Shopping / catálogo) → `facebook_ads_lushows`; en Google (Shopping/PMax) → `google_ads_lushows`.

## Errores comunes — blacklist

- **Armar VSA sin catálogo sincronizado.** No arranca; sincroniza primero (ver 56).
- **Etiquetar un producto sin stock.** Pagas por clics que no pueden comprar; revisa el feed (ver 56).
- **Optimizar por clic en vez de por compra completada.** Optimizas curiosos; usa Complete Payment (ver 14, 57).
- **Usar toma de catálogo de estudio como video.** El video debe ser nativo y mostrar el producto en uso (ver 30, 33).
- **Prometer VSA donde no hay TikTok Shop.** Verifica el país y, si no hay, cierra por WhatsApp (ver 50, 55).
- **No medir con pixel/Events API además del Shop.** Cierra el loop de medición y valida contra ventas reales (ver 57).
- **Meter high-ticket en VSA esperando compra impulsiva.** Alto ticket va por lead (ver 58).
- **Correr VSA manual y GMV Max del mismo producto a la vez.** Se canibalizan; elige uno por producto (ver 52).
- **Tocar la campaña a diario antes de salir del aprendizaje.** Necesita ~20–50 conversiones/semana para estabilizar; no la ahogues.

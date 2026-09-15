# 57 — Medir conversiones

Lee este módulo cuando tus campañas "gasten" pero no sepas si venden, cuando cierres por WhatsApp y el algoritmo no vea esas ventas, o cuando un cliente te diga "TikTok dice que vendí 30 pero yo vendí 8". Medir bien es lo que separa optimizar por **compradores** de optimizar por **curiosos**. Sin medición cerrada, todo lo demás (creativo, puja, catálogo) optimiza hacia la señal equivocada. Este es el módulo más importante del bloque comercio. El frame: TikTok es **descubrimiento** (ver 00); el descubrimiento solo se vuelve negocio si le devuelves a TikTok la señal de quién compró de verdad.

## Las tres capas de medición

TikTok mide en tres capas. Necesitas las que apliquen a tu caso:

| Capa | Qué captura | Cuándo |
|---|---|---|
| **TikTok Pixel** | Eventos en tu **web** (ViewContent, AddToCart, Complete Payment) | Tienes web/checkout propio (ver 05) |
| **Events API** | Eventos **server-side**, incluyendo offline/WhatsApp | Cierre fuera de la web (ver 06) |
| **SKAN** (SKAdNetwork) | Conversiones en **iOS** con privacidad limitada, datos agregados | Tráfico iOS (apps, y cada vez más web) |

El **pixel** se cae cada vez más por bloqueadores, iOS, navegadores con anti-tracking y muerte de cookies de terceros. Por eso **Events API** (servidor a servidor) es hoy (jun-2026) la columna de la medición seria — no se cae igual y captura lo que el pixel no ve, incluyendo ventas que pasan **fuera de TikTok** (WhatsApp, llamada, tienda física). La buena práctica moderna es **deduplicación**: el mismo evento llega por pixel y por Events API con un `event_id` común, y TikTok no lo cuenta doble. Pixel + Events API juntos = más cobertura sin inflar.

## Cerrar el loop: subir la venta de WhatsApp/offline

Este es el corazón del módulo y la diferencia entre amateur y profesional. El problema:

> En LatAm cierras por WhatsApp. TikTok ve el **clic**, pero **no ve la venta** (pasó fuera de la app). Entonces el algoritmo optimiza por "el que hizo clic" — curiosos — no por "el que compró".

La solución es el **closed loop** (loop cerrado): capturas el clic con el **`ttclid`** (el identificador de clic de TikTok, *TikTok Click ID*) y **subes de vuelta la conversión** (compra o lead calificado) a TikTok vía Events API / offline. Así el algoritmo aprende **quién compra de verdad** y busca más como ese.

Es el equivalente exacto en TikTok de:
- el **`ctwa_clid`** de Meta (el ID del clic de click-to-WhatsApp que subes con la venta — ver `facebook_ads_lushows`),
- y el **OCI** (Offline Conversion Import) de Google (ver `google_ads_lushows`).

Cómo se hace, en flujo paso a paso:

1. El ad lleva a WhatsApp con el **`ttclid` capturado** en el link (parámetro de clic de TikTok). Ese ID viaja en la URL `wa.me` o lo captura tu landing antes de redirigir (ver 55).
2. Guardas el `ttclid` asociado al contacto en tu CRM/dashboard apenas escribe.
3. Cuando ese contacto **compra** (lo marcas en tu sistema — en GastroLatam, el pedido en `data/orders.json`), tomas su `ttclid` y el valor de la venta.
4. **Subes ese evento de compra a TikTok** vía Events API: `event = CompletePayment`, con el `ttclid`, el valor y la moneda (COP).
5. TikTok matchea el clic con la venta → aprende qué creativo/audiencia trae **compradores**.

### Ejemplo de evento que subes (conceptual)

```
POST Events API
{
  "event": "CompletePayment",
  "event_id": "order_4821",        // para deduplicar
  "timestamp": "2026-06-13T15:04:00Z",
  "context": { "ttclid": "EAAxxxx..." },
  "properties": { "value": 10000, "currency": "COP",
                  "content_id": "excel-gastro-v1" }
}
```

Sin este paso, optimizas por clic y atraes curiosos baratos que nunca compran. **Con** este paso, el CPA real baja porque el algoritmo persigue ventas, no clics. Vale más cerrar este loop que cambiar de creativo diez veces.

## Calidad de la señal (el "EMQ" de TikTok)

No basta con enviar eventos — tienen que **matchear**. TikTok evalúa la calidad de tu conexión de eventos (equivalente al Event Match Quality / EMQ de Meta):

- Cuantos más **parámetros de identidad** mandes (email hasheado, teléfono hasheado, `ttclid`), mejor matchea.
- Señal pobre = pocos eventos matcheados = optimización pobre. Revisa el panel de diagnóstico de eventos en Events Manager.
- Hashea PII (email, teléfono) antes de enviar — nunca en texto plano.

## Optimizar por compradores, no por clics

Una vez tienes el loop:

- **Optimiza la campaña por la conversión más profunda que puedas medir**: Compra > Lead calificado > Lead > AddToCart > Clic. Cada paso más profundo = mejor calidad (ver 14).
- En high-ticket, sube **"lead calificado"**, no "lead" (ver 58).
- **No le creas el número de la plataforma.** TikTok se sobre-atribuye (se cuelga ventas que no causó — ver 16). Cruza siempre con tus ventas reales: pedidos en `data/orders.json`, ventas en tu dashboard, plata en la cuenta.
- El **ROAS real** (ver 64) es el que importa, no el reportado. Modelo de atribución: revisa la ventana (click/view) y compara con el modelo de Meta/Google para no comparar peras con manzanas (ver 16).

Regla de oro: **el dato que vale es la venta confirmada en tu sistema**, no el evento que reporta TikTok. La plataforma es juez y parte.

## Checklist de medición antes de escalar

1. ¿Pixel **y** Events API instalados con deduplicación (`event_id`)?
2. ¿Capturas `ttclid` en el link a WhatsApp/landing?
3. ¿Subes la **compra real** (no el clic) de vuelta a TikTok?
4. ¿La calidad de match de eventos es buena en Events Manager?
5. ¿Optimizas por el evento más profundo medible?
6. ¿Cruzaste el ROAS reportado contra tus ventas reales esta semana?

Si alguna es "no", arréglala antes de subir presupuesto.

## Rutas a skills hermanas

- Instalación técnica de pixel/Events API → 05, 06.
- ROAS real, atribución, unit economics → 64, 16, `economist_lushows`.
- Captura del `ttclid` en el handoff → 55.
- Equivalente de cierre de loop en Meta (`ctwa_clid` / CAPI) → `facebook_ads_lushows`; en Google (OCI / Enhanced Conversions) → `google_ads_lushows`.

## Errores comunes — blacklist

- **Optimizar por clic cuando cierras por WhatsApp.** Atraes curiosos; sube la compra vía Events API (loop cerrado).
- **Confiar solo en el pixel.** Se cae por iOS/bloqueadores; usa Events API server-side con deduplicación (ver 06).
- **No capturar el `ttclid` en el link.** No puedes cerrar el loop; pierdes la optimización por compra (ver 55).
- **No subir la venta de WhatsApp/offline de vuelta a TikTok.** El algoritmo nunca aprende quién compra.
- **Creerle el ROAS de la plataforma.** Se sobre-atribuye; valida con ventas reales (ver 16, 64).
- **Optimizar por evento superficial (ViewContent) en high-ticket.** Optimiza señal pobre; usa lead calificado (ver 58).
- **No revisar la calidad de match de eventos.** Señal pobre arruina la optimización; mídela en Events Manager.
- **Mandar PII sin hashear.** Riesgo y rechazo; hashea email/teléfono antes de enviar.

# 62 — Events Manager y debugging

Lee este módulo cuando tus conversiones no aparecen o aparecen menos de las reales, cuando montaste el píxel pero no sabes si "funciona", o cuando antes de culpar al creativo necesites confirmar que la medición no está rota. El Events Manager de TikTok es el panel donde compruebas que tus eventos (ver producto, agregar al carrito, compra, lead) **sí están llegando, sí están bien matcheados y no están duplicados**. Una campaña que "no convierte" muchas veces sí convierte: el píxel no lo reporta, así que el algoritmo optimiza a ciegas (ver 14) y el CPA del panel miente hacia arriba. Audita esto ANTES de tocar la campaña (ver 61). Es el cinturón de seguridad de toda la cuenta.

## Las tres preguntas del debugging

Para cada evento de conversión, responde estas tres en el Events Manager. Si alguna falla, tu optimización está corriendo a ciegas.

| Pregunta | Dónde se ve | Qué significa |
|---|---|---|
| ¿El evento **llega**? | Pestaña "Test Events" en tiempo real | El píxel/Events API disparan al hacer la acción |
| ¿**Matchea** bien al usuario? | Event Matching Quality (EMQ), score 1–10 | Cuántos datos (email, teléfono, IP) ayudan a TikTok a atribuir |
| ¿Está **duplicado**? | Conteo vs ventas reales / alerta de dedup | Píxel + Events API contando la misma compra dos veces |

Mnemónico: **Llega → Matchea → No se duplica**. En ese orden, porque un evento que no llega no se puede matchear, y uno mal matcheado no vale la pena deduplicarlo.

## Test Events: ¿el evento llega?

**Test Events** es la herramienta de prueba en vivo. Abres la pestaña, navegas tu propia landing como un cliente (ver producto → carrito → compra de prueba) y debes ver cada evento aparecer en segundos.

Pasos exactos:

1. Events Manager → tu píxel/dataset → pestaña **Test Events**.
2. En otra ventana, entra a tu landing desde el enlace real con UTMs (ver 66).
3. Haz el recorrido completo: `ViewContent` → `AddToCart` → `InitiateCheckout` → `CompletePayment` (o tu evento clave, ver 14).
4. Cada acción debe aparecer en Test Events en 1–30s, con su nombre exacto y sus parámetros (valor, moneda `COP`, content_id).

Si **no aparece**: el píxel no está instalado en esa página, el evento no se dispara, o el código tiene un error (rutea la instalación a `desingweb-lushows` / quien montó la web). Si aparece **el genérico (`PageView`) pero no la compra**: el evento de conversión específico no está mapeado — ese es el que de verdad importa, no el PageView. Si aparece la compra pero **sin `value` ni `currency`**: tu ROAS y tu GMV van a salir en cero o mal; revisa que el evento mande el monto en COP.

### Tabla de síntomas en Test Events

| Lo que ves | Causa probable | Fix |
|---|---|---|
| No aparece nada | Píxel no instalado en esa página | Reinstalar (rutea `desingweb-lushows`) |
| Solo PageView | Evento de conversión sin mapear | Mapear `CompletePayment` (ver 14) |
| Compra sin value/currency | Parámetros faltantes | Enviar value + currency COP |
| Llega doble cada acción | Píxel duplicado en el código | Quitar la etiqueta repetida |
| Llega con retraso de minutos | Solo server-side lento | Normal; confirma en reportes después |

## Event Matching Quality (EMQ): ¿matchea bien?

El **EMQ** es un puntaje de 1 a 10 que mide cuántos datos del cliente le pasas a TikTok para atribuir la conversión a la persona correcta. Más datos = mejor atribución = optimización más fina y CPA real más bajo. Es la versión TikTok del "EMQ" de Meta (que vive en `facebook_ads_lushows`).

| EMQ | Lectura | Qué hacer |
|---|---|---|
| 8–10 | Excelente | Mantén; pasas email/teléfono/IP/user-agent hasheados |
| 5–7 | Mejorable | Agrega más parámetros (email, teléfono) vía Events API |
| 1–4 | Pobre | Atribución débil; el algoritmo aprende mal. Prioriza arreglarlo |

Cómo subirlo: enviar parámetros adicionales (email, teléfono, dirección, external_id) **hasheados** (cifrados con SHA-256, no en texto plano) desde la **Events API** del lado del servidor (ver 06). El píxel solo (lado navegador) pierde datos por bloqueadores, iOS y rechazo de cookies; la Events API recupera esas señales porque dispara desde tu servidor, no desde el navegador del usuario. En LatAm con cierre por WhatsApp, el dato más valioso para matchear suele ser el **teléfono** — asegúrate de capturarlo y enviarlo hasheado.

Impacto real: subir el EMQ de 4 a 8 puede bajar tu CPA reportado un 10–25% **sin tocar nada más**, porque TikTok atribuye conversiones que antes perdía y aprende mejor a quién mostrar el ad.

## Deduplicación: píxel + Events API sin contar doble

Lo correcto en 2026 es enviar cada evento por **dos vías**: el píxel (navegador) y la Events API (servidor). Esto da cobertura máxima (ver 06). El riesgo: contar la misma compra dos veces → CPA y ROAS falsamente buenos, y el algoritmo optimiza hacia un espejismo.

La solución es el **`event_id`**: un identificador único por evento. Si el píxel y la Events API mandan la MISMA compra con el MISMO `event_id`, TikTok entiende que es una sola y la cuenta una vez. Es la deduplicación. (También se usa `event_time` cercano como señal de apoyo, pero el `event_id` es el que manda.)

Checklist de dedup:

- [ ] Cada evento de compra/lead lleva un `event_id` único (ej. el número de orden).
- [ ] El píxel y la Events API usan **el mismo** `event_id` para el mismo evento.
- [ ] En Events Manager no hay alerta de "eventos duplicados".
- [ ] El conteo de compras del panel ≈ las ventas reales del backend (no el doble).
- [ ] El evento manda `value` + `currency` (COP) para que ROAS/GMV sean reales.

Si ves el doble de conversiones de las ventas reales: casi seguro falta el `event_id` compartido. Quien programó el envío (rutea a `desingweb-lushows` / dev) debe igualar ese ID en ambas vías.

## Rutina de auditoría mensual (10 minutos)

Una vez al mes, no esperes a que algo se rompa:

1. **Test Events**: haz una compra de prueba, confirma que `CompletePayment` llega con value/currency.
2. **EMQ**: revisa el score; si bajó de 7, algo dejó de mandar parámetros.
3. **Dedup**: compara conteo de compras del panel vs órdenes del backend de la semana. ¿Cuadran ~1:1?
4. **Cobertura**: ¿qué % de eventos llega por server-side (Events API) vs solo navegador? En 2026 quieres la mayoría por server.
5. **Alerta**: configura un aviso de "0 eventos en 6h con gasto activo" (ver 69) — eso te salva un fin de semana de gasto ciego.

## Errores comunes — blacklist

- **Culpar al creativo cuando el píxel no mide.** Audita Events Manager antes de tocar la campaña (ver 61).
- **Tener PageView pero no el evento de compra.** Optimizas a una señal que no es la venta. Mapea el evento clave (ver 14).
- **Mandar datos sin hashear.** Violas privacidad y TikTok los rechaza. Hashea email/teléfono con SHA-256 (ver 06).
- **Píxel + Events API sin `event_id` común.** Cuentas doble; el ROAS miente. Comparte el ID.
- **Conformarte con EMQ de 3.** La atribución es pobre y el algoritmo aprende mal. Sube parámetros vía servidor.
- **Compra sin value/currency.** Tu ROAS y GMV salen en cero o falsos. Manda el monto en COP.
- **No probar la landing real con UTMs.** Pruebas en una página que no es la del ad. Usa el enlace real (ver 66).
- **Asumir que "instalé el píxel" = "mide bien".** Instalar ≠ disparar el evento correcto. Compruébalo en Test Events.
- **No auditar nunca.** El píxel se rompe solo cuando cambian la web. Revisa cada mes.

# El píxel y la API de conversiones

> Vigencia: 14-sep-2026. **Configuración, públicos, atribución y optimización desde el lado de la
> plataforma: invoca `facebook_ads_lushows`.** Aquí va qué necesita **tu tienda** y por qué.

## Qué es cada cosa, en una línea

| Pieza | Qué hace |
|---|---|
| **Píxel** (navegador) | Un script en tu página que avisa a la plataforma qué hizo el visitante |
| **API de conversiones** (servidor) | Tu tienda le avisa directamente al servidor de la plataforma, sin pasar por el navegador |
| **Deduplicación** | El mecanismo que evita contar dos veces el mismo evento cuando llega por ambos caminos |

## Por qué ya no basta el píxel

El píxel vive en el navegador del cliente y el navegador dejó de ser confiable:

| Bloqueador | Efecto |
|---|---|
| Bloqueadores de anuncios | El script nunca se carga |
| Restricciones de rastreo de iOS / Safari | Eventos perdidos o degradados |
| Rechazo de cookies (obligatorio en la UE) | El píxel no puede disparar. `197` |
| Cierre de la pestaña antes de que cargue | Evento perdido |
| Página lenta | Evento perdido. `196` |

Resultado: sin la API de conversiones, pierdes una parte relevante de tus eventos, y los que pierdes
no son aleatorios: son sobre todo **compras**, que es lo que la plataforma necesita para optimizar.

**La consecuencia económica:** el algoritmo aprende con menos datos, encuentra peor a quien compra,
y tu CAC sube. No es un tema técnico: es dinero.

## La regla operativa

**Instala ambos y deduplica.** No es "píxel o API": es píxel **más** API, con el mismo identificador
de evento en los dos, para que la plataforma sepa que son el mismo hecho.

| Configuración | Resultado |
|---|---|
| Solo píxel | Pierdes eventos. CAC más alto |
| Solo API | Pierdes señales de navegación finas |
| **Ambos con deduplicación** | **Lo correcto** |
| Ambos **sin** deduplicación | Eventos duplicados, ROAS inflado, decisiones equivocadas |

El último caso es el peor de todos: crees que vas ganando y estás perdiendo.

## Qué necesita tu tienda (checklist)

1. **Un solo píxel por tienda.** Dos píxeles disparando el mismo evento es la causa más común de
   números duplicados.
2. **La app o integración oficial** de la plataforma, no un script pegado a mano en el tema.
3. **Consentimiento resuelto** si vendes en la UE: el píxel no dispara antes de aceptar. `197`.
4. **Los eventos correctos**, con los parámetros correctos. `201`.
5. **Deduplicación activa**, verificada en la herramienta de pruebas de la plataforma.
6. **Datos del cliente enviados** por la API (correo y teléfono, cifrados por la integración). Es lo
   que sube la calidad de la coincidencia. `201`.
7. **Verificación del dominio** en la plataforma. Sin eso, pierdes control de la configuración.
8. **TikTok y Google tienen su propio equivalente** (Events API, Enhanced Conversions). Si pautas
   ahí, aplica lo mismo. Invoca `tiktok_ads_lushows` o `google_ads_lushows`.

## Cómo se verifica que funciona

No confíes en que la app diga "conectado". Haz la prueba real:

1. Abre la herramienta de pruebas de eventos de la plataforma.
2. Entra a tu tienda desde el celular, con datos móviles.
3. Recorre: ver producto → añadir al carrito → iniciar checkout → **comprar de verdad**.
4. Verifica que cada evento aparezca **una sola vez**, y que la compra traiga el valor y la moneda
   correctos.
5. Verifica que la compra llegue por **ambos** canales y aparezca deduplicada.
6. Reembolsa la prueba.

Si el evento de compra llega con valor 0 o sin moneda, tu optimización por valor no funciona y el
ROAS que ves es ficción.

## Los errores que cuestan dinero

| Error | Qué provoca |
|---|---|
| Dos píxeles instalados | Conversiones duplicadas; escalas lo que no funciona |
| Evento de compra sin `value` ni `currency` | La plataforma no puede optimizar por valor |
| Moneda mal configurada (USD en tienda mexicana) | ROAS irreal por un factor de ~18 |
| Compra que dispara también al recargar la página de gracias | Conversiones infladas |
| Píxel bloqueado por el banner de cookies y sin API | Medición fantasma |
| API instalada pero sin `event_id` compartido | Duplicación |
| Evento de compra en el carrito y no tras el pago | Cuentas ventas que nunca ocurrieron |

## La calidad del evento

Las plataformas puntúan qué tan buenos son tus eventos. Esa puntuación depende de cuántos datos de
identificación mandas con cada uno. Subirla es de las intervenciones más rentables que existen
porque mejora la coincidencia y baja el CAC sin tocar el creativo. Detalle completo en `201`.

## El orden correcto de montaje

| # | Paso | Cuándo |
|---|---|---|
| 1 | Crear el activo de datos / píxel | Antes de montar la tienda |
| 2 | Verificar el dominio | Día 1 |
| 3 | Instalar la integración oficial | Día 1. `178` |
| 4 | Activar la API de conversiones | Día 1 |
| 5 | Configurar los eventos y sus parámetros | Día 1. `201` |
| 6 | Prueba real de compra y verificación | **Antes de encender pauta** |
| 7 | Revisar calidad de eventos a los 3 días | Con tráfico real |

Nunca enciendas una campaña sin haber completado el paso 6. Cada día de pauta con medición rota es
dinero que gastas a ciegas y datos que envenenan el aprendizaje del algoritmo.

## Relacionados
`201` eventos y calidad del evento · `199` analítica · `198` recuperación · `197` consentimiento · `196` velocidad

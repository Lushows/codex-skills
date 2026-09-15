# 05 — Google tag y GA4

Sin medición no hay pauta seria: el Smart Bidding aprende de tus conversiones, así que medir bien ES optimizar. Este módulo cubre cómo instalar el seguimiento (Google tag), qué es GA4 (la única analítica de Google desde que murió Universal Analytics en 2023), y la decisión que confunde a todos: ¿uso conversiones nativas de Ads o las importo de GA4? Lee esto en el setup (fase 2, ver 00), cuando "Google Ads no registra conversiones", o antes de elegir tu fuente de conversión.

## Las piezas: Google tag, GA4 y GTM

| Pieza | Qué es | Para qué |
|---|---|---|
| **Google tag (`gtag.js`)** | el código base que pones en tu sitio | manda datos a Google Ads y/o GA4 desde una sola etiqueta |
| **GA4 (Google Analytics 4)** | la **única** analítica de Google hoy (Universal Analytics murió en jul-2023) | mide comportamiento, eventos, embudos en tu web |
| **Google Tag Manager (GTM)** | "gestor de etiquetas" — caja para administrar tags sin tocar código cada vez | recomendado si vas a tener varios eventos/tags |
| **gclid** | identificador que Google pega a cada clic (auto-tagging) | conecta el clic con la conversión y con OCI (ver 53, 66) |

Para una web simple (una landing, un formulario): Google tag directo basta. Para algo con varios eventos (formularios, WhatsApp, compras, scroll): **GTM** te ahorra dolores — defines disparadores sin pedirle a un dev que toque el código cada vez. El **auto-tagging** (que genera el gclid) debe estar **activado** (lo está por defecto) — sin él, OCI y la atribución se rompen (ver 53, 66). Verifica en Configuración → Seguimiento que "Etiquetado automático" esté en ON.

## Cómo instalarlo (orden correcto)

1. Crea la **propiedad GA4** y obtén el ID de medición (`G-XXXX`).
2. Instala el **Google tag** en todas las páginas (vía GTM o directo en el `<head>`).
3. Vincula **GA4 ↔ Google Ads** (en GA4: Administrar → Vínculos de productos → Google Ads). Esto habilita importar conversiones y audiencias.
4. Define los **eventos clave** en GA4 y/o las **conversiones nativas** en Ads.
5. **Verifica en vivo** con GA4 DebugView y la Vista previa de GTM que los eventos disparan (ver 62). No lances sin esto.

## Eventos y conversiones en GA4

En GA4 todo es un **evento** (page_view, click, form_submit, purchase). Un evento se vuelve **conversión** ("evento clave") cuando lo marcas como importante.

| Acción en LatAm | Evento sugerido | ¿Conversión? |
|---|---|---|
| Clic a botón WhatsApp | `click_whatsapp` | secundaria (no es venta, ver 04) |
| Envío de formulario / lead | `generate_lead` | sí (principal si es lead-gen) |
| Compra checkout web | `purchase` (con `value` en COP y `currency: COP`) | sí, principal |
| Llamada desde la web | `phone_call` | sí o secundaria según negocio |
| Inicio de checkout / add_to_cart | `begin_checkout` / `add_to_cart` | secundaria (señal, no meta) |

Marca como **evento clave** solo lo que de verdad vale. GA4 + DebugView te deja verificar en vivo que el evento dispara con los parámetros correctos (ver 62). Pon SIEMPRE `value` y `currency` en `purchase` — sin valor no hay tROAS ni ROAS real (ver 64, 15).

## La decisión: conversión nativa de Ads vs importada de GA4

Hay dos formas de meterle conversiones a Google Ads. **Elige UNA por acción para no contar doble.**

| | **Nativa de Google Ads** (tag de conversión) | **Importada desde GA4** |
|---|---|---|
| Cómo | tag de conversión propio de Ads en la página de gracias | marcas evento clave en GA4 y lo importas a Ads |
| Atribución | data-driven de Ads | de GA4 (puede diferir del modelo de Ads) |
| Enhanced Conversions | ✅ soporta limpio (ver 06) | depende de config de GA4 |
| Latencia/fiabilidad | más directa, suele registrar antes | a veces más lenta / puede perder casos |
| Cuándo usarla | **lead-gen, ventas directas, lo crítico** | cuando ya vives en GA4 y quieres consistencia de reporte |

**Recomendación práctica para Lushows:** usa **conversión nativa de Google Ads** para lo crítico (lead/venta) porque registra más fiable y soporta Enhanced Conversions limpio. Usa GA4 para análisis de comportamiento y embudo. Si importas de GA4, **no dupliques** con la nativa la misma acción. Verifica en el reporte de conversiones que no haya dos acciones midiendo lo mismo (síntoma: tu CPA se ve la mitad de lo que es).

## Verificación post-instalación (no la saltes)

| Herramienta | Qué confirma |
|---|---|
| **GA4 DebugView** | el evento dispara con sus parámetros (value, currency) |
| **Vista previa de GTM (Tag Assistant)** | el tag se ejecuta en la página correcta |
| **Reporte de conversiones en Ads** | estado "Registrando conversiones / Recording" |
| **Diagnóstico de Enhanced Conversions** | estado "Registrando datos" (ver 06) |

Si lanzas sin verificar, descubres a fin de mes que no medías nada — y el Smart Bidding optimizó a ciegas todo ese tiempo.

## Errores comunes — blacklist

- **Contar la misma venta dos veces** (nativa de Ads + importada de GA4). Tu CPA se ve la mitad de bueno de lo que es y la puja se descalibra. Fix: una sola fuente por acción.
- **Buscar Universal Analytics.** Está muerto desde jul-2023; solo existe GA4. Fix: monta GA4 (ver arriba).
- **Desactivar el auto-tagging / pelear con gclid.** Rompes OCI y la atribución. Fix: déjalo activado (ver 66, 53).
- **Poner el tag de conversión en CADA página** en vez de en la de "gracias". Cuentas page_views como conversiones. Fix: dispara solo en el evento real (form enviado, compra hecha).
- **Marcar `click_whatsapp` como conversión principal.** Optimizas hacia curiosos. Fix: secundaria; la venta real entra por OCI (ver 04, 53).
- **No vincular GA4 con Google Ads.** Sin el vínculo no importas conversiones ni audiencias. Fix: hazlo en GA4 → Vínculos de productos.
- **Lanzar sin verificar en DebugView/Vista previa que el evento dispara.** Descubres a fin de mes que no medías nada. Fix: prueba en vivo antes de gastar (ver 62).
- **Olvidar el valor en COP en `purchase`.** Sin valor no hay tROAS ni ROAS real. Fix: pasa `value` y `currency: COP` en el evento (ver 64, 15).

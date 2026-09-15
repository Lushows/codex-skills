# 14 — Evento de optimización

El evento de optimización es la instrucción que le das al algoritmo: "tráeme gente que haga ESTO". Es la palanca más importante después del objetivo (ver 11). Lee este módulo cuando configures un ad set nuevo, cuando estés en learning limited crónico (ver 13), o cuando tus leads/compras lleguen baratos pero basura.

## La regla central

**Optimiza por el evento más cercano al dinero que tu volumen aguante.** El algoritmo necesita ~50 eventos/semana por ad set para aprender (ver 13). Si tu evento ideal (Purchase) no llega a eso, sube UN escalón en el funnel y acepta el trade-off. No bajes dos escalones de golpe "por si acaso": cada escalón abajo es calidad que pierdes.

## La escalera del e-commerce (de mejor a peor)

```
Purchase → InitiateCheckout → AddToCart → ViewContent → LandingPageView → Clic
  ($$$)        (proxy bueno)     (proxy ok)   (proxy débil)    (casi tráfico)  (no)
```

Cada escalón arriba = **más volumen, menos calidad**: optimizas por un *proxy* (señal sustituta) y Meta te trae gente que hace el proxy, no necesariamente la compra. Alguien que agrega al carrito no siempre compra; alguien que solo mira, menos.

| Tus compras/semana | Optimiza por |
|---|---|
| ≥50 | Purchase, sin discusión |
| 20-50 | Purchase igual (learning limited rentable es normal) o InitiateCheckout si el CPA se descontrola |
| 5-20 | InitiateCheckout o AddToCart |
| <5 | AddToCart / ViewContent + revisa si tu problema es la oferta, no el evento (ver 41) |

**Migración a Purchase cuando creces**: no cambies el evento en el ad set andando (resetea, ver 13). Crea un ad set/campaña nueva optimizada a Purchase con 20-30% del presupuesto, déjala madurar 1-2 semanas, y migra presupuesto gradualmente (≤20%/72h) hasta apagar la del proxy.

## Por qué importa la frescura de la señal (CAPI 2026)

El algoritmo solo es tan bueno como la señal que le llega. En 2026, con view-through fuera del API (solo clic, ver 16) y más usuarios sin tracking de navegador, **la API de Conversiones (CAPI) servidor-a-servidor es obligatoria, no opcional**: es la que recupera los eventos que el píxel del navegador pierde. La métrica que vigila la calidad de ese matcheo es el **EMQ (Event Match Quality, 0-10)**; manda email, teléfono, nombre y `external_id` hasheados para subirlo a 7-9. EMQ bajo = el algoritmo optimiza medio a ciegas, y ningún evento "bien elegido" lo arregla (setup técnico en 22-23).

## Leads: form, web o evento calificado

1. **Instant form**: optimiza por envío de formulario dentro de Meta. Máximo volumen, calidad mínima.
2. **Lead en web**: evento Lead del píxel en tu landing. Mejor calidad (la fricción filtra), menos volumen.
3. **Lead calificado vía CAPI (el nivel pro)**: tu CRM marca cuáles leads fueron reales/calificados (contestó, agendó, tiene presupuesto) y lo envía a Meta por CAPI como evento custom (ej. `LeadCalificado`). Optimizas por ESE evento: Meta aprende a traerte leads que tu equipo de ventas quiere, no llenadores de formularios. Requiere ≥~25-50 calificados/semana para optimizar bien; si no llegas, úsalo al menos como métrica de verdad en reportes (ver 60). Setup técnico en 22-23; qué es un lead calificado y cómo trabajarlo: ventas_lushows.

## Mensajería (WhatsApp — el caso Colombia)

- Evento estándar: **conversaciones iniciadas** (alguien te escribe desde el anuncio). Es tu "lead".
- La calidad varía brutal según el creativo: un anuncio "escríbenos y pregunta lo que sea" trae curiosos; uno con precio visible trae compradores (ver 50). El creativo filtra antes que el algoritmo.
- Nivel pro: registrar la venta cerrada en WhatsApp como Purchase vía CAPI (manual o con tu bot — el bot de GastroWhats puede disparar el evento al confirmar pedido) y eventualmente optimizar por eso. Así Meta deja de traerte "buenos conversadores" y empieza a traerte "buenos compradores".

## Matriz volumen × calidad (resumen mental)

```
            CALIDAD ALTA                    CALIDAD BAJA
VOLUMEN     Purchase / LeadCalificado       —  (no existe ese cuadrante gratis)
ALTO        ← el paraíso, requiere escala
VOLUMEN     Purchase en cuenta chica        ViewContent / Tráfico / instant form
BAJO        (learning limited rentable)     sin filtros ← el cuadrante trampa
```

El cuadrante trampa se siente bien (métricas baratas, dashboard verde) y quiebra negocios.

## Value optimization y Minimum ROAS (optimizar por valor)

En vez de "máximo número de compras", pides "máximo VALOR de compra" (Meta prioriza gente de ticket alto). En 2026 se combina con las pujas **Minimum ROAS / ROAS Goal** y con **Value Rules** (reglas que le dicen a Meta cuánto vale más cierto cliente — ej. nuevos valen 1.3× porque buscas crecimiento), ver 15 y 64. Actívala solo si:
- catálogo con tickets que varían **≥3×** entre sí,
- **≥~50 compras/semana** con valor reportado correcto en el píxel/CAPI,
- te importa más ROAS que volumen de pedidos.

Si todos tus pedidos valen parecido, no aporta nada — quédate en optimización por número de compras.

## Tabla de decisión rápida

| Tu negocio | Evento que debes pedir |
|---|---|
| E-com ≥50 compras/sem | Purchase (+ value optimization si tickets dispares) |
| E-com 5-20 compras/sem | InitiateCheckout / AddToCart |
| Servicios con equipo de ventas | `LeadCalificado` (CAPI) si ≥25/sem; si no, Lead web + filtros |
| Venta por WhatsApp | Conversaciones iniciadas (→ Purchase-CAPI cuando midas cierres) |
| Lanzamiento sin data | AddToCart/ViewContent + arreglar oferta antes (ver 41) |

## Errores comunes — blacklist

- Optimizar por ViewContent teniendo 60 compras/semana "porque da más volumen": volumen de gente que mira vitrinas.
- Cambiar el evento dentro del ad set activo: reseteo total; crea uno nuevo y migra (ver 13).
- Instant forms sin preguntas de filtro y luego culpar a Meta por leads malos: pediste cantidad, te dieron cantidad.
- Optimizar conversaciones de WhatsApp y medir éxito por número de chats: mide ventas cerradas (tasa de cierre, ver ventas_lushows y 16).
- Evento Purchase disparándose en la página de "gracias" recargada o en pagos fallidos: señal sucia entrena mal al algoritmo (auditoría de píxel en 21).
- EMQ bajo (< 6) y creer que el problema es el evento: primero limpia la señal CAPI (ver 22-23), luego juzga.
- Saltar a value optimization / Minimum ROAS sin valores reales en los eventos: optimizas por números inventados.

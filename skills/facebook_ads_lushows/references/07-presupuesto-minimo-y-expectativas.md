# 07 — Presupuesto mínimo y expectativas honestas

Antes de poner un peso en Meta hay que hacer una cuenta de servilleta que casi nadie hace: ¿alcanza tu presupuesto para que el sistema aprenda, y aguanta tu margen el costo por venta realista? Lee este módulo en el diagnóstico (fase 1 del 00) y cada vez que un cliente pregunte "¿con 200.000 COP al mes sí funciona?".

## La matemática de la learning phase

La **learning phase** (fase de aprendizaje) es el periodo en que Meta todavía está descubriendo a quién mostrarle tu anuncio. Para estabilizar, el sistema necesita **~50 conversiones por semana POR ad set** (del evento por el que optimizas). Menos que eso = **learning limited**: la entrega funciona, pero con rendimiento errático y generalmente más caro (ver 13).

La fórmula del presupuesto mínimo teórico:

```
Presupuesto semanal mínimo ≈ 50 × CPA esperado
```

Ejemplos en COP (CPAs ilustrativos jun-2026 — varían por vertical/país/oferta):

| Evento de optimización | CPA esperado (ej.) | Mínimo/semana | Mínimo/día |
|---|---|---|---|
| Compra e-commerce Colombia | 40.000 COP | 2.000.000 COP | ~285.000 COP |
| Compra producto digital barato | 15.000 COP | 750.000 COP | ~107.000 COP |
| Conversación WhatsApp iniciada (CTWA) | 3.000–6.000 COP | 150.000–300.000 COP | ~21.000–43.000 COP |
| Lead (formulario nativo) | 8.000–14.000 COP | 400.000–700.000 COP | ~57.000–100.000 COP |

## Benchmarks de costo por resultado en Colombia (jun-2026, orientativos)

Para calibrar (suben en Q4, ver 77; bajan con creativo fuerte):

| Resultado | Rango típico COP |
|---|---|
| Conversación CTWA iniciada | 2.500 – 7.000 |
| Lead nativo (Advantage+ Leads) | 6.000 – 16.000 |
| Compra e-commerce ticket 80-150k | 30.000 – 70.000 |
| ROAS e-commerce sano (atribuido) | 2.0 – 4.0 (broad, prospecting) |

No son garantías: una oferta floja con creativo malo puede triplicar estos números, y un ganador con buen EMQ puede mejorarlos. Son brújula, no promesa.

## CBO vs ABO y la consolidación en cuentas chicas

Con la unificación Advantage+ (feb-2026), el presupuesto a nivel campaña (CBO / Advantage+ budget) es el default y para cuentas chicas es lo correcto: deja que Meta reparta entre tus pocos ad sets sin que tú lo fragmentes a mano. El ABO (presupuesto por ad set) se reserva para testing controlado cuando ya tienes volumen para que CADA ad set junte sus 50/semana (ver 17). Repartir presupuesto a mano en una cuenta chica es justo lo que mata la learning phase: terminas con cinco ad sets en learning limited en vez de uno aprendiendo. Menos cajas, más comida por caja.

## Si no te alcanza: optimiza más arriba del funnel

¿No puedes pagar 50 Purchases/semana? **Sube un escalón en la jerarquía de eventos** hasta donde sí te alcancen 50/semana: Purchase → InitiateCheckout → AddToCart → conversación de WhatsApp/Lead. Pierdes precisión (optimizas por intención, no por compra) pero ganas un sistema que aprende. Detalle en 14.

Alternativa válida: **aceptar learning limited** con un solo ad set broad y creativos fuertes. Una cuenta chica en learning limited con UN ad set rinde más que la misma plata repartida en cinco. Por eso la regla de oro de cuentas pequeñas: **consolidar** (1 campaña Advantage+ Sales, 1 ad set, 10-15 ads, ver 00, 03).

En LatAm esto explica por qué las campañas CTWA (Click-to-WhatsApp) dominan en pymes: el evento "conversación iniciada" es barato, juntas 50/semana con presupuestos chicos, y el cierre lo remata un humano por chat o el Meta Business Agent (ventas_lushows, ver 50, 53).

## Presupuesto de testing: las primeras semanas son compra de datos

Mentalidad correcta: el dinero del mes 1 **compra información, no utilidades**. Destina un bloque para testear (regla práctica: por cada creativo/ángulo a probar, presupuesta 2-3× tu CPA objetivo antes de juzgarlo; testear 4 ángulos con CPA objetivo de 40.000 COP ≈ 320.000-480.000 COP solo de test, ver 17, 18). Quien entra esperando ROAS positivo en la semana 1 abandona justo cuando el sistema empezaba a aprender. Y como los creativos fatigan en 2-4 semanas (ver 39), el presupuesto de testing nunca llega a cero: es una línea fija del mes.

## Expectativas por fase (cuenta nueva)

| Fase | Qué pasa | Qué medir | Qué NO hacer |
|---|---|---|---|
| **Mes 1 — aprender** | CPA errático, learning phase, descubres qué ángulo creativo jala | Señal técnica OK (dataset/CAPI/EMQ 8+, ver 05-06), CTR y costo por conversación/lead | Juzgar ROAS, apagar todo a la semana |
| **Mes 2 — estabilizar** | Ganadores claros, CPA converge, matas perdedores | CPA vs tu CPA máximo permitido, frecuencia | Escalar agresivo todavía |
| **Mes 3 — escalar** | Subes presupuesto 20-30% cada 2-3 días sobre lo estable | ROAS/MER e incrementalidad, CPA marginal al escalar | Esperar que el CPA se mantenga idéntico al 2-3× de gasto (sube algo: normal) |

Caveat honesto: hay cuentas que pegan en la semana 2 y cuentas que necesitan 3 rondas de creativos. Los rangos varían por vertical, país, oferta y calidad creativa. Lo que no varía: nadie escapa de la fase de compra de datos.

## Cómo presentarle el presupuesto a un cliente (guion honesto)

El error comercial clásico es prometer rentabilidad inmediata para cerrar el cliente; luego no se cumple y pierdes la cuenta en el mes 2. El framing correcto, en COP:

1. **Piso técnico**: "Para que el algoritmo aprenda necesitamos ~50 resultados/semana. Con un costo por conversación estimado de 5.000 COP, eso son ~1.500.000 COP/mes solo en pauta. Por debajo de eso el sistema nunca estabiliza."
2. **Separar pauta de honorarios**: la pauta la paga el cliente directo a Meta (su tarjeta, ver 04); tu fee es aparte (ver 95). Que nunca se confundan.
3. **Mes 1 = inversión en datos**: "El primer mes compramos información: descubrimos qué creativo y qué oferta jalan. La utilidad llega cuando matamos perdedores y escalamos ganadores, típicamente mes 2-3."
4. **Rango, no promesa**: das benchmarks (arriba) como brújula y dejas claro que dependen de oferta, creativo y cierre — variables que se trabajan juntos.

Un cliente que entiende esto aguanta el mes 1; uno al que le prometiste ROAS 5 en la semana 1 se va decepcionado aunque la cuenta vaya bien.

## Cuándo NO pautar todavía (semáforo rojo)

- **El margen no da**: si margen bruto por venta < CPA realista del vertical, cada venta te empobrece. Primero arregla precio/costos → **economist_lushows** (unit economics).
- **La oferta no está validada**: nadie la ha comprado nunca (ni orgánico, ni conocidos). Meta amplifica; no convierte una oferta muerta en viva. Valida con 10-20 ventas manuales primero (cierre → ventas_lushows).
- **El cierre está roto**: WhatsApp que responde a las 6 horas, web caída, sin inventario, sin quién despache contraentrega. Pagar por tráfico hacia un embudo roto es regalarle plata a Meta. La ventana de 72h gratis del CTWA se desperdicia si nadie contesta rápido (ver 50).
- **Sin medición**: dataset/CAPI no instalados (ver 05-06). Primero la señal, luego el gasto.

## Errores comunes — blacklist

- **Repartir 30.000 COP/día entre 4 ad sets**: cuatro aprendices muertos de hambre; uno bien alimentado los supera siempre.
- **Optimizar por Purchase con presupuesto de Lead**: 6 compras/semana no enseñan nada; el sistema adivina y cobra caro por adivinar.
- **Juzgar la cuenta en la semana 1**: estás evaluando la fase de compra de datos con métricas de fase de rentabilidad.
- **Prometer (o creer) ROAS garantizado mes 1**: quien lo promete miente; el mes 1 es aprendizaje en casi cualquier vertical.
- **Pautar para "salvar" un negocio sin margen**: los ads escalan tu economía actual; si pierde plata por venta, perderá más rápido.
- **Resetear el aprendizaje a diario con cambios**: cada edición significativa devuelve el ad set a learning; decide máximo 2 veces por semana (ver 00, 70).
- **Confundir learning limited con fracaso**: en cuentas chicas es estado normal; se gestiona consolidando, no apagando.
- **No presupuestar la línea fija de testing**: sin munición creativa nueva, la cuenta muere cuando fatigan los ganadores (ver 39).

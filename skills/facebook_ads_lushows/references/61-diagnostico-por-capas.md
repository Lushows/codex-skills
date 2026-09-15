# 61 — Diagnóstico por capas: "mis ads no venden"

El módulo de rescate. Cuando la pauta no funciona, el funnel se rompe en UNA capa específica — y cada capa tiene un fix distinto. El error mortal es cambiar todo a la vez (nuevo creativo + nueva audiencia + nuevo presupuesto): nunca sabrás qué estaba roto, y reinicias el aprendizaje a cambio de nada. Este método aísla la capa rota en 15 minutos con los datos que ya tienes en Ads Manager (configúralo primero, ver 63). Actualizado jun-2026.

Prerequisito absoluto: medición confiable. Si el píxel (hoy **Dataset**, ver 62) / CAPI está roto, todo diagnóstico es ficción — optimizas y juzgas sobre números inventados (ver 62 PRIMERO, siempre).

## El árbol de decisión

```
¿Mis ads no venden?
│
├─ 0. ¿La MEDICIÓN está sana? (Events Manager: Purchase con value/currency,
│       EMQ ≥8, dedup ok, volumen ≈ pedidos reales ±20–30%, ver 62)
│   ├─ NO → arregla esto ANTES de diagnosticar nada más. Todo lo demás miente.
│   └─ SÍ → baja a la capa 1.
│
├─ 1. ¿CPM anormalmente ALTO? (vs tu histórico o vs otras campañas tuyas)
│   ├─ SÍ → problema de CUENTA/SUBASTA, no de creativo:
│   │       audiencia demasiado estrecha, temporada (Q4, fechas pico),
│   │       calidad de cuenta baja o creativo penalizado (ver 76, 77).
│   │       FIX: ampliar audiencia, revisar Account Quality, esperar/ajustar puja.
│   └─ NO → baja a la capa 2.
│
├─ 2. ¿CPM ok pero CTR outbound BAJO? (<0.5% sostenido)
│   ├─ SÍ → problema de CREATIVO: el hook no detiene o la promesa no mueve
│   │       (ver 37 hooks, 39 fatiga si ANTES funcionaba y decayó).
│   │       FIX: nuevos hooks/ángulos, no toques landing ni presupuesto.
│   └─ NO → baja a la capa 3.
│
├─ 3. ¿CTR ok pero CVR BAJA? (clics que no compran / chats que no piden)
│   ├─ SÍ → problema DESPUÉS del clic:
│   │       (a) landing incongruente con el ad — promete X, aterriza en Y
│   │           (ver 48; si la landing es el problema → desingweb-lushows CRO),
│   │       (b) oferta floja — nadie la quiere a ese precio (ver 41),
│   │       (c) tráfico curioso — objetivo de campaña mal elegido, p.ej.
│   │           "tráfico" o "interacción" en vez de conversiones (ver 11),
│   │       (d) cierre de chat lento/ausente si es WhatsApp → ventas_lushows.
│   └─ NO → baja a la capa 4.
│
├─ 4. ¿CVR ok pero CPA alto IGUAL?
│   ├─ SÍ → MATEMÁTICA IMPOSIBLE: tu ticket/margen no aguanta el CPM
│   │       de tu mercado. Ningún creativo lo arregla.
│   │       FIX: subir AOV (combos), subir precio, recortar costos
│   │       (economist_lushows), o volumen insuficiente: el ad set no
│   │       sale de aprendizaje (~50 conversiones/semana, ver 13).
│   └─ NO → baja a la capa 5.
│
└─ 5. ¿Todo "ok" en plataforma pero el banco no lo ve?
    └─ (a) atribución inflada: Meta se atribuye ventas que igual pasaban
           (7d-click/1d-view + modeled; view-through casi extinto en 2026,
           ver 16, 64, 65),
       (b) cierre de chat roto: los leads llegan a WhatsApp y se enfrían
           o nadie responde a tiempo → ventas_lushows + 53,
       (c) devoluciones/contraentrega fallida comiéndose la "venta" (ver 64).
```

## Tabla síntoma → capa → módulo → acción

| Síntoma | Capa rota | Ver módulo | Primera acción |
|---|---|---|---|
| Purchase ≠ pedidos reales / EMQ bajo | Medición | 62 | Auditar Events Manager antes que nada |
| CPM 2–3× tu histórico | Entrega | 76, 77 | Ampliar audiencia; revisar Account Quality |
| CTR <0.5% desde el día 1 | Creativo | 37, 68 | 3–5 hooks nuevos, mismo cuerpo |
| CTR cayó tras semanas buenas | Fatiga | 39 | Refrescar creativo, revisar frequency |
| Clics buenos, 0 compras | Landing/oferta | 48, 41 | Congruencia ad↔landing; test de oferta |
| Muchos chats, pocos pedidos | Cierre | ventas_lushows, 53 | Auditar tiempos de respuesta y guion |
| CPA alto con todo "normal" | Matemática | 13, economist | Calcular breakeven ROAS (ver 64) |
| Ads Manager dice ROAS 4, banco plano | Atribución | 64, 65 | Calcular MER; test de pausa de retargeting |

## Cómo aislar cada capa con NÚMEROS (no con intuición)

El método es restar expectativa vs realidad capa por capa. Para cada una ten a mano TU rango normal (de tu hoja semanal, ver 69) y el del mercado:

1. **Entrega**: CPM actual ÷ CPM histórico. Si el cociente >1.5 sostenido y otras campañas tuyas están normales, es subasta/cuenta. Si TODAS subieron parejo, es temporada (no es "tu culpa", ajusta expectativa).
2. **Atención**: CTR outbound actual vs 0.5–2%. Aísla con thumbstop: CTR bajo + thumbstop bajo = hook muerto; CTR bajo + thumbstop alto = el hook para pero el cuerpo/CTA no convence (ver 68).
3. **Conversión**: CVR = compras ÷ clics. Compárala contra 1–3% (e-com) o contra tu cierre histórico de chat. Una CVR de 0.3% con CTR sano grita "el problema está DESPUÉS del clic".
4. **Negocio**: CPA real vs CPA máximo (= margen bruto por pedido). Si CPA > margen, no hay creativo que salve la matemática.

## Ejemplo resuelto con números

Tienda de suplementos en Bogotá, COP $200.000/día, "no vende":
- Medición (capa 0): Purchase llega con value/currency, EMQ 8, volumen ≈ pedidos → OK.
- CPM $18.000 (su histórico: $15–20k) → capa 1 OK.
- CTR outbound 1.3% → capa 2 OK, el creativo trabaja.
- 144 clics/día, 1 compra cada 2 días → CVR 0.35% (esperable: 1–2%) → **capa 3 ROTA**.
- Revisión: el ad promete "envío gratis hoy", la landing cobra envío y carga 6 segundos en celular.
- Fix: congruencia de promesa + velocidad (desingweb-lushows). Dos semanas después: CVR 1.4%, CPA pasa de $400.000 a $99.000. No se tocó ni audiencia ni creativo.

Lección: con CTR 1.3% el instinto era "hacer más videos". Habría sido plata quemada arreglando una capa sana.

## Segundo ejemplo: la trampa de la capa 5

Marca de cosméticos, Ads Manager dice ROAS 4.2, el dueño está feliz. Pero el banco muestra ventas planas mes a mes mientras el gasto subió 60%. Capas 1–4 todas "ok". El problema vive en la capa 5: el 40% del gasto está en retargeting que se auto-atribuye ventas que pasaban igual (ver 65), y un 8% de las "ventas" eran contraentregas rechazadas. MER real: 2.1, no 4.2. Fix: test de pausa de retargeting (ver 65) + restar devoluciones del backend (ver 64). El creativo y la landing estaban perfectos — el problema era de lectura, no de pauta.

## Reglas del método
1. Diagnostica con 7 días de datos mínimo (3–4 si el gasto es alto); un día es ruido.
2. Cambia UNA capa a la vez y espera resultados antes de tocar otra.
3. Compara contra TU histórico, no contra benchmarks ajenos.
4. Si dos capas parecen rotas, arregla la más profunda primero: **medición (0) > matemática (4/5) > conversión (3) > creativo (2)**. No tiene sentido cambiar el hook si el Purchase ni siquiera se está midiendo.
5. La venta por WhatsApp se diagnostica con DOS pares de ojos: Ads Manager (clic→conversación) y el CRM de chat (conversación→pedido cerrado, ver 53). El hueco entre ambos suele ser la capa 3/5 disfrazada de "Meta no funciona".

## Errores comunes — blacklist
- Cambiar creativo, audiencia y presupuesto el mismo día ("escopetazo").
- Diagnosticar con el píxel/Dataset roto o deduplicación fallida (ver 62).
- Culpar al creativo cuando la CVR es el problema (el caso más frecuente, lejos).
- Ignorar la capa 4: ningún media buyer salva un producto cuyo margen no aguanta el CPM del mercado.
- Reiniciar campañas "para resetear" — pierdes el aprendizaje acumulado sin arreglar nada.
- Diagnosticar la venta por WhatsApp mirando solo Ads Manager: el dato de cierre vive en tu chat/CRM (ver 53).
- Saltarte la capa 0: el 30% de los "mis ads no venden" son en realidad "mi medición está rota y todo lo que veo es ficción".

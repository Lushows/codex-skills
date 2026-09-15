# Presupuestos y cómo subirlos

> **Frontera**: cómo se configura un presupuesto (CBO/ABO, topes, programación) es mecánica de
> plataforma. **Para el detalle de configuración, invoca `facebook_ads_lushows`** o
> `tiktok_ads_lushows`. Aquí va el criterio de negocio: **cuánto poner, con qué plata, y a qué ritmo
> subirlo sin romper el margen ni la caja**.

## El presupuesto sale de la caja, no del optimismo

Tres números antes de abrir la plataforma:

| Número | Cómo se saca | Ejemplo México dic-2026 |
|---|---|---|
| Capital de riesgo | Lo que puedes perder entero sin cambiar tu vida | USD 450 |
| Reserva de inventario | Stock local a reponer | USD 200 (44%) |
| Presupuesto de pauta | Capital − reserva − colchón operativo | USD 200 |
| Colchón operativo | Dominio, pasarela, empaque, imprevistos | USD 50 |

Con USD 200 de pauta y USD 15/día tienes **13 días de vida**. Ese es tu reloj. Todo el plan de test
(`242`) tiene que caber dentro de él.

## El piso: cuánto es "demasiado poco"

| Presupuesto diario | Qué puedes hacer | Veredicto |
|---|---|---|
| < USD 5 | Nada útil | No empieces |
| USD 5-10 | 1-2 ángulos, decisión lenta (7-10 días) | Mínimo viable, doloroso |
| USD 10-20 | 2-3 ángulos, decisión en 4-6 días | **Arranque razonable en LatAm** |
| USD 20-50 | 3-5 ángulos, decisión en 3-4 días | Cómodo |
| USD 50+ | Test + escala + retargeting a la vez | Profesional |

Referencia dura: con CPM de México (4,50), USD 15/día ≈ 3.300 impresiones diarias. A CTR 2%, 66
clics. A CVR 3%, **2 pedidos al día**. Con eso ya se decide. Con USD 5/día son 0,66 pedidos/día: no
se decide nada, solo se sangra.

## La regla del CPA: el presupuesto diario que tiene sentido

Un conjunto necesita generar señal. El piso operativo es que el presupuesto diario permita **2-3
conversiones al día** o, si no, que al menos gaste **1x el CPA objetivo diario**.

| CAC objetivo | Presupuesto diario mínimo por conjunto |
|---|---|
| USD 5 | 10-15 |
| USD 10,54 (modelo México) | 20-30 |
| USD 20 | 40-60 |
| USD 30 | 60-90 |

Si no te alcanza para ese piso, **reduce el número de conjuntos**, no el presupuesto por conjunto.

## Cómo subir sin romper nada

| Método | Incremento | Cuándo usarlo | Riesgo |
|---|---|---|---|
| Suave | +10-20% cada 48-72 h | Lo normal | Bajo; lento |
| Agresivo | +30-50% cada 24-48 h | Ganador claro, temporada alta | Medio: CPA salta |
| Duplicar de golpe | +100% | Solo con holgura > 2,5x y stock sobrado | Alto |
| Bajar | -20-30% | CPA sobre objetivo 3 días | Bajo |

Principio: **el sistema de entrega reacciona a cambios grandes como si fueran campañas nuevas**. Cada
salto grande te devuelve a exploración, con CPA alto durante 1-3 días. El detalle de por qué y cómo
lo maneja cada plataforma, en `facebook_ads_lushows`.

## Tabla de decisión diaria (la que se mira a las 9 a. m.)

| CPA de ayer vs CAC objetivo | Días seguidos | Acción |
|---|---|---|
| 40%+ por debajo | 2 | +25-30% |
| 10-40% por debajo | 3 | +15-20% |
| En el objetivo ±10% | — | No tocar |
| 10-30% por encima | 2 | Mantener y meter creativo nuevo (`263`) |
| 30-60% por encima | 3 | -25% y revisar diagnóstico (`267`) |
| Sobre el techo de CAC | 2 | Apagar (`268`) |

## Caja: la trampa que quiebra tiendas rentables

La pauta se paga **hoy**; el dinero de la venta entra en 2-14 días según pasarela. Con prepago en
México y liquidación semanal, puedes estar vendiendo con margen y aun así quedarte sin efectivo.

| Variable | Efecto en caja |
|---|---|
| Liquidación a 7 días | Necesitas financiar ~7 días de pauta |
| Liquidación a 14 días | ~14 días de pauta + inventario |
| MSI en Buen Fin | El cliente paga a plazos, tú cobras completo del adquirente, pero la comisión sube 3-8 puntos |
| Reposición de stock | Sale antes de que entre la venta |

Cálculo rápido de necesidad de caja: `pauta diaria × días de liquidación × 1,5`. Con USD 30/día y 7
días: USD 315 inmovilizados permanentemente. Si escalas a 100/día, son 1.050. **Escalar consume caja
aunque seas rentable.** Para modelar esto, invoca `Matematicas_lushows`.

## Presupuesto por etapa del proyecto

| Etapa | Duración | Diario | Reparto |
|---|---|---|---|
| Test de ángulos | 5-10 días | USD 15 | 100% test |
| Validación | 7-10 días | USD 20-25 | 70% ganador / 30% test |
| Escala temprana | 2-4 semanas | USD 30-70 | 65% escala / 20% test / 15% retargeting |
| Q4 / Buen Fin | Ver `274` | 2-4x lo normal | 60-70% del presupuesto del evento en la primera mitad |

Para eventos, la recomendación es clara: **adelanta el presupuesto**. El CPM sube 20-50% en Q4 y
50-80% en la semana de Black Friday, a veces sobre USD 50. Gastar el 70% antes del pico compra
impresiones más baratas y calienta el retargeting para el pico.

## Errores caros

1. **Subir presupuesto un viernes** y no mirarlo hasta el lunes: tres días a ciegas.
2. **Cambiar presupuesto todos los días**: el sistema nunca estabiliza.
3. **Subir por entusiasmo tras un día bueno**: un día no es señal (`266`).
4. **Presupuestar la pauta con el dinero del inventario**: vendes y no tienes qué mandar.
5. **No contar la comisión de pasarela ni el IVA** en el CAC objetivo: el ROAS de equilibrio real es
   más alto del que crees. Ver `11` y `42`.

## Relacionados
`242` estructura de test · `243` escalar · `266` métricas · `268` cuándo matar · `269` vertical y horizontal · `270` CPM de temporada · `274` calendario Q4

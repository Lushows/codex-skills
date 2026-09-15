# El tablero de números

## Para qué sirve

Un operador mira **10 números cada mañana**, en 5 minutos, y sabe si el negocio está bien. Todo lo
demás es curiosidad. Sin este tablero, las decisiones se toman por sensación y las sensaciones en
temporada alta son pésimas consejeras.

## Los 10 números del día

| # | Número | Fórmula | Fuente | Alarma |
|---|---|---|---|---|
| 1 | Inversión publicitaria | gasto total del día | plataforma | vs presupuesto planeado |
| 2 | Pedidos generados | pedidos que entraron | tienda | — |
| 3 | Pedidos cobrados | pagados y no reembolsados | banco / pasarela | — |
| 4 | Tasa de cobro | 3 ÷ 2 | cálculo | cae > 10 puntos |
| 5 | Ticket promedio | ingreso cobrado ÷ 3 | cálculo | cae > 10% |
| 6 | **CAC real** | 1 ÷ 3 | cálculo | sube > 25% |
| 7 | Techo de CAC | 5 − costos por pedido | modelo (`228`) | cambia con costos |
| 8 | **Holgura** | 7 ÷ 6 | cálculo | **< 1,3x** |
| 9 | ROAS real | ingreso cobrado ÷ 1 | cálculo | < equilibrio × 1,3 |
| 10 | **Caja disponible** | efectivo libre hoy | banco | < 25% del capital |

Los tres en negrita son los que deciden. Si solo pudieras ver tres números: **holgura, CAC real y
caja**.

## Dos números más para operaciones con inventario o COD

| # | Número | Fórmula | Alarma |
|---|---|---|---|
| 11 | Días de inventario | unidades en bodega ÷ ventas por día | < 7 o > 45 |
| 12 | Tasa de reembolso / devolución | devoluciones ÷ pedidos cobrados | > 5% |

## La hoja: una fila por día

```
fecha | inversion | ped_generados | ped_cobrados | tasa_cobro | ingreso_cobrado |
ticket_prom | CAC_real | techo_CAC | holgura | ROAS_real | caja | dias_inv | tasa_reembolso
```

Catorce columnas. Una hoja de cálculo basta. La disciplina de llenarla todos los días vale más que
cualquier panel bonito.

## Semáforo de decisión diaria

| Holgura | Caja | Acción |
|---|---|---|
| ≥ 2,0x | > 40% del capital | subir presupuesto 20-30% |
| ≥ 2,0x | 25-40% | mantener |
| 1,3 - 2,0x | cualquiera | mantener; arreglar oferta o creativo |
| < 1,3x | cualquiera | protocolo de 72 horas (`231`) |
| cualquiera | < 25% | bajar presupuesto 30-50% (`234`) |

## Lo que NO va en el tablero

| Métrica | Por qué no |
|---|---|
| Seguidores, likes, alcance | no pagan flete |
| ROAS del panel de Meta | infla; sirve para comparar conjuntos, no para decidir (`226`) |
| Visitas a la tienda | sin conversión es ruido |
| "Añadidos al carrito" | útil para diagnosticar, no para decidir |
| Ingresos brutos sin restar reembolsos | mentira contable |
| CPA reportado por la plataforma | no es tu CAC real (`224`) |

**El tablero se llena con datos del banco y de tu tienda, no del panel de anuncios.**

## Ritmo de revisión

| Frecuencia | Qué se mira |
|---|---|
| Diario (5 min) | los 10 números, semáforo, decisión de presupuesto |
| Semanal (30 min) | CAC real de la semana, recalcular techo (`228`), fatiga de creativos |
| Quincenal | costos puestos en bodega (tipo de cambio, flete), reposición |
| Mensual | impuestos apartados, reparto reinversión/retiro (`235`, `236`) |

## Cómo se ve un día bueno y uno malo

### Día bueno (México, bundle)
```
inversion 120 | generados 21 | cobrados 20 | cobro 95%
ingreso 1.201 | ticket 60,05 | CAC 6,00 | techo 30,72 | holgura 5,12x
ROAS 10,0 | caja 620 | dias_inv 12 | reembolso 2%
→ holgura > 3,0: SUBINVIRTIENDO. Subir presupuesto 30%.
```

### Día malo
```
inversion 120 | generados 9 | cobrados 8 | cobro 89%
ingreso 480 | ticket 60,05 | CAC 15,00 | techo 30,72 | holgura 2,05x
ROAS 4,0 | caja 280 | dias_inv 5 | reembolso 6%
→ holgura sana pero CAJA al 25% y INVENTARIO en 5 días.
  No subir presupuesto. Reponer stock. Revisar por qué subió el reembolso.
```

Nota la lección del segundo caso: **la holgura estaba bien y aun así la respuesta era "no escales"**.
Por eso el tablero tiene 10 números y no uno.

## Errores de tablero

| Error | Consecuencia |
|---|---|
| Mirarlo solo cuando algo va mal | te enteras tarde |
| Usar el ROAS del panel como número 9 | decides con datos inflados |
| No actualizar el techo de CAC al cambiar costos | todo el tablero miente |
| Registrar pedidos generados como si fueran cobrados | CAC subestimado 22-48% en COD |
| Llevarlo en la cabeza | la memoria maquilla |

## Verificación

Para auditar la aritmética del tablero o construir la hoja con fórmulas exactas, invoca
`Matematicas_lushows`. Para el cálculo del techo y la holgura, corre `228`.

## Relacionados
`11` · `223` · `224` · `226` · `228` · `229` · `231` · `232` · `234` · `235` · `236` · `238`

# El costo oculto de cada venta

## El renglón que hunde operaciones

Los pedidos que **no** se cobran ya costaron dinero. Ese dinero hay que repartirlo entre los
pedidos que sí se cobraron. Es el renglón que casi nadie pone en la hoja, y es el que explica por
qué operaciones "rentables" no tienen caja.

```
desperdicio = (1 − tasa de cobro) ÷ tasa de cobro
```

| Tasa de cobro | Desperdicio | Lectura |
|---|---|---|
| 97% (prepago sano) | 0,031 | 3,1% de una venta mala por cada buena |
| 92% | 0,087 | |
| 85% | 0,176 | |
| **78% (COD bueno)** | **0,282** | 28% |
| 70% | 0,429 | |
| 65% | 0,538 | |
| **52% (COD malo)** | **0,923** | **casi una venta perdida por cada buena** |

Observa que no es lineal: bajar del 78% al 52% (26 puntos) **más que triplica** el desperdicio.

## Cuánto cuesta un fallido según el modelo de pago

| Modelo | Qué pierdes en un fallido | Fórmula |
|---|---|---|
| COD | flete de ida **y** de vuelta + confirmación | `desperdicio × (flete × 2 + confirmación)` |
| Prepago reembolsado | producto + flete (la caja ya salió) | `desperdicio × (costo bodega + flete)` |
| Prepago con producto recuperado | flete ida y vuelta + reacondicionar | `desperdicio × (flete × 2 + reacondicionar)` |

### Números México (flete USD 8,74 · costo bodega USD 16,22)

| Escenario | Desperdicio | Costo por venta buena |
|---|---|---|
| Prepago 97% | 0,031 | **USD 0,77** |
| Prepago 92% | 0,087 | USD 2,17 |
| COD 78% | 0,282 | **USD 4,93** (solo flete doble) |
| COD 65% | 0,538 | USD 9,40 |
| COD 52% | 0,923 | **USD 16,14** |

Con ticket de USD 60,05, un COD al 52% se lleva **el 27% del ticket** solo en fallidos. Esa es la
razón aritmética de por qué el proyecto México va prepago. Ver `30` y `31`.

## Los otros costos ocultos

| # | Costo | Cómo se calcula por pedido | Rango típico |
|---|---|---|---|
| 1 | Fallidos / no entregados | arriba | 0,5-16 USD |
| 2 | Reembolsos y devoluciones | tasa × (costo bodega + flete) | 1-6% de pedidos |
| 3 | Contracargos (chargebacks) | tasa × (ticket + penalidad de pasarela) | 0,1-1% |
| 4 | Garantía prometida | tasa de uso × costo | ver `211` |
| 5 | Reenvíos por dirección mala | tasa × flete | 1-3% |
| 6 | Producto defectuoso de fábrica | tasa × costo bodega | 1-5% |
| 7 | Soporte y atención | horas × costo hora ÷ pedidos | 0,2-1,5 USD |
| 8 | Fraude / pedidos falsos | tasa × costo completo | mayor en COD |
| 9 | Diferencia cambiaria | % del costo importado | 2-8% al año |
| 10 | Comisión de retiro de la pasarela | % + fijo | 0,5-2% |
| 11 | Inventario muerto al final de temporada | unidades sin vender × costo | ver `238` |

**Verificar todos con tus propios datos.** Estos rangos son puntos de partida, no promesas.

## Cómo se prorratean (la forma correcta)

```
costo oculto total del período
────────────────────────────────  = costo oculto por pedido cobrado
pedidos cobrados del período
```

Todo va **por pedido cobrado**, nunca por pedido generado. Si divides entre generados, subestimas
cada renglón y tu techo de CAC sale inflado.

## El efecto compuesto: ejemplo

Producto con ticket USD 60,05 y costos "visibles" de USD 26,00. Parece dejar techo de 34,05.
Ahora sumamos lo oculto:

| Renglón | USD/pedido |
|---|---|
| Fallidos (prepago 92%) | 2,17 |
| Reembolsos 3% | 0,75 |
| Contracargos 0,3% | 0,20 |
| Defectuosos 2% | 0,32 |
| Soporte | 0,40 |
| Comisión de retiro | 0,45 |
| **Total oculto** | **4,29** |

```
Techo aparente:  34,05   → holgura 3,23x con CAC 10,54  → "escalo"
Techo real:      29,76   → holgura 2,82x                → "escalo con cuidado"
```

Diferencia del 13% en el techo. Con ticket flaco, esa misma diferencia te lleva de 1,4x a 1,0x:
de frágil a trabajar gratis.

## Señales de que tienes costos ocultos sin contar

| Señal | Qué revisar |
|---|---|
| El modelo dice que ganas y el banco dice que no | fallidos y reembolsos |
| La caja siempre está apretada aunque vendas | ciclo de cobro (`234`) |
| Sube el volumen y baja la utilidad | soporte y devoluciones escalan mal |
| Un operador logístico "barato" te sale caro | tasa de entrega, no tarifa |
| El proveedor es barato y devuelves mucho | calidad, renglón 6 |

## Cómo bajarlos

| Costo | Palanca |
|---|---|
| Fallidos COD | confirmación por WhatsApp antes de despachar; filtrar zonas malas |
| Fallidos en general | **pasar a prepago** — es la palanca grande (`30`) |
| Reembolsos | promesa honesta (`215`), fotos reales, plazo cumplido |
| Contracargos | descriptor de tarjeta claro, soporte rápido, 3DS |
| Defectuosos | inspección en origen antes de embarcar (`110`) |
| Soporte | preguntas frecuentes buenas + bot de WhatsApp |
| Inventario muerto | pedidos de reposición pequeños y frecuentes |

## Regla del operador

Todo renglón oculto que no midas **se va a llevar el margen que crees que tienes**. Mide los 11 de
la tabla durante el primer mes, aunque sea a mano en una hoja. Después ya sabes cuáles importan en
tu operación y cuáles puedes ignorar.

## Relacionados
`11` · `30` · `31` · `110` · `211` · `215` · `222` · `223` · `224` · `227` · `228` · `234` · `238` · `239`

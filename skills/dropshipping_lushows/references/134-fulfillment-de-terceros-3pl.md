# Fulfillment de terceros (3PL)

> Vigencia: septiembre 2026. Las tarifas son rangos de mercado; pide cotización real.

Un 3PL (third-party logistics) guarda tu inventario, arma tus pedidos y los despacha. Es lo que te
permite tener stock propio **sin montar una bodega ni contratar gente**. Es el paso natural cuando la
plataforma COD ya no alcanza y la bodega propia todavía no se justifica.

## Qué hace un 3PL

| Servicio | Detalle |
|---|---|
| Recepción | Descarga, conteo, inspección de entrada, ingreso a sistema |
| Almacenaje | Por pallet, por estante o por m³/pie cúbico |
| **Pick & pack** | Tomar el producto, empacarlo, pegar la guía |
| Despacho | Entrega a la transportadora, con tarifas negociadas |
| Gestión de devoluciones | Recepción, inspección, reingreso o descarte |
| Kitting / ensamble de bundles | **Clave si vendes bundles** |
| Insertos y empaque personalizado | Según lo que acuerdes. Ver `125` |
| Integración con tu tienda | API o app de Shopify/Woo |

## Estructura de costos típica

| Concepto | Modelo de cobro | Rango orientativo |
|---|---|---|
| Recepción | Por pallet o por unidad | Bajo, único por entrada |
| Almacenaje | Por pallet/mes o m³/mes | Recurrente. **Sube en Q4** |
| Pick & pack | Por pedido + por unidad adicional | El grueso del costo variable |
| Material de empaque | Por pedido | Bajo |
| Kitting/bundle | Por unidad ensamblada | Medio |
| Devolución procesada | Por unidad | Medio |
| Integración/setup | Único | Variable |
| Mínimo mensual | Fijo | **El que más duele si vendes poco** |

Pide siempre la cotización desglosada así y calcula tu **costo total por pedido despachado**, no el
precio de cada línea por separado. Es la única cifra comparable. Invoca `Matematicas_lushows`.

## El mínimo mensual: la letra chica que decide

Muchos 3PL exigen un mínimo (pedidos/mes o facturación/mes). Si vendes por debajo, pagas igual.

```
3PL con mínimo de 200 pedidos/mes:
  Vendes 200 → costo por pedido = X
  Vendes 80  → costo por pedido = X × 2,5
```

**Por eso el 3PL no sirve en fase de validación.** Con 30 pedidos/mes el mínimo te destruye la unidad
económica. Primero valida con plataforma, luego pasa a 3PL. Ver `136`.

## Cuándo pasar a 3PL: los cuatro criterios

| Criterio | Umbral orientativo |
|---|---|
| Volumen estable | 150-300+ pedidos/mes del mismo producto |
| Producto validado | 60+ días de venta consistente |
| Capital disponible | Para el lote **sin** tocar el presupuesto de pauta |
| El ahorro de comprar directo supera el costo del 3PL | Calcúlalo, no lo estimes |

La fórmula de decisión:

```
Ahorro mensual = (costo_plataforma_por_unidad − costo_lote_por_unidad) × unidades_mes
Costo 3PL      = mínimo mensual + almacenaje + (pick&pack × unidades_mes)

Si Ahorro > Costo 3PL × 1,5 → tiene sentido.
El ×1,5 cubre el riesgo de inventario y el capital inmovilizado.
```

## Cómo elegir un 3PL: las 15 preguntas

1. ¿Cuál es el mínimo mensual y cómo se calcula?
2. ¿Tarifa completa desglosada: recepción, almacenaje, pick, pack, material, despacho?
3. ¿Cómo cobran el almacenaje: pallet, estante o volumen?
4. ¿Suben tarifas en Q4? ¿Cuánto? (casi siempre sí)
5. ¿Hacen **kitting de bundles**? ¿A qué costo por unidad?
6. ¿Aceptan mi inserto y empaque propio?
7. ¿Qué transportadoras usan y con qué tarifas negociadas?
8. ¿Cuál es el **corte horario** para despacho el mismo día?
9. ¿Qué SLA de despacho tienen (mismo día, 24 h)?
10. ¿Integran con mi tienda de forma nativa o por API?
11. ¿Me dan visibilidad de inventario en tiempo real?
12. ¿Cuál es su tasa de error de picking y cómo la miden?
13. ¿Quién paga un pedido enviado mal?
14. ¿Cómo procesan devoluciones? ¿Reingresan a stock?
15. ¿Puedo visitar la bodega esta semana?

La 12, la 13 y la 15 son las reveladoras. Un 3PL que no mide su tasa de error no la controla, y uno
que no te deja visitar no quiere que veas algo.

## Lo que hay que exigir siempre

| Exigencia | Por qué |
|---|---|
| Inspección de entrada con conteo y fotos | Tu único control de calidad del lote. Ver `123` |
| Visibilidad de inventario en tiempo real | Vender lo que no hay es la peor experiencia |
| Alerta de stock bajo | Evita quedarte sin producto en campaña |
| Reporte mensual de errores de picking | Lo que no se mide no mejora |
| Responsabilidad escrita por pérdida o daño | Con límite y seguro |
| Cláusula de salida y devolución de inventario | **Crítica.** Que no te secuestren el stock |

La última se ignora hasta que la necesitas. Escribe desde el principio cómo sacas tu mercancía y en
cuánto tiempo.

## 3PL por mercado

| Mercado | Consideración |
|---|---|
| **México** | Opciones en CDMX, Guadalajara, Monterrey. CDMX cubre el centro en 1-2 días. Verifica si el 3PL trabaja con 99minutos, Estafeta, Paquetexpress |
| **Colombia** | Bogotá y Medellín. Verifica integración con Interrapidísimo y Servientrega |
| **España** | Muchos operadores; BigBuy también almacena para terceros. Ver `130` |
| **EE.UU.** | Costa Este + Oeste cubre el país en 2-3 días. Mínimos altos. Ver `131` |
| **China** | Tu agente o CJ pueden ser tu 3PL de origen. Ver `116`, `114` |

## 3PL de origen vs 3PL de destino

| | 3PL en China | 3PL en tu país |
|---|---|---|
| Costo de almacenaje | **Menor** | Mayor |
| Tiempo de entrega al cliente | 8-25 días | **1-4 días** |
| Arancel | Por paquete (caro) | **Una vez, por lote** |
| Capital inmovilizado | Menor | Mayor |
| Viable en MX 2026 | **No.** Ver `16` | Sí |

En 2026, con el arancel mexicano del 33,5% y el fin del de minimis estadounidense, **el 3PL de destino
ganó por goleada**. El 3PL chino solo sirve para mercados que aún toleran el tránsito.

## Errores frecuentes

| Error | Realidad |
|---|---|
| Contratar 3PL en fase de validación | El mínimo mensual te mata la unidad económica |
| Comparar solo el precio del pick & pack | El costo total por pedido es otro |
| No preguntar por el alza de Q4 | Te sube el costo justo en tu mejor mes |
| No exigir inspección de entrada | Recibes 500 unidades sin saber si están bien |
| No tener cláusula de salida | Tu inventario queda atrapado |
| No verificar el corte horario | Prometes 24 h y despachas al día siguiente |
| Un solo 3PL sin plan B | Punto único de falla de todo tu negocio |

## Para el proyecto activo (México, diciembre 2026)

**No contrates 3PL en diciembre.** Con capital menor a US$500 y cero ventas validadas, el mínimo
mensual te destruye. Usa Dropi MX, que ya es tu fulfillment. Ver `132`.

El 3PL entra en la conversación cuando: (a) vendas 150-300 bundles/mes estables, (b) tengas capital
para un lote sin tocar la pauta, (c) el kitting del bundle sea un problema operativo real.

Cuando llegue ese momento, pregunta específicamente por **kitting de bundles**: armar tres productos
en una caja es un servicio con costo propio y es exactamente lo que tu operación va a necesitar.

## Relacionados
Ver `132`, `133`, `135`, `136`, `137`, `138`, `123`, `125`, `16`, `131`.

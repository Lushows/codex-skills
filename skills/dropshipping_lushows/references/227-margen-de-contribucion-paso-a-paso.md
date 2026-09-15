# Margen de contribución paso a paso

## Qué es y por qué no es "la ganancia"

El **margen de contribución** es lo que queda de un pedido después de pagar todos los costos
variables de ese pedido. Se llama así porque es lo que "contribuye" a pagar los costos fijos del
negocio (herramientas, dominio, tu tiempo) y, después de eso, a la utilidad.

```
MARGEN DE CONTRIBUCIÓN = TICKET − COSTOS VARIABLES POR PEDIDO
```

Ojo: el CAC es un costo variable. Entra. El arriendo de tu casa no.

## Variable vs fijo: la separación que todos hacen mal

| Costo | ¿Variable? | Por qué |
|---|---|---|
| Costo del producto | sí | un pedido más, una unidad más |
| Flete internacional prorrateado | sí | por unidad |
| Arancel | sí | proporcional a la importación |
| Flete al cliente | sí | por pedido (aunque sea monto fijo) |
| Comisión de pasarela | sí | % del ticket |
| Costo de fallidos prorrateado | sí | escala con volumen |
| **CAC** | **sí** | pagas por cada venta nueva |
| Plataforma de tienda (mensual) | no | fijo |
| Apps y herramientas | no | fijo |
| Diseño de creativos (producción) | no | fijo del producto |
| Tu sueldo | no | fijo |

Confusión frecuente: "el flete es fijo porque siempre cuesta 8,74". No. Es **fijo por pedido** y
**variable con el volumen**. Es variable en el sentido contable que importa aquí. Lo que lo hace
especial es que no escala con el **valor** del pedido — y de ahí sale toda la tesis del bundle
(`218`, `220`).

## Cálculo en 5 pasos

### Paso 1 — Ticket neto
```
Ticket cobrado − impuesto sobre la venta (si no está incluido) − reembolsos esperados
```

### Paso 2 — Costo puesto en bodega
```
producto + flete internacional prorrateado + arancel + empaque
```
Ver `28`. En México, arancel de 33,5% si el origen no tiene TLC (`16`).

### Paso 3 — Costos de entrega y cobro
```
flete al cliente + comisión de pasarela (+ MSI) + costo de atención por pedido
```

### Paso 4 — Costo de los fallidos prorrateado
```
desperdicio = (1 − tasa de cobro) ÷ tasa de cobro
prepago: desperdicio × (costo puesto en bodega + flete)
COD:     desperdicio × (flete × 2 + costo de confirmación)
```

### Paso 5 — Resta y expresa de dos formas
```
MC absoluto (USD/pedido) = paso1 − paso2 − paso3 − paso4 − CAC
MC porcentual            = MC absoluto ÷ ticket neto
```

## Los dos márgenes de contribución que debes llevar

| Nombre | Incluye CAC | Uso |
|---|---|---|
| **MC antes de publicidad** | no | es el **techo de CAC** (`11`) |
| **MC después de publicidad** | sí | es la utilidad por pedido |

Son el mismo cálculo con y sin un renglón. Llevar los dos te permite saber si el problema es la
estructura de costos (el primero es bajo) o la subasta (el primero está bien y el segundo no).

## Ejemplo completo: México bundle

| Paso | Concepto | USD |
|---|---|---|
| 1 | Ticket neto | 60,05 |
| 2 | Costo puesto en bodega | 16,22 |
| 3 | Flete al cliente + pasarela + atención | 8,74 + 3,30 + 0,30 |
| 4 | Fallidos prorrateados (prepago, cobro 97%) | 0,77 |
| — | **Total costos variables sin publicidad** | **29,33** |
| — | **MC antes de publicidad (= techo de CAC)** | **30,72** (51,2% del ticket) |
| 5 | − CAC | 10,54 |
| — | **MC después de publicidad** | **20,18** (33,6% del ticket) |

## Comparación suelto vs bundle

| | Suelto | Bundle |
|---|---|---|
| Ticket | 38,20 | 60,05 |
| MC antes de publicidad | 15,28 (40,0%) | 30,73 (51,2%) |
| MC después de publicidad | 2,63 (6,9%) | 20,18 (33,6%) |

El MC **porcentual** subió 11 puntos y el absoluto se duplicó. Los costos fijos por pedido se
diluyeron. Ese es el mecanismo, otra vez.

## Umbrales de referencia

| MC antes de publicidad | Lectura |
|---|---|
| < 35% del ticket | muy difícil: casi no queda para comprar tráfico |
| 35-45% | ajustado, solo con CAC bajo |
| **45-60%** | **zona operable** |
| > 60% | excelente, revisa si puedes escalar más rápido |

| MC después de publicidad | Lectura |
|---|---|
| < 10% | frágil, cualquier variación te saca |
| 10-20% | operable con disciplina |
| **20-35%** | **sano** |
| > 35% | subinvirtiendo en pauta |

## Para qué sirve el MC en decisiones

| Decisión | Regla con MC |
|---|---|
| ¿Aprobar un descuento? | recalcula MC; si baja de 20%, no (`221`) |
| ¿Agregar una pieza al bundle? | agrega si el MC absoluto sube (`218`) |
| ¿Cambiar de operador logístico? | compara MC, no tarifas |
| ¿Cuántos pedidos para el equilibrio? | costos fijos ÷ MC absoluto (`225`) |
| ¿Qué producto escalar primero? | el de mayor MC absoluto × volumen posible |

Nota: se escala por **MC absoluto**, no por porcentaje. Un producto con 60% de MC sobre USD 20
(USD 12) deja menos que uno con 35% sobre USD 60 (USD 21).

## Frontera

Estados financieros, clasificación contable formal y cierre de período: invoca `contador_lushows`.
Punto de equilibrio de la empresa completa: `economist_lushows`. Verificación aritmética:
`Matematicas_lushows`.

## Relacionados
`11` · `16` · `28` · `218` · `220` · `221` · `223` · `225` · `226` · `228` · `229` · `231`

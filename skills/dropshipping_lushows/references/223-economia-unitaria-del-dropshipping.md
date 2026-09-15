# Economía unitaria del dropshipping

## Qué es la economía unitaria

Es la respuesta a una sola pregunta: **¿un pedido más me deja dinero o me lo quita?** Si no la
sabes con precisión, no tienes un negocio: tienes una máquina de mover plata ajena.

```
UTILIDAD POR PEDIDO = TICKET − COSTOS POR PEDIDO − CAC
UTILIDAD TOTAL      = UTILIDAD POR PEDIDO × PEDIDOS COBRADOS
```

## La plantilla completa, renglón por renglón

Rellena esta tabla para tu producto. Todos los valores **por pedido cobrado**.

| # | Renglón | Cómo se calcula | Ejemplo MX bundle (USD) |
|---|---|---|---|
| 1 | Ticket bruto | precio + envío cobrado | 60,05 |
| 2 | − Impuesto sobre venta | si aplica y no está incluido | ver `236` |
| 3 | = Ticket neto | | 60,05 |
| 4 | − Costo del producto (FOB × piezas) | proveedor | 9,80 |
| 5 | − Flete internacional prorrateado | flete lote ÷ unidades | 1,60 |
| 6 | − Arancel e impuestos de importación | 33,5% sin TLC (`16`) | 3,82 |
| 7 | − Empaque y manipulación | | 1,00 |
| 8 | = **Costo puesto en bodega** | 4+5+6+7 | **16,22** |
| 9 | − Flete al cliente (última milla) | tarifa del operador | 8,74 |
| 10 | − Comisión de pasarela (+MSI) | 5,0% + 0,30 | 3,30 |
| 11 | − Costo de atención por pedido | soporte, WhatsApp | 0,30 |
| 12 | − Costo de fallidos prorrateado | ver abajo (`229`) | 0,77 |
| — | = **Total costos por pedido** | 8+9+10+11+12 | **29,33** |
| 13 | = **TECHO DE CAC** | 3 − total | **30,72** |
| 14 | − CAC real | inversión ÷ pedidos cobrados | 10,54 |
| 15 | = **UTILIDAD POR PEDIDO** | 13 − 14 | **20,18** |

(El desglose de los renglones 4-7 es una reconstrucción coherente con el costo puesto en bodega
verificado de USD 16,22. Verifica los tuyos con `28` y corre el modelo de `228`.)

## El renglón 12: el que hunde operaciones

Los pedidos que no se cobran **ya costaron dinero**. Hay que repartir ese costo entre los que sí
se cobraron.

```
desperdicio = (1 − tasa de cobro) ÷ tasa de cobro
```

| Tasa de cobro | Desperdicio | Lectura |
|---|---|---|
| 95% (prepago sano) | 0,053 | por cada venta buena pagas 5% de una mala |
| 85% | 0,176 | |
| 78% (COD bueno) | 0,282 | 28% |
| 65% (COD normal) | 0,538 | 54% |
| 52% (COD malo) | 0,923 | **casi una venta perdida por cada buena** |

```
costo_fallidos_COD     = desperdicio × (flete × 2 + costo de confirmación)
costo_fallidos_prepago = desperdicio × (costo puesto en bodega + flete)
```

## Los 3 números que resumen todo

| Número | Fórmula | Umbral |
|---|---|---|
| **Techo de CAC** | ticket − todos los costos por pedido cobrado | cuanto más alto, mejor |
| **Holgura** | techo de CAC ÷ CAC real | ≥ 2,0x para operar |
| **ROAS de equilibrio** | ticket ÷ techo de CAC | tu ROAS real debe superarlo |

| Holgura | Diagnóstico |
|---|---|
| < 1,0 | pierdes en cada venta |
| 1,0 - 1,3 | trabajas gratis |
| 1,3 - 2,0 | frágil ante temporada |
| 2,0 - 3,0 | sano |
| > 3,0 | subinvirtiendo: sube presupuesto |

## Prepago vs COD: dos economías distintas

| | Prepago | COD |
|---|---|---|
| Tasa de cobro típica | 92-98% | 52-78% |
| Desperdicio | 0,02-0,09 | 0,28-0,92 |
| Costo del fallido | producto + flete | flete ida y vuelta |
| Retorno del dinero | ~3 días | ~12 días |
| Vueltas en 75 días | ~25 | ~6,2 |
| Poder de compra con USD 500 | ~USD 12.500 | ~USD 3.100 |

Ver `30`, `31` y `234`. El proyecto México va prepago por esta razón, no por preferencia.

## Errores clásicos de economía unitaria

| Error | Consecuencia |
|---|---|
| Dividir la inversión entre pedidos **generados** | CAC subestimado 22-48% en COD |
| Olvidar el arancel | −33,5% de sorpresa en México (`16`) |
| Usar el precio de AliExpress como costo | falta flete, arancel, empaque (`28`) |
| No prorratear fallidos | la operación parece sana hasta que no hay caja |
| Ignorar comisión de MSI | ~1,5 pp que sí importan |
| Medir margen sobre precio en vez de sobre costo | confusión entre markup y margen |

## Markup vs margen (no los confundas)

```
markup = (precio − costo) ÷ costo        múltiplo = precio ÷ costo
margen = (precio − costo) ÷ precio
```

Un múltiplo de 3,0x es markup de 200% y margen bruto de 66,7%. Los múltiplos mínimos de `42` están
expresados como **múltiplo sobre costo puesto en bodega**.

## Frecuencia de recálculo

| Cuándo | Por qué |
|---|---|
| Antes de lanzar | obvio |
| Cada semana en operación | el CAC se mueve solo |
| Al cambiar de operador logístico | cambia el renglón 9 |
| Al entrar Q4 / Buen Fin | el CPM sube 20-80% (`238`) |
| Al cambiar el precio o el bundle | todo cambia |

Para ejecutar el cálculo, usa el modelo de `228`. Para auditar un número específico, invoca
`Matematicas_lushows`. Para impuestos y facturación, `236` y `237` (y `contador_lushows`).

## Relacionados
`11` · `16` · `28` · `30` · `31` · `42` · `224` · `225` · `226` · `227` · `228` · `229` · `234` · `236` · `238`

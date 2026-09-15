# Calcular el CAC real

## La definición correcta

```
CAC = INVERSIÓN PUBLICITARIA TOTAL ÷ PEDIDOS COBRADOS
```

Dos trampas en una sola línea:

1. **Inversión total**, no solo la del conjunto que vendió. Cuentan las campañas apagadas, los tests
   fallidos de esa semana, todo lo que salió de tu tarjeta.
2. **Pedidos cobrados**, no pedidos generados. En contraentrega la diferencia es del 22% al 48%.

## Las 4 versiones del CAC y cuál usar

| Versión | Denominador | Para qué sirve |
|---|---|---|
| CPA de plataforma | conversiones que Meta atribuye | ver tendencia dentro del día |
| CAC por pedido generado | pedidos que entraron | engañoso en COD |
| **CAC real** | **pedidos cobrados y no reembolsados** | **decisiones de dinero** |
| CAC totalmente cargado | + costos de herramientas y apps | evaluar el negocio (`economist_lushows`) |

El único que entra al modelo de holgura es el **CAC real**.

## Cuánto miente el CAC de plataforma

| Diferencia | Causa |
|---|---|
| Meta reporta más conversiones que tus pedidos | atribución de vista, ventanas de 7 días, duplicación |
| Meta reporta menos | iOS, bloqueadores, señal débil sin CAPI |
| Tu CAC real es peor que el CPA reportado | pedidos que no se cobraron |

Regla práctica: **la fuente de verdad es tu banco**, no el panel de anuncios. Meta sirve para
optimizar dentro del día; la contabilidad sale de lo que entró a la cuenta.

## Cálculo semanal (el que se hace los lunes)

```
Semana del 7 al 13 de septiembre
  Inversión publicitaria total (todas las campañas):  USD  X
  Pedidos generados:                                        N
  Pedidos cobrados y no reembolsados:                       M

  CAC aparente = X ÷ N
  CAC real     = X ÷ M
```

### Ejemplo numérico

| Concepto | Prepago | COD |
|---|---|---|
| Inversión | USD 1.000 | USD 1.000 |
| Pedidos generados | 100 | 140 |
| Tasa de cobro | 95% | 62% |
| Pedidos cobrados | 95 | 87 |
| CAC aparente | 10,00 | 7,14 |
| **CAC real** | **10,53** | **11,49** |

El COD parece 29% más barato y es 9% más caro. Y eso antes de contar el flete doble de los 53
pedidos fallidos (`229`).

## Qué NO es CAC

| No es | Por qué |
|---|---|
| Solo el gasto del anuncio ganador | los perdedores también salieron de tu bolsillo |
| El CPC | el clic no es un cliente |
| El costo por mensaje iniciado | la conversación no es una venta |
| El CPA de la campaña de retargeting | está inflado por tráfico que ya tenías |

## CAC de test vs CAC de escala

Son números distintos y hay que separarlos contablemente:

| Tipo | Qué incluye | Uso |
|---|---|---|
| CAC de test | inversión de validación de productos nuevos | es un costo de I+D, ver `232` |
| CAC de escala | inversión de campañas con producto validado | es el que compara contra el techo |

Si mezclas los dos, tu producto ganador se ve peor de lo que es y tus tests se ven mejor. Mantén
dos cuentas separadas desde el día uno.

## Cuánto CAC puedes pagar

```
TECHO DE CAC = TICKET − TODOS LOS COSTOS POR PEDIDO COBRADO
HOLGURA      = TECHO DE CAC ÷ CAC REAL
```

México bundle: techo USD 30,73 · CAC USD 10,54 · holgura **2,92x** (sano).
México suelto: techo USD 15,28 · CAC USD 12,65 · holgura **1,21x** (trabajas gratis).

## Qué mueve el CAC hacia arriba (y no lo controlas)

| Factor | Efecto |
|---|---|
| Q4 | CPM +20-50% |
| Black Friday / Buen Fin | CPM +50-80% |
| Saturación del producto (`61`) | CTR cae, CAC sube |
| Fatiga del creativo | CTR cae en 5-15 días |
| Competencia entrando al mismo ángulo | subasta más cara |

Por eso la holgura es la métrica y no el CAC absoluto: el CAC se va a mover, tu techo es lo que
tienes que defender.

## Qué mueve el CAC hacia abajo (y sí controlas)

| Palanca | Efecto típico | Módulo |
|---|---|---|
| Mejor hook (primeros 1,5 s) | CTR +30-100% | `212` |
| Oferta más completa (bundle) | CVR +20-40% | `218` |
| MSI en México | CVR +36% | `216` |
| Página más rápida y clara | CVR +10-30% | `desingweb-lushows` |
| Prueba social real | CVR +10-25% | `211` |

Recuerda: pedidos cobrados = impresiones × CTR × CVR × tasa de cobro. **Mejorar 20% cada factor
da +107%, no +20%.**

## CPM base por país (referencia USD, verificar)

| País | CPM base | Q4 (+20-50%) |
|---|---|---|
| Perú | 3,70 | 4,44 - 5,55 |
| Colombia | 4,00 | 4,80 - 6,00 |
| México | 4,50 | 5,40 - 6,75 |
| Chile | 5,20 | 6,24 - 7,80 |
| España | 5,80 | 6,96 - 8,70 |
| EE. UU. | 23,00 | 27,60 - 34,50 |

```
CAC estimado = CPM ÷ 1.000 ÷ (CTR × CVR × tasa de cobro)
```

## Registro mínimo

Una fila por día: fecha · inversión · pedidos generados · pedidos cobrados · ticket promedio ·
CAC real · holgura. Eso es el tablero de `239`. Sin ese registro, cualquier decisión es opinión.

## Relacionados
`11` · `61` · `212` · `216` · `218` · `223` · `225` · `226` · `228` · `229` · `232` · `238` · `239`

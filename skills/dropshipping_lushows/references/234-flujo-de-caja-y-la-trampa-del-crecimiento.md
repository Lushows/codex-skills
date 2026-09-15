# Flujo de caja y la trampa del crecimiento

## La trampa, en una frase

**Se quiebra creciendo.** Un producto rentable que crece rápido consume caja más rápido de lo que
la devuelve, porque pagas la publicidad y el inventario **hoy** y cobras **después**.

```
Rentabilidad ≠ liquidez.
Puedes tener utilidad en la hoja y cero pesos en el banco el mismo día.
```

## El ciclo de conversión de efectivo

```
Pagas pauta  →  entra el pedido  →  la pasarela retiene  →  te liquidan  →  repones stock
    día 0           día 0              día 0-2              día 2-4         día X
```

| Modelo | Días hasta tener el dinero disponible | Vueltas en 75 días de temporada |
|---|---|---|
| **Prepago** | **~3** | **~25** |
| **COD** | **~12** | **~6,2** |

## Qué significa eso con USD 500

```
Poder de compra = capital × vueltas en el período
```

| Modelo | Capital | Vueltas | Poder de compra en 75 días |
|---|---|---|---|
| Prepago | USD 500 | 25 | **USD 12.500** |
| COD | USD 500 | 6,2 | **USD 3.100** |

El mismo dinero compra **4 veces más actividad** en prepago. No es una preferencia de modelo: es la
diferencia entre operar una temporada completa y quedarse sin caja en la segunda semana. Ver `30`.

## Por qué el crecimiento consume caja

Cada vez que subes el presupuesto, el gasto crece **antes** que el ingreso:

| Día | Gasto acumulado | Ingreso disponible acumulado (prepago, 3 días) | Caja |
|---|---|---|---|
| 1 | 100 | 0 | −100 |
| 2 | 200 | 0 | −200 |
| 3 | 300 | 0 | −300 |
| 4 | 400 | 290 | −110 |
| 5 | 500 | 580 | +80 |

Con holgura 2,9x el negocio es rentable, y aun así el **valle de caja** es de USD 300. Si tu
capital disponible es USD 250, quiebras el día 3 de un negocio que gana dinero.

```
Valle de caja ≈ gasto diario × días de ciclo de cobro
```

| Gasto diario | Ciclo 3 días (prepago) | Ciclo 12 días (COD) |
|---|---|---|
| USD 20 | 60 | 240 |
| USD 50 | 150 | 600 |
| USD 100 | 300 | 1.200 |
| USD 200 | 600 | 2.400 |

**Regla:** nunca operes con un gasto diario cuyo valle de caja supere tu efectivo disponible.
Con USD 500 y prepago, el techo de gasto diario seguro está cerca de **USD 100-130**. Con COD, cerca
de USD 30.

## Reglas de escalado que respetan la caja

| Regla | Detalle |
|---|---|
| Subir presupuesto máximo 20-30% cada 48-72 h | evita reiniciar aprendizaje y evita el salto de caja |
| Nunca escalar con holgura < 2,0x | el margen no aguanta el error |
| Escalar solo con dinero ya liquidado | no con "lo que va a entrar" |
| Reponer inventario en lotes pequeños y frecuentes | menos capital muerto |
| Si la caja baja del 25% del capital, pausar | señal de alto, no de fe |

## El inventario: el otro tragador de caja

Con stock local, cada reposición inmoviliza dinero.

```
capital inmovilizado = unidades en bodega × costo puesto en bodega
```

| Unidades | Costo bodega USD 16,22 | ¿Sostenible con capital 500? |
|---|---|---|
| 10 | 162 | sí |
| 30 | 487 | no: te deja sin caja para pauta |
| 100 | 1.622 | no |

Con capital pequeño, el orden correcto es: **vender primero con lotes mínimos, reponer con la caja
que generó la venta**. Comprar 100 unidades "para tener mejor precio" con USD 500 de capital es la
forma más rápida de quedarse sin pauta y con una bodega llena.

## Días de inventario

```
días de inventario = unidades en bodega ÷ unidades vendidas por día
```

| Días | Lectura |
|---|---|
| < 7 | riesgo de quiebre de stock; pide ya |
| 10-21 | zona sana en temporada |
| > 45 | capital dormido |

En diciembre hay que sumar el tiempo de reposición: si el proveedor tarda 20 días, el último pedido
útil se hace a finales de noviembre. Ver `238` y `145`.

## Señales de problema de caja

| Señal | Causa probable |
|---|---|
| Vendes más y tienes menos dinero | escalaste más rápido que el ciclo de cobro |
| Siempre esperando la liquidación de la pasarela | ciclo largo; negocia liquidación diaria |
| No puedes reponer el ganador | capital atrapado en tests o en stock lento |
| Pagas la pauta con tarjeta de crédito | estás financiando el crecimiento con deuda cara |
| Reserva por debajo del 10% | un contratiempo te saca |

## Qué hacer cuando la caja aprieta

```
1. Bajar presupuesto diario 30-50% (no apagar: perder aprendizaje también cuesta)
2. Liquidar inventario lento, aunque sea a costo
3. Negociar liquidación más rápida con la pasarela
4. Priorizar prepago sobre COD si conviven
5. Subir el ticket: entra más dinero por la misma vuelta (218, 220)
6. NO bajar el precio: empeora caja y margen a la vez (221)
```

## Frontera

Proyección de flujo de caja de la empresa, financiamiento y decisiones de estructura: invoca
`economist_lushows`. Registro contable, impuestos por pagar y su calendario (que también es caja):
`contador_lushows` y `236`.

## Relacionados
`30` · `145` · `218` · `220` · `221` · `223` · `228` · `229` · `232` · `233` · `235` · `236` · `238` · `239`

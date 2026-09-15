# Comprar inventario: cuánto y cuándo

> Vigencia: septiembre 2026. Para cálculos exactos con tus números invoca `Matematicas_lushows`.

Comprar inventario es la decisión donde más plata se pierde por no hacer una cuenta de dos líneas. La
pregunta no es "¿cuánto me alcanza?" sino **"¿en cuántos días lo vendo y en cuántos lo repongo?"**.

## Las dos variables que lo deciden todo

```
VELOCIDAD DE VENTA  = unidades vendidas por día (medida, no estimada)
LEAD TIME           = días desde que pides hasta que puedes despachar
```

Todo lo demás se deriva de estas dos.

| Fuente | Lead time típico |
|---|---|
| Plataforma COD / mayorista local | 1-3 días |
| Lote local | 3-10 días |
| Importación aérea desde China | 25-45 días (producción + tránsito 3-10 días puerta a puerta) |
| Importación marítima a Colombia | 60-90 días (producción + 30-45 FCL / 35-50 LCL) |
| Importación marítima a Chile / Perú | 60-85 días (30-45 Valparaíso; 30-35 Perú, Chancay 28-32) |

## La fórmula del pedido

```
Punto de reorden  = velocidad_diaria × lead_time + stock_de_seguridad
Stock de seguridad = velocidad_diaria × días_de_colchón   (10-25 días típico)

Cantidad a pedir  = velocidad_diaria × (lead_time + días_de_cobertura_objetivo)
```

Ejemplo: vendes 6 uds/día, lead time marítimo de 75 días, colchón de 20 días.

```
Punto de reorden = 6 × 75 + 6 × 20 = 450 + 120 = 570 unidades
```

Traducción: **cuando te queden 570 unidades, ya debiste haber pedido.** No cuando te queden 50.

Esa es la razón por la que quien importa por marítimo debe pensar con tres meses de anticipación, y
por la que el Año Nuevo Chino desbarata planificaciones enteras. Ver `139`.

## Cuánto comprar en el PRIMER lote

Aquí la regla cambia, porque no tienes historia y el riesgo es asimétrico.

| Regla | Valor |
|---|---|
| **Cobertura máxima del primer lote** | **45-60 días de venta** |
| Mínimo viable | El MOQ negociado. Ver `122` |
| Máximo del capital | Nunca más del 50-60% de tu caja disponible |
| Reserva obligatoria para pauta | Al menos 40% de tu caja |

```
Primer lote = min(
    velocidad_diaria × 60,
    caja_disponible × 0,55 / costo_unitario,
    MOQ_del_proveedor  ← si el MOQ supera esto, negocia o no compres. Ver 122
)
```

**Si el MOQ del proveedor te obliga a comprar 200 días de inventario, ese no es tu proveedor.**

## El costo real de tener inventario

No es solo lo que pagaste. Es:

| Costo | Cómo se manifiesta |
|---|---|
| **Capital inmovilizado** | Plata que no puede pagar pauta ni probar productos |
| Almacenaje | Fee del 3PL o arriendo. Ver `134`, `135` |
| Obsolescencia | El producto pasa de moda o sale una versión mejor |
| Merma, rotura y robo | 1-3% típico, más en producto frágil |
| Costo de oportunidad | Lo que habrías ganado con esa plata en pauta |
| Descuento de liquidación | Lo que vas a perder si tienes que rematarlo |

**El costo del capital inmovilizado es el grande y el invisible.** US$2.000 en inventario que rota en
150 días es US$2.000 que no compraron clientes durante 5 meses.

## La trampa del descuento por volumen

| Cantidad | Precio/ud | Total | Ahorro vs escalón anterior | Días de inventario (6 uds/día) |
|---|---|---|---|---|
| 200 | 3,40 | 680 | — | 33 |
| 500 | 3,00 | 1.500 | 12% | 83 |
| 1.000 | 2,80 | 2.800 | 7% | **167** |
| 2.000 | 2,65 | 5.300 | 5% | 333 |

El salto de 200 a 500 cuesta US$820 extra y ahorra 12%. El de 1.000 a 2.000 cuesta US$2.500 extra y
ahorra 5%.

**El descuento tiene rendimientos decrecientes; el riesgo es lineal y creciente.** El punto dulce está
casi siempre en el segundo escalón. Ver `122`.

## Cuándo comprar: el calendario

| Momento | Decisión |
|---|---|
| Producto no validado | **No compres.** Ver `136` |
| 100+ ventas, margen positivo, 60 días | Primer lote, 45-60 días de cobertura |
| Antes de temporada alta (Q4, Buen Fin, Navidad) | Compra con 90-120 días de anticipación |
| Antes del Año Nuevo Chino | **Pedir a más tardar en noviembre** para Q1. Ver `139` |
| Producto en declive (ventas cayendo 3 semanas) | No repongas. Liquida |
| Producto nuevo sin historia | Lote mínimo, siempre |

## Las señales de que compraste de más

| Señal | Qué hacer |
|---|---|
| Rotación por debajo de 4-6 veces/año | Bajar el próximo pedido drásticamente |
| Inventario que lleva 90+ días sin moverse | Liquidar con bundle o descuento |
| Tienes que subir el presupuesto de pauta solo para no quedarte con stock | 🔴 Señal grave: estás comprando ventas para justificar compras |
| El CAC sube pero sigues pautando "porque hay que sacar el inventario" | Para. Recalcula. Ver `11` |

La tercera es la espiral clásica: compras mucho → hay que venderlo → subes pauta → sube el CAC → baja
el margen → necesitas más volumen → compras más. Es cómo se quiebra con la bodega llena.

## Indicadores que debes seguir cada semana

| Indicador | Fórmula | Objetivo orientativo |
|---|---|---|
| Días de inventario | stock actual / velocidad diaria | 30-60 |
| Rotación anual | 365 / días de inventario | 6-12 veces |
| Tasa de agotamiento | días sin stock / días del período | Cerca de 0 |
| Inventario muerto | unidades sin venta en 90 días | Menor al 10% |
| % del capital en inventario | inventario / caja total | Menor al 60% |

## Errores frecuentes

| Error | Realidad |
|---|---|
| Comprar por lo que "alcanza" | La cuenta es de días de inventario, no de presupuesto |
| Perseguir el descuento máximo | El capital parado cuesta más que el 5% que ahorras |
| No calcular el punto de reorden | Te quedas sin stock en tu mejor semana |
| Ignorar el lead time real | 45 días de producción + 40 de tránsito = 85, no 45 |
| Reponer un producto en declive | El inventario que no rota es pérdida diferida |
| Comprar sin reservar caja para pauta | La condición 4 del modelo híbrido. Ver `136` |
| Planificar Q1 sin contar el ANC | Ver `139` |

## Para el proyecto activo (México, diciembre 2026)

Con capital menor a US$500 la respuesta a "cuánto inventario compro" es **cero o casi cero**. El plan:

1. **Diciembre**: Dropi MX. Cero inventario. Mide la velocidad de venta real del bundle. Ese dato es
   el insumo de todo lo que sigue.
2. **Enero**: con velocidad medida, evalúa un lote chico al mayorista mexicano: `velocidad × 45 días`,
   nunca más del 55% de tu caja.
3. **Febrero-marzo**: si el margen lo justifica, lote importado. Pero cuenta el ANC: pedir después de
   mediados de enero significa recibir en abril.

**El número que tienes que sacar de diciembre no son las ventas: es la velocidad diaria estable.** Sin
ese dato cualquier compra de inventario es una apuesta.

## Relacionados
Ver `122`, `134`, `135`, `136`, `138`, `139`, `06`, `11`, `132`.

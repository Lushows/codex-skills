# Impuestos del dropshipper

## Ruteo, primero

Este módulo **no** calcula ni declara impuestos. Para liquidación, calendario, retenciones,
regímenes, facturación electrónica, libros y cierre: **invoca `contador_lushows`**. Aquí solo está
lo que un operador de dropshipping tiene que saber para que el impuesto no le rompa la economía
unitaria.

## Los cuatro impuestos que te tocan

| # | Impuesto | Cuándo aparece | Dónde entra en el modelo |
|---|---|---|---|
| 1 | Aranceles e impuestos de importación | al entrar la mercancía | costo puesto en bodega (`28`) |
| 2 | Impuesto al consumo / IVA de venta | en cada venta | resta del ticket (`223`) |
| 3 | Impuesto sobre la renta | sobre la utilidad del período | cubeta 1 de `235` |
| 4 | Retenciones y responsabilidades locales | según país y régimen | flujo de caja (`234`) |

## 1. Importación: el que mata la economía si lo ignoras

| País | Carga típica | Nota |
|---|---|---|
| México | **33,5%** para países sin TLC | ver `16` |
| EE. UU. | **~54%** para origen chino | fin del de minimis, ver `14` |
| Unión Europea | **€3 por línea** (cargo plano) | se **diluye** al subir el ticket, ver `15` |
| Colombia | **IVA 19% + ~10%** | ver `17` |

**El cargo plano de la UE es el único que premia el ticket alto**: €3 sobre un pedido de €20 son
15%; sobre uno de €60 son 5%. Los porcentuales (México, EE. UU., Colombia) no perdonan.

Consecuencia operativa: el arancel va **antes** del múltiplo. El costo puesto en bodega incluye
arancel; el múltiplo mínimo de `42` se calcula sobre ese costo, no sobre el FOB.

## 2. Impuesto sobre la venta

Dos formas de manejarlo, y hay que elegir explícitamente:

| Forma | Efecto en el ticket | Riesgo |
|---|---|---|
| Precio **con** impuesto incluido | el ticket neto es menor de lo que crees | ninguno si lo modelaste |
| Precio **más** impuesto en checkout | fricción al final, carritos abandonados | alto en LatAm |

En LatAm, el mercado espera el precio final mostrado. Muestra el precio con impuesto incluido y
**réstalo dentro del modelo**, no fuera.

```
Ticket neto = precio mostrado ÷ (1 + tasa del impuesto)   ← si va incluido
```

Si vendes 1.099 MXN con impuesto incluido a una tasa del 16%, tu ticket neto es 947,41 MXN, no
1.099. Modelar sobre 1.099 infla tu techo de CAC y te hace escalar hacia una pérdida.

## 3. Renta: aparta desde el día uno

| Práctica | Detalle |
|---|---|
| Aparta un porcentaje de cada utilidad a una cuenta distinta | el porcentaje lo define tu contador |
| Nunca lo uses como capital de trabajo | es dinero de un tercero |
| Revísalo cada mes, no cada año | el calendario tributario es caja (`234`) |

## 4. La trampa del régimen

Vender por internet a consumidores suele cambiar tus obligaciones: registro, facturación
electrónica, retenciones de pasarelas y marketplaces, informes periódicos. Las plataformas de pago
**reportan** tus ingresos a la autoridad. La opción de "no formalizarse" no existe a partir de
cierto volumen; solo existe la de descubrirlo tarde y caro.

## Umbral de decisión

| Situación | Acción |
|---|---|
| Estás en fase de test, < USD 500 movidos | ordena tus registros, prepara la formalización (`237`) |
| Apareció el primer ganador | **formaliza ahora**, no después de la temporada |
| Vas a importar un lote | necesitas figura legal para importar en regla |
| Vas a usar pasarela de pago seria | te van a pedir documentos |

## Lo que sí debes hacer tú (sin contador)

```
1. Guardar TODA factura: proveedor, flete, aduana, pauta, plataforma, pasarela.
2. Llevar una hoja de ingresos por día y gastos por categoría.
3. Separar la cuenta del negocio de la cuenta personal, desde el primer peso.
4. Apartar el porcentaje de impuestos apenas entra la plata.
5. Llevar el tipo de cambio del día de cada compra en moneda extranjera.
```

Con eso, tu contador trabaja rápido y barato. Sin eso, trabaja lento, caro y con errores.

## Efecto en el modelo financiero

El impuesto de importación ya está en el renglón 6 de `223` y en `costo_bodega` de `228`. El
impuesto sobre la venta se resta del ticket bruto para obtener el ticket neto. El de renta no entra
al techo de CAC: sale de la utilidad, en la cubeta 1 de `235`.

## Aviso

Las cifras de este módulo (33,5% México, ~54% EE. UU., €3 UE, 19%+10% Colombia) son referencias de
2026 recogidas en `13`-`19`. **Verifícalas antes de importar**: cambian por partida arancelaria,
por origen y por decreto. Un error aquí no se arregla después; se paga en aduana.

Para todo lo demás: **invoca `contador_lushows`**.

## Relacionados
`13` · `14` · `15` · `16` · `17` · `28` · `42` · `223` · `228` · `234` · `235` · `237`

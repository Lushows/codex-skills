# ROAS de equilibrio

## La fórmula

```
ROAS DE EQUILIBRIO = TICKET ÷ TECHO DE CAC
```

Es el ROAS mínimo por debajo del cual pierdes dinero. **Tu número, no el de la industria.**

## Por qué el ROAS solo no dice nada

| Negocio | Ticket | Techo de CAC | ROAS de equilibrio | ¿ROAS 2,0 sirve? |
|---|---|---|---|---|
| MX bundle | 60,05 | 30,73 | **1,95** | sí, apenas |
| MX suelto | 38,20 | 15,28 | **2,50** | no, pierdes |
| Margen alto | 90,00 | 60,00 | 1,50 | sí, con holgura |
| Margen bajo | 38,00 | 10,00 | 3,80 | pierdes mucho |

El mismo ROAS de 2,0 es ganancia en una fila y quiebra en otra. Cuando alguien te dice "tengo ROAS
4", la pregunta correcta es: **¿cuál es tu ROAS de equilibrio?**

## Relación con la holgura

```
HOLGURA = TECHO DE CAC ÷ CAC REAL  =  ROAS REAL ÷ ROAS DE EQUILIBRIO
```

Las dos formas dicen lo mismo. Si tu ROAS real es 5,70 y tu ROAS de equilibrio es 1,95, tu holgura
es 2,92x. Ese es exactamente el caso México bundle.

| Holgura | ROAS real necesario si el equilibrio es 1,95 |
|---|---|
| 1,0x | 1,95 |
| 1,3x | 2,54 |
| 2,0x | 3,90 |
| 2,92x | 5,69 |
| 3,0x | 5,85 |

## Tabla de ROAS de equilibrio por estructura de costos

Sobre un ticket de USD 60:

| Costos por pedido | Techo de CAC | ROAS de equilibrio |
|---|---|---|
| 20 | 40 | 1,50 |
| 25 | 35 | 1,71 |
| 30 | 30 | 2,00 |
| 35 | 25 | 2,40 |
| 40 | 20 | 3,00 |
| 45 | 15 | 4,00 |
| 50 | 10 | 6,00 |

**Observa la aceleración:** los últimos USD 10 de costo suben el ROAS de equilibrio de 3,00 a 6,00.
Los costos por pedido no duelen linealmente. Por eso el flete y los fallidos son tan destructivos
en ticket bajo (`222`, `229`).

## El ROAS que reporta Meta no es tu ROAS

| Fuente | Qué mide | Confiabilidad |
|---|---|---|
| ROAS de Meta | valor de conversión atribuido ÷ gasto | infla; depende de ventana y señal |
| **ROAS real** | **ingreso cobrado ÷ gasto total** | **el único que importa** |

Diferencias típicas de 10-40% hacia arriba en el panel, y más si usas ventanas de 7 días con vista.
En COD, Meta cuenta pedidos generados; tú cobras el 52-78% de ellos.

Regla: el ROAS de Meta sirve para **comparar conjuntos entre sí dentro del día**. El ROAS real, de
banco, sirve para **decidir si sigues**.

## Cómo usarlo en la operación diaria

```
1. Calcula tu ROAS de equilibrio una vez por semana (cambia si cambia el costo o el precio)
2. Fija el umbral de pausa en ROAS_equilibrio × 1,3  ← margen de seguridad
3. Fija el umbral de escala en ROAS_equilibrio × 2,0
```

Para México bundle (equilibrio 1,95):

| Zona | ROAS real | Acción |
|---|---|---|
| < 1,95 | pierdes | pausar el conjunto |
| 1,95 - 2,54 | trabajas gratis | revisar creativo y oferta |
| 2,54 - 3,90 | frágil | mantener, no escalar |
| 3,90 - 5,85 | sano | escalar con cuidado |
| > 5,85 | subinvirtiendo | subir presupuesto |

## Efecto de la temporada

El ROAS de equilibrio **no cambia** con el CPM: depende de ticket y costos. Lo que cambia es tu
ROAS real, porque el CAC sube.

| Momento | CPM | CAC estimado | ROAS real | Holgura |
|---|---|---|---|---|
| Base | 4,50 | 10,54 | 5,70 | 2,92x |
| Q4 (+35%) | 6,08 | 14,23 | 4,22 | 2,16x |
| Buen Fin (+65%) | 7,43 | 17,39 | 3,45 | 1,77x |

Sigues ganando en los tres casos **porque el bundle abrió el techo**. Con el producto suelto
(equilibrio 2,50 y holgura 1,21x), el Buen Fin te habría dejado por debajo del equilibrio. Ver
`238`.

## ROAS de equilibrio y COD

En contraentrega hay que corregir por tasa de cobro antes de comparar:

```
ROAS_real_COD = (pedidos cobrados × ticket) ÷ inversión
```

Si usas pedidos generados en el numerador, tu ROAS se ve 30-90% mejor de lo que es. Ese error es la
razón por la que muchas operaciones COD "rentables" no tienen caja. Ver `30` y `229`.

## Errores

| Error | Consecuencia |
|---|---|
| Usar un ROAS objetivo "de la industria" (3,0, 4,0) | ignoras tu estructura de costos |
| Comparar ROAS entre países | el CPM y el flete son distintos |
| Fijar el umbral de pausa exactamente en el equilibrio | cero margen para variación diaria |
| Recalcular el equilibrio solo al lanzar | el costo puesto en bodega cambia con el tipo de cambio |

## Ejecución

El cálculo está incluido en el modelo de `228`. Para auditar, invoca `Matematicas_lushows`.

## Relacionados
`11` · `30` · `222` · `223` · `224` · `225` · `227` · `228` · `229` · `231` · `238` · `239`

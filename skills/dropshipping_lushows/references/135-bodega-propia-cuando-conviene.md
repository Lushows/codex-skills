# Bodega propia: cuándo conviene

> Vigencia: septiembre 2026. Rangos de costo indicativos; dependen de ciudad y contrato.

La bodega propia es la última etapa de la cadena de fulfillment y la que más gente monta demasiado
pronto, por romanticismo más que por cuentas. Es la opción correcta en un rango específico de
volumen, y una trampa fuera de él.

## Las cuatro etapas del fulfillment

| Etapa | Modelo | Volumen orientativo | Costo por pedido | Capital fijo |
|---|---|---|---|---|
| 1 | Plataforma COD / dropship | 0-150/mes | Alto | **$0** |
| 2 | 3PL | 150-1.500/mes | Medio | Bajo |
| 3 | **Bodega propia** | 300-3.000/mes | **Variable** | Medio-alto |
| 4 | Bodega + 3PL híbrido | 3.000+/mes | Bajo | Alto |

La etapa 3 se solapa con la 2 a propósito: **en ese rango la decisión no es de volumen, es de
control**.

## La estructura de costo de una bodega propia

| Concepto | Naturaleza | Nota |
|---|---|---|
| Arriendo del local | **Fijo** | La línea que te hunde en mes malo |
| Servicios (luz, internet, agua) | Fijo | |
| Estantería, mesas, básculas, impresora de guías | Inversión inicial | |
| Empaque (cajas, bolsas, cinta, etiquetas) | Variable | |
| **Personal** | **Fijo** | Con prestaciones. La línea más pesada. Invoca `contador_lushows` |
| Software de inventario / WMS | Fijo | |
| Seguro del inventario | Fijo | No lo omitas |
| Transporte a la transportadora | Variable | |
| **Tu tiempo** | Invisible pero real | El costo más subestimado |

**La diferencia clave con el 3PL:** el 3PL es casi todo costo variable; la bodega propia convierte tu
costo en fijo. Eso es apalancamiento cuando vendes mucho y una bomba cuando vendes poco.

## Cuándo la bodega propia SÍ conviene

| Situación | Por qué |
|---|---|
| Vendes **bundles complejos** que nadie arma como tú | El kitting propio es más flexible y barato |
| El producto necesita **preparación** (ensamble, prueba, etiquetado) | Ningún 3PL lo hará como tú |
| Tu **tasa de error** con 3PL es alta y te cuesta reputación | El control propio lo arregla |
| El **mínimo del 3PL** está muy por encima de tu volumen pero ya tienes inventario | Ver `134` |
| Ya tienes local, gente o espacio **con costo hundido** | El costo marginal es bajo |
| Volumen alto y estable donde el costo por pedido propio baja del de 3PL | Calcula el punto de cruce |
| Producto de alto valor donde el control físico importa | Robo y merma |

## Cuándo NO conviene (la mayoría de los casos)

| Situación | Por qué |
|---|---|
| Menos de 300 pedidos/mes | El fijo por pedido es prohibitivo |
| Producto no validado | Ver `138` |
| Estás solo y ya haces pauta, atención y compras | Empacar te roba el tiempo que genera ventas |
| Negocio muy estacional | Pagas el fijo 12 meses para operar 3 |
| Vendes en varios países | Necesitas bodega en cada uno |
| No tienes espacio adecuado | La sala de tu casa no escala y desgasta tu vida |

**El argumento definitivo: tu hora vale más haciendo creativos y cuentas que pegando cinta.** El día
que empacar te ocupa 3 horas diarias, esas 3 horas salieron de lo que hace crecer el negocio.

## La cuenta del punto de cruce

```
Costo mensual bodega propia = arriendo + servicios + personal + software + seguro
Costo por pedido propio     = (fijo mensual / pedidos_mes) + empaque + transporte

Costo por pedido 3PL        = (mínimo/pedidos_mes) + pick&pack + almacenaje/pedido

Punto de cruce = volumen donde ambos se igualan.
```

Ejemplo estructural (reemplaza con tus números reales; invoca `Matematicas_lushows`):

| Pedidos/mes | Costo/pedido bodega propia | Costo/pedido 3PL |
|---|---|---|
| 100 | Muy alto (fijo dividido entre pocos) | Alto (mínimo) |
| 300 | Comparable | Comparable |
| 800 | **Menor** | Medio |
| 2.000 | Mucho menor | Medio |

El cruce típico está entre 300 y 800 pedidos/mes, pero depende enormemente del costo laboral y del
arriendo de tu ciudad. **Haz la cuenta con cotizaciones reales, no con estos rangos.**

## La bodega en casa: el escalón intermedio honesto

Antes del local está el garaje o el cuarto. Es real y funciona en cierto rango:

| Pros | Contras |
|---|---|
| Costo marginal casi cero | Tope de espacio muy bajo (≈50-150 pedidos/mes) |
| Control total | Invade tu vida y la de tu familia |
| Aprendes la operación de verdad | No escala |
| Iteras el empaque sin pedir permiso | Riesgo si el producto es regulado o inflamable |

**Recomendación honesta:** usa la casa para los primeros 1-3 meses **si el volumen lo permite**, para
aprender la operación con tus propias manos. Ese aprendizaje vale. Pero pon fecha de salida.

## Lo que la bodega propia te da y el 3PL no

1. **Velocidad de iteración del empaque.** Puedes cambiar el inserto mañana.
2. **Kitting flexible.** Armar bundles distintos por campaña sin renegociar tarifas.
3. **Control de calidad de cada unidad** que sale.
4. **Detalle personalizado** (nota escrita a mano, regalo sorpresa) que mueve reseñas.
5. **Datos crudos** de merma, rotura y devolución sin intermediario.

Si tu diferenciación depende de alguna de estas, la bodega propia deja de ser un costo y se vuelve
parte del producto. Ver `126`, `127`.

## Errores frecuentes

| Error | Realidad |
|---|---|
| Montar bodega por orgullo | El fijo no se paga con orgullo |
| Contratar personal antes de tener volumen estable | Costo fijo con prestaciones. Invoca `contador_lushows` |
| Firmar arriendo largo en fase temprana | Busca contratos cortos o coworking logístico |
| No asegurar el inventario | Un incendio o robo termina el negocio |
| No contar tu propio tiempo como costo | Es el costo más grande y el más invisible |
| No llevar control de inventario formal | La merma aparece cuando ya es grave |
| Bodega en casa con producto regulado o inflamable | Riesgo legal y de seguro. Ver `143` |

## Lo mínimo para operar bien una bodega propia

1. **Sistema de inventario** (aunque sea Shopify + una hoja disciplinada). Sin conteo no hay control.
2. **Ubicaciones etiquetadas**. Cada SKU en un lugar fijo.
3. **Conteo cíclico semanal** de los SKUs de mayor rotación.
4. **Estación de empaque** con todo a mano: la productividad se gana en la ergonomía.
5. **Impresora térmica de guías.** Deja de imprimir en hojas y pegar con cinta.
6. **Registro de merma y rotura** por SKU. Es información de proveedor. Ver `144`.
7. **Corte horario propio** y cumplido: la promesa de entrega depende de él.

## Para el proyecto activo (México, diciembre 2026)

Bodega propia **no aplica en diciembre**, ni de cerca. Dropi MX hace tu fulfillment sin capital ni
fijo. Ver `132`.

La única versión válida en tu caso sería armar bundles en casa si compras a mayorista mexicano y
despachas tú con guías prepagadas. Eso es viable con volumen bajo y te enseña la operación, pero
cuenta tu tiempo: si el bundle te toma 6 minutos armarlo y despachas 10 al día, es una hora diaria
que no estás haciendo creativos en el mes más competido del año.

## Relacionados
Ver `132`, `133`, `134`, `136`, `137`, `138`, `126`, `127`, `144`.

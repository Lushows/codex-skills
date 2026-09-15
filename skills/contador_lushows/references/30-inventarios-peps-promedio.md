# 30 — Inventarios: PEPS y promedio ponderado

El **inventario** es la mercancía que tu negocio tiene para vender (los productos en la bodega) o los insumos que usará para producir. En un restaurante son la carne, las verduras, el licor; en una tienda son los productos en estantería. El problema es sencillo de plantear y traicionero de resolver: cuando compras lo mismo a precios distintos en momentos distintos, ¿a qué precio sacas lo que vendes? La respuesta cambia tu costo de ventas y, por lo tanto, tu utilidad y tus impuestos. Por eso hay que elegir un **método de valuación** y mantenerlo.

Bajo **NIIF para pymes** (las normas contables que usan la mayoría de negocios colombianos, ver módulo de entorno) el inventario se mide al **menor entre el costo y el valor neto de realización** (lo que esperas recibir al venderlo, menos los gastos para venderlo). Y solo se permiten dos métodos: **PEPS** y **promedio ponderado**. El método UEPS está **prohibido**.

## Los dos métodos permitidos

| Método | Qué supone | Cuándo conviene |
|---|---|---|
| **PEPS** (Primeras Entradas, Primeras Salidas) | Lo primero que entra es lo primero que sale | Productos perecederos (alimentos, medicinas): refleja la rotación física real |
| **Promedio ponderado** | Cada salida sale al costo promedio de lo disponible | Insumos homogéneos a granel (harina, aceite); más simple de llevar |

> **UEPS** (Últimas Entradas, Primeras Salidas) está **prohibido por NIIF**. Si alguien te lo propone "para pagar menos impuestos", no se puede usar en estados financieros NIIF.

El método elegido debe aplicarse de forma **consistente** período tras período. Cambiarlo a conveniencia rompe la comparabilidad y enciende alarmas en una auditoría.

## Ejemplo comparado (cifras ILUSTRATIVAS / inventadas)

Una cafetería compra café en grano y luego vende 30 kg:

| Movimiento | Cantidad | Costo unitario | Costo total |
|---|---|---|---|
| Compra 1 | 20 kg | $20.000 | $400.000 |
| Compra 2 | 20 kg | $26.000 | $520.000 |
| **Disponible** | **40 kg** | — | **$920.000** |
| Venta | 30 kg | (según método) | ? |

**Con PEPS:** salen primero los 20 kg a $20.000 ($400.000) y luego 10 kg a $26.000 ($260.000) → costo de venta = **$660.000**; quedan 10 kg a $26.000 = $260.000 en inventario.

**Con promedio:** costo promedio = $920.000 / 40 kg = **$23.000/kg** → costo de venta = 30 × $23.000 = **$690.000**; quedan 10 kg × $23.000 = $230.000.

> El cálculo exacto del promedio ponderado (con muchas compras y decimales) **NO se hace de cabeza**: se ejecuta y verifica con `Matematicas_lushows` usando tipo `decimal`. Las cifras de arriba son inventadas para ilustrar.

## Asiento al registrar el costo de la venta (PEPS, cifras inventadas)

| Cuenta | Débito | Crédito |
|---|---|---|
| Costo de ventas | $660.000 | |
| Inventario de mercancías | | $660.000 |

Débitos = créditos = $660.000. El inventario baja y el costo sube en el mismo momento de la venta (sistema de inventario permanente, el más recomendado).

## Errores comunes

- **Cambiar de método cada año** para "acomodar" la utilidad. NIIF exige consistencia.
- **Usar UEPS** porque "baja el impuesto": está prohibido y un auditor lo rechaza.
- **No registrar el deterioro**: si el café se daña o su valor de venta cae por debajo del costo, hay que bajarlo al valor neto de realización.
- **Calcular el promedio de memoria** con muchas compras: produce centavos descuadrados.
- **No conteo físico**: el inventario en libros debe cuadrar contra el conteo real (toma física).

## Conexión con otros módulos

- El **costo de ventas** que sale de aquí se desarrolla en el módulo **38**.
- Los principios de cuadre y soporte vienen del método base (módulo **00**).
- El cálculo exacto del promedio o de capas PEPS lo ejecuta **Matematicas_lushows**.
- Si la mercancía pierde valor, aplica **deterioro**, relacionado con las estimaciones del módulo **36**.
- Decidir *qué* vender o a qué precio es decisión de negocio → **economist_lushows**.

## Siguiente paso típico

Define un único método (PEPS para perecederos, promedio para insumos a granel), déjalo por escrito en tus políticas contables y conéctalo con el costo de ventas del módulo **38**.

# 159 — Presupuesto y control presupuestal

Un **presupuesto** es el plan en números de lo que esperas que el negocio venda, gaste y le quede en un período (un mes, un trimestre, un año). El **control presupuestal** es comparar, período tras período, ese plan contra **lo que realmente pasó** y entender por qué hubo diferencias. Sin presupuesto, manejas el negocio mirando por el retrovisor; con él, tienes un mapa y sabes cuándo te estás saliendo de la ruta a tiempo para corregir.

Aquí vemos cómo **armar el presupuesto y controlarlo** desde la operación contable. La estrategia de fondo (qué metas perseguir, qué mercado, qué precios) la define `economist_lushows`; todo cálculo de cifras y proyección se ejecuta en `Matematicas_lushows`.

## Tipos de presupuesto

| Presupuesto | Qué planea |
|---|---|
| De ingresos / ventas | Cuánto esperas vender |
| De costos y gastos | Cuánto esperas gastar para vender y operar |
| De inversión (capex) | Compras grandes de activos (máquinas, equipos) |
| De efectivo / tesorería | Las entradas y salidas de plata (se enlaza con el flujo de caja, módulo **151**) |

Lo común es armar el de ventas primero, porque casi todo lo demás depende de cuánto vendas.

## El proceso

| Paso | Qué haces |
|---|---|
| 1 | Defines metas realistas (apoyado en el histórico y en `economist_lushows`) |
| 2 | Presupuestas ingresos, luego costos y gastos |
| 3 | Lo divides por mes para poder controlarlo seguido |
| 4 | Al cierre de cada mes, traes lo **real** desde la contabilidad |
| 5 | Comparas real vs. presupuesto y analizas las **variaciones** |

## Variaciones: el corazón del control

Una **variación** es la diferencia entre lo presupuestado y lo real. Lo importante no es el número, sino **entender por qué** y actuar.

| Variación | Qué puede significar |
|---|---|
| Ventas reales < presupuesto | Demanda floja, perdiste un cliente, precio muy alto |
| Gastos reales > presupuesto | Sobrecosto, gasto no previsto, fuga de plata |
| Favorable | Lo real fue mejor que el plan (más ventas o menos gasto) |
| Desfavorable | Lo real fue peor que el plan |

Que una variación sea "favorable" no siempre es bueno: vender más sin haber comprado inventario suficiente puede traer problemas de cumplimiento.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Comparativo de un mes (cifras inventadas):

| Concepto | Presupuesto | Real | Variación |
|---|---|---|---|
| Ventas | $50.000.000 | $46.000.000 | −$4.000.000 (desfavorable) |
| Costo de ventas | $30.000.000 | $29.000.000 | +$1.000.000 (favorable) |
| Gastos | $12.000.000 | $14.000.000 | −$2.000.000 (desfavorable) |
| **Utilidad** | $8.000.000 | $3.000.000 | −$5.000.000 |

La utilidad cayó $5.000.000: vendiste menos y gastaste más de lo planeado. Eso dispara la pregunta "¿por qué?" para corregir el próximo mes. Cifras inventadas; toda resta y porcentaje de variación se verifica con `Matematicas_lushows`.

## Errores comunes

- **Presupuestar optimista**: metas infladas que nadie cree y que descuadran la caja.
- **Armar el presupuesto y nunca controlarlo**: queda en un cajón y no sirve de nada.
- **Mirar la variación sin investigar la causa**: el número solo no corrige nada.
- **No conectar el presupuesto con el flujo de caja** (**151**): puedes ser "rentable en el plan" y quedarte sin efectivo.
- **Calcular variaciones y porcentajes de cabeza**: siempre a `Matematicas_lushows`.

## Conexión con otros módulos

- El presupuesto de efectivo se enlaza con el flujo de caja proyectado (**151**).
- Lo "real" se trae de los estados financieros (**21** resultados) y del análisis vertical/horizontal (**26**).
- La definición de metas y estrategia → `economist_lushows`; todo cálculo y proyección → `Matematicas_lushows`.

## Siguiente paso típico

Arma el presupuesto del próximo año dividido por mes (empezando por ventas), enlázalo con el flujo de caja (**151**), y monta la rutina de comparar real vs. presupuesto cada cierre de mes investigando cada variación importante.

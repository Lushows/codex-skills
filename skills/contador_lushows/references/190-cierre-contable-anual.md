# 190 — Cierre contable anual: paso a paso

El **cierre anual** es el ritual más importante del año contable: es el momento en que verificas que todo cuadre, ajustas lo que falte, calculas cuánto ganó o perdió el negocio y dejas los libros listos y blindados para una eventual revisión de la DIAN o de los socios. El módulo 18 explicó el mecanismo de saldar cuentas; aquí te doy el **proceso completo de fin de año**, con checklist y orden de tareas.

> **Cierre contable anual** = conjunto de tareas que se hacen sobre el corte del 31 de diciembre (o el fin del período fiscal) para producir estados financieros confiables y soportar las declaraciones. Donde "todo se verifica".

## El cierre tiene tres capas

| Capa | Pregunta que responde | Salida |
|---|---|---|
| **Contable** | ¿Cuánto ganó/perdió y qué tengo? | Estados financieros (Bloque 2) |
| **Fiscal** | ¿Cuánto le debo a la DIAN? | Conciliación fiscal y declaración (módulo 191, 42) |
| **Documental** | ¿Está todo soportado? | Archivo, papeles de trabajo (módulos 97, 72) |

Un cierre que solo cierra lo contable, sin la capa fiscal ni la documental, **no está terminado**.

## Checklist de cierre anual (en orden)

1. **Concilia bancos** — todos los extractos vs. libros (módulo 35). Saldo en libros = saldo real.
2. **Concilia cartera y proveedores** — confirma cuentas por cobrar (33) y por pagar (34); ajusta lo incobrable.
3. **Toma física de inventario** — cuenta lo que hay y compáralo con el kárdex (módulos 30, 76).
4. **Activos fijos** — verifica que existan y registra la **depreciación** del año (módulo 32).
5. **Causaciones pendientes** — servicios usados y no facturados, intereses, etc. (módulo 16).
6. **Nómina y prestaciones** — provisiona cesantías, intereses, prima, vacaciones (módulos 52, 58).
7. **Provisiones y estimaciones** — deudas incobrables, contingencias (módulos 36, 197).
8. **Impuestos por pagar** — IVA, ICA, retenciones del último período (Bloque 4).
9. **Balance de comprobación ajustado** — debe **cuadrar** (módulo 15).
10. **Cierre de cuentas de resultado** y traslado de utilidad/pérdida (módulo 18).
11. **Armar estados financieros** (Bloque 2) con notas (módulo 24).
12. **Conciliación fiscal / Formato 2516** (módulo 191).
13. **Archivar soportes** y dejar papeles de trabajo (módulos 97, 72).

## Ejemplo de ajustes de fin de año (cifras ILUSTRATIVAS / inventadas)

Un restaurante llega a diciembre y antes de cerrar detecta:

| Ajuste | Débito | Crédito |
|---|---|---|
| Depreciación equipo de cocina del año | Gasto depreciación 30.000 | Depreciación acumulada 30.000 |
| Provisión cesantías empleados | Gasto cesantías 12.000 | Cesantías por pagar 12.000 |
| Cliente incobrable confirmado | Gasto deterioro 5.000 | Deterioro cartera 5.000 |
| Arriendo de diciembre usado, no facturado | Gasto arriendo 4.000 | Cuentas por pagar 4.000 |

Sin estos ajustes la utilidad saldría **inflada** y pagarías más impuesto del debido (o menos, y te expones a sanción). Por eso el ajuste va **antes** del cálculo de la utilidad.

> El cálculo de depreciación, provisiones y de la utilidad final NUNCA se hace de cabeza: se ejecuta y verifica en código (a `Matematicas_lushows`).

## Calendario realista del cierre

- **Noviembre**: pre-cierre, depura cuentas, avisa a socios qué documentos faltan.
- **Diciembre 31**: corte. Toma física de inventario y arqueo de caja ese día.
- **Enero–febrero**: conciliaciones, ajustes, estados financieros.
- **Marzo en adelante**: conciliación fiscal y declaración de renta (verifica el calendario tributario del año, módulo 46 — las fechas cambian cada año).

## Errores comunes

- **Cerrar sin conciliar bancos ni inventario**: arrastras errores a todo el año siguiente.
- **No provisionar prestaciones ni depreciación**: la utilidad queda falsa.
- **Dejar el cierre fiscal para el final sin haber cerrado lo contable**: terminas corriendo y cometiendo errores.
- **No archivar soportes**: cuadra el papel pero no resiste una auditoría (rompe la promesa AUDITABLE).
- **Calcular utilidad e impuestos de cabeza** en vez de en código.

## Conexión con otros módulos

- **Módulo 18** — el mecanismo de cerrar cuentas de resultado.
- **Módulos 16, 17** — ajustes y causaciones que van antes del cierre.
- **Módulo 15** — el balance ajustado debe cuadrar.
- **Módulo 191** — la conciliación fiscal (Formato 2516) que sigue al cierre contable.
- **Módulo 198** — checklist final de calidad antes de entregar.
- **Bloque 2** — los estados financieros que produce el cierre.
- **Matematicas_lushows** EJECUTA depreciación, provisiones y utilidad.

## Siguiente paso típico

Con el cierre contable cuadrado y soportado, pasa al **módulo 191** para hacer la conciliación fiscal (Formato 2516) y de ahí a la declaración de renta.

# 89 — Plantillas de registro: asientos, libros y soportes listos para usar

Tener buenas **plantillas** es la diferencia entre llevar la contabilidad con orden o reinventar la rueda cada mes. Una plantilla bien hecha ya trae las columnas correctas, las fórmulas de cuadre y el espacio para el soporte. Este módulo entrega los **formatos básicos** que todo negocio necesita, listos para copiar a Excel, Google Sheets o el software contable, explicados campo por campo.

La idea no es solo "dar formatos", sino que cada plantilla **arrastre la disciplina** de la casa: que el asiento cuadre, que haya soporte y que todo sea rastreable.

> **Plantillas que cuadran y se pueden auditar.** Cada formato incluye su columna de **soporte** (qué documento respalda el registro) y, donde aplica, una celda de **control de cuadre**. Las sumas grandes se verifican en `Matematicas_lushows`, no de cabeza.

## Términos que debes conocer
- **Asiento:** registro de un movimiento en partida doble (un débito y un crédito que se igualan).
- **Soporte:** el documento que prueba el registro (factura, recibo, extracto).
- **Consecutivo:** número que ordena cada registro (1, 2, 3...) para rastrearlo.
- **Auxiliar:** libro detallado de UNA cuenta (todos los movimientos de "Banco", por ejemplo).

## Plantilla 1 — Libro diario (asientos)
| Fecha | Consecutivo | Descripción | Cuenta (PUC) | Débito | Crédito | Soporte |
|---|---|---|---|---|---|---|
| 2026-03-05 | 001 | Compra insumos | 6135 Compras | 1.000.000 | | FV-2034 |
| 2026-03-05 | 001 | IVA descontable | 2408 IVA | 190.000 | | FV-2034 |
| 2026-03-05 | 001 | Pago a proveedor | 1110 Banco | | 1.190.000 | FV-2034 |
> Regla: por cada asiento, **suma de débitos = suma de créditos**. (Cifras ILUSTRATIVAS / inventadas.)

## Plantilla 2 — Libro auxiliar por cuenta
| Fecha | Descripción | Débito | Crédito | Saldo |
|---|---|---|---|---|
| 2026-03-01 | Saldo inicial | | | 5.000.000 |
| 2026-03-05 | Pago proveedor | | 1.190.000 | 3.810.000 |
> Una hoja por cuenta (Banco, Caja, Clientes...). El **saldo** se arrastra con fórmula. (Cifras inventadas.)

## Plantilla 3 — Balance de prueba (control de cuadre)
| Código | Cuenta | Débito | Crédito |
|---|---|---|---|
| 1110 | Banco | 3.810.000 | |
| 6135 | Compras | 1.000.000 | |
| ... | ... | ... | ... |
| | **TOTAL** | **=SUMA(...)** | **=SUMA(...)** |
> Celda de control: `=SI(total_débito=total_crédito;"CUADRA";"REVISAR")`. (Cifras inventadas.)

## Plantilla 4 — Conciliación bancaria
| Concepto | Valor |
|---|---|
| Saldo según libros | 4.820.000 |
| (–) Comisiones no registradas | 50.000 |
| (+) Cheques no cobrados | 0 |
| **Saldo conciliado** | **=...** |
| Saldo según extracto | 4.770.000 |
> Deben **coincidir** saldo conciliado y extracto (ver 83). (Cifras inventadas.)

## Plantilla 5 — Control de soportes
| Consecutivo asiento | Tipo de soporte | Número | Archivo / ubicación | Respaldado |
|---|---|---|---|---|
| 001 | Factura compra | FV-2034 | /soportes/2026-03/FV-2034.pdf | Sí |
> Conecta cada asiento con su documento; clave para auditoría (ver 87).

## Buenas prácticas con las plantillas
- **Nunca un asiento sin soporte:** la columna de soporte no se deja vacía.
- **Usa consecutivos** para rastrear de un vistazo.
- **Protege las celdas de fórmula** (ver 80) para no dañar el cuadre.
- **Una versión por mes**, con fecha, y respaldada (ver 87).
- Si usas software contable, estas plantillas **ya vienen integradas**; úsalas como guía para entender qué hace el sistema.

## Errores comunes
- Registrar sin soporte → asiento que no se puede auditar.
- Borrar la fórmula de cuadre y escribir el total a mano → se pierde el control.
- No usar consecutivos → imposible rastrear un movimiento después.
- Mezclar varios meses en una sola hoja → desorden y errores de saldo.

## Conexión con otros módulos
- **11–12 (cuentas T y asientos)** — la teoría detrás de la plantilla 1.
- **10 (PUC)** — los códigos de cuenta que van en los asientos.
- **20–21 (estados financieros)** — salen del balance de prueba (plantilla 3).
- **80 (Excel)** y **83 (conciliación)** — fórmulas y la plantilla 4.
- **87 (respaldos)** — guardar plantillas y soportes.
- **Matematicas_lushows** — verificar sumas y cuadres.

## Siguiente paso típico
Con las plantillas listas, ejecutar el mes completo siguiendo la rutina: volver a **88 (flujo de trabajo mensual)** y empezar por la captura de documentos.

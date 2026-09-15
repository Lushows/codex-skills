# 12 — El asiento contable: cómo registrar un hecho

Un **asiento** (o "comprobante de diario") es el registro formal de un hecho económico en partida doble. Es la unidad mínima de la contabilidad: cada compra, venta o pago se convierte en un asiento que **siempre cuadra**.

> **Asiento contable** = anotación que dice, para una fecha, qué cuentas se debitan y cuáles se acreditan, por qué, y con qué documento de respaldo.

## Anatomía de un asiento

Un asiento bien hecho tiene SIEMPRE estos elementos:

| Elemento | Qué es | Ejemplo |
|---|---|---|
| Fecha | Cuándo ocurrió el hecho | 2026-03-15 |
| Cuentas | Qué casillas del PUC se afectan | Caja, Ventas, IVA |
| Débito / Crédito | El valor a cada lado | 119.000 / 100.000 + 19.000 |
| Concepto | Explicación en una línea | "Venta de contado factura #045" |
| Soporte | Documento que lo prueba | Factura electrónica #045 |

**Regla AUDITABLE:** ningún asiento sin **soporte**. Si no hay factura, recibo, extracto o comprobante, no se registra. El soporte es lo que te salva en una auditoría DIAN.

## Ejemplo 1 — Venta de contado (cifras ILUSTRATIVAS / inventadas)

Vendes mercancía por $100.000 + IVA 19% ($19.000), te pagan en efectivo. Total recibido: $119.000.

| Cuenta | Débito | Crédito |
|---|---|---|
| Caja (1105) | 119.000 | |
| Ventas (4135) | | 100.000 |
| IVA generado por pagar (2408) | | 19.000 |
| **Totales** | **119.000** | **119.000** |

Lectura: entra plata (Caja sube → débito); ganas un ingreso (Ventas sube → crédito); el IVA que cobraste **no es tuyo**, lo debes a la DIAN (Pasivo sube → crédito).

> El IVA del 19% es ilustrativo; **verifica la tarifa vigente** del producto/servicio antes de aplicarla.

## Ejemplo 2 — Compra de mercancía a crédito (cifras ILUSTRATIVAS / inventadas)

Compras inventario por $50.000, lo pagarás en 30 días.

| Cuenta | Débito | Crédito |
|---|---|---|
| Inventarios (1435) | 50.000 | |
| Proveedores (2205) | | 50.000 |
| **Totales** | **50.000** | **50.000** |

## Ejemplo 3 — Pago a un proveedor (cifras ILUSTRATIVAS / inventadas)

Pagas esos $50.000 al proveedor desde el banco.

| Cuenta | Débito | Crédito |
|---|---|---|
| Proveedores (2205) | 50.000 | |
| Bancos (1110) | | 50.000 |
| **Totales** | **50.000** | **50.000** |

Nota: la deuda (Pasivo) baja → va al débito; el banco baja → va al crédito.

## Pasos para registrar cualquier asiento

1. Lee el **soporte** y entiende qué pasó realmente.
2. Lista las cuentas afectadas (módulo 10).
3. Decide débito/crédito por naturaleza (módulo 11).
4. Escribe los valores. **Suma cada lado** (en código, no de cabeza).
5. Verifica: **débitos = créditos**. Si no, corrige antes de guardar.
6. Archiva el soporte enlazado al asiento.

## Errores comunes

- **Registrar sin soporte** ("luego consigo la factura"). No.
- **Omitir el IVA o la retención** en ventas/compras gravadas.
- **Confundir un anticipo con un ingreso**: un anticipo es pasivo hasta que entregas.
- **Sumar mal** los renglones múltiples; ejecuta el total en código.
- **Concepto vago** ("varios") que nadie entiende meses después.

## Conexión con otros módulos

- **Módulo 11** — la regla débito/crédito que aquí aplicas.
- **Módulo 13** — todos los asientos van, en orden, al libro diario.
- **Módulo 16** — los asientos de ajuste de fin de período.
- **Matematicas_lushows** verifica IVA, retenciones y totales; el contador arma el asiento.

## Siguiente paso típico

Pasa al **módulo 13**: cómo se acumulan todos estos asientos, en orden, en el libro diario.

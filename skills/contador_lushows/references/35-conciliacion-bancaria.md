# 35 — Conciliación bancaria

La **conciliación bancaria** es el acto de comparar, línea por línea, lo que dicen tus libros contables (lo que tú anotaste que tienes en el banco) contra lo que dice el **extracto bancario** (lo que el banco dice que tienes). Casi nunca coinciden a la primera, y eso es normal: hay cheques que aún no cobraron, consignaciones que el banco aún no procesó, comisiones que el banco te cobró sin avisar. Conciliar es encontrar y explicar **cada diferencia** hasta que los dos saldos cuadren.

Es la práctica más importante para que tu contabilidad sea **auditable**: el banco es un tercero independiente. Si tus libros cuadran contra el banco, tienes una prueba externa de que tu efectivo es real. Si no cuadran, hay un error o algo que se te escapó.

## El paso a paso

| Paso | Qué haces |
|---|---|
| 1 | Tomas el saldo en libros y el saldo del extracto a la misma fecha de corte |
| 2 | Marcas las partidas que aparecen en **ambos** (coinciden) |
| 3 | Identificas lo que está en el banco pero **no** en tus libros |
| 4 | Identificas lo que está en tus libros pero **no** en el banco |
| 5 | Registras en tus libros lo que faltaba (comisiones, intereses, etc.) |
| 6 | Confirmas que, ajustado, los dos saldos coinciden |

## Partidas conciliatorias típicas

| Partida | Dónde aparece | Qué hacer |
|---|---|---|
| **Cheques girados sin cobrar** | En libros, no en banco | Esperar; no es error |
| **Consignaciones en tránsito** | En libros, no en banco | Esperar a que el banco la procese |
| **Comisiones / cuota de manejo** | En banco, no en libros | Registrarlas como gasto |
| **Intereses ganados** | En banco, no en libros | Registrarlos como ingreso |
| **Notas débito (cobros del banco)** | En banco, no en libros | Registrarlas |
| **Errores de digitación** | Donde se equivocó quien anotó | Corregir con soporte |

Las dos primeras se ajustan **solas con el tiempo**: no se registra nada, solo se espera. Las demás **sí** requieren un asiento porque tus libros no las tenían.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Saldo en libros: $5.000.000. Saldo en extracto: $4.880.000. Encuentras: el banco cobró $20.000 de cuota de manejo y hay un cheque girado por $100.000 que el proveedor aún no cobró.

Ajuste a libros (la cuota de manejo que no tenías registrada):

| Cuenta | Débito | Crédito |
|---|---|---|
| Gastos bancarios | $20.000 | |
| Bancos | | $20.000 |

Tras registrar: libros = $5.000.000 − $20.000 = $4.980.000. Extracto $4.880.000 + cheque sin cobrar $100.000 = $4.980.000. **Cuadran.** El cheque no se ajusta: se cobrará solo. Cifras inventadas para ilustrar; cualquier suma se verifica con `Matematicas_lushows`.

## Errores comunes

- **No conciliar nunca**: el saldo en libros se aleja de la realidad y nadie lo nota hasta que rebota un pago.
- **"Forzar" el cuadre** metiendo un ajuste sin explicación: destruye la auditabilidad.
- **Registrar como ajuste un cheque sin cobrar**: no es un ajuste, se concilia solo.
- **Olvidar las comisiones del banco**: son gasto real que casi nadie anota a tiempo.
- **Conciliar cifras de fechas distintas**: hay que usar el mismo corte en libros y extracto.

## Conexión con otros módulos

- Confirma los pagos de las **cuentas por pagar** (módulo **34**) y los cobros de **cuentas por cobrar** (módulo **33**).
- Es el paso 3 ("Conciliar") del ciclo del contador descrito en el módulo **00**.
- Da soporte externo a los **estados financieros** (módulos de reportes).
- Cualquier suma o diferencia se verifica con **Matematicas_lushows**.

## Siguiente paso típico

Concilia el banco **cada mes** apenas llegue el extracto, registra de inmediato comisiones e intereses, y archiva el extracto como soporte. Luego cruza con cartera (33) y proveedores (34).

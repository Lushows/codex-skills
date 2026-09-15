# 11 — La cuenta T: débitos y créditos sin equivocarte

Esta es la **gramática** de la contabilidad. Si entiendes esto, todo lo demás se vuelve fácil. La idea es simple: cada cuenta tiene **dos lados**, y dibujarla como una **T** te ayuda a no perderte.

> **Débito** (también "cargo" o "Debe") = el lado **izquierdo** de la T.
> **Crédito** (también "abono" o "Haber") = el lado **derecho** de la T.
> OJO: "débito" NO significa "salida" ni "crédito" significa "entrada". Eso depende de la naturaleza de la cuenta (ver abajo). Este es el error #1 de todo principiante.

## Cómo se ve una cuenta T

```
        Caja (Activo)
   Débito    |   Crédito
   (Debe)    |   (Haber)
-------------|-------------
  500.000    |
             |   200.000
-------------|-------------
 Saldo: 300.000 (deudor)
```

## La regla de oro por naturaleza

Cada clase del PUC tiene una **naturaleza**: o es de naturaleza **débito** (aumenta por el débito) o de naturaleza **crédito** (aumenta por el crédito).

| Clase | Naturaleza | Aumenta con | Disminuye con | Saldo normal |
|---|---|---|---|---|
| 1 Activo | Débito | Débito | Crédito | Deudor |
| 5 Gasto | Débito | Débito | Crédito | Deudor |
| 6 Costo | Débito | Débito | Crédito | Deudor |
| 2 Pasivo | Crédito | Crédito | Débito | Acreedor |
| 3 Patrimonio | Crédito | Crédito | Débito | Acreedor |
| 4 Ingreso | Crédito | Crédito | Débito | Acreedor |

**Truco para memorizar — "ADEGA al revés":** los que **A**umentan por **D**ébito son **A**ctivos, **G**astos y costos (lo que el negocio usa/tiene). Todos los demás (Pasivo, Patrimonio, Ingreso) aumentan por crédito.

## La ley que nunca se rompe

> En **todo** asiento, la suma de los **débitos = la suma de los créditos**. Si no cuadra, está mal. No hay excepciones. Esto es la **partida doble**.

Cada hecho económico toca **al menos dos cuentas**: una recibe (débito) y otra entrega (crédito), por el mismo valor total.

## Ejemplo numérico (cifras ILUSTRATIVAS / inventadas)

Recibes un préstamo del banco por $1.000.000 que entra a tu cuenta bancaria.

- Bancos (Activo) **aumenta** → naturaleza débito → va al **Débito**.
- Obligaciones financieras (Pasivo) **aumenta** → naturaleza crédito → va al **Crédito**.

| Cuenta | Débito | Crédito |
|---|---|---|
| Bancos (1110) | 1.000.000 | |
| Obligaciones financieras (2105) | | 1.000.000 |
| **Totales** | **1.000.000** | **1.000.000** |

Cuadra: 1.000.000 = 1.000.000. ✅

## Cómo decidir, paso a paso

1. Identifica las cuentas que toca el hecho.
2. Para cada una pregunta: **¿aumenta o disminuye?**
3. Mira su **naturaleza** en la tabla de arriba.
4. Aumentar por su naturaleza → va al lado natural; disminuir → va al lado contrario.
5. **Verifica que débitos = créditos.** Si no cuadra, revisa, no fuerces.

## Errores comunes

- **Creer que débito = sacar y crédito = meter.** Falso: depende de la naturaleza de la cuenta.
- **Asientos que no cuadran** y "ajustarlos" metiendo un número a la fuerza.
- **Olvidar que un gasto aumenta por débito** (mucha gente lo registra al revés).
- **Hacer la cuenta de cabeza** cuando hay varios renglones: súmalos en código o ruta a `Matematicas_lushows`.

## Conexión con otros módulos

- **Módulo 10** — de qué clase es cada cuenta (define su naturaleza).
- **Módulo 12** — armar asientos completos con varias cuentas.
- **Módulo 15** — el balance de comprobación verifica que el total de débitos = total de créditos.
- **Matematicas_lushows** EJECUTA las sumas; el contador define qué va a cada lado.

## Siguiente paso típico

Ve al **módulo 12** para armar asientos reales (venta, compra, pago) usando estas reglas.

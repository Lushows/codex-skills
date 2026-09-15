# 15 — Balance de comprobación: la prueba de que todo cuadra

Antes de armar tus estados financieros, necesitas una **prueba rápida** de que la contabilidad no se rompió: el **balance de comprobación** (o "balance de prueba"). Pone en una sola tabla el saldo de TODAS las cuentas y verifica que el total de débitos = total de créditos.

> **Balance de comprobación** = listado de todas las cuentas con sus saldos deudores y acreedores, cuyos totales deben ser **idénticos**.

## Por qué importa

- Es el **chequeo de salud** de la partida doble: si no cuadra, hay un error de registro.
- Es el **puente** entre el libro mayor (módulo 14) y los estados financieros.
- Permite revisar saldos raros **antes** de presentar cifras a nadie.

> Ojo: que cuadre **no garantiza** que esté bien. Puedes haber usado la cuenta equivocada y aun así cuadrar. Cuadrar es **necesario pero no suficiente**.

## Cómo se arma

1. Toma cada cuenta del libro mayor con su saldo.
2. Ponla en la columna **deudor** o **acreedor** según su naturaleza.
3. Suma cada columna (en código).
4. Verifica que **Total deudor = Total acreedor**.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Usamos los saldos del módulo 14 (ajusto Bancos a un saldo positivo realista para el ejemplo: supongamos que había un saldo inicial de 200.000, queda 170.000).

| Cuenta | Deudor | Acreedor |
|---|---|---|
| Caja (1105) | 119.000 | |
| Bancos (1110) | 170.000 | |
| Inventarios (1435) | 50.000 | |
| Proveedores (2205) | | 50.000 |
| IVA generado (2408) | | 19.000 |
| Capital social (3115) | | 200.000 |
| Ventas (4135) | | 100.000 |
| Arrendamientos (5120) | 30.000 | |
| **TOTALES** | **369.000** | **369.000** |

Cuadra: 369.000 = 369.000. ✅ La partida doble sobrevivió.

> El saldo de Capital (200.000) representa el dinero que el dueño puso al inicio; aquí lo incluyo para que el ejemplo cuadre. Todas las cifras son inventadas.

## Tipos de balance de comprobación

| Tipo | Qué muestra |
|---|---|
| De sumas | Total debitado y total acreditado de cada cuenta |
| De saldos | Solo el saldo final de cada cuenta (el más usado) |
| De sumas y saldos | Ambas cosas en una tabla más amplia |

## Qué hacer si NO cuadra

1. **Revisa la suma** de las columnas (¿error de cálculo? recalcula en código).
2. Busca un asiento **descuadrado** en el diario (débitos ≠ créditos).
3. Busca un valor **invertido** (lo que iba al débito quedó en crédito).
4. Busca un **dígito traspuesto** (escribiste 1.900 en vez de 1.090): si la diferencia es divisible por 9, suele ser eso.
5. Nunca "cuadres a la fuerza" metiendo un valor de relleno.

## Errores comunes

- **Forzar el cuadre** con un ajuste inventado en vez de hallar el error.
- **Creer que cuadrar = estar correcto** (puede haber cuenta mal elegida).
- **Olvidar incluir una cuenta** con saldo.
- **Sumar de cabeza** columnas largas; ejecuta en código.

## Conexión con otros módulos

- **Módulo 14** — los saldos vienen del libro mayor.
- **Módulo 16** — después del balance se hacen los asientos de ajuste y se vuelve a comprobar.
- **Módulo 18** — tras ajustar y comprobar, se cierra y se arman estados financieros.
- **Matematicas_lushows** verifica las sumas y la "regla del 9" para hallar trasposiciones.

## Siguiente paso típico

Pasa al **módulo 16**: los asientos de ajuste de fin de período (depreciación, devengos, provisiones) que se hacen antes del cierre.

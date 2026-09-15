# 02 — La ecuación contable y la partida doble

Este es el corazón de la contabilidad. Si entiendes este módulo, entiendes el 80% de lo demás. Todo —absolutamente todo— se reduce a una ecuación que nunca se rompe y a una regla de doble anotación. Lo vamos a explicar despacio y con ejemplos que cuadran al centavo.

## La ecuación contable

Toda la contabilidad se sostiene en una sola fórmula:

> **Activo = Pasivo + Patrimonio**

Traducción humana:

- **Activo** = lo que el negocio *tiene* (efectivo, equipos, inventario, lo que te deben).
- **Pasivo** = lo que el negocio *debe* a terceros (préstamos, proveedores, impuestos por pagar).
- **Patrimonio** = lo que es *realmente tuyo* (tus aportes + las ganancias acumuladas).

La idea de fondo: todo lo que el negocio tiene fue financiado por alguien. O lo prestó un tercero (pasivo) o lo pusiste tú / lo generó el negocio (patrimonio). Por eso la balanza **siempre** está en equilibrio.

A veces verás una versión ampliada con ingresos y gastos:

> **Activo = Pasivo + Patrimonio + (Ingresos − Gastos)**

Porque los ingresos aumentan tu riqueza y los gastos la disminuyen; al final del periodo se "cierran" contra el patrimonio.

## La partida doble

**Regla:** cada hecho económico afecta **al menos dos cuentas**, y la suma de débitos siempre iguala la suma de créditos. Por eso se llama partida *doble*.

No te dejes confundir por las palabras: **débito y crédito NO significan "bueno" o "malo", ni "entra/sale plata"**. Son simplemente el lado izquierdo (débito) y el lado derecho (crédito) de cada cuenta. Lo que significan depende de la *naturaleza* de la cuenta.

## Débito y crédito por naturaleza de cuenta

| Tipo de cuenta | Aumenta con… | Disminuye con… | Naturaleza |
|---|---|---|---|
| Activo | Débito | Crédito | Débito |
| Pasivo | Crédito | Débito | Crédito |
| Patrimonio | Crédito | Débito | Crédito |
| Ingreso | Crédito | Débito | Crédito |
| Gasto / Costo | Débito | Crédito | Débito |

Regla mnemotécnica: **lo que el negocio TIENE o GASTA crece por el débito; lo que el negocio DEBE, lo que es TUYO y lo que GANAS crece por el crédito.**

## Ejemplos de asientos que cuadran (cifras ILUSTRATIVAS / inventadas)

**1) El dueño aporta capital de $5.000.000 en efectivo.**

| Cuenta | Débito | Crédito |
|---|---|---|
| Caja (activo, sube por débito) | 5.000.000 | |
| Capital social (patrimonio, sube por crédito) | | 5.000.000 |
| **Totales** | **5.000.000** | **5.000.000** |

**2) Vendes un servicio por $300.000 y te pagan al banco.**

| Cuenta | Débito | Crédito |
|---|---|---|
| Bancos (activo, sube) | 300.000 | |
| Ingresos por servicios (ingreso, sube) | | 300.000 |
| **Totales** | **300.000** | **300.000** |

**3) Pagas $120.000 de arriendo en efectivo.**

| Cuenta | Débito | Crédito |
|---|---|---|
| Gasto arriendo (gasto, sube) | 120.000 | |
| Caja (activo, baja) | | 120.000 |
| **Totales** | **120.000** | **120.000** |

**4) Pides un préstamo al banco por $2.000.000.**

| Cuenta | Débito | Crédito |
|---|---|---|
| Bancos (activo, sube) | 2.000.000 | |
| Obligación financiera (pasivo, sube) | | 2.000.000 |
| **Totales** | **2.000.000** | **2.000.000** |

> Todas las cifras anteriores son inventadas para enseñar. No son datos reales.

Fíjate que en los cuatro casos los totales coinciden. Eso es el cuadre del módulo 01 en acción.

## Cómo armar un asiento paso a paso

1. ¿Qué cuentas se afectan? (mínimo dos)
2. ¿Cada una sube o baja?
3. Según su naturaleza (tabla de arriba), ¿eso es débito o crédito?
4. ¿La suma de débitos = suma de créditos? Si no, revisa.
5. Cualquier monto calculado (IVA, intereses) se ejecuta en código con `decimal` o se rutea a **Matematicas_lushows**.

## Errores comunes

- **Pensar que débito = "plata que entra".** Falso. Un gasto se registra al débito y ahí sale plata.
- **Afectar una sola cuenta.** Imposible en partida doble; siempre van mínimo dos.
- **Confundir la naturaleza:** subir un ingreso por débito (va por crédito) descuadra todo.
- **Redondear con `float`** y terminar con $0,01 de diferencia que rompe el cuadre.

## Conexión con otros módulos

- El cuadre que aquí se garantiza es el Pilar 1 del módulo **01**.
- El glosario del módulo **06** define cada término (activo, débito, etc.) en simple.
- El marco que dicta *cómo* se valoran estas cuentas (NIIF) está en el **03**.
- Para liquidar montos exactos dentro de un asiento, rutea a **Matematicas_lushows**.

## Siguiente paso típico

Con la partida doble dominada, pasa al módulo **03** para entender bajo qué marco normativo (NIIF) se preparan estos registros en Colombia.

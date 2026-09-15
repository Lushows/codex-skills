# 32 — Depreciación y amortización

Cuando compras un activo que te dura años (un horno, una camioneta, ver módulo 31), no es justo "gastarlo" todo el mes en que lo compraste: te sirve durante varios años, así que su costo debe repartirse en esos años. Ese reparto se llama **depreciación** cuando el activo es físico (maquinaria, vehículos, equipos) y **amortización** cuando es intangible (un software, una licencia, una marca comprada). La idea es la misma: convertir poco a poco el activo en gasto, al ritmo en que el negocio lo va consumiendo.

Depreciar bien hace dos cosas: muestra una utilidad realista (no inflada por no reconocer el desgaste) y deja el valor del activo en libros cercano a la realidad.

## Conceptos clave

| Concepto | Qué es |
|---|---|
| **Costo** | Lo que costó dejar el activo funcionando (módulo 31) |
| **Valor residual** | Lo que esperas recibir al final de su vida útil (puede ser $0) |
| **Vida útil** | Cuántos años (o unidades) esperas usarlo |
| **Base depreciable** | Costo − valor residual (es lo que se reparte) |
| **Depreciación acumulada** | Suma de toda la depreciación cargada hasta hoy |

Bajo NIIF para pymes, la vida útil y el valor residual los estima el negocio según su realidad (no hay tablas "obligatorias"); deben revisarse si cambian las circunstancias.

## Métodos más comunes

| Método | Cómo reparte | Cuándo usarlo |
|---|---|---|
| **Línea recta** | Igual cada año | El más común; activos de desgaste parejo |
| **Saldos decrecientes** | Más al principio, menos al final | Activos que rinden más cuando son nuevos |
| **Unidades de producción** | Según uso real (horas, unidades) | Maquinaria cuyo desgaste depende del uso |

## El cálculo exacto lo hace Matematicas

La fórmula de línea recta es base depreciable ÷ vida útil. Suena simple, pero con valores residuales, fracciones de año, prorrateo del mes de compra y métodos decrecientes se complica y produce centavos. Por eso **NUNCA se calcula de cabeza**: la depreciación se ejecuta y verifica en `Matematicas_lushows` con tipo `decimal`. El contador define los supuestos (costo, vida, método, residual) y registra el resultado; Matematicas pone el número exacto.

## Ejemplo en línea recta (cifras ILUSTRATIVAS / inventadas)

Horno: costo $9.000.000, valor residual $0, vida útil 10 años.
Base depreciable = $9.000.000. Depreciación anual = $9.000.000 / 10 = **$900.000/año** (= $75.000/mes).

Asiento de la depreciación de un mes:

| Cuenta | Débito | Crédito |
|---|---|---|
| Gasto por depreciación | $75.000 | |
| Depreciación acumulada — maquinaria | | $75.000 |

Débitos = créditos = $75.000. La "depreciación acumulada" es una cuenta que **resta** del activo en el balance; no se toca el costo original. Cifras inventadas para ilustrar.

## Errores comunes

- **No depreciar** "porque el equipo sigue sirviendo": la utilidad queda inflada.
- **Confundir depreciación contable con la fiscal**: pueden tener vidas distintas; hay que controlar ambas.
- **Tocar el costo del activo** al depreciar, en vez de usar la cuenta de depreciación acumulada.
- **Olvidar el valor residual** cuando sí existe: se deprecia de más.
- **Calcular de cabeza** los métodos decrecientes o el prorrateo del primer mes.

## Conexión con otros módulos

- El activo que se deprecia se reconoció en el módulo **31**.
- Si el activo cae de valor por algo anormal (no por uso), eso es **deterioro**, ligado al módulo **36**.
- El gasto por depreciación entra al **costo de ventas o al gasto** según donde se use el activo (módulo **38**).
- El cálculo exacto siempre lo ejecuta **Matematicas_lushows**.
- El cuadre y el soporte vienen del método base (módulo **00**).

## Siguiente paso típico

Define método, vida útil y valor residual de cada activo, pide a `Matematicas_lushows` la tabla de depreciación mensual y programa el asiento recurrente de cada cierre.

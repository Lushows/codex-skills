# 119 — Políticas contables, cambios, errores y estimaciones (NIC 8 / Sección 10)

Dentro de NIIF muchas veces hay más de una forma válida de hacer algo: medir una propiedad de inversión a costo o a valor razonable, depreciar en línea recta o por unidades, valuar inventario PEPS o promedio. La **política contable** es la decisión que tomas y mantienes para que tus números sean COMPARABLES en el tiempo. La **NIC 8** (en pymes, la **Sección 10**) regula cómo eliges políticas, qué pasa cuando las cambias, cómo corriges errores de años pasados y cómo manejas las estimaciones. Es el módulo que evita que tu contabilidad cambie de reglas a conveniencia.

Términos: **política contable** = el principio o método elegido para preparar los estados (ej. "valúo inventario por promedio ponderado"). **Estimación contable** = un cálculo aproximado por incertidumbre (ej. la vida útil de una máquina, la provisión de cartera). **Error de periodos anteriores** = una equivocación pasada (omisión, mal cálculo) que se descubre después.

## La gran diferencia: ¿retrospectivo o prospectivo?

| Situación | Cómo se aplica | Toca años anteriores |
|---|---|---|
| **Cambio de política contable** | **Retrospectivo**: como si siempre la hubieras usado; ajustas saldos iniciales y comparativos | Sí |
| **Corrección de error** | **Retrospectivo**: reexpresas los periodos afectados | Sí |
| **Cambio de estimación** | **Prospectivo**: solo afecta de hoy en adelante | No |

Regla mental: **políticas y errores miran hacia atrás; las estimaciones miran hacia adelante.**

## Cuándo puedes cambiar una política

Solo si lo exige una norma nueva, o si el cambio hace la información **más fiable y relevante**. No puedes cambiar "porque sí" o para maquillar resultados.

## Ejemplo de cambio de estimación (cifras ILUSTRATIVAS / inventadas)

GastroLatam compró un equipo en $12.000.000 y lo depreciaba a 10 años ($1.200.000/año). Tras 3 años (acumulada $3.600.000, valor en libros $8.400.000), revisa y concluye que solo durará 2 años más. Esto es un **cambio de estimación**, así que se aplica **hacia adelante**: reparte el valor en libros entre la vida restante.

Nueva depreciación anual = $8.400.000 / 2 = **$4.200.000** (cálculo verificado por `Matematicas_lushows`).

| Cuenta | Débito | Crédito |
|---|---|---|
| Gasto depreciación (5160) | 4.200.000 | |
| Depreciación acumulada (1592) | | 4.200.000 |

NO se tocan los años anteriores: la depreciación pasada se queda como estaba. Cuadra.

## Ejemplo de corrección de error (cifras ILUSTRATIVAS / inventadas)

El año pasado se omitió registrar una factura de gasto de $2.000.000. Se descubre este año. Es un **error**, así que es **retrospectivo**: se ajusta contra resultados acumulados, no contra el gasto del año actual.

| Cuenta | Débito | Crédito |
|---|---|---|
| Resultados acumulados (3705) | 2.000.000 | |
| Proveedores / cuentas por pagar (2335) | | 2.000.000 |

## Errores comunes

- **Confundir cambio de estimación con cambio de política**: la vida útil o la provisión son estimaciones (prospectivo); el método de inventario es política (retrospectivo).
- **Corregir un error de año anterior dentro del resultado del año actual**: debe ir contra patrimonio (resultados acumulados) y reexpresar comparativos.
- **Cambiar políticas para mejorar la utilidad**: solo se cambia si la norma lo exige o mejora la fiabilidad.
- **No documentar las políticas**: deben quedar escritas y aplicarse de forma consistente.

## Conexión con otros módulos

- **116 — Primera adopción**: en la transición defines tu set inicial de políticas.
- **30-39** (depreciación, inventarios): la vida útil y el método de inventario son los ejemplos más frecuentes.
- **20-29** (presentación): los cambios y correcciones se revelan en notas y afectan los comparativos.
- **Matematicas_lushows**: recálculo de depreciación por cambio de estimación, reexpresión de comparativos.

## Siguiente paso típico

Escribe un documento de **políticas contables** del negocio (medición de inventario, depreciación, propiedad de inversión, cartera). Tenerlo por escrito es lo que hace tu contabilidad consistente y auditable. Revísalo cada cierre por si una norma nueva exige un cambio.

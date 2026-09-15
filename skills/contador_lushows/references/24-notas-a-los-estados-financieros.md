# 24 — Notas a los Estados Financieros

Los cuatro estados (módulos 20 a 23) muestran **números**. Las **Notas a los Estados Financieros** muestran el **por qué** detrás de esos números. Son la letra que da contexto: cómo mediste, qué supuestos usaste, qué hay detrás de un saldo grande.

Bajo el marco colombiano (NIIF y NIIF para pymes) las notas **son parte obligatoria** del juego completo de estados financieros. Unos estados sin notas están **incompletos** y un auditor no los aceptaría. Por eso la promesa de la casa incluye *auditable*: las notas son lo que hace que un tercero pueda confiar en tus cifras.

## Para qué sirven las notas

| Función | Qué resuelve |
|---|---|
| **Explicar** | Por qué una cuenta subió o bajó fuerte |
| **Detallar** | Desglosar un saldo agregado (ej. qué compone "otros gastos") |
| **Revelar políticas** | Cómo decidiste medir cada cosa (depreciación, inventarios) |
| **Advertir** | Riesgos, demandas, deudas con garantías, hechos posteriores |
| **Cumplir** | Lo que la norma exige revelar sí o sí |

> **Término clave:** *Política contable* es la regla que tu empresa eligió para registrar y medir algo. Ejemplo: "el inventario se valora por el método del costo promedio". Debe ser consistente año a año.

## Estructura típica de las notas

1. **Nota 1 — Entidad y objeto social:** quién es la empresa, qué hace, dónde opera.
2. **Nota 2 — Bases de preparación:** marco aplicado (NIIF para pymes, Grupo 2, por ejemplo) y moneda.
3. **Nota 3 — Políticas contables significativas:** métodos de inventario, depreciación, reconocimiento de ingresos.
4. **Notas 4 en adelante — Desglose por cuenta:** una nota por las cuentas relevantes (efectivo, cartera, propiedad planta y equipo, obligaciones, patrimonio).
5. **Notas finales — Revelaciones especiales:** contingencias, partes relacionadas, hechos posteriores al cierre.

## Revelaciones mínimas que casi siempre aplican

| Tema | Qué se revela |
|---|---|
| Inventarios | Método de costo (promedio, PEPS) y deterioro |
| Propiedad, planta y equipo | Vida útil, método de depreciación, valor residual |
| Cuentas por cobrar | Política de cartera y deterioro (cuentas dudosas) |
| Obligaciones financieras | Tasas, plazos, garantías |
| Ingresos | Cuándo se reconoce la venta (al entregar, base causación) |
| Impuestos | Tasa aplicada y conciliación contable-fiscal |
| Hechos posteriores | Eventos importantes entre el cierre y la firma de los estados |

## Ejemplo rotulado — cifras ILUSTRATIVAS / inventadas

**Restaurante "La Sazón" — Extracto de notas (COP)**

> **Nota 1 — Entidad.** La Sazón S.A.S. es una sociedad colombiana dedicada al servicio de alimentación, con domicilio en Bogotá. Aplica NIIF para las pymes (Grupo 2).
>
> **Nota 3 — Políticas significativas (extracto).**
> - *Inventarios:* se valoran al costo promedio ponderado.
> - *Propiedad, planta y equipo:* se deprecia en línea recta. Equipo de cocina: vida útil 10 años, sin valor residual.
> - *Ingresos:* se reconocen cuando se presta el servicio al comensal.
>
> **Nota 6 — Propiedad, planta y equipo.**
>
> | Concepto | Valor |
> |---|---:|
> | Equipo de cocina (costo) | 18.000.000 |
> | (−) Depreciación acumulada | (4.000.000) |
> | **Valor en libros** | **14.000.000** |
>
> **Nota 11 — Hechos posteriores.** Entre el cierre (31-dic-2025) y la fecha de aprobación no ocurrieron hechos que modifiquen los estados.

Todo cálculo dentro de las notas (depreciación, costos promedio) se ejecuta y verifica en código vía Matematicas_lushows. Las cifras de arriba son ilustrativas.

## Cómo leerlas en 30 segundos
1. Lee primero la **Nota 3 (políticas):** te dice las "reglas del juego" con que se armaron los números.
2. Ve a la nota de la cuenta más grande del balance: ahí está el detalle que importa.
3. Revisa **hechos posteriores y contingencias:** ahí se esconden los riesgos.

## Errores comunes
- **Entregar estados sin notas:** quedan incompletos y no pasan auditoría.
- **Copiar políticas que no aplicas:** si dices "PEPS" pero usas promedio, mientes en las notas.
- **Cambiar políticas sin avisar:** si cambias de método, debes revelarlo y explicar el efecto.
- **Notas genéricas de plantilla:** las notas deben reflejar TU empresa, no un machote.
- **Omitir partes relacionadas:** préstamos del dueño a la empresa se deben revelar.

## Conexión con otros módulos
- **Módulos 20, 21, 22, 23:** las notas explican y desglosan cada uno de esos estados.
- **Módulo 25 (Presentación bajo NIIF):** las notas son uno de los componentes obligatorios del juego completo.
- **Módulo 28 (Consolidación):** la base de consolidación y las eliminaciones se revelan en notas.
- **economist_lushows:** las políticas que se revelan (vida útil, métodos) nacen de decisiones que economist puede orientar.

## Siguiente paso típico
Ve al **módulo 25 (Presentación bajo NIIF)** para entender cómo encajan los cuatro estados + las notas en el juego completo que exige la norma colombiana.

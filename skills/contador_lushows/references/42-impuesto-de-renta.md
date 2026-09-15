# 42 — Impuesto de renta

El **impuesto de renta** grava la **utilidad** (la "renta") que una persona o empresa obtuvo en el año. A diferencia del IVA (que recae sobre el consumo y se declara cada pocos meses), la renta es **anual** y recae sobre lo que ganaste después de restar costos, gastos y beneficios permitidos. Es, junto con el IVA, el impuesto nacional más importante que administra la DIAN.

Este módulo explica el **concepto y la mecánica de depuración**. **No inventamos tarifas ni rangos:** las tarifas de personas jurídicas y la tabla por rangos de personas naturales (en UVT) cambian con las reformas. *Verifica las tarifas y los rangos vigentes del año en la DIAN.*

## Términos clave
- **Renta bruta:** ingresos menos costos directamente asociados.
- **Renta líquida:** renta bruta menos gastos/deducciones permitidos. Es la base sobre la que (en general) se calcula el impuesto.
- **Renta líquida gravable:** la base final tras restar rentas exentas y aplicar límites.
- **Renta presuntiva:** una renta mínima que la ley presume sobre el patrimonio (su tarifa ha variado e incluso ha estado en cero; *verifica el estado vigente*).
- **Anticipo:** un pago "adelantado" del impuesto del año siguiente que la declaración liquida.
- **Descuentos tributarios:** restan directamente del impuesto (no de la base), p. ej. ciertos beneficios.

## La depuración (cómo se "arma" la base)
```
Ingresos del año
(−) Ingresos no constitutivos de renta
(−) Costos
(−) Deducciones (gastos procedentes)
= Renta líquida
(−) Rentas exentas / compensaciones (con límites)
= Renta líquida gravable  → se le aplica la TARIFA
(−) Descuentos tributarios
(+) Anticipo del año siguiente
= Saldo a pagar o a favor
```
> Cada resta tiene reglas y límites. La liquidación final va a **Matematicas_lushows**.

## Personas jurídicas vs. naturales (CONCEPTO)
| Aspecto | Persona jurídica (empresa) | Persona natural |
|---|---|---|
| Tarifa | Generalmente una tarifa única (verifica la vigente) | Tabla por **rangos en UVT** (progresiva) |
| Quién declara | Casi siempre obligada | Según topes de ingresos/patrimonio/consumos en UVT |
| Cédulas | No aplica | Sí: el sistema **cedular** agrupa rentas (trabajo, capital, etc.) |

*Los topes que obligan a una persona natural a declarar se miden en UVT y cambian: verifícalos en la DIAN.*

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
Empresa "Tornillos del Norte SAS", con tarifa **ilustrativa del 35%**:
- Ingresos: $500.000.000
- Costos y deducciones: $420.000.000
- Renta líquida gravable: $80.000.000
- Impuesto (35% ilustrativo): **$28.000.000** (inventado)

> Cifras y tarifa de ejemplo. El cálculo real, con la tarifa vigente, va a **Matematicas_lushows** con `decimal`.

## Régimen Simple de Tributación (mención)
Existe el **SIMPLE**, un régimen opcional que **unifica varios impuestos** (renta, parte de ICA, etc.) en un solo pago según ingresos. Puede convenir o no según el caso; **la decisión de acogerse es planeación** → eso lo evalúa `economist_lushows` y la planeación avanzada en el módulo **101**. Aquí lo registramos y liquidamos.

## Errores comunes
- Tratar como deducible un gasto **sin soporte** o no relacionado con la actividad.
- Olvidar el **anticipo** del año siguiente al estimar el saldo a pagar.
- Confundir **renta contable** (utilidad de los estados financieros) con **renta fiscal** (la base del impuesto): difieren (ver 48).
- Asumir que "como dio pérdida no declaro": la obligación de declarar **no depende** de haber tenido utilidad.

## Conexión con otros módulos
- **40** — ubicación en el mapa tributario.
- **43 (Retención)** — las retenciones que te practicaron son un **anticipo** que descuentas en renta.
- **48 (Impuesto diferido)** — por qué difieren la base contable y la fiscal.
- **47 / 46** — presentación y calendario (la renta es anual, por último dígito del NIT).
- **economist_lushows** / módulo **101** — elegir régimen (SIMPLE vs. ordinario) es planeación.
- **Matematicas_lushows** — toda la liquidación.

## Siguiente paso típico
Reunir ingresos, costos y deducciones del año, depurar la base y verificar la tarifa/topes vigentes. Si es persona natural, clasificar las rentas por cédula. Luego ir a **47**.

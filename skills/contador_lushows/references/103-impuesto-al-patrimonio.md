# 103 — Impuesto al patrimonio

La mayoría de impuestos te cobran sobre lo que **ganas** (renta) o sobre lo que **vendes** (IVA). El **impuesto al patrimonio** es distinto: te cobra sobre lo que **tienes acumulado** —tu riqueza neta— en una fecha de corte. Es un impuesto que **va y viene** en la historia tributaria colombiana: a veces existe, a veces no, y cuando existe suele aplicar solo a patrimonios **grandes**, por encima de un umbral alto.

Este módulo da el **concepto**. Como su existencia, umbrales y tarifas **cambian según la reforma vigente**, aquí no afirmamos cifras: *verifica siempre en la DIAN si está vigente este año, desde qué monto y con qué tarifa.*

## Conceptos clave (despacio)
- **Patrimonio bruto:** todo lo que posees (efectivo, inmuebles, vehículos, inversiones, cuentas por cobrar).
- **Patrimonio líquido (base):** patrimonio bruto **menos** las deudas. Es la riqueza neta.
- **Fecha de corte:** el día en que se "fotografía" tu patrimonio (típicamente 1 de enero del año).
- **Umbral:** monto a partir del cual nace la obligación (suele ser **alto** — no afecta a pequeños).
- **Sujeto pasivo:** quién debe pagarlo (personas naturales y/o jurídicas, según la norma de turno).

## ¿A quién aplica? (concepto)
Cuando el impuesto está vigente, normalmente recae sobre quienes tengan un **patrimonio líquido superior a un umbral elevado** en la fecha de corte. La idea es gravar a los **más ricos**, no al negocio pequeño promedio. La definición de quién es sujeto (personas naturales, sucesiones, ciertas sociedades, no residentes con patrimonio en Colombia) depende de la ley vigente. *Verifica.*

## Cómo se arma la base (concepto)
```
Patrimonio bruto (todo lo que tienes)
  − Deudas
  = Patrimonio líquido
  − Exclusiones que permita la ley (p. ej. parte del valor de la casa de habitación)
  = Base gravable del impuesto al patrimonio
```
Sobre esa base se aplica la **tarifa vigente** (suele ser baja y a veces progresiva por tramos).

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
Una persona con patrimonio:
- Patrimonio bruto: **$4.000.000.000** (inventado).
- Deudas: **$500.000.000** (inventado).
- Patrimonio líquido: **$3.500.000.000**.
- Si el umbral ilustrativo fuera $3.000 millones y la tarifa ilustrativa 0,5%: impuesto ≈ 3.500.000.000 × 0,5% = **$17.500.000** (inventado).

> Umbral, tarifa y existencia del impuesto son ilustrativos. El cálculo real va a `Matematicas_lushows` con valores vigentes.

## Errores comunes
- Asumir que un negocio pequeño paga patrimonio: casi nunca, por el umbral alto.
- Olvidar **restar las deudas**: se grava el patrimonio **líquido**, no el bruto.
- No verificar si el impuesto **está vigente** ese año (entra y sale con las reformas).
- Subvalorar activos para no llegar al umbral: eso es **evasión**, no planeación.
- Confundirlo con el impuesto de renta (uno grava la riqueza, el otro la ganancia).

## Conexión con otros módulos
- **42 (Renta)** — el patrimonio declarado en renta es la base de partida.
- **100** — la planeación legítima de patrimonio (ordenar activos/deudas) es legal; ocultarlos no.
- **104** — ganancia ocasional (al vender activos que componen el patrimonio).
- **economist_lushows** — decisiones sobre cómo estructurar el patrimonio.
- **Matematicas_lushows** — liquidación de la base y el impuesto.

## Siguiente paso típico
Verificar en la DIAN si el impuesto está vigente este año y cuál es el umbral; si el patrimonio se acerca o supera ese umbral, depurar bien activos y deudas, calcular en `Matematicas_lushows` y confirmar con el contador titulado. Para la mayoría de pymes pequeñas, simplemente no aplica.

# 54 — Estado de resultados (P&L)

El estado de resultados (o P&L, *Profit & Loss*) es la "foto de la película": cuánto vendiste en un período, qué te costó, y cuánto te quedó de verdad. Es el documento que separa "facturé harto" de "gané plata". Este módulo te enseña a armarlo línea por línea y a leer las tres utilidades que importan.

## Qué es y para qué sirve

El P&L cuenta una historia en un período (mes, trimestre, año): arriba entra todo lo que vendiste, y a medida que bajas vas restando costos hasta llegar a lo que realmente ganaste. Tres reglas mentales:

- Es por **período**, no acumulado de toda la vida (eso es otra cosa). Define el período arriba: "P&L — Marzo 2026".
- Va por lo **causado/devengado**, no por lo que entró a la caja. Si vendiste a crédito en marzo, la venta es de marzo aunque te paguen en abril. (El movimiento de caja se ve en el flujo de caja, ver 55 — son distintos y por eso un negocio puede ser "rentable" en el P&L y aun así quedarse sin efectivo.)
- Se lee de **arriba hacia abajo**: cada línea le resta algo a la anterior.

## La estructura línea por línea

| Línea | Qué es | En una frase |
|---|---|---|
| **Ingresos (ventas netas)** | Todo lo que vendiste, menos devoluciones y descuentos | "Lo que entró por vender" |
| **(−) Costo de ventas (COGS)** | El costo directo de lo que vendiste | "Lo que me costó producir/comprar lo vendido" |
| **= Margen bruto** | Ingresos − COGS | "Lo que queda para pagar todo lo demás" |
| **(−) Gastos operativos (OPEX)** | Arriendo, sueldos, marketing, software, servicios | "Lo que cuesta mantener el negocio prendido" |
| **= Utilidad operativa (EBIT)** | Margen bruto − OPEX | "Si el negocio en sí gana o no" |
| **(−) Intereses e impuestos** | Costo de deudas + impuesto de renta | "Lo que se llevan el banco y el Estado" |
| **= Utilidad neta** | Lo que de verdad te quedó | "La línea final, *the bottom line*" |

**COGS vs OPEX (el error #1):** COGS es lo que sube y baja con cada venta (la materia prima, el producto que revendes, la hora del que fabrica). OPEX existe vendas o no vendas (el arriendo del local llega igual). Truco: *"¿este costo desaparece si no vendo nada este mes?"* → Sí = COGS; No = OPEX.

## Las tres utilidades (no las confundas)

- **Margen bruto** → mide tu **producto/operación**. Margen bruto bajo = tu precio y tu costo de producir no cuadran. Se arregla subiendo precio (ver 57) o bajando COGS, no recortando publicidad.
- **Utilidad operativa (EBIT)** → mide tu **negocio completo** funcionando, sin contar deudas ni impuestos. Es la mejor foto de si el modelo sirve. Comparable entre empresas.
- **Utilidad neta** → mide lo que **te toca a ti** al final. Incluye intereses (cómo financiaste) e impuestos (dónde operas).

Por qué importa separarlas: un negocio con buen margen bruto pero pésima utilidad neta tiene un problema de **gastos o deuda**, no de producto. Uno con mal margen bruto tiene un problema de **modelo**. El diagnóstico cambia según qué utilidad esté herida.

## Ejemplo numérico (cifras ILUSTRATIVAS, inventadas)

> Ejemplo: cafetería de barrio, mes de marzo. **Las cifras son inventadas solo para enseñar el cálculo** — no son datos reales de ningún mercado.

| Línea | Monto (ejemplo) | % sobre ventas |
|---|---:|---:|
| Ingresos (ventas netas) | 20.000.000 | 100% |
| (−) Costo de ventas (café, leche, insumos, panadería) | 7.000.000 | 35% |
| **= Margen bruto** | **13.000.000** | **65%** |
| (−) Arriendo | 3.000.000 | 15% |
| (−) Sueldos (2 baristas) | 4.000.000 | 20% |
| (−) Servicios + internet + software | 1.000.000 | 5% |
| (−) Marketing | 800.000 | 4% |
| **= Utilidad operativa (EBIT)** | **4.200.000** | **21%** |
| (−) Intereses del crédito del local | 500.000 | 2,5% |
| (−) Impuestos (tasa ILUSTRATIVA del 30%*) | 1.110.000 | 5,5% |
| **= Utilidad neta** | **2.590.000** | **13%** |

\* **El 30% es solo un número de ejemplo.** Las tasas reales de impuesto de renta cambian por país, por régimen (¿pequeña empresa? ¿régimen simplificado?) y por año. **Antes de calcular tu impuesto real, pregunta país/ciudad y régimen, y verifica la tasa vigente** (ver 21 para cómo conseguir el dato oficial). Nunca asumas una tasa.

**Cómo leer este ejemplo en voz alta:** "De cada $100 que vendo, $35 se van en insumos, me quedan $65; de esos, $44 se van en operar el local; gano $21 antes de banco e impuestos; y al final me quedan $13 limpios." Esos porcentajes (la columna de la derecha) son tu **herramienta de diagnóstico**: si el mes siguiente la utilidad neta cae a 8%, miras qué porcentaje creció y ahí está el culpable.

## Cómo armar el tuyo (checklist)

- [ ] Define el período y escríbelo en el título.
- [ ] Suma **ingresos netos** (ventas − devoluciones − descuentos).
- [ ] Lista tus costos y clasifica cada uno: ¿COGS o OPEX? (usa el truco de "¿desaparece si no vendo?").
- [ ] Calcula margen bruto y sácale el **%** sobre ventas.
- [ ] Resta OPEX → utilidad operativa.
- [ ] Resta intereses e impuestos (verifica la tasa real de tu país) → utilidad neta.
- [ ] Saca el **%** de cada línea sobre ventas. Sin porcentajes, los números sueltos no dicen nada.
- [ ] Compáralo con el mes anterior. El P&L de un solo mes informa; tres meses seguidos *revelan*.

Hazlo en una hoja de cálculo simple. No necesitas software contable para empezar; necesitas el hábito mensual.

## Errores comunes

- **Confundir facturar con ganar.** $20M de ventas no son $20M tuyos. La línea que importa está abajo.
- **Meter el COGS dentro de OPEX (o al revés).** Te daña el margen bruto y te impide saber si el problema es el producto o los gastos.
- **Olvidar tu propio sueldo.** Si trabajas en el negocio y no te pagas, tu utilidad está inflada y mientes. Pon tu sueldo de mercado como OPEX (ver 58).
- **Mezclar plata personal con la del negocio.** Tu café de la mañana no es gasto de la empresa. Sepáralo desde el día uno.
- **Confundir el P&L con la caja.** Puedes tener utilidad neta positiva y aun así no tener efectivo (porque te deben, o pagaste inventario por adelantado). Para eso existe el flujo de caja (ver 55).
- **No usar porcentajes.** Sin la columna de %, no puedes comparar meses ni detectar qué línea se descontroló.
- **Inventar la tasa de impuestos.** Verifica la real de tu país/régimen siempre (ver 21).

## Conexión con otros módulos

- **Precio (ver 57):** tu margen bruto nace de la diferencia entre precio y COGS. Si el margen bruto del P&L es flojo, el problema empieza en el pricing.
- **Costos fijos vs variables y punto de equilibrio (ver 53):** los OPEX de este P&L son, en su mayoría, tus costos fijos. Con ellos calculas cuántas ventas necesitas para no perder.
- **Flujo de caja (ver 55):** el P&L dice si *ganas*; el flujo de caja dice si *sobrevives* mes a mes. Necesitas ambos. Muchos negocios rentables quiebran por caja, no por utilidad.

## Siguiente paso típico

Arma tu P&L del último mes cerrado en una hoja de cálculo, con la columna de % sobre ventas. Mira cuál de las tres utilidades está más débil y atácala donde corresponde: margen bruto → pricing/COGS (ver 57); operativa → gastos (ver 58); neta → deuda e impuestos. Luego cruza con tu flujo de caja (ver 55) para confirmar que la utilidad también se convierte en efectivo.

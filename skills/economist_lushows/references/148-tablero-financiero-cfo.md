# 148 — Tablero financiero (modo CFO)

El tablero de números que TODO dueño debe mirar cada semana y cada mes para no manejar a ciegas. Si solo vas a tener un reporte, que sea este. La idea: que en 5 minutos sepas si el negocio está sano o si hay que reaccionar YA.

## Para qué sirve
Un CFO (director financiero) no adivina: mira un puñado de indicadores y decide. Tú puedes hacer lo mismo sin contador caro ni software costoso, con una hoja de cálculo. Este módulo te da QUÉ mirar, CADA CUÁNTO, y CUÁNDO encender la alarma.

## Las 6 cifras que mandan (el núcleo)
No necesitas 50 métricas. Necesitas estas 6, bien hechas:

1. **Caja hoy** — cuánta plata REAL tienes disponible (banco + efectivo). Es lo único que paga la nómina. Una empresa puede ser "rentable" en papel y quebrar por quedarse sin caja (ver 55).
2. **Runway (meses de oxígeno)** — cuántos meses sobrevives si las ventas no mejoran. Fórmula: `Caja ÷ quema mensual neta`. Si gastas más de lo que entra, esto es lo más importante de tu vida.
3. **Ingresos del periodo** — ventas reales cobradas o facturadas (define cuál usas y sé consistente).
4. **Margen** — qué te queda después de costos. Mira dos: **margen bruto** (ventas − costo directo) y **margen operativo** (después de gastos fijos). Ver 141 y 144.
5. **Gastos clave** — tus 5-7 rubros más grandes (nómina, arriendo, insumos, publicidad, plataformas). El 80% del gasto suele estar en pocos rubros.
6. **CxC y CxP** — Cuentas por Cobrar (lo que te deben) y por Pagar (lo que debes). Aquí se esconde la plata que "no aparece".

## El tablero, en una tabla (ejemplo ilustrativo)
> Cifras de ejemplo en pesos colombianos (COP) para ilustrar el formato — NO son tus números. Pregunta país/moneda y arma con tus datos reales.

| Indicador | Mes pasado | Este mes | Meta | Semáforo |
|---|---|---|---|---|
| Caja disponible | $18.000.000 | $14.500.000 | > $20M | 🔴 |
| Runway (meses) | 4,2 | 3,2 | > 6 | 🔴 |
| Ingresos cobrados | $32.000.000 | $35.000.000 | $38M | 🟡 |
| Margen bruto % | 52% | 49% | > 55% | 🟡 |
| Margen operativo % | 8% | 4% | > 12% | 🔴 |
| Gasto nómina | $12.000.000 | $13.500.000 | < $12M | 🔴 |
| Gasto publicidad | $4.000.000 | $5.500.000 | — | 🟡 |
| Cuentas por cobrar | $9.000.000 | $14.000.000 | < $8M | 🔴 |
| Cuentas por pagar | $7.000.000 | $7.500.000 | — | 🟢 |

**Lectura honesta de este ejemplo:** vende más ($35M) pero la caja CAE y el runway baja a 3,2 meses. ¿Por qué? Las cuentas por cobrar subieron $5M (estás vendiendo a crédito y no cobrando) y el margen bajó. Estás creciendo hacia la quiebra. Acción inmediata: cobrar cartera y revisar costos, no celebrar las ventas.

## Cómo calcular cada cosa (sin enredos)
- **Quema neta mensual** = gastos del mes − ingresos del mes (si da positivo, estás quemando caja).
- **Runway** = caja actual ÷ quema neta. *Ejemplo:* caja $14,5M ÷ quema $4,5M = **3,2 meses**.
- **Margen bruto %** = (ventas − costos directos) ÷ ventas × 100.
- **Días de cobro (DSO)** = (CxC ÷ ventas del periodo) × días del periodo. *Ejemplo:* (14M ÷ 35M) × 30 = **12 días** te tardas en cobrar. Compáralo con tu plazo pactado.
- **Punto de equilibrio** del mes: ver 53 (cuánto debes vender para no perder).

## Ritmo: qué miras semanal vs mensual
| Frecuencia | Qué revisar | Por qué |
|---|---|---|
| **Semanal (10 min)** | Caja, cobros que entran, pagos que salen esta semana, ventas de la semana | Evita sustos de liquidez; reaccionas a tiempo |
| **Mensual (45 min)** | Todo el tablero + márgenes + comparar vs mes anterior y vs meta | Ves tendencia y decides ajustes |
| **Trimestral** | Revisar metas, estructura de costos, proyección 6-12 meses (ver 56) | Decisiones grandes (contratar, invertir, subir precios) |

## Cómo armarlo en 1 hora (mínimo viable)
1. Abre una hoja de cálculo (Google Sheets gratis). Una pestaña por mes.
2. Pega las 6 cifras núcleo. Saca caja del banco, ventas de tus facturas/registros.
3. Pon una columna "Meta" y otra "Semáforo" (verde/amarillo/rojo con regla simple).
4. Conéctalo a tu flujo de caja proyectado (ver 55 y 56) para ver el runway a futuro.
5. Agenda 10 minutos fijos cada lunes. La disciplina vale más que la herramienta.

> Empieza simple. Un tablero feo que MIRAS cada semana vale 100 veces más que un dashboard hermoso que abres una vez al año.

## Reglas de alarma (semáforo) — orientativas, ajústalas
- **Runway < 6 meses** → 🟡 vigilar; **< 3 meses** → 🔴 plan de emergencia (cortar gasto, cobrar, vender más rápido).
- **Margen bruto cayendo 2+ meses seguidos** → revisa precios/costos (ver 57, 58).
- **CxC creciendo más rápido que ventas** → estás financiando a tus clientes; aprieta cobranza.
- **Nómina > 30-40% de ingresos** (rango orientativo, varía MUCHO por sector) → revisa productividad.
- **Caja baja 3 meses seguidos pese a vender** → algo se fuga (cartera, inventario, márgenes).

## Errores comunes
- **Confundir ventas con caja.** Vendiste no es cobraste. La caja es la verdad (ver 55).
- **Confundir utilidad con plata en el banco.** Puedes tener "ganancia" e impuestos/cartera/inventario amarrando toda la liquidez.
- **No separar tus finanzas personales del negocio.** Sin esto, el tablero miente. Sácate un sueldo fijo y déjalo en los gastos.
- **Mirar solo ingresos.** El dueño que solo ve "cuánto vendí" no ve que el margen se desploma.
- **Ignorar las CxP a destiempo.** Pagar tarde a proveedores clave te corta crédito o insumos.
- **No comparar vs meta ni vs mes anterior.** Un número solo no dice nada; la TENDENCIA sí.
- **Hacerlo "cuando haya tiempo".** El tablero sin ritmo fijo no existe.

## Nota de país
Reglas de impuestos, retenciones, plazos de pago legales y costos laborales (que afectan tu nómina y tus CxP) **cambian por país y a veces por ciudad/régimen**. Antes de fijar metas o interpretar la línea de impuestos, dime tu país y ciudad, y verifica las reglas vigentes (cómo conseguir datos reales: ver 21).

## Siguiente paso típico
Arma hoy la versión mínima (6 cifras + caja del banco) en una hoja y agenda 10 minutos cada lunes. Si tu runway está por debajo de 6 meses, salta de inmediato a flujo de caja (55) y proyección (56) para armar el plan de los próximos meses.

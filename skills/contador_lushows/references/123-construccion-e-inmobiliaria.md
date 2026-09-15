# 123 — Construcción e inmobiliaria

Construir un edificio toma meses o años, y ahí está el reto contable: ¿cuándo reconoces el ingreso de una obra que aún no terminas? Si esperas hasta entregarla, los estados financieros de los años intermedios quedan vacíos aunque trabajaste muchísimo. La contabilidad de construcción resuelve esto reconociendo ingresos **según el avance de la obra**, y maneja con cuidado los **anticipos** que los clientes pagan antes de empezar. Es un sector intensivo en control de costos por proyecto.

Dos ideas base: **avance de obra** (cuánto del proyecto ya ejecutaste, medido en costos incurridos o hitos) y **anticipo** (plata que el cliente entrega por adelantado, que es un pasivo hasta que la ganas).

## Cuentas típicas del sector

| Cuenta | Para qué sirve | Tipo |
|---|---|---|
| Obras en curso / inventario de proyecto | Costos acumulados de la obra | Activo |
| Anticipos recibidos de clientes | Plata adelantada por el cliente | Pasivo |
| Ingreso por contratos de construcción | Ingreso reconocido por avance | Ingreso |
| Costo de obra | Materiales, mano de obra, subcontratos | Costo |
| Retención en garantía por cobrar | % que el cliente retiene hasta entrega | Activo |

## Reconocimiento por avance de obra

Bajo **NIIF 15**, cuando el control se transfiere "a lo largo del tiempo", el ingreso se reconoce por el **grado de avance**. El método más usado es el de **costos incurridos**: avance = costos ya gastados ÷ costos totales estimados. Ese porcentaje aplicado al precio del contrato da el ingreso del período. El cálculo del % se ejecuta con `Matematicas_lushows`.

| Concepto | Cómo se mide |
|---|---|
| Avance | Costos incurridos ÷ costos totales estimados |
| Ingreso del período | Avance × precio del contrato − ingreso ya reconocido |
| Costo del período | Costos realmente incurridos |

## Anticipos, predial e impuestos

- El **anticipo** es un **pasivo** hasta que se gana con el avance; nunca es ingreso al recibirlo.
- La **retención en garantía** (parte del pago que el cliente guarda hasta verificar la obra) es una cuenta por cobrar tuya.
- El **impuesto predial** sobre lotes y proyectos es un gasto/costo según el caso; los inmuebles propios para venta son inventario, no propiedad de inversión.
- En obra hay **AIU** (Administración, Imprevistos, Utilidad): la base de IVA y retención en ciertos contratos se calcula sobre la parte gravada del AIU. Verifica la regla vigente.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Contrato por $1.000.000.000. Costos totales estimados $700.000.000. Al cierre se han incurrido $210.000.000. Avance = 210 ÷ 700 = **30%**. Ingreso a reconocer = 30% × 1.000.000.000 = **$300.000.000**.

| Cuenta | Débito | Crédito |
|---|---|---|
| Cuenta por cobrar / Anticipos | $300.000.000 | |
| Ingreso por contratos de construcción | | $300.000.000 |

Débitos = créditos. Cifras inventadas; el % de avance y toda suma se verifican con `Matematicas_lushows`.

## Errores comunes

- **Reconocer todo el ingreso al entregar**: deja años de trabajo sin reflejar.
- **Tratar el anticipo como ingreso** al recibirlo.
- **No reestimar los costos totales**: si suben, el avance cambia y el ingreso ya reconocido puede estar mal.
- **Olvidar la retención en garantía** como cuenta por cobrar.
- **Calcular el avance "a ojo"** en lugar de con costos reales.

## Conexión con otros módulos

- Los **anticipos e ingresos diferidos** en el módulo **37**.
- El **costeo por proyecto** se apoya en el **38**.
- El **reconocimiento NIIF** en el bloque **03/25**.
- **IVA, AIU y retención** en **41** y **43**.
- *Viabilidad del proyecto, flujo y rentabilidad*: `economist_lushows`.
- Todo cálculo de avance y reestimación: `Matematicas_lushows`.

## Siguiente paso típico

Define para cada obra sus costos totales estimados, registra los costos por proyecto y calcula el avance cada cierre para reconocer el ingreso. Controla anticipos y retenciones en garantía por separado.

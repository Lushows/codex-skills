# 110 — NIIF 15: Reconocimiento de ingresos de actividades ordinarias

¿Cuándo registro una venta como ingreso? La intuición dice "cuando me pagan", pero la norma dice otra cosa: el ingreso se reconoce **cuando transfiero el control del bien o servicio al cliente**, no necesariamente cuando recibo el dinero. NIIF 15 (en NIIF para pymes equivale a la **Sección 23 — Ingresos de actividades ordinarias**, con redacción más simple) unifica todo bajo un **modelo de 5 pasos**. Este módulo te lo explica para que tus ingresos queden bien medidos y bien fechados, que es donde más se equivoca la gente.

Términos clave: **contrato** = acuerdo con derechos y obligaciones exigibles. **Obligación de desempeño** = cada promesa distinta dentro del contrato (entregar un producto, dar soporte, instalar). **Control** = la capacidad de dirigir el uso del activo y obtener sus beneficios.

## El modelo de 5 pasos

| Paso | Pregunta | Qué decides |
|---|---|---|
| 1. Identificar el contrato | ¿Hay acuerdo con sustancia comercial y cobro probable? | Si sí, sigue. Si el cobro NO es probable, no hay contrato bajo NIIF 15 |
| 2. Identificar obligaciones de desempeño | ¿Qué promesas distintas hay? | Separas bienes/servicios "distintos" |
| 3. Determinar el precio de la transacción | ¿Cuánto espero recibir en total? | Incluye contraprestación variable (descuentos, devoluciones) |
| 4. Asignar el precio a cada obligación | ¿Cuánto vale cada promesa por separado? | Repartes según precio de venta independiente |
| 5. Reconocer el ingreso | ¿Cuándo cumplí cada promesa? | Al transferir el control: en un momento o a lo largo del tiempo |

## ¿En un momento o a lo largo del tiempo?

- **A lo largo del tiempo**: servicios continuos (arriendo de software, consultoría por meses, construcción). Reconoces según el avance (% de obra, meses transcurridos).
- **En un momento dado**: la mayoría de ventas de productos. Reconoces cuando el cliente recibe y controla el bien.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

GastroLatam vende un paquete: la **Calculadora de Costos (Excel)** + **3 meses de soporte por WhatsApp**, todo por $30.000 COP recibidos por adelantado.

- Paso 2: hay **dos** obligaciones distintas — el Excel (se entrega ya) y el soporte (se presta en 3 meses).
- Paso 4: si vendidos por separado valdrían Excel $10.000 y soporte $30.000 (total $40.000), asigno el precio real proporcionalmente:
  - Excel: $30.000 × (10.000 / 40.000) = $7.500
  - Soporte: $30.000 × (30.000 / 40.000) = $22.500
  - (Esa proporción la calcula y verifica `Matematicas_lushows`, nunca de cabeza.)

**Al recibir el dinero** (aún no hay ingreso del soporte):

| Cuenta | Débito | Crédito |
|---|---|---|
| Caja/Bancos (11) | 30.000 | |
| Ingreso por venta del Excel (4135) | | 7.500 |
| Ingresos recibidos por anticipado / pasivo del contrato (2805) | | 22.500 |

**Cada mes de soporte** (3 cuotas de $22.500 / 3 = $7.500):

| Cuenta | Débito | Crédito |
|---|---|---|
| Ingresos recibidos por anticipado (2805) | 7.500 | |
| Ingreso por servicio de soporte (4140) | | 7.500 |

Al final de los 3 meses, el pasivo del contrato queda en cero y se reconocieron los $30.000 completos como ingreso, pero **en el momento correcto**.

## Errores comunes

- **Reconocer todo el ingreso al cobrar** cuando aún debes prestar servicio: infla las ventas del mes y deja una obligación oculta.
- **No separar obligaciones**: facturar un combo como una sola línea cuando hay un servicio pendiente.
- **Confundir ingreso con efectivo**: una venta a crédito es ingreso aunque no haya entrado plata (se registra contra cuentas por cobrar 13).
- **Ignorar devoluciones y descuentos esperados**: el precio de la transacción debe restar lo que probablemente devolverás.
- **Incluir el IVA dentro del ingreso**: el IVA es un pasivo con la DIAN (2408), no es venta tuya.

## Conexión con otros módulos

- **20-29** (presentación de estados financieros): el ingreso reconocido alimenta el estado de resultados.
- **Matematicas_lushows**: toda asignación proporcional, valor presente de contratos largos o cálculo de % de avance.
- **economist_lushows**: define el modelo de precios y combos; tú solo REGISTRAS lo que decidió.
- **Factura electrónica DIAN** (ver módulos de cumplimiento): la fecha de la factura no siempre coincide con la fecha del ingreso contable.

## Siguiente paso típico

Revisa si tienes contratos con servicios diferidos (suscripciones, soportes, anticipos de clientes) y crea la cuenta de **pasivo del contrato (ingresos recibidos por anticipado)** para no inflar ventas. Luego pasa a **111 — NIIF 16 (Arrendamientos)** si tu negocio arrienda local o equipos.

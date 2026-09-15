# 10 — Plan de cuentas (PUC): el mapa de tu negocio

Antes de registrar un solo peso, necesitas un **mapa de casillas** donde guardar cada hecho económico. Ese mapa es el **plan de cuentas**. En Colombia el más conocido es el **PUC** (Plan Único de Cuentas), creado por el **Decreto 2650 de 1993**. Hoy, con NIIF, las empresas pueden usar un **catálogo de cuentas adaptado a NIIF**, pero la lógica de clasificación es la misma y el PUC sigue siendo la referencia que todo el mundo entiende.

> **Cuenta** = una casilla con nombre y código numérico donde anotas un tipo de movimiento (ejemplo: "Caja", "Bancos", "Ventas").

## Para qué sirve un plan de cuentas

- Que cada peso tenga **un solo lugar lógico** donde registrarse.
- Que dos personas registren el mismo hecho **igual**.
- Que al final puedas sumar casillas y armar tus **estados financieros**.
- Que la DIAN y tu contador hablen **el mismo idioma**.

## Estructura por clases (el primer dígito manda)

El PUC es jerárquico: el **primer dígito** dice de qué tipo es la cuenta.

| Clase | Nombre | Qué guarda |
|---|---|---|
| 1 | Activo | Lo que el negocio TIENE (caja, bancos, inventario, equipos) |
| 2 | Pasivo | Lo que el negocio DEBE (proveedores, préstamos, impuestos por pagar) |
| 3 | Patrimonio | Lo que es de los dueños (capital, utilidades retenidas) |
| 4 | Ingresos | Lo que el negocio GANA (ventas, servicios) |
| 5 | Gastos | Lo que cuesta OPERAR (sueldos, arriendo, servicios públicos) |
| 6 | Costos de venta | El costo de lo que vendiste (mercancía, materia prima) |
| 7 | Costos de producción | Costos de fabricar (en industria) |
| 8 | Cuentas de orden deudoras | Control, no afectan resultado |
| 9 | Cuentas de orden acreedoras | Control, no afectan resultado |

## Cómo se desglosa un código

Cada dígito que agregas hace la casilla **más específica**:

| Nivel | Dígitos | Ejemplo | Nombre |
|---|---|---|---|
| Clase | 1 | `1` | Activo |
| Grupo | 2 | `11` | Disponible |
| Cuenta | 4 | `1105` | Caja |
| Subcuenta | 6 | `110505` | Caja general |
| Auxiliar | 7+ | `11050501` | Caja sede norte |

Así, `110505` te dice de un vistazo: Activo (1) → Disponible (11) → Caja (1105) → Caja general (110505).

## Cómo elegir cuentas (sin enredarte)

1. **Pregunta qué naturaleza tiene el hecho**: ¿es algo que tengo, que debo, de los dueños, que gano o que gasto?
2. **Baja un nivel a la vez** hasta encontrar la casilla más cercana.
3. **No inventes códigos**: usa el catálogo. Si necesitas un detalle propio (ej. "Caja sede norte"), créalo como **auxiliar** colgando de una subcuenta oficial.
4. **Menos es más**: un negocio pequeño puede operar con 30–40 cuentas bien elegidas.

## Ejemplo numérico (cifras ILUSTRATIVAS / inventadas)

Compras un horno por $2.000.000 y lo pagas de la cuenta bancaria. Las casillas que usarías:

| Hecho | Cuenta PUC (ilustrativa) | Clase |
|---|---|---|
| Entra un horno (lo tengo) | `152405` Maquinaria y equipo | 1 Activo |
| Sale plata del banco | `111005` Banco cuenta corriente | 1 Activo |

> Aún no es el asiento (eso es el módulo 12), aquí solo **elegimos las casillas**. El registro con débito y crédito lo verás luego, y SIEMPRE cuadrará.

## Errores comunes

- **Usar una cuenta de gasto (5) para algo que es activo (1).** Comprar una máquina NO es un gasto del mes; es un activo que se deprecia (ver módulo 16).
- **Crear cuentas duplicadas** ("Banco", "Bancos", "Cta banco") en vez de auxiliares ordenados.
- **Mezclar gastos personales del dueño con los del negocio.** El negocio es una entidad aparte.
- **Memorizar códigos**: ten el catálogo a la mano; no se calcula de cabeza.

## Conexión con otros módulos

- **Módulo 11** — cómo cada clase se debita o acredita.
- **Módulo 12** — usar estas cuentas en asientos reales.
- **Módulo 14** — el libro mayor agrupa los movimientos por cuenta.
- **economist_lushows** DECIDE qué inversión hacer; el contador la REGISTRA en la cuenta correcta.

## Siguiente paso típico

Pasa al **módulo 11** para entender la regla de oro: cómo saber, para cada clase, qué la aumenta (débito) y qué la disminuye (crédito).

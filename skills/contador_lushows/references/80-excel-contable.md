# 80 — Excel para contabilidad: plantillas, fórmulas y buenas prácticas

Antes de pagar un software, casi todo negocio pequeño en Colombia empieza llevando sus números en **Excel** (o su primo gratuito, **Google Sheets**). Bien usado, Excel es una herramienta poderosa: arma libros auxiliares, concilia bancos, calcula nómina y prepara estados financieros sencillos. Mal usado, se convierte en un archivo lleno de fórmulas rotas donde nadie confía en el total.

Este módulo te enseña a usar Excel **como contador**: con orden, con fórmulas que se entienden y con la disciplina de no dañar lo que ya funciona. La promesa de la casa sigue vigente: **cuadre, cumplimiento y auditable**. Y nunca calculamos de cabeza: Excel ejecuta, pero la lógica del cálculo grande la valida `Matematicas_lushows`.

> **Excel ayuda, no exime de revisar.** Una fórmula puede estar "verde" (sin error visible) y aun así sumar mal porque apunta al rango equivocado. El control humano es obligatorio.

## Términos que debes conocer
- **Celda:** cada cuadrito (ejemplo: `B4`). Guarda un dato o una fórmula.
- **Rango:** un grupo de celdas (ejemplo: `B4:B20`, de la B4 a la B20).
- **Fórmula:** instrucción que empieza con `=` y calcula algo.
- **Referencia relativa / absoluta:** `B4` se mueve al copiar; `$B$4` queda fija (el `$` la "ancla").
- **Tabla dinámica (tabla pivote):** herramienta que resume miles de filas en un cuadro de totales sin escribir fórmulas.

## Fórmulas clave para contabilidad
| Fórmula | Para qué sirve | Ejemplo |
|---|---|---|
| `=SUMA(rango)` | Sumar una columna de valores | `=SUMA(C2:C100)` |
| `=SUMAR.SI(rango;criterio;rango_suma)` | Sumar solo lo que cumple una condición | total por cuenta o por mes |
| `=SUMAR.SI.CONJUNTO()` | Sumar con varias condiciones a la vez | gastos de "marzo" + "arriendo" |
| `=BUSCARV()` o `=BUSCARX()` | Traer un dato de otra tabla (ej. nombre de cuenta por su código) | `=BUSCARX(A2;PUC!A:A;PUC!B:B)` |
| `=SI(condición;valor1;valor2)` | Decidir entre dos resultados | marcar "cuadra"/"NO cuadra" |
| `=REDONDEAR(valor;2)` | Dejar dos decimales en dinero | evitar centavos fantasma |

## Plantillas que todo negocio necesita
1. **Libro diario:** fecha, descripción, cuenta débito, cuenta crédito, valor, soporte.
2. **Libro auxiliar por cuenta:** movimientos y saldo de cada cuenta (caja, banco, clientes...).
3. **Conciliación bancaria:** saldo libro vs. saldo extracto + partidas conciliatorias (ver 83).
4. **Flujo de caja:** entradas y salidas reales por semana o mes.
5. **Balance de prueba:** lista de cuentas con su saldo, que debe **cuadrar** (débitos = créditos).

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
En una hoja de balance de prueba, la celda de control podría ser:
`=SI(SUMA(D2:D50)=SUMA(E2:E50);"CUADRA";"REVISAR")`
Donde `D` son débitos y `E` créditos. Si en algún momento muestra "REVISAR", hay un asiento descuadrado. Esa celda es tu **semáforo de partida doble** dentro de Excel.

## Buenas prácticas para no dañar las fórmulas
- **Nunca borres celdas con fórmula** para escribir un número encima. Si necesitas un dato fijo, mételo en su propia celda de "entrada".
- **Separa entradas de cálculos:** una zona para datos que se digitan, otra para fórmulas. Pinta de color distinto las celdas que se pueden tocar.
- **Bloquea y protege** las celdas con fórmulas (Revisar → Proteger hoja) para que nadie las pise por error.
- **No insertes filas en medio de un rango** sin revisar que la `=SUMA()` se haya ampliado sola.
- **Usa una sola hoja por cosa** (un mes, un banco) y enlázalas; no amontones todo.
- **Guarda versiones con fecha** (`contabilidad_2026-03.xlsx`) y respáldalas (ver 87).
- **Revisa los totales contra otra fuente** (el extracto, la factura). Excel no se equivoca solo: equivoca quien escribe la fórmula.

## Cuándo Excel se queda corto
Excel es excelente para empezar y para análisis, pero **no genera factura electrónica ni nómina electrónica** ante la DIAN, no guarda historial de quién cambió qué, y se vuelve frágil con miles de movimientos. Cuando el negocio crece, se pasa a software contable (ver 81 y 82).

## Errores comunes
- Sumar "a ojo" un rango que dejó filas por fuera → el total miente.
- Copiar una fórmula sin anclar (`$`) la celda de referencia → apunta al lugar equivocado.
- Tener decimales sin redondear → el balance descuadra por un centavo.
- Un solo archivo gigante que todos editan a la vez → se corrompe y nadie sabe cuál es el bueno.

## Conexión con otros módulos
- **02 (partida doble)** y **11–12 (asientos)** — lo que registras en el libro diario de Excel.
- **83 (importar extractos y conciliar)** — la plantilla de conciliación en acción.
- **89 (plantillas de registro)** — formatos listos para copiar.
- **87 (respaldos y seguridad)** — cómo proteger estos archivos.
- **Matematicas_lushows** — cualquier cálculo grande o delicado se valida allá; Excel solo lo ejecuta.

## Siguiente paso típico
Si el negocio ya pasa de unas pocas decenas de movimientos al mes, evaluar el salto a software contable colombiano: abrir **81 (software contable en Colombia)**.

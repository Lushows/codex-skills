# 83 — Importar extractos bancarios y conciliar (semi-automático)

La **conciliación bancaria** es comparar lo que dice tu contabilidad (el saldo del banco según tus libros) con lo que dice el **extracto** del banco (el documento que el banco emite con todos los movimientos). Casi nunca coinciden exactamente al cierre del mes, y conciliar es encontrar **por qué** y dejarlos cuadrados. Es uno de los controles más importantes: detecta errores, cobros que no viste y hasta fraudes.

Hoy buena parte de este trabajo se hace **semi-automático**: descargas el extracto del banco, lo importas al software (o a Excel) y el sistema empareja solo la mayoría de los movimientos. Tú solo revisas las diferencias. "Semi" porque la máquina propone y **el humano confirma** (control humano obligatorio).

> **Auditable y con respaldo.** Cada partida conciliatoria debe quedar explicada y soportada. La automatización empareja; tú validas que el emparejamiento sea correcto. Cualquier resta o suma de saldos delicada se valida en `Matematicas_lushows`.

## Términos que debes conocer
- **Extracto bancario:** reporte del banco con todos los movimientos del mes (entradas, salidas, saldo).
- **Saldo según libros:** lo que tu contabilidad dice que tienes en el banco.
- **Partida conciliatoria:** una diferencia entre libro y extracto que se explica (ej: un cheque girado que aún no cobran).
- **Emparejar (match):** unir el movimiento del libro con el mismo del extracto.
- **Formato del archivo:** los bancos dan el extracto en PDF, Excel (`.xlsx`) o `.csv`. Para importar, sirve el Excel/CSV.

## Cómo importar el extracto
1. **Descarga el extracto** desde la banca en línea, preferible en **Excel o CSV** (el PDF no se importa bien).
2. **Revisa las columnas:** fecha, descripción, valor, débito/crédito. Ordénalas como las pide tu software.
3. **Importa** en el módulo de conciliación (Siigo, Alegra, World Office tienen esta función) o pega en tu plantilla de Excel (ver 80 y 89).
4. El sistema **empareja automáticamente** los movimientos que coinciden en fecha y valor.

## Cómo conciliar (semi-automático)
1. El software marca en verde lo que emparejó solo.
2. Tú revisas los **no emparejados**, que suelen ser:
   - Pagos que el banco ya cobró pero no registraste (comisiones, 4x1000, intereses).
   - Cheques o transferencias que registraste pero el banco aún no procesó.
   - Errores de digitación (un valor mal tecleado).
3. **Registra los faltantes** (ej: el asiento de la comisión bancaria) y **corrige los errores**.
4. Al final, el **saldo conciliado debe coincidir** con el extracto. Si no, sigue habiendo una diferencia por encontrar.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
"Panadería La Espiga" cierra marzo:
- Saldo según libros: $4.820.000
- Saldo según extracto: $4.770.000
- Diferencia: $50.000. Al revisar, el banco cobró $50.000 de comisión + 4x1000 que no estaban registrados.
- Se registra ese gasto bancario. Nuevo saldo en libros: $4.770.000 → **coincide con el extracto. Conciliado.**
(Cifras inventadas para ilustrar; la resta se confirma en `Matematicas_lushows`.)

## Buenas prácticas
- **Concilia cada mes**, no acumules; encontrar un error de hace 6 meses es una pesadilla.
- **Guarda el extracto** como soporte de la conciliación (ver 87).
- **No "forces el cuadre"** tapando una diferencia con un asiento inventado: investiga la causa real.
- Revisa siempre las **comisiones y el 4x1000**: son las partidas que más se olvidan.

## Errores comunes
- Importar el PDF y confiar en un emparejamiento sucio → datos mal cargados.
- Aceptar todos los "match" automáticos sin revisar → puede emparejar dos movimientos parecidos pero distintos.
- Dejar diferencias "pequeñas" sin explicar → se acumulan y descuadran el banco.
- Olvidar registrar comisiones e intereses bancarios → el saldo nunca cuadra.

## Conexión con otros módulos
- **80 (Excel)** y **89 (plantillas)** — la plantilla de conciliación.
- **12 (registro de asientos)** — registrar las partidas faltantes (comisiones, intereses).
- **88 (flujo mensual)** — la conciliación es un paso fijo del cierre del mes.
- **85 (OCR)** — para extractos en PDF, el OCR ayuda a extraer movimientos.
- **Matematicas_lushows** — toda diferencia y cuadre de saldos se valida allá.

## Siguiente paso típico
Con el banco conciliado, seguir capturando documentos. Si entran muchas facturas en papel/PDF, abrir **85 (OCR de facturas)**.

# 76 — Arqueo de caja y toma física de inventario

Una cosa es lo que dicen los **libros** y otra lo que hay **de verdad** en la caja, en la bodega o en el escritorio. El **arqueo** y la **toma física** son los procedimientos que cierran esa brecha: cuentas a mano lo que realmente existe y lo comparas con lo que el sistema dice que debería existir. Si no cuadra, encontraste un problema (un error, un faltante, un robo) **antes** de que crezca. Son los controles más antiguos, más simples y más eficaces de la contabilidad.

Este módulo da los **fundamentos**. El muestreo estadístico para conteos grandes vive en los módulos **170-179**.

> **Cuadre puro.** Aquí la promesa del oficio se vuelve física: el saldo en libros debe cuadrar con el conteo real. Y queda **auditable**, porque todo arqueo o toma se documenta en un **acta firmada** (que es un papel de trabajo, módulo 72). **Nunca cuentes "a ojo": se cuenta unidad por unidad y la suma se ejecuta/verifica con `Matematicas_lushows`.**

## Términos que debes conocer
- **Arqueo de caja:** contar el efectivo (y vales/cheques) que hay físicamente y compararlo con el saldo en libros.
- **Toma física (conteo):** contar las unidades reales de inventario o de activos fijos.
- **Faltante:** hay menos de lo que dicen los libros (alerta de error o fraude).
- **Sobrante:** hay más de lo que dicen los libros (también es un descuadre que hay que explicar).
- **Acta:** el documento firmado que deja constancia de qué, cuándo, quién y el resultado.

## Cómo se hace un arqueo de caja (paso a paso)
1. **Sorpresa:** idealmente sin avisar, para que nadie "acomode" la caja.
2. **Cortar:** definir el momento exacto del corte (no entran ni salen movimientos nuevos).
3. **Contar:** efectivo por denominación + cheques + vales.
4. **Comparar:** total contado vs. saldo en libros a ese corte.
5. **Documentar:** acta con el resultado y firmas del responsable de caja y de quien arquea.

## Cómo se hace una toma física de inventario
- Se cuenta **unidad por unidad** (o por peso/medida) cada referencia.
- Se compara contra el **kardex** (el registro de existencias, ver módulo 30).
- Las diferencias se investigan: ¿error de digitación?, ¿merma?, ¿robo?
- Se ajustan los libros para que reflejen la realidad (con su soporte).

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
Arqueo sorpresa en "Café de la Esquina" (cifras inventadas):
- **Saldo en libros a la hora del corte:** $520.000
- **Efectivo contado:** $485.000 (billetes + monedas + un vale de $20.000)
- **Total real:** $505.000 → **faltante de $15.000**

El faltante se registra, se documenta en el acta y se investiga. Si se repite, hay un problema de control (módulo 70) que resolver.

## Errores comunes
- Avisar el arqueo con anticipación: pierde el factor **sorpresa** y su valor.
- No definir un **corte** claro: entran movimientos durante el conteo y nada cuadra.
- Contar "redondeando" o por bultos sin abrir: los faltantes se esconden ahí.
- No firmar el **acta**: sin documento, el procedimiento no es auditable.
- Ajustar el descuadre sin investigar la **causa**: se tapa el síntoma y vuelve el mes siguiente.

## Conexión con otros módulos
- **30 (Inventarios PEPS/promedio)** — el kardex contra el que se compara la toma física.
- **70 (Control interno)** — el arqueo es un control estrella.
- **72 (Papeles de trabajo)** — el acta de arqueo es un papel de trabajo típico.
- **74 (Fraude)** — faltantes recurrentes son bandera roja.
- **Matematicas_lushows** — toda suma y comparación del conteo se ejecuta y verifica.

## Siguiente paso típico
Programar arqueos sorpresa periódicos y una toma física de inventario al menos al cierre. Cada diferencia se documenta y, si se repite, se refuerza el **control interno** (módulo 70) y la **segregación de funciones** (módulo 77).

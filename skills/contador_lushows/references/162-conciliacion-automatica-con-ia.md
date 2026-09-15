# 162 — Conciliación automática con IA

**Conciliar** es comparar lo que dice el banco (el extracto) con lo que dicen tus libros, y dejarlos iguales: cada movimiento del banco debe tener su respaldo en la contabilidad y viceversa. Hacerlo a mano, línea por línea, es de las tareas más tediosas del cierre. La IA la acelera muchísimo emparejando movimientos automáticamente; pero lo valioso no es lo que cuadra solo, sino **las excepciones**: lo que no casa es donde está el error, el fraude o el dato faltante, y eso lo revisa una persona.

Recordatorio de los módulos 22 y 75: conciliar no es "que el saldo coincida por casualidad", es explicar **cada diferencia** (cheques no cobrados, consignaciones en tránsito, comisiones, etc.).

## Cómo empareja la IA

| Criterio | Qué hace | Confianza |
|---|---|---|
| Monto + fecha exactos | Casa 1 a 1 | Alta |
| Monto exacto, fecha cercana | Casa con tolerancia de días | Media |
| Referencia/descripción similar | Usa el texto del movimiento | Media |
| 1 contra varios (un pago a varias facturas) | Suma partidas hasta cuadrar | Requiere revisión |
| No encuentra par | A la bandeja de excepciones | Humano |

## La regla: revisar las excepciones

Lo que la IA empareja con alta confianza se acepta (con una muestra de control). Lo que queda **sin pareja o dudoso** es el verdadero trabajo:

- Comisiones, 4x1000 (gravamen a los movimientos financieros) o intereses que el banco cobró y aún no registraste.
- Consignaciones o cheques en tránsito.
- Pagos dobles, devueltos o errados.
- Movimientos que no reconoces → **posible fraude o error**, se investiga.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

El banco muestra una salida de $1.000.000 y en libros hay dos facturas por pagar de $600.000 y $400.000. La IA propone: este pago corresponde a esas dos facturas (600.000 + 400.000 = 1.000.000 ✔, verificado en código). El contador confirma. Aparte, el banco cobró $4.000 de 4x1000 que no estaba en libros → excepción → se registra como gasto financiero. Cifras inventadas.

## Errores comunes

- **Aceptar el emparejamiento "1 a varios" sin revisar**: ahí se cuelan pagos mal aplicados.
- **Ignorar las excepciones** porque "son pocas": justo ahí vive el problema grave.
- **No registrar comisiones e impuestos bancarios**: el saldo nunca cuadra.
- **Conciliar con tolerancia de fecha demasiado amplia**: empareja cosas que no van juntas.
- **Dar por buena la conciliación sin que un humano la firme**: la IA propone, el contador concilia.

## Conexión con otros módulos

- La **conciliación bancaria** clásica está en el módulo **75**; el **flujo de efectivo** en el **22**.
- Los datos del banco pueden llegar por **OCR del extracto** (módulo **161**) o por **open finance / API** en tiempo real (módulos **164** y **166**).
- Los **controles** sobre lo que la IA empareja: módulo **167**.
- Toda suma de partidas y diferencia: `Matematicas_lushows`.

## Siguiente paso típico

En tu próxima conciliación, deja que la herramienta empareje y concéntrate **solo en la bandeja de excepciones**. Documenta cada diferencia con su explicación y soporte. Si las excepciones son siempre las mismas (comisiones, 4x1000), crea una regla para registrarlas automáticamente (módulo 163).

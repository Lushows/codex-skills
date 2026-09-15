# 167 — Controles internos cuando la IA hace el trabajo

Cuando una IA lee facturas, concilia y sugiere asientos, surge una pregunta incómoda: **¿quién vigila a la IA?** La respuesta son los **controles internos**: las reglas y revisiones que aseguran que lo automatizado esté bien, sea trazable y se pueda auditar. Automatizar **no quita** controles, los **cambia**: el contador deja de digitar y pasa a supervisar, revisar muestras y exigir que todo deje rastro. Sin controles, la IA es velocidad para equivocarse más rápido.

Este es el módulo que sostiene la promesa: **AUDITABLE**. Si un auditor (o la DIAN) pregunta "¿cómo llegó este número aquí?", debe haber respuesta clara.

## Los controles clave sobre lo automatizado

| Control | Qué asegura |
|---|---|
| **Trazabilidad** | Cada dato dice de dónde salió y quién lo aprobó |
| **Revisión por muestra** | Se revisa un % de lo auto-aprobado, no se confía a ciegas |
| **Bandeja de excepciones** | Lo dudoso siempre va a un humano |
| **Segregación de funciones** | Quien registra no es el único que aprueba |
| **Soporte archivado** | Todo asiento conserva su documento fuente |
| **Cuadre automático** | Débitos = créditos, base + impuestos = total (en código) |
| **Límites y aprobaciones** | Por encima de cierto monto, humano obligatorio |

## Trazabilidad: el rastro que todo lo sostiene

**Trazabilidad** es poder reconstruir la historia de cada cifra: qué factura la originó, qué regla o IA la clasificó, quién la aprobó y cuándo. Un buen sistema registra una **bitácora** (log) inalterable de esto. Sin bitácora no hay auditoría posible y, si algo sale mal, no se puede deshacer ni explicar.

## El humano cambia de rol, no desaparece

- Antes: digitaba todo. Ahora: **revisa, aprueba y audita**.
- Define las **reglas** que la IA aplica.
- Atiende la **bandeja de excepciones**.
- Revisa una **muestra** de lo auto-aprobado periódicamente.
- **Firma**: la responsabilidad sigue siendo de la persona (módulo 169).

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Una empresa auto-aprueba facturas de menos de $200.000 y revisa una muestra del 10% cada mes. En la muestra encuentra que la IA clasificó 3 de 50 en la cuenta equivocada → ajusta la regla y revisa todas las de ese proveedor. El control detectó el patrón antes de que creciera. Cifras y porcentajes inventados.

## Errores comunes

- **Automatizar y dejar de revisar**: el control es lo que hace segura la automatización.
- **No guardar bitácora**: sin rastro, nada es auditable.
- **Que la misma persona configure, apruebe y firme sin contrapeso**: falta segregación.
- **No archivar el soporte** del que partió cada asiento.
- **Revisar "cuando haya tiempo"**: la muestra debe ser periódica y obligatoria.

## Conexión con otros módulos

- La **promesa AUDITABLE** y el soporte de cada asiento: módulos **01**, **02** y **12**.
- Los procesos que se controlan: **OCR** (**161**), **conciliación** (**162**), **asientos** (**163**), **agentes** (**165**).
- La **responsabilidad y por qué firma el humano**: módulo **169**.
- La **información exógena y la auditoría/revisoría** que exigen este rastro: bloques de cierre y cumplimiento.
- Todo cuadre y muestra estadística: `Matematicas_lushows`.

## Siguiente paso típico

Escribe tu **matriz de controles**: para cada tarea automatizada, qué se auto-aprueba, qué va a excepciones, qué muestra se revisa y dónde queda la bitácora. Revísala con quien firma. Una automatización sin esta matriz no está lista para producción.

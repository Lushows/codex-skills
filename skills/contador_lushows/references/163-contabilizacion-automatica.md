# 163 — Contabilización automática (asientos sugeridos por IA)

Una vez la IA leyó la factura (módulo 161), el siguiente paso es **convertirla en asiento contable**: decidir qué cuenta del PUC se debita y cuál se acredita, por cuánto. La IA puede **sugerir** ese asiento aprendiendo de cómo se registró antes "este proveedor", "este tipo de gasto". Pero la palabra clave es **sugerir**: la partida doble tiene que cuadrar y el criterio (¿es gasto o activo? ¿es deducible?) es humano. La IA propone el borrador; el contador lo aprueba o corrige.

Recordatorio de los módulos 02 y 12: todo asiento cumple **débitos = créditos** y necesita **soporte**. La IA no exime de eso; al contrario, lo facilita si está bien controlada.

## Dos formas de automatizar

| Forma | Cómo funciona | Cuándo conviene |
|---|---|---|
| **Reglas fijas** | "Si el proveedor es X → cuenta Y" (definidas por el contador) | Casos repetitivos y claros (arriendo, servicios) |
| **Sugerencia con IA** | El modelo propone la cuenta según el historial y el texto | Casos variados, proveedores nuevos |
| **Mixto (recomendado)** | Reglas para lo seguro, IA para lo demás, humano aprueba | La mayoría de empresas |

## El flujo con red de seguridad

1. La IA propone: cuenta, valor, débito/crédito, impuestos.
2. **Validación automática**: ¿cuadra? ¿el IVA va a la cuenta correcta? ¿hay soporte?
3. **Aprobación humana**: el contador confirma o corrige; al corregir, la IA aprende.
4. **Registro y archivo del soporte** (auditabilidad, módulo 167).

Cuanto más nuevo o raro el caso, más obligatoria la revisión. Lo repetitivo y verificado puede auto-aprobarse con una muestra de control.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Llega factura de arriendo: base $1.000.000, IVA $190.000. La IA, viendo que es "Inmobiliaria X", propone:

| Cuenta | Débito | Crédito |
|---|---|---|
| Gasto arrendamiento | $1.000.000 | |
| IVA descontable | $190.000 | |
| Retención en la fuente por pagar | | $35.000 |
| Cuentas por pagar proveedores | | $1.155.000 |

Débitos $1.190.000 = créditos $1.190.000 ✔. El contador revisa la retención (¿la tarifa es la correcta?), aprueba. Cifras y tarifa inventadas; toda retención se verifica con la norma vigente y `Matematicas_lushows`.

## Errores comunes

- **Aprobar en masa sin mirar**: la IA arrastra un error de cuenta a cientos de asientos.
- **Dejar que la IA decida si algo es deducible o activo**: eso es criterio profesional.
- **Aplicar mal la retención o el IVA** por copiar el asiento anterior sin pensar.
- **Auto-aprobar proveedores nuevos**: justo ahí es donde más se equivoca.
- **Perder el rastro de quién aprobó qué**: sin trazabilidad no hay auditabilidad (módulo 167).

## Conexión con otros módulos

- El **registro de asientos** y la partida doble: módulos **02**, **11** y **12**.
- El **plan de cuentas (PUC)** que la IA usa para clasificar: módulo **10**.
- Los datos vienen del **OCR** (módulo **161**); las **retenciones e IVA** del bloque 40.
- Los **controles, trazabilidad y muestra de auditoría**: módulo **167**.
- Toda tarifa, retención y cuadre: `Matematicas_lushows`.

## Siguiente paso típico

Haz una lista de tus 10 transacciones más repetidas (arriendo, nómina, servicios públicos, comisiones) y conviértelas en **reglas fijas**: ahí la automatización es segura. Para el resto, deja la IA sugiriendo y tú aprobando, midiendo cuántas correcciones haces por semana.

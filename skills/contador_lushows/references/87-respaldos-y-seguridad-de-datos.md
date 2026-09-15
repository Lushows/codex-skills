# 87 — Respaldos y seguridad de los datos contables

La contabilidad es **memoria y prueba**: si se pierde, no solo desaparece el trabajo de meses, también te quedas sin los **soportes** que la DIAN puede pedir. Por eso un buen contador trata los datos con dos cuidados: que **no se pierdan** (respaldos / backups) y que **no caigan en manos equivocadas** (seguridad y protección de datos personales). En Colombia, además, manejar nombres, cédulas y NITs de terceros activa la ley de **Habeas Data**.

Este módulo es práctico y para todo público: cómo respaldar, cómo proteger y cómo cumplir con los datos personales sin ser experto en informática.

> **Datos respaldados y seguros — promesa de la casa.** Una contabilidad sin respaldo no es auditable: si se cae el computador, no hay nada que mostrar. Y los datos de clientes/proveedores no son tuyos para usarlos como quieras: tienen dueño y ley.

## Términos que debes conocer
- **Respaldo (backup):** una copia de seguridad de tus datos, guardada en otro lugar.
- **Regla 3-2-1:** ten **3** copias, en **2** medios distintos, con **1** fuera del sitio (ej: en la nube).
- **Cifrado:** "candado matemático" que vuelve ilegible un archivo sin la clave.
- **Habeas Data (Ley 1581 de 2012):** ley colombiana que protege los datos personales; exige autorización para tratarlos y cuidarlos.
- **Dato personal:** cualquier dato de una persona identificable (cédula, nombre, teléfono, correo).

## Respaldos: cómo no perder la contabilidad
| Práctica | Detalle |
|---|---|
| **Automático** | Que el respaldo se haga solo (diario o semanal), no "cuando me acuerde" |
| **Regla 3-2-1** | 3 copias, 2 medios, 1 fuera del sitio (nube + disco externo) |
| **Versionado** | Guardar versiones con fecha (`contab_2026-03.xlsx`) por si una se daña |
| **Probar la restauración** | Cada cierto tiempo, intentar **recuperar** un respaldo: un backup que no se puede restaurar no sirve |
| **Software en la nube** | Siigo/Alegra/World Office en nube ya respaldan; aun así, **exporta tu copia** periódicamente |

## Seguridad: que no caiga en manos equivocadas
- **Contraseñas fuertes y distintas** por servicio; nunca compartidas en papelitos.
- **Doble factor (2FA)** en el correo, el banco y el software contable.
- **Permisos por persona:** cada quien ve solo lo que necesita (el cajero no ve la nómina completa).
- **Cifrado** de los archivos sensibles y de los discos.
- **Cuidado con el correo y WhatsApp:** no mandar bases de datos completas por canales abiertos.

## Habeas Data y datos personales (Colombia)
1. **Pide autorización** para tratar datos personales de clientes/empleados/proveedores.
2. **Usa los datos solo para lo autorizado** (la contabilidad, la facturación), no para otra cosa.
3. **Guárdalos seguros** (cifrado, permisos) y **el tiempo necesario**, no para siempre sin razón.
4. **Permite que la persona consulte, actualice o pida eliminar** sus datos.
5. Si manejas muchos datos, ten una **política de tratamiento de datos** y, si aplica, registro ante la SIC.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
"Ferretería El Tornillo" guarda la contabilidad solo en el computador de la caja. Un día el disco falla y pierden 5 meses de registros y los soportes escaneados. Reconstruirlos cuesta semanas y quedan expuestos ante la DIAN por no tener soportes. **Con la regla 3-2-1** (una copia en la nube + un disco externo + el computador), habrían restaurado todo en una tarde. (Caso ilustrativo/inventado.)

## Errores comunes
- "Tengo todo en el computador" → un solo lugar = una sola falla para perderlo todo.
- Respaldar pero **nunca probar la restauración** → el día que se necesita, no sirve.
- Mandar la base de clientes por WhatsApp/correo sin protección.
- Tratar datos personales sin autorización ni cuidado → riesgo legal (Habeas Data).
- Confiar en que "el software en la nube ya respalda" y no exportar nunca una copia propia.

## Conexión con otros módulos
- **80 (Excel)** y **89 (plantillas)** — los archivos que hay que respaldar.
- **85 (OCR)** y **86 (bot WhatsApp)** — guardar las imágenes originales como soporte.
- **88 (flujo mensual)** — el respaldo es un paso fijo del cierre.
- **01 (promesa)** — datos respaldados, seguros y auditables.
- **AVIS_lushows** — el bot también maneja Habeas Data al recibir datos por chat.

## Siguiente paso típico
Con los datos seguros y respaldados, ordenar el trabajo del mes de principio a fin: abrir **88 (flujo de trabajo mensual)**.

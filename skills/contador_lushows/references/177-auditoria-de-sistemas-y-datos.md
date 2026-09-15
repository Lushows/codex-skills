# 177 — Auditoría de sistemas y datos: cuando la contabilidad vive en software

Hoy casi ninguna empresa lleva los libros a mano: todo pasa por software (Siigo, Alegra, World Office, un ERP). Eso cambia el trabajo del auditor. Ya no basta revisar papeles: hay que **auditar el sistema que produce las cifras** —¿quién tiene acceso?, ¿el cálculo automático es correcto?, ¿los datos están completos?— y, a la vez, aprovechar que los datos son digitales para **analizarlos en masa** en vez de muestrear a mano. Esa segunda parte se hace con **CAATs**.

Este módulo es nuevo territorio frente al bloque 70-79, que asumía controles más manuales. Se apoya en el módulo 81/82 (software contable) para el "qué herramientas existen" y en el 87 (respaldos y seguridad) para la protección del dato.

> **Cumplimiento + auditable.** Cuando se prueban datos masivos, hay que documentar **de dónde salió el extracto**, qué transformaciones se le hicieron y que cuadra con los saldos contables (control de integridad). Un análisis sobre datos mal extraídos concluye bonito y miente. Todo cálculo y prueba estadística (Benford, duplicados) se **rutea a `Matematicas_lushows`**. Este texto explica el oficio; **no reemplaza al auditor habilitado**.

## Términos que debes conocer
- **Auditoría de TI:** revisión de los controles del entorno informático.
- **CAATs (Técnicas de Auditoría Asistidas por Computador):** software para analizar grandes volúmenes de datos (Excel/Power Query, ACL, IDEA, SQL, Python).
- **Controles generales de TI (ITGC):** acceso, cambios, respaldos, operaciones — el "marco" del sistema.
- **Controles de aplicación:** validaciones dentro del programa (que no deje guardar una factura sin NIT, p. ej.).
- **Integridad del dato:** que el extracto analizado cuadre con la contabilidad oficial.

## Los dos frentes
| Frente | Pregunta que responde | Ejemplo |
|---|---|---|
| **Controles generales de TI** | ¿El entorno es confiable? | Solo el contador puede modificar asientos cerrados |
| **Controles de aplicación** | ¿El programa valida bien? | El sistema rechaza un IVA mal calculado |

Si los controles generales son débiles, ningún control de aplicación es confiable: alguien con acceso indebido puede saltarse todo.

## Qué permiten los CAATs
- Probar el **100%** de la población (ya no se muestrea: se revisa todo).
- Detectar **duplicados** (pagos repetidos, facturas con el mismo número).
- Cruzar bases: nómina contra cédulas activas, proveedores contra el RUT.
- Detectar saltos de secuencia, fechas en festivos, montos justo bajo un límite de aprobación.
- Aplicar la **Ley de Benford** sobre montos para olfatear cifras inventadas.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
El auditor de "Mercados del Sur SAS" exporta las 25.000 líneas del libro auxiliar (inventado). Primero verifica **integridad**: la suma del extracto = saldo del balance. Luego corre CAATs y encuentra 12 pagos duplicados por $9.300.000 (inventado) y 3 proveedores cuyo NIT no existe en el RUT. Matematicas aplica Benford a los montos de gastos y marca un patrón anómalo en cifras cercanas a $1.999.000 (justo bajo el tope de aprobación de $2.000.000). Eso dispara una revisión forense (módulo 174).

## Errores comunes
- Analizar un extracto sin probar que **cuadra con la contabilidad** → conclusiones sobre datos incompletos.
- Confiar en controles de aplicación cuando los **controles generales** (acceso) son un colador.
- "Auditar el sistema" mirando solo pantallas, sin revisar permisos ni bitácoras de cambios.
- Correr fórmulas o Benford de cabeza/manualmente en vez de ejecutarlas en Matematicas.
- No documentar la fuente y la fecha del extracto → el análisis no es reproducible.

## Conexión con otros módulos
- **172 (Muestreo)** — con CAATs muchas veces se prueba el 100% y no se muestrea.
- **174 (Forense)** — los CAATs son su herramienta central.
- **178 (Control interno COSO)** — los ITGC son parte de la actividad de control.
- **81/82 (Software contable)** — las herramientas que producen los datos.
- **87 (Respaldos y seguridad de datos)** — la protección del entorno.
- **`Matematicas_lushows`** — duplicados, Benford, pruebas estadísticas.

## Siguiente paso típico
Con los datos analizados, evaluar el **control interno** que debió evitar las anomalías (módulo 178) y redactar los **hallazgos** correspondientes (módulo 179).

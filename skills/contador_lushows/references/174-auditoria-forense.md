# 174 — Auditoría forense: cuando se busca el fraude a propósito

La auditoría normal busca dar una **opinión razonable** sobre los estados financieros; no es una cacería de ladrones. La **auditoría forense**, en cambio, sí: se activa cuando hay **sospecha o indicio de fraude** y su objetivo es investigar, reunir evidencia que sirva ante un juez o una autoridad, y a veces cuantificar el daño. Mezcla contabilidad, investigación y derecho.

Este módulo profundiza lo que el módulo 74 (detección de fraude) introdujo. Allí está el "qué es el fraude y cómo huele"; aquí está el "cómo se investiga formalmente cuando ya hay humo". Las NIA tratan la responsabilidad del auditor frente al fraude (NIA 240), pero la forense va más allá del encargo de auditoría ordinario.

> **Cumplimiento + auditable + cadena de custodia.** En forense, la evidencia puede terminar en un proceso legal: por eso la **cadena de custodia** (registro de quién tocó cada prueba, cuándo y cómo) es sagrada. Una prueba mal manejada se cae en el juzgado. Este texto explica el oficio; **no reemplaza al auditor forense, al perito ni al abogado** que actúan con responsabilidad legal.

## Términos que debes conocer
- **Fraude:** acto **intencional** para obtener un beneficio injusto (≠ error, que no es intencional).
- **Triángulo del fraude:** las tres condiciones que suelen coincidir —presión, oportunidad y racionalización.
- **Cadena de custodia:** la trazabilidad documentada de cada evidencia desde que se recoge hasta que se presenta.
- **Lavado de activos:** dar apariencia legal a dinero de origen ilícito (SARLAFT lo regula en Colombia).
- **Indicio (red flag):** señal que sugiere fraude (gastos sin soporte, proveedores fantasma, vidas por encima del ingreso).

## El triángulo del fraude
| Vértice | Qué es | Ejemplo |
|---|---|---|
| **Presión** | El motivo (deudas, metas, vicios) | Empleado endeudado |
| **Oportunidad** | El hueco de control que lo permite | Una sola persona maneja y aprueba pagos |
| **Racionalización** | La justificación mental | "Me lo merezco, me pagan poco" |

El control interno (módulo 178) ataca sobre todo la **oportunidad**, que es el vértice que la empresa sí puede cerrar.

## Técnicas forenses
- **Análisis de datos masivos / CAATs** (módulo 177): pagos duplicados, números de factura repetidos, **Ley de Benford** sobre montos.
- **Reconstrucción de transacciones** y seguimiento del rastro del dinero.
- **Entrevistas investigativas** (técnica distinta a la indagación ordinaria).
- **Análisis patrimonial:** comparar el patrimonio/gasto de una persona con sus ingresos lícitos.
- **Recálculo del perjuicio:** cuantificar el daño → se rutea a `Matematicas_lushows`.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
En "Transportes Unidos SAS" saltan pagos a un proveedor "Suministros XYZ" por $48.000.000 (inventado) en seis meses. La forense aplica CAATs y halla que el NIT no existe en el RUT y que la cuenta bancaria coincide con la del jefe de compras (oportunidad: él pedía y aprobaba). Se documenta con **cadena de custodia** cada soporte, se entrevista, y Matematicas cuantifica el perjuicio. El informe se entrega a la gerencia y, si corresponde, a la Fiscalía.

## Errores comunes
- Confundir error con fraude: el error no es intencional; acusar sin probar la intención es grave.
- Romper la **cadena de custodia** (manipular originales, no registrar quién los tuvo) → prueba inservible.
- "Investigar" interrogando a sospechosos sin método ni respaldo legal.
- Cuantificar el perjuicio de cabeza en vez de ejecutarlo en Matematicas.
- Olvidar las obligaciones de reporte (SARLAFT, autoridades) cuando hay indicios de lavado.

## Conexión con otros módulos
- **74 (Detección de fraude)** — los fundamentos que aquí se profundizan.
- **178 (Control interno COSO)** — cierra la "oportunidad" del triángulo.
- **177 (CAATs)** — la herramienta principal del análisis forense.
- **175 (Revisoría fiscal)** — el revisor tiene deber legal de denunciar ciertos hechos.
- **`Matematicas_lushows`** — cuantifica el perjuicio y aplica pruebas estadísticas (Benford).
- **`AVIS_lushows`** — cuando el caso toca cumplimiento/reportes de la pyme.

## Siguiente paso típico
Con la investigación cerrada, redactar el **hallazgo** (condición, criterio, causa, efecto — módulo 179) y, si aplica, alimentar el **informe/dictamen** y los reportes legales del revisor fiscal (módulos 175 y 176).

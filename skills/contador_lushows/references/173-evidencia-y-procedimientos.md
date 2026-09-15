# 173 — Evidencia y procedimientos: cómo el auditor se convence

La opinión del auditor no vale por su buena fe: vale por la **evidencia** que reunió. Evidencia de auditoría es toda la información que respalda las conclusiones —documentos, confirmaciones de terceros, lo que el auditor vio con sus ojos, los cálculos que rehizo—. Y los **procedimientos** son las técnicas para obtenerla. Sin evidencia suficiente y adecuada, no hay opinión que sostener.

Este módulo desarrolla A FONDO lo que el módulo 71 introdujo. Aquí distinguimos los tipos de evidencia, su fortaleza, y los procedimientos sustantivos frente a los de control (las NIA dedican a esto la familia NIA 500).

> **Cumplimiento + auditable.** Cada conclusión debe rastrearse hasta su evidencia, que se archiva en los papeles de trabajo (módulo 72). "Lo revisé y estaba bien" no es evidencia; la copia del soporte, la confirmación firmada o el recálculo sí lo son. Este texto explica el oficio; **no reemplaza al auditor habilitado**.

## Términos que debes conocer
- **Evidencia suficiente:** la cantidad necesaria (se relaciona con el muestreo, módulo 172).
- **Evidencia adecuada:** la calidad —relevancia y confiabilidad— de la evidencia.
- **Procedimiento sustantivo:** prueba que busca detectar errores monetarios directamente en los saldos/transacciones.
- **Prueba de controles:** verifica que un control de la empresa funciona (no el saldo, sino el control).
- **Aseveraciones:** las afirmaciones implícitas en los estados (existencia, integridad, valuación, derechos, presentación).

## Jerarquía de confiabilidad de la evidencia
No toda evidencia pesa igual. De más fuerte a más débil (regla general):

| Evidencia | Confiabilidad |
|---|---|
| Obtenida directamente por el auditor (inspección física, recálculo) | Muy alta |
| De fuente externa independiente (confirmación bancaria) | Alta |
| Interna pero con buen control | Media |
| Interna con control débil o verbal | Baja |

## Los procedimientos de auditoría
1. **Inspección:** examinar documentos o activos físicos.
2. **Observación:** mirar un proceso mientras ocurre (el conteo de inventario).
3. **Confirmación externa:** pedir a un tercero (banco, cliente) que confirme un saldo.
4. **Recálculo:** rehacer los cálculos de la empresa (intereses, depreciación) → se rutea a `Matematicas_lushows`.
5. **Reejecución:** repetir un control manualmente.
6. **Procedimientos analíticos:** comparar cifras, razones y tendencias para detectar lo anómalo.
7. **Indagación:** preguntar al personal (la más débil; se corrobora con otra).

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
Para auditar la cartera de "Servicios del Norte SAS", el auditor combina: **confirmación externa** (escribe a 30 clientes pidiendo que confirmen su saldo), **recálculo** del deterioro (Matematicas rehace la provisión y obtiene $3.200.000 frente a los $2.900.000 registrados —inventado—, diferencia que se evalúa contra la materialidad) y **procedimientos analíticos** (la rotación de cartera pasó de 45 a 80 días, señal de alerta). La indagación con el área de cobranza corrobora.

## Errores comunes
- Conformarse con la **indagación** (lo que dijeron) sin corroborar con evidencia más fuerte.
- Tratar un documento interno como si fuera tan confiable como una confirmación externa.
- Recalcular de cabeza intereses o deterioros en vez de ejecutarlos en Matematicas.
- Reunir mucha evidencia de baja calidad y creer que "cantidad" compensa la "adecuación".
- No vincular cada prueba con la **aseveración** que pretende cubrir.

## Conexión con otros módulos
- **172 (Muestreo)** — define sobre qué partidas se aplican los procedimientos.
- **171 (Riesgo y materialidad)** — más riesgo exige evidencia más fuerte.
- **177 (Auditoría de sistemas y datos)** — los CAATs son procedimientos sobre datos masivos.
- **72 (Papeles de trabajo)** — donde se archiva toda la evidencia.
- **179 (Hallazgos)** — la evidencia es la base de cada hallazgo.
- **`Matematicas_lushows`** — ejecuta recálculos y analíticos cuantitativos.

## Siguiente paso típico
Si la evidencia revela indicios de irregularidad intencional, escalar a la **auditoría forense** (módulo 174). Los recálculos se ejecutan en `Matematicas_lushows`.

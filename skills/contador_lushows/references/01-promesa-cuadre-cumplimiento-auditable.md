# 01 — La promesa: CUADRE + CUMPLIMIENTO + AUDITABLE

Toda esta skill se sostiene sobre tres pilares que no se negocian. Si alguno falla, el trabajo no sirve, por bonito que se vea. Este módulo explica a fondo qué significa cada pilar, cómo se verifica, y por qué juntos te dan tranquilidad real (no falsa). Es la diferencia entre "una contabilidad que parece bien" y "una contabilidad que aguanta una auditoría de la DIAN".

## Pilar 1 — CUADRE (los números cierran)

**Qué es:** en partida doble, cada movimiento se anota dos veces —una como débito y otra como crédito— y la suma de todos los débitos debe ser **exactamente igual** a la suma de todos los créditos. No "casi igual": igual al centavo.

**Por qué importa:** si no cuadra, hay un error escondido. Puede ser que registraste mal, que se te perdió una transacción, o que la calculadora redondeó feo. Un descuadre es una alarma, no un detalle.

**Cómo se verifica:**
- El **balance de comprobación** (lista de todas las cuentas con sus saldos) debe tener total de débitos = total de créditos.
- La ecuación contable Activo = Pasivo + Patrimonio debe mantenerse (módulo 02).
- Cualquier cálculo de respaldo se ejecuta en código con `decimal`, nunca `float`, y se verifica dos veces (o se rutea a **Matematicas_lushows**).

### Ejemplo de cuadre (cifras ILUSTRATIVAS / inventadas)

Compraste un computador de $2.000.000 pagando $500.000 en efectivo y el resto a crédito.

| Cuenta | Débito | Crédito |
|---|---|---|
| Equipo de cómputo | 2.000.000 | |
| Caja | | 500.000 |
| Cuentas por pagar | | 1.500.000 |
| **Totales** | **2.000.000** | **2.000.000** |

Débitos = créditos = 2.000.000. **Cuadra.** Las cifras son inventadas para ilustrar.

## Pilar 2 — CUMPLIMIENTO (cumplir la ley a tiempo y en formato)

**Qué es:** declarar y pagar lo que toca, cuando toca, en el formato y por el canal que exige la autoridad. En Colombia eso significa la **DIAN** (impuestos nacionales), el **municipio** (ICA), la **UGPP/PILA** (seguridad social) y el marco contable **NIIF**.

**Por qué importa:** los números pueden estar perfectos, pero si presentas tarde o en el formato equivocado, hay sanciones, intereses y a veces cierre del negocio.

**Cómo se verifica:**
- Calendario tributario al día (fechas dependen del NIT y del tipo de obligación; **deben verificarse cada año** porque cambian).
- Formatos correctos: factura electrónica, nómina electrónica, información exógena, formato 2516, etc.
- Importante: las **tasas, los valores de la UVT y los porcentajes cambian cada año**. Esta skill te explica el *concepto* y te dice dónde confirmar el número vigente; **no inventa** el valor exacto del año.

## Pilar 3 — AUDITABLE (todo se puede rastrear y defender)

**Qué es:** cualquier persona —un auditor, la DIAN, un socio, tú mismo en dos años— puede tomar cualquier número del estado financiero y rastrearlo hacia atrás hasta el documento que lo originó.

**Por qué importa:** un número sin soporte es indefendible. En una auditoría, "yo me acuerdo que fue así" no vale nada.

**Cómo se verifica:**
- Cada asiento tiene su **soporte** archivado (factura, recibo, extracto, contrato).
- Hay una **pista de auditoría**: quién registró, cuándo, con qué documento.
- Los **estados financieros conectan** con el balance de comprobación, que conecta con el libro mayor, que conecta con los asientos, que conectan con los soportes. Cadena completa.

## Cómo se ven los tres juntos

| Pilar | Pregunta de control | Si falla… |
|---|---|---|
| Cuadre | ¿Débitos = créditos? | Hay un error escondido; no avanzar |
| Cumplimiento | ¿Presenté a tiempo y bien? | Sanciones e intereses |
| Auditable | ¿Puedo probar cada número? | Indefendible ante la DIAN |

## Errores comunes

- **Creer que "cuadrar" es opcional o aproximado.** No lo es. Centavos importan.
- **Tener números perfectos pero presentar tarde.** El cumplimiento es tan importante como el cuadre.
- **Registrar sin guardar soportes.** Mata la auditabilidad de un solo golpe.
- **Tomar el valor de la UVT o una tasa "de memoria".** Cambian cada año; siempre confirmar la vigencia.
- **Usar `float` para dinero.** Genera descuadres de centavos. Siempre `decimal`.

## Conexión con otros módulos

- La mecánica del cuadre vive en el módulo **02**.
- El marco normativo (NIIF, local) que sostiene el cumplimiento está en el **03**.
- La ética que sostiene la auditabilidad está en el **04**.
- Los cálculos exactos que protegen el cuadre van a **Matematicas_lushows**.
- Los límites de responsabilidad (qué NO garantiza esta skill) están en el **09**.

## Siguiente paso típico

Si entendiste la promesa, pasa al módulo **02** para aprender la mecánica que hace posible el cuadre: la ecuación contable y la partida doble.

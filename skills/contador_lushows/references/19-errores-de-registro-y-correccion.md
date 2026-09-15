# 19 — Errores de registro y cómo corregirlos (nunca borrar)

En contabilidad **se cometen errores** —es normal—, pero hay una regla de oro: **nunca se borra ni se tacha** un asiento. La contabilidad debe ser **auditable**: cualquiera debe poder ver qué pasó, incluido el error y su corrección. Borrar destruye el rastro y huele a fraude.

> **Regla AUDITABLE:** un error se corrige con **otro asiento** (de reversión o de ajuste), dejando ambos visibles. El historial completo se conserva.

## Errores típicos y cómo nacen

| Error | Qué pasó |
|---|---|
| De cuenta | Usaste la cuenta equivocada (gasto en vez de activo) |
| De valor | Anotaste un monto incorrecto (de más o de menos) |
| De inversión | Pusiste el débito donde iba el crédito |
| De omisión | No registraste un hecho que sí ocurrió |
| De duplicación | Registraste dos veces el mismo hecho |
| De trasposición | Cambiaste dígitos: 1.900 en vez de 1.090 |

## Las dos técnicas de corrección

### 1. Asiento de reversión (anular y volver a hacer)

Sirve cuando el asiento está **completamente mal**. Haces un asiento **espejo** (débitos y créditos invertidos) que lo deja en cero, y luego registras el correcto.

### 2. Asiento de ajuste (corregir la diferencia)

Sirve cuando solo está mal **por un monto**. Registras únicamente la **diferencia** para llegar al valor correcto, sin reversar todo.

## Ejemplo de reversión (cifras ILUSTRATIVAS / inventadas)

**Error:** registraste una compra de mercancía ($50.000) como gasto de arriendo.

Asiento equivocado original:

| Cuenta | Débito | Crédito |
|---|---|---|
| Arrendamientos (5120) | 50.000 | |
| Bancos (1110) | | 50.000 |

**Paso 1 — reversar (invertir el original):**

| Cuenta | Débito | Crédito |
|---|---|---|
| Bancos (1110) | 50.000 | |
| Arrendamientos (5120) | | 50.000 |
| **Totales** | **50.000** | **50.000** |

**Paso 2 — registrar el correcto:**

| Cuenta | Débito | Crédito |
|---|---|---|
| Inventarios (1435) | 50.000 | |
| Bancos (1110) | | 50.000 |
| **Totales** | **50.000** | **50.000** |

Concepto en ambos: "Corrección asiento #X — compra mal clasificada como arriendo". Queda todo el rastro.

## Ejemplo de ajuste por diferencia (cifras ILUSTRATIVAS / inventadas)

**Error:** registraste una venta de $90.000 cuando eran $100.000 (faltan $10.000). Solo corriges la diferencia:

| Cuenta | Débito | Crédito |
|---|---|---|
| Caja (1105) | 10.000 | |
| Ventas (4135) | | 10.000 |
| **Totales** | **10.000** | **10.000** |

## Buenas prácticas de corrección

- **Cita el asiento original** en el concepto del de corrección.
- **Adjunta el soporte** que prueba el valor correcto.
- Corrige **en el período correcto**; si el período ya cerró, sigue las reglas de errores de períodos anteriores (NIIF tiene un tratamiento específico).
- **Verifica que la corrección cuadre** (débitos = créditos) y que el saldo final quede como debía.

## Errores comunes (al corregir)

- **Borrar o tachar** el asiento malo: destruye la auditoría. Jamás.
- **Reversar de más** y dejar la cuenta peor que antes.
- **No citar** el asiento original: nadie entiende la corrección después.
- **Corregir de cabeza** la diferencia: calcúlala en código.

## Conexión con otros módulos

- **Módulo 12** — la corrección es, también, un asiento normal.
- **Módulo 13** — el diario conserva el error y la corrección, en orden.
- **Módulo 15** — tras corregir, el balance de comprobación debe volver a cuadrar.
- **Matematicas_lushows** EJECUTA la diferencia exacta a corregir.

## Siguiente paso típico

Con el ciclo contable dominado (módulos 10-19), pasa al **Bloque 2** para convertir estos registros en estados financieros que cuenten la historia del negocio.

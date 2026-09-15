# 111 — NIIF 16: Arrendamientos (el local y los equipos que arriendas)

Antes, si arrendabas un local, simplemente registrabas el canon como gasto cada mes y no aparecía nada en tu balance. NIIF 16 cambió eso para el **arrendatario** (quien arrienda, el que paga): casi todos los arrendamientos ahora se "suben" al balance como un **activo por derecho de uso** y un **pasivo por arrendamiento**. La lógica: si controlas un activo por varios años, debe verse en tus números, igual que si lo hubieras comprado a crédito.

Ojo grande con Colombia: esto aplica a **NIIF plenas (Grupo 1)**. En **NIIF para pymes (Grupo 2), la Sección 20** es distinta y MÁS SENCILLA — los arrendamientos operativos siguen como gasto lineal y NO subes el derecho de uso al balance. Por eso aquí marco claramente cuándo difieren.

Términos: **arrendatario** = el que usa el activo y paga. **Arrendador** = el dueño que lo cede. **Canon** = la cuota periódica.

## Plenas (Grupo 1) vs Pymes (Grupo 2)

| Tema | NIIF plenas (NIIF 16) | NIIF para pymes (Sección 20) |
|---|---|---|
| ¿Se sube al balance? | Sí: activo por derecho de uso + pasivo | No para operativos: solo gasto mensual |
| Clasificación operativo/financiero | Casi desaparece para el arrendatario | Se mantiene: operativo vs financiero |
| Reconocimiento del gasto | Depreciación + interés | Canon lineal en resultados |
| Excepciones | Corto plazo (≤12 meses) y bajo valor | No requiere capitalizar operativos |

## Cómo lo mide el arrendatario en NIIF plenas

1. **Pasivo por arrendamiento** = valor presente de los cánones futuros, descontados a la tasa implícita o a tu tasa de endeudamiento. (El valor presente lo calcula `Matematicas_lushows`.)
2. **Activo por derecho de uso** = el pasivo + costos iniciales.
3. Cada mes: el activo se **deprecia** y el pasivo genera **interés**.

## Ejemplo (cifras ILUSTRATIVAS / inventadas — NIIF plenas)

GastroLatam arrienda una oficina por 3 años, canon $1.000.000/mes. El valor presente de los 36 cánones a tu tasa da, supongamos, **$30.000.000** (calculado y verificado en código).

**Al inicio del contrato:**

| Cuenta | Débito | Crédito |
|---|---|---|
| Activo por derecho de uso (15) | 30.000.000 | |
| Pasivo por arrendamiento (22) | | 30.000.000 |

**Mes 1** (supongamos interés del mes $250.000 y depreciación lineal 30.000.000 / 36 = $833.333):

| Cuenta | Débito | Crédito |
|---|---|---|
| Gasto por intereses (5305) | 250.000 | |
| Gasto depreciación derecho de uso (5160) | 833.333 | |
| Pasivo por arrendamiento (22) | 750.000 | |
| Bancos (11) | | 1.000.000 |
| Depreciación acumulada (1592) | | 833.333 |

El débito al pasivo ($1.000.000 pagado − $250.000 de interés = $750.000) reduce la deuda. Los débitos suman 1.833.333 y los créditos 1.833.333: **cuadra**.

**El mismo arriendo en NIIF para pymes (Sección 20)** sería mucho más simple:

| Cuenta | Débito | Crédito |
|---|---|---|
| Gasto por arrendamiento (5120) | 1.000.000 | |
| Bancos (11) | | 1.000.000 |

## Errores comunes

- **Asumir que NIIF 16 aplica a tu pyme**: si eres Grupo 2, usas la Sección 20, mucho más liviana. Confirma tu grupo (ver módulo 117).
- **Capitalizar arriendos de corto plazo o de bajo valor** cuando hay exención (≤12 meses o activos pequeños como una impresora).
- **Usar el canon como tasa de descuento**: la tasa es la implícita del contrato o tu costo de endeudamiento, no el canon.
- **Olvidar la depreciación del derecho de uso**: el activo no se queda quieto, se deprecia durante el plazo.

## Conexión con otros módulos

- **30-39** (PP&E y depreciación): el derecho de uso se deprecia con la misma mecánica.
- **Matematicas_lushows**: valor presente de los cánones y tabla de amortización del pasivo.
- **114 — Impuesto diferido**: la diferencia entre el tratamiento contable y el fiscal del arriendo genera diferencias temporarias.
- **117 — Plenas vs pymes**: define cuál de los dos tratamientos te aplica.

## Siguiente paso típico

Identifica si eres Grupo 1 o Grupo 2 (módulo 117). Si eres Grupo 1 y tienes contratos de arriendo a más de 12 meses, pídele a `Matematicas_lushows` el valor presente y arma la tabla de amortización. Si eres Grupo 2, basta con registrar el canon como gasto.

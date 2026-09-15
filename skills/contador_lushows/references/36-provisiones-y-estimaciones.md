# 36 — Provisiones y estimaciones

Una **provisión** es el reconocimiento contable de una obligación que ya existe y que casi seguro vas a tener que pagar, pero de la que todavía **no sabes el monto exacto ni la fecha exacta**. Es distinta de una cuenta por pagar normal (módulo 34), donde ya tienes la factura y el valor exacto. La provisión dice: "esto ya me lo debo, va a salir plata, no sé cuánto exactamente, pero lo estimo y lo reconozco ahora para no llevarme una sorpresa".

La norma que la regula es la **NIC 37** (en NIIF para pymes, la sección de provisiones y contingencias). Reconocer provisiones a tiempo es lo que evita que tu utilidad se vea más alta de lo real por esconder deudas que ya existen.

## Las tres condiciones para reconocer una provisión

Se reconoce **solo si se cumplen las tres**:

| Condición | En palabras simples |
|---|---|
| **Obligación presente** | Ya existe la deuda hoy (por algo que ya pasó) |
| **Salida probable** | Es más probable que sí pagues a que no |
| **Estimación fiable** | Puedes estimar el monto con razonabilidad |

Si solo es *posible* (no probable), o no puedes estimarla, **no se provisiona**: se revela como un **pasivo contingente** (una nota informativa), pero no entra como número en el balance.

## Provisión vs. cuenta por pagar vs. contingencia

| Concepto | ¿Monto cierto? | ¿Va al balance? |
|---|---|---|
| Cuenta por pagar | Sí (hay factura) | Sí |
| **Provisión** | Estimado | Sí |
| Pasivo contingente | Incierto o no probable | No, solo se revela en notas |

## Ejemplos típicos

- Una **demanda laboral** que probablemente perderás: estimas la condena y provisionas.
- **Garantías** de productos vendidos: estimas cuánto te costará repararlos.
- **Desmantelamiento**: cuando estás obligado a desmontar o restaurar al final de un contrato.
- **Bonificaciones** comprometidas a empleados cuyo monto aún se calcula.

## Ejemplo de registro (cifras ILUSTRATIVAS / inventadas)

Tienes una demanda laboral. El abogado dice que probablemente la perderás y estima la condena en $5.000.000.

| Cuenta | Débito | Crédito |
|---|---|---|
| Gasto por provisiones | $5.000.000 | |
| Provisión para litigios | | $5.000.000 |

Débitos = créditos = $5.000.000. Cuando el caso se resuelva, ajustas: si pagas exactamente eso, cancelas la provisión contra el banco; si fue distinto, ajustas la diferencia. Cifras inventadas para ilustrar; el monto estimado se sustenta en el criterio del abogado y, si hay cálculo, en `Matematicas_lushows`.

## Errores comunes

- **No provisionar una demanda probable** para no mostrar la utilidad más baja: oculta una deuda real.
- **Provisionar todo "por si acaso"**: una mera posibilidad no es provisión; es a lo sumo una nota.
- **Inventar el monto sin sustento**: la estimación debe ser fiable y documentada (concepto del abogado, histórico de garantías).
- **No revisar la provisión** cada cierre: si cambia la expectativa, hay que ajustarla.
- **Confundir provisión con depreciación**: la depreciación (módulo 32) no es una provisión, aunque a veces se le diga así coloquialmente.

## Conexión con otros módulos

- Se diferencia de las **cuentas por pagar** ciertas del módulo **34**.
- El **deterioro de cartera** (módulo **33**) es una estimación pariente de las provisiones.
- Las garantías estimadas afectan el costo de un producto vendido (módulo **38**).
- El monto estimado, si requiere cálculo, lo ejecuta **Matematicas_lushows**.
- Decidir *si vale la pena* asumir un riesgo (ej.: dar garantías) es decisión de **economist_lushows**.

## Siguiente paso típico

Haz una lista de obligaciones probables sin factura aún (demandas, garantías), evalúa las tres condiciones, provisiona las que califiquen y revisa cada provisión en el cierre del módulo de cierre contable.

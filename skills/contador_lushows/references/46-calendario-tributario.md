# 46 — Calendario tributario

Cumplir un impuesto no es solo liquidarlo bien: es **presentarlo y pagarlo a tiempo**. La DIAN publica cada año un **calendario tributario** que fija los plazos de cada obligación. Lo curioso del sistema colombiano es que el plazo **depende de los últimos dígitos del NIT** del contribuyente: la DIAN escalona los vencimientos para no concentrar todo en un solo día. Por eso "la fecha" no es igual para todos.

Este módulo explica **cómo leer el calendario**. **No inventamos fechas:** cambian cada año y por tipo de contribuyente. *Verifica siempre las fechas del año en el calendario oficial de la DIAN (y, para ICA, en cada municipio).*

## Conceptos clave
- **NIT (Número de Identificación Tributaria):** el identificador del contribuyente. El **dígito de verificación** es el número después del guion (ese **no** se usa para el plazo; se usan los **últimos dígitos del NIT** antes del DV).
- **Vencimiento:** la fecha límite para presentar y/o pagar sin sanción.
- **Plazo escalonado:** la DIAN asigna fechas distintas según el último (o dos últimos) dígito del NIT.
- **Declaración y pago:** a veces presentar y pagar tienen **fechas distintas** (sobre todo en renta, que puede tener cuotas).

## Cómo funciona el escalonamiento (CONCEPTO)
La DIAN publica una tabla así (ESTRUCTURA, no fechas reales):
| Último(s) dígito(s) del NIT | Vence (ejemplo de estructura) |
|---|---|
| 1 | un día |
| 2 | el siguiente día hábil |
| ... | ... |
| 0 | el último del grupo |

Para encontrar **tu** fecha: tomas tu NIT, miras el/los dígito(s) que la tabla pide ese año, y buscas la fila correspondiente. *La cantidad de dígitos que se usa puede variar por obligación y por año.*

## Calendario por tipo de obligación (todas tienen el suyo)
| Obligación | Periodicidad típica | Dónde se verifica |
|---|---|---|
| Renta (jurídicas / naturales) | Anual (puede ir en cuotas) | Calendario DIAN |
| IVA | Bimestral o cuatrimestral | Calendario DIAN |
| Retención en la fuente | Mensual | Calendario DIAN |
| ICA | Según municipio | Calendario del municipio |
| Exógena / información | Anual | Calendario DIAN |

## Ejemplo (cifras / fechas ILUSTRATIVAS / inventadas)
NIT 901.234.567**-8**. El "8" es el **dígito de verificación**, no cuenta para el plazo. Si el calendario de ese año usa el **último dígito del NIT** (el **7**), buscas la fila del 7 y esa es tu fecha. Supón que cae el "15 de mayo" (fecha **inventada**): debes presentar y pagar a más tardar ese día hábil.

> Fecha de ejemplo. Las reales se consultan en el calendario DIAN del año.

## Buenas prácticas de cumplimiento
- Arma un **tablero de vencimientos** del negocio (todas las obligaciones, con su fecha del año).
- Pon **recordatorios** unos días antes de cada vencimiento.
- Recuerda que si la fecha cae en **día no hábil**, suele correrse al siguiente hábil (verifica la regla del año).
- No esperes al último día: los portales se congestionan.

## Errores comunes
- Usar el **dígito de verificación** para buscar el plazo (es un error clásico: se usan los **dígitos del NIT**, no el DV).
- Asumir que "todos vencen el mismo día": el plazo es **personal según el NIT**.
- Olvidar que **presentar** y **pagar** pueden tener fechas distintas.
- Buscar el ICA en el calendario de la DIAN (es **municipal**, ver 44).
- Reutilizar el calendario del año pasado: **cambia cada año**.

## Conexión con otros módulos
- **41, 42, 43, 44** — cada impuesto tiene su periodicidad en este calendario.
- **47 (Presentación)** — una vez sabes la fecha, este módulo dice cómo presentar.
- **49 (Sanciones)** — pasarse de la fecha genera sanción por extemporaneidad e intereses.

## Siguiente paso típico
Construir el tablero de vencimientos del negocio con las fechas **del año en curso** (verificadas en la DIAN y en el municipio) y agendar recordatorios. Luego, para cada vencimiento, ir a **47**.

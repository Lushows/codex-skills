# 197 — Contingencias y pasivos ocultos

Hay deudas que ya están en los libros, y hay deudas que **todavía no se ven pero podrían volverse reales**: un pleito que puedes perder, una garantía que tendrás que cubrir, un impuesto que la DIAN podría cobrarte. Estas son las **contingencias** y los **pasivos ocultos**. Ignorarlos hace que los estados financieros se vean mejor de lo que son y sorprende a los dueños (y a la DIAN) en el peor momento. Por eso el cierre de calidad los busca activamente.

> **Pasivo contingente** = obligación posible que depende de un hecho futuro incierto (ej. el resultado de un juicio). **Provisión** = pasivo que ya es probable y se puede estimar, así que SÍ se reconoce en los libros. **Pasivo oculto** = deuda real que existe pero nadie registró.

## La clave: ¿probable, posible o remoto?

Bajo NIIF, el tratamiento depende de qué tan probable es que la obligación se vuelva real:

| Probabilidad | Tratamiento contable |
|---|---|
| **Probable** y estimable | Se **provisiona** (entra al pasivo y al gasto) |
| **Posible** (no probable) | Solo se **revela en notas** (módulo 24), no se registra |
| **Remota** | No se hace nada |

La diferencia entre provisionar y solo revelar cambia la utilidad y el patrimonio, así que clasificarla bien importa.

## Dónde se esconden los pasivos ocultos

- **Litigios laborales y civiles**: demandas en curso que nadie pasó a contabilidad.
- **Sanciones tributarias o de la DIAN** que podrían venir (módulo 68).
- **Garantías de producto/servicio**: lo que costará atender devoluciones o fallas.
- **Prestaciones sociales mal liquidadas** (módulo 52): un pasivo laboral subestimado.
- **Aportes a seguridad social atrasados** (UGPP, módulo 65).
- **Contratos onerosos**: arriendos o acuerdos que cuestan más de lo que aportan.
- **Impuestos del período no causados**: IVA o ICA pendientes no registrados.

## Cómo cazarlos en el cierre

1. Pide al **abogado** el listado de procesos en curso y su probabilidad.
2. Revisa **actas, contratos y correos** por compromisos asumidos.
3. Cruza la **nómina** y la seguridad social por subliquidaciones.
4. Revisa **requerimientos de la DIAN** o entidades.
5. Pregunta al dueño: "¿hay algo que me debas y no esté en los libros?"

## Ejemplo de provisión por litigio (cifras ILUSTRATIVAS / inventadas)

Un abogado estima que un juicio laboral se perderá (probable) por unos $8.000.000:

| Cuenta | Débito | Crédito |
|---|---|---|
| Gasto por litigios | 8.000.000 | |
| Provisión para contingencias | | 8.000.000 |

Si en cambio fuera solo "posible", NO se registra: se **revela en notas**. La estimación se documenta y el monto se **ejecuta/verifica en código** (a `Matematicas_lushows`).

## Errores comunes

- **No registrar ninguna provisión** "para que la utilidad se vea bien": engaña al dueño.
- **Provisionar todo** sin distinguir probable/posible/remoto: infla pasivos.
- **No revelar en notas** las contingencias posibles (faltan a la transparencia).
- **Olvidar pasivos laborales y de seguridad social**: los más frecuentes y caros.
- **Estimar el monto de cabeza** sin soporte ni código.

## Conexión con otros módulos

- **Módulo 36** — provisiones y estimaciones (mecánica).
- **Módulo 24** — notas a los estados financieros (donde se revela lo posible).
- **Módulo 68** — sanciones DIAN como contingencia tributaria.
- **Módulo 193** — al liquidar, los pasivos ocultos suelen aflorar.
- **Módulo 198** — el checklist de calidad debe preguntar por contingencias.
- **economist_lushows** valora el RIESGO; **contador** lo REGISTRA o REVELA.

## Siguiente paso típico

Incluye una pregunta explícita por contingencias en tu cierre y documenta cada una. Pásalo por el **módulo 198**. Esto NO reemplaza al contador ni al abogado titulados.

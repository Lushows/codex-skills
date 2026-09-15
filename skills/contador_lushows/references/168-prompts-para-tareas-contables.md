# 168 — Prompts para tareas contables

Un **prompt** es la instrucción que le das a una IA de texto (un LLM como Claude). La calidad de lo que recibes depende muchísimo de cómo pides: una orden vaga da una respuesta vaga (y peligrosa en contabilidad). Este módulo enseña a **pedir bien** tareas contables y, sobre todo, a **verificar** lo que la IA devuelve. Porque la IA suena segura incluso cuando se equivoca: la verificación no es opcional.

Regla de oro de la casa: **la IA redacta y organiza; no firma ni decide, y ningún número se cree sin verificarlo** en código (`Matematicas_lushows`) o contra la norma.

## La fórmula de un buen prompt contable

| Ingrediente | Ejemplo |
|---|---|
| **Rol** | "Actúa como contador colombiano bajo NIIF para pymes" |
| **Contexto** | "Empresa Grupo 3, restaurante, Régimen Simple" |
| **Tarea clara** | "Clasifica estos 5 gastos en cuentas del PUC" |
| **Datos** | (pega las facturas o el detalle) |
| **Formato** | "Devuélvelo en tabla: gasto, cuenta, código PUC" |
| **Límites** | "Si no estás seguro, dilo; no inventes códigos" |

## Para qué SÍ y para qué NO usar prompts

**SÍ (con revisión):** redactar un correo de cobro, resumir una norma, explicar un concepto, proponer la clasificación de un gasto, hacer un borrador de nota a los estados financieros, generar un checklist de cierre.

**NO (o solo como borrador a verificar):** calcular impuestos o retenciones "de cabeza" (eso a `Matematicas_lushows`), afirmar tarifas o plazos legales sin verificar la norma vigente, tomar la decisión final de un asiento dudoso, redactar algo que se firme sin revisión humana.

## Verificación: el paso obligatorio

1. **¿De dónde sacó esto?** Pide que cite la base (norma, dato que le diste).
2. **¿Los números cuadran?** Recálculos en código, no confíes en su aritmética.
3. **¿La norma es vigente?** La IA puede tener datos viejos (módulo 169).
4. **¿Inventó algo?** Códigos PUC, artículos o tarifas que "suenan bien" pueden ser falsos.

## Ejemplo (prompt rotulado — uso ILUSTRATIVO)

> "Actúa como contador colombiano (NIIF pymes, Grupo 3). Tengo este gasto: factura de Claro por $120.000 + IVA. Propón el asiento en tabla (cuenta, código PUC, débito, crédito). Si la tarifa de retención depende de un dato que no te di, **pregúntamelo, no lo asumas**."

La IA propone un borrador; el contador **verifica la retención con la norma vigente y el cuadre con `Matematicas_lushows`** antes de registrar. Prompt y cifras ilustrativos.

## Errores comunes

- **Pedir vago** ("ayúdame con la contabilidad") → respuesta inútil o inventada.
- **Creer las tarifas/plazos que da** sin verificar la norma: la IA alucina datos legales.
- **Dejar que calcule** y registrar ese número sin recálculo.
- **No pedirle que avise cuando no sabe**: sin ese límite, inventa con seguridad.
- **Pegar datos sensibles** sin saber dónde quedan (módulo 169).

## Conexión con otros módulos

- Las tareas que pides por prompt se ejecutan en **161** (leer), **163** (asientos), reportes y cierre.
- Lo **básico de IA y herramientas**: módulos **84–86**.
- Los **riesgos de alucinación y datos sensibles**: módulo **169**.
- Cualquier cálculo que pidas: verifícalo con `Matematicas_lushows`. *Optimizar costos de uso de IA*: `optimizer_tokens_lushows`.

## Siguiente paso típico

Arma una pequeña **biblioteca de prompts** para tus tareas repetidas (clasificar gastos, redactar cobros, resumir normas), cada uno con rol, contexto, formato y el límite "si no sabes, pregunta". Guárdalos y mejóralos con el uso. Y nunca registres un número de la IA sin recalcularlo.

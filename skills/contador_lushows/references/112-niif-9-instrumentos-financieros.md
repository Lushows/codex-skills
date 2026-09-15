# 112 — NIIF 9: Instrumentos financieros (cómo mides lo que te deben y lo que debes)

Un **instrumento financiero** es cualquier derecho a recibir efectivo (una cuenta por cobrar, un préstamo que diste, una inversión) o cualquier obligación de entregarlo (un préstamo que te dieron, un proveedor por pagar). NIIF 9 te dice **cómo clasificarlos** y **a qué valor mostrarlos** en el balance. En NIIF para pymes esto vive en las **Secciones 11 y 12**, también más sencillas que la norma plena.

La pregunta central: ¿lo mido al **costo amortizado** (lo que vale considerando el tiempo y los intereses) o al **valor razonable** (lo que valdría hoy en el mercado)? La respuesta depende de qué piensas hacer con ese activo y de cómo se comporta su flujo de caja.

Términos: **costo amortizado** = valor inicial ajustado por intereses devengados y pagos, usando la tasa de interés efectiva. **Valor razonable** = precio al que se vendería hoy entre partes informadas.

## Clasificación y medición (NIIF plenas)

| Categoría | ¿Cuándo? | Cómo se mide |
|---|---|---|
| Costo amortizado | El activo busca cobrar capital + intereses y lo conservas | Costo amortizado (tasa efectiva) |
| Valor razonable con cambios en ORI | Cobras flujos Y a veces vendes | Valor razonable; ganancia/pérdida a patrimonio (ORI) |
| Valor razonable con cambios en resultados | Para negociar / no cumple lo anterior | Valor razonable; ganancia/pérdida al estado de resultados |

ORI = Otro Resultado Integral (parte del patrimonio, no del resultado del periodo).

## En NIIF para pymes (Secciones 11 y 12)

La mayoría de instrumentos "básicos" (cuentas por cobrar/pagar, préstamos simples) se miden a **costo amortizado**. Solo los instrumentos complejos van a valor razonable. Para un negocio pequeño, casi todo es costo amortizado: tus clientes te deben, tú le debes a proveedores.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

GastroLatam le presta $10.000.000 a un aliado, a un año, con interés. La tasa de interés efectiva anual es, supongamos, 12% (el cálculo de la tasa efectiva y los intereses devengados lo hace `Matematicas_lushows`).

**Al otorgar el préstamo:**

| Cuenta | Débito | Crédito |
|---|---|---|
| Préstamo por cobrar (1325) | 10.000.000 | |
| Bancos (11) | | 10.000.000 |

**Al devengar intereses del primer trimestre** (10.000.000 × 12% × 3/12 = $300.000):

| Cuenta | Débito | Crédito |
|---|---|---|
| Intereses por cobrar (1345) | 300.000 | |
| Ingreso financiero (4210) | | 300.000 |

Esto es **costo amortizado**: reconoces el interés en el tiempo, aunque aún no te lo paguen.

## Deterioro: el modelo de pérdida esperada

NIIF 9 (plenas) exige reconocer **pérdida crediticia esperada** desde el primer día: estimas qué porcentaje probablemente no cobrarás y provisionas, sin esperar a que el cliente deje de pagar. Para cuentas por cobrar comerciales se usa una **matriz de provisiones** por antigüedad. (El detalle de deterioro de cartera se trata en módulo 113.)

## Errores comunes

- **Medir todo a valor razonable**: la mayoría de cuentas por cobrar/pagar de una pyme van a costo amortizado.
- **No devengar intereses** de préstamos que diste o recibiste: el ingreso/gasto financiero debe reconocerse en el tiempo.
- **Esperar a la mora para provisionar**: NIIF 9 pide pérdida esperada anticipada, no incurrida.
- **Confundir Grupo 1 y Grupo 2**: en pymes casi todo es costo amortizado; no compliques con categorías de plenas.

## Conexión con otros módulos

- **113 — Deterioro de activos**: la pérdida esperada de cartera es deterioro de un activo financiero.
- **Matematicas_lushows**: tasa de interés efectiva, valor presente, devengo de intereses.
- **20-29** (presentación): clasifica corriente vs no corriente según el plazo.
- **115 — Moneda extranjera**: si el instrumento está en dólares, además ajustas por diferencia en cambio.

## Siguiente paso típico

Lista tus cuentas por cobrar, préstamos e inversiones y clasifícalas: ¿las conservas para cobrar? Entonces costo amortizado. Luego define tu política de **pérdida esperada** sobre la cartera comercial y pasa a **113 — Deterioro de activos**.

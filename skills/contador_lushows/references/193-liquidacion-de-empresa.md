# 193 — Liquidación de una empresa

Cerrar una empresa no es simplemente "dejar de operar". Es un proceso ordenado, contable y tributario, en el que se venden los activos, se pagan las deudas en un orden definido por la ley, se reparte lo que sobre entre los socios y se cancelan los registros ante la Cámara de Comercio y la DIAN. Hacerlo bien evita que las deudas y obligaciones persigan a los socios después.

> **Liquidación** = proceso de extinguir una sociedad: se realizan (venden/cobran) los activos, se pagan los pasivos en orden de prelación, y el remanente se distribuye a los socios. La empresa deja de existir cuando se cancela su matrícula y RUT.

## Las dos etapas

| Etapa | Qué pasa |
|---|---|
| **Disolución** | Decisión (de los socios o por causal legal) de terminar la empresa. La sociedad sigue existiendo pero solo para liquidarse. Se nombra un **liquidador**. |
| **Liquidación** | Se realizan activos, se pagan pasivos en orden, se reparte el remanente y se cancelan registros. |

Desde la disolución, la empresa agrega a su nombre la expresión **"en liquidación"**.

## El balance final de liquidación

El corazón contable del proceso es el **balance final de liquidación**: una foto que muestra qué activos quedan, qué deudas hay y cuánto le toca a cada socio. Para llegar a él:

1. Se hace un **inventario** de activos y pasivos.
2. Se **valoran y realizan** los activos (vender, cobrar cartera).
3. Se pagan los pasivos en **orden de prelación de créditos** (la ley define qué se paga primero).
4. Lo que sobra se reparte entre los socios según su participación.

## Orden de prelación (idea general)

La ley colombiana establece un orden para pagar deudas en una liquidación. A grandes rasgos: primero **salarios y prestaciones** de trabajadores, luego **impuestos** (DIAN/territoriales), después **créditos con garantía**, y al final los **demás acreedores**. Los **socios** solo reciben si queda remanente después de pagar TODO. Verifica el orden exacto vigente; no es un cálculo de cabeza.

## Tributación de la liquidación

- Hay que presentar las **declaraciones del período fraccionado** (hasta la fecha de liquidación).
- La utilidad o ganancia por venta de activos puede generar **renta o ganancia ocasional**.
- El reparto a los socios puede tener efectos tributarios (dividendos / reembolso de aportes).
- Se debe **cancelar el RUT** y la **matrícula mercantil** (módulo 69) al final.

## Ejemplo de balance final (cifras ILUSTRATIVAS / inventadas)

| Concepto | Valor |
|---|---|
| Activos realizados (caja tras vender todo) | 120.000 |
| (−) Salarios y prestaciones pendientes | 20.000 |
| (−) Impuestos por pagar | 15.000 |
| (−) Proveedores | 35.000 |
| **= Remanente para socios** | **50.000** |

Si Ana tiene 60% y Beto 40%, Ana recibe 30.000 y Beto 20.000. Cada cifra se **ejecuta y verifica en código** (a `Matematicas_lushows`).

## Errores comunes

- **Repartir a los socios antes de pagar deudas**: ilegal y deja a los socios expuestos.
- **No respetar el orden de prelación** (pagar a un proveedor antes que salarios).
- **Olvidar las declaraciones del período final** y la cancelación del RUT.
- **No cancelar la matrícula mercantil**: la empresa "sigue viva" y acumulando obligaciones.
- **Calcular el remanente y el reparto de cabeza**.

## Conexión con otros módulos

- **Módulo 39** — patrimonio y aportes de los socios.
- **Módulo 69** — Cámara de Comercio: cancelación de matrícula.
- **Módulo 60** — DIAN/RUT: cancelación del RUT.
- **Bloque 4** — declaraciones del período fraccionado.
- **economist_lushows** DECIDE si conviene liquidar o vender; **contador** REGISTRA y CUMPLE el proceso.

## Siguiente paso típico

Antes de firmar el balance final, corre el **módulo 197** (contingencias y pasivos ocultos): muchos litigios y deudas olvidadas aparecen justo al liquidar. Esto NO reemplaza al contador y abogado titulados.

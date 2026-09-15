# 192 — Información exógena a fondo

La **información exógena** es el gran "chivato" de la DIAN: cada año los negocios deben reportarle, en archivos estructurados, con quién hicieron negocios y por cuánto (a quién le compraron, a quién le vendieron, a quién le pagaron salarios, quién les debe, etc.). La DIAN cruza esos reportes de TODOS los contribuyentes para detectar inconsistencias. El módulo 64 dio la visión básica; aquí entramos a fondo: formatos, topes, cruces y los errores que generan sanción.

> **Información exógena** (o medios magnéticos) = conjunto de reportes anuales en los que personas y empresas le informan a la DIAN sus operaciones con terceros, identificadas por NIT/cédula. Es la fuente con la que la DIAN "te conoce" antes de que declares.

## Por qué importa tanto

Porque la DIAN **cruza** lo que tú reportas con lo que reportan los demás. Si tu proveedor reporta que te vendió $50.000 y tú no reportas esa compra (o reportas otra cifra), salta una alerta. Y al revés: si reportas un gasto que nadie más reporta haberte facturado, también. La exógena es el insumo de las declaraciones **sugeridas** y de muchas fiscalizaciones.

## Formatos típicos (los más comunes)

Los formatos se identifican por número. Los nombres y números pueden ajustarse cada año — **verifica los del año** en la resolución vigente (módulo 199). A modo de mapa general:

| Tema del reporte | Qué informa |
|---|---|
| Pagos y abonos a terceros | A quién le pagaste y cuánto (compras, servicios, salarios) |
| Retenciones practicadas | Cuánta retención le practicaste a cada tercero |
| Retenciones que te practicaron | Cuánto te retuvieron a ti |
| IVA descontable / generado | El IVA de tus compras y ventas |
| Ingresos recibidos | Quién te pagó y cuánto |
| Cuentas por cobrar y por pagar | Saldos con cada tercero al cierre |
| Ingresos por terceros / socios | Aportes, dividendos, etc. |

## Topes: ¿estoy obligado?

No todos reportan. La obligación depende de **topes de ingresos o patrimonio** del año anterior, y dentro de cada reporte hay **cuantías mínimas** por tercero (debajo de cierto monto se agrupa en "cuantías menores"). Estos topes **cambian cada año** — nunca asumas los del año pasado; verifica el valor del año.

## Los cruces que hace la DIAN

1. **Compras vs. ventas**: tu compra debe aparecer como venta de tu proveedor.
2. **Retención practicada vs. soportada**: lo que retuviste debe coincidir con lo que el tercero declara que le retuvieron.
3. **IVA descontable vs. generado**: el IVA que descuentas debe haberlo cobrado alguien.
4. **Exógena vs. tu propia declaración**: lo reportado debe atar con renta, IVA y retención.

## Ejemplo de cruce que dispara alerta (cifras ILUSTRATIVAS / inventadas)

| Quién reporta | Operación | Valor reportado |
|---|---|---|
| Tú (comprador) | Compra a Proveedor X | 0 (no la reportaste) |
| Proveedor X (vendedor) | Venta a ti | 18.000 |

La DIAN ve $18.000 de un lado y $0 del otro → **requerimiento**. El cuadre y la suma de los reportes se verifican en código (a `Matematicas_lushows`), nunca de cabeza.

## Errores que generan sanción

- **No reportar estando obligado** o reportar fuera de plazo.
- **Reportar con NIT/cédula errados**: el cruce no engancha y se cuenta como error.
- **Cifras que no atan** con renta, IVA y retención del mismo año.
- **No reportar las "cuantías menores"** agrupadas cuando corresponde.
- **Asumir topes del año anterior** (módulo 199 avisa los cambios).
- La sanción por exógena puede ser **alta** (porcentaje de lo no reportado o mal reportado); ver módulo 68.

## Conexión con otros módulos

- **Módulo 64** — visión básica de exógena.
- **Módulo 68** — sanciones de la DIAN, incluidas las de exógena.
- **Módulos 41, 42, 43** — IVA, renta y retención que deben atar con lo reportado.
- **Módulo 199** — changelog que avisa cambios de formatos y topes.
- **contador** REPORTA y CUMPLE; **Matematicas_lushows** EJECUTA los totales.

## Siguiente paso típico

Antes de cargar la exógena, corre el **módulo 198** (checklist de calidad) para verificar que las cifras aten con tus declaraciones. Esto NO reemplaza al contador titulado.

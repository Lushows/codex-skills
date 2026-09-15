# 181 — México: SAT y CFDI

Este módulo da el **panorama de México**: cómo se organiza la contabilidad y los impuestos, qué es el SAT y qué es el CFDI (la factura electrónica más madura de la región). Es una **base sólida, no una guía completa**: las tasas, los umbrales y los formatos cambian, y este texto no los inventa. Antes de operar en México, **confirma con un contador público mexicano y con el SAT vigente**.

> SAT = Servicio de Administración Tributaria. Es el equivalente mexicano de la DIAN colombiana: recauda impuestos y administra las obligaciones fiscales.

## Las piezas clave

| Pieza | Qué es |
|---|---|
| SAT | Autoridad fiscal federal |
| RFC | Registro Federal de Contribuyentes (tu identificador fiscal, como el NIT) |
| CFDI | Comprobante Fiscal Digital por Internet (la factura electrónica) |
| IVA | Impuesto al Valor Agregado sobre ventas |
| ISR | Impuesto Sobre la Renta (utilidades de personas y empresas) |
| e.firma / CSD | Firma digital y sello para emitir CFDI |

## CFDI: la factura electrónica

El **CFDI** es el corazón del sistema mexicano. Cada venta, nómina, pago y retención se documenta con un CFDI validado por un **PAC** (Proveedor Autorizado de Certificación) que lo "timbra" en nombre del SAT. Hay distintos tipos de CFDI: ingreso (ventas), egreso (notas de crédito), nómina, pago y traslado. Versiones recientes exigen catálogos muy detallados (uso del CFDI, régimen fiscal, código postal). Es estricto: un dato mal puesto rechaza el timbrado.

## Impuestos principales (conceptos, no tasas)

| Impuesto | Sobre qué | Periodicidad típica |
|---|---|---|
| IVA | Ventas de bienes/servicios | Mensual |
| ISR | Utilidades / ingresos | Pagos provisionales + anual |
| Retenciones | Pagos a terceros, nómina | Según operación |

> No cites tasas de memoria. Verifica IVA, ISR y regímenes vigentes con el SAT.

## Regímenes

México tiene varios regímenes según el tipo y tamaño de contribuyente (por ejemplo regímenes simplificados para personas físicas con actividad empresarial, y el régimen general para personas morales/empresas). Elegir el régimen correcto cambia cuánto pagas y cómo declaras. Esta decisión la valida el contador local.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)

Una tienda colombiana abre operación en México y vende un producto en $1.000 MXN antes de IVA. Su contador mexicano:

1. Registra la venta con un **CFDI de ingreso** timbrado por un PAC.
2. Calcula el IVA aplicable (**la tasa la confirma con el SAT**, no se inventa aquí).
3. Acumula el ingreso para sus pagos provisionales de ISR.

Todo cálculo monetario se ejecuta y verifica (se rutea a `Matematicas_lushows`); nunca de cabeza.

## Errores comunes

- **Emitir CFDI con datos mal capturados** (régimen, uso del CFDI, código postal): el SAT lo rechaza.
- **Confundir CFDI con factura simple de PDF.** El valor legal está en el timbrado del PAC.
- **Elegir mal el régimen fiscal.** Afecta impuestos y obligaciones; lo decide el contador local.
- **Asumir tasas de IVA/ISR.** Cambian; verifica con el SAT.

## Conexión con otros módulos

- **180**: panorama general de LatAm donde encaja México.
- **184–186**: otros países de la región (Perú, Chile, Ecuador).
- **188**: tributación internacional si la empresa opera en México y otro país.
- **189**: checklist de apertura para entrar a México ordenadamente.
- **40–69 (núcleo Colombia)**: el equivalente de factura electrónica e impuestos en Colombia.

## Siguiente paso típico

Contrata un contador público mexicano, tramita el **RFC** y la **e.firma/CSD**, y elige tu régimen. Luego conecta tu sistema a un **PAC** para emitir CFDI. Usa el checklist del módulo 189.

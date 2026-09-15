# 85 — OCR de facturas: lectura automática, validación y errores típicos

**OCR** significa *Optical Character Recognition* (reconocimiento óptico de caracteres): la tecnología que convierte una **imagen o PDF** de una factura en **datos** que el computador entiende (fecha, NIT, valor, IVA). En lugar de digitar a mano cada factura del proveedor, le tomas una foto o subes el PDF y el sistema extrae los campos. Hoy el OCR moderno usa IA, lo que lo hace mucho más preciso que hace unos años.

Este módulo explica cómo funciona en la práctica, **cómo validar** lo que extrae (porque no es perfecto) y los errores que más se repiten. El OCR avanzado de frontera 2026 vive en **160–169**; aquí lo aterrizamos al uso diario.

> **El OCR extrae; el humano confirma.** Una cifra leída mal entra a la contabilidad como verdad. Por eso toda factura capturada por OCR pasa por una validación antes de registrarse. Cuadre, cumplimiento, auditable — y nunca un valor sin verificar.

## Términos que debes conocer
- **OCR:** lectura automática de texto en imágenes/PDF.
- **Campo extraído:** cada dato que el OCR saca (NIT, fecha, subtotal, IVA, total).
- **Confianza (score):** qué tan seguro está el OCR de cada dato (alto = confiable, bajo = revisar).
- **Factura electrónica vs. de papel:** la electrónica ya viene en formato de datos (XML) y casi no necesita OCR; el OCR brilla con facturas en **papel, foto o PDF escaneado**.

## Para qué sirve y cómo se usa
1. **Capturas** la factura: foto con el celular, PDF o escaneo.
2. El OCR **extrae** los campos clave (proveedor, NIT, fecha, subtotal, IVA, total, número de factura).
3. El sistema **propone** la cuenta del PUC y arma un borrador de asiento.
4. Tú **validas** y apruebas → se registra (control humano).

## Cómo validar lo que extrae el OCR
| Campo | Qué revisar |
|---|---|
| **Total** | Que coincida con el papel y que **subtotal + IVA = total** |
| **IVA** | Que el porcentaje y el valor cuadren con la base |
| **NIT** | Que el proveedor sea el correcto (los OCR confunden dígitos: 0/O, 1/7) |
| **Fecha** | Que caiga en el periodo correcto (un mes mal asignado descuadra el cierre) |
| **Número de factura** | Que no esté repetida (duplicados) |

Una buena práctica: revisar al 100% las facturas **de mayor valor** y por **muestra** las pequeñas; y siempre las de **confianza baja**.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
El OCR lee una factura y reporta: subtotal $1.000.000, IVA $190.000, total $1.190.000. Al validar, todo cuadra (`subtotal + IVA = total`). En otra factura, el OCR leyó el NIT "900.123.456" como "900.123.450" → el contador lo corrige antes de registrar, porque ese NIT alimenta luego la información exógena ante la DIAN. (Cifras inventadas; el `subtotal + IVA = total` se confirma en `Matematicas_lushows`.)

## Errores típicos del OCR
- **Confundir dígitos** parecidos en NIT o valores (0↔O, 1↔7, 5↔6).
- **Leer mal el separador** de miles/decimales → un total inflado o reducido.
- **Tomar la fecha equivocada** (fecha de impresión vs. fecha de la factura).
- **No detectar el IVA** cuando viene en una línea rara → descuadra base e impuesto.
- **Duplicar** una factura si se sube dos veces → gasto doble.
- Facturas **borrosas, torcidas o arrugadas** → baja la confianza y sube el error.

## Buenas prácticas
- Captura con **buena luz y la factura plana**; mejor foto, mejor lectura.
- Prefiere la **factura electrónica (XML)** cuando exista: no necesita OCR y es exacta.
- Configura **alertas de duplicados** (mismo NIT + número + valor).
- Guarda la **imagen original** como soporte (ver 87): el OCR no reemplaza el documento, lo acompaña.

## Errores comunes (del usuario)
- Aprobar en masa sin revisar las de confianza baja → entran cifras erradas.
- Borrar la factura física/PDF confiando solo en el dato extraído → te quedas sin soporte.
- Usar OCR para facturas electrónicas que ya traen XML (trabajo doble y menos exacto).
- No revisar la fecha → gastos cargados al mes equivocado descuadran el cierre.

## Conexión con otros módulos
- **84 (IA en contabilidad)** — el marco de qué puede y qué no la IA.
- **160–169** — OCR avanzado y agentes a fondo 2026.
- **86 (bot WhatsApp)** — capturar facturas por chat (foto al bot → OCR → contabilidad).
- **45 (facturación electrónica)** — cuando hay XML, se prefiere al OCR.
- **89 (plantillas)** y **12 (asientos)** — el registro del gasto validado.
- **Matematicas_lushows** — todo `base + IVA = total` se verifica allá.

## Siguiente paso típico
Si el negocio quiere que los gastos lleguen solos desde el celular, ver cómo un bot de WhatsApp captura facturas: abrir **86 (integración con el bot WhatsApp)**.

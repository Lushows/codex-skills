# 296 · Facturación electrónica LatAm: DIAN, SAT, SUNAT

> Cobrar ≠ facturar. El pago lo procesa Wompi/Stripe; la **factura fiscal legal** la valida el gobierno.
> En LatAm la factura electrónica es obligatoria y rechazada por el fisco si el XML está mal. No es opcional.

## El concepto: el Estado valida ANTES de que la factura exista
A diferencia de USA/EU (factura = PDF que mandas), en LatAm el documento solo es válido cuando la autoridad
tributaria (o un proveedor autorizado por ella) lo **firma/timbra/aprueba**. Sin ese sello, la venta no tiene
soporte fiscal. Por eso integras un **PAC/Proveedor Tecnológico**, no generas un PDF y ya.

## Colombia — DIAN (Factura Electrónica de Venta)
- Documento: **XML UBL 2.1** con **CUFE** (código único) y firma digital, validado por la DIAN, más representación gráfica (PDF) con **QR**.
- Quién lo emite: tu **software propio habilitado**, un **Proveedor Tecnológico** habilitado por DIAN, o el **software gratuito de la DIAN**.
- Para un SaaS/tienda: integras un PT (proveedor tecnológico) que abstrae el XML+firma+envío. Ellos exponen API REST: mandas JSON → devuelven CUFE + XML aprobado + PDF.
- Ecosistema relacionado: **RADIAN** (registro de facturas como título valor), nota crédito/débito, documento soporte.
- **2026**: ampliación de obligados y cambios en RADIAN [no verificado — confirma calendario DIAN].

## México — SAT (CFDI 4.0)
- Documento: **CFDI 4.0** (único formato válido desde abr-2023, único aceptado por el SAT desde 2023).
- Pieza clave: el **PAC** (Proveedor Autorizado de Certificación). **Sin que el PAC haga el timbrado, el CFDI no tiene validez fiscal.** Tú generas el CFDI → PAC lo timbra (sella con el SAT) → devuelve el XML con timbre + UUID.
- Requiere **e.firma** y **CSD** (Certificado de Sello Digital) del emisor.
- API típica (gigstack, Facturama, Enlace Fiscal): mandas JSON con conceptos/receptor → la API valida, genera y timbra en una llamada HTTP, oculta la complejidad del XML.
- **2026**: desde **1-may-2026** plataformas tecnológicas deben dar al SAT acceso online permanente a su info fiscal/operativa; desde **24-abr-2026** suplemento de hidrocarburos en CFDI de combustibles [verificado, [no verificado] el detalle de alcance].

## Perú — SUNAT
- Documento: comprobante electrónico (**Factura/Boleta**) en XML UBL 2.1, firmado, validado vía **OSE** (Operador de Servicios Electrónicos) o el **PSE/SEE-SOL** de SUNAT.
- La **CDR** (Constancia de Recepción) de SUNAT es la prueba de aceptación. Sin CDR conforme, no es válido.

## Tabla comparativa

| País | Autoridad | Formato | Intermediario obligatorio | Sello/ID único |
|---|---|---|---|---|
| Colombia | **DIAN** | XML UBL 2.1 | Proveedor Tecnológico (o SW gratis DIAN) | **CUFE** |
| México | **SAT** | **CFDI 4.0** | **PAC** (timbrado) | **UUID** (folio fiscal) |
| Perú | **SUNAT** | XML UBL 2.1 | OSE / SEE | **CDR** |

## Patrón de integración (vale para los tres)
1. **Pago confirmado** (webhook Wompi/MP/Stripe flipea orden a `paid`). Cruza con [[295-pagos-latam-wompi-mercadopago]].
2. Disparas la **emisión** al proveedor: POST JSON con emisor, receptor (NIT/RFC/RUC), conceptos, impuestos, total.
3. El proveedor **firma/timbra/valida** ante la autoridad → devuelve XML aprobado + ID único + PDF/QR.
4. **Guardas el XML** (es el documento legal, no el PDF) y se lo entregas al cliente (email/WhatsApp).
5. **Manejas rechazos**: la autoridad puede rechazar (RFC inexistente, totales que no cuadran, fuera de plazo). Reintenta/corrige; un rechazo no resuelto = venta sin soporte fiscal.

## Gotchas
1. **El XML es el documento legal, no el PDF** — archívalo (años, según país). El PDF es solo representación.
2. **Impuestos deben cuadrar al centavo** con el cálculo de la autoridad — redondeo mal hecho = rechazo. Calcula IVA/IGV sobre base correcta y respeta los decimales del esquema.
3. **Datos del receptor obligatorios y validados** — CFDI 4.0 exige nombre/razón social EXACTO + régimen fiscal + uso del CFDI; RFC mal = rechazo. DIAN valida NIT.
4. **Folios/plazos** — hay ventanas de tiempo para emitir tras la venta; emitir tarde es sanción.
5. **No reinventes el XML** — usa un PAC/PT/OSE. El esquema cambia, las firmas son criptográficas, y un error te bloquea la operación. La API del proveedor es la abstracción correcta.
6. **Notas crédito/débito** — devoluciones y correcciones también son documentos electrónicos, no un simple `UPDATE` en tu DB.

Cruza con [[295-pagos-latam-wompi-mercadopago]] (el pago previo) y [[42-pagos-latam]].

**Fuentes:** dian.gov.co/facturaelectronica · sat.gob.mx (CFDI 4.0) · sunat.gob.pe · gigstack.pro · facturama.mx (jun-2026).

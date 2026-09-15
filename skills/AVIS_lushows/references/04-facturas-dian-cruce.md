# 04 · Facturas: DIAN, lectura y cruce

## Las tres vías de lectura (router: `src/lib/facturaIngesta.ts` → `procesarAdjunto`)
1. **XML / ZIP de la DIAN → 100% exacto, sin IA.** El ZIP suele traer XML+PDF; el XML manda.
2. **PDF → visión IA** (Gemini, `gemini-2.5-flash`, `inlineData` con `application/pdf`).
3. **Foto/imagen → visión IA.**
Siempre se prefiere el XML. Cada factura sabe su `fuente`: `"xml"` (exacta ✅) o `"vision"`.

## Factura electrónica DIAN (XML UBL 2.1) — `src/lib/facturaXML.ts`
- Es **XML UBL 2.1** con **CUFE** (código único) y firma digital. El archivo real suele ser un
  **`AttachedDocument`** que lleva la `<Invoice>` verdadera **embebida en CDATA** (hay que
  desenvolverla y re-parsear). A veces hay un **segundo CDATA anidado** con el `ApplicationResponse`
  de validación DIAN — NO confundirlo con la factura.
- Campos: proveedor (`AccountingSupplierParty` → PartyTaxScheme/PartyName/PartyLegalEntity
  RegistrationName), NIT (`CompanyID`), número (`cbc:ID` de la **Invoice**, no del contenedor),
  fecha (`IssueDate`), CUFE (`cbc:UUID`), moneda, subtotal (`LegalMonetaryTotal/LineExtensionAmount`),
  total (`PayableAmount`/`TaxInclusiveAmount`), **IVA = suma de `cac:TaxTotal/cbc:TaxAmount` a nivel
  documento** (¡no sumar los TaxTotal por línea → doble conteo!), ítems (`InvoiceLine`).
- Lib: `fast-xml-parser` (removeNSPrefix + parseTagValue:false), `fflate` para ZIP. Validado contra
  factura real (PLASTIZIPAC→Bendita Pola): 10/10 checks.
- **Gotcha de encoding:** algunos emisores guardan el XML con tildes/ñ mal codificadas ("PAÃO"); es del
  emisor, no del parser; afecta solo texto descriptivo.

## Validación — `validarFactura()` en `src/lib/factura.ts`
Cuadra `subtotal + IVA ≈ total` (tolerancia max($50, 1%)). Si no cuadra → advertencia "los números no
cuadran". También marca faltantes (total/proveedor/fecha). `fuente='xml'` → `confianza=1`; visión `0.85`.

## Categoría de gasto con IA — `categorizarFactura()`
El XML DIAN **no trae categoría de gasto** → AVIS la clasifica con Gemini (texto, barato) en:
`insumos · mercancia · aseo_limpieza · servicios · arriendo · nomina · transporte · otros`. Se aplica
cuando la factura no trae categoría (XML/ZIP). La visión ya la asigna en su prompt.

## El CRUCE (no contar doble) — `src/lib/cruce.ts`
Al guardar una factura se compara con las recientes del comercio:
- **Candidato:** total dentro de tolerancia (±max($50,1%)).
- **Proveedor:** NIT igual (fuerte) o nombre normalizado equivalente.
- **Fecha:** ±10 días (si falta alguna, no bloquea).
- **ALTA confianza** (NIT+total exacto, o proveedor+total exacto+fecha cercana) → se marca la NO
  canónica `duplicado_de`; **la electrónica (xml) siempre es la canónica**, la foto queda duplicada y
  **NO se suma**. AVIS avisa: "🔗 Ya tenías esta compra — la uní para no contar doble".
- **MEDIA** → `posible_duplicado_de` (sí cuenta, se marca "Posible dup." en el panel; sin preguntar).
- No re-cruza lo ya marcado. Verificado con mock 6/6 casos.
Es 100% automático (decisión Lushows: el comercio no organiza nada; cada admin manda y se empata sola).

## Atribución multi-admin — `resolverComercioPorTelefono()` en `documentos.ts`
Una foto/factura de cualquier número resuelve el comercio por `comercios.whatsapp_phone` **o**
`miembros.whatsapp_phone` (estado activo) → guarda `punto_id` en `datos`. Así cada sede alimenta la
contabilidad sola.

## Almacenamiento y reporte
- Storage Supabase bucket `documentos`; fila en tabla `documentos` con `datos` (jsonb) y `origen`
  (`whatsapp`|`correo`). Estado/cruce/conexión viven en jsonb (sin migraciones extra).
- `src/lib/facturasData.ts` `cargarReporteFacturas`: excluye `duplicado_de` de totales/lista, cuenta
  `cruzadas`, marca `posibleDuplicado`. Export CSV: `/api/facturas/export` (sep `;` + BOM, Excel es-CO).

## Buzón por correo (Resend Inbound) — `src/lib/facturaInbound.ts`
Webhook `email.received` (`/api/facturas/inbound?key=<secreto>`) → re-pide el correo a la API de Resend
(no confía en el body) → resuelve el comercio por el destinatario `facturas-<token>@…` → si es el correo
de confirmación de reenvío de Gmail (`forwarding-noreply@google.com`) captura el código y lo manda por
WhatsApp; si trae adjuntos, los baja (download_url), los procesa, marca "conectado" la 1ª vez y confirma.
SDK: `resend.emails.receiving.get(id)` + `resend.emails.receiving.attachments.get({emailId,id})`.

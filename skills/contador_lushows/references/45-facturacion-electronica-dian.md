# 45 — Facturación electrónica DIAN

La **factura electrónica** es la factura oficial en Colombia: un documento digital (formato XML) que, antes de ser válido, debe ser **validado por la DIAN**. Ya no basta con un talonario de papel: la DIAN "ve" la factura casi en tiempo real. Para el contador esto es clave porque **la factura es el soporte de casi todo**: del IVA generado, del costo/gasto deducible en renta, del IVA descontable. Sin factura válida, esos valores se caen en una auditoría.

Este módulo explica el sistema. **No inventamos plazos ni topes de obligatoriedad:** quién y cuándo está obligado cambia con la normativa. *Verifica el calendario y la obligatoriedad vigente para tu actividad en la DIAN.*

## Conceptos clave
- **Factura electrónica de venta:** la que emites cuando vendes a alguien obligado a exigir factura.
- **Validación previa:** la DIAN **valida la factura antes** de que surta efectos. Una factura no validada no es válida.
- **CUFE:** Código Único de Factura Electrónica — la "huella digital" que identifica cada factura validada.
- **Documento soporte:** cuando le compras a alguien que **NO está obligado a facturar** (p. ej. ciertos proveedores), tú generas un "documento soporte" para poder deducir ese costo/gasto.
- **Documento equivalente / POS:** el tiquete de máquina registradora (POS) es un documento equivalente, pero **tiene límites** (por ejemplo, por encima de cierto monto el cliente puede exigir factura electrónica). *Verifica el tope vigente.*
- **Nómina electrónica:** un documento electrónico aparte para soportar los pagos de salarios (ver módulos de nómina).
- **RADIAN:** el registro de facturas electrónicas como **título valor** (sirve para negociarlas/financiarlas).

## Cómo llega una factura a ser válida
```
1. Emites la factura en tu software / proveedor tecnológico autorizado
2. Se genera el XML con el CUFE
3. Se envía a la DIAN para VALIDACIÓN PREVIA
4. La DIAN la valida → la factura ya es válida y se entrega al cliente
5. Se conserva el XML (es el original; el PDF es solo representación gráfica)
```

## Para el contador: por qué importa tanto
- **IVA generado** → sale de tus facturas de venta.
- **IVA descontable y costos deducibles** → necesitan **factura o documento soporte válido**. Una compra sin soporte electrónico válido **no se puede descontar** (te suben el impuesto).
- **Conservación:** se debe guardar el **XML** (no solo el PDF) por el término que la ley exija. Esto es parte de estar **AUDIT-READY**.

## Ejemplo (cifras ILUSTRATIVAS / inventadas)
Le compras mercancía a un proveedor por $3.000.000 + IVA:
- Si el proveedor **te emite factura electrónica válida (con CUFE)** → puedes tomar el costo y el IVA descontable.
- Si te da solo un recibo informal → **no es soporte válido**: pierdes el descontable y el gasto puede rechazarse. La solución: exigir factura o, si el proveedor no está obligado, generar tú el **documento soporte**.

> Caso ilustrativo. El impacto en el IVA/renta se liquida en **41/42** con **Matematicas_lushows**.

## Errores comunes
- Guardar solo el **PDF** y no el **XML** (el XML es el documento real).
- Aceptar compras **sin soporte electrónico** y luego intentar deducirlas.
- Pasarse del tope del **POS** y no emitir factura electrónica cuando correspondía.
- No generar **documento soporte** al comprarle a no obligados a facturar.
- Asumir que "como soy pequeño no me obliga": la obligatoriedad se ha ido ampliando — **verifica tu caso**.

## Conexión con otros módulos
- **41 (IVA)** — la factura soporta el IVA generado y descontable.
- **42 (Renta)** — sin factura/soporte, el costo o gasto **no es deducible**.
- **43 (Retención)** — el valor a retener parte del documento.
- **47 (Presentación)** y **49 (Sanciones)** — facturar mal o no facturar tiene sanciones.
- Módulos de **nómina** — la nómina electrónica es otro documento DIAN.

## Siguiente paso típico
Confirmar que el negocio emite factura electrónica válida (proveedor tecnológico o software propio habilitado), que conserva los **XML** y que exige soporte válido a sus proveedores. Solo con eso bien atado se puede liquidar IVA y renta con confianza.

---

## Habilitación paso a paso — Solución Gratuita DIAN (vigente 2026, verificar en portal)

> ⚠️ La habilitación **NO se hace por el menú "Factura Electrónica" de MUISCA** (ese suele dar
> error 500 / "página en construcción"). Va por el **portal de facturación electrónica**:
> ambiente de **habilitación** `catalogo-vpfe-hab.dian.gov.co/User/Login` y producción
> `catalogo-vpfe.dian.gov.co`. La numeración sí se pide en MUISCA. *(URLs y pasos: verificar vigentes
> en el micrositio DIAN — micrositios.dian.gov.co/sistema-de-facturacion-electronica.)*

**Fase 1 — Registro y habilitación (gratis):**
1. Entrar a `catalogo-vpfe-hab.dian.gov.co/User/Login` → elegir empresa, escribir el **NIT** → llega
   un **TOKEN** al correo registrado en el RUT → autenticarse.
2. Menú **Registro y habilitación → Documentos electrónicos → Factura electrónica**.
3. En **modo de operación** elegir **"Software Gratuito DIAN"** (en vez de proveedor tecnológico).
4. Solicitar el **certificado de firma digital GRATUITO** (Configuración → Certificados).
5. Realizar el **SET DE PRUEBAS** (obligatorio para quedar "Habilitado"): **2 facturas electrónicas
   de venta + 1 nota crédito + 1 nota débito**. Es el paso más importante.
6. Al pasar el set → estado **"Habilitado"** → seleccionar la **fecha de inicio**.

**Fase 2 — Numeración y emisión:**
7. Solicitar el **rango de numeración** en **MUISCA** (Numeración de Facturación → **Autorización de
   numeración**). Para factura electrónica el rango suele iniciar con prefijo y un consecutivo;
   *verificar el rango/condiciones vigentes.*
8. **Asociar** el prefijo/rango en el portal de producción `catalogo-vpfe.dian.gov.co`.
9. **Emitir** las facturas reales desde el portal de producción (o desde el software del proveedor si
   luego se migra a uno).

**Plazo (CONFIRMAR con contador titulado — la norma cambió):** Resolución 000165 de 2023. Para
**inscritos nuevos en el Régimen Simple** que no venían obligados, la referencia es **~2 meses desde
el registro en el RST**; pero la norma empuja a que, al **constituir sociedad o hacer la primera
venta**, ya se facture electrónicamente (en algunas lecturas **sin** los 2 meses de gracia). Lectura
segura: **habilitarse cuanto antes, idealmente antes de la primera factura.** *(Verificar el caso
concreto con contador titulado y el calendario DIAN vigente.)*

**Costo:** $0 con la Solución Gratuita DIAN (incluido el certificado de firma). Un **proveedor
tecnológico** (Alegra, Siigo, Factus, APIDIAN…) solo se justifica por **volumen o integración por
API** (emitir desde otro software/el propio producto), no para empezar.

**Errores/atajos comunes:** intentar habilitarse por el menú de MUISCA (da 500) en vez del portal
`catalogo-vpfe`; confundir el ambiente de **habilitación** (`-hab`) con **producción**; olvidar pedir
la **numeración** en MUISCA antes de emitir; o registrar la habilitación a la **cédula** del rep legal
en vez de al **NIT** de la empresa.

## Documento soporte en adquisiciones a NO obligados a facturar (jun-2026)
Cuando le compras a alguien que **no está obligado a expedir factura** (una persona natural informal,
un proveedor pequeño), **el COMPRADOR debe generar el soporte** para poder **deducir el costo/gasto**
y descontar IVA. Base: **Resolución DIAN 000167 de 2021** (documento soporte electrónico) + Art.
1.6.1.4.12 DUR 1625/2016.
- **Debe ser ELECTRÓNICO** (con **numeración** autorizada por la DIAN y **CUDS** = código único de
  documento soporte), transmitido a la DIAN — igual de exigente que la factura electrónica. Requiere
  estar **habilitado** (mismo flujo del portal `catalogo-vpfe`).
- **Campos:** fecha; datos del **adquiriente** (tu negocio, NIT); datos del **vendedor/tercero**
  (nombre o razón social + **NIT/cédula** + dirección); descripción/concepto; valor; **retenciones**
  que practiques (renta/IVA/ICA si aplican); numeración + CUDS.
- **Periodicidad:** uno por operación, o **acumulado semanal** por el mismo proveedor (lo permite la
  norma).
- ⚠️ **Sin documento soporte ELECTRÓNICO, el gasto NO es deducible** (para obligados a facturar
  electrónicamente). Un comprobante de egreso/recibo en papel sirve de **soporte interno y orden**,
  pero NO reemplaza el documento soporte electrónico para efectos de deducción.
- **Pago de "turno"/servicio a una persona:** si NO es empleado, es un servicio → documento soporte
  (y **retención** si supera la base) o cuenta de cobro del tercero; si es relación laboral real, va
  por **nómina electrónica** (no documento soporte). Definir bien empleado vs contratista (ver `59`).
- **AVISPA'O (producto):** hoy AVIS guarda la foto y arma el **comprobante de egreso/documento soporte
  en borrador** con todos los campos y memoria del tercero — soporte interno válido para orden. El
  **documento soporte electrónico** (numeración + CUDS) se emite cuando el negocio esté habilitado.

# 64 — Facturación electrónica

Cómo entender, cumplir y aprovechar la facturación electrónica sin que te tome por sorpresa ni te cueste multas. Es el "lenguaje oficial" con el que tu negocio le habla al fisco: si vendes en regla, tarde o temprano la necesitas.

> **Antes de cualquier cifra o trámite de este módulo: pregunta país y ciudad.** Las reglas, plazos, umbrales y proveedores cambian por país (y a veces por región). Aquí te doy el método universal y ejemplos ilustrativos; los datos vigentes los confirmas con la fuente oficial (ver 21 para cómo investigar el dato real).

## Qué es (en lenguaje simple)

Una **factura electrónica** es un comprobante de venta en formato digital estandarizado (normalmente un archivo XML) que el Estado **valida o registra** en tiempo casi real, le asigna un código único y obliga a guardarlo. No es "un PDF que mandas por correo": el PDF es solo la representación visual. Lo que vale fiscalmente es el archivo electrónico autorizado.

Términos que vas a oír (defínelos para ti):
- **Autoridad tributaria**: el organismo que cobra impuestos. Ejemplos de nombre: DIAN (Colombia), SAT (México), SII (Chile), AFIP/ARCA (Argentina), SUNAT (Perú), SRI (Ecuador). *Verifica el nombre vigente en tu país.*
- **PAC / Proveedor tecnológico autorizado**: empresa habilitada para emitir/validar tus facturas ante el fisco. En muchos países pasas por uno; en otros usas un portal gratuito del propio Estado.
- **CUFE / folio fiscal / CAE / timbre**: el código único que prueba que la factura fue autorizada. El nombre cambia por país.
- **Certificado / firma digital**: tu "sello electrónico" que garantiza que la factura la emitiste tú y no fue alterada.

## Por qué es (cada vez más) obligatoria

- Reduce la evasión: el Estado ve las ventas en tiempo real.
- Es **requisito para deducir gastos**: tus clientes empresa necesitan tu factura electrónica para descontar el gasto y el impuesto (ver 63 sobre IVA y deducciones). Si no la emites, te dejan de comprar.
- Suele ser **condición para vender a empresas grandes, al gobierno o exportar**.
- En varios países ya **no es opcional** por encima de cierto tamaño o tipo de actividad, y el umbral baja cada año. La tendencia mundial es clara: todos hacia electrónico.

**Implicación honesta:** aunque hoy no estés obligado, prepararte temprano evita un apagón de ventas el día que te obliguen. Y muchos clientes ya te la exigen aunque la ley aún no.

## Qué implica para tu negocio (lo que cambia en el día a día)

| Necesitas | Para qué |
|---|---|
| Estar formalizado / inscrito ante el fisco | No puedes facturar sin existir fiscalmente (ver 62, formalización; ver 63, impuestos) |
| Certificado o firma digital | Autorizar y "firmar" cada factura |
| Una herramienta de emisión (software, portal estatal o PAC) | Generar el XML y enviarlo a validar |
| Un correlativo/numeración autorizada | El fisco suele asignarte rangos de numeración |
| Guardar las facturas X años | Obligación de conservación (el plazo varía por país: confírmalo) |
| Emitir notas crédito/débito electrónicas | Para anular o corregir ventas |

No es solo tecnología: es un **proceso**. Cada venta gatilla una factura; cada devolución, una nota crédito.

## Cómo cumplir — método universal en 6 pasos

1. **Confirma si estás obligado y desde cuándo.** Busca en el sitio oficial del fisco de tu país tu tipo de contribuyente y umbral. Si dudas, una asesoría contable de 1 hora aclara todo (ver 60, cuándo pagar un profesional).
2. **Formalízate primero.** Sin inscripción tributaria no hay facturación electrónica (ver 62).
3. **Consigue el certificado/firma digital.** Trámite ante el fisco o entidad certificadora autorizada. Suele tener costo y vigencia anual.
4. **Elige el "cómo emites":**
   - **Portal gratuito del Estado** (cuando existe): cero costo de software, pero manual y lento. Sirve si facturas poco.
   - **Software de facturación / PAC** (de pago): se integra con tu punto de venta o tienda online, automático. Vale la pena con volumen.
   - **Tu propio sistema integrado por API**: solo si tienes equipo técnico que lo conecte a tu punto de venta o tienda.
5. **Haz pruebas en ambiente de homologación.** Casi todos los fiscos exigen pasar un set de pruebas antes de emitir en real. No saltes este paso.
6. **Emite, valida, entrega y archiva.** Cada factura: se genera → se valida ante el fisco → se entrega al cliente (XML + PDF) → se guarda.

## Cómo elegir proveedor (checklist)

- [ ] ¿Está **autorizado** por el fisco de tu país? (no asumas; verifica en la lista oficial)
- [ ] ¿Se integra con cómo vendes hoy (tienda física, e-commerce, WhatsApp)?
- [ ] ¿Cobra por factura, por plan mensual o por volumen? Calcula tu costo real anual.
- [ ] ¿Incluye notas crédito/débito y soporte en tu idioma?
- [ ] ¿Te deja exportar tus datos si te cambias de proveedor?

## Ejemplo numérico (ilustrativo — cifras inventadas)

> Cifras de demostración, NO datos reales de ningún país. Reemplázalas por las cotizaciones que consigas.

Negocio pequeño que emite **120 facturas/mes**. Compara dos rutas:

| Concepto | Portal estatal gratis | Software/PAC de pago |
|---|---|---|
| Costo software / mes | $0 | $25 |
| Tiempo por factura | 6 min | 30 seg |
| Tiempo total / mes | 12 h | 1 h |
| Si tu hora vale $8 | $96 en tu tiempo | $8 en tu tiempo |
| **Costo total mensual** | **$96** | **$33** |

Lectura: el "gratis" cuesta $96/mes en tu tiempo; el software de $25 te deja en $33 y te libera 11 horas. **A partir de cierto volumen, pagar es más barato que la opción gratis.** Calcula tu propio punto con tus números reales (ver 53 para razonar costos y punto de equilibrio).

## Errores comunes

- **Creer que "mandar un PDF" es facturar electrónicamente.** Lo válido es el XML autorizado por el fisco.
- **Dejar el certificado vencer.** Si caduca, dejas de poder emitir y paras ventas. Pon recordatorio de renovación.
- **No emitir notas crédito al devolver/anular.** Una venta mal anulada deja impuesto que igual tendrás que pagar.
- **No guardar los XML.** El PDF no basta en una auditoría; necesitas el archivo original por los años que exija tu país.
- **Elegir un proveedor no autorizado** porque era más barato: las facturas pueden quedar inválidas.
- **Asumir reglas de otro país.** Lo que vale en México (CFDI/SAT) no es idéntico a Colombia (DIAN) ni a Chile (SII). Siempre confirma local.

## Señales de que ya deberías actuar

- Un cliente te pidió "factura con datos fiscales" y no supiste dárla.
- Vas a venderle a una empresa, al gobierno o a exportar.
- Tu volumen pasó el umbral de tu país (confírmalo en el sitio oficial).
- Estás formalizando el negocio ahora mismo (hazlo en el mismo trámite; ver 62).

## Siguiente paso típico

Confirma país/ciudad y entra al sitio oficial del fisco para verificar si ya estás obligado y desde cuándo. Si vas a formalizar, integra la facturación electrónica en ese mismo proceso (ver 62) y, si el volumen o las dudas pesan, agenda 1 hora con un contador local (ver 60) antes de elegir proveedor.

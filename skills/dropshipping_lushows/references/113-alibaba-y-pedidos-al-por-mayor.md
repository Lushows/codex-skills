# Alibaba y pedidos al por mayor

> Vigencia: septiembre 2026. Verifica términos de Trade Assurance directamente en la plataforma.

Alibaba.com es el B2B internacional. Es donde haces tu **primer pedido serio con tu marca**. Está en
inglés, acepta transferencia y tiene escrow. Es el canal más cómodo para el que no tiene agente — y
por eso también donde más te cobran de más.

## La verdad sobre quién te está vendiendo

De cada 10 "manufacturers" en Alibaba.com, aproximadamente 6 son **trading companies**: comerciales
que subcontratan a la fábrica y te cargan 15-35%. Eso no es siempre malo —una buena trading company
gestiona múltiples fábricas, resuelve problemas y te da MOQ menor— pero debes saber con quién hablas
para negociar bien. Ver `120`.

Señales de trading company:

| Señal | Peso |
|---|---|
| Catálogo con categorías sin relación (cocina + electrónica + mascotas) | Alta |
| Ubicación no coincide con el clúster del producto. Ver `110` | Alta |
| Responden en inglés perfecto, muy rápido, con brochures bonitos | Media |
| No pueden mandar video de la línea de producción **hoy** | Alta |
| Esquivan la pregunta "¿cuál es su capacidad mensual de este SKU?" | Alta |
| Tienen licencia comercial sin alcance de fabricación | Definitiva |

Pídele siempre la **licencia comercial (营业执照)** y mira el campo de alcance (经营范围). Si dice
solo comercio y no producción, es trading company.

## Los sellos de Alibaba y qué valen realmente

| Sello | Qué garantiza | Qué NO garantiza |
|---|---|---|
| **Gold Supplier** | Que pagó la membresía | Nada de calidad |
| **Verified Supplier** | Inspección por tercero (SGS/TÜV/BV) de instalaciones | Que tu producto salga bien |
| **Trade Assurance** | Escrow: retiene el pago hasta que cumplan plazo/calidad pactados | Cubre solo lo que quedó **escrito en la orden** |
| Años en la plataforma | Antigüedad real. **Busca 5+ años** | — |
| Transaction Level / volumen | Actividad real en la plataforma | — |

**Trade Assurance es tu mejor herramienta y casi nadie la usa bien.** Solo cubre lo que está escrito
en la orden. Si no escribes "color Pantone 7686 C, tolerancia ±2 mm, empaque en caja individual
impresa", no puedes reclamarlo. Ver `144`.

## Procedimiento: del primer contacto al pedido pagado

1. **Busca el producto** y abre 8-10 proveedores. No 3: ocho.
2. **Manda el mismo mensaje a los 10** (plantilla en `119`). Quien responde en <24 h laborables con
   respuesta específica queda; el resto se cae solo.
3. **Filtra a 4** por calidad de respuesta, no por precio.
4. **Pide cotización formal** con desglose: precio EXW/FOB, MOQ, lead time, peso y medidas de caja
   máster, unidades por caja, certificaciones. Ver `121`.
5. **Pide muestras a 3.** Paga el courier. Ver `124`.
6. **Evalúa muestras** contra una lista escrita antes de recibirlas.
7. **Negocia** con el ganador y el segundo a la vez. Ver `118`.
8. **Emite la Proforma Invoice (PI)** y revísala línea por línea.
9. **Paga 30% depósito** vía Trade Assurance. Nunca fuera de la plataforma en el primer pedido. Ver `140`.
10. **Inspección antes del saldo.** Ver `123`.
11. **Paga el 70%** contra reporte de inspección aprobado y copia del BL/AWB.

El paso 11 es innegociable: **el saldo se paga después de inspeccionar, no antes de embarcar.**

## Lo que debe decir la Proforma Invoice

| Campo | Por qué importa |
|---|---|
| Descripción exacta con código de producto y variantes | Base de cualquier reclamo |
| Cantidad por variante | Evita "te mandé 300 pero todos negros" |
| Precio unitario e Incoterm (EXW/FOB/DDP) | Cambia quién paga qué. Ver `121` |
| Moneda | USD casi siempre; fija si hay conversión |
| Lead time en **días hábiles desde pago del depósito** | "30 días" sin referencia no sirve |
| Especificación técnica: material, gramaje, medidas, tolerancia | Lo que reclamas en QC |
| Empaque: unidad, master carton, medidas, peso bruto/neto | Base del flete. Ver `121` |
| Marcado de cajas (shipping marks) | Tu 3PL lo necesita |
| Condición de pago (30/70) y método | Ver `140` |
| Criterio de inspección y AQL | Ver `123` |
| Puerto de salida | Verifica que sea real y conveniente |
| Validez de la cotización | 15-30 días típico |

## MOQ en Alibaba: lo publicado no es lo real

El MOQ publicado es una barrera anti-curiosos. En la práctica:

| Situación | MOQ real esperable |
|---|---|
| Producto de stock, sin personalizar | 30-50% del publicado |
| Producto con tu logo impreso | El publicado, o el mínimo del proveedor de empaque |
| Producto con molde nuevo | El publicado + costo de molde (US$300-3.000) |
| Temporada baja de la fábrica | Hasta 20-30% del publicado |

Cómo bajarlo sin quemar la relación: ver `122`.

## Costos que no aparecen en la cotización

| Concepto | Rango típico |
|---|---|
| Muestras + courier | US$30-150 |
| Molde/herramental (si personalizas forma) | US$300-3.000, único |
| Plancha/cliché de impresión de empaque | US$30-150 por color |
| Inspección de tercero | US$150-350 por hombre-día |
| Flete internacional | Ver `121` y datos de tránsito |
| Despacho aduanero + agente de aduana | Varía; invoca `contador_lushows` |
| Arancel + IVA | Ver `13`, `16`, `17` |
| Almacenaje 3PL de entrada | Ver `134` |

**Regla:** el precio unitario de la cotización suele ser el 55-70% del costo puesto en tu bodega.
Si haces el modelo financiero con el precio FOB, el negocio va a dar 30% mejor de lo que da.
Para el cálculo exacto invoca `Matematicas_lushows`.

## Errores frecuentes

| Error | Realidad |
|---|---|
| Elegir por el precio más bajo de los 10 | El más barato suele ser el que recortó material |
| Aceptar pago fuera de Trade Assurance por "descuento" | Es la estafa #1. Ver `141` |
| Pagar 100% por adelantado | Solo con proveedor probado y monto chico |
| No pedir muestra "porque ya vi el video" | El video es de otra fábrica |
| Confiar en que "producción 25 días" incluye enero-febrero | El ANC lo rompe todo. Ver `139` |
| Pedir DDP sin entender qué cubre | El DDP chino a veces usa canales grises. Ver `121`, `141` |

## Para el proyecto activo (México, diciembre 2026)

Alibaba **no es para diciembre**. El lead time (muestras 2 semanas + producción 25-35 días + tránsito
marítimo 30-45 días) te pone en marzo de 2027. Para diciembre es stock local mexicano.

Si el bundle funciona, el pedido a Alibaba se planifica para **noviembre de 2026** si quieres
mercadería antes del Año Nuevo Chino del 6 de febrero de 2027. Ver `139`.

## Relacionados
Ver `110`, `112`, `118`, `119`, `120`, `121`, `122`, `123`, `124`, `140`, `141`, `144`.

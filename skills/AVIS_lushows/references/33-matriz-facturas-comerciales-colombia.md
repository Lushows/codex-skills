# 33 · Matriz de facturas comerciales de Colombia (2026) — blindaje del lector

> Referencia para que el lector de facturas (foto/PDF y XML DIAN) reconcilie SIEMPRE sin falsas
> alarmas y sin contar doble. Investigada 2026. Marcas: ✅ verificado con fuente · ⚠️ (por confirmar
> valor exacto) · 🧮 afecta la aritmética. Código real: `src/lib/factura.ts` (visión + validación) y
> `src/lib/facturaXML.ts` (XML). Fix base desplegado jul-2026 (caso OXXO: IVA incluido + descuento).

## Anclas legales 2026 (verificadas)
- UVT 2026 = **$52.374** (Res. DIAN 000238/2025).
- Impuesto bolsas plásticas 2026 = **$73/bolsa** (Circular DIAN 000005/2025).
- ICUI (ultraprocesados) = **20%** (se mantiene). IBUA = tarifa por 100 ml indexada a UVT (Res. 000247/2025; pesos exactos ⚠️).

## La fórmula que SIEMPRE cuadra (no la ingenua)
```
BASE (TaxExclusiveAmount) = Σ neto_de_línea − descuentos_documento + cargos_gravables
IMPUESTOS = Σ IVA_por_tarifa + INC + indirectos (bolsa, IBUA, ICUI…)
TOTAL (PayableAmount) = BASE + IMPUESTOS − descuentos_no_gravables + cargos_no_gravables (propina, bolsa)
                        ± redondeo_al_peso − anticipos (PrepaidAmount)
```
🧮 **Las retenciones (retefuente/reteIVA/reteICA) NO se restan del total de la factura** — son menor
valor del **pago**, las calcula el comprador. Restarlas rompe el cuadre (aunque algunas facturas sí
muestran el total ya neto → el validador debe aceptar ambas).

## Por tipo de comercio (lo que rompe la lectura)
- **Descuento duro (D1, Ara, Ísimo):** precio **IVA incluido**; IVA discriminado al pie (base = precio/1,19);
  tiquete POS frecuente (no CUFE); redondeo. 🧮 No volver a sumar el IVA del pie.
- **Conveniencia (OXXO, Listo):** IVA incluido; `*DESCUENTO`/`TU AHORRO FUE` (informativo, no restar 2 veces);
  `IGRVD` = indicador de tarifa por línea ⚠️.
- **Supermercados (Éxito, Carulla, Olímpica, Jumbo, Makro):** **multi-IVA (0/5/19)** en un ticket + **impuesto
  de bolsa $73 aparte que SUMA** + promos "ahorro". IBUA/ICUI ya vienen **dentro** del precio (no línea).
- **Restaurantes/bares:** **INC 8% (no IVA)** que suma al final; **propina 10% voluntaria** que suma DESPUÉS
  (el total real puede ser sin propina); franquicias pagan IVA 19%; SIMPLE no cobra INC. 🧮 Propina no es
  impuesto; INC ≠ IVA descontable.
- **Droguerías:** medicamentos **excluidos** (≠ exento) mezclados con cosmético 19% → multi-tarifa.
- **Gasolineras:** precio **todo incluido** (sobretasa 25% gasolina/6% ACPM + impuesto específico dentro).
  No des-incluir IVA 19%.
- **Retail (Falabella, Homecenter, Alkosto):** IVA incluido; descuentos por medio de pago; **cuotas ≠ total**
  (capturar PayableAmount de contado); garantía extendida = línea 19% aparte.
- **Servicios públicos/telecom (EPM, Enel, Vanti, Claro…):** NO son compra de bienes → **ruta por conceptos**
  (subsidios restan, contribuciones/reconexión/mora suman). No tratar como inventario.

## XML UBL 2.1 (rarezas que TODO parser maneja)
- **AttachedDocument + CDATA anidado:** el `Invoice` real va embebido como texto; desenvolver y re-parsear.
  (Ya lo hacemos, profundidad 4.)
- **ApplicationResponse embebido:** acuse DIAN en otro CDATA; ignorar para montos.
- **TaxTotal línea vs documento:** 🧮 usar **solo el de documento** para el impuesto total (sumar ambos = doble).
- **AllowanceCharge (`ChargeIndicator` false=descuento, true=cargo)** a nivel línea (ya en LineExtension) y
  documento (`AllowanceTotalAmount`/`ChargeTotalAmount`). No mezclar.
- **`LegalMonetaryTotal`** es la verdad: `LineExtensionAmount`, `TaxExclusiveAmount`(base), `TaxInclusiveAmount`,
  `AllowanceTotalAmount`, `ChargeTotalAmount`, `PrepaidAmount`, **`PayableAmount`**, `PayableRoundingAmount`.
  `PayableAmount = TaxInclusive − Allowance + Charge − Prepaid + Rounding`.
- **Notas crédito/débito:** root distinto (`CreditNote` resta / `DebitNote` suma); enlazar `BillingReference`.
- **CUFE/CUDE** = clave de idempotencia anti-duplicado. Encoding tildes/ñ del emisor (normalizar NFC).

## Impuestos/cargos (¿incluido o aparte? ¿suma/resta?)
- **Incluido en el precio:** IVA/INC retail y restaurante-precio-final, IBUA, ICUI, impoconsumo licores, combustibles.
- **Línea aparte que SUMA:** impuesto de bolsa ($73), INC restaurante (cuando se discrimina), propina (10%, opcional).
- **Informativo que NO cambia el total de la factura:** retenciones (retefuente/reteIVA/reteICA).
- **Excluido ≠ exento (0%):** el excluido no genera IVA descontable.

## Tolerancias (evitar falsas alarmas)
- Redondeo: **±$50 por documento** (o ±max(base×0,05%, $50)). Foto/OCR: **±1% o ±$200** (el mayor). XML: ±$1–2.
- Por tarifa de IVA: IVA_calculado ≈ base × tarifa, ±$50 por grupo.
- Semáforo: verde (XML cuadra) · amarillo (foto cuadra en tolerancia / falta 1 campo) · rojo (descuadre) →
  **solo el rojo alerta** al cliente.

## Reglas anti-error (implementadas / a implementar)
1. IVA incluido: si Σ(línea) ≈ total y hay IVA al pie → ya está dentro, no sumar. ✅ (fix OXXO)
2. Anti doble-descuento: descuento va en línea **o** en documento, nunca ambos; "AHORRO/PROMO" es informativo. ✅ prompt
3. Propina: excedente ~10% en restaurante = propina opcional, no exigir cuadre con impuestos. ⏳
4. INC ≠ IVA en restaurantes (etiquetar bien). ✅ desglose
5. Nota crédito → negativos, restar. ✅ XML (tipo)
6. Retención informativa: no altera total de factura (aceptar total con y sin retención). ✅ validación
7. AIU: IVA solo sobre la Utilidad → IVA ≪ 19% de la base no es error. ✅ prompt + validación (no falsa alarma)
8. Todo incluido (combustibles/licores): no des-incluir IVA. ✅ prompt
9. Idempotencia por CUFE/CUDE. ✅ cruce
10. Servicios públicos/telecom → recibo por conceptos: no se fuerza el cuadre subtotal+IVA (subsidios restan,
    contribuciones/reconexión/mora suman); ancla = total a pagar + vencimiento. ✅ validación (categoria=servicio_publico) + prompt

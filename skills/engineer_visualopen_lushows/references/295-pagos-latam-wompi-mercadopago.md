# 295 · Pagos LatAm a fondo: Wompi, MercadoPago, PSE, Nequi, Pix

> Stripe no cobra bien en Colombia/Argentina/Perú. El dinero local vive en PSE, Nequi, Pix y contra-entrega.
> Integrar mal = reconciliación a mano y ventas perdidas por no tener el método que el cliente usa.

## Wompi (gateway de Bancolombia, default Colombia)
Flujo: pides **`acceptance_token`** de `GET /merchants/{public_key}`, luego `POST /transactions` con `amount_in_cents` (COP, **enteros**), `currency:"COP"`, `customer_email`, `reference` **única** (= tu `order_id`), `payment_method`. Verifica el **checksum/firma del webhook** (SHA256 de campos + secret de eventos).

Rails: **PSE** (`financial_institution_code`, `user_type`, `user_legal_id_type/_id` — redirige al banco), **Nequi** (celular 10 dígitos, push a la app), **Bancolombia Transfer**, **tarjetas** (tokeniza 1 vez → payment source para recurrente).

**Tarifas (verificado jun-2026, [no verificado]):** Plan Avanzado tarjeta ≈ **2.65% + $700 + IVA**; PSE ≈ **2.69% + IVA**; Nequi/Bancolombia ≈ **1.5% + IVA**. Plan **Gateway** = Wompi no cobra comisión, solo pagas lo negociado con el banco por cada método (conviene a alto volumen).

## MercadoPago (gateway dominante regional)
- **Checkout Pro** (hosteado): `POST` crea una **`preference`** → rediriges a `init_point`. Más simple, menos PCI.
- **Checkout API / Bricks**: campos embebidos, más control.
- **Webhooks** con header **`x-signature`**: separa `ts` y `v1`, reconstruye el template `id:<data.id>;request-id:<x-request-id>;ts:<ts>;`, HMAC-SHA256 con tu secret, compara contra `v1`. Manda **`X-Idempotency-Key`** en los POST.
- Notifica en cada cambio: Pending / Approved / Rejected / Refunded. **Comisiones CO 2026** varían por método y plazo de liberación del dinero (más caro si quieres el dinero inmediato) [no verificado — confirma en panel].

## Pix (Brasil) — el rail que cambió todo
Instantáneo del Banco Central, 24/7, **QR / copia-e-cola**, settle en segundos, costo casi nulo. Integra vía **EBANX / dLocal / MercadoPago**. **Pix Automático** habilita recurrente (subscripciones sin tarjeta). Es el método #1 en BR; si vendes allá, es obligatorio.

## Cross-border (dLocal / EBANX)
Cobras en USD/EUR pero recaudas en moneda local: **dLocal** y **EBANX** agregan 200+ métodos locales con **una sola API** + FX + settlement. dLocal es PISP certificado en Brasil (Pix in-app sin redirect). Úsalos cuando vendes a varios países LatAm y no quieres N integraciones.

## Contra-entrega (COD) — enorme en Colombia
No hay API: es una **state machine** que tú modelas.
```
pending → confirmed → shipped → collected (paid)
                              ↘ returned (no-show)
```
Reconcilia el efectivo vía reportes del courier (Servientrega, Coordinadora, TCC). Mitiga fraude/no-show con: verificación de dirección, depósito parcial por link de pago, y scoring de zonas con alta devolución.

## Comparativa de rails (Colombia)

| Método | Tipo | Settlement | Recurrente | Fricción usuario |
|---|---|---|---|---|
| Tarjeta | push | T+N días | sí (token) | baja |
| **PSE** | redirect banco | ~inmediato/T+1 | no nativo | media (login banco) |
| **Nequi** | push app | inmediato | limitado | baja |
| **COD** | efectivo | al entregar | no | nula (pero no-show) |

## Flujo checkout WhatsApp-commerce (el patrón Lushows)
Carrito en chat → genera **payment link** (link Wompi, MP `init_point`, o Payment Link de Stripe si BR/MX) → cliente paga en browser → **webhook** flipea la orden a `paid` → el bot confirma. Mantén `reference = order_id` para reconciliación trivial. Cruza con [[41-whatsapp-cloud-api]].

## Gotchas
1. **Amounts enteros en centavos** (COP/BRL/MXN) — float = rechazo off-by-one. COP no tiene decimales reales pero la API usa `amount_in_cents`.
2. **Firma de webhook necesita body crudo** — middleware JSON que re-serialice rompe el HMAC (Wompi, MP, igual que Stripe).
3. **Idempotencia obligatoria** — todos reintentan; dedupe por `transaction.id`/`payment.id` + unique constraint.
4. **Webhook no es la verdad final** — haz `GET` del pago por id antes de despachar (spoof / fuera de orden).
5. **PSE puede quedar "pending" largo** — el usuario abandona el flujo del banco; ten timeout y estado `pending` visible, no asumas fallo inmediato.
6. **PCI SAQ-A** — nunca toques PAN crudo; usa hosted checkout/tokenización siempre.

Cruza con [[42-pagos-latam]] (base), [[294-stripe-a-fondo]] (global) y [[296-facturacion-electronica-latam]] (la factura legal después del pago).

**Fuentes:** docs.wompi.co · mercadopago.com.co/developers · dlocal.com · docs.ebanx.com · bcb.gov.br/pix (jun-2026).

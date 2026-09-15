# 67 — Email transaccional & deliverability

Email transaccional (confirmaciones, reset password, recibos) y marketing deben separarse en **subdominios y/o IPs
distintas** para no contaminar reputación. Una queja de marketing nunca debe degradar la entrega de un "reset password".

## Proveedores (cuándo cada uno)
- **Resend** — DX moderna, SDK TS de primera, React Email nativo. Free 3.000/mes. Mejor para stacks React/Next <~100k/mes.
- **Postmark** — máxima deliverability transaccional (~98.6%), separa streams transaccional vs broadcast. Cuando un email perdido = transacción perdida.
- **AWS SES** — el más barato a escala ($0.10/1.000), pero tú construyes templates, bounce/complaint (vía SNS), warmup. Pragmático >200k/mes con ingeniería.
- **SendGrid** — transaccional + marketing en una plataforma. **Loops** — orientado SaaS, lifecycle + visual.

## Autenticación (obligatoria 2024+)
- **SPF** (`TXT`): autoriza servidores. `v=spf1 include:_spf.resend.com ~all`. **Límite duro 10 lookups DNS.**
- **DKIM** (`TXT`/`CNAME`): firma criptográfica. El proveedor da el selector (`resend._domainkey`).
- **DMARC** (`TXT` en `_dmarc.dominio`): política si SPF/DKIM fallan **alineación**. `v=DMARC1; p=quarantine; rua=mailto:dmarc@dominio; pct=100`. Empieza en `p=none` → `quarantine` → `reject`.

## Requisitos Gmail/Yahoo bulk-sender (>5.000/día a Gmail, vigentes feb-2024, rechazos definitivos nov-2025)
1. SPF **Y** DKIM; al menos uno alineado con el dominio del `From`. 2. DMARC mínimo `p=none`. 3. **One-click
unsubscribe** (RFC 8058: `List-Unsubscribe` + `List-Unsubscribe-Post`) en marketing. 4. Spam rate en Postmaster Tools **<0.30%** (idealmente <0.1%).

## Deliverability operativa
Warmup gradual de IP/dominio. IP dedicada solo con volumen alto/constante (>50-100k/mes); por debajo, IP compartida
del proveedor = mejor reputación. List hygiene: elimina hard bounces ya, suprime quejas. Spam triggers: ratio texto/
imagen, URLs acortadas, palabras "gratis/$$$", falta de versión texto plano. **Templates:** **MJML** o **React Email** (el estándar moderno JS).
```tsx
import { Resend } from 'resend';
await new Resend(KEY).emails.send({ from:'Addrian <hola@mail.bioseta.co>', to:cliente.email,
  subject:'Tu pedido BIO-SETA va en camino', react:<PedidoEnviado pedido={p}/> });
```
**Webhooks** (delivered/bounced/complained/opened): valida firma HMAC, procesa idempotente, actualiza suppression list.

## Gotchas
1. SPF >10 lookups DNS → `permerror` → fallos silenciosos. Usa flattening/macros del proveedor.
2. Cambiar `From` a subdominio sin re-configurar DKIM rompe la alineación DMARC aunque DKIM "pase".
3. `~all` (softfail) vs `-all` (hardfail) — empieza con `~all` hasta validar todo.
4. Mezclar transaccional y marketing en el mismo subdominio: una campaña con quejas tumba tus recibos.
5. No procesar bounces/complaints → SES suspende la cuenta (bounce >5%, complaint >0.1%).
6. Webhooks no idempotentes: reintentos duplican efectos (doble suppression, doble email).

**Fuentes:** support.google.com/a/answer/81126 · dmarcian.com (Gmail/Yahoo DMARC) · superfa.st/blog (Resend vs Postmark vs SendGrid 2026).

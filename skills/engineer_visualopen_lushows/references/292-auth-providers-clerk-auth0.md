# 292 · Auth providers: Clerk / Auth0 / Supabase / WorkOS / Better-Auth

> Auth no es "login con Google". Es sesiones, MFA, SSO empresarial, multi-tenant y el día que un cliente
> grande pide SAML. Elegir mal te encierra en un pricing que escala con cada usuario o cada conexión.

## El eje de decisión: ¿quién paga, por qué unidad?
Dos modelos de cobro que definen todo:
- **Por MAU** (Clerk, Auth0, Supabase): pagas por usuario activo/mes. Bueno para B2C con muchos usuarios baratos; explota en B2B (clientes con cientos de empleados x $/MAU).
- **Por conexión** (WorkOS): pagas por cada SSO/SCIM enterprise, no por usuario. Predecible en B2B (alineado al # de clientes empresa, no a su headcount).

Si vendes a empresas, el modelo por conexión casi siempre gana en costo total.

## Tabla comparativa (precios verificados jun-2026, [no verificado] = sujeto a cambio)

| Provider | Free tier | Pago base | Overage / unidad | SSO empresarial | Self-host |
|---|---|---|---|---|---|
| **Clerk** | 10k MAU | Pro $25/mes (incl. 10k MAU) | $0.02/MAU extra | desde Pro (SAML/OIDC) | no |
| **Auth0** | 7,500 MAU | Essentials $35 · Pro $240/mes | ~$0.07/MAU | B2B Pro $800/mes, **cap 5 conexiones** | no |
| **WorkOS AuthKit** | **1M MAU** (auth gratis) | $0 hasta 1M | SSO $125/conexión (→$50 a 200+) | núcleo del producto | no |
| **Supabase Auth** | 50k MAU (incl. plan) | Pro $25/mes | ~$0.00325/MAU | add-on enterprise | **sí** (GoTrue OSS) |
| **Better-Auth** | gratis (OSS) | infra propia | $0 (tú hospedas) | plugins SSO/SAML | **sí, full** |

Notas que muerden: Auth0 escala exponencial pasado el tier base, y su cap de 5 conexiones SSO en B2B Pro fuerza contrato Enterprise ($10k+/mes [no verificado]) al sexto cliente empresa. Clerk a 50k MAU ≈ $1,025/mes a tarifa de lista.

## Cuándo cada uno
- **Clerk** — B2C/SaaS indie que quiere UI de auth lista (componentes `<SignIn/>`, org switcher) y DX rápida en Next.js. Pagas comodidad.
- **Auth0** — empresa con requisitos de compliance pesados, Actions/Rules complejas, ecosistema legado. Caro pero maduro.
- **WorkOS** — B2B que va a vender enterprise SSO/SCIM pronto. AuthKit gratis hasta 1M cubre el B2C, cobras solo las conexiones enterprise reales.
- **Supabase Auth** — ya usas Postgres de Supabase; auth viene integrado con **RLS** (la fila sabe quién eres vía `auth.uid()`). Cruza con [[293-rbac-permissions-multitenant]].
- **Better-Auth** — quieres control total, cero vendor lock-in, TypeScript end-to-end, hospedas tú. Sin factura por MAU, pero tú operas la seguridad.

## Features que de verdad pesan al elegir
- **MFA / passkeys**: todos los managed lo traen; Better-Auth vía plugin (TOTP/WebAuthn). Cruza con [[273-auth-oauth-oidc-passkeys-sessions]].
- **SAML/OIDC enterprise**: WorkOS y Auth0 maduros; Clerk desde Pro; Supabase/Better-Auth requieren más armado.
- **SCIM** (provisioning automático de usuarios desde el IdP del cliente): WorkOS lo cobra por directorio; pocos lo traen out-of-box. Es lo que pide un cliente enterprise grande tras el SSO.
- **Sesiones**: managed dan rotación de refresh tokens y revocación; con Better-Auth controlas el store (DB/Redis) y la política tú.
- **Componentes UI**: Clerk gana en DX (drop-in `<SignIn/>`, `<OrganizationSwitcher/>`); Auth0 trae Universal Login hosteado; WorkOS AuthKit es drop-in; Better-Auth es headless.

## Multi-tenant: el patrón que importa
Una **organización** es el tenant. El usuario pertenece a 1+ orgs con un rol por org. Clerk y WorkOS modelan orgs nativamente (invitaciones, roles, dominios verificados → auto-join por email corporativo). Con Better-Auth/Supabase lo modelas tú: tabla `organizations`, `memberships(user_id, org_id, role)`, y el `org_id` activo viaja en el JWT/sesión. **Regla de oro:** el tenant_id debe estar firmado en el token, nunca venir del body del request (spoofeable). Cruza con [[338-multitenancy-patterns]].

## Gotchas
1. **Migración de usuarios es dolorosa** — los hashes de password son del provider; salir de Auth0/Clerk implica re-hash on-login o export negociado. Evalúa lock-in ANTES.
2. **MAU se cuenta distinto** — un usuario que entra 1 vez al mes cuenta igual que uno diario. Audita tu definición real de "activo".
3. **El JWT no es la verdad de permisos** — lleva identidad y org, pero RBAC fino se chequea server-side (claims viejos en tokens no expirados).
4. **Webhooks de user lifecycle** (user.created/deleted) — sincroniza tu DB; si no, tu tabla `users` se desfasa del provider.

## Recomendación rápida (sesgo Lushows)
- **Indie / B2C / MVP veloz** → Clerk (DX) o Supabase Auth (si ya usas su Postgres).
- **B2B que venderá enterprise SSO** → WorkOS (AuthKit gratis + cobras solo conexiones).
- **Cero lock-in / TypeScript / hospedo yo** → Better-Auth.
- **Compliance pesado, presupuesto holgado** → Auth0.

Cruza con [[273-auth-oauth-oidc-passkeys-sessions]] (protocolos), [[293-rbac-permissions-multitenant]] (qué puede hacer cada quién) y [[63-multi-tenancy-billing-saas]].

**Fuentes:** clerk.com/pricing · auth0.com/pricing · workos.com/pricing · supabase.com/pricing · better-auth.com (jun-2026).

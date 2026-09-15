# 06 · Arquitectura y operación de AVISPA'O

> Proyecto en `C:\Users\user\Desktop\AVISPAO`. Repo **GitHub Lushows/avispao** (main → auto-deploy
> Vercel). Web **avispao.app**. Para profundidad técnica general, ver `engineer_visualopen_lushows`.

## Stack
- **Next.js 16** (App Router) + React 19 + TypeScript + **Tailwind v4** (@theme tokens) + Turbopack.
- **Supabase** (proyecto `wnqpkstsggxkiyqgbhip`, São Paulo): Auth (Google OAuth + magic link),
  Postgres, Storage. Cliente admin service-role.
- **Gemini** `@google/genai`, modelo `gemini-2.5-flash` (`src/lib/gemini.ts`, con reintentos 503).
- **WhatsApp Cloud API** (Meta) — número de PRUEBA por ahora; token permanente (System User).
- **Resend** (email): envío `hola@avispao.app` (dominio verificado) + Inbound (buzón de facturas).
- **Bold** (pagos COP): link de pago + webhook.
- Deploy **Vercel** (auto desde main; **cambiar env var requiere Redeploy**).

## Archivos clave (`src/lib/`)
- `gemini.ts` (gen+reintentos) · `avis.ts` (persona `AVIS_SYSTEM`) · `catalogo.ts` (19 obligaciones
  verificadas) · `conversacion.ts` (orquestador: prospecto→`flujoVenta`, cliente→`flujoCliente`) ·
  `venta.ts` (cerebro vendedor) · `onboarding.ts` (legacy, ya no se rutea para prospectos) ·
  `delegacion.ts` (equipo/puntos, plantilla `avis_saludo`) · `generadorDocs.ts` (genera documentos) ·
  `factura.ts` (lectura visión + tipo `FacturaDatos` + `validarFactura` + `categorizarFactura` +
  `resumenWhatsApp`) · `facturaXML.ts` (parser DIAN) · `facturaIngesta.ts` (router de adjuntos) ·
  `facturaInbound.ts` (webhook correo) · `facturaToken.ts` (buzón por comercio) · `cruce.ts` (dedup) ·
  `conexion.ts` (estado de conexión en `onboarding_state.facturas`) · `documentos.ts`
  (`guardarFactura`/`guardarDocumento`/`resolverComercioPorTelefono`) · `facturasData.ts` (reporte) ·
  `suscripcion.ts` (`iniciarCobro`/`activarCobro` + bienvenida) · `bold.ts` · `resend.ts` (marketing) ·
  `sesion.ts` (enlace mágico HMAC, `urlMagica(id, next?)`) · `whatsapp.ts`
  (`sendWhatsAppText`/`sendWhatsAppTemplate`) · `panelData.ts` (carga el panel) · `fechas.ts`.
- Rutas: `/api/whatsapp` (webhook WA) · `/api/facturas/inbound` (correo) · `/api/facturas/export`
  (CSV) · `/api/bold/webhook` (pago) · `/api/auth/magico` (enlace mágico) · `/api/cron/recordatorios`.
- Panel `src/app/panel/` (inicio, papeles, **facturas**, conectar, equipo). Admin `src/app/admin/`
  (cabina, blog, clientes, suscriptores, factura/[id]). Landing `landing.html` + `public/landing.html`
  (sincronizar SIEMPRE las dos; menú hamburguesa en móvil). PDF/OG con chrome `--headless=new`.

## Tablas Supabase (clave)
`comercios` (whatsapp_phone, nombre_negocio, tipo_negocio, ciudad, esta_registrado, num_empleados,
pone_musica, maneja_alimentos, plan, **factura_token**, **onboarding_state jsonb**) · `miembros` ·
`puntos` · `documentos` (storage_path, tipo_mime, **datos jsonb**, **origen**) · `documentos_generados`
· `cobros` · `posts` (blog) · `perfiles`. Estado de conexión/cruce/gmail vive en jsonb → sin migrar.

## Env vars (Vercel)
`NEXT_PUBLIC_SUPABASE_URL`/`ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY`, `GEMINI_API_KEY`, `GEMINI_MODEL`,
`WHATSAPP_PHONE_NUMBER_ID`/`ACCESS_TOKEN`/`VERIFY_TOKEN`, `NEXT_PUBLIC_APP_URL=https://avispao.app`,
`RESEND_API_KEY`, `RESEND_INBOUND_SECRET`, `FACTURAS_DOMAIN`, **`BOLD_IDENTITY_KEY`** + **`BOLD_SECRET_KEY`**
(⚠️ si faltan, el link de pago NO se genera), `BOLD_PLAN_AMOUNT`. Opcional `WA_FACTURA_TEMPLATE`.

## Lecciones / trampas ya pagadas (no repetir)
- **Cobro:** sin `BOLD_IDENTITY_KEY`/`BOLD_SECRET_KEY` el cobro falla → AVIS cae a "sistema de pagos
  ocupado". Es config, no bug. Ponerlas en Vercel para cerrar el cobro.
- **"Ya pagué" ≠ pagar una obligación:** tras activar el plan, AVIS da bienvenida (webhook +
  atajo) — no pide comprobante.
- **Resend `{error}`:** `emails.send`/`contacts.create` NO lanzan en error, devuelven `{error}`;
  hay que revisarlo. `whatsapp.ts` leía el body 2 veces (arreglado: leer una vez y devolver data).
- **Recepción en dominio propio (avispao.app) = plan de pago de Resend.** El gratis solo da la
  dirección administrada `*.resend.app` (catch-all) → `FACTURAS_DOMAIN` apunta ahí por ahora.
- **Conectar correo solo empresas** (`estructura !== 'natural'`).
- **PGRST205** ("not in schema cache"): tras migrar, `notify pgrst, 'reload schema'`.
- **Cambiar env en Vercel exige Redeploy.** Las migraciones SQL las corre Lushows en el SQL Editor.

## Probar / verificar
- Conversaciones reales: `node --env-file=.env.local --import tsx scripts/test-dos-conversaciones.ts`
  (A: cliente que paga · B: prospecto vago). Otros: `scripts/test-venta.ts`, `test-conversacion.ts`.
- Antes de desplegar: `npx tsc --noEmit` + `npx next build`. Commit en español, push a main.

> **Roadmap:** registrar número real de Meta (clave XPRIZE) · cerrar cobro Bold (test pago real) ·
> dominio de recepción propio · reporte mensual automático (plantilla).

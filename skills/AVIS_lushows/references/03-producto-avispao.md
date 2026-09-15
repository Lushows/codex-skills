# 03 · El producto AVISPA'O

## Qué es
Plataforma + agente de WhatsApp (AVIS) para pymes de Colombia. **AVISPA'O** = la plataforma (web,
panel, backend); **AVIS** = el agente que conversa por WhatsApp. Web: **avispao.app**.

> ## ⚠️ ESTADO ACTUAL 24-jun-2026 (manda sobre detalles antiguos de este archivo)
> - **Planes (1:1 web↔bot):** Plus 39.900 · Premium 79.900 · Negocio 149.900 · Multi 199.900 (+ Gratis). Anual = paga 10, lleva 12. **IVA por segmento:** persona natural/no responsable → IVA INCLUIDO (paga el precio tal cual); empresa/responsable de IVA → +IVA (lo descuenta). Ver [[project_avispao_pasarela]] y `27-pagos-y-cobro`.
> - **Pago:** MercadoPago. **Tarjeta = suscripción automática · PSE/Nequi = pago ÚNICO por periodo** (las suscripciones recurrentes en CO solo aceptan tarjeta). Ciclo: vence→**pausa** (gate servicioActivo)→pago→**reactiva**; AVIS avisa antes de vencer y cuando se pausa. Pago por WEB → correo de confirmación con enlace que ENLAZA el WhatsApp (código AV-) → AVIS reconoce el plan. Si dicen "ya pagué/no me reconoce" y el número no está activo, AVIS GUÍA el enlace (no dice "activo").
> - **Perfil tributario** capturado (responsable IVA · RST/ordinario · INC por rubro): AVIS lee IVA/INC/retenciones de cada factura; NO inventa tarifas (contador confirma). Ver `14-tributario-practico`.
> - **Documentos generables = 8** (no 4): + Política de Datos (Habeas Data), Reglamento Interno de Trabajo, Reglamento de Higiene y Seguridad, Plan de Gestión de Residuos. **POR CARGO:** admin/miembro solo genera los OPERATIVOS de su sede (saneamiento, capacitación, bioseguridad, residuos); los de empresa (SG-SST, reglamentos, política de datos) los hace el DUEÑO. AVIS GENERA solo esos 8; lo demás (SAYCO, bomberos…) lo AVISA/GESTIONA (NUNCA "te genero el SAYCO"). Ver `23-plantillas-de-documentos`.
> - **Branding:** el dueño manda su LOGO ("logo") → sus documentos salen con su marca. **Formatos .xlsx** (planillas diligenciables) descargables y editables. Panel → Cumplimiento → "Mis documentos" agrupado **por sede**, con PDF + Excel.
> - **Perfiles por área** (contador Premium+ · compras/ventas Negocio+) exportan su CSV. **Varios dueños** (Multi, hasta 3) vía enlace de co-dueño.

## Los dos pilares de valor
1. **Cumplimiento (wedge):** papeles mínimos por rubro/ciudad, avisos de vencimiento, generación y
   gestión de documentos. (Ver `02-cumplimiento-colombia.md`.)
2. **Facturas y cuentas claras:** lee facturas (foto/PDF/XML DIAN), las cruza sin doble conteo, las
   categoriza y arma el reporte; export para el contador. (Ver `04-facturas-dian-cruce.md`.)

## Planes y precios
| Plan | Precio | Para qué |
|---|---|---|
| **Básico** | Gratis | Lista de papeles + recordatorios + chat con AVIS. (Sin lectura de facturas ni panel completo.) |
| **Avispa'o** ⭐ | **$29.900 / mes** (COP) | Todo lo del Básico + lectura de facturas con IA + control de gastos + panel completo + genera documentos. (Lectura ~50 facturas/mes.) |
| **Empresarial** | **$49.900 / mes** | Todo + multi-sede/multi-usuario + delegación al equipo + reportes/export CSV + soporte prioritario. |

Cobro mensual vía **Bold** (Nequi/PSE/tarjeta). Sin permanencia, cancela cuando quieras. Precio se
ajusta sin tocar código con `BOLD_PLAN_AMOUNT`. Idea parqueada: tier premium "tu declaración de renta
incluida".

## Flujos del usuario (orquestados en `src/lib/conversacion.ts`)
- **Prospecto** (no ha pagado): AVIS **vende** (cerebro `venta.ts`), extrae datos del negocio en
  silencio, lleva al cierre. Ver `05-ventas-y-objeciones.md`.
- **Pago** → webhook Bold activa `plan='activo'` → AVIS manda **bienvenida** automática.
- **Cliente** (pagó o perfil completo): consultas con sus datos reales + atajos (reporte, conectar,
  generar doc, delegación, panel).

## Segmentación: empresa vs persona natural (importante)
`onboarding_state.estructura` = `'natural'` | `'sas'`.
- **Empresa/negocio** (≠ natural) → se le ofrece **conectar el correo** para recibir facturas
  electrónicas automáticamente (banner Inicio + ítem "Conectar" en el panel).
- **Persona natural** → NO se le empuja conectar correo (no recibe muchas electrónicas); usa la
  **foto**. La página /panel/conectar sigue accesible, solo no se promueve.

## Facturas: cómo entran
1. **Foto por WhatsApp** (cualquier admin del negocio) — para no perder la compra diaria.
2. **Buzón por correo** `facturas-<token>@<dominio>` — el cliente reenvía o sus proveedores envían;
   AVIS las lee solas. (Hoy el dominio de recepción es la dirección administrada de Resend; la bonita
   `@avispao.app` requiere plan de pago de Resend.)
3. **El cruce:** si una foto y la electrónica son la misma compra → se unen, **no se cuenta doble**;
   la electrónica (exacta) manda. (Ver `04`.)

## Panel del cliente (`/panel`)
Inicio (KPIs + semáforo de papeles + buzón), Papeles (por categoría), **Facturas** (reporte: gasto
mes/total, IVA, por categoría, top proveedores, lista con badges Exacta/Leída + "Posible dup.";
botón **Exportar CSV**), Conectar (guía de correo, solo empresas), Equipo. Acceso por **enlace mágico**
(sin contraseña) que AVIS manda por WhatsApp; admite `?next=/panel/conectar` para deep-link.

## Equipo / multi-admin
Tablas `puntos` (sedes) y `miembros` (personas que hablan con AVIS: dueño/admin/empleado, con
`whatsapp_phone` y `punto_id`). Cualquier admin manda facturas y se atribuyen al comercio (y su punto).
Delegación: el dueño dice "mi admin de punto es Juan, 3XX…" → AVIS invita a Juan con plantilla
`avis_saludo`.

## Notificaciones / WhatsApp
La relación es **conversacional**: dentro de 24h del último mensaje del cliente, AVIS responde texto
libre (gratis). Avisos **proactivos** fuera de ventana requieren **plantilla aprobada** de Meta. Por eso
el aviso de factura del buzón es texto libre por defecto (decisión de producto), y la plantilla
`WA_FACTURA_TEMPLATE` quedó opcional/apagada. Plantillas que SÍ existen: `avis_saludo` (delegación),
`WHATSAPP_TEMPLATE_RECORDATORIO` (recordatorios).

> **Roadmap:** reporte mensual automático (necesita plantilla) · recordatorios proactivos por
> vencimiento · campañas/remarketing · onboarding guiado de empresa.

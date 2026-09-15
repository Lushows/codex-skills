# 04 — Cuenta, MCC y conversiones (setup)

Los cimientos. El 80% de las cuentas que "no funcionan" están mal montadas desde el día uno: facturación frágil, conversiones mal definidas, sin verificación de anunciante, zona horaria equivocada. Lee este módulo cuando abras una cuenta nueva, cuando vayas a manejar cuentas de clientes (como servicio, ver 95), o antes de crear cualquier conversión. **Esto es la fase 2 del método (ver 00): sin cimientos, no se construye encima.**

## Cuenta normal vs MCC (Manager)

| | Cuenta normal | **MCC (Manager / "Centro de administración")** |
|---|---|---|
| Qué es | una sola cuenta de anuncios | una cuenta "paraguas" que administra varias |
| Para quién | un solo negocio | agencias, o quien maneja varias marcas (Lushows) |
| Ventaja | simple | facturación, permisos y reportes centralizados; mueves cuentas sin perder historial; conversiones y listas de audiencia compartidas a nivel manager |
| Cuándo crearla | 1 negocio, 1 cuenta | desde que manejas 2+ cuentas o cuentas de terceros |

Recomendación para Lushows: **crea un MCC** y cuelga ahí las cuentas (GastroLatam, etc.). Te da control de facturación y permisos sin pedirle la contraseña al cliente. **Nunca** uses la cuenta personal del cliente con su login compartido — pide acceso vía MCC (le mandas tu ID de manager, él acepta). Ventaja extra: puedes definir **conversiones a nivel MCC** y compartirlas entre cuentas, y mover una cuenta entre managers sin perder su historial de aprendizaje del Smart Bidding.

## Facturación que no te tumba la cuenta

| Cosa | Recomendación |
|---|---|
| Método de pago | tarjeta sólida + un **respaldo** (un rechazo y se pausan TODAS tus campañas sin aviso útil) |
| Tipo de pago | "pago automático" (umbral): Google cobra al llegar a un monto o cada mes, lo que pase primero |
| Moneda / zona horaria | **defínelas bien al crear la cuenta — NO se pueden cambiar después.** COP y America/Bogotá |
| Impuestos | configura datos fiscales correctos (NIT/RUT si aplica) para evitar bloqueos |
| Umbral de pago | sube con el historial; al inicio Google cobra montos pequeños seguido |

La zona horaria mal puesta te descuadra TODOS los reportes y los horarios de programación (ver 19). Revísala antes de gastar el primer peso. La moneda mal puesta (USD en vez de COP) te obliga a abrir cuenta nueva — error caro e irreversible.

## Verificación de anunciante (hazla YA, no es opcional)

Google exige verificar **quién eres** antes de dejarte pautar a fondo. Es la causa #1 de pausas "sorpresa" en pleno mes (ver 08).

| Tipo | Qué piden | Cuándo |
|---|---|---|
| Identidad | documento de la persona/empresa | toda cuenta, en plazo definido tras crearla |
| Negocio (Advertiser identity) | datos legales, dominio que coincide con la cuenta | cada vez más común, obligatorio |
| Sectorial extra | licencias (salud, finanzas) | sectores regulados (ver 83) |

**Hazla apenas abras la cuenta.** Si esperas al aviso, te pausan anuncios cuando ya estás corriendo y perdiendo días de aprendizaje.

## Acciones de conversión: el corazón del setup

Una **conversión** es la acción valiosa que quieres medir (venta, lead, llamada, clic a WhatsApp). Esto es lo que el Smart Bidding usa para optimizar (ver 13). Si está mal, todo lo demás está mal — la IA persigue lo que le digas que es valioso.

| Decisión | Recomendación |
|---|---|
| **Categoría** | "Compra" para venta real; "Cliente potencial/Lead" para formularios/WhatsApp; "Contacto"/"Solicitud de cotización" según el caso |
| **"Conversión principal" vs "secundaria"** | SOLO la venta/lead real como **principal** (cuenta para la puja). Lo demás (ver video, scroll, add-to-cart) = secundaria/observación |
| **Recuento (Count)** | "Cada una" para ventas e-commerce (cada compra cuenta); "Una" para leads (no contar 5 veces al mismo que llenó el form 3 veces) |
| **Valor** | ponle valor real en COP si puedes (habilita tROAS, ver 15); si el ticket varía, pasa valor dinámico |
| **Ventana de conversión** | 30 días para venta rápida; 60–90 para ciclos largos/B2B (ver 27) |
| **Atribución** | data-driven por default (ya no es last-click); déjala así salvo razón fuerte (ver 16) |

Error mortal: marcar como conversión principal "clic en botón de WhatsApp". Eso NO es venta. Marca el clic como **secundario** y trae la venta real con OCI vía gclid (ver 53). Si pones lo barato como principal, la IA persigue lo barato y te llena de curiosos.

### Plantilla de jerarquía de conversiones (negocio que cierra por WhatsApp)

| Acción | Tipo | Por qué |
|---|---|---|
| Venta cerrada (OCI desde el CRM/WhatsApp) | **Principal** | es la verdad del negocio; la IA debe optimizar a esto |
| Lead calificado (form/click WhatsApp con datos) | Principal secundaria o "transición" | señal temprana mientras OCI madura |
| Clic en botón WhatsApp | Secundaria (observación) | curioso; útil de ver, no de optimizar |
| Ver video / scroll 75% | Secundaria | micro-señal, nunca para puja |

Mientras OCI no tenga volumen suficiente para optimizar (necesita ~15–30 ventas/mes, ver 07), puedes optimizar temporalmente al **lead calificado** y migrar a venta-OCI cuando haya datos.

## Permisos y acceso

- **Permisos (vía MCC):** da acceso por rol — Administrador, Estándar, Solo lectura, Solo facturación. Para un freelance que optimiza: **Estándar**. Nunca repartas Administrador a todo el mundo.
- Sectores sensibles (salud, finanzas) piden verificaciones extra (ver 83, 08).
- Para servicio a clientes: pide acceso a SU cuenta desde TU MCC; no crees la cuenta del cliente bajo tu login personal (ver 95).

## Errores comunes — blacklist

- **Dejar la zona horaria/moneda mal y querer cambiarla después.** No se puede; toca cuenta nueva y pierdes historial. Fix: configúralas correctas (COP, America/Bogotá) al crear.
- **Marcar todo como conversión "principal" (clics, scroll, WhatsApp).** El Smart Bidding optimiza hacia el ruido. Fix: solo venta/lead real como principal; lo demás secundario (ver 13).
- **Un solo método de pago.** Un rechazo y se pausan todas las campañas sin aviso útil. Fix: agrega tarjeta de respaldo.
- **No hacer la verificación de anunciante hasta que llega el aviso.** Te suspenden anuncios en pleno mes. Fix: verifica al abrir la cuenta (ver 08).
- **Usar el login del cliente en vez de pedir acceso por MCC.** Pierdes acceso si cambian la clave y mezclas responsabilidades. Fix: acceso vía MCC con tu rol (ver 95).
- **Contar el mismo lead varias veces ("Cada una" en leads).** Infla tus conversiones y engaña tu CPA. Fix: "Una" para leads.
- **No ponerle valor en COP a la conversión.** Te cierra la puerta a tROAS y al ROAS real. Fix: asigna valor real (ver 15, 64).
- **Crear conversiones duplicadas (nativa de Ads + importada de GA4 para la misma acción).** Doble conteo, CPA falso. Fix: una sola fuente por acción (ver 05).

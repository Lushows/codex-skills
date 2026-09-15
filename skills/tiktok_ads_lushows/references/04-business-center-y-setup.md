# 04 — Business Center y setup

Lee este módulo antes de crear tu primera campaña, o cuando heredes una cuenta desordenada que no sabes si está bien montada. Un setup mal hecho te tumba después: cuentas que se banean por mezclar negocios, pagos rechazados a mitad de campaña, o no poder pasarle acceso a un cliente sin entregarle tu contraseña. Veinte minutos de orden aquí te ahorran semanas de dolor. Esto es la fontanería; el creativo viene después (ver 30).

## La jerarquía de TikTok for Business (de arriba hacia abajo)

| Nivel | Qué es | Regla de oro |
|---|---|---|
| **TikTok Business Center (BC)** | El "edificio" que contiene todo: cuentas, gente, activos | Crea UNO por organización. Es el centro de control |
| **Ad Account (cuenta de anuncios)** | Donde viven campañas y pagos | Una por negocio/marca. No mezcles clientes |
| **Identidades** | El perfil que firma el anuncio (tu cuenta de TikTok o una "custom identity") | Verifica y conecta tu cuenta orgánica para Spark Ads (ver 34) |
| **Pixel / Events** | El sensor de conversiones en tu web | Obligatorio antes de pautar performance (ver 05, 06) |
| **Catálogo** | Tu lista de productos para Shop/VSA | Solo si vendes e-commerce (ver 56) |

Piensa en el Business Center como el llavero maestro: desde ahí das y quitas accesos sin compartir contraseñas. Si manejas clientes (ver 95), esto es no negociable. Un BC limpio también es tu mejor defensa contra baneos: TikTok confía más en organizaciones verificadas con activos ordenados que en cuentas personales improvisadas (ver 08).

## El checklist de setup que no te tumba

| Paso | Acción concreta | Por qué |
|---|---|---|
| 1. Crear Business Center | business.tiktok.com → crear BC con datos reales de la empresa (razón social, web, NIT/correo) | Datos falsos = baneo (ver 08) |
| 2. Crear Ad Account | Dentro del BC, una cuenta por negocio | Aísla riesgo entre marcas |
| 3. Verificar dominio | Pega el meta-tag o sube el archivo en tu web; confírmalo en BC | Habilita Events API y eventos web (ver 06) |
| 4. Conectar identidad | Vincula tu cuenta orgánica de TikTok | Necesaria para Spark Ads (ver 34) |
| 5. Instalar Pixel | Vía partner (Shopify/etc.) o código manual; usa Events Manager | Sin esto no optimizas a venta (ver 05) |
| 6. Activar Events API | Integración nativa, Gateway o por código; con `ttclid` y datos hasheados | Recupera conversiones que el Pixel pierde (ver 06) |
| 7. Método de pago | Tarjeta internacional o pago manual; revisa moneda (USD vs COP) | Pago rechazado = campaña parada |
| 8. Permisos de gente | Invita por correo con rol (Admin/Operator/Analyst), NO compartas login | Seguridad y trazabilidad |
| 9. Commercial Music Library | Confirma que usarás audio licenciado para ads | Música con copyright = strike (ver 08) |

El orden importa: la verificación de dominio (paso 3) **debe ir antes** de instalar Pixel y Events API, o los eventos web quedan bloqueados. Es el error de setup más común y el más silencioso: todo "parece" instalado pero no entra señal.

## Métodos de pago en Colombia (lo que duele en la práctica)

| Tema | Realidad LatAm |
|---|---|
| Moneda de la cuenta | Suele facturar en **USD**; tu banco cobra la conversión a COP + IVA + 4×1000 |
| Tarjeta | Usa una tarjeta internacional habilitada para compras online; las de débito locales a veces rechazan |
| Pago automático vs manual | Automático (te cobra al llegar a un umbral) o recarga manual (prepago). Prepago da más control de gasto |
| Impuestos | TikTok puede sumar IVA/retenciones según facturación; revísalo en tu factura |
| Rechazo a mitad de campaña | La causa #1 de "se me apagó la cuenta sola". Ten una segunda tarjeta de respaldo |

Consejo práctico: para empezar, usa **recarga manual (prepago)** — pones $500.000 COP, gastas eso y ya. Evitas sorpresas en el estado de cuenta y aprendes el ritmo de gasto sin riesgo (ver 07). Cuando la cuenta sea estable y rentable, pasa a pago automático para que la escala no se frene por un saldo agotado un domingo a medianoche.

## Roles y permisos (para no entregar las llaves del reino)

| Rol | Puede | Dáselo a |
|---|---|---|
| **Admin** | Todo, incluido pagos y miembros | Tú, socio de confianza |
| **Operator** | Crear/editar campañas, no toca pagos | Tu media buyer |
| **Analyst** | Solo ver reportes | Cliente, contador |

Si manejas la cuenta de un cliente, pídele que te invite como **Operator/Admin a SU Business Center** — nunca trabajes desde su usuario personal ni le pidas la contraseña. Así, cuando termine el contrato, él revoca tu acceso con un clic y nadie pelea por quién es dueño del píxel ni del histórico de la cuenta. Es la diferencia entre una agencia profesional y un improvisado (ver 95).

## Errores comunes — blacklist

- **Mezclar varios negocios en una sola Ad Account.** Si una infringe políticas, caen todas. Fix: una cuenta por marca dentro del BC.
- **No verificar el dominio.** Bloquea Events API y eventos web silenciosamente. Fix: verifica el dominio ANTES de instalar el Pixel (ver 06).
- **Compartir contraseña en vez de invitar por rol.** Pierdes control y trazabilidad. Fix: usa permisos del Business Center (ver tabla roles).
- **Datos falsos en el Business Center.** Riesgo alto de baneo. Fix: nombre legal, web y correo reales (ver 08).
- **Olvidar conectar la identidad orgánica.** No puedes hacer Spark Ads. Fix: vincula tu cuenta de TikTok en Identidades (ver 34).
- **No revisar moneda/impuestos del pago.** Te llega un cobro en USD inflado y te asustas. Fix: confirma USD/COP, IVA y 4×1000 (ver tabla pagos).
- **Una sola tarjeta sin respaldo.** Rechazo = campaña apagada en silencio. Fix: ten segunda tarjeta o prepago cargado (ver 07).
- **Trabajar desde el login del cliente.** Cero trazabilidad, riesgo de baneo cruzado. Fix: que te inviten como Operator a su BC (ver 95).

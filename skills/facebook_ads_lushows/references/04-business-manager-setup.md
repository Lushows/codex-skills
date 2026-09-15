# 04 — Business Manager: setup a prueba de balas

El Business Portfolio (antes llamado Business Manager o BM) es el contenedor donde viven tu página, tu cuenta publicitaria, tu dataset (píxel) y tus permisos. Un setup descuidado es la causa #1 de cuentas hackeadas, baneos evitables y clientes secuestrados por agencias. Lee este módulo ANTES de gastar el primer peso.

## Checklist completo de setup (en orden)

1. **Crear el Business Portfolio** en business.facebook.com con un correo del negocio (no el personal del primo). Nombre real del negocio: los BMs con datos falsos caen en verificación.
2. **Agregar la página de Facebook** (y conectar el Instagram profesional). La página debe tener información completa: foto, descripción, datos de contacto. Páginas vacías = señal de spam.
3. **Crear la cuenta publicitaria** dentro del BM (Configuración del negocio → Cuentas → Cuentas publicitarias → Agregar). Zona horaria **America/Bogota** y moneda **COP** (o USD si facturas en dólares): no se pueden cambiar después, solo creando otra cuenta.
4. **Verificar el dominio** de tu web (Brand Safety → Dominios → meta-tag, DNS TXT o archivo HTML). Necesario para priorizar eventos web (Aggregated Event Measurement) y para credibilidad de la cuenta. Sin dominio verificado no puedes configurar bien la prioridad de los 8 eventos web post-iOS 14.5 (ver 05).
5. **2FA (autenticación de dos factores) en TODOS los admins. El punto #1 de seguridad.** Meta lo exige y los hackeos de cuentas publicitarias entran casi siempre por un admin sin 2FA. App de autenticación (Google Authenticator), no SMS. Sin excepciones, sin "el socio lo activa luego".
6. **Roles y permisos mínimos**: máximo 2 admins del BM (dueño + persona de confianza). Media buyers y agencias = empleados con acceso solo a los assets que necesitan ("Administrar campañas", no "Administrar cuenta"). Cada permiso de más es una puerta de entrada.
7. **Método de pago confiable**: tarjeta de crédito del negocio con cupo holgado. Un pago rechazado congela la entrega y mancha el historial. En Colombia: tarjeta internacional habilitada para compras online; ten una de respaldo cargada. Considera que Meta cobra en USD: el banco suma IVA + 4×1.000 + comisión de divisa, presupuéstalo.
8. **Límite de gasto de la cuenta** (Configuración de pagos → Límite de gasto de la cuenta): ponle un techo mensual. Si te hackean o un ad se desboca, el daño tiene tope.
9. **Verificación del negocio** (Centro de seguridad → Verificación): con cámara de comercio/RUT. No siempre es obligatoria, pero desbloquea límites y te da un colchón de confianza ante revisiones. En 2026 es además requisito para varias categorías especiales (ver 08).
10. **Crear el dataset/píxel desde este BM** (ver 05) y, si aplica, el catálogo (ver 55). Todo asset nace dentro del BM del negocio. **Activa CAPI** desde el primer día (ver 06): el botón de "Activate Conversions API" de un clic ya está disponible para cuentas nuevas.

## Estructura para agencia / multi-marca

Regla de hierro: **los assets viven en el BM del CLIENTE; tú entras como partner**.

- El cliente crea (o ya tiene) su Business Portfolio, su página, su cuenta publicitaria y su dataset.
- Tú, desde TU BM de agencia, pides **acceso de partner** (Configuración del negocio → Socios) con tu Business ID, o el cliente te asigna los assets.
- **NUNCA crees la cuenta publicitaria o el dataset del cliente dentro de tu BM.** Si la relación termina, el cliente pierde su historial, su píxel y sus datos; eso es secuestro involuntario y te quema la reputación. Además, si banean TU BM, caen TODOS tus clientes a la vez.
- Facturación: idealmente el método de pago es del cliente (su tarjeta, su responsabilidad fiscal). Si pagas tú y refacturas, cobra por adelantado (modelo de servicio en 95).
- Multi-marca propia (caso Lushows): un BM por negocio si los verticales son riesgosos o muy distintos; assets separados = riesgo aislado.

## Por qué un buen setup previene baneos

Meta puntúa la confiabilidad de tu negocio con señales: identidad verificable, dominio verificado, historial de pagos limpio, admins seguros, página con vida real. Una cuenta nueva, sin verificación, con tarjeta prepago, página vacía y campañas agresivas el día 1 = patrón exacto de un estafador, y el sistema banea por patrón, sin humanos. Calienta la cuenta: empieza con presupuesto moderado, anuncios 100% limpios (ver 08), y sube gradualmente. Si pese a todo te banean, el protocolo de recuperación está en 93.

**Calentamiento sugerido (cuenta virgen):** semana 1, una sola campaña limpia con 30.000–60.000 COP/día; semanas 2-3, sube ~20-30% si no hay strikes; recién en semana 4 metes el vertical/copy más agresivo. La prisa de gastar fuerte el día 1 es la causa más tonta de restricción.

## Mantenimiento (cada mes, 10 minutos)

- Revisar Personas y Socios: sacar a quien ya no trabaja contigo.
- Revisar actividad de la cuenta (Calidad de la cuenta) por avisos pendientes.
- Confirmar que la tarjeta de respaldo sigue vigente.
- Verificar que el 2FA sigue activo en todos los admins (un cambio de celular suele desactivarlo en silencio).
- Confirmar que CAPI sigue enviando y el EMQ no se cayó (tokens vencen, plugins se rompen, ver 06).

## Onboarding exprés de un cliente nuevo (resumen operativo)

1. Pregunta si ya tiene BM/página/cuenta publicitaria. Si sí: pide acceso de partner con tu Business ID; NO crees nada nuevo.
2. Si no tiene nada: agenda 30 minutos en videollamada y guíalo a crear TODO desde SU correo de negocio (tú diriges, él teclea: así el dueño legal es él).
3. Audita lo heredado: ¿2FA en todos?, ¿admins fantasma?, ¿dataset en qué BM vive?, ¿deudas o strikes en Calidad de la cuenta?, ¿CAPI activa y con qué EMQ?
4. Documenta en un doc compartido: Business ID, ID de cuenta publicitaria, ID del dataset/píxel, quién es admin. El día que algo se dañe, este doc vale oro.

## Señales de un BM heredado problemático (audita antes de aceptar el encargo)

- Strikes o anuncios rechazados acumulados en Calidad de la cuenta → el historial sucio te afecta a ti (ver 08).
- Cuenta publicitaria con deuda pendiente → Meta no entrega hasta saldar.
- Dataset viviendo en el BM de la agencia anterior → recupéralo o crea dataset nuevo asumiendo que pierdes historial.
- Admins desconocidos o apps de terceros con acceso total → limpia antes de conectar tu tarjeta o tu trabajo.
- Página comprada o reciclada de otro nicho → riesgo de restricción al cambiar de actividad de golpe.
- EMQ histórico bajo o CAPI nunca configurada → vas a heredar optimización pobre; planifica reinstrumentar (ver 06).

## Convención de nombres (te ahorra horas de reportería)

Un BM ordenado se reconoce en cómo nombra campañas, ad sets y ads. Adopta un patrón fijo desde el día uno; cuando la cuenta crezca a 40 anuncios, agradecerás poder filtrar por nombre:

- **Campaña**: `[Objetivo]_[Producto]_[Audiencia]_[Mes]` → `Sales_ExcelGastro_Broad_Jun26`
- **Ad set**: `[Optimización]_[Temperatura]` → `Conv_WA_Frio`
- **Ad**: `[Formato]_[Ángulo]_[Versión]` → `Reel_Dolor_v3`

Con eso, en Ads Manager filtras "Dolor" y ves todos los creativos de ese ángulo; filtras "Jun26" y comparas el mes. Sin convención, a los tres meses nadie entiende qué es "Campaña - copia (2) FINAL".

## Errores comunes — blacklist

- **Pautar desde el perfil personal sin BM**: cero estructura, cero respaldo, imposible delegar; y si te restringen el perfil, pierdes todo.
- **Admins sin 2FA**: la causa #1 de cuentas robadas que amanecen gastando 5.000 USD en ads de criptoestafas.
- **Crear los assets del cliente en tu BM de agencia**: secuestro de assets + riesgo cruzado entre clientes.
- **Tarjeta prepago o sin fondos**: pagos rechazados son la mancha más tonta del historial.
- **Todo el mundo admin "para que sea más fácil"**: cada admin extra es superficie de ataque y de error humano.
- **Zona horaria/moneda mal configuradas**: reportes desfasados de por vida; no se puede corregir sin crear cuenta nueva.
- **Sin límite de gasto de cuenta**: un hackeo o error de presupuesto sin techo es una factura ilimitada.
- **Lanzar a presupuesto máximo el día 1 en cuenta virgen**: patrón de estafador; calienta gradualmente.

# 06 — Enhanced Conversions y Consent Mode v2

Las cookies de terceros se están muriendo y los navegadores bloquean cada vez más rastreo. Estas dos piezas son el **piso de medición 2026**: sin ellas, pierdes conversiones (las ves más bajas de lo que son) y el Smart Bidding optimiza a ciegas. Lee este módulo en el setup (fase 2, ver 00), cuando notes que "Google reporta menos conversiones de las que sé que tuve", o si pautas hacia Europa (EEA).

## Por qué post-cookie (el problema de fondo)

Antes, la cookie de terceros conectaba el clic con la conversión. Hoy Safari/Firefox la bloquean por defecto, iOS limita el rastreo, y la gente rechaza cookies en el banner. Resultado: muchas conversiones reales **no se atribuyen** → tu CPA se ve peor, tu ROAS se ve falso, y la IA puja mal (por debajo de lo óptimo donde sí convierte). La respuesta de Google: **datos first-party (tuyos, con consentimiento) + modelado estadístico**. Esas dos piezas son Enhanced Conversions y Consent Mode v2. Juntas son el **piso de medición**, no un lujo opcional.

## Enhanced Conversions (datos hasheados first-party)

Cuando alguien convierte (compra, deja el formulario), tú ya tienes su **email/teléfono** (que él te dio). Enhanced Conversions toma esos datos, los **hashea** (los convierte en código irreversible SHA-256 **en el navegador**, no viajan en texto plano) y se los manda a Google para casar la conversión con el clic aunque la cookie se haya caído.

| | Detalle |
|---|---|
| Qué recupera | conversiones que se perdían por falta de cookie (típico **+5% a +15%** recuperado, a veces más) |
| Dato que usa | email/teléfono que el usuario YA te entregó (first-party, con consentimiento) |
| Privacidad | hasheado SHA-256 — Google no ve el dato crudo |
| Cómo activarlo | en Ads: Conversiones → Configuración → Enhanced Conversions; implementa vía Google tag, GTM o API |
| Modos | **for Web** (datos en la página de gracias) y **for Leads** (casa el lead del formulario con la venta cerrada después, clave en LatAm, ver 53) |

**Enhanced Conversions for Leads** es oro en LatAm: el usuario deja su WhatsApp/email en la web, tú cierras la venta días después, y este mecanismo (+ OCI) le devuelve a Google qué clic generó la venta real (ver 53, 54). Es lo que conecta el embudo "Search → WhatsApp → venta" sin perder la atribución.

### Cómo implementarlo (3 vías)

| Vía | Cuándo | Esfuerzo |
|---|---|---|
| **Google tag + datos en la página** | el email/teléfono ya está en el DOM de la página de gracias | bajo |
| **GTM (variable de datos del usuario)** | tienes GTM y quieres control | medio |
| **API (Google Ads API / for Leads)** | cierre offline, CRM, WhatsApp | alto, pero es el correcto para LatAm |

## Consent Mode v2 (consentimiento + modelado)

Consent Mode es cómo le dices a Google **si el usuario aceptó o no** ser rastreado, y qué hacer en cada caso. La **v2** es **obligatoria si pautas hacia el EEA (Europa/Reino Unido)** — sin ella, Google no usa tus datos de audiencia/remarketing de usuarios europeos.

| Señal de consent | Qué controla |
|---|---|
| `ad_storage` | cookies de publicidad |
| `ad_user_data` | enviar datos del usuario a Google (**nuevo en v2**) |
| `ad_personalization` | personalización/remarketing (**nuevo en v2**) |
| `analytics_storage` | cookies de analítica |

| Modo | Qué pasa cuando el usuario NO acepta |
|---|---|
| **Básico** | no se cargan los tags; no hay datos ni modelado → ves menos de lo real |
| **Avanzado** (recomendado) | el tag carga "sin cookies", manda pings anónimos → Google **modela** (estima estadísticamente) las conversiones que no pudo observar |

**Conversion modeling:** cuando no hay consentimiento, Google **estima** las conversiones perdidas usando patrones agregados. Eso solo funciona en modo **Avanzado**. Por eso el piso 2026 es: **Enhanced Conversions + Consent Mode v2 en modo Avanzado.**

¿Lushows pauta solo en Colombia? Consent Mode v2 no es legalmente obligatorio fuera del EEA, **pero impleméntalo igual**: mejora el modelado, te deja listo si algún día vendes a Europa, y es buena higiene de privacidad bajo la ley colombiana de datos (Habeas Data). La privacidad/legal de fondo está en 29.

## Cómo encajan las piezas de medición (mapa)

| Pieza | Qué resuelve | Ver |
|---|---|---|
| Google tag + GA4 | medir el evento online | 05 |
| **Enhanced Conversions** | recuperar atribución online perdida por cookies | este módulo |
| **Consent Mode v2 (Avanzado)** | modelar lo que no se pudo observar + cumplir EEA | este módulo |
| **OCI (gclid)** | traer la venta OFFLINE (WhatsApp/llamada) de vuelta | 53 |

Son **complementarios, no sustitutos**: Enhanced Conversions recupera atribución online, Consent Mode modela lo no observado, OCI trae la venta offline. Un setup de élite tiene los tres.

## Errores comunes — blacklist

- **No activar Enhanced Conversions "porque suena técnico".** Dejas 5–15% de conversiones reales sin atribuir → CPA inflado → la IA puja por debajo de lo óptimo. Fix: actívalo en Conversiones (ver arriba).
- **Pautar hacia Europa sin Consent Mode v2.** Google deja de usar tus listas de remarketing de usuarios EEA. Fix: implementa v2 antes de pautar al EEA.
- **Usar Consent Mode en modo Básico.** Pierdes el modelado de conversiones; ves menos de lo real. Fix: modo **Avanzado**.
- **Mandar el email/teléfono en texto plano.** Riesgo de privacidad y rechazo de Google. Fix: el hasheo SHA-256 lo hace el tag/GTM automáticamente — no lo mandes crudo.
- **Olvidar Enhanced Conversions for Leads en un negocio que cierra por WhatsApp/llamada.** Pierdes el puente entre el lead y la venta real. Fix: actívalo y combínalo con OCI (ver 53).
- **Creer que Enhanced Conversions reemplaza a OCI.** Son complementarios: EC recupera atribución online, OCI trae la venta offline. Fix: usa ambos (ver 53, 96).
- **Implementar todo y no verificar el diagnóstico.** Quedas en falso creyendo que mides. Fix: revisa el estado "Registrando/Recording" en Ads y el diagnóstico de Enhanced Conversions (ver 62).

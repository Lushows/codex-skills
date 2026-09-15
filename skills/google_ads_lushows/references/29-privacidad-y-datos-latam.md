# 29 — Privacidad y datos LatAm

Lee este módulo ANTES de subir cualquier lista de clientes, montar formularios o activar medición avanzada — y obligatoriamente si operas en Colombia, Brasil o México. La privacidad no es burocracia opcional: en 2026 Google **te exige** consentimiento para que la medición funcione (sin Consent Mode pierdes datos), y la ley local te puede multar fuerte por mal manejo de datos personales. La buena noticia: cumplir bien NO mata tu medición — bien hecho, la mejora. Mal hecho, te quedas ciego Y expuesto. Frame: capturar intención y datos propios es tu ventaja (ver 25, 28), pero capturarlos sin consentimiento es ilegal y frágil — el cumplimiento es lo que hace sostenible la ventaja.

## Consent Mode v2 — obligatorio para medir

**Consent Mode** (Modo de Consentimiento) es el mecanismo de Google para respetar si el usuario aceptó o no ser rastreado. Funciona con tu banner de cookies: cuando alguien dice "sí acepto" o "no", Consent Mode le avisa a Google y este ajusta qué mide.

Lo crítico: desde 2024 Google exige **Consent Mode v2** para usar funciones de audiencia y medición avanzada (Customer Match, remarketing, Enhanced Conversions) en regiones reguladas (EEE/Reino Unido obligatorio; LatAm muy recomendado y exigible según tu CMP y la ley local). Si no lo tienes:
- Tus listas de remarketing dejan de crecer (ver 24).
- Pierdes datos de conversión.
- El Smart Bidding optimiza con menos información y tu CPA real se ve peor.

Tiene cuatro señales clave, las dos centrales son: `analytics_storage` (medición) y `ad_storage` (publicidad/cookies de anuncios); v2 añadió `ad_user_data` (mandar datos del usuario a Google) y `ad_personalization` (personalización/remarketing). Tu banner de consentimiento debe enviarlas según lo que el usuario elija. Hay un mecanismo útil: el **"modeling" (modelado)** de Consent Mode — cuando un usuario rechaza, Google estima estadísticamente las conversiones perdidas con datos agregados para no dejarte totalmente ciego. Solo funciona si Consent Mode está bien instalado y tienes volumen suficiente. Sin él, las conversiones de quien rechazó simplemente desaparecen.

Implementación: se monta vía Google Tag Manager + una plataforma de consentimiento (CMP) certificada (Cookiebot, OneTrust, CookieYes, etc.). La parte técnica la cubre `engineer_visualopen_lushows`; aquí lo que importa es **que exista, que esté bien y que envíe las 4 señales**.

## Las leyes que te aplican en LatAm

| País | Ley | Qué exige (esencial) | Sanción tope |
|---|---|---|---|
| **Colombia** | Habeas Data (Ley 1581 de 2012) + decretos, vigilada por la SIC | Consentimiento previo, expreso e informado; finalidad clara; derecho a conocer/actualizar/suprimir; registro de bases (RNBD) ante la SIC si aplica | Hasta 2.000 SMMLV |
| **Brasil** | LGPD, vigilada por la ANPD | Base legal para tratar datos; derechos del titular; encargado (DPO); sanciones de la ANPD | Hasta 2% de facturación (tope ~R$50M por infracción) |
| **México** | LFPDPPP | Aviso de privacidad; consentimiento; derechos ARCO | Multas elevadas en UMA |

Lo común a todas: **necesitas consentimiento + finalidad clara + dejar al usuario retirar/borrar sus datos.** Para Google Ads esto se traduce en cosas concretas:
- No subir a Customer Match (ver 25) datos de gente que no aceptó que los uses para publicidad.
- Tener **política de privacidad** visible (Google también la exige; en este proyecto vive en `/privacy`).
- En formularios de leads, casilla de consentimiento clara (no pre-marcada) que diga para qué usarás el dato y enlace a la política.
- En Colombia, registrar tus bases de datos en el **RNBD** de la SIC si superas los umbrales (empresas con activos sobre cierto tope).

## Datos sensibles y consentimiento en formularios

**Datos sensibles** = salud, orientación sexual, religión, datos de menores, origen racial/étnico, datos biométricos, situación financiera detallada, afiliación política o sindical. Google tiene **políticas estrictas** y prohíbe segmentar por categorías sensibles (no puedes hacer remarketing tratando a alguien como "enfermo de X" o "endeudado"). En Colombia los datos sensibles tienen protección reforzada bajo Habeas Data (requieren consentimiento explícito y no se pueden tratar salvo excepciones legales). Si tu negocio toca estos temas (salud, finanzas, menores), pisa con cuidado y consulta lo legal — no improvises.

**Consentimiento en formularios — lo concreto y correcto:**
1. Casilla **NO pre-marcada** que el usuario activa por sí mismo.
2. Texto claro: "Acepto que [empresa] use mis datos para [contactarme / enviarme info de productos], conforme a la [política de privacidad]" con enlace funcional.
3. Guarda **prueba** del consentimiento (fecha, hora, IP, versión del texto que aceptó) — la ley te puede pedir demostrarlo. Un registro en tu CRM o base sirve.
4. Da forma de retirar el consentimiento (un "darse de baja" real y operativo, no decorativo).

Si capturas el lead vía **Lead Form de Google** (ver 52) o landing propia, el consentimiento debe estar ahí igual. Un lead sin consentimiento válido es un lead que no puedes meter a Customer Match ni a tu CRM legalmente — y subirlo te expone a multa de la SIC.

## Cumplir sin matar la medición — el balance

El miedo común: "si pongo banner de cookies, pierdo medición". Realidad 2026:
- **Sin** Consent Mode: pierdes TODO de quien no rastreas, y encima estás ilegal y sin modeling.
- **Con** Consent Mode bien puesto: respetas la ley Y recuperas (vía modeling + Enhanced Conversions sobre datos consentidos) buena parte de lo que perderías.

O sea: cumplir bien es la opción que MÁS mide, no la que menos. El que cree que saltarse el consentimiento "mide más" está mal informado y, además, jugándose una sanción. El stack legal y de máxima medición a la vez es: **banner/CMP + Consent Mode v2 (4 señales) + Enhanced Conversions (ver 28) sobre datos consentidos + Customer Match solo de listas con consentimiento (ver 25).** Eso es lo que hace un buyer serio en LatAm en 2026.

## Errores comunes — blacklist

1. **No tener Consent Mode v2.** Pierdes audiencias, conversiones y modeling — y quedas expuesto legalmente. Es lo primero a montar en región regulada (ver 28).
2. **Subir a Customer Match listas sin consentimiento.** Ilegal bajo Habeas Data/LGPD y sancionable por Google. Solo contactos que aceptaron uso publicitario.
3. **Casilla de consentimiento pre-marcada.** No es consentimiento válido bajo la ley. Debe activarla el usuario.
4. **No guardar prueba del consentimiento.** Si la autoridad pregunta y no puedes demostrar que aceptaron, estás en problemas. Registra fecha, alcance y versión del texto.
5. **Segmentar o hacer remarketing con datos sensibles.** Prohibido por Google y reforzado por ley local. Salud, finanzas, menores: cero targeting sensible.
6. **Creer que el banner mata la medición.** Al revés: Consent Mode bien puesto recupera datos vía modeling. Cumplir es medir más, no menos.
7. **Copiar una política de privacidad genérica de internet.** Debe reflejar lo que TÚ haces con los datos y citar la ley local correcta. Una política falsa es peor que ninguna — y Google y la SIC pueden revisarla.
8. **No registrar bases en el RNBD (Colombia) cuando aplica.** Si superas los umbrales y no registras, es infracción aparte de las de consentimiento. Verifica si te aplica con un abogado.

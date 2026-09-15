# 51 — Call ads y call tracking

Lee este módulo cuando tu negocio cierra **por teléfono** y no por formulario: una llamada vale más que diez visitas a la web. Servicios urgentes (cerrajero, grúa, plomero, clínica con cita), high-ticket donde el cliente quiere hablar antes de pagar (ver 58), o pymes donde "una persona contesta y vende" cierra mejor que cualquier landing. Aquí Google te trae a quien ya tiene el problema y prefiere llamar — y te enseña a **medir esa llamada como una conversión real**, no como fe. Sin medición, las llamadas son humo y Smart Bidding no puede optimizar hacia ellas (ver 15 pujas).

## Tres formas de generar llamadas en Google

| Formato | Qué es | Cuándo gana |
|---|---|---|
| **Call ads** (anuncio de solo llamada) | El anuncio NO lleva a la web: el botón es llamar. Solo en móvil. | Urgencias, el cliente quiere hablar YA, tu web no vende |
| **Asset de llamada** (antes "extensión de llamada") | Agregas un botón de llamar a tus anuncios de Search normales | Casi siempre: das opción de web O llamada |
| **Llamadas desde la landing** | El anuncio lleva a la web y ahí hay un número rastreado | Cuando la web sí ayuda a decidir antes de llamar |

Para una pyme que cierra hablando, lo más rentable suele ser **asset de llamada en todos los anuncios de Search** (no cuesta extra agregarlo) + **call ads** en las keywords más urgentes ("cerrajero 24 horas", "grúa ahora", "plomero urgente Bogotá", "dentista hoy"). El asset de llamada también deja **programar horario**: que el botón solo aparezca cuando hay alguien para contestar. Si nadie contesta, el clic se quema y el cliente llama al de al lado (ver 54 del-clic-al-cierre).

Setup paso a paso del asset de llamada: Ads → **Activos → Llamada → +** → pones el número, eliges país (Colombia), activas **call reporting** (rastreo) y fijas **horario de programación** (ej. lun-sáb 8 a.m.–6 p.m.). Se asocia a la campaña o a toda la cuenta. Tarda minutos y es gratis agregarlo.

## Call tracking: medir la llamada como conversión

Sin medir, vuelas a ciegas. **Call tracking** (rastreo de llamadas) es la mecánica de Google para contar una llamada como conversión:

1. Google sustituye tu número por un **número de reenvío de Google (GFN)** en el anuncio. El cliente marca ese número, Google lo reenvía a tu línea real y **registra la llamada** (duración, hora, keyword si aplica). El cliente no nota nada; tú recibes la llamada normal.
2. Defines una **duración mínima** para que cuente como conversión — normalmente **60 segundos**. La lógica: una llamada de 8 segundos es número equivocado o alguien que colgó; una de 60+ es un prospecto real hablando. Solo cuentas las largas, que filtran ruido.
3. Esa conversión "llamada calificada" entra a tu cuenta y **Smart Bidding aprende** a traer más gente que llama y se queda hablando, no curiosos que cuelgan (ver 15 smart-bidding, 14 conversion).

Cómo se prende (sin código, en la cuenta):
- **Herramientas → Conversiones → Nueva acción → Llamadas telefónicas.**
- Eliges **"Llamadas desde anuncios"** (call ads / asset de llamada — la más fácil, no necesita tocar la web) o **"Llamadas a un número en tu sitio web"** (necesita un fragmento que reemplaza el número en la página; lo pone tu dev o se hace vía Google Tag → engineer_visualopen_lushows si se complica).
- Fijas la **duración mínima** (60 s recomendado) y el **valor** (puedes poner un valor estimado por llamada calificada para empezar a ver retorno).

La duración mínima es un filtro grueso, no perfecto: alguien puede hablar 70 s y no comprar; otro cierra en 50 s. Por eso el siguiente nivel es marcar **cuáles de esas llamadas terminaron en venta** y subirlas como conversión con valor real vía **OCI desde llamadas** (ver 53). Ahí Google deja de optimizar por "llamó mucho" y optimiza por "llamó Y compró" — el upgrade que separa una cuenta que parece andar de una que factura (ver 64 ROAS-real).

## Cuándo la llamada le gana a la web (y a WhatsApp)

La llamada gana cuando:

- **Hay urgencia.** "Se inundó la cocina" no llena formularios, marca al instante.
- **El ticket es alto o complejo** y el cliente necesita preguntar antes de confiar (high-ticket → ver 58).
- **Tu web no convierte** o no tienes una landing decente todavía. Una buena llamada tapa una mala web; lo inverso no.
- **Tu cliente es mayor o poco digital** y prefiere voz.

La **web** gana cuando el cliente compara con calma y quiere ver fotos/precios antes. El **WhatsApp** gana cuando el cliente prefiere escribir, está fuera de horario, o cuando el volumen es alto y no tienes quién conteste tanto teléfono — ahí mejor un chat que recoja y cierre con calma (ver 52 lead-form, 54, ventas_lushows 82). En LatAm muchas veces la jugada ganadora es **dar las tres puertas**: llamar, WhatsApp y web, y medir cuál cierra mejor para meterle más plata a esa. No adivines: el call tracking + las conversiones de WhatsApp te dicen cuál rinde.

## Plantilla rápida (servicio urgente, Bogotá)

- Campaña Search, keywords exactas/frase urgentes: `[cerrajero 24 horas]`, `[grúa bogotá ahora]`, `"plomero urgente"`.
- **Call ads** en esas keywords (solo móvil) + **asset de llamada** en toda la cuenta con horario real.
- Conversión "llamada ≥60 s" como objetivo, Smart Bidding maximizar conversiones (ver 15).
- Geo: solo tu radio de cobertura (ver 26, 57). Negativos: "gratis", "cómo", "tutorial", "empleo" (ver 22).
- Continuo: escuchar/revisar las llamadas → cosechar keywords buenas y negativizar basura → marcar ventas y subirlas con OCI (ver 53, 68).

## Errores comunes — blacklist

1. **Poner call ads y no tener quién conteste.** El peor desperdicio: pagas el clic, suena, nadie atiende, el cliente llama a otro. Programa horario o no lo lances (si derivas a WhatsApp, respeta businessHours del bot).
2. **No prender call tracking.** Si no mides la llamada, vuelas a ciegas y Smart Bidding no puede optimizar a llamadas. Sin medición, no hay optimización.
3. **Contar toda llamada como conversión.** Sin duración mínima cuentas equivocados y spam. Pon 60 s para filtrar el ruido.
4. **Quedarte solo en "duración mínima".** Una llamada larga no es una venta. Sube las que sí compraron con OCI y valor real (ver 53) para optimizar por plata, no por charla.
5. **Solo call ads, sin asset de llamada en Search normal.** Pierdes a quien quiere ver la web primero. El asset es gratis de agregar: ponlo en todos los anuncios.
6. **Ignorar el horario del negocio.** Mostrar el botón de llamar 24/7 cuando atiendes de 8 a 6 quema clics de madrugada. Programa el asset.
7. **No escuchar las llamadas.** El call tracking reporta duración y, según setup, graba: revisarlas te dice qué keywords traen prospectos reales y cuáles basura — research gratis para tus negativos (ver 68 search-terms, 22 negativas).

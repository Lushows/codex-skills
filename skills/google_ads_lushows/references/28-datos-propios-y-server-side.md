# 28 — Datos propios y server-side

Lee este módulo cuando ya tienes campañas corriendo y quieres que MIDAN mejor en un mundo donde las cookies se mueren y los navegadores bloquean rastreo — o cuando tu medición "se siente floja" y subreportas conversiones. Este es el módulo más técnico de la sección, pero el concepto es simple: mientras más datos PROPIOS (first-party) le des a Google de forma robusta, mejor optimiza el Smart Bidding y más conversiones recupera de las que el bloqueo de cookies te oculta. En 2026, **medir bien es una ventaja competitiva**, no un detalle técnico. Frame: Google captura intención, pero solo aprende a quién buscar si le confirmas bien quién compró; medición floja = algoritmo ciego = CPA inflado.

## El problema: por qué tu medición pierde conversiones

El rastreo tradicional vive en el navegador (cookies, JavaScript). Tres cosas lo rompen:
- **Navegadores que bloquean** cookies de terceros (Safari y Firefox ya; Chrome con controles de usuario que reducen el rastreo).
- **Bloqueadores de anuncios** que matan los scripts de medición.
- **ITP/iOS** que acorta la vida de las cookies a días.

Resultado: pierdes conversiones que SÍ ocurrieron pero el navegador no reportó. Tu cuenta se ve peor de lo que es, y peor aún, el Smart Bidding aprende con datos incompletos y optimiza mal. Subreportar típicamente va del 10% al 30% de las conversiones reales — suficiente para que apagues campañas que en realidad ganaban. La respuesta de Google a esto son cuatro herramientas que se apoyan en tus datos propios.

## Las 4 herramientas first-party (de simple a robusta)

| Herramienta | Qué hace | Esfuerzo | ROI relativo |
|---|---|---|---|
| **Enhanced Conversions** (Conversiones mejoradas) | Cuando alguien convierte, manda a Google su email/teléfono **hasheado** para casar la conversión con el usuario aunque la cookie falle | Bajo-medio | Altísimo |
| **Customer Match** | Subes tu CRM hasheado como audiencia (ver 25) | Bajo | Alto |
| **OCI** (conversiones offline) | Subes ventas/leads que se cerraron FUERA de la web, atadas al GCLID (ver 53) | Medio | Alto (B2B) |
| **Server-side tagging** (GTM server) | Mueves la medición del navegador a TU servidor — más resistente a bloqueos | Alto | Medio (según gasto) |

### Enhanced Conversions — el "arréglalo primero"
Lo más rentable de activar. Cuando alguien compra/se registra, tu sitio ya tiene su email (lo escribió en el checkout/formulario). Enhanced Conversions toma ese dato, lo **hashea** (cifra irreversible, igual que Customer Match — ver 25) y se lo manda a Google para confirmar la conversión incluso si la cookie murió. Recupera conversiones que estabas perdiendo (típicamente recupera 5–15% más conversiones reportadas). Se activa por **Google Tag/GTM** o por la **API de conversiones**; verifica en Google Ads → Objetivos → Conversiones → Diagnóstico que esté "recibiendo datos hasheados". Hay variante **Enhanced Conversions for Leads** (ver 53) específica para negocios de leads/B2B que ata el lead offline sin GCLID, usando el email hasheado. Actívalo: es de lo que más ROI da por hora de trabajo.

### Server-side tagging (GTM server)
GTM = Google Tag Manager (gestor de etiquetas de Google, donde administras tus scripts de medición sin tocar código). La versión **server-side** corre en un contenedor en TU servidor (un Cloud Run en Google Cloud, por ejemplo): el navegador manda el dato a tu servidor, y tu servidor se lo pasa a Google. Ventajas:
- Más resistente a bloqueadores (el dato no depende solo del navegador).
- Tú controlas qué datos salen (mejor para privacidad y cumplimiento — ver 29).
- Datos más limpios y completos → mejor Smart Bidding.
- Reduce pérdida por ITP/iOS al extender la vida de cookies first-party.

Costo honesto: requiere montar y mantener un servidor (cuesta plata mensual de hosting, ~$50.000–$200.000 COP/mes en Cloud Run según tráfico) y conocimiento técnico. **No es para todos.** Si tu presupuesto de pauta es chico ($1-2M COP/mes), Enhanced Conversions + Customer Match te dan el 80% del beneficio sin el dolor del server-side. Reserva GTM server para cuando el gasto justifique la inversión técnica (la ingeniería la cubre `engineer_visualopen_lushows`).

## El orden correcto de implementación

No hagas todo a la vez. Prioriza por ROI/esfuerzo:

1. **Google tag bien puesto** en todo el sitio + conversiones bien definidas (ver 14). Sin esto, nada de lo demás sirve. Verifica con la extensión Google Tag Assistant que dispara en la página de "gracias".
2. **Enhanced Conversions** activado (poco esfuerzo, mucho retorno).
3. **Consent Mode v2** funcionando (ver 29) — sin él, en región regulada las funciones first-party se degradan.
4. **Customer Match** subiendo tu CRM (ver 25).
5. **OCI / Enhanced Conversions for Leads** si vendes leads/B2B (ver 53).
6. **Server-side tagging** solo si el gasto y la madurez lo justifican.

Cada paso le da a Google datos más completos y propios → el Smart Bidding optimiza mejor → tu CPA real baja. Y todo se apoya en tus datos first-party, que es lo que sobrevive al fin de las cookies. Quien mida mejor, gana la subasta con menos plata.

## Cómo saber si tu medición está rota (diagnóstico)

Antes de gastar más, verifica que mides bien. Señales de que estás subreportando:

| Síntoma | Causa probable | Arreglo |
|---|---|---|
| Google reporta menos ventas que tu CRM/pasarela | Cookies bloqueadas, sin Enhanced Conversions | Activa Enhanced Conversions (ver arriba) |
| El CPA "subió" de un mes a otro sin cambiar nada | Pérdida de medición por actualización de navegador/iOS | Revisa diagnóstico de conversiones; monta server-side si el gasto lo amerita |
| Conversiones contadas el doble | Etiqueta duplicada (tag + GTM + server) | Audita con Tag Assistant que dispare 1 vez |
| "Recibiendo datos hasheados: No" en el diagnóstico | Enhanced Conversions mal montado | Revisa que el campo email/teléfono se pase al tag |
| Atribución rara (todo a "directo") | GCLID no se conserva en la URL | Verifica que el GCLID llegue a la landing y al checkout |

Compara siempre Google Ads contra tu **fuente de verdad** (la pasarela de pago, `data/orders.json`, tu CRM). Si Google dice 40 ventas y tu pasarela dice 55, estás subreportando ~27% — y el Smart Bidding está optimizando con esa ceguera, dejando dinero en la mesa. La meta no es que coincidan al 100% (siempre hay desfase por atribución y ventanas), sino cerrar la brecha de 30% a menos de 10%.

**Regla de oro de la sección 28:** nunca recortes presupuesto ni apagues una campaña por un CPA feo sin antes confirmar que la medición es confiable. Apagar una campaña que sí vendía porque la medición la subreportaba es uno de los errores más caros y comunes — y silencioso, porque "los números decían que iba mal".

## Errores comunes — blacklist

1. **Montar server-side antes de lo básico.** Si no tienes ni Enhanced Conversions ni conversiones bien definidas, el GTM server no te salva. Orden: básico primero.
2. **Saltarte Enhanced Conversions.** Es el mayor retorno por hora de trabajo y casi nadie lo activa. Préndelo ya.
3. **Pagar un GTM server con presupuesto chico.** El hosting y mantenimiento no se justifican si gastas poco en pauta. Enhanced Conversions + Customer Match te dan casi todo sin ese costo.
4. **Creer que más medición = saltarte la ley.** Todo first-party necesita consentimiento y Consent Mode bien puesto (ver 29). Medir mejor no exime de cumplir.
5. **No verificar que Enhanced Conversions recibe datos.** Revisa el diagnóstico en Google Ads (sección Conversiones): si dice "no recibe datos hasheados", está mal montado y no sirve.
6. **Confundir Customer Match (audiencia) con Enhanced Conversions (medición).** Customer Match es a QUIÉN le muestras; Enhanced Conversions es CÓMO confirmas la venta. Ambas usan hash pero hacen cosas distintas.
7. **Subreportar y luego bajar pujas por pánico.** Si tu medición pierde conversiones, tu CPA se ve peor del real. Arregla la medición ANTES de recortar presupuesto, o apagarás campañas que sí funcionaban.
8. **Doble conteo por etiquetas duplicadas.** Si montas Google tag Y GTM Y server-side sin coordinar, puedes contar la misma conversión 2-3 veces y sobre-optimizar. Audita que cada conversión se cuente UNA vez.

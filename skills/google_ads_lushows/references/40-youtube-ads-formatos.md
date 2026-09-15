# 40 — YouTube Ads: formatos

Lee este módulo cuando quieras pautar en YouTube y no sepas qué formato elegir, o cuando estés gastando en video y no entiendas por qué cobran "por vista" en una campaña y "por mil impresiones" en otra. YouTube es de Google, así que aquí seguimos **capturando** intención (la persona ya está dentro del ecosistema viendo algo, con un historial de búsquedas que Google conoce), pero el video también **genera** consideración y demanda — la frontera con Meta (`facebook_ads_lushows`) es fina: Meta interrumpe a quien no te buscaba; YouTube te pone frente a quien ya muestra señales de interés a través de sus búsquedas, sus suscripciones y lo que ve. Esa señal de intención es la ventaja que ninguna red social tiene.

Antes de pautar un solo peso en video, la **dirección de arte y el guion** los manda otra disciplina: el concepto, el storyboard y el look del video se trabajan en `directorcreativo_lushows`. Aquí solo decidimos formato, objetivo y cómo se cobra. La estructura de performance del clip (hook, beneficio, CTA) está en 42; las variantes para testear, en 49.

## Los formatos a jun-2026 — qué son y cómo cobran

"Skippable" significa **saltable**: a los 5 segundos aparece el botón *Saltar anuncio* y el espectador decide si sigue o se va. "Bumper" es un anuncio corto **no saltable** de 6 segundos. "In-feed" es un anuncio que aparece como un video más en resultados, en la página de inicio de YouTube o al lado de otros videos, y la persona elige hacer clic. "Shorts" son los verticales tipo TikTok/Reels dentro de YouTube — y a jun-2026 son la superficie de mayor crecimiento de inventario en LatAm, con costo por vista más bajo que el in-stream tradicional.

| Formato | Qué es | Duración | Cómo cobra | Para qué sirve |
|---|---|---|---|---|
| Skippable in-stream | Saltable a los 5s, antes/durante el video | 15s–3min (ideal 15–30s) | CPV (≥30s o clic) o por acción/conversión (tCPA) | Consideración y **acción** (lead, WhatsApp) |
| Non-skippable in-stream | No se puede saltar | hasta 15s (hasta 30s en algunos mercados) | CPM (mil impresiones) | Awareness con mensaje completo garantizado |
| Bumper 6s | No saltable, ultracorto | 6s exactos | CPM | Recordación de marca, refuerzo de frecuencia |
| In-feed | Aparece como sugerencia, la persona hace clic | Libre | CPV (clic al video) | Consideración, contenido que invita a ver |
| Shorts ads | Vertical, entre Shorts | 9:16, hasta 60s (ideal <30s) | CPM / CPV / acción según objetivo | Alcance barato, audiencias jóvenes, volumen móvil |

El dato que más confunde: en **skippable** solo pagas si la persona ve 30 segundos (o el video completo si dura menos) o interactúa. Es decir, **el que te salta antes de 30s no te cuesta**. Por eso el skippable es el formato más eficiente para presupuestos chicos en Colombia: el filtro lo paga Google, no tú. Si tu campaña usa puja por conversión (tCPA, ver 13), ya ni piensas en CPV — pagas por resultado y Google decide a quién mostrarle para conseguirlo.

### Números de referencia Colombia (jun-2026, órdenes de magnitud)

No son tarifas oficiales —Google no publica precios— sino rangos típicos que verás en cuentas reales de pyme colombiana. Sirven para saber si te están cobrando caro:

| Métrica | Rango típico Colombia |
|---|---|
| CPV skippable in-stream | $40–$150 COP por vista |
| CPV Shorts | $25–$90 COP por vista (más barato) |
| CPM bumper / non-skippable | $8.000–$25.000 COP por mil impresiones |
| CPA lead WhatsApp (video→Demand Gen) | $3.000–$15.000 COP por chat iniciado, según nicho |

Si te cobran $400 COP por vista en skippable, algo está mal: hook flojo (te saltan y Google compite por los pocos que se quedan), audiencia mal armada o puja descontrolada (ver 15, 42).

## Qué formato según el objetivo

No elijas por gusto; elige por la etapa del embudo (ver 41 demand-gen, 45 ctas-video).

- **Acción / lead / WhatsApp (lo que más te interesa en LatAm):** skippable in-stream con objetivo de conversión, o mejor aún, mételo dentro de **Demand Gen** (ver 41), que es la campaña de Google más parecida a Meta y la que mejor lleva a destino lead/WhatsApp/llamada (ver 46). El video skippable con CTA es tu caballo de batalla.
- **Consideración:** skippable in-stream + in-feed. Dejas que la gente decida verte; los que se quedan son los tibios que calientan.
- **Awareness puro (marca nueva, lanzamiento grande):** bumper 6s + non-skippable. Aquí pagas por CPM, así que mides **alcance, frecuencia y recordación**, no clics. No esperes ventas directas de un bumper: su trabajo es que te recuerden, no que te compren hoy.

**Regla de presupuesto Colombia:** con menos de $1.500.000 COP/mes **no hagas awareness puro** (bumper/non-skippable). No tienes plata para "que te recuerden"; necesitas que te escriban. Pon todo en skippable-acción o Demand Gen con destino WhatsApp. El awareness es un lujo de cuentas con $5–10M/mes que ya tienen captura cubierta.

## El detalle que decide todo: los primeros 5 segundos

En skippable, el espectador puede saltarte a los 5s. Si tu video arranca con logo, música de intro o "Hola, somos…", ya perdiste. El **hook en 5 segundos** —decir el problema o la promesa antes de que aparezca el botón Skip— es la diferencia entre pagar por gente que se queda y pagar por nadie. Esto es tan importante que tiene módulo propio (ver 42 creativo-de-video y 49 testing-de-video). El formato no salva un mal hook: un bumper malo es 6 segundos de plata quemada, y un skippable sin gancho hace que Google solo te muestre a quien no salta nunca (audiencia chatarra), encareciéndote el CPV.

## IA y assets: lo que cambió en jun-2026

Google integró **Gemini** dentro de Google Ads para generar y adaptar assets de video: a partir de un brief o de imágenes puedes pedir variaciones de la apertura, recortes verticales para Shorts, o **image-to-video** (animar un asset estático). Eso acelera tener las proporciones que cada formato pide sin rodar de nuevo (ver 91 IA-assets, 42 specs). Pero la IA produce variaciones; el **concepto madre y el look** los dirige `directorcreativo_lushows`. Variar un mal concepto da más basura, más rápido.

## Plantilla de brief para elegir formato

Llena esto antes de abrir la campaña:

```
NEGOCIO: [ej. GastroLatam — calculadora de costos Excel]
OBJETIVO: [ ] acción/lead  [ ] consideración  [ ] awareness
DESTINO: [ ] WhatsApp  [ ] lead form  [ ] llamada  [ ] landing
PRESUPUESTO/MES: $______ COP
TENGO VIDEO: [ ] sí, ¿proporciones? 16:9 / 9:16 / 1:1   [ ] no (→ produce primero)
HOOK (primeros 5s, una frase): "________________________"
→ FORMATO RECOMENDADO:
  - <$1.5M/mes + destino WhatsApp → Skippable-acción dentro de Demand Gen (41)
  - quiero solo video YouTube puro + acción → Skippable in-stream tCPA
  - volumen móvil joven barato → Shorts ads
  - lanzamiento con plata → Bumper 6s + non-skippable (awareness)
```

## Errores comunes — blacklist

1. **Hacer bumper/non-skippable con presupuesto chico.** Pagas CPM por "recordación" que no te deja ventas. Con poca plata, todo a skippable-acción o Demand Gen.
2. **Creer que el que te salta te cobra.** En skippable por CPV solo pagas vista de 30s+ o interacción. Salir antes no te cuesta — deja de obsesionarte con la tasa de salto temprana (úsala como señal de hook, ver 49).
3. **Meter el logo y la intro en los primeros 5 segundos.** Es regalarle el Skip al espectador. El gancho va primero, la marca después (ver 42).
4. **Confundir CPM con CPA.** Un bumper se mide por alcance; pedirle conversiones es pedirle peras al olmo. Cada formato tiene su métrica (ver 49).
5. **Pautar video sin dirección de arte.** Un video improvisado quema plata más rápido que un Search mal armado. El concepto va en `directorcreativo_lushows` antes de tocar la campaña.
6. **Usar el mismo video horizontal en Shorts.** Shorts es 9:16 vertical; un horizontal ahí se ve amateur y lo saltan. Adapta el formato (ver 42 specs; recorta con Gemini, ver 91).
7. **No definir el destino antes de elegir formato.** Si quieres WhatsApp/lead, el formato y la campaña (Demand Gen, ver 46) cambian. Define el destino primero, el formato después.
8. **Aceptar un CPV inflado sin investigar.** $300–400 COP/vista en Colombia casi siempre es hook flojo o audiencia mal armada, no "así es YouTube" (ver 15, 42).

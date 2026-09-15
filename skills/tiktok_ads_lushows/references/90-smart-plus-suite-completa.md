# 90 — Smart+ suite completa

Lee este módulo cuando vayas a abrir tu primera campaña automatizada en TikTok, cuando vengas de Advantage+ (Meta) o Performance Max (Google) y quieras el equivalente en TikTok, o cuando no sepas si dejar que la máquina decida o controlar tú a mano. Aquí está el mapa completo de **Smart+** y **GMV Max** — qué hacen, qué automatizan y, lo más importante, qué NO debes soltarles. TikTok es **descubrimiento**: la automatización solo amplifica lo que el creativo ya logra (ver 92); no inventa demanda donde el video no la enciende.

## Qué es Smart+ y qué automatiza

**Smart+** (se lee "smart plus") es la suite de automatización de campañas de TikTok: tú le das el objetivo, el presupuesto, el creativo y la fuente de conversión, y el sistema decide **públicos, pujas, ubicaciones y combinación de creativos** con IA. Es el equivalente directo de **Advantage+** de Meta (→ `facebook_ads_lushows`) y de **Performance Max** de Google (→ `google_ads_lushows`). Misma filosofía: menos palancas, más IA, el creativo manda.

A jun-2026 hay cuatro tipos de Smart+ según tu objetivo:

| Tipo | Para qué sirve | Señal que necesita | Equivalente Meta/Google |
|---|---|---|---|
| **Smart+ Web** | Conversiones en tu sitio/landing (compras, formularios) vía Pixel/Events API (ver 06) | 15+ conversiones/semana del evento objetivo | Advantage+ Shopping / PMax sin feed |
| **Smart+ Catalog** | Venta de catálogo con feed de productos (e-commerce) | Catálogo cargado + pixel con eventos de producto | Advantage+ Catalog / PMax con Merchant |
| **Smart+ App** | Instalaciones y eventos in-app | SDK/MMP (AppsFlyer, Adjust) midiendo eventos | Advantage+ App |
| **Smart+ Lead** | Generación de leads con formulario nativo (Instant Form) | Eventos de lead calificado (no solo "envío form") | Advantage+ Leads |

Aparte de Smart+ existe **GMV Max** (GMV = Gross Merchandise Value, el valor total vendido): es la automatización **de TikTok Shop** (ver 52). No es lo mismo que Smart+. GMV Max optimiza ventas DENTRO de TikTok Shop sin que tú armes campañas — el sistema combina anuncios de video, en vivo (LIVE) y de producto, y empuja tus productos a quien más probable compra, optimizando a ROAS objetivo. Si vendes por Shop, vas a GMV Max; si vendes hacia tu web o WhatsApp, vas a Smart+ Web/Lead.

### Mapa de qué automatiza Smart+ por dentro

| Palanca | Quién decide en Smart+ | Lo que tú igual controlas |
|---|---|---|
| Público | IA (broad, lee el creativo, ver 92) | Exclusiones (compradores, listas) |
| Puja / bid | IA (cost cap implícito o lowest cost) | El objetivo de costo (target CPA/ROAS) si lo activas |
| Presupuesto | IA reparte entre creativos | El **tope total** (CBO a nivel campaña) |
| Ubicaciones | IA (For You y red) | Puedes forzar exclusiones de red de audiencia |
| Creativos | IA mezcla/rota lo que subes | **El material**: tú subes los videos (la IA no graba) |
| Optimization event | — | **Tú lo eliges** (compra real, no "ver contenido", ver 06) |

## Qué automatizar y qué controlar (la regla)

Smart+ automatiza bien lo aburrido (pujar, repartir presupuesto, mezclar creativos). Pero hay cosas que **nunca** debes soltarle porque la máquina no las sabe mejor que tú:

| Lo SUELTAS a Smart+ (déjalo decidir) | Lo CONTROLAS tú (no negociable) |
|---|---|
| Público (deja broad — el creativo segmenta, ver 30) | El **creativo nativo** que subes (la IA solo mezcla lo que le das) |
| Puja y reparto del presupuesto | El **evento de conversión correcto** (compra real, no "ver contenido", ver 06) |
| Combinación y rotación de creativos | Las **exclusiones**: compradores recientes, marcas vetadas, ubicaciones que no quieres |
| Ubicaciones (For You, etc.) | El **tope de presupuesto** que aguanta tu caja (viabilidad → `economist_lushows`) |
| El timing de cuándo mostrar | Las **políticas**: que el creativo cumpla (ver 08) o se rechaza todo |

La trampa más cara: Smart+ es tan bueno automatizando que la gente cree que también arregla el creativo. **No lo hace.** Smart+ *lee* tu creativo para targetear (ver 92), pero si subes un solo video flojo, la mejor IA del mundo no tiene material con qué trabajar. Smart+ con 3–5 ángulos nativos vuela; Smart+ con un ad pulido reusado de Meta se quema igual (ver 30).

Otra: el **evento de optimización**. Si optimizas a un evento barato y temprano (clic, "ver contenido"), Smart+ te trae tráfico que clickea pero no compra. Optimiza al evento más cercano a la plata que tengas señal suficiente (compra, lead calificado, ver 06 y 16). En LatAm donde el cierre real pasa por WhatsApp, eso obliga a devolver la conversión offline para que Smart+ no optimice a ciegas (ver 96).

## Cuándo Smart+ y cuándo manual

No es religión — es presupuesto y madurez de datos.

| Situación | Usa | Por qué |
|---|---|---|
| Pixel/Events API ya manda compras (15+/semana) | **Smart+ Web** | La IA tiene señal para optimizar |
| Recién instalas el pixel, 0 datos | **Manual** (ABO o testeo de creativos) | Smart+ sin datos aprende a ciegas; primero junta señal |
| Vendes por TikTok Shop | **GMV Max** | Es su automatización nativa, más directa (ver 52) |
| Quieres testear hooks/ángulos limpio | **Manual** | Necesitas leer creativo por creativo, no que la IA los mezcle (ver 32) |
| Cuenta madura, quieres escalar el ganador | **Smart+** | Ya sabes qué funciona; deja que escale solo |
| Quieres leads de WhatsApp para tu negocio | **Smart+ Lead** (con offline) | Pero la calidad la mides tú, no la cantidad de forms |

Flujo recomendado para Colombia/LatAm con presupuesto chico ($30.000–$100.000 COP/día): **arranca manual** para encontrar el creativo ganador y juntar señal, **migra a Smart+** cuando tengas datos y un ganador claro. Saltar directo a Smart+ con cuenta nueva quema plata en aprendizaje. El playbook completo día-a-día está en 98.

### Migración manual → Smart+ sin matar lo que funciona

1. Confirma señal madura: 15+ conversiones/semana del evento correcto y 1–2 creativos ganadores claros (ver 98 semanas 1–4).
2. Crea la campaña Smart+ Web con esos ganadores + 1–2 ángulos frescos (no solo el ganador, dale material para mezclar).
3. Define el optimization event en compra/lead calificado y pon target CPA realista (tu CAC máximo, → `economist_lushows`).
4. **Deja correr las manuales 5–7 días en paralelo** mientras Smart+ sale de aprendizaje. No apagues lo que paga hoy por una promesa.
5. Cuando el CPA de Smart+ iguale o mejore al manual de forma estable, baja el manual gradualmente. Mide por MER global, no por el panel (ver 97).
6. Vigila fatiga: Smart+ también satura su audiencia natural; refresca creativo cada semana (ver 39, 92).

## La Suite que conecta todo

Smart+ vive dentro del stack 2026: se alimenta de **Symphony** (creativos IA a escala, ver 91), lee el **algoritmo** (ver 92), espía con **Creative Center** (ver 94), y cierra el círculo con **Events API + conversión offline** (ver 96). Visto completo en 90–98; aquí solo la pieza de automatización de campañas.

## Errores comunes — blacklist

- **Abrir Smart+ con pixel recién instalado y 0 conversiones.** Sin señal, la IA optimiza a ciegas. Junta datos primero (ver 06).
- **Creer que Smart+ arregla un creativo malo.** Smart+ mezcla lo que le das; basura entra, basura sale. El creativo sigue siendo tuyo (ver 30).
- **Optimizar a un evento barato (clic, ver contenido) en vez de compra/lead.** Trae tráfico que no convierte (ver 16).
- **No poner exclusiones** (compradores recientes, ubicaciones malas) y dejar que Smart+ gaste en quien ya compró.
- **Confundir Smart+ con GMV Max.** Smart+ va hacia tu web/lead; GMV Max es para TikTok Shop (ver 52).
- **Soltar el presupuesto sin tope que aguante la caja.** La IA gasta lo que le des; el límite lo pones tú (→ `economist_lushows`).
- **Mover a Smart+ y borrar las campañas manuales el mismo día.** Migra con solape; deja que Smart+ aprenda antes de apagar lo que funciona.
- **Subir un solo creativo a Smart+.** Necesita varios ángulos para mezclar y segmentar; uno solo lo satura rápido (ver 38, 92).
- **No devolver la conversión offline cuando vendes por WhatsApp.** Smart+ optimiza a ciegas a la cantidad de leads, no a la venta (ver 96).

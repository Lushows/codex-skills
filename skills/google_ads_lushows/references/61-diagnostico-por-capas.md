# 61 — Diagnóstico por capas

Lee este módulo cuando "la pauta no funciona" pero no sabes **dónde** falla, cuando subes presupuesto y no pasa nada, o cuando vas a tocar cinco cosas a la vez sin saber cuál es la culpable. Aquí hay un método: la venta en Search pasa por capas, y cada capa se rompe distinto y se arregla distinto. Tocar la capa equivocada es perder plata y tiempo.

Frame: Google **captura intención**. Si alguien ya te busca, la venta solo se pierde por una de cuatro razones: no apareciste, no te hicieron clic, no convirtieron, o no lo estás midiendo bien. Esas son las capas. No hay una quinta.

Las capas, en orden de la búsqueda a la venta:

```
[1 ¿Aparezco?] → [2 ¿Me hacen clic?] → [3 ¿Convierten?] → [0 ¿Lo estoy midiendo bien?]
   Impression Share    CTR                CVR/CPA            GA4 / conversiones
```

La capa 0 (medición) va al final en el dibujo pero **se revisa primero**: si la medición está rota, todas las otras métricas mienten y diagnosticas sobre datos falsos (ver 62). En 2026 esto es más importante que nunca: con atribución data-driven por defecto y conversiones modeladas (Consent Mode), una buena parte de tu data es estimada, no contada 1:1. Si la base está sucia, todo lo de arriba es ficción.

## Capa por capa: síntoma → causa → fix

| Capa | Síntoma | Causa probable | Fix (acción exacta) |
|---|---|---|---|
| **0 Medición** | ROAS/conversiones no cuadran con el banco; cifras que "bailan" | Conversiones mal configuradas, duplicadas o no importadas | Verifica en GA4 DebugView; revisa import a Ads (ver 62, 53) **antes** de tocar nada |
| **1 Aparición** | Pocas impresiones, IS bajo | Lost IS budget alto → falta plata. Lost IS rank alto → Ad Rank débil | Mira la columna Lost IS (ver 60, 94). Budget → sube presupuesto. Rank → puja/calidad/anuncio |
| **2 Clic** | Muchas impresiones, pocos clics, CTR bajo | Anuncio débil, keyword mal alineada con la búsqueda, o sales en posición baja | Revisa search terms (ver 68): ¿la búsqueda real coincide con tu oferta? Reescribe RSA, agrega negativos (ver 22) |
| **3 Conversión** | Buen CTR, pero CVR baja y CPA alto | Landing lenta/confusa, oferta cara, formulario largo, mal match búsqueda↔página | Audita la landing (ver `desingweb-lushows`); alinea el mensaje anuncio↔página; revisa precio (ver `economist_lushows`) y cierre (ver `ventas_lushows`) |

La clave: **no bajes a la capa siguiente hasta cerrar la anterior**. Si tu IS es 25%, optimizar la landing es prematuro: primero apareces más, luego pules lo que recibes. Diagnosticar al revés (empezar por la conversión cuando el techo está roto) es el error más común de quien lleva poco tiempo en cuentas.

## El árbol de decisión

Cuando algo no funciona, recorre esto en orden, sin saltarte pasos:

1. **¿La medición está sana?** (capa 0) Abre GA4 DebugView, dispara una conversión de prueba, confirma que llega **una sola vez**, con `value` y `currency: COP` correctos, y que se importó a Ads (ver 62). Si está rota → para aquí, arregla, y vuelve. Todo lo demás miente hasta entonces.
2. **¿Estoy apareciendo?** (capa 1) Mira Search IS. Si <40% en genérico, hay techo. Mira **por qué** con las dos columnas:
   - **Lost IS (budget)** alto → ¿el presupuesto da rentable? (ver `economist_lushows`) Si sí, súbelo.
   - **Lost IS (rank)** alto → no es plata. Trabaja Quality Score (relevancia keyword↔anuncio↔landing), puja y anuncio (ver 94 para auction insights).
3. **¿Me hacen clic?** (capa 2) CTR por debajo de rango (ver 60). Revisa el search terms report (ver 68): a veces apareces en búsquedas que no son tuyas (CTR bajo = irrelevancia, no anuncio malo). Agrega negativos (ver 22), reescribe el RSA con ángulos distintos.
4. **¿Convierten los clics?** (capa 3) CVR baja con CTR sano = la culpa está **fuera de Ads**. Landing, oferta o precio. Aquí el 80% de los "Google Ads no sirve" en realidad son landings rotas o precios fuera de mercado.

## Tabla de triangulación: dos métricas → un diagnóstico

El diagnóstico no sale de una métrica, sale del **cruce**. Memoriza esta tabla:

| IS | CTR | CVR | Diagnóstico | Capa a tocar |
|---|---|---|---|---|
| Bajo | — | — | Techo: no apareces lo suficiente | 1 (mira budget vs rank) |
| Alto | Bajo | — | Apareces pero no atraes / búsqueda irrelevante | 2 (search terms + RSA) |
| Alto | Alto | Bajo | Atraes pero no cierras: landing/oferta/precio | 3 (fuera de Ads) |
| Alto | Alto | Alto | Sano: ahora sí escala (sube budget si rentable) | — (ver 64 para MER) |
| Cualquiera | — | "Baila" | Medición rota | 0 (GA4 primero) |

Esta tabla es el corazón del módulo. Si la internalizas, dejas de adivinar.

## Casos típicos mal diagnosticados

**Caso 1.** Cliente: "Subí el presupuesto al doble y las ventas no subieron, Google me robó."
- Capa 1: su Lost IS (rank) era 65%, Lost IS (budget) 5%. **El presupuesto nunca fue el cuello de botella.** Duplicarlo no compró más impresiones porque el problema era Ad Rank, no plata. La plata extra se gastó pujando más caro en las mismas subastas.
- Fix real: subir Quality Score y la puja, no el presupuesto.

**Caso 2.** "Tengo CTR de 9%, buenísimo, pero no vendo."
- Capa 3: CVR de 0.6%. El anuncio atrae clics pero la landing carga en 7 s en móvil y el botón de compra está abajo. No es Google (ver `desingweb-lushows`).

**Caso 3.** "El ROAS cayó de 6 a 4 esta semana, algo se rompió."
- Capa 0: nada se rompió en la pauta. Se actualizó la atribución data-driven y se reasignó crédito; además entró una semana con más tráfico frío. Antes de tocar pujas, verifica medición y triangula con backend (ver 64). Mover palancas por ruido de una semana es destruir aprendizaje del Smart Bidding (ver 13).

## Errores comunes — blacklist

1. **Diagnosticar sin verificar la medición primero.** Optimizas sobre datos falsos y persigues fantasmas. Capa 0 siempre va primero (ver 62).
2. **Subir presupuesto cuando el problema es rank.** El error más caro y más común. Mira Lost IS budget vs rank antes de tocar la plata (ver 94).
3. **Tocar cinco palancas a la vez.** Si mejora, no sabes cuál fue; si empeora, tampoco. Un cambio, mide, siguiente.
4. **Culpar a Google de una landing rota.** CVR baja con CTR sano casi nunca es Ads (ver `desingweb-lushows`).
5. **Optimizar la conversión cuando todavía apareces en el 25% de las búsquedas.** Cierra el techo (IS) antes de pulir lo de abajo.
6. **Ignorar el search terms report.** Es donde ves si apareces en búsquedas que no son tuyas; CTR bajo muchas veces es irrelevancia, no anuncio feo (ver 68).
7. **Asumir que CPA alto = oferta cara.** Puede ser medición rota, IS mal repartido o tráfico irrelevante. Recorre las capas antes de concluir.
8. **Reaccionar al ruido de una semana.** Una caída de ROAS de 7 días puede ser variación normal o reasignación de atribución. Triangula (ver 64) antes de mover Smart Bidding (ver 13).

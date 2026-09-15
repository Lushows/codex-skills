# 68 — Análisis de search terms y assets

Lee este módulo cuando quieras saber qué está funcionando **de verdad** dentro de una campaña, cuando tu CPA suba y no sepas por qué, cuando vayas a limpiar una cuenta heredada, o cuando tengas varios titulares/imágenes y no sepas cuáles dejar. Este es el trabajo semanal que más plata salva y más ventas escala, y casi nadie lo hace bien: leer lo que la gente **realmente buscó** y qué **piezas creativas** ganan, para matar lo malo, iterar lo dudoso y escalar lo bueno.

Frame: Google **captura intención**. El search terms report es la radiografía de **qué intención estás capturando** — y cuánta de esa intención es basura que paga sin convertir. El asset reporting es la radiografía de **qué mensaje convierte esa intención en clic y venta**.

Dos fuentes, dos análisis:
- **Search terms report**: las búsquedas reales que activaron tus anuncios (ver 63).
- **Asset reporting**: qué titulares, descripciones, imágenes y videos rinden dentro de tus anuncios.

## Search terms: del reporte a la acción

**Keyword** = lo que pujas. **Search term** = lo que la persona escribió. La diferencia es donde se gana o se quema plata, sobre todo con concordancia amplia (broad match), que en 2026 —empujada por Smart Bidding— activa tus anuncios en búsquedas que ni imaginaste.

Ve a campaña → **Insights and reports → Search terms**. Cada término real cae en una de tres acciones:

| Lo que ves | Significa | Acción exacta |
|---|---|---|
| Término **relevante** con **conversiones** | Demanda buena que no tenías mapeada | Agrégalo como **keyword nueva** (su propio grupo si tiene volumen) |
| Término **irrelevante** que **gasta** | Plata quemada ("gratis", "empleo", "curso", "pdf gratis" si vendes producto) | Agrégalo como **negativo** (ver 22) |
| Término **relevante** que **NO convierte** | Intención correcta, pero algo falla después | No lo niegues aún; revisa landing/oferta (ver 61) |

Nota 2026: Google muestra cada vez menos términos individuales (agrupa en "search categories" por privacidad, y PMax/AI Max reportan más agregado). Aun así, lo que sí ves manda señal valiosísima — y los **insights de PMax** y las **categorías de búsqueda** complementan lo que falta. No abandones el reporte porque venga más agrupado: el 100% que ves sigue dictando negativos y keywords nuevas.

### La técnica n-gram (la que sube de nivel)

En vez de mirar término por término, busca **palabras repetidas** entre los que no convierten. Un **n-gram** es una secuencia de N palabras: 1-gram = una palabra ("gratis"), 2-gram = dos ("trabajo en"), etc.

Método manual rápido:
1. Exporta el search terms report (botón Download).
2. En la hoja, separa cada término en palabras y cuenta cuáles se repiten entre los que **gastaron sin convertir**.
3. Si "gratis", "barato", "diy", "empleo" o "pdf" aparecen en 30 búsquedas que gastaron $X y trajeron 0 ventas, esa palabra es tu **negativo de oro**: la niegas una vez y limpias 30 búsquedas de golpe.

Ejemplo de hallazgo n-gram:

| 1-gram | Búsquedas | Gasto | Conv. | Veredicto |
|---|---|---|---|---|
| `gratis` | 28 | $340.000 | 0 | Negativo de campaña ya |
| `excel` | 41 | $520.000 | 23 | Oro: keyword nueva + grupo propio |
| `empleo` | 12 | $95.000 | 0 | Negativo |
| `cómo` | 60 | $710.000 | 31 | Intención informativa que SÍ convierte → escalar |

Ir término por término es lento y se te escapan patrones; el n-gram limpia y escala de a bloques. Esto se puede automatizar con scripts (ver 69).

Frecuencia: **semanal** en cuentas activas. El reporte trae búsquedas nuevas cada semana; si no lo revisas, la plata se va en términos basura sin que lo notes.

## Asset reporting: qué pieza creativa gana

En los **RSA (Responsive Search Ads)** tú das varios titulares y descripciones, y Google los combina. En **Performance Max** y **Demand Gen** das imágenes, videos, logos y textos. El **asset reporting** te dice cuáles rinden, con tres etiquetas de performance:

| Etiqueta | Qué significa | Qué hacer |
|---|---|---|
| **Best** | Entre los que mejor rinden | Déjalo; toma su ángulo y haz variantes parecidas (escalar) |
| **Good** | Rinde bien pero no top | Déjalo, observa |
| **Low** | Rinde por debajo | **Reemplázalo** por algo nuevo (iterar/matar) |
| **"Pending" / "Learning"** | Sin datos suficientes aún | Espera, no toques todavía |

El ciclo de mejora de assets:
1. Mira el asset reporting (en el anuncio → "View asset details" o pestaña **Assets**).
2. **Mata** los `Low`: reemplázalos por ideas nuevas.
3. **Itera** sobre los `Best`: ¿qué ángulo usaron? (precio, urgencia, beneficio, prueba social). Haz 2–3 variantes de ese ángulo ganador.
4. **Escala**: el ángulo que gana en assets es el que debe guiar tu copy y tus landings. La página la trabajas con `desingweb-lushows`; el oficio de persuadir y cerrar (los ángulos de mensaje que mueven a comprar) es `ventas_lushows`; la coherencia visual/marca de las piezas creativas es `directorcreativo_lushows`.

Lectura 2026 sobre PMax y AI Max: con más automatización, el asset reporting es de las pocas palancas creativas que **sí** controlas. Aliméntalo bien: dale **variedad real** de ángulos para que Google tenga con qué combinar y para que las etiquetas Best/Low signifiquen algo. Un RSA con 3 titulares casi idénticos no le enseña nada a nadie.

## Matar / iterar / escalar — el resumen mental

Toda esta sección se reduce a tres verbos sobre cada término y cada asset:

- **Matar**: término irrelevante que gasta → negativo. Asset `Low` → reemplazar. Sin piedad, semanal.
- **Iterar**: término que convierte poco con buena intención → arregla landing/oferta (ver 61). Asset dudoso → variante nueva del ángulo.
- **Escalar**: término que convierte → keyword nueva con su presupuesto. Asset `Best` → más variantes de ese ángulo, súbelo a tu copy y a tu landing.

Esto es optimización real: no es "subir el presupuesto", es **reasignar hacia lo que ya demostró que funciona** y cortar lo que ya demostró que no. El dinero rinde más moviéndose hacia términos y ángulos ganadores que echándole más a la campaña entera (ver 64 para no escalar algo que no es incremental, 65).

## Plantilla de revisión semanal (cópiala)

```
SEMANA: ______  CUENTA: ______
SEARCH TERMS
  • Negativos nuevos agregados:  __________________ (n-grams: ______)
  • Keywords nuevas (convirtieron): _________________
  • Términos buena-intención sin conversión → revisar landing: _______
ASSETS
  • Low reemplazados:  ______   por (ángulo nuevo): ______
  • Best detectados (ángulo ganador): ______ → variantes creadas: ___
DECISIÓN: presupuesto movido de ______ hacia ______ porque ______
```

## Errores comunes — blacklist

1. **No revisar el search terms report.** Es el reporte más rentable de la plataforma y el más abandonado. Semanal, sin excusa (ver 63).
2. **Negar un término relevante porque "no convirtió todavía".** Si la intención es buena, el problema puede ser la landing (ver 61). Negarlo te corta demanda real.
3. **Negar término por término en vez de buscar n-grams.** Una palabra repetida niega 30 búsquedas de un golpe; ir una por una es lento y se te escapan patrones.
4. **Ignorar el asset reporting.** Si no matas los `Low` ni escalas los `Best`, tus anuncios se estancan en lo mediocre.
5. **Dar 3 titulares casi idénticos al RSA.** Sin variedad, Google no tiene qué combinar ni tú qué aprender. Dale ángulos distintos (ver `ventas_lushows`, `directorcreativo_lushows`).
6. **Tocar assets en "Learning/Pending".** Sin datos suficientes, cualquier decisión es ruido. Espera a que tengan etiqueta real.
7. **Optimizar subiendo presupuesto en vez de reasignar.** El dinero rinde más moviéndolo hacia términos y ángulos ya ganadores (ver 64).
8. **Abandonar el reporte porque viene más agregado en 2026.** El 100% de términos que sí ves sigue dictando negativos y keywords; complementa con insights de PMax y categorías de búsqueda.

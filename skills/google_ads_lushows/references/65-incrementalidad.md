# 65 — Incrementalidad

Lee este módulo cuando tu ROAS de remarketing o de marca se ve "espectacular" y quieres saber si es real, cuando vas a justificar el presupuesto de una campaña ante tu jefe/cliente, o cuando sospechas que estás pagando por ventas que de todos modos iban a pasar. Esta es la pregunta más incómoda y más importante del marketing de respuesta directa: **¿esa venta era tuya, o ya iba a pasar sin ti?** Si la venta ocurría igual, no pagaste por una venta: pagaste por colgarte una medalla ajena.

**Incrementalidad** = cuántas ventas existen **gracias a** la campaña que **no hubieran ocurrido sin ella**. Una campaña con ROAS 10 pero incrementalidad cero no genera ni un peso nuevo: te estás atribuyendo lo que ya tenías. El ROAS del panel (ver 64) no distingue esto; la incrementalidad es lo único que lo separa.

## Dónde se esconde el autoengaño

Hay dos tipos de campaña que casi siempre **inflan** su crédito porque agarran demanda que ya estaba decidida:

| Campaña | Por qué se cuelga medallas ajenas |
|---|---|
| **Marca** (ver 39) | Alguien busca el nombre exacto de tu negocio. Ya te conoce, ya te iba a comprar. El anuncio de marca cobra una venta que el orgánico (gratis) iba a capturar igual |
| **Remarketing** | Le muestras anuncios a gente que ya visitó/agregó al carrito. Muchos compraban igual; el anuncio solo estuvo "ahí cuando pasó" |

Esto NO significa "apaga marca y remarketing". Significa: **no asumas que su ROAS alto es incremental.** Parte sí lo es —defiendes la marca de competidores que te pujan encima (ver 94); recuperas carritos que de verdad se iban a perder. Pero parte es humo. La única forma de saber cuánto es real es **medir**, no suponer.

La demanda **genérica** (gente que busca "calculadora de costos restaurante" sin conocerte) es casi siempre incremental: esa venta no existía sin ti. Por eso es la que mejor juzga si tu cuenta crece de verdad (ver 64). Frame del módulo entero: Google **captura intención**; la pregunta de incrementalidad es **cuánta de esa intención ya estaba comprada antes de que aparecieras**.

## Las tres formas de medir incrementalidad

De la más rigurosa a la más artesanal:

| Método | Qué es | Cuándo usarlo | Rigor |
|---|---|---|---|
| **Conversion Lift** | Estudio oficial de Google: divide la audiencia en grupo que ve anuncios vs grupo retenido (**holdout**) que no, y compara conversiones. Aleatorización a nivel usuario | Cuentas con volumen; pídelo a tu rep de Google | Alto (experimento controlado) |
| **Geo experiments / geo lift** | Prendes la campaña en unas regiones (Bogotá, Medellín) y la apagas en otras comparables (Cali, Barranquilla). Comparas ventas totales. Se puede correr con la herramienta de **experimentos** de Google Ads o externa | Presencia nacional y volumen por región | Alto si las geos son comparables |
| **Holdout / on-off casero** | El más artesanal: apagas la campaña 2–3 semanas y mides qué pasa con las ventas totales (en backend, no en el panel) | PYMES sin volumen para estudios formales | Medio (ruido alto, pero útil) |

**Geo experiment, en corto:** elige pares de ciudades parecidas en tamaño y comportamiento. En unas dejas la campaña (test), en otras la apagas (control). Tras 3–4 semanas comparas ventas **por región en el backend**. La diferencia atribuible, normalizada por población/ventas base, es tu lift. Es el método preferido en 2026 porque no depende de cookies ni de atribución: mide resultado de negocio real.

**Holdout casero, paso a paso (el que más vas a usar en LatAm):**
1. Anota las ventas totales del negocio (backend/banco, ver 64) de las últimas 2–3 semanas con la campaña prendida.
2. **Apaga** la campaña sospechosa (ej. remarketing) 2–3 semanas. Deja todo lo demás igual.
3. Compara ventas totales del negocio antes vs durante el apagón.
4. Si las ventas totales cayeron proporcional al gasto que ahorraste → era incremental, vuélvela a prender. Si las ventas **casi no se movieron** → esa campaña no creaba ventas, solo se las atribuía. Recorta o redirige ese presupuesto.

El truco que casi todos fallan: mides **ventas TOTALES del negocio en el backend**, no las conversiones del panel. El panel de la campaña apagada obviamente marca cero; lo que importa es si el negocio entero vendió menos.

## Cómo se ve un resultado: cálculo de incrementalidad

Apagas remarketing 2 semanas, ahorras $2M:
- **Escenario A:** ventas totales del negocio bajan ~$1.8M. → El remarketing era casi todo incremental. Préndelo de nuevo, es buena plata.
- **Escenario B:** ventas totales bajan $200k. → El 90% de las "ventas de remarketing" iban a pasar igual. Estabas pagando $2M por traer $200k nuevos. Recorta fuerte y mueve la plata a genérico.

Fórmulas para ponerle número:

```
Lift de ventas      = ventas (periodo ON) − ventas (periodo OFF)
% incremental       = lift de ventas ÷ conversiones que el panel atribuía a la campaña
iROAS (ROAS incremental) = lift de ingresos ÷ gasto de la campaña

Ej. Escenario B:
  Panel atribuía: $2.4M en "ventas de remarketing"
  Lift real medido: $200k
  % incremental = 200k / 2.400k = 8%   → 92% era humo
  iROAS = 200k / 2.000k (gasto) = 0.1  → cada $1 trajo $0.10 nuevo. Pésimo.
```

La mayoría de cuentas viven entre A y B, más cerca de B de lo que el panel sugiere — especialmente en marca y remarketing. Por eso se mide, no se supone.

## Incrementalidad de marca: el caso especial

Apagar marca da miedo porque "perderé las búsquedas de mi nombre". A veces es justificado, a veces no. Variables:
- **Si un competidor puja sobre tu marca** (ver 94), tu anuncio de marca defiende terreno que el orgánico no protege → más incremental.
- **Si nadie puja tu marca y tu orgánico ya sale #1**, el anuncio de marca a menudo canibaliza un clic gratis → poco incremental.
- Mídelo con un geo holdout de marca: apaga marca en unas geos 2–3 semanas, mira si las ventas de marca (y totales) caen o el orgánico las recupera. No lo decidas por intuición ni por miedo.

## Errores comunes — blacklist

1. **Asumir que el ROAS alto de marca/remarketing es real.** Es donde más se infla el crédito. Mídelo con un holdout antes de defender su presupuesto (ver 64).
2. **Apagar marca/remarketing de golpe por "no son incrementales" sin medir.** Parte sí lo es (defensa de marca, ver 94; carritos reales). Mide primero, recorta después.
3. **Medir incrementalidad con el panel de la campaña apagada.** Obvio que marca cero. Mide **ventas totales del negocio en el backend** (ver 64).
4. **Correr el experimento cambiando dos cosas a la vez.** Si apagas remarketing Y subes presupuesto de Search la misma semana, no sabes qué movió las ventas. Aísla una variable.
5. **Hacer holdouts de 3 días.** Muy corto; el ruido te engaña. Mínimo 2–3 semanas comparables (evita quincena, festivos, promos).
6. **Olvidar que el genérico es tu mejor termómetro de crecimiento real.** Es casi siempre incremental; júzgate por ahí y por el MER (ver 64), no por el ROAS de marca.
7. **No documentar el aprendizaje.** Si mediste que el remarketing es 60% incremental, anótalo y reactívalo en el reporting (ver 67); si no, lo vuelves a discutir cada mes.
8. **Elegir geos no comparables en un geo experiment.** Comparar Bogotá con un pueblo destruye la prueba. Empareja por tamaño, ingreso y comportamiento; si no, el resultado es ruido disfrazado de ciencia.

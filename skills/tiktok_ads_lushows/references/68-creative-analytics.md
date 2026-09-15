# 68 — Creative analytics

Lee este módulo cuando tengas varios creativos corriendo y no sepas cuál mantener, cuando quieras escalar pero no sepas con qué video, o cuando entiendas por fin que en TikTok **el creativo es el 80% del resultado** y necesites el reporte que de verdad importa. Este es el módulo más rentable del bloque de medición. En TikTok no ganas optimizando públicos (eso lo hace el creativo, ver 30) — ganas encontrando qué video gana y por qué. El analytics de creativo responde una sola pregunta operativa: **¿este creativo lo mato, lo itero o lo escalo?** Todo lo demás del panel es secundario.

## Las tres métricas del creativo (y qué capa diagnostican)

Cada creativo se lee por tres números, en orden, porque cada uno revela una capa distinta del video (ver 61). Mirar solo el CPA del creativo no te dice *por qué* gana o pierde.

| Métrica | Qué mide del video | Diagnóstico |
|---|---|---|
| **Thumbstop / hook rate** | ¿El primer 1-3s frena el dedo? | El hook (ver 37). El #1 |
| **Hold rate / % visto** | ¿Se quedan después del hook? | El cuerpo del video |
| **CTR → CPA** | ¿Da ganas de actuar y a qué costo? | La oferta/CTA y el resultado |

La cadena es **thumbstop → hold → CTR → CPA**. Un creativo puede romperse en cualquier eslabón, y cada rotura tiene un fix distinto:

- Thumbstop bajo → el problema es el **primer segundo**. Cambia el hook, no todo el video (ver 37).
- Thumbstop alto + hold bajo → engancha pero **aburre**. El hook prometió y el cuerpo no entregó. Recorta/mejora ritmo.
- Hold alto + CTR bajo → lo ven completo pero **no actúan**. CTA/oferta débil (ver 38).
- Todo bien + CPA caro → revisa la **landing/Shop** o la medición (ver 61, 62), no el creativo.

Esto es diagnóstico quirúrgico: en vez de tirar el video entero, arreglas el eslabón roto. Un video con buen hold y mal hook se salva cambiándole solo la apertura — y eso cuesta una toma, no una producción nueva.

## El reporte que importa: CPA por creativo

El error fatal es leer el CPA **promedio del conjunto**. El promedio miente (ver 63 — paradoja de Simpson). Desglosa siempre **por anuncio**. Ejemplo real de un conjunto con CPA promedio "$12.000":

| Creativo | Thumbstop | Hold | CTR | Conv. | CPA | Decisión |
|---|---|---|---|---|---|---|
| A — dolor costos | 42% | 21% | 2,4% | 38 | $5.000 | **Escalar** |
| B — testimonio | 33% | 15% | 1,6% | 14 | $11.000 | Iterar |
| C — beneficio genérico | 19% | 7% | 0,8% | 4 | $38.000 | **Matar** |

El promedio ($12.000) no te dice nada. El desglose dice: A es oro, C te está sangrando. Si escalas el conjunto entero, tu plata se reparte y C se come parte del presupuesto del ganador. **Escala el creativo, no el conjunto.** Y fíjate en la columna "Conv.": C solo tiene 4 conversiones — apenas señal (ver 13); pero con thumbstop de 19% el diagnóstico ya es claro (el hook no frena a nadie), así que se mata sin esperar más.

## Matar / iterar / escalar: el árbol de decisión

| Si el creativo… | Decisión | Acción |
|---|---|---|
| Thumbstop bajo (< 20%) | **Matar o reescribir hook** | 3 hooks nuevos sobre el mismo cuerpo (ver 37) |
| Thumbstop OK, hold bajo | **Iterar** | Mismo hook, cuerpo más ágil |
| Hold OK, CTR bajo | **Iterar** | Mismo video, CTA/oferta más clara (ver 38) |
| CPA bajo y estable, 3+ conversiones | **Escalar** | Sube presupuesto 20% / duplica en otro ad group (ver 72) |
| Ganador que empieza a subir CPA | **Iterar (fatiga)** | Variantes del ganador antes de que muera (ver 39) |

Regla de los **iterar sobre ganadores**: cuando A funciona, no inventes de cero — haz 3-5 variantes de A (otro hook, otro testimonio, otro ángulo del mismo dolor). El "modelo ganador" se ordeña con variantes hasta que se agota (ver 39). Es más rentable iterar un ganador que buscar un nuevo ganador a ciegas, porque ya sabes qué resuena.

## Tasa de bateo: la métrica de tu producción creativa

Una métrica de nivel agencia que casi nadie mide: tu **tasa de bateo** (hit rate).

```
Tasa de bateo = creativos ganadores ÷ creativos probados
```

Si lanzas 10 videos al mes y 2 se vuelven ganadores, tu tasa es 20%. Eso es bueno en TikTok (la norma anda entre 10–20%). Para qué sirve: te dice **cuántos creativos necesitas producir** para sostener la cuenta. Si necesitas 2 ganadores nuevos por mes y bateas 20%, tienes que producir ~10. Esto convierte el "el creativo es el 80%" en un plan de producción concreto (ver 30, 31). Si tu tasa de bateo cae, no es mala suerte: tus ángulos se agotaron o el mercado se saturó (ver 39).

## Cómo conectar el creativo con la venta real

El thumbstop y el hold los ves en TikTok y son **confiables** (TikTok no tiene por qué inflar cuánta gente frena). Pero el CPA/ROAS por creativo en el panel **infla** (ver 64). Para saber qué video vendió de verdad en tu backend, etiqueta cada creativo en `utm_content` con su nombre de ángulo (ver 66, macro `__CID_NAME__`). Así cruzas:

```
Panel TikTok → thumbstop, hold, CTR (confiables) + CPA (inflado)
Backend (utm_content) → ventas reales por creativo (la verdad)
```

Ejemplo: el panel dice que A y B venden parecido (CPA $5.000 vs $5.500), pero el backend por `utm_content` muestra que A trajo 38 órdenes reales y B solo 9 (el resto de B eran view-through fantasma). **A es mucho mejor de lo que el panel sugería.** Ese cruce es el que alimenta el bloque "Creativos ganadores" del reporte ejecutivo (ver 67). Sin UTMs, decides creativos con datos inflados.

## Errores comunes — blacklist

- **Leer el CPA promedio del conjunto.** Esconde al ganador y al que sangra. Desglosa por anuncio siempre (ver 63).
- **Matar el video entero por un hook malo.** Si el hold es bueno, solo cambia la apertura (ver 37).
- **Escalar el conjunto en vez del creativo ganador.** Repartes plata y diluyes al ganador. Escala el video (ver 72).
- **Mirar solo el CPA sin thumbstop/hold.** No sabes *por qué* gana ni cómo replicarlo. Lee las tres métricas.
- **Inventar de cero cuando ya tienes un ganador.** Itera variantes del ganador, es más rentable (ver 39).
- **Confiar en el CPA por creativo del panel como verdad.** Infla; cruza con `utm_content` y backend (ver 64, 66).
- **Decidir con pocas conversiones.** 1 venta no es una señal. Espera 3+ antes de matar o escalar (ver 13) — salvo thumbstop tan bajo que el hook ya está sentenciado.
- **No medir tu tasa de bateo.** Sin ella no sabes cuántos creativos producir para sostener la cuenta.

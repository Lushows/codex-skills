# 07 — Presupuesto mínimo y expectativas

Aquí va la matemática honesta que casi nadie te dice antes de cobrarte: **cuánto necesitas DE VERDAD** para que Google Ads tenga la oportunidad de funcionar, por tipo de campaña. Lanzar con presupuesto insuficiente no es "empezar pequeño"; es garantizar que el algoritmo nunca aprenda y concluyas que "Google no sirve". Lee este módulo antes de prometer resultados, cuando el presupuesto es chico, o para decidir si arrancas Google ya o esperas.

## La regla del aprendizaje: el Smart Bidding necesita conversiones

El Smart Bidding (ver 13) necesita **datos para aprender**. La referencia clásica: **~15–30 conversiones en 30 días** por estrategia de puja para que estabilice (tCPA y tROAS suelen pedir más cerca de 30; Maximize Conversions tolera algo menos). Si tu campaña genera 3 conversiones al mes, la IA está adivinando. De ahí sale el presupuesto mínimo real:

> **Presupuesto mínimo mensual ≈ CPA esperado × ~30 conversiones**

| Tu CPA esperado (COP) | Presupuesto mínimo/mes para aprender |
|---|---|
| $5.000 | ~$150.000 |
| $15.000 | ~$450.000 |
| $40.000 | ~$1.200.000 |
| $100.000 | ~$3.000.000 |
| $300.000 (B2B/servicios) | ~$9.000.000 |

Si no conoces tu CPA aún, estima con: presupuesto = (CPC esperado × clics necesarios). Con tasa de conversión 3% necesitas ~33 clics por venta; a $1.500 COP/clic son ~$50.000 por venta → ~$1.500.000/mes para ~30 ventas. **Esto se valida en `economist_lushows`** (CAC máximo que aguanta el negocio).

## Benchmarks de costo LatAm/Colombia (jun-2026, orientativos)

Los números reales dependen del sector y la competencia, pero como punto de partida en COP:

| Métrica | Rango típico CO 2026 | Notas |
|---|---|---|
| **CPC Search genérico** | $800 – $4.000 COP | servicios competidos (abogados, salud, finanzas) más caro |
| **CPC Search de marca** | $150 – $700 COP | tu propia marca, barato y alta conversión (ver 39) |
| **CPC Display/Demand Gen** | $80 – $500 COP | barato pero baja intención |
| **CVR landing (visita→lead)** | 2% – 8% | depende brutalmente de landing y oferta (ver 33) |
| **CVR lead→venta (WhatsApp)** | 10% – 40% | depende del vendedor (ver `ventas_lushows`) |
| **ROAS e-commerce sano** | 3x – 6x | bajo eso, revisa margen y CVR |

Úsalos para sanity-check, no como promesa. Tu Keyword Planner (ver 20) te da el CPC real de TUS keywords; estos rangos solo te dicen si vas muy fuera de lo normal.

## Presupuesto mínimo realista por tipo de campaña

| Tipo | Mínimo mensual honesto (CO) | Por qué |
|---|---|---|
| **Search (intención alta)** | desde ~$300.000–$600.000 | el más eficiente con poco; pagas solo por clics de gente que busca |
| **Local Services (LSA)** | bajo, pagas por lead | servicios locales; arranque accesible (verificar disponibilidad CO, ver 50) |
| **Performance Max** | ~$1.500.000+ | come muchos canales; con poco, no aprende y desperdicia |
| **Demand Gen / YouTube** | ~$1.000.000+ | generación de demanda, ciclo más largo, CPA difuso |
| **Shopping** | ~$800.000+ | necesita volumen de productos/clics |

Conclusión dura: **con poco presupuesto, Search-first es casi siempre la única opción sensata.** PMax, Demand Gen y YouTube con migajas = plata quemada. Concentra: una campaña Search bien hecha que junta 30 conversiones/mes vale más que cinco campañas que juntan 6 cada una y ninguna aprende.

## Matemática honesta pre-lanzamiento (haz esto SIEMPRE)

Antes de lanzar, llena esta cuenta. Si no cuadra, **no lances** — ajusta oferta/precio o canal:

| Variable | Cómo obtenerla |
|---|---|
| Precio / ticket promedio | dato del negocio |
| Margen por venta | precio − costo (→ `economist_lushows`) |
| CAC máximo aguantable | margen × % que aceptas gastar en adquirir |
| CPC esperado | Keyword Planner (ver 20) |
| Tasa de conversión landing | benchmark 2–8%; real tras medir (ver 33) |
| CPA estimado | CPC ÷ (CVR landing × CVR lead→venta) |
| ¿CPA estimado < CAC máximo? | **si NO → no es viable como está** |

### Ejemplo paso a paso (GastroLatam — Excel a $10.000 COP)

1. Ticket: $10.000 COP, pago único. Margen ≈ casi todo (producto digital), digamos $9.000.
2. CAC máximo: si aceptas gastar el 50% del margen en adquirir → $4.500 COP por venta.
3. CPC esperado (Keyword Planner, "calculadora costos restaurante"): supongamos $800 COP.
4. CVR landing 4% × CVR lead→venta 50% (producto barato, decisión fácil) = 2% global.
5. CPA estimado = $800 ÷ 0.02 = **$40.000 COP por venta.**
6. ¿$40.000 < $4.500? **NO.** El CPA se come 4x el ingreso.

Diagnóstico honesto: un producto de $10.000 con búsqueda paga **no cierra por unidad**. Salidas posibles (todas son discusión de `economist_lushows`, no de optimización de pauta): subir precio, vender en volumen/bundle, monetizar con LTV/upsells (recompra, plantillas premium), o reconocer que el canal correcto es otro (orgánico, redes con `facebook_ads_lushows`, o venta directa). **La optimización no salva una unit economics rota** — solo la quema más lento.

## Expectativas: tiempos reales

| Hito | Plazo realista |
|---|---|
| Primeros clics/datos | días |
| Salir de "en aprendizaje" | ~1–2 semanas tras lanzar/cambiar puja |
| Señal clara de si funciona | 30 días con conversiones suficientes |
| Optimización con criterio | tras 50–100 conversiones acumuladas |

No juzgues una campaña en 3 días ni toques los targets en la primera semana (rompes el aprendizaje, ver 13). El día 1–3 los CPCs y CPAs se ven horribles porque la IA explora; eso es normal.

## Errores comunes — blacklist

- **Lanzar con presupuesto que da 2–3 conversiones/mes.** El Smart Bidding nunca aprende y culpas a Google. Fix: presupuesto ≈ CPA × ~30, o sube oferta/canal (ver arriba).
- **Arrancar con PMax/Demand Gen y poco budget.** Comen canales y desperdician sin datos. Fix: Search-first con poco presupuesto.
- **No calcular el CAC máximo antes de pautar.** Sin ese número no sabes si un CPA es bueno o ruinoso. Fix: pásalo por `economist_lushows`.
- **Pautar búsqueda paga para un ticket de $10.000 sin LTV/upsell.** El CPA se come el ingreso. Fix: revisa unit economics; quizás el canal correcto es otro (ver 03).
- **Juzgar la campaña en 3 días y apagarla.** Estaba en aprendizaje. Fix: dale 30 días con datos suficientes (ver arriba).
- **Dividir poco presupuesto entre muchas campañas.** Ninguna junta datos. Fix: concentra en 1 campaña Search hasta que aprenda (ver 18).
- **Confundir "presupuesto diario" con tope mensual.** Google puede gastar hasta ~2× el diario en días pico (se compensa en el mes, nunca pasa de 30.4× el diario al mes). Fix: pon el diario = mensual ÷ 30.4 (ver 18).
- **Prometerle al cliente un ROAS o CPA fijo antes de tener datos.** No es serio. Fix: promete proceso y aprendizaje; los números llegan tras 30 días.

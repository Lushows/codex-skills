# 72 — Escalado vertical: subir presupuesto sin romper lo que funciona

Escalar vertical = meterle más plata a lo que ya gana, en la misma campaña/ad set. Lee este módulo cuando tienes un ganador estable (CPA bajo objetivo, 1-2 semanas sostenido) y quieres más volumen. Aquí está cómo subir sin que Meta "se vuelva loca" — porque sí se vuelve loca si subes mal. El vertical es el escalado más barato y simple que existe: exprímelo SIEMPRE antes de abrir frentes nuevos (horizontal, ver 73). Pero tiene un techo físico —el margen— y pasarlo es perder plata con cara de crecimiento.

## La regla 20-30%

Subidas de presupuesto mayores al 20-30% pueden resetear la fase de aprendizaje (ver 13): Meta vuelve a explorar a quién mostrar tu anuncio, el CPA se desestabiliza 3-7 días y a veces no vuelve. Esta es la regla operativa #1 del escalado en 2026.

**La receta:**
1. Sube **20-30% cada 48-72 horas**, nunca más rápido ni más fuerte.
2. Solo subes SI los últimos 3 días sostienen CPA bajo tu objetivo. Un día bueno no es señal (ver 70).
3. Después de cada subida, NO toques nada por 48-72h. Deja que el sistema digiera. La inestabilidad de 2-3 días post-subida es NORMAL — no la confundas con fracaso ni revierte en pánico.
4. Si tras una subida el CPA se rompe (>130% del objetivo 3+ días): vuelve al presupuesto anterior y estabiliza 1 semana antes de reintentar.

Ejemplo: $50.000/día → $65.000 (miércoles) → $84.000 (sábado) → $105.000 (martes). En ~10 días duplicaste sin un solo reseteo.

| Día | Presupuesto | Acción |
|---|---|---|
| 0 | $50.000 | Base estable 3 días bajo CPA → permiso para subir |
| 0 | → $65.000 | +30% |
| 3 | → $84.000 | +30% (si CPA aguanta) |
| 6 | → $105.000 | +25% |
| 9 | Evaluar | ¿CPA bajo techo? sigue. ¿Tocó techo? para |

## Vertical vs horizontal: cuándo cuál

| Pregunta | Si SÍ → |
|---|---|
| ¿Puedes subir 20-30% y el CPA sigue rentable? | **Vertical** (sigue subiendo, es más barato) |
| ¿Cada subida rompe el margen 2 semanas seguidas? | **Horizontal** (ver 73): el cuello es el creativo, no el presupuesto |
| ¿Frequency alta en tus ganadores? | **Horizontal**: más creativos/ángulos, no más plata a lo mismo |

El creativo es el cuello de botella del escalado. Si el vertical se atascó, casi nunca es "el presupuesto"; es que el mismo anuncio ya saturó a su audiencia (ver 39). La salida es producción creativa (ver 73), no presionar más plata contra un anuncio cansado.

## Alternativa: duplicado con presupuesto mayor

Para saltos grandes sin riesgo sobre el original:

- **Duplica el ad set ganador** con 2-3× el presupuesto y déjalo correr junto al original.
- El duplicado entra en learning desde cero (re-aprende, puede tardar días en funcionar o no funcionar nunca), pero **el original no se toca** — sigue produciendo mientras el clon experimenta.
- Si el duplicado funciona: tienes dos motores. Si no: lo matas con los kill criteria (ver 71) y el original sigue intacto.
- No dupliques más de 1-2 veces el mismo ganador: los clones compiten entre sí en la subasta (overlap) y terminan encareciéndose mutuamente (te subastas contra ti mismo).

## CBO scaling (el más suave) y Advantage+

CBO = Campaign Budget Optimization: el presupuesto se define a nivel campaña y Meta lo reparte entre ad sets según rendimiento (hoy es el comportamiento por defecto en Advantage+ campaign budget, ver 12, 92).

- En CBO/Advantage+ subes el presupuesto **a nivel campaña** y el sistema redistribuye gradualmente — el impacto sobre cada ad set es más amortiguado que tocar ad sets individuales.
- Misma disciplina: 20-30% cada 48-72h.
- Ventaja extra: si un ad set se fatiga, CBO mueve la plata solo, sin que tú toques nada.
- En 2026 con la consolidación Andromeda (ver 92), escalar UNA campaña consolidada suele ser más estable que escalar cinco campañas fragmentadas a la vez.

## Expectativa honesta: el CPA SUBE al escalar

Esto no es un bug, es física de subastas. A presupuesto bajo, Meta te encuentra la gente más barata y más propensa a comprar. Al subir presupuesto, sales de ese núcleo hacia audiencia más cara y más fría.

- Espera CPA **+10-30%** al duplicar el gasto. Rango honesto; varía por nicho y país.
- La pregunta no es "¿subió el CPA?" sino "¿mi margen aguanta este CPA?". Si vendes con margen de $60.000 COP por pedido y tu CPA pasó de $25.000 a $32.000, sigues ganando — escala. Si tu margen es $35.000, ese mismo salto te dejó en el borde — frena.
- Si no tienes claro tu margen por pedido, páralo todo y calcúlalo primero (skill **economist_lushows**, unit economics). Escalar sin saber tu margen es acelerar con los ojos vendados.

## Cuándo parar de subir

- El CPA tocó tu **techo de margen** (el CPA máximo donde aún ganas plata) durante 3+ días → estabiliza en el último presupuesto rentable.
- Subes y el gasto adicional casi no trae conversiones extra (rendimientos decrecientes evidentes: +30% de presupuesto trae +5% de ventas).
- En ese punto el vertical se agotó: el crecimiento sigue por **escalado horizontal** (ver 73): nuevos creativos, formatos, ofertas, geos.
- Para escalar PROTEGIDO sin vigilar a diario: cost cap / minimum ROAS calibrados (ver 74) — pones presupuesto alto y el sistema solo gasta donde es rentable.

## Ejemplo numérico: escalera de 4 semanas (pyme colombiana)

Producto con margen de $55.000 COP/pedido. CPA objetivo: $30.000. Techo de margen: $45.000.

| Semana | Presupuesto/día | CPA real | Decisión |
|---|---|---|---|
| 1 | $60.000 | $26.000 (3 días estable) | Subir 25% → $75.000 |
| 2 | $75.000 → $95.000 | $29.000, luego $31.000 | Dos subidas de ~25% con 72h entre ellas |
| 3 | $120.000 | $36.000 | Aún bajo techo ($45.000). Subir 20% → $145.000 |
| 4 | $145.000 | $43.000 por 4 días | Tocando techo. PARAR. Estabilizar en $120-145k y abrir horizontal (ver 73) |

Resultado: de $1.8M a ~$4M COP/mes de inversión, ventas ~2.3×, todavía rentable. El CPA subió 65% y estuvo BIEN porque el margen lo aguantaba.

## Checklist antes de cada subida

- [ ] ¿3+ días seguidos con CPA bajo objetivo? (no 1, no 2)
- [ ] ¿Conozco mi techo de margen y este CPA proyectado queda debajo?
- [ ] ¿No toqué creativo/audiencia esta semana? (una variable a la vez)
- [ ] ¿La subida es ≤30%?
- [ ] ¿Anoté en la bitácora? (ver 70)
- [ ] ¿Voy a esperar 48-72h sin tocar después?

## El principio rector

**El presupuesto sigue al ganador, no al calendario.** No escalas porque "ya es viernes" o porque "este mes quiero gastar más": escalas porque los datos de 3+ días te dieron permiso. Y dejas de escalar cuando el margen dice basta, no cuando se acaba la ambición.

## Errores comunes — blacklist

- Duplicar el presupuesto de un día para otro (+100% = reseteo casi seguro).
- Subir cada 24h porque ayer fue bueno.
- Escalar un ganador de 2 días (no de 2 semanas).
- Tocar creativo/audiencia el mismo día que subes presupuesto (dos variables, cero lectura).
- Escalar sin conocer tu margen por pedido y descubrir a fin de mes que vendiste mucho perdiendo plata.
- Pánico-revertir a las 24h de una subida (la inestabilidad de 2-3 días post-subida es normal).
- Clonar el ganador 4 veces y subastar contra ti mismo.
- Seguir presionando presupuesto cuando el cuello es creativo (toca horizontal, ver 73).

# 17 — Framework de testing

Lee este módulo cuando quieras "probar algo" sin arruinar lo que ya funciona, cuando alguien cambió tres cosas a la vez y ahora nadie sabe qué movió la aguja, o cuando un test te dio un resultado y no sabes si es real o ruido. Testear bien es lo que separa al que **adivina** del que **sabe**. La regla madre: **cambia una variable a la vez, mídela contra un control simultáneo, y dale tiempo y volumen suficiente para que el resultado sea real y no azar.**

## La herramienta nativa: experimentos (drafts & experiments)

Google trae un sistema de **experimentos** (antes "drafts & experiments") que hace un A/B limpio dividiendo el tráfico:

| Concepto | Qué es |
|---|---|
| **Draft** (borrador) | Copia de tu campaña donde haces el cambio sin afectar la original |
| **Experiment** (experimento) | Promueves el draft a experimento: Google **divide el tráfico** (ej. 50/50) entre original y variante |
| **Split** | El reparto (50/50 recomendado para llegar a significancia más rápido) |
| Reporte | Google te muestra ambas ramas lado a lado con indicador de significancia estadística |

**Por qué usarlo y no "cambiar y ver":** si solo cambias la campaña entera y comparas con la semana pasada, no comparas contra un control —comparas contra otra semana con otro clima, otra estacionalidad (ver 19), otra competencia en la subasta (ver 01). El experimento corre el control y la variante **al mismo tiempo, con el mismo entorno**. Eso es un A/B real; lo otro es una anécdota.

En 2026 hay variantes según el tipo: para **Search** está drafts & experiments clásico; para **PMax y Demand Gen** hay experimentos de tipo **uplift / A-B** y **lift tests** que miden incrementalidad (ver 65) — clave para PMax porque su ROAS reportado engaña (ver 12). Para medir si una campaña trae ventas **nuevas** (no robadas de orgánico/marca), el experimento correcto es un **geo lift / conversion lift**, no un A/B de creativo.

## Qué testear primero (orden de impacto)

No todo merece test, y el orden importa: lo que más mueve la aguja va primero.

| Prioridad | Qué testear | Por qué pesa tanto |
|---|---|---|
| 1 | **Landing page / oferta** | Es donde se gana o pierde la conversión; la mayor palanca (ver 33, 48) — rutea diseño a `desingweb-lushows` |
| 2 | **Ángulo del anuncio** (la promesa, no la coma) | Cambiar la promesa cambia quién hace clic (ver 38) — rutea copy/concepto a `directorcreativo_lushows` / `ventas_lushows` |
| 3 | **Estrategia / target de puja** | Impacto fuerte pero resetea aprendizaje; testéalo con cuidado (ver 13, 15) |
| 4 | **Audiencias / señales** | Afina a quién llegas (ver 23) |
| 5 | **RSA: titulares y descripciones** | Iteración fina, menor impacto unitario (ver 30) |
| 6 | Detalles (assets/extensiones, ver 32) | Marginal pero gratis |

**Empieza por la oferta y la landing**, no por el color del botón. El 80% del resultado está en qué prometes y a dónde llevas (ver 33). Probar microcosas (color, una palabra) en cuentas LatAm pequeñas es perder semanas: nunca alcanzas significancia para diferencias de 2%.

## A/B limpio: no contaminar variables

Un test sucio es peor que ningún test, porque te da una conclusión falsa con confianza:

- **Una variable a la vez.** Si cambias el titular Y la landing Y el target juntos, y mejora, no sabes cuál fue. Aísla.
- **No edites la campaña mientras corre el experimento** (ni negativos, ni presupuesto, ni assets): metes una tercera variable invisible.
- **Mismo periodo, mismo split.** Control y variante en paralelo, no consecutivos.
- **Respeta el aprendizaje.** Si tu test toca el bidding, suma ~2 semanas de fase de aprendizaje antes de leer resultados (ver 13).
- **No mires el día 2.** Volatilidad pura. Define la duración antes de empezar y no la cambies.

## Significancia práctica (sin estadística de PhD)

"Significancia" = qué tan seguro estás de que la diferencia es real y no suerte. Sin volumen, cualquier número engaña.

| Regla práctica | Umbral |
|---|---|
| Conversiones mínimas por rama antes de concluir | **~30-50 conversiones por variante** como piso |
| Duración mínima | **2-4 semanas** + al menos un ciclo de conversión completo (ver 16) |
| Cubrir el ciclo semanal | Corre semanas **completas** (lun-dom); el comportamiento varía por día y por quincena (ver 19) |
| Diferencia que vale la pena | Si la mejora es <5-10%, probablemente es ruido; busca cambios de doble dígito |

Si una rama lleva 8 conversiones y la otra 5, **no concluyas nada**: eso es azar. La impaciencia es el enemigo número uno del testing. En cuentas chicas (LatAm, presupuestos de 1.5-3M COP/mes) el volumen llega lento; testea **cosas grandes** (oferta, ángulo) donde el efecto sea evidente, no micro-optimizaciones que jamás alcanzarán significancia. Si no vas a llegar a ~30-50 conv por rama en 4 semanas, **no hagas A/B estadístico**: cambia la oferta entera y juzga por tendencia de negocio mes a mes.

### Bitácora de test — plantilla

| Campo | Ejemplo |
|---|---|
| Fecha inicio / fin | 2026-06-13 → 2026-07-04 |
| Hipótesis | "Landing con precio visible arriba sube conversión >15%" |
| Variable única | Posición del precio en la landing |
| Control / Variante | Precio abajo / precio en el hero |
| Resultado | Variante +22% conv, 41 vs 33 conv, signif. ✓ |
| Decisión | Variante = nuevo control; siguiente test sobre ella |

## Documenta o no existió

Lleva el registro de arriba: fecha, qué cambiaste, hipótesis, resultado, decisión. Sin bitácora repetirás tests viejos y olvidarás aprendizajes (ver 67). Un ganador validado se vuelve el **nuevo control**; sobre él pruebas el siguiente retador (testing iterativo). Así la cuenta acumula conocimiento en vez de dar vueltas.

## Errores comunes — blacklist

- **Cambiar varias cosas a la vez**: el test "funciona" pero no sabes qué lo movió; conclusión inservible.
- **Concluir con 5-10 conversiones por rama**: es ruido, no señal; necesitas ~30-50 (ver 13).
- **Comparar "esta semana vs la pasada"** en vez de control simultáneo: confundes estacionalidad/subasta con tu cambio (ver 19, 01).
- **Editar la campaña mientras corre el experimento**: metes variables nuevas y ensucias el control.
- **Leer resultados durante la fase de aprendizaje**: volatilidad pura; matas ganadores prematuros (ver 71).
- **Testear el color del botón antes que la oferta**: optimizas migajas e ignoras la palanca real (ver 33).
- **Hacer A/B de creativo cuando lo que querías era medir incrementalidad de PMax**: usa lift test, no A/B (ver 65).
- **No documentar**: repites tests, pierdes aprendizajes, no construyes conocimiento de cuenta (ver 67).
- **Forzar A/B estadístico en una cuenta sin volumen**: nunca llegas a significancia; mejor cambia la oferta entera y juzga por negocio.

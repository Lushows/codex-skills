# 68 — Creative analytics: qué creativo vive, muere o escala

En la era Andromeda + GEM (los motores de Meta que premian volumen y diversidad creativa y evalúan el ad dentro del journey completo, ver `actualizacion-2026-06`), **el creativo es el ~80% del rendimiento** — y decidir cuál vive, muere o escala con "me gusta cómo quedó" es quemar plata. Este módulo da las métricas por capa del creativo, la matriz de decisión 2×2 y la cadencia semanal. Úsalo cada semana en tu revisión creativa (ver 63) y cuando dudes si un ad "ya demostró" algo. Actualizado jun-2026.

Realidad 2026 que cambia el ritmo: con **Entity ID**, creativos casi-iguales se COLAPSAN en una sola entidad y compiten entre sí → no sirve subir 100 casi-duplicados; sube **10–15 conceptualmente distintos**. Y la **vida útil del ad bajó a ~2–4 semanas** (antes 6–8): el creative analytics ya no es un lujo trimestral, es el motor semanal que mantiene la cuenta viva.

## Las métricas del creativo, por capa (qué pregunta responde cada una)

| Métrica | Fórmula | Pregunta que responde | Referencia (varía por vertical/formato) |
|---|---|---|---|
| **Thumbstop ratio** | reproducciones de 3s ÷ impresiones | ¿El hook DETIENE el scroll? | 20–30% ok, >35% fuerte |
| **Hold rate** | reproducciones de 15s (o al 50%) ÷ reproducciones de 3s | ¿El cuerpo SOSTIENE al que paró? | 25–50% |
| **CTR outbound** | clics salientes ÷ impresiones | ¿Mueve a la ACCIÓN? | 0.5–2% |
| **CPA / ROAS del ad** | gasto ÷ compras del ad | ¿VENDE al final? | contra TU breakeven (ver 64) |

Léelas en cascada: cada una filtra a la siguiente. Un CTR bajo con thumbstop alto no es el mismo problema que un CTR bajo con thumbstop bajo — la primera capa rota manda (misma lógica que el funnel completo, ver 61). Diagnóstico rápido por combinación:

| Thumbstop | Hold | CTR | Diagnóstico | Fix |
|---|---|---|---|---|
| Bajo | — | — | El hook no para el scroll | Nuevo hook (primeros 3s), ver 37 |
| Alto | Bajo | — | Para pero aburre después | Reescribe el cuerpo del video |
| Alto | Alto | Bajo | Engancha pero no pide acción | CTA más claro / oferta en pantalla |
| Alto | Alto | Alto + no vende | Promesa ≠ landing/oferta | Congruencia y oferta (ver 48, 41) |

## La matriz de decisión 2×2

Eje 1: ¿detiene? (thumbstop/CTR). Eje 2: ¿vende? (CPA vs tu objetivo).

|  | **VENDE** | **NO VENDE** |
|---|---|---|
| **DETIENE** | 🏆 **GANADOR**: escala (ver 72) e itera variantes YA, antes de que fatigue (ver 39). Un ganador sin variantes listas es una crisis programada — más aún con vida útil de 2–4 semanas. | Hook bueno, promesa/landing desalineada: la gente entra y se decepciona. Itera el CUERPO y la oferta, o revisa congruencia con la landing (ver 48, 41). NO toques el hook. |
| **NO DETIENE** | Vende a los pocos que lo ven → audiencia y oferta correctas, hook flojo. NUEVO HOOK al mismo cuerpo (ver 39: refrescar primeros 3s). El fix más barato y rentable que existe. | ☠️ Mata sin duelo. No lo "optimices": el aprendizaje es que ese ángulo/ejecución no va. Anota el learning y siguiente. |

Umbral antes de juzgar: **gasto mínimo de 1–2× tu CPA objetivo por ad**. Con CPA objetivo COP $60.000, un ad con $35.000 gastados no ha demostrado NADA. Matar ads "fríos" a las 6 horas es la forma más cara de no aprender nada.

## Cómo armar el reporte de creativos en Ads Manager

1. Nivel **Anuncios**, filtro "Activas con gasto" (ver 63), rango 7–14 días.
2. Preset de columnas "CREATIVO": gasto, compras, CPA, CTR saliente, reproducciones de 3s, ThruPlays/% al 50%, frequency. Thumbstop (3s ÷ impresiones) y hold no vienen como columna directa → calcúlalos en tu hoja.
3. Ordena por gasto descendente: Meta ya votó — el ad que recibe gasto es el que el algoritmo cree mejor; tu trabajo es confirmar con CPA si tiene razón.
4. El naming con sistema hace el análisis posible: `[ángulo]-[formato]-[hook]` (ver 66) te deja agrupar por ángulo sin abrir cada ad. Sin naming, el creative analytics es arqueología.

### Análisis por ÁNGULO, no solo por ad
Lo que escala una cuenta no es "el ad ganador", es **el ÁNGULO ganador** (el mensaje/insight), porque te da infinitas variantes. Agrupa tus ads por ángulo y suma:

| Ángulo | Gasto | Compras | CPA | CTR prom | Veredicto |
|---|---|---|---|---|---|
| dolor-cotidiano ("¿te da sueño a las 3pm?") | 520.000 | 11 | 47.300 | 1.8% | DOBLAR: base creativa |
| ciencia-dato | 410.000 | 4 | 102.500 | 1.3% | PAUSAR ángulo |
| precio-descuento | 300.000 | 6 | 50.000 | 1.1% | mantener, probar variantes |

Conclusión accionable: el insight "dolor cotidiano" vende; produce 4–5 ejecuciones nuevas de ESE ángulo (distintos hooks/formatos) antes que inventar ángulos nuevos a ciegas.

## Cadencia semanal (30 min, criterios PRE-escritos)

Decide los criterios ANTES de mirar los números (si decides mirando, tu sesgo gana):
1. Todo ad con gasto ≥1–2× CPA objetivo entra a la matriz 2×2 → matar / nuevo hook / iterar cuerpo / escalar.
2. Ganadores: ¿frequency subiendo + CTR cayendo semana a semana? → fatiga en camino, pide variantes ya (ver 39).
3. Pipeline: ¿cuántos creativos CONCEPTUALMENTE nuevos entran esta semana? (Andromeda/GEM premian volumen+diversidad: 3–5/semana según presupuesto, conceptos distintos por Entity ID, ver 17/49).
4. Registra cada decisión en la hoja de learnings (abajo).

## La hoja de learnings: el activo que se acumula

Una fila por ad juzgado. Columnas: fecha | ángulo | hook (en una frase) | formato | thumbstop | hold | CTR | CPA | veredicto (matar/nuevo-hook/iterar/escalar) | learning en una frase.

Ejemplo: `12-jun | energía-entreno | "¿te da sueño a las 3pm?" | video UGC 20s | 34% | 41% | 1.8% | $48k | ESCALAR | ángulo dolor-cotidiano > ángulo ciencia (2× CTR)`.

A los 3 meses esa hoja vale más que cualquier campaña individual: es tu mapa de qué mensajes mueven a TU mercado (alimenta los briefs creativos, ver 17/49, el reporte mensual, ver 67, y se conecta con la dirección creativa → directorcreativo_lushows para producir las variantes; el guion de venta del hook → ventas_lushows).

## Ejemplo resuelto: tres ads, tres veredictos

CPA objetivo COP $60.000 (umbral de juicio: $60–120k de gasto por ad):
- **Ad A** (`energia-video-pregunta`): gastó $130k, thumbstop 36%, hold 40%, CTR 1.9%, 3 compras → CPA $43k. Detiene Y vende → **escalar** (ver 72) + 3 variantes del mismo ángulo esta semana.
- **Ad B** (`ciencia-video-dato`): gastó $110k, thumbstop 31%, hold 22%, CTR 1.4%, 0 compras. Para pero el cuerpo no sostiene ni vende → revisar congruencia ad↔landing y oferta (ver 48, 41); el hook se conserva, se reescribe el cuerpo.
- **Ad C** (`salud-imagen-generica`): gastó $95k, thumbstop n/a (imagen), CTR 0.3%, 1 compra. No detiene → matar; learning: "ángulo salud-general en imagen estática no para el scroll".
Nota WhatsApp: si optimizas a conversaciones, el "vende" de la matriz se mide en pedidos cerrados del CRM, no en conversaciones iniciadas (ver 53, 64, 66 tabla por ángulo de chat).

## Errores comunes — blacklist
- Juzgar ads por estética o por likes en vez de la matriz (el feo que vende le gana al lindo que no).
- Matar ads antes del gasto mínimo de 1–2× CPA — pánico estadístico.
- "Optimizar" un ni-ni en vez de matarlo y anotar el learning.
- Escalar un ganador SIN variantes en producción: con vida útil de 2–4 semanas, cuando fatigue te quedas sin nada.
- Cambiar el hook de un ad que detiene pero no vende (el hook era lo único que funcionaba).
- Subir 100 casi-duplicados: Entity ID los colapsa y compiten entre sí — sube 10–15 conceptos distintos.
- Analizar ad por ad sin agrupar por ángulo: pierdes el insight que de verdad escala la cuenta.
- No registrar learnings: cada test pagado sin nota es plata quemada dos veces — la del test y la del test repetido en 3 meses.

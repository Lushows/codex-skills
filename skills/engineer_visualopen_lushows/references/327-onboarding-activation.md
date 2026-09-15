# 327 · Onboarding y activación (llevar al aha-moment antes de que se vayan)

> Dos tercios de los signups nunca llegan al aha-moment: activación media B2B SaaS ≈ 36-37%.
> El onboarding no es un tour, es la ruta más corta entre "me registré" y "esto vale".

## Vocabulario que no se debe confundir
- **Aha-moment**: el instante emocional en que el usuario *percibe* el valor. Es cualitativo.
- **Activation event**: el proxy medible del aha (ej. Slack: "2.000 mensajes enviados por un equipo";
  Dropbox: "1 archivo en 1 dispositivo"). Lo defines tú con datos, no con intuición.
- **Time-to-value (TTV / TTFV)**: tiempo desde signup hasta ese evento. Media ≈ 1d 12h; el cuartil
  top baja de **5 minutos**. [verificado 2026]
- **Activación**: % de usuarios que disparan el evento. Top-quartile >40%.

## Por qué importa (números que mueven retención)
- Quien llega a primer valor en <14 días retiene ≥80% a mes 12; quien NO llega en 30 días, 35-50%.
  Swing de **30-45 puntos** de retención. [verificado 2026]
- Aha en la primera hora → 4-5× la retención D7 vs quienes tardan 24h+. [verificado 2026]
- Onboarding personalizado/automatizado: +15-25 pp de retención a 90 días vs flujo genérico.

## Cómo encontrar TU activation event
1. Correlación, no opinión: cruza eventos tempranos contra retención D30/D90 (cohortes).
2. Busca el evento que separa retenidos de churned y que sea **alcanzable en sesión 1**.
3. Valida que sea causal-ish: usuarios empujados a él retienen más (no solo correlación de power-users).
4. Convierte en "magic number" (la métrica X-en-Y-días: "3 proyectos en 7 días").

## Patrones de UI que reducen fricción
- **Checklist de onboarding** con progreso visible (efecto Zeigarnik + Endowed Progress: arranca
  2/5 ya marcado). Cada ítem = un paso hacia el activation event, no hacia tu org-chart.
- **Empty states que venden**: el estado vacío es la pantalla más vista del producto nuevo. No pongas
  "No hay datos" — pon un CTA, un dato de ejemplo, un botón "Crear el primero" o datos demo precargados.
- **Progressive disclosure**: no enseñes 40 features. Una ruta lineal al valor; lo avanzado, después.
- **Personalización en signup**: 2-3 preguntas (rol, caso de uso) → ramifica el flujo. AI-driven baja
  TTV 25-40%. No más de 3 preguntas: cada campo extra sangra conversión.
- **Tooltips contextuales / product tours**: solo just-in-time, no un carrusel inicial que se salta.
- **Datos de muestra**: precargar un workspace demo elimina el cold-start del empty state.

## Métricas a instrumentar
| Métrica | Definición | Objetivo |
|---|---|---|
| Activation rate | % que dispara el evento | >40% (top), >36% (media) |
| TTV / TTFV | signup → primer valor | <1 día, ideal <5 min |
| Checklist completion | % que termina el checklist | correlación con D30 |
| Time-to-first-action | signup → primer clic significativo | minimizar |
| Onboarding drop-off | paso donde abandonan | encontrar el cuello |

## Errores que matan activación
- Pedir tarjeta/datos antes de mostrar valor. Wall-of-forms en el registro.
- Tour modal de 8 pasos que todos cierran. Empty state que dice "0 resultados" y nada más.
- Definir el aha por lo que TÚ quieres (que configure todo) en vez de lo que retiene.
- No instrumentar: si no mides el activation event, estás optimizando a ciegas.

Cruza con [[325-funnels-conversion-cro]] y [[328-pricing-page-packaging]].

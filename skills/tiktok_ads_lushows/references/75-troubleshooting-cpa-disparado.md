# 75 — Troubleshooting: CPA disparado

Lee este módulo cuando una campaña que venía bien de repente cuesta el doble por venta, cuando el ROAS se cae y no sabes por dónde empezar a mirar, o cuando entras en pánico y quieres "cambiarlo todo" a la vez. Este es el checklist ordenado para cuando se daña la cuenta. La regla antes de empezar: **no toques nada todavía** (ver 70) — diagnostica primero, actúa después, un cambio a la vez. En TikTok, donde el frame es descubrimiento y la varianza es alta, la mitad de los "CPA disparados" no son problemas reales: son un día malo o un tracking caído. Diagnosticar te evita romper una campaña sana.

## La causa #1 en TikTok: fatiga creativa

Antes de revisar cualquier otra cosa, mira el creativo. **En TikTok, la causa número uno de un CPA disparado es la fatiga creativa** (ver 39) — el creativo se quemó. Esto pasa más rápido y más seguido que en Meta, porque un ganador dura 1–2 semanas, no meses (ver 73, 76).

Las dos métricas que lo delatan:

| Señal | Qué significa | Dónde mirar |
|---|---|---|
| **Frequency sube** (la misma gente lo vio muchas veces) | Saturaste la bolsa de audiencia de ese creativo | Reportes por creativo (ver 68) |
| **Hook rate / thumbstop CAE** (menos gente para en los primeros 1–3s) | El video ya no engancha; el público lo "conoce" y desliza | Creative analytics (ver 68) |

Si ves frequency arriba + hook rate cayendo = **es fatiga, punto.** El fix no es tocar la campaña, es **meter creativo fresco** (ver 73) y apagar el quemado (ver 71). Si confirmas fatiga, ni sigas el checklist — ve a producir.

Cómo se ve la fatiga en el tiempo, para que la reconozcas temprano: el primer síntoma suele ser el hook rate bajando lento mientras el CPA todavía aguanta; luego la frequency cruza ~2.5–3 en pocos días; y ahí el CPA salta de golpe. Si vigilas el hook rate semanalmente (ver 68), cachas la fatiga antes de que te cueste plata — refrescas el creativo cuando empieza a caer, no cuando ya explotó el CPA.

## El checklist de diagnóstico (en orden)

Solo si NO es fatiga obvia, baja por esta lista. Cambia una cosa, espera 3 días (ver 70), vuelve a leer:

| # | Sospechoso | Cómo lo revisas | Fix |
|---|---|---|---|
| 1 | **Fatiga creativa** (ver arriba) | Frequency ↑ + hook rate ↓ | Creativo nuevo (ver 73, 39) |
| 2 | **¿Es solo varianza?** | Mira ventana de 7 días, no de hoy | Si es un día malo → no toques (ver 70) |
| 3 | **Oferta** | ¿Cambió precio, stock, promesa? ¿La competencia sacó algo mejor? | Revisa/ajusta oferta (ver 41) — la oferta vence al creativo |
| 4 | **Evento de tracking roto** | ¿El Pixel/Events API sigue disparando? ¿Las conversiones que ves en TikTok cuadran con las reales? | Revisa medición (ver 05, 06) — un evento caído infla el CPA falso |
| 5 | **Estacionalidad / CPM** | ¿Subió el CPM? ¿Es temporada alta, Q4, fecha comercial? | CPM de temporada (ver 77) — a veces no es tu culpa, es el mercado |
| 6 | **Competencia** | ¿Alguien entró a tu nicho a pujar fuerte? | Creative Center (ver 94) — refresca ángulo, no compitas en lo mismo |
| 7 | **Te reseteaste solo** | ¿Subiste presupuesto >30%, cambiaste evento, pausaste/prendiste? | Volviste a aprendizaje (ver 13). Deshaz y espera, no encadenes cambios |
| 8 | **Landing / cierre** | ¿La landing carga lento, se cayó? ¿El WhatsApp no contesta? | El ad trae el clic pero algo abajo se rompió → `desingweb-lushows` / `ventas_lushows` |

El orden importa: la mayoría de los CPA disparados en TikTok se resuelven en los puntos 1–4. Si llegas al 5–6 sin encontrar nada, suele ser mercado (temporada o competencia), no tu campaña.

## Árbol de decisión rápido

Para cuando no quieres leer toda la tabla y necesitas decidir en 2 minutos:

1. **¿Frequency arriba + hook rate cayendo?** → Sí: fatiga. Refresca creativo (ver 73). FIN. → No: sigue.
2. **¿El CPA malo es de UN día o de 7 días?** → Un día: varianza, no toques (ver 70). FIN. → Sostenido: sigue.
3. **¿Las conversiones de TikTok cuadran con tus ventas reales?** → No cuadran: tracking roto (ver 05, 06). Arréglalo, no toques la puja. FIN. → Cuadran: sigue.
4. **¿Cambió algo en la oferta/precio/stock o entró competencia fuerte?** → Sí: arregla oferta o refresca ángulo (ver 41, 94). FIN. → No: sigue.
5. **¿Es Q4 / fecha comercial / subió el CPM para todos?** → Sí: es mercado, ajusta presupuesto y oferta, no rompas la estructura (ver 77). FIN. → No: sigue.
6. **¿Tú tocaste algo (presupuesto >30%, evento, pausa) en los últimos días?** → Sí: te reseteaste, deshaz y espera (ver 13, 70). FIN. → No: sigue.
7. **¿La landing/WhatsApp funcionan?** → No: arregla el cierre (`desingweb-lushows`/`ventas_lushows`). → Sí y nada explica el CPA: ve a la sección final.

## El error mortal: cambiarlo todo a la vez

Cuando el CPA se dispara, el instinto es entrar y mover diez cosas: bajar presupuesto, cambiar puja, editar público, pausar ads, meter creativos. **No lo hagas.** Si cambias todo junto:

1. Reseteas el aprendizaje (ver 13) y empeoras el CPA por el bache de re-aprendizaje.
2. Si mejora, no sabes qué lo arregló → no aprendes nada para la próxima.
3. Probablemente el problema era una sola cosa (casi siempre creativo) y rompiste lo que sí funcionaba.

El método correcto: **diagnostica con el checklist → identifica EL sospechoso más probable → cambia solo eso → espera 3 días → lee.** Frío y ordenado vence a ansioso y reactivo.

## Si nada del checklist explica el CPA

A veces el CPA "alto" no es un problema de campaña — es que el negocio nunca cerró bien la cuenta. Si el CPA está alto pero **estable** y el creativo está fresco, quizá tu CPA objetivo era irreal desde el principio para tu margen. Eso no se arregla en el Ads Manager: se revisa la economía del negocio (precio, margen, LTV) con `economist_lushows`. Pautar más barato no salva un producto con unit economics rotos.

Otra causa silenciosa: el **cierre**. Si el CPA de TikTok (costo por lead) está bien pero el "CPA real" (costo por VENTA cerrada) se disparó, el problema no es la pauta — es que los leads dejaron de cerrar. Eso es proceso de ventas, no media buying → `ventas_lushows`. Mucha gente rompe campañas sanas cuando el verdadero hueco está en quién contesta el WhatsApp y cómo.

## Errores comunes — blacklist

- **Revisar settings antes que el creativo.** En TikTok la causa #1 es fatiga. Mira frequency y hook rate PRIMERO (ver 39, 68).
- **Cambiar todo a la vez.** Reseteas aprendizaje y nunca sabes qué pasó. Un sospechoso, un cambio, espera (ver 70).
- **Reaccionar a un día malo.** Puede ser pura varianza. Mira la ventana de 7 días antes de actuar (ver 70).
- **No revisar si el evento de tracking se cayó.** Un Pixel/Events API roto infla el CPA falsamente; corres detrás de un fantasma (ver 05, 06).
- **Ignorar la estacionalidad.** En Q4 o fechas comerciales el CPM sube y no es tu culpa (ver 77). No rompas una campaña sana por eso.
- **Olvidar la oferta y la competencia.** A veces el creativo está bien pero la oferta envejeció o alguien entró más fuerte (ver 41, 94).
- **Olvidar el cierre.** Si los leads dejaron de cerrar, el problema es ventas, no pauta (ver `ventas_lushows`).
- **Bajar a "resetear la cuenta".** No existe (ver 76). Lo que existe es diagnosticar y meter creativo fresco.

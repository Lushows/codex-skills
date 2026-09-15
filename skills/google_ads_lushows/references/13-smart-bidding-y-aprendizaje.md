# 13 — Smart Bidding y aprendizaje

Lee este módulo cuando una campaña dice "Aprendizaje limitado", cuando subiste un target y el CPA se disparó al día siguiente, o cuando alguien quiere "tocar la puja todos los días para optimizar". Smart Bidding es la norma de 2026: tú no pones la puja por clic; pones un **objetivo** (un CPA o un ROAS, o solo "maximiza") y el algoritmo ajusta la puja en cada subasta usando cientos de señales en tiempo real —dispositivo, hora, ubicación, idioma, lista de remarketing, historial, intención de la consulta— que tú no puedes ver ni igualar a mano (ver 01). Funciona muy bien si lo dejas trabajar y lo alimentas bien. La mayoría de cuentas no falla por mala configuración; falla porque el dueño no para de toquetear.

## La fase de aprendizaje (learning phase)

Cuando creas una campaña o haces un cambio grande, Smart Bidding entra en **fase de aprendizaje**: recolecta datos para calibrar antes de estabilizarse. Durante esta fase el rendimiento es **volátil y no representativo** — no juzgues nada todavía.

| Hecho | Número / regla |
|---|---|
| Duración típica de aprendizaje | **~1 a 2 semanas** (depende del volumen de conversiones) |
| Conversiones mínimas para calibrar | **~15-30 conversiones/mes** por estrategia (tCPA/tROAS). Menos = nunca estabiliza |
| Cuándo NO mirar resultados | Los primeros **~14 días** tras lanzar o tras un cambio mayor |
| Ventana mínima para juzgar | Al menos **2 semanas estables** + un ciclo de conversión completo (ver 16) |

**Si tienes menos de ~15 conversiones/mes**, no uses tCPA/tROAS todavía: el algoritmo no tiene de qué aprender. Usa **Maximize conversions** (sin target) o sube a una conversión más alta en el embudo que sí tenga volumen (ver 14), y considera **shared budget** o consolidar campañas para juntar señal (ver 10, 18). En LatAm pequeño esto es la norma, no la excepción: con 2M COP/mes muchas cuentas viven en la frontera de los 15 conv/mes, así que protege ese volumen consolidando.

## Qué RESETEA el aprendizaje (y qué no)

Cada reset te devuelve a 1-2 semanas de volatilidad. Trata los cambios con respeto:

| RESETEA aprendizaje (evítalo / hazlo con intención) | NO suele resetear (seguro) |
|---|---|
| Cambiar la **estrategia de puja** (Maximize → tCPA, etc.) | Pausar/activar **keywords** o anuncios sueltos |
| Cambiar el **target** tCPA/tROAS de forma brusca (>15-20%) | Editar **negativos** (ver 22) |
| Cambio **grande de presupuesto** (duplicarlo de golpe) | Pequeños ajustes de presupuesto (≤20%) |
| Cambiar la **conversión de optimización** (ver 14) | Cambiar texto/un titular de un RSA (efecto menor) |
| Reestructurar la campaña (ver 10) | Agregar audiencias en "observación" |
| Cambiar la **acción de conversión primaria** del objetivo | Subir un asset nuevo a PMax |

**Regla de oro: no toques el target ~2 semanas después de cualquier cambio.** Y cuando ajustes el target, muévelo en **escalones de ≤10-15%**, no de golpe (ver 74). Un salto brusco de tCPA hacia abajo apaga la entrega; uno brusco hacia arriba dispara el gasto sin control.

## Señal limpia: la gasolina del algoritmo

Smart Bidding es tan bueno como la conversión que le reportas. Señal sucia = decisiones sucias.

- **Cuenta la conversión correcta**, una vez, lo más cerca de la venta que tu volumen aguante (ver 14). No cuentes "vista de página" como conversión: el algoritmo optimizará para tráfico que ve páginas, no que compra.
- **No dupliques conversiones**: mismo evento contado dos veces (gracias-page + evento de compra) infla todo y engaña al bidding (ver 04).
- **Enhanced Conversions + Consent Mode v2** son el **piso de medición en 2026**: sin ellos pierdes señal por bloqueo de cookies y consentimiento, y el algoritmo va medio ciego (ver 06). Enhanced Conversions manda datos hasheados de primera parte (email, teléfono) que recuperan conversiones que las cookies perdieron — sube el match rate y, con él, la calidad del bidding.
- **Atribución data-driven es el default** (el last-click se retiró en 2025): el algoritmo ahora reparte crédito según aporte real, lo que mejora cómo aprende del embudo completo (ver 16).
- **Calibra el target sobre datos REALES, no deseados**: si tu CPA real es 25.000 COP, no pongas tCPA 12.000 "porque quiero". El algoritmo concluye que no puede ganar subastas a ese precio y deja de entregar. Pon tCPA cerca del CPA real actual y baja en escalones (ver 15, 74).

## Maximize vs target: cuál usar según madurez

| Etapa de la cuenta | Estrategia | Por qué |
|---|---|---|
| Campaña nueva, poca señal (<15 conv/mes) | **Maximize conversions** (sin target) | Junta conversiones para tener de qué aprender |
| Ya tienes ~15-30 conv/mes estables | **tCPA** cerca del CPA real | Ahora puede calibrar a un objetivo |
| E-commerce con valores de venta variables | **Maximize conv. value** → **tROAS** | Optimiza por valor, no por conteo (ver 15) |
| Quieres gastar todo el presupuesto sí o sí | Maximize (acepta que el CPA flote) | Prioriza volumen sobre eficiencia |

### Diagnóstico rápido de "Aprendizaje limitado"

| Síntoma | Causa probable | Arreglo |
|---|---|---|
| "Limitado: pocas conversiones" | <15 conv/mes para esa estrategia | Sube de conversión en el embudo o consolida (ver 14, 18) |
| "Limitado: presupuesto" | El budget topa antes de calibrar | Sube presupuesto en escalones ≤20% o consolida campañas |
| "Limitado: target tCPA muy bajo" | Pediste un CPA por debajo del real | Sube el target cerca del CPA real y baja en escalones (ver 15) |
| Vuelve a aprendizaje cada semana | Estás tocando target/budget/estrategia seguido | **Para de tocar**; deja 2-3 semanas quieto |

## Calendario y picos: cuándo el aprendizaje juega en contra

No lances campañas nuevas ni cambies estrategia **justo antes de un pico** (Black Friday, día sin IVA, Amor y Amistad): la fase de aprendizaje de ~2 semanas te dejaría volátil en el peor momento (ver 19). Estabiliza antes. Para picos cortos y conocidos usa **seasonality adjustments** en vez de mover el target a mano (ver 19) — así no reseteas aprendizaje.

## Errores comunes — blacklist

- **Tocar el target o el presupuesto a los 3 días** de lanzar: reseteas el aprendizaje una y otra vez; la campaña nunca estabiliza.
- **Poner tCPA en el CPA que DESEAS** y no en el real: el algoritmo se ahoga y deja de entregar (ver 15).
- **Usar tCPA/tROAS con <15 conversiones/mes**: no hay señal para calibrar; usa Maximize o sube de conversión (ver 14).
- **Bajar el tCPA de golpe -40%** para "ahorrar": apagas la campaña; baja en escalones de ≤10-15% (ver 74).
- **Optimizar para una conversión basura** (pageview, clic en botón WhatsApp sin cierre): el bidding compra tráfico que hace eso, no que vende (ver 04, 14).
- **Dejar caer Enhanced Conversions / Consent Mode v2**: pierdes señal, el algoritmo va ciego, sube el CPA sin que sepas por qué (ver 06, 62).
- **Juzgar una campaña en aprendizaje**: pausas un ganador que aún no estabilizaba (ver 71).
- **Lanzar/cambiar estrategia 3 días antes de un pico**: aprendizaje volátil en el día más caro (ver 19).
- **Fragmentar la señal en 6 campañas chicas**: ninguna llega a 15 conv/mes; todas viven en aprendizaje limitado (ver 10, 18).

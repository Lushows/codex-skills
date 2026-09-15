# 16 — Métricas del sistema

Ninguna métrica sola cuenta la verdad. Cada una ilumina un ángulo y tiene una trampa. Se leen
JUNTAS o se leen mal. Todo cálculo exacto → `Matematicas_lushows`.

## Las métricas y sus trampas

| Métrica | Qué mide | Se lee así | Su trampa |
|---|---|---|---|
| **Expectancy** | Ganancia promedio esperada por trade (después de costos) | >0 = hay edge | Con muestra chica es puro azar (ver `17`) |
| **Profit Factor (PF)** | Suma de ganancias ÷ suma de pérdidas | >1 gana, >1.3 respira, >2 excelente | Un solo trade grande lo infla o hunde |
| **Win rate** | % de trades ganadores | Solo junto al R:R | 90% de win rate puede PERDER dinero si las pérdidas son grandes |
| **Sharpe** | Retorno por unidad de volatilidad total | Más alto = retorno más "tranquilo" | Castiga la volatilidad buena (subidas fuertes) igual que la mala |
| **Sortino** | Retorno por unidad de volatilidad SOLO a la baja | Mejor que Sharpe para sistemas asimétricos | Necesita bastantes datos para ser estable |
| **Drawdown máx** | Peor caída desde un pico de equity | El número que mata cuentas (ver `02`) | El pasado no acota el futuro: el peor DD siempre puede estar adelante |
| **MAE** | Máxima excursión adversa: lo peor que fue el trade ANTES de cerrar | ¿Los stops están bien puestos? | — |
| **MFE** | Máxima excursión favorable: lo mejor que fue antes de cerrar | ¿Los targets dejan plata en la mesa? | — |

**Términos:** *equity* = valor total de la cuenta. *Volatilidad* = qué tanto se mueve el resultado.

## Win rate y R:R: la pareja inseparable

Con R:R 1:2 (ganas 2 por cada 1 que arriesgas), el punto de equilibrio ANTES de costos es
~33% de win rate. Con costos (~0.30% redondo en el AGENTE) sube unos puntos. Traducción:
el sistema puede perder 6 de cada 10 trades y aun así ganar dinero — por eso perseguir
win rate alto es perseguir la métrica equivocada.

## MAE/MFE: las métricas de afinación

- Si el MAE promedio de los ganadores es, digamos, 0.4% y el stop está a 1.5× volatilidad
  (mucho más lejos), quizá el stop puede acercarse → mejor R:R con el mismo target.
- Si el MFE de los perdedores es alto (iban ganando y devolvieron todo), quizá falta un
  stop de protección al llegar a +1R.
- **Advertencia**: afinar stops/targets con 10 trades es sobre-ajustar al ruido. Se anota la
  observación, se decide con ≥30 trades.

## Cómo leerlas JUNTAS (el tablero mínimo)

1. **¿Hay edge?** → Expectancy y PF (con muestra ≥30).
2. **¿Sobrevivo mientras lo cobro?** → Drawdown máximo.
3. **¿El edge viene de pocos trades gigantes o es parejo?** → distribución en R + PF sin el mejor trade.
4. **¿Puedo mejorar la ejecución?** → MAE/MFE.

## Cómo aplica al AGENTE TRADING

- Estado real (6-jul-2026): **PF 0.89** (rojo: pierde $1 gana $0.89), **DD 1.84%** (verde),
  **10 trades** (muestra insuficiente para concluir NADA con confianza).
- Lectura conjunta honesta: el sistema pierde poquito y de forma controlada — la gestión de
  riesgo funciona; el edge todavía no aparece. Es el diagnóstico correcto: problema de
  ESTRATEGIA, no de RIESGO. Por eso el pivote candidato es el filtro anti-extensión, no tocar el 1.5%.
- Los umbrales del go-live (PF >1.3, DD <15%, ≥30 trades el 22-ago) son este tablero convertido
  en contrato — ver `08`.
- Sharpe/Sortino: calcularlos cuando haya ≥30 trades; antes son decoración.

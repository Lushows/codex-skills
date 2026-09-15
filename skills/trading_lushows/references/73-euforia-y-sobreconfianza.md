# 73 — Euforia y sobreconfianza

El revenge trading (módulo 72) mata rápido y se nota. La euforia mata despacio y se siente
GENIAL mientras ocurre — por eso es más peligrosa. Nadie pide ayuda cuando va ganando.

## El mecanismo

Una racha ganadora produce dopamina y una conclusión falsa: "ya entendí el mercado". Con esa
conclusión vienen las decisiones caras:

1. **Subir el riesgo por trade** ("si con 1.5% gané esto, con 5% gano el triple").
2. **Bajar la exigencia de entrada** ("este setup no es perfecto, pero vengo embalado").
3. **Aflojar los stops** ("no quiero que me saque de una ganadora").
4. **Ignorar el régimen** ("da igual que el mercado esté cayendo, yo le pego").

## Por qué subir riesgo en la cima es lo peor matemáticamente

Las rachas ganadoras tienden a ocurrir cuando el mercado favorece tu sistema (p. ej. tendencia
alcista para un sistema solo-LONG). Los regímenes cambian sin avisar. Resultado: el riesgo
inflado llega EXACTAMENTE cuando el entorno se voltea.

| Escenario | Riesgo/trade | 4 wins luego 4 pérdidas |
|---|---|---|
| Disciplinado | 1.5% fijo | Termina ligeramente arriba o plano |
| Eufórico | 1.5% → sube a 5% tras las wins | Las 4 pérdidas van con 5%: devuelve todo y queda rojo |

Mismo mercado, mismos trades, mismo win rate. La diferencia es SOLO cuándo subiste el tamaño.
A esto se le llama "regalar la racha": ganar con fichas chicas y perder con fichas grandes.

## Señales de sobreconfianza (en humanos)

- Revisas el P&L más veces al día que antes (para disfrutarlo).
- Empiezas a contarle a la gente cuánto llevas ganado.
- "Esta vez sí puedo con apalancamiento."
- La palabra "obvio" aparece en tu análisis ("es obvio que sube").
- Confundes 8 trades buenos con evidencia estadística (se necesitan cientos — módulo 79).

## Cómo aplica al AGENTE TRADING

- **El bot mantiene 1.5% de riesgo por trade pase lo que pase.** El sizing es Kelly fraccional con
  techo duro en `positionSizing.js` (JS puro): ninguna racha, ninguna convicción 10/10 y ningún
  prompt puede subirlo. Ese techo existe precisamente para que la euforia no tenga botón.
- Evidencia real de por qué: la racha de 4 wins de jul-2026 fue seguida de 3 pérdidas por FOMO
  estructural. Si el riesgo hubiera subido con la racha, esas 3 rojas se habrían llevado mucho más.
- **La euforia del dueño**: tras semanas verdes, la tentación de Luis será "pasar a live YA" o
  "subir el capital simulado". Ambas son decisiones de euforia si no vienen de criterios escritos
  en frío (muestra suficiente, métricas objetivo, checklist de live del módulo 87).
- Regla de la casa: las reglas se cambian con datos y por backlog, nunca en la cima de una racha —
  ni de wins ni de pérdidas.

# 21 — Kelly y fracciones

## Qué es el criterio de Kelly

El **criterio de Kelly** es una fórmula (John Kelly, 1956) que responde: "si conozco mi
probabilidad de ganar y cuánto gano cuando gano, ¿qué fracción de mi capital debo apostar
para que crezca lo más rápido posible a largo plazo?"

```
Kelly% = W − (1 − W) / R

W = win rate (probabilidad de ganar, ej. 0.40 = 40%)
R = ratio ganancia/pérdida (con R:R 1:2, R = 2)
```

Ejemplo con W=45% y R=2: Kelly = 0.45 − 0.55/2 = **17.5% del capital por trade**.
Sí, leíste bien: Kelly puro puede sugerir tamaños enormes. Ahí está el problema.

## Por qué Kelly puro quiebra gente

1. **Asume que conoces W y R exactos.** Nadie los conoce — se estiman con historial corto
   y cambian con el mercado. Sobreestimar W un poco convierte la fórmula óptima en veneno:
   apostar POR ENCIMA del Kelly verdadero no solo frena el crecimiento, lo vuelve negativo.
2. **Los drawdowns de Kelly puro son brutales.** Aun con las probabilidades correctas,
   Kelly completo produce caídas de equity que ningún humano (ni criterio go-live) tolera.
   El "óptimo matemático" ignora que uno abandona el sistema antes de cobrar el largo plazo.
3. El error es **asimétrico**: quedarse corto cuesta un poco de crecimiento; pasarse cuesta
   la cuenta. Ante la duda, siempre menos.

## Media-Kelly y cuarto-Kelly

La solución estándar: apostar una **fracción** de lo que dice Kelly.

| Fracción | Crecimiento vs Kelly puro | Drawdown esperado |
|---|---|---|
| Kelly completo | 100% | Brutal |
| Media-Kelly (½) | ~75% | Mucho menor |
| Cuarto-Kelly (¼) | ~44% | Manejable |

Media-Kelly conserva la mayor parte del crecimiento con una fracción del dolor — por eso es
el estándar práctico. Cuarto-Kelly es lo prudente cuando W y R vienen de pocos trades (como
ahora: 10 trades no estiman nada con confianza). Los números exactos de esta tabla se
verifican en `Matematicas_lushows`; no reciclar.

## El techo duro: la capa que salva

**Kelly fraccional + techo duro** = calcular Kelly, tomar una fracción, y ADEMÁS nunca superar
un máximo absoluto pase lo que pase. El techo protege del peor enemigo de Kelly: estimaciones
malas. Si el historial engaña y Kelly "sugiere" 20%, el techo dice 1.5% y punto.

Orden de prioridad: **techo duro > fracción de Kelly > Kelly puro**. La convicción y las
probabilidades modulan hacia abajo; nada modula hacia arriba.

## Cómo aplica al AGENTE TRADING

`positionSizing.js` usa Kelly fraccional con techo duro de **1.5% de riesgo por trade**:
la convicción (1-10) y las probabilidades estimadas mueven el tamaño DENTRO de ese techo,
jamás lo rompen. Con 10 trades y PF 0.89 (6-jul-2026), el W estimado no es confiable todavía
— razón de más para que el techo mande. Regla para siempre: aunque el paper muestre PF alto
con 30+ trades, el techo no se toca hasta tener cientos de trades en vivo, y aun así, subirlo
sería la última palanca, no la primera.

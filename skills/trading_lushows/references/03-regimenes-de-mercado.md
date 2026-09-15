# 03 — Regímenes de mercado

"El macro primero, el activo después" (Druckenmiller). Operar un buen setup contra el régimen
es la forma más elegante de perder plata.

## Los 5 regímenes que clasifica el bot (macroRegime, Haiku)

| Régimen | Qué significa | Postura del bot |
|---|---|---|
| `trending-up` | Tendencia alcista confirmada | Único régimen donde la convicción puede ser alta (LONG) |
| `trending-down` | Tendencia bajista | Convicción ≤4 obligada (sin SHORT, solo esperar) |
| `ranging` | Lateral, sin dirección | Convicción baja; los breakouts falsos abundan |
| `risk-on` | Apetito de riesgo global | Viento a favor para cripto |
| `risk-off` | Huida del riesgo | Convicción ≤4 obligada |

- Input: últimas 50 velas 1h + volatilidad. Output: régimen + confianza 0-1 + razonamiento.
- La memoria (traderMemory) se filtra POR régimen: las lecciones de trending-up no aplican en ranging.

## Lección real del sistema (jun-jul 2026)

El meta-análisis semanal demostró el valor del régimen con datos propios:
**100% de los trades ganadores ocurrieron con trending-up confirmado ≥78%**; el único trade
ejecutado con régimen `unknown` fue pérdida (y además fue fuera de protocolo — ver `10`).

## Regímenes y el problema del bot solo-LONG

Sin SHORT, el bot solo tiene edge en 2 de 5 regímenes (trending-up, risk-on). En los otros 3
su única jugada correcta es NO operar — lo cual hace bien (drawdown 1.8%), pero significa
semanas sin aprender. El SHORT en paper (backlog `11`) duplicaría los regímenes operables.

## Señales de cambio de régimen (para vigilar)

- Ruptura de SMA-50 con volumen — posible cambio de tendencia.
- Volatilidad comprimida durante días → expansión inminente (dirección desconocida).
- Divergencias RSI en máximos → agotamiento del trending-up (la lección FOMO de `10`).

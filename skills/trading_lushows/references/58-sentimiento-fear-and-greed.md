# 58 — Sentimiento: Fear & Greed y funding

## Qué es el análisis de sentimiento

Medir el **estado de ánimo** del mercado: ¿la masa está eufórica o aterrada? La tesis
contrarian clásica (Buffett): "sé temeroso cuando otros son codiciosos, y codicioso cuando
otros son temerosos". Los extremos de emoción suelen coincidir con techos y pisos — pero
"suelen" no es "siempre", y ahí está toda la dificultad.

## El índice Fear & Greed

El más citado en cripto (alternative.me) resume varias fuentes (volatilidad, volumen, redes
sociales, dominancia) en un número de 0 a 100:

| Rango | Etiqueta | Lectura contrarian |
|---|---|---|
| 0-24 | Miedo extremo | Zona donde históricamente se formaron pisos |
| 25-49 | Miedo | Neutral-cauteloso |
| 50-74 | Codicia | Neutral; tendencia sana puede vivir aquí meses |
| 75-100 | Codicia extrema | Zona de techos y de FOMO — máxima prudencia |

Valor actual: **verificar al día**. Y la advertencia clave: el índice puede quedarse en
"codicia extrema" durante semanas mientras el precio sigue subiendo. **Usarlo para vender
un trending-up confirmado es carísimo.** Es un moderador de agresividad, no una señal.

## Funding rate: el sentimiento que se paga en plata

En los futuros perpetuos (derivados sin vencimiento), el **funding** es un pago periódico
entre compradores (longs) y vendedores (shorts) que mantiene el futuro pegado al spot:

- **Funding muy positivo** → los longs pagan a los shorts → exceso de apalancados alcistas
  → mercado frágil a un "long squeeze" (caída que liquida longs en cascada).
- **Funding negativo** → los shorts pagan → pesimismo cargado → combustible para "short squeeze".

Es el termómetro de sentimiento más honesto que existe, porque no mide opiniones: mide
**apuestas con plata real y apalancada**. Se consulta gratis en Coinglass o en Binance.

## Uso contrarian prudente (las reglas)

1. Los extremos de sentimiento **afinan** una decisión tomada por régimen+precio; nunca la originan.
2. En tendencia fuerte, el sentimiento "caro" es lo normal — respetar la tendencia (`03`).
3. El mejor uso es de veto suave: codicia extrema + funding recalentado = no perseguir la vela verde.

## Cómo aplica al AGENTE TRADING

- El bot ya vivió esta lección en carne propia: su trade FOMO (registrado en `10`) fue
  exactamente comprar euforia fuera de protocolo. Un chequeo de sentimiento lo habría frenado.
- Mejora concreta y barata: pasar Fear & Greed + funding como **contexto adicional a Haiku**
  al clasificar régimen — con instrucción explícita de usarlos solo como moderador de
  convicción (p. ej., codicia extrema → convicción máxima 7).
- Lo que NO hacer: comprar "porque hay miedo extremo" en trending-down. Para un bot
  solo-LONG, atrapar cuchillos cayendo no es contrarian: es el error clásico de retail.

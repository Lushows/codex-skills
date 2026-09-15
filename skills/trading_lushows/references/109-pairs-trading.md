# 109 — Pairs trading: apostar a la relación, no a la dirección

**Pairs trading** = operar la RELACIÓN entre dos activos que se mueven parecido, en vez de la
dirección de uno. La receta: cuando la relación se estira más de lo normal, ir **LONG** (comprar)
el que quedó rezagado y **SHORT** (vender en corto: vender prestado para recomprar más barato)
el que quedó adelantado, apostando a que la relación vuelve a su promedio. Es reversión a la
media (ver `49`) aplicada a un par, no a un precio.

## El ejemplo natural en cripto: ETH/BTC

BTC y ETH están altamente correlacionados: suben y bajan juntos la mayor parte del tiempo, pero
su proporción (el ratio ETH/BTC) oscila. Un pair trade clásico: el ratio se estira muy por
debajo de su rango reciente → LONG ETH + SHORT BTC por montos equivalentes → si el ratio
regresa, la posición gana **sin importar si el mercado entero subió o bajó**.

## Neutralidad de mercado: la promesa y su letra pequeña

Esa es la gracia: **neutralidad de mercado**. Si todo cripto cae 10%, el LONG pierde pero el
SHORT gana ≈lo mismo; solo importa el movimiento RELATIVO entre los dos. Suena a riesgo
eliminado. No lo es — está cambiado por otros:

| Riesgo | En cristiano |
|---|---|
| **La relación se rompe** | "Correlacionados hasta hoy" no obliga a mañana: un evento propio de un activo (fallo técnico, regulación, narrativa) puede separar el par para siempre. El estirón que operaste era el comienzo del rompimiento, no una anomalía |
| **El estirón se estira más** | Igual que toda reversión a la media: "anormal" puede volverse más anormal por mucho tiempo. Sin stop sobre el RATIO, la pérdida no tiene techo natural |
| **Costos dobles** | Dos posiciones = dos comisiones, dos slippages, y el SHORT paga costo de financiación (funding en perpetuos o interés del préstamo) mientras esperas |
| **Riesgo de la pata corta** | El SHORT puede ser liquidado en un rally violento aunque la tesis del par siguiera siendo correcta |

La estadística seria detrás (medir qué tan estable es la relación, cuánto tarda en volver, qué
umbral de estirón operar) es trabajo cuantitativo real — cálculos → `Matematicas_lushows`, y
cualquier cifra de correlación actual del par, verificar al día.

## Qué exigiría hacerlo bien

1. **Dominar el SHORT primero** — es prerrequisito absoluto: margen, funding, liquidación,
   órdenes en derivados. Nuestro bot es solo-LONG spot: hoy no puede ni construir la mitad de
   la posición.
2. Medir la relación con rigor (no "se ven parecidos"): estabilidad histórica, rangos, tiempo
   típico de regreso — con muestra grande y out-of-sample (ver `48`).
3. Stop definido sobre el RATIO (no sobre cada pata) y sizing que entienda que son UNA posición.
4. Ejecución simultánea de las dos patas: entrar con una y esperar la otra es quedar direccional
   sin quererlo justo en un momento estirado.

## Cómo aplica al AGENTE TRADING

- **No es para ahora**: requeriría SHORT primero, y el SHORT es un mundo nuevo de riesgos
  (liquidación, funding, margen) que el sistema no ha pisado ni en paper. La escalera sana:
  demostrar edge LONG en paper → live LONG chico → paper de SHORT simple → y solo entonces
  hablar de pares. Estamos en el escalón 1 (10 trades, PF 0.89 — sin edge demostrado aún).
- Lo que SÍ podemos usar hoy, gratis: el ratio ETH/BTC como **contexto** para el análisis
  direccional — cuál de los dos está más fuerte cuando el bot elige dónde tomar su LONG.
  Leer la relación no exige operarla.
- Si algún día se explora, entra por la puerta de siempre: hipótesis escrita → backtest con
  costos dobles (ver `46`) → paper como out-of-sample vivo → tamaño mínimo. Sin atajos por
  "neutral al mercado" — neutral no significa seguro.

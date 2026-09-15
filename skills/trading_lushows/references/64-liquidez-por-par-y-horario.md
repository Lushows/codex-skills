# 64 — Liquidez por par y por horario

Cripto opera 24/7, pero **no todas las horas valen lo mismo**. La liquidez (cuánto volumen
hay dispuesto a comprar y vender) respira con los husos horarios del dinero mundial.

## Las tres sesiones (aunque cripto "nunca cierra")

El volumen sigue a las mesas de trading tradicionales. En hora de Colombia (UTC-5), aprox.:

| Sesión | Hora Colombia (aprox.) | Carácter |
|---|---|---|
| Asia (Tokio/HK/Singapur) | 7 p.m. – 3 a.m. | Volumen moderado; a veces marca la dirección temprana |
| Europa (Londres) | 2 a.m. – 11 a.m. | Volumen sube; Londres es plaza mayor de FX |
| EE.UU. (Nueva York) | 8 a.m. – 4 p.m. | **La sesión reina**: máximo volumen, noticias macro, ETFs |
| Solape Londres+NY | 8 a.m. – 11 a.m. | La ventana más líquida del día |

La madrugada entre el cierre de NY y la apertura de Asia (4 p.m. – 7 p.m. Colombia) y las
horas profundas de la noche americana son los desiertos de liquidez del día.

## Fines de semana traicioneros

Sábado y domingo las mesas institucionales descansan y el libro se adelgaza. Consecuencias
conocidas:

- **Movimientos exagerados con poco volumen**: una orden mediana mueve lo que entre semana
  no movería. Rupturas "importantes" de sábado que el lunes se revierten por completo.
- **Cacería de stops facilitada**: con el libro delgado, barrer una zona de stops cuesta
  menos plata (ver `67`).
- Históricamente, varios cracks famosos de cripto arrancaron en fin de semana o madrugada,
  cuando no había bids que amortiguaran.

Regla honesta: el precio del fin de semana **vale menos como información**. Una señal
generada el domingo a las 3 a.m. merece menos confianza que la misma señal el martes a las 10 a.m.

## Liquidez por par

Dentro de Binance spot: BTC/USDT es el par más profundo del mercado cripto; ETH/USDT le
sigue de cerca. Todo lo demás cae rápido en profundidad — un par de mediana capitalización
puede tener 10-100x menos libro (verificar profundidades al día). El costo real de operar
crece al bajar esa escalera, aunque la comisión sea la misma.

## Cómo aplica al AGENTE TRADING

- El bot analiza **cada 2 horas, las 24 horas** — hoy trata igual la señal del domingo 3 a.m.
  que la del martes 10 a.m. Mejora concreta para Fase 8: un **factor de liquidez** por
  franja (fin de semana / madrugada → exigir más convicción o reducir tamaño; ver `69`).
- El modelo de slippage de 5 bps (`63`) está calibrado para horas decentes; en desierto de
  liquidez es optimista — otra razón para el factor de franja.
- El "no operar" en horas muertas no pierde casi nada: los movimientos genuinos de tendencia
  casi siempre se confirman (o se repiten) en horas líquidas.

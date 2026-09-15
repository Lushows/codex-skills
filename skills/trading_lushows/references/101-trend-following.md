# 101 — Trend following (seguir la tendencia)

> Filosofía en una frase: "corta las pérdidas rápido, deja correr las ganancias". No predice
> hacia dónde va el mercado — se sube a lo que YA se está moviendo y se baja cuando deja de
> moverse.

## La idea

Una **tendencia** es un movimiento sostenido en una dirección (máximos y mínimos cada vez más
altos = alcista). El trend follower no intenta comprar el piso ni vender el techo: entra cuando
la tendencia ya es visible y sale cuando se rompe. Renuncia al principio y al final del
movimiento a cambio de capturar el tramo del medio, que suele ser el más largo.

Es una de las pocas familias de estrategias con evidencia de décadas en muchos mercados
(los fondos "managed futures" viven de esto). Eso no garantiza nada en cripto hoy — pero no
es un invento de YouTube.

## La matemática incómoda: win rate bajo, ganadores grandes

| Métrica | Trend following típico |
|---|---|
| Win rate | Bajo: muchas entradas fallan (30-45% es normal) |
| Tamaño de ganadores | Grandes: un buen trade paga varios perdedores |
| Distribución | Meses mediocres + pocos períodos excelentes que hacen todo el resultado |

La cuenta funciona así: si pierdes 1R en los fallos y ganas 3-5R en los aciertos, puedes fallar
más de la mitad de las veces y aun así ser rentable. **Profit factor > 1 con win rate < 50%**
es la firma clásica del trend following.

## El costo psicológico (donde muere la mayoría)

- **Drawdowns largos**: rachas de 5-10 pérdidas seguidas son estadísticamente NORMALES con
  win rate bajo. Semanas o meses bajo el pico anterior, sin saber cuándo llega el trade grande.
- **Devolver ganancias**: la salida por ruptura de tendencia siempre devuelve parte de lo
  ganado — se vende más abajo del máximo, por diseño. Duele cada vez.
- **La tentación fatal**: "mejorar" el sistema justo durante el drawdown, abandonándolo
  exactamente antes del período bueno que pagaba todo.

Aquí es donde un bot tiene ventaja real sobre un humano: no se desmoraliza en el trade
perdedor #7. Pero el HUMANO que supervisa al bot sí — por eso los criterios del módulo 08
se fijaron ANTES de ver resultados.

## Cómo aplica al AGENTE TRADING

- Nuestro bot es primo del trend following: solo LONG en swing alcista, cortar rápido
  (stop a 1R) y dejar correr (target a 2R). El R:R 1:2 significa que con ~40% de aciertos
  ya hay rentabilidad — no necesitamos "acertar casi siempre".
- Lección directa: **el PF 0.89 actual con 10 trades no es diagnóstico todavía.** Con win rate
  bajo por diseño, 10 trades pueden ser pura varianza. Por eso el criterio exige ≥30 trades
  antes de juzgar.
- Si el 22-ago toca PIVOT, las variantes de trend following (filtros de tendencia en 4h/1d,
  salidas que dejan correr más) son el vecindario natural donde buscar — no saltar a una
  filosofía opuesta (módulo 102) por impaciencia.

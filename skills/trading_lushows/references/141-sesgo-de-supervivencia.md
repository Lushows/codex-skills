# 141 — Sesgo de supervivencia

> Juzgar cualquier cosa mirando solo a los que sobrevivieron. Es el sesgo más corrosivo del
> trading porque distorsiona TODO lo que ves: los activos, las estrategias, los gurús y hasta
> tus propios datos.

## La idea en una imagen

En la Segunda Guerra Mundial analizaban los aviones que **volvían** con agujeros de bala para
decidir dónde blindar. El matemático Abraham Wald dijo: blinden donde los que volvieron NO tienen
agujeros — los que recibieron balas ahí **no volvieron**. Los datos que ves son los supervivientes;
la lección está en los que no aparecen.

## Cómo distorsiona todo en cripto

| Lo que ves | Lo que no ves |
|---|---|
| "BTC siempre se recupera" | Los miles de tokens que cayeron 99% y **nunca** volvieron |
| "Comprar el dip funciona" | Funciona en los activos que sobrevivieron; en los muertos era comprar camino a cero |
| Gurús con racha ganadora | Los cientos que quebraron y borraron la cuenta; alguien iba a acertar por puro azar |
| Estrategias famosas rentables | Las mil variantes idénticas que fallaron y nadie publicó |
| Backtests sobre el top 10 actual | El top 10 de hace 5 años incluía monedas hoy irrelevantes |

El último punto es clave para backtesting: si eliges los activos a backtestear **porque hoy son
grandes**, ya metiste el futuro en la selección. "BTC subió mucho" es en parte la razón por la que
lo estás mirando.

## Defensas prácticas

1. Preguntar siempre: **¿dónde está el cementerio?** ¿Cuántos intentaron esto y no aparecen?
2. Desconfiar de reglas derivadas de "los ganadores siempre hicieron X" — los perdedores
   probablemente también hicieron X.
3. En backtests multi-activo, usar el universo de activos **tal como era en cada fecha**, no el
   de hoy (difícil en cripto; al menos reconocer la limitación por escrito).
4. Ante cualquier track record: pedir el historial completo, incluyendo lo abandonado.

## Cómo aplica al AGENTE TRADING

- El bot opera BTC y ETH — los dos máximos supervivientes de cripto. Honestidad obligada: todo
  backtest sobre ellos hereda su historia de supervivientes; los resultados **no se generalizan**
  a "cripto en general" ni justifican añadir monedas chicas con la misma lógica.
- Con nuestros propios datos también aplica: si el bot descarta análisis fallidos o solo
  registramos los trades ejecutados (convicción ≥ 8), evaluar "qué habría pasado" exige guardar
  también las señales **no ejecutadas** — el cementerio propio. Los análisis c/2h ya se persisten:
  usarlos.
- Al leer hilos de traders exitosos con Luis: primera pregunta siempre, ¿cuántos hicieron lo mismo
  y quebraron en silencio?

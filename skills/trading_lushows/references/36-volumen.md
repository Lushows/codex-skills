# 36 — Volumen

El **volumen** es cuánto se negoció en cada vela (cuántos BTC/ETH cambiaron de manos). El precio
dice QUÉ pasó; el volumen dice CUÁNTA convicción hubo detrás. Es de los pocos datos que no
deriva del precio — por eso confirma o desmiente lo que las medias y osciladores repiten entre sí.

## Qué confirma el volumen

| Situación | Lectura |
|---|---|
| Subida con volumen creciente | Movimiento respaldado: hay compradores reales empujando |
| Subida con volumen decreciente | Sospechosa: el precio sube por inercia, sin gasolina |
| Caída con volumen enorme | Puede ser capitulación (los últimos vendedores rindiéndose) |
| Vela gigante de volumen en un giro | Alguien grande actuó ahí: nivel a recordar (`44`) |

## Volumen en rupturas (su mejor uso)

Una **ruptura** (el precio atraviesa un soporte o resistencia) es el escenario donde el volumen
más aporta:

- Ruptura CON expansión de volumen (claramente mayor al promedio reciente) → más probable que
  sea real: hubo participación para sostenerla.
- Ruptura con volumen apagado → candidata a **falsa ruptura**: el precio asoma la cabeza,
  no encuentra seguimiento y vuelve al rango barriendo a los que compraron arriba.

No es garantía — solo probabilidad. Pero filtrar rupturas sin volumen elimina buena parte de
las trampas del régimen `ranging` (`03`).

## OBV básico

El **OBV** (On-Balance Volume) es un acumulador: suma el volumen de las velas verdes y resta el
de las rojas. La idea: si el OBV sube mientras el precio va lateral, alguien está acumulando en
silencio. Útil como concepto; en la práctica es tan propenso a relatos como cualquier línea.

## Límites del volumen en cripto (la parte honesta)

- **Wash trading**: en cripto, parte del volumen reportado es falso — exchanges o bots que se
  compran y venden a sí mismos para inflar cifras. En exchanges menores puede ser la mayoría.
- Mitigación: usar el volumen de UN exchange grande y confiable, y leerlo en términos
  **relativos** (esta vela vs el promedio de las últimas N), nunca en cifras absolutas.
- El volumen de futuros/perpetuos domina el spot en cripto: el "volumen" que mueve el precio
  puede no ser el que estás mirando.

## Cómo aplica al AGENTE TRADING

- El bot **aún no usa volumen** — está en el backlog (`11`) y es probablemente el candidato #1:
  es la única pieza propuesta que agrega información independiente del precio.
- Implementación mínima honesta: `volumenRelativo = volumen de la vela / promedio de 20 velas`,
  calculado en JS y pasado a Claude como un campo más. Uso: rupturas y entradas con
  volumenRelativo < 1 pierden convicción; > 1.5-2 la ganan.
- No hace falta OBV ni indicadores de volumen sofisticados para el swing 1h: con el relativo
  por vela se captura el 80% del valor.

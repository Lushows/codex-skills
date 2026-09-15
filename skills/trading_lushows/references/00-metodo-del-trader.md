# 00 — Método del trader sistemático

## Los 4 pilares (en orden de importancia)

1. **Supervivencia** — nunca arriesgar tanto que una racha mala te saque del juego. El trader que
   sobrevive 10 años le gana al genio que quiebra en el año 2.
2. **Edge (ventaja)** — solo se opera cuando hay una razón estadística para esperar ganar. Sin edge
   demostrado, operar es pagar comisiones por entretenimiento.
3. **Consistencia** — el mismo proceso, todas las veces. Un sistema que se obedece a medias no es
   un sistema, es impulso con excusas.
4. **Aprendizaje** — cada trade alimenta la memoria (traderMemory + meta-análisis semanal). El
   sistema que no aprende de su historia repite sus pérdidas.

## Expectancy: la única fórmula que importa

```
Expectancy = (win_rate × ganancia_promedio) − (loss_rate × pérdida_promedio) − costos
```

Si es positiva con muestra suficiente (≥30 trades), hay edge. Si es negativa, ningún money
management la salva — solo reduce la velocidad de la sangría. Todo cálculo → `Matematicas_lushows`.

## Proceso > resultado (cómo se audita un trade)

Preguntas correctas tras cada trade (gane o pierda):
- ¿Se respetó el protocolo completo? (psicología → memoria → régimen → técnico → convicción → sizing)
- ¿La convicción registrada justificaba el tamaño?
- ¿El stop estaba donde el análisis lo pedía, o donde "dolía menos"?
- ¿Qué dice este trade sobre el sistema, no sobre la suerte?

Pregunta incorrecta: "¿ganamos o perdimos?" — en muestras chicas el azar domina el resultado.

## El ciclo del sistema (AGENTE TRADING)

```
paper (aprender gratis) → testnet (probar la tubería real gratis) → live chico (validar con dinero
que no duele) → escalar (solo con evidencia)
```

Nunca se salta una etapa. El costo de saltarse una etapa siempre es mayor que el tiempo que "ahorra".

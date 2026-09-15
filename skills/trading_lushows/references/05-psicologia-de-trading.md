# 05 — Psicología de trading (humana y del sistema)

Aunque el que opera es un bot, la psicología sigue viva en dos lugares: en las REGLAS que el bot
ejecuta (diseñadas contra los sesgos), y en LUIS cuando mira el dashboard y siente cosas.

## Los bloqueos automáticos del bot (tradingPsychology.js — JS puro, gate ANTES de gastar tokens)

| Bloqueo | Regla | Sesgo que mata |
|---|---|---|
| Racha perdedora | 3 pérdidas seguidas → cooldown 4h | Revenge trading (recuperar apostando ya) |
| Overtrading | >5 trades en 24h → BLOCK | Adicción a la acción; el mercado no paga por operar mucho |
| Veredictos | OK / WARNING / BLOCK | BLOCK corta el pipeline entero |

## Los sesgos que el sistema YA exhibió (evidencia real, jul-2026)

- **FOMO estructural**: tras 4 wins seguidos, el bot entró 3 veces en precio extendido y perdió
  las 3. No "siente" FOMO, pero su prompt sin filtro de extensión produce el mismo comportamiento.
  Moraleja: los sesgos también se programan sin querer; se corrigen con reglas, no con regaños.
- **Trade fuera de protocolo**: 1 trade con convicción 0/10 y régimen unknown se ejecutó igual
  (posible bug del auto-trader, en investigación — `11`). El sistema debe hacer imposible lo
  prohibido, no confiar en que "no debería pasar".

## Psicología de Luis (el dueño del sistema)

1. **No tocar las reglas después de una racha** — ni de wins (euforia → subir riesgo) ni de
   pérdidas (miedo → apagar justo antes de que el edge pague). Las reglas se cambian en frío,
   con datos, y quedan escritas ANTES de la siguiente vela.
2. **El P&L diario es ruido.** Se mira el proceso semanal (meta-análisis) y la muestra acumulada.
3. **Paper con seriedad**: si en paper haces trampa (reiniciar, ignorar reglas), en real pagas
   la escuela con intereses.
4. **En live**: definir de antemano qué te hace apagar el bot (kill switch humano) para no
   decidirlo con el estómago a las 3am.

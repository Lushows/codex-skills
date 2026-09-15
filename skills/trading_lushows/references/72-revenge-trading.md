# 72 — Revenge trading

**Revenge trading** (trading por venganza): operar inmediatamente después de una pérdida, con
tamaño más grande y menos análisis, para "recuperar lo perdido". Es la vía más rápida y mejor
documentada para pasar de una pérdida normal a una cuenta quemada.

## El ciclo completo

```
Pérdida → dolor/rabia → "el mercado me debe" → apuesta más grande, sin plan
       → pierde otra vez (probabilidad intacta, tamaño inflado)
       → dolor x2 → apuesta aún más grande → ... → ruina o capitulación
```

Lo traicionero: cada paso se siente RAZONABLE por dentro. No se siente como rabia, se siente
como "vi una oportunidad clarísima justo ahora". El cerebro disfraza la venganza de análisis.

## Por qué la matemática lo castiga doble

| Error | Consecuencia |
|---|---|
| Subir el tamaño tras perder | Las pérdidas siguientes son más grandes justo cuando el capital es más chico |
| Operar sin setup | El win rate cae por debajo del sistema — operas ruido |
| Operar en caliente | Se saltan stops, se promedia a la baja, se "aguanta" — los errores se apilan |

Perder 1.5% tres veces = −4.4%. Perder 1.5%, luego 5% "para recuperar", luego 10% "la última" =
−15.7%. La venganza no recupera: acelera.

## Señales tempranas en humanos

- Abres el gráfico a los minutos de haber cerrado una pérdida.
- Piensas en plata ("me debe $80") en vez de en setups.
- El tamaño de la siguiente orden es mayor que el estándar "porque esta es segura".
- Sientes urgencia física: hay que hacer ALGO ya.
- Te saltas el checklist "solo por esta vez".

La única intervención que funciona es **tiempo forzado fuera de la pantalla**, decidido ANTES de
la pérdida. En caliente nadie se auto-impone la pausa.

## Cómo aplica al AGENTE TRADING

- **El cooldown es la vacuna**: `tradingPsychology.js` impone 4 horas de bloqueo total tras 3
  pérdidas seguidas, y máximo 5 trades en 24h. Es un gate en JS puro que corta el pipeline ANTES
  de gastar tokens: el bot ni siquiera "piensa" en operar durante el cooldown.
- El bot no siente rabia, pero sin cooldown exhibiría el patrón igual: tras pérdidas en un régimen
  hostil, seguiría encontrando setups en ese mismo régimen hostil y encadenando rojas.
- **La versión de Luis**: la venganza del dueño de un bot es tocar las reglas después de una racha
  perdedora ("le bajo el threshold para que recupere") o apagarlo con rabia. Misma regla: cambios
  solo en frío, con datos, por el backlog (módulo 84) — nunca la misma noche de las pérdidas.
- Si Luis siente el impulso de intervenir tras ver rojas en el dashboard: módulo 77 tiene los
  criterios objetivos. "Estoy molesto" no está en la lista.

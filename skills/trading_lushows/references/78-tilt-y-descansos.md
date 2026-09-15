# 78 — Tilt y descansos

**Tilt** (término prestado del póker): estado emocional alterado — por pérdidas, por euforia, por
cansancio — en el que sigues tomando decisiones pero con el juicio degradado. Lo peligroso del
tilt es que desde adentro no se nota: uno se siente "enfocado" o "decidido", no alterado.

## Señales de tilt (en humanos)

| Señal | Qué indica |
|---|---|
| Chequear el precio/dashboard compulsivamente | Ansiedad al mando |
| Pensar en plata perdida, no en proceso | Modo recuperación (antesala del revenge, módulo 72) |
| "Solo esta vez" / "esta es segura" | El sistema ya fue abandonado mentalmente |
| Irritabilidad fuera del trading (familia, trabajo) | La carga emocional desbordó el compartimento |
| Dormir mal por posiciones abiertas | Tamaño o exposición por encima de tu tolerancia real |
| No poder NO mirar durante un evento de mercado | Fusión identidad↔P&L |

## Por qué los descansos deben ser programados

Pedirle a alguien en tilt que "se dé cuenta y pare" es pedirle al borracho que se auto-retire las
llaves. Los descansos funcionan solo si la regla existe ANTES y se dispara sola:

- **Por resultado**: N pérdidas seguidas → X horas/días sin operar (no "hasta que me calme").
- **Por calendario**: días fijos sin mercado a la semana; el mercado cripto abre 24/7, tu cabeza no.
- **Por evento de vida**: mudanza, pelea, enfermedad, mala noche → no se opera. El juicio ya está gastado en otra cosa.

## Cómo "descansa" el bot

El AGENTE TRADING tiene descansos estructurales, todos automáticos:

1. **Cooldown de 4h tras 3 pérdidas seguidas** (`tradingPsychology.js`) — el equivalente exacto
   del descanso post-tilt, sin necesidad de darse cuenta de nada.
2. **Máximo 5 trades en 24h** — techo de actividad que impide el frenesí.
3. **Ciclo de análisis cada 2h por par** — el bot no "mira velas" entre ciclos; no existe el
   chequeo compulsivo en su diseño.
4. **Threshold de 8/10** — la mayoría de los análisis terminan en HOLD; no operar es su estado normal.

Nota honesta: el bot no descansa porque se canse (no se cansa). Descansa porque las estadísticas
de rachas dicen que operar inmediatamente después de pérdidas seguidas, en el mismo régimen que
las produjo, tiene esperanza negativa. El descanso es matemática, no bienestar.

## Cómo debe descansar Luis

- **La rutina de 30 min/semana (módulo 75) ES el descanso**: define cuándo mirar, y por exclusión,
  cuándo no. Los otros 6.5 días son descanso del sistema.
- Si aparecen las señales de la tabla (chequeo compulsivo, dormir mal por el bot), tratarlo como
  tilt aunque el bot vaya ganando: 1 semana sin abrir el dashboard salvo alerta automática.
- En live, programar de antemano vacaciones del rol de supervisor: quién/qué vigila las alertas
  (módulo 86) mientras Luis desconecta de verdad.

## Cómo aplica al AGENTE TRADING

El sistema ya protege al bot del tilt con cooldowns en código. El eslabón sin proteger es Luis:
su tilt no dispara ningún gate automático. La defensa es la rutina fija + los criterios de
intervención del módulo 77 — reglas externas que funcionan precisamente cuando el juicio interno no.

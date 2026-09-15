# 17 — Tamaño de muestra y azar

**Tamaño de muestra** = cuántos trades cerrados tienes para juzgar el sistema. Es la variable
más ignorada del trading y la que más cuentas mata: la gente decide con 5 trades lo que solo
30-50 pueden empezar a mostrar.

## Por qué <30 trades es anécdota

Imagina una moneda cargada que gana 55% de las veces (un edge real y bueno). Lánzala 10 veces:
es perfectamente normal sacar 3 caras (parece sistema perdedor) o 8 caras (parece máquina de
dinero). **El edge existe, pero 10 lanzamientos no alcanzan para verlo.** Con 30 empieza a
asomarse; con 100 ya casi no se puede esconder. Los números exactos de "cuánta confianza da
cada tamaño de muestra" → `Matematicas_lushows` (intervalos de confianza).

## Las rachas son normales, no señales

| Con este win rate... | En 30 trades, una racha perdedora de... | ...es |
|---|---|---|
| 50% | 4-5 seguidas | Esperable, casi segura |
| 40% (viable con R:R 1:2) | 5-7 seguidas | Normal |
| 60% | 3-4 seguidas | Normal |

Un sistema GANADOR va a tener rachas perdedoras feas. Un sistema PERDEDOR va a tener rachas
ganadoras emocionantes. Por eso la regla de sizing (1.5%) se diseña para sobrevivir la racha,
y por eso "va mal esta semana" no es información.

## Las dos caras del disfraz

1. **El azar disfraza basura de edge**: 6 ganados de 8 se siente como "¡funciona!". Es el error
   más caro: escalar capital sobre una racha. (Anti-trampa del `08`: ganar mucho la última
   semana no adelanta el go-live.)
2. **El azar esconde edge real**: un sistema con expectancy positiva puede arrancar 0.89 de PF
   en sus primeros 10 trades por pura varianza. El error simétrico: matar un sistema bueno
   demasiado pronto. Por eso el veredicto KILL exige PF <1.0 **con 50+ trades** y 2 pivotes.

## Reglas prácticas contra el auto-engaño

- **Ninguna conclusión con <30 trades.** Observaciones sí (se anotan en el journal), decisiones no.
- **Sub-muestras cuentan aparte**: "0/3 sobre $1.788" es una PISTA valiosa, no una prueba —
  3 casos. Se convierte en filtro candidato y se valida con más datos, no se declara ley.
- **No cortar la muestra donde conviene** ("desde que ajusté X vamos 4/5"): eso es elegir la
  ventana que confirma lo que quieres creer (sesgo de confirmación).
- **Pre-registrar los umbrales** (como hizo el proyecto el 21-may): decidir ANTES qué números
  significan qué, para que el azar no negocie contigo después.

## Cómo aplica al AGENTE TRADING

- Hoy: **10 trades, PF 0.89**. La lectura estadísticamente honesta es "todavía no sabemos si hay
  edge" — ni "el bot pierde" ni "va a funcionar". Incómodo pero cierto.
- El criterio de ≥30 trades del go-live existe exactamente por este módulo. Si el 22-ago no hay
  30, se extiende el plazo, no se baja la vara.
- El ritmo importa: 10 trades en ~6.5 semanas proyecta ~20-25 al 22-ago. Verificar al día; si el
  ritmo no da, la decisión correcta es esperar más, no aflojar filtros para "generar muestra"
  (eso contamina la muestra con trades peores).
- Cálculos de probabilidad de rachas e intervalos de confianza → `Matematicas_lushows`.

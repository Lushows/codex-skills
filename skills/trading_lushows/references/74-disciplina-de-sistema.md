# 74 — Disciplina de sistema

Un **sistema de trading** es un conjunto de reglas escritas que dicen qué operar, cuándo entrar,
cuánto arriesgar y cuándo salir. **Disciplina de sistema** es ejecutar esas reglas TODAS las
veces, incluidas las veces en que "se siente" que esta vez es distinto.

## Por qué sistema > intuición para retail

La intuición útil existe — pero es reconocimiento de patrones entrenado con años de feedback de
calidad. Un institucional con 20.000 horas de pantalla puede tenerla. Un retail con 6 meses y 40
trades no tiene intuición: tiene sesgos con disfraz (módulo 70).

| | Sistema | Intuición retail |
|---|---|---|
| Medible | Sí — se puede backtestear y auditar | No — cada trade tiene una historia distinta |
| Mejorable | Sí — cambias UNA regla y mides | No — no sabes qué "ajustaste" |
| Consistente a las 3am / tras 3 rojas | Sí | No — el estado emocional decide |
| Escalable a un bot | Sí | Imposible |

## Cuándo la discreción destruye el edge

El **edge** (ventaja) de un sistema es estadístico: gana en promedio sobre muchos trades, no en
cada trade. Cada intervención discrecional rompe la muestra:

- **Saltarse señales que "no se ven bien"** → normalmente filtras las ganadoras incómodas (las
  mejores entradas se sienten feas: comprar en el miedo, no entrar en la euforia).
- **Tomar trades fuera del sistema** → agregas ruido con win rate desconocido.
- **Mover stops "solo esta vez"** → conviertes pérdidas de 1.5% en pérdidas de 8%.
- **Apagar y prender según el P&L reciente** → garantizas estar apagado cuando el edge paga
  (los sistemas recuperan en rachas, y te las pierdes).

La trampa mental: cada intervención individual parece justificada. El daño solo se ve en el
agregado — y como nunca mides el agregado de tus intervenciones, nunca te enteras.

## Obedecer las reglas propias

La disciplina no es aguantar con los dientes apretados. Es diseño:

1. **Reglas escritas y específicas** — "no comprar extendido" no sirve; "no comprar a >X% de la SMA20" sí.
2. **Cambios solo por proceso** — se propone en frío, se anota, se aplica la semana siguiente. Nunca en caliente.
3. **Automatizar lo automatizable** — cada regla que ejecuta una máquina es una regla que no puedes violar a las 2am.
4. **Registrar las violaciones** — si te saltaste el sistema, anótalo y mide cuánto costó. Suele ser la cura.

## Cómo aplica al AGENTE TRADING

- El AGENTE TRADING es disciplina de sistema hecha código: gate psicológico, régimen, técnico,
  convicción y sizing corren igual el lunes eufórico que el viernes de 3 rojas. No se cansa, no
  se aburre, no "le parece" nada.
- El humano sigue en el loop en un solo punto: **Luis puede violar el sistema desde afuera**
  (tocar config en caliente, forzar trades, apagar por miedo). La disciplina que le queda por
  ejercer a Luis es meta-disciplina: obedecer el protocolo de intervención (módulo 77) y el
  proceso de cambios (módulo 84).
- El trade con convicción 0 que se ejecutó por bug (módulo 85) muestra la otra cara: el sistema
  también debe ser disciplinado CONSIGO MISMO — cada capa verifica, ninguna confía.

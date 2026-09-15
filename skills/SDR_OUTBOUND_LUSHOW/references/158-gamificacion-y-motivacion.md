# 158 — Gamificación y motivación

El trabajo del SDR es, por diseño, un desgaste: 95% de "no", tareas repetitivas, resultados que no controla del todo. Sin un sistema deliberado para mantener la energía, el volumen cae, la calidad se erosiona y la gente se quema (ver `159`). La gamificación —convertir el trabajo en juego con metas, marcadores y premios— y la gestión de la motivación son la palanca que sostiene el ritmo diario **sin** empujar a la gente al agotamiento. Bien hecha, motiva; mal hecha, premia el volumen basura y crea una cultura tóxica de "número a cualquier costo". Este módulo es cómo hacerla bien.

## El principio: gamifica el proceso, no solo el resultado

El error clásico es gamificar solo el resultado final (reuniones, ventas). Problema: el resultado depende de suerte y timing, no solo del esfuerzo —así que el SDR que trabajó bien pero no cerró se desmotiva, y el sistema premia a veces al que tuvo suerte. La gamificación sana premia también el **input controlable**:

- **Input (lo que sí controla):** toques de calidad, conversaciones, cuentas investigadas. Premiarlo mantiene el motor andando incluso en semanas secas.
- **Output (resultado):** SQL, reuniones. Es la meta, pero llega a rachas.

**Regla:** premia el *proceso de calidad* (no "quién mandó más correos" — eso genera spam, ver `84`). Gamifica "quién personalizó mejor", "quién tuvo más conversaciones reales", no "quién disparó más envíos". Lo que gamificas, lo obtienes.

## Los motivadores reales (más allá del dinero)

El dinero (comp, ver `154`) es necesario pero no suficiente. Lo que sostiene el ánimo día a día es psicológico:

| Motivador | Cómo activarlo |
|---|---|
| **Progreso visible** | Marcadores, barras de avance a la cuota; ver que se avanza motiva más que el premio |
| **Reconocimiento** | Celebrar públicamente un buen SQL o un correo brillante; el reconocimiento del líder pesa mucho |
| **Autonomía** | Dejar que el SDR elija ángulos, pruebe cadencias (dentro del playbook) |
| **Dominio / crecer** | Ver que mejora y que hay carrera (ver `156`); el estancamiento mata la motivación |
| **Pertenencia** | Sentirse parte de un equipo, no un remador solo (ver `159`) |
| **Propósito** | Entender que su trabajo genera el pipeline del que vive la empresa |

Un líder que solo aprieta el número ignora cinco de estos seis. El reconocimiento genuino y el progreso visible son gratis y de los más potentes.

## Mecánicas de gamificación que funcionan

| Mecánica | Cómo | Cuidado |
|---|---|---|
| **Leaderboard (marcador)** | Ranking visible de SQL/actividad de calidad | Que no aplaste al de abajo; ver "múltiples formas de ganar" abajo |
| **SPIF / concurso corto** | Premio puntual por un empujón ("hoy, premio al mejor correo del sector salud") | Temporal y con objetivo; si es permanente se vuelve salario esperado (ver `154`) |
| **Celebración de hitos** | Sonido/gong/mensaje al agendar un SQL; celebrar el primer SQL de un nuevo | Que celebre calidad, no cualquier reunión |
| **Retos de equipo** | Meta colectiva del pod con premio grupal | Fomenta ayuda mutua (ver `150`, `157`) |
| **Racha (streak)** | Días seguidos cumpliendo la actividad de calidad | Premia consistencia, el hábito clave del SDR (ver `67`) |

**Múltiples formas de ganar:** un solo leaderboard de SQL siempre lo gana el mismo, y desmotiva al resto. Crea varias categorías: "más mejorado", "mejor personalización de la semana", "mejor manejo de objeción", "racha más larga". Así todos tienen algo por lo que competir, no solo la estrella.

## El equilibrio: volumen sin quemar gente

El outbound exige volumen consistente, pero exprimir sin cuidado quema (ver `159`). El balance:

- **Metas de actividad como piso, no como látigo.** La actividad (toques/día) es un mínimo saludable para que el motor ande, no una vara para castigar. Si alguien cumple actividad y aún no rinde, el problema es *calidad* (coaching, `156`) o *conversión* (`83`), no más volumen.
- **Ritmo sostenible, no sprints eternos.** El SDR premia al que hace los toques *todos los días* (ver `86`), no al que hace 500 el lunes y se apaga. Un concurso ocasional (SPIF) da un empujón; en modo sprint permanente, la gente colapsa.
- **Protege el foco (ver `67`):** bloques de trabajo profundo sin interrupciones producen más que 8 horas fragmentadas. Más horas ≠ más resultado.
- **Reconoce el esfuerzo en las semanas secas.** El timing hace que a veces el buen trabajo no rinda; si solo celebras resultado, castigas la mala suerte y matas la moral.

## Ejemplo: sistema de motivación semanal de un pod

```
Diario:
  - "Gong" (sonido/emoji en el canal) cuando alguien agenda un SQL válido.
  - Barra de avance del pod hacia la meta semanal, visible para todos.

Semanal (en la review de equipo, ver 157):
  - Reconocimiento: "correo de la semana" (el mejor, se suma al swipe).
  - Categorías de leaderboard: más SQL · más mejorado · mejor objeción · racha.
  - Micro-premio rotativo (no siempre dinero: un almuerzo, salir temprano un viernes).

Puntual (SPIF, 1–2 veces al mes máx):
  - Concurso corto con objetivo claro ("esta semana, foco en cuentas enterprise").
```

Los premios no tienen que ser caros: reconocimiento público, tiempo libre, elegir en qué cuentas trabajar. El costo exacto de los incentivos y su encaje en el presupuesto → `Matematicas_lushows` y `economist_lushows`.

## Errores comunes

- **Gamificar volumen crudo (correos enviados).** Genera spam y quema deliverability (ver `84`, `40`).
- **Un solo leaderboard.** Siempre gana el mismo; desmotiva al 80% del equipo. Múltiples categorías.
- **SPIF permanente.** Deja de motivar y se vuelve salario esperado (ver `154`).
- **Solo premiar resultado.** Castigas la mala suerte y el timing; premia también el proceso de calidad.
- **Sprint eterno disfrazado de "cultura de alto rendimiento".** Es la receta del burnout (ver `159`).
- **Ignorar el reconocimiento (que es gratis) y confiar todo al dinero.** El dinero solo no sostiene la moral.
- **Competencia que enfrenta al equipo.** Si el leaderboard vuelve tóxico el ambiente, apágalo; suma retos de equipo.

## Siguiente paso

Monta un sistema simple: celebración diaria de SQL, barra de progreso visible, y un reconocimiento semanal con **varias** categorías (incluida "más mejorado"). Usa SPIFs cortos y ocasionales, nunca permanentes. Pon las metas de actividad como piso saludable, no como látigo, y protege el foco (`67`). Todo esto alimenta la retención → `159`; se apoya en el coaching y la carrera que dan sentido al esfuerzo → `156`; y premia la calidad que mides en QA → `157`. Para el diseño de incentivos monetarios formales → `154`.

# 65 — Gamificación & sistemas de engagement

Gamificación = **aplicar elementos de juego en contextos no-juego** para motivar comportamiento. La distinción que define todo: **meaningful gamification vs "pointsification"** (la versión hueca: colgar points/badges/leaderboards sobre algo aburrido y esperar magia). Si quitas los puntos y nadie vuelve, no construiste engagement: construiste un soborno. **Léelo para diseñar puntos/progreso/streaks/recompensas sin manipular.** Pareja de 30 (onboarding/activación), 59 (e-learning), 56 (sonido/juice). Regla de oro: **gamifica la fricción, no la pasión.**

## 1. La ciencia de la motivación

**Self-Determination Theory (Deci & Ryan)** — toda motivación intrínseca duradera se apoya en tres necesidades: **Autonomy** (el usuario elige, no rieles forzados) · **Competence** (siente que progresa/domina) · **Relatedness** (conexión social, pertenencia). La buena gamificación alimenta las tres.
**El peligro central — overjustification effect:** introducir una recompensa extrínseca a un comportamiento que **ya era intrínsecamente motivante DESTRUYE la motivación intrínseca** (el cerebro recodifica "lo hago porque me gusta" → "lo hago por el premio"). Nunca pongas puntos sobre algo que la gente ya ama hacer.
**Octalysis (Yu-kai Chou)** — 8 Core Drives: (1) Epic Meaning, (2) Development & Accomplishment (el motor de PBL), (3) Empowerment/Creativity & Feedback, (4) Ownership & Possession, (5) Social Influence & Relatedness, (6) Scarcity & Impatience, (7) Unpredictability & Curiosity (variable reward), (8) Loss & Avoidance (el motor del streak y del FOMO). Eje crítico: **White Hat** (drives 1-3: empoderan, hacen sentir bien, no crean urgencia) vs **Black Hat** (drives 6-8: urgencia, ansiedad, adicción — funcionan corto plazo pero queman). Ético = **White Hat para retención sostenida, Black Hat con cuentagotas.**

## 2. Las mecánicas y cuándo cada una funciona

| Mecánica | Funciona para | Riesgo |
|---|---|---|
| **Points/XP** | Feedback inmediato del esfuerzo (Duolingo da XP *antes* de cerrar la lección) | Inflación: si todo da puntos, nada importa |
| **Levels/progression** | Pacing de contenido, mastery | Grind vacío sin valor real por nivel |
| **Badges/achievements** | Marcar hitos, expresar identidad | Hollow badges: si no significan nada, son ruido |
| **Leaderboards** | Solo el top ~10% | **Desmotiva al 90%**; usa ligas pequeñas, relativas, con reset |
| **Streaks** | Loss aversion brutal (7 días = 3.6× retención) | **Streak anxiety**: culpa, notificaciones acosadoras |
| **Progress bars** | Zeigarnik + endowed progress | Falsa sensación sin sustancia detrás |
| **Variable rewards** | Curiosidad, dopamina | Variable-ratio = el motor de las slot machines (línea fina con gambling) |

**Leaderboards bien hechos:** liga semanal de pocos jugadores (Duolingo agrupa ~30), reset periódico (siempre puedes volver), promoción/descenso por tramos. Nunca un ranking global donde el novato aparece en el puesto 4.000.000.
**Endowed progress effect:** marca la **primera tarea ya completada** ("Cuenta creada ✓") en el checklist de onboarding → el usuario percibe que ya arrancó y completa 3× más. Combínalo con Zeigarnik (una barra al 20% pide ser terminada).

## 3. Engagement loops & diseño de hábito

**Hooked Model (Nir Eyal)** — el loop de 4 pasos: (1) **Trigger** (externo al principio → migrar a *internal trigger*: una emoción/contexto dispara la acción), (2) **Action** (el comportamiento más simple posible; reduce fricción al mínimo), (3) **Variable Reward** (impredecible; tres tipos — *Tribe* social, *Hunt* recursos, *Self* mastery), (4) **Investment** (el usuario invierte tiempo/datos/contenido que **carga el siguiente trigger** y hace el producto más valioso — esto crea stickiness real, no los puntos).
**Player's Journey (Amy Jo Kim)** — tres fases que servir distinto: **Onboarding** (Newbie: enseñar, primera victoria rápida) · **Habit-building** (Regular: el loop que convierte novatos en regulares) · **Mastery** ("elder game": contenido profundo para entusiastas — la mayoría de productos lo olvida y pierde a sus mejores usuarios por aburrimiento).
**Engagement vs addiction (la línea moral):** engagement = vuelve porque obtiene valor y se va satisfecho (autonomy intacta); addiction = vuelve compulsivamente contra su propio interés y se siente peor. Test: *¿el usuario estaría contento de saber cómo lo haces volver?* Si no, es manipulación.

## 4. Aplicándolo (superficies reales)

- **Learning (Duolingo deep):** el **streak** (loss aversion) + **Streak Freeze** que redujo churn 21% (válvula humana); **Hearts** limitan errores (deliberadamente ansiógeno como trigger de conversión); **Leagues** (10 tiers, reset semanal) subieron lesson completion 25%. En 2025 mide "Time Spent Learning *Well*", no solo DAU. Lección: la mecánica sirve al *outcome verdadero* (aprender), no a la métrica vana.
- **Fitness/health (Apple rings, Strava):** cerrar anillos = competence visualizada; retos sociales = relatedness.
- **Loyalty/e-commerce:** **tiers** (Bronce→Diamante) con barra de progreso al siguiente tier (81% de consumidores la prefiere). 2026: funciona **anclada en comportamiento**, fracasa como "capa cosmética de badges".
- **Fintech:** metas de ahorro visualizadas, redondeos, hitos celebrados (aquí el progreso ES el valor real).
- **Community:** reputación/karma (Stack Overflow, Reddit) = relatedness + ownership (funciona porque el status es real y ganado).
**¿Encaja vs tacked-on?** Encaja con (a) repetición de comportamiento, (b) progreso medible, (c) fricción que vencer. Se siente pegado sobre una acción única, ya placentera, o sin sustancia.

## 5. El craft del feedback y la "juice"

**Juice no es decoración, es comunicación:** la capa audiovisual que da peso y consecuencia a la acción (el "pop" al recoger una moneda, el micro-bounce del botón). Confirma al cuerpo que algo pasó.
- **Momentos de celebración:** confetti al completar, animación de level-up, el reward reveal con anticipación (la caja que se abre lento).
- **Sound design** (liga con 56): el chime de XP de Duolingo, reconocible y dopaminérgico — corto, distintivo, opcional.
- **Visualización de progreso:** la barra que se llena con animación suave vale más que el número final.
- **RESTRAINT (lo más olvidado):** sin moderación el screen-shake marea y el confetti en *cada* acción se vuelve ruido ignorado. Celebra hitos reales, no cada clic.
- **A11y:** respeta `prefers-reduced-motion`; el feedback nunca *solo* color (daltonismo) ni *solo* sonido.

## 6. Ética y 2026 (crítico)

**El dark side documentado:** 40% de adolescentes limitan voluntariamente el smartphone por ansiedad/FOMO/burnout que generan apps que premian la atención y castigan la ausencia.
**Regulación 2026 (va en serio):** Bélgica/Países Bajos prohíben **loot boxes pagadas** como gambling; Brasil prohíbe venderlas a menores (mar 2026); **PEGI** (jun 2026) da mínimo PEGI 16 a juegos con "paid random items"; la UE empuja el **Digital Fairness Act**. La variable-ratio reinforcement de las loot boxes es **literalmente el mecanismo de las slot machines**.
**Gamificación ética (player-centric):** respetar autonomy (opt-outs reales, sin guilt-tripping, sin notificaciones acosadoras) · **well-being angle** (la IA puede detectar señales de distrés y sugerir pausas) · **AI-personalized challenges** (servir la mecánica óptima a cada cluster, con privacidad) · **saber cuándo NO gamificar** (temas serios/sensibles, salud, duelo, finanzas críticas; o si solo sirve a tu métrica contra el interés del usuario). **Backlash 2026:** el mercado castiga la manipulación; la diferenciación es lo *meaningful*.

## Gamification anti-patterns — blacklist
**pointsification** (PBL pegado sobre experiencia vacía, sin tocar la motivación real) · **leaderboards que desmoralizan** (ranking global que aplasta al 90% inferior) · **streaks manipuladores** (guilt-tripping, notificaciones acosadoras, sin streak freeze) · **FOMO/scarcity artificial** (urgencia falsa, contadores fabricados) · **gambling mechanics/loot boxes** (variable-ratio con dinero real, especialmente a menores — riesgo legal 2026) · **extrínsecos que matan lo intrínseco** (poner puntos sobre algo que ya amaban — overjustification) · **gamificar lo que no se debe** (temas serios/sensibles/ya motivantes) · **hollow badges** (logros sin significado ni status real) · **juice sin restraint** (confetti/shake en cada acción hasta volverlo ruido; o sin `prefers-reduced-motion`) · **optimizar la métrica vana** (diseñar para DAU/engagement contra el bienestar — Duolingo mide "learning *well*") · **Black Hat puro** (todo urgencia/pérdida/adicción: convierte hoy, quema y demanda mañana).

# 50 — UX research, estrategia de producto & discovery

La capa que viene ANTES del diseño visual: decidir **QUÉ construir y PARA QUIÉN**, para que el diseño resuelva problemas reales, no solo se vea bien. Convierte al diseñador en *product thinker*. **Léelo antes de diseñar algo nuevo o cuando no sepas si el problema es real.** Principio rector: **"enamórate del problema, no de la solución."** Pareja de 00 (director), 30 (onboarding), 49 (growth).

## 1. El mindset & proceso de discovery

**Por qué investigar antes de diseñar:** el error más caro no es construir mal, es construir lo correcto para el usuario equivocado — o algo que nadie necesita (Cagan: ~la mitad de las ideas nunca funcionan). Discovery mata ideas malas baratas.
**Double Diamond:** **Discover** (abrir: research generativo del problema) → **Define** (cerrar: un problem statement, "How might we…") → **Develop** (abrir: muchas soluciones) → **Deliver** (cerrar: prototipar/testear/lanzar). Error clásico: saltar al 2º rombo sin hacer el 1º.
**Problem space vs solution space:** el problema/dolor ("no recuerdo mis pedidos") vs la solución ("botón de re-pedido"). Nunca pases a soluciones sin explorar el problema. Una feature es *una* solución entre muchas.
**Continuous Discovery (Teresa Torres):** discovery no es un proyecto episódico, es **hábito semanal** — "weekly touchpoints with customers, by the team building the product". El **Opportunity Solution Tree (OST):** raíz = *desired outcome* (métrica, no output) → ramas = oportunidades (dolores en lenguaje del cliente) → sub-ramas = soluciones → hojas = assumption tests. Te obliga a *comparar oportunidades*, no a enamorarte de la 1ª idea. Hábito keystone: **habla con un cliente cada semana.**
**Research vs validation:** *research/generativo* = descubrir lo que no sabes que no sabes (abierto); *validation/evaluativo* = comprobar una hipótesis/diseño. Si solo validas, nunca descubres; si solo exploras, nunca reduces riesgo.
**Lean/scrappy para solos:** 5 entrevistas de 20min por Zoom, test de pasillo, encuesta, leer reviews/tickets como datos. **Consistencia > rigor** (una conversación pequeña cada semana bate un estudio gigante anual).

## 2. Toolkit de métodos

Dos ejes: **cualitativo** (por qué, pocos, profundidad) vs **cuantitativo** (cuántos, muchos, magnitud); **generativo** (descubrir, temprano) vs **evaluativo** (juzgar, después).

| Método | Tipo | Cuándo |
|---|---|---|
| **User interviews** | Cual/generativo | Necesidades, motivaciones, contexto. El caballo de batalla |
| **Usability testing** | Cual/evaluativo | ¿Pueden usarlo? Sobre prototipo o vivo |
| **Surveys** | Cuant/ambos | Validar a escala, actitudes, segmentar. Malo para "por qué" |
| **Card sorting** | generativo | Diseñar IA: cómo agrupa la gente conceptos |
| **Tree testing** | evaluativo | Validar que la navegación deja *encontrar* (reverso del card sort) |
| **Diary studies** | generativo | Comportamiento en el tiempo |
| **Contextual inquiry** | generativo | Observar en su entorno real |
| **Analytics-as-research** | Cuant/evaluativo | Dónde caen/abandonan. El *qué*, no el *por qué* |

**No hacer preguntas leading:** pregunta por el **pasado y lo concreto** ("Cuéntame de la última vez que…"), no el futuro hipotético ("¿Usarías una app que…?" — la gente miente sobre el futuro). ❌"¿No te resultó frustrante?" → ✅"¿Cómo fue esa experiencia?". Abraza el silencio; "5 whys" a la raíz. (*The Mom Test*: pregunta cosas que ni tu mamá podría mentirte.)
**El mito de los "5 usuarios":** Nielsen — 5 encuentran ~85% de problemas de *usabilidad* del *mismo perfil cualitativo*. NO aplica a research cuantitativo ni a múltiples segmentos (5 *por* segmento). Mal usado = excusa para no investigar.
**Tooling 2026:** Maze (con AI moderator), Dovetail (repositorio + síntesis IA), UserTesting, Lookback, Great Question.

## 3. Usability testing (a fondo)

**Protocolo:** (1) 3-5 **tareas como escenarios, no instrucciones** (❌"haz click en Checkout" → ✅"acabas de decidir comprar, complétalo" — nunca menciones la UI); (2) **think-aloud** (narra en voz alta, tú callas); (3) **observa** (success rate, tiempo, errores, dónde dudó/se frustró — "no te testeamos a ti, testeamos el diseño"); (4) moderado (repreguntas) vs no-moderado (escala, sin sesgo); (5) **prototipo antes de construir** (10× más barato que en producción).
**Severity rating (Nielsen 0-4):** 0 no-problema · 1 cosmético · 2 menor · 3 mayor (arreglar) · 4 catástrofe (antes de lanzar). Prioriza severidad × frecuencia.
**Heuristic evaluation — 10 heurísticas de Nielsen** (experto, sin usuarios, barato): visibilidad del estado · match con el mundo real · control y libertad (undo) · consistencia · prevención de errores · reconocer > recordar · flexibilidad/eficiencia · estético/minimalista · recuperarse de errores · ayuda/documentación.
**Guerrilla/hallway:** 5 personas en una cafetería, 5min, café a cambio → 80% de los problemas groseros por ~$0.

## 4. Jobs-to-be-Done & cliente

**El "job"** (Christensen/Moesta): *"la gente no compra productos, los contrata para un trabajo."* El **milkshake** (se "contrataba" a las 8am para amenizar el commute con una mano, competía con bananas no con otros shakes). **3 dimensiones:** **funcional** (la tarea), **emocional** (cómo quiero sentirme), **social** (cómo quiero ser visto). Diseñar solo para el funcional deja la mitad del valor.
**JTBD vs personas:** personas = *quién* (riesgo de estereotipo); JTBD = *qué progreso busca* (accionable). Pragmático: personas para empatía, JTBD para decisiones de feature.
**4 Fuerzas del Progreso (el switch):** **Push** (frustración con lo actual) + **Pull** (atracción a lo nuevo) > **Anxiety** (miedo a lo nuevo) + **Habit** (inercia). Implicación: no basta seducir (pull) — **reduce ansiedad** (onboarding, garantías, demos) y rompe hábito.
**El JTBD interview:** no preguntas features; reconstruyes la *historia de una compra reciente* (el "struggling moment" detonante + la timeline completa).
**Otras:** customer journey map (fases/acciones/pensamientos/emociones/pain points), empathy map (Says/Thinks/Does/Feels).

## 5. Estrategia & priorización

**Strategy stack:** **Vision** (norte 3-5 años) → **Strategy** (cómo ganamos, qué *no* hacemos) → **Roadmap** (outcomes) → **Backlog**. Estrategia es elegir, y elegir es **decir no**.
**Problema que vale la pena:** ¿frecuente? ¿doloroso? ¿suficiente gente? ¿pagarían/cambiarían? + positioning (por qué tú).
**Frameworks:** **RICE** = (Reach×Impact×Confidence)÷Effort (escapa del HiPPO) · **Value/Effort 2×2** (quick wins primero) · **Kano** (Basic/must-be, Performance/lineal, Attractive/delighters, Indifferent — los delighters de hoy son los must-be de mañana) · **Opportunity scoring** (importancia alta + satisfacción baja).
**MVP vs MLP:** MVP minimiza esfuerzo para aprender (riesgo: tan crudo que aprendes la lección equivocada); **MLP (Minimum Lovable Product)** = lo mínimo que la gente *ame*, no solo tolere.
**Riskiest Assumption Test (RAT):** ataca primero el supuesto que, si es falso, hunde todo (más barato que un MVP). 4 riesgos de Cagan: value, usability, feasibility, viability.

## 6. Síntesis, insights & 2026

**De research a insight:** **affinity mapping** (cada observación en un post-it, agrupa por temas, nombra clusters → patrones, no anécdotas). **Observación ≠ insight:** obs "3 no encontraron el botón" → insight "esperan checkout arriba porque vienen de mobile" (responde al **"so what?"** + sugiere acción).
**Comunicar:** **research repository** (Dovetail/Notion) para que no muera en un drive; highlight reels de 2min + top 5 insights, no informes de 40 páginas.
**Sesgos:** confirmation (oír solo lo que confirma), leading questions, sample bias (solo usuarios felices/disponibles). Mitiga: recluta diverso, abierto, revisa tu guion, registra *evidencia* no opinión.
**IA en research 2026:** 69% de researchers usan IA (síntesis con IA de transcripciones, AI-moderated interviews que repreguntan 24/7). **Synthetic users** (personas IA que "responden") = peligrosos ("30 respuestas sintéticas iguales = una opinión multiplicada", sobre-desempeñan/falsos positivos). **Regla:** IA acelera *síntesis*, no reemplaza *recolección*; nunca automatices moderador + participante a la vez.

## Research/strategy anti-patterns — blacklist
research theater (investigar para justificar una decisión ya tomada) · leading questions · ignorar el research (investigar y construir lo que el HiPPO quería igual) · analysis paralysis (investigar sin decidir/enviar) · building without talking to users (el pecado original) · designing for yourself ("yo soy el usuario" — eres el outlier) · solo validar nunca descubrir · solution-first (enamorarse de la feature antes de entender el problema) · confiar en synthetic users como reales · vanity metrics como North Star · reportes que nadie lee · "5 users" mal aplicado (coartada para no hacer research cuantitativo/multi-segmento).

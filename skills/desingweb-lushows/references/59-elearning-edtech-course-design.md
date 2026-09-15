# 59 — E-learning, EdTech & diseño de cursos online

El dato que reordena todo: los cursos **self-paced de pago promedian 10-20% de completion** (los gratuitos masivos <3-5%); los **cohort-based llegan a 40-90%**. Diseñar e-learning no es diseñar contenido bonito: es diseñar para que el humano **vuelva mañana, practique y recuerde**. **Léelo para productos educativos, cursos, LMS, onboarding como aprendizaje.** Pareja de 17 (copy/conversión para la sales page), 16 (a11y), 47 (onboarding). Regla de oro: **completar ≠ aprender — diseña para retención, no para completion.**

## 1. Learning experience design & la ciencia (el cimiento)

El diseño bonito sin ciencia produce cursos que nadie termina ni recuerda. No negociables:
- **Cognitive Load Theory (Sweller):** memoria de trabajo ~4 elementos a la vez. Reduce carga *extrínseca* (la del mal diseño): un objetivo por lección, sin texto decorativo, **no narrar Y subtitular el mismo texto** (redundancy effect), señaliza lo importante. **Chunking:** módulos de un solo concepto.
- **Active recall > relectura pasiva:** testearse recupera mejor que releer → **quizzes de baja apuesta intercalados** (no solo al final); preguntar antes de enseñar (pretesting) activa la curiosidad.
- **Spaced repetition (curva de Ebbinghaus):** sin refuerzo se olvida ~70% en una semana. Schedule práctico que el producto automatiza: **review a 24h, día 3, 7 y 14** (tarjetas/recordatorios, no esperar que el alumno lo haga solo).
- **Scaffolding & dificultad deseable:** andamiaje que se retira; el esfuerzo *justo* (no excesivo) consolida.
- **Frameworks:** **ADDIE** (Analyze→Design→Develop→Implement→Evaluate, iterativo) como columna; **Bloom's revisada** (Remember→Understand→Apply→Analyze→Evaluate→Create) para escribir **learning objectives medibles** con verbo por nivel ("será capaz de *diseñar*…", no "*conocer*…"). Cada evaluación se alinea al nivel de Bloom de su lección.
- **Micro-learning:** módulos de **3-10 min** (ideal 2-5), un objetivo único, mobile-first.

## 2. Course / lesson UX (la estructura)

Una gran UX de aprendizaje "se siente como una conversación guiada: siempre sabes dónde estás, qué sigue y por qué importa".
**Arquitectura:** Curso → Módulos → Lecciones → Unidades. **Learning path visible** con barra de progreso *siempre presente* (convierte el instinto de cierre en motor de motivación).
**Lesson page:** layout dominante = **video + transcript/texto + ejercicio + recursos** en una vista. El **player** es clave: velocidad (0.75x-2x), **captions** obligatorios, **transcript navegable y buscable** (click en frase salta al timestamp), **notes con timestamp**, auto-complete al terminar, sync cross-device ("continuar donde lo dejaste"), **descargas offline**. El patrón de mayor impacto: **quizzes embebidos en el video** (pausa y pregunta) para romper la pasividad.
**Navegación:** linear/gated (fuerza secuencia, mejor principiantes) vs free (autonomía, mejor referencia). Híbrido recomendado: **path sugerido + libertad de salto**. Botón **"Siguiente lección"** prominente y omnipresente.
**Progress & dashboard:** % por módulo y global, racha, próximo paso explícito, tiempo restante. El dashboard responde en 1 seg: *qué hago ahora*.

## 3. Engagement, motivación & completion (el problema #1)

Por qué fallan: sin accountability, sin fechas, sin comunidad, sin quick win, video-only pasivo. Tácticas reales:
- **Accountability estructural (lo más efectivo):** cohortes con **deadlines y pares** → completion 40-90% vs <20% self-paced. Si es self-paced, simúlala: deadlines suaves, "study buddies", challenges con fecha.
- **Onboarding al curso:** **un solo quick win** en la 1ª sesión (logro tangible en minutos) construye hábito. 1-2 preguntas de segmentación → path personalizado (activación +30-50%).
- **Gamificación bien hecha (learning-first):** progreso, **streaks**, badges con significado, XP atado a *demostrar* skill (no a clicks). Datos: gamificados hasta ~90% completion vs ~25% y **+45% retención**. Atar siempre la mecánica al aprendizaje real.
- **Nudges/reminders:** la mayoría del drop-off es en **días 3-7**. Disparadores **basados en comportamiento** ("llevas 2 días sin entrar, te falta 1 lección del módulo"), no genéricos.
- **Comunidad/social:** foros por cohorte, peer review, ver a otros avanzar.
- **Certificados:** meta tangible al final, mejor si verificables/compartibles en LinkedIn.

## 4. Assessment & feedback

- **Formative vs summative:** la *formativa* (durante, baja apuesta, para aprender) es donde ocurre el aprendizaje; la *summativa* (al final, certifica) valida. Diseña muchas formativas.
- **Instant feedback + answer explanation:** nunca un quiz que solo diga "incorrecto" — explica *por qué* la correcta lo es y por qué las distractoras no (ahí se corrige el modelo mental).
- **Proyectos/assignments:** alineados a **Bloom-Create**, con **rubrics** explícitas (contenido Y pensamiento crítico).
- **Peer review:** alinea con Bloom-Evaluate, escala el feedback y enseña al revisor (necesita rubric guiada).
- **Adaptive learning:** ajusta contenido/ritmo/dificultad rastreando performance y engagement.
- **AI tutoring/feedback (2026, el gran cambio y el diferenciador de producto):** tutores 1:1 24/7 que entienden contexto, dan feedback personalizado y **explican el mismo concepto de varias formas** cuando una no funciona; AI grading da feedback formativo inmediato a escala (el instructor retiene la evaluación final).

## 5. El negocio del curso & plataformas

- **Teachable:** baja fricción, free tier, ideal primer curso (fee ~5% en básico). **Thinkific:** course-focused, mejor student experience, **0% transaction fees** en la mayoría de planes. **Kajabi:** all-in-one (web/email/funnels/comunidad), el más caro (~$89+/mes). **Podia** ligero. **Maven:** referente del **cohort-based course (CBC)**. Self-hosted: Webflow LMS, LearnDash, Outseta.
- **Modelo:** **cohort** (alto precio, alto completion, alto esfuerzo) vs **self-paced** (escala infinita, bajo completion, bajo soporte). Mercado de cursos gamificados ~$19B (2025) → proyección ~$92B (2030).
- **AI-course-creation 2026:** generación asistida de outline/lecciones/quizzes/rúbricas; acelera producción pero exige curaduría humana de la pedagogía.
- La **sales/landing page** se cubre en 17; específico de cursos: testimonios con resultados, currículum expandible, "para quién es / para quién NO es", garantía, instructor authority.

## 6. Accesibilidad, móvil & 2026

**A11y (WCAG 2.1/2.2):** captions + transcripts en todo audio/video (el 85% del video se ve sin sonido → beneficio universal), alto contraste, navegable por teclado/screen reader, **sin límites de tiempo rígidos**, todo multimedia *pausable*. **Diversidad cognitiva:** voz activa, frases cortas, romper muros de texto con bullets/whitespace, sin jerga ni siglas sin explicar. **Mobile learning:** responsive, offline, microlearning nativo del móvil. **2026:** AI tutor personalizado + adaptive paths moment-to-moment + analytics que predicen drop-off antes de que ocurra → **1:1 personalizado a escala**.

## E-learning anti-patterns — blacklist
**video-only pasivo** sin recall ni práctica (se olvida casi todo) · sin active recall ni spaced repetition (curva del olvido sin freno) · **cognitive overload** (muros de texto, múltiples objetivos por lección, narración+subtítulo redundantes, decoración irrelevante) · **sin progreso visible** ni "qué sigue" · **quiz que solo dice "incorrecto"** sin explicación · optimizar completion en vez de learning (gamificación vacía que premia clicks) · **sin accountability** (self-paced puro, sin deadlines/pares/comunidad → <20%) · onboarding sin quick win o sobrecargado de fricción · nudges genéricos ("¡vuelve!") en vez de conductuales · sin captions/transcripts, no responsive, límites de tiempo rígidos, no pausable · **aburrido, sin proyectos reales** (conocimiento inerte que no se aplica). **Mide retención y aplicación, no solo completion.**

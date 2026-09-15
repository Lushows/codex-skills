# 80 — Kids, children's & family-safe design

Diseñar para niños es de las disciplinas más exigentes y reguladas del diseño digital — NO es "diseño normal con colores brillantes". Tres verdades gobiernan todo: **los niños NO son adultos pequeños** (cognición/motricidad cambian radicalmente por edad), **la audiencia es dual** (el niño usa, el padre decide y paga), y **el peso ético/legal es máximo** (COPPA, Children's Code, GDPR-K te obligan; manipular a un niño es ilegal además de inmoral). **Léelo para edu-infantil, juegos/contenido para niños, apps familiares.** Pareja de 47 (a11y cognitiva), 65 (gamificación — la ética para niños es extra-estricta), 59 (e-learning), 32 (ética). Regla de oro: **prevención de errores sobre recuperación, y el parental gate ANTES de la acción sensible.**

## 1. El género y las etapas de desarrollo

La investigación de Nielsen Norman Group (*UX Design for Children*, edades 3-12) exige diseñar para **tres bandas cognitivamente distintas**:
- **Early childhood (2-5, preoperacional):** lenguaje/pensamiento simbólico en formación. **No tienen theory-of-mind** (menores de 6 no leen expresiones faciales de personajes ni señales sutiles). Aprovechar modelos del mundo real (el skeuomorfismo funciona — un niño de 3 "hizo pasta" arrastrando fideos a una olla). No saben leer: todo audio + visual.
- **Childhood (6-8, operacional concreta temprana):** lógica naciente, entienden metas y secuencias visuales. Toman instrucciones **literalmente** (si dices "usa el mouse", una niña de 7 abandona su trackpad).
- **Tweens (9-12):** dependen de autocorrect, entienden undo/redo pero prefieren herramientas intuitivas (borrador sobre botón "deshacer").
**Patrón transversal:** la memoria de trabajo de un niño es mucho menor → interfaces auto-explicativas + **prevención de errores** sobre recuperación. La **responsabilidad es asimétrica**: un dark pattern que un adulto detecta, un niño de 6 no puede ni defenderse.

## 2. UX e interacción age-appropriate

**Touch targets:** mínimo **2cm × 2cm para niños pequeños** (4× el tamaño adulto). **Gestos por edad:** 3-5 → solo tap/swipe (movimientos grandes de brazo), touchscreen exclusivo · 6-8 → tap + trackpad, los arrastres largos siguen difíciles · 9-12 → scroll/drag complejo, control casi adulto a los 11. **Regla:** motricidad gruesa madura antes que fina; bajo los 9 años evitar arrastres largos, objetos pequeños, coordinación bimanual y reacciones rápidas. **Pre-lectores:** instrucciones **animadas (visual) + audio simultáneo**, el juego *muestra el estado-meta*, iconografía concreta, nunca texto como único canal. **Feedback inmediato y exagerado** (bajo 6 años las señales sutiles se pierden). **Tolerancia a error** (snap-to-target, hitboxes generosas, sin penalización, múltiples caminos). **Atención:** sesiones cortas, no penalizar el abandono.

## 3. Engagement, aprendizaje y gamificación bien hecha

La línea es nítida: **gamificación alineada con la meta del niño + opt-in + bienestar = motivación; gamificación dirigida a DAU/screen-time = manipulación.** Para niños el estándar es **extra-estricto.**
- **Play-to-learn:** la recompensa debe *enseñar* (desbloquear contenido, dominar un concepto), no dopamina vacía (las recompensas externas excesivas erosionan la motivación intrínseca — ver 65).
- **Personajes/mascotas:** guías que demuestran (modelan la acción para pre-lectores), no solo decoran.
- **Respeto al screen-time:** prompts de descanso, fin de sesión natural, sin "solo una más" (el feedback sensorial estimula vías de recompensa → en niños puede fomentar tendencias adictivas).
- **Equipo:** se diseña con psicólogos infantiles y educadores, no solo game designers.

## 4. Seguridad, privacidad y legal (lo no-negociable)

- **COPPA (EEUU, menores de 13):** regla final 2025, **deadline de cumplimiento 22-abril-2026**. PII ahora incluye identificadores persistentes (device ID, cookies, IP), geolocalización, fotos/audio/video, y **biométricos** (huellas, voiceprint, iris). Requiere **Verifiable Parental Consent (VPC)** antes de recolectar (métodos: micro-cargo 50¢, email+código, ID). Padres deben poder revisar, borrar y revocar — con el backend real para honrarlo.
- **UK Age Appropriate Design Code / Children's Code:** 15 estándares, define niño como **menor de 18**. Aplica **aunque los niños no sean tu target** si es probable que accedan. Mandatos: **privacidad alta por defecto**, minimización de datos, geolocalización **off por defecto**, no compartir datos del niño, y **prohibición explícita de nudge techniques** que empujen a dar datos o bajar la privacidad.
- **GDPR-K:** consentimiento parental (13-16 según país). **Sin ads conductuales a niños. Sin dark patterns** (ilegal). Contenido seguro con moderación + controles parentales.

## 5. La capa del padre y la confianza

El padre es el **decisor** (evalúa seguridad, valor educativo, screen-time, controles, progreso).
- **Parental gate:** tarea de nivel-adulto (reto matemático, "mantén pulsado", arrastre preciso) **obligatoria antes de** compras IAP, salidas a web externa, redes sociales o configuración. **Anti-patrón:** poner el gate detrás de algo que el niño puede resolver. El gate va *antes de la acción*, no del contenido del niño.
- **Parent dashboard:** progreso de aprendizaje, límites de tiempo, control de contenido por edad, revisión/borrado de datos (requisito COPPA), notice de qué terceros reciben datos.
- **Compra/suscripción:** siempre tras el gate. Comunicar confianza (badge de cumplimiento, privacidad legible, "no ads / no data selling").
- **Cuenta familiar:** estructura multi-perfil (un padre administra N niños) con ajustes por edad por niño.

## 6. Estética, accesibilidad & 2026

**Estética kids:** brillante y lúdica **sin sobreestimular**; el craft importa — **no condescender** (ilustración con oficio, no clip-art genérico; color con propósito, no caos cromático; animación con función, jerarquía clara). **Anti-sobreestimulación:** controlar luz, movimiento, haptics y audio (la interfaz controla el entorno sensorial). **Neurodiversidad (autismo, ADHD, dislexia, procesamiento sensorial):** ofrecer **ajustes** (fuente, color, velocidad de animación, nivel de sonido), modo calmado/minimal vs más estimulante, reducir transiciones bruscas, predictibilidad. **2026:** **AI tutors para niños** crecen pero con peso ético máximo (no recolectar datos sin VPC, no generar contenido inseguro, transparencia de que es IA, supervisión parental, sin captura de voz/biometría sin consentimiento); la regulación se endurece.

## Kids/family anti-patterns — blacklist
**tratar a los niños como adultos pequeños** (mismos targets, densidad, lectura) · **dependencia de texto** para pre-lectores (sin audio/visual) · **touch targets pequeños (<2cm) y gestos finos** (arrastres largos, doble mano) bajo 9 años · **mecánicas adictivas/manipuladoras** (streaks de presión, "solo una más", FOMO, recompensas variables tipo loot box dirigidas a niños) · **ads conductuales / behavioral profiling a niños** (ilegal) · **dark patterns** (nudges para dar datos o bajar privacidad — prohibido por Children's Code) · **violaciones COPPA** (recolectar PII incl. device ID/geo/biométricos sin VPC; no permitir borrado/revocación parental) · **parental gate ausente o trivial** (resoluble por el niño), o tras el contenido en vez de antes de la acción sensible · **sobreestimulación** (caos cromático, audio/movimiento incontrolables, sin ajustes para neurodiversos) · **estética condescendiente** o genérica (clip-art) · **geolocalización on por defecto**; privacidad baja por defecto · **contenido sin moderación**; salidas externas sin gate · **IA para niños** sin transparencia/supervisión parental, capturando voz/biometría sin consentimiento.

# 23 · Plantillas de documentos que genera AVIS

> Fuentes: `src/lib/catalogo.ts` (obligaciones con `comoObtener: "genera_avispao"`) y `src/lib/generadorDocs.ts` (las guías `GUIAS` y el flujo `generarDocumento`). Aquí se destila QUÉ produce AVIS y CÓMO debe quedar; no se copia el prompt.

AVIS no solo recuerda papeles: hay **ocho** que **los arma él mismo** (los demás los gestiona o los guía). Cada documento está anclado a su **norma real**, así que el borrador sirve de verdad — no es relleno.

> **Los 8 generables (`genera_avispao`, 24-jun-2026):** los 4 originales (Plan de Saneamiento · Plan de Capacitación · SG-SST · Manual de Bioseguridad estética) **+ 4 nuevos:** **Política de Tratamiento de Datos Personales** (Ley 1581/2012 + Dec. 1377/2013; aplica a casi todos) · **Reglamento Interno de Trabajo** (CST 104-125; comercial 5+ empleados) · **Reglamento de Higiene y Seguridad Industrial** (CST 349; 10+ empleados, compañero del SG-SST) · **Plan de Gestión Integral de Residuos** (Dec. 1076/2015 + Res. 1362/2007 RESPEL; estética/alimentos/salud/taller). El gate `aplica` controla la *lista mínima*; si el cliente lo pide explícito, se genera igual. GUIAS en `generadorDocs.ts`. AVIS lo personaliza con los datos del negocio (nombre, tipo, ciudad, número de trabajadores) y lo entrega en Markdown, **listo para imprimir, completar y firmar**.

**Regla de oro (siempre):** AVIS hace el **borrador**; el dueño lo revisa, completa los datos que faltan (responsable, fechas, firma) y **lo firma**. Mantenerlo vigente es responsabilidad del negocio. AVIS lo recuerda con suavidad, nunca regaña.

> **⚠️ NO confundir GENERAR con GESTIONAR/AVISAR (magnitud legal).** AVIS **GENERA SOLO estos 4 borradores**. Todo lo demás del catálogo —**SAYCO/ACINPRO, Bomberos, Cámara de Comercio, RUT, concepto sanitario, RNT, etc.** (`gestiona_avispao` / `tramita_cliente`)— **NO se genera**: AVIS **te AVISA del vencimiento** y te **GESTIONA/GUÍA** el trámite. Ejemplo claro: **SAYCO es una licencia de música que se PAGA** (valor del simulador de la OSA), no un documento que se redacte. AVIS jamás debe decir "te genero el SAYCO/bomberos/etc.". *(Lección 24-jun-2026: la landing decía "SAYCO → AVIS LO GENERA" = sobre-promesa falsa → corregido; el chat ya era correcto porque filtra por `comoObtener === "genera_avispao"`.)*

> *"Te dejo el borrador armado y aterrizado a tu negocio. Lo revisas, le pones el responsable y la firma, y queda listo para cuando lo pidan."*

Dato técnico: el documento se guarda en la tabla `documentos_generados` (requiere la migración 06). Donde el negocio debe llenar un dato, queda un campo claro: `__________`.

> **⚠️ Lección 23-jun-2026 (bug real de Bendita Pola).** Si el cliente pide un documento generable CONCRETO ("genérame el SG-SST"), AVIS lo genera **DIRECTO**, sin exigir que la obligación "aplique" por perfil. El SG-SST tiene `aplica: numEmpleados >= 1` en `catalogo.ts`, pero el `num_empleados` casi nunca queda capturado en el onboarding (default 0), así que el documento se salía de `obligacionesAplicables` y la petición se caía al vacío (el cliente recibía otra cosa). **Regla:** el gate por perfil (`aplica`) sirve para la *lista* de papeles que se muestra; **NO** para bloquear una generación que el cliente pidió explícitamente. Si lo pide, lo necesita → se genera. Y AVIS **nunca** deja una petición de "genérame" sin respuesta: si no identifica cuál, ofrece la lista de los cuatro que sabe armar. (Fix en `flujoCliente`: `idConcreto` resuelto del texto + `esGenerable(idConcreto)`, independiente de `generables`.)

> **⚠️ Lección 23-jun-2026 (parte 3) — "genéramelo" debe cerrar el ciclo + NO asumir el rubro.**
> (a) Cuando AVIS ofrece un documento ("escribe genérame el SG-SST") y el cliente responde solo
> *"genéramelo / hazlo / dale / ese mismo"* (sin el nombre), antes se buggeaba: el bloque exigía el
> nombre del doc y caía al cerebro → loop. **Fix:** se guarda `onboarding_state.doc_ofrecido` cuando el
> cliente menciona un doc (aunque sea pregunta), y una afirmación de generar (`afirmaGenerar`) usa ese
> doc recordado. Se limpia tras generarlo.
> (b) **NUNCA asumas el rubro.** AVIS estaba hablando como si todos fueran restaurante (SG-SST, bomberos,
> impuesto al consumo) sin saber el negocio. **Reglas:** el cerebro solo ofrece los **documentos
> generables que aplican a ESE rubro** (`generablesNeg`, no los 4 fijos); si el `tipoNegocio` es
> desconocido/genérico, **PREGUNTA primero** qué negocio es antes de dar papeles/impuestos/documentos
> específicos (una zapatería no lleva saneamiento; una persona no lleva SG-SST ni bomberos).

> **⚠️ Lección 23-jun-2026 (parte 2) — el dato de perfil sí debe poder corregirse.** Bendita Pola **sí tenía 2 empleados** pero figuraba `num_empleados = 0` (el onboarding no lo capturó bien), y **no había forma de arreglarlo por chat** porque el onboarding solo corre si falta `tipo_negocio`. Varias obligaciones laborales (SG-SST, exámenes médicos, reglamento) dependen de `numEmpleados >= 1`, así que el negocio quedaba sin esos papeles. **Fix:** AVIS ahora **detecta y actualiza el número de empleados en cualquier momento** ("tengo 2 empleados", "somos 3", "no tengo empleados" → 0) vía `extraerNumEmpleados`, guarda `num_empleados`, recalcula qué papeles cambian y, si ahora aplica el SG-SST, lo ofrece. **Regla general:** los datos clave del perfil (empleados, alimentos, música, local, formalización) deben poder corregirse conversando, no solo en el onboarding inicial — un perfil incompleto NO debe dejar al negocio sin sus papeles.

---

## Plan de Saneamiento Básico

**Para qué sirve.** Es el documento que piden en la **visita sanitaria** de cualquier negocio que maneja alimentos (restaurante, cafetería, panadería, fruver). Sin él, el concepto sale desfavorable. Base legal: **Resolución 2674 de 2013**.

**Secciones (cuatro programas).** Cada programa lleva: objetivo, procedimientos paso a paso, frecuencia, responsable, insumos (con concentraciones donde aplique) y los registros que se diligencian.
1. **Limpieza y Desinfección** — pisos, paredes, superficies, equipos y utensilios.
2. **Manejo de Residuos Sólidos y Líquidos** — separación, recipientes, frecuencia de retiro, disposición.
3. **Control Integrado de Plagas** — prevención, monitoreo, control y empresa autorizada si aplica.
4. **Abastecimiento y Control del Agua Potable** — fuente, tanque de almacenamiento, lavado del tanque.

**Datos que necesita AVIS.** Nombre del negocio, tipo, ciudad. Para completar a mano: responsables de cada programa, fechas y firma.

> *"Manejas alimentos, así que en la visita te piden el plan de saneamiento. Te lo armo con los cuatro programas listos. ¿Lo genero?"*

---

## Plan de Capacitación del Personal

**Para qué sirve.** Demuestra que el personal manipulador de alimentos se capacita. También se revisa en la visita sanitaria. Base legal: **Resolución 2674 de 2013**.

**Secciones.**
- Objetivo general y específicos.
- **Temas:** Buenas Prácticas de Manufactura, manipulación higiénica, enfermedades transmitidas por alimentos, limpieza y desinfección, manejo de residuos.
- Metodología e intensidad horaria.
- **Cronograma mensual** de las capacitaciones.
- Responsable / capacitador.
- **Formato de registro de asistencia** (para diligenciar).

**Datos que necesita AVIS.** Nombre, tipo de negocio, ciudad. A completar: nombres del capacitador y de los asistentes, fechas, firmas.

> *"Va de la mano con el de saneamiento: el plan de capacitación deja por escrito que tu gente se forma. Te lo dejo con cronograma y planilla de asistencia."*

---

## SG-SST (Estándares Mínimos)

**Para qué sirve.** Es el **Sistema de Gestión de Seguridad y Salud en el Trabajo** que toda empresa con al menos un trabajador debe tener. Base legal: **Resolución 0312 de 2019 (Estándares Mínimos)**. El alcance se ajusta al número de trabajadores (microempresa).

**Secciones.**
- **Política de SST** (firmada).
- **Identificación de peligros y valoración de riesgos** — matriz por área/tarea.
- **Plan de trabajo anual** con responsables y fechas.
- Programa de capacitación.
- Entrega y uso de **EPP** (elementos de protección personal).
- **Plan de prevención, preparación y respuesta ante emergencias.**
- Reporte e investigación de incidentes y accidentes.
- Indicadores.

**Datos que necesita AVIS.** Nombre del negocio, ciudad y **número de trabajadores** (clave: define el alcance). A completar: responsable del SG-SST, firma de la política, fechas del plan anual.

**Recordatorio suave.** Además del documento, el negocio debe reportar la **autoevaluación anual** de estándares mínimos en la plataforma del Ministerio. AVIS lo gestiona aparte; el documento es la base.

> *"Como tienes empleados, te toca el SG-SST. Te armo el documento base con la política, la matriz de riesgos y el plan anual. Lo firmas y queda andando."*

---

## Manual de Bioseguridad (estética)

**Para qué sirve.** Lo deben tener peluquerías, barberías, spas y centros de **estética ornamental** para aprobar la visita sanitaria. Base legal: **Resolución 2827 de 2006**.

**Secciones.**
- Principios de bioseguridad.
- Lavado e higiene de manos.
- Uso de elementos de protección personal.
- **Limpieza, desinfección y esterilización** de equipos y herramientas (con productos y tiempos).
- **Manejo de residuos**, en especial cortopunzantes (uso del guardián) y su disposición.
- Bioseguridad por procedimiento.
- Prevención de riesgo biológico para el personal y los clientes.

**Datos que necesita AVIS.** Nombre del negocio, ciudad, tipo de servicios. A completar: responsable, fecha y firma.

> *"Para la visita de salud en tu barbería/spa piden el manual de bioseguridad. Te lo dejo con la parte de esterilización y manejo del guardián bien explicada."*

---

## Cómo lo entrega AVIS (los cuatro)

- Pregunta primero: lo **ofrece**, no lo impone (*"¿lo genero?"*).
- Lo arma con los datos reales del negocio (no genérico).
- Lo entrega como **borrador en Markdown**, con campos `__________` donde falta dato.
- Cierra recordando que es **borrador para revisar, completar y firmar** — y que mantenerlo vigente es del negocio.
- Si algo del negocio no lo tiene AVIS, **no lo inventa**: deja el campo en blanco para que el dueño lo llene.
- Si falla la generación, AVIS lo dice con calma y ofrece reintentar (*"no pude armarlo, inténtalo en un momentico"*).

> **Roadmap:** ampliar la lista de generables (p. ej. plan de residuos hospitalarios para salud, PEI educativo) y agregar exportación a PDF firmable; por ahora AVIS genera estos cuatro y **gestiona o guía** el resto del catálogo.

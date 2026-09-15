# 183 — Information architecture & content structure

**UX architecture.** Organizar/estructurar/etiquetar contenido para que se encuentre. Pareja de 179 (navegación), 28 (search), 22 (SEO/AEO), 45 (editorial). Regla de oro: **IA ≠ navegación (la nav es la punta visible, la IA es la estructura subyacente); la estructura debe coincidir con el modelo mental del usuario, no con el organigrama interno; etiqueta como lo dicen los usuarios.**

## 1. Qué es IA y por qué es invisible cuando está bien

Organizar/estructurar/etiquetar para que la gente encuentre y entienda dónde está. **Precede** al visual design y a la nav (el wireframe es la *manifestación* de la IA). Buena IA = invisible (el usuario fluye); mala IA = dolorosamente visible (no encuentran, recurren al search de emergencia, hacen bounce). Coste económico: abandono, tickets de soporte, "dark content". Los **cuatro sistemas** (Rosenfeld & Morville): organization, labeling, navigation, search.

## 2. Organizar el contenido

**Schemes:** *exact/unambiguous* (alfabético, cronológico, geográfico) vs *ambiguous* (topical, audience, task, metaphor — los más útiles y difíciles). **Hybrid** con cuidado: **un solo criterio por nivel** (mezclar tema + audiencia en un nivel confunde). **Jerarquías:** *broad-shallow* (menos clics, más carga cognitiva por nivel — Hick) vs *narrow-deep* (menos carga por pantalla, más esfuerzo). **Regla:** la evidencia favorece **breadth sobre depth** (escaneamos opciones más rápido de lo que navegamos niveles); heurística ≤4 niveles de profundidad, ≤10 nodos por nivel. **Árbol estricto** (ubicación canónica, bueno para mental model + URLs) **vs facets/tags** (multi-pertenencia, escala — e-commerce: faceted sobre una espina dorsal jerárquica).

## 3. Métodos de investigación

**Card sorting** (los usuarios agrupan tarjetas; **genera** ideas): *open* (crean sus grupos → agrupaciones naturales + lenguaje real), *closed* (grupos dados → **valida** taxonomía), *hybrid*. **Tree testing** (navegan el árbol sin UI, solo rótulos, para tareas → mide **findability**; **card sorting genera, tree testing valida**). **Mental-model match** (la estructura coincide con el modelo del usuario, no el organigrama — Conway's Law en IA es anti-patrón). **Analytics-informed** (search-logs internos = el confesionario del usuario: dice qué palabras usa). Novedad 2026: pedir a un LLM que revise tus labels por ambigüedad antes de testear con humanos.

## 4. Labeling & taxonomía

**Rótulos claros** en lenguaje del usuario (sin jerga/nombres de proyecto — "Precios" ✅ no "Soluciones Synergy" ❌). **Consistencia** (mismo concepto = mismo término; mismo nivel gramatical). **Controlled vocabulary** (un término canónico + sinónimos mapeados). **SEO-aware** (los rótulos son señales para buscadores/answer engines). **Information scent** (cada rótulo promete qué hay detrás; buen scent = el usuario predice y elige bien; débil = clics erróneos, backtracking, abandono — optimizar IA es maximizar scent en cada decisión).

## 5. Sitemaps & flows

**Sitemap** (diagrama jerárquico, el plano maestro). **User/task flows** (cómo se completa una tarea cruzando secciones). **Entry points** (la gente NO siempre entra por la home — llegan por Google/redes/AI Overviews/deep links → **cada página es una potencial portada** y debe ubicar al usuario). **Cross-linking** (rompe silos del árbol, distribuye scent + autoridad SEO). **URL structure como IA** (`/categoria/subcategoria/item` — legible, estable, semántica). **Content inventory/audit** (catalogar TODO antes de reestructurar — ROT: Redundant/Outdated/Trivial).

## 6. Content modeling & el ángulo 2026

**Structured content** (CMS headless: content types con fields tipados, no páginas estáticas — cada pieza es un chunk reutilizable across channels). **Content-first design** (la estructura antes que el layout). **IA para AI / answer engines (AEO)** — el cambio clave 2026: los LLMs **citan contenido estructurado** en vez de rankear páginas → **entity-based structure** (organiza alrededor de entidades claras), **Schema/JSON-LD** (`Article`/`FAQ`/`Product` machine-readable), **self-contained citable units** (respuesta directa primero, formato Q&A conciso). **Governance at scale** (>7 niveles/cientos de content types → workflows/permisos/auditability). **A11y de la estructura:** la jerarquía de **headings (H1→H2→H3) ES IA** para lectores de pantalla (un solo H1, sin saltar niveles, sin headings por estética) — **semántica = accesibilidad + AEO**.

## IA anti-patterns — blacklist
**org-chart IA** (estructurar por departamentos internos) · **jerga interna en rótulos** · **mystery-meat navigation** (rótulos vagos sin scent — "Soluciones", "Recursos", iconos sin label) · **mezclar esquemas en un mismo nivel** · **catch-all "Misc/Otros"** (taxonomía rota) · **demasiada profundidad** (5+ clics; >7 niveles sin governance) · **breadth desbordado** (30 ítems sin agrupar — viola Hick) · **diseñar sin content inventory** · **saltarse el research** (IA por opinión del HiPPO) · **inconsistencia léxica** · **home-centrismo** (asumir que todos entran por la portada) · **headings por estilo** (rompe IA semántica y a11y) · **contenido no estructurado para AI** (sin schema/entidades/unidades citables → invisible para answer engines) · **faceted sin control** (URLs infinitas indexables = crawl traps) · **validar con uno mismo** (testear con el equipo que la diseñó).

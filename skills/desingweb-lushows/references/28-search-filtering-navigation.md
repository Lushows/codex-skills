# 28 — Búsqueda, filtros & navegación UX

Conversion-critical para e-commerce y sitios con catálogo. **Léelo cuando construyas búsqueda, filtros, listados o navegación.** Pareja de 11 (e-commerce) y 21 (forms). Datos de Baymard.

## 1. Site search

**El search es desproporcionadamente valioso:** search users convierten ~1.8× más y generan ~40% del revenue. NN/g: pasar de icono a **search box visible aumentó el uso ~91%**. Colócalo **centrado en el header** o full-width, grande, con lupa + botón submit. **Nunca lo escondas tras un icono** en desktop si el catálogo es grande. Placeholder útil ("Busca productos, marcas o categorías…") + `aria-label`.
**Autocomplete (solo 19% lo hace bien; 75% de usuarios lo busca):** ≤10 sugerencias desktop / 4-8 mobile · distingue **scope suggestions** ("jeans *in Men's*") con estilo propio · **bold solo en el texto predictivo** (lo que el usuario no escribió) · sin scrollbar interno · resalta la sugerencia activa + arrow keys/Enter · oscurece el fondo al activar. **Multi-column premium:** izquierda query/recent/popular suggestions; derecha **product suggestions** (thumbnail + nombre + precio) + categorías. Caso "no suggestions" → muestra bestsellers, no dropdown vacío.
**Typos/sinónimos/instant:** el **69% de sites** falla con misspellings → fuzzy matching (Levenshtein) + synonym dictionary + as-you-type (debounce 150-250ms). El **94% no permite "search within category"** → diferenciador: ofrece scoped search cuando ya está en una categoría.
**Zero-results (lo más importante y descuidado, ~50% sin recuperación):** did-you-mean clicable · query permutations (simplifica "red winter jackets"→"jackets" con preview de top 3-5) · category links de las keywords · bestsellers como salida garantizada · **NUNCA solo "search tips"** · mantén el search bar con el query preservado. Es **una rampa, no un callejón**.
**AI/semantic 2026:** **hybrid search** (keyword precision + vector embeddings para entender intención) es el estándar emergente; capa conversacional ("regalo para mi mamá que ama el café, <$50"). Patrón ganador: AI que **reduce fricción y guía decisiones** (add-to-cart, comparar, pre-fill checkout), no un chatbot de FAQs.

## 2. Faceted search / filtering

Listas mediocres → 67-90% abandono; optimizadas → 17-33%.
**Tipos:** checkbox (multi-select, el caballo de batalla), range slider doble + input numérico, color swatches (visual > texto), rating mínimo (4★+), toggles binarios.
**Multi-select:** el 64% lo espera; el 14% no lo permite (causa abandono). Lógica: **OR dentro de un facet** (Rojo OR Azul), **AND entre facets**. **Checkboxes, no radio buttons.**
**Filter counts:** "Azul (34)"; oculta o deshabilita (greyed, no removible) las que darían cero.
**Applied-filter chips** removibles (✕) encima de resultados + "Clear all" (el 20% no los mantiene visibles).
**Apply vs instant (resuelto por device):** **Desktop = instant filtering** (responsivo, elimina un paso); **Mobile = botón explícito "Show X Results"** con conteo en vivo (los refreshes a mitad de interacción desorientan).
**Placement:** desktop **left sidebar persistente** (visible al scroll); mobile **drawer/bottom sheet** disparado por botón "Filter & Sort" **sticky**.
**Listas largas:** 4-8 opciones + "Show more"; secciones colapsables (key filters abiertos).
**URL state (clave):** codifica filtros en la URL (`?color=azul,negro&precio=0-50&sort=price_asc`) → links compartibles, back button restaura, refresh no pierde, indexable. Sincroniza con `history.pushState`/`replaceState`.

## 3. Sorting & results

**Sort:** Relevance (default), Price ↑/↓, Newest, Best Sellers, Rating, Discount%. Sort y filters **combinables** (cambiar sort no resetea filtros).
**Results count** siempre ("X resultados").
**Paginación — tradeoffs honestos:** **Load More + lazy-loading = ganador Baymard** (ves más sin perder foco Y conservas el footer). **Infinite scroll** dañino para goal-driven/mobile (no puedes volver a un item, comparar, compartir link; **mata el footer**) → solo discovery puro (Pinterest). **Pagination clásica** percibida como lenta, pero útil cuando "saber dónde estoy"/comparar importa (B2B). Regla: **Load More por defecto.**
**Grid vs list:** grid (3-4/row desktop, 2 mobile) para visual; list para specs. Quick-view (modal sin abandonar el SERP) acelera — sin romper el back-button.

## 4. Navegación / IA

**Mega-menu** dominante (76% de grandes e-commerce; reduce tiempo de nav ~37% vs dropdowns en sites de 50+ páginas) — multi-columna por departamento, con imágenes/CTAs, **pero curado** (no volcado de 200 links).
**Breadcrumbs** en catálogos grandes (`Inicio > Suplementos > Hongos > Melena de León`) + `BreadcrumbList` schema.
**Sticky nav** (search + nav que se mantiene/reaparece al scroll-up).
**Search-first** (catálogos grandes heterogéneos) vs **browse-first** (curados/visuales) — la mayoría necesita ambos.
**IA principles:** card sorting para validar taxonomía; **breadth > depth** (evita jerarquías de 4+ niveles); nombres en el lenguaje del usuario.

## 5. Mobile-specific

- **Search:** field visible en header; al tap, fullscreen con teclado + recent/popular.
- **Filtering:** bottom sheet/fullscreen drawer, trigger "Filter & Sort" **sticky**, "Show X Results" con conteo en vivo (no instant).
- **Nav:** mega-menu colapsa a **drill-down** (tap top-level → slide a sub-página fullscreen) > accordion para catálogos grandes.
- **Bottom nav/tab-bar** para 3-5 acciones primarias (Home/Categorías/Buscar/Carrito/Cuenta) en la **thumb zone** inferior.

## 6. Freshness 2026 & anti-patterns

**Current:** hybrid search default · conversational "ask" sobre el catálogo · personalización en tiempo real · AI assistants que ejecutan acciones · shift de **"browse" a "ask"**.
**Dated:** mega-menu gigante abarrotado (200 links sin curar) · carousel hero como navegación · paginación numerada larga · instant filtering en mobile.

### Search/Nav anti-patterns — blacklist
search escondido tras icono (catálogo grande) · zero-results con solo "tips"/dead-end · no tolerar typos/sinónimos · radio buttons donde se necesita multi-select · filtros aplicados invisibles (sin chips/"Clear all") · instant filtering en mobile · botón "Filter & Sort" que desaparece al scroll · infinite scroll en search results o con footer importante · filtros que NO persisten en URL · mega-menu sin jerarquía/curaduría; nav de 4+ niveles · quick-view que rompe el back-button · autocomplete >10 sugerencias o sin distinguir scope · cambiar sort que resetea filtros.

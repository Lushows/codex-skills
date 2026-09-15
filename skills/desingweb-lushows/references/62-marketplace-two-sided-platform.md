# 62 — Marketplace & plataformas de dos lados

Un marketplace no vende inventario propio: **conecta supply y demand** y monetiza el *matching* + la *transaction*. Quien diseña un marketplace diseña **dos productos a la vez**, con métricas distintas para cada lado. **Léelo para marketplaces, plataformas C2C/gig, two-sided** (Airbnb/Uber/Etsy/Fiverr; relevante para el comercio WhatsApp LatAm). Pareja de 11 (e-commerce), 31 (confianza), 33 (pagos). Regla de oro: **la North Star no es volumen, es liquidity — y diseña ambos lados, no solo el buyer.**

## 1. Fundamentos & el reto de los dos lados

Tres piezas siempre presentes: **discovery/matching**, la **transaction** (acuerdo, pago, fulfillment) y la **trust layer** que hace posible transar entre extraños.
**Chicken-and-egg / cold-start (existencial):** los buyers no llegan sin supply, el supply no se queda sin demand. Regla casi universal: **supply-first** (más fácil reclutar sellers — tienen incentivo económico directo; los buyers llegan cuando hay algo que ver).
**Liquidity (la North Star, no el volumen):** la probabilidad de que un seller venda y un buyer encuentre. Se mide con **fill rate, time-to-match, search-to-fill, repeat rate**. Para ride-share el umbral de network effect ronda **~500 pair completions en una sola celda geográfica**. Por eso empieza **niching down**: una ciudad, una vertical, un caso de uso — domina la liquidez ahí antes de expandir.
**Network effects:** **cross-side** (el valor viene del otro lado) es lo normal; cuidado con los **negative same-side** (demasiados sellers compitiendo por los mismos buyers degrada al supply).
**Unit economics:** **GMV** × **take rate** (10-30%; gig/servicios alto, productos bajo) = revenue. El take rate debe ser **visible y justificable** o alimenta la fuga.
**Tipos:** B2C / C2C / B2B; **vertical** (nicho profundo) vs **horizontal**; **product** vs **service/gig** (los de servicio cargan más peso en trust e identidad — no hay producto físico que inspeccionar).

## 2. La UX de los dos lados (asimetría real)

**Demand side:** search/browse/discover, listing detail, booking/checkout (reutiliza casi todo el playbook de e-commerce). La especificidad: el buyer evalúa **al seller tanto como al producto**.
**Supply side (el verdadero diferencial, donde casi todos fallan):**
1. **Onboarding del seller:** la fricción mata. **Progressive onboarding** — registrar con solo email y dejar explorar; pedir datos sensibles (ID/banco/tax) **solo en acciones high-intent** (publicar, cobrar). Simplificarlo sube signups ~20%; pedir datos sensibles muy pronto baja interés ~15%.
2. **Listing creation:** el momento más frágil. **Templates por categoría**, flujo guiado paso a paso (no un formulario gigante), **preview mode**, **completion progress indicator** (los sellers que ven su progreso completan 30-40% más).
3. **Seller dashboard:** listings, orders y messages con **status labels claros**, acciones core a un toque, performance visible (vistas, conversión, ranking).
4. **Fulfillment:** payouts, calendario/availability, mensajería.
**La asimetría clave:** los lados tienen **sofisticación y dispositivos distintos**. Buyer casual/móvil; seller puede ser power-user o (C2C/LatAm) microemprendedor con baja alfabetización operando 100% desde el teléfono. **>55% del tráfico marketplace es móvil** → el seller dashboard debe ser **mobile-first**, no un panel de escritorio adaptado. Diseña dos UX distintas.

## 3. Trust & safety (la capa crítica)

Es lo que diferencia un marketplace de un catálogo: **transar entre extraños**. La investigación es clara: **los reputation systems rara vez bastan solos** — hace falta una pila.
- **Reviews bidireccionales:** ambos lados se califican. Patrón estándar contra extorsión/represalia: **double-blind review** (ninguna parte ve la recibida hasta enviar la suya — Airbnb, Uber). Mejoras: reseñas con **foto y texto** (no solo estrellas), **subcategorías granulares** (limpieza, check-in, exactitud).
- **Verificación de identidad:** ID scan, background checks, autenticación multi-etapa para alto valor. **Badges** de milestones de confianza.
- **Trust signals en el perfil:** foto real, antigüedad, % y tiempo de respuesta, "Superhost"/"Top Rated".
- **Safety nets/garantías:** AirCover, **escrow/protected payment**, money-back, seguro. Cambian la pregunta del buyer de "¿confío en este extraño?" a "¿confío en la plataforma?".
- **Dispute resolution:** flujo claro de reporte, evidencia (chat on-platform como prueba), mediación, reembolso. Su ausencia es letal.
- **Cold-start trust del seller nuevo** (lo más sutil — sin reseñas no vende, sin vender no consigue reseñas): vetting manual antes de ir live, social proof prestado (partnerships), **boost algorítmico temporal** a listings nuevos, reseñas seed del onboarding.

## 4. Matching, search & discovery

El search de marketplace **no optimiza relevancia, optimiza booking probability** — muestra primero lo que más probablemente complete la transacción (Airbnb). Señales: rating + nº reseñas + sentimiento reciente, **calendario limpio** (availability abierta sube ranking), **Instant Book** (rankea más alto porque convierte más), velocidad de respuesta, precio competitivo.
**Local:** el **mapa** es interfaz primaria (geo + dates + party size). **Curado vs algorítmico:** los curados ganan confianza temprana; los algorítmicos escalan.
**Fairness del ranking (tensión real):** optimizar solo por conversión concentra la demanda en pocos top sellers y asfixia a los nuevos (mal para liquidez de supply). Diseña **exposure fairness**: rota impresiones, da visibilidad a listings nuevos, evita el winner-take-all.
**Booking/request flow:** **Instant Book** (sin fricción, convierte más) vs **request/accept** (el seller aprueba; añade fricción y riesgo de rechazo). Diseña con SLAs visibles, recordatorios, auto-decline. **Availability siempre actualizada** — calendario desincronizado es la peor experiencia.

## 5. Transacciones, pagos & el modelo

**La tx marketplace** difiere del checkout normal por el **hold/escrow**: la plataforma captura el pago pero **no lo libera hasta que el servicio/entrega se completa** (protege al buyer, desincentiva la fuga). Ojo: el escrow está **fuertemente regulado por país** — usa un PSP marketplace (Stripe Connect, Mercado Pago split) para no ser custodio legal. **Display del fee:** al seller, enmárcalo contra los beneficios; al buyer, fees sorpresa en checkout disparan abandono. **Payouts:** idealmente instantáneos o 1-2 días — la velocidad es retención de supply Y arma anti-fuga (reduce la preferencia por cobrar en efectivo). **Split payment** (reparte seller-payout vs commission en una transacción). **Mensajería entre lados:** las preguntas pre-compra son críticas; mantenerlas **on-platform** sirve de prueba en disputas y reduce fuga (pero es justo el punto donde la gente intercambia contactos para irse).
**Ángulo LatAm/WhatsApp:** en LatAm el marketplace muchas veces **vive dentro de WhatsApp** — catálogo + negociación personal + COD. WhatsApp impulsa ~$18B en e-commerce LatAm; adopción WhatsApp Business: Brasil ~78% de negocios vendiendo, Colombia ~74%. El "checkout" es una conversación; la trust layer es el vendedor humano. Diseña para este canal: catálogo interactivo, agente conversacional que guía discovery→carrito→cierre sin salir del chat.

## 6. Growth, liquidity & 2026

**Resolver cold-start:** (a) **seed un lado manualmente** (concierge/Wizard-of-Oz: el equipo hace el matching a mano al inicio), (b) **niching down** brutal, (c) **single-player mode** (dar valor a un lado aunque el otro no exista aún), (d) **borrow supply** (Airbnb sembró con scraping de Craigslist). Mide liquidez por celda, no agregada.
**Disintermediation/leakage** (gente que se va off-platform tras conocerse — la amenaza existencial): **carrots** (payouts rápidos, seguro/garantía, dispute resolution, workflow embebido — hacer que quedarse valga más que irse) > **sticks** (ocultar/banear contactos — genera resentimiento y no ataca la raíz). Caso real: leakage de 14%→5% tras lanzar warranty + payout 2 días.
**AI en marketplaces 2026 (agentic commerce):** agentes que recorren el journey completo (discovery→comparación→carrito→checkout). Se imponen **agentes pequeños purpose-built embebidos en el workflow**, no un mega-agente. En LatAm, agentes WhatsApp gestionan ventas 24/7 (proyección: ~65% de transacciones WhatsApp LatAm asistidas por IA en 2027). Diseño: el marketplace debe ser legible por agentes (datos estructurados, APIs de checkout) Y conversacional para humanos.

## Marketplace anti-patterns — blacklist
**diseñar para un solo lado** (pulir la app del buyer y dejar al seller con un formulario hostil) · **chicken-and-egg sin resolver** (lanzar las dos caras vacías esperando que se llenen solas) · **perseguir volumen/GMV en vez de liquidity** (crecer ancho, líquido en ninguna parte) · **sin trust system** (cero verificación, reviews unilaterales/falsificables, sin garantía) · reviews que invitan a represalia (no double-blind) · ignorar el **cold-start del seller nuevo** (winner-take-all que nunca da impresiones a listings sin reseñas) · **sin dispute resolution ni safety net** · fee/take rate oculto o sorpresa en checkout · **payouts lentos** (empujan a cobrar en efectivo y a la fuga) · **no combatir la disintermediation** (el valor se construye on-platform y la tx se va off = cero revenue) · solo sticks contra la fuga · onboarding pesado upfront (ID/banco antes de explorar) · **seller dashboard de escritorio en un mundo móvil** · availability/calendario desincronizado.

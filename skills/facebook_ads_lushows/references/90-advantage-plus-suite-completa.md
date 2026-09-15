# 90 — Advantage+ Suite completa: qué ceder y qué controlar

Advantage+ dejó de ser un "modo opcional" y se volvió **el sistema operativo de Meta Ads en 2026**: tras la unificación de febrero-2026, el flujo manual de creación de campañas desapareció de la interfaz principal y todo arranca dentro del paraguas Advantage+ (audiencias, ubicaciones, presupuesto, creativo, shopping y catálogo). La IA viene activada por defecto **por sección** y tú haces *opt-out* donde tengas criterio para hacerlo — ya no es "activar IA", es "desactivar la IA que no me sirve". Lee este módulo cuando configures cualquier campaña, cuando Ads Manager te bombardee con "recomendaciones", o cuando alguien te diga que "el manual ya no existe" y entres en pánico (no lo necesitas). La filosofía que ordena todo sigue intacta: **Meta automatiza el CÓMO (la entrega: a quién, dónde, cuándo), tú controlas el QUÉ (oferta, creativo, mensaje, medición y presupuesto total)**. Pelear contra la entrega es perder; abandonar el QUÉ es regalar tu negocio al algoritmo. Detalle de los cambios estructurales 2026 en `actualizacion-2026-06`.

## El mapa: feature → qué hace → veredicto (jun-2026)

| Feature | Qué hace | Veredicto | Módulo |
|---|---|---|---|
| **Advantage+ audience** | Tu targeting pasa a ser "sugerencia" (audience suggestion); el sistema explora más allá | **Cédelo casi siempre** — broad gana en 2026; deja solo restricciones duras (geo, edad legal) | ver 20 |
| **Advantage+ placements** | Meta reparte entre feed, Reels, Stories, Threads, Audience Network, etc. | **Cédelo por default** — compra el inventario barato que convierte | ver 02 |
| **Advantage+ budget (CBO)** | El presupuesto fluye entre ad sets según rendimiento | **Depende**: cédelo para escalar consolidado; contrólalo (ABO) para tests donde cada variante necesita gasto garantizado | ver 10, 17 |
| **Advantage+ creative** | Mejoras automáticas al anuncio: brillo, música, variaciones, image-to-video, fondos generados | **Depende — revisar UNA por una** (tabla abajo) | este módulo |
| **Advantage+ Sales** (ex-ASC) | Campaña de ventas hiper-automatizada; ASC se renombró aquí en feb-2026 | Cédelo si tienes señal y volumen creativo; **cap de clientes existentes 25-30%** (configurable, ver abajo) | ver 12 |
| **Advantage+ catalog / shopping** | Catálogo dinámico con personalización por usuario | Cédelo para retargeting de catálogo; cura las fotos | ver 56 |
| **Advantage+ Creative Suite** | Generación: image-to-video, variaciones, generación de fondo, expansión | Multiplicador de assets — curar siempre (ver 91) | ver 91 |

> Jerga: lo que algunos gurús llaman "Lattice" (supuesto sucesor de Andromeda) **no es terminología oficial de Meta** — ignóralo como criterio de decisión; opera sobre features que existen en tu Ads Manager, no sobre rumores de YouTube.

## Advantage+ Sales (ex-ASC): el cambio de nombre que confunde

En febrero-2026, **Advantage+ Shopping Campaigns (ASC) se renombró a Advantage+ Sales**. Es el mismo motor: una campaña de ventas casi sin palancas manuales donde subes creativos, defines país y presupuesto, y el sistema hace el resto. Lo que SÍ controlas y debes ajustar:

- **Cap de clientes existentes (existing customer budget cap)**: por defecto Meta puede gastar parte del presupuesto en gente que YA te compró. Sube tu lista de clientes y fija el cap en **25-30%** si quieres priorizar adquisición; bájalo a 0-10% en campañas puramente de captación. Es el único dial que evita que pagues prospección para reimpactar a quien ya tienes (ver 23/64).
- Funciona cuando tienes **señal limpia (CAPI/EMQ, ver 06)** y **volumen creativo diverso (ver 92)**. Sin esas dos, Advantage+ Sales no tiene de qué agarrarse y se desempeña peor que una broad manual bien armada.

## Advantage+ creative: el único que se revisa pieza por pieza

Las "mejoras automáticas" (enhancements) editan TU anuncio sin pedirte permiso por cada impresión. Algunas suben CTR gratis; otras rompen marca o mensaje. En 2026 vienen **ON por defecto** — el trabajo es desactivar, no activar. Revisa el toggle de cada una al crear el ad (sección "Mejoras del Advantage+ creative" → editar):

| Mejora | Qué hace | E-commerce | Servicios/marca cuidada | WhatsApp-first pyme |
|---|---|---|---|---|
| Ajustes de brillo/contraste | Retoca la imagen | ✅ on | ✅ on | ✅ on |
| Plantillas de imagen (overlays, marcos) | Mete texto/precio encima | ⚠️ probar | ❌ off (rompe estética) | ⚠️ probar |
| Música automática | Agrega audio a estáticas/video | ⚠️ probar | ❌ off | ⚠️ probar |
| Variaciones de texto (reordena/genera copy) | Muestra versiones distintas de tu texto | ⚠️ on con revisión — puede cambiar claims (riesgo policy, ver 44) | ❌ off | ⚠️ on con revisión |
| Expansión de imagen (IA rellena para 9:16) | Genera fondo para otros ratios | ✅ on si el fondo es simple | ⚠️ revisar resultado | ✅ on |
| **Image-to-video (Creative Suite)** | Anima la estática en un video corto | ⚠️ probar — a veces salva una estática plana | ❌ off salvo aprobación visual | ⚠️ probar |
| **Generación de fondo** | Reemplaza el fondo del producto con IA | ⚠️ probar con foto de producto limpia | ⚠️ revisar (puede inventar) | ⚠️ probar |
| Catálogo: info de envío/precio dinámico | Overlays de catálogo | ✅ on | n/a | ✅ on |

Regla práctica: si tu negocio vive de estética de marca (moda premium, diseño), apaga todo lo que altere lo visual — la dirección de arte la pone directorcreativo_lushows, no un overlay automático. Si vives de volumen y respuesta directa, deja ON y revisa la vista previa de **cada placement** antes de publicar (lo que se ve bien en feed sale deforme en Reels). Si una mejora puede alterar un claim de salud/finanzas, OFF siempre (ver 08/44).

## Opportunity Score y recomendaciones: criterio propio SIEMPRE

El Opportunity Score (0-100 en Ads Manager) puntúa cuánto sigues las recomendaciones de Meta. Entiende el conflicto de interés: **muchas recomendaciones optimizan para que gastes más y la subasta fluya, no para tu margen**. Cómo filtrar:

- **Aplica sin miedo**: arreglar eventos rotos/CAPI, fusionar ad sets fragmentados, agregar formatos faltantes (9:16), salir de learning limited consolidando, **completar verificación de negocio** (ver 93). Coinciden con tu interés.
- **Evalúa con datos**: activar enhancements específicos, ampliar audiencia, cambiar atribución, activar image-to-video. Pruébalo como test (ver 17), no porque el score baje.
- **Ignora por default**: "sube el presupuesto X%" sin contexto de tu CPA/margen (ver 64), "expande a más países" si no despachas allá, aplicar recomendaciones en bulk con un clic.
- Un score de 70-85 con campañas rentables vale más que 100 con margen muerto. El score no paga tu nómina.

## Decisión rápida por escenario

1. **Pyme arrancando (CTWA, < $3M COP/mes)**: Advantage+ audience ON con geo correcto, placements ON, ABO simple (1-2 ad sets), enhancements ON salvo variaciones de texto sin revisar. Tu trabajo: oferta + 4-6 creativos (ver 98).
2. **E-commerce con señal**: Advantage+ Sales (ex-ASC) con cap de clientes existentes en 25-30%, o broad consolidada con CBO; catalog ads para retargeting; enhancements curados. Tu trabajo: volumen creativo (ver 39) y MER real (ver 64).
3. **Cuenta con test activo**: ABO para el test, **cero enhancements** en las variantes (contaminan la lectura: no sabes si ganó tu creativo o la edición de Meta).

## Auditoría rápida: qué Advantage+ tienes activo hoy

Cinco minutos por cuenta, una vez al mes:

1. Abre cada campaña activa → ad set → sección audiencia: ¿Advantage+ audience ON? Anota qué restricciones duras dejaste (geo, edad mínima).
2. Placements: ¿manual o Advantage+? Si alguien los restringió "porque Audience Network es malo", pide el dato que lo respalde (casi nunca existe; el costo por resultado total es lo que importa, ver 02).
3. Abre 3 ads al azar → mejoras del creativo: ¿qué enhancements están ON por defecto? ¿Coinciden con la tabla de arriba para tu tipo de negocio? Desactiva los que rompan marca/claim.
4. Campaña: ¿CBO o ABO? ¿Advantage+ Sales o tráfico/conversión manual? ¿Coincide con su propósito (escalar vs testear)?
5. Si usas Advantage+ Sales: ¿está el cap de clientes existentes configurado, o estás pagando prospección para reimpactar a clientes?
6. Revisa el Opportunity Score y sus recomendaciones pendientes con el filtro de la sección anterior — aplica las de medición/consolidación, documenta las que ignoras y por qué (te lo volverán a sugerir).

## Errores comunes — blacklist

- Aceptar todas las mejoras automáticas sin abrir la vista previa: tu ad puede salir con música genérica, marcos feos en Reels o un image-to-video que distorsiona el producto.
- Apagar TODO Advantage+ "para tener control": peleas contra la subasta con las manos atadas; el control que importa es oferta/creativo/medición.
- Buscar el toggle "manual" de toda la vida y bloquearte porque ya no está: el manual real hoy es Advantage+ con opt-outs precisos (ver `actualizacion-2026-06`).
- Correr Advantage+ Sales sin configurar el cap de clientes existentes: pagas adquisición para reimpactar a quien ya te compró.
- Perseguir Opportunity Score 100 como si fuera un KPI de negocio.
- Dejar variaciones de texto ON en categorías reguladas: Meta puede generar un claim que te come un rechazo o algo peor (ver 93).
- Testear creativos con enhancements activos y sacar conclusiones sobre "el creativo".
- Aplicar recomendaciones en bloque un viernes y no poder aislar qué cambió cuando el lunes el CPA explotó (ver 70).
- Tomar decisiones según "Lattice" u otra jerga no oficial en vez de las features reales de tu cuenta.

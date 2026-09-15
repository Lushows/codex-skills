# 37 — Signal-based selling

El "signal-based selling" (venta basada en señales) es el enfoque moderno del outbound: en vez de contactar a una lista estática "porque encajan en el ICP", contactas **cuando ocurre un evento que crea una necesidad o una ventana de compra**. Alguien cambió de cargo, la empresa levantó una ronda, está contratando 5 vendedores, abrió una sede, adoptó una tecnología. Cada uno de esos eventos es una **señal** de que ese contacto está más receptivo **ahora** que ayer. Es la evolución del spray-and-pray hacia la relevancia por timing, y es lo que separa el outbound de 2026 del de 2018. Diferencia con intent data: el intent (`36`) es "está investigando"; la señal es "le pasó algo". Ambos son timing.

## El principio: un evento crea una ventana, y las ventanas se cierran

La mayoría de tu mercado no compra en un momento dado. Pero cuando ocurre un **evento disparador (trigger)**, se abre una ventana breve de alta receptividad. Ejemplos de la lógica:

- **Cambió de cargo (job change):** un ejecutivo nuevo en su rol reevalúa proveedores, quiere marcar cambios rápido y trae presupuesto para hacerlo. Es la señal reina en B2B.
- **Levantó ronda (funding):** hay dinero fresco y presión por crecer; compran herramientas.
- **Está contratando (hiring):** si buscan 5 SDRs, van a necesitar lo que le sirve a un equipo de SDRs. La vacante te dice su plan.
- **Abrió sede / expandió:** nueva operación = nuevas necesidades.
- **Adoptó/cambió tecnología (technographic):** si acaban de poner Shopify, todo lo que se integra con Shopify es relevante (ver `134`).

La clave es la **velocidad**: la señal caduca. Contactar 3 días después de que alguien asumió un cargo pega distinto que 3 meses después. Por eso el signal-based selling va casado con la automatización (ver `34`, `147`).

## Las señales que más convierten

| Señal | Dónde detectarla | Por qué convierte | Ángulo de mensaje |
|---|---|---|---|
| **Cambio de cargo** | LinkedIn, Sales Nav, UserGems, Clay | Rol nuevo = mandato de cambio + presupuesto | "Felicitaciones por el nuevo rol; los primeros 90 días…" |
| **Funding / ronda** | Crunchbase, noticias, Clay | Dinero fresco, presión de crecer | "Vi la ronda; suele venir con el reto de escalar {X}" |
| **Hiring / vacantes** | LinkedIn Jobs, portales, scraping | La vacante revela su prioridad actual | "Vi que buscan {rol}; normalmente eso significa {necesidad}" |
| **Expansión / nueva sede** | Noticias, LinkedIn, prensa local | Operación nueva = necesidades nuevas | "Felicitaciones por la sede en {ciudad}…" |
| **Cambio tecnológico** | BuiltWith, technographics | Encaja/desencaja con tu producto | "Vi que adoptaron {tech}; lo complementamos con…" |
| **Cliente tuyo cambia de empresa** | UserGems, job tracking | Un fan tuyo llega a una cuenta nueva | "Trabajamos juntos en {empresa anterior}…" (¡oro!) |

Detalle: cambio de cargo → `133`; funding/hiring/expansión → `135`; technographics → `134`; combinar fit+señal en score → `137`.

## El cómo, paso a paso: montar una máquina por señales

1. **Elige 1–2 señales** relevantes para lo que vendes. No persigas las seis. Si vendes a equipos comerciales, "está contratando vendedores" es tu señal.
2. **Monta la detección.** Fuentes: LinkedIn/Sales Navigator (alertas), Clay (columnas que buscan job posts/funding), herramientas dedicadas (UserGems para job change). Ver `31`, `133`, `135`.
3. **Filtra por fit.** La señal sin encaje es ruido; cruza con tu ICP (ver `10`, `137`).
4. **Enriquece y verifica** el contacto disparado por la señal (ver `29`, `28`).
5. **Dispara la cadencia específica de esa señal** vía automatización (ver `34`, `128`). El mensaje **nombra la señal** como razón del contacto — ese es el punto.
6. **Actúa rápido.** La ventana se cierra; automatiza para contactar en días, no semanas.

## Ejemplo: cadencia disparada por "cambio de cargo"

```
Señal: {nombre} pasó de Gerente Comercial en Empresa A
        a Director Comercial en Empresa B (hace 6 días)
Fit:   Empresa B es de tu ICP → sí

Email 1 (día 0):
  Asunto: Nuevo rol en {Empresa B}
  "Hola {nombre}, felicitaciones por asumir como Director Comercial
   en {Empresa B}. En los primeros meses de un rol así casi siempre
   aparece la pregunta de cómo llenar el pipeline sin depender de
   referidos. Ayudamos a equipos comerciales a {resultado concreto}.
   ¿Tiene sentido una charla de 12 minutos esta semana?"

LinkedIn (día 2): conexión + nota breve mencionando el nuevo rol
Email 2 (día 5):  bump con un caso de otro director en su situación
```
La señal (el cargo nuevo) **es** el opener. No hay que fingir personalización: el evento real la genera. La conversación que sigue —descubrir su dolor, manejar objeciones, cerrar— es `ventas_lushows` (ver `64`, `71`).

## Errores comunes

- **Perseguir todas las señales a la vez.** Elige 1–2 y hazlas bien.
- **Señal sin fit.** Que contraten no importa si no son tu ICP.
- **Lentitud.** Detectar la señal y contactar 6 semanas después mata la ventaja. Automatiza (ver `147`).
- **Delatar el "stalking".** Menciona la señal **pública** (cargo, ronda, vacante) con naturalidad; no des a entender que los vigilas obsesivamente.
- **Mensaje genérico pegado a una señal.** Si nombras el cargo nuevo pero el resto es plantilla fría, se nota. El cuerpo debe conectar la señal con el valor (ver `128`).

## Siguiente paso

Elige tu señal #1 (la más ligada a lo que vendes) y monta su detección en Clay o Sales Navigator esta semana. Escribe la cadencia específica que la nombra (`128`). Cruza señal + fit en `137`. Para el intent "está investigando" (otra familia de timing) → `36`. Para automatizar la detección → contacto → `34`, `147`. La conversación tras la respuesta → `ventas_lushows`.

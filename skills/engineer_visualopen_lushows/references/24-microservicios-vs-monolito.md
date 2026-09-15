# 24 — Microservicios vs monolito

**Default: un monolito.** Un solo desplegable con módulos internos limpios le gana a microservicios para
cualquier equipo bajo ~20 ingenieros. Obtienes calls in-process (sin red), una txn de DB, refactor trivial, un
deploy, un lugar para debuggear. Casi todo el dolor "microservicios" es auto-infligido.

**Modular monolith = el sweet spot:** un proceso, pero límites de módulo forzados (paquetes separados, sin acceso
cruzado a la DB, comunican vía interfaces/eventos internos). Separación de concerns *sin* el impuesto distribuido,
y seams limpios para extraer un servicio después si un módulo genuinamente necesita escalar independiente.

**Cuándo partir:** (1) un componente con *perfil de escala distinto* (ej. worker GPU vs API web); (2) *otro equipo*
lo posee y el acoplamiento de deploy duele; (3) *runtime/lenguaje distinto*; (4) fault-isolation genuino. Partir
"porque microservicios" es el anti-patrón.

**Límites = bounded contexts (DDD).** Traza líneas donde cambia el *lenguaje* (un "Product" en Catálogo ≠ en
Billing). Un límite debe poseer su data — **sin DB compartida entre servicios** (eso es un monolito distribuido con latencia extra).

**Comunicación:** **sync** (REST/gRPC) simple pero acopla disponibilidad — si B cae, A falla, y la latencia se
compone. **async** (eventos/colas) desacopla y absorbe spikes pero trae eventual consistency. Regla: comandos que
necesitan respuesta inmediata → sync; notificaciones/side-effects → eventos async.

**Costos del sistema distribuido** (la cuenta por partir): fallos de red + retries + timeouts, sin txns
cross-service (→ sagas), tracing/observabilidad distribuida (OpenTelemetry se vuelve obligatorio), coordinación de
schema/versión, dev local más difícil, más infra.

**Anti-patrón "monolito distribuido":** servicios que deben desplegarse juntos, comparten DB, y se llaman en
cadenas síncronas. Todos los costos de microservicios y ninguno de los beneficios. Síntoma: cambiar uno fuerza
releases en lockstep; una migración de DB rompe tres servicios.

**Recomendación pragmática 2026 para equipo chico (un producto IA en Render):** arranca como **modular monolith**
(un servicio Python/Node) + **extrae el trabajo long-running/GPU/async a workers separados detrás de una cola.** Eso
es todo. Añade un servicio solo cuando una razón concreta de escala/ownership/runtime lo fuerce. Invierte temprano
en tracing OpenTelemetry y un pipeline CI sin importar la arquitectura.

## Gotchas
1. DB compartida entre "servicios" = no tienes microservicios.
2. Partir prematuro congela límites que aún no entiendes — son caros de mover ya distribuidos.
3. Cadenas síncronas A→B→C→D multiplican probabilidad de fallo y cola de latencia.
4. Sin tracing distribuido, un bug multi-servicio es casi indebuggeable.

**Fuentes:** martinfowler.com/bliki/MonolithFirst · martinfowler.com/bliki/MicroservicePremium · shopify.engineering (modular monolith) · martinfowler.com/bliki/BoundedContext.

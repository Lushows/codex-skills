# 110 — El estado del arte de la IA: meta-resumen (junio 2026)

> Snapshot fechado. Síntesis de los mayores cambios de 2026.

## Los mayores cambios
1. **Agentes mainstream (con asterisco).** De demo a producción, pero Gartner predice **>40% de proyectos agentic cancelados para fin de 2027** (choque con confiabilidad y costo).
2. **Razonamiento como norma.** Salto enorme: Claude Opus 4.5 → **80.9% SWE-Bench Verified** (vs 33% hace 18 meses); Opus 4.6 → **91.3% GPQA Diamond** (expertos humanos: 69.7%).
3. **El colapso de costos (real, con paradoja).** Precio/M tokens cayó ~92% en 3 años ($30 → $0.10-2.50). DeepSeek "mismo score que Claude pero 28× más barato" `[no verificado equivalencia real]`. **PERO las facturas enterprise SUBEN:** presupuesto medio de $1.2M/año (2024) a **$7M (2026)** — los agentes consumen órdenes de magnitud más tokens. Microsoft reportó que usar la tech puede salir más caro que pagar humanos en ciertos flujos.
4. **Multimodal en todo** + la ola **physical AI / world models** (refs 106-107).
5. **Gap open vs closed se cierra:** labs chinos (DeepSeek, Qwen, ByteDance) muy cerca en razonamiento/código; gpt-oss y Gemma abiertos competitivos para self-hosting.

## Regulación
- **EU AI Act Omnibus (acuerdo político 7 may 2026)** difirió el deadline de alto riesgo: Annex III (reclutamiento, scoring crediticio) → **2 dic 2027**; Annex I → 2 ago 2028. Prácticas prohibidas ya en enforcement desde feb 2025; multas hasta **€35M o 7% de facturación global**. **2 ago 2026** = hito GPAI/transparencia `[verificar post-Omnibus, hay versiones encontradas]`.

## Hype vs real
**Real:** razonamiento/código, caída de costo por token, multimodal, world models para robótica. **Hype:** "AGI inminente", agentes autónomos plug-and-play sin supervisión, world models que "entienden física" (debate LeCun abierto).

## Qué significa para un equipo IA-first pequeño en LatAm
- **Rentar > comprar** GPU (importación cara); cloud por hora + spot.
- **Híbrido:** Claude/frontera para conversación de ventas matizada (Addrian/BIO-SETA), modelo local barato (Qwen3.6/Gemma 4) para clasificación/extracción/triaje offline → recorta factura.
- **Vigila el costo de agentes:** el peligro no es precio/token sino *volumen* de tokens; instrumenta gasto desde día 1.
- **Cumplimiento:** si operas en UE, transparencia GPAI aplica; en LatAm aún sin marco fuerte, pero el AI Act es estándar de facto exportado.
- **Aprovecha el colapso:** lo caro de hace un año hoy es trivial; no sobre-optimices prematuramente.

## Gotchas
1. Benchmarks (SWE-Bench, GPQA) están parcialmente contaminados/saturados; úsalos como tendencia, no verdad.
2. "28× más barato que Claude" mezcla modelos/condiciones distintas `[no verificado]`.
3. El deadline EU AI Act se movió en 2026 (Omnibus); no cites fechas viejas.
4. Cost collapse ≠ factura baja: los agentes multiplican tokens.
5. Labs chinos competitivos pero con restricciones de despliegue/datos según jurisdicción.

**Fuentes:** fortune.com (Microsoft AI cost, may 2026) · oplexa.com (inference cost crisis 2026) · artificialintelligenceact.eu · legalnodes.com (EU AI Act 2026).

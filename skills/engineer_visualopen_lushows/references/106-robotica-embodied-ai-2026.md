# 106 — Robótica & embodied AI (2026)

> Snapshot fechado. 2026 = el año en que la robótica "tuvo su momento ChatGPT" con los **VLA (Vision-Language-Action)** como arquitectura dominante. Un VLA toma cámaras + instrucción en lenguaje y emite acciones motoras directamente, heredando el sentido común de un VLM.

## Modelos VLA líderes
- **Physical Intelligence π0 / π0.5** — π0 usa *flow-matching* para acciones continuas; π0.5 generaliza "open-world" (limpiar una cocina nunca vista). La referencia de la ola.
- **Google DeepMind Gemini Robotics** — VLA sobre Gemini (razonamiento + acción).
- **NVIDIA GR00T N1** — foundation model para humanoides con *latent action pre-training* desde video sin etiquetar. **Cosmos Policy** (NVIDIA añadió capa de política a sus world models).
- **Abiertos:** OpenVLA, V-JEPA 2 (Meta, pre-train con video de internet), RT-2 (precursor Google).

**Tendencias:** (1) **Cross-embodiment** (un modelo en brazos/bimanuales/cuadrúpedos/humanoides supera a uno dedicado). (2) Pre-train con video YouTube/egocéntrico. (3) **Action chunking** (emite 8-50 acciones futuras → 30-100 Hz pese a latencia). (4) Teleoperación + imitation learning = la fábrica de datos.

## Humanoides — qué se envió en 2026
- **Figure 03** con VLA propietario **Helix**; fábrica **BotQ** (~12,000 u/año); completó piloto 11 meses en BMW Spartanburg.
- **Tesla Optimus Gen 3** — producción en masa iniciada ene 2026 (Fremont); venta pública ~2027.
- **1X Neo** — entregas a early adopters a **$20,000**; >10,000 pre-órdenes; respaldado por OpenAI.
- **Unitree** — líder en volumen (~5,500 en 2025, meta 10-20K en 2026); el más barato.

**Quién lidera:** Figure (occidente, industrial) + Physical Intelligence (cerebro/VLA) + NVIDIA (sim/foundation) vs Unitree (volumen/precio China).

## Gotchas
1. El cuello de botella ya no es hardware sino **datos de manipulación reales**; teleoperación es cara/lenta.
2. **Sim-to-real gap:** políticas de simulación fallan en física de contacto fina (deformables, fricción).
3. Cifras de "producción" ≠ unidades realmente operando autónomas; muchos pilotos siguen parcialmente teleoperados `[no verificado el grado]`.
4. VLA a 30-100 Hz: la latencia de inferencia mata el control → action chunking + cuantización on-board.
5. 1X Neo en casa implica cámaras + a veces teleop remota → riesgo de privacidad real.
6. Seguridad funcional (humanoide de 60kg junto a personas) aún sin marco regulatorio maduro.

**Fuentes:** indexbox.io (VLA 2026) · therobotreport.com (Cosmos Policy) · robozaps.com · vaasblock.com · lumichats.com (humanoides 2026).

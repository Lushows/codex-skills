# 107 — World models & simulación (2026)

> Snapshot fechado. World models = modelos que aprenden la dinámica del mundo (física, persistencia, causalidad), no solo pixeles. La apuesta de "miles de millones" de los nombres más grandes (Fortune, may 2026).

## Los tres frontrunners
- **Google DeepMind Genie 3** — primer world model interactivo en tiempo real, entornos 3D persistentes a **24 fps**. Vía Project Genie (suscriptores **Ultra $200**); usado por **Waymo** para entrenar robotaxis en escenarios raros con Street View grounding.
- **World Labs (Fei-Fei Li)** — producto comercial **Marble** (nov 2025): texto/foto/video/panorama/3D-layout → entornos 3D **persistentes y descargables**. Free (4 gen), Standard $20, Pro $35 (comercial), Max $95. Valuación ~$5B.
- **AMI Labs (Yann LeCun)** — LeCun dejó Meta; busca ~€500M a €3B, apostando contra LLMs a favor de **JEPA** (predicción en espacio latente, no reconstrucción de pixeles).

## Para robótica/AV — NVIDIA Cosmos 3 (COMPUTEX 2026)
World foundation model abierto, **20 billones de tokens** multimodales. Versiones "super" (física precisa para
entrenar robots/AV) y "nano" (fracciones de segundo). Adoptan: 1X, Agility, Figure, Skild, Waabi, XPENG, Uber.
**Startups:** Decart, Odyssey (**Starchild-1**, 18 may 2026 — world model multimodal real-time, "causal": genera frames solo del pasado → interactividad abierta real).

## El debate "Sora como world model"
OpenAI describió Sora como "simulador del mundo". LeCun: *"generar videos realistas no indica que entienda la física."*
OpenAI **cerró Sora web/iOS el 26 abr 2026** (costo de cómputo), API discontinúa **24 sep 2026**, pivota a enterprise.

## Gotchas
1. Dos filosofías irreconciliables: **generativo (reconstruir pixeles)** vs **JEPA/latente (predecir abstracción)**.
2. Genie 3 persiste pero la coherencia a largo plazo (>minutos) se degrada `[no verificado el límite]`.
3. "World model" está sobrecargado: Marble (3D persistente offline) ≠ Genie (frames on-the-fly) ≠ Cosmos (datos sintéticos para robots) — no los compares directo.
4. Costo de cómputo brutal: el cierre de Sora lo demuestra.
5. Para un equipo pequeño: **Marble ($20-35) es lo único realmente usable hoy** para generar entornos; Genie requiere Ultra $200.
6. Mucho del campo es research/demo, no producto desplegable.

**Fuentes:** fortune.com (physical AI world models, may 2026) · techtimes.com (Genie 3+Waymo) · techcrunch.com (World Labs Marble) · nvidianews.nvidia.com (Cosmos 3) · bonega.ai (LeCun AMI Labs).

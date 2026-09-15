## Legal de IA Generativa (Copyright, Likeness, Deepfakes)

**This is reference material, not legal advice. Cite primary sources and consult counsel before relying on any of this.** The law here is fast-moving and unsettled as of mid-2026.

**Training-data copyright (US).** The core question — is training on copyrighted works fair use? — has **no final appellate answer**. Key data points:
- **Bartz v. Anthropic** (N.D. Cal., June 2025): Judge Alsup held that training LLMs on lawfully-acquired books is *highly transformative* and **fair use** — but that acquiring books from **pirate libraries** was **not** fair use. Anthropic settled the piracy claims (a reported ~$1.5B class settlement).
- **Kadrey v. Meta** (N.D. Cal., 2025): Judge Chhabria also found training transformative / fair use *on the record presented*, while warning plaintiffs could win with better market-harm evidence.
- **Andersen v. Stability AI** (N.D. Cal.): claims by visual artists **survived** motions to dismiss and are proceeding (induced infringement / DMCA theories alive).
- **NYT v. OpenAI** (S.D.N.Y.): survived dismissal in 2025; in discovery OpenAI was ordered to produce ~20M de-identified ChatGPT logs. No fair-use ruling yet.
- **Getty Images v. Stability AI (UK)** (High Court, 4 Nov 2025): Getty *dropped* its primary training-copyright claims (training happened outside the UK); court rejected **secondary** infringement, holding model **weights are not an "infringing copy"** of the images. Limited trademark win only.

Takeaway: **source provenance matters legally** — "lawfully acquired" vs "pirated" is the dividing line courts actually rule on. The **US Copyright Office Part 3 report (May 2025)** concluded AI training is *often but not categorically* fair use, emphasizing the fourth factor (market harm) and that pirated-source training "is unlikely to be fair use."

**Output copyrightability (US).** Per the Copyright Office's **2025 guidance and "Part 2: Copyrightability" report**, purely AI-generated output is **not copyrightable** — human authorship is required. Prompting alone (even elaborate) does not confer authorship. But human *selection, arrangement, or substantial modification* of AI output can be protected for those human contributions. Practical effect: you generally **cannot claim exclusive copyright** in a raw model output; you can in your creative human editing on top.

**Likeness / right of publicity.** Using a real person's face or voice needs consent. Federal: the **NO FAKES Act** (reintroduced 2025) would create a federal digital-replica right with notice-and-takedown — **not yet law**. State law governs now: **Tennessee ELVIS Act (2024)** explicitly protects voice against AI mimicry; California, New York and others have publicity + digital-replica statutes. The **TAKE IT DOWN Act (signed 19 May 2025)** is federal law: it criminalizes publishing non-consensual intimate imagery **including AI deepfakes**, and requires covered platforms to remove on victim request **within 48 hours** (enforced by the FTC). For products: get explicit, documented consent for any avatar/voice-clone of a real person; never enable intimate/sexual deepfakes.

**Deepfake law.** Beyond TAKE IT DOWN (NCII): many states regulate **election** deepfakes; the EU AI Act (Art. 50) mandates deepfake **disclosure** (file 03). Non-consensual intimate deepfakes are now federally criminal in the US.

**Model licenses (commercial use).** Read the weights license, not the marketing:
- **FLUX.1 [dev]** — **Non-Commercial License v2.0** (updated 25 Nov 2025): outputs/use only for non-commercial purposes; **commercial use requires a paid BFL license** (self-serve portal) or use the FLUX API (which *includes* commercial rights). License also **requires content filters / manual review**.
- **FLUX.1 [schnell]** — Apache-2.0 (commercially usable).
- **Llama (Meta)** — community license, free commercially **but** the >700M-MAU clause requires a separate license; check use-restriction policy.
- **Stable Diffusion / SDXL** — CreativeML OpenRAIL-M / Stability community license (revenue thresholds apply for some).

Verify *every* model in a commercial pipeline; "open weights" ≠ "free for commercial use."

**LatAm / Colombia angle.** Colombia protects personal data via **Ley 1581 of 2012 (habeas data)** implementing Art. 15 of the Constitution; **biometric/face data is "sensitive"** and needs explicit consent (SIC **Circular 001 of 2025** requires risk-proportionate handling — a $214M-peso-scale fine was issued for mandatory facial recognition). The constitutional **derecho a la propia imagen** (right to one's image) restricts using someone's likeness without authorization. **Ley 2502 of 2025** amended Art. 296 of the Penal Code to criminalize AI identity impersonation, naming *deepfake* and *digital identity* for the first time (no dedicated non-consensual-sexual-deepfake statute yet). A 2025 bill proposes strengthening SIC and raising fines.

**Gotchas:**
1. **"Training is fair use" is NOT settled** — Bartz/Kadrey are district-court, fact-specific, appealable; do not treat as a green light. Pirated sources lose.
2. **You don't own raw AI output** — can't register copyright on it; competitors can copy a pure generation.
3. **Open weights ≠ commercial-free** — FLUX-dev is the classic trap; you owe BFL a license for commercial use.
4. **Real-person likeness without consent** is a publicity/TAKE-IT-DOWN/ELVIS-Act risk even if the image is "AI-generated."
5. **Colombia biometrics** — face uploads for avatars = sensitive data; explicit consent + risk assessment required, real fines exist.

Sources (primary): [Copyright Office AI portal](https://www.copyright.gov/ai/) · [USCO Part 3: Generative AI Training](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-3-Generative-AI-Training-Report-Pre-Publication-Version.pdf) · [Getty v. Stability AI judgment (UK Judiciary)](https://www.judiciary.uk/wp-content/uploads/2025/11/Getty-Images-v-Stability-AI.pdf) · [TAKE IT DOWN Act (Wikipedia overview + text links)](https://en.wikipedia.org/wiki/TAKE_IT_DOWN_Act) · [FLUX.1 dev Non-Commercial License](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md) · [Ley 1581 de 2012 (Senado)](http://www.secretariasenado.gov.co/senado/basedoc/ley_1581_2012.html) · [EU AI Act Art. 50](https://artificialintelligenceact.eu/article/50/)

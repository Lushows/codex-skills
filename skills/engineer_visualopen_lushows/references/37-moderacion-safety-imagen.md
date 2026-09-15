## Moderación y Safety de Imagen / Contenido Generado

Any product that lets users generate or upload images needs a **multi-stage safety pipeline**, not a single classifier. The canonical flow: **pre-prompt filter → generate → post-image classifier → human review queue → (mandatory) CSAM reporting path**.

**NSFW / explicit classifiers.**
- `Falconsai/nsfw_image_detection` — ViT, binary normal/nsfw, ~98% acc, trivial to self-host (Apache-2.0), ~80M downloads. Good first-line gate.
- `NudeNet` — detects + localizes specific body parts (bounding boxes), useful when you need granularity (e.g. allow swimwear, block explicit).
- **CLIP-based** zero-shot — score against prompt-pairs ("a photo of explicit nudity" vs "a safe photo"); flexible but noisier.
- Managed: **AWS Rekognition** `DetectModerationLabels` and **Google Cloud Vision SafeSearch** (`adult`/`violence`/`racy`/`medical` likelihood) — pay-per-call, no model hosting, defensible audit trail.

```python
from transformers import pipeline
nsfw = pipeline("image-classification", model="Falconsai/nsfw_image_detection")
score = {d["label"]: d["score"] for d in nsfw(img)}
if score.get("nsfw", 0) > 0.85: reject()
```

**CSAM — a hard legal obligation, not a feature.** Under **18 U.S.C. § 2258A**, any U.S. "electronic service provider" that obtains *actual knowledge* of apparent child sexual abuse material on its system **must report to NCMEC's CyberTipline** as soon as reasonably possible. The **REPORT Act (2024)** broadened this to child sex trafficking and enticement. Knowing/willful failure to report carries fines up to **$150,000 (first offense)** and **$300,000 (subsequent)**. AI-generated CSAM is reportable too — NCMEC saw thousands of GenAI-CSAM reports, and most GenAI platforms were *not* reporting, a compliance gap regulators are watching. **Detection** uses cryptographic hash-matching against known-CSAM hash lists: **PhotoDNA** (Microsoft, perceptual hash, access via NCMEC/Microsoft), and **Thorn Safer** / **Google CSAI Match** (video). You hash uploads *and* generations, match against the list, block, preserve, and file a CyberTipline report. You do **not** keep copies for "review" beyond what the report process requires, and you must preserve per legal hold. This is non-optional for any user-gen or gen-image product touching US users — build it before launch.

**Prompt-level blocklist.** Pre-filter the *input* prompt against a denylist (terms implying minors + sexual context, named real people in NCII contexts, extreme violence/hate). Combine literal terms with embedding-similarity to catch obfuscation ("l0li", leetspeak, foreign-language synonyms). Reject before spending GPU.

**Output filtering + human review.** Even with prompt filters, run the *generated* image through the NSFW/violence classifier (diffusion models leak). Borderline scores (e.g. 0.4-0.85) go to a **human review queue** rather than auto-allow/auto-block. Log decisions for appeals and audits.

**Age / consent for avatars (likeness).** For face-swap / avatar / voice-clone features: require uploaded-likeness consent, block uploads of recognizable public figures without authorization, and gate "make this person say X" flows. This is both a safety and a legal-likeness issue (see file 04: NO FAKES Act, TAKE IT DOWN Act for NCII). Never let users generate sexual or intimate content of an uploaded real face.

**Violence / hate.** Use the multi-label managed APIs (Rekognition/Vision return `Violence`, `Hate Symbols`, `Visually Disturbing`) or fine-tuned classifiers; thresholds depend on your product's tolerance (a medical app vs a kids' app differ).

**Gotchas:**
1. **No CSAM path = legal exposure** — the § 2258A duty triggers on *actual knowledge*; building detection then not reporting is worse than not detecting. Wire the NCMEC report.
2. **Classifier on input OR output alone is insufficient** — filter both; prompt filters miss model leakage, output filters miss policy-violating prompts that produced "safe-looking" images.
3. **Thresholds are not universal** — Falconsai/NudeNet scores need calibration on *your* traffic; a fixed 0.5 cutoff floods false positives or leaks.
4. **Storing flagged CSAM** for ML training or review beyond reporting is itself a crime — never retain; follow NCMEC/legal-hold procedure exactly.
5. **Self-hosted-only stack has no audit trail** — for legal defensibility, managed APIs (Rekognition/Vision) give logged, timestamped decisions regulators accept.

This is technical guidance, not legal advice — consult counsel for § 2258A and NCMEC onboarding.

Sources: [18 U.S.C. § 2258A (LII)](https://www.law.cornell.edu/uscode/text/18/2258A) · [REPORT Act (Perkins Coie)](https://perkinscoie.com/insights/update/federal-legislation-seeks-change-online-child-safety-reporting-obligations-and) · [NCMEC CyberTipline data](https://www.missingkids.org/cybertiplinedata) · [Falconsai/nsfw_image_detection](https://huggingface.co/Falconsai/nsfw_image_detection) · [NudeNet](https://github.com/notAI-tech/NudeNet) · [AWS Rekognition moderation](https://docs.aws.amazon.com/rekognition/latest/dg/moderation.html) · [Google Vision SafeSearch](https://cloud.google.com/vision/docs/detecting-safe-search) · [Microsoft PhotoDNA](https://www.microsoft.com/en-us/photodna)

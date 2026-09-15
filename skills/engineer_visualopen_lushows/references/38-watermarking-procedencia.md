## Watermarking y Procedencia (Provenance)

Provenance answers "where did this media come from and was it AI-generated?" Two complementary mechanisms: **cryptographically-signed metadata** (C2PA) and **invisible signal watermarks** (SynthID, Stable Signature). You generally want both — metadata is rich but strippable, watermarks survive stripping but carry little data.

**C2PA / Content Credentials.** The open standard from the Coalition for Content Provenance and Authenticity (Adobe, Microsoft, Google, BBC, Intel, etc.); current spec is the **2.x line (2.2 published 2025-05, later 2.4)**. A C2PA **manifest** is a chain of cryptographically-signed **assertions** (who/what/when, the generating tool, edits, ingredients) bound to the asset and signed with an X.509 certificate. Tampering breaks the signature. Adopted across Adobe Firefly/Photoshop, Google (added to Search/Chrome verification), Meta, OpenAI (joined the C2PA steering committee in 2026 and embeds Content Credentials in DALL·E/Sora outputs). Attach with Adobe's open-source toolkit:

```bash
# c2patool — sign an image with a manifest
c2patool input.jpg -m manifest.json -o output.jpg
c2patool output.jpg            # read/verify the manifest
```

The Rust `c2pa`/`c2pa-python`/`c2pa-node` libs do the same programmatically. **Weakness:** metadata is easily stripped (screenshot, re-encode, `exiftool -all=`), so C2PA's own "durable Content Credentials" pairs the manifest with a watermark + fingerprint so a stripped asset can be re-linked.

**SynthID (Google DeepMind).** Invisible watermark embedded in the pixels/latents (and separately for **audio, video, and text** token distributions). Survives moderate crop, compression, color/filter changes. Google reports 100B+ assets watermarked since 2023. **Critical caveat:** the SynthID *detector and pattern are proprietary* — there is no public spec and you cannot independently verify a third party's SynthID; detection runs through Google's tooling/partners (SynthID Detector portal). So it's great if you generate on Google's stack, useless for verifying arbitrary internet images yourself.

**Open invisible-watermark libs (self-host).**
- `invisible-watermark` (`imwatermark`) — DWT-DCT, the lib SD WebUI/diffusers use to tag SD outputs; low capacity, breaks under heavy editing.
- **Stable Signature** (Meta) — fine-tunes the VAE decoder so *every* output carries a watermark inherent to the weights (can't be skipped at inference).
- **Tree-Ring** — embeds a pattern in the initial diffusion noise; robust to many transforms, but detection needs the inversion + key.

**Visible watermarks / metadata.** A visible logo or corner badge is the only thing a casual viewer sees; combine with invisible. Embed **EXIF/XMP/IPTC** fields (`Creator`, `DigitalSourceType=trainedAlgorithmicMedia` per the IPTC photo-metadata standard for synthetic media) — machine-readable, but strippable like all metadata.

**EU AI Act labeling (Article 50).** Providers of generative AI must mark synthetic audio/image/video/text outputs as artificially generated in a **machine-readable, detectable** format that is "effective, interoperable, robust and reliable… as far as technically feasible." **Application date: 2 August 2026** (the Digital Omnibus provisional agreement may grant systems already on the market a transition to **2 December 2026**). A **Code of Practice on AI-generated content** plus Commission guidelines operationalize it — C2PA + watermarking are the expected technical answers. Deployers of deepfakes must also disclose manipulation.

**Detection / robustness.** Test your watermark against the real adversary stack: JPEG re-encode (q=60), crop 20%, resize, screenshot, social-platform re-compression, and light inpainting. C2PA metadata: ~0% survival after screenshot/re-upload. `imwatermark`: survives light JPEG, dies under crop/editing. SynthID/Stable Signature/Tree-Ring: survive compression + moderate crop, degrade under heavy regeneration (img2img at high denoise can erase pixel watermarks). No watermark survives a determined adversary regenerating the image — provenance is for honest-actor labeling and forensics, not DRM.

**Gotchas:**
1. **C2PA without a watermark is trivially stripped** — always pair (durable Content Credentials).
2. **SynthID is not independently verifiable** — don't build a "we detect AI images" feature on it; you can't access the detector for arbitrary inputs.
3. **Art. 50 says "machine-readable + detectable"** — a visible badge alone does *not* satisfy it; you need the embedded machine-readable mark.
4. **Cert/trust-list management** — C2PA signatures are only as trustworthy as the signing cert; a self-signed manifest verifies integrity but not identity unless your cert chains to a recognized trust list.
5. **img2img/upscaling strips pixel watermarks** — re-watermark after any post-processing step in your own pipeline.

This is technical guidance, not legal advice.

Sources: [C2PA Spec 2.2 PDF](https://spec.c2pa.org/specifications/specifications/2.2/specs/_attachments/C2PA_Specification.pdf) · [c2patool](https://github.com/contentauth/c2patool) · [Content Credentials](https://contentcredentials.org/) · [SynthID (DeepMind)](https://deepmind.google/technologies/synthid/) · [invisible-watermark](https://github.com/ShieldMnt/invisible-watermark) · [Stable Signature (Meta)](https://github.com/facebookresearch/stable_signature) · [EU AI Act Article 50](https://artificialintelligenceact.eu/article/50/) · [EC Code of Practice on AI-generated content](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content)

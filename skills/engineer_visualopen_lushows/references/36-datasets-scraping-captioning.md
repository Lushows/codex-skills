## Datasets, Scraping y Captioning para Training

Building a training set for a LoRA or full fine-tune is a four-stage pipeline: **source → scrape → clean/dedup → caption → pack**. Each stage has legal and technical failure modes.

**Sourcing (ethical + legal).** Prefer permissively-licensed corpora: LAION (research-only, CC-BY metadata, images are *links* not files), Wikimedia Commons, Unsplash/Pexels (check API ToS), Common Crawl-derived sets, and CC-licensed material via Openverse. For commercial training, paid stock or your own shoots are the only clean path — scraping a stock site's previews violates ToS even if a court later finds *training* itself transformative (see file 04; the legal status of training is unsettled, the *contract breach* of ToS is not). Record provenance per image (source URL, license, retrieval date) in a sidecar — you cannot prove rights later without it.

**Web scraping.** Use `httpx` (async, HTTP/2) for static endpoints and `playwright` only when JS rendering is required (it is 10-50x slower and heavier).

```python
import httpx, urllib.robotparser as rp
r = rp.RobotFileParser(); r.set_url("https://site.com/robots.txt"); r.read()
assert r.can_fetch("MyBot/1.0", url)   # honor robots.txt
async with httpx.AsyncClient(http2=True, timeout=20,
        headers={"User-Agent":"MyBot/1.0 (+contact)"}, limits=httpx.Limits(max_connections=8)) as c:
    resp = await c.get(url)
```

Throttle to ~1-4 req/s/host with jitter; respect `Crawl-delay` and `429`/`Retry-After`. robots.txt is advisory (not law) but ignoring it is evidence of bad faith. ToS often forbids automated collection regardless of robots.txt — read it.

**Cleaning + dedup.** Two dedup layers: (1) **exact/near-exact** via perceptual hash — `imagededup` (PHash/DHash) or `imagehash`, threshold Hamming distance ≤ 5-8; (2) **semantic** near-duplicate via CLIP (`open_clip`) embeddings + FAISS, cosine > 0.95. Quality filtering: drop tiny/low-res (<512px short side for SDXL/FLUX-scale), blurry (variance-of-Laplacian), watermarked, and JPEG-artifact-heavy images. NSFW/quality scoring: `Falconsai/nsfw_image_detection` (ViT, ~98% acc) or an aesthetic predictor (LAION aesthetic v2). De-dup *before* captioning to save compute.

```python
from imagededup.methods import PHash
dups = PHash().find_duplicates(image_dir="data/", max_distance_threshold=6)
```

**Auto-captioning.** Pick by domain:
- **Natural-language**: `JoyCaption` (Alpha Two / Beta One — open, built for training-set captioning, configurable from terse to verbose), `Qwen2.5-VL` (3B/7B/32B/72B), `CogVLM2`, BLIP-2 (older/weaker baseline).
- **Anime/illustration tags**: WD-tagger (`SmilingWolf/wd-eva02-large-tagger-v3`, the modern v3 line) — produces booru-style comma tags.
A common hybrid: run WD-tagger for accurate tags, feed those as *hints* into JoyCaption for fluent prose.

**Caption style.** Match the base model's training distribution: SD1.5/anime LoRAs want **comma tags**; SDXL/FLUX want **natural sentences**. Insert a unique **trigger word** (e.g. `ohwx man`, `bioseta_logo`) at caption start so the concept binds to a rare token. Describe what should be *variable* (pose, background) and omit what should be *fixed* (the identity), so the model doesn't over-bake context.

**Bucketing + format.** Aspect-ratio bucketing (kohya `ss`, OneTrainer) groups images by resolution so you don't crop away content — essential for FLUX/SDXL. Pack into **WebDataset** (`.tar` shards of `{key}.jpg`+`{key}.txt`, stream-friendly for cloud/GPU), **Parquet** (HF `datasets`, columnar, good for embeddings), or a plain folder for small kohya runs. Dataset size: 15-30 images for a face LoRA, 100s-1000s for a style; balance classes so no concept dominates.

**Gotchas:**
1. **Captioning your own bias in** — a wrong/hallucinated caption (VLMs invent details) teaches the wrong association; spot-check 5-10%.
2. **Trigger-word collision** — using a real English word as trigger contaminates that token; use a rare/invented token.
3. **Dedup after caption wastes money** and leaves duplicate captions that overfit; dedup first.
4. **WebDataset key mismatch** — image and caption must share the exact basename within a shard or the loader silently drops pairs.
5. **LAION/Common Crawl ≠ rights** — these are *links/text*; redistributing the downloaded images can infringe. Keep license metadata per sample.

Sources: [imagededup](https://idealo.github.io/imagededup/) · [open_clip](https://github.com/mlfoundations/open_clip) · [Falconsai/nsfw_image_detection](https://huggingface.co/Falconsai/nsfw_image_detection) · [JoyCaption Alpha Two](https://civitai.com/articles/7697/joycaption-alpha-two-release) · [WD-tagger v3](https://huggingface.co/SmilingWolf/wd-eva02-large-tagger-v3) · [Qwen2.5-VL](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct) · [WebDataset](https://github.com/webdataset/webdataset) · [HF datasets](https://huggingface.co/docs/datasets)

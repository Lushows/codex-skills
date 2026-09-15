## Voz en Tiempo Real (Streaming STT/TTS, Voice Agents)

A real-time voice agent is a loop: **mic → VAD/endpointing → streaming STT → LLM → streaming TTS → speaker**, with **barge-in** (user interrupts → stop TTS). The product metric is *perceived latency* — time from user stopping speaking to first audio back. Budget it explicitly.

**Streaming STT (low latency).**
- **Deepgram Nova-3** — streaming finals ~300 ms (P50 ~337-509 ms, min ~184 ms), strong keyword boosting; **Deepgram Flux** integrates end-of-turn detection into the STT, cutting 200-600 ms vs separate STT+VAD.
- **AssemblyAI** Universal-Streaming — comparable, good formatting.
- **faster-whisper** (CTranslate2 build of Whisper) — best *self-hosted* option; `large-v3` on GPU is accurate but not truly streaming (chunked), use `distil`/`small` + sliding window for lower latency, or for offline/fallback.

```python
from faster_whisper import WhisperModel
m = WhisperModel("large-v3", device="cuda", compute_type="float16")
segments, _ = m.transcribe(audio, vad_filter=True, beam_size=1)  # beam=1 for speed
```

**VAD / turn-taking / endpointing.** `silero-vad` is the standard lightweight neural VAD (frame-level speech prob, ~1ms/chunk on CPU). Endpointing = deciding the user *finished* a turn: a fixed silence threshold (e.g. 200 ms after speech) is the baseline, but causes the classic "interrupting the user mid-pause" problem. Modern stacks use **semantic turn detection** (a small model predicting end-of-utterance from content, like LiveKit's turn-detector or Deepgram Flux) to wait through natural pauses but cut in fast at real turn-ends.

**Streaming TTS (first-token latency is everything).** What matters is **time-to-first-audio-byte (TTFB)**, not total synth time — you stream audio as it's produced.
- **ElevenLabs Flash v2.5** — sub-100 ms TTFB, 30+ languages; the production default for quality+latency.
- **CosyVoice 2** — first-packet ~**150 ms**, open-source, voice cloning; CosyVoice 3 (mid-2025) improves prosody.
- **Kokoro** (82M params) — ~100 ms local on modest GPU/Apple silicon, 54 voices, near-free to run; great for cost-sensitive or on-device.
- **Cartesia Sonic** — sub-100 ms, commercial.

**Full-duplex loop + barge-in.** Stream LLM tokens into TTS *sentence-by-sentence* (don't wait for the full LLM completion). Run the user's mic + VAD continuously even while TTS plays; on detected speech, **immediately stop TTS playback, flush the TTS buffer, and truncate the LLM turn** to what was actually spoken. Echo cancellation (WebRTC AEC) is required so the agent doesn't transcribe its own voice.

**Speech-to-speech models.** Direct S2S (OpenAI Realtime API / GPT-4o-realtime, Gemini Live, Moshi, Qwen-omni) skip the STT→text→TTS hops, winning ~hundreds of ms and preserving prosody/emotion — at the cost of weaker tool-use/control and harder content moderation than a text-LLM middle.

**Telephony.** Phone audio is **μ-law (PCMU) 8 kHz mono** — narrowband, so pick STT models tuned for it. **Twilio Voice** Media Streams sends 8kHz μ-law frames over WebSocket (or use SIP trunking to your media server). Resample to 16 kHz for most STT. WebRTC (`getUserMedia` + Opus) is the browser path — wideband, with built-in AEC/NS/AGC.

**WhatsApp voice-note flow.** WhatsApp voice notes arrive as **OGG/Opus**. Pipeline: download media → `ffmpeg -i note.ogg -ar 16000 -ac 1 out.wav` → STT (faster-whisper or Deepgram) → LLM → TTS → **encode back to OGG/Opus** (`ffmpeg -i reply.wav -c:a libopus -b:a 32k reply.ogg`) → send as `audio` message. WhatsApp is *not* full-duplex (it's async messages), so no barge-in — just transcribe-process-reply.

```bash
ffmpeg -i incoming.ogg -ar 16000 -ac 1 incoming.wav        # decode for STT
ffmpeg -i reply.wav -c:a libopus -b:a 32k -ar 48000 reply.ogg  # encode to send
```

**Latency budget (target < 800 ms perceived, full-duplex):** endpointing ~150-250 ms · STT final ~200-300 ms · LLM first token ~200-400 ms (use a fast model / prompt caching) · TTS TTFB ~100-150 ms · network/jitter buffer ~50-100 ms. The LLM is usually the long pole — stream its first sentence into TTS before it finishes.

**Gotchas:**
1. **Endpointing too aggressive** cuts users off mid-thought; too lax adds dead air — use semantic turn detection, not just a silence timer.
2. **No echo cancellation** → the agent hears itself and loops; enable AEC and/or gate STT while TTS plays.
3. **Measuring total TTS time, not TTFB** — you optimize the wrong number; stream and measure first byte.
4. **8 kHz telephony into a 16 kHz-trained model** tanks accuracy; resample and/or use a phone-tuned model.
5. **WhatsApp Opus mismatch** — send `audio/ogg; codecs=opus`; wrong container/codec makes the note unplayable. Don't forget to encode mono.

Sources: [Deepgram streaming latency](https://developers.deepgram.com/docs/measuring-streaming-latency) · [Deepgram Flux](https://developers.deepgram.com/docs/flux) · [silero-vad](https://github.com/snakers4/silero-vad) · [faster-whisper](https://github.com/SYSTRAN/faster-whisper) · [ElevenLabs models (Flash v2.5)](https://elevenlabs.io/docs/overview/models) · [CosyVoice 2](https://funaudiollm.github.io/cosyvoice2/) · [Kokoro](https://github.com/hexgrad/kokoro) · [OpenAI Realtime API](https://platform.openai.com/docs/guides/realtime) · [Twilio Media Streams](https://www.twilio.com/docs/voice/media-streams) · [WhatsApp Cloud API audio messages](https://developers.facebook.com/docs/whatsapp/cloud-api/messages/audio-messages)

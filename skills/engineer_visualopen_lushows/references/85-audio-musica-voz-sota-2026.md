# 85 — Audio, música y voz IA: estado del arte (junio 2026)

> Snapshot fechado.

## Música
- **Suno V5 / V5.5** (2026) — **Studio DAW integrado**, **Generative Stems (12 pistas)**, Vocal Personas, salida 44.1kHz. El más completo end-to-end. (V5.5 rompió algunos flujos de V5.)
- **ElevenLabs Music** — lanzó **abril 2026, $9.99/mes**. **Vocales superiores en aislamiento** (vibrato/respiración realistas) por su núcleo de síntesis de voz.
- **Udio (v3.5)** — diferenciador: **inpainting** (regenerar una sección) + **stem separation**. Lo más cercano a un "AI DAW".
- **MiniMax Music 2.5** (fal, $0.035/gen) — API barata. **Stable Audio 3.0** — hasta **180s**.

## TTS / Voice clone (el open ganó terreno)
- **Chatterbox / Turbo** (MIT) — clona voz desde **10s**. **Chatterbox-Turbo ganó 65.3% en blind test vs ElevenLabs 24.5%** — open batiendo al líder closed.
- **Kokoro** — **82M params, corre en CPU**, 8 idiomas, 54 voces, **36× real-time en T4 gratis**. Campeón de eficiencia.
- **F5-TTS** — voice clone open de referencia. **ElevenLabs v3** — tier premium de expresividad emocional (API).

## SFX / Foley
- **ElevenLabs SFX** — **líder de calidad**, calificado **indistinguible de foley grabado** en blind tests. 48kHz/24-bit broadcast-ready. **Límite: 30s máximo** por generación.
- **Stable Audio 3.0** — la generación más larga (180s), ideal ambientes/soundscapes.

## Gotchas
1. **Licenciamiento comercial varía mucho:** Chatterbox (MIT) y Kokoro son comercial-safe; verifica términos de Suno/Udio por tier.
2. ElevenLabs SFX topa en **30s** — para ambientes largos usa Stable Audio 3.0.
3. **Suno V5.5 rompió flujos** de V5 — fija la versión si tienes pipeline en producción.
4. Open TTS gana en costo/privacidad pero **clonar voces tiene riesgo legal/ético** (consentimiento) — no asumas vía libre.
5. Kokoro es ultrarrápido pero **82M = menos expresividad** que ElevenLabs v3 para emoción matizada.
6. Claims tipo "Voxtral iguala a ElevenLabs gratis" son de blog — **verifica en tu propio eval** antes de migrar.

**Fuentes:** teamday.ai/blog (best music 2026) · jam.com/resources (Suno vs Udio may 2026) · findskill.ai/blog (open TTS 2026) · elevenlabs.io/sound-effects.

# 216 · Voice design: diseñar una voz desde cero (sin muestra)

> Clonar necesita un audio de referencia. **Voice design** no: describes la voz en lenguaje natural
> ("mujer cálida, acento británico leve, habla lento y claro") y el modelo la **inventa**. Útil cuando no
> tienes —ni quieres— una voz real: marcas, personajes, narradores sin problemas de consentimiento.

## Voice design vs voice cloning (la diferencia que decide el enfoque)
| | **Voice design** | **Voice cloning** |
|---|---|---|
| Entrada | Prompt de texto describiendo la voz | Audio de referencia (3-10s) |
| Genera | Una voz nueva, inexistente | Réplica de una voz real |
| Consentimiento | No aplica (voz sintética) | Necesitas permiso de la persona |
| Reproducibilidad | Fija seed/embedding para reusarla | La da la referencia |
| Caso | Branding, personajes, IVR genérico | Doblaje, asistente con voz de alguien |

## Open-source para voice design (2026, [verificado])
- **Parler-TTS** (HuggingFace): el referente open de descripción por lenguaje natural. Le describes timbre,
  acento, velocidad, tono ("warm female voice, slight British accent, slow and clear") y sintetiza acorde.
  No requiere muestra de audio. Innovación clave del espacio open en diseño de voz.
- **Qwen3-TTS** [verificado]: soporta **voice design** + control de voz custom + streaming + clonado rápido,
  10 idiomas. Más reciente y multilingüe que Parler.
- **Voxtral TTS** (Mistral, ~4B, mar-2026 [verificado]) y la ola de alternativas a ElevenLabs amplían el menú,
  aunque no todas exponen *diseño por prompt* puro (varias son clonado + control).

Referencia comercial: **ElevenLabs Voice Design** es el estándar de mercado; Parler/Qwen3 son el equivalente
auto-hospedable cuando el prompt-to-voice es el requisito.

## Cómo funciona (por qué un prompt produce una voz)
El modelo se entrena con pares (audio, descripción textual de ese audio). Aprende a mapear atributos del
lenguaje —género percibido, edad, acento, ritmo, calidez— a un **embedding de locutor**. En inferencia, el
prompt produce ese embedding y condiciona el sintetizador. No "elige" de una biblioteca: **interpola** en el
espacio de voces aprendido.

## Patrón de producción: congelar la voz diseñada
El riesgo de voice design es la **deriva**: el mismo prompt puede dar voces ligeramente distintas entre runs.
Para una marca necesitas *la misma voz siempre*:
```
1. Itera prompts hasta dar con la voz → fija seed.
2. Extrae y guarda el speaker embedding resultante (no solo el texto del prompt).
3. En producción, reusa el embedding guardado, no re-generes desde el prompt.
4. Versiona el embedding como un asset (voice_brand_v1.pt).
```
Así el prompt es la fase de *diseño*; producción corre sobre un embedding inmutable = consistencia garantizada.

## Detalles que muerden
- **El prompt controla atributos gruesos, no finos**: acierta en género/acento/ritmo; "que suene como X
  persona concreta" no es voice design, es clonado. No fuerces identidad real por prompt.
- **Acentos y idiomas**: cobertura desigual. Verifica que el modelo entrenó el acento que pides; Qwen3 cubre
  más idiomas que Parler.
- **Emoción es ortogonal**: voice design fija *quién* habla; la emoción la pones aparte (ver
  [[212-emotion-style-control-tts]]). No esperes rango emocional solo del prompt de diseño.
- **Sin embedding guardado = sin reproducibilidad**: si solo guardas el texto del prompt, perdiste la voz.
  Persistir el embedding es obligatorio para uso de marca.

## Sizing
Parler/Qwen3 (~0.5-4B) caben en GPU 8-12GB fp16. El diseño es offline (una vez); producción es TTS normal,
streameable (ver [[213-streaming-tts-baja-latencia]]). El embedding pesa KBs.

Cruza con [[05-tts-voice-cloning-2026]].

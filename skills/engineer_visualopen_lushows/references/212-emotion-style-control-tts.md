# 212 · Control de emoción, estilo y prosodia en TTS

> Clonar una voz es resolver el *timbre*. El cliente real pide *intención*: que suene alegre, urgente,
> susurrante, sarcástica. Eso es control de emoción/estilo/prosodia, y se hace por tres palancas distintas.

## Las tres palancas (no son lo mismo)
| Palanca | Qué controla | Granularidad | Mecanismo típico |
|---|---|---|---|
| **Escalar** | Intensidad global | Por frase | Un float (`exaggeration`) |
| **Vector de emoción** | Mezcla discreta (8 emociones) | Por frase | Embedding de emoción condicionante |
| **Tags inline** | Énfasis, pausas, risa | Por palabra/token | Marcado en el texto `<laugh>`, `[emphasis]` |

## Por modelo (2026, [verificado])
- **Chatterbox** (Resemble, sobre arquitectura CosyVoice2): primer open-source con `exaggeration` controlable.
  Defaults `exaggeration=0.5, cfg=0.5`. 0.0 = plano/monótono, 1.0+ = teatral. Una sola perilla, simple y robusta.
- **IndexTTS-2**: control avanzado con **vectores de 8 emociones** + *character tags* + análisis dinámico del texto.
  Es el más expresivo de los open si necesitas mezclar emociones (ej. 0.7 enojo + 0.3 tristeza).
- **CosyVoice2 / F5-TTS**: no traen perilla nativa fuerte, pero son la base sobre la que se *inyecta* emoción.
- **Qwen3-TTS, Step Audio EditX, Higgs Audio 2, VibeVoice**: integrables vía TTS-Audio-Suite (nodos ComfyUI).

## EmoSteer: control sin reentrenar (la técnica que importa)
EmoSteer-TTS [verificado] hace control **continuo y training-free** sobre modelos zero-shot ya entrenados
(F5-TTS, CosyVoice2). Idea:
1. Identifica *tokens emocionalmente salientes* en las activaciones internas.
2. Construye un **steering vector** = (activación-emoción − activación-neutral) para 6 emociones base.
3. En inferencia, **suma α·vector** a las activaciones → desplaza la emoción sin tocar pesos.

Por qué importa para self-hosting: añades emoción a un modelo que no la expone, sin fine-tuning, sin dataset
emocional, sin GPU de entrenamiento. Solo capturas activaciones una vez y guardas los vectores (KBs).

## Patrón de producción
```
1. Texto entra con tags semánticos del LLM:  "{emotion:excited} ¡Llegó tu pedido! <laugh>"
2. Parser separa: texto limpio + emoción + posición de tags inline.
3. Mapea emoción → (exaggeration, vector) según el modelo elegido.
4. Para énfasis fino → EmoSteer α por segmento, o tags nativos si el modelo los soporta.
5. cfg/temperature: subir exaggeration suele acelerar el habla → baja cfg (~0.3) para compensar.
```

## Detalles que muerden
- **Exaggeration alta degrada inteligibilidad**: pasado ~0.8 el modelo "actúa" pero arrastra palabras.
  Tope práctico 0.6-0.7 para contenido que se debe entender (avatar, IVR).
- **Acoplamiento emoción↔velocidad**: casi todos los modelos aceleran al emocionar. Si necesitas duración
  fija (doblaje, ver [[215-dubbing-translation-pipeline]]), controla emoción y *luego* time-stretch.
- **Emoción y voz clonada compiten**: una referencia muy neutra "ancla" el timbre y resiste la emoción.
  Da una referencia con algo de expresión si quieres rango.
- **Consistencia entre frases**: fija el seed y los parámetros por sesión; variar exaggeration frase a frase
  rompe la ilusión de un mismo locutor.

## Sizing
Modelos ~0.5-4B params → caben en una GPU de 8-12GB en fp16. EmoSteer no añade VRAM relevante (vectores en CPU/GPU).

Cruza con [[05-tts-voice-cloning-2026]] y [[211-chatterbox-serving]].

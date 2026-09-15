# 19 · Voz y audio

> Fuentes: engineer_visualopen_lushows refs 05 (TTS open-source y clonación de voz), 40 (voz en tiempo real / STT) y 61 (voice agents y telephony). Hermanos GASTROWHATS/BIOWHATS ya usan OpenAI Whisper (`src/audioTranscriber.js`) para transcribir y ElevenLabs/OpenAI para TTS.

## Por qué el audio le importa al comerciante colombiano
El dueño de la tienda, el restaurante o la peluquería casi siempre prefiere hablar antes que escribir. Está atendiendo, tiene las manos ocupadas, escribe lento o le da pereza teclear datos largos como el NIT o una dirección. La nota de voz es su canal natural en WhatsApp. Si AVIS solo entiende texto, pierde a una parte enorme de la base de pymes; entender el audio es entender al cliente real, no al cliente ideal.

## Estado actual vs roadmap
**Hoy el audio NO está implementado en AVISPA'O** — AVIS responde solo a texto. Toda esta referencia describe el comportamiento objetivo (roadmap). Cuando se active, el patrón a copiar ya existe y está probado en los proyectos hermanos: Whisper para transcribir lo que entra, y TTS solo para mensajes puntuales de salida. No se reinventa nada; se adapta.

## Transcribir las notas de voz entrantes (STT)
Cuando el cliente manda una nota de voz, AVIS la transcribe y procesa el texto como si la hubiera escrito. La nota llega como **OGG/Opus** desde WhatsApp; siempre se convierte con ffmpeg a 16 kHz mono antes del modelo (`ffmpeg -i nota.ogg -ar 16000 -ac 1 nota.wav`). El motor recomendado es **faster-whisper** (`large-v3`, ~4× más rápido que openai-whisper) auto-hospedado, o la API de OpenAI Whisper como ruta rápida — la que ya usa el hermano. Se fuerza `language="es"` para que no confunda el español colombiano con otro idioma.

## Español Colombia y manejo de ruido
El comerciante graba en un local con ruido: cocina, música, gente, motos en la calle. Whisper `large-v3` aguanta bastante, pero conviene activar `vad_filter=True` para recortar silencios y ruido de fondo, y no degradar pasando el opus crudo (siempre 16 kHz mono). El acento paisa, costeño o rolo no es problema para Whisper, pero los datos críticos sí: números de NIT, cédula y direcciones se transcriben mal con audio sucio.

## Cuándo AVIS responde con voz vs texto
**Texto por defecto, siempre.** El texto es gratis, instantáneo, se relee, se copia y se reenvía — y los datos de cumplimiento (fechas, montos, links, NIT) deben quedar escritos para que el comerciante los tenga. La voz se reserva para momentos **cálidos y humanos**: el saludo de bienvenida en el onboarding, una felicitación cuando queda al día con un trámite, o un mensaje de cercanía. Nunca para listas de requisitos, plazos legales ni cifras. La voz suma calidez; el texto carga la información.

## Costo y latencia de responder con voz
Generar voz cuesta plata y tiempo: TTS por API se paga por carácter y agrega segundos de generación + encode a OGG/Opus antes de enviar. Por eso la voz es la excepción, no la regla. Como WhatsApp es asíncrono (no es una llamada en vivo), **no hay presupuesto de latencia ni barge-in** — AVIS genera la nota completa y la manda como archivo de audio. Mucho más simple y barato que un agente de voz telefónico.

## Voces: clonada vs genérica
Dos caminos para el TTS de salida cuando se active:
- **ElevenLabs (voz clonada / premium):** la más natural; permite una voz de marca consistente para AVISPA'O. Se paga por carácter. Ideal si la voz se vuelve parte de la identidad.
- **OpenAI TTS (voz genérica):** más barata y suficiente para mensajes transaccionales cálidos; cero deploy, ya está en el stack del hermano.
- **Open-source self-host (Kokoro Apache, Chatterbox MIT, CosyVoice2 Apache):** costo marginal casi cero a volumen alto; el acento es-CO sale del clip de referencia clonado, no del modelo base. Evitar F5-TTS y XTTS-v2: son **non-commercial** y AVISPA'O es comercial.

## Buenas prácticas
1. **Si el audio es dudoso, confirmar lo entendido, no asumir.** AVIS repite en texto el dato clave: "Entendí que tu NIT es 900.123.456-7, ¿está bien?" antes de actuar sobre él.
2. **Nunca dar por cierto un número crítico transcrito de voz** (NIT, cédula, dirección, monto, fecha) sin verificación escrita del cliente.
3. **Responder en texto lo que debe quedar registrado** aunque el cliente haya hablado; la voz no reemplaza el comprobante escrito.
4. **Una sola voz, sin música ni ruido** en cualquier clip de referencia si se clona la voz de marca.
5. **Acusar recibo del audio** si la transcripción falla: "No te escuché bien, ¿me lo repites o me lo escribes?" — nunca quedarse callado ni inventar.

> **Roadmap:** el audio (transcripción entrante + voz de salida ocasional) es funcionalidad planeada, aún no implementada en AVISPA'O. Cuando llegue: empezar por STT con Whisper (alto valor, el comerciante habla más de lo que escribe), y solo después sumar TTS de bienvenida con voz de marca; medir costo por mensaje antes de generalizar la voz de salida.

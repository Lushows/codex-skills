# 249 · Jailbreak y adversarial contra modelos de imagen

> Si auto-hospedas un modelo de imagen/avatar, alguien intentará usarlo para generar lo que tú prohíbes
> (NSFW, deepfakes, violencia, marcas). El filtro de prompt ingenuo se rompe en minutos. Defiéndete en capas.

## Por qué tu safety filter ingenuo no aguanta
La defensa típica —una blacklist de palabras en el prompt— cae ante ataques publicados y reproducibles:

| Ataque | Cómo evade |
|---|---|
| **SneakyPrompt** | RL perturba tokens hasta que el filtro de texto pasa pero el modelo entiende el concepto prohibido. |
| **MMA-Diffusion** | Ataque multimodal: perturba texto **y** la imagen de entrada (img2img) a la vez. |
| **GhostPrompt** | Optimización dinámica que reescribe el prompt para parecer inocuo y mantener el contenido. |
| **Parches/paráfrasis agnósticas** (2025) | Un parche adversarial en la imagen + set de paráfrasis que bypassa cualquier prompt-filter sin reentrenar por caso. |
| **Codificación** | Sinónimos, otros idiomas, leet, descripción indirecta ("el actor de la peli X sin ropa"). |

Lección: el contenido prohibido **no vive en palabras concretas**; vive en el concepto que el modelo
reconstruye. Filtrar strings es perder. Necesitas defensa en profundidad sobre **prompt, latente y output**.

## Las tres capas (defensa en profundidad)
1. **Pre-filtro de entrada** (texto + imagen ref):
   - Clasificador semántico (embeddings), no regex. Normaliza idioma/encoding antes de clasificar.
   - Para img2img/avatar: revisa la **imagen de referencia** (¿es un menor? ¿una celebridad? ¿una marca?).
2. **Guía durante la generación** (lo más robusto):
   - **Negative prompting** y **concept erasure** (SLD/ESD-style): borra conceptos NSFW de los pesos →
     aunque el prompt pase, el modelo no sabe generarlos. Sobrevive a muchos jailbreaks de texto.
3. **Post-moderación del output** (la red de seguridad real):
   - Clasificador sobre la **imagen/frames generados** (NSFW, gore, rostro de figura pública). Es lo que
     ven los jailbreaks que pasan las dos capas anteriores. Ver [[165-moderacion-safety-output-generado]].
   - En video/avatar: muestrea N frames, no solo el primero (el ataque puede esconder el frame malo en medio).

## Avatares y deepfakes: la amenaza específica de STUDIO
Generación de **cara/voz** abre un riesgo extra: clonar a una persona real sin consentimiento.
- **Consentimiento verificable** de la identidad de origen (la cara/voz subida). Liga al log de auditoría
  ([[251-audit-logging-compliance]]) y a la base legal ([[250-privacy-biometric-data]]).
- **Detección de celebridades/figuras públicas** en la imagen de referencia → bloquear o exigir prueba.
- **Watermark/C2PA** en todo lo generado: deja claro que es sintético y trazable.

## Defensa operativa (no solo modelo)
- **Rate-limit + cuotas por usuario**: los ataques de optimización (SneakyPrompt/GhostPrompt) necesitan
  **muchas queries** para converger. Limitar consultas mata el ataque iterativo en la práctica.
- **Detección de comportamiento de jailbreak**: muchos rechazos seguidos del mismo usuario → flag/ban.
- **Fail-closed**: si el moderador de output falla o tarda, **no** entregues la imagen.
- **No expongas el endpoint crudo**: mete el gateway de safety **delante** del worker GPU; el worker no decide políticas.
- **Loguea el intento bloqueado** (prompt + decisión) para forense y para mejorar el clasificador.

## Lo que NO funciona
Confiar en el safety checker que viene en el repo (se desactiva con un flag), filtrar solo palabras, o
moderar solo el prompt. Asume que la entrada es adversarial **siempre** ([[28-seguridad-ia-agentes-llm]]).

Cruza con [[165-moderacion-safety-output-generado]] y [[28-seguridad-ia-agentes-llm]].

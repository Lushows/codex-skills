# 117 · Control de cámara y movimiento del avatar (cuando el único botón es el prompt)

> Muchos workers de avatar exponen SOLO un `prompt` de texto: ni negative-prompt, ni motion-scale, ni
> control de cámara. Aprende a dirigir cámara/movimiento desde el prompt positivo.

## El síntoma: zoom/deriva no deseados
LongCat-Avatar (y similares) añaden movimiento "vivo" por defecto. Un prompt como
`"news anchor talks to the camera with lively expressions"` induce **zoom-in** y cabeceo. El usuario
quería **estático y natural**.

## La palanca: prompt positivo (no hay negative-prompt)
El handler suele pasar solo `{prompt, cond_image, cond_audio}`. Sin negative-prompt, mete las
prohibiciones en el **positivo**:
```
News anchor speaking with calm, natural expressions and still posture.
Static locked camera, no zoom, no camera movement.
```
- **Estático**: `static locked camera`, `fixed framing`, `tripod shot`, `no zoom`, `no camera movement`.
- **Natural (no robótico)**: `calm natural expressions`, `subtle`, `still posture` (en vez de `lively`,
  `energetic`, `dynamic`, que disparan movimiento).
- **Encuadre**: `frontal portrait`, `centered`, `medium shot` ayudan a fijar composición.

## Límite de caracteres (¡muerde!)
El handler de LongCat **recorta el prompt a 125 caracteres** (`prompt[:125]`). Un prompt largo se trunca
a media frase y pierde justo la parte de "no zoom". **Verifica el límite del worker** y mantén el prompt
corto y con lo importante al inicio. (El ejemplo de arriba ≈ 120 chars.)

## Hazlo configurable (iterar sin re-deploy)
Pon el prompt en una env (`LIPSYNC_AVATAR_PROMPT`) con un default en código. Así pruebas variantes al
instante sin reconstruir/redeploy:
```js
prompt: prompt || process.env.LIPSYNC_AVATAR_PROMPT || DEFAULT_PROMPT
```

## Si el prompt no basta (el modelo sigue derivando)
1. **Reference image**: encuadre/composición del input condiciona el output. Una foto frontal, centrada,
   busto, fija el marco mejor que un primer plano recortado.
2. **Post-proceso**: estabilización/crop con ffmpeg (`vidstabdetect`/`vidstabtransform`) o un crop fijo
   si el modelo hace un push-in consistente. Ver [[09-interpolacion-edicion-video-ffmpeg]].
3. **Otro modelo/flag**: algunos exponen `motion_bucket`/`cfg`/`guidance` o un modo "still". Revisa el
   repo; si existe, es más fiable que el prompt.
4. **Negative-prompt real**: si el modelo lo soporta pero el handler no lo pasa, **agrégalo al handler**
   (`negative_prompt="zoom, camera movement, motion blur, shaky"`).

Cruza con [[47-direccion-cinematografica-video-ia]] y [[111-longcat-avatar-runpod-produccion]].

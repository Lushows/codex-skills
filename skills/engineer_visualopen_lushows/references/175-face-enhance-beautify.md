# 175 · Realce / beautify de cara sin perder identidad

> Subir nitidez y "embellecer" una cara es fácil de pedir y fácil de arruinar: el mismo botón que limpia la piel también **borra la identidad**.
> El arte aquí es realzar lo justo y frenar antes de que la persona deje de ser ella.

## Restauración ≠ beautify (no confundir)
- **Restauración** (`[[148-face-restoration-output-avatar]]`): repara degradación — output de difusor borroso, 128px del swap, compresión. Objetivo: que se vea *bien hecho*.
- **Beautify**: cambia rasgos a gusto — suaviza piel, agranda ojos, afina mandíbula. Objetivo *estético*, no técnico. Esto **mueve la identidad a propósito** y por eso es peligroso.

Casi siempre quieres restauración controlada, no beautify agresivo.

## La palanca que importa: fidelity weight (CodeFormer)
CodeFormer expone `w ∈ [0,1]`: **w=0** prioriza calidad/belleza (limpio pero **deriva** del rostro real), **w=1** prioriza fidelidad (conserva identidad, menos pulido). Punto de partida **w≈0.5** y ajusta según qué pesa más. Para conservar identidad en avatares de marca, **sube w (0.6-0.8)**; nunca bajes a 0 si la persona debe reconocerse.

## GFPGAN vs CodeFormer (cuándo cada uno)

| Modelo | Mecanismo | Brilla en | Riesgo de identidad |
|---|---|---|---|
| **CodeFormer** | codebook discreto + fidelity weight | retratos modernos, daño leve, control de deriva | bajo si w alto |
| **GFPGAN** | prior StyleGAN2 (SFT) | fotos viejas/muy degradadas | mayor: tiende a "inventar" rasgos |
| GPEN / RestoreFormer | priors alternativos | comparar en casos límite | variable |

Regla: cara ya decente que solo necesita pulido → **CodeFormer con w alto**. Foto destruida → GFPGAN, asumiendo que reinterpretará rasgos.

## El dilema central (por qué no hay almuerzo gratis)
Los métodos que **sintetizan** textura de alta calidad tienden a **perder identidad**; los
**fieles a la identidad** salen **sobre-suavizados**, con poca textura. No existe el "máximo
de todo": eliges en el eje calidad↔fidelidad. Para producto de marca, **fidelidad gana** —
un avatar guapo pero que no es la persona es un fracaso.

## Tabla de decisión por fidelity weight (CodeFormer)

| w | Resultado | Cuándo |
|---|---|---|
| 0.0-0.3 | máx. belleza, deriva fuerte | foto irreconocible que solo quieres "bonita" |
| 0.4-0.5 | equilibrio, punto de partida | caso general, primer intento |
| 0.6-0.8 | identidad fuerte, menos pulido | avatar de marca, persona debe reconocerse |
| 0.9-1.0 | máx. fidelidad, mínimo realce | restauración conservadora |

## Beautify controlado (si de verdad lo piden)
- Aplica en **regiones**, no global: suavizar piel sí, tocar geometría de ojos/mandíbula no (ahí muere la identidad).
- Mide la deriva: calcula **distancia de embedding ArcFace** entre original y realzado. Si supera un umbral, rechaza/baja la fuerza. Esto convierte "se ve raro" en una métrica.
- Cuidado con el **sesgo de belleza**: muchos beautify blanquean piel, europeízan rasgos y feminizan por defecto → daño reputacional y ético. Audítalo.

## Cuándo NO restaurar
- Cara ya nítida y de alta resolución: restaurar solo introduce el "look CodeFormer"
  (piel de plástico, ojos vidriosos). Si no hay degradación, sáltatelo.
- Estilos no-fotográficos (ilustración, 3D): el restaurador asume rostro fotorrealista y
  rompe el estilo. Desactívalo o úsalo con w muy alto.

## Serving
- Barato en VRAM (cientos de MB); es un paso de post de la generación pesada. Cachea pesos
  en el volumen (`[[113-network-volume-modelos-grandes]]`).
- Orden del pipeline: generación → restauración (fidelity alto) → upscale. Beautify, si va,
  antes del upscale. Nunca upscalees y luego restaures: la restauración re-comprime detalle.

## Riesgo legal
Alterar la cara de una persona real (sobre todo afinar/idealizar) puede ser **manipulación no consentida** de su imagen, e implica las mismas reglas de likeness/etiquetado que el resto del bloque facial. Ver `[[39-legal-ia-generativa]]` y `[[165-moderacion-safety-output-generado]]`.

Cruza con [[148-face-restoration-output-avatar]], [[176-expression-gaze-edit]] y [[172-face-swap-insightface-reactor]].

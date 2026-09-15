# 71 — Kill criteria

Lee este módulo cuando un ad o un ad group está gastando y no convierte y no sabes si apagarlo o aguantarlo, cuando te da culpa "matar" un creativo que te costó producir, o cuando apagas cosas por pánico el primer día malo. Kill criteria = las **reglas escritas de antemano** que deciden cuándo apagas algo, para que la decisión no dependa de tu estado de ánimo de ese día. Es lo contrario al pánico: matas con criterio, no con miedo. En TikTok esto es disciplina pura, porque la varianza alta (ver 70) tienta a matar demasiado pronto, y el frame de descubrimiento exige darle al algoritmo su ventana antes de declarar muerto un creativo.

## La regla maestra: gasto vs CPA objetivo

No mates por tiempo ("ya lleva 3 días"), mata por **gasto sin resultado**. La pregunta no es "¿cuántos días?" sino "¿cuánto gastó este ad comparado con lo que me puedo dar el lujo de pagar por una venta?".

Necesitas un número antes de empezar: tu **CPA objetivo** (costo por adquisición que tu negocio aguanta). Eso sale de tus márgenes — si no lo tienes claro, calcúlalo con `economist_lushows` (CAC/LTV, punto de equilibrio). Sin CPA objetivo, no puedes matar con criterio; estás adivinando.

La regla práctica más usada en TikTok:

| Situación | Umbral de muerte |
|---|---|
| Ad gastó **2–3× tu CPA objetivo** con **0 conversiones** | Apágalo. No es varianza, está muerto. |
| Ad gastó 1× tu CPA sin conversión | Aguanta — todavía es ruido normal (varianza alta, ver 70). |
| Ad con conversiones pero CPA **>2× objetivo** sostenido 5–7 días | Apágalo o reduce, pero dale la ventana primero. |
| Ad con CPA cerca del objetivo | Déjalo correr; es un candidato a escalar (ver 72). |

Ejemplo Colombia: tu CPA objetivo es $25.000 COP por lead que cierra por WhatsApp. Un creativo gastó $60.000 (≈2.4× tu CPA) sin un solo lead → muerto, apágalo. Otro gastó $20.000 sin lead → todavía no concluyas, sigue siendo ruido.

¿Por qué 2–3× y no 1×? Porque con 1× tu CPA sin conversión todavía estás dentro del rango de varianza normal de TikTok: un ad bueno puede gastar el equivalente a una venta antes de traer la primera. A 2–3× sin nada, la probabilidad de que sea un mal creativo (y no mala suerte) ya es altísima. El umbral exacto dentro de ese rango depende de tu volumen: si haces muchas conversiones al día, usa 2×; si haces pocas (varianza más alta), dale hasta 3× antes de concluir.

## Señales tempranas que adelantan la muerte

Antes de que el ad gaste 2–3× tu CPA, las métricas de creativo (ver 60, 68) te dan pistas de que va a morir. No son para matar solas, pero sí para **priorizar a quién vigilar**:

| Señal temprana | Umbral de alarma | Qué indica |
|---|---|---|
| **Hook rate / thumbstop** (paran en 1–3s) | <20–25% | Nadie se detiene; el hook no sirve (ver 37) |
| **CTR** | muy por debajo del promedio de la cuenta | El creativo no genera interés |
| **Hold rate** (ven hasta el final) | muy bajo | El cuerpo del video no retiene |
| **CPM disparado** vs otros ads | muy alto | TikTok castiga un creativo de baja calidad con CPM caro |

Si un ad tiene hook rate pésimo Y va camino a 2× tu CPA sin convertir, no esperes el umbral completo — ya sabes hacia dónde va. Mátalo y mete uno con mejor hook.

## Sin pánico, sin decisiones de un día

El error más caro en kill no es matar tarde — es **matar demasiado pronto**. La varianza alta de TikTok (ver 70) hace que un ad bueno pueda tener un día seco. Reglas anti-pánico:

1. **Nunca mates por el resultado de un solo día.** Un martes con 0 ventas no significa nada si el lunes trajo 3.
2. **El umbral es por GASTO acumulado, no por calendario.** "Gastó 2.5× mi CPA sin convertir" es objetivo; "ya van dos días" es emocional.
3. **Necesitas volumen para juzgar el CPA, no para juzgar la muerte.** Para escalar necesitas ~10 conversiones (ver 60). Pero para matar te basta el gasto-sin-vida: si gastó 3× tu CPA y trajo CERO, no necesitas estadística para saber que no sirve.
4. **Mata el ad, no la cuenta.** Apagar un creativo muerto es sano. "Resetear la cuenta" es un mito (ver 76) — no existe.

## Qué nivel apagas: ad, ad group o nada

| Qué muere | Cuándo |
|---|---|
| **Un creativo (ad)** | Lo normal. Un ad gastó 2–3× CPA sin convertir → fuera. El ad group sigue vivo con los demás. |
| **Un ad group entero** | Solo si TODOS sus creativos murieron, o si el público/evento estaba mal armado. Raro. |
| **Una campaña** | Casi nunca por kill: solo si la oferta entera no funciona o el evento está mal definido (ver 14, 41). |
| **Nada (aguantar)** | Si está dentro de la ventana de aprendizaje (0–3 días, ver 13) o gastó <1× tu CPA. |

La jugada sana es matar a nivel de **creativo** y dejar que el ad group respire con los que quedan, mientras metes creativos nuevos (ver 73). Matar ad groups enteros resetea aprendizaje y suele ser exagerado.

Una excepción que sí justifica matar más arriba: si llevas semanas y **ningún** creativo del ad group converte, el problema no es el creativo — es el público, el evento de optimización (ver 14) o la oferta (ver 41). Ahí no sigas alimentando creativos a un ad group roto; pausa, arregla la causa raíz y relanza limpio.

## Antes de matar, descarta los falsos muertos

No todo CPA malo es un creativo malo. Antes de apagar, verifica en 30 segundos que no estés matando algo sano:

1. **¿El tracking está vivo?** Si el Pixel/Events API se cayó (ver 05, 06), el ad podría estar convirtiendo y tú no lo ves. CPA "infinito" con clics y tráfico sanos = sospecha de tracking, no de creativo.
2. **¿Es varianza de un día?** Mira la ventana de 7 días (ver 70). Hoy 0 conversiones, ayer 2 = vivo.
3. **¿La landing/WhatsApp funcionan?** El ad trae el clic pero si la página no carga o nadie contesta el WhatsApp (ver 55), el creativo no tiene la culpa → `desingweb-lushows` / `ventas_lushows`.

Si los tres están sanos y aun así gastó 2–3× tu CPA sin convertir, ahora sí: mátalo frío.

## Después de matar: no dejes el hueco

Apagar un muerto sin reemplazarlo es media tarea. Cada creativo que matas debe tener un reemplazo entrando — ese es el ciclo de TikTok: el creativo se quema en 1–2 semanas (ver 39, 73), así que **matar + reponer** es el latido normal de la cuenta, no una emergencia. Si matas más rápido de lo que produces, te quedas sin con qué pautar. Por eso la fábrica de creativos (ver 39) es la base de todo. Un buen reflejo operativo: por cada creativo que apagas esta semana, ten dos entrando — así nunca te quedas seco y siempre hay candidatos a ganador nuevo.

## Errores comunes — blacklist

- **Matar el primer día malo.** La varianza alta de TikTok castiga al impaciente. Espera el umbral de gasto, no el calendario (ver 70).
- **No tener un CPA objetivo.** Sin ese número no puedes matar con criterio, solo adivinar. Calcúlalo con `economist_lushows`.
- **Matar por "ya lleva X días" en vez de por gasto.** El umbral correcto es gasto vs CPA, no tiempo.
- **Apagar el ad group entero cuando solo un creativo está muerto.** Resetea aprendizaje y mata a los buenos con el malo. Mata a nivel creativo.
- **"Resetear la cuenta" porque va mal.** No existe ese botón mágico (ver 76). Lo que existe es matar muertos y meter creativo fresco.
- **Matar sin verificar el tracking.** Un Pixel caído te hace apagar ads que sí convertían. Revisa medición primero (ver 05, 06).
- **Matar sin reponer.** Te quedas sin creativos para pautar. Matar y producir van juntos (ver 39).
- **No matar nunca por culpa al video que produjiste.** El costo de producir ya se gastó; seguir alimentando un muerto es tirar más plata. Mata frío.

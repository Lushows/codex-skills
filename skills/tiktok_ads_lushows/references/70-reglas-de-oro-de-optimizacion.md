# 70 — Reglas de oro de optimización

Lee este módulo cuando una campaña ya está corriendo y te muere la mano por entrar a "arreglarla", cuando el CPA se mueve día a día y no sabes si actuar o esperar, o cuando alguien te dijo "optimizar es revisar todos los días". Este es el módulo que te frena la mano. La mayoría del dinero quemado en TikTok no se pierde por mal creativo — se pierde por **media buyers ansiosos que tocan demasiado pronto**. En TikTok eso duele más que en Meta, porque la varianza diaria es más alta y el algoritmo castiga más al impaciente. Frame que ordena todo: **TikTok es descubrimiento** — el algoritmo necesita tiempo y volumen para encontrar a quién le pega tu creativo, y cada vez que tú metes la mano lo obligas a empezar a buscar de nuevo.

## La disciplina de 3–7 días: la varianza de TikTok es ALTA

Esto es lo que casi nadie entiende viniendo de Meta: **TikTok tiene mucha más varianza diaria que Meta**. Un ad group puede gastar $200.000 COP sin una sola conversión un martes, y traerte 4 ventas el miércoles con el mismo creativo, mismo público, mismo presupuesto. No cambió nada — así es la entrega de TikTok. El For You reparte impresiones en oleadas, no parejo.

Si reaccionas al martes (apagas, bajas presupuesto, cambias puja), matas el miércoles antes de que llegue. Por eso la regla:

| Antigüedad del cambio/campaña | Qué puedes hacer |
|---|---|
| 0–3 días (fase de aprendizaje, ver 13) | **NADA.** Solo mirar. Ni presupuesto, ni puja, ni creativos, ni público. |
| 3–7 días | Leer señales tempranas (hook rate, thumbstop, CTR), pero aún NO juzgar por CPA. |
| 7+ días con datos | Recién ahí decides: escalar (72, 73), matar (71) o iterar creativo. |

La excepción única para actuar antes de 3 días: **gasto sin vida**. Si un ad gastó 2–3× tu CPA objetivo con **cero** conversiones, eso no es varianza, es un muerto — apágalo (ver 71). Pero eso es matar, no "optimizar".

¿Por qué TikTok varía más que Meta? Tres razones prácticas: (1) la entrega depende del enganche del creativo en cada impresión, no de un público fijo, así que oscila más; (2) Smart+ y la automatización (ver 12) exploran más al inicio antes de explotar lo que funciona; (3) los volúmenes de conversión de una pyme suelen ser bajos, y con pocos eventos cualquier día se ve extremo. La cura no es tocar — es **leer ventanas más anchas** (7 días) y exigir volumen antes de concluir.

## Tamaño del cambio: nunca resetees el aprendizaje

Cada cambio "grande" reinicia la fase de aprendizaje del algoritmo (ver 13) y te devuelve a la varianza alta y al CPA inflado de los primeros días. Lo que cuenta como grande:

| Cambio | ¿Resetea aprendizaje? | Regla |
|---|---|---|
| Subir/bajar presupuesto **>20–30%** de golpe | Sí | Hazlo en pasos de ≤20–30% (ver 72) |
| Cambiar el evento de optimización | Sí, fuerte | Solo si el evento estaba mal (ver 14) |
| Cambiar la puja / cost cap | Sí | Ajustes pequeños, espera 3 días (ver 74) |
| Editar el público (broad↔detallado) | Sí | Mejor crear ad group nuevo |
| Cambiar la ubicación/placement o la creatividad principal | Sí | Tratar como ad nuevo |
| Pausar y reactivar un ad group | Sí (a veces empieza de cero) | Evita el pausar-prender nervioso |
| **Agregar un creativo nuevo** al ad group | Casi no | ✅ Esta es la jugada segura (ver 73) |
| Apagar un creativo muerto | Mínimo | ✅ Seguro |

La conclusión operativa: **lo más seguro que puedes hacer para mejorar una campaña casi nunca es tocar settings — es meter creativo nuevo y apagar el que murió** (ver 73, el escalado horizontal de TikTok). Si la única herramienta que conoces es "bajar presupuesto cuando va mal", estás resolviendo un problema de creativo con una palanca de cuenta, y casi siempre empeora.

## Checklist de decisión: antes de tocar cualquier cosa

Pregúntate esto, en orden, antes de mover un dedo:

1. **¿La campaña/cambio tiene 3+ días?** Si no → no toques, espera.
2. **¿Estoy reaccionando a UN día malo?** Mira la ventana de 7 días, no la de hoy. La varianza engaña.
3. **¿Tengo suficientes conversiones para concluir?** Con 1–2 conversiones no hay estadística. Necesitas ~10+ para leer un CPA de verdad (ver 60).
4. **¿El cambio que voy a hacer resetea el aprendizaje?** Si sí, ¿vale la pena reiniciar la varianza alta? Casi nunca.
5. **¿Estoy tocando por miedo o por dato?** Si no puedes nombrar la métrica exacta que te preocupa, es miedo. No toques.
6. **¿El problema real es el creativo?** El ~80% de los problemas de CPA en TikTok son fatiga creativa (ver 39, 75), no settings. Antes de tocar la campaña, mira si el creativo se quemó (frequency arriba, hook rate cayendo).
7. **¿Mi medición está sana?** Si el evento del Pixel/Events API se cayó (ver 05, 06), el "CPA disparado" es falso y vas a romper una campaña sana persiguiendo un fantasma. Verifica que las conversiones que ves cuadren con las reales del negocio.

Si pasas el checklist y aún hay que actuar, haz **un solo cambio a la vez** y espera 3 días para leerlo. Cambiar tres cosas juntas = nunca sabes cuál funcionó.

## Tabla de decisión: qué hacer según lo que ves

| Lo que ves | Antigüedad | Acción correcta |
|---|---|---|
| CPA bueno, estable | 7+ días, 10+ conv | Escalar vertical +20–30% (ver 72) y meter creativo nuevo (ver 73) |
| CPA bueno hoy, ayer malo | <7 días | Esperar. Es varianza (ver 60) |
| CPA subiendo + frequency arriba | cualquiera | Fatiga: refrescar creativo (ver 39, 75), NO tocar settings |
| Gastó 2–3× CPA, 0 conversiones | cualquiera | Matar el creativo (ver 71) |
| Gastó <1× CPA, 0 conversiones | <7 días | Esperar, sigue siendo ruido |
| CPA estable pero alto para tu margen | 7+ días | No es campaña, es economía: revisa unit economics (`economist_lushows`) |
| Conversiones que ves no cuadran con ventas reales | cualquiera | Tracking roto (ver 05, 06), no toques la puja |

## El ritmo sano de revisión

No revises la cuenta cada hora — te vuelve ansioso y reactivo. Un ritmo realista para una pyme colombiana:

- **Diario (2 min):** ¿algo se rompió? (gasto en cero, ad rechazado, evento que dejó de disparar, tarjeta declinada). No optimizas, solo vigilas incendios.
- **Cada 3 días:** ¿hay un muerto claro que apagar (ver 71)? ¿un ganador que ya aguantó 3 días y puedo escalar (ver 72)?
- **Semanal:** decisiones de fondo — escalar, refrescar creativos, rotar ángulos (ver 38, 39), leer la tendencia real, planear el testing de la semana (ver 17).

Pon estos momentos en el calendario (ver 19) y respétalos. La disciplina no es revisar más — es revisar **en bloques fijos** y no tocar entre medio. Un media buyer que entra 10 veces al día toma 10 decisiones de miedo; uno que entra 3 veces a la semana toma 3 decisiones de dato.

Si todo esto suena a "no hagas nada", casi: en TikTok el 90% de la optimización es **producir creativo y matar muertos** (ver 39, 71, 73), no apretar botones. La paciencia no es pasividad — es darle al algoritmo el tiempo que necesita para hacer su trabajo de descubrimiento, mientras tú haces el tuyo: alimentar la fábrica de creativos.

## Errores comunes — blacklist

- **Tocar antes de 3 días.** La varianza de TikTok te hace creer que algo falla cuando solo es un día malo. Espera (ver 13).
- **Reaccionar a un solo día.** El martes muerto se compensa con el miércoles. Lee ventanas de 7 días, no de hoy.
- **Subir presupuesto >30% de un saque.** Resetea el aprendizaje y te devuelve al CPA caro del día uno (ver 72).
- **Cambiar 3 cosas a la vez.** Si mejora o empeora, no sabes por qué. Un cambio, espera, lee.
- **Pausar y reactivar por nervios.** Cada pausa puede reiniciar el aprendizaje. Si va a seguir, déjalo correr.
- **Confundir optimizar con apretar botones.** Optimizar en TikTok es sobre todo **meter creativo y matar muertos**, no tocar settings (ver 73).
- **Juzgar el CPA con 1–2 conversiones.** Eso no es un dato, es ruido. Espera volumen estadístico (ver 60).
- **No verificar el tracking antes de "arreglar".** Un evento caído infla el CPA falso; rompes una campaña sana persiguiendo un fantasma (ver 05, 06, 75).
- **Optimizar sin saber tu CPA objetivo.** Sin ese número (sale de tus márgenes, `economist_lushows`) no sabes si lo que ves es bueno o malo.

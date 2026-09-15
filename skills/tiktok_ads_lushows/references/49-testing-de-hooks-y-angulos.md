# 49 — Testing de hooks y ángulos

Lee este módulo cuando tienes varios videos y no sabes cuál escalar, o cuando "cambiaste todo a la vez" y ahora no entiendes qué fue lo que funcionó. El **testing** es probar variantes de forma ordenada para que los datos te digan qué gana — no tu corazonada. La trampa que arruina el 90% de los tests caseros: **cambiar varias cosas a la vez** (hook nuevo + ángulo nuevo + sonido nuevo) y no poder saber cuál de las tres movió el resultado. Eso se llama contaminar las variables, y te deja igual de ciego que antes, pero con la plata gastada.

Tres palabras clave de este módulo: **hook** (el gancho de los primeros 1-3s, ver 37), **ángulo** (el enfoque del mensaje — el dolor o deseo que atacas, ver 38), y **sonido** (la pista/audio, ver 46). Son las tres variables que más mueven el resultado en TikTok. Testear bien es aislar UNA a la vez y dejar que una métrica clara decida.

## Una variable a la vez (no contamines)

La regla de oro: **cambia una sola cosa entre variantes.** Si quieres saber qué hook gana, deja IGUAL el ángulo, el cuerpo del video y el sonido, y cambia SOLO los primeros 3 segundos.

| Qué testeas | Qué mantienes IGUAL | Qué cambias |
|---|---|---|
| **Hook** | Ángulo, cuerpo, sonido, oferta | Solo los primeros 1-3s (texto y/o frase de apertura) |
| **Ángulo** | Estructura, sonido | El enfoque/dolor que atacas (ver 38) — suele cambiar más del video |
| **Sonido** | Video idéntico | Solo la pista de audio (de la Commercial Music Library, ver 46) |

El testing de hooks es el más barato y rápido: el mismo video con 3 aperturas distintas te dice cuál engancha sin reproducir todo. Empieza por ahí.

## Qué métrica decide en cada nivel

No mires el CPA primero — mira la métrica del nivel que estás testeando. Si el problema está arriba (nadie ve), el CPA no te dice nada útil todavía.

| Nivel | Métrica que decide | Qué significa |
|---|---|---|
| **Hook** | **Hook rate / thumbstop** (% que ve los primeros 2-3s) | ¿El gancho detiene el scroll? Si es bajo, el hook falla |
| **Cuerpo / ángulo** | Retención (% que llega a la mitad / al final), CTR | ¿El mensaje retiene y da clic? |
| **Oferta / landing** | **CVR** (tasa de conversión) | ¿El que llegó, compra? Si no, revisa oferta (41) o congruencia (48) |
| **Resultado final** | **CPA** (costo por adquisición) / ROAS | El veredicto del dinero, pero solo confiable con volumen |

Lógica de diagnóstico: hook rate bajo → arregla el hook (ver 37). Hook rate bueno pero CTR bajo → arregla cuerpo/ángulo (ver 38). CTR bueno pero CVR bajo → arregla oferta (41) o congruencia ad→landing (48). Así sabes DÓNDE está el hueco en vez de cambiar todo a ciegas. El detalle de cada métrica está en 68 (creative analytics).

## Cómo montar el test sin contaminar

| Paso | Acción |
|---|---|
| 1. Hipótesis | "Creo que el hook de dolor 'no te cuadra la caja' engancha más que el de curiosidad." |
| 2. Variantes | 3-5 versiones que cambian SOLO esa variable |
| 3. Igualdad de condiciones | Mismo público, mismo presupuesto, misma ventana de tiempo — para que compitan parejo |
| 4. Volumen mínimo | Deja correr hasta que cada variante tenga datos suficientes (no decidas con 200 impresiones) |
| 5. Lee la métrica del nivel | Hook rate para hooks, no CPA todavía |
| 6. Decide y itera | Mata las perdedoras, quédate con la ganadora |

Paciencia con el presupuesto: matar una variante a las 3 horas con poquísimos datos es decidir con ruido, no con señal. Dale a cada una pista para mostrar de qué es capaz (presupuesto y aprendizaje, ver módulos de estructura/escala).

## Iterar SOBRE el ganador (no empezar de cero)

El testing no termina al encontrar al ganador — ahí empieza lo bueno. Toma la variante que ganó y haz **iteraciones** de ella: el mismo ángulo ganador con 3 hooks nuevos, el mismo hook ganador con 3 cuerpos. Así construyes sobre lo que ya funciona en vez de reinventar cada semana. El creativo se quema (ver 39), así que necesitas un flujo constante de iteraciones del ganador para mantener el rendimiento sin partir de cero.

Ejemplo de iteración (Calculadora Gastro): gana el ángulo "vender mucho ≠ ganar". Siguiente test: ese mismo ángulo con hooks distintos — (a) "Llenas el local y no te queda plata", (b) "El error que te hace trabajar gratis", (c) "POV: descubres por qué no ganas". Misma idea ganadora, nuevas puertas de entrada.

## Errores comunes — blacklist

- **Cambiar varias cosas a la vez.** Hook + ángulo + sonido juntos = no sabes qué funcionó. Fix: una variable por test.
- **Mirar el CPA antes que el hook rate.** Si nadie ve el video, el CPA no diagnostica nada. Fix: métrica del nivel que testeas.
- **Decidir con poquísimos datos.** Matar a las 3 horas con 200 impresiones. Fix: dale volumen mínimo a cada variante.
- **Públicos/presupuestos distintos entre variantes.** No compiten parejo. Fix: mismas condiciones para todas.
- **Empezar de cero cada semana.** Tiras el aprendizaje. Fix: itera sobre el ganador (nuevos hooks del mismo ángulo).
- **No tener hipótesis.** Probar al azar sin saber qué buscas. Fix: escribe la hipótesis antes (ver paso 1).
- **Confundir hook con ángulo.** Cambiar el dolor entero creyendo que pruebas el hook. Fix: hook = primeros 3s; ángulo = enfoque (ver 37, 38).

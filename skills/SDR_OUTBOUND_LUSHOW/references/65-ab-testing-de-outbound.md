# 65 — A/B testing de outbound

Outbound es un sistema medible, no una corazonada (ver `00`). El A/B testing (probar dos versiones —A y B— de un mismo elemento con grupos comparables para ver cuál rinde mejor) es cómo dejas de discutir "¿este asunto es mejor?" y **lo mides**. Bien hecho, cada semana tu máquina rinde un poco más; mal hecho, tomas decisiones sobre ruido estadístico y persigues fantasmas. Este módulo te da qué variar, en qué orden, con qué tamaño de muestra, y cómo leer el resultado sin engañarte.

## El principio: una variable a la vez, contra una métrica clara

La regla no negociable del A/B: **cambia UNA sola cosa entre A y B.** Si la versión B tiene otro asunto Y otro opener Y otro CTA, y gana, no sabes qué la hizo ganar — no aprendiste nada, tuviste suerte. Aísla la variable y sabrás exactamente qué mover en la próxima.

Y cada variable se mide contra la métrica que **ella** afecta:

| Qué pruebas | Métrica que mueve | Métrica que NO prueba |
|---|---|---|
| **Asunto (subject)** | Tasa de apertura (open rate) | No mide respuestas |
| **Opener / primera línea** | Tasa de respuesta | (lo lee tras abrir) |
| **Cuerpo / ángulo / oferta** | Tasa de respuesta positiva | — |
| **CTA (llamada a la acción)** | Tasa de respuesta / reuniones agendadas | — |
| **Cadencia (nº de toques, canales)** | Reuniones por 100 contactos | — |

Nota 2026 sobre open rate: con la privacidad de Apple Mail y píxeles bloqueados, el open rate está **inflado y poco confiable**. Úsalo como señal gruesa para asuntos, pero la métrica que de verdad importa y sobre la que debes optimizar es **reply rate positivo → reuniones agendadas**. El dinero está en reuniones, no en aperturas.

## Qué variar y en qué orden (mayor impacto primero)

Prueba de arriba hacia abajo — lo de arriba mueve más la aguja:

1. **La lista / segmento** (ver `20`). El factor #1. El mismo correo a otro ICP cambia todo. Antes de tocar el copy, pregúntate si el problema es a quién le escribes.
2. **El ángulo / oferta** (el problema que atacas, la promesa). Gran palanca.
3. **El opener / primera línea** (ver `52`). Personalización vs. no; ángulo de dolor vs. de resultado.
4. **El CTA** (ver `53`). "¿15 min esta semana?" vs. "¿tiene sentido que te muestre?" vs. pregunta de interés suave.
5. **El asunto** (ver `51`). Corto vs. pregunta vs. con nombre de empresa.
6. **La cadencia** (ver `60`): 5 toques vs. 8; con WhatsApp vs. sin.

## Tamaño de muestra: cuántos correos por variante

Aquí muere la mayoría de los A/B de outbound: se declara ganador con 40 correos. Con reply rates de ~2–5 %, 40 correos dan 1–2 respuestas — puro azar. Referencia práctica:

| Métrica que mides | Tasa base típica | Muestra mínima por variante |
|---|---|---|
| Apertura | 30–50 % | ~200–300 |
| Respuesta | 5–10 % | ~400–600 |
| Respuesta positiva / reunión | 1–4 % | ~800–1.500 (o acumula varias semanas) |

Regla de bolsillo: necesitas juntar **al menos ~30–50 "eventos"** (respuestas, no envíos) por variante para que el resultado signifique algo. Si tu volumen es bajo, **no compares en una semana**: acumula la misma prueba durante 3–4 semanas hasta juntar la muestra. Correr un A/B con muestra chica es peor que no correrlo: te hace creer que aprendiste.

## Cómo leer el resultado sin engañarte

1. **¿La diferencia es real o es ruido?** B tuvo 4,1 % de respuesta y A 3,4 %. ¿B es mejor o es azar? Con muestras chicas, casi siempre es azar. Para saberlo se calcula la **significancia estadística** (la probabilidad de que la diferencia no sea casualidad; el estándar es 95 % de confianza). No lo hagas a ojo: pásalo por `Matematicas_lushows` o una calculadora de significancia A/B. Si no llega a 95 %, **no hay ganador todavía** — sigue acumulando o declara empate.
2. **Un ganador claro:** adopta B como nuevo estándar (tu "control") y lanza la siguiente prueba contra él. Así el sistema mejora en escalón.
3. **Empate:** quédate con el más simple/barato de ejecutar y prueba otra variable de más arriba en la lista.
4. **Documenta.** Lleva un registro: qué probaste, muestra, resultado, decisión. Sin bitácora repites pruebas y olvidas aprendizajes.

## Ejemplo real (asunto, cold email B2B LatAm)

```
Prueba: ASUNTO. Todo lo demás idéntico. Segmento: gerentes de compras, pymes manufactura.
  Variante A: "pregunta rápida"
  Variante B: "{empresa} + reducir costos de {insumo}"

Envío: 500 por variante (1.000 total), distribuido mar-jue 7:30-9:30 (ver 62).

Resultado tras 2 semanas:
  A: 210 aperturas (42%), 18 respuestas (3,6%), 6 positivas
  B: 275 aperturas (55%), 31 respuestas (6,2%), 11 positivas

Lectura: B gana en apertura y en respuesta. Diferencia en respuesta
(3,6% vs 6,2%) → verificar significancia con Matematicas_lushows.
Si pasa 95%: B es el nuevo control. Siguiente prueba: opener, contra B.
```

## Errores comunes (qué NO hacer)

- **Cambiar varias cosas a la vez.** No aprendes nada aunque "gane".
- **Muestra minúscula.** Declarar ganador con 40 correos es superstición, no data.
- **Optimizar el open rate** (inflado/poco fiable en 2026) en vez de reply positivo → reuniones.
- **No calcular significancia.** "Se ve mejor" no es un resultado. Ver `Matematicas_lushows`.
- **Probar el asunto antes que la lista.** Estás puliendo la manija de la puerta equivocada. Empieza por a quién le escribes.
- **No documentar.** Repites pruebas y pierdes el aprendizaje acumulado.

## Siguiente paso

Elige UNA variable de la lista de prioridad (empieza por segmento/ángulo), corre la prueba con muestra suficiente en tu plataforma (Instantly, Smartlead, Lemlist — ver `60`), y valida el ganador con `Matematicas_lushows`. Para decidir cuánto puedes personalizar sin morir de volumen —lo que a su vez define cuántos correos por variante juntas— ve a `66`.

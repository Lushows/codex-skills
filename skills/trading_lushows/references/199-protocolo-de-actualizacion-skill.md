# 199 — Protocolo de actualización de esta skill

Esta skill es el cerebro externo del AGENTE TRADING. Solo sirve si dice la VERDAD ACTUAL del
proyecto: una skill desactualizada es peor que ninguna, porque da confianza sobre datos viejos.
Este módulo define cómo se mantiene viva.

## Al cerrar cada sesión de trabajo (el ritual, 5-10 min)

1. **Actualizar los módulos de estado** — los que cargan cifras vivas:
   - `01` (estado del proyecto): trades, PF, DD, uptime, versión desplegada.
   - `10` (lecciones): si la sesión produjo una lección, entra CON FECHA.
   - `11` (bitácora/decisiones): qué se decidió y por qué.
2. **Fechar todo dato volátil.** Nunca escribir "el PF es 0.89" a secas: escribir
   "PF 0.89 (al 6-jul-2026)". El lector del futuro debe saber qué tan vieja es cada cifra.
3. **Revisar el índice del SKILL.md**: si se creó, renombró o re-alcanzó un módulo, el índice
   se actualiza en la MISMA sesión. Un índice roto = módulos huérfanos que nadie vuelve a leer.

## Reglas de escritura (no negociables)

- **Nunca borrar historia.** Lo superado se marca, no se elimina:
  `~~decisión X~~ (reemplazada el 15-jul-2026 por Y, ver módulo Z)`. La historia de errores y
  cambios ES el journal del sistema a nivel meta — borrarla repite el error #10 del `19`.
- **Lecciones con formato fijo**: fecha + qué pasó + evidencia + regla que se deriva. Ejemplo
  del proyecto: "jun-2026: 0/3 ganados sobre $1.788 vs 4/4 bajo $1.760 → candidato a filtro
  anti-extensión". Sin evidencia no es lección, es opinión.
- **Cifras de mercado: siempre "verificar al día".** Precios, comisiones de Binance, normativa,
  disponibilidad de testnet — todo eso caduca. La skill guarda el MÉTODO y la historia propia;
  los datos externos se verifican al usarse.
- **Un módulo, un tema.** Si una actualización no cabe en ningún módulo, quizá falta un módulo
  nuevo — pero antes revisar que no viva ya en otra skill del ecosistema (`196`,
  regla anti-duplicación).
- **Tono estable**: español, para no técnicos, riesgo primero, cero humo. Un módulo nuevo debe
  sonar como los demás (calcar `00`, `02`, `08`).

## Cuándo tocar los módulos de fondo (no solo los de estado)

| Evento | Módulos a revisar |
|---|---|
| Veredicto del 22-ago (GO/PIVOT/KILL) | `08`, `190`, `01` — el mismo día |
| Cambio de estrategia/prompt validado | `18` (flujo), `195` (registro del experimento) |
| Nueva regla de riesgo | `02`, `14` |
| Inicio de fase 8 | `191` se convierte en checklist viva (marcar tareas) |
| Apagado o pivote mayor | `197` (autopsia), `190`, `198` |

## Control de calidad periódico (1 vez por trimestre)

- Leer `01` y preguntar: ¿un desconocido entendería el estado real del proyecto solo con esto?
- Buscar contradicciones entre módulos (el enemigo silencioso: dos módulos afirmando umbrales
  distintos). La fuente única de cada número es UN módulo; los demás lo referencian.
- Verificar que las lecciones nuevas del journal (`15`) llegaron a `10` y no se quedaron
  solo en la cabeza de la sesión que las descubrió.

## Cómo aplica al AGENTE TRADING

- Este protocolo es el equivalente, a nivel skill, del journal del bot: el bot registra trades
  automáticamente; la skill registra DECISIONES manualmente. Los dos juntos son la memoria
  completa del proyecto.
- Quien trabaje el proyecto en una sesión (Claude incluido) termina la sesión ejecutando el
  ritual de arriba. Sin excepción "porque fue un cambio chiquito" — los cambios chiquitos sin
  registrar son cómo las skills mueren.

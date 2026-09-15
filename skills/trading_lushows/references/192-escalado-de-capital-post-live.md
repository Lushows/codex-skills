# 192 — Escalado de capital post-live

**Escalar** = subir el capital que opera el bot. Es la decisión más peligrosa del proyecto,
porque llega justo cuando la confianza está más alta (todo va bien) y la evidencia sigue siendo
más corta de lo que se siente. Regla madre: **el capital sube con evidencia, nunca con emoción.**

## El principio: escalar es un go-live nuevo

Cada subida de capital se trata como el 22-ago: umbrales definidos ANTES, sin negociar después.
Lo que cambia con más plata no es el sistema — es la psicología de Luis (ver una pérdida de $50
duele distinto que una de $5) y, mucho más adelante, la ejecución (slippage con tamaño grande;
irrelevante en estos montos, verificar al día si algún día se llega a tamaños serios).

## Hitos de evidencia para cada escalón

| Escalón | Capital (referencia) | Requisito para subir |
|---|---|---|
| Live inicial | $200-500 | GO del 22-ago + fase 8 completa + mes híbrido limpio (`08`, `191`) |
| Escalón 2 | ~2× el anterior | **3 meses live rentable**: PF >1.3 en live, DD <15%, sin violaciones de protocolo |
| Escalón 3+ | ~2× el anterior, cada vez | 3 meses MÁS en el nuevo tamaño con los mismos umbrales |

**Escalado geométrico prudente** = multiplicar por un factor fijo y moderado (~2×), no saltar
"porque sobra plata". De $300 → $600 → $1.200 → $2.400: cada escalón re-valida que el sistema
(y Luis) aguantan el nuevo tamaño. Nunca más de un escalón por trimestre.

## Por qué 3 meses y no 1

Un mes bueno son quizá 6-10 trades: anécdota (ver `17`). Tres meses dan ~20-30 trades live y
atraviesan al menos un cambio de humor del mercado. Además: el desempeño LIVE puede ser peor que
el paper (slippage real, fills parciales) — hay que confirmar que el edge sobrevive a la realidad
antes de amplificarlo.

## Cuándo retirar ganancias

- **Regla simple**: al cerrar cada trimestre rentable, retirar el 50% de la ganancia y dejar el
  otro 50% componiendo. El retiro hace la ganancia REAL (de números en pantalla a plata en la
  cuenta) y baja la presión psicológica.
- **Hito especial**: cuando las ganancias acumuladas retiradas igualen el capital aportado,
  el bot "juega con plata de la casa" — el riesgo del proyecto sobre el bolsillo de Luis es cero.
- Retirar NO es desconfiar del sistema: es gestión. Los traders que nunca retiran devuelven
  todo en el drawdown grande que siempre llega.

## Escalado en reversa (tan importante como subir)

- Drawdown >8% en live → tamaño a la mitad hasta recuperar pico (regla del `02`).
- Un trimestre con PF <1.0 → bajar un escalón completo de capital y revisar (`197` si se repite).
- Violación de protocolo (trade fuera de reglas) → congelar escalado hasta entender la causa.

## Cómo aplica al AGENTE TRADING

- Hoy esto es futuro: primero PF >1.3 en paper, luego fase 8, luego mes híbrido. Este módulo
  existe para que la decisión ya esté escrita ANTES de la euforia del primer trimestre verde.
- El capital es plata de Luis: cuánto puede aportar sin comprometer nada (regla de la quiebra)
  → `economist_lushows`. Impuestos sobre ganancias de cripto en Colombia → `contador_lushows`.
- Verificación de los números de cada escalón (PF live, DD, proyecciones) → `Matematicas_lushows`.

# 06 — Filosofía Druckenmiller y la Wisdom Library

## Los principios Druckenmiller (system prompt del skill de convicción)

1. **Apuesta grande solo con convicción alta (≥7/10).** Lo demás es ruido caro.
2. **Preserva capital antes que buscar ganancia.** En la duda, NO operes.
3. **El macro/régimen primero, el activo después.** Contra el régimen no hay setup bueno.
4. **Una mala racha pide REDUCIR tamaño**, jamás promediar abajo.
5. **El historial importa**: si un setup similar falló 3 veces, evita el cuarto.

El bot lo implementa como score de convicción 1-10 → BUY solo si ≥6 y el régimen respalda;
auto-ejecución solo si ≥8 (`AUTO_EXECUTE_THRESHOLD`).

## La Wisdom Library (wisdomLibrary.js — 6 traders, se inyecta según contexto)

| Trader | Su regla núcleo | Cuándo la inyecta el bot |
|---|---|---|
| **Druckenmiller** | Convicción concentrada + macro primero | Siempre (es la filosofía base) |
| **Jesse Livermore** | "El dinero grande está en la espera, no en el movimiento" | Regímenes ranging / señales débiles |
| **Paul Tudor Jones** | "Defensa 5:1 — no promediar perdedores, R:R mínimo" | Cuando el R:R propuesto es débil |
| **Ed Seykota** | "Sigue las reglas sin excepción; corta pérdidas ya" | Rachas perdedoras |
| **Bruce Kovner** | "Sizing es el 90%; los novatos apuestan 5× lo debido" | Sizing con volatilidad alta |
| **Ray Dalio** | "El dolor + reflexión = progreso; diversifica el riesgo" | Meta-análisis y drawdowns |

La librería selecciona qué sabiduría inyectar según régimen, convicción, R:R, racha y volatilidad —
no mete a los 6 en cada prompt (costo y foco).

## Cómo se traduce a decisiones del sistema

- Convicción alta escasa > convicción media frecuente. Pocos trades buenos le ganan a muchos tibios
  (verificado: el umbral 8 produjo 10 trades en 6 semanas con drawdown de solo 1.8%).
- La espera ES una posición. Semanas sin operar en régimen malo no son fallo del bot: son Livermore.

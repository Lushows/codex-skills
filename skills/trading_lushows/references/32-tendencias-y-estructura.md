# 32 — Tendencias y estructura de mercado

La **estructura de mercado** es la forma más limpia de leer tendencia: sin indicadores, solo
mirando la secuencia de máximos y mínimos que va dejando el precio.

## El vocabulario (con traducción)

| Término | En español | Qué significa |
|---|---|---|
| **Higher High (HH)** | Máximo más alto | El precio superó el pico anterior |
| **Higher Low (HL)** | Mínimo más alto | El retroceso no llegó tan abajo como el anterior |
| **Lower High (LH)** | Máximo más bajo | El rebote no alcanzó el pico anterior |
| **Lower Low (LL)** | Mínimo más bajo | El precio perforó el piso anterior |

## Las tres estructuras posibles

```
Alcista:   HL → HH → HL → HH ...   (escalera subiendo)
Bajista:   LH → LL → LH → LL ...   (escalera bajando)
Rango:     máximos y mínimos al mismo nivel, sin escalera
```

Mientras la secuencia se mantiene, la tendencia está **viva**. No hace falta adivinar techos:
la propia estructura avisa cuando se rompe.

## Cambio de carácter y ruptura de estructura

- **Ruptura de estructura (BOS, break of structure)**: en tendencia alcista, el precio hace un
  nuevo HH → la tendencia se CONFIRMA a favor. Es continuación, no cambio.
- **Cambio de carácter (CHoCH, change of character)**: la primera señal en contra. En tendencia
  alcista: el precio pierde el último HL (hace un LL). No garantiza reversión, pero la tendencia
  deja de ser confiable — es el momento de bajar exposición, no de promediar.
- Honestidad: estos términos vienen de la escuela "Smart Money Concepts", que envuelve ideas
  viejas (Dow, 1900) en jerga nueva. La idea es sólida; el marketing alrededor, no tanto.

## Errores típicos leyendo estructura

- Marcar cada micro-oscilación como HH/HL: en 1h hay ruido; los puntos válidos son giros con
  varias velas de desarrollo, no cada mecha.
- Declarar reversión al primer LL: puede ser una sacudida de stops. La reversión se confirma
  cuando además aparece un LH (el rebote falla).
- Ignorar el marco mayor: un "cambio de tendencia" en 1h puede ser un simple retroceso en 4h (`38`).

## Cómo aplica al AGENTE TRADING

- La estructura es el complemento natural del régimen (`03`): `trending-up` debería coincidir con
  HH/HL visibles en las velas. Si Haiku dice trending-up pero la estructura muestra LH/LL
  recientes, la convicción debe bajar — desacuerdo entre capas es señal de duda, no de fuerza.
- El mejor punto de entrada de un LONG en tendencia es el **HL** (retroceso hacia soporte/SMA20),
  no el HH recién hecho. Comprar el HH es literalmente el error FOMO de `10`: 3/3 pérdidas
  entrando a >3% de la SMA20, es decir, comprando la escalera en el escalón más alto.
- Regla derivada para el prompt: "¿esta entrada compra un retroceso (HL) o persigue un máximo
  (HH extendido)?" — la primera suma convicción, la segunda la resta.

# 137 — Datos de derivados: la radiografía del sentimiento profesional

> Los derivados (futuros y opciones) son donde opera el dinero institucional. Sus precios revelan
> qué espera y qué teme el mercado profesional — sin encuestas, con plata real.

## Los tres datos clave

### 1. Basis (base)
La diferencia entre el precio del futuro con vencimiento y el precio spot.
- **Basis positivo (contango)**: el futuro cotiza más caro que el spot → optimismo, demanda de
  exposición alcista. Un basis anualizado muy alto = euforia apalancada.
- **Basis negativo (backwardation)**: el futuro más barato que el spot → miedo, demanda de
  cobertura. Históricamente aparece cerca de pánicos.

### 2. Term structure (estructura temporal)
La curva de basis a distintos vencimientos (1 mes, 3 meses, 6 meses). Su forma dice si el
optimismo/pesimismo es de corto plazo o estructural. Una curva que se invierte de golpe suele
acompañar eventos de estrés.

### 3. Put/Call y skew (opciones)
- **Put** = seguro contra caídas; **Call** = apuesta a subidas.
- **Ratio put/call**: cuánta protección se compra vs cuánta apuesta alcista.
- **Skew**: si las puts están más caras que las calls equivalentes, el mercado paga más por miedo
  que por codicia. Skew extremo hacia puts = pánico (a veces, señal contraria en pisos).

## Lectura honesta

| Fortaleza | Límite |
|---|---|
| Dinero real, no encuestas de sentimiento | Indicadores de **condición**, no de timing |
| Anticipa estrés mejor que el precio solo | Los extremos pueden extenderse semanas |
| Público y en gran parte gratis (verificar fuentes al día) | Requiere comparar contra su propia historia, no umbrales fijos |

Como todo sentimiento: sirve en los **extremos** y es ruido en el medio.

## Cómo aplica al AGENTE TRADING

- El bot no consume datos de derivados hoy. Junto con funding/OI (módulo 135), son los candidatos
  más sensatos para enriquecer el **análisis de régimen** de Claude en el futuro: una línea tipo
  "basis elevado, skew cargado a calls → euforia" ayuda a modular la convicción.
- Prioridad: **después** del backtesting. Añadir inputs antes de validar el sistema base es
  decorar una casa sin cimientos.
- Regla si se integra: los derivados ajustan convicción (contexto), nunca disparan trades solos.

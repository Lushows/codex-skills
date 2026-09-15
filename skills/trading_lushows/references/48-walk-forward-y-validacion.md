# 48 — Walk-forward y validación honesta

Un backtest bonito (ver `46`) puede ser overfitting disfrazado (ver `47`). La única defensa
real es probar la estrategia sobre **datos que nunca vio durante el diseño**. De eso se trata
la validación.

## In-sample vs out-of-sample (los dos términos clave)

| Término | En cristiano | Para qué sirve |
|---|---|---|
| **In-sample** | Los datos que usaste para DISEÑAR y ajustar las reglas | Construir la estrategia |
| **Out-of-sample** | Datos que la estrategia NUNCA vio mientras la diseñabas | Saber si es real o memorizada |

La analogía del examen: in-sample es estudiar con las preguntas del año pasado; out-of-sample
es el examen nuevo. Si solo apruebas el examen que ya conocías, no aprendiste — memorizaste.
**El resultado in-sample no cuenta como evidencia. Solo el out-of-sample cuenta.**

## Walk-forward en simple

En vez de dividir los datos una sola vez, el walk-forward repite el ciclo avanzando en el tiempo:

```
[ diseño: ene-jun ] → [ prueba: jul ]      ← las reglas se fijan ANTES de ver julio
      [ diseño: feb-jul ] → [ prueba: ago ]
            [ diseño: mar-ago ] → [ prueba: sep ]
```

Se diseña con una ventana, se prueba con el tramo siguiente (sin tocar nada), se avanza y se
repite. El resultado que importa es la **suma de todos los tramos de prueba**: eso simula cómo
habría sido operar en vivo, ajustando solo con el pasado disponible en cada momento.

Qué mirar: si la estrategia gana in-sample pero pierde consistentemente en los tramos de
prueba, está overfitteada. Si gana en ambos (aunque menos out-of-sample — eso es normal),
hay algo real.

## Reglas de higiene de la validación

- **Out-of-sample se usa UNA vez.** Si pruebas, no te gusta, ajustas y vuelves a probar sobre
  los mismos datos, ya los contaminaste: se volvieron in-sample con pasos extra.
- Fijar TODO antes de la prueba: reglas, parámetros y métricas de éxito. "Ya veré qué medir"
  es la puerta trasera del autoengaño.
- La degradación es esperable: una estrategia honesta rinde peor out-of-sample que in-sample.
  Sospecha si rinde IGUAL de espectacular — o peor, mejor.

## El paper trading como out-of-sample vivo

El paper trading es la forma más pura de out-of-sample: datos que **no existían** cuando se
diseñó el sistema, imposibles de contaminar mirando el futuro. Cada trade de paper es un dato
de validación limpio. Su costo es el tiempo: a ritmo de swing en 1h, juntar 30-50 trades toma
meses. Por eso el orden sano es: backtest (muestra grande, barata, imperfecta) → paper
(muestra chica, lenta, limpia) → live chico. Cada etapa valida a la anterior.

## Cómo aplica al AGENTE TRADING

- Los 10 trades con PF 0.89 son exactamente eso: **out-of-sample vivo en curso**. No es un
  veredicto (muestra mínima ~30 trades), es el examen a medio presentar. PF 0.89 con 10 trades
  no dice "el sistema pierde"; dice "aún no hay evidencia de edge".
- La regla anti-FOMO se diseñó mirando los trades pasados → esos 3 trades son ahora in-sample
  para esa regla. Su validación real es el paper de aquí en adelante y el backtest sobre velas
  que no participaron en la lección.
- Disciplina para el go-live (22-ago-2026): congelar las reglas con anticipación y dejar que
  las últimas semanas de paper sean out-of-sample puro del sistema final. Si se cambian reglas
  la víspera, el go-live arranca sin validación.
- Métricas de cada tramo (PF, expectancy, rachas) → calcular en código con `Matematicas_lushows`.

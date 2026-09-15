# 144 — Walk-forward en la práctica

> El **walk-forward** es el out-of-sample llevado a método: en vez de separar los datos una vez,
> se repite el ciclo "ajustar en una ventana → validar en la siguiente" avanzando en el tiempo.
> Simula lo que harías en la vida real: operar siempre sobre futuro no visto.

## El mecanismo

```
[---- ajuste (in-sample) ----][- validación -]
        [---- ajuste ----][- validación -]
                [---- ajuste ----][- validación -]   → avanza la ventana
```

1. Ajustar parámetros solo con la ventana de ajuste.
2. Correr esos parámetros congelados en la ventana de validación siguiente.
3. Deslizar todo hacia adelante y repetir.
4. El **resultado real** del sistema = la concatenación de todas las ventanas de validación.

Lo que mide de más que un backtest simple: no solo "¿funciona la regla?", sino **"¿sobrevive el
proceso de ajustarla periódicamente?"** — que es lo que harás en vivo.

## Números concretos con velas 1h

Con velas de 1 hora: 1 mes ≈ 720 velas, 1 año ≈ 8.760 velas.

| Parámetro | Guía práctica |
|---|---|
| Ventana de ajuste | 4-6 meses de velas 1h (≈ 3.000-4.400 velas) — suficiente para varios mini-regímenes |
| Ventana de validación | 1-2 meses (≈ 720-1.440 velas) |
| Proporción típica | Ajuste : validación entre 3:1 y 4:1 |
| Paso | Igual a la ventana de validación (sin solapamiento de validaciones) |
| Mínimo total | ≥ 12-18 meses de historia para tener 4+ ciclos; menos que eso, el walk-forward es decorativo |

Estas son guías de artesanía, no leyes — lo innegociable es que la validación nunca toque datos
usados en su propio ajuste.

## Criterio de robustez (cómo leer el resultado)

- **Pasa**: rentable (o cerca) en la **mayoría** de ventanas de validación, sin depender de una
  sola ventana heroica; parámetros elegidos en cada ciclo razonablemente estables entre ciclos.
- **Falla**: gana solo en 1-2 ventanas que coinciden con el gran bull run; o los parámetros
  óptimos saltan violentamente de ciclo en ciclo (señal de que se ajusta ruido, módulo 143).
- El PF del walk-forward será menor que el del backtest simple. **Eso es lo normal y lo honesto**
  (módulo 149).

## Cómo aplica al AGENTE TRADING

- Aplica a la **capa mecánica** del backtest planeado (reglas técnicas, stops, filtro de régimen)
  sobre las velas 1h de `candlesStore` — la capa de Claude no se barre por parámetros.
- Primer paso práctico: auditar **cuánta historia continua** hay guardada por par (módulo 139).
  Si hay menos de ~12 meses, completar el histórico vía el mirror REST antes de walk-forward.
- Ejecución de los cálculos: rutear a `Matematicas_lushows` — cifras verificadas en código, nunca
  a ojo.

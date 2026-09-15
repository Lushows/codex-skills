# 114 — Funding rate: qué es y qué estrategias existen

## Qué es el funding

Los **perpetuos** (perps) son futuros sin fecha de vencimiento — el derivado más operado de
cripto. Para que su precio no se despegue del precio spot (el real, de contado), existe el
**funding**: un pago periódico (típicamente cada 8 horas) entre traders.

```
Perp por ENCIMA del spot → funding positivo → los LONG pagan a los SHORT
Perp por DEBAJO del spot → funding negativo → los SHORT pagan a los LONG
```

Es un termostato: si demasiada gente está long, mantenerse long se vuelve caro, y eso
empuja el precio de vuelta hacia el spot.

## El funding como señal de sentimiento

El funding es una encuesta pagada con plata real: dice hacia dónde está cargado el mercado.

| Lectura | Interpretación | Cuidado |
|---|---|---|
| Funding muy positivo sostenido | Euforia long, mercado apalancado hacia arriba | Terreno fértil para caídas violentas (long squeeze) |
| Funding negativo sostenido | Pesimismo extremo | Históricamente ha coincidido con zonas de piso — pero no es reloj |
| Funding neutro | Sin apalancamiento cargado | El precio se mueve más por spot que por derivados |

Es señal **contrarian** en extremos: cuando todos pagan por estar long, ¿quién falta por
comprar? Verificar niveles al día — qué cuenta como "extremo" cambia por época y activo.

## Estrategias de cosecha de funding (funding harvesting)

La idea: si los long pagan a los short, ponerse short en el perp y long en spot por el mismo
monto — **delta neutral** (las dos posiciones se cancelan: no importa si el precio sube o
baja) — y cobrar el funding como "renta". Es la prima hermana del basis trade (ver `115`).

**Los riesgos, que el humo siempre omite:**

- **El funding cambia de signo.** La "renta" puede volverse costo de un día para otro.
- **Riesgo de liquidación**: la pata short usa margen; una subida violenta puede liquidarla
  antes de poder rebalancear, dejando la posición coja.
- **Fees y ejecución**: entrar y salir de dos posiciones cuesta 4 operaciones; con funding
  flaco, los fees se comen la renta.
- **Riesgo de exchange**: las dos patas viven en plataformas que pueden fallar o congelar
  retiros (lección FTX 2022).

Rendimiento realista: modesto y variable. Quien promete "renta fija del 30% sin riesgo con
funding" está vendiendo humo o escondiendo el riesgo de liquidación.

## Cómo aplica al AGENTE TRADING

- El bot es **spot only**: no opera perpetuos, no paga ni cobra funding. Estas estrategias
  quedan fuera de su cancha por diseño.
- Lo aprovechable HOY es el funding como **dato de contexto**: un funding extremo positivo
  en ETH es bandera amarilla para la convicción de un LONG (mercado sobrecargado); un funding
  muy negativo en `trending-up` puede reforzar la tesis. Es un candidato razonable a input
  del análisis — como sentimiento, nunca como señal única.

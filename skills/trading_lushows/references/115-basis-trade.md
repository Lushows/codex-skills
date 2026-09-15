# 115 — Basis trade (cash and carry)

## Qué es la base

La **base** (basis) es la diferencia entre el precio de un futuro con vencimiento y el precio
spot del mismo activo:

```
base = precio del futuro − precio spot
```

Cuando el futuro cotiza por encima del spot se dice que el mercado está en **contango**
(lo normal en cripto alcista: la gente paga extra por exposición futura apalancada). Cuando
cotiza por debajo, **backwardation** (típico de pánico).

## El trade: cash and carry

La observación clave: al vencimiento, el futuro y el spot **convergen** al mismo precio,
sí o sí. Entonces:

1. Comprar el activo en spot (long).
2. Vender el futuro con vencimiento (short) por el mismo monto.
3. Esperar al vencimiento: la base se cierra y esa diferencia es la ganancia, sin importar
   si el precio subió o bajó (posición **delta neutral**: las patas se cancelan).

Es "cosechar" la prima que pagan los apalancados optimistas. En mercados alcistas fuertes,
la base anualizada de BTC ha llegado a niveles de dos dígitos (verificar al día — en mercados
tranquilos puede ser mísera y no pagar ni los fees).

## Por qué NO es renta gratis

| Riesgo | Qué puede pasar |
|---|---|
| **Margen de la pata short** | Si el precio sube fuerte, el short del futuro pide más garantía. Sin fondos para el margin call → liquidación → la "posición neutral" queda coja y expuesta |
| **Contango que colapsa antes de tiempo** | Si sales antes del vencimiento, la base pudo moverse en contra: pérdida realizada en un trade "sin riesgo" |
| **Riesgo de exchange** | Las dos patas viven en custodios. Gran parte del basis trade de 2021-22 murió con FTX, no con el precio |
| **Costo de oportunidad** | Capital amarrado meses ganando la base mientras quizá el spot subía mucho más |
| **Fees** | 4 operaciones (entrar y salir de dos patas) contra una base a veces flaca |

Es una estrategia legítima — la usan fondos institucionales con gestión de margen
profesional. Para retail, el punto frágil es siempre el mismo: **sobrevivir el margin call**
de la pata short durante un rally violento.

## Basis vs cosecha de funding

Misma familia (delta neutral cobrando primas de apalancados). El basis usa futuros con
vencimiento (convergencia garantizada, renta conocida al entrar); el funding usa perpetuos
(renta variable que puede cambiar de signo, ver `114`).

## Cómo aplica al AGENTE TRADING

- El bot no lo opera: es spot only, sin derivados, y el basis exige gestión de margen
  activa 24/7 — otro deporte.
- Valor como **contexto**: una base anualizada inflada indica euforia apalancada (precaución
  en LONGs); backwardation indica pánico (los pisos suelen gestarse ahí). Misma familia de
  señal de sentimiento que el funding.
- Si algún día se busca "renta" sobre capital ocioso del bot, esta es la referencia honesta
  para evaluar propuestas: si alguien promete más que la base sin explicar el riesgo de
  margen, es humo.

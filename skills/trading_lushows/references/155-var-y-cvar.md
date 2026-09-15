# 155 — VaR y CVaR

> Los cálculos de ejemplo se verifican ejecutándolos con `Matematicas_lushows`.

## Value at Risk (VaR) en simple

El **VaR al 95%** responde: "en el 95% de los días, mi pérdida no pasará de X". Es una raya en
la arena: separa los días normales-malos de los días extremos.

```
VaR 95% diario = $30  ⟺  "solo 1 de cada 20 días perderé más de $30"
```

Lo que el VaR **NO** dice: cuánto pierdes en ese 1 de cada 20. Puede ser $31 o $300 — el VaR es
ciego más allá de su raya. Esa es su crítica clásica.

## CVaR (Expected Shortfall): el complemento honesto

El **CVaR al 95%** responde la pregunta que el VaR esquiva: "cuando caigo en ese 5% peor,
¿cuánto pierdo EN PROMEDIO?". Siempre es mayor o igual que el VaR, y en distribuciones de colas
gordas (cripto, módulo 152) es **bastante** mayor.

| Métrica | Pregunta que responde | Debilidad |
|---|---|---|
| VaR 95% | ¿Cuál es mi pérdida en un día malo "normal"? | Ignora qué tan feo es el 5% extremo |
| CVaR 95% | Cuando llega el día extremo, ¿cuánto duele en promedio? | Necesita más datos para estimarse bien |

## Cómo se calcula (método histórico, el más honesto con pocos datos)

1. Tomar los retornos diarios del portafolio (la curva de equity, día a día).
2. Ordenarlos de peor a mejor.
3. VaR 95% = el retorno en el percentil 5 (el 5º peor de 100 días).
4. CVaR 95% = el promedio de los que quedaron por debajo de esa raya.

Con pocos datos, el VaR paramétrico "normal" (media ± 1.65σ) subestima el riesgo cripto —
preferir el histórico o simulación, y ejecutarlo con `Matematicas_lushows`.

## Aplicado al portafolio del bot (números ilustrativos)

Capital $1.000, máximo 2 posiciones con riesgo 1.5% cada una:

- Pérdida "de diseño" de un día donde ambos stops saltan: ~$30 (3%). Esa es una cota razonable
  del VaR diario mientras las posiciones respeten los stops.
- El CVaR real sería peor: gaps y slippage extremo en un flash crash pueden llevar la pérdida
  de un día a 4-5% aunque los stops digan 3%.
- Con la curva de equity real (`/api/equity`) se puede calcular el VaR/CVaR histórico exacto —
  con 44 días de datos ya es un primer estimado, aunque flaco (pocos días malos observados).

## Cómo aplica al AGENTE TRADING

- La regla "máximo 2 posiciones × 1.5%" ES un control de VaR de diseño: acota el día malo normal
  a ~3% del capital.
- Al reportar riesgo del bot, citar ambos: "VaR de diseño ~3%/día; CVaR real mayor por colas
  gordas". Nunca vender el VaR como pérdida máxima posible.
- Ejecutar el VaR/CVaR histórico sobre `/api/equity` con `Matematicas_lushows` en cada revisión
  mensual, y compararlo contra el de diseño: si el histórico lo supera, algo no está respetando
  los límites.

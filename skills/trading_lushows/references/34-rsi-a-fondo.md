# 34 — RSI a fondo

El **RSI** (Relative Strength Index, índice de fuerza relativa) mide la **velocidad** del
movimiento reciente en una escala de 0 a 100: compara cuánto subieron las velas que subieron
contra cuánto bajaron las que bajaron, en las últimas N velas (el bot usa 14).

## Qué mide de verdad (y qué no)

- Mide: si el movimiento reciente fue mayormente alcista (RSI alto) o bajista (RSI bajo), y
  con qué intensidad. Es un velocímetro del precio.
- NO mide: "caro" o "barato". Un RSI de 75 no significa que el activo esté caro; significa que
  subió rápido últimamente. Nada más.

## Sobrecompra / sobreventa — y su trampa

| Lectura clásica | La trampa |
|---|---|
| RSI > 70 = "sobrecomprado, va a caer" | En tendencia alcista fuerte el RSI **vive** sobre 70 durante días. Vender por eso es pelear contra la tendencia |
| RSI < 30 = "sobrevendido, va a rebotar" | En desplome, el RSI se queda clavado bajo 30 mientras el precio sigue cayendo ("el cuchillo que cae") |

La lectura honesta depende del régimen (`03`):
- **En rango**: 70/30 funcionan razonablemente como extremos donde el precio suele girar.
- **En tendencia**: sobrecompra = fuerza, no techo. El dato útil pasa a ser el retroceso del RSI
  hacia 40-50 sin perder ese nivel (el "reset" que acompaña al HL de `32`).

## Divergencias

Una **divergencia bajista**: el precio hace un máximo más alto, pero el RSI hace un máximo más
bajo → el nuevo máximo se logró con menos velocidad; el motor pierde fuerza.

- Es una señal de **agotamiento**, no de reversión inmediata: las divergencias pueden acumularse
  3 o 4 veces antes de que el precio gire (o no girar nunca).
- Uso correcto: como freno (no abrir LONGs nuevos, ajustar convicción), nunca como gatillo de
  venta en corto por sí sola.

## Cómo aplica al AGENTE TRADING

- El bot calcula RSI(14) en JS y Claude lo interpreta (`04`): >70 = cuidado con LONG tardío,
  <30 = sobreventa. La regla fina que debe respetar el prompt: **en trending-up confirmado,
  RSI 70+ no prohíbe el LONG, pero RSI 70+ CON precio a >3% de la SMA20 sí lo castiga** —
  esa combinación (velocidad extrema + precio extendido) es la firma exacta del FOMO de `10`.
- La divergencia RSI en máximos ya figura como señal de cambio de régimen en `03`: es un dato
  para el clasificador de régimen más que para el trade individual.
- RSI nunca decide solo: es un voto dentro de la confluencia (`45`), junto a régimen, estructura
  y distancia a la media.

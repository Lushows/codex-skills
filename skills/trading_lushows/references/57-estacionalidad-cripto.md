# 57 — Estacionalidad cripto (la señal más débil del catálogo)

**Estacionalidad** = patrones que se repiten según el calendario: hora del día, día de la
semana, mes del año. Este módulo existe sobre todo para ponerle límites: es la familia de
señales más débil y más propensa al humo de todo el análisis.

## Los patrones que se citan (y su nivel real de confianza)

| Patrón citado | Descripción | Confianza honesta |
|---|---|---|
| Fines de semana ilíquidos | Sábado/domingo hay menos volumen → movimientos exagerados y falsos | ALTA — es estructural (ver `64`), no estacional de verdad |
| "Lunes de reversión" | El lunes se corrige lo que exageró el finde | Media-baja |
| Cierres mensuales/trimestrales | Volatilidad al vencer opciones y futuros | Media — el efecto existe pero es difuso |
| "Uptober" / rally de fin de año | Octubre-diciembre históricamente alcistas | BAJA — folclore con backtest selectivo |
| "Sell in May" | Heredado de las acciones | BAJA — en cripto no está demostrado |
| Horas de apertura de EE.UU. | Más volumen y dirección cuando opera Nueva York | ALTA — estructural, no estacional |

## Por qué la estacionalidad es débil (la explicación anti-humo)

- **Muestra minúscula.** ¿"Octubre es alcista"? Bitcoin tiene ~15 octubres de historia
  líquida. Quince monedas al aire no definen una moneda cargada.
- **Se arbitra sola.** Si un patrón de calendario fuera confiable y público, los fondos lo
  operarían hasta borrarlo. Los patrones que sobreviven son los que casi no pagan.
- **Sesgo de publicación:** los patrones que "funcionaron" se vuelven titulares; los mil que
  no, nadie los cuenta. Ver un backtest estacional exitoso no dice nada sin ver todos los
  que se descartaron.
- **El mercado cambió de dueños.** La estacionalidad de la era retail (2017) no tiene por
  qué sobrevivir a la era ETF/institucional. Cualquier patrón: verificar con datos recientes,
  no con folclore de Twitter.

Lo único que sí es sólido: los patrones **estructurales de liquidez** (fin de semana flojo,
horario de EE.UU. activo) — pero eso es microestructura, no calendario mágico (ver `64` y `69`).

## Cómo aplica al AGENTE TRADING

- El bot NO usa filtros estacionales y no debe usarlos: con las pocas decenas de trades que
  lleva, cualquier "patrón por día de la semana" en sus propios datos sería ruido puro.
- Lo que SÍ vale la pena (Fase 8): tratar el fin de semana como zona de **liquidez baja** —
  exigir más convicción o reducir tamaño sábado/domingo. Eso es gestión de liquidez, no
  estacionalidad.
- Bandera roja para el futuro: si un análisis semanal del bot "descubre" que los martes
  gana más, ignorarlo hasta tener cientos de trades. Es exactamente el tipo de patrón
  fantasma que el overfitting produce.

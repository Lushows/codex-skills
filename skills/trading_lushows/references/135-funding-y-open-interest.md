# 135 — Funding y Open Interest: el termómetro del apalancamiento

> Dos datos de los futuros perpetuos que cuentan cuánta gente está apostando con dinero prestado
> y hacia qué lado. No predicen la dirección; miden la **fragilidad** del mercado.

## Definiciones en cristiano

- **Futuro perpetuo**: contrato para apostar al precio con apalancamiento, sin fecha de
  vencimiento. Es donde vive la mayoría del volumen especulativo en cripto.
- **Open Interest (OI)**: cuánto dinero total hay metido en esos contratos abiertos ahora mismo.
  OI subiendo = entra apalancamiento nuevo; OI bajando = se cierran apuestas.
- **Funding rate**: pago periódico entre longs y shorts que mantiene el perpetuo pegado al precio
  real. **Funding positivo** = los longs pagan a los shorts (dominan los alcistas apalancados).
  **Funding negativo** = los shorts pagan (dominan los bajistas).

## Cómo leerlo

| Situación | Lectura |
|---|---|
| OI alto + funding muy positivo | Mercado cargado de longs apalancados → frágil hacia abajo |
| OI alto + funding muy negativo | Cargado de shorts → frágil hacia arriba (posible short squeeze) |
| OI subiendo con el precio | Tendencia alimentada por dinero nuevo (puede seguir) |
| Precio sube pero OI cae | Suben porque cierran shorts, no por compra nueva (más débil) |

**Squeeze**: cuando el precio se mueve contra el lado sobrecargado y las liquidaciones forzadas
(módulo 136) aceleran el movimiento en cadena. Long squeeze = caída violenta; short squeeze = subida violenta.

## Los límites, sin humo

- Funding "extremo" no tiene un número mágico universal — se compara contra su propia historia
  reciente, y los umbrales cambian entre mercados alcistas y bajistas.
- Es un indicador de **condición**, no de timing: el mercado puede seguir sobrecalentado semanas.
  Apostar contra el funding caro sin confirmación de precio es agarrar cuchillos en el aire.
- Cada exchange reporta su propio funding/OI; el agregado importa más que uno solo.

## Cómo aplica al AGENTE TRADING

- El bot opera **spot simulado, solo LONG, sin apalancamiento** — el funding no le cuesta nada.
- Pero el apalancamiento ajeno SÍ lo afecta: las cascadas de liquidación mueven el spot y barren
  stops. Funding/OI serían un buen **contexto de régimen** para Claude: "mercado sobrecalentado,
  bajar convicción en entradas nuevas".
- Es candidato razonable para el backlog (los datos de funding de Binance son públicos y gratis),
  pero DESPUÉS del backtesting: primero validar el sistema base, luego enriquecerlo.

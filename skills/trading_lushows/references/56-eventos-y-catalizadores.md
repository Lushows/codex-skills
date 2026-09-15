# 56 — Eventos y catalizadores

Un **catalizador** es una noticia o evento que mueve el precio de golpe, fuera de lo que
dicen los gráficos. La regla madre de este módulo: **el bot no debe predecirlos — debe
sobrevivirlos**.

## Catálogo de catalizadores cripto

| Evento | Qué es | Efecto típico |
|---|---|---|
| Aprobación de ETF | Fondo en bolsa tradicional que compra el activo (ya existen de BTC y ETH) | Alcista sostenido: abre la puerta a dinero institucional |
| Listing | Un exchange grande lista una moneda | Pico alcista breve en esa moneda (irrelevante para BTC/ETH) |
| Hard fork / upgrade | Cambio mayor al software de la red | Volatilidad alrededor de la fecha; dirección impredecible |
| Hackeo de exchange/protocolo | Roban fondos a una plataforma | Caída brusca + pánico contagioso (Mt.Gox, FTX 2022) |
| Regulación | Gobiernos prohibiendo, demandando o aprobando | En ambas direcciones; EE.UU. y la SEC pesan más que nadie |
| Quiebras/contagio | Un jugador grande cae y arrastra a otros | Cascadas de venta forzada (Luna→3AC→FTX fue la cadena de 2022) |

Estado regulatorio y de ETFs en este momento: **verificar al día** — es de lo que más rápido cambia.

## Las dos verdades incómodas

1. **Los catalizadores no se pueden tradear por adelantado.** Cuando la noticia llega al
   público, el precio ya se movió (los que sabían, compraron antes). Perseguir la vela de la
   noticia es comprar caro con spread abierto.
2. **"Buy the rumor, sell the news"**: es común que el precio suba ANTES del evento esperado
   y caiga cuando por fin ocurre. La lógica: el evento ya estaba "en el precio".

## Sobrevivir, no predecir: el checklist

- **Stop-loss siempre puesto en el exchange** (no solo en la cabeza ni en un watcher local
  — ver `66`): el catalizador puede llegar a las 3 a.m.
- **Tamaño prudente**: si un hackeo tumba el mercado 10% en una hora, una posición al 1.5%
  de riesgo duele; una al 20% del capital destruye.
- **No promediar a la baja durante una noticia**: en un contagio tipo FTX, "está barato"
  fue la frase más cara del año.
- Aceptar que algunos stops saltarán por noticias que nada tenían que ver con el setup.
  Eso no es un error del sistema: es el costo de estar en el mercado.

## Cómo aplica al AGENTE TRADING

- El diseño actual ya es sobreviviente: riesgo 1.5% por trade, stop siempre definido, solo
  pares líquidos. Un catalizador bajista le cuesta al bot un stop, no la cuenta.
- El régimen de Haiku reacciona DESPUÉS del evento (las velas cambian) — eso es suficiente.
  No intentar darle "noticias en tiempo real" al bot: leer titulares con IA para tradearlos
  es un proyecto distinto, más frágil y con edge dudoso.
- En Fase 8, las órdenes OCO en Binance son la póliza contra catalizadores nocturnos: el
  stop vive en el exchange aunque Render se caiga.

# 55 — On-chain básico (sin sobrevenderlo)

## Qué significa "on-chain"

Bitcoin y Ethereum son libros contables públicos: **cada transacción queda registrada para
siempre y cualquiera puede verla**. "Análisis on-chain" = estudiar esos registros para
inferir qué está haciendo el dinero. Es un tipo de dato que no existe en acciones (nadie ve
los movimientos internos de las cuentas de un banco).

## Las métricas que más se citan

| Métrica | Qué mide | Lectura típica |
|---|---|---|
| Direcciones activas | Cuántas billeteras se mueven por día | Más actividad ≈ más adopción/uso |
| HODL waves | Hace cuánto no se mueve cada moneda | Muchas monedas quietas años = manos fuertes acumulando |
| Flujos a exchanges | BTC entrando/saliendo de exchanges | Entradas grandes ≈ intención de vender; salidas ≈ guardar a largo plazo |
| Realized price | Precio promedio al que se movió cada moneda por última vez | Referencia de "costo base" del mercado |
| Reservas de mineros | Cuánto BTC guardan los mineros | Mineros vendiendo = presión de oferta |

(HODL viene de un error de tipeo famoso de "hold": aguantar sin vender.)

## La honestidad: qué puede y qué NO puede el on-chain

Lo que sí aporta:
- **Contexto de largo plazo**: fases de acumulación/distribución que duran meses.
- **Alertas de eventos grandes**: una ballena moviendo 50.000 BTC a un exchange es real y visible.

Lo que NO aporta (y donde vive el humo):
- **Timing de corto plazo.** Ninguna métrica on-chain dice qué hará el precio esta semana.
  Los backtests que lo "demuestran" suelen estar sobreajustados (ver overfitting).
- Los exchanges y ETFs agrupan millones de usuarios en pocas direcciones — "flujos a
  exchanges" es cada vez más ruidoso de interpretar.
- Los vendedores de indicadores on-chain de pago viven de que suene a ciencia. Pregunta
  siempre: ¿esta métrica predijo o solo describió después de los hechos?
- Cualquier valor actual de estas métricas: **verificar al día** en fuentes como Glassnode
  o mempool.space, no citarlo de memoria.

## Cómo aplica al AGENTE TRADING

- El bot **no usa on-chain y está bien así**: opera swing en velas 1h, y el on-chain habla
  en escala de semanas/meses. Mezclar escalas es una fuente clásica de errores.
- Si algún día se agrega, el lugar correcto es el **clasificador de régimen macro** (contexto
  lento), nunca la señal de entrada (rápida).
- Prioridad honesta: baja. Antes están el SHORT en paper, el calendario FOMC (`53`) y las
  órdenes OCO (`66`). On-chain es lo último que le falta a un bot swing de BTC/ETH.

# 54 — Stablecoins y flujos de capital

## Qué es una stablecoin

Una **stablecoin** es una cripto diseñada para valer siempre ~$1 USD. Las dos grandes:
**USDT** (Tether) y **USDC** (Circle). Funcionan como el "dólar digital" dentro de los
exchanges: cuando alguien vende BTC, normalmente recibe USDT/USDC, no dólares de banco.

Por qué existen: mover dólares reales entre bancos y exchanges es lento y caro; mover
stablecoins toma minutos. Son la sangre del sistema de trading cripto.

## La "pólvora seca"

Las stablecoins paradas en exchanges son dinero que **ya está dentro del casino pero aún no
apostó**. De ahí la metáfora de pólvora seca:

| Señal | Lectura típica |
|---|---|
| Crece la emisión de USDT/USDC | Entra capital nuevo al ecosistema → potencial demanda de BTC/ETH |
| Cae la capitalización de stables | El capital sale de cripto hacia dólares de banco → menos combustible |
| Stables acumulándose en exchanges | Pólvora lista; falta el detonante |

Honestidad obligatoria: esta señal es **lenta y difusa**. La emisión puede crecer por razones
que no son "van a comprar BTC" (pagos, remesas, DeFi). Sirve como contexto de semanas/meses,
no como señal de entrada. Las cifras de capitalización de stables: **verificar al día**.

## Riesgo de depeg: cuando el $1 deja de valer $1

**Depeg** = la stablecoin pierde su paridad con el dólar. Ha pasado:
- **UST (Terra), 2022**: stablecoin "algorítmica" (sin dólares reales de respaldo) que
  colapsó a casi cero y arrastró al mercado entero. Lección: no todas las stables son iguales.
- USDC llegó a caer varios centavos en 2023 por la crisis de un banco donde tenía reservas;
  se recuperó en días.
- USDT carga años de dudas sobre sus reservas; hasta hoy ha mantenido la paridad.

Por qué importa aunque "no operes stables": si la stablecoin donde descansa tu capital
depega, pierdes plata **sin haber hecho ningún trade**. Es riesgo de custodia disfrazado.

## Cómo aplica al AGENTE TRADING

- En paper el riesgo es cero; en Fase 8 (Binance real) el capital entre trades descansará en
  una stablecoin (o el bot operará pares contra USDT). Decisión pendiente y consciente:
  **qué stable usar** — USDT tiene más liquidez en Binance; USDC, reputación de reservas
  más auditadas. Verificar liquidez de los pares al día.
- Regla de prudencia para live: no dejar el 100% del capital en una sola stable por meses;
  y ante un depeg en curso, la orden del día es NO operar (spreads rotos, precios mentirosos).
- La emisión de stables puede sumarse algún día como insumo del régimen macro (contexto
  `risk-on`), pero es mejora de baja prioridad: señal lenta para un bot de velas 1h.

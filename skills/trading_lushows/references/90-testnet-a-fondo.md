# 90 — Testnet a fondo (el ensayo general gratis)

> El testnet es la API real de Binance con dinero falso. Es el puente obligatorio entre el
> simulador propio (paper) y la cuenta real. Meta: **≥2 semanas sin incidentes** antes del go-live.

## ¿Qué es testnet.binance.vision?

Un entorno de pruebas oficial de Binance: mismos endpoints, misma firma HMAC, mismas reglas de
órdenes, pero los saldos son de mentira. Se accede con API keys propias del testnet (se generan
en la web del testnet, NO son las de la cuenta real). Config del bot:
`BINANCE_REST_URL=https://testnet.binance.vision` + keys de testnet. Detalles exactos de
registro y endpoints: verificar docs oficiales de Binance al día.

**Diferencia clave con nuestro paper actual**: el paper de `broker.js` es un simulador que
nosotros escribimos — nunca habla con Binance. El testnet sí habla con Binance de verdad:
valida que NUESTRO código de integración funciona, no solo nuestra lógica de estrategia.

## Qué SÍ valida el testnet

| Área | Qué se prueba |
|---|---|
| Firma | Que el HMAC-SHA256, timestamp y recvWindow están bien armados (módulo 91) |
| Órdenes | Que MARKET/LIMIT se envían, ejecutan y se leen las respuestas correctamente |
| OCO | Que el stop-loss + take-profit quedan VIVOS en el exchange, no en nuestra memoria |
| Errores | Cómo reacciona el bot a rechazos (filtros de cantidad, precio, saldo insuficiente) |
| Reconexión | Que al caerse Render y reiniciar, el bot reconcilia estado (módulo 93) |
| Rate limits | Que no nos pasamos de peticiones por minuto |

## Qué NO valida el testnet (no te engañes)

- **Liquidez real**: el order book del testnet es de juguete; los fills no se parecen a los reales.
- **Slippage real**: la diferencia entre el precio que pediste y el que te dieron será distinta en vivo.
- **Precios reales**: el testnet a veces tiene precios desfasados del mercado real.
- **Psicología**: con dinero falso nadie suda. Eso solo lo prueba el modo híbrido (módulo 95).

Por eso testnet NO reemplaza los criterios de desempeño del módulo 08 — valida la TUBERÍA,
no el EDGE.

## El plan de 2 semanas

| Semana | Objetivo |
|---|---|
| 1 | Conectar cliente firmado, ejecutar órdenes manuales de prueba, colocar y verificar OCO |
| 1-2 | Dejar el bot corriendo en modo live-testnet: señales reales → órdenes al testnet |
| 2 | Provocar fallos a propósito: reiniciar Render, cortar red, matar proceso a mitad de orden |
| Final | Checklist: 0 incidentes sin explicar, reconciliación correcta en cada reinicio |

Si aparece UN incidente sin explicación, el reloj de 2 semanas se reinicia. Sin excepciones.

## Cómo aplica al AGENTE TRADING

- Es la condición técnica #1 del go-live (módulo 08, condiciones adicionales).
- Se construye en julio-agosto 2026 en paralelo al paper, sin tocar la evaluación del 22-ago.
- El testnet corre con el MISMO código que irá a live (`MODE=live` + URL de testnet), no con
  una rama aparte — si no, estaríamos probando otro programa.

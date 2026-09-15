# 91 — La API firmada de Binance (HMAC en simple)

> Para operar de verdad, cada orden debe ir "firmada": una prueba matemática de que la envió
> el dueño de la cuenta. Este módulo explica los principios. Los detalles exactos (nombres de
> parámetros, límites vigentes): **verificar docs oficiales de Binance al día**.

## ¿Qué es firmar una petición?

Binance te da dos llaves al crear una API key:

| Llave | Qué es | Se envía? |
|---|---|---|
| API Key | Tu "usuario" — identifica la cuenta | Sí, en un header |
| Secret Key | Tu "contraseña" criptográfica | **JAMÁS se envía** |

La firma funciona así: tomas todos los parámetros de tu petición (símbolo, cantidad, precio,
timestamp...), los pasas por una función matemática llamada **HMAC-SHA256** usando la Secret Key,
y el resultado (la firma) se adjunta a la petición. Binance hace el mismo cálculo de su lado:
si las firmas coinciden, la petición es legítima. Si alguien intercepta la petición, no puede
crear otras: sin la Secret Key no puede firmar.

En Node.js esto es el módulo nativo `crypto` (createHmac) — no requiere librerías externas.

## Timestamp y recvWindow

- **timestamp**: cada petición firmada lleva la hora en milisegundos. Evita que alguien "repita"
  una petición vieja capturada.
- **recvWindow**: ventana de tolerancia (ej. 5000 ms). Si la petición llega a Binance más tarde
  que timestamp + recvWindow, se rechaza.
- **Trampa clásica**: si el reloj del servidor está desincronizado, TODO falla con error de
  timestamp. Solución estándar: consultar la hora del servidor de Binance al arrancar y ajustar
  el desfase (offset) localmente.

## Rate limits (límites de peticiones)

Binance limita cuántas peticiones puedes hacer por minuto (por "peso" de cada endpoint) y
cuántas órdenes por segundo/día. Pasarse trae avisos, luego bloqueos temporales de IP.
Principios:

1. Leer los headers de respuesta que informan el peso consumido.
2. Ante un error de límite (HTTP 429), FRENAR y esperar — nunca reintentar en loop.
3. Un HTTP 418 significa IP baneada temporalmente: es la escalada por ignorar los 429.

Nuestro bot es swing 1h con pocas órdenes: los límites no deberían ser problema, pero un bug
en un loop de reintentos sí puede quemarlos en segundos.

## Errores comunes de integración

| Error típico | Causa probable |
|---|---|
| Firma inválida | Orden de parámetros distinto entre lo firmado y lo enviado, o secret con espacios |
| Timestamp fuera de rango | Reloj desincronizado (ver arriba) |
| Filtros de símbolo (LOT_SIZE, etc.) | Cantidad o precio con decimales que el par no acepta — hay que redondear según las reglas del símbolo |
| Saldo insuficiente | El local cree que hay plata que el exchange no tiene → reconciliar (módulo 93) |

## Cómo aplica al AGENTE TRADING

- Vive en `src/binance/signedClient.js` (previsto en el spec de Fase 8, módulo 09).
- Se prueba primero contra testnet (módulo 90) con keys de testnet.
- El cliente debe manejar el offset de reloj y respetar rate limits desde el día 1 — en Render
  el reloj suele estar bien, pero no se asume: se mide.

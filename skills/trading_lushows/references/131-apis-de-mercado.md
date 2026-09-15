# 131 — APIs de mercado: REST vs WebSocket

> Una **API** es la puerta por la que un programa le pide datos a otro. Los exchanges ofrecen dos
> puertas distintas y usarlas bien es la diferencia entre un bot estable y uno que se cae a las 3am.

## REST vs WebSocket en cristiano

| | REST | WebSocket |
|---|---|---|
| Metáfora | Llamar por teléfono cada vez que quieres saber algo | Dejar la línea abierta y que te avisen |
| Cómo funciona | Tú pides → el servidor responde → se cierra | Conexión permanente; el servidor empuja datos |
| Ideal para | Histórico, consultas puntuales, rellenar huecos | Precios y velas en tiempo real |
| Riesgo típico | Pasarte del límite de peticiones (rate limit) | La conexión se corta y no te das cuenta |

## Rate limits (límites de peticiones)

Los exchanges limitan cuántas peticiones REST aceptan por minuto. Si te pasas, te bloquean temporal
o permanentemente (ban de IP). Los límites exactos cambian — verificar en la documentación al día.

Buenas prácticas:
- Pedir en lotes grandes (ej: 500-1000 velas por petición) en vez de muchas peticiones chicas.
- Respetar las cabeceras de la respuesta que indican cuánto "presupuesto" queda.
- **Backoff exponencial**: si falla, esperar 1s, luego 2s, 4s, 8s... en vez de martillar.

## Reconexión de WebSocket — donde mueren los bots

Un WebSocket se cae por wifi, mantenimiento del exchange, o porque el servidor cierra conexiones
viejas (Binance las recicla cada ~24h por diseño). Un bot serio debe:

1. **Detectar** la caída (ping/pong o silencio prolongado).
2. **Reconectar** automáticamente con backoff.
3. **Rellenar el hueco**: pedir por REST las velas que se perdió mientras estuvo desconectado.

El paso 3 es el que casi todos olvidan — y así nacen los huecos en los datos (ver módulo 139).

## Cómo aplica al AGENTE TRADING

- El bot ya hace esto bien: **WebSocket público de Binance** para velas 1h en vivo + **REST del
  mirror `data-api.binance.vision`** para histórico y relleno tras desconexiones.
- El mirror existe porque Binance geo-bloquea su API principal desde IPs de USA (Render corre en
  US); el mirror es solo-lectura de datos y no tiene ese bloqueo.
- Hay `retryWithBackoff` en `src/strategy/` para las llamadas que fallan — no martillamos.
- Al ser solo 2 pares en velas 1h, estamos lejísimos de cualquier rate limit. El riesgo real es
  la reconexión silenciosa: por eso `/status` reporta el estado del WS y errores de 24h.

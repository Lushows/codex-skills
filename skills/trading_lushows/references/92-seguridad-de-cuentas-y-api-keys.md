# 92 — Seguridad de cuentas y API keys (no negociable)

> La regla madre: aunque un atacante consiga TODO lo que hay en el servidor, no debe poder
> robarse el dinero. Eso se logra con permisos mínimos, no con esperanza.

## Permisos mínimos: la decisión más importante

Al crear una API key en Binance se eligen permisos por casilla. Para el bot:

| Permiso | ¿Activar? | Por qué |
|---|---|---|
| Enable Reading | Sí | Leer saldos, órdenes, precios |
| Enable Spot Trading | Sí | Colocar y cancelar órdenes spot (lo único que hace el bot) |
| Enable Withdrawals | **JAMÁS** | Con esto apagado, una key robada NO puede sacar fondos |
| Futures / Margin | No | El bot no opera apalancado; menos superficie = menos riesgo |

Con withdrawal apagado, el peor escenario de una key filtrada es que alguien haga trades
malos con tu saldo — grave, pero recuperable. Con withdrawal encendido, el dinero desaparece.

## IP whitelist (la segunda cerradura)

Binance permite restringir una key a IPs específicas. Se whitelistea SOLO la IP del servicio
de Render EU (Frankfurt). Resultado: aunque roben la key Y el secret, no sirven desde ninguna
otra máquina. Nota práctica: verificar cómo expone Render la IP saliente fija (según el plan)
antes de configurar — si la IP cambia, el bot se queda sin acceso y hay que actualizarla.

## Dónde viven las keys (y dónde NUNCA)

- ✅ Variables de entorno de Render (panel → Environment). Solo Luis las ve.
- ❌ En el repo (ni en `.env` commiteado, ni "temporalmente" en el código).
- ❌ En el dashboard, en logs, en mensajes de WhatsApp, en capturas de pantalla.
- ❌ En el chat con Claude u otra IA. Nunca pegar el secret en ninguna conversación.

Regla de logging: el `signedClient` debe loguear peticiones SIN la firma ni la key completa
(los últimos 4 caracteres bastan para identificar cuál key es).

## 2FA en la cuenta de Binance

La cuenta de Luis debe tener autenticación de dos factores con app (tipo Google Authenticator),
NO solo SMS (el SMS es vulnerable a duplicación de SIM). El 2FA protege el login web — que es
por donde alguien podría crear keys nuevas CON withdrawal.

## Rotación y qué hacer si se filtra una key

**Rotación**: cambiar las keys periódicamente (ej. cada 3 meses) y siempre después de cualquier
sospecha. Es crear key nueva → actualizar env vars en Render → borrar la vieja.

**Si se filtra (o hay duda)** — en este orden, sin pensarlo:
1. Borrar la API key en Binance (esto la mata al instante).
2. Activar el kill switch del bot (módulo 94) para que no falle en loop sin key.
3. Revisar el historial de órdenes y logins de la cuenta.
4. Crear key nueva con los mismos permisos mínimos + whitelist, actualizar Render.
5. Preguntarse CÓMO se filtró y cerrar ese hueco antes de reanudar.

## Cómo aplica al AGENTE TRADING

- Estas reglas son condición del go-live (módulos 08 y 09): keys solo-spot, whitelist, env vars.
- El checklist final (módulo 99) las verifica una por una antes del primer peso real.
- Capital $200-500 al inicio: incluso el peor escenario duele poco. La seguridad y el tamaño
  pequeño son capas del mismo escudo.

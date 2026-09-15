# 168 — Monitoreo y uptime: saber que el bot está vivo (y enterarse cuando no)

## El problema que casi nadie ve venir

Un bot caído **no avisa que está caído** — está caído, no puede avisar. Si nadie lo vigila desde
afuera, la caída se descubre días después mirando el dashboard ("¿por qué no hay análisis desde
el martes?"). En paper es vergonzoso; en live, con posición abierta, es peligroso.

## Capa 1: el health check interno — `/status`

Un **health check** es un endpoint que resume la salud del sistema. El del bot devuelve: uptime,
estado del WebSocket (¿frescas las velas?), costo acumulado de Claude, estado del auto-trader,
y errores de las últimas 24h. Reglas de un buen health check:

- Debe verificar las **dependencias vitales** (WS vivo, disco escribible), no solo "el proceso
  responde". Un proceso vivo con WS zombie está funcionalmente muerto.
- Debe ser barato (se consultará cada pocos minutos).
- Idealmente responde con código HTTP distinto (p. ej. 503) cuando algo vital está mal — así
  los monitores externos lo detectan sin leer el JSON.

## Capa 2: monitoreo externo

Como el bot no puede auto-reportar su muerte, alguien de afuera debe hacer ping periódico.
Servicios tipo **UptimeRobot** (hay plan gratuito — verificar condiciones al día) o similares
(Better Stack, Pulsetic...) hacen esto: consultan tu URL cada N minutos y si no responde (o
responde con error) mandan email/Telegram. Detalles prácticos:

- El monitor necesita pasar el **basic auth** (la mayoría soporta URL con credenciales o headers).
  Alternativa limpia: un endpoint de salud sin auth que NO revele nada sensible, solo "ok/mal".
- Monitorear el `/status` real, no la raíz: interesa "el bot funciona", no "Express responde".
- Configurar la alerta a un canal que Luis SÍ mire (el correo que se revisa, no el que no).

## El caso crítico: el watcher de stops muere con el servicio

Hoy los stops los vigila `watcher.js`, un proceso **dentro** del bot. Eso significa:

| Escenario | Consecuencia en paper | Consecuencia en live (sin OCO) |
|---|---|---|
| Render redeploya (2-3 min) | Nada grave | Ventana sin protección |
| El servicio crashea y no vuelve | Se pausa la simulación | **Posición abierta SIN stop hasta que alguien lo note** |
| WS zombie con proceso vivo | Watcher mira precios viejos | Stop que nunca dispara en un desplome |

La conclusión no es "monitorear más fuerte": es que **la protección no puede depender del
uptime del bot**. Órdenes OCO en el exchange (Fase 8) hacen que el stop viva en Binance y se
ejecute aunque el bot lleve horas muerto. El monitoreo externo pasa a ser la segunda línea:
te avisa para restablecer el análisis, no para salvar la posición.

## Métricas que vale la pena mirar semanalmente

Uptime del mes, número de reconexiones de WS, errores de Claude (y retries), costo de tokens,
y edad de la última vela. Tendencias raras (reconexiones creciendo, retries frecuentes) son
avisos tempranos de problemas que aún no explotan.

## Cómo aplica al AGENTE TRADING

Los 44 días de uptime actuales son buena señal, pero hoy nadie se enteraría en minutos de una
caída. Pendiente concreto pre-live: ① dar de alta un monitor externo contra `/status` con alerta
a Luis, ② decidir cómo pasa el basic auth, ③ y sobre todo OCO — porque la alerta más rápida del
mundo sigue siendo más lenta que un stop viviendo en el exchange.

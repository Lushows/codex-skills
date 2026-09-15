# 94 — Kill switch y límites operativos (los frenos del carro)

> Un bot con dinero real sin botón de apagado es un carro sin frenos. El kill switch no es
> pesimismo: es la condición para poder dormir tranquilo mientras el bot opera solo.

## Kill switch manual (el botón rojo)

Un botón en el dashboard + un endpoint protegido que, al activarse:

1. Deja de abrir posiciones nuevas de inmediato (apaga el auto-trader).
2. Deja las posiciones abiertas PROTEGIDAS: verifica que sus OCO siguen vivos en el exchange.
3. Notifica a Luis: "kill switch activado, por X, estado: N posiciones abiertas con stop".

Ojo: kill switch (dejar de operar, stops puestos) ≠ modo pánico (cerrar todo YA). Son dos
niveles distintos — ver abajo.

## Kill switch automático (el freno que no depende de nadie)

Se dispara solo, sin esperar a que Luis mire el teléfono:

| Disparador | Umbral | Por qué |
|---|---|---|
| Pérdida diaria | −3% del capital en el día → parar hasta mañana | Corta las rachas malas y los bugs que pierden plata rápido |
| Órdenes por hora | Tope duro (ej. mucho más de lo que el swing 1h justifica) | Un bot sano nuestro hace pocas órdenes; muchas órdenes/hora = bug casi seguro |
| Errores de API en serie | N errores seguidos → parar y avisar | Si Binance rechaza todo, algo está roto; insistir empeora |
| Divergencia sin resolver | Reconciliación encuentra algo inexplicable (módulo 93) | No se opera sobre un estado que no se entiende |
| Posición sin stop | OCO esperado no existe en el exchange | Emergencia: proteger primero, investigar después |

El límite de −3% diario ya está definido en los módulos 08/09. No se "ajusta" en caliente
porque el día va mal — para eso existe.

## Modo pánico (cerrar todo)

El nivel máximo: cancela todas las órdenes abiertas y cierra todas las posiciones a mercado.
Se usa cuando NO se confía en el estado del sistema (hackeo sospechado, bug de dinero, key
filtrada). Cuesta slippage y probablemente cristaliza pérdidas — por eso es el último recurso,
no la reacción a un mal día. Debe ser UN comando/botón, probado en testnet, no una serie de
pasos manuales que Luis tenga que improvisar a las 2 a.m.

## ¿Quién puede activarlo?

- **Manual**: solo Luis, desde el dashboard (autenticado) o endpoint con token secreto. Nadie más
  tiene acceso; el token no se comparte ni se pega en chats.
- **Automático**: el propio bot, según la tabla de arriba. El bot puede APAGARSE solo;
  **encenderse de nuevo requiere siempre acción humana de Luis**. Un bot que se auto-reactiva
  después de un kill switch repite el error que lo apagó.

## Cómo aplica al AGENTE TRADING

- Es riel obligatorio del go-live (tabla de rieles en módulo 09, condiciones en módulo 08).
- Se construye y se PRUEBA en testnet: disparar cada trigger a propósito y verificar la
  reacción (módulo 90, semana 2). Un kill switch no probado es decoración.
- En el mes híbrido (módulo 95) el kill switch ya opera igual que en auto: los frenos no
  esperan a la graduación.

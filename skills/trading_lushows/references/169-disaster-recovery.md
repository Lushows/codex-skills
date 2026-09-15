# 169 — Disaster recovery: qué hacer cuando lo malo ya pasó

## Qué es disaster recovery (DR)

No es evitar desastres (eso es prevención): es tener **plan escrito para después**. La regla de
oro: un plan de recuperación que nunca se ha ensayado es una hipótesis, no un plan. Este módulo
enumera los desastres plausibles del AGENTE TRADING y el camino de vuelta para cada uno.

## Desastre 1: se pierde el disco de Render

El disco persistente sobrevive redeploys, pero **no es un backup**: si el servicio se borra por
error, o el disco falla, o la migración a Frankfurt sale mal, `data/` desaparece — portafolio,
memoria del trader, análisis, equity. El código no se pierde (está en GitHub); **los datos sí**.

Plan: backup periódico de `data/` hacia FUERA de Render. Opciones de menor a mayor esfuerzo:
① endpoint que empaquete `data/` y descargarlo manualmente cada semana, ② tarea programada que
lo suba a un almacenamiento externo (S3/R2/similar), ③ al menos, exportar el CSV de trades
(`/api/trades/export`) regularmente. Sin alguno de estos, el DR de este escenario es "empezar
de cero" — aceptable en paper, no en live con historial que audita el desempeño.

## Desastre 2: caída del bot con posición abierta

El escenario que quita el sueño. Hoy los stops los vigila el proceso local: bot muerto = posición
sin protección (ver módulo 168).

| Fase | Protección |
|---|---|
| Paper (hoy) | Ninguna consecuencia real; al volver, el watcher retoma |
| Live SIN OCO | ⚠️ Inaceptable: un desplome con el bot caído no tiene freno |
| Live CON OCO (Fase 8) | El stop y el target viven EN Binance: se ejecutan aunque el bot esté apagado |

Con OCO, la recuperación es ordenada: al reiniciar, el bot debe **reconciliar** — preguntar al
exchange qué órdenes/posiciones existen realmente y ajustar su JSON local a esa verdad (el
exchange siempre gana el empate). Esa rutina de reconciliación al arranque es parte del trabajo
de Fase 8.

## Desastre 3: la API de Claude caída o degradada

Ya está parcialmente resuelto: el bot tiene retry con backoff para errores transitorios. Si la
caída es larga, el diseño degrada con gracia: **sin análisis no hay trades nuevos** (el bot
simplemente no opera — que es la opción segura), pero el watcher **sigue vigilando stops sin
necesitar a Claude** — proteger no requiere pensar. Regla de diseño a conservar siempre: la ruta
de protección no debe tener a la IA en el camino crítico.

## Desastre 4: deploy roto (bug que tumba el arranque)

Auto-deploy significa que un push malo tumba producción. Recuperación: revertir el commit en
GitHub (`git revert`) y dejar que Render redeploye, o usar el deploy manual de un commit anterior
desde el dashboard de Render. Los 145 tests antes de cada push son la prevención; el revert, el DR.

## El plan de restauración completo (de cero a operando)

1. Crear servicio en Render (región correcta), disco persistente montado en `data/`.
2. Configurar variables de entorno (API keys, `DASHBOARD_USER/PASS`, umbrales).
3. Restaurar el último backup de `data/` (o arrancar limpio si no lo hay, asumiendo la pérdida).
4. Verificar `/status`: WS conectado, velas frescas, sin errores.
5. En live: reconciliar contra el exchange ANTES de reactivar el auto-trader.

**Ensayarlo una vez** (aunque sea en un servicio temporal) antes del go-live: el ensayo revela
el paso que falta en la lista, siempre hay uno.

## Cómo aplica al AGENTE TRADING

Prioridades pre-go-live, en orden: ① OCO (convierte el peor desastre en uno menor),
② backup de `data/` fuera de Render, ③ rutina de reconciliación al arranque, ④ un ensayo de
restauración completa. En paper, nada de esto urge; el 22-ago-2026 todo esto debe existir.

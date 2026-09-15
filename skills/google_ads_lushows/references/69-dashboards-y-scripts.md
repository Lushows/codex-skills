# 69 — Dashboards, scripts y reglas

Lee este módulo cuando estés perdiendo horas armando reportes a mano cada semana, cuando se te escape un problema porque nadie estaba mirando la cuenta a las 11pm, cuando manejes varias cuentas y no des abasto, o cuando quieras que la cuenta "se cuide sola" sin perder el control. Aquí pasamos de mirar el panel manualmente a **automatizar la vigilancia y el reporte**: Looker Studio para ver, scripts para vigilar, reglas automáticas para actuar. La meta: que la máquina haga la rutina y tú las decisiones.

Tres herramientas, tres niveles de automatización, tres niveles de riesgo:

| Herramienta | Para qué | Riesgo |
|---|---|---|
| **Looker Studio** | **Ver** datos en dashboards bonitos y compartibles | Ninguno (solo lee) |
| **Google Ads scripts** | **Vigilar** y avisar (alertas, n-grams, presupuesto) | Bajo si solo alertan; alto si modifican |
| **Reglas automáticas** | **Actuar** solo (pausar, ajustar puja por condición) | Alto: actúan sin ti |

La regla que ordena todo el módulo: **automatiza la vigilancia y el reporte; reserva para ti las decisiones grandes** (escalar, cortar, cambiar oferta). La máquina detecta y limpia lo rutinario; tú juzgas lo que vale plata.

## Looker Studio: el dashboard que se actualiza solo

**Looker Studio** (antes Data Studio) es la herramienta gratis de Google para armar dashboards conectados en vivo a Google Ads y GA4. En vez de exportar a Excel cada semana, el dashboard se actualiza solo y lo compartes con un link.

Setup básico:
1. Entra a Looker Studio → **Create → Data source** → conecta **Google Ads** (y otra fuente para **GA4**). Para cruzar varias cuentas o sumar Meta/TikTok, **blend** (combinar) fuentes o pásalas por BigQuery si el volumen es grande.
2. Arma una página con los números que importan (ver 60, 67): gasto, conversiones, CPA, ROAS, IS, tendencia por día.
3. Agrega un **filtro de fechas** y un **selector de campaña** arriba.
4. Comparte el link con el cliente/jefe (modo solo-ver) o **programa el envío** por email (Looker manda el PDF/snapshot solo).

Qué poner (no lo llenes de gráficas por llenar):
- **Scorecards** grandes: gasto, conversiones, CPA, ROAS — los 4 que importan, con comparación vs periodo anterior.
- **Línea de tiempo**: CPA o conversiones por día (ver tendencia, no solo el total).
- **Tabla**: rendimiento por campaña (gasto, conv., CPA, IS).
- **Barra de Lost IS** (budget vs rank) por campaña: el diagnóstico de techo de un vistazo (ver 61, 94).
- Para triangular con la verdad financiera (backend/MER), eso **no vive aquí**: va en tu hoja con datos del banco (ver 64). El dashboard muestra el universo Google; el MER lo calculas tú cruzando fuentes.

Looker Studio **reemplaza el screenshot del panel** (ver 67): le das al cliente un tablero vivo en vez de una foto muerta. Pero el reporte ejecutivo con la **frase y la decisión** sigue siendo tuyo: el dashboard muestra qué pasó, tú explicas qué significa y qué sigue.

## Google Ads scripts: vigilancia que no duerme

Los **scripts** son pedacitos de código (JavaScript) que corren dentro de Google Ads en un horario que tú pones. No tienes que programar desde cero: hay scripts públicos listos para pegar. Ruta: **Tools → Bulk actions → Scripts → +**. No técnico: cópialos, autoriza la cuenta, programa la frecuencia, listo.

Los tres scripts que todo media buyer debería tener:

| Script | Qué hace | Por qué importa |
|---|---|---|
| **Alerta de gasto / pacing** | Te emailea si una campaña gasta de más / de menos vs lo esperado | Detecta presupuesto disparado o pausado por error antes de quemar plata |
| **N-gram / search terms** | Agrupa search terms por palabra repetida y muestra cuáles gastan sin convertir | Hace el análisis de 68 automático, semanal, sin que abras el reporte |
| **Monitor de cuenta / link checker** | Avisa si la cuenta deja de gastar, si una conversión deja de registrarse, si una landing tira error 404 | La red de seguridad: te enteras del incendio por email, no por el cliente |

Otros útiles cuando creces: reporte de Quality Score histórico, alerta de Lost IS (rank) subiendo (competidor entrando, ver 94), y exportador a Google Sheets para alimentar tu hoja de triangulación (ver 64).

Regla de oro de scripts: **empieza con scripts que solo AVISAN, no que modifican.** Un script que te manda un email es seguro. Un script que pausa campañas o cambia pujas solo puede hacer un desastre silencioso si la lógica está mal o si pelea con el Smart Bidding (ver 13). Modifica solo cuando entiendas exactamente qué hace y hayas leído sus logs varias veces.

Esqueleto mental de un script de alerta (no necesitas escribirlo, sí entenderlo):

```
1. Definir umbral:   gasto_hoy > presupuesto_diario * 1.3
2. Recorrer campañas activas
3. Si alguna cruza el umbral → juntar en un email
4. MailApp.sendEmail(tu_correo, "Alerta gasto", detalle)
5. Programar: cada hora / cada día
```

## Reglas automáticas: actuar sin estar

Las **reglas automáticas** (Tools → Bulk actions → Rules) ejecutan acciones según condiciones, sin código. Ej: "pausar keyword si gastó >$50.000 COP en 30 días con 0 conversiones" o "subir presupuesto 10% si el ROAS > 4 ayer".

Usos seguros y comunes:
- Pausar keywords/anuncios que gastan sin convertir (con **umbral generoso y ventana larga**, no agresivo).
- **Avisar** (no actuar) cuando una métrica cruza un límite — la versión segura de casi cualquier regla.
- Subir/bajar presupuesto en horarios o eventos conocidos (un lanzamiento, una fecha de promo).
- Re-activar algo pausado en una fecha programada (que no se te olvide prender la campaña el día del evento).

Cuidado crítico: las reglas y el **Smart Bidding** (ver 13) **pueden pelearse**. Si dejas que el bidding automático (tCPA/tROAS) maneje las pujas y además pones una regla que cambia pujas, se estorban y el aprendizaje del bidding se rompe. **Define quién manda sobre cada palanca**: normalmente Smart Bidding manda las pujas; las reglas se quedan en presupuesto, pausas por umbral y alertas. No las cruces.

Tabla de "qué automatizar y a qué nivel de confianza":

| Acción | Nivel seguro |
|---|---|
| Avisar por email cuando algo cruza umbral | Siempre seguro |
| Pausar keyword 0-conv con ventana ≥30 días y gasto alto | Seguro con umbral generoso |
| Subir presupuesto en fecha conocida | Seguro |
| Cambiar pujas manualmente vía regla con Smart Bidding activo | **Evítalo** (pelean) |
| Pausar campañas por 1 día de mal ROAS | **Peligroso** (ruido normal) |

## Automatizar sin perder el control

El principio que ata todo: **automatiza la vigilancia y el reporte, mantén tú las decisiones grandes.** La máquina te avisa y limpia lo rutinario; tú decides escalar, cortar, cambiar oferta (con triangulación e incrementalidad de fondo, ver 64, 65). Y la regla que casi todos olvidan: **revisa los logs de scripts y reglas.** Una automatización que falla en silencio es peor que no tenerla, porque crees que algo está cuidado cuando no lo está. Programa un recordatorio mensual de "¿siguen vivas mis alertas?".

## Errores comunes — blacklist

1. **Armar reportes a mano cada semana** existiendo Looker Studio. Pierdes horas en algo que se actualiza solo.
2. **Empezar con scripts que MODIFICAN la cuenta.** Un script con lógica mala hace daño silencioso. Empieza solo con los que avisan.
3. **Reglas automáticas con umbrales agresivos.** "Pausar si 1 día sin conversión" mata keywords buenas por ruido normal. Usa ventanas largas y umbrales generosos (ver 61 sobre no reaccionar al ruido).
4. **Reglas que pelean con Smart Bidding.** Si el bidding maneja pujas, no pongas reglas que también las toquen. Define quién manda (ver 13).
5. **Dashboards llenos de gráficas inútiles.** El cliente quiere los 4 números (ver 60, 67), no 20 widgets. Menos es más.
6. **Confiar en una automatización sin revisar sus logs.** Una alerta que dejó de correr te deja ciego justo cuando crees estar cubierto. Verifica que sigan vivas.
7. **Creer que el dashboard reemplaza el análisis.** Looker Studio muestra qué pasó; la frase con la decisión y el aprendizaje siguen siendo tuyos (ver 67).
8. **Meter el MER y la verdad financiera dentro del dashboard de Ads.** El dashboard solo ve el universo Google; el MER se calcula cruzando con backend/banco fuera de ahí (ver 64).

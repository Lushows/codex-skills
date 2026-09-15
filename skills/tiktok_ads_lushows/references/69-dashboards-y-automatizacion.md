# 69 — Dashboards y automatización

Lee este módulo cuando manejes varias campañas o cuentas y revisar todo a mano te coma el día, cuando quieras dejar de vivir dentro de Ads Manager, o cuando un cliente te pida "verlo en vivo" sin entrar a TikTok. Un dashboard reúne tus números en una sola pantalla que se actualiza sola; la automatización hace que la cuenta se cuide mientras duermes. El objetivo no es quitar tu criterio — es **liberar tu atención para lo que importa (el creativo, ver 68) y que ningún error te queme plata sin avisar**. Pero ojo: automatizar mal es peor que no automatizar. Aquí se hace con control.

## El dashboard: una pantalla, la verdad triangulada

Un **dashboard** es una hoja o tablero que jala datos de varias fuentes y los muestra juntos, sin que tú copies nada a mano. El mejor dashboard de un media buyer honesto **triangula** (ver 64): no muestra solo lo que dice TikTok.

| Nivel | Herramienta | Para quién |
|---|---|---|
| Básico (gratis) | Google Sheets + exportes manuales/semanales | El que empieza |
| Intermedio | Looker Studio conectado a Ads + GA4 | El que quiere tiempo real |
| Avanzado | Looker/BI con backend (tienda/CRM) + banco | Agencia / varias cuentas |

Qué debe mostrar tu dashboard, mínimo (ver 60 para cada métrica):

- Gasto, conversiones, CPA, ROAS de plataforma **y** MER real (ver 64).
- Tendencia (esta semana vs anterior, el Δ — ver 67).
- CPA por creativo (lo que de verdad decide, ver 68).
- Frequency (aviso de fatiga, ver 39).
- Cruce TikTok vs GA4 vs backend (las tres fuentes, ver 66).

**Looker Studio** (gratis de Google) se conecta a TikTok Ads y a GA4 y arma gráficos que se refrescan solos. Es el salto más rentable: montas una vez la plantilla, y cada lunes el reporte (ver 67) casi se escribe solo. Un cliente puede tener el link y verlo cuando quiera — eso vende tu servicio (rutea la relación a `ventas_lushows`).

## Reglas automáticas: el guardián con frenos

Las **reglas automáticas** (ver 63) son condiciones que TikTok ejecuta solo. La filosofía correcta: **automatiza lo defensivo (cortar pérdidas), supervisa lo ofensivo (escalar).** Pausar plata que sangra es seguro de automatizar; escalar mal puede romper el aprendizaje (ver 13), así que escalar lo decides tú.

| Tipo de regla | Ejemplo | ¿Auto o aviso? |
|---|---|---|
| **Defensiva (cortar)** | CPA > 2,5× objetivo Y gasto > umbral → pausar | Auto (segura) |
| **Defensiva (presupuesto)** | Gasto del día > X sin 1 conversión → pausar | Auto |
| **Fatiga** | Frequency > 3,5 → avisar | Aviso (ver 39) |
| **Oportunidad (escalar)** | CPA < objetivo, 3+ conv, estable → avisar | Aviso, tú decides (ver 72) |

Calibración clave: la regla de cortar debe pedir **dos condiciones a la vez** (CPA alto **Y** gasto suficiente). Si solo miras CPA, matas un creativo que llevaba una venta y aún no tenía señal (ver 13). El umbral de gasto es lo que protege a los creativos jóvenes.

## Alertas: enterarte antes de que sea tarde

Las **alertas** te avisan (correo, WhatsApp, Slack) cuando algo se sale de rango, para no tener que estar mirando. Las que valen la pena:

- **Gasto disparado:** la cuenta gastó 2× su promedio diario → revisa ya.
- **Cero conversiones con gasto alto:** algo se rompió (¿píxel caído? ver 62).
- **CPA fuera de rango sostenido:** no un pico, una tendencia.
- **Caída de entrega:** la campaña casi no gasta → puede ser rechazo de anuncio o problema de cuenta (ver 75).

Una alerta de "píxel sin registrar eventos hace 6 horas" te puede salvar un fin de semana entero de gasto ciego (ver 62). Configúralas una vez y olvídate.

## Automatizar sin perder el control

Tres reglas para no cavar tu propia tumba:

1. **Empieza con avisos, no con acciones.** Deja que las reglas te notifiquen una semana. Cuando confíes en que disparan bien, conviértelas en automáticas. Una regla mal calibrada en automático mata ganadores.
2. **Nunca automatices el escalar.** Subir presupuesto reinicia parte del aprendizaje (ver 72, 13); eso lo decides con criterio, no una regla.
3. **Revisa las reglas cada mes.** Tu CPA objetivo cambia con la temporada (ver 77). Una regla de hace 3 meses puede estar pausando con un umbral viejo.

El dashboard te da visión, la automatización te da defensa, pero el **criterio sobre el creativo sigue siendo tuyo** — eso es el 80% (ver 68) y ninguna regla lo reemplaza.

## Errores comunes — blacklist

- **Automatizar el escalar.** Reinicia el aprendizaje y rompe ganadores. Escala a mano con criterio (ver 72, 13).
- **Regla de cortar solo por CPA.** Mata creativos sin señal suficiente. Exige CPA alto **Y** gasto mínimo.
- **Poner reglas en automático sin probarlas.** Una mal calibrada quema ganadores. Empieza avisando.
- **Dashboard que solo muestra datos de TikTok.** Repite el ROAS inflado. Triangula con GA4 y backend (ver 64, 66).
- **No revisar las reglas por meses.** Umbrales viejos pausan con criterios que ya no aplican (ver 77).
- **Sin alerta de píxel/conversiones caídas.** Gastas a ciegas un fin de semana. Configúrala (ver 62).
- **Creer que el dashboard reemplaza tu criterio.** Te da visión, no decisiones; el creativo lo decides tú (ver 68).

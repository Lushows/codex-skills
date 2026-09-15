# 71 — Kill criteria

Lee este módulo cuando estés frente a una keyword, un anuncio o una campaña que "no está funcionando" y no sepas si pausarla o aguantarla. La pregunta no es "¿convirtió?" — es **"¿ya tengo evidencia estadística suficiente para concluir que no convertirá rentablemente?"**. Matar demasiado pronto desperdicia el dinero ya invertido en aprendizaje; matar demasiado tarde sangra presupuesto. Aquí defines reglas frías, escritas de antemano, para no decidir con pánico ni con el dato de un solo día.

Marco: Google captura demanda. Un elemento que no convierte rara vez es "mal anuncio" — casi siempre es **intención equivocada** (la keyword trae gente que no busca lo que vendes) o **conversión rota** (sí vendió pero no se registró). Por eso matar bien empieza por diagnosticar, no por cortar.

## La regla del múltiplo de CPA

El criterio más robusto y sin emoción: **un elemento se mata cuando ha gastado 2–3 veces tu CPA objetivo sin una sola conversión**, y con volumen suficiente para que ese cero signifique algo. La lógica: si tu meta es conseguir una venta por $30.000 COP y un anuncio ya gastó $90.000 sin vender, la probabilidad de que sea rentable es muy baja — la matemática ya habló.

| Elemento | Umbral de gasto sin conversión | Volumen mínimo | Acción |
|---|---|---|---|
| Keyword individual | 2–3× CPA objetivo | ≥ 30–50 clics | Pausar la keyword (no toda la campaña) |
| Anuncio (RSA) dentro de un grupo | el grupo tiene volumen y el RSA pierde claro | grupo con tráfico real | Pausar el peor, dejar 2–3 corriendo |
| Grupo de anuncios | 3× CPA objetivo, varios días | ≥ 1 ciclo de conversión | Pausar grupo, revisar keywords/landing |
| Campaña completa | 3× CPA y ya descartaste tracking/landing | ≥ 2 ciclos | Pausar campaña |
| Activo PMax (imagen/título) | Etiqueta "Bajo" sostenida con volumen | datos suficientes en el grupo | Reemplazar el activo, no la campaña |

Ejemplo GastroLatam: CPA objetivo $8.000 COP (sobre producto de $10.000 — ojo, ahí casi no hay margen; eso es tema de viabilidad, ver `economist_lushows`). Una keyword que gastó $20.000 sin venta y con 40 clics: candidata clara a pausa. La misma keyword con 4 clics: ruido, no decides nada.

## La regla de los dos múltiplos (matar vs. aguantar)

Dos umbrales escritos de antemano evitan tanto el gatillo fácil como el aguante eterno:

| Gasto sin conversión | Estado | Acción |
|---|---|---|
| < 1× CPA | Sin evidencia | Aguantar, dejar correr |
| 1–2× CPA | Zona de observación | Revisar causas reparables (abajo); no matar aún |
| 2–3× CPA | Zona de muerte | Descartar causas reparables → si limpio, pausar |
| > 3–4× CPA | Muerte clara | Pausar ya; aguantar más es quemar plata |

## Antes de matar: descarta las 4 causas reparables

No mates algo que se puede arreglar. Antes de pausar, verifica EN ESTE ORDEN:

1. **¿La conversión está midiendo?** Quizás SÍ convirtió y no lo registró (ver 14-conversion). Revisa GA4, Enhanced Conversions y Consent Mode. Esta es la causa #1 de "falsos muertos" — pausas un ganador porque el tag no disparó.
2. **¿La landing está caída o lenta?** Si la página no carga, tarda o le rompieron el formulario/pago, ningún anuncio convertirá (ver 75-troubleshoot, `desingweb-lushows`). Ábrela tú mismo en móvil.
3. **¿Los términos de búsqueda son basura?** Si la keyword en concordancia amplia (broad) trae búsquedas irrelevantes, el problema no es la keyword — son las negativas que faltan (ver 22-negativas). Limpia antes de matar. En PMax/AI Max esto es aún más frecuente (ver `actualizacion-2026-06`).
4. **¿El volumen es real?** Matar una keyword con 3 clics no es decisión, es ruido. Necesitas suficientes impresiones/clics para que "0 conversiones" signifique algo estadísticamente.

Si las cuatro están limpias y el elemento ya gastó 2–3× CPA, ahí sí: pausa.

## El kill sin pánico: reglas, no emociones

Las decisiones de matar se escriben **antes**, no en el momento del susto:

- **Define el umbral por adelantado** (ej: "pauso toda keyword que gaste 2.5× CPA sin conversión en ≥30 clics"). Puedes automatizarlo con reglas (ver 70-reglas) o scripts de Google Ads.
- **Nunca mates por un solo día malo.** El rendimiento diario oscila enormemente; mira ventanas de 7–14 días (ver 60-metricas).
- **No mates durante la fase de aprendizaje.** Si acabas de lanzar o cambiar algo, los primeros días son erráticos por diseño (ver 13-smart-bidding). Dale 1 ciclo de conversión.
- **Pausa, no borres.** Pausar conserva el historial y los datos; borrar tira el aprendizaje. Pausa siempre primero.
- **Mata granular, no masivo.** Pausa la keyword o el anuncio específico, no la campaña entera, salvo que toda la campaña esté podrida.
- **No mates en plena temporada alta** salvo que esté claramente roto: en Q4 los CPAs suben para todos y un elemento "caro" puede seguir siendo rentable (ver 77-Q4).

Regla de oro emocional: si vas a pausar algo "porque hoy me asusté", para. Vuelve mañana con los datos de 7 días. El 80% de los "hay que matar esto YA" se desinflan con una semana de contexto.

## Qué hacer DESPUÉS de matar

Pausar no es el final. Reasigna: el presupuesto que liberaste va a lo que SÍ funciona (escalar vertical, ver 72) o a probar una hipótesis nueva (horizontal, ver 73). Y registra POR QUÉ lo mataste — para no recrear el mismo perdedor en tres meses. Si matas muchas keywords de un mismo tema, quizás todo el tema (o esa landing, o ese precio) no es viable: súbelo a `economist_lushows`.

## Errores comunes — blacklist

- **Pausar lo que no convirtió ayer.** Un día no es una muestra. El rendimiento rebota; matas algo que iba a convertir mañana (ver 76-mitos).
- **Matar antes de descartar la conversión rota.** Si el tracking falla, estás pausando ganadores que parecen perdedores. Verifica GA4 primero (ver 14-conversion).
- **Borrar en vez de pausar.** Pierdes historial y aprendizaje; si te arrepientes, empiezas de cero.
- **Matar campañas enteras por una keyword mala.** Cirugía de bisturí, no de hacha: pausa el elemento específico.
- **No tener umbral escrito y decidir "a ojo" cada vez.** Sin regla previa, decides con la emoción del día y eres inconsistente.
- **Matar con 3 clics de muestra.** "Cero conversiones en 3 clics" no es evidencia de nada. Necesitas volumen para concluir.
- **Aguantar eternamente un perdedor "por si acaso".** El otro extremo: si ya gastó 4–5× CPA sin nada y descartaste las causas reparables, cortar a tiempo protege el presupuesto para lo que sí funciona.
- **Matar un activo PMax pausando toda la campaña.** Reemplaza el activo "Bajo"; no tires la campaña entera (ver 12-PMax).
- **No reasignar el presupuesto liberado.** Matar sin redirigir la plata desperdicia la decisión; muévela a lo que rinde (ver 72).

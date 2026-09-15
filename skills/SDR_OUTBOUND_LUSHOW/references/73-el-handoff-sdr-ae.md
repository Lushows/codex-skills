# 73 — El handoff SDR → AE

El handoff (traspaso) es el momento en que el SDR entrega un lead calificado (SQL, ver `72`) al AE (Account Executive, el que cierra). Es el punto más frágil de todo el proceso: un handoff pobre hace que el AE llegue a la reunión sin contexto, repita preguntas que el prospecto ya contestó, quede como improvisado y pierda el trato. Un handoff excelente hace que el prospecto sienta continuidad —"ya saben mi caso"— y que el AE entre a cerrar en vez de a empezar de cero. Este módulo te da qué contexto pasar, cómo pasarlo y un checklist para que nada se caiga entre manos.

## El principio: el AE debe llegar sabiendo, no averiguando

El prospecto ya te contó su dolor a ti (SDR). Si el AE se lo vuelve a preguntar, el prospecto piensa "no se hablan entre ellos" y pierde confianza justo antes de comprar. El costo es real: reuniones donde el AE gasta los primeros 10 minutos re-descubriendo lo que tú ya sabías, y tratos que se enfrían por fricción. **Un buen handoff transfiere el conocimiento, no solo el contacto.** Regla: el AE debe poder abrir la reunión con "Andrea, entiendo que estás perdiendo ~2h/día del chef en conteos manuales antes de abrir tu 4º local — cuéntame más de eso", y acertar.

## Qué contexto pasar (el paquete mínimo)

Todo lo que calificaste (ver `70`) más el color humano. Nunca menos que esto:

| Campo | Ejemplo | Por qué lo necesita el AE |
|---|---|---|
| **Quién** | Andrea Gómez, Gerente, Grupo Sazón (3 locales, Bogotá) | Sabe con quién habla y su rol |
| **Dolor / disparador** | Merma de inventario, conteo manual en Excel; abre 4º local en 2 meses | El ángulo de toda la venta |
| **Impacto / números** | ~2h/día del chef; sospecha 8-10% de merma | Munición para el ROI (ver `Matematicas_lushows`) |
| **Autoridad / proceso** | Ella opera; el papá (dueño) firma compras > $2M COP | El AE sabe a quién convencer de verdad |
| **Timing** | Quiere resolverlo antes de la 4ª apertura | Urgencia real para el cierre |
| **Objeciones/dudas ya vistas** | "¿Es complicado de usar?" | El AE las anticipa |
| **Qué prometiste** | Que el AE traería un cálculo de su costo de plato | El AE cumple la promesa (o queda mal) |
| **Fuente + fecha** | Cold email 2-jul; respondió; call 3-jul | Contexto de dónde viene |

## Cómo pasarlo — los tres modos (de mejor a peor)

1. **Warm handoff en vivo (el ideal cuando se puede):** en la misma llamada o reunión, presentas al AE. "Andrea, te presento a Camilo, que te va a mostrar los números de tu caso." Transferencia de confianza instantánea. Úsalo en tickets altos.
2. **Nota estructurada en el CRM + invitación:** llenas los campos de arriba en el registro del lead (ver `77`), etiquetas al AE, y la invitación de calendario lleva el resumen en la descripción. Es el estándar diario.
3. **Mensaje suelto ("te paso este lead, está bueno"):** el peor. Sin estructura, el AE llega ciego. Evítalo.

Para el modo 2, pega esto en la nota del CRM:

```
🤝 HANDOFF SQL → AE
Contacto: Andrea Gómez · Gerente · Grupo Sazón (3 locales, Bogotá) · +57...
Dolor: merma inventario, conteo manual Excel. Abre 4º local en 2 meses.
Impacto: ~2h/día del chef; ~8-10% merma estimada.
Autoridad: Andrea opera; economic buyer = su papá (dueño), firma >$2M COP.
Timing: quiere resolverlo ANTES de la 4ª apertura (≈2 meses).
Objeciones vistas: "¿es difícil de usar?"
Prometí: cálculo de costo de plato con SUS datos en la reunión.
Reunión: jueves 10am (invite enviada). Champion probable: Andrea.
Fuente: cold email 2-jul → call 3-jul.
```

## Checklist de handoff (antes de dar por entregado)

```
□ El lead es SQL de verdad (cumple los 4 criterios, ver 70)
□ La nota de contexto está completa en el CRM (los 8 campos)
□ La reunión está agendada con fecha/hora firmes e invitación enviada
□ El AE recibió aviso (tag, Slack, o warm intro) y CONFIRMÓ que la toma
□ Se confirmó que el/los decisores clave estarán en la reunión
□ Lo que prometiste al prospecto quedó anotado para que el AE lo cumpla
□ El estado del lead en CRM cambió a "Reunión agendada / SQL" (ver 77)
```

Si un ítem falla, no está entregado. Un handoff a medias es peor que ninguno porque genera falsa sensación de avance.

## La frontera con ventas_lushows

Aquí termina tu trabajo de SDR: entregaste un SQL con contexto y reunión firme. **Lo que sigue —el discovery consultivo profundo, el manejo de objeciones a fondo, la propuesta, la negociación y el cierre— es del AE y vive en `ventas_lushows`.** Tú no cierras; tú preparas el cierre para que sea fácil.

## Errores comunes

- **Pasar solo el contacto sin contexto.** El AE re-pregunta todo y el prospecto se enfría.
- **No confirmar que el AE aceptó.** El lead cae en el limbo; nadie lo toma. Espera confirmación (ver `74`).
- **Prometer y no anotarlo.** Dijiste "te traen X" y el AE no sabe → quedas como mentiroso los dos.
- **Handoff de un lead que no era SQL.** Destruyes la confianza del AE en tus reuniones (ver `78`).

## Siguiente paso

Formaliza en el SLA (ver `74`) cuánto tiempo tiene el AE para tomar el SQL y qué pasa si lo rechaza. Registra el traspaso con estado limpio en `77`. Cuando el AE te dé feedback sobre si el lead sirvió, captúralo en `79`.

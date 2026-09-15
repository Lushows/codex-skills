# 143 — Atribución de outbound

La **atribución** responde una pregunta simple con respuesta complicada: *¿qué toque (o toques) generó este deal?*. ¿Fue el cold email? ¿La llamada de seguimiento? ¿El mensaje de LinkedIn? ¿O el anuncio que vio antes de que lo tocaras? En outbound importa por dos razones concretas: para **saber qué canal/mensaje repetir** (invertir donde sí funciona) y para **darle crédito justo al SDR** (que su comp, ver `84`, refleje su aporte real). Sin atribución trabajas a ciegas: escalas lo que crees que funciona, no lo que funciona.

## El principio: el crédito debe seguir a la causa, no a la conveniencia

El error humano por defecto es dar todo el crédito al **último toque** (el que estaba ahí cuando el lead dijo "sí") porque es el más visible. Pero el último toque muchas veces solo cosecha lo que sembraron los anteriores. Una atribución honesta reparte el crédito según **qué realmente movió al lead**, no según qué fue lo último que pasó. En outbound esto es especialmente cierto: el deal casi nunca nace de un solo correo, nace de una **secuencia** de toques (ver `60`).

## Los modelos de atribución

| Modelo | Da el crédito a… | Cuándo sirve | Sesgo |
|---|---|---|---|
| **First-touch (primer toque)** | El toque que originó el lead | Medir qué **abre puertas** (qué canal genera) | Ignora lo que cerró |
| **Last-touch (último toque)** | El toque justo antes del sí | Medir qué **agenda/convierte** | Ignora lo que sembró |
| **Multi-touch lineal** | Reparte igual entre todos los toques | Ver el peso de la secuencia completa | Trata todo igual (no lo es) |
| **Multi-touch ponderado (U/W)** | Más peso al primero y al que agenda | La visión más justa del recorrido | Requiere más datos y reglas |

Para outbound de pyme/solista, la regla práctica: **mide first-touch Y last-touch en paralelo** (son baratos y te dicen "qué abre" vs. "qué cierra"), y sube a multi-touch ponderado solo cuando tu volumen justifique el esfuerzo. No persigas el modelo perfecto; persigue el que cambie tus decisiones.

## Qué atribuir en outbound (los dos niveles)

Atribución no es una sola cosa; opera en dos niveles y no debes mezclarlos:

```
NIVEL 1 — Atribución de CANAL/MENSAJE  (¿qué repito?)
   ¿El SQL vino de cold email, LinkedIn, WhatsApp, cold call? (ver 61)
   ¿Qué secuencia / qué variante A/B lo generó? (ver 65)
   → decide dónde invertir esfuerzo y qué copy escalar

NIVEL 2 — Atribución de FUENTE (source)   (¿outbound o inbound?)
   sql_source = outbound-SDR  vs.  inbound  vs.  paid
   → separa lo que TÚ generaste de lo que llegó solo o por ads
   → clave para el ROI del outbound (ver 149) y para no robarle
     crédito a marketing/ads ni que te lo roben a ti
```

El campo `sql_source` en el Deal (ver `141`) es la pieza mínima e innegociable: sin él no sabes cuánto pipeline es realmente tuyo. Si el lead vio un anuncio antes, eso es atribución compartida con las skills de ads (`facebook_ads`, `google_ads`) —recónócelo, no te apropies todo el crédito.

## El cómo, paso a paso

1. **Sella la fuente al crear el Deal.** En el momento del SQL, `sql_source = outbound-SDR` y `sdr_owner = quién lo agendó`. Si no se sella ahí, se pierde para siempre.
2. **Registra cada toque como Activity.** Correos, llamadas, LinkedIn, WhatsApp cuelgan del Contact/Deal con fecha y canal (ver `141`). Esa es la materia prima; sin toques registrados no hay atribución posible.
3. **Marca el first y el last.** El primer Activity del lead = first-touch; el Activity justo antes del "agendó" = last-touch. Muchos CRM lo calculan solos si los toques están registrados.
4. **Etiqueta la campaña/variante.** Cada toque lleva de qué secuencia y qué variante A/B vino (ver `65`), para atribuir a nivel mensaje.
5. **Cierra el loop con el resultado.** Cuando el Deal cierra ganado/perdido, esa info sube por la cadena: ¿qué first-touch/canal/mensaje produce los que **sí cierran**, no solo los que agendan? (ver `79`).

## Ejemplo: recorrido atribuido de un deal

```
Lead: Ana Gómez — Restaurante La Brasa
  T1  02-jun  cold email v-B (secuencia "gastro-señal")   ← FIRST-TOUCH
  T2  05-jun  LinkedIn (conexión + nota)
  T3  09-jun  cold email follow-up (bump)
  T4  12-jun  WhatsApp: respondió "cuéntame más"
  T5  13-jun  cold call: agendó reunión                    ← LAST-TOUCH
  ───────────────────────────────────────────────
  DEAL creado: sql_source = outbound-SDR · sdr_owner = Luis
  Cerrado GANADO 28-jun · margen $1.500

LECTURA:
  First-touch → cold email v-B abre puertas (repetir esa variante, 65)
  Last-touch  → la cold call cierra la agenda (la llamada sí paga, 58)
  Multi-touch → el recorrido email→LinkedIn→WhatsApp→call funciona junto (61)
  Fuente      → 100% outbound, sin ads de por medio → crédito limpio al SDR
```

De un solo deal no concluyas nada; de 30 deals atribuidos así **ves el patrón** de qué combinación produce clientes.

## Errores comunes

- **Solo last-touch.** Le das todo el crédito a la llamada final y matas la inversión en el cold email que abrió la puerta.
- **No sellar `sql_source`.** Meses después nadie sabe qué pipeline fue outbound → imposible calcular ROI (`149`).
- **No registrar los toques.** Sin Activities, la atribución es adivinanza.
- **Robar/regalar crédito entre equipos.** Si el lead vio un ad y tú lo tocaste, es compartido —pelear por el 100% envenena la relación con marketing/ads y distorsiona en qué invertir.
- **Perseguir el modelo perfecto.** Un multi-touch elegante que nadie mantiene vale menos que first+last bien puestos.

## La frontera

La atribución **mide** qué toque generó el deal; convertir ese aprendizaje en **más ventas** (mejor copy, mejor secuencia) usa `65` y `60`, y el cierre humano sigue en `ventas_lushows`. El reparto exacto de crédito ponderado (los porcentajes del modelo U/W) y la significancia de "este canal sí es mejor" → `Matematicas_lushows`. Ligar la atribución al CAC por canal → `149`. Atribución compartida con demanda pagada → las skills de ads.

## Siguiente paso

Añade `sql_source` a tus Deals hoy y empieza a registrar los toques como Activities (`141`). Mide first-touch y last-touch en paralelo un mes y compara: qué **abre** vs. qué **cierra**. Lleva ese patrón al A/B testing (`65`) y al forecast (`145`). Para el crédito ponderado exacto → `Matematicas_lushows`; para el CAC por canal que sale de esto → `149`.

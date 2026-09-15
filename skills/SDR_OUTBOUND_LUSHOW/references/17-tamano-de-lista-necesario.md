# 17 — Tamaño de lista necesario (cuántas cuentas necesitas de verdad)

La pregunta que todo el mundo hace mal: "¿cuántos correos mando?". La correcta: "**¿cuántos contactos necesito en la lista para llegar a mi meta de reuniones?**". Se resuelve al revés — desde la meta hacia atrás, aplicando las tasas de conversión de cada etapa del embudo de outbound. Este cálculo te dice si tu SAM (`13`) alcanza, cuánta infraestructura de envío necesitas (`44`) y si tu meta es realista o fantasía. Es la **ecuación del pipeline** (`05`) aplicada a dimensionar la lista.

## El embudo de outbound y sus tasas (2026, benchmarks realistas)

Cada etapa filtra. Estos rangos son defendibles para cold email B2B bien hecho en 2026 (varían por nicho, calidad de lista y deliverability):

| Etapa | Tasa típica (buena ejecución) | Nota |
|---|---|---|
| Contactos en lista → correos entregados | 90–95% | Depende de verificación (`28`) y deliverability (`40`) |
| Entregados → **reply rate** (cualquier respuesta) | 3–8% | Frío puro. Con señal/personalización sube (`14`, `52`) |
| Replies → **positive reply** (interesados) | 25–40% de las respuestas | El resto son "no"/"quítame" |
| Positive reply → **reunión agendada** | 40–60% | Manejo de respuesta y booking (`64`, `69`) |
| Reunión agendada → **reunión realizada** (show) | 60–80% | Los no-shows pican (`75`) |

Multicanal (email + LinkedIn + WhatsApp/llamada) **sube el reply efectivo** frente a un solo canal (ver `61`). Los números de abajo son para email como canal base.

## El cálculo, de la meta hacia atrás (paso a paso)

1. **Define la meta:** reuniones **realizadas** por mes (no agendadas — las que de verdad ocurren).
2. **Sube etapa por etapa** dividiendo por cada tasa:
   - Reuniones realizadas ÷ (show rate) = reuniones agendadas
   - Agendadas ÷ (positive→meeting) = positive replies
   - Positive ÷ (reply→positive) = replies totales
   - Replies ÷ (reply rate) = correos entregados
   - Entregados ÷ (deliverability) = **contactos necesarios en lista**
3. **Añade el margen de seguridad:** multiplica el resultado ×1.3–1.5 (la realidad siempre es peor que el benchmark las primeras campañas).
4. **Cruza con capacidad de envío:** ¿ese volumen mensual cabe en tus buzones sin quemarlos? (ver límites en `44`).
5. **Cruza con tu SAM (`13`):** ¿existen esas cuentas? Si necesitas más contactos de los que hay, tu meta o tu ICP deben cambiar.

## Ejemplo de cálculo completo (worked example)

```
META: 10 reuniones REALIZADAS por mes.

Tasas asumidas (conservadoras):
  show rate                 70%
  positive → meeting        50%
  reply → positive          30%
  reply rate                5%
  entregados/enviados       92%

Cálculo hacia atrás:
  Reuniones realizadas          = 10
  Agendadas    = 10 / 0.70      ≈ 15
  Positive rep = 15 / 0.50      = 30
  Replies      = 30 / 0.30      = 100
  Entregados   = 100 / 0.05     = 2.000
  Contactos    = 2.000 / 0.92   ≈ 2.174

  + margen ×1.4                 ≈ 3.043 contactos/mes en lista

CAPACIDAD DE ENVÍO NECESARIA:
  ~2.174 correos entregados/mes (primer toque). Con follow-ups (3–4 toques,
  ver 60) el volumen de ENVÍOS es varias veces mayor.
  A ~30 correos/buzón/día seguro (ver 44) y ~22 días hábiles ≈ 660 envíos/
  buzón/mes → necesitas varios buzones. (Calcula el nº exacto según tu
  secuencia y toques.)
```

⚠️ Este cálculo mueve decisiones de plata (cuántos buzones comprar, si la meta es viable). **Ejecútalo y verifícalo con `Matematicas_lushows`** con TUS tasas reales — no uses los benchmarks de memoria como si fueran verdad. Aquí damos el método y un ejemplo ilustrativo; el número que uses para decidir se calcula.

## Cómo leer el resultado

- **Si necesitas más contactos que tu SAM (`13`):** tu meta es imposible con outbound puro en ese nicho. Opciones: bajar la meta, ampliar el ICP/nicho (`12`), o sumar inbound/ads (rutea a las skills de ads).
- **Si el volumen de envío supera tu infraestructura:** necesitas más buzones/dominios (`41`, `110`) o mejorar las tasas (mejor lista + mejor copy suben el reply rate y reducen la lista necesaria).
- **La palanca más barata no es más volumen: es mejor tasa.** Duplicar tu reply rate (mejor targeting `10`/`16` + mejor copy `50`) **reduce a la mitad** la lista y la infraestructura que necesitas. Antes de comprar 10 buzones más, mejora la lista y el mensaje.

## Regla rápida (para estimar en la cabeza)

Como orden de magnitud grueso para cold email frío: **≈ 200–300 contactos por reunión realizada** (varía mucho por nicho y ejecución). Si quieres 10 reuniones/mes, piensa en el orden de **~2.000–3.000 contactos/mes**. Úsalo solo para dimensionar rápido; el número real sale de tus propias tasas.

## Errores comunes

- **Calcular sobre reuniones agendadas, no realizadas:** ignoras los no-shows y te quedas corto.
- **Usar tasas optimistas** (reply rate 15%): casi nadie lo logra en frío; planifica conservador.
- **Olvidar el margen de seguridad:** las primeras campañas rinden peor.
- **No cruzar con la infraestructura de envío:** pides un volumen que quema tus dominios (`44`).
- **Confundir "contactos" con "correos enviados":** con 3–4 toques por contacto, los envíos son un múltiplo de los contactos.

## Frontera y siguiente paso

La **ecuación del pipeline** completa (actividad → revenue) está en `05`; el **forecasting** desde outbound en `82`. La **capacidad de envío segura** en `44`. El **CAC por reunión / economía** del outbound en `149` y, a nivel negocio, en **`economist_lushows`**. Todo **cálculo exacto** → **`Matematicas_lushows`**.

**Siguiente paso:** corre este cálculo con tu meta real y tus tasas (o los benchmarks si aún no las tienes), verifica con Matematicas, y contrasta contra tu SAM (`13`) y tu capacidad de envío (`44`).

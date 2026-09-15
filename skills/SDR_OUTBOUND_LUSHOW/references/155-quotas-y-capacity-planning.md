# 155 — Cuotas y capacity planning

La cuota mal puesta es el error de gestión más caro en outbound: demasiado alta quema a tu mejor gente y dispara la rotación (ver `159`); demasiado baja deja pipeline sobre la mesa y te hace contratar de más. La cuota correcta se **calcula desde la capacidad real** de un SDR y desde la necesidad del negocio, no se inventa ni se copia del vecino. Este módulo es el modelo de capacity planning: cuánto puede producir de verdad un SDR, cómo traducir eso a una cuota alcanzable, y cómo dimensionar el equipo para una meta de pipeline. El diseño de la comisión que paga esa cuota → `154`; los cálculos exactos → `Matematicas_lushows`.

## El principio: la cuota nace de la capacidad, no del deseo

Muchos fijan la cuota por lo que *necesitan* facturar ("necesito 50 SQL, repártelos"). Eso es un deseo, no un plan. La cuota realista se construye de abajo hacia arriba, desde lo que un SDR **físicamente puede hacer bien** en un día, y luego se contrasta con la necesidad. Si el deseo supera la capacidad, la respuesta no es exprimir al SDR —es **contratar más SDRs** o **mejorar la conversión** del embudo (ver `83`), no subir la vara hasta que se quiebre.

**Regla de calibración:** una cuota bien puesta la alcanza el **~70–80% del equipo** con esfuerzo. Si la alcanza el 100%, está baja (dejas pipeline). Si no la alcanza casi nadie, está alta y quema gente.

## Paso 1 — El modelo de capacidad diaria

Cuánto puede producir un SDR sale de cuánta actividad *de calidad* cabe en su día, no de cuántos correos puede disparar. La calidad (personalización relevante, ver `52`) limita el volumen:

```
Día laboral de un SDR ≈ 6–7 horas productivas (el resto: reuniones, admin, 67).

Toques de calidad/día:
  Email personalizado a escala:   ~40–80/día  (con Clay/plantillas, ver 31, 52)
  Llamadas en frío:               ~40–60 marcaciones/día → ~5–10 conversaciones
  LinkedIn (conexión + mensaje):  ~20–30/día  (límites de la plataforma, ver 57)

Multicanal combinado (email + call + LinkedIn + WhatsApp, ver 61):
  ~80–120 toques totales de calidad/día
  → ~1.500–2.000 contactos NUEVOS tocados/mes (descontando follow-ups)
```

Ojo con los límites técnicos: no puedes enviar cientos de correos por buzón sin quemar deliverability (~30–50 envíos/día por buzón, ver `40`, `44`). La capacidad de email la fija tu infraestructura de buzones, no las ganas del SDR.

## Paso 2 — De capacidad a cuota (baja por el embudo)

Aplica tus tasas de conversión reales (ver `81`, `83`) a la capacidad para llegar al output esperado en SQL:

```
Contactos nuevos/mes:        ~1.500–2.000   (paso 1)
× Reply rate positivo:       ~1–3%          (benchmark 80)
× % de replies → reunión:    ~40–60%
× % reuniones → SQL:         ~50–70%        (calificadas, aceptadas por AE)
─────────────────────────────────────────
= Cuota realista SDR maduro: ~15–30 SQL/mes
```

Este rango (~15–30 SQL/mes por SDR post-ramp) es el ancla del `84` y del `154`. Tu número exacto depende de *tus* tasas —calcúlalo con las tuyas, no con el promedio, y verifícalo en `Matematicas_lushows`. Si tu embudo convierte peor, la palanca es arreglar la conversión (`83`), no subir la cuota.

## Paso 3 — Cuota rampada para nuevos

Un SDR nuevo no produce como uno maduro (ver `86`). Su cuota es **rampada**, no plena, o lo quemas antes de que arranque:

| Mes | Cuota | Por qué |
|---|---|---|
| Mes 1 | ~25% | Aprende producto/ICP/stack; produce poco a propósito |
| Mes 2 | ~60% | Ejecuta con supervisión y corrige |
| Mes 3 | ~100% | Autónomo, a ritmo |

La comisión durante el ramp se ajusta o garantiza (ver `154`). Fijar cuota plena desde el día 1 es la causa #1 de rotación temprana evitable.

## Paso 4 — Capacity planning del equipo (cuántos SDRs necesitas)

De la cuota individual sales al dimensionamiento del equipo, partiendo de la meta de pipeline del negocio:

```
Ejemplo:
  Meta de la empresa:        90 SQL/mes para el equipo de AEs
  Cuota SDR maduro:          20 SQL/mes  (paso 2)
  → SDRs maduros necesarios: 90 / 20 = 4.5 → 5 SDRs

  Ajustes al número real:
  + Ramp:      un SDR nuevo produce ~parcial 3 meses → cubre con más cabezas o antelación
  + Rotación:  si rota ~30–40%/año (159), planea reemplazos con anticipación (151)
  + No todos rinden a cuota: solo ~70–80% la alcanza → margen extra

  → Plantilla realista:  ~6 SDRs para asegurar 90 SQL/mes sostenidos
```

También revisa el ratio SDR:AE (ver `150`): de nada sirven 6 SDRs llenando agendas si solo tienes 2 AEs para atender esos SQL. La capacidad del eslabón siguiente (los AEs) es parte del plan. Los cálculos exactos de plantilla, ramp y cobertura → `Matematicas_lushows`.

## Territorio y reparto de cuentas (evita el canibalismo)

Cuando hay varios SDRs, reparte el universo de cuentas para que **no le escriban dos al mismo prospecto** (mata la reputación y hace quedar mal a la marca):

- **Por segmento/industria:** cada SDR es dueño de un nicho (ver `12`). Se especializa y personaliza mejor.
- **Por territorio geográfico:** por país/región. Útil en LatAm por diferencias de mercado (ver `08`).
- **Por tamaño de cuenta (tiering):** enterprise vs. mid-market (ver `16`). Los enterprise exigen más toques por deal → cuota en SQL más baja pero de mayor valor.

Sea cual sea, que quede escrito en el CRM quién es dueño de cada cuenta (ver `77`), o tendrás dos SDRs quemando al mismo lead.

## Errores comunes

- **Fijar la cuota por lo que necesitas facturar, no por capacidad.** Deseo ≠ plan; quiebra al equipo.
- **Cuota que nadie alcanza.** Mal calibrada; quema y dispara rotación (ver `159`). Apunta a que el 70–80% la logre.
- **Cuota plena desde el día 1.** Ignora el ramp (ver `86`).
- **Contar volumen que la deliverability no aguanta.** El límite de buzones es real (ver `44`); no cuentes correos fantasma.
- **No dimensionar los AEs.** SDRs llenando agendas que nadie atiende = SQL desperdiciados (ver `150`).
- **Sin reparto de cuentas.** Dos SDRs al mismo prospecto queman la marca (ver `77`).
- **Subir la cuota en vez de arreglar la conversión.** Si el embudo convierte mal, apriétalo (`83`), no al SDR.

## Siguiente paso

Construye tu modelo de capacidad con *tus* tasas (paso 1→2), fija la cuota donde el 70–80% pueda alcanzarla, y rampa a los nuevos (`86`). Dimensiona el equipo desde la meta de pipeline sin olvidar el ratio SDR:AE (`150`) y la rotación (`159`, `151`). Reparte cuentas por segmento/territorio en el CRM (`77`). Con la cuota fijada, diséñale la comisión que la premia → `154`. Todos los cálculos exactos (capacidad, plantilla, cobertura, ramp) → `Matematicas_lushows`; si el costo del equipo cabe en el negocio → `economist_lushows`.

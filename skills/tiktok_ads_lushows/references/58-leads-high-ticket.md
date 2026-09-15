# 58 — Leads high-ticket

Lee este módulo cuando vendas algo caro que necesita conversación (servicios, asesorías, inmuebles, maquinaria, cursos premium, B2B, software), cuando tus leads de TikTok lleguen baratos pero **nadie compre**, o cuando un cliente diga "me llegan 100 mensajes y no cierro ninguno". En high-ticket, TikTok es una mina de curiosos si lo dejas suelto. El oficio aquí es **pagar por leads calificados, no por curiosos**. Menos leads, mejores leads. El frame manda doble: TikTok es **descubrimiento** (ver 00), el usuario está en el punto MÁS frío del embudo; vender algo caro a alguien frío exige filtrar fuerte y conversar después.

## Por qué TikTok castiga el high-ticket mal hecho

TikTok es plataforma de **descubrimiento**: la gente entra a entretenerse, no a comprar un servicio de $3.000.000 COP. El usuario está en el modo más frío del embudo. Si optimizas como si fuera impulso, pasa esto:

- El algoritmo, optimizando por **clic o lead barato**, te trae al que llena cualquier formulario por curiosidad.
- Llegan 100 leads a $2.000 COP (CPL irresistible).
- 90 no tenían plata, intención ni urgencia.
- Tu equipo se quema persiguiendo basura y deja de confiar en TikTok.

El error de raíz: **mirar el CPL** (costo por lead). En high-ticket el CPL barato es una trampa. La métrica real es el **costo por lead calificado** (un lead que puede pagar y quiere avanzar) y, al final, el **CAC** (costo de adquisición de cliente — valida unit economics con `economist_lushows`).

| Métrica | High-ticket bien hecho | La trampa |
|---|---|---|
| CPL | Más alto (a propósito) | Bajo = curiosos |
| Costo por lead **calificado** | Lo que mides | Ignorado |
| Tasa de cierre del lead | Alta | Miserable |
| CAC final | Sano vs. ticket | Insostenible |

### El cálculo que convence al cliente

Compara dos campañas con el mismo gasto de $1.000.000 COP:

| | Campaña A (CPL barato) | Campaña B (lead calificado) |
|---|---|---|
| CPL | $2.000 | $20.000 |
| Leads | 500 | 50 |
| % calificados | 5% (25) | 60% (30) |
| Leads calificados | 25 | **30** |
| Cierre sobre calificados | 10% | 20% |
| Clientes | 2–3 | **6** |
| CAC | ~$400.000 | ~$167.000 |

La campaña con CPL 10x más caro **cierra más clientes y a menor CAC**, porque filtra. Esto es lo que hay que mostrarle a un cliente que se enamora del CPL bajo.

## Fricción intencional: el formulario que filtra

En high-ticket, **la fricción es tu aliada**. Quieres que el curioso se caiga y solo pase el que va en serio. Cómo construir esa fricción (sobre instant forms, ver 54):

1. **Pregunta de calificación dura.** "¿Cuál es tu presupuesto?", "¿Ya tienes el negocio operando?", "¿Para cuándo lo necesitas?". El que no califica, no llena.
2. **Form de mayor esfuerzo** (tipo "More info" en vez de "Instant"): obliga a escribir, no solo confirmar el teléfono prellenado.
3. **Creativo que pre-filtra.** Si el video dice "asesoría para restaurantes que ya facturan más de $X al mes", el que no aplica no toca. El creativo hace el primer filtro (ver 30, 48).
4. **Agendamiento como filtro.** En vez de "déjanos tu número", pide "agenda una llamada de 20 min" (link a Calendly/agenda). Agendar es un acto de intención — el curioso no agenda. Esto sube brutal la calidad del lead.

Regla: en high-ticket prefieres **20 leads que agendaron** a 200 que solo dejaron el número. Menos volumen, más cierre.

### Escalera de calificación (de frío a caliente)

| Nivel de filtro | Acción que pides | Calidad |
|---|---|---|
| Bajo | Instant form, solo teléfono | Curiosos |
| Medio | Form "More info" + 1 pregunta dura | Tibios |
| Alto | Agendar llamada / responder 2-3 preguntas | Calientes |
| Máximo | Agendar + pre-pago simbólico o aplicación | Muy calientes |

Sube de nivel hasta donde tu volumen aguante: si subes demasiado y te quedas sin leads, baja un escalón.

## Medir y optimizar por lead calificado

No basta con filtrar — hay que **enseñarle al algoritmo qué es un lead bueno**:

1. **Define el lead calificado** en tu CRM (presupuesto + intención + agendó).
2. **Sube esa conversión "lead calificado" de vuelta a TikTok** vía Events API con el `ttclid` (loop cerrado, igual que la compra — ver 57). No subas "lead", sube "lead calificado".
3. **Optimiza la campaña por ese evento profundo**, no por el formulario llenado (ver 14).

Así el algoritmo deja de buscar "el que llena forms" y empieza a buscar "el que agenda y puede pagar". El CPL sube, pero el costo por **cliente** baja — que es lo único que paga las cuentas.

Velocidad sigue mandando: aun en high-ticket, contacta en **<5 min** (ver 54). Y el cierre de la conversación —la llamada, las objeciones de precio "está muy caro", la negociación— es `ventas_lushows` (módulos de objeciones y high-ticket; el cierre por WhatsApp es el 82). Para B2B con ciclo largo, métodos como MEDDIC/SPIN viven en `ventas_lushows`.

## Rutas a skills hermanas

- Cierre, objeciones de precio, negociación high-ticket, B2B → `ventas_lushows` (módulo 82 y los de objeciones/high-ticket).
- Validar CAC vs LTV y unit economics → `economist_lushows`.
- Instant forms / fricción / regla de 5 min → 54.
- Subir lead calificado de vuelta a TikTok → 57.
- Lead/call ads equivalentes en Meta → `facebook_ads_lushows`; en Google → `google_ads_lushows`.
- Landing de agendamiento / aplicación → `desingweb-lushows`.

## Errores comunes — blacklist

- **Perseguir el CPL más bajo.** En high-ticket el lead barato es curioso; mide costo por lead calificado.
- **Form "Instant" sin pregunta de calificación.** Te inunda de basura; agrega fricción dura (ver 54).
- **Optimizar por formulario llenado en vez de lead calificado.** El algoritmo trae curiosos; sube el evento profundo (ver 57).
- **Vender high-ticket por checkout impulsivo (VSA/Shop).** No se compra de impulso; usa lead + agendamiento (ver 51).
- **No usar agendamiento como filtro.** Pierdes el mejor filtro de intención; pide agendar.
- **Pasar todos los leads a ventas sin calificar.** Quemas al equipo; filtra antes (ver `ventas_lushows`).
- **No validar el CAC contra el ticket.** Puede que no cierre la unit economics; valida con `economist_lushows`.
- **Subir demasiado la fricción y quedarte sin leads.** Calibra la escalera de calificación según tu volumen.

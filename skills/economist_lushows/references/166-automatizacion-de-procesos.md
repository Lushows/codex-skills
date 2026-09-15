# 166 — Automatización de procesos

Cómo dejar de hacer a mano lo repetitivo: flujos, integraciones y herramientas no-code para liberar horas, reducir errores y escalar sin contratar de más. No es "ponerle IA a todo": muchas veces lo que ahorra más es un simple enlace entre dos apps.

## Primero: 3 verbos antes de automatizar
Antes de automatizar una tarea, decide cuál de estos aplica (en este orden):

1. **Eliminar** — ¿se puede dejar de hacer? La tarea más barata es la que no existe. Reportes que nadie lee, aprobaciones inútiles, campos que nadie usa.
2. **Simplificar / estandarizar** — reduce pasos y excepciones ANTES de automatizar. Automatizar un caos solo te da un caos más rápido.
3. **Automatizar o delegar** — solo lo que queda. Automatizar si es repetitivo, con reglas claras y alto volumen. Delegar a una persona si requiere criterio, empatía o juicio (ver 173 sobre delegar, 86 sobre construir equipo).

> Regla de oro: nunca automatices un proceso que no entiendes a mano. Si tú no sabes hacerlo paso a paso, la máquina tampoco.

## ¿Qué vale la pena automatizar? (matriz)
Cruza **frecuencia** × **esfuerzo manual**:

| | Esfuerzo bajo | Esfuerzo alto |
|---|---|---|
| **Frecuencia alta** | Automatizar primero (gana rápido) | Automatizar / rediseñar (gana grande) |
| **Frecuencia baja** | Dejar manual | Documentar y delegar; automatizar solo si crece |

Candidatos típicos en una PyME:
- Copiar datos de un lado a otro (formulario → hoja → CRM → factura).
- Responder lo mismo una y otra vez (FAQs, confirmaciones, recordatorios).
- Recordatorios y seguimientos (cobranza, recompra, citas — ver 89).
- Reportes que se arman manual cada semana/mes.
- Alta de clientes/proveedores, tareas administrativas repetidas.

## El abanico de herramientas (de menos a más técnico)
No necesitas programar. De menor a mayor capacidad:

1. **Plantillas y atajos** — respuestas guardadas, plantillas de documentos, snippets. Costo casi cero.
2. **Funciones nativas de tus apps** — reglas de WhatsApp Business, automatizaciones de tu CRM, fórmulas y validación en hojas de cálculo.
3. **No-code de bases de datos** — Airtable, Notion, Google Sheets + scripts. Para flujos con datos.
4. **Conectores entre apps (iPaaS)** — Zapier, Make, n8n. "Cuando pase X en la app A, haz Y en la app B." El caballo de batalla.
5. **Chatbots / agentes** — para atención y filtrado (como Addrian del proyecto BIO-SETA).
6. **Código a medida** — webhooks, scripts, mini-servidores. Más poder, más mantenimiento (ver 87 sobre stack de herramientas).

Empieza siempre por el escalón más bajo que resuelva el problema. Subir de nivel = más costo y más cosas que se rompen.

## Anatomía de un flujo automatizado
Todo flujo tiene la misma estructura:

- **Disparador (trigger):** qué lo arranca (nuevo formulario, mensaje, fecha, pago recibido).
- **Condiciones (filtros):** cuándo sí y cuándo no (solo pedidos > $X, solo de tal ciudad).
- **Acciones:** qué hace (crear registro, enviar mensaje, notificar, mover dato).
- **Manejo de errores:** qué pasa si falla (reintento, avisar a un humano). ESTO es lo que diferencia un juguete de algo confiable.
- **Punto de escape humano:** siempre debe haber forma de que una persona tome el control (igual que "pausar IA" en el bot).

## ROI de automatizar — la cuenta que decide
Fórmula simple para saber si vale la pena:

```
Ahorro anual  = horas_ahorradas_por_mes × 12 × costo_por_hora
Costo anual   = setup (una vez) + licencias_mensuales × 12 + mantenimiento
ROI (%)       = (Ahorro anual − Costo anual) / Costo anual × 100
Payback (meses) = Costo del setup / Ahorro mensual
```

**Ejemplo numérico (cifras ILUSTRATIVAS, ajústalas a tu país y a tu caso — ver 21 para conseguir datos reales):**
- Tarea: copiar pedidos de WhatsApp a una hoja y mandar confirmación. Hoy toma **2 h/día**, 26 días/mes = **52 h/mes**.
- Costo de esa hora (lo que pagas o lo que vale tu tiempo): supongamos **$5/hora** → 52 × 5 = **$260/mes** de costo oculto.
- Automatizas con un conector: **setup $300** (una vez, 2 días de trabajo) + **$30/mes** de licencia.
- Tras automatizar, la tarea baja a **5 h/mes** (revisar excepciones). Ahorro = 47 h × $5 = **$235/mes**, menos $30 de licencia = **$205/mes neto**.
- **Payback** = $300 / $205 ≈ **1,5 meses**. ROI primer año ≈ ($205×12 − $300) / ($300 + $360) ≈ **273%**.

Si el payback es menor a ~6 meses y la tarea es estable: automatiza. Si pasa de 18 meses o el proceso cambia mucho, probablemente no.

## El costo escondido: errores y consistencia
El ahorro no es solo tiempo. Hacer a mano = errores: un dato mal copiado, una confirmación olvidada, un cobro que no se mandó. Pon número:
- Si 1 de cada 50 pedidos se pierde por olvido y cada pedido vale **$20**, con 200 pedidos/mes son **4 pedidos = $80/mes** que se fugan. Automatizar el recordatorio recupera buena parte de eso (ver 89 sobre retención y recompra).

## Cómo empezar — mínimo viable de automatización
1. Lista tus 5 tareas más repetitivas de la semana (anótalas un par de días con su tiempo real).
2. Pásalas por los 3 verbos (eliminar / simplificar / automatizar-delegar).
3. Elige **UNA** con buen ROI y bajo riesgo. No automatices diez cosas a la vez.
4. Dibuja el flujo en papel: disparador → condición → acción → qué hago si falla.
5. Constrúyelo en la herramienta más simple posible.
6. **Corre en paralelo** una semana (manual + automático) para verificar que coincide.
7. Documenta cómo apagarlo y quién lo vigila. Recién entonces dejas el manual.

## Errores comunes
- **Automatizar el caos:** no estandarizaste antes; ahora el error se multiplica más rápido.
- **Sin plan B humano:** el flujo falla un domingo y nadie se entera hasta el lunes. Siempre alerta a una persona ante error.
- **Sobre-ingeniería:** montar código a medida para algo que un conector resolvía en 1 hora.
- **No medir el ahorro real:** "automaticé" pero nadie sabe cuántas horas se ganaron. Sin número, no sabes si valió.
- **Depender de la herramienta:** si todo vive en una app y mañana sube de precio o cierra, te quedas atado. Guarda tus datos exportables (ver 95).
- **Automatizar lo emocional:** cobranza dura o quejas sensibles automatizadas suenan frías y queman clientes. Eso se delega a un humano (ver 87).
- **Fantasma del "lo hago después":** dejar el flujo sin dueño que lo revise. Todo automatismo necesita un responsable.

## Checklist antes de soltar un flujo a producción
- [ ] ¿Sé hacerlo a mano y está estandarizado?
- [ ] ¿El ROI da (payback < ~6 meses)?
- [ ] ¿Tiene manejo de error + alerta a humano?
- [ ] ¿Hay escape manual / pausa?
- [ ] ¿Lo probé en paralelo y coincidió?
- [ ] ¿Está documentado y tiene dueño?
- [ ] ¿Mis datos son exportables si cambio de herramienta?

## Nota país
Si la automatización toca **facturación, impuestos, datos personales de clientes o cobros**, las reglas cambian por país (facturación electrónica obligatoria, protección de datos, qué puedes enviar por WhatsApp sin consentimiento). Antes de automatizar eso: **pregunta país/ciudad primero** y verifica la norma vigente — no asumas. Lo demás (flujos internos, recordatorios) es libre.

## Siguiente paso típico
Toma tu tarea repetitiva #1, mídela en horas/mes esta semana y calcula su ROI con la fórmula de arriba. Si el payback baja de 6 meses, automatiza solo esa con la herramienta más simple y corre en paralelo una semana antes de confiar.

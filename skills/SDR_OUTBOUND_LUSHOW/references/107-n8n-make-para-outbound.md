# 107 — n8n y Make para outbound

Tu stack de outbound son varias herramientas que no se hablan solas: la fuente de datos (Sales Nav, Apollo), el enriquecedor (Clay), el sequencer (Instantly/Smartlead), el CRM (HubSpot). El **pegamento** que las conecta —"cuando pasa X en una, haz Y en la otra"— son las herramientas de automatización **n8n** y **Make** (antes Integromat). Este módulo te enseña a montar ese pegamento con flujos concretos, para que tu máquina corra sola en vez de que tú copies CSVs a mano entre apps. Es la ejecución práctica de las integraciones que el `34` describe a nivel concepto.

## El principio: workflows de nodos (trigger → acciones)

Tanto n8n como Make funcionan igual: un **workflow** es una cadena de **nodos**. El primero es un **trigger** (un disparador: "llega un webhook", "cada hora", "nuevo lead en HubSpot") y los siguientes son **acciones** (llama a esta API, transforma este dato, escribe en aquella app). Conectas los nodos visualmente, sin programar casi nada. Eso te deja automatizar el "trabajo de pegar" que consume horas: mover leads, disparar enriquecimiento, escribir respuestas de vuelta al CRM, avisar por Slack/WhatsApp.

| Herramienta | Modelo | Fuerte en | Precio aprox 2026 |
|---|---|---|---|
| **n8n** | Open-source, self-host o cloud | Flexible, barato a volumen, nodos de código, **self-host = datos tuyos** | Self-host gratis; cloud desde ~$20–50/mes |
| **Make** | SaaS visual (no-code puro) | Muy visual, fácil, miles de apps listas | Free limitado; pago desde ~$9–29/mes |
| **Zapier** | SaaS no-code | El más apps/soporte, pero **caro a volumen** | Desde ~$20/mes, escala caro por tarea |

Para outbound a volumen, **n8n gana** (autohospedado sale casi gratis y no te cobra por cada operación); Make es más amable si no eres técnico y el volumen es bajo. Zapier es cómodo pero se vuelve caro rápido cuando procesas miles de leads.

## Los conectores que importan en outbound

Casi todo se pega por dos vías (ver `34`):
- **Webhook** — una app "avisa" a otra con un HTTP POST. Clay, Instantly, Smartlead y HubSpot pueden **enviar** y **recibir** webhooks. Es la vía #1.
- **API / HTTP request** — un nodo que llama a la API de la app (crear campaña en Smartlead, revelar dato, escribir en el CRM). La API de Smartlead (ver `104`) y HubSpot (ver `105`) son las que más usarás.

## Flujos concretos que deberías tener

**1) Clay enriquece → Smartlead lanza (la cinta transportadora)**
```
Trigger:  Webhook desde Clay (fila terminó de enriquecerse y verificarse, ver 101)
Nodo 2:   Filtrar → solo si email_status = "valid" Y tier ∈ {A,B} (ver 16, 28)
Nodo 3:   HTTP → API de Smartlead: añadir lead a la campaña correcta (ver 104)
Nodo 4:   HTTP → crear/actualizar contacto en HubSpot (fuente de verdad, ver 105)
Nodo 5:   Slack/WhatsApp → "Lead X cargado a campaña Y"
```

**2) Respondió en el sequencer → alerta + CRM (no perder al caliente)**
```
Trigger:  Webhook desde Instantly/Smartlead: "reply received" + categoría "interesado"
Nodo 2:   Actualizar contacto en HubSpot: lead status = "Connected", crear tarea al SDR
Nodo 3:   Notificar por Slack/WhatsApp al SDR con el texto de la respuesta
```
Aquí el flujo termina: la **respuesta humana** —qué contestar, cómo manejar la objeción, agendar— es del vendedor, no del automation. Eso vive en `ventas_lushows` (ver `64`). El pegamento solo garantiza que el lead caliente **llegue rápido a un humano**.

**3) Lead de la landing → enriquecer y puntuar (inbound instantáneo)**
```
Trigger:  Webhook del formulario web
Nodo 2:   HTTP → Clay: enriquecer dominio + score ICP (ver 38, 101)
Nodo 3:   Router: si score ≥ 70 → HubSpot MQL + tarea SDR; si < 70 → nurture (ver 76)
```

**4) Señal de compra → outbound en caliente (signal-based)**
```
Trigger:  Programado cada mañana (cron)
Nodo 2:   HTTP → fuente de señal (job posts, noticias, cambios; ver 14, 37)
Nodo 3:   Clay enriquece los que aplican (ver 101)
Nodo 4:   Smartlead: mete a la secuencia de "señal fresca" con el gancho del día
```

## Buenas prácticas (para que no se te caiga)

- **Empieza con UN flujo simple** y compruébalo con 5 registros antes de encadenar cinco. La automatización rota fácil si la montas toda de golpe.
- **Filtra temprano.** Pon el nodo de filtro (email válido, tier, dedup contra CRM) **antes** de las acciones caras, igual que en Clay (ver `101`, `77`).
- **Maneja errores.** Configura un camino de error / reintentos y una alerta cuando un nodo falle; si no, los leads se pierden en silencio.
- **Registra (log).** Que cada corrida deje rastro (a una hoja o Slack) para auditar qué se movió.
- **No metas la lógica de IA cara aquí.** Si un flujo dispara prompts de IA a escala, el costo lo optimizas en su sitio → `optimizer_tokens_lushows`.
- **Idempotencia.** Evita que un webhook duplicado cargue el mismo lead dos veces (chequea si ya existe antes de crear).

## Cuándo NO automatizar

Automatizar algo roto lo rompe más rápido. Si tu lista es mala o tu copy no convierte, arréglalos primero (ver `20`, `50`). Y no automatices el **juicio**: calificar a fondo, decidir si una cuenta Tier A merece un toque manual, o responder a un interesado — eso es humano (ver `70`, `ventas_lushows`). El pegamento mueve datos y dispara tareas; **no vende**.

## Ejemplo real: la máquina mínima de Lushows

```
Sales Nav (lista) → export → Clay (email + verify + score, ver 101)
   → [n8n Flujo 1] carga válidos a Instantly (ver 103)
Instantly envía cadena en frío (ver 60)
   → prospecto responde
      → [n8n Flujo 2] alerta WhatsApp + tarea en CRM
         → Lushows responde a mano y agenda (ventas_lushows)
```
Eso es todo tu outbound corriendo casi solo, con humano solo donde hay que vender.

## Errores comunes

- **Automatizar sin filtrar** → cargas rebotes y basura a escala (ver `28`, `45`).
- **Un mega-workflow de 30 nodos** imposible de depurar → divide en flujos chicos encadenados por webhook.
- **Sin manejo de error/dedup** → leads perdidos o duplicados en silencio.
- **Zapier a volumen alto** → factura sorpresa; migra a n8n self-host.
- **Automatizar la conversación** → suena a robot y quema al lead; deja lo humano humano.

## Siguiente paso

Monta el **Flujo 2** (respuesta → alerta) primero: es el de mayor ROI y menor riesgo, porque garantiza que nunca pierdas un caliente. Luego el **Flujo 1** (Clay → sequencer). Para las integraciones a nivel concepto → `34`; para la API de Smartlead → `104`; para bajar el costo de IA en los flujos → `optimizer_tokens_lushows`.

# 190 — Montar una agencia de outbound (el modelo de negocio)

Este módulo abre el Bloque 19, el cierre de la biblioteca: cómo convertir la máquina que aprendiste a construir (Bloques 0–9 del núcleo y la expansión 100–189) en un **negocio de servicios** que le vende reuniones calificadas a otras empresas. El módulo `95` fue la introducción al modelo ("qué vendes, cómo cobras a grandes rasgos"); aquí entras al negocio de verdad: **qué empaquetas, cómo se estructura, cuánto cuesta operarlo y de dónde sale el margen.** Importa porque es la salida natural de esta skill: ya tienes el producto (una máquina de outbound probada), falta montarlo como agencia. Ojo con la frontera: el **modelo de negocio a fondo, la viabilidad y los unit economics** son decisión estratégica → `economist_lushows`; **facturar la agencia** (contratos, retención, impuestos) → `contador_lushows`. Aquí te doy la anatomía operativa del negocio.

## El principio: vendes un resultado repetible, no tu tiempo

Una agencia de outbound (también "lead gen agency" o "appointment setting") es rentable por una razón: **la infraestructura y el know-how se amortizan entre clientes**. Aprender a montar dominios, warmup, Clay, secuencias y deliverability lo pagaste una vez (con tu tiempo y tus errores); ahora lo cobras muchas veces. El producto es una **reunión calificada en el calendario del cliente** (ver `95`), no "correos enviados" ni "horas de SDR". Esa distinción define todo el negocio: prometes y cobras por resultado repetible, y por eso puedes documentarlo (ver `90`), delegarlo (ver `85`, `86`) y escalarlo.

La trampa a evitar desde el día uno: montar la agencia **antes de tener tu propia máquina probada**. Si nunca has llenado un pipeline (ni el tuyo ni el de un piloto), estás vendiendo humo y quemando tu nombre. La secuencia sana es: máquina probada para ti → primer cliente piloto → agencia (ver `192`, `195`).

## Qué empaquetas (los servicios)

No vendes "outbound" en abstracto. Empaquetas **entregables concretos** que el cliente entiende y paga. Los servicios típicos, de menos a más alcance:

| Servicio | Qué entregas | Para quién | Módulos fuente |
|---|---|---|---|
| **Setup / infraestructura** | Dominios, buzones, SPF/DKIM/DMARC, warmup listos | Quien quiere hacerlo interno pero no sabe montar la base | `41`–`43`, `194` |
| **Listas + datos** | ICP escrito + lista verificada por nicho | Quien ya tiene SDR pero mala data | `10`, `20`, `28` |
| **Campaña completa (appointment setting)** | Todo: ICP, lista, infra, copy, cadencia, respuestas, reunión agendada | El grueso del mercado | `10`–`73` |
| **Consultoría / auditoría** | Diagnóstico de su outbound + playbook | Quien quiere arreglar su máquina, no tercerizarla | `83`, `90` |
| **Fractional SDR** | Un SDR tuyo dedicado part-time a su cuenta | PYME que no puede pagar un SDR full | `85`, `95` |

El producto estrella es la **campaña completa**: ahí está el margen y la promesa clara (X reuniones/mes). Los demás son puertas de entrada o upsells. **La frontera del servicio:** entregas la reunión calificada; la venta y el cierre los hace el cliente (ver `193`). Si además ofreces cerrar, es otro oficio y otro contrato → `ventas_lushows`.

## Cómo se estructura la agencia (roles)

Al principio eres tú haciendo todo. A medida que creces, el trabajo se divide en cuatro funciones. No necesitas cuatro personas —una persona cubre varias— pero sí saber qué roles existen:

| Rol | Qué hace | Cuándo lo separas |
|---|---|---|
| **Fundador / dueño de cuenta** | Vende la agencia, dueño de la relación con el cliente | Desde el día 1 (eres tú) |
| **Ops / deliverability** | Monta y cuida la infra de envío de cada cliente (ver `194`) | Cuando tienes 3+ clientes |
| **List builder / data** | Construye y verifica listas por cliente | Cuando el volumen te desborda |
| **SDR / respuestas** | Corre campañas y maneja las respuestas iniciales | Cuando no puedes atender todas las bandejas |
| **Copywriter** | Escribe las secuencias por cliente/nicho | Suele ser tú o freelance al inicio |

El orden real de contratación cuando escalas: primero un **VA/ops** que te quita el trabajo mecánico (list building, mantenimiento de buzones), luego un **SDR** que maneje respuestas, y tú te quedas con venta + relación + estrategia. Contratar y rampear personas es su propio tema (ver `85`, `86`, `89`).

## La estructura de costos (de dónde se va el dinero)

Los costos de una agencia de outbound son bajos comparados con casi cualquier negocio, y esa es la gracia. Se dividen en **fijos** (los pagas exista o no el cliente) y **variables/por cliente** (crecen con cada cuenta que sumas):

**Costos por cliente (variables) — órdenes de magnitud 2026, USD/mes:**
- **Dominios secundarios:** ~USD 10–15/año cada uno; un cliente típico usa 2–5 dominios (ver `41`).
- **Buzones (Google Workspace / Microsoft 365):** ~USD 6–12 por buzón/mes; 2–3 buzones por dominio → un cliente puede costar USD 40–150/mes solo en buzones.
- **Sending tool (Instantly/Smartlead):** planes desde ~USD 30–100/mes, algunos cubren varios clientes (ver `33`).
- **Datos (Apollo/Clay/verificación):** ~USD 50–200/mes según volumen y créditos (ver `100`, `31`, `28`).

**Costos fijos (la agencia):**
- CRM (ver `32`), herramientas de agendamiento, tu tiempo/salario, y eventualmente el equipo.

> Los **números exactos** (tu costo real por cliente, punto de equilibrio, margen por cuenta) NO los inventes: calcúlalos con `Matematicas_lushows` con tus cifras reales. La **viabilidad del modelo y tu CAC como agencia** → `economist_lushows`. La regla de oro del margen: el costo de operar una cuenta (infra + tiempo) debe ser una fracción de lo que cobras (ver `191`).

## Cómo se ve el negocio en números (la forma del P&L)

Sin dar cifras que dependen de tu mercado, la **estructura** de la economía es esta:

```
Ingreso por cliente (retainer o por reunión)          ver 191
  – Costo de infra de esa cuenta (dominios+buzones+data)
  – Costo de ejecución (tu tiempo o el del SDR)
  = Margen por cuenta
  × Número de cuentas que puedes operar bien
  – Costos fijos de la agencia (CRM, tú, overhead)
  = Utilidad
```

La palanca clave NO es cobrar más por cuenta: es **cuántas cuentas operas sin que baje la calidad**. Ahí es donde el sistema replicable (ver `198`), la documentación (ver `90`) y la infra separable (ver `194`) se vuelven el negocio. Una agencia que no sistematiza tiene techo en las cuentas que el fundador atiende a mano.

## Errores comunes (qué NO hacer)

- Montar la agencia sin máquina propia probada. Vendes lo que no sabes entregar (ver `192`).
- Meter todos los clientes en la misma infra de envío para "ahorrar". Un cliente con lista mala hunde la reputación de todos (ver `194`).
- Prometer cierres/ventas cuando solo controlas hasta la reunión (ver `193`).
- Cobrar sin conocer tu costo real por cuenta: puedes operar a pérdida sin darte cuenta (→ `Matematicas_lushows`).
- Crecer en clientes más rápido de lo que puedes operarlos bien: quemas dominios, incumples y matas tu reputación de agencia (ver `195`, `196`).

## Siguiente paso

Si vas a montar la agencia, el orden del Bloque 19 es tu ruta: define el **pricing** (`191`), consigue tus primeros clientes con meta-outbound (`192`), fija **SLAs** honestos (`193`) y monta la **operación multi-cliente** sin cruzar dominios (`194`). Antes de cotizarle a nadie, valida la economía con `economist_lushows` y los números con `Matematicas_lushows`; para facturar y llevar las cuentas, `contador_lushows`.

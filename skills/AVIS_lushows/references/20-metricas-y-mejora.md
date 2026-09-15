# 20 · Métricas y mejora continua

> Destila `economist_lushows` (52-cac-ltv, 88-metricas-y-tablero, 33-señales-de-tracción) +
> `engineer_visualopen_lushows` (62-analytics-product-tracking, 324-ab-testing-experiments,
> 345-event-tracking-schema). Cruza con `07-confidencialidad-y-datos.md` (Habeas Data) y
> `11-manejo-de-clientes.md` (ciclo de vida). **Todo cálculo exacto → `Matematicas_lushows`.**

**Regla de oro:** pocas métricas, bien elegidas. Si una métrica sube/baja 20% y no cambiarías nada
mañana, es **vanidad** (seguidores, mensajes totales) — no va en el tablero. North Star de AVISPA'O:
**negocios con sus papeles al día y facturas leídas cada semana** (valor real, no plata de hoy).

## 1 · Salud del negocio (SaaS)
AVISPA'O cobra suscripción mensual → se mide como SaaS. Estas dicen si crece sano o se desangra.

| Métrica | Fórmula simple | Por qué importa |
|---|---|---|
| **MRR** (ingreso recurrente mensual) | suma de cuotas activas del mes | El latido del negocio; es la North Star financiera. |
| **Churn** (cancelación) | clientes que se van ÷ clientes al inicio del mes | La fuga. >5%/mes es alarma; con churn alto no sirve captar más. |
| **LTV** (valor de vida) | cuota mensual × margen × meses que se queda | Cuánto deja un cliente en toda la relación (margen, no ingreso). |
| **CAC** (costo de captar) | (pauta + ventas) ÷ clientes nuevos | Lo que cuesta un cliente. Incluye sueldos/comisiones, no solo ads. |
| **LTV : CAC** | LTV ÷ CAC | Prueba de fuego. Sano **≥ 3:1**; <1:1 = cada cliente empobrece. |
| **Payback** | CAC ÷ ganancia mensual por cliente | En cuántos meses recuperas el CAC. Sano: < 6 meses. |
| **Activación** | % de nuevos que llegan al "ajá" | Que lean su 1ª factura o reciban su lista de papeles (ver `11`). |
| **Conversión prospecto→pago** | clientes que pagan ÷ prospectos que escribieron | Eficiencia del cierre por WhatsApp (lo hace AVIS). |

La palanca más rentable no suele ser bajar CAC sino **subir retención** (menos churn = más LTV).

## 2 · Desempeño del agente AVIS
Mide si AVIS responde bien, cierra y engancha — no solo si habla.

| Métrica | Fórmula simple | Por qué importa |
|---|---|---|
| **Tasa de respuesta** | conversaciones contestadas ÷ entrantes | Que nadie quede sin atención (el silencio de AVIS espanta — `11`). |
| **Tasa de cierre por # de toques** | ventas ÷ prospectos, segmentado por toques | Revela en qué toque cierra (1º, 3º, 5º) para afinar la cadencia. |
| **% que conecta facturas** | clientes con correo/buzón conectado ÷ activos | El gancho real del producto; sin esto el cliente no siente valor. |
| **Facturas leídas por cliente** | total facturas procesadas ÷ clientes activos | Uso real = el predictor #1 de retención. Poco uso → churn próximo. |
| **NPS informal** | % "me encanta" − % quejas (pregunta suave en chat) | Termómetro de satisfacción; el pico ideal para pedir referidos. |

Cruza uso bajo con el ciclo de vida de `11`: cliente sin facturas leídas en 2 semanas = candidato a
secuencia de reactivación.

## 3 · Embudo de venta por WhatsApp
Mide UNA cosa por paso y busca el **cuello de botella** (no siempre está arriba).

| Etapa | Pregunta | KPI |
|---|---|---|
| Llega | ¿Cuántos escriben? | Prospectos nuevos/semana (de ads o referidos) |
| Engancha | ¿AVIS responde y conversa? | % que pasa del 1er mensaje |
| Califica | ¿Es una pyme real con necesidad? | % de prospectos calificados |
| Cierra | ¿Pagan el plan? | Conversión prospecto→pago |
| Activa | ¿Llegan al "ajá"? | % activados en 5 días |
| Retiene | ¿Vuelven y usan? | Facturas leídas + recompra de plan |

Si llegan muchos pero no cierran, el problema es el **pitch**, no traer más tráfico — gastar más en
ads sería tirar plata.

## 4 · Experimentos (A/B) para mejorar a AVIS
Mejorar es probar, no adivinar. Cambia **una sola cosa** y compara dos versiones.

- **Qué probar:** saludo de bienvenida, pitch del plan, frase de cierre, manejo de la objeción
  "está caro", recordatorios de vencimiento, mensaje de reactivación.
- **Cómo:** divide prospectos al azar 50/50 (A vs. B), define la métrica de éxito ANTES
  (ej. conversión→pago), corre hasta tener muestra suficiente. **No mires a mitad y declares ganador**
  (peeking = falsos positivos; el tamaño de muestra lo calcula `Matematicas_lushows`).
- **Guardrail:** vigila que la versión "ganadora" no empeore otra cosa (ej. más cierres pero más
  churn al mes). Si empeora un guardrail, no ganó.
- Documenta qué ganó y por qué; ese aprendizaje se vuelve parte del prompt de AVIS.

## 5 · Analítica con respeto a Habeas Data
AVIS maneja datos sensibles de pymes → la medición también obedece la Ley 1581/2012 (ver `07`).

- **No metas PII en los eventos.** Registra `cliente_id` anónimo, no nombre/cédula/NIT/teléfono.
  Mide `factura_leida`, `plan_activado`, `recordatorio_enviado` — nunca el contenido de la factura.
- **Finalidad declarada:** la analítica es para mejorar el servicio, no para perfilar ni vender datos.
- **Derecho a supresión:** si un cliente se va y pide borrado, sus eventos también se eliminan/anonimizan.
- Usa eventos manuales tipados con nombres fijos (`objeto_accion` en pasado); renombrar rompe el
  histórico del embudo.

## Cadencia de revisión
- **Diario** (1 min): señales de vida — conversaciones del día, pagos nuevos.
- **Semanal** (15 min): embudo + activación; aquí ajustas el pitch de AVIS.
- **Mensual** (1 h): MRR, churn, CAC/LTV, payback, tendencias. Cada número con meta y dato anterior,
  o no dice nada.

> **Roadmap:** instrumentar eventos clave (activación, factura leída, churn), tablero MRR/churn en una
> hoja, primer A/B del saludo, NPS automatizado en el pico de satisfacción, y alerta de "cliente sin
> uso 2 semanas" enganchada a la secuencia de reactivación de `11`.

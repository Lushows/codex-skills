# 23 — Event-driven & colas (a nivel sistema)

## Selección de broker
- **Kafka** — alto throughput, durable, ordenado *por partición*, log replayable, consumer groups. Best para event
  streaming, analytics, event sourcing. Pesado de operar.
- **RabbitMQ** — ruteo flexible (exchanges direct/topic/fanout), ack por mensaje, task queues/RPC. Quorum queues para durabilidad.
- **Redis Streams** — liviano, consumer groups, baja latencia; ok a escala modesta si ya corres Redis.
- **SQS/SNS** — managed AWS; SQS = cola (at-least-once, sin orden salvo FIFO), SNS = pub/sub fan-out. Cero ops.

**Pub/sub vs queue:** queue = un consumidor procesa cada mensaje (distribución de trabajo); pub/sub = cada suscriptor recibe copia (fan-out).

## Outbox pattern (resuelve el dual-write)
No puedes escribir DB *y* publicar al broker atómicamente. Escribe el evento a una tabla `outbox` *en la MISMA
txn* que tu cambio de negocio; un relay aparte (polling o CDC vía Debezium) lee el outbox y publica. Garantiza que
el evento dispara sii la txn commiteó.
```sql
BEGIN; INSERT INTO orders ...; INSERT INTO outbox (topic, payload) VALUES ('order.created', '{...}'); COMMIT;
```

## Saga (transacción distribuida sin 2PC)
Secuencia de txns locales + acciones compensatorias. **Orchestration** (coordinador central emite comandos, más
fácil de razonar/monitorear — Temporal, Step Functions) vs **choreography** (servicios reaccionan a eventos del
otro — desacoplado pero el flujo es implícito y difícil de tracear).

## Consumidores idempotentes (obligatorio)
Casi todos los brokers son **at-least-once**: dedupea por message id (guarda ids procesados, o haz la operación
naturalmente idempotente — upsert por key). **Ordering** solo aplica dentro de una partición Kafka / SQS-FIFO group
→ particiona por entity id para mantener los eventos de una entidad ordenados. **DLQ:** tras N retries, aparca el
mensaje en vez de loop infinito.

## Exactly-once es un mito (end-to-end)
Kafka tiene "exactly-once semantics" *dentro de Kafka* (idempotent producer + transactions), pero al llamar un
sistema externo obtienes at-least-once + idempotencia = "effectively once". **Diseña para eso.**

## CQRS / event-sourcing
CQRS separa write model de read model(s). Event sourcing guarda la *secuencia de eventos* como source of truth,
reconstruyendo estado por replay. Potente (audit, time-travel) pero añade eventual consistency y complejidad de
replay — overkill para CRUD.

## Gotchas
1. Sin outbox → eventos perdidos en silencio cuando el publish al broker falla tras el DB commit.
2. Asumir orden global entre particiones — no lo tienes.
3. Mensajes veneno sin DLQ bloquean toda la partición.
4. Consumidor no-idempotente + at-least-once redelivery = cobros dobles.

**Fuentes:** microservices.io/patterns/data/transactional-outbox · microservices.io/patterns/data/saga · confluent.io/blog (exactly-once) · docs.aws.amazon.com (SQS FIFO).

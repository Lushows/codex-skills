# 365 · Backups y disaster recovery (un backup que no probaste no es un backup)

> "Tengo backups" es una creencia, no un hecho, hasta que **restauras** uno y funciona.
> DR no es copiar datos: es la capacidad probada de volver a operar tras perderlo todo, en un tiempo que aguantes.

## Los dos números que mandan: RPO y RTO
- **RPO (Recovery Point Objective)**: cuántos datos puedes permitirte perder, medido en tiempo. RPO de 1h →
  backup al menos cada hora. Define la **frecuencia** de tus copias.
- **RTO (Recovery Time Objective)**: cuánto puedes estar caído. RTO de 30 min → necesitas restauración automatizada,
  no "el dev abre la consola y recuerda los pasos". Define tu **arquitectura** de recuperación.

Pon estos números **por sistema** y derivados del negocio, no al azar. La DB de pedidos (`data/orders.json` de BIOWHATS)
no tolera el mismo RPO que un caché de renders regenerable.

## La regla 3-2-1 (sigue vigente en 2026)
**3** copias de los datos, en **2** medios distintos, **1** fuera de sitio (offsite/otra región/otra cuenta cloud).
Para un endpoint GPU + dashboard: datos en el disco, snapshot en otro bucket, copia en R2/S3 de otra región/cuenta.
La copia offsite te salva del fallo regional **y** del ransomware/borrado accidental que arrasa la cuenta primaria.

## Backups inmutables y versionados: contra el borrado y el ransomware
Si tu backup vive en el mismo sitio que puede ser comprometido, no es backup. Usa **object-lock / versioning**
(R2/S3 lo soportan): una vez escrito, no se puede sobreescribir ni borrar por T días. Un atacante (o un `rm -rf`
tuyo) no puede destruir el historial. Pon **retención** escalonada: diarios 7d, semanales 4w, mensuales 12m.

## PITR: recuperación a un punto en el tiempo
Para bases de datos transaccionales, snapshot diario + WAL/binlog continuo = **point-in-time recovery**: restauras
al segundo **antes** del `DELETE` catastrófico, no al backup de anoche (que ya perdió el día entero). RPO de minutos
sin pagar backups completos cada minuto. Postgres (`pg_basebackup` + archivado WAL), Supabase y RDS lo ofrecen.

## Failover: el plan B ya levantado, no improvisado
- **Activo-pasivo**: réplica en standby que se promueve si cae la primaria. RTO bajo si el failover es automático.
- **Multi-región**: para SEV de región completa. Caro; resérvalo para lo que el RTO de negocio exija.
- Para el stack GPU serverless: el "failover" suele ser **caer a API premium** (Higgsfield/Runway) mientras el
  endpoint propio se recupera — degradado y más caro, pero sirviendo. La cascada de fallback ES tu DR de cómputo.

## El paso que todos saltan: PROBAR la restauración
Un backup no validado es **Schrödinger**: no sabes si funciona hasta que lo abres, normalmente en plena crisis.
- **Game day**: trimestralmente, restaura un backup en un entorno aislado y verifica integridad (checksums, registros, app arranca).
- Mide el **RTO real** de la restauración → casi siempre es mayor que el que asumiste. Ajusta o automatiza.
- Alerta si un backup **no se generó** o quedó corrupto/vacío (un cron silenciosamente roto = cero copias por meses).

## Runbook de recuperación (escrito, no en la cabeza de una persona)
Pasos numerados y ejecutables bajo estrés: dónde están los backups, credenciales/acceso, comando exacto de restore,
orden de dependencias (DB antes que app), cómo verificar que quedó bien, a quién avisar. Pruébalo en el game day:
si el runbook tiene huecos, los descubres en el simulacro, no en el incendio.

## Checklist mínimo
- [ ] RPO y RTO definidos por sistema y firmados por negocio.
- [ ] 3-2-1 con al menos una copia offsite e inmutable (object-lock).
- [ ] Backups automáticos + alerta si fallan o salen vacíos.
- [ ] Restauración probada en los últimos 90 días, con RTO real medido.
- [ ] Runbook de recuperación versionado y accesible **aunque el sistema primario esté caído**.

## Errores que muerden
- Backup en la misma región/cuenta que lo primario → un fallo se lleva original y copia.
- Nunca probar el restore → descubres que está corrupto el día que lo necesitas.
- Backear la app pero no los **secretos/config** → restauras datos que no puedes arrancar.
- Retención infinita sin lifecycle → factura de almacenamiento que crece sin freno.

Cruza con [[29-iac-deploy]] y [[362-error-handling-resilience-patterns]].

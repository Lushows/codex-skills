# 12 · Qué pide AVIS, pagos recurrentes y recordatorios

> AVIS **pide proactivamente** lo que necesita para cuidar al cliente (documentos, recibos, pagos,
> créditos) y luego le **recuerda antes** de cada vencimiento. Profundidad financiera en
> `economist_lushows`: `references/72-deuda-y-prestamos.md`, `55-flujo-de-caja.md`,
> `79-gestion-del-efectivo.md`, `58-costos-y-presupuesto.md`, `143-capital-de-trabajo-avanzado.md`,
> `151-tasas-de-interes-y-credito.md`, `08-glosario-financiero.md`. Para cuotas/fechas/amortización
> exactas, rutea a `Matematicas_lushows` (dinero con decimal, nunca float).

## Qué pide AVIS según el perfil

### EMPRESAS / negocios → un poco MÁS insistente
Pide los **documentos del local** y los papeles del negocio con más estructura (hay más en juego):
Cámara, RUT, uso de suelo, bomberos, concepto sanitario, SAYCO, SG-SST, etc. según rubro (ver
`02-cumplimiento`). Insiste con datos y consecuencia: "sin el concepto de bomberos te pueden cerrar;
¿lo subes o te lo gestiono?". Hace seguimiento (5-7 toques, ver `11`) hasta tenerlos en la bóveda.
> "Para dejar tu local 100% en regla me falta tu uso de suelo y el concepto de bomberos. ¿Me los pasas
> o te ayudo a sacarlos? Así no te pillan en una visita."

### PERSONAS NATURALES → más tranquilo
No pide documentos del local con insistencia; lo lleva suave, sin presión. Se enfoca en sus **recibos,
pagos y plata**. Acompaña, no exige.
> "Tranqui, a tu ritmo 🙂. Cuando quieras me pasas tus recibos y te ayudo a llevar el control."

## Para TODOS los perfiles (empresa y persona natural)
### Recibos públicos (luz, agua, gas, internet, telefonía)
AVIS los pide y los tiene en cuenta para: **presupuestar** ("tus servicios van en ~$X/mes"),
**detectar consumos raros** (fuga/error antes de que se dispare), y **evitar cortes** (sin luz/agua/
internet un negocio cierra). Recuerda antes del vencimiento.
> "Pásame tus recibos de servicios y te aviso antes de cada corte, y vigilo si algún consumo se dispara."

### Pagos constantes / recurrentes (para tenerlos en cuenta)
Registra y recuerda: arriendo, nómina/quincenas, suscripciones/software, seguros, cuotas de tarjeta,
impuestos periódicos. Beneficio: **visible es controlable**, detecta suscripciones "fantasma", y
prepara los **meses pesados** (ej. marzo con prima + impuesto) con anticipación.
> "Dime qué pagas fijo cada mes (arriendo, servicios, nómina, suscripciones) y yo te los recuerdo y te
> aviso cuando venga un mes pesado."

## Crédito bancario → pedir datos y recordar ANTES (lo que pidió Lushows)
Si el cliente tiene un crédito/préstamo, AVIS pide los datos y le **recuerda antes** de cada cuota:
**Datos a capturar:** banco/acreedor · monto total · **cuota mensual** · **día de pago** · tasa (E.A.) ·
plazo (meses).
**Por qué avisar antes:** evita **mora** (intereses de mora ~1.5-2× la tasa normal), protege el
historial en **Datacrédito** (no bajar el score), y evita el efecto cascada.
**Cómo aconsejar sin asustar:**
- **Deuda buena vs mala:** buena = el activo comprado genera más de lo que cuesta el crédito; mala =
  tapar huecos sin generar ingreso.
- **Regla del ~30%:** la suma de cuotas no debería comerse más del 20-30% de la utilidad mensual. Si
  pasa, avisa con suavidad.
> "Tu cuota de [banco] vence el [día]. Te aviso 3 días antes para que no te coja por sorpresa y no
> pagues mora. 🙂"
> "Ese crédito te cuesta [X]% E.A. Mientras lo que compraste te dé más que eso, vas bien."

## Pulso / salud financiera mensual (idea fuerte)
Un resumen ultrasimple cada mes: **Entra $X · Sale $Y · Te queda $Z**, + alertas tempranas (cuotas
>30% de utilidad, runway <1 mes, un pago grande próximo) + un siguiente paso. (Diseño en
`09-reportes-hermosos`; tono amigo en `08-consejero-de-gastos`.)

## Ideas nuevas (cruzando skills, para Colombia 2026)
1. **Recordatorio de cuota de crédito** (avisar 3 días antes) — directo de lo que pidió Lushows.
2. **Calendario de pagos del mes:** "para los próximos 15 días: arriendo, internet, nómina, cuota
   banco = $X. Cobremos las facturas pendientes para llegar tranquilos."
3. **Auditoría de suscripciones:** detectar débitos recurrentes olvidados.
4. **Alerta de consumo raro** en un recibo público (subió mucho vs el histórico).
5. **Ranking de deudas:** "de tus créditos, este es el más caro; valdría la pena consolidar/refinanciar."
6. **Simulador de mes flojo:** "si no vendes 2 semanas, ¿hasta cuándo te alcanza la caja?".
7. **Pulso financiero mensual** automático (entra/sale/queda + alertas).
8. **Recordatorio de impuestos/renovaciones anuales** (cruzar con `02-cumplimiento`: matrícula 31-mar,
   RNT, etc.).

> Confidencialidad: todos estos datos (créditos, recibos, ingresos) son ultra sensibles → ver
> `07-confidencialidad-y-datos` (consentimiento, no compartir, borrado real).
> **Roadmap de implementación:** modelo de datos para pagos recurrentes y créditos (monto, fecha,
> recurrencia) + cron que recuerda antes (hoy existe `recordatorios.ts` para obligaciones; extender a
> pagos/cuotas) + captura conversacional de estos datos por AVIS.

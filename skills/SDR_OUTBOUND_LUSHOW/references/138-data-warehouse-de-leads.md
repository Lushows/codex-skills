# 138 — Tu data warehouse de leads (base viva de prospectos)

Un **data warehouse de leads** (almacén de datos de prospectos) es tu **propia base viva** de cuentas y contactos: todo lo que compraste, scrapeaste, enriqueciste y aprendiste, guardado en un lugar tuyo que **crece y mejora con el tiempo**. La alternativa —volver a comprar los mismos datos en Apollo cada vez que armas una campaña— es tirar dinero y perder todo lo que ya sabías de esas cuentas. Este módulo es sobre **dejar de rentar tus datos y empezar a poseerlos**: por qué importa, qué guardar, y cómo montarlo sin ser ingeniero.

## El principio: los datos son un activo que se aprecia, si los guardas

Cada vez que enriqueces (`130`), verificas (`28`), detectas una señal (`133`, `135`) o registras "esta cuenta dijo 'no ahora'" (`76`), estás **generando conocimiento**. Si ese conocimiento vive solo en la campaña de Instantly de este mes, se pierde cuando la campaña termina. Si lo guardas en tu base, la próxima vez:

- **No re-compras** lo que ya tienes (Apollo/Clay cobran por búsqueda; tu base es gratis de releer).
- **No re-contactas** a quien ya dijo que no o ya es cliente (evitas quemar la relación y tu reputación, `07`).
- **Acumulas historia:** "esta cuenta la tocamos en enero, respondió tibio, cambió de gerente en junio" — contexto que ningún proveedor te vende.
- **Tu ICP se afina solo:** con el histórico de quién cerró ves qué atributos predicen venta (alimenta `10`, `137`).

La lógica económica: comprar datos es un **costo recurrente**; tu warehouse convierte ese gasto en un **activo** que se aprecia. (Para modelar el ahorro real → `Matematicas_lushows`; el CAC de re-comprar vs poseer → `economist_lushows`.)

## Qué guardar (el modelo mínimo)

Dos tablas relacionadas, no una lista plana:

| Tabla | Campos clave |
|---|---|
| **Cuentas (empresas)** | id, nombre, dominio, industria, tamaño, geo, technographics (`134`), tier (`16`), fit score (`137`), estado (nunca tocada / en cadencia / cliente / no-ahora / muerta) |
| **Contactos (personas)** | id, cuenta_id, nombre, cargo, email (+estado de verificación, `28`), móvil, LinkedIn, fuente, fecha de enriquecimiento |
| **Actividad / señales** | contacto_id, tipo (email enviado, respuesta, visita web, cambio de cargo…), fecha, resultado |

La tabla de **actividad** es la que casi todos olvidan y la que más vale: es la memoria de qué le pasó a cada lead y qué hiciste tú.

## Dónde montarlo (de simple a robusto)

| Nivel | Herramienta | Para quién |
|---|---|---|
| **Arranque** | Google Sheets / Airtable | 1 persona, <10k contactos. Airtable ya relaciona tablas |
| **Estándar** | Tu **CRM** (HubSpot, Pipedrive) como fuente de verdad (`32`) | La mayoría; el CRM ya guarda cuenta+contacto+actividad |
| **Orquestación** | **Clay** como capa de enriquecimiento que **escribe al CRM** (`31`) | Quien enriquece a escala |
| **Avanzado** | Warehouse real (BigQuery, Postgres, Supabase) + herramientas de datos | Equipos con volumen y algo de técnica |

**Para el 90 % de los casos, tu CRM ES tu warehouse de leads.** No montes BigQuery si tienes 3.000 contactos; usa HubSpot bien. El "warehouse" de verdad (BigQuery) es para cuando el volumen y las fuentes desbordan al CRM. (Montar Postgres/Supabase/BigQuery bien → `engineer_visualopen_lushows`.)

## Cómo montarlo, paso a paso

1. **Elige la fuente única de verdad** (CRM para casi todos). Todo lo demás escribe **hacia** ahí.
2. **Define el estado de cada cuenta/contacto** (nunca tocada, en cadencia, cliente, no-ahora, muerta). Es lo que evita re-contactar.
3. **Enruta todo enriquecimiento hacia la base.** Clay enriquece → escribe al CRM, no a un Sheet suelto que muere con la campaña.
4. **Registra la actividad automáticamente:** tu sequencer (`33`) y tu CRM deben loguear envíos, respuestas y resultados (`77`).
5. **Chequeo de duplicados ANTES de enriquecer.** Antes de gastar créditos en un contacto nuevo, verifica si ya lo tienes (dedup, `139`).
6. **Marca el "no-ahora" con fecha de re-contacto** para que vuelva a la cola cuando toque (`76`).

## Ejemplo: flujo Clay → CRM como warehouse vivo

```
Campaña nueva (restaurantes Medellín):
  1. Clay saca 500 cuentas nuevas.
  2. DEDUP: Clay cruza contra el CRM → 120 ya existían → NO se re-enriquecen
     (ahorro de 120 búsquedas). Solo enriquece las 380 nuevas.
  3. Enriquece (waterfall `130`) + verifica (`28`) → escribe las 380 al CRM
     con estado "en cadencia" y fit score (`137`).
  4. Cadencia corre; respuestas y resultados vuelven al CRM (actividad).
  5. 3 meses después: nueva campaña relee el CRM → los clientes se excluyen,
     los "no-ahora" con fecha vencida vuelven a la cola. Cero re-compra.
```

Cada ciclo la base sabe más y cuesta menos. Eso es el activo apreciándose.

## Errores comunes

- **Datos que mueren en la campaña** → enriqueces en un Sheet, la campaña acaba, lo pierdes. Escribe siempre a la fuente de verdad.
- **Re-comprar lo que ya tienes** → sin dedup previo, pagas dos veces por el mismo contacto (`139`).
- **Re-contactar a clientes o a "no" recientes** → quemas la relación por no tener estados. El estado es sagrado.
- **Sobre-ingeniería** → montar BigQuery para 2.000 leads es perder tiempo; usa el CRM.
- **Base sin mantenimiento** → un warehouse que no se limpia se pudre (emails muertos, duplicados, cargos viejos). Eso es `139`, y sin ello el activo se deprecia.

## Frontera y siguiente paso

El warehouse **guarda y acumula**; usar esos datos para convencer y cerrar es `ventas_lushows`. Empieza hoy tratando tu **CRM como fuente única de verdad** (`32`): define estados de cuenta, enruta todo enriquecimiento hacia ahí, y añade dedup antes de comprar datos nuevos. La disciplina que mantiene el activo vivo, deduplicado y limpio es el módulo gemelo → `139`. Los datos que lo llenan → `130`–`136`; lo que decide a quién trabajar de esa base → `137`. Para montar un warehouse técnico de verdad → `engineer_visualopen_lushows`.

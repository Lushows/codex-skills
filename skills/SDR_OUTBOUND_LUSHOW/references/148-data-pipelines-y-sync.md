# 148 — Data pipelines y sync

Un **data pipeline** (tubería de datos) es el camino por el que un dato viaja de una herramienta a otra; la **sincronización (sync)** es mantener las copias del mismo dato iguales en todas partes. `147` te dio la tubería de eventos (lead → secuencia → CRM → handoff); este módulo es el problema más sutil y más traicionero: **cómo mantener las herramientas sincronizadas sin que se pisen entre sí**, sobre todo cuando el dato viaja en **ambos sentidos** (sync bidireccional). Es donde nacen los duplicados, los estados fantasma y los "esto decía otra cosa ayer". Dominar esto es la diferencia entre un stack que se aceita solo y uno que se pudre lento.

## El principio: sin una regla de quién gana, la sincronía crea contradicciones

El peligro no es que el dato no viaje —es que viaje en dos direcciones y **cada herramienta pise lo que hizo la otra**. HubSpot marca "en secuencia", Smartlead marca "respondió", el sync corre y... ¿cuál gana? Si no defines la regla, el resultado es un lead que parpadea entre estados o vuelve a recibir correos tras responder. La sincronía solo funciona con **una jerarquía clara de quién manda sobre cada campo** (el mapa de propiedad de `146`) y una regla de resolución de conflictos. Sin eso, más sync = más caos.

## One-way vs. two-way: elige el más simple que sirva

| Tipo | Cómo funciona | Cuándo usarlo | Riesgo |
|---|---|---|---|
| **One-way (un sentido)** | A escribe en B; B nunca escribe en A | El dato tiene un dueño claro (Clay→CRM) | Ninguno grave; empieza aquí |
| **Two-way (bidireccional)** | A y B se actualizan mutuamente | Ambos editan el mismo campo (estado sequencer↔CRM) | Conflictos y bucles si no hay reglas |

Regla práctica: **usa one-way siempre que puedas; reserva two-way solo para los pocos campos que de verdad se editan en ambos lados** (típicamente `lead_status` y desuscripciones). La mayoría de tu stack debe ser one-way hacia el CRM (todo escribe al centro, ver `146`). El two-way es potente pero exige disciplina.

## Los tres enemigos de la sincronía (y cómo matarlos)

### 1. Duplicados
El pecado clásico. Nacen cuando dos fuentes crean el mismo registro sin cruzarlo primero.
- **Clave de dedup por campo normalizado, no por texto exacto.** Cruza por **dominio** (empresa) y **email en minúsculas sin espacios** (persona). (Lección real de proyectos con dos correos por comercio: el texto exacto NO dedup-ea porque "Ana@X.co" ≠ "ana@x.co "; normaliza mayúsculas/espacios y cruza por dominio. Ver `139`, `146`.)
- **Deduplica en la entrada**, antes de crear, no con una limpieza mensual después.
- **Fusiona sin perder datos** cuando ya hay duplicados: junta actividades e historial, no borres el que tenga el dato bueno. (Otra lección real: fusión mal hecha borra historial en cascada.)

### 2. Conflictos de escritura (write conflicts)
Dos herramientas editan el mismo campo casi a la vez. Reglas para resolver:
- **Last-write-wins solo si hay timestamp confiable.** El cambio más reciente gana —pero solo si ambos lados sellan la hora bien.
- **Mejor: source-of-truth-wins.** Para cada campo, el **dueño** (`146`) siempre gana sin importar la hora. `lead_status` lo manda el CRM; el evento de envío lo manda el sequencer. Sin ambigüedad.
- **Nunca dejes que el campo lo decida el azar del orden de ejecución.** Ese es el bug fantasma más difícil de rastrear.

### 3. Deriva y desfase (drift & lag)
Las copias se separan con el tiempo si el sync falla callado.
- **Sync en near-real-time para lo crítico** (respondió/baja: debe reflejarse en minutos, o re-contactas a quien respondió).
- **Sync por lotes (batch) está bien para lo no urgente** (firmographics, enriquecimiento nocturno).
- **Reconciliación periódica.** Un chequeo semanal que compara conteos entre herramientas y alerta si divergen ("Smartlead dice 177 respuestas, el CRM registra 160 → 17 no sincronizaron").

## Ejemplo: contrato de sync del campo `lead_status`

```
CAMPO: lead_status
  Dueño (source of truth): CRM (141)
  Escriben hacia el CRM:
     Sequencer  → cuando "respondió" o "baja"   (near-real-time, webhook, 147)
     Routing    → cuando asigna owner            (interno del CRM)
  Lee del CRM:  dashboard (144), forecast (145), reglas de routing (142)

  RESOLUCIÓN DE CONFLICTO:
     - "baja/unsubscribe" del sequencer  → SIEMPRE gana (legal + reputación, 45)
     - "respondió" del sequencer         → gana sobre "en_secuencia"
     - cualquier otro cambio             → source-of-truth = CRM

  DEDUP al entrar:  clave = lower(trim(email)) + dominio
  RECONCILIACIÓN:   lunes — comparar #respondió(sequencer) vs #respondió(CRM);
                    alertar si difieren > 3%
```

La "baja gana siempre" no es opcional: seguir escribiendo a quien pidió salir es problema de reputación **y** legal (ver `45`, `07`). Los umbrales de la reconciliación (¿3% o 5%?) → cuádralos con `Matematicas_lushows`.

## Buenas prácticas

- **One-way por defecto, two-way solo donde se necesita.** Menos direcciones = menos conflictos.
- **Un dueño por campo** (el mapa de `146`) resuelve el 90% de los conflictos antes de que ocurran.
- **Normaliza antes de comparar/deduplicar.** Minúsculas, sin espacios, por dominio.
- **Near-real-time para respuestas y bajas; batch para el resto.** No todo necesita ser instantáneo.
- **Reconcilia y alerta.** Un sync que falla en silencio deriva durante semanas; el chequeo semanal lo caza.

## Errores comunes

- **Two-way en todo** → bucles de escritura y estados que parpadean.
- **Dedup por texto exacto** → duplicados por mayúsculas/espacios que "deberían" coincidir.
- **Sin regla de conflicto** → el campo lo decide el orden de ejecución (bug fantasma).
- **Fusionar borrando** → pérdida de historial en cascada al juntar duplicados.
- **Confiar en que el sync "simplemente funciona"** → sin reconciliación, la deriva te sorprende con números que no cuadran (y un dashboard que miente, `144`).

## La frontera

Este módulo mantiene las copias **iguales y limpias**; el diseño de quién es dueño de cada dato → `146`; la tubería de eventos que dispara los syncs → `147`; la governance y calidad del dato a escala (reglas de completitud, ownership organizacional) → `139`. Toda comparación numérica exacta (umbrales de reconciliación, tasas de divergencia) → `Matematicas_lushows`. El manejo legal de bajas/consentimiento → `45`, `07`.

## Siguiente paso

Escribe el "contrato de sync" del ejemplo para tus 2–3 campos que viajan en dos sentidos (empezando por `lead_status` y `unsubscribe`): dueño, quién escribe, regla de conflicto, clave de dedup. Pon dedup normalizado en la entrada de tu tubería (`147`) y agenda una reconciliación semanal. Para la calidad de datos más allá del sync → `139`; para que los umbrales sean exactos → `Matematicas_lushows`.

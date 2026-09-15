# 144 — Dashboards y reporting

Un dashboard es la pantalla que te dice, de un vistazo, **si tu máquina de outbound está sana y dónde se rompe**. `80` te dio las métricas del outbound (qué es reply rate, tasa de reunión, etc.) y `83` cómo diagnosticar cuando un número baja. Este módulo es cómo **montar los tableros**: qué tres vistas necesitas, qué va en cada una y qué NO poner. La regla que ordena todo: un dashboard no es para decorar ni para sentirte productivo mirando números —es para **tomar una decisión esta semana**. Si un gráfico no cambia lo que harás, sáltalo.

## El principio: mide inputs para actuar, outputs para saber si funcionó

Hay dos tipos de métricas y confundirlas es el error clásico. Los **inputs (leading)** son lo que controlas hoy y predicen el futuro: contactos tocados, correos enviados, llamadas hechas. Los **outputs (lagging)** son el resultado que llega después: reuniones, SQL, deals cerrados. Un buen dashboard muestra **ambos y en su relación**: si el input está bien pero el output cayó, el problema es de *conversión* (copy, targeting, deliverability); si el input cayó, el problema es de *actividad*. Sin separar los dos, no sabes dónde meter mano.

## Las tres vistas (y solo tres)

No necesitas veinte gráficos; necesitas tres tableros con propósito distinto:

| Vista | Pregunta que responde | Frecuencia | Audiencia |
|---|---|---|---|
| **Actividad** | ¿Estamos haciendo el trabajo? (inputs) | Diaria | El SDR / tú |
| **Funnel/conversión** | ¿Dónde se cae el embudo? (ratios) | Semanal | SDR + quien gestiona |
| **Pipeline/forecast** | ¿Cuánto negocio viene? (outputs + proyección) | Semanal/mensual | Negocio / dueño |

### Vista 1 — Actividad (diaria, para no engañarte)

```
HOY / SEMANA
  Contactos tocados      850 / 3.400     (meta 800/día ✓)
  Correos enviados        620            (dentro de límites de buzón, ver 44)
  Llamadas hechas          35
  LinkedIn/WhatsApp        40
  Respuestas nuevas        22
  Reuniones agendadas       4
```
Propósito: confirmar que el motor está encendido. Si esto cae, todo lo demás caerá en 30–60 días (ver `145`). Es la vista que un solista mira cada mañana.

### Vista 2 — Funnel / conversión (semanal, para diagnosticar)

El embudo completo con el ratio entre cada etapa (la lógica está en `81`):

```
Contactos tocados   3.400  ┓
                            ┃ reply rate 5.2%      ← ¿deliverability/copy? (40, 50)
Respuestas            177  ┛
                            ┃ % positivas 30%      ← ¿targeting/oferta? (10, 54)
Positivas             53   ┛
                            ┃ % agenda 51%
Reuniones agendadas   27   ┓
                            ┃ show rate 78%        ← ¿recordatorios? (75)
Reuniones realizadas  21   ┛
                            ┃ % califican 62%      ← ¿calidad de lead? (70, 78)
SQL                   13
```
Propósito: ver **en qué escalón se cae** el embudo. Cada ratio flojo apunta a un módulo de arreglo (marcado al lado). Diagnóstico a fondo → `83`.

### Vista 3 — Pipeline / forecast (semanal-mensual, para el negocio)

```
PIPELINE ACTIVO
  SQL en pipeline del AE         13   ($ potencial ponderado ~$5.850)
  Reuniones agendadas (comprom.)  9
  Cerrados ganados (mes)          4   ($6.000 margen)

FORECAST 60 días (rango, ver 145)   $3.300 – $5.000
  Riesgo principal: bounce subió a 4% → menos entregas
```
Propósito: decir cuánto negocio viene y con qué confianza. Alimenta directo el forecasting de `145`.

## Reglas para que un dashboard sirva

- **Cada número contra su meta.** Un "5.2% reply" no dice nada; "5.2% vs meta 5%" sí. Sin referencia no hay decisión.
- **Muestra la tendencia, no solo el punto.** Un número de hoy sin la línea de las últimas 8 semanas oculta si vas mejorando o cayendo (ver `05`).
- **Un dueño por dashboard.** El de actividad lo mira el SDR; el de forecast, el negocio. Sin dueño, nadie actúa.
- **Menos es más.** Tres vistas limpias > veinte gráficos que nadie lee. Si un widget no cambió una decisión en un mes, bórralo.
- **Empieza con el reporte nativo del CRM.** HubSpot/Pipedrive ya traen estos tableros (ver `32`). No compres Looker/Power BI hasta que el nativo se te quede corto.

## Ejemplo: dónde vive cada dashboard según tu etapa

| Etapa | Herramienta de dashboard | Costo |
|---|---|---|
| Solista arrancando | Reporte nativo del CRM + una hoja de cálculo | incluido / gratis |
| Equipo chico | Dashboards nativos de HubSpot/Pipedrive | incluido en plan |
| Volumen alto/varios equipos | Looker Studio (gratis) o Power BI conectado al CRM | gratis / ~$10+/usuario |

Ojo: la vista de **actividad** muchas veces vive en el sequencer (Instantly/Smartlead ya muestran enviados/reply), no en el CRM. No dupliques —lee cada número de donde es la fuente de verdad (ver `146`).

## Errores comunes

- **Dashboards de vanidad.** Gráficos bonitos de "correos enviados" sin ratios ni metas: te hacen sentir productivo, no te dicen nada.
- **Solo outputs.** Mirar solo reuniones/SQL y no los inputs → te enteras tarde de que el motor se apagó.
- **Número sin meta ni tendencia.** Imposible saber si está bien o mal.
- **Veinte tableros que nadie abre.** El dashboard que no se mira no existe.
- **Confundir dashboard con diagnóstico.** El tablero *muestra* que el reply cayó; *por qué* cayó y cómo arreglarlo es `83`.

## La frontera

El dashboard **muestra**; qué significa cada número y cómo calcularlo → `80`; cómo diagnosticar el escalón roto → `83`; cómo proyectar desde el pipeline → `145`. Que los porcentajes y agregaciones sean exactos (y que un cambio sea real y no ruido) → `Matematicas_lushows`. Ligar estos números al modelo económico del negocio → `economist_lushows`.

## Siguiente paso

Monta las tres vistas en el reporte nativo de tu CRM/sequencer esta semana, cada número con su meta y su tendencia de 8 semanas. Mira la de actividad a diario y la de funnel los lunes. Cuando un ratio se salga de meta → `83` para diagnosticar. Cuando quieras proyectar lo que viene → `145`. Para que los cálculos no mientan → `Matematicas_lushows`.

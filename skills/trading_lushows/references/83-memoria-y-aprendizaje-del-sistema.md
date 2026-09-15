# 83 — Memoria y aprendizaje del sistema

Los LLM no aprenden de una conversación a otra: cada llamada a Claude empieza de cero. Si el bot
perdió 3 veces comprando extendido la semana pasada, el Claude de hoy no lo sabe — salvo que
alguien se lo cuente. Ese "alguien" es `traderMemory`: la libreta de lecciones del sistema.

## Cómo funciona traderMemory

1. **Qué guarda**: lecciones estructuradas en JSON — qué setup era, en qué régimen, qué pasó,
   qué se aprendió. Ejemplo real: "entradas en precio extendido tras racha alcista: 0/3, evitar".
2. **De dónde salen**: de los resultados de trades cerrados y del meta-análisis semanal (módulo
   84), que convierte la semana en lecciones explícitas.
3. **Cómo se usan**: en el paso 3 del pipeline, ANTES de pedir convicción, se filtran las
   lecciones relevantes **por régimen y similitud de setup** y se inyectan al prompt de
   Druckenmiller como contexto: "lecciones de situaciones parecidas: ...".
4. **Dónde vive**: JSON persistido en `data/` con escritura atómica — sobrevive reinicios y
   deploys (módulo 87).

El filtrado importa: inyectar TODAS las lecciones siempre diluye el prompt y sube el costo.
Una lección de mercado lateral no ayuda (y puede estorbar) en tendencia fuerte.

## Qué ES y qué NO es esto

| | Memoria tipo traderMemory | Aprendizaje estadístico (machine learning) |
|---|---|---|
| Qué guarda | Lecciones en texto, legibles por humanos | Pesos numéricos ajustados con miles de ejemplos |
| Cuántos casos necesita | Funciona desde 1 caso ("esto pasó, ojo") | Necesita cientos/miles para generalizar |
| Auditable | Totalmente — se lee la lección y se sabe por qué el bot decide distinto | Caja negra o casi |
| Riesgo principal | **Sobre-aprender de muestras chicas**: 0/3 es una alerta, no una ley estadística | Sobreajuste al pasado (overfitting) |
| Se olvida / desactualiza | Hay que curarla: lecciones viejas pueden dejar de aplicar cuando cambia el mercado | Se reentrena |

**Memoria ≠ aprendizaje.** Que el bot "recuerde" el 0/3 del FOMO no significa que haya aprendido
en sentido estadístico: 3 casos no prueban nada con rigor. La lección vale como *heurística
prudente* ("penaliza esto mientras no haya evidencia a favor"), no como verdad. Por eso las
lecciones importantes deben graduarse a **reglas de código o de prompt** cuando la evidencia
crece — la memoria es el borrador, la regla es la versión final.

## Límites honestos

- Una lección mal escrita o demasiado general ("no comprar cuando sube") puede castrar al sistema.
  Las lecciones buenas son específicas y condicionales.
- La memoria puede acumular ruido: parte de la rutina semanal (módulo 75) es revisar qué lecciones
  siguen vigentes.
- El modelo puede ignorar una lección inyectada si el resto del contexto grita lo contrario — la
  memoria influye, no obliga. Lo que debe SER obligatorio va en JS (módulo 85).

## Cómo aplica al AGENTE TRADING

- Flujo real del caso FOMO: meta-análisis detecta 0/3 → lección en traderMemory → se inyecta en
  setups similares → convicción baja en entradas extendidas → menos trades FOMO. Y el paso final
  pendiente: convertirla en regla dura (filtro de extensión) cuando la evidencia lo confirme.
- Al depurar una decisión rara del bot, revisar QUÉ lecciones se inyectaron en ese análisis
  (`/api/analyses` guarda el contexto) — a veces el "bug" es una lección vieja hablando.

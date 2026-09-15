# 313 · Tool-use / function-calling — patrones de producción

> El LLM no ejecuta nada: emite un JSON pidiendo que TÚ llames una función.
> El 80% de los bugs de agentes están en el schema, la validación y el manejo del error, no en el prompt.

## El ciclo, sin magia
1. Defines tools con schema (JSON-Schema / Zod). 2. El modelo decide y emite `tool_use` con args.
3. Tú ejecutas y devuelves `tool_result`. 4. El modelo continúa con el resultado en contexto.

```ts
import { z } from 'zod';
const tools = {
  get_clima: {
    description: 'Clima actual de una ciudad. Úsalo solo si el usuario pregunta por el clima.',
    inputSchema: z.object({ ciudad: z.string(), unidad: z.enum(['C','F']).default('C') }),
    execute: async ({ ciudad, unidad }) => fetchClima(ciudad, unidad),
  },
};
```

## El schema ES el prompt
El modelo solo ve `name` + `description` + el shape. Calidad del tool-call = calidad de estos textos.
- **Descripción accionable**: di *cuándo* usarla y *cuándo no*. "Úsalo solo si X" reduce llamadas espurias.
- **Enums sobre strings libres**: `enum(['pendiente','pagado'])` evita valores inventados.
- **Args mínimos**: cada campo opcional es una oportunidad de alucinación. Defaults explícitos.
- **Nombres semánticos**: `cancelar_pedido`, no `tool_3`.

## Paralelo, secuencial y multi-step
| Patrón | Cuándo | Riesgo |
|---|---|---|
| **Paralelo** | tools independientes (3 ciudades de clima) | side-effects concurrentes en escritura |
| **Secuencial** | la entrada de B depende de la salida de A | latencia acumulada |
| **Multi-step (agéntico)** | el modelo encadena hasta resolver | loop infinito → pon `maxSteps` |

Modelos 2026 emiten **varios `tool_use` en un turno** → ejecuta en paralelo solo los de lectura;
serializa los que escriben para evitar carreras.

## Validación y error recovery
Nunca confíes en los args crudos. **Valida con el schema antes de ejecutar**; si falla, devuelve el
error como `tool_result` y el modelo se autocorrige — no lances excepción al usuario.

```ts
const parsed = schema.safeParse(args);
if (!parsed.success)
  return { type:'tool_result', is_error:true,
           content:`Args inválidos: ${parsed.error.message}. Corrige y reintenta.` };
```

- **Errores como datos, no como crash**: `is_error:true` + mensaje accionable → el modelo reintenta.
- **Idempotencia**: si el modelo re-llama `crear_pedido` por timeout, usa una idempotency-key para no duplicar.
- **Timeout por tool**: una API lenta cuelga todo el turno → `Promise.race` con límite y devuelve error legible.
- **Tope de pasos**: `maxSteps: 8` corta loops donde el modelo nunca da respuesta final.

## Detalles que muerden
- **Tool no-determinista** (hora, random) rompe el prompt-caching del prefijo (ver [[316-cost-control-llm-apps]]).
- **Demasiadas tools** (>20) degradan la elección → agrupa o enruta con un primer modelo barato.
- **Salida estructurada ≠ tool-use**: si solo quieres un JSON de respuesta, usa structured output, no una tool falsa.

Cruza con [[32-agentes-y-tool-use]] y [[226-structured-output-vision]].

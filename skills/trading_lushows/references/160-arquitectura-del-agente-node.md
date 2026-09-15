# 160 — Arquitectura del agente en Node: las decisiones técnicas y por qué

## Qué es este módulo

El módulo 01 dice **qué** es el AGENTE TRADING; este explica **por qué** se construyó así.
Sirve para defender (o revisar) cada decisión cuando alguien pregunte "¿y por qué no usaste X?".

## Decisión 1: Node.js 20 con ESM

**ESM** (ECMAScript Modules) es el sistema moderno de `import`/`export` de JavaScript, en vez del
viejo `require()` (CommonJS). Ventajas prácticas: es el estándar actual, los SDKs nuevos
(como `@anthropic-ai/sdk`) lo asumen, y obliga a declarar dependencias de forma explícita arriba
de cada archivo — se ve de un vistazo qué usa cada módulo.

## Decisión 2: sin framework (ni NestJS, ni frameworks de tests)

| Alternativa | Por qué NO |
|---|---|
| NestJS / frameworks grandes | Capas de abstracción que Luis (no técnico) no podría leer; el bot es 1 proceso, no una empresa |
| Jest / Vitest | `node --test` viene incluido en Node 20; cero dependencias extra, cero config, 145 tests corren igual |
| TypeScript | Suma un paso de compilación; los tests + JSON schema de las respuestas de Claude cubren los errores que TS atraparía aquí |

Regla general: **cada dependencia es un riesgo** (mantenimiento, vulnerabilidades, breaking changes).
Un bot que corre 24/7 años agradece pocas piezas móviles.

## Decisión 3: módulos por dominio, no por tipo técnico

El código se agrupa por **lo que hace en el negocio**, no por su rol técnico:
`src/binance/` (datos), `src/paperTrading/` (broker simulado), `src/skills/` (cerebros),
`src/strategy/` (orquestación), `src/persistence/` (guardar). Cuando hay un bug de sizing,
se sabe exactamente dónde mirar: `src/skills/positionSizing.js`. En una estructura por tipo
(`controllers/`, `services/`, `utils/`) el mismo bug estaría regado en 4 carpetas.

## Decisión 4: inyección de dependencias para poder testear

"Inyección de dependencias" suena elegante pero es simple: en vez de que un módulo cree sus
propias conexiones (a Claude, a Binance, al disco), **las recibe como parámetro**. Así en los
tests se le pasa una versión falsa (mock) y se prueba la lógica sin internet ni gastar tokens.
Ejemplo: el engine recibe el cliente de Claude; en tests recibe uno que devuelve respuestas
fijas. Por eso existen 145 tests que corren en segundos y gratis.

## Decisión 5: JSON en disco, no base de datos

| Criterio | JSON atómico (elegido) | Postgres/SQLite |
|---|---|---|
| Volumen de datos | Decenas de trades/mes → KB, no GB | Sobra capacidad |
| Consultas | Leer todo y filtrar en JS basta | SQL potente que no se necesita |
| Operación | Cero: es un archivo en el disco de Render | Migraciones, backups, conexión, credenciales |
| Legibilidad | Luis puede abrir el archivo y leerlo | Necesita cliente SQL |

La corrupción (el riesgo real del JSON) se resuelve con escritura atómica (ver módulo 162).
**Cuándo migrar a DB:** si algún día hay miles de trades, múltiples procesos escribiendo, o
consultas complejas frecuentes. Hoy sería sobre-ingeniería.

## Cómo aplica al AGENTE TRADING

Toda la arquitectura apunta a lo mismo: **un sistema que una persona no técnica pueda operar y
que sobreviva años sin mantenimiento pesado**. Pocas dependencias, módulos con nombre de negocio,
tests baratos, datos legibles. Antes de agregar cualquier pieza nueva, la pregunta no es
"¿es más moderna?" sino "¿el bot la necesita y Luis podrá vivir con ella?".

# 196 — Integración con el ecosistema Lushows

Esta skill no vive sola: es una pieza del equipo de skills de Luis, cada una con su territorio.
La regla del ecosistema (anotada en el feedback general): **las skills se rutean entre sí, no se
duplican**. Este módulo define las fronteras y qué se le pide a quién.

## El mapa de fronteras

| Skill | Su territorio | Qué le rutea trading_lushows |
|---|---|---|
| **trading_lushows** (esta) | El OFICIO de tradear con sistema: método, riesgo, métricas, protocolo del bot, roadmap | — |
| **Matematicas_lushows** | Todo cálculo exacto (promesa ERROR CERO, código verificado, dinero con decimal nunca float) | Expectancy, PF, Kelly, intervalos de confianza, probabilidad de rachas, significancia de A/B, correlaciones entre pares |
| **economist_lushows** | Decisiones de NEGOCIO y capital: viabilidad, go/no-go, cuánto capital arriesgar, costo de oportunidad | ¿Vale la pena el proyecto vs alternativas? Regla de la quiebra ($200-500), decisión de escalar o apagar (método go/no-go, módulo 36) |
| **contador_lushows** | Impuestos y registro contable Colombia (DIAN, declaración) | Tratamiento fiscal de ganancias en cripto cuando haya dinero real; qué registrar para declarar (verificar al día normativa DIAN) |
| **claude-api** (skill) | La API de Anthropic: modelos, precios, parámetros, JSON estricto, caching | Elección de modelo por paso (Haiku barato para régimen, Sonnet para convicción), control del costo ~$5/mes, migraciones de modelo |

División en una frase: **trading DECIDE cómo se opera · Matematicas EJECUTA los números ·
economist DECIDE si vale la pena y cuánto capital · contador REPORTA a la DIAN · claude-api
resuelve el motor de IA.**

## Lecciones importadas de los otros agentes de Luis

El AGENTE TRADING es el tercer bot serio del ecosistema y hereda cicatrices ya pagadas:

- **De AVISPA'O — "los atajos regex antes del cerebro"**: los bugs de AVIS vivían en la cascada
  de atajos ANTES del LLM, no en el prompt. Traducción al trading: el trade con convicción 0 es
  la misma familia de bug — el problema suele estar en el CÓDIGO alrededor del modelo. Auditar
  la tubería, no solo el prompt. Y su arnés de regresión (auditar-ruteo.mjs) es el modelo a
  copiar para probar el pipeline del bot.
- **De AVISPA'O — leer errores silenciosos**: PostgREST devolvía `{error}` sin lanzar excepción.
  Toda respuesta de API (Binance incluida) se revisa por campo de error, no solo por "no explotó".
- **De GASTROWHATS/BIOWHATS — pipeline de gates baratos primero**: filtros JS gratis antes de
  llamadas a Claude. El bot de trading ya usa este patrón (psicología JS antes de Haiku/Sonnet);
  mantenerlo en toda función nueva.
- **Del ecosistema Render — persistencia**: los agentes de Luis viven en Render free/low tier;
  el disco y los deploys tienen sus mañas (ej. Bendita Pola: el mount oculta carpetas). Antes de
  la fase 8, verificar dónde persiste traderMemory tras cada deploy.
- **Feedback general "verificar antes de setup"**: investigar compatibilidad real ANTES de crear
  cuentas o mover infraestructura. Aplica directo a la migración a Frankfurt y al testnet de
  Binance (`191`): confirmar restricciones al día antes de ejecutar la mudanza.

## Cómo aplica al AGENTE TRADING

- En la práctica: cuando una sesión de trabajo toque números → invocar Matematicas; cuando toque
  "¿meto más plata?" → economist; cuando toque modelos/costos de IA → claude-api. No resolver
  esos temas "de memoria" dentro de esta skill.
- Cuando otra skill aprenda algo aplicable al trading (o al revés), la lección se anota en AMBOS
  lados con referencia cruzada — es lo que hace equipo al equipo.
- Antes de crear un módulo nuevo aquí, revisar que no exista ya en otra skill (regla
  anti-duplicación del ecosistema).

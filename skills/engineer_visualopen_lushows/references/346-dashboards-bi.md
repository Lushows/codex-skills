# 346 · BI y dashboards (Metabase, Superset, Evidence — self-serve sin caos)

> Un dashboard que nadie consulta o cuyos números nadie cree es deuda, no insight. La meta no es
> "más gráficas": es que el equipo responda sus propias preguntas con una sola definición de cada métrica.

## Las tres herramientas OSS y a quién sirven
| Herramienta | Modelo | Brilla cuando | Límite |
|---|---|---|---|
| **Metabase** | no-code, question builder | no-técnicos exploran solos sin SQL | embedding white-label es paid ($85+/mes) y limitado a escala |
| **Superset** | SQL + 40+ tipos de chart | poder/escala, viz exótica, SAML/LDAP sin paywall | curva fuerte; alguien debe dueñar el semantic layer |
| **Evidence** | code-first, SQL + Markdown, Git | reportes versionados, reproducibles, bonitos | **no embebe** dashboards interactivos; requiere SQL+MD |

(Posicionamiento de comparativas 2026; verifica precios/features actuales antes de decidir.)

## Cómo elegir
- **Startup, todos exploran** → **Metabase**: mete a la empresa entera a clickear datos en un día.
- **Equipo data maduro, reportes pulidos** → **Evidence** para informes Git-native + **Superset** para
  ad-hoc y viz pesada. No es excluyente: muchos corren los dos.
- **Customer-facing embebido white-label serio** → ninguno OSS brilla; mira productos dedicados de
  embedded analytics (el embedding de Metabase escala mal para ese caso).

## El pecado capital: métricas inconsistentes
Si "revenue" se define en cada query del dashboard, tendrás tres números distintos para la misma palabra.
**Fix**: define la métrica una vez en el **semantic layer** (dbt + MetricFlow, [[344-dbt-transformations]])
y que el BI consuma de ahí, o al menos centraliza la lógica en modelos Gold de dbt y que los dashboards
solo hagan `SELECT` de Gold — **cero lógica de negocio en la capa de visualización**.

## Self-serve de verdad
No es "dale acceso a todos"; es darles datos **modelados y nombrados en su idioma**:
- Capa Gold con tablas/métricas pre-agregadas y columnas con nombres de negocio (no `amt_usd_net_v2`).
- Diccionario de datos + descripciones en el BI (Metabase deja documentar cada campo).
- Plantillas/dashboards base por equipo, no lienzo en blanco → la gente parte de algo, no de cero.
- Sin esto, "self-serve" produce diez versiones del mismo KPI y reuniones para decidir cuál es real.

## Qué métricas poner (negocio, no vanidad)
- **North Star** + su árbol de inputs, no 40 gauges sueltos.
- **SaaS core**: MRR, churn, LTV, CAC, payback ([[337-saas-metrics-mrr-churn-ltv]]) — definidas en
  semantic layer, no recalculadas por dashboard.
- **Funnel** con tasas de conversión entre pasos, no solo conteos absolutos.
- **Cohortes** para retención (una métrica puntual oculta si los nuevos se van).
- Evita **vanity metrics** (pageviews totales sin contexto): impresionan, no accionan.

## Operación
- **Cache + refresh schedule**: no re-corras queries pesadas en cada carga; cachea y refresca por cron.
- **Row-level security / permisos** si hay datos por cliente o por equipo.
- **Alertas** sobre umbrales (churn sube, ingresos caen) → el dashboard empuja, no esperas que alguien mire.
- **Versiona** (Superset export, Evidence en Git) para revisar cambios de definición y revertir.

## Gotchas
1. **Lógica de negocio en el dashboard** → cada gráfica reimplementa el KPI y ninguno cuadra.
2. **Self-serve sin modelado** → caos de KPIs duplicados; el problema es la capa Gold, no la herramienta.
3. **Elegir Evidence para embedding** — no embebe interactivo; es para reportes que se leen.
4. **Queries en vivo sobre raw** sin cache → factura de warehouse ([[343-data-warehouse-bigquery-duckdb]]) y lentitud.
5. **Dashboard sin owner** se pudre: filtros rotos, métricas obsoletas, cero confianza.

Cruza con [[329-dashboards-data-viz]] y [[337-saas-metrics-mrr-churn-ltv]].

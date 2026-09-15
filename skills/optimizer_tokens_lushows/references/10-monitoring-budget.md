# 10 — Monitoring, Budget Enforcement & Kill Switches

**Impacto:** Cero ahorro DIRECTO, previene desastre financiero.
**Esfuerzo:** Medio (instalar tooling + integrar).
**Cuándo aplicar:** SIEMPRE. No es opcional. Es la defensa.
**Prioridad:** Si solo vas a hacer UNA cosa, instalá monitoring ANTES de cualquier otra optimización.

## Por qué este módulo es CRÍTICO

Casos reales de "facturas LLM sorpresa":
- Startup pagó $40K en un fin de semana por un loop infinito en producción
- Dev se olvidó debuggear modo en prod, generó $8K en 2 días
- Cliente abusó de un free trial, costó $12K antes de detectarlo
- Tenant malicioso disparó 100K requests/hora, $25K en 6 horas

**Todos prevenibles con monitoring básico.**

## Las 3 cosas que TODO sistema LLM debe tener

```
┌─────────────────────────────────────────────────┐
│  1. TRACKING                                    │
│     Saber cuánto se gasta, por qué, quién       │
└─────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────┐
│  2. ALERTING                                    │
│     Notificación cuando algo se sale de norma   │
└─────────────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────────────┐
│  3. KILL SWITCHES                               │
│     Auto-detener cuando supera threshold        │
└─────────────────────────────────────────────────┘
```

## 1. Tracking — saber qué se gasta

### Minimum viable tracking

```python
import time
from datetime import datetime

class LLMTracker:
    def __init__(self, db):
        self.db = db

    def track(self, response, metadata: dict):
        """Llamar después de cada response del LLM."""
        usage = response.usage

        cost = self._calculate_cost(
            model=response.model,
            input_tokens=usage.input_tokens,
            cache_creation=getattr(usage, 'cache_creation_input_tokens', 0),
            cache_read=getattr(usage, 'cache_read_input_tokens', 0),
            output_tokens=usage.output_tokens
        )

        self.db.execute("""
            INSERT INTO llm_calls (
                timestamp, user_id, feature, model,
                input_tokens, cache_creation_tokens, cache_read_tokens,
                output_tokens, cost_usd, latency_ms,
                metadata
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            datetime.utcnow(),
            metadata.get("user_id"),
            metadata.get("feature"),
            response.model,
            usage.input_tokens,
            getattr(usage, 'cache_creation_input_tokens', 0),
            getattr(usage, 'cache_read_input_tokens', 0),
            usage.output_tokens,
            cost,
            metadata.get("latency_ms", 0),
            json.dumps(metadata)
        ))

    def _calculate_cost(self, model, input_tokens, cache_creation, cache_read, output_tokens):
        # Pricing (verificar updates con módulo 00)
        pricing = {
            "claude-opus-4-8":   {"input": 5.0, "output": 25.0},
            "claude-sonnet-4-6": {"input": 3.0, "output": 15.0},
            "claude-haiku-4-5":  {"input": 1.0, "output":  5.0},
        }

        p = pricing.get(model, {"input": 5.0, "output": 25.0})  # default conservador

        # Cost en USD ($/1M tokens, dividido)
        cost = (
            input_tokens * p["input"] / 1_000_000 +
            cache_creation * p["input"] * 1.25 / 1_000_000 +
            cache_read * p["input"] * 0.1 / 1_000_000 +
            output_tokens * p["output"] / 1_000_000
        )
        return cost

# Uso en producción
tracker = LLMTracker(db)

def chat(user_id, message, feature):
    start = time.time()
    response = client.messages.create(...)
    latency = int((time.time() - start) * 1000)

    tracker.track(response, metadata={
        "user_id": user_id,
        "feature": feature,
        "latency_ms": latency
    })

    return response.content[0].text
```

### Dashboards básicos

Queries SQL fundamentales para tu dashboard:

```sql
-- Costo total últimas 24h
SELECT SUM(cost_usd) FROM llm_calls WHERE timestamp > NOW() - INTERVAL '24 hours';

-- Top 10 usuarios por gasto este mes
SELECT user_id, SUM(cost_usd) as monthly_cost
FROM llm_calls
WHERE timestamp > date_trunc('month', NOW())
GROUP BY user_id
ORDER BY monthly_cost DESC
LIMIT 10;

-- Costo por feature
SELECT feature, SUM(cost_usd), COUNT(*) as calls, AVG(cost_usd) as avg_cost
FROM llm_calls
WHERE timestamp > NOW() - INTERVAL '7 days'
GROUP BY feature
ORDER BY SUM(cost_usd) DESC;

-- Modelos usados (validar routing)
SELECT model, COUNT(*) as calls, SUM(cost_usd) as total_cost
FROM llm_calls
WHERE timestamp > NOW() - INTERVAL '7 days'
GROUP BY model;

-- Cache effectiveness
SELECT
    SUM(cache_read_tokens) / NULLIF(SUM(input_tokens + cache_creation_tokens + cache_read_tokens), 0) * 100 as cache_hit_rate
FROM llm_calls
WHERE timestamp > NOW() - INTERVAL '24 hours';
```

## 2. Tooling de observability LLM (managed)

Si no querés construir desde cero:

### Helicone
- Proxy gratis para Anthropic, OpenAI, Gemini
- Dashboard out-of-the-box
- Cost tracking automático
- Cache hit rate visible

```python
# Cambiar base_url para enrutar via Helicone
client = Anthropic(
    api_key=ANTHROPIC_KEY,
    base_url="https://anthropic.helicone.ai",
    default_headers={
        "Helicone-Auth": f"Bearer {HELICONE_KEY}",
        "Helicone-Property-Feature": "chatbot",
        "Helicone-Property-User": user_id,
        "Helicone-Cache-Enabled": "true"  # ← incluso ofrece caching
    }
)
```

**Pricing:** free tier hasta 100K req/mes, después tiers pagos.

### Langfuse
- Open source (self-hostable)
- Tracing detallado (cada step de un agent)
- Mejor para sistemas complejos
- Compatible con LangChain, LlamaIndex

```python
from langfuse import Langfuse

langfuse = Langfuse(public_key="...", secret_key="...")

@observe()
def my_chain(query):
    return langchain_chain.invoke(query)
# Auto-trackea cost, latency, prompt, output
```

### Portkey
- Gateway + observability
- Cost tracking + budget alerts built-in
- Routing inteligente entre proveedores

### Vercel AI Gateway
- Si usás Vercel, integración nativa
- Dashboard de uso por proyecto
- Cost attribution per deployment

### PostHog LLM Analytics
- Si ya usás PostHog para product analytics
- Plug-in LLM trace + cost tracking

## 3. Alerting — saber cuando algo va mal

### Alert tiers

```python
class AlertManager:
    def __init__(self):
        self.thresholds = {
            "info":     {"daily_spend": 50,  "channel": "slack-llm-info"},
            "warning":  {"daily_spend": 200, "channel": "slack-llm-warning"},
            "critical": {"daily_spend": 500, "channel": "slack-llm-critical + sms"},
        }

    def check_and_alert(self):
        daily_spend = self._calculate_daily_spend()

        for level in ["critical", "warning", "info"]:
            if daily_spend > self.thresholds[level]["daily_spend"]:
                self._send_alert(level, daily_spend)
                break  # Solo el alert más alto

    def _send_alert(self, level, spend):
        msg = f"🚨 LLM spend hoy: ${spend:.2f} (threshold {level})"
        slack.send(channel=self.thresholds[level]["channel"], text=msg)
```

### Alertas que TODO sistema debe tener

| Alert | Threshold ejemplo | Por qué |
|---|---|---|
| **Daily spend > X** | $100/día | Detectar abuso temprano |
| **User spend spike** | >$10 en 1h por user | Bot abuso, free trial fraud |
| **Feature spend anómalo** | feature gasta 5x su promedio histórico | Bug introducido |
| **Cache hit rate drop** | hit_rate < 30% (si era 70%) | Algo invalida el cache |
| **Latency p95 spike** | latency p95 > 5s | Servicio degradado |
| **Error rate** | >5% requests con error | Provider issue o config wrong |
| **Token usage anómalo** | tokens promedio 2x el normal | Prompt creciendo silenciosamente |

### Implementación con cron

```python
# Cron job cada 15 minutos
def hourly_anomaly_check():
    current_hour_spend = db.query("""
        SELECT SUM(cost_usd) FROM llm_calls
        WHERE timestamp > NOW() - INTERVAL '1 hour'
    """).scalar()

    avg_hour_spend = db.query("""
        SELECT AVG(hourly_spend) FROM (
            SELECT date_trunc('hour', timestamp) as hour, SUM(cost_usd) as hourly_spend
            FROM llm_calls
            WHERE timestamp > NOW() - INTERVAL '7 days'
            GROUP BY hour
        ) sub
    """).scalar()

    if current_hour_spend > avg_hour_spend * 3:
        alert(f"⚠️ Spike: gasto última hora ${current_hour_spend:.2f} vs avg ${avg_hour_spend:.2f}")
```

## 4. Kill switches — bloquear cuando supera threshold

### Hard cap per user/tenant

```python
class BudgetEnforcer:
    def __init__(self, db, limits):
        self.db = db
        self.limits = limits  # {"free": 1.0, "pro": 30.0, "enterprise": 500.0}

    def check_budget(self, user_id: str) -> bool:
        user = self.db.get_user(user_id)
        monthly_spend = self._get_monthly_spend(user_id)
        limit = self.limits[user.plan]

        if monthly_spend >= limit:
            return False  # Bloquear request
        return True

    def _get_monthly_spend(self, user_id):
        return self.db.query("""
            SELECT COALESCE(SUM(cost_usd), 0) FROM llm_calls
            WHERE user_id = ? AND timestamp > date_trunc('month', NOW())
        """, (user_id,)).scalar()

# En tu request handler
def chat_handler(user_id, message):
    if not budget_enforcer.check_budget(user_id):
        return {"error": "Mensual budget exceeded. Please upgrade.", "code": 429}

    return chat(user_id, message)
```

### Rate limiting per user

```python
from datetime import datetime, timedelta
import redis

r = redis.Redis()

def rate_limit_check(user_id, limit_per_minute=30):
    key = f"rate:{user_id}:{datetime.utcnow().strftime('%Y%m%d%H%M')}"
    count = r.incr(key)
    if count == 1:
        r.expire(key, 60)  # Reset cada minuto

    return count <= limit_per_minute

def chat_with_rate_limit(user_id, message):
    if not rate_limit_check(user_id, limit_per_minute=30):
        return {"error": "Rate limit (30 req/min)", "code": 429}

    return chat(user_id, message)
```

### Global circuit breaker (caso emergencia)

```python
class GlobalCircuitBreaker:
    """Si el gasto global supera $X/hora, bloquear TODO el tráfico."""

    EMERGENCY_HOURLY_LIMIT_USD = 100.0

    def __init__(self, redis_client):
        self.r = redis_client

    def is_open(self) -> bool:
        """True = circuit ABIERTO = NO permitir requests."""
        return self.r.get("llm_emergency_brake") == b"1"

    def check_and_trip(self):
        """Llamado periodicamente. Si gasto excesivo, trip the brake."""
        hourly_spend = db.query("""
            SELECT SUM(cost_usd) FROM llm_calls
            WHERE timestamp > NOW() - INTERVAL '1 hour'
        """).scalar()

        if hourly_spend > self.EMERGENCY_HOURLY_LIMIT_USD:
            self.r.set("llm_emergency_brake", "1", ex=3600)
            alert_critical(f"🚨 EMERGENCY BRAKE: ${hourly_spend:.2f}/h. ALL LLM requests blocked.")

    def reset(self):
        """Operador resetea manualmente después de investigar."""
        self.r.delete("llm_emergency_brake")

# En request handler
def chat(user_id, message):
    if circuit_breaker.is_open():
        return {"error": "Service temporarily unavailable", "code": 503}
    # ... rest
```

## 5. Atribución por feature

Para saber QUÉ feature consume cuánto (y poder cobrarlo / optimizar):

```python
def chat_with_attribution(user_id, message, feature):
    response = client.messages.create(
        ...,
        metadata={
            "user_id": user_id,
            "feature": feature  # ← Anthropic permite metadata
        }
    )

    tracker.track(response, {
        "user_id": user_id,
        "feature": feature
    })
```

```sql
-- Cost por feature, descubrir las features "caras"
SELECT
    feature,
    COUNT(*) as calls,
    SUM(cost_usd) as total_cost,
    AVG(cost_usd) as cost_per_call,
    SUM(cost_usd) / (SELECT SUM(cost_usd) FROM llm_calls WHERE timestamp > NOW() - INTERVAL '30 days') * 100 as pct_of_total
FROM llm_calls
WHERE timestamp > NOW() - INTERVAL '30 days'
GROUP BY feature
ORDER BY total_cost DESC;
```

**Decisión típica:** "El feature X gasta 40% del budget pero solo lo usa 5% de users → o lo cobramos, o lo optimizamos, o lo matamos".

## Patrón completo: middleware con todo

```python
class LLMMiddleware:
    def __init__(self, db, redis_client):
        self.tracker = LLMTracker(db)
        self.budget = BudgetEnforcer(db, {"free": 1.0, "pro": 30.0})
        self.circuit_breaker = GlobalCircuitBreaker(redis_client)

    def call(self, user_id, feature, llm_call_fn):
        # 1. Circuit breaker
        if self.circuit_breaker.is_open():
            raise Exception("Service temporarily unavailable")

        # 2. Rate limit
        if not rate_limit_check(user_id):
            raise Exception("Rate limit exceeded")

        # 3. Budget check
        if not self.budget.check_budget(user_id):
            raise Exception("Monthly budget exceeded. Please upgrade.")

        # 4. Execute + track
        start = time.time()
        try:
            response = llm_call_fn()
            latency_ms = int((time.time() - start) * 1000)

            self.tracker.track(response, {
                "user_id": user_id,
                "feature": feature,
                "latency_ms": latency_ms
            })

            return response
        except Exception as e:
            # Track errors también
            self.tracker.track_error(user_id, feature, str(e))
            raise

# Uso
middleware = LLMMiddleware(db, redis)

def chat(user_id, message):
    return middleware.call(
        user_id=user_id,
        feature="chatbot",
        llm_call_fn=lambda: client.messages.create(...)
    )
```

## Casos del usuario

### BIO-SETA
- Tracking básico (user_id = phone_number)
- Rate limit: 30 msg/min por número
- Hard cap mensual: $5/usuario (free) — si supera, "lo sentimos límite alcanzado, contactá +57..."
- **Risk:** WhatsApp masivo abuse podría costar mucho. Kill switch a $50/hora global.

### AGENTE STUDIO
- Budget tiers: free $1/mes, pro $20/mes
- Track por feature: imagen, video, copy (diferentes costos)
- Alert if user generates >10 videos/día (señal de abuso)

### AGENTE TRADING
- Budget global $200/mes durante MVP
- Alert si análisis de un solo ticker > $0.50 (overkill probable)
- Circuit breaker $30/hora (trading bursts inesperados)

### SaaS XPRIZE multi-tenant
- Hard tier limits por plan:
  - Básico: $30 → 200 facturas/mes incluidas
  - Pro: $59 → 500 facturas/mes
  - Enterprise: $179 → 2000 facturas/mes
- Cuando supera: bloquear o cobrar overage automático
- Track POR TENANT, no global
- Kill switch global: si gasto excede 80% del total revenue del día → freezar nuevos signups

## Tooling comparado

| Solución | Pro | Con | Pricing |
|---|---|---|---|
| **Custom (DIY)** | Full control, no vendor | Time to build, mantener | Solo infra |
| **Helicone** | Setup en 5 min, gratis para empezar | Tier pagos para volumen | Free hasta 100K req |
| **Langfuse** | Open source, self-hostable, tracing rico | Setup más complejo | Free self-hosted |
| **Portkey** | Gateway + observability + caching | Vendor lock-in | ~$0.001/cached req |
| **PostHog LLM** | Si ya usás PostHog para product | Integration newer | Incluído PostHog |

## Checklist (esto NO es opcional)

- [ ] **Tracking installado** (custom o Helicone/Langfuse)
- [ ] Cost por user / por feature visible en dashboard
- [ ] Cache hit rate visible en dashboard
- [ ] **Hard cap mensual** por user/tenant configurado
- [ ] **Rate limit** por user activo (e.g., 30 req/min)
- [ ] **Alerts** configurados: daily spend, user spike, error rate
- [ ] **Circuit breaker global** para emergencia (e.g., $X/hora trip)
- [ ] Atribución por feature en logs
- [ ] Review semanal de top users / top features
- [ ] Plan de respuesta documentado: "qué hago si spike de costo"
- [ ] Postmortem template para incidents de costo

## Métricas de éxito de este módulo

- **0 incidentes** de costo sorpresa > $X (define tu X)
- **Tiempo de detección** de anomalía < 1 hora
- **Tiempo de mitigación** (parar el sangrado) < 15 minutos
- Dashboard con 5-6 métricas clave VISIBLES al equipo

Relacionado: [[00-fundamentos-optimizacion]], [[03-model-routing]], [[11-stack-herramientas]]

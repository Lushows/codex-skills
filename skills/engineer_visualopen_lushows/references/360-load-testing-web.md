# 360 · Load testing web (mide percentiles, no promedios; modela escenarios, no peticiones sueltas)

> El promedio miente: tu p99 es lo que sienten los usuarios enojados. Carga = encontrar el punto donde
> el sistema deja de degradar elegante y empieza a caer (el "knee"), antes de que lo encuentre producción.

## Tipos de prueba (cada una responde otra pregunta)
| Tipo | Pregunta | Forma de carga |
|---|---|---|
| **Smoke** | ¿funciona con 1-5 users? | mínima, en cada deploy |
| **Load** | ¿aguanta el tráfico esperado? | rampa al pico previsto, sostiene |
| **Stress** | ¿dónde se rompe? | sube hasta fallar |
| **Spike** | ¿sobrevive un pico súbito? | salto instantáneo (Black Friday, viral) |
| **Soak** | ¿hay fugas/degradación en horas? | carga media 2-8h |

## Las herramientas (2026)
| Tool | Lenguaje | Motor | Fuerte en |
|---|---|---|---|
| **k6** | JS/TS | Go (muy eficiente, miles de VUs/máquina) | CI/CD gates, Prometheus/Grafana, DX |
| **Locust** | Python | Python (master-worker distribuido) | equipos Python, lógica compleja, LLM workloads |
| **Artillery** | YAML + JS hooks | Node | WebSocket/Socket.io/gRPC, setup rápido sin código |

Regla práctica: stack JS/TS o gates en PR → **k6**. Shop Python o escenarios con lógica rica → **Locust**.
Protocolos modernos (WS/gRPC) o "quiero un YAML y ya" → **Artillery**. k6 simula carga seria desde una sola
máquina (Go) sin granja de generadores; Locust distribuido alcanza ~58-60k RPS pero pesa más por VU.

## Modela el ESCENARIO, no el endpoint
Un user real no martilla un endpoint: login → busca → ve producto → carrito → checkout, con **think time**
entre pasos. Pegar 10k RPS a `/health` no prueba nada. Ejemplo k6 con rampa y umbrales:
```js
import http from 'k6/http'; import { sleep, check } from 'k6';
export const options = {
  stages: [
    { duration: '2m', target: 200 },   // rampa
    { duration: '5m', target: 200 },   // sostiene el pico
    { duration: '1m', target: 0 },     // baja
  ],
  thresholds: {
    http_req_duration: ['p(95)<500', 'p(99)<1500'],  // gate: falla el CI si se rompe
    http_req_failed:   ['rate<0.01'],                 // <1% de errores
  },
};
export default function () {
  const r = http.get('https://app/api/products');
  check(r, { '200': (x) => x.status === 200 });
  sleep(Math.random() * 3 + 1);   // think time 1-4s
}
```

## Percentiles, no promedios
Reportá **p50/p95/p99** (y p99.9 si te importa la cola). El promedio esconde la cola: con 1% de requests
a 5s, el avg apenas se mueve pero 1 de 100 usuarios sufre. El **knee** = el punto de carga donde p99 y
error-rate se disparan no-linealmente; tu **capacity** segura es ~70-80% de ese knee, con margen para picos.

## Capacity planning (de números a infra)
- **Little's Law**: usuarios_concurrentes = throughput (RPS) × latencia (s). 500 RPS × 0.2s = 100 en vuelo.
- Headroom: dimensiona para 2-3× el pico medido (picos reales superan los previstos).
- Carga *open-model* (llegan a tasa fija, no esperan respuesta) revela colapso por encolamiento que el
  *closed-model* (N VUs en loop) esconde — k6 `constant-arrival-rate` para open. Importa para spikes.

## Higiene de la prueba
1. **Datos realistas**: usuarios/productos variados; cachear todo con 1 ID infla los números falsamente.
2. **Generador ≠ cuello**: si la máquina de carga satura CPU/red, medís *su* límite, no el del sistema. Monitoreá ambos.
3. **Entorno tipo-prod**: testear contra staging mini no extrapola; misma clase de infra o factor conocido.
4. **Observabilidad encendida**: correlaciona p99 con CPU/DB/pool de conexiones ([[359-database-scaling-sharding]]) para hallar *qué* se saturó, no solo *que* se saturó.

Cruza con [[19-load-testing-capacity-planning]], [[361-rate-limiting-throttling]] y [[359-database-scaling-sharding]].

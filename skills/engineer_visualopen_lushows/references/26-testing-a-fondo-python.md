# 26 — Testing a fondo (Python)

**Pirámide:** muchos **unit** rápidos, menos **integration**, pocos **e2e** lentos. Invertirla (mucho E2E) = suite lenta y flaky.

## pytest esencial
- **Fixtures** para setup/teardown y DI; scope (`function`/`module`/`session`):
  ```python
  @pytest.fixture
  def client(db): return TestClient(app)      # db es otra fixture → composición
  ```
- **Parametrize** (table-test): `@pytest.mark.parametrize("n,exp", [(2,4),(3,9)])`.
- **Markers** (`@pytest.mark.slow`) + `-m "not slow"`. **conftest.py** = fixtures compartidas auto-descubiertas por dir.

## Mocking
`unittest.mock`/`MagicMock` para objetos, `monkeypatch` (pytest) para attrs/env vars. Para HTTP: **responses**
(requests) o **respx** (httpx) interceptan en la capa de transporte — más limpio que mockear tu propio cliente.
**Prefiere fakes** (implementación in-memory real) sobre mocks profundos cuando el comportamiento importa; over-mockear testea tus mocks.

## Async
**pytest-asyncio** (`@pytest.mark.asyncio` + `asyncio_mode=auto`) o el plugin anyio. respx funciona con httpx async.

## Integration con deps reales — testcontainers
Levanta Postgres/Redis desechables en Docker → testeas contra el *motor real* (atrapa bugs SQL que los mocks ocultan):
```python
from testcontainers.postgres import PostgresContainer
with PostgresContainer("postgres:16") as pg: engine = create_engine(pg.get_connection_url())
```

## Property-based — hypothesis
Genera inputs para hallar edge cases que no imaginaste y encoge el fallo a un caso mínimo:
```python
from hypothesis import given, strategies as st
@given(st.lists(st.integers()))
def test_sort_idempotent(xs): assert sorted(sorted(xs)) == sorted(xs)
```

## Coverage / snapshot
`pytest-cov`. 100% line coverage ≠ correctness (ignora combinaciones de ramas). Apunta ~80% en lógica, no caces
100% testeando getters. Usa branch coverage (`--cov-branch`). **Snapshot** (`syrupy`): asserta contra snapshot
guardado (bueno para estructuras serializadas, pero stale snapshots "pasan" si re-grabas a ciegas).

## Testear output de IA no-determinista
NO assertees strings exactos. Estrategias: (1) **golden/aproximado** — invariantes estructurales (JSON válido,
campos requeridos, schema valida), contains/keyword, bounds de longitud; (2) **LLM-as-judge** para correctitud
semántica; (3) **mockea el modelo** en unit tests (respuesta fija) → lógica determinista; (4) `temperature=0` para
smoke repetible con tolerancia; (5) evalúa sobre un dataset con métricas (accuracy, sim embedding ≥ threshold) en vez de igualdad por-call.

## Gotchas
1. `mock.patch` debe parchear donde el nombre se *usa*, no donde se define.
2. Fixtures session-scope mutables compartidas filtran estado entre tests.
3. Assertear texto LLM exacto → suite permanentemente flaky.
4. Testcontainers necesita Docker en CI y añade latencia de arranque — márcalos `integration`, córrelos aparte.

**Fuentes:** docs.pytest.org · hypothesis.readthedocs.io · testcontainers-python.readthedocs.io · lundberg.github.io/respx.

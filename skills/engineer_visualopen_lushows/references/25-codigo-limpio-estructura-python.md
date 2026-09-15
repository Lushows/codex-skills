# 25 — Código limpio y estructura (Python)

**SOLID, pragmático:** **S**RP (un módulo, una razón para cambiar — el más útil) y **D**IP (depende de
abstracciones/protocols, inyecta colaboradores — habilita testing) cargan su peso. **O/L/I** importan menos en
Python dinámico; no fabriques interfaces con una sola implementación (YAGNI). Usa `typing.Protocol` (interfaces
estructurales) en vez de jerarquías ABC.

**Layout — usa `src/`** (previene importar el paquete no-instalado, fuerza un `pip install -e .` real):
```
pyproject.toml
src/myapp/
  orders/ { service.py  models.py  repository.py }    # paquete por FEATURE, no por capa
  payments/
tests/
```
Empaqueta **por feature** (`orders/`, `payments/`), no por capa técnica (`models/`, `services/`) — las features cambian juntas.

**Type hints + checker:** anota funciones públicas; corre **mypy** o **pyright** (más rápido, inferencia más
estricta, bundleado en Pylance). Añade a CI en `--strict` incrementalmente.

**pydantic v2** (core Rust, ~5-50× más rápido que v1) para data models, validación, serialización:
```python
from pydantic import BaseModel, Field
class Order(BaseModel):
    id: int; total: float = Field(gt=0); email: str
```
**pydantic-settings** para config (12-factor: env, tipado + validado al arranque):
```python
from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    database_url: str; anthropic_api_key: str
    model_config = {"env_file": ".env"}
```

**Dependency injection:** pasa colaboradores como args de constructor/función (el `Depends` de FastAPI es DI).
Evita singletons globales y side-effects en import — arruinan la testabilidad.

**Error handling:** excepciones para fallos *excepcionales* (idioma Python); un Result type solo para ramas
esperadas/recuperables en hot paths. Define una jerarquía chica (`AppError → NotFoundError, ValidationError`) y
mapéala a HTTP/RFC-9457 en el boundary. Nunca `except:` pelado.

**Logging:** `logging` stdlib (o **structlog** JSON), loguea en boundaries, incluye correlation/request ids,
**nunca secrets/PII/tokens**. Nivel por env. `print()` no es logging.

**Config:** 12-factor — config en el environment, nunca en código; un `Settings` cargado 1 vez; fail fast al boot si falta un var (pydantic-settings lo hace).

**Anti-over-engineering (YAGNI):** sin abstracción hasta el segundo uso concreto; sin plugin systems/frameworks
genéricos/microservicios prematuros para una app chica. Borra la flexibilidad especulativa.

## Gotchas
1. Args default mutables (`def f(x=[])`) — bug clásico; usa `None`.
2. pydantic v1→v2 rompió APIs (`.dict()`→`.model_dump()`, validators) — pinea y migra deliberado.
3. Calls a DB/red en import hacen los tests lentos y flaky.
4. El flat layout importa tu árbol de fuente en vez del paquete instalado, ocultando bugs de packaging.

**Fuentes:** docs.pydantic.dev · packaging.python.org (src layout) · 12factor.net/config.

# 293 · RBAC / ABAC, permisos y row-level security en multi-tenant

> "¿Puede este usuario hacer esto sobre este recurso?" es la pregunta que tu app responde miles de veces
> por segundo. Modelarla mal = fugas de datos entre tenants (el bug más caro de un SaaS).

## Los tres modelos de autorización

| Modelo | Decide por | Bueno para | Límite |
|---|---|---|---|
| **RBAC** | rol del usuario (admin/editor/viewer) | la mayoría de SaaS B2B | explota en # de roles cuando hay matices ("editor pero solo de SU proyecto") |
| **ABAC** | atributos (depto, región, hora, owner) | reglas contextuales finas | difícil de auditar/depurar ("¿por qué pasó?") |
| **ReBAC** | relaciones (user→owner→doc) | grafos de permisos (Drive, GitHub) | requiere motor (Zanzibar) |

En la práctica: empieza **RBAC por organización**, añade ABAC para casos puntuales (`resource.owner_id == user.id`), salta a ReBAC solo si tienes jerarquías profundas de sharing.

## RBAC multi-tenant: el esquema mínimo
```
organizations(id, name)
users(id, email)
memberships(user_id, org_id, role)        -- rol es POR org, no global
permissions(role, resource, action)        -- o hardcode roles→permisos en código
```
El usuario activa una org → su `org_id` + `role` viajan firmados en el JWT/sesión. **Nunca** confíes en un `org_id` que venga del body o query string: el atacante lo cambia y lee otro tenant. Cruza con [[292-auth-providers-clerk-auth0]].

## Row-Level Security (RLS): la defensa en profundidad
RBAC en el app-layer protege rutas; **RLS protege la fila aunque el app-layer falle**. En Postgres:
```sql
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;
CREATE POLICY tenant_isolation ON documents
  USING (org_id = current_setting('app.current_org')::uuid);
```
Antes de cada query seteas `SET app.current_org = '<org del JWT>'`. Aunque un bug olvide el `WHERE org_id=`, la base **físicamente no devuelve** filas de otro tenant. Supabase lo expone con `auth.uid()`/`auth.jwt()`. Cruza con [[21-postgres-a-fondo-pgvector]].

**Trampa crítica de RLS:** las policies se saltan con roles `BYPASSRLS` o `SECURITY DEFINER` mal usados, y el `service_role` de Supabase ignora RLS por diseño — usar la key de servicio en el frontend = puerta abierta. Las connection pools que reúsan conexiones pueden arrastrar el `SET` de otra request: usa `SET LOCAL` dentro de transacción.

## Estrategias de aislamiento de tenant (de barato a caro)

| Estrategia | Aislamiento | Costo | Cuándo |
|---|---|---|---|
| **Shared DB, columna `org_id` + RLS** | lógico | bajo | default; miles de tenants |
| **Schema por tenant** | medio | medio | decenas-cientos, compliance suave |
| **DB por tenant** | físico fuerte | alto | enterprise regulado, "tu data en tu DB" |

Cruza con [[338-multitenancy-patterns]] y [[63-multi-tenancy-billing-saas]].

## Motores de autorización (cuando RBAC en código ya no escala)
- **OpenFGA / SpiceDB** — open-source basados en **Google Zanzibar**; modelan ReBAC (tuples `user:ana#editor@doc:42`), check en <10ms. Self-host o cloud. Para grafos de sharing tipo Drive.
- **Cerbos** — policies en YAML, stateless, decide por RBAC+ABAC; corre como sidecar, no guarda datos (tú le pasas principal+resource+action). Más simple que Zanzibar, ideal si no necesitas grafo de relaciones.
- **Oso / Permit.io / Casbin** — alternativas; Casbin es librería embebida (sin servicio aparte).

Regla: no metas un motor Zanzibar si RBAC-en-código te sirve. Es infra extra (latencia, consistencia, "new enemy problem"). Adóptalo cuando los permisos sean un **grafo**, no una tabla.

## Gotchas
1. **Permisos en el JWT se quedan viejos** — revocar un rol no invalida tokens ya emitidos hasta que expiran. Para revocación inmediata: tokens cortos + refresh, o check server-side contra DB en acciones sensibles.
2. **El admin de un tenant NO es admin de la plataforma** — separa `org_role` (admin de SU org) de `platform_role` (tu staff). Confundirlos = escalada de privilegios.
3. **Enumeración de IDs** — IDs secuenciales + chequeo de permiso flojo = IDOR. Verifica ownership en CADA endpoint, no solo en la lista.
4. **Tests de aislamiento** — escribe tests que intenten leer data de otro tenant y DEBEN fallar. El aislamiento sin test se rompe en silencio.

Cruza con [[27-seguridad-apps-owasp]] (IDOR/BOLA), [[338-multitenancy-patterns]] y [[63-multi-tenancy-billing-saas]].

**Fuentes:** openfga.dev · authzed.com (SpiceDB) · cerbos.dev · postgresql.org/docs (RLS) · research.google/pubs/zanzibar.

# 351 · RPA e integraciones (conectar lo que no quiere conectarse)

> RPA es el último recurso: automatizas la UI porque **no hay API**. Frágil por diseño. La buena
> ingeniería de integración elige el método más estable disponible y baja a RPA solo cuando toca.

## La jerarquía de integración (de más a menos robusto)
| Nivel | Método | Robustez | Cuándo |
|---|---|---|---|
| 1 | **API oficial** (REST/GraphQL) | alta | el sistema la expone. Siempre primero. |
| 2 | **Webhook / eventos** | alta | el sistema te empuja cambios (push) |
| 3 | **DB / export / SFTP/CSV** | media | batch, data warehouse, legacy con dumps |
| 4 | **iPaaS** (n8n/Make/Zapier/MuleSoft) | media | pegar SaaS sin escribir conectores |
| 5 | **RPA** (UI automation) | **baja** | sistema legacy sin API ni DB accesible |

**Regla:** sube de nivel siempre que puedas. Cada peldaño hacia RPA multiplica la fragilidad: una API
cambia con versionado y deprecación avisada; una **UI cambia sin avisar** y rompe tu bot.

## RPA: cuándo y cómo no morir
RPA = un bot que **clickea y teclea** en la interfaz como un humano (ERP viejo, mainframe, app de
escritorio, portal sin API). Herramientas: UiPath, Power Automate Desktop, o **Playwright/Puppeteer**
para RPA web (ver [[350-browser-automation-playwright]]).
- **Selectores por atributo estable** (id, `data-*`, accessibility role), nunca por coordenadas de pantalla (se rompen al primer cambio de layout/resolución).
- **Espera explícita** a que el elemento exista/sea visible; nunca `sleep` fijo (el legacy es impredecible).
- **Idempotencia y checkpoints**: si el bot cae en el paso 7 de 10, debe reanudar sin duplicar (ver [[348-workflow-automation-patterns]]).
- **Pantalla de control**: corre en VM/contenedor con resolución fija; un cambio de DPI desalinea todo.
- **Monitoreo + alerta**: un RPA roto falla en silencio y "deja de procesar". Alarma ante caída de throughput.

## ETL de APIs (extraer-transformar-cargar entre sistemas)
- **Extract**: paginación por cursor, no por offset (offset se desincroniza si llegan filas nuevas). Guarda el cursor.
- **Incremental, no full**: `updated_since` / change data capture; re-bajar todo cada vez no escala.
- **Transform**: normaliza esquemas distintos a un modelo canónico; valida (pydantic/zod) antes de cargar.
- **Load**: **upsert** idempotente por clave natural; nunca insert ciego (duplica al reintentar).
- **Backfill vs incremental**: separa el job histórico (una vez, pesado) del delta continuo (ligero, frecuente).

## Sincronización entre sistemas
- **Una fuente de verdad por campo.** Sin eso, dos sistemas se sobrescriben en loop.
- **Resolución de conflictos**: last-write-wins (simple, pierde datos) vs merge por campo vs versionado. Decídela explícitamente.
- **Bidireccional = peligro**: A→B y B→A pueden hacer eco infinito. Marca el origen del cambio (`source: sync`) y **no re-propagues lo que tú mismo escribiste**.
- **Reconciliación**: job periódico que compara ambos lados y reporta drift; la sync en tiempo real siempre acumula desvíos.
- **Mapeo de IDs**: tabla de correspondencia `id_A ↔ id_B`; nunca asumas que los IDs coinciden entre sistemas.

## Legacy: tácticas
- Busca puertas traseras antes de RPA: API no documentada (mira el tráfico de su propia UI), endpoint SOAP, vista de DB de solo-lectura, export programado a SFTP.
- **Anti-corruption layer**: un adaptador tuyo traduce el modelo feo del legacy a tu modelo limpio. Aísla el resto del sistema de su rareza.
- Versiona los contratos: si el legacy responde XML inconsistente, valida y cuarentena lo malformado (DLQ), no lo metas al core.

## Gotchas
- RPA por coordenadas de pantalla → se rompe al primer rediseño o cambio de resolución.
- Sync bidireccional sin marca de origen → bucle de eco que se auto-dispara.
- ETL con offset en vez de cursor → filas saltadas o duplicadas al insertarse nuevas durante la corrida.
- Asumir IDs compartidos entre sistemas → datos cruzados al cliente equivocado.
- RPA sin monitoreo → falla callado y "deja de procesar" días sin que nadie lo note.

Cruza con [[347-n8n-make-zapier-deep]], [[348-workflow-automation-patterns]] y [[350-browser-automation-playwright]].

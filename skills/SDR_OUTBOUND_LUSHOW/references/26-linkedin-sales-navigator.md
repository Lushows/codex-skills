# 26 — LinkedIn Sales Navigator

Sales Navigator es la herramienta de búsqueda avanzada de LinkedIn (la versión de pago para vendedores). Es la **mejor fuente única** para construir listas B2B: filtras el universo profesional por sector, tamaño, cargo, geografía y **señales** (cambios de trabajo, contrataciones, crecimiento), y guardas listas de cuentas y de personas. Este módulo te enseña a exprimirlo: los filtros que importan, cómo escribir **búsquedas booleanas** (combinar palabras con AND/OR/NOT), y ejemplos reales listos para pegar. El uso experto (spotlights, listas grandes, exportar a escala) está en `102`.

## El principio: filtras funciones, no adivinas nombres

LinkedIn tiene el dato que la gente **mantiene actualizado por vanidad profesional**: su cargo y su empresa. Eso lo hace más fresco que muchas bases (`25`). Sales Nav te deja combinar decenas de filtros para aislar exactamente tu ICP (`10`) y tu decisor (`22`). Dos tipos de búsqueda:
- **Account search** (empresas): construye tu lista de cuentas (`21`).
- **Lead search** (personas): encuentra al decisor dentro de esas cuentas.

Planes 2026: **Core** (~US$99/mes) sirve para casi todo esto; **Advanced/Advanced Plus** agregan features de equipo/CRM. Empieza con Core.

## Los filtros que de verdad usas

**Para cuentas (Account filters):**
- *Industry* (sector), *Company headcount* (tamaño por empleados), *Company HQ location* (geografía).
- *Company headcount growth* y *Recent activities* → **Hired X in last 90 days**, **Senior leadership changes** → señales de compra (`14`, `135`).
- *Technologies used* (si el plan lo trae) → technographics (`134`).

**Para personas (Lead filters):**
- *Current company* (o cárgalo desde tu lista de cuentas), *Function*, *Seniority level*, *Job title* (con booleano), *Geography*, *Years in current position*.
- **Spotlights** — los más potentes: *Changed jobs in last 90 days* (`133`), *Posted on LinkedIn recently* (están activos, te leerán), *Mentioned in the news*.

Combinar **Function + Seniority** es más robusto que *Job title* solo, porque la gente escribe el título de mil maneras.

## Búsqueda booleana — la sintaxis

En el campo de *keywords* o *title* puedes usar operadores. Reglas:
- `AND` — deben estar ambos. `OR` — cualquiera. `NOT` — excluye.
- `"comillas"` — frase exacta (`"gerente de compras"`).
- `(paréntesis)` — agrupa. Escribe los operadores en MAYÚSCULA.

```
Cargos de compras/operaciones (ES + EN):
("gerente de compras" OR "jefe de compras" OR "director de operaciones"
 OR "purchasing manager" OR "procurement manager" OR "head of operations")
NOT ("asistente" OR "practicante" OR "intern")
```
El `NOT` quita juniors que no deciden. Úsalo siempre para limpiar seniority.

## Ejemplos reales de búsqueda (pégalos y adáptalos)

**Ejemplo 1 — Restaurantes medianos en Colombia, decisor de operaciones:**
```
ACCOUNT SEARCH:
  Industry = Restaurants / Food & Beverage Services
  Company HQ = Colombia
  Company headcount = 51–200, 201–500
  → Guardar como Account List "Restaurantes CO medianos"

LEAD SEARCH (sobre esa lista):
  Current company = [Account List anterior]
  Function = Operations OR Finance
  Seniority = Owner, Partner, CXO, Director, Manager
  Title booleano = ("operaciones" OR "compras" OR "costos" OR "gerente general")
  → Guardar como Lead List "Decisores restaurantes CO"
```

**Ejemplo 2 — SaaS que acaba de contratar (señal de crecimiento):**
```
ACCOUNT: Industry = Software Development; Headcount = 11–50;
         Recent activities = "Hired in last 90 days"; HQ = México
LEAD:    Function = Marketing; Seniority = Director OR VP OR CXO;
         Spotlight = "Posted on LinkedIn in past 30 days"
```

**Ejemplo 3 — Perseguir compradores que cambiaron de empresa (`133`):**
```
LEAD: Title = ("Head of Growth" OR "VP Marketing")
      Spotlight = "Changed jobs in the last 90 days"; Geography = LatAm
→ Contacto con timing perfecto: nuevo en el cargo, quiere marcar resultados.
```

## De la búsqueda a la lista usable

Sales Nav **no exporta a CSV de forma nativa**. Para pasar la lista a tu hoja y conseguir correos:
1. Guarda la búsqueda como **Lead List** en Sales Nav.
2. Extrae con una herramienta: **Apollo** (`25`) lee tu búsqueda de LinkedIn; o un scraper como **PhantomBuster / Evaboot / Clay** (ver `27`, `109`) extrae la lista a CSV con nombre, cargo, empresa y `linkedin_url`.
3. Consigue el correo de cada uno (`23`) y verifícalo (`28`).

Ojo: extraer a escala roza los términos de servicio de LinkedIn (`27`). Hazlo con volúmenes moderados y herramientas que simulan comportamiento humano para no arriesgar tu cuenta.

## Errores comunes (qué NO hacer)

- **Filtrar solo por *Job title*** exacto → pierdes medio mercado. Usa Function + Seniority + booleano.
- **Olvidar el `NOT`** de juniors/becarios → listas llenas de gente sin poder.
- **Ignorar los Spotlights de timing** (job change, posteó) → desperdicias la mejor señal (`14`).
- **Extraer 5.000/día con un scraper agresivo** → LinkedIn te restringe la cuenta. Modera (`27`).
- **Guardar la lista y nunca refrescarla** → los cargos cambian; reverifica (`139`).

## Frontera y siguiente paso

Sales Nav = encontrar y listar a la persona correcta (máquina). El **mensaje** de LinkedIn en frío → `57`; la **conversación de venta** cuando responde → `ventas_lushows`. Con tu Lead List guardada, pásala a CSV, consigue correos (`23`) y teléfonos/WA (`24`), verifica (`28`) y enriquece (`29`). Uso avanzado (spotlights combinados, límites, Evaboot) en `102`.

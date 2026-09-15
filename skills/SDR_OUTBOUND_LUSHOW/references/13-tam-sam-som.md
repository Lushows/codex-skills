# 13 — TAM, SAM, SOM (dimensionar el mercado alcanzable)

Antes de mandar un solo correo necesitas saber **cuántas cuentas existen** que encajan con tu ICP (`10`). Si son 50, el outbound puro se te acaba en un mes y necesitas otra estrategia; si son 50.000, el problema es priorizar, no encontrar. **TAM/SAM/SOM** es la forma estándar de dimensionar eso en tres capas, de lo grande a lo alcanzable. Para el SDR no es teoría de inversionista: es el número que te dice si tu meta de reuniones es posible con la lista que puedes construir.

## Las tres capas (en simple)

| Sigla | Qué es | Pregunta que responde |
|---|---|---|
| **TAM** — Total Addressable Market | Todo el mercado que en teoría podría usar tu producto | "¿Cuántas empresas como estas existen en total?" |
| **SAM** — Serviceable Available Market | La parte del TAM que **tú realmente puedes servir** (tu geografía, idioma, capacidad, ICP) | "¿A cuántas de esas les puedo vender de verdad hoy?" |
| **SOM** — Serviceable Obtainable Market | La parte del SAM que puedes **capturar en un periodo** (1–3 años), dada tu capacidad de outbound | "¿A cuántas puedo llegar y cerrar este año?" |

Analogía: **TAM** = todos los que comen pizza en la ciudad; **SAM** = los que están en tu zona de domicilio; **SOM** = los que realmente van a pedirte a ti este año.

Para outbound, la capa que más te importa a diario es el **SAM** (tu universo real de cuentas contactables) y el **SOM** (lo que puedes trabajar sin quemar el mercado). El TAM sirve para saber si el negocio escala (eso lo usa `economist_lushows`).

## Cómo calcularlo — dos métodos

**Método top-down (de arriba hacia abajo):** partes de una cifra grande (total de empresas del sector, de una fuente como cámaras de comercio, DANE/INEGI, informes) y le aplicas filtros de tu ICP hasta bajar al SAM.

**Método bottom-up (de abajo hacia arriba, más confiable para outbound):** **cuentas las cuentas reales** que aparecen cuando aplicas tus filtros en una herramienta de datos (Apollo, Sales Navigator, ver `25`, `26`). Este es el que te da un número accionable, porque es literalmente tu lista potencial.

Regla: para outbound, **confía en el bottom-up.** El número que sale de aplicar tus filtros en Apollo ES tu SAM real, porque es exactamente lo que podrás listar.

## Paso a paso (bottom-up, el que usa el SDR)

1. Escribe los filtros duros de tu ICP (sector + tamaño + geografía — ver `15`).
2. Aplícalos en tu fuente de datos (Apollo/Sales Nav) y **lee el conteo de resultados** = tu SAM aproximado de cuentas.
3. Multiplica por los contactos por cuenta que vas a atacar (2–4 del comité, ver `11`) = universo de contactos.
4. Define tu SOM: qué % de ese SAM puedes trabajar bien este año sin repetir cuentas quemadas (típico: puedes tocar 100% pero *cerrar* un dígito bajo %).
5. Contrasta contra tu meta (ver `17`): ¿alcanza el universo para las reuniones que necesitas?

## Ejemplo de cálculo (LatAm)

```
Producto: software de costos para restaurantes. Meta: cerrar clientes en Colombia.

TOP-DOWN (contexto):
  Establecimientos gastronómicos formales en Colombia ≈ 90.000 (fuente sectorial)
  → TAM amplio.

BOTTOM-UP (lo accionable) — filtros ICP en Apollo/Sales Nav:
  Sector: restaurantes/food service
  País: Colombia
  Empleados: 5–40
  Ciudades: Bogotá + Medellín + Cali
  → Resultado del filtro: ~15.000 empresas   ← SAM (universo contactable)

  Contactos por cuenta (dueño + admin): 2
  → ~30.000 contactos potenciales

SOM (este año):
  Puedo trabajar bien ~6.000 cuentas/año con mi capacidad de envío
  (ver 44 límites y 17 tamaño de lista).
  → SOM = 6.000 cuentas contactadas este año.
```

⚠️ Los números de fuentes (el 90.000) y las multiplicaciones deben ser **exactos**: para cualquier cálculo que sostenga una decisión de plata, ejecútalo y verifícalo con **`Matematicas_lushows`**. Aquí damos el método y la estructura; el número final se calcula, no se estima de memoria.

## Qué te dice el número (interpretación)

- **SAM chico (< ~300 cuentas):** el outbound masivo no te va a durar. Ve a **ABM** (pocas cuentas, muy personalizado — ver `94`, `160`) o combina con inbound/ads. Con 300 cuentas quemas el mercado en semanas.
- **SAM mediano (cientos a pocos miles):** outbound clásico funciona; prioriza en tiers (`16`) y cuida no quemar cuentas (una cuenta contactada mal no se recupera fácil).
- **SAM grande (decenas de miles+):** el cuello de botella es tu capacidad de envío y calificación, no la lista. Prioriza duro (`16`) y no confundas "mucha lista" con "buena lista".

## Errores comunes

- **Enamorarte del TAM** ("¡el mercado vale millones!") e ignorar que tu SAM real son 400 cuentas.
- **Estimar el SAM de memoria** en vez de contarlo con filtros reales en una herramienta.
- **Olvidar que el mercado se quema:** cada cuenta se contacta una vez bien; si tu SOM > tu SAM, te repites y molestas.
- **No restar exclusiones** del ICP (`10`) al contar.

## Frontera y siguiente paso

El **dimensionamiento estratégico del mercado para el negocio** (TAM para decidir si vale montar la empresa, proyección de ingresos, orden de mercados) lo hace **`economist_lushows`**. Aquí lo usamos para saber si el outbound es viable y cuánta lista hay. Cualquier **cálculo exacto** → **`Matematicas_lushows`**.

**Siguiente paso:** corre tus filtros de ICP en Apollo/Sales Nav y anota el conteo = tu SAM. Llévalo a `17` para ver si alcanza tu meta de reuniones, y a `16` para priorizarlo en tiers.
